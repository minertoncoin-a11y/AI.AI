"""src/i18n.py — Sodda tarjima tizimi"""

_STORE: dict[int, str] = {}

_TEXTS: dict[str, dict[str, str]] = {
    "welcome": {
        "uz": "👋 Salom! O'rganishni boshlaymizmi?",
        "ru": "👋 Привет! Начнём обучение?",
        "en": "👋 Hello! Ready to learn?",
    },
    "error": {
        "uz": "❌ Xato yuz berdi. /start bosing.",
        "ru": "❌ Произошла ошибка. Нажмите /start.",
        "en": "❌ An error occurred. Press /start.",
    },
    "reminder": {
        "uz": "🔔 Bugun o'rganish vaqti! Bir dars ham bo'lsa yetarli. /start",
        "ru": "🔔 Время учиться! Один урок уже прогресс. /start",
        "en": "🔔 Time to learn! Even one lesson counts. /start",
    },
    "ai_no_key": {
        "uz": "⚠️ AI hozircha yoqilmagan. OPENAI_API_KEY .env ga qo'shing.",
        "ru": "⚠️ ИИ пока недоступен. Добавьте OPENAI_API_KEY в .env.",
        "en": "⚠️ AI not enabled. Add OPENAI_API_KEY to .env.",
    },
}


def set_lang(uid: int, lang: str) -> None:
    _STORE[uid] = lang


def get_lang(uid: int) -> str:
    return _STORE.get(uid, "uz")


def tr(key: str, lang: str = "uz", **kw) -> str:
    bundle = _TEXTS.get(key, {})
    text   = bundle.get(lang) or bundle.get("uz") or key
    if kw:
        try:
            text = text.format(**kw)
        except KeyError:
            pass
    return text
