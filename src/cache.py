"""src/cache.py — TTL in-memory kesh"""
import time, threading
from src.logger import log

class Cache:
    def __init__(self):
        self._s: dict = {}
        self._lock    = threading.Lock()
        self._last_gc = time.time()

    def get(self, key: str):
        self._gc()
        with self._lock:
            item = self._s.get(key)
            if item is None: return None
            val, exp = item
            if exp and time.time() > exp:
                del self._s[key]; return None
            return val

    def set(self, key: str, value, ttl: int = 0):
        with self._lock:
            self._s[key] = (value, time.time() + ttl if ttl else None)

    def delete(self, key: str):
        with self._lock:
            self._s.pop(key, None)

    def delete_prefix(self, prefix: str):
        with self._lock:
            for k in [k for k in self._s if k.startswith(prefix)]:
                del self._s[k]

    def _gc(self):
        now = time.time()
        if now - self._last_gc < 300: return
        self._last_gc = now
        with self._lock:
            expired = [k for k,(_, e) in self._s.items() if e and now > e]
            for k in expired: del self._s[k]
        if expired: log.debug("Cache GC: %d o'chirildi", len(expired))
