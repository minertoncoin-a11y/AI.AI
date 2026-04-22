"""src/ai_helper.py — OpenAI GPT integratsiyasi"""
import asyncio, aiohttp
from src.logger import log
from src.config import cfg

_SYS = {
    "uz": (
        "Sen tajribali IT o'qituvchisan. Foydalanuvchi Linux, Python, DevOps va boshqa "
        "IT haqida savol beradi. Qisqa, aniq, amaliy javob ber. Kod misollar ko'rsat. "
        "O'zbek tilida javob ber. Maksimum 350 so'z."
    ),
    "ru": (
        "Ты опытный IT-преподаватель. Пользователь задаёт вопросы по Linux, Python, DevOps. "
        "Отвечай кратко, точно, практично. Показывай примеры кода. "
        "Отвечай по-русски. Максимум 350 слов."
    ),
    "en": (
        "You are an experienced IT instructor. The user asks about Linux, Python, DevOps and IT. "
        "Give short, accurate, practical answers with code examples. "
        "Answer in English. Max 350 words."
    ),
}

_EX = {
    "uz": "Quyidagi dars matnini oddiy so'zlar bilan tushuntir, misol kel:\n\n",
    "ru": "Объясни следующий текст урока простыми словами с примерами:\n\n",
    "en": "Explain the following lesson text simply with examples:\n\n",
}


class AIHelper:
    def __init__(self, api_key: str):
        self._key     = api_key
        self._enabled = bool(api_key and "YOUR" not in api_key)

    async def _call(self, messages: list, lang: str = "uz") -> str:
        if not self._enabled:
            msgs = {
                "uz": "⚠️ AI yoqilmagan. .env ga OPENAI_API_KEY qo'shing.",
                "ru": "⚠️ ИИ недоступен. Добавьте OPENAI_API_KEY в .env.",
                "en": "⚠️ AI not enabled. Add OPENAI_API_KEY to .env.",
            }
            return msgs.get(lang, msgs["uz"])

        headers = {
            "Authorization": f"Bearer {self._key}",
            "Content-Type": "application/json",
        }
        body = {
            "model": cfg.OPENAI_MODEL if hasattr(cfg, "OPENAI_MODEL") else "gpt-4o-mini",
            "max_tokens": 500,
            "temperature": 0.7,
            "messages": messages,
        }
        try:
            async with aiohttp.ClientSession() as s:
                async with s.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers=headers, json=body,
                    timeout=aiohttp.ClientTimeout(total=25),
                ) as resp:
                    if resp.status != 200:
                        err = await resp.text()
                        log.error("OpenAI %d: %s", resp.status, err[:200])
                        return "❌ AI so'rovida xato. Keyinroq urinib ko'ring."
                    data = await resp.json()
                    return data["choices"][0]["message"]["content"].strip()
        except asyncio.TimeoutError:
            return "⏱ AI javob bermadi (timeout). Qayta urinib ko'ring."
        except Exception as e:
            log.error("AI xato: %s", e)
            return "❌ AI bilan ulanishda xato."

    async def chat(self, question: str, lang: str = "uz") -> str:
        return await self._call([
            {"role": "system", "content": _SYS.get(lang, _SYS["uz"])},
            {"role": "user",   "content": question},
        ], lang)

    async def explain(self, lesson_text: str, lang: str = "uz") -> str:
        prompt = _EX.get(lang, _EX["uz"]) + lesson_text[:700]
        return await self._call([
            {"role": "system", "content": _SYS.get(lang, _SYS["uz"])},
            {"role": "user",   "content": prompt},
        ], lang)
