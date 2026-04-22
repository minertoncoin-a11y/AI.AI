# 🐧 Linux Master Bot — v11.0 ULTIMATE PLUS

## 📊 Versiyalar taqqoslash

| Ko'rsatkich | v9 | v10 | **v11.0** |
|---|---|---|---|
| Mavzular | 30 | 30 | **30** |
| Darslar | 728 | 728 | **728** |
| Quiz savollari | 69 | 69 | **149 (+80!)** |
| Quiz mavzular | 11 | 11 | **30/30 (hammasi!)** |
| Achievements | 36 | 36 | **36** |
| Yangi formatter | ❌ | ❌ | **✅** |

## 🆕 v11.0 Yangiliklari

### 🎯 80 ta YANGI Quiz savoli (19 mavzuda)
Avval quiz yo'q edi — endi BARCHA 30 mavzuda quiz bor:
- `kubernetes` — 5 savol
- `rust_lang` — 5 savol  
- `golang` — 5 savol
- `microservices` — 5 savol
- `system_design` — 5 savol
- `graphql` — 4 savol
- `postgres_pro` — 5 savol
- `redis_deep` — 4 savol
- `terraform` — 4 savol
- `cicd_github` — 4 savol
- `pytorch_basics` — 4 savol
- `mlops_intro` — 4 savol
- `zero_trust` — 4 savol
- `devops_cicd` — 4 savol
- `networking_pro` — 4 savol
- `git_mastery` — 3 savol
- `cloud_aws` — 3 savol
- `security_pro` — 4 savol
- `web_frontend` — 3 savol

### 🎨 Yangi Formatter funksiyalar
- `fmt_daily_challenge()` — Kunlik topshiriq sahifasi
- `fmt_shop()` — Coin do'kon sahifasi  
- `fmt_coins_status()` — Coin holati bar
- `fmt_quiz_answer_correct/wrong()` — Quiz javob format
- `fmt_topic_complete()` — Mavzu yakunlash

### 💰 Profilga Coin va Freeze
- Profil sahifasida coin va freeze ko'rinadi

## 📋 O'rnatish

```bash
# 1. .env faylini to'ldiring
BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_key
ADMIN_IDS=your_telegram_id

# 2. Paketlar o'rnatish
pip install -r requirements.txt

# 3. Ishga tushirish
python main.py
# yoki Windows:
run_bot.bat
```

## 📁 Yangi fayl tuzilmasi
```
linux_master_v11/
├── main.py                  # Bot v11.0 ULTIMATE PLUS
├── src/
│   ├── achievements.py      # 36 badge
│   ├── ai_helper.py         # OpenAI GPT
│   ├── database.py          # SQLite + coins/daily/notes
│   ├── formatter.py         # UI + yangi formatlar
│   ├── lessons.py           # 500+ dars
│   ├── extended_lessons.py  # PRO mavzular
│   ├── new_topics.py        # 10 yangi mavzu
│   └── mega_quizzes.py      # 80 yangi quiz ← YANGI!
└── .env.example
```
