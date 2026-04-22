"""src/lessons.py — Barcha darslar va quizlar"""

ALL_LESSONS = [
    """<b>🔰 DARS 1: TERMINAL BILAN TANISHUV</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 BUYRUQLAR:</b>

<code>uname -a</code>  → Tizim haqida to'liq ma'lumot
<code>whoami</code>    → Hozirgi foydalanuvchi
<code>pwd</code>       → Joriy papka manzili
<code>ls</code>        → Fayllar ro'yxati
<code>ls -la</code>    → Barcha fayllarni batafsil
<code>date</code>      → Sana va vaqt
<code>uptime</code>    → Tizim ishlagan vaqti
<code>clear</code>     → Ekranni tozalash
<code>history</code>   → Buyruqlar tarixi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 AMALIY MASHQ:</b>

<pre>
# Terminalni oching va quyidagilarni bajaring:

# 1. Tizim ma'lumotini ko'ring
uname -a

# 2. Foydalanuvchi nomingizni tekshiring
whoami

# 3. Joriy papkani aniqlang
pwd

# 4. Fayllar ro'yxatini ko'ring
ls -la

# 5. Sana va vaqtni tekshiring
date

# 6. Tizim qancha vaqt ishlaganini bilib oling
uptime

# 7. Buyruqlar tarixini ko'ring
history
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi barcha buyruqlarni terminalda birma-bir bajaring!""",

    """<b>🔰 DARS 2: FAYL VA PAPKA OPERATSIYALARI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 BUYRUQLAR:</b>

<code>mkdir papka</code>        → Papka yaratish
<code>mkdir -p a/b/c</code>    → Ichma-ich papkalar
<code>touch fayl.txt</code>     → Fayl yaratish
<code>cp manba nusxa</code>     → Faylni nusxalash
<code>cp -r papka/ nusxa/</code> → Papkani nusxalash
<code>mv fayl /manzil/</code>   → Faylni ko'chirish
<code>mv eski.txt yangi.txt</code> → Nom o'zgartirish
<code>rm fayl.txt</code>        → Faylni o'chirish
<code>rm -r papka/</code>       → Papkani o'chirish
<code>cat fayl.txt</code>       → Faylni ko'rish

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 AMALIY MASHQ:</b>

<pre>
# 1. Uy papkangizda amaliyot papkasi yarating
mkdir ~/linux_amaliyot

# 2. Papkaga o'ting
cd ~/linux_amaliyot

# 3. 3 ta fayl yarating
touch fayl1.txt fayl2.txt fayl3.txt

# 4. Fayllarga matn yozing
echo "Birinchi fayl" > fayl1.txt
echo "Ikkinchi fayl" > fayl2.txt
echo "Uchinchi fayl" > fayl3.txt

# 5. Faylni nusxalang
cp fayl1.txt fayl1_nusxa.txt

# 6. Faylni ko'chiring
mv fayl2.txt /tmp/

# 7. Qolgan fayllarni ko'ring
ls -la

# 8. Orqaga qayting
cd ..

# 9. Papkani o'chiring
rm -r ~/linux_amaliyot
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'zingizning papka tuzilmangizni yarating va fayllar bilan ishlang!""",

    """<b>🔰 DARS 3: FAYL HUQUQLARI (PERMISSIONS)</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 HUQUQLAR JADVALI:</b>

┌───────┬─────────┬──────────┬────────────┐
│ BELGI │ MA'NOSI │ RAQAMI   │ TAVSIFI    │
├───────┼─────────┼──────────┼────────────┤
│ r     │ Read    │ 4        │ O'qish     │
│ w     │ Write   │ 2        │ Yozish     │
│ x     │ Execute │ 1        │ Bajarish   │
│ -     │ Yo'q    │ 0        │ Huquq yo'q │
└───────┴─────────┴──────────┴────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 TOIFALAR:</b>

<code>u</code> → User (egasi)
<code>g</code> → Group (guruhi)
<code>o</code> → Others (boshqalar)
<code>a</code> → All (hammasi)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 KOD MISOL:</b>

<pre>
# Fayl yaratish
touch skript.sh

# Huquqlarni ko'rish
ls -l skript.sh
# Natija: -rw-r--r-- 1 user user 0 Jan 1 12:00 skript.sh

# Raqamli usulda huquq berish
chmod 755 skript.sh   # rwxr-xr-x
chmod 644 skript.sh   # rw-r--r--
chmod 700 skript.sh   # rwx------
chmod 600 skript.sh   # rw-------

# Harfiy usulda huquq berish
chmod u+x skript.sh   # User ga execute qo'shish
chmod go-w skript.sh  # Group va Others dan write olish
chmod a+r skript.sh   # Hammaga read berish
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yangi fayl yarating va unga turli huquqlarni bering!""",

    """<b>🔰 DARS 4: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 4-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_4
cd ~/linux_dars_4

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_4
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 5: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 5-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_5
cd ~/linux_dars_5

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_5
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 6: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 6-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_6
cd ~/linux_dars_6

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_6
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 7: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 7-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_7
cd ~/linux_dars_7

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_7
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 8: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 8-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_8
cd ~/linux_dars_8

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_8
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 9: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 9-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_9
cd ~/linux_dars_9

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_9
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 10: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 10-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_10
cd ~/linux_dars_10

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_10
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 11: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 11-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_11
cd ~/linux_dars_11

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_11
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 12: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 12-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_12
cd ~/linux_dars_12

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_12
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 13: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 13-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_13
cd ~/linux_dars_13

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_13
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 14: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 14-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_14
cd ~/linux_dars_14

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_14
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 15: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 15-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_15
cd ~/linux_dars_15

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_15
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 16: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 16-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_16
cd ~/linux_dars_16

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_16
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 17: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 17-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_17
cd ~/linux_dars_17

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_17
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 18: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 18-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_18
cd ~/linux_dars_18

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_18
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 19: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 19-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_19
cd ~/linux_dars_19

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_19
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 20: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 20-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_20
cd ~/linux_dars_20

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_20
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 21: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 21-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_21
cd ~/linux_dars_21

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_21
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 22: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 22-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_22
cd ~/linux_dars_22

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_22
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 23: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 23-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_23
cd ~/linux_dars_23

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_23
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 24: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 24-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_24
cd ~/linux_dars_24

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_24
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 25: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 25-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_25
cd ~/linux_dars_25

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_25
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 26: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 26-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_26
cd ~/linux_dars_26

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_26
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 27: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 27-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_27
cd ~/linux_dars_27

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_27
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 28: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 28-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_28
cd ~/linux_dars_28

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_28
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 29: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 29-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_29
cd ~/linux_dars_29

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_29
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 30: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 30-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_30
cd ~/linux_dars_30

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_30
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 31: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 31-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_31
cd ~/linux_dars_31

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_31
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 32: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 32-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_32
cd ~/linux_dars_32

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_32
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 33: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 33-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_33
cd ~/linux_dars_33

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_33
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 34: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 34-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_34
cd ~/linux_dars_34

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_34
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 35: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 35-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_35
cd ~/linux_dars_35

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_35
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 36: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 36-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_36
cd ~/linux_dars_36

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_36
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 37: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 37-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_37
cd ~/linux_dars_37

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_37
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 38: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 38-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_38
cd ~/linux_dars_38

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_38
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 39: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 39-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_39
cd ~/linux_dars_39

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_39
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 40: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 40-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_40
cd ~/linux_dars_40

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_40
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 41: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 41-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_41
cd ~/linux_dars_41

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_41
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 42: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 42-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_42
cd ~/linux_dars_42

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_42
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 43: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 43-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_43
cd ~/linux_dars_43

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_43
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 44: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 44-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_44
cd ~/linux_dars_44

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_44
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 45: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 45-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_45
cd ~/linux_dars_45

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_45
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 46: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 46-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_46
cd ~/linux_dars_46

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_46
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 47: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 47-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_47
cd ~/linux_dars_47

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_47
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 48: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 48-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_48
cd ~/linux_dars_48

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_48
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 49: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 49-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_49
cd ~/linux_dars_49

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_49
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔰 DARS 50: AMALIY MASHQLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 50-DARS AMALIYOTI:</b>

<pre>
# 1. Yangi papka yarating
mkdir ~/linux_dars_50
cd ~/linux_dars_50

# 2. Bir nechta fayl yarating
for n in 1 2 3 4 5; do
    touch fayl_$n.txt
    echo "Bu $n-fayl" > fayl_$n.txt
done

# 3. Fayllarni ko'ring
ls -la

# 4. Fayllarni birlashtiring
cat fayl_*.txt > barcha.txt

# 5. Papkani tozalang
cd ..
rm -r linux_dars_50
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Yuqoridagi buyruqlarni bajaring va natijalarni tekshiring!""",

    """<b>🔍 DARS 51: GREP BILAN MATN QIDIRISH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 GREP BUYRUQLARI:</b>

<code>grep "so'z" fayl.txt</code>     → Qidirish
<code>grep -i "so'z" fayl.txt</code>  → Katta-kichik farqsiz
<code>grep -n "so'z" fayl.txt</code>  → Qator raqami bilan
<code>grep -c "so'z" fayl.txt</code>  → Nechta qator
<code>grep -v "so'z" fayl.txt</code>  → Teskari qidirish
<code>grep -r "so'z" ./</code>        → Rekursiv qidirish
<code>grep -w "so'z" fayl.txt</code>  → To'liq so'z
<code>grep -l "so'z" *.txt</code>     → Fayl nomlarini chiqarish

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 KOD MISOL:</b>

<pre>
# Test fayl yaratish
cat > test.txt << EOF
error: disk full
info: system ok
error: connection failed
warning: low memory
error: timeout
EOF

# Qidirish misollari
grep "error" test.txt
# Natija: error: disk full
#        error: connection failed
#        error: timeout

grep -c "error" test.txt
# Natija: 3

grep -n "error" test.txt
# Natija: 1:error: disk full
#        3:error: connection failed
#        5:error: timeout

grep -v "error" test.txt
# Natija: info: system ok
#        warning: low memory
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'zingizning log faylingizni yarating va grep bilan tahlil qiling!""",

    """<b>🔍 DARS 52: FIND BILAN FAYL QIDIRISH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 FIND BUYRUQLARI:</b>

<code>find . -name "*.txt"</code>      → Nom bo'yicha
<code>find . -type f</code>           → Faqat fayllar
<code>find . -type d</code>           → Faqat papkalar
<code>find . -size +10M</code>        → 10MB dan katta
<code>find . -size -1k</code>         → 1KB dan kichik
<code>find . -mtime -7</code>         → 7 kun ichida o'zgargan
<code>find . -mtime +30</code>        → 30 kundan eski
<code>find . -user ali</code>         → Ali ga tegishli
<code>find . -perm 755</code>         → Huquq bo'yicha

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 KOD MISOL:</b>

<pre>
# Turli fayllar yaratish
mkdir -p test_find
cd test_find
touch file1.txt file2.log script.sh data.txt
echo "test" > large.txt
dd if=/dev/zero of=10M.bin bs=1M count=10

# Qidirish misollari
find . -name "*.txt"
# Natija: ./file1.txt
#        ./data.txt

find . -type f
# Barcha fayllar

find . -size +1M
# Natija: ./10M.bin

find . -name "*.sh" -exec chmod +x {} \\\\;
# script.sh ga execute huquqi beradi

# Tozalash
cd ..
rm -r test_find
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Turli fayllar yarating va ularni find bilan qidiring!""",

    """<b>🔍 DARS 53: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 54: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 55: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 56: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 57: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 58: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 59: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 60: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 61: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 62: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 63: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 64: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 65: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 66: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 67: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 68: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 69: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 70: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 71: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 72: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 73: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 74: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 75: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 76: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 77: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 78: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 79: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 80: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 81: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 82: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 83: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 84: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 85: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 86: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 87: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 88: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 89: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 90: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 91: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 92: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 93: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 94: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 95: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 96: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 97: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 98: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 99: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>🔍 DARS 100: QIDIRISH AMALIYOTI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 GREP, FIND, AWK AMALIYOTI:</b>

<pre>
# grep bilan qidirish
grep -r "pattern" /path/to/dir

# find bilan fayl topish
find / -name "*.log" -mtime -7

# awk bilan matn qayta ishlash
awk '{print $1, $3}' file.txt

# sed bilan almashtirish
sed 's/old/new/g' file.txt

# Pipe bilan birlashtirish
ps aux | grep python | awk '{print $2}'
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
O'z tizimingizda shu buyruqlarni sinab ko'ring!""",

    """<b>⚙️ DARS 101: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 102: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 103: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 104: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 105: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 106: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 107: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 108: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 109: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 110: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 111: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 112: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 113: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 114: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 115: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 116: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 117: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 118: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 119: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 120: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 121: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 122: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 123: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 124: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 125: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 126: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 127: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 128: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 129: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 130: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 131: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 132: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 133: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 134: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 135: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 136: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 137: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 138: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 139: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 140: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 141: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 142: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 143: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 144: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 145: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 146: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 147: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 148: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 149: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 150: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 151: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 152: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 153: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 154: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 155: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 156: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 157: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 158: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 159: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 160: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 161: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 162: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 163: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 164: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 165: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 166: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 167: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 168: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 169: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 170: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 171: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 172: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 173: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 174: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 175: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 176: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 177: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 178: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 179: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 180: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 181: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 182: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 183: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 184: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 185: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 186: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 187: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 188: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 189: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 190: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 191: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 192: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 193: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 194: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 195: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 196: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 197: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 198: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 199: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>⚙️ DARS 200: TIZIM BOSHQARUVI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 SYSTEMD, XIZMATLAR, JARAYONLAR:</b>

<pre>
# Xizmatlarni boshqarish
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx

# Jarayonlarni ko'rish
ps aux | grep nginx
kill -9 PID

# Resurslarni monitoring
top
htop
vmstat 1 5
iostat -x 1 3

# Loglarni ko'rish
journalctl -u nginx -f
tail -f /var/log/syslog
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizda xizmatlar ro'yxatini ko'ring: systemctl list-units""",

    """<b>📜 DARS 201: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=201

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 202: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=202

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 203: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=203

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 204: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=204

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 205: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=205

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 206: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=206

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 207: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=207

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 208: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=208

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 209: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=209

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 210: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=210

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 211: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=211

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 212: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=212

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 213: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=213

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 214: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=214

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 215: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=215

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 216: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=216

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 217: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=217

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 218: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=218

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 219: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=219

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 220: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=220

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 221: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=221

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 222: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=222

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 223: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=223

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 224: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=224

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 225: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=225

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 226: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=226

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 227: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=227

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 228: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=228

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 229: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=229

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 230: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=230

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 231: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=231

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 232: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=232

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 233: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=233

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 234: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=234

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 235: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=235

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 236: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=236

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 237: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=237

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 238: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=238

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 239: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=239

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 240: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=240

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 241: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=241

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 242: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=242

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 243: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=243

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 244: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=244

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 245: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=245

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 246: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=246

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 247: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=247

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 248: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=248

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 249: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=249

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 250: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=250

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 251: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=251

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 252: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=252

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 253: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=253

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 254: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=254

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 255: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=255

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 256: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=256

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 257: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=257

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 258: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=258

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 259: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=259

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 260: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=260

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 261: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=261

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 262: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=262

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 263: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=263

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 264: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=264

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 265: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=265

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 266: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=266

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 267: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=267

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 268: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=268

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 269: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=269

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 270: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=270

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 271: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=271

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 272: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=272

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 273: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=273

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 274: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=274

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 275: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=275

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 276: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=276

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 277: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=277

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 278: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=278

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 279: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=279

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 280: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=280

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 281: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=281

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 282: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=282

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 283: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=283

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 284: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=284

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 285: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=285

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 286: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=286

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 287: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=287

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 288: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=288

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 289: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=289

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 290: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=290

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 291: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=291

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 292: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=292

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 293: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=293

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 294: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=294

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 295: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=295

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 296: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=296

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 297: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=297

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 298: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=298

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 299: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=299

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>📜 DARS 300: BASH SKRIPT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 BASH SCRIPTING AMALIYOTI:</b>

<pre>
#!/bin/bash
set -euo pipefail

# O'zgaruvchilar
NAME="Linux"
VERSION=300

# Funksiya
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Shart
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    log "OS: $NAME"
fi

# Sikl
for i in {1..5}; do
    log "Iteratsiya: $i"
    sleep 0.1
done

log "Script $VERSION tugadi!"
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Ushbu skriptni fayl sifatida saqlang va ishga tushiring!""",

    """<b>🌐 DARS 301: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 302: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 303: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 304: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 305: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 306: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 307: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 308: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 309: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 310: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 311: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 312: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 313: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 314: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 315: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 316: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 317: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 318: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 319: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 320: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 321: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 322: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 323: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 324: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 325: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 326: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 327: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 328: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 329: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 330: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 331: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 332: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 333: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 334: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 335: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 336: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 337: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 338: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 339: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 340: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 341: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 342: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 343: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 344: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 345: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 346: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 347: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 348: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 349: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 350: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 351: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 352: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 353: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 354: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 355: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 356: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 357: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 358: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 359: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 360: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 361: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 362: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 363: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 364: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 365: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 366: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 367: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 368: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 369: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 370: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 371: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 372: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 373: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 374: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 375: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 376: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 377: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 378: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 379: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 380: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 381: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 382: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 383: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 384: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 385: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 386: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 387: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 388: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 389: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 390: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 391: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 392: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 393: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 394: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 395: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 396: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 397: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 398: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 399: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🌐 DARS 400: TARMOQ VA XAVFSIZLIK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 TARMOQ BUYRUQLARI:</b>

<pre>
# Tarmoq ma'lumotlari
ip addr show
ip route show
ss -tulpn

# Firewall (ufw)
ufw status
ufw allow 22/tcp
ufw allow 80/tcp
ufw enable

# SSH ulanish
ssh -i key.pem user@server
ssh-keygen -t ed25519 -C "comment"

# Portlarni tekshirish
nmap -sV localhost
netstat -tulpn | grep LISTEN

# Trafik monitoring
tcpdump -i eth0 port 80
iftop -i eth0
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Tizimingizning ochiq portlarini ko'ring: ss -tulpn""",

    """<b>🚀 DARS 401: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:401 .
docker run -d -p 8080:80 myapp:401
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-401
git add . && git commit -m "dars 401"
git push origin feature/dars-401
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 402: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:402 .
docker run -d -p 8080:80 myapp:402
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-402
git add . && git commit -m "dars 402"
git push origin feature/dars-402
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 403: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:403 .
docker run -d -p 8080:80 myapp:403
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-403
git add . && git commit -m "dars 403"
git push origin feature/dars-403
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 404: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:404 .
docker run -d -p 8080:80 myapp:404
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-404
git add . && git commit -m "dars 404"
git push origin feature/dars-404
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 405: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:405 .
docker run -d -p 8080:80 myapp:405
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-405
git add . && git commit -m "dars 405"
git push origin feature/dars-405
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 406: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:406 .
docker run -d -p 8080:80 myapp:406
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-406
git add . && git commit -m "dars 406"
git push origin feature/dars-406
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 407: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:407 .
docker run -d -p 8080:80 myapp:407
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-407
git add . && git commit -m "dars 407"
git push origin feature/dars-407
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 408: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:408 .
docker run -d -p 8080:80 myapp:408
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-408
git add . && git commit -m "dars 408"
git push origin feature/dars-408
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 409: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:409 .
docker run -d -p 8080:80 myapp:409
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-409
git add . && git commit -m "dars 409"
git push origin feature/dars-409
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 410: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:410 .
docker run -d -p 8080:80 myapp:410
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-410
git add . && git commit -m "dars 410"
git push origin feature/dars-410
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 411: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:411 .
docker run -d -p 8080:80 myapp:411
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-411
git add . && git commit -m "dars 411"
git push origin feature/dars-411
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 412: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:412 .
docker run -d -p 8080:80 myapp:412
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-412
git add . && git commit -m "dars 412"
git push origin feature/dars-412
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 413: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:413 .
docker run -d -p 8080:80 myapp:413
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-413
git add . && git commit -m "dars 413"
git push origin feature/dars-413
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 414: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:414 .
docker run -d -p 8080:80 myapp:414
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-414
git add . && git commit -m "dars 414"
git push origin feature/dars-414
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 415: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:415 .
docker run -d -p 8080:80 myapp:415
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-415
git add . && git commit -m "dars 415"
git push origin feature/dars-415
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 416: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:416 .
docker run -d -p 8080:80 myapp:416
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-416
git add . && git commit -m "dars 416"
git push origin feature/dars-416
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 417: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:417 .
docker run -d -p 8080:80 myapp:417
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-417
git add . && git commit -m "dars 417"
git push origin feature/dars-417
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 418: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:418 .
docker run -d -p 8080:80 myapp:418
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-418
git add . && git commit -m "dars 418"
git push origin feature/dars-418
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 419: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:419 .
docker run -d -p 8080:80 myapp:419
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-419
git add . && git commit -m "dars 419"
git push origin feature/dars-419
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 420: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:420 .
docker run -d -p 8080:80 myapp:420
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-420
git add . && git commit -m "dars 420"
git push origin feature/dars-420
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 421: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:421 .
docker run -d -p 8080:80 myapp:421
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-421
git add . && git commit -m "dars 421"
git push origin feature/dars-421
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 422: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:422 .
docker run -d -p 8080:80 myapp:422
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-422
git add . && git commit -m "dars 422"
git push origin feature/dars-422
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 423: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:423 .
docker run -d -p 8080:80 myapp:423
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-423
git add . && git commit -m "dars 423"
git push origin feature/dars-423
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 424: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:424 .
docker run -d -p 8080:80 myapp:424
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-424
git add . && git commit -m "dars 424"
git push origin feature/dars-424
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 425: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:425 .
docker run -d -p 8080:80 myapp:425
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-425
git add . && git commit -m "dars 425"
git push origin feature/dars-425
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 426: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:426 .
docker run -d -p 8080:80 myapp:426
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-426
git add . && git commit -m "dars 426"
git push origin feature/dars-426
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 427: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:427 .
docker run -d -p 8080:80 myapp:427
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-427
git add . && git commit -m "dars 427"
git push origin feature/dars-427
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 428: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:428 .
docker run -d -p 8080:80 myapp:428
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-428
git add . && git commit -m "dars 428"
git push origin feature/dars-428
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 429: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:429 .
docker run -d -p 8080:80 myapp:429
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-429
git add . && git commit -m "dars 429"
git push origin feature/dars-429
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 430: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:430 .
docker run -d -p 8080:80 myapp:430
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-430
git add . && git commit -m "dars 430"
git push origin feature/dars-430
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 431: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:431 .
docker run -d -p 8080:80 myapp:431
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-431
git add . && git commit -m "dars 431"
git push origin feature/dars-431
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 432: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:432 .
docker run -d -p 8080:80 myapp:432
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-432
git add . && git commit -m "dars 432"
git push origin feature/dars-432
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 433: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:433 .
docker run -d -p 8080:80 myapp:433
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-433
git add . && git commit -m "dars 433"
git push origin feature/dars-433
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 434: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:434 .
docker run -d -p 8080:80 myapp:434
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-434
git add . && git commit -m "dars 434"
git push origin feature/dars-434
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 435: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:435 .
docker run -d -p 8080:80 myapp:435
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-435
git add . && git commit -m "dars 435"
git push origin feature/dars-435
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 436: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:436 .
docker run -d -p 8080:80 myapp:436
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-436
git add . && git commit -m "dars 436"
git push origin feature/dars-436
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 437: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:437 .
docker run -d -p 8080:80 myapp:437
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-437
git add . && git commit -m "dars 437"
git push origin feature/dars-437
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 438: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:438 .
docker run -d -p 8080:80 myapp:438
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-438
git add . && git commit -m "dars 438"
git push origin feature/dars-438
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 439: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:439 .
docker run -d -p 8080:80 myapp:439
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-439
git add . && git commit -m "dars 439"
git push origin feature/dars-439
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 440: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:440 .
docker run -d -p 8080:80 myapp:440
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-440
git add . && git commit -m "dars 440"
git push origin feature/dars-440
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 441: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:441 .
docker run -d -p 8080:80 myapp:441
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-441
git add . && git commit -m "dars 441"
git push origin feature/dars-441
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 442: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:442 .
docker run -d -p 8080:80 myapp:442
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-442
git add . && git commit -m "dars 442"
git push origin feature/dars-442
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 443: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:443 .
docker run -d -p 8080:80 myapp:443
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-443
git add . && git commit -m "dars 443"
git push origin feature/dars-443
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 444: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:444 .
docker run -d -p 8080:80 myapp:444
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-444
git add . && git commit -m "dars 444"
git push origin feature/dars-444
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 445: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:445 .
docker run -d -p 8080:80 myapp:445
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-445
git add . && git commit -m "dars 445"
git push origin feature/dars-445
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 446: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:446 .
docker run -d -p 8080:80 myapp:446
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-446
git add . && git commit -m "dars 446"
git push origin feature/dars-446
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 447: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:447 .
docker run -d -p 8080:80 myapp:447
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-447
git add . && git commit -m "dars 447"
git push origin feature/dars-447
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 448: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:448 .
docker run -d -p 8080:80 myapp:448
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-448
git add . && git commit -m "dars 448"
git push origin feature/dars-448
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 449: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:449 .
docker run -d -p 8080:80 myapp:449
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-449
git add . && git commit -m "dars 449"
git push origin feature/dars-449
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 450: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:450 .
docker run -d -p 8080:80 myapp:450
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-450
git add . && git commit -m "dars 450"
git push origin feature/dars-450
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 451: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:451 .
docker run -d -p 8080:80 myapp:451
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-451
git add . && git commit -m "dars 451"
git push origin feature/dars-451
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 452: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:452 .
docker run -d -p 8080:80 myapp:452
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-452
git add . && git commit -m "dars 452"
git push origin feature/dars-452
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 453: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:453 .
docker run -d -p 8080:80 myapp:453
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-453
git add . && git commit -m "dars 453"
git push origin feature/dars-453
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 454: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:454 .
docker run -d -p 8080:80 myapp:454
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-454
git add . && git commit -m "dars 454"
git push origin feature/dars-454
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 455: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:455 .
docker run -d -p 8080:80 myapp:455
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-455
git add . && git commit -m "dars 455"
git push origin feature/dars-455
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 456: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:456 .
docker run -d -p 8080:80 myapp:456
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-456
git add . && git commit -m "dars 456"
git push origin feature/dars-456
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 457: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:457 .
docker run -d -p 8080:80 myapp:457
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-457
git add . && git commit -m "dars 457"
git push origin feature/dars-457
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 458: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:458 .
docker run -d -p 8080:80 myapp:458
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-458
git add . && git commit -m "dars 458"
git push origin feature/dars-458
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 459: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:459 .
docker run -d -p 8080:80 myapp:459
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-459
git add . && git commit -m "dars 459"
git push origin feature/dars-459
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 460: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:460 .
docker run -d -p 8080:80 myapp:460
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-460
git add . && git commit -m "dars 460"
git push origin feature/dars-460
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 461: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:461 .
docker run -d -p 8080:80 myapp:461
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-461
git add . && git commit -m "dars 461"
git push origin feature/dars-461
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 462: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:462 .
docker run -d -p 8080:80 myapp:462
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-462
git add . && git commit -m "dars 462"
git push origin feature/dars-462
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 463: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:463 .
docker run -d -p 8080:80 myapp:463
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-463
git add . && git commit -m "dars 463"
git push origin feature/dars-463
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 464: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:464 .
docker run -d -p 8080:80 myapp:464
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-464
git add . && git commit -m "dars 464"
git push origin feature/dars-464
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 465: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:465 .
docker run -d -p 8080:80 myapp:465
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-465
git add . && git commit -m "dars 465"
git push origin feature/dars-465
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 466: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:466 .
docker run -d -p 8080:80 myapp:466
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-466
git add . && git commit -m "dars 466"
git push origin feature/dars-466
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 467: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:467 .
docker run -d -p 8080:80 myapp:467
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-467
git add . && git commit -m "dars 467"
git push origin feature/dars-467
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 468: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:468 .
docker run -d -p 8080:80 myapp:468
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-468
git add . && git commit -m "dars 468"
git push origin feature/dars-468
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 469: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:469 .
docker run -d -p 8080:80 myapp:469
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-469
git add . && git commit -m "dars 469"
git push origin feature/dars-469
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 470: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:470 .
docker run -d -p 8080:80 myapp:470
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-470
git add . && git commit -m "dars 470"
git push origin feature/dars-470
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 471: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:471 .
docker run -d -p 8080:80 myapp:471
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-471
git add . && git commit -m "dars 471"
git push origin feature/dars-471
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 472: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:472 .
docker run -d -p 8080:80 myapp:472
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-472
git add . && git commit -m "dars 472"
git push origin feature/dars-472
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 473: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:473 .
docker run -d -p 8080:80 myapp:473
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-473
git add . && git commit -m "dars 473"
git push origin feature/dars-473
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 474: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:474 .
docker run -d -p 8080:80 myapp:474
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-474
git add . && git commit -m "dars 474"
git push origin feature/dars-474
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 475: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:475 .
docker run -d -p 8080:80 myapp:475
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-475
git add . && git commit -m "dars 475"
git push origin feature/dars-475
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 476: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:476 .
docker run -d -p 8080:80 myapp:476
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-476
git add . && git commit -m "dars 476"
git push origin feature/dars-476
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 477: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:477 .
docker run -d -p 8080:80 myapp:477
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-477
git add . && git commit -m "dars 477"
git push origin feature/dars-477
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 478: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:478 .
docker run -d -p 8080:80 myapp:478
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-478
git add . && git commit -m "dars 478"
git push origin feature/dars-478
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 479: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:479 .
docker run -d -p 8080:80 myapp:479
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-479
git add . && git commit -m "dars 479"
git push origin feature/dars-479
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 480: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:480 .
docker run -d -p 8080:80 myapp:480
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-480
git add . && git commit -m "dars 480"
git push origin feature/dars-480
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 481: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:481 .
docker run -d -p 8080:80 myapp:481
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-481
git add . && git commit -m "dars 481"
git push origin feature/dars-481
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 482: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:482 .
docker run -d -p 8080:80 myapp:482
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-482
git add . && git commit -m "dars 482"
git push origin feature/dars-482
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 483: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:483 .
docker run -d -p 8080:80 myapp:483
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-483
git add . && git commit -m "dars 483"
git push origin feature/dars-483
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 484: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:484 .
docker run -d -p 8080:80 myapp:484
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-484
git add . && git commit -m "dars 484"
git push origin feature/dars-484
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 485: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:485 .
docker run -d -p 8080:80 myapp:485
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-485
git add . && git commit -m "dars 485"
git push origin feature/dars-485
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 486: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:486 .
docker run -d -p 8080:80 myapp:486
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-486
git add . && git commit -m "dars 486"
git push origin feature/dars-486
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 487: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:487 .
docker run -d -p 8080:80 myapp:487
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-487
git add . && git commit -m "dars 487"
git push origin feature/dars-487
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 488: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:488 .
docker run -d -p 8080:80 myapp:488
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-488
git add . && git commit -m "dars 488"
git push origin feature/dars-488
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 489: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:489 .
docker run -d -p 8080:80 myapp:489
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-489
git add . && git commit -m "dars 489"
git push origin feature/dars-489
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 490: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:490 .
docker run -d -p 8080:80 myapp:490
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-490
git add . && git commit -m "dars 490"
git push origin feature/dars-490
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 491: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:491 .
docker run -d -p 8080:80 myapp:491
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-491
git add . && git commit -m "dars 491"
git push origin feature/dars-491
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 492: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:492 .
docker run -d -p 8080:80 myapp:492
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-492
git add . && git commit -m "dars 492"
git push origin feature/dars-492
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 493: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:493 .
docker run -d -p 8080:80 myapp:493
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-493
git add . && git commit -m "dars 493"
git push origin feature/dars-493
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 494: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:494 .
docker run -d -p 8080:80 myapp:494
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-494
git add . && git commit -m "dars 494"
git push origin feature/dars-494
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 495: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:495 .
docker run -d -p 8080:80 myapp:495
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-495
git add . && git commit -m "dars 495"
git push origin feature/dars-495
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 496: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:496 .
docker run -d -p 8080:80 myapp:496
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-496
git add . && git commit -m "dars 496"
git push origin feature/dars-496
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 497: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:497 .
docker run -d -p 8080:80 myapp:497
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-497
git add . && git commit -m "dars 497"
git push origin feature/dars-497
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 498: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:498 .
docker run -d -p 8080:80 myapp:498
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-498
git add . && git commit -m "dars 498"
git push origin feature/dars-498
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 499: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:499 .
docker run -d -p 8080:80 myapp:499
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-499
git add . && git commit -m "dars 499"
git push origin feature/dars-499
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

    """<b>🚀 DARS 500: ILGOR LINUX</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💻 DOCKER, KUBERNETES, CI/CD:</b>

<pre>
# Docker
docker build -t myapp:500 .
docker run -d -p 8080:80 myapp:500
docker logs -f container_id
docker exec -it container_id bash

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# Kubernetes
kubectl get pods -A
kubectl describe pod myapp
kubectl logs -f pod/myapp

# Git CI/CD
git checkout -b feature/dars-500
git add . && git commit -m "dars 500"
git push origin feature/dars-500
</pre>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>✅ VAZIFA:</b>
Docker o'rnatilgan bo'lsa: docker run hello-world""",

]

LESSONS = {
    "asoslar":  {"title": "🔰 ASOSLAR (1-50)",    "lessons": ALL_LESSONS[0:50]},
    "qidirish": {"title": "🔍 QIDIRISH (51-100)",  "lessons": ALL_LESSONS[50:100]},
    "tizim":    {"title": "⚙️ TIZIM (101-200)",     "lessons": ALL_LESSONS[100:200]},
    "skript":   {"title": "📜 SKRIPT (201-300)",    "lessons": ALL_LESSONS[200:300]},
    "tarmoq":   {"title": "🌐 TARMOQ (301-400)",    "lessons": ALL_LESSONS[300:400]},
    "ilgor":    {"title": "🚀 ILG'OR (401-500)",   "lessons": ALL_LESSONS[400:500]},
}

QUIZZES = {
    "asoslar": [
        {"question": "Linux'da faylni nusxalash uchun qaysi buyruq?",
         "options": ["cp", "mv", "rm", "ls"], "correct": 0,
         "explanation": "cp (copy) buyrug'i fayllarni nusxalaydi"},
        {"question": "Joriy papkani ko'rsatadigan buyruq?",
         "options": ["pwd", "ls", "cd", "whoami"], "correct": 0,
         "explanation": "pwd (Print Working Directory) joriy papkani ko'rsatadi"},
        {"question": "Faylga bajarish huquqini beradigan buyruq?",
         "options": ["chmod +x", "chmod +r", "chmod +w", "chmod 444"], "correct": 0,
         "explanation": "chmod +x execute (bajarish) huquqini beradi"},
        {"question": "Fayl ichidan matn qidirish uchun?",
         "options": ["grep", "find", "locate", "search"], "correct": 0,
         "explanation": "grep (Global Regular Expression Print) matn qidiradi"},
        {"question": "Jarayonlarni ko'rish uchun?",
         "options": ["ps", "ls", "cd", "pwd"], "correct": 0,
         "explanation": "ps (Process Status) jarayonlarni ko'rsatadi"},
        {"question": "Disk bo'sh joyini ko'rish?",
         "options": ["df -h", "du -sh", "free -h", "ls -la"], "correct": 0,
         "explanation": "df -h (Disk Free human-readable) disk bo'sh joyini ko'rsatadi"},
        {"question": "Linux'da faylni o'chirish?",
         "options": ["rm", "del", "erase", "remove"], "correct": 0,
         "explanation": "rm (remove) buyrug'i fayllarni o'chiradi"},
        {"question": "Papka yaratish buyrug'i?",
         "options": ["mkdir", "mkfile", "newdir", "create"], "correct": 0,
         "explanation": "mkdir (make directory) papka yaratadi"},
    ],
    "qidirish": [
        {"question": "grep -r nima qiladi?",
         "options": ["Rekursiv qidiradi", "Teskari qidiradi", "Regex qidiradi", "Remote qidiradi"],
         "correct": 0, "explanation": "grep -r papka ichida rekursiv qidiradi"},
        {"question": "find buyrug'ida -name nima?",
         "options": ["Nom bo'yicha qidirish", "Yangi fayl", "Nomlash", "Node"],
         "correct": 0, "explanation": "find -name fayl nomini qidiradi"},
        {"question": "awk dasturida $1 nima?",
         "options": ["Birinchi ustun", "Birinchi satr", "Birinchi fayl", "Bir belgi"],
         "correct": 0, "explanation": "awk da $1 birinchi ustunni anglatadi"},
        {"question": "sed 's/a/b/g' nima qiladi?",
         "options": ["Hammasini almashtiradi", "Birinchisini almashtiradi", "Sana ko'rsatadi", "Saqlaydi"],
         "correct": 0, "explanation": "s/old/new/g - g=global, barcha uchrashuvlarni almashtiradi"},
        {"question": "pipe (|) operatori nima uchun?",
         "options": ["Natijani keyingi buyruqqa uzatish", "Fayl yaratish", "Ruxsat berish", "Qidirish"],
         "correct": 0, "explanation": "| (pipe) birinchi buyruq natijasini ikkinchisiga uzatadi"},
    ],
    "tizim": [
        {"question": "systemctl start nima qiladi?",
         "options": ["Xizmatni boshlaydi", "To'xtatadi", "O'chiradi", "Qayta boshlaydi"],
         "correct": 0, "explanation": "systemctl start xizmatni ishga tushiradi"},
        {"question": "journalctl -f nima ko'rsatadi?",
         "options": ["Real-time loglar", "Fayllar", "Jarayonlar", "Tarmoq"],
         "correct": 0, "explanation": "journalctl -f (follow) real-vaqt loglarini ko'rsatadi"},
        {"question": "kill -9 PID nima qiladi?",
         "options": ["Jarayonni kuchli to'xtatadi", "Qayta boshlaydi", "Pauza qiladi", "O'zgartiradi"],
         "correct": 0, "explanation": "kill -9 (SIGKILL) jarayonni to'liq to'xtatadi"},
        {"question": "top buyrug'i nima ko'rsatadi?",
         "options": ["Jarayon monitoringi", "Fayl tizimi", "Tarmoq trafigi", "Disk holati"],
         "correct": 0, "explanation": "top real-vaqt jarayon va resurs monitoringi"},
        {"question": "cron nima?",
         "options": ["Jadval tizimi", "Fayl arxivi", "Tarmoq demoni", "Paket menejeri"],
         "correct": 0, "explanation": "cron - Linux da jadval bo'yicha buyruq bajarish tizimi"},
    ],
    "skript": [
        {"question": "Bash skriptning birinchi qatori?",
         "options": ["#!/bin/bash", "#!bash", "/bin/bash", "bash!"],
         "correct": 0, "explanation": "Shebang #!/bin/bash interpretaterni ko'rsatadi"},
        {"question": "$? nima anglatadi?",
         "options": ["Oxirgi buyruq exit kodi", "O'zgaruvchi", "Argument", "PID"],
         "correct": 0, "explanation": "$? oxirgi bajarilgan buyruqning chiqish kodini saqlaydi"},
        {"question": "set -e nima qiladi?",
         "options": ["Xatoda to'xtaydi", "Echo yoqadi", "Exit qiladi", "Env ko'rsatadi"],
         "correct": 0, "explanation": "set -e skriptni xato yuzaga kelganda to'xtatadi"},
        {"question": "$(command) nima?",
         "options": ["Buyruq natijasini qo'yadi", "Ro'yxat", "Shart", "Funksiya"],
         "correct": 0, "explanation": "Command substitution - buyruq natijasini o'zgaruvchiga beradi"},
        {"question": "while true; do nima?",
         "options": ["Cheksiz sikl", "Bir marta bajari", "Shart tekshiradi", "Funksiya"],
         "correct": 0, "explanation": "while true cheksiz sikl — break bilan to'xtatiladi"},
    ],
    "tarmoq": [
        {"question": "ssh -i key.pem nima?",
         "options": ["SSH kalit fayli bilan kirish", "IP manzil", "Port ko'rsatish", "Interface"],
         "correct": 0, "explanation": "-i flag SSH private kalit faylini ko'rsatadi"},
        {"question": "ufw allow 80/tcp nima?",
         "options": ["80-portga TCP ruxsat beradi", "Portni bloklaydi", "UFW o'chiradi", "Test qiladi"],
         "correct": 0, "explanation": "ufw allow 80/tcp HTTP trafigi uchun 80-portni ochadi"},
        {"question": "ss -tulpn nima ko'rsatadi?",
         "options": ["Ochiq portlar va jarayonlar", "Trafik statistikasi", "DNS sozlamalari", "ARP jadvali"],
         "correct": 0, "explanation": "ss -tulpn TCP/UDP tinglayotgan portlar va jarayonlarni ko'rsatadi"},
        {"question": "ip addr show nima qiladi?",
         "options": ["Tarmoq interfeyslarini ko'rsatadi", "IP bloklaydi", "DNS sozlaydi", "Ping yuboradi"],
         "correct": 0, "explanation": "ip addr show barcha tarmoq interfeyslari va IP manzillarini ko'rsatadi"},
        {"question": "nmap -sV localhost nima?",
         "options": ["Port va servis versiyalarini skanerlaydi", "Tarmoqni bloklaydi", "VPN sozlaydi", "Virus qidiradi"],
         "correct": 0, "explanation": "nmap -sV portlarni va ularda ishlovchi servislar versiyasini topadi"},
    ],
    "ilgor": [
        {"question": "docker run -d nima qiladi?",
         "options": ["Fonda ishga tushiradi", "O'chiradi", "Debug qiladi", "Download qiladi"],
         "correct": 0, "explanation": "docker run -d (detached) konteynerni fon rejimida ishga tushiradi"},
        {"question": "kubectl get pods -A nima?",
         "options": ["Barcha namespace podlarini ko'rsatadi", "Pod yaratadi", "Pod o'chiradi", "Log ko'rsatadi"],
         "correct": 0, "explanation": "kubectl get pods -A barcha namespacelardagi podlarni ko'rsatadi"},
        {"question": "git rebase vs merge farqi?",
         "options": ["Rebase tarixni tuzatadi, merge birlashtiradi", "Ikkalasi bir xil", "Merge tarixni tuzatadi", "Rebase o'chiradi"],
         "correct": 0, "explanation": "git rebase commit tarixni qayta yozadi, merge esa birlashtiradi"},
        {"question": "Helm nima?",
         "options": ["Kubernetes paket menejeri", "Docker orkestratori", "CI/CD tizimi", "Monitoring vosita"],
         "correct": 0, "explanation": "Helm - Kubernetes uchun paket menejeri (chart-based deployment)"},
        {"question": "Terraform nima?",
         "options": ["Infrastructure as Code vositasi", "Konteyner runtime", "Monitoring sistema", "Load balancer"],
         "correct": 0, "explanation": "Terraform - infratuzilmani kod orqali boshqarish (IaC) vositasi"},
    ],
}

# Extended PRO darslar
try:
    from src.extended_lessons import ALL_EXTENDED
    LESSONS.update(ALL_EXTENDED)
except Exception as e:
    pass

# ── Extended QUIZZES ham qo'shish ─────────────────────────
try:
    from src.extended_lessons import EXTENDED_QUIZZES
    QUIZZES.update(EXTENDED_QUIZZES)
except Exception:
    pass
