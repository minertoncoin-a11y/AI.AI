"""src/achievements.py — Badge tizimi v9.0 ULTIMATE (35+ badge)"""
from src.logger import log

BADGES = [
    # Dars
    {"id": "first_lesson",   "name": "Birinchi qadam",     "icon": "🌱",  "description": "Birinchi darsni yakunla"},
    {"id": "lessons_5",      "name": "5 dars!",            "icon": "⭐",  "description": "5 ta dars yakunla"},
    {"id": "lessons_10",     "name": "O'nlab o'quvchi",    "icon": "📚",  "description": "10 ta dars yakunla"},
    {"id": "lessons_25",     "name": "Yigirma besh!",      "icon": "🌟",  "description": "25 ta dars yakunla"},
    {"id": "lessons_50",     "name": "Ellik dars!",        "icon": "🎯",  "description": "50 ta dars yakunla"},
    {"id": "lessons_100",    "name": "Yuz dars!",          "icon": "💯",  "description": "100 ta dars yakunla"},
    {"id": "lessons_200",    "name": "Ikki yuz!",          "icon": "🚀",  "description": "200 ta dars yakunla"},
    {"id": "lessons_300",    "name": "300 Dars USTASI",    "icon": "⚡",  "description": "300 ta dars yakunla"},
    {"id": "lessons_500",    "name": "500 Dars LEGENDA",   "icon": "👑",  "description": "500 ta dars yakunla"},
    {"id": "lessons_1000",   "name": "MING DARS XUDO",     "icon": "🔱",  "description": "1000 ta dars yakunla"},
    # Streak
    {"id": "streak_3",       "name": "3 kunlik streak",    "icon": "🔥",  "description": "3 kun ketma-ket o'qi"},
    {"id": "streak_7",       "name": "Haftalik streak",    "icon": "⚡",  "description": "7 kun ketma-ket o'qi"},
    {"id": "streak_14",      "name": "2 haftalik streak",  "icon": "💫",  "description": "14 kun ketma-ket o'qi"},
    {"id": "streak_30",      "name": "Oylik streak",       "icon": "🌟",  "description": "30 kun ketma-ket o'qi"},
    {"id": "streak_100",     "name": "100 kun TITAN",      "icon": "🏆",  "description": "100 kun ketma-ket o'qi"},
    # XP
    {"id": "xp_50",          "name": "XP Boshlovchi",      "icon": "⚡",  "description": "50 XP yig'"},
    {"id": "xp_100",         "name": "XP Yig'uvchi",       "icon": "💫",  "description": "100 XP yig'"},
    {"id": "xp_500",         "name": "XP Master",          "icon": "💎",  "description": "500 XP yig'"},
    {"id": "xp_1000",        "name": "XP Legend",          "icon": "🏆",  "description": "1000 XP yig'"},
    {"id": "xp_3000",        "name": "XP GOD",             "icon": "👑",  "description": "3000 XP yig'"},
    # Quiz
    {"id": "quiz_first",     "name": "Birinchi quiz",      "icon": "🎮",  "description": "Birinchi quizni yakunla"},
    {"id": "quiz_perfect",   "name": "Mukammal quiz",      "icon": "✨",  "description": "Quizda 100% natija"},
    {"id": "quiz_5",         "name": "Quiz faoli",         "icon": "🎯",  "description": "5 ta quiz yakunla"},
    {"id": "quiz_10",        "name": "Quiz chempion",      "icon": "🥇",  "description": "10 ta quiz yakunla"},
    {"id": "quiz_25",        "name": "Quiz grandmaster",   "icon": "🏆",  "description": "25 ta quiz yakunla"},
    # Mavzu
    {"id": "topic_asoslar",  "name": "Linux Asoslari",     "icon": "🐧",  "description": "Asoslar kursini yakunla"},
    {"id": "topic_docker",   "name": "Docker Usta",        "icon": "🐳",  "description": "Docker Mastery yakunla"},
    {"id": "topic_python",   "name": "Python PRO",         "icon": "🐍",  "description": "Python PRO kursini yakunla"},
    {"id": "multi_topic_3",  "name": "Ko'p mavzu (3)",     "icon": "📖",  "description": "3 ta mavzuni yakunla"},
    {"id": "multi_topic_5",  "name": "Ko'p mavzu (5)",     "icon": "📚",  "description": "5 ta mavzuni yakunla"},
    {"id": "multi_topic_10", "name": "Ko'p mavzu (10)",    "icon": "🎓",  "description": "10 ta mavzuni yakunla"},
    # Maxsus
    {"id": "early_bird",     "name": "Early Bird",         "icon": "🌅",  "description": "Ertalab 06-09 o'rtasida o'qi"},
    {"id": "night_owl",      "name": "Night Owl",          "icon": "🦉",  "description": "Tunda 23:00-03:00 o'rtasida o'qi"},
    {"id": "weekend_warrior","name": "Weekend Warrior",    "icon": "⚔️",  "description": "Dam olish kunida o'qi"},
    {"id": "bookmarker",     "name": "Bookmark Collector", "icon": "🔖",  "description": "10 ta darsni bookmark qil"},
    {"id": "ai_user",        "name": "AI Foydalanuvchi",   "icon": "🤖",  "description": "AI'dan 5 marta foydalaning"},
]


class AchievementSystem:
    def __init__(self, db):
        self._db = db

    def all_badges(self) -> list:
        return BADGES

    def check(self, uid: int, topic: str, lesson_idx: int) -> list:
        try:
            import datetime
            earned = {e["badge_id"] for e in self._db.get_achievements(uid)}
            stats  = self._db.get_stats(uid) or {}
            new    = []
            now_h  = datetime.datetime.now().hour
            now_wd = datetime.datetime.now().weekday()

            ctx = {
                "total_done":    stats.get("total_done", 0),
                "streak":        stats.get("streak_days", 0),
                "xp":            stats.get("xp", 0),
                "total_quizzes": stats.get("total_quizzes", 0),
                "has_perfect":   bool(stats.get("has_perfect", 0)),
                "topic_done":    self._topic_done(uid, topic),
                "multi_topics":  self._count_done_topics(uid),
                "bookmarks":     len(self._db.get_bookmarks(uid)),
                "is_morning":    6 <= now_h < 9,
                "is_night":      now_h >= 23 or now_h < 3,
                "is_weekend":    now_wd >= 5,
            }

            rules = {
                "first_lesson":   ctx["total_done"] >= 1,
                "lessons_5":      ctx["total_done"] >= 5,
                "lessons_10":     ctx["total_done"] >= 10,
                "lessons_25":     ctx["total_done"] >= 25,
                "lessons_50":     ctx["total_done"] >= 50,
                "lessons_100":    ctx["total_done"] >= 100,
                "lessons_200":    ctx["total_done"] >= 200,
                "lessons_300":    ctx["total_done"] >= 300,
                "lessons_500":    ctx["total_done"] >= 500,
                "lessons_1000":   ctx["total_done"] >= 1000,
                "streak_3":       ctx["streak"] >= 3,
                "streak_7":       ctx["streak"] >= 7,
                "streak_14":      ctx["streak"] >= 14,
                "streak_30":      ctx["streak"] >= 30,
                "streak_100":     ctx["streak"] >= 100,
                "xp_50":          ctx["xp"] >= 50,
                "xp_100":         ctx["xp"] >= 100,
                "xp_500":         ctx["xp"] >= 500,
                "xp_1000":        ctx["xp"] >= 1000,
                "xp_3000":        ctx["xp"] >= 3000,
                "quiz_first":     ctx["total_quizzes"] >= 1,
                "quiz_perfect":   ctx["has_perfect"],
                "quiz_5":         ctx["total_quizzes"] >= 5,
                "quiz_10":        ctx["total_quizzes"] >= 10,
                "quiz_25":        ctx["total_quizzes"] >= 25,
                "topic_asoslar":  topic == "asoslar" and ctx["topic_done"],
                "topic_docker":   topic == "docker_mastery" and ctx["topic_done"],
                "topic_python":   topic == "python_pro" and ctx["topic_done"],
                "multi_topic_3":  ctx["multi_topics"] >= 3,
                "multi_topic_5":  ctx["multi_topics"] >= 5,
                "multi_topic_10": ctx["multi_topics"] >= 10,
                "early_bird":     ctx["is_morning"],
                "night_owl":      ctx["is_night"],
                "weekend_warrior":ctx["is_weekend"],
                "bookmarker":     ctx["bookmarks"] >= 10,
            }

            for badge in BADGES:
                bid = badge["id"]
                if bid not in earned and rules.get(bid, False):
                    self._db.award(uid, bid)
                    new.append(badge)
            return new
        except Exception as e:
            log.error("Achievement check xato: %s", e)
            return []

    def check_ai_usage(self, uid: int) -> list:
        try:
            earned = {e["badge_id"] for e in self._db.get_achievements(uid)}
            stats  = self._db.get_stats(uid) or {}
            new = []
            if "ai_user" not in earned and stats.get("total_ai_requests", 0) >= 5:
                self._db.award(uid, "ai_user")
                for b in BADGES:
                    if b["id"] == "ai_user":
                        new.append(b); break
            return new
        except Exception:
            return []

    def _topic_done(self, uid: int, topic: str) -> bool:
        try:
            from src.lessons import LESSONS
            if topic not in LESSONS: return False
            prog  = self._db.get_progress(uid, topic)
            total = len(LESSONS[topic]["lessons"])
            done  = sum(1 for p in prog.values() if p.get("completed"))
            return done >= total > 0
        except Exception:
            return False

    def _count_done_topics(self, uid: int) -> int:
        try:
            from src.lessons import LESSONS
            return sum(1 for t in LESSONS if self._topic_done(uid, t))
        except Exception:
            return 0
