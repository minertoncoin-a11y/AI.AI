"""src/formatter.py — Telegram uchun ULTRA PREMIUM formatlar (v8)"""

# ═══════════════════════════════════════════════════════════
#  DIZAYN KONSTANTALARI
# ═══════════════════════════════════════════════════════════
SEP   = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
SUB   = "─────────────────────────────────"
THIN  = "· · · · · · · · · · · · · · · ·"
WAVE  = "〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰"
STAR  = "✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦"
DBL   = "══════════════════════════════════"


# ═══════════════════════════════════════════════════════════
#  PROGRESS BAR — 4 xil stil
# ═══════════════════════════════════════════════════════════

def fmt_progress_bar(pct: int, width: int = 14, style: str = "block") -> str:
    pct = max(0, min(100, int(pct)))
    filled = min(width, round(width * pct / 100))
    empty  = width - filled

    if style == "block":
        if pct == 100:
            return "█" * width + " ✅"
        if pct == 0:
            return "░" * width
        return "█" * filled + "░" * empty

    elif style == "circle":
        # ●●●●●○○○○○
        if pct == 100:
            return "●" * width + " ✅"
        if pct == 0:
            return "○" * width
        return "●" * filled + "○" * empty

    elif style == "square":
        # ■■■■■□□□□□
        if pct == 100:
            return "■" * width + " ✅"
        if pct == 0:
            return "□" * width
        return "■" * filled + "□" * empty

    return "█" * filled + "░" * empty


def fmt_mini_bar(pct: int) -> str:
    """Kichik inline progress: [████░░] 60%"""
    pct = max(0, min(100, int(pct)))
    w   = 10
    f   = round(w * pct / 100)
    bar = "█" * f + "░" * (w - f)
    return f"[{bar}] {pct}%"


# ═══════════════════════════════════════════════════════════
#  XP DARAJALAR — 8 bosqich
# ═══════════════════════════════════════════════════════════

def _xp_level(xp: int) -> tuple:
    """(icon, name, next_xp) qaytaradi"""
    if xp >= 3000: return "👑", "Grandmaster",  None
    if xp >= 1500: return "🏆", "Legend",        3000
    if xp >= 800:  return "💎", "Master",         1500
    if xp >= 400:  return "🥇", "Pro",             800
    if xp >= 200:  return "🥈", "Advanced",        400
    if xp >= 80:   return "🥉", "Intermediate",    200
    if xp >= 25:   return "🌟", "Beginner",         80
    return             "🌱", "Newcomer",            25


def fmt_xp_progress(xp: int) -> str:
    """XP → keyingi darajagacha progress"""
    icon, name, nxt = _xp_level(xp)
    if nxt is None:
        return f"{icon} <b>{name}</b>  ·  ⚡ <b>{xp}</b> XP  🏆 MAX DARAJA"
    need = nxt - xp
    pct  = int((xp / nxt) * 100)
    bar  = fmt_progress_bar(pct, 12, "square")
    return f"{icon} <b>{name}</b>  [{xp}/{nxt} XP]\n{bar}\n<i>+{need} XP → keyingi daraja</i>"


# ═══════════════════════════════════════════════════════════
#  STREAK VIZUAL
# ═══════════════════════════════════════════════════════════

def fmt_streak(days: int) -> str:
    if days == 0:    return "🌱 Streak yo'q — bugun boshlang!"
    if days < 3:     return f"🔥 {days} kun streak"
    if days < 7:     return f"🔥🔥 {days} kun streak — yaxshi!"
    if days < 14:    return f"🔥🔥🔥 {days} kun streak — zo'r!"
    if days < 30:    return f"⚡🔥 {days} kun streak — USTOZ!"
    return               f"👑🔥 {days} kun streak — LEGENDA!"


# ═══════════════════════════════════════════════════════════
#  DARS FORMATI — PREMIUM
# ═══════════════════════════════════════════════════════════

def fmt_lesson(title: str, body: str, num: int, total: int, pct: int) -> str:
    bar      = fmt_progress_bar(pct, 14)
    pct_txt  = f"<b>{pct}%</b>"
    header   = "🆕 Yangi" if pct == 0 else ("✅ Yakunlandi" if pct == 100 else f"📖 {pct}%")
    return (
        f"╔{'═'*32}╗\n"
        f"║  📘 <b>{title[:28].upper()}</b>\n"
        f"╚{'═'*32}╝\n"
        f"{SEP}\n\n"
        f"{body.strip()}\n\n"
        f"{SEP}\n"
        f"📖 <b>Dars {num}/{total}</b>  ·  {header}\n"
        f"{bar}  {pct_txt}"
    )


# ═══════════════════════════════════════════════════════════
#  ASOSIY MENYU BANNER
# ═══════════════════════════════════════════════════════════

def fmt_hub(topics: int, lessons: int, pct: int) -> str:
    bar   = fmt_progress_bar(pct, 16)
    stars = "⭐" * min(5, pct // 20) if pct > 0 else "—"
    return (
        f"╔══════════════════════════════════╗\n"
        f"║  🐧  <b>LINUX MASTER BOT</b>  v11.0   ║\n"
        f"║   <i>ULTIMATE PLUS — AI POWERED</i>   ║\n"
        f"╚══════════════════════════════════╝\n"
        f"📚 <b>{topics}</b> mavzu  ·  <b>{lessons}+</b> dars  ·  🤖 AI\n"
        f"{bar}  <b>{pct}%</b>  {stars}\n"
        f"{SEP}\n\n"
    )


# ═══════════════════════════════════════════════════════════
#  START XABARI — Yangi foydalanuvchi uchun
# ═══════════════════════════════════════════════════════════

def fmt_welcome(name: str) -> str:
    return (
        f"🐧 <b>LINUX MASTER BOT</b> — v11.0 ULTIMATE\n"
        f"{DBL}\n\n"
        f"👋 Xush kelibsiz, <b>{name}</b>!\n\n"
        f"Men Linux va IT bo'yicha <b>eng kuchli</b> o'qituvchi botman.\n\n"
        f"<b>📚 Nima o'rganasiz?</b>\n"
        f"{THIN}\n"
        f"🔰 Linux Asoslari — <b>150+ dars</b>\n"
        f"🔥 Linux Advanced — <b>10 dars (PRO)</b>\n"
        f"🌐 Tarmoq va SSH — <b>100+ dars</b>\n"
        f"🐳 Docker Mastery — <b>8 dars</b>\n"
        f"🐍 Python PRO — <b>8 dars</b>\n"
        f"⚙️ DevOps & CI/CD — <b>8 dars</b>\n"
        f"🗄️ SQL & Databases — <b>5 dars</b>\n"
        f"🌐 Networking PRO — <b>5 dars</b>\n"
        f"🔀 Git Mastery — <b>3 dars</b>\n"
        f"☁️ Cloud & AWS — <b>3 dars</b>\n"
        f"🛡️ Cybersecurity — <b>4 dars</b>\n"
        f"🌈 Frontend PRO — <b>3 dars</b>\n"
        f"☸️ Kubernetes PRO + Rust + Go va boshqalar!\n\n"
        f"<b>🎮 Tizim xususiyatlari:</b>\n"
        f"{THIN}\n"
        f"⚡ XP tizimi — 8 ta daraja (🌱 → 👑)\n"
        f"🔥 Streak — kundalik ketma-ket o'qish\n"
        f"🏆 Leaderboard — raqobat reytingi\n"
        f"🎖️ 35+ Achievement badge (yangi!)\n"
        f"🤖 AI yordamchi — har qanday IT savol\n"
        f"🎯 Quiz — mavzu bo'yicha test\n"
        f"🔖 Bookmark — darslarni saqlash\n\n"
        f"{DBL}\n"
        f"<b>Boshlash uchun tugmani bosing 👇</b>"
    )


def fmt_welcome_back(name: str, xp: int, streak: int, total_c: int, total_l: int) -> str:
    pct      = int(total_c / total_l * 100) if total_l else 0
    bar      = fmt_progress_bar(pct, 14)
    icon, lvl_name, _ = _xp_level(xp)
    streak_s = fmt_streak(streak)
    return (
        f"👋 Qaytib keldingiz, <b>{name}</b>!\n\n"
        f"{icon} <b>{lvl_name}</b>  ·  ⚡ <b>{xp}</b> XP\n"
        f"{streak_s}\n"
        f"{bar}  <b>{pct}%</b>  ({total_c}/{total_l} dars)\n"
    )


# ═══════════════════════════════════════════════════════════
#  PROGRESS SAHIFASI — TO'LIQ
# ═══════════════════════════════════════════════════════════

def fmt_progress_page(lessons_data: dict, uid_progress_fn, uid: int,
                      streak: int, xp: int) -> str:
    icon, lvl_name, nxt = _xp_level(xp)
    xp_bar   = fmt_xp_progress(xp)
    streak_s = fmt_streak(streak)

    lines = [
        f"📊 <b>O'RGANISH STATISTIKASI</b>\n{SEP}\n",
        f"{xp_bar}\n",
        f"🔥 {streak_s}\n",
        f"{SUB}\n📚 <b>MAVZULAR BO'YICHA PROGRESS:</b>\n{SUB}\n",
    ]

    total_c = total_l = done_topics = 0
    for topic, data in lessons_data.items():
        prog = uid_progress_fn(uid, topic)
        done = sum(1 for p in prog.values() if p.get("completed"))
        tot  = len(data["lessons"])
        pct  = int(done / tot * 100) if tot else 0
        total_c += done; total_l += tot
        if pct == 100: done_topics += 1

        bar  = fmt_progress_bar(pct, 12)
        icon_t = "✅" if pct == 100 else ("🔵" if pct >= 50 else ("🟡" if pct > 0 else "⭕"))
        title  = data["title"].split("(")[0].strip()
        lines.append(
            f"{icon_t} <b>{title}</b>\n"
            f"  {bar}  <b>{pct}%</b>  <i>({done}/{tot})</i>\n"
        )

    overall     = int(total_c / total_l * 100) if total_l else 0
    overall_bar = fmt_progress_bar(overall, 16)
    lines.append(f"{SEP}")
    lines.append(
        f"🎯 <b>Umumiy:</b> {overall_bar}  <b>{overall}%</b>\n"
        f"📖 <b>{total_c}/{total_l}</b> dars yakunlandi\n"
        f"✅ <b>{done_topics}</b> ta mavzu to'liq tugatildi"
    )
    if overall == 100:
        lines.append(f"\n{STAR}\n🏆 <b>BARCHA DARSLAR YAKUNLANDI!</b>\n👑 Siz GRANDMASTER darajasiga yetdingiz!\n{STAR}")
    return "\n".join(lines)


def fmt_progress_full(lessons_data, uid_progress_fn, uid, streak, xp):
    return fmt_progress_page(lessons_data, uid_progress_fn, uid, streak, xp)


# ═══════════════════════════════════════════════════════════
#  PROFIL SAHIFASI — ULTRA PREMIUM
# ═══════════════════════════════════════════════════════════

def fmt_profile(name: str, uid: int, xp: int, streak: int, rank_num,
                total_done: int, total_l: int, earned_count: int,
                all_badges_count: int, bms_count: int, lang: str,
                total_quizzes: int = 0, coins: int = 0, streak_freeze: int = 0) -> str:

    icon, lvl_name, nxt = _xp_level(xp)
    overall  = int(total_done / total_l * 100) if total_l else 0
    main_bar = fmt_progress_bar(overall, 16)
    xp_txt   = fmt_xp_progress(xp)
    streak_s = fmt_streak(streak)
    lang_lbl = {"uz": "🇺🇿 O'zbek", "ru": "🇷🇺 Русский", "en": "🇬🇧 English"}.get(lang, lang)
    rank_str = f"#{rank_num}" if rank_num else "?"

    # Badge progress
    badge_pct = int(earned_count / all_badges_count * 100) if all_badges_count else 0
    badge_bar = fmt_progress_bar(badge_pct, 10, "circle")

    # Daraja pog'onalar
    levels = [
        ("🌱", "Newcomer", 25),
        ("🌟", "Beginner", 80),
        ("🥉", "Intermediate", 200),
        ("🥈", "Advanced", 400),
        ("🥇", "Pro", 800),
        ("💎", "Master", 1500),
        ("🏆", "Legend", 3000),
        ("👑", "Grandmaster", None),
    ]
    # Qaysi darajada ekanligini topish
    current_idx = 0
    for i, (li, ln, lx) in enumerate(levels):
        if lx is None or xp < lx:
            current_idx = i
            break

    level_path = ""
    for i, (li, ln, lx) in enumerate(levels[:current_idx+2]):
        if i < current_idx:
            level_path += f"✅{li}"
        elif i == current_idx:
            level_path += f"▶️{li}"
        else:
            level_path += f"🔒{li}"
        if i < min(len(levels)-1, current_idx+1):
            level_path += "→"

    return (
        f"╔══════════════════════════════════╗\n"
        f"║  👤  <b>{name[:20]}</b>\n"
        f"║  🆔  <code>{uid}</code>\n"
        f"╚══════════════════════════════════╝\n\n"
        f"<b>🏅 DARAJA VA REYTING</b>\n{SUB}\n"
        f"{icon} <b>{lvl_name}</b>  ·  🏅 O'rin: <b>{rank_str}</b>\n"
        f"{xp_txt}\n\n"
        f"<b>📈 PROGRESS</b>\n{SUB}\n"
        f"{main_bar}  <b>{overall}%</b>\n"
        f"📖 <b>{total_done}/{total_l}</b> dars yakunlandi\n\n"
        f"<b>🎯 FAOLLIK</b>\n{SUB}\n"
        f"🔥 {streak_s}\n"
        f"🎯 Quizlar: <b>{total_quizzes}</b> ta\n\n"
        f"<b>🎖️ YUTUQLAR</b>\n{SUB}\n"
        f"{badge_bar}  <b>{earned_count}/{all_badges_count}</b> badge\n\n"
        f"<b>📊 DARAJA YO'LI</b>\n{SUB}\n"
        f"{level_path}\n\n"
        f"<b>⚙️ SOZLAMALAR</b>\n{SUB}\n"
        f"🌐 Til: {lang_lbl}  ·  🔖 Bookmarks: <b>{bms_count}</b>\n\n"
        f"<b>💰 BOYLIK</b>\n{SUB}\n"
        f"🪙 Coin: <b>{coins}</b>  ·  🧊 Streak Freeze: <b>{streak_freeze}</b>"
    )


# ═══════════════════════════════════════════════════════════
#  LEADERBOARD — PREMIUM
# ═══════════════════════════════════════════════════════════

def fmt_leaderboard(rows: list, uid: int, total_l: int, my_rank: dict) -> str:
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    lines  = [
        f"🏆 <b>LEADERBOARD — TOP 10</b>\n{DBL}\n"
        f"<i>Eng ko'p dars yakunlagan foydalanuvchilar</i>\n{SEP}\n"
    ]
    for i, r in enumerate(rows):
        pct  = int(r.get("total_done", 0) / total_l * 100) if total_l else 0
        bar  = fmt_mini_bar(pct)
        is_me = r["user_id"] == uid
        mark  = "  👈 <b>SEN</b>" if is_me else ""
        m     = medals[i] if i < len(medals) else f"<b>{i+1}.</b>"
        name  = r.get("first_name") or r.get("username") or f"#{r['user_id']}"
        xp    = r.get("xp", 0)
        lv_icon, lv_name, _ = _xp_level(xp)

        # "Sen" bo'lsa ajralib tursin
        prefix = "┌" if is_me else "│"
        lines.append(
            f"{prefix} {m} {lv_icon} <b>{name}</b>{mark}\n"
            f"│  {bar}  ⚡<b>{xp}</b> XP  ·  <i>{lv_name}</i>\n"
            f"└{'─'*32}\n"
        )
    if my_rank and my_rank.get("rank", 0) > 10:
        my_pct = int(my_rank.get("total_done", 0) / total_l * 100) if total_l else 0
        lines.append(
            f"\n{SEP}\n"
            f"📍 <b>Sening o'rning:</b>  #{my_rank['rank']}\n"
            f"   {fmt_mini_bar(my_pct)}"
        )
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════
#  ACHIEVEMENTS — PREMIUM
# ═══════════════════════════════════════════════════════════

def fmt_achievements(all_badges: list, earned_ids: set) -> str:
    earned_count = sum(1 for a in all_badges if a["id"] in earned_ids)
    total        = len(all_badges)
    pct          = int(earned_count / total * 100) if total else 0
    bar          = fmt_progress_bar(pct, 14, "circle")

    lines = [
        f"🎖️ <b>YUTUQLAR — ACHIEVEMENTS</b>\n{DBL}\n"
        f"{bar}  <b>{earned_count}/{total}</b>  (<b>{pct}%</b>)\n"
        f"{SEP}\n"
    ]

    # Guruhlash
    groups = {
        "dars": ("📚 DARS YUTUQLARI", []),
        "streak": ("🔥 STREAK YUTUQLARI", []),
        "xp": ("⚡ XP YUTUQLARI", []),
        "quiz": ("🎯 QUIZ YUTUQLARI", []),
        "other": ("🌟 BOSHQA", []),
    }
    for a in all_badges:
        aid = a["id"]
        if "lesson" in aid:     groups["dars"][1].append(a)
        elif "streak" in aid:   groups["streak"][1].append(a)
        elif "xp" in aid:       groups["xp"][1].append(a)
        elif "quiz" in aid:     groups["quiz"][1].append(a)
        else:                   groups["other"][1].append(a)

    for gkey, (gtitle, gitems) in groups.items():
        if not gitems: continue
        lines.append(f"\n<b>{gtitle}</b>")
        for a in gitems:
            has    = a["id"] in earned_ids
            icon   = a["icon"] if has else "🔒"
            name   = f"<b>{a['name']}</b>" if has else f"<i>{a['name']}</i>"
            status = " ✅" if has else ""
            lines.append(f"{icon} {name}{status}\n   <i>{a['description']}</i>")

    lines.append(f"\n{SEP}\n💡 <i>Dars o'qi va quiz yechib badge yig'!</i>")
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════
#  QUIZ SAHIFALARI
# ═══════════════════════════════════════════════════════════

def fmt_quiz_question(topic_label: str, idx: int, total: int, question: str) -> str:
    pct = int(idx / total * 100)
    bar = fmt_progress_bar(pct, 14)
    num_icons = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    num_icon  = num_icons[idx] if idx < len(num_icons) else f"{idx+1}."
    return (
        f"🎯 <b>{topic_label.upper()}</b>\n{SEP}\n\n"
        f"{num_icon} Savol <b>{idx+1}/{total}</b>\n"
        f"{bar}  <b>{pct}%</b>\n\n"
        f"❓ <b>{question}</b>"
    )


def fmt_quiz_result(topic_label: str, score: int, total: int, secs: int, xp_earned: int, perfect: bool = False) -> str:
    pct  = int(score / total * 100)
    bar  = fmt_progress_bar(pct, 16)

    if pct == 100:
        emoji, msg = "🏆", "MUKAMMAL! Barcha savollar to'g'ri!"
    elif pct >= 80:
        emoji, msg = "🎉", "AJOYIB NATIJA! Zo'r eding!"
    elif pct >= 60:
        emoji, msg = "👍", "YAXSHI! Davom eting!"
    elif pct >= 40:
        emoji, msg = "📚", "Yana o'qib, qayta urining!"
    else:
        emoji, msg = "💪", "Asoslarni takrorlab ko'ring!"

    stars    = "⭐" * (pct // 20)
    coin_txt = "\n🪙 Mukofot: <b>+15 🪙</b> coin (100% uchun!)" if perfect else ""
    return (
        f"{emoji} <b>QUIZ NATIJASI</b>\n{DBL}\n\n"
        f"📚 <b>{topic_label}</b>\n{SUB}\n\n"
        f"🎯 Natija: <b>{score}/{total}</b>  to'g'ri\n"
        f"{bar}  <b>{pct}%</b>  {stars}\n\n"
        f"⚡ Mukofot: <b>+{xp_earned}</b> XP qo'shildi{coin_txt}\n"
        f"⏱ Vaqt:  <b>{secs}</b> soniya\n\n"
        f"✨ <i>{msg}</i>"
    )


# ═══════════════════════════════════════════════════════════
#  SOZLAMALAR SAHIFASI
# ═══════════════════════════════════════════════════════════

def fmt_settings(lang: str, reminder_on: bool, streak: int, xp: int) -> str:
    labels   = {"uz": "🇺🇿 O'zbek", "ru": "🇷🇺 Русский", "en": "🇬🇧 English"}
    rem      = "✅ Yoqilgan" if reminder_on else "❌ O'chirilgan"
    icon, lvl_name, _ = _xp_level(xp)
    streak_s = fmt_streak(streak)
    xp_info  = fmt_xp_progress(xp)
    return (
        f"⚙️ <b>SOZLAMALAR</b>\n{DBL}\n\n"
        f"<b>🌐 TIL</b>\n{SUB}\n"
        f"Joriy: <b>{labels.get(lang, lang)}</b>\n\n"
        f"<b>🔔 ESLATMALAR</b>\n{SUB}\n"
        f"Kundalik: <b>{rem}</b>\n"
        f"<i>Har kuni ertalab o'qishga undash</i>\n\n"
        f"<b>📊 HISOBINGIZ</b>\n{SUB}\n"
        f"{xp_info}\n"
        f"🔥 {streak_s}\n"
    )




# ═══════════════════════════════════════════════════════════
#  YANGI QOSHILGAN: COIN / DAILY / SHOP FORMATLAR (v11)
# ═══════════════════════════════════════════════════════════

def fmt_coins_status(coins: int, freeze: int) -> str:
    bar_c = fmt_progress_bar(min(100, coins * 2), 10, "square")
    return (
        f"💰 <b>Coin:</b> <b>{coins}</b> 🪙  ·  🧊 Freeze: <b>{freeze}</b> ta\n"
        f"{bar_c}"
    )


def fmt_daily_challenge(topic_name: str, lesson_num: int, completed: bool,
                        today: str, dc_streak: int = 0) -> str:
    icon   = "✅" if completed else "🎯"
    status = "✅ <b>BAJARILDI!</b> +50 XP, +20 🪙" if completed else "⏳ <b>Bajarilmagan</b>"
    streak_line = f"🔥 Ketma-ket: <b>{dc_streak}</b> kun\n" if dc_streak > 0 else ""
    return (
        f"╔══════════════════════════════════╗\n"
        f"║  📅  <b>KUNLIK TOPSHIRIQ</b>          ║\n"
        f"╚══════════════════════════════════╝\n"
        f"📆 <b>{today}</b>  {icon}\n\n"
        f"📚 Mavzu: <b>{topic_name}</b>\n"
        f"📖 Dars: <b>{lesson_num}-dars</b>\n\n"
        f"Status: {status}\n"
        f"{streak_line}"
        f"{SUB}\n"
        f"💰 Mukofot: <b>+50 XP</b> + <b>+20 🪙</b>\n"
        f"<i>Har kuni yangi topshiriq!</i>"
    )


def fmt_shop(coins: int, freeze_count: int) -> str:
    return (
        f"╔══════════════════════════════════╗\n"
        f"║  🏪  <b>COIN DO'KON</b>               ║\n"
        f"╚══════════════════════════════════╝\n\n"
        f"💰 Sizda: <b>{coins}</b> 🪙 coin\n\n"
        f"<b>📦 MAHSULOTLAR:</b>\n"
        f"{SUB}\n\n"
        f"🧊 <b>Streak Freeze</b>  —  30 🪙\n"
        f"   <i>1 kun streak saqlanadi (2 kun o'tkazsa)</i>\n"
        f"   Sizda hozir: <b>{freeze_count}</b> ta\n\n"
        f"{SUB}\n"
        f"<b>💡 Coin qanday topiladi?</b>\n"
        f"• 📅 Kunlik topshiriq: <b>+20 🪙</b>\n"
        f"• 🎯 100% quiz natija: <b>+15 🪙</b>\n"
        f"• 📖 Har 10 dars: <b>+10 🪙</b>"
    )


def fmt_quiz_answer_correct(xp: int, remaining: int, total: int) -> str:
    return f"✅ <b>TO'G'RI!</b>  ⚡ <b>+{xp} XP</b>  🎉  ({remaining}/{total})"


def fmt_quiz_answer_wrong(correct_letter: str, correct_text: str, explanation: str = "") -> str:
    expl = f"\n\n💡 <i>{explanation}</i>" if explanation else ""
    return f"❌ <b>Noto'g'ri!</b>\n✅ To'g'ri: <b>{correct_letter}) {correct_text}</b>{expl}"


def fmt_topic_complete(topic_name: str, lesson_count: int, xp_earned: int) -> str:
    return (
        f"🎉 <b>MAVZU YAKUNLANDI!</b>\n"
        f"{DBL}\n\n"
        f"✅ <b>{topic_name}</b>\n"
        f"📖 {lesson_count} ta dars o'qildi\n"
        f"⚡ +{xp_earned} XP qo'shildi\n\n"
        f"🏆 Keyingi mavzuga o'ting!"
    )
