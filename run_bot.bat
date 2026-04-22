@echo off
chcp 65001 > nul
title Linux Master Bot v7.0 PRO
color 0A

echo.
echo  =============================================
echo   🐧 LINUX MASTER BOT v7.0 PRO
echo  =============================================
echo.

REM .env fayl tekshirish
if not exist ".env" (
    echo  ❌ .env fayl topilmadi!
    echo  📝 .env.example nusxasini .env nomi bilan saqlang
    echo     va BOT_TOKEN ni to'ldiring.
    echo.
    pause
    exit /b 1
)

REM Python tekshirish
python --version >nul 2>&1
if errorlevel 1 (
    echo  ❌ Python topilmadi! python.org dan yuklab oling.
    pause
    exit /b 1
)

REM Requirements o'rnatish
echo  📦 Kutubxonalar tekshirilmoqda...
pip install -r requirements.txt -q

echo.
echo  ✅ Bot ishga tushmoqda...
echo  📖 To'xtatish uchun Ctrl+C bosing
echo.

python main.py

pause
