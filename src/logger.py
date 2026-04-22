"""src/logger.py"""
import logging, sys, os

def _setup():
    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    handlers = [logging.StreamHandler(sys.stdout)]
    try:
        handlers.append(logging.FileHandler("bot.log", encoding="utf-8"))
    except Exception:
        pass
    logging.basicConfig(format=fmt, level=logging.INFO, handlers=handlers)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("telegram").setLevel(logging.WARNING)
    return logging.getLogger("zet_bot")

log = _setup()
