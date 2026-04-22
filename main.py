# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║     🐧 LINUX MASTER BOT — v11.0 ULTIMATE PLUS PLUS             ║
║  1000+ Dars | AI GPT | Leaderboard | 30+ Achievements       ║
║     Docker | Python | DevOps | SQL | Security | Cloud        ║
╚══════════════════════════════════════════════════════════════╝
"""

import asyncio
import logging
import os
import re
import sys
import time
import datetime
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes,
    MessageHandler, filters, CallbackQueryHandler
)

from src.config      import cfg
from src.database    import BotDatabase
from src.cache       import Cache
from src.i18n        import tr, set_lang, get_lang
from src.formatter   import (
    fmt_lesson, fmt_hub, fmt_progress_bar, fmt_mini_bar,
    fmt_leaderboard, fmt_achievements, fmt_settings,
    fmt_welcome, fmt_welcome_back, fmt_profile,
    fmt_quiz_question, fmt_quiz_result, fmt_progress_page,
    fmt_streak, fmt_xp_progress, _xp_level,
    SEP, SUB, DBL, THIN
)
from src.lessons     import LESSONS, QUIZZES
from src.extended_lessons import EXTENDED_LESSONS
from src.new_topics import NEW_TOPICS, NEW_QUIZZES
from src.mega_quizzes import MEGA_QUIZZES
LESSONS.update(EXTENDED_LESSONS)
LESSONS.update(NEW_TOPICS)
QUIZZES.update(NEW_QUIZZES)
QUIZZES.update(MEGA_QUIZZES)
from src.achievements import AchievementSystem
from src.ai_helper   import AIHelper
from src.admin       import setup_admin
from src.reminders   import setup_reminders
from src.logger      import log

if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()

db      = BotDatabase(cfg.DB_PATH)
cache   = Cache()
achieve = AchievementSystem(db)
ai      = AIHelper(cfg.OPENAI_KEY)

TOPICS_PER_PAGE = 8

# ── Rate limiter ─────────────────────────────────────────────
_rate_store: dict = {}

def _check_rate(uid: int, secs: int = 2) -> bool:
    now  = time.time()
    last = _rate_store.get(uid, 0)
    if now - last < secs:
        return False
    _rate_store[uid] = now
    return True

# ═══════════════════════════════════════════════════════════
#  YORDAMCHI
# ═══════════════════════════════════════════════════════════

def _ensure(update: Update) -> None:
    u = update.effective_user
    if not u: return
    if not cache.get(f"ue:{u.id}"):
        if not db.user_exists(u.id):
            db.add_user(u.id, u.username, u.first_name, u.last_name)
        cache.set(f"ue:{u.id}", True, ttl=3600)

def _lang(uid: int) -> str:
    v = cache.get(f"lang:{uid}")
    if v: return v
    lang = db.get_lang(uid) or "uz"
    cache.set(f"lang:{uid}", lang, ttl=600)
    return lang

def _pct(uid: int, topic: str) -> int:
    ck = f"pct:{uid}:{topic}"
    v  = cache.get(ck)
    if v is not None: return v
    prog  = db.get_progress(uid, topic)
    total = len(LESSONS[topic]["lessons"])
    done  = sum(1 for p in prog.values() if p.get("completed"))
    pct   = int(done / total * 100) if total else 0
    cache.set(ck, pct, ttl=60)
    return pct

def _save_lesson(uid: int, topic: str, idx: int) -> None:
    db.save_progress(uid, topic, idx)
    db.update_streak(uid)
    db.add_xp(uid, cfg.XP_LESSON)
    cache.delete(f"pct:{uid}:{topic}")
    cache.delete(f"stats:{uid}")
    # Coins: har 10 darsda
    stats = db.get_stats(uid) or {}
    total_done = stats.get("total_done", 0)
    if total_done > 0 and total_done % 10 == 0:
        db.add_coins(uid, 10)
    new = achieve.check(uid, topic, idx)
    if new:
        cache.set(f"badges:{uid}", new, ttl=180)

def _topic_label(t: str) -> str:
    return LESSONS[t]["title"].split("(")[0].strip()

def _total_stats(uid: int) -> tuple:
    total_l = sum(len(d["lessons"]) for d in LESSONS.values())
    total_c = sum(
        sum(1 for p in db.get_progress(uid, t).values() if p.get("completed"))
        for t in LESSONS
    )
    overall = int(total_c / total_l * 100) if total_l else 0
    return total_c, total_l, overall

# ═══════════════════════════════════════════════════════════
#  TUGMALAR
# ═══════════════════════════════════════════════════════════

def main_menu_kb(uid: int, page: int = 0) -> InlineKeyboardMarkup:
    topics      = list(LESSONS.keys())
    start       = page * TOPICS_PER_PAGE
    batch       = topics[start: start + TOPICS_PER_PAGE]
    total_pages = max(1, (len(topics) + TOPICS_PER_PAGE - 1) // TOPICS_PER_PAGE)
    kb  = []
    row = []
    for t in batch:
        pct  = _pct(uid, t)
        icon = "✅" if pct == 100 else ("🔵" if pct > 0 else "📚")
        lbl  = _topic_label(t)
        if len(lbl) > 15: lbl = lbl[:14] + "…"
        row.append(InlineKeyboardButton(f"{icon} {lbl}", callback_data=f"T:{t}"))
        if len(row) == 2:
            kb.append(row); row = []
    if row: kb.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton("◀️", callback_data=f"PG:{page-1}"))
    nav.append(InlineKeyboardButton(f"📄 {page+1}/{total_pages}", callback_data="NOOP"))
    if start + TOPICS_PER_PAGE < len(topics):
        nav.append(InlineKeyboardButton("▶️", callback_data=f"PG:{page+1}"))
    if nav: kb.append(nav)

    kb.append([
        InlineKeyboardButton("🎯 Quiz sinovi",     callback_data="QUIZ_MENU"),
        InlineKeyboardButton("📊 Progress",         callback_data="PROGRESS"),
    ])
    kb.append([
        InlineKeyboardButton("🏆 Leaderboard",      callback_data="LEADERS"),
        InlineKeyboardButton("🎖️ Yutuqlar",         callback_data="ACHIEVE"),
    ])
    kb.append([
        InlineKeyboardButton("🤖 AI Yordam",        callback_data="AI_MENU"),
        InlineKeyboardButton("👤 Profilim",          callback_data="PROFILE"),
    ])
    kb.append([
        InlineKeyboardButton("🔖 Bookmark",           callback_data="BOOKMARKS"),
        InlineKeyboardButton("⚙️ Sozlamalar",         callback_data="SETTINGS"),
    ])
    kb.append([
        InlineKeyboardButton("📅 Kunlik topshiriq",   callback_data="DAILY"),
        InlineKeyboardButton("🏪 Do'kon",              callback_data="SHOP"),
    ])
    kb.append([
        InlineKeyboardButton("📝 Eslatmalarim",       callback_data="NOTES"),
        InlineKeyboardButton("📊 Statistika",         callback_data="PROGRESS"),
    ])
    return InlineKeyboardMarkup(kb)


def lesson_kb(topic: str, idx: int, total: int) -> InlineKeyboardMarkup:
    rows = []
    nav  = []
    if idx > 0:
        nav.append(InlineKeyboardButton("⬅️ Oldingi dars", callback_data=f"PREV:{topic}"))
    if idx < total - 1:
        nav.append(InlineKeyboardButton("Keyingi dars ➡️", callback_data=f"NEXT:{topic}"))
    if nav: rows.append(nav)
    rows.append([
        InlineKeyboardButton("🎯 Quiz yech",       callback_data=f"QUIZ:{topic}"),
        InlineKeyboardButton("🤖 AI tushuntir",    callback_data=f"AI_EX:{topic}"),
    ])
    rows.append([
        InlineKeyboardButton("🔖 Saqlash",         callback_data=f"BM:{topic}"),
        InlineKeyboardButton("📝 Eslatma qo'sh",   callback_data=f"NOTE_ADD:{topic}"),
    ])
    rows.append([
        InlineKeyboardButton("📊 Progress",         callback_data="PROGRESS"),
        InlineKeyboardButton("🏠 Asosiy menyu",     callback_data="MENU"),
    ])
    return InlineKeyboardMarkup(rows)


def back_kb(cb: str = "MENU", label: str = "🏠 Asosiy menyu") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(label, callback_data=cb)]])


# ═══════════════════════════════════════════════════════════
#  START VA ASOSIY MENYU
# ═══════════════════════════════════════════════════════════

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE,
                         page: int = 0, edit: bool = False) -> None:
    _ensure(update)
    uid                   = update.effective_user.id
    stats                 = db.get_stats(uid) or {}
    total_c, total_l, overall = _total_stats(uid)
    streak                = stats.get("streak_days", 0)
    xp                    = stats.get("xp", 0)
    name                  = update.effective_user.first_name or "Do'stim"
    hub                   = fmt_hub(len(LESSONS), total_l, overall)
    back_txt              = fmt_welcome_back(name, xp, streak, total_c, total_l)

    text   = hub + back_txt + "\n📚 Mavzu tanlang 👇"
    markup = main_menu_kb(uid, page)
    q      = update.callback_query

    if edit and q:
        try:
            await q.edit_message_text(text, reply_markup=markup, parse_mode="HTML")
        except Exception:
            await q.message.reply_text(text, reply_markup=markup, parse_mode="HTML")
    elif update.message:
        await update.message.reply_text(text, reply_markup=markup, parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#  DARS
# ═══════════════════════════════════════════════════════════

async def show_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE,
                      topic: str, idx: int) -> None:
    uid     = update.effective_user.id
    lessons = LESSONS[topic]["lessons"]
    idx     = max(0, min(idx, len(lessons) - 1))
    context.user_data["topic"] = topic
    context.user_data["idx"]   = idx
    _save_lesson(uid, topic, idx)

    pct  = _pct(uid, topic)
    text = fmt_lesson(_topic_label(topic), lessons[idx], idx + 1, len(lessons), pct)

    badges = cache.get(f"badges:{uid}")
    if badges:
        cache.delete(f"badges:{uid}")
        names = "  ·  ".join(f"{b['icon']} <b>{b['name']}</b>" for b in badges)
        text += f"\n\n🎉 YANGI YUTUQ:\n{names}"

    markup = lesson_kb(topic, idx, len(lessons))
    q = update.callback_query
    if q:
        try:   await q.edit_message_text(text, reply_markup=markup, parse_mode="HTML")
        except Exception: await q.message.reply_text(text, reply_markup=markup, parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=markup, parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#  QUIZ — PREMIUM
# ═══════════════════════════════════════════════════════════

async def show_quiz_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid = update.effective_user.id
    kb  = []
    row = []
    for t in LESSONS:
        if t in QUIZZES and QUIZZES[t]:
            pct  = _pct(uid, t)
            icon = "✅" if pct == 100 else ("🔵" if pct > 0 else "🎯")
            lbl  = _topic_label(t)
            if len(lbl) > 15: lbl = lbl[:14] + "…"
            row.append(InlineKeyboardButton(f"{icon} {lbl}", callback_data=f"QSTART:{t}"))
            if len(row) == 2:
                kb.append(row); row = []
    if row: kb.append(row)
    kb.append([InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")])

    q = update.callback_query
    await q.edit_message_text(
        f"🎯 <b>QUIZ — MAVZU TANLANG</b>\n{DBL}\n\n"
        f"<b>Qoidalar:</b>\n"
        f"✅ To'g'ri javob = ⚡ <b>+{cfg.XP_QUIZ} XP</b>\n"
        f"❌ Noto'g'ri = tushuntirish beriladi\n"
        f"🏆 100% natija = maxsus badge\n\n"
        f"Qaysi mavzudan test topshirasiz? 👇",
        reply_markup=InlineKeyboardMarkup(kb),
        parse_mode="HTML",
    )


async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE, topic: str) -> None:
    context.user_data.update(q_topic=topic, q_idx=0, q_score=0,
                              q_start=datetime.datetime.now())
    await _show_q(update, context)


async def _show_q(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    topic  = context.user_data["q_topic"]
    idx    = context.user_data["q_idx"]
    qs     = QUIZZES[topic]
    if idx >= len(qs):
        await _quiz_done(update, context)
        return
    q_item = qs[idx]
    text   = fmt_quiz_question(_topic_label(topic), idx, len(qs), q_item["question"])

    # Variant tugmalari — A/B/C/D ikonlar
    opt_icons = ["🅰️", "🅱️", "🅾️", "🆗"]
    kb = [
        [InlineKeyboardButton(f"{opt_icons[i] if i < len(opt_icons) else chr(65+i)+')'} {opt}",
                              callback_data=f"QA:{i}")]
        for i, opt in enumerate(q_item["options"])
    ]
    kb.append([
        InlineKeyboardButton(f"⏭ O'tkazib yuborish", callback_data="QA:SKIP"),
        InlineKeyboardButton("🚪 Chiqish",            callback_data="QUIZ_MENU"),
    ])
    q = update.callback_query
    try:
        await q.edit_message_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
    except Exception:
        pass


async def answer_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE, ans) -> None:
    uid   = update.effective_user.id
    topic = context.user_data.get("q_topic")
    idx   = context.user_data.get("q_idx", 0)
    if not topic or topic not in QUIZZES or idx >= len(QUIZZES[topic]):
        return

    q_item = QUIZZES[topic][idx]
    q      = update.callback_query

    # O'tkazib yuborish
    if ans == "SKIP":
        context.user_data["q_idx"] = idx + 1
        await q.answer("⏭ O'tkazib yuborildi")
        await _show_q(update, context)
        return

    correct = ans == q_item["correct"]
    if correct:
        context.user_data["q_score"] = context.user_data.get("q_score", 0) + 1
        db.add_xp(uid, cfg.XP_QUIZ)
        cache.delete(f"stats:{uid}")

    context.user_data["q_idx"] = idx + 1
    expl     = q_item.get("explanation", "")
    expl_txt = f"\n💡 {expl}" if expl else ""

    if correct:
        await q.answer(f"✅ TO'G'RI!  +{cfg.XP_QUIZ} XP  🎉", show_alert=False)
    else:
        feedback = f"❌ Noto'g'ri!\nTo'g'ri javob: {chr(65+q_item['correct'])}) {q_item['options'][q_item['correct']]}{expl_txt}"
        await q.answer(feedback, show_alert=True)

    await _show_q(update, context)


async def _quiz_done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid   = update.effective_user.id
    topic = context.user_data["q_topic"]
    score = context.user_data.get("q_score", 0)
    total = len(QUIZZES[topic])
    secs  = (datetime.datetime.now() - context.user_data.get("q_start", datetime.datetime.now())).seconds
    db.save_quiz(uid, topic, score, total, secs)

    xp_earned = score * cfg.XP_QUIZ
    pct_score = int(score / total * 100) if total else 0
    if pct_score == 100:
        db.add_coins(uid, 15)
        db.get_stats(uid)  # refresh cache
    text  = fmt_quiz_result(_topic_label(topic), score, total, secs, xp_earned, pct_score == 100)
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Qayta topshirish", callback_data=f"QSTART:{topic}"),
         InlineKeyboardButton("🎯 Boshqa mavzu",     callback_data="QUIZ_MENU")],
        [InlineKeyboardButton("📊 Progress ko'r",    callback_data="PROGRESS"),
         InlineKeyboardButton("🏠 Asosiy menyu",     callback_data="MENU")],
    ])
    q = update.callback_query
    await q.edit_message_text(text, reply_markup=markup, parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#  LEADERBOARD — PREMIUM
# ═══════════════════════════════════════════════════════════

async def show_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid     = update.effective_user.id
    rows    = db.get_leaderboard(10)
    my      = db.get_rank(uid)
    total_l = sum(len(d["lessons"]) for d in LESSONS.values())
    text    = fmt_leaderboard(rows, uid, total_l, my or {})
    markup  = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Yangilash",    callback_data="LEADERS"),
         InlineKeyboardButton("👤 Profilim",     callback_data="PROFILE")],
        [InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")],
    ])
    q = update.callback_query
    try:
        await q.edit_message_text(text, reply_markup=markup, parse_mode="HTML")
    except Exception:
        await q.message.reply_text(text, reply_markup=markup, parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#  ACHIEVEMENTS
# ═══════════════════════════════════════════════════════════

async def show_achievements(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid    = update.effective_user.id
    earned = {e["badge_id"] for e in db.get_achievements(uid)}
    all_a  = achieve.all_badges()
    text   = fmt_achievements(all_a, earned)
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("👤 Profilim",     callback_data="PROFILE"),
         InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")],
    ])
    q = update.callback_query
    try:
        await q.edit_message_text(text, reply_markup=markup, parse_mode="HTML")
    except Exception:
        await q.message.reply_text(text, reply_markup=markup, parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#  PROGRESS
# ═══════════════════════════════════════════════════════════

async def show_progress(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid    = update.effective_user.id
    stats  = db.get_stats(uid) or {}
    streak = stats.get("streak_days", 0)
    xp     = stats.get("xp", 0)
    text   = fmt_progress_page(LESSONS, db.get_progress, uid, streak, xp)
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🏆 Leaderboard", callback_data="LEADERS"),
         InlineKeyboardButton("🎖️ Yutuqlar",   callback_data="ACHIEVE")],
        [InlineKeyboardButton("👤 Profilim",    callback_data="PROFILE"),
         InlineKeyboardButton("🏠 Asosiy",      callback_data="MENU")],
    ])
    q = update.callback_query
    try:
        await q.edit_message_text(text, reply_markup=markup, parse_mode="HTML")
    except Exception:
        await q.message.reply_text(text, reply_markup=markup, parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#  PROFIL — ULTRA PREMIUM
# ═══════════════════════════════════════════════════════════

async def show_profile(update: Update, context: ContextTypes.DEFAULT_TYPE,
                       edit: bool = False) -> None:
    uid    = update.effective_user.id
    u      = update.effective_user
    stats  = db.get_stats(uid) or {}
    earned = db.get_achievements(uid)
    bms    = db.get_bookmarks(uid)
    rank   = db.get_rank(uid)

    xp          = stats.get("xp", 0)
    streak      = stats.get("streak_days", 0)
    total_done  = stats.get("total_done", 0)
    total_quizzes = stats.get("total_quizzes", 0)
    total_l     = sum(len(d["lessons"]) for d in LESSONS.values())
    lang        = _lang(uid)
    name        = u.first_name or u.username or f"#{uid}"
    all_badges  = achieve.all_badges()
    rank_num    = rank.get("rank") if rank else None

    coins  = db.get_coins(uid)
    freeze = stats.get("streak_freeze", 0)
    text = fmt_profile(
        name=name, uid=uid, xp=xp, streak=streak,
        rank_num=rank_num, total_done=total_done, total_l=total_l,
        earned_count=len(earned), all_badges_count=len(all_badges),
        bms_count=len(bms), lang=lang, total_quizzes=total_quizzes,
        coins=coins, streak_freeze=freeze,
    )
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎖️ Yutuqlarim",   callback_data="ACHIEVE"),
         InlineKeyboardButton("🏆 Leaderboard",  callback_data="LEADERS")],
        [InlineKeyboardButton("📊 Progress",      callback_data="PROGRESS"),
         InlineKeyboardButton("🔖 Saqlangan",     callback_data="BOOKMARKS")],
        [InlineKeyboardButton("⚙️ Sozlamalar",   callback_data="SETTINGS"),
         InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")],
    ])
    q = update.callback_query
    if edit and q:
        try:
            await q.edit_message_text(text, reply_markup=markup, parse_mode="HTML")
        except Exception:
            await q.message.reply_text(text, reply_markup=markup, parse_mode="HTML")
    elif update.message:
        await update.message.reply_text(text, reply_markup=markup, parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#  AI YORDAM
# ═══════════════════════════════════════════════════════════

async def show_ai_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid   = update.effective_user.id
    today = datetime.date.today().isoformat()
    count = cache.get(f"ai_count:{uid}:{today}") or 0
    left  = max(0, cfg.AI_DAILY_LIMIT - count)
    bar   = fmt_progress_bar(int(count / cfg.AI_DAILY_LIMIT * 100), 12)

    context.user_data["ai_mode"] = True
    q = update.callback_query
    await q.edit_message_text(
        f"🤖 <b>AI YORDAMCHI</b>\n{DBL}\n\n"
        f"IT haqida istalgan savolingizni yozing!\n\n"
        f"<b>💡 Misol savollar:</b>\n"
        f"• <code>Linux'da cron job qanday ishlaydi?</code>\n"
        f"• <code>Docker va Kubernetes farqi nima?</code>\n"
        f"• <code>Python'da async/await tushuntir</code>\n"
        f"• <code>Nginx SSL sertifikat sozlash</code>\n"
        f"• <code>Git rebase vs merge farqi?</code>\n\n"
        f"{SUB}\n"
        f"📊 Bugungi limit:\n"
        f"{bar}  <b>{left}/{cfg.AI_DAILY_LIMIT}</b> so'rov qoldi\n\n"
        f"<b>Savolingizni yozing 👇</b>",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")
        ]]),
        parse_mode="HTML",
    )


async def ai_explain(update: Update, context: ContextTypes.DEFAULT_TYPE, topic: str) -> None:
    uid = update.effective_user.id
    idx = context.user_data.get("idx", 0)
    if topic not in LESSONS: return

    lesson_text = re.sub(r"<[^>]+>", "", LESSONS[topic]["lessons"][idx])[:700]
    lang = _lang(uid)
    q    = update.callback_query

    # Limit tekshirish
    today = datetime.date.today().isoformat()
    key   = f"ai_count:{uid}:{today}"
    count = cache.get(key) or 0
    if count >= cfg.AI_DAILY_LIMIT:
        await q.answer("⚠️ Bugungi AI limitiga yetdingiz!", show_alert=True)
        return
    cache.set(key, count + 1, ttl=86400)

    await q.answer("🤖 AI tayyorlamoqda...")
    await q.edit_message_text(
        f"🤖 <b>AI tahlil qilyapti...</b>\n\n⏳ Biroz kuting",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⏳", callback_data="NOOP")]]),
        parse_mode="HTML",
    )
    answer = await ai.explain(lesson_text, lang)
    remaining = cfg.AI_DAILY_LIMIT - count - 1
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("◀️ Darsga qaytish", callback_data=f"T:{topic}")],
        [InlineKeyboardButton("🤖 Yana savol",      callback_data="AI_MENU"),
         InlineKeyboardButton("🏠 Asosiy menyu",   callback_data="MENU")],
    ])
    await q.edit_message_text(
        f"🤖 <b>AI TUSHUNTIRISHI</b>\n{SEP}\n\n{answer}\n\n"
        f"{THIN}\n<i>💬 Qolgan so'rovlar: {remaining}/{cfg.AI_DAILY_LIMIT}</i>",
        reply_markup=markup,
        parse_mode="HTML",
    )


# ═══════════════════════════════════════════════════════════
#  SOZLAMALAR
# ═══════════════════════════════════════════════════════════

async def show_settings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid   = update.effective_user.id
    lang  = _lang(uid)
    stats = db.get_stats(uid) or {}
    rem   = stats.get("reminder_on", False)
    xp    = stats.get("xp", 0)
    streak = stats.get("streak_days", 0)
    text  = fmt_settings(lang, rem, streak, xp)
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🇺🇿 O'zbek",  callback_data="LANG:uz"),
         InlineKeyboardButton("🇷🇺 Русский", callback_data="LANG:ru"),
         InlineKeyboardButton("🇬🇧 English", callback_data="LANG:en")],
        [InlineKeyboardButton(
            "🔕 Eslatmani o'chir" if rem else "🔔 Eslatmani yoq",
            callback_data="REMIND_TOGGLE",
        )],
        [InlineKeyboardButton("👤 Profil",       callback_data="PROFILE"),
         InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")],
    ])
    q = update.callback_query
    try:
        await q.edit_message_text(text, reply_markup=markup, parse_mode="HTML")
    except Exception:
        await q.message.reply_text(text, reply_markup=markup, parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#  BOOKMARKS
# ═══════════════════════════════════════════════════════════

async def show_bookmarks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid = update.effective_user.id
    bms = db.get_bookmarks(uid)
    q   = update.callback_query
    if not bms:
        await q.edit_message_text(
            f"📭 <b>Saqlangan dars yo'q</b>\n{SEP}\n\n"
            "Dars ichida 🔖 <b>Saqlash</b> tugmasini bosib\n"
            "darslarni keyinroq davom ettirish uchun saqlang.",
            reply_markup=back_kb(),
            parse_mode="HTML",
        )
        return
    kb = [
        [InlineKeyboardButton(
            f"📖 {LESSONS[b['topic']]['title'].split('(')[0].strip()[:18]} — {b['lesson_idx']+1}-dars",
            callback_data=f"GO:{b['topic']}:{b['lesson_idx']}",
        )]
        for b in bms if b["topic"] in LESSONS
    ]
    kb.append([InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")])
    await q.edit_message_text(
        f"🔖 <b>SAQLANGAN DARSLAR</b>  ({len(bms)} ta)\n{SEP}",
        reply_markup=InlineKeyboardMarkup(kb),
        parse_mode="HTML",
    )


# ═══════════════════════════════════════════════════════════
#  DAILY CHALLENGE
# ═══════════════════════════════════════════════════════════

async def show_daily_challenge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid   = update.effective_user.id
    today = datetime.date.today().strftime("%d.%m.%Y")
    chal  = db.get_daily_challenge(uid)
    q     = update.callback_query

    if not chal:
        # Generate daily challenge: random topic and lesson
        import random
        topics = [t for t in LESSONS.keys() if len(LESSONS[t]["lessons"]) > 5]
        topic  = random.choice(topics)
        lesson_count = len(LESSONS[topic]["lessons"])
        idx    = random.randint(0, min(lesson_count - 1, 20))
        db.set_daily_challenge(uid, topic, idx)
        chal   = db.get_daily_challenge(uid)

    topic     = chal.get("topic", "asoslar")
    lesson_idx= chal.get("lesson_idx", 0)
    completed = chal.get("completed", 0)
    topic_name= _topic_label(topic) if topic in LESSONS else topic
    lesson_num= lesson_idx + 1

    if completed:
        status_text = "✅ <b>BAJARILDI!</b> +50 XP va +20 🪙 coin olindi!"
        action_btn  = [InlineKeyboardButton("🎉 Bajarilgan", callback_data="DAILY_DONE")]
    else:
        status_text = "⏳ Hali bajarilmagan. Darsni o'qib challenge qiling!"
        action_btn  = [InlineKeyboardButton("📖 Darsni boshlash", callback_data="DAILY_START")]

    from src.formatter import fmt_daily_challenge
    text = fmt_daily_challenge(topic_name, lesson_num, bool(completed), today)
    kb = [action_btn, [InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")]]
    try:
        await q.edit_message_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
    except Exception:
        await q.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")


async def start_daily_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid  = update.effective_user.id
    chal = db.get_daily_challenge(uid)
    if not chal:
        await update.callback_query.answer("Xato!")
        return
    topic = chal["topic"]
    idx   = chal["lesson_idx"]
    # Mark complete and give rewards
    was_new = db.complete_daily_challenge(uid)
    if was_new:
        db.add_xp(uid, 50)
        db.add_coins(uid, 20)
        cache.delete(f"stats:{uid}")
        await update.callback_query.answer("🎉 +50 XP +20 🪙 mukofot olindi!", show_alert=True)
        # Check achievements
        new_badges = achieve.check(uid, topic, idx)
        if new_badges:
            cache.set(f"badges:{uid}", new_badges, ttl=180)
    await show_lesson(update, context, topic, idx)


# ═══════════════════════════════════════════════════════════
#  SHOP — COIN BOZOR
# ═══════════════════════════════════════════════════════════

async def show_shop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid   = update.effective_user.id
    coins = db.get_coins(uid)
    stats = db.get_stats(uid) or {}
    freeze_count = stats.get("streak_freeze", 0)
    q     = update.callback_query

    from src.formatter import fmt_shop
    text = fmt_shop(coins, freeze_count)
    kb = [
        [InlineKeyboardButton("🧊 Streak Freeze — 30🪙", callback_data="SHOP_FREEZE")],
        [InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")],
    ]
    try:
        await q.edit_message_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
    except Exception:
        await q.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")


async def buy_streak_freeze(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid = update.effective_user.id
    q   = update.callback_query
    if db.spend_coins(uid, 30):
        db.add_streak_freeze(uid, 1)
        await q.answer("🧊 Streak Freeze sotib olindi! Endi 1 kunlik tanaffus streak'ni saqlab qoladi.", show_alert=True)
    else:
        coins = db.get_coins(uid)
        await q.answer(f"❌ Yetarli coin yo'q! Sizda {coins} 🪙 bor, kerak 30 🪙.", show_alert=True)
    await show_shop(update, context)


# ═══════════════════════════════════════════════════════════
#  NOTES — ESLATMALAR
# ═══════════════════════════════════════════════════════════

async def show_notes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid   = update.effective_user.id
    notes = db.get_notes(uid)
    q     = update.callback_query

    if not notes:
        SEP32 = "━" * 32
        text = (
            f"📝 <b>ESLATMALARIM</b>\n"
            f"{SEP32}\n\n"
            f"📭 Hali eslatma yo'q.\n\n"
            f"<i>Dars ichida 📝 tugmasini bosib eslatma qo'shing!</i>"
        )
        kb = [[InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")]]
        try:
            await q.edit_message_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        except Exception:
            await q.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return

    kb = []
    SEP32 = "━" * 32
    lines = [f"📝 <b>ESLATMALARIM</b> ({len(notes)} ta)\n{SEP32}\n"]
    for note in notes[:10]:
        topic_name = _topic_label(note["topic"]) if note["topic"] in LESSONS else note["topic"]
        note_preview = note['note_text'][:80] + ("..." if len(note['note_text']) > 80 else "")
        lines.append(
            f"📌 <b>{topic_name}</b> — {note['lesson_idx']+1}-dars\n"
            f"   <i>{note_preview}</i>\n"
        )
        kb.append([InlineKeyboardButton(
            f"🗑 O'chirish: {topic_name[:15]}",
            callback_data=f"NOTE_DEL:{note['id']}"
        )])

    kb.append([InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")])
    text = "\n".join(lines)
    try:
        await q.edit_message_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
    except Exception:
        await q.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")


async def prompt_add_note(update: Update, context: ContextTypes.DEFAULT_TYPE, topic: str) -> None:
    uid = update.effective_user.id
    idx = context.user_data.get("idx", 0)
    context.user_data["note_mode"] = True
    context.user_data["note_topic"] = topic
    context.user_data["note_idx"]   = idx
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(
        "\U0001f4dd <b>ESLATMA QO'SHISH</b>\n\n"
        f"<b>{_topic_label(topic) if topic in LESSONS else topic}</b> \u2014 {idx+1}-dars\n\n"
        "Eslatma matnini yozing \U0001f447\n"
        "<i>(Max 500 belgi)</i>",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("\u274c Bekor qilish", callback_data=f"T:{topic}")
        ]]),
        parse_mode="HTML",
    )


async def delete_note_cb(update: Update, context: ContextTypes.DEFAULT_TYPE, note_id: int) -> None:
    uid = update.effective_user.id
    db.delete_note(uid, note_id)
    await update.callback_query.answer("🗑 Eslatma o'chirildi!")
    await show_notes(update, context)


# ═══════════════════════════════════════════════════════════
#  CALLBACK HANDLER
# ═══════════════════════════════════════════════════════════

async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    q    = update.callback_query
    data = q.data
    uid  = update.effective_user.id
    _ensure(update)

    if not _check_rate(uid):
        await q.answer("⚠️ Juda tez! Biroz kuting.", show_alert=False)
        return
    await q.answer()

    if   data == "MENU":              await show_main_menu(update, context, edit=True)
    elif data == "PROGRESS":          await show_progress(update, context)
    elif data == "PROFILE":           await show_profile(update, context, edit=True)
    elif data == "QUIZ_MENU":         await show_quiz_menu(update, context)
    elif data == "LEADERS":           await show_leaderboard(update, context)
    elif data == "ACHIEVE":           await show_achievements(update, context)
    elif data == "AI_MENU":           await show_ai_menu(update, context)
    elif data == "BOOKMARKS":         await show_bookmarks(update, context)
    elif data == "SETTINGS":          await show_settings(update, context)
    elif data == "NOOP":              pass

    elif data.startswith("PG:"):
        markup = main_menu_kb(uid, int(data[3:]))
        try:    await q.edit_message_reply_markup(markup)
        except: pass

    elif data.startswith("T:"):
        topic = data[2:]
        if topic in LESSONS:
            idx = context.user_data.get("idx", 0) if context.user_data.get("topic") == topic else 0
            await show_lesson(update, context, topic, idx)

    elif data.startswith("NEXT:"):
        topic = data[5:]
        await show_lesson(update, context, topic, context.user_data.get("idx", 0) + 1)

    elif data.startswith("PREV:"):
        topic = data[5:]
        await show_lesson(update, context, topic, max(0, context.user_data.get("idx", 0) - 1))

    elif data.startswith("GO:"):
        parts = data[3:].split(":")
        await show_lesson(update, context, parts[0], int(parts[1]))

    elif data.startswith("QUIZ:"):   await start_quiz(update, context, data[5:])
    elif data.startswith("QSTART:"): await start_quiz(update, context, data[7:])

    elif data.startswith("QA:"):
        raw = data[3:]
        ans = "SKIP" if raw == "SKIP" else int(raw)
        await answer_quiz(update, context, ans)

    elif data.startswith("AI_EX:"):  await ai_explain(update, context, data[6:])

    elif data.startswith("BM:"):
        topic = data[3:]
        idx   = context.user_data.get("idx", 0)
        db.add_bookmark(uid, topic, idx)
        await q.answer("🔖 Dars saqlandi!")

    elif data.startswith("LANG:"):
        lang = data[5:]
        db.set_lang(uid, lang)
        cache.delete(f"lang:{uid}")
        await q.answer({"uz": "🇺🇿 O'zbek!", "ru": "🇷🇺 Русский!", "en": "🇬🇧 English!"}.get(lang, "OK"))
        await show_settings(update, context)

    elif data == "REMIND_TOGGLE":
        stats = db.get_stats(uid) or {}
        new   = not stats.get("reminder_on", False)
        db.set_reminder(uid, new)
        await q.answer("✅ Yoqildi!" if new else "❌ O'chirildi!")
        await show_settings(update, context)

    elif data == "DAILY":            await show_daily_challenge(update, context)
    elif data == "DAILY_START":      await start_daily_lesson(update, context)
    elif data == "SHOP":             await show_shop(update, context)
    elif data == "SHOP_FREEZE":      await buy_streak_freeze(update, context)
    elif data == "NOTES":            await show_notes(update, context)
    elif data.startswith("NOTE_ADD:"): await prompt_add_note(update, context, data[9:])
    elif data.startswith("NOTE_DEL:"): await delete_note_cb(update, context, int(data[9:]))
    elif data == "DAILY_DONE":
        await q.answer("✅ Kunlik topshiriq allaqachon bajarilgan!", show_alert=True)

    else:
        log.warning("Noma'lum callback: %s", data)


# ═══════════════════════════════════════════════════════════
#  COMMANDS
# ═══════════════════════════════════════════════════════════

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid   = update.effective_user.id
    stats = db.get_stats(uid) or {}
    name  = update.effective_user.first_name or "Do'stim"

    # Birinchi marta kirish
    if stats.get("xp", 0) == 0 and stats.get("total_done", 0) == 0:
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🚀 Boshlash!", callback_data="MENU")],
            [InlineKeyboardButton("📚 Darslar",   callback_data="PG:0"),
             InlineKeyboardButton("🎯 Quiz",       callback_data="QUIZ_MENU")],
            [InlineKeyboardButton("🤖 AI Yordam", callback_data="AI_MENU"),
             InlineKeyboardButton("🏆 Top",        callback_data="LEADERS")],
        ])
        await update.message.reply_text(
            fmt_welcome(name),
            reply_markup=markup,
            parse_mode="HTML",
        )
    else:
        await show_main_menu(update, context)


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    lang = _lang(update.effective_user.id)
    texts = {
        "uz": (
            f"📖 <b>BARCHA BUYRUQLAR</b>\n{DBL}\n\n"
            "/start — 🏠 Asosiy menyu\n"
            "/lesson &lt;kalit&gt; — 📖 Darsga kirish\n"
            "/quiz &lt;kalit&gt; — 🎯 Quiz boshlash\n"
            "/progress — 📊 Mening progressim\n"
            "/profile — 👤 Mening profilim\n"
            "/leaderboard — 🏆 Top reyting\n"
            "/achievements — 🎖️ Yutuqlar\n"
            "/bookmarks — 🔖 Saqlangan darslar\n"
            "/search &lt;so'z&gt; — 🔍 Darslardan qidirish\n"
            "/list — 📚 Barcha mavzular ro'yxati\n"
            "/settings — ⚙️ Sozlamalar\n"
            "/about — ℹ️ Bot haqida\n\n"
            f"{THIN}\n"
            "🤖 Istalgan IT savolingizni yozing — AI javob beradi!"
        ),
        "ru": (
            f"📖 <b>ВСЕ КОМАНДЫ</b>\n{DBL}\n\n"
            "/start — 🏠 Главное меню\n"
            "/lesson &lt;ключ&gt; — 📖 Открыть урок\n"
            "/quiz &lt;ключ&gt; — 🎯 Начать квиз\n"
            "/progress — 📊 Мой прогресс\n"
            "/profile — 👤 Мой профиль\n"
            "/leaderboard — 🏆 Рейтинг\n"
            "/achievements — 🎖️ Достижения\n"
            "/settings — ⚙️ Настройки\n\n"
            "🤖 Задайте любой IT вопрос — ИИ ответит!"
        ),
        "en": (
            f"📖 <b>ALL COMMANDS</b>\n{DBL}\n\n"
            "/start — 🏠 Main menu\n"
            "/lesson &lt;key&gt; — 📖 Open lesson\n"
            "/quiz &lt;key&gt; — 🎯 Start quiz\n"
            "/progress — 📊 My progress\n"
            "/profile — 👤 My profile\n"
            "/leaderboard — 🏆 Rankings\n"
            "/achievements — 🎖️ Badges\n"
            "/settings — ⚙️ Settings\n\n"
            "🤖 Ask any IT question — AI will answer!"
        ),
    }
    await update.message.reply_text(texts.get(lang, texts["uz"]), parse_mode="HTML")


async def cmd_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    if not context.args:
        keys = ", ".join(list(LESSONS.keys())[:8])
        await update.message.reply_text(
            f"❌ Kalit kiritilmadi!\nMisol: <code>/lesson asoslar</code>\n"
            f"Mavzular: <code>{keys}...</code>\n/list — to'liq ro'yxat",
            parse_mode="HTML",
        )
        return
    topic = context.args[0].lower()
    if topic not in LESSONS:
        await update.message.reply_text(
            f"❌ <b>'{topic}'</b> topilmadi.\n/list — ro'yxatni ko'ring",
            parse_mode="HTML",
        )
        return
    context.user_data["topic"] = topic
    context.user_data["idx"]   = 0
    await show_lesson(update, context, topic, 0)


async def cmd_progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid    = update.effective_user.id
    stats  = db.get_stats(uid) or {}
    text   = fmt_progress_page(LESSONS, db.get_progress, uid,
                                stats.get("streak_days", 0), stats.get("xp", 0))
    await update.message.reply_text(text, parse_mode="HTML")


async def cmd_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    lines = [f"📚 <b>BARCHA MAVZULAR</b>\n{DBL}\n"]
    for k, d in LESSONS.items():
        cnt = len(d["lessons"])
        lines.append(f"• <b>{d['title'].split('(')[0].strip()}</b> ({cnt} dars)\n  → <code>/lesson {k}</code>")
    await update.message.reply_text("\n".join(lines), parse_mode="HTML")


async def cmd_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    if not context.args:
        await update.message.reply_text(
            f"🔍 <b>QIDIRISH</b>\n\nMisol: <code>/search chmod</code>\nMisol: <code>/search docker run</code>",
            parse_mode="HTML",
        )
        return
    term = " ".join(context.args).lower().strip()
    if len(term) < 2:
        await update.message.reply_text("⚠️ Kamida 2 ta harf kiriting.")
        return

    results = []
    for topic, data in LESSONS.items():
        for i, lesson in enumerate(data["lessons"]):
            clean = re.sub(r"<[^>]+>", "", lesson).lower()
            if term in clean:
                results.append((topic, i, data["title"].split("(")[0].strip()))

    total = len(results)
    if not results:
        await update.message.reply_text(
            f"🔍 <b>'{term}'</b> — hech narsa topilmadi.\n💡 Boshqa kalit so'z sinab ko'ring.",
            parse_mode="HTML",
        )
        return

    shown = results[:cfg.SEARCH_MAX_RESULTS]
    kb = [
        [InlineKeyboardButton(f"📖 {title[:18]} — {i+1}-dars", callback_data=f"GO:{topic}:{i}")]
        for topic, i, title in shown
    ]
    more = f"\n<i>+{total - cfg.SEARCH_MAX_RESULTS} ta ko'proq natija bor.</i>" if total > cfg.SEARCH_MAX_RESULTS else ""
    kb.append([InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")])
    await update.message.reply_text(
        f"🔍 <b>'{term}'</b> — <b>{total}</b> natija{more}",
        reply_markup=InlineKeyboardMarkup(kb),
        parse_mode="HTML",
    )


async def cmd_bookmarks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid = update.effective_user.id
    bms = db.get_bookmarks(uid)
    if not bms:
        await update.message.reply_text("📭 Saqlangan dars yo'q.\nDars ichida 🔖 tugmasini bosing.")
        return
    kb = [
        [InlineKeyboardButton(
            f"📖 {LESSONS[b['topic']]['title'].split('(')[0].strip()[:18]} — {b['lesson_idx']+1}-dars",
            callback_data=f"GO:{b['topic']}:{b['lesson_idx']}",
        )]
        for b in bms if b["topic"] in LESSONS
    ]
    kb.append([InlineKeyboardButton("🏠 Asosiy menyu", callback_data="MENU")])
    await update.message.reply_text(
        f"🔖 <b>SAQLANGAN DARSLAR</b> ({len(bms)} ta):",
        reply_markup=InlineKeyboardMarkup(kb),
        parse_mode="HTML",
    )


async def cmd_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid     = update.effective_user.id
    rows    = db.get_leaderboard(10)
    my      = db.get_rank(uid)
    total_l = sum(len(d["lessons"]) for d in LESSONS.values())
    text    = fmt_leaderboard(rows, uid, total_l, my or {})
    await update.message.reply_text(text, parse_mode="HTML")


async def cmd_achievements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid    = update.effective_user.id
    earned = {e["badge_id"] for e in db.get_achievements(uid)}
    all_a  = achieve.all_badges()
    await update.message.reply_text(fmt_achievements(all_a, earned), parse_mode="HTML")


async def cmd_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid   = update.effective_user.id
    lang  = _lang(uid)
    stats = db.get_stats(uid) or {}
    rem   = stats.get("reminder_on", False)
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🇺🇿 O'zbek",  callback_data="LANG:uz"),
         InlineKeyboardButton("🇷🇺 Русский", callback_data="LANG:ru"),
         InlineKeyboardButton("🇬🇧 English", callback_data="LANG:en")],
        [InlineKeyboardButton("🔔 Eslatma" if not rem else "🔕 O'chir",
                              callback_data="REMIND_TOGGLE")],
    ])
    labels = {"uz": "🇺🇿 O'zbek", "ru": "🇷🇺 Русский", "en": "🇬🇧 English"}
    await update.message.reply_text(
        f"⚙️ <b>SOZLAMALAR</b>\n\nTil: <b>{labels.get(lang, lang)}</b>\nEslatma: {'✅' if rem else '❌'}",
        reply_markup=markup,
        parse_mode="HTML",
    )


async def cmd_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    if not context.args:
        await update.message.reply_text(
            "Misol: <code>/quiz asoslar</code>\n/list — mavzular",
            parse_mode="HTML",
        )
        return
    topic = context.args[0].lower()
    if topic not in QUIZZES or not QUIZZES[topic]:
        await update.message.reply_text(f"'{topic}' uchun quiz yo'q.")
        return
    context.user_data.update(q_topic=topic, q_idx=0, q_score=0,
                              q_start=datetime.datetime.now())
    qs     = QUIZZES[topic]
    q_item = qs[0]
    opts   = "\n".join(f"{chr(65+i)}) {o}" for i, o in enumerate(q_item["options"]))
    await update.message.reply_text(
        f"🎯 <b>{_topic_label(topic)}</b>\n\nSavol 1/{len(qs)}:\n<b>{q_item['question']}</b>\n\n{opts}\n\n<i>A/B/C/D yozing:</i>",
        parse_mode="HTML",
    )


async def cmd_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    await show_profile(update, context, edit=False)


async def cmd_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    total_l = sum(len(d["lessons"]) for d in LESSONS.values())
    await update.message.reply_text(
        f"🤖 <b>Linux Master Bot — v11.0 ULTIMATE PLUS</b>\n{DBL}\n\n"
        f"📚 <b>{len(LESSONS)}</b> mavzu  ·  <b>{total_l}+</b> dars\n"
        f"🌐 O'zbek / Rus / Ingliz\n"
        f"🤖 AI yordamchi ({cfg.OPENAI_MODEL})\n"
        f"🏆 Leaderboard va XP tizimi (8 daraja)\n"
        f"🎖️ Achievement tizimi (35+ badge!)\n"
        f"🔥 Streak va kundalik eslatmalar\n"
        f"🔖 Darslarni bookmark qilish\n"
        f"👤 Ultra-premium profil sahifasi\n"
        f"⚡ Rate limiting va spam himoyasi\n"
        f"🛡️ Kunlik AI so'rov limiti\n"
        f"👮 Admin panel (statistika, broadcast)\n"
        f"🐳 Docker, 🐍 Python PRO, ⚙️ DevOps yangi kurslar!\n\n"
        f"/help — barcha buyruqlar",
        parse_mode="HTML",
    )


# ═══════════════════════════════════════════════════════════
#  XABAR HANDLER
# ═══════════════════════════════════════════════════════════

async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid  = update.effective_user.id
    text = update.message.text.strip()
    lang = _lang(uid)

    # Quiz rejimi (A/B/C/D)
    if context.user_data.get("q_topic") and text.upper() in "ABCD" and len(text) == 1:
        topic = context.user_data["q_topic"]
        idx   = context.user_data.get("q_idx", 0)
        if topic in QUIZZES and idx < len(QUIZZES[topic]):
            ans   = ord(text.upper()) - 65
            q_obj = QUIZZES[topic][idx]
            corr  = q_obj["correct"]
            ok    = ans == corr
            if ok:
                context.user_data["q_score"] = context.user_data.get("q_score", 0) + 1
                db.add_xp(uid, cfg.XP_QUIZ)
                cache.delete(f"stats:{uid}")
            context.user_data["q_idx"] = idx + 1
            expl = q_obj.get("explanation", "")
            resp = (f"✅ <b>To'g'ri! +{cfg.XP_QUIZ} XP</b>" if ok
                    else f"❌ <b>Noto'g'ri.</b> To'g'ri: <b>{chr(65+corr)}</b>\n💡 <i>{expl}</i>")
            await update.message.reply_text(resp, parse_mode="HTML")
            nidx = idx + 1
            if nidx >= len(QUIZZES[topic]):
                score = context.user_data.get("q_score", 0)
                total = len(QUIZZES[topic])
                db.save_quiz(uid, topic, score, total, 0)
                await update.message.reply_text(
                    fmt_quiz_result(_topic_label(topic), score, total, 0, score * cfg.XP_QUIZ),
                    parse_mode="HTML",
                )
                for k in ["q_topic", "q_idx", "q_score"]:
                    context.user_data.pop(k, None)
            else:
                q_item = QUIZZES[topic][nidx]
                opts   = "\n".join(f"{chr(65+i)}) {o}" for i, o in enumerate(q_item["options"]))
                await update.message.reply_text(
                    f"🎯 Savol <b>{nidx+1}/{len(QUIZZES[topic])}</b>:\n<b>{q_item['question']}</b>\n\n{opts}",
                    parse_mode="HTML",
                )
        return

    # Note mode
    if context.user_data.get("note_mode"):
        context.user_data["note_mode"] = False
        topic = context.user_data.pop("note_topic", None)
        idx   = context.user_data.pop("note_idx", 0)
        if topic and len(text) >= 3:
            db.add_note(uid, topic, idx, text)
            markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("📝 Eslatmalarim", callback_data="NOTES"),
                 InlineKeyboardButton("◀️ Darsga qaytish", callback_data=f"T:{topic}")],
            ])
            await update.message.reply_text(
                f"\u2705 <b>Eslatma saqlandi!</b>\n<i>{text[:100]}</i>",
                reply_markup=markup,
                parse_mode="HTML",
            )
        else:
            await update.message.reply_text("❌ Matn juda qisqa. Kamida 3 belgi kiriting.")
        return

    # AI mode
    if context.user_data.get("ai_mode"):
        context.user_data["ai_mode"] = False
        today = datetime.date.today().isoformat()
        key   = f"ai_count:{uid}:{today}"
        count = cache.get(key) or 0
        if count >= cfg.AI_DAILY_LIMIT:
            await update.message.reply_text(
                f"⚠️ Bugun AI limitiga yetdingiz ({cfg.AI_DAILY_LIMIT} ta).\nErtaga yangilanadi. 🔄"
            )
            return
        cache.set(key, count + 1, ttl=86400)
        wait   = await update.message.reply_text("🤖 <b>AI javob tayyorlamoqda...</b> ⏳", parse_mode="HTML")
        answer = await ai.chat(text, lang)
        await wait.delete()
        remaining = cfg.AI_DAILY_LIMIT - count - 1
        db.inc_ai_requests(uid)
        # AI badge check
        new_badges = achieve.check_ai_usage(uid)
        if new_badges:
            badge_txt = "  ·  ".join(f"{b['icon']} <b>{b['name']}</b>" for b in new_badges)
            answer += f"\n\n🎉 Yangi badge: {badge_txt}"
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🤖 Yana savol", callback_data="AI_MENU"),
             InlineKeyboardButton("🏠 Asosiy",     callback_data="MENU")],
        ])
        await update.message.reply_text(
            f"🤖 <b>AI JAVOBI</b>\n{SEP}\n\n{answer}\n\n"
            f"{THIN}\n<i>💬 Qolgan so'rovlar: {remaining}/{cfg.AI_DAILY_LIMIT}</i>",
            reply_markup=markup,
            parse_mode="HTML",
        )
        return

    # Default
    await update.message.reply_text(
        f"👋 /start — asosiy menyu\n🤖 AI savol uchun: <b>AI Yordam</b> tugmasini bosing",
        parse_mode="HTML",
    )


# ═══════════════════════════════════════════════════════════
#  XATO HANDLER
# ═══════════════════════════════════════════════════════════

async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE):
    log.error("Xato:", exc_info=context.error)
    if isinstance(update, Update):
        if update.callback_query:
            try: await update.callback_query.answer("❌ Xato. Qayta urining.", show_alert=True)
            except: pass
        elif update.message:
            await update.message.reply_text("❌ Xato yuz berdi. /start ni bosing.")


# ═══════════════════════════════════════════════════════════
#  POST INIT
# ═══════════════════════════════════════════════════════════

async def post_init(application):
    cmds = [
        BotCommand("start",        "🏠 Asosiy menyu"),
        BotCommand("lesson",       "📖 Darsga kirish: /lesson asoslar"),
        BotCommand("quiz",         "🎯 Quiz: /quiz asoslar"),
        BotCommand("progress",     "📊 Mening progressim"),
        BotCommand("profile",      "👤 Mening profilim"),
        BotCommand("leaderboard",  "🏆 Top reyting"),
        BotCommand("achievements", "🎖️ Yutuqlar"),
        BotCommand("bookmarks",    "🔖 Saqlangan darslar"),
        BotCommand("daily",        "📅 Kunlik topshiriq"),
        BotCommand("shop",         "🏪 Coin do'kon"),
        BotCommand("notes",        "📝 Eslatmalarim"),
        BotCommand("search",       "🔍 Qidirish: /search chmod"),
        BotCommand("list",         "📚 Barcha mavzular"),
        BotCommand("settings",     "⚙️ Sozlamalar"),
        BotCommand("about",        "ℹ️ Bot haqida"),
        BotCommand("help",         "❓ Yordam"),
    ]
    await application.bot.set_my_commands(cmds)
    log.info("✅ Bot buyruqlari o'rnatildi.")



# ═══════════════════════════════════════════════════════════
#  YANGI BUYRUQLAR — DAILY, SHOP, NOTES
# ═══════════════════════════════════════════════════════════

async def cmd_daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid   = update.effective_user.id
    today = datetime.date.today().strftime("%d.%m.%Y")
    chal  = db.get_daily_challenge(uid)
    if not chal:
        import random
        topics = [t for t in LESSONS.keys() if len(LESSONS[t]["lessons"]) > 3]
        topic  = random.choice(topics)
        idx    = random.randint(0, min(len(LESSONS[topic]["lessons"]) - 1, 20))
        db.set_daily_challenge(uid, topic, idx)
        chal   = db.get_daily_challenge(uid)
    topic_name = _topic_label(chal["topic"]) if chal["topic"] in LESSONS else chal["topic"]
    completed  = chal.get("completed", 0)
    status     = "✅ Bajarildi!" if completed else "⏳ Bajarilmagan"
    markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("📅 Batafsil", callback_data="DAILY")
    ]])
    await update.message.reply_text(
        f"📅 <b>Bugungi topshiriq ({today})</b>\n"
        f"📚 {topic_name} — {chal['lesson_idx']+1}-dars\n"
        f"Status: {status}",
        reply_markup=markup,
        parse_mode="HTML",
    )


async def cmd_shop_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid   = update.effective_user.id
    coins = db.get_coins(uid)
    markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("🏪 Do'konni ochish", callback_data="SHOP")
    ]])
    await update.message.reply_text(
        f"🏪 <b>Coin Do'kon</b>\n💰 Sizda: <b>{coins} 🪙</b>",
        reply_markup=markup,
        parse_mode="HTML",
    )


async def cmd_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ensure(update)
    uid   = update.effective_user.id
    notes = db.get_notes(uid)
    if not notes:
        await update.message.reply_text("📝 Hali eslatma yo'q. Dars ichida 📝 tugmasini bosing.")
        return
    markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("📝 Eslatmalarni ko'rish", callback_data="NOTES")
    ]])
    await update.message.reply_text(
        f"📝 <b>Eslatmalaringiz: {len(notes)} ta</b>",
        reply_markup=markup,
        parse_mode="HTML",
    )



# ═══════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════

def main():
    TOKEN = cfg.BOT_TOKEN
    if not TOKEN or TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("❌ BOT_TOKEN topilmadi!")
        print("   .env faylga: BOT_TOKEN=your_token_here")
        print("   @BotFather dan token oling: https://t.me/BotFather")
        sys.exit(1)

    app = ApplicationBuilder().token(TOKEN).post_init(post_init).build()

    for cmd, fn in [
        ("start",        cmd_start),
        ("menu",         cmd_start),
        ("help",         cmd_help),
        ("list",         cmd_list),
        ("lesson",       cmd_lesson),
        ("progress",     cmd_progress),
        ("quiz",         cmd_quiz),
        ("search",       cmd_search),
        ("bookmarks",    cmd_bookmarks),
        ("leaderboard",  cmd_leaderboard),
        ("achievements", cmd_achievements),
        ("settings",     cmd_settings),
        ("about",        cmd_about),
        ("profile",      cmd_profile),
        ("daily",        cmd_daily),
        ("shop",         cmd_shop_cmd),
        ("notes",        cmd_notes),
    ]:
        app.add_handler(CommandHandler(cmd, fn))

    setup_admin(app, db)
    setup_reminders(app, db)
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    app.add_error_handler(on_error)

    log.info("🚀 Linux Master Bot v11.0 ULTIMATE PLUS ishga tushdi!")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
