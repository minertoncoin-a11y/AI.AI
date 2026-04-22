"""src/database.py — SQLite database (to'liq versiya)"""
import sqlite3, json, datetime, os, threading
from typing import Optional
from src.logger import log
from src.config import cfg


class BotDatabase:
    def __init__(self, path: str):
        self.path  = path
        self._lock = threading.Lock()
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        # Doimiy ulanish — har so'rovda yangi connect() emas
        self._db = sqlite3.connect(self.path, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._db.execute("PRAGMA journal_mode=WAL")
        self._db.execute("PRAGMA foreign_keys=ON")
        self._db.execute("PRAGMA synchronous=NORMAL")
        self._db.execute("PRAGMA cache_size=-8000")   # 8MB kesh
        self._init()

    def _conn(self):
        """Mavjud ulanishni qaytaradi (context manager sifatida ishlaydi)."""
        return self._db

    def _init(self):
        with self._lock, self._conn() as c:
            c.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                user_id    INTEGER PRIMARY KEY,
                username   TEXT,
                first_name TEXT,
                last_name  TEXT,
                lang       TEXT    DEFAULT 'uz',
                xp         INTEGER DEFAULT 0,
                streak_days INTEGER DEFAULT 0,
                last_lesson_date TEXT,
                last_active TEXT,
                reminder_on  INTEGER DEFAULT 0,
                total_done   INTEGER DEFAULT 0,
                total_quizzes INTEGER DEFAULT 0,
                has_perfect  INTEGER DEFAULT 0,
                total_ai_requests INTEGER DEFAULT 0,
                streak_freeze    INTEGER DEFAULT 0,
                coins            INTEGER DEFAULT 0,
                created_at   TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS daily_challenges (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id    INTEGER REFERENCES users(user_id),
                date       TEXT,
                topic      TEXT,
                lesson_idx INTEGER,
                completed  INTEGER DEFAULT 0,
                UNIQUE(user_id, date)
            );

            CREATE TABLE IF NOT EXISTS notes (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id    INTEGER REFERENCES users(user_id),
                topic      TEXT,
                lesson_idx INTEGER,
                note_text  TEXT,
                created_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS lesson_progress (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id    INTEGER REFERENCES users(user_id),
                topic      TEXT,
                lesson_idx INTEGER,
                completed  INTEGER DEFAULT 0,
                score      INTEGER DEFAULT 100,
                saved_at   TEXT DEFAULT (datetime('now')),
                UNIQUE(user_id, topic, lesson_idx)
            );

            CREATE TABLE IF NOT EXISTS quiz_results (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id  INTEGER REFERENCES users(user_id),
                topic    TEXT,
                score    INTEGER,
                total    INTEGER,
                pct      INTEGER,
                secs     INTEGER DEFAULT 0,
                taken_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS achievements (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id   INTEGER REFERENCES users(user_id),
                badge_id  TEXT,
                given_at  TEXT DEFAULT (datetime('now')),
                UNIQUE(user_id, badge_id)
            );

            CREATE TABLE IF NOT EXISTS bookmarks (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id    INTEGER REFERENCES users(user_id),
                topic      TEXT,
                lesson_idx INTEGER,
                saved_at   TEXT DEFAULT (datetime('now')),
                UNIQUE(user_id, topic, lesson_idx)
            );

            CREATE TABLE IF NOT EXISTS user_settings (
                user_id       INTEGER PRIMARY KEY REFERENCES users(user_id),
                lang          TEXT DEFAULT 'uz',
                reminder_on   INTEGER DEFAULT 0,
                daily_goal    INTEGER DEFAULT 1,
                reminder_time TEXT DEFAULT '09:00'
            );

            CREATE TABLE IF NOT EXISTS linked_auth (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id      INTEGER REFERENCES users(user_id),
                provider     TEXT,
                provider_uid TEXT,
                email        TEXT,
                display_name TEXT,
                extra_json   TEXT,
                linked_at    TEXT DEFAULT (datetime('now')),
                UNIQUE(user_id, provider)
            );

            CREATE INDEX IF NOT EXISTS idx_lp_user  ON lesson_progress(user_id);
            CREATE INDEX IF NOT EXISTS idx_lp_topic ON lesson_progress(topic);
            CREATE INDEX IF NOT EXISTS idx_quiz_user ON quiz_results(user_id);
            CREATE INDEX IF NOT EXISTS idx_ach_user  ON achievements(user_id);
            """)
        # Migrate existing DB safely
        try:
            with self._lock, self._conn() as c:
                for col, dtype in [
                    ("total_ai_requests", "INTEGER DEFAULT 0"),
                    ("streak_freeze", "INTEGER DEFAULT 0"),
                    ("coins", "INTEGER DEFAULT 0"),
                ]:
                    try:
                        c.execute(f"ALTER TABLE users ADD COLUMN {col} {dtype}")
                    except Exception:
                        pass
        except Exception:
            pass
        log.info("DB tayyor: %s", self.path)

    # ── Users ────────────────────────────────────────────────

    def user_exists(self, uid: int) -> bool:
        with self._lock, self._conn() as c:
            r = c.execute("SELECT 1 FROM users WHERE user_id=?", (uid,)).fetchone()
            return r is not None

    def add_user(self, uid: int, username=None, first_name=None, last_name=None):
        with self._lock, self._conn() as c:
            c.execute(
                """INSERT OR IGNORE INTO users (user_id,username,first_name,last_name,last_active)
                   VALUES (?,?,?,?,datetime('now'))""",
                (uid, username, first_name, last_name),
            )
            c.execute(
                "INSERT OR IGNORE INTO user_settings (user_id) VALUES (?)", (uid,)
            )

    def get_stats(self, uid: int) -> dict:
        with self._lock, self._conn() as c:
            r = c.execute("SELECT * FROM users WHERE user_id=?", (uid,)).fetchone()
            return dict(r) if r else {}

    def add_xp(self, uid: int, amount: int):
        with self._lock, self._conn() as c:
            c.execute("UPDATE users SET xp=xp+?, last_active=datetime('now') WHERE user_id=?",
                      (amount, uid))

    def update_streak(self, uid: int):
        today    = datetime.date.today().isoformat()
        yest     = (datetime.date.today() - datetime.timedelta(1)).isoformat()
        two_days = (datetime.date.today() - datetime.timedelta(2)).isoformat()
        with self._lock, self._conn() as c:
            r = c.execute(
                "SELECT last_lesson_date, streak_days, COALESCE(streak_freeze,0) as streak_freeze FROM users WHERE user_id=?",
                (uid,)).fetchone()
            if not r: return
            last   = r["last_lesson_date"]
            streak = r["streak_days"] or 0
            freeze = r["streak_freeze"] or 0
            if last == today: return
            if last == yest:
                new_streak = streak + 1
            elif last == two_days and freeze > 0:
                c.execute("UPDATE users SET streak_freeze=streak_freeze-1 WHERE user_id=?", (uid,))
                new_streak = streak + 1
            else:
                new_streak = 1
            xp_bonus   = cfg.XP_STREAK if new_streak % 7 == 0 else 0
            c.execute(
                "UPDATE users SET last_lesson_date=?, streak_days=?, xp=xp+?, last_active=datetime('now') WHERE user_id=?",
                (today, new_streak, xp_bonus, uid)
            )

    def get_lang(self, uid: int) -> Optional[str]:
        with self._lock, self._conn() as c:
            r = c.execute("SELECT lang FROM users WHERE user_id=?", (uid,)).fetchone()
            return r["lang"] if r else None

    def set_lang(self, uid: int, lang: str):
        with self._lock, self._conn() as c:
            c.execute("UPDATE users SET lang=? WHERE user_id=?", (lang, uid))
            c.execute("UPDATE user_settings SET lang=? WHERE user_id=?", (lang, uid))

    def set_reminder(self, uid: int, on: bool):
        with self._lock, self._conn() as c:
            c.execute("UPDATE users SET reminder_on=? WHERE user_id=?", (1 if on else 0, uid))

    def get_reminder_users(self) -> list:
        with self._lock, self._conn() as c:
            rows = c.execute(
                "SELECT user_id, lang FROM users WHERE reminder_on=1"
            ).fetchall()
            return [dict(r) for r in rows]

    # ── Progress ─────────────────────────────────────────────

    def save_progress(self, uid: int, topic: str, lesson_idx: int):
        with self._lock, self._conn() as c:
            # Yangi bo'lsa qo'shish
            existing = c.execute(
                "SELECT completed FROM lesson_progress WHERE user_id=? AND topic=? AND lesson_idx=?",
                (uid, topic, lesson_idx)
            ).fetchone()
            c.execute(
                """INSERT INTO lesson_progress (user_id, topic, lesson_idx, completed, saved_at)
                   VALUES (?,?,?,1,datetime('now'))
                   ON CONFLICT(user_id,topic,lesson_idx) DO UPDATE SET
                   completed=1, saved_at=datetime('now')""",
                (uid, topic, lesson_idx)
            )
            if not existing or not existing["completed"]:
                c.execute(
                    "UPDATE users SET total_done=total_done+1, xp=xp+?, last_active=datetime('now') WHERE user_id=?",
                    (cfg.XP_LESSON, uid)
                )

    def get_progress(self, uid: int, topic: str) -> dict:
        with self._lock, self._conn() as c:
            rows = c.execute(
                "SELECT lesson_idx, completed, score FROM lesson_progress WHERE user_id=? AND topic=?",
                (uid, topic)
            ).fetchall()
            return {r["lesson_idx"]: {"completed": bool(r["completed"]), "score": r["score"]}
                    for r in rows}

    # ── Quiz ─────────────────────────────────────────────────

    def save_quiz(self, uid: int, topic: str, score: int, total: int, secs: int):
        pct = int(score / total * 100) if total else 0
        with self._lock, self._conn() as c:
            c.execute(
                "INSERT INTO quiz_results (user_id,topic,score,total,pct,secs) VALUES (?,?,?,?,?,?)",
                (uid, topic, score, total, pct, secs)
            )
            c.execute("UPDATE users SET total_quizzes=total_quizzes+1 WHERE user_id=?", (uid,))
            if pct == 100:
                c.execute("UPDATE users SET has_perfect=1 WHERE user_id=?", (uid,))

    # ── Achievements ─────────────────────────────────────────

    def get_achievements(self, uid: int) -> list:
        with self._lock, self._conn() as c:
            rows = c.execute(
                "SELECT badge_id, given_at FROM achievements WHERE user_id=?", (uid,)
            ).fetchall()
            return [dict(r) for r in rows]

    def award(self, uid: int, badge_id: str):
        try:
            with self._lock, self._conn() as c:
                c.execute(
                    "INSERT OR IGNORE INTO achievements (user_id, badge_id) VALUES (?,?)",
                    (uid, badge_id)
                )
        except Exception as e:
            log.warning("Award xato: %s", e)

    # ── Bookmarks ────────────────────────────────────────────

    def add_bookmark(self, uid: int, topic: str, lesson_idx: int):
        with self._lock, self._conn() as c:
            c.execute(
                "INSERT OR IGNORE INTO bookmarks (user_id,topic,lesson_idx) VALUES (?,?,?)",
                (uid, topic, lesson_idx)
            )

    def get_bookmarks(self, uid: int) -> list:
        with self._lock, self._conn() as c:
            rows = c.execute(
                "SELECT topic, lesson_idx FROM bookmarks WHERE user_id=? ORDER BY saved_at DESC",
                (uid,)
            ).fetchall()
            return [dict(r) for r in rows]

    # ── Leaderboard ──────────────────────────────────────────

    def get_leaderboard(self, limit: int = 10) -> list:
        with self._lock, self._conn() as c:
            rows = c.execute(
                """SELECT user_id, username, first_name, xp, total_done
                   FROM users ORDER BY xp DESC, total_done DESC LIMIT ?""",
                (limit,)
            ).fetchall()
            return [dict(r) for r in rows]

    def get_rank(self, uid: int) -> dict:
        with self._lock, self._conn() as c:
            r = c.execute(
                "SELECT COUNT(*)+1 AS rank FROM users WHERE xp>(SELECT xp FROM users WHERE user_id=?)",
                (uid,)
            ).fetchone()
            s = c.execute("SELECT xp, total_done FROM users WHERE user_id=?", (uid,)).fetchone()
            if not r or not s: return {}
            return {"rank": r["rank"], "xp": s["xp"], "total_done": s["total_done"]}

    # ── Global stats ─────────────────────────────────────────

    def global_stats(self) -> dict:
        today = datetime.date.today().isoformat()
        with self._lock, self._conn() as c:
            tu   = c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
            au   = c.execute(
                "SELECT COUNT(*) FROM users WHERE last_active LIKE ?", (f"{today}%",)
            ).fetchone()[0]
            tl   = c.execute("SELECT COALESCE(SUM(total_done),0) FROM users").fetchone()[0]
            tq   = c.execute("SELECT COUNT(*) FROM quiz_results").fetchone()[0]
            txp  = c.execute("SELECT COALESCE(SUM(xp),0) FROM users").fetchone()[0]
            return {"users": tu, "active_today": au,
                    "lessons": tl, "quizzes": tq, "xp": txp}

    def recent_users(self, limit: int = 10) -> list:
        with self._lock, self._conn() as c:
            rows = c.execute(
                """SELECT user_id, username, first_name, xp, total_done, last_active
                   FROM users ORDER BY created_at DESC LIMIT ?""", (limit,)
            ).fetchall()
            return [dict(r) for r in rows]

    # ── AI tracking
    def inc_ai_requests(self, uid: int):
        with self._lock, self._conn() as c:
            c.execute("UPDATE users SET total_ai_requests=COALESCE(total_ai_requests,0)+1 WHERE user_id=?", (uid,))

    # ── Coins
    def get_coins(self, uid: int) -> int:
        with self._lock, self._conn() as c:
            r = c.execute("SELECT COALESCE(coins,0) as coins FROM users WHERE user_id=?", (uid,)).fetchone()
            return r["coins"] if r else 0

    def add_coins(self, uid: int, amount: int):
        with self._lock, self._conn() as c:
            c.execute("UPDATE users SET coins=COALESCE(coins,0)+? WHERE user_id=?", (amount, uid))

    def spend_coins(self, uid: int, amount: int) -> bool:
        with self._lock, self._conn() as c:
            r = c.execute("SELECT COALESCE(coins,0) as coins FROM users WHERE user_id=?", (uid,)).fetchone()
            if not r or r["coins"] < amount:
                return False
            c.execute("UPDATE users SET coins=coins-? WHERE user_id=?", (amount, uid))
            return True

    def add_streak_freeze(self, uid: int, count: int = 1):
        with self._lock, self._conn() as c:
            c.execute("UPDATE users SET streak_freeze=COALESCE(streak_freeze,0)+? WHERE user_id=?", (count, uid))

    # ── Daily challenge
    def get_daily_challenge(self, uid: int) -> dict:
        today = datetime.date.today().isoformat()
        with self._lock, self._conn() as c:
            r = c.execute("SELECT * FROM daily_challenges WHERE user_id=? AND date=?", (uid, today)).fetchone()
            return dict(r) if r else {}

    def set_daily_challenge(self, uid: int, topic: str, lesson_idx: int):
        today = datetime.date.today().isoformat()
        with self._lock, self._conn() as c:
            c.execute(
                "INSERT OR REPLACE INTO daily_challenges (user_id, date, topic, lesson_idx) VALUES (?,?,?,?)",
                (uid, today, topic, lesson_idx)
            )

    def complete_daily_challenge(self, uid: int) -> bool:
        today = datetime.date.today().isoformat()
        with self._lock, self._conn() as c:
            r = c.execute("SELECT id, completed FROM daily_challenges WHERE user_id=? AND date=?", (uid, today)).fetchone()
            if r and not r["completed"]:
                c.execute("UPDATE daily_challenges SET completed=1 WHERE id=?", (r["id"],))
                return True
            return False

    # ── Notes
    def add_note(self, uid: int, topic: str, lesson_idx: int, text: str):
        with self._lock, self._conn() as c:
            c.execute(
                "INSERT INTO notes (user_id, topic, lesson_idx, note_text) VALUES (?,?,?,?)",
                (uid, topic, lesson_idx, text[:500])
            )

    def get_notes(self, uid: int, topic: str = None) -> list:
        with self._lock, self._conn() as c:
            if topic:
                rows = c.execute(
                    "SELECT * FROM notes WHERE user_id=? AND topic=? ORDER BY created_at DESC", (uid, topic)
                ).fetchall()
            else:
                rows = c.execute(
                    "SELECT * FROM notes WHERE user_id=? ORDER BY created_at DESC LIMIT 20", (uid,)
                ).fetchall()
            return [dict(r) for r in rows]

    def delete_note(self, uid: int, note_id: int):
        with self._lock, self._conn() as c:
            c.execute("DELETE FROM notes WHERE id=? AND user_id=?", (note_id, uid))

    # ── Social auth ──────────────────────────────────────────

    def link_social(self, uid, provider, provider_uid, email=None, display_name=None, extra=None):
        with self._lock, self._conn() as c:
            c.execute(
                """INSERT INTO linked_auth (user_id,provider,provider_uid,email,display_name,extra_json)
                   VALUES (?,?,?,?,?,?)
                   ON CONFLICT(user_id,provider) DO UPDATE SET
                   provider_uid=excluded.provider_uid, email=excluded.email,
                   display_name=excluded.display_name, extra_json=excluded.extra_json,
                   linked_at=datetime('now')""",
                (uid, provider, provider_uid, email, display_name, json.dumps(extra or {}))
            )

    def get_linked(self, uid: int) -> list:
        with self._lock, self._conn() as c:
            rows = c.execute(
                "SELECT provider,provider_uid,email,display_name,linked_at FROM linked_auth WHERE user_id=?",
                (uid,)
            ).fetchall()
            return [dict(r) for r in rows]

    def unlink(self, uid: int, provider: str) -> bool:
        with self._lock, self._conn() as c:
            cur = c.execute(
                "DELETE FROM linked_auth WHERE user_id=? AND provider=?", (uid, provider)
            )
            return cur.rowcount > 0
