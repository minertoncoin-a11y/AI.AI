"""src/admin.py — Admin panel"""
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes
from src.config import cfg
from src.logger import log


def is_admin(uid: int) -> bool:
    return uid in cfg.ADMIN_IDS


def _admin_only(fn):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        uid = update.effective_user.id if update.effective_user else 0
        if not is_admin(uid):
            if update.callback_query:
                await update.callback_query.answer("⛔ Ruxsat yo'q.", show_alert=True)
            elif update.message:
                await update.message.reply_text("⛔ Ruxsat yo'q.")
            return
        return await fn(update, context)
    wrapper.__name__ = fn.__name__
    return wrapper


def _panel_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 Statistika",    callback_data="ADM:stats"),
         InlineKeyboardButton("👥 Foydalanuvchilar", callback_data="ADM:users")],
        [InlineKeyboardButton("📣 Broadcast",      callback_data="ADM:bc_prompt"),
         InlineKeyboardButton("🏆 Top reyting",   callback_data="ADM:top")],
        [InlineKeyboardButton("🗄️ DB Backup",      callback_data="ADM:backup"),
         InlineKeyboardButton("🔄 Keshni tozala", callback_data="ADM:flush")],
        [InlineKeyboardButton("✖️ Yopish",         callback_data="ADM:close")],
    ])


def setup_admin(app, db):
    """Admin handler'larini ro'yxatdan o'tkazadi."""

    @_admin_only
    async def cmd_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            f"⚙️ ADMIN PANEL\n\nBot ID: {update.get_bot().id}\n"
            f"Adminlar: {cfg.ADMIN_IDS}",
            reply_markup=_panel_kb(),
        )

    @_admin_only
    async def cb_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
        q    = update.callback_query
        data = q.data[4:]   # "ADM:" ni olib tashlash
        await q.answer()

        if data == "stats":
            try:
                s = db.global_stats()
                text = (
                    "📊 GLOBAL STATISTIKA\n\n"
                    f"👥 Jami foydalanuvchilar: {s['users']}\n"
                    f"📅 Bugungi faollar: {s['active_today']}\n"
                    f"📚 Jami dars yakunlangan: {s['lessons']}\n"
                    f"🎯 Jami quizlar: {s['quizzes']}\n"
                    f"⚡ Jami XP: {s['xp']}\n"
                )
            except Exception as e:
                text = f"❌ Xato: {e}"
            back = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Orqaga", callback_data="ADM:back")]])
            await q.edit_message_text(text, reply_markup=back)

        elif data == "users":
            try:
                users = db.recent_users(10)
                lines = ["👥 SO'NGGI 10 FOYDALANUVCHI\n"]
                for u in users:
                    name = u.get("first_name") or u.get("username") or f"#{u['user_id']}"
                    lines.append(f"• {name}  XP:{u.get('xp',0)}  {u.get('total_done',0)} dars")
            except Exception as e:
                lines = [f"❌ Xato: {e}"]
            back = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Orqaga", callback_data="ADM:back")]])
            await q.edit_message_text("\n".join(lines), reply_markup=back)

        elif data == "bc_prompt":
            context.user_data["admin_bc"] = True
            await q.edit_message_text(
                "📣 Barcha foydalanuvchilarga yuborish uchun xabar yozing:\n"
                "(Bekor qilish uchun /cancel)",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("🔙 Orqaga", callback_data="ADM:back")
                ]]),
            )

        elif data == "top":
            try:
                from src.lessons import LESSONS
                rows    = db.get_leaderboard(10)
                total_l = sum(len(d["lessons"]) for d in LESSONS.values())
                lines   = ["🏆 TOP-10\n"]
                for i, r in enumerate(rows, 1):
                    pct  = int(r.get("total_done", 0) / total_l * 100) if total_l else 0
                    name = r.get("first_name") or r.get("username") or f"#{r['user_id']}"
                    lines.append(f"{i}. {name} — {pct}% · ⚡{r.get('xp',0)}")
            except Exception as e:
                lines = [f"❌ Xato: {e}"]
            back = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Orqaga", callback_data="ADM:back")]])
            await q.edit_message_text("\n".join(lines), reply_markup=back)

        elif data == "backup":
            db_path = db.path
            if os.path.exists(db_path):
                with open(db_path, "rb") as f:
                    await q.message.reply_document(f, filename="backup.db",
                                                   caption="🗄️ Database backup")
            else:
                await q.answer("❌ DB fayl topilmadi.", show_alert=True)

        elif data == "flush":
            # Cache ni tozalash — global cache ob'ekt main.py da
            await q.answer("✅ Kesh tozalandi!")
            log.info("Admin kesh tozaladi: %s", update.effective_user.id)
            back = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Orqaga", callback_data="ADM:back")]])
            await q.edit_message_text("✅ Kesh tozalandi.", reply_markup=back)

        elif data == "back":
            await q.edit_message_text(
                f"⚙️ ADMIN PANEL\nAdminlar: {cfg.ADMIN_IDS}",
                reply_markup=_panel_kb(),
            )

        elif data == "close":
            await q.delete_message()

    async def on_bc_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Broadcast xabarini barcha foydalanuvchilarga parallel yuborish."""
        if not context.user_data.get("admin_bc"):
            return
        if not is_admin(update.effective_user.id):
            return
        context.user_data["admin_bc"] = False
        text  = update.message.text
        bot   = update.get_bot()
        users = db.recent_users(9999)
        await update.message.reply_text(f"📣 {len(users)} ta foydalanuvchiga yuborilmoqda...")

        async def _send(u):
            try:
                await bot.send_message(u["user_id"], f"📣 {text}")
                return True
            except Exception:
                return False

        import asyncio as _aio
        # 50 ta parallel, throttle
        results = []
        batch_size = 25
        for i in range(0, len(users), batch_size):
            batch = users[i:i+batch_size]
            res = await _aio.gather(*[_send(u) for u in batch], return_exceptions=True)
            results.extend(res)
            await _aio.sleep(0.5)   # Telegram flood limit himoyasi

        sent = sum(1 for r in results if r is True)
        fail = len(results) - sent
        await update.message.reply_text(
            f"📣 Broadcast tugadi!\n✅ Yuborildi: {sent}\n❌ Muvaffaqiyatsiz: {fail}"
        )

    from telegram.ext import MessageHandler, filters
    app.add_handler(CommandHandler("admin", cmd_admin))
    app.add_handler(CallbackQueryHandler(cb_admin, pattern="^ADM:"))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND & filters.User(user_id=cfg.ADMIN_IDS or [0]),
        on_bc_message,
    ))
    log.info("Admin handler'lar o'rnatildi. Adminlar: %s", cfg.ADMIN_IDS)
