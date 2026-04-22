"""src/config.py — Konfiguratsiya (v7)"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class _Cfg:
    # ── Asosiy token — FAQAT .env dan o'qiladi ─────────────
    BOT_TOKEN    : str  = os.getenv("BOT_TOKEN", "")
    OPENAI_KEY   : str  = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL : str  = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    LOG_LEVEL    : str  = os.getenv("LOG_LEVEL", "INFO")
    DEBUG        : bool = os.getenv("DEBUG", "False").lower() == "true"

    # ── Yo'llar ─────────────────────────────────────────────
    ROOT    = Path(__file__).parent.parent
    DB_PATH : str = str(ROOT / "bot_data.db")

    # ── XP tizimi ───────────────────────────────────────────
    XP_LESSON : int = 5
    XP_QUIZ   : int = 10
    XP_STREAK : int = 20

    # ── Admin IDlari ─────────────────────────────────────────
    ADMIN_IDS : list = [
        int(x) for x in os.getenv("ADMIN_IDS", "").split(",")
        if x.strip().isdigit()
    ]

    # ── Eslatma (UTC+5) ──────────────────────────────────────
    REMINDER_HOUR   : int = 9
    REMINDER_MINUTE : int = 0

    # ── Sahifalash ───────────────────────────────────────────
    TOPICS_PER_PAGE : int = 8

    # ── Rate limiting (soniyada 1 so'rov) ───────────────────
    RATE_LIMIT_SECONDS : int = 2

    # ── AI kunlik limit ──────────────────────────────────────
    AI_DAILY_LIMIT : int = int(os.getenv("AI_DAILY_LIMIT", "30"))

    # ── Qidiruv natijasi maksimum ────────────────────────────
    SEARCH_MAX_RESULTS : int = 5


cfg = _Cfg()
