"""src/reminders.py — Kundalik eslatmalar"""
import datetime
from telegram.ext import Application
from src.logger import log
from src.config import cfg


async def _daily_reminder(context):
    bot = context.bot
    db  = context.job.data["db"]
    try:
        users = db.get_reminder_users()
        sent = fail = 0
        msgs = {
            "uz": "🔔 Bugun o'rganish vaqti! Hatto bir dars ham katta qadam. /start",
            "ru": "🔔 Время учиться! Даже один урок — это прогресс. /start",
            "en": "🔔 Time to learn! Even one lesson is great progress. /start",
        }
        for u in users:
            try:
                lang = u.get("lang", "uz")
                await bot.send_message(u["user_id"], msgs.get(lang, msgs["uz"]))
                sent += 1
            except Exception as e:
                fail += 1
                log.debug("Eslatma yuborilmadi uid=%s: %s", u["user_id"], e)
        log.info("Kundalik eslatmalar: %d yuborildi, %d muvaffaqiyatsiz", sent, fail)
    except Exception as e:
        log.error("Eslatma job xato: %s", e)


def setup_reminders(app: Application, db) -> None:
    jq = app.job_queue
    if jq is None:
        log.warning("JobQueue yo'q — eslatmalar o'rnatilmadi.")
        return
    tz     = datetime.timezone(datetime.timedelta(hours=5))   # UTC+5
    target = datetime.time(cfg.REMINDER_HOUR, cfg.REMINDER_MINUTE, tzinfo=tz)
    jq.run_daily(_daily_reminder, time=target, data={"db": db}, name="daily_reminder")
    log.info("Kundalik eslatma: %02d:%02d (UTC+5)", cfg.REMINDER_HOUR, cfg.REMINDER_MINUTE)
