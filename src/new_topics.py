"""src/new_topics.py — v9.0 ULTIMATE yangi mavzular (+300 dars)"""

NEW_TOPICS = {

    # ═══════════════════════════════════════════════════════════
    "linux_advanced": {
        "title": "🔥 Linux Advanced — Chuqur tizim (PRO)",
        "lessons": [
            """<b>🔥 DARS 1: KERNEL VA TIZIM ARXITEKTURASI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 KERNEL KOMPONENTLARI:</b>

<code>uname -r</code>           → Kernel versiyasi
<code>cat /proc/version</code>  → To'liq kernel info
<code>lsmod</code>              → Yuklangan modullar
<code>modinfo module_name</code> → Modul haqida
<code>modprobe module</code>    → Modulni yuklash
<code>rmmod module</code>       → Modulni o'chirish

<b>📌 KERNEL PARAMETRLARI:</b>

<code>sysctl -a</code>                → Barcha parametrlar
<code>sysctl net.ipv4.ip_forward</code> → IP forward holati
<code>sysctl -w vm.swappiness=10</code>  → Swappiness o'zgartirish

<b>💻 AMALIY MASHQ:</b>

<pre>
# Kernel va tizim haqida to'liq ma'lumot
uname -a
cat /proc/cpuinfo | head -20
cat /proc/meminfo | head -10
lsmod | head -15
sysctl vm.swappiness
</pre>

<b>✅ VAZIFA:</b> Kernel versiyangizni va yuklangan modullar sonini aniqlang!""",

            """<b>🔥 DARS 2: PROCESS MANAGEMENT (CHUQUR)</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 PROCESS MONITORING:</b>

<code>ps aux</code>              → Barcha jarayonlar
<code>ps -eo pid,ppid,cmd,%cpu,%mem</code> → Custom format
<code>pstree -a</code>          → Jarayon daraxti
<code>top -b -n1</code>         → Snapshot holati
<code>htop</code>               → Interaktiv monitor
<code>pidstat 1</code>          → PID statistikasi

<b>📌 SIGNAL VA BOSHQARISH:</b>

<code>kill -l</code>             → Signal ro'yxati
<code>kill -9 PID</code>        → Majburiy to'xtatish (SIGKILL)
<code>kill -15 PID</code>       → Yumshoq to'xtatish (SIGTERM)
<code>killall nginx</code>      → Nom bo'yicha o'ldirish
<code>pkill -u username</code>  → Foydalanuvchi jarayonlari

<b>📌 NICE VA PRIORITY:</b>

<code>nice -n 19 ./script.sh</code>   → Past prioritet
<code>renice -n 5 -p PID</code>       → Prioritetni o'zgartirish
<code>chrt -f 99 ./realtime</code>    → Real-time scheduling

<b>💻 AMALIY MASHQ:</b>

<pre>
# Eng ko'p CPU olayotgan 5 ta jarayon
ps aux --sort=-%cpu | head -6

# Memory bo'yicha top 5
ps aux --sort=-%mem | head -6

# Jarayon daraxti
pstree -ap | head -30
</pre>

<b>✅ VAZIFA:</b> PID 1 (init/systemd) jarayonining barcha child jarayonlarini ko'ring!""",

            """<b>🔥 DARS 3: CGROUPS VA NAMESPACES (KONTEYNER ASOSI)</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 CGROUPS v2:</b>

<code>ls /sys/fs/cgroup/</code>           → Cgroup hierarxiyasi
<code>cat /proc/self/cgroup</code>        → Joriy jarayon cgroup
<code>systemd-cgls</code>                → Systemd cgroup daraxti
<code>systemd-cgtop</code>               → Cgroup resurslari

<b>📌 NAMESPACES:</b>

<code>ls -la /proc/self/ns/</code>     → Namespace fayllari
<code>lsns</code>                      → Barcha namespace
<code>unshare --pid --fork bash</code> → Yangi PID namespace
<code>nsenter -t PID -p -m bash</code> → Namespace ichiga kirish

<b>📌 NAMESPACES TURLARI:</b>

• <b>pid</b>    — Jarayon ID izolyatsiyasi
• <b>net</b>    — Tarmoq izolyatsiyasi
• <b>mnt</b>    — Mount point izolyatsiyasi
• <b>uts</b>    — Hostname izolyatsiyasi
• <b>user</b>   — UID/GID izolyatsiyasi
• <b>ipc</b>    — IPC izolyatsiyasi

<b>💡 ESLATMA:</b> Docker, Podman, LXC — barchasi shu ikki mexanizmdan foydalanadi!

<b>✅ VAZIFA:</b> <code>unshare --pid --fork --mount-proc bash</code> bilan yangi PID namespace yarating!""",

            """<b>🔥 DARS 4: LINUX FAYL TIZIMI CHUQUR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 INODE VA HARDLINK:</b>

<code>ls -li</code>                  → Inode raqamlari
<code>stat fayl.txt</code>          → Fayl metadata
<code>ln manba hardlink</code>       → Hard link yaratish
<code>ln -s manba symlink</code>     → Soft link yaratish
<code>find / -inum 12345</code>      → Inode bo'yicha topish

<b>📌 EXT4 XUSUSIYATLARI:</b>

<code>tune2fs -l /dev/sda1</code>    → FS parametrlari
<code>dumpe2fs /dev/sda1</code>      → Batafsil ma'lumot
<code>e2fsck -f /dev/sda1</code>     → Fayl tizimini tekshirish

<b>📌 /PROC VA /SYS VIRTUAL FS:</b>

<code>cat /proc/loadavg</code>       → Tizim yuklanishi
<code>cat /proc/net/dev</code>       → Tarmoq interfeyslari
<code>cat /sys/block/sda/queue/scheduler</code> → I/O scheduler

<b>📌 LVM (LOGICAL VOLUME MANAGER):</b>

<code>pvs</code>  → Physical volumes
<code>vgs</code>  → Volume groups
<code>lvs</code>  → Logical volumes
<code>lvcreate -L 10G -n data vg0</code> → LV yaratish

<b>✅ VAZIFA:</b> Tizimingizda LVM bor-yo'qligini tekshiring va fayl tizimi ma'lumotlarini o'rganing!""",

            """<b>🔥 DARS 5: SYSTEMD CHUQUR TAHLIL</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 SYSTEMD ASOSIY BUYRUQLAR:</b>

<code>systemctl list-units</code>          → Barcha unitlar
<code>systemctl list-units --failed</code> → Muvaffaqiyatsiz
<code>systemctl status nginx</code>        → Servis holati
<code>journalctl -u nginx -f</code>        → Real-time log
<code>journalctl --since "1 hour ago"</code> → Vaqt bo'yicha

<b>📌 UNIT FAYL YARATISH:</b>

<pre>
# /etc/systemd/system/myapp.service
[Unit]
Description=Mening ilovam
After=network.target

[Service]
Type=simple
User=appuser
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 app.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
</pre>

<b>📌 TIMER (CRON O'RNIGA):</b>

<code>systemctl list-timers</code>        → Barcha timerlar
<code>OnCalendar=*-*-* 09:00:00</code>    → Har kuni ertalab
<code>OnBootSec=5min</code>              → Boot dan 5 min keyin

<b>✅ VAZIFA:</b> O'zingizning systemd service yarating va <code>enable</code> qiling!""",

            """<b>🔥 DARS 6: LINUX TARMOQ DIAGNOSTIKASI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 NETWORK MONITORING:</b>

<code>ss -tulpn</code>              → Ochiq portlar
<code>netstat -an | grep LISTEN</code> → Tinglovchi portlar
<code>ip -s link show eth0</code>   → Paket statistikasi
<code>nload eth0</code>            → Real-time bandwidth
<code>iftop</code>                 → Tarmoq foydalanuvchilari

<b>📌 TCPDUMP:</b>

<code>tcpdump -i eth0</code>                    → Barcha traffic
<code>tcpdump -i eth0 port 80</code>            → HTTP traffic
<code>tcpdump -i eth0 host 192.168.1.1</code>  → IP bo'yicha
<code>tcpdump -w capture.pcap</code>            → Faylga yozish

<b>📌 IP ROUTE VA FIREWALL:</b>

<code>ip route show</code>         → Yo'naltirish jadvali
<code>ip route add default via 192.168.1.1</code>
<code>iptables -L -n -v</code>     → Firewall qoidalar
<code>nft list ruleset</code>      → nftables qoidalar

<b>✅ VAZIFA:</b> <code>ss -tulpn</code> bilan 80, 443 portlarini kim tutib turganini aniqlang!""",

            """<b>🔥 DARS 7: LINUX XAVFSIZLIK (HARDENING)</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 SSH XAVFSIZLIGI:</b>

<pre>
# /etc/ssh/sshd_config
PermitRootLogin no          # Root kirish taqiq
PasswordAuthentication no   # Faqat kalit
PubkeyAuthentication yes    # RSA/ED25519
MaxAuthTries 3              # 3 urinish
AllowUsers deploy admin     # Faqat bu userlar
Port 2222                   # Portni o'zgartirish
</pre>

<b>📌 FAIL2BAN:</b>

<code>fail2ban-client status</code>      → Status
<code>fail2ban-client status sshd</code> → SSH jail
<code>fail2ban-client set sshd banip 1.2.3.4</code>

<b>📌 AUDIT LOG (auditd):</b>

<code>auditctl -w /etc/passwd -p wa</code>  → /etc/passwd kuzatuv
<code>ausearch -f /etc/passwd</code>        → Log qidirish
<code>aureport --summary</code>            → Umumiy hisobot

<b>📌 SELinux/AppArmor:</b>

<code>getenforce</code>              → SELinux holati
<code>setenforce 0</code>           → Permissive mode
<code>aa-status</code>              → AppArmor profillari

<b>✅ VAZIFA:</b> SSH konfigni xavfsizlashtiring va fail2ban o'rnating!""",

            """<b>🔥 DARS 8: DISK VA I/O OPTIMALLASHTIRISH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 DISK DIAGNOSTIKA:</b>

<code>smartctl -a /dev/sda</code>     → Disk salomatligi (SMART)
<code>iostat -x 1</code>             → I/O statistikasi (real-time)
<code>iotop</code>                   → Jarayonlar I/O
<code>lsblk -f</code>               → Fayl tizimi bo'yicha

<b>📌 DISK TESTI:</b>

<code>hdparm -tT /dev/sda</code>     → O'qish testi
<code>dd if=/dev/zero of=/tmp/test bs=1G count=1 oflag=direct</code>
<code>fio --name=test --rw=randread --size=1G</code>

<b>📌 I/O SCHEDULER:</b>

<code>cat /sys/block/sda/queue/scheduler</code>  → Joriy scheduler
<code>echo "mq-deadline" > /sys/block/sda/queue/scheduler</code>

• <b>none/noop</b>  — SSD uchun ideal
• <b>mq-deadline</b> — Umumiy maqsad
• <b>bfq</b>        — Desktop/multimedia

<b>📌 TMPFS (RAM DISK):</b>

<code>mount -t tmpfs -o size=1G tmpfs /mnt/ramdisk</code>

<b>✅ VAZIFA:</b> <code>iostat -x 1 5</code> bilan disk I/O ni monitoring qiling!""",

            """<b>🔥 DARS 9: LINUX MEMORY MANAGEMENT</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 MEMORY TAHLIL:</b>

<code>free -h</code>                    → RAM holati
<code>cat /proc/meminfo</code>          → Batafsil memory
<code>vmstat 1 5</code>                → Virtual memory stat
<code>smem -t -p</code>               → Jarayon memory
<code>pmap -x PID</code>              → Jarayon memory map

<b>📌 SWAP BOSHQARISH:</b>

<code>swapon --show</code>             → Swap haqida
<code>dd if=/dev/zero of=/swapfile bs=1G count=4</code>
<code>mkswap /swapfile</code>
<code>swapon /swapfile</code>

<b>📌 OOM KILLER:</b>

<code>cat /proc/PID/oom_score</code>    → OOM ball
<code>echo -17 > /proc/PID/oom_adj</code> → OOM taqiqlash

<b>📌 HUGE PAGES:</b>

<code>grep HugePages /proc/meminfo</code>
<code>echo 512 > /proc/sys/vm/nr_hugepages</code>

<b>📌 MEMORY OPTIMALLASHTIRISH:</b>

<code>echo 3 > /proc/sys/vm/drop_caches</code>  → Keshni tozalash
<code>sysctl vm.swappiness=10</code>            → Kamroq swap

<b>✅ VAZIFA:</b> <code>smem -t -p</code> bilan eng ko'p memory ishlatayotgan jarayonni toping!""",

            """<b>🔥 DARS 10: SHELL SCRIPTING MASTERY</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 KUCHLI BASH TEXNIKALAR:</b>

<pre>
#!/bin/bash
set -euo pipefail  # Xato bo'lsa to'xta

# Array boshqarish
arr=(one two three)
echo "${arr[@]}"       # Barchasi
echo "${#arr[@]}"      # Uzunlik
echo "${arr[0]}"       # Birinchi

# Assoc array (hashtable)
declare -A map
map[key]="value"
echo "${map[key]}"

# Here document
cat <<EOF
Ko'p satrli
matn
EOF
</pre>

<b>📌 PROCESS SUBSTITUTION:</b>

<pre>
# diff ikkita buyruq natijasi
diff <(ls dir1) <(ls dir2)

# Parallel ishlov berish
while read line; do
    process "$line" &
done < input.txt
wait  # Hammasini kut
</pre>

<b>📌 TRAP VA SIGNAL:</b>

<pre>
cleanup() { rm -f /tmp/tmpfile; }
trap cleanup EXIT INT TERM
</pre>

<b>📌 REGEX VA SED/AWK:</b>

<code>sed -n '/pattern/p' fayl</code>    → Pattern satrlar
<code>awk '{sum+=$2} END{print sum}'</code> → Yig'indi
<code>awk -F: '$3>1000{print $1}' /etc/passwd</code>

<b>✅ VAZIFA:</b> Backup skript yozing: papkani arxivlab, 7 kundan eski backup'larni o'chirsin!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "docker_mastery": {
        "title": "🐳 Docker Mastery — Konteyner SAN'ATI",
        "lessons": [
            """<b>🐳 DARS 1: DOCKER ARXITEKTURASI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 ASOSIY KOMPONENTLAR:</b>

• <b>Docker Daemon</b> (dockerd) — Asosiy server
• <b>Docker CLI</b> — Buyruq qatori
• <b>Docker Registry</b> — Image ombori (Hub, ECR, GCR)
• <b>containerd</b> — Container runtime
• <b>runc</b> — OCI container runner

<b>📌 IMAGE VA CONTAINER FARQI:</b>

• <b>Image</b>  → O'zgarmas qatlam (layers), blueprint
• <b>Container</b> → Ishayotgan image instansiyasi

<b>📌 ASOSIY BUYRUQLAR:</b>

<code>docker images</code>           → Mahalliy imagelar
<code>docker ps -a</code>           → Barcha containerlar
<code>docker pull nginx:alpine</code> → Image yuklash
<code>docker run -d -p 80:80 nginx</code>
<code>docker exec -it CONT bash</code> → Container ichiga

<b>💻 AMALIY MASHQ:</b>

<pre>
# Nginx ishga tushirish
docker run -d --name web \
  -p 8080:80 \
  -v $(pwd)/html:/usr/share/nginx/html \
  nginx:alpine

# Container loglarini ko'rish
docker logs -f web

# Container ichiga kirish
docker exec -it web sh
</pre>

<b>✅ VAZIFA:</b> Nginx containerini ishga tushirib, brauzerda <code>localhost:8080</code> ni oching!""",

            """<b>🐳 DARS 2: DOCKERFILE — PRO YOZISH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 DOCKERFILE DIREKTIVALARI:</b>

<pre>
# ── Multi-stage build ──────────────────────
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# ── Production stage ───────────────────────
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
</pre>

<b>📌 YAXSHI AMALIYOTLAR:</b>

✅ Kichik base image (alpine, distroless)
✅ Layer keshini optimallashtirish
✅ Package.json ni avval nusxa (deps kesh)
✅ Non-root user ishlatish
✅ .dockerignore yaratish

<b>📌 .dockerignore:</b>

<pre>
node_modules
.git
*.log
.env
__pycache__
</pre>

<b>📌 BUILD VA INSPECT:</b>

<code>docker build -t myapp:v1 .</code>
<code>docker history myapp:v1</code>    → Qatlamlar
<code>docker inspect myapp:v1</code>   → JSON config
<code>dive myapp:v1</code>            → Layer tahlil (tool)

<b>✅ VAZIFA:</b> Python Flask ilovasi uchun multi-stage Dockerfile yozing!""",

            """<b>🐳 DARS 3: DOCKER COMPOSE — MIKROSERVISLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 DOCKER COMPOSE V2:</b>

<pre>
# docker-compose.yml
version: '3.9'
services:
  web:
    build: .
    ports: ["8000:8000"]
    environment:
      - DATABASE_URL=postgresql://user:pass@db/mydb
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    networks: [backend]

  db:
    image: postgres:15-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks: [backend]

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redisdata:/data
    networks: [backend]

volumes:
  pgdata:
  redisdata:

networks:
  backend:
    driver: bridge
</pre>

<b>📌 COMPOSE BUYRUQLAR:</b>

<code>docker compose up -d</code>         → Fon rejimida ishga tushirish
<code>docker compose logs -f web</code>   → Loglar
<code>docker compose down -v</code>       → To'xtatib, volume o'chirish
<code>docker compose scale web=3</code>   → Masshtablash

<b>✅ VAZIFA:</b> Web + PostgreSQL + Redis uchun compose fayl yozing!""",

            """<b>🐳 DARS 4: DOCKER NETWORKING</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 NETWORK TURLARI:</b>

• <b>bridge</b>  — Default, izolyatsiyalangan
• <b>host</b>   — Host tarmoqi (port mapping kerak emas)
• <b>none</b>   — Tarmoqsiz izolyatsiya
• <b>overlay</b> — Swarm uchun (ko'p host)
• <b>macvlan</b> — Container'ga MAC manzil

<b>📌 TARMOQ BOSHQARISH:</b>

<code>docker network ls</code>                    → Tarmoqlar ro'yxati
<code>docker network create mynet</code>          → Yangi tarmoq
<code>docker network inspect bridge</code>        → Batafsil
<code>docker network connect mynet container1</code>

<b>📌 DNS RESOLUTION:</b>

<pre>
# Bir tarmoqdagi containerlar ismi bilan muloqot:
docker run -d --name web --network mynet nginx
docker run --rm --network mynet alpine \
  wget -qO- http://web  # Container nomi = DNS
</pre>

<b>📌 PORT BINDING:</b>

<code>-p 8080:80</code>       → Barcha interfeys
<code>-p 127.0.0.1:8080:80</code> → Faqat localhost
<code>-p ::8080:80</code>     → Faqat IPv6

<b>✅ VAZIFA:</b> Ikki container yarating, bir tarmoqqa ulang va bir-birini ping qiling!""",

            """<b>🐳 DARS 5: DOCKER VOLUMES VA SAQLASH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 VOLUME TURLARI:</b>

• <b>Named volume</b>  → Docker boshqaradi (<code>-v pgdata:/var/lib/pgsql</code>)
• <b>Bind mount</b>   → Host papkasi (<code>-v /host/path:/container/path</code>)
• <b>tmpfs</b>        → RAM'da vaqtinchalik

<b>📌 VOLUME BUYRUQLAR:</b>

<code>docker volume ls</code>              → Barcha volumelar
<code>docker volume create mydata</code>  → Yaratish
<code>docker volume inspect mydata</code> → Batafsil
<code>docker volume rm mydata</code>      → O'chirish
<code>docker volume prune</code>          → Ishlatilmaganlarni tozalash

<b>📌 BACKUP VA RESTORE:</b>

<pre>
# Volume backup
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/pgdata.tar.gz /data

# Volume restore
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/pgdata.tar.gz -C /
</pre>

<b>📌 VOLUME PERMISSION:</b>

<pre>
# Non-root user uchun permission berish
RUN chown -R appuser:appuser /data
USER appuser
</pre>

<b>✅ VAZIFA:</b> PostgreSQL container uchun volume yarating va backup qiling!""",

            """<b>🐳 DARS 6: DOCKER SECURITY</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 XAVFSIZLIK ASOSLARI:</b>

<pre>
# Non-root user yaratish
FROM alpine:3.18
RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup
USER appuser
</pre>

<b>📌 READ-ONLY FILESYSTEM:</b>

<code>docker run --read-only nginx</code>
<code>docker run --tmpfs /tmp nginx</code>  → Faqat /tmp yoziladi

<b>📌 CAPABILITIES CHEKLASH:</b>

<code>--cap-drop=ALL --cap-add=NET_BIND_SERVICE</code>

<b>📌 SECCOMP VA APPARMOR:</b>

<code>--security-opt seccomp=/path/to/profile.json</code>
<code>--security-opt apparmor=docker-default</code>

<b>📌 IMAGE SKANERLASH:</b>

<code>docker scout cves nginx:latest</code>   → CVE skaneri
<code>trivy image nginx:latest</code>        → Trivy skaneri
<code>snyk container test nginx</code>       → Snyk

<b>📌 SECRETS BOSHQARISH:</b>

<pre>
# Docker secrets (Swarm)
echo "mypassword" | docker secret create db_pass -

# Compose'da
secrets:
  db_pass:
    external: true
</pre>

<b>✅ VAZIFA:</b> Trivy o'rnatib, biror image'ni CVE skanidan o'tkazing!""",

            """<b>🐳 DARS 7: DOCKER REGISTRY VA IMAGE BOSHQARISH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 DOCKER HUB:</b>

<code>docker login</code>
<code>docker tag myapp:v1 username/myapp:v1</code>
<code>docker push username/myapp:v1</code>
<code>docker pull username/myapp:v1</code>

<b>📌 MAHALLIY REGISTRY:</b>

<pre>
# Registry ishga tushirish
docker run -d -p 5000:5000 \
  --restart=always \
  --name registry \
  -v /opt/registry:/var/lib/registry \
  registry:2

# Push
docker tag myapp localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1
</pre>

<b>📌 IMAGE OPTIMIZATSIYA:</b>

<code>docker images --format "table {{.Repository}}\t{{.Size}}"</code>
<code>docker image prune -a</code>  → Ishlatilmaganlarni tozalash

<b>📌 MULTI-ARCH IMAGE:</b>

<pre>
docker buildx create --use
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myapp:latest --push .
</pre>

<b>✅ VAZIFA:</b> Mahalliy registry o'rnatib, o'z imageingizni push qiling!""",

            """<b>🐳 DARS 8: DOCKER SWARM (KLASTER)</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 SWARM BOSHLASH:</b>

<code>docker swarm init --advertise-addr <IP></code>  → Manager
<code>docker swarm join --token TOKEN IP:2377</code>  → Worker
<code>docker node ls</code>                           → Node ro'yxati

<b>📌 SERVICE YARATISH:</b>

<code>docker service create --name web --replicas 3 -p 80:80 nginx</code>
<code>docker service ls</code>              → Servicelar
<code>docker service ps web</code>          → Task holatlari
<code>docker service scale web=5</code>     → Masshtablash

<b>📌 ROLLING UPDATE:</b>

<pre>
docker service update \
  --image nginx:latest \
  --update-parallelism 2 \
  --update-delay 10s \
  web
</pre>

<b>📌 OVERLAY NETWORK:</b>

<pre>
docker network create \
  --driver overlay \
  --attachable \
  myoverlay

docker service create \
  --network myoverlay \
  --name api myapp
</pre>

<b>✅ VAZIFA:</b> Swarm init qilib, 3 replika bilan nginx service yarating!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "python_pro": {
        "title": "🐍 Python PRO — Ilg'or dasturlash",
        "lessons": [
            """<b>🐍 DARS 1: PYTHON ASYNC/AWAIT MASTERY</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 EVENT LOOP ARXITEKTURASI:</b>

<pre>
import asyncio

# Async funksiya
async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)  # I/O simulatsiya
    return f"Data from {url}"

# Parallel bajarish
async def main():
    # Ketma-ket (SEKIN)
    r1 = await fetch_data("url1")
    r2 = await fetch_data("url2")  # 2 soniya

    # Parallel (TEZKOR!)
    r1, r2 = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2"),
    )  # ~1 soniya

asyncio.run(main())
</pre>

<b>📌 ASYNCIO PRIMITIVES:</b>

<pre>
# Lock
lock = asyncio.Lock()
async with lock:
    # kritik bo'lim

# Semaphore (max parallellik)
sem = asyncio.Semaphore(10)
async with sem:
    await make_request()

# Queue
q = asyncio.Queue()
await q.put(item)
item = await q.get()
</pre>

<b>✅ VAZIFA:</b> 10 ta URL ni async bilan parallel fetch qilib, vaqtni o'lchang!""",

            """<b>🐍 DARS 2: PYTHON DEKORATORLAR — CHUQUR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 DEKORATOR ANATOMIYASI:</b>

<pre>
import functools, time

def timer(func):
    @functools.wraps(func)  # metadata saqlash
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {end-start:.3f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
</pre>

<b>📌 PARAMETRLI DEKORATOR:</b>

<pre>
def retry(max_attempts=3, delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=5, delay=0.5)
def unstable_api_call():
    ...
</pre>

<b>📌 CLASS DEKORATOR:</b>

<pre>
class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Cache
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)
</pre>

<b>✅ VAZIFA:</b> Rate limiter dekorator yozing: funksiya 1 daqiqada max N marta chaqirilsin!""",

            """<b>🐍 DARS 3: PYTHON GENERATORS VA ITERATORLAR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 GENERATOR NIMA?</b>

<pre>
# Oddiy funksiya — barcha qiymat xotirada
def get_squares(n):
    return [i**2 for i in range(n)]  # O(n) xotira

# Generator — lazy, bir-bitta
def gen_squares(n):
    for i in range(n):
        yield i**2  # O(1) xotira!

# Generator expression
squares = (i**2 for i in range(1_000_000))
</pre>

<b>📌 KUCHLI GENERATOR TEXNIKALAR:</b>

<pre>
# Pipeline (chained generators)
def read_file(path):
    with open(path) as f:
        yield from f  # har qator

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

def parse(lines):
    for line in lines:
        yield line.split("|")

# Ishlatish — xotira samarali!
lines = read_file("big.log")
errors = filter_errors(lines)
parsed = parse(errors)

for row in parsed:
    process(row)
</pre>

<b>📌 SEND VA THROW (COROUTINE):</b>

<pre>
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)       # Prime
gen.send(10)    # 10
gen.send(20)    # 30
</pre>

<b>✅ VAZIFA:</b> 1 GB log faylni xotira samarali o'qib, ERROR satrlarni hisoblang!""",

            """<b>🐍 DARS 4: PYTHON METACLASS VA DESCRIPTOR</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 METACLASS:</b>

<pre>
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "connected"

db1 = Database()
db2 = Database()
assert db1 is db2  # True — bitta instance
</pre>

<b>📌 DESCRIPTOR PROTOCOL:</b>

<pre>
class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{self.name}: musbat butun son")
        obj.__dict__[self.name] = value

class Product:
    price = Validator()
    quantity = Validator()

p = Product()
p.price = 100   # OK
p.price = -5    # ValueError!
</pre>

<b>✅ VAZIFA:</b> ORM'ga o'xshash: model field'larni descriptor bilan yasang!""",

            """<b>🐍 DARS 5: PYTHON PERFORMANCE OPTIMALLASHTIRISH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 PROFILING:</b>

<pre>
import cProfile, pstats

with cProfile.Profile() as pr:
    your_function()

stats = pstats.Stats(pr)
stats.sort_stats("cumulative")
stats.print_stats(10)
</pre>

<b>📌 MEMORY OPTIMALLASHTIRISH:</b>

<pre>
# __slots__ — dict o'rniga
class Point:
    __slots__ = ['x', 'y']  # ~50% kam xotira
    def __init__(self, x, y):
        self.x = x
        self.y = y

# sys.getsizeof taqqoslash
import sys
p1 = Point(1, 2)       # ~56 bytes
# dict versiya          # ~232 bytes
</pre>

<b>📌 MULTIPROCESSING (GIL BYPASS):</b>

<pre>
from concurrent.futures import ProcessPoolExecutor

def cpu_task(n):
    return sum(i**2 for i in range(n))

with ProcessPoolExecutor() as ex:
    results = list(ex.map(cpu_task, [1_000_000]*8))
</pre>

<b>📌 NUMPY VA NUMBA:</b>

<pre>
import numpy as np
# Python loop: 1000x sekin
result = [x**2 for x in data]

# NumPy: vektorlashtirilgan
result = np.array(data) ** 2
</pre>

<b>✅ VAZIFA:</b> cProfile bilan kod profilingini bajaring va bottleneck'ni toping!""",

            """<b>🐍 DARS 6: FASTAPI — ZAMONAVIY WEB API</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 FASTAPI ASOSLARI:</b>

<pre>
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI(title="Linux Master API")

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

@app.post("/users/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email allaqachon ro'yxatda")
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
</pre>

<b>📌 MIDDLEWARE VA AUTHENTICATION:</b>

<pre>
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

app.add_middleware(CORSMiddleware, allow_origins=["*"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Token tekshirish
    ...
</pre>

<b>✅ VAZIFA:</b> FastAPI bilan CRUD API yozing: create, read, update, delete!""",

            """<b>🐍 DARS 7: PYTHON TESTING — PYTEST MASTERY</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 PYTEST ASOSLARI:</b>

<pre>
import pytest

# Oddiy test
def test_addition():
    assert 1 + 1 == 2

# Parametrli test
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Exception tekshirish
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
</pre>

<b>📌 FIXTURE:</b>

<pre>
@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()

def test_user_creation(db_session):
    user = User(name="Test")
    db_session.add(user)
    db_session.commit()
    assert user.id is not None
</pre>

<b>📌 MOCK:</b>

<pre>
from unittest.mock import patch, MagicMock

@patch("mymodule.requests.get")
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {"status": "ok"}
    result = call_api()
    assert result["status"] == "ok"
</pre>

<b>✅ VAZIFA:</b> 90%+ test coverage bilan to'liq test suite yozing!""",

            """<b>🐍 DARS 8: PYTHON DESIGN PATTERNS</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 OBSERVER PATTERN:</b>

<pre>
from abc import ABC, abstractmethod
from typing import List

class Event:
    def __init__(self):
        self._handlers: List = []

    def subscribe(self, handler):
        self._handlers.append(handler)

    def unsubscribe(self, handler):
        self._handlers.remove(handler)

    def fire(self, *args, **kwargs):
        for handler in self._handlers:
            handler(*args, **kwargs)

# Ishlatish
on_lesson_complete = Event()
on_lesson_complete.subscribe(update_xp)
on_lesson_complete.subscribe(check_achievements)
on_lesson_complete.fire(user_id=123, topic="linux")
</pre>

<b>📌 COMMAND PATTERN:</b>

<pre>
class Command(ABC):
    @abstractmethod
    def execute(self): ...
    @abstractmethod
    def undo(self): ...

class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def execute(self, cmd: Command):
        cmd.execute()
        self.history.append(cmd)

    def undo(self):
        if self.history:
            self.history.pop().undo()
</pre>

<b>📌 STRATEGY PATTERN:</b>

<pre>
from typing import Protocol

class SortStrategy(Protocol):
    def sort(self, data: list) -> list: ...

class QuickSort:
    def sort(self, data): return sorted(data)

class MergeSort:
    def sort(self, data): return sorted(data, key=lambda x: -x)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)
</pre>

<b>✅ VAZIFA:</b> Repository pattern bilan SQLite va PostgreSQL interchangeable qiling!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "devops_cicd": {
        "title": "⚙️ DevOps & CI/CD — Zamonaviy deployment",
        "lessons": [
            """<b>⚙️ DARS 1: DEVOPS MADANIYATI VA TAMOYILLARI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 DEVOPS NIMA?</b>

DevOps = Development + Operations

• <b>CALMS</b> modeli:
  - <b>C</b>ulture (Madaniyat)
  - <b>A</b>utomation (Avtomatlashtirish)
  - <b>L</b>ean (Kam israf)
  - <b>M</b>easurement (O'lchov)
  - <b>S</b>haring (Ulashish)

<b>📌 DEVOPS HAYOT SIKLI:</b>

<code>Plan → Code → Build → Test → Release → Deploy → Operate → Monitor</code>

<b>📌 ASOSIY METRIKALAR:</b>

• <b>DORA Metrics:</b>
  - Deployment Frequency
  - Lead Time for Changes
  - Mean Time to Recovery (MTTR)
  - Change Failure Rate

<b>📌 ASOSIY TOOLCHAIN:</b>

• Version Control: Git, GitHub/GitLab
• CI/CD: Jenkins, GitHub Actions, GitLab CI
• Konteyner: Docker, Podman
• Orkestratsiya: Kubernetes, Docker Swarm
• Infrastructure: Terraform, Ansible
• Monitoring: Prometheus, Grafana, ELK

<b>✅ VAZIFA:</b> DORA metrikalarini o'rganing va jamoangiz holini baholang!""",

            """<b>⚙️ DARS 2: GITHUB ACTIONS — PROFESSIONAL CI/CD</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 TO'LIQ CI/CD PIPELINE:</b>

<pre>
# .github/workflows/deploy.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  IMAGE: ghcr.io/${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Python setup
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest --cov=. --cov-report=xml

      - name: Coverage check
        run: coverage report --fail-under=80

  build:
    needs: test
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: ${{ env.IMAGE }}:${{ github.sha }}

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to server
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: deploy
          key: ${{ secrets.SSH_KEY }}
          script: |
            docker pull ${{ env.IMAGE }}:${{ github.sha }}
            docker service update --image \
              ${{ env.IMAGE }}:${{ github.sha }} myapp
</pre>

<b>✅ VAZIFA:</b> O'z GitHub Actions pipeline'ingizni yozing!""",

            """<b>⚙️ DARS 3: TERRAFORM — INFRASTRUCTURE AS CODE</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 TERRAFORM ASOSLARI:</b>

<pre>
# main.tf
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
  backend "s3" {
    bucket = "my-tfstate"
    key    = "prod/terraform.tfstate"
    region = "eu-central-1"
  }
}

# Nginx container
resource "docker_image" "nginx" {
  name         = "nginx:alpine"
  keep_locally = false
}

resource "docker_container" "web" {
  image = docker_image.nginx.image_id
  name  = "web-server"

  ports {
    internal = 80
    external = var.web_port
  }
}

variable "web_port" {
  type    = number
  default = 8080
}

output "web_url" {
  value = "http://localhost:${var.web_port}"
}
</pre>

<b>📌 TERRAFORM BUYRUQLAR:</b>

<code>terraform init</code>      → Provider yuklab olish
<code>terraform plan</code>     → O'zgarishlar preview
<code>terraform apply</code>    → Infrastruktura yaratish
<code>terraform destroy</code>  → Hammasini o'chirish
<code>terraform state list</code> → Resurs holati

<b>✅ VAZIFA:</b> Terraform bilan mahalliy Docker infrastruktura yarating!""",

            """<b>⚙️ DARS 4: ANSIBLE — KONFIGURATSIYA BOSHQARISH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 ANSIBLE TUZILMASI:</b>

<pre>
# inventory/hosts.yml
all:
  children:
    webservers:
      hosts:
        web1: {ansible_host: 10.0.0.1}
        web2: {ansible_host: 10.0.0.2}
    databases:
      hosts:
        db1: {ansible_host: 10.0.0.10}
</pre>

<b>📌 TO'LIQ PLAYBOOK:</b>

<pre>
# deploy.yml
---
- name: Web serverni sozlash
  hosts: webservers
  become: true
  vars:
    app_port: 8000
    app_user: deploy

  tasks:
    - name: Paketlarni yangilash
      apt:
        update_cache: yes
        upgrade: safe
      tags: [packages]

    - name: Nginx o'rnatish
      apt:
        name: nginx
        state: present

    - name: Nginx config deploy
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/sites-available/myapp
        owner: root
        mode: '0644'
      notify: restart nginx

    - name: App user yaratish
      user:
        name: "{{ app_user }}"
        system: yes
        shell: /bin/bash

  handlers:
    - name: restart nginx
      service:
        name: nginx
        state: restarted
</pre>

<b>📌 ISHLATISH:</b>

<code>ansible-playbook deploy.yml --check</code>   → Dry-run
<code>ansible-playbook deploy.yml --tags packages</code>
<code>ansible all -m ping</code>                   → Ulanish tekshirish

<b>✅ VAZIFA:</b> Ansible bilan Nginx server sozlash playbook yozing!""",

            """<b>⚙️ DARS 5: MONITORING — PROMETHEUS + GRAFANA</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 PROMETHEUS ASOSLARI:</b>

<pre>
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alerts.yml"

alerting:
  alertmanagers:
    - static_configs:
        - targets: ["alertmanager:9093"]

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'myapp'
    static_configs:
      - targets: ['myapp:8000']
    metrics_path: /metrics
</pre>

<b>📌 PROMQL QUERIES:</b>

<code>rate(http_requests_total[5m])</code>          → So'rov tezligi
<code>histogram_quantile(0.95, rate(...))</code>    → P95 latency
<code>sum by (status) (http_requests_total)</code>  → Status bo'yicha
<code>100 - (node_memory_Available_bytes / node_memory_MemTotal_bytes * 100)</code>

<b>📌 ALERTING:</b>

<pre>
# alerts.yml
groups:
  - name: app_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_errors_total[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Yuqori xato darajasi"
</pre>

<b>📌 DOCKER COMPOSE BILAN:</b>

<code>docker compose up -d prometheus grafana alertmanager node-exporter</code>

<b>✅ VAZIFA:</b> Prometheus + Grafana stack'ni compose bilan ishga tushiring!""",

            """<b>⚙️ DARS 6: LOGGING — ELK STACK</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 ELK STACK:</b>

• <b>E</b>lasticsearch — Ma'lumot saqlash va qidirish
• <b>L</b>ogstash — Log yig'ish va parsing
• <b>K</b>ibana — Vizualizatsiya

<b>📌 LOGSTASH KONFIGURATSIYA:</b>

<pre>
# logstash.conf
input {
  beats {
    port => 5044
  }
  tcp {
    port => 5000
    codec => json
  }
}

filter {
  if [type] == "nginx" {
    grok {
      match => {
        "message" => '%{IPORHOST:client} - %{USER:auth} \[%{HTTPDATE:timestamp}\] "%{WORD:method} %{DATA:request}" %{INT:status}'
      }
    }
    date {
      match => ["timestamp", "dd/MMM/yyyy:HH:mm:ss Z"]
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }
}
</pre>

<b>📌 FILEBEAT:</b>

<pre>
filebeat.inputs:
  - type: log
    paths:
      - /var/log/nginx/*.log
    fields:
      type: nginx

output.logstash:
  hosts: ["logstash:5044"]
</pre>

<b>✅ VAZIFA:</b> ELK stack'ni compose bilan ishga tushirib, Nginx loglarini yig'ing!""",

            """<b>⚙️ DARS 7: GITOPS — ARGO CD BILAN</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 GITOPS NIMA?</b>

Git = Yagona haqiqat manbai (single source of truth)

• Barcha infrastruktura kodi Git'da
• Pull-based deployment (push emas)
• Avtomatik muvofiqlashtirish
• Audit trail (kim nima o'zgartirdi)

<b>📌 ARGO CD:</b>

<pre>
# Application manifest
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/user/myapp-config
    targetRevision: main
    path: k8s/overlays/prod
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true      # Eski resurslarni o'chirish
      selfHeal: true   # Muvofiqlashtirish
    syncOptions:
      - CreateNamespace=true
</pre>

<b>📌 ARGO CD BUYRUQLAR:</b>

<code>argocd app list</code>
<code>argocd app sync myapp</code>
<code>argocd app history myapp</code>
<code>argocd app rollback myapp 3</code>

<b>📌 KUSTOMIZE BILAN:</b>

<pre>
# kustomization.yaml
resources:
  - ../../base
images:
  - name: myapp
    newTag: v2.5.0
</pre>

<b>✅ VAZIFA:</b> GitOps workflow'ni loyihangiz uchun loyihalang!""",

            """<b>⚙️ DARS 8: SITE RELIABILITY ENGINEERING (SRE)</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 SRE ASOSIY TUSHUNCHALAR:</b>

• <b>SLI</b> (Service Level Indicator) — O'lchov
• <b>SLO</b> (Service Level Objective) — Maqsad
• <b>SLA</b> (Service Level Agreement) — Shartnoma
• <b>Error Budget</b> — Ruxsat etilgan xato miqdori

<b>📌 MISOL:</b>

<pre>
SLI: 99.9% so'rovlar 200ms'dan tez
SLO: 99.95% availability (oyiga 21 daqiqa downtime)
Error Budget: 0.05% = oyiga ~21 daqiqa
</pre>

<b>📌 POSTMORTEM (BLAMELESS):</b>

Tuzilma:
1. Voqea qachon sodir bo'ldi?
2. Ta'sir qancha davom etdi?
3. Sabab nima edi?
4. Qanday hal qilindi?
5. Oldini olish uchun nima qilish kerak?

<b>📌 RUNBOOK:</b>

<pre>
# Runbook: DB Slow Queries
## Aniqlash
SELECT * FROM pg_stat_activity WHERE state='active';
SELECT query, calls, total_time/calls as avg_ms
FROM pg_stat_statements ORDER BY avg_ms DESC LIMIT 10;

## Hal qilish
EXPLAIN ANALYZE slow_query;
CREATE INDEX CONCURRENTLY idx ON table(column);
</pre>

<b>📌 CHAOS ENGINEERING:</b>

<code>chaos-mesh pod-kill --selector app=web</code>
<code>toxiproxy -- tarmoq kechiktirishni simulatsiya</code>

<b>✅ VAZIFA:</b> O'z loyihangiz uchun SLO va Error Budget aniqlang!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "sql_mastery": {
        "title": "🗄️ SQL & Databases — Ma'lumotlar bazasi USTASI",
        "lessons": [
            """<b>🗄️ DARS 1: SQL ADVANCED QUERIES</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 WINDOW FUNCTIONS:</b>

<pre>
-- Har bir bo'limdagi reyting
SELECT
    name, department, salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dense_rank,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as row_num,
    LAG(salary, 1) OVER (ORDER BY hire_date) as prev_salary,
    LEAD(salary, 1) OVER (ORDER BY hire_date) as next_salary
FROM employees;
</pre>

<b>📌 CTE (COMMON TABLE EXPRESSIONS):</b>

<pre>
-- Rekursiv CTE: tashkilot daraxti
WITH RECURSIVE org_tree AS (
    SELECT id, name, manager_id, 1 as level
    FROM employees
    WHERE manager_id IS NULL  -- Top

    UNION ALL

    SELECT e.id, e.name, e.manager_id, ot.level + 1
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.id
)
SELECT * FROM org_tree ORDER BY level, name;
</pre>

<b>📌 ADVANCED JOINS:</b>

<pre>
-- LATERAL JOIN
SELECT u.name, last_orders.*
FROM users u
CROSS JOIN LATERAL (
    SELECT * FROM orders
    WHERE user_id = u.id
    ORDER BY created_at DESC
    LIMIT 3
) last_orders;
</pre>

<b>✅ VAZIFA:</b> O'z bazangizda Window Functions bilan xodimlar reytingini tuzing!""",

            """<b>🗄️ DARS 2: POSTGRESQL PROFESSIONAL</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 INDEXLAR — CHUQUR:</b>

<pre>
-- B-tree (default)
CREATE INDEX idx_email ON users(email);

-- Partial index
CREATE INDEX idx_active_users ON users(email)
WHERE status = 'active';

-- Composite index
CREATE INDEX idx_user_date ON orders(user_id, created_at);

-- GIN index (full-text, JSON)
CREATE INDEX idx_tags ON articles USING GIN(tags);

-- Index explain
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE email = 'x@y.com';
</pre>

<b>📌 JSONB:</b>

<pre>
-- JSONB maydoni
CREATE TABLE events (
    id SERIAL,
    data JSONB
);

-- JSONB query
SELECT data->>'name', data->'tags'->0
FROM events
WHERE data @> '{"type": "login"}';

-- JSONB index
CREATE INDEX idx_events_data ON events USING GIN(data);
</pre>

<b>📌 PARTITIONING:</b>

<pre>
CREATE TABLE logs (
    id BIGSERIAL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    message TEXT
) PARTITION BY RANGE (created_at);

CREATE TABLE logs_2024_01 PARTITION OF logs
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
</pre>

<b>✅ VAZIFA:</b> EXPLAIN ANALYZE bilan sekin queryingizni optimallashtiring!""",

            """<b>🗄️ DARS 3: POSTGRESQL PERFORMANCE TUNING</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 POSTGRESQL.CONF PARAMETRLARI:</b>

<pre>
# postgresql.conf optimallashtirish
shared_buffers = 4GB              # RAM ning 25%
effective_cache_size = 12GB       # RAM ning 75%
work_mem = 64MB                   # Sort uchun
maintenance_work_mem = 1GB        # VACUUM uchun
wal_buffers = 64MB
checkpoint_completion_target = 0.9
random_page_cost = 1.1            # SSD uchun

# Parallel query
max_parallel_workers = 8
max_parallel_workers_per_gather = 4
</pre>

<b>📌 VACUUM VA AUTOVACUUM:</b>

<pre>
-- Manual vacuum
VACUUM ANALYZE users;
VACUUM FULL users;  -- Jadval qulflaydi!

-- Autovacuum sozlash
ALTER TABLE big_table SET (
    autovacuum_vacuum_scale_factor = 0.01,
    autovacuum_analyze_scale_factor = 0.005
);

-- Dead tuples monitoring
SELECT relname, n_dead_tup, last_vacuum
FROM pg_stat_user_tables ORDER BY n_dead_tup DESC;
</pre>

<b>📌 CONNECTION POOLING (PgBouncer):</b>

<pre>
# pgbouncer.ini
[databases]
mydb = host=localhost port=5432 dbname=mydb

[pgbouncer]
pool_mode = transaction  # Eng samarali
max_client_conn = 1000
default_pool_size = 25
</pre>

<b>✅ VAZIFA:</b> pg_stat_statements bilan eng sekin 10 ta queryni toping!""",

            """<b>🗄️ DARS 4: REDIS — IN-MEMORY DATABASE</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 REDIS DATA STRUCTURES:</b>

<pre>
# String
SET user:1:name "Hakimbek" EX 3600
GET user:1:name
INCR counter

# Hash
HSET user:1 name "Hakimbek" age 25 city "Tashkent"
HGET user:1 name
HGETALL user:1

# List (queue)
LPUSH queue:tasks "task1" "task2"
RPOP queue:tasks
LLEN queue:tasks

# Set (unique)
SADD online:users 101 102 103
SISMEMBER online:users 101
SMEMBERS online:users

# Sorted Set (leaderboard)
ZADD leaderboard 1500 "user:1" 2300 "user:2"
ZREVRANGE leaderboard 0 9 WITHSCORES
ZINCRBY leaderboard 100 "user:1"
</pre>

<b>📌 REDIS PATTERNS:</b>

<pre>
# Rate limiting
MULTI
INCR rate:user:101
EXPIRE rate:user:101 60
EXEC

# Pub/Sub
SUBSCRIBE channel
PUBLISH channel "message"

# Distributed lock
SET lock:resource "uuid" NX EX 30
</pre>

<b>📌 PYTHON REDIS:</b>

<pre>
import redis.asyncio as redis
r = redis.Redis(host='localhost', decode_responses=True)
await r.setex("key", 3600, "value")
</pre>

<b>✅ VAZIFA:</b> Redis bilan Leaderboard tizimi yarating!""",

            """<b>🗄️ DARS 5: DATABASE DESIGN PATTERNS</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 NORMALIZATSIYA:</b>

• <b>1NF</b> — Atomik qiymatlar, takrorlash yo'q
• <b>2NF</b> — To'liq funksional bog'liqlik
• <b>3NF</b> — Tranzitiv bog'liqlik yo'q

<b>📌 YAXSHI SCHEMA DIZAYNI:</b>

<pre>
-- Soft delete
ALTER TABLE users ADD COLUMN deleted_at TIMESTAMPTZ;
SELECT * FROM users WHERE deleted_at IS NULL;

-- Audit trail
CREATE TABLE audit_log (
    id BIGSERIAL PRIMARY KEY,
    table_name TEXT,
    record_id BIGINT,
    action TEXT, -- INSERT/UPDATE/DELETE
    old_values JSONB,
    new_values JSONB,
    changed_by INTEGER REFERENCES users(id),
    changed_at TIMESTAMPTZ DEFAULT NOW()
);

-- Trigger bilan avtomatik audit
CREATE OR REPLACE FUNCTION audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log(table_name, record_id, action, old_values, new_values)
    VALUES (TG_TABLE_NAME, NEW.id, TG_OP, row_to_json(OLD), row_to_json(NEW));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
</pre>

<b>📌 SHARDING STRATEGIYASI:</b>

• <b>Horizontal sharding</b> — Qator bo'yicha
• <b>Vertical sharding</b> — Ustun bo'yicha
• <b>Hash sharding</b> — Hash(user_id) % N

<b>✅ VAZIFA:</b> Audit trail tizimini trigger bilan qo'shib implement qiling!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "networking_pro": {
        "title": "🌐 Networking PRO — Tarmoq USTASI",
        "lessons": [
            """<b>🌐 DARS 1: TCP/IP CHUQUR TAHLIL</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 TCP 3-WAY HANDSHAKE:</b>

<pre>
Client                    Server
  |  --SYN (seq=x)-->      |
  |  <--SYN-ACK (seq=y, ack=x+1)--|
  |  --ACK (ack=y+1)-->    |
  |     [ESTABLISHED]      |
</pre>

<b>📌 TCP XUSUSIYATLARI:</b>

• <b>Flow Control</b> — Sliding window, receiver buffer
• <b>Congestion Control</b> — Slow start, AIMD
• <b>Reliability</b> — Retransmission, ordering
• <b>TIME_WAIT</b> — 2*MSL kutish

<b>📌 SOCKET STATES:</b>

<code>ss -tn state established</code>
<code>ss -tn state time-wait | wc -l</code>

<b>📌 TCP PARAMETRLAR:</b>

<pre>
# Yangi serverlar uchun optimallashtirish
sysctl net.ipv4.tcp_fin_timeout=15
sysctl net.ipv4.tcp_tw_reuse=1
sysctl net.core.somaxconn=65535
sysctl net.ipv4.tcp_max_syn_backlog=65535
</pre>

<b>📌 UDP VS TCP:</b>

| Xususiyat   | TCP          | UDP           |
|-------------|--------------|---------------|
| Ulanish     | Kerak        | Kerak emas    |
| Ishonchlilik| Kafolatlangan| Kafolat yo'q  |
| Tartib      | Saqlangan    | Saqlanmagan   |
| Tezlik      | Sekinroq     | Tezroq        |
| Foydalanish | HTTP, FTP    | Video, DNS    |

<b>✅ VAZIFA:</b> <code>tcpdump</code> bilan 3-way handshake'ni ushlang!""",

            """<b>🌐 DARS 2: DNS — CHUQUR TAHLIL</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 DNS RECORD TURLARI:</b>

<code>A</code>     → IPv4 manzil (example.com → 1.2.3.4)
<code>AAAA</code>  → IPv6 manzil
<code>CNAME</code> → Taxallus (www → example.com)
<code>MX</code>   → Mail server
<code>TXT</code>  → SPF, DKIM, DMARC, tasdiqlash
<code>NS</code>   → Name server
<code>SOA</code>  → Start of Authority
<code>PTR</code>  → Reverse DNS
<code>SRV</code>  → Servis (port va protokol)

<b>📌 DNS DIAGNOSTIKA:</b>

<code>dig example.com</code>           → A record
<code>dig MX example.com</code>       → MX record
<code>dig +trace example.com</code>   → To'liq yo'l
<code>dig @8.8.8.8 example.com</code> → Google DNS
<code>nslookup example.com</code>     → Windows usuli

<b>📌 DNS XAVFSIZLIGI:</b>

• <b>DNSSEC</b> — Kriptografik imzo
• <b>DoH</b> — DNS over HTTPS
• <b>DoT</b> — DNS over TLS

<b>📌 MAHALLIY DNS:</b>

<pre>
# /etc/hosts
127.0.0.1   myapp.local
192.168.1.10 db.local

# systemd-resolved
resolvectl status
resolvectl query example.com
</pre>

<b>✅ VAZIFA:</b> <code>dig +trace google.com</code> bilan DNS yo'lini kuzating!""",

            """<b>🌐 DARS 3: NGINX — REVERSE PROXY MASTERY</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 TO'LIQ NGINX KONFIGURATSIYA:</b>

<pre>
# /etc/nginx/sites-available/myapp
upstream backend {
    least_conn;  # load balancing strategy
    server 127.0.0.1:8001 weight=3;
    server 127.0.0.1:8002 weight=2;
    server 127.0.0.1:8003 backup;
    keepalive 32;
}

server {
    listen 443 ssl http2;
    server_name api.example.com;

    ssl_certificate     /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:HIGH:!aNULL;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Strict-Transport-Security "max-age=31536000" always;

    # Rate limiting
    limit_req zone=api burst=20 nodelay;

    location / {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_connect_timeout 5s;
        proxy_read_timeout 60s;

        proxy_cache_bypass $http_pragma;
        proxy_cache_valid 200 10m;
    }

    location /static/ {
        root /var/www;
        expires 1y;
        add_header Cache-Control "public, immutable";
        gzip_static on;
    }
}
</pre>

<b>✅ VAZIFA:</b> Nginx bilan load balancing va SSL termination sozlang!""",

            """<b>🌐 DARS 4: HTTP/2 VA HTTP/3 (QUIC)</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 HTTP/1.1 MUAMMOLARI:</b>

• Head-of-line blocking
• Connection per request
• Plain text header (katta o'lcham)

<b>📌 HTTP/2 YAXSHILANISHLARI:</b>

• <b>Multiplexing</b> — Bir ulanishda ko'p so'rov
• <b>Header compression</b> — HPACK
• <b>Server Push</b> — So'ralmadan yuborish
• <b>Binary framing</b> — Samaraliroq

<b>📌 HTTP/3 (QUIC):</b>

• UDP asosida
• 0-RTT ulanish
• Connection ID (IP o'zgarsa ham)
• Yaxshilangan xato tuzatish

<b>📌 STATUS KODLAR:</b>

• <b>1xx</b> — Informational
• <b>2xx</b> — Success (200 OK, 201 Created, 204 No Content)
• <b>3xx</b> — Redirect (301 Moved, 302 Found, 304 Not Modified)
• <b>4xx</b> — Client Error (400, 401, 403, 404, 429)
• <b>5xx</b> — Server Error (500, 502, 503, 504)

<b>📌 DIAGNOSTIKA:</b>

<code>curl -I https://example.com</code>      → Headers
<code>curl -v https://example.com</code>      → Verbose
<code>curl --http2 https://example.com</code>  → HTTP/2

<b>✅ VAZIFA:</b> <code>curl -v</code> bilan HTTP/2 muloqotini kuzating!""",

            """<b>🌐 DARS 5: VPN VA TUNNELING</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 WIREGUARD VPN:</b>

<pre>
# Server konfiguratsiya (/etc/wireguard/wg0.conf)
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = SERVER_PRIVATE_KEY

[Peer]
PublicKey = CLIENT_PUBLIC_KEY
AllowedIPs = 10.0.0.2/32

# Buyruqlar
wg-quick up wg0
wg show
</pre>

<b>📌 SSH TUNNELING:</b>

<pre>
# Local tunneling (lokal portdan remote'ga)
ssh -L 8080:localhost:80 user@server

# Remote tunneling (serverdan lokal'ga)
ssh -R 8080:localhost:80 user@server

# Dynamic SOCKS proxy
ssh -D 1080 user@server
curl --socks5 localhost:1080 http://example.com
</pre>

<b>📌 IPTABLES NAT:</b>

<pre>
# IP masquerading (NAT)
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
echo 1 > /proc/sys/net/ipv4/ip_forward

# Port forwarding
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
</pre>

<b>✅ VAZIFA:</b> WireGuard bilan oddiy VPN server o'rnating!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "git_mastery": {
        "title": "🔀 Git Mastery — Versiyalar USTASI",
        "lessons": [
            """<b>🔀 DARS 1: GIT ICHKI ARXITEKTURASI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 GIT OBYEKT MODELI:</b>

• <b>blob</b>   — Fayl tarkibi
• <b>tree</b>   — Katalog (blob va tree pointerlar)
• <b>commit</b> — Snapshot + metadata
• <b>tag</b>    — Annotatsiyali tag

<b>📌 GIT ICHKI FAYLLAR:</b>

<code>cat .git/HEAD</code>                    → Joriy branch
<code>cat .git/refs/heads/main</code>         → Branch SHA
<code>git cat-file -p HEAD</code>             → Commit objekti
<code>git cat-file -p HEAD^{tree}</code>      → Tree objekti

<b>📌 KUCHLI GIT BUYRUQLAR:</b>

<code>git reflog</code>                 → Barcha harakat tarixi
<code>git bisect start</code>          → Bug'ni ikkilik qidirish
<code>git blame -L 10,20 file</code>   → Qator bo'yicha muallif
<code>git log --graph --oneline --all</code>
<code>git shortlog -sn</code>          → Commit soni bo'yicha

<b>📌 STASH MANAGEMENT:</b>

<code>git stash push -m "WIP: feature"</code>
<code>git stash list</code>
<code>git stash pop stash@{2}</code>
<code>git stash branch new-branch stash@{0}</code>

<b>✅ VAZIFA:</b> <code>git bisect</code> bilan bitta bug'ni toping!""",

            """<b>🔀 DARS 2: GIT WORKFLOW VA BRANCHING STRATEGIYASI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 GITFLOW:</b>

<pre>
main ──────────────────●────────────●
         \           /    \        /
develop   ●──●──●──●       ●──●──●
              \  /
             feature/login
</pre>

• <b>main</b> — Production'ga mos
• <b>develop</b> — Integratsiya branch
• <b>feature/*</b> — Yangi imkoniyat
• <b>hotfix/*</b> — Tezkor tuzatish
• <b>release/*</b> — Chiqarish tayyorligi

<b>📌 TRUNK BASED DEVELOPMENT:</b>

• Barcha main'ga push
• Feature flag bilan yashirish
• Kichik, tez-tez commit

<b>📌 REBASE VS MERGE:</b>

<pre>
# Merge (tarix saqlanadi)
git merge feature/login

# Rebase (chiziqli tarix)
git rebase main
git rebase -i HEAD~5  # Interactive rebase

# Squash merge
git merge --squash feature/login
</pre>

<b>📌 COMMIT YAXSHI XABAR:</b>

<pre>
feat(auth): JWT token yangilash mexanizmi qo'shildi

- Refresh token 7 kun davomida ishlaydi
- Access token 15 daqiqa
- Redis'da blacklist saqlash

Closes #123
</pre>

<b>✅ VAZIFA:</b> Interactive rebase bilan 5 ta commitni bitta qilib birlashtiring!""",

            """<b>🔀 DARS 3: GIT HOOKS VA AUTOMATION</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 GIT HOOKS TURLARI:</b>

• <b>pre-commit</b>    — Commitdan oldin
• <b>commit-msg</b>   — Xabar formati
• <b>pre-push</b>     — Pushdan oldin
• <b>post-receive</b> — Server: qabul qilgandan keyin

<b>📌 PRE-COMMIT HOOK:</b>

<pre>
#!/bin/bash
# .git/hooks/pre-commit
set -e

echo "🔍 Tekshiruv boshlanmoqda..."

# Python lint
python -m flake8 . --max-line-length=88
python -m black . --check
python -m mypy . --ignore-missing-imports

# Test
pytest tests/ -x -q

echo "✅ Barcha tekshiruvlar muvaffaqiyatli!"
</pre>

<b>📌 COMMIT-MSG HOOK:</b>

<pre>
#!/bin/bash
# Conventional Commits tekshirish
COMMIT_MSG=$(cat "$1")
PATTERN="^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .{1,72}"

if ! [[ "$COMMIT_MSG" =~ $PATTERN ]]; then
    echo "❌ Commit xabari noto'g'ri format!"
    echo "Misol: feat(auth): login funksiyasi"
    exit 1
fi
</pre>

<b>📌 PRE-COMMIT FRAMEWORK:</b>

<pre>
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
</pre>

<b>✅ VAZIFA:</b> Pre-commit hook'larni o'z loyihangizga qo'shib, avtomatik lint sozlang!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "cloud_aws": {
        "title": "☁️ Cloud & AWS — Bulut hisoblash",
        "lessons": [
            """<b>☁️ DARS 1: CLOUD COMPUTING ASOSLARI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 CLOUD MODELLARI:</b>

• <b>IaaS</b> — Infrastructure as a Service (VM, Network, Storage)
• <b>PaaS</b> — Platform as a Service (Runtime, Middleware)
• <b>SaaS</b> — Software as a Service (Gmail, Slack)
• <b>FaaS</b> — Function as a Service (Lambda, Cloud Functions)

<b>📌 DEPLOYMENT MODELLARI:</b>

• <b>Public Cloud</b>  — AWS, GCP, Azure (umumiy)
• <b>Private Cloud</b> — OpenStack (xususiy)
• <b>Hybrid Cloud</b>  — Ikkalasini birlashtirish
• <b>Multi-Cloud</b>   — Bir necha provayderda

<b>📌 AWS ASOSIY XIZMATLAR:</b>

• <b>EC2</b>        — Virtual mashinalar
• <b>S3</b>        — Object storage
• <b>RDS</b>       — Managed database
• <b>Lambda</b>    — Serverless funksiya
• <b>ECS/EKS</b>   — Konteyner orkestrasiya
• <b>VPC</b>       — Virtual private network
• <b>IAM</b>       — Access management
• <b>CloudWatch</b> — Monitoring va logging

<b>📌 NARX OPTIMALLASHTIRISH:</b>

• Reserved Instances (1-3 yil) — 40-75% arzon
• Spot Instances — 90% arzon (bekor bo'lishi mumkin)
• Savings Plans — Moslashuvchan chegirma

<b>✅ VAZIFA:</b> AWS Free Tier'da EC2 va S3 ishga tushiring!""",

            """<b>☁️ DARS 2: AWS S3 VA STORAGE</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 S3 XUSUSIYATLARI:</b>

• 11 nine's durability (99.999999999%)
• Object size: 0 B dan 5 TB gacha
• Bucket — global nom (unikal)
• Region — ma'lumot joylashuvi

<b>📌 S3 STORAGE CLASSLAR:</b>

• <b>Standard</b>           — Tez-tez kirish
• <b>Intelligent-Tiering</b> — Avtomatik optimizatsiya
• <b>Standard-IA</b>        — Kam kiriladi, tez kirish
• <b>Glacier</b>            — Arxiv (daqiqalar)
• <b>Glacier Deep Archive</b>— Arxiv (soatlar, arzon)

<b>📌 AWS CLI:</b>

<code>aws s3 ls</code>                           → Bucketlar ro'yxati
<code>aws s3 cp fayl.txt s3://mybucket/</code>  → Yuklash
<code>aws s3 sync ./local s3://mybucket/</code>  → Sinxronlashtirish
<code>aws s3 presign s3://bucket/file --expires-in 3600</code>

<b>📌 S3 XAVFSIZLIGI:</b>

<pre>
# Bucket policy
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::mybucket/public/*"
  }]
}
</pre>

<b>📌 LIFECYCLE POLICY:</b>

30 kun → Standard-IA → 90 kun → Glacier

<b>✅ VAZIFA:</b> S3 bucket'ga statik website hosting sozlang!""",

            """<b>☁️ DARS 3: AWS LAMBDA — SERVERLESS</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 LAMBDA ARXITEKTURASI:</b>

• Event-driven
• Avtomatik masshtablash
• Millisecond billing
• Max 15 daqiqa runtime
• 10 GB RAM, 10 GB /tmp

<b>📌 LAMBDA FUNKSIYA (Python):</b>

<pre>
import json, boto3

s3 = boto3.client('s3')

def handler(event, context):
    # Event parsing
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Fayl o'qish
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read()

    # Qayta ishlash
    result = process(content)

    # Natijani saqlash
    s3.put_object(
        Bucket='output-bucket',
        Key=f'processed/{key}',
        Body=result
    )

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }
</pre>

<b>📌 SERVERLESS FRAMEWORK:</b>

<pre>
# serverless.yml
service: myapp
provider:
  name: aws
  runtime: python3.11
  region: eu-central-1

functions:
  process:
    handler: handler.handler
    events:
      - s3:
          bucket: input-bucket
          event: s3:ObjectCreated:*
</pre>

<b>✅ VAZIFA:</b> S3'ga fayl yuklansa, uni qayta ishlaydigan Lambda yozing!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "security_pro": {
        "title": "🛡️ Cybersecurity PRO — Xavfsizlik USTASI",
        "lessons": [
            """<b>🛡️ DARS 1: KRIPTOGRAFIYA ASOSLARI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 SIMMETRIK KRIPTOGRAFIYA:</b>

• <b>AES-256-GCM</b> — Eng kuchli simmetrik
• <b>ChaCha20-Poly1305</b> — Mobil uchun

<pre>
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=256)
nonce = os.urandom(12)
aad = b"authenticated data"  # Qo'shimcha autentifikatsiya
aesgcm = AESGCM(key)

ciphertext = aesgcm.encrypt(nonce, b"sir matn", aad)
plaintext = aesgcm.decrypt(nonce, ciphertext, aad)
</pre>

<b>📌 ASIMMETRIK KRIPTOGRAFIYA:</b>

• <b>RSA-4096</b> — Keng tarqalgan (sekin)
• <b>Ed25519</b>  — Elliptic curve, tezkor
• <b>X25519</b>   — ECDH key exchange

<pre>
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()

signature = private_key.sign(b"xabar")
public_key.verify(signature, b"xabar")  # OK
</pre>

<b>📌 HASH FUNKSIYALAR:</b>

• <b>SHA-256/SHA-3</b> — Umumiy maqsad
• <b>BLAKE3</b>       — Eng tezkor zamonaviy
• <b>bcrypt/Argon2</b>— Parol uchun (sekin!)

<b>✅ VAZIFA:</b> Python'da fayl integrity checker yozing (SHA-256)!""",

            """<b>🛡️ DARS 2: WEB XAVFSIZLIGI (OWASP TOP 10)</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 OWASP TOP 10 (2021):</b>

1. <b>Broken Access Control</b> — Noto'g'ri ruxsat boshqarish
2. <b>Cryptographic Failures</b> — Zaif kriptografiya
3. <b>Injection</b> — SQL, LDAP, OS injection
4. <b>Insecure Design</b> — Arxitektura xatolari
5. <b>Security Misconfiguration</b> — Noto'g'ri sozlama
6. <b>Vulnerable Components</b> — Eskirgan kutubxonalar
7. <b>Auth Failures</b> — Autentifikatsiya xatolari
8. <b>Software Integrity Failures</b> — CI/CD xavfsizligi
9. <b>Logging Failures</b> — Yetarli log yo'q
10. <b>SSRF</b> — Server-Side Request Forgery

<b>📌 SQL INJECTION HIMOYA:</b>

<pre>
# YOMON (SQL injection)
query = f"SELECT * FROM users WHERE name='{user_input}'"

# YAXSHI (parametrized)
cursor.execute("SELECT * FROM users WHERE name=%s", (user_input,))

# ORM bilan
User.query.filter_by(name=user_input).first()
</pre>

<b>📌 XSS HIMOYA:</b>

<pre>
from markupsafe import escape

# Output encoding
safe_html = escape(user_input)

# CSP header
Content-Security-Policy: default-src 'self'; script-src 'nonce-{random}'
</pre>

<b>✅ VAZIFA:</b> O'z ilovangizda OWASP Top 10 tekshiruvidan o'tkazing!""",

            """<b>🛡️ DARS 3: PENETRATION TESTING ASOSLARI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 PENTEST BOSQICHLARI:</b>

1. <b>Reconnaissance</b> — Ma'lumot yig'ish
2. <b>Scanning</b>       — Port va servis skanerlash
3. <b>Exploitation</b>   — Zaiflikdan foydalanish
4. <b>Post-Exploitation</b> — Tizimda qolish
5. <b>Reporting</b>      — Hisobot tayyorlash

<b>📌 RECON VOSITALAR:</b>

<code>nmap -sV -sC -O target.com</code>     → Port skan
<code>nmap -p- --min-rate 5000 target</code> → Tezkor
<code>whois target.com</code>               → Domain ma'lumot
<code>subfinder -d target.com</code>        → Subdomain
<code>theHarvester -d target.com -b all</code>

<b>📌 WEB PENTEST VOSITALAR:</b>

• <b>Burp Suite</b>   — Web proxy
• <b>OWASP ZAP</b>   — Avtomatik skanerlash
• <b>gobuster</b>    — Directory fuzzing
• <b>SQLmap</b>      — SQL injection
• <b>nikto</b>       — Web zaiflik skaneri

<pre>
# gobuster directory scan
gobuster dir -u http://target.com \
  -w /usr/share/wordlists/dirbuster/medium.txt \
  -x php,html,txt

# SQLmap
sqlmap -u "http://target.com/page?id=1" \
  --dbs --batch
</pre>

⚠️ <b>OGOHLANTIRISH:</b> Faqat ruxsat berilgan tizimlarni test qiling!

<b>✅ VAZIFA:</b> HackTheBox yoki TryHackMe'da bitta mashq mashinani hacking qiling!""",

            """<b>🛡️ DARS 4: JWT VA OAUTH2 XAVFSIZLIGI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 JWT TUZILMASI:</b>

<pre>
Header.Payload.Signature

Header:  {"alg": "RS256", "typ": "JWT"}
Payload: {
  "sub": "12345",
  "name": "Hakimbek",
  "iat": 1709000000,
  "exp": 1709003600,
  "iss": "myapp.com",
  "aud": "api.myapp.com"
}
</pre>

<b>📌 JWT ZAIFLIKLAR VA HIMOYA:</b>

❌ <b>alg:none hujumi</b> → Har doim alg tekshiring
❌ <b>HS256 bilan public key</b> → RS256 ishlating
❌ <b>Uzun muddatli token</b> → Qisqa exp + refresh token
❌ <b>Sensitive ma'lumot payload'da</b> → Faqat ID saqlang

<pre>
# PyJWT xavfsiz ishlatish
import jwt

# Imzolash
token = jwt.encode(
    {"sub": user_id, "exp": datetime.utcnow() + timedelta(minutes=15)},
    private_key,
    algorithm="RS256"
)

# Tekshirish
payload = jwt.decode(
    token,
    public_key,
    algorithms=["RS256"],  # Faqat RS256!
    options={"require": ["exp", "iat", "sub"]}
)
</pre>

<b>📌 OAUTH2 FLOWS:</b>

• <b>Authorization Code + PKCE</b> — Web/SPA (eng xavfsiz)
• <b>Client Credentials</b>         — Server-to-server
• <b>Device Code</b>                — TV, CLI

<b>✅ VAZIFA:</b> RS256 bilan JWT authentication implementatsiya qiling!""",
        ],
    },

    # ═══════════════════════════════════════════════════════════
    "web_frontend": {
        "title": "🌈 Frontend Pro — React & Modern Web",
        "lessons": [
            """<b>🌈 DARS 1: REACT HOOKS — MASTERY</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 USESTATE VA USEEFFECT CHUQUR:</b>

<pre>
import { useState, useEffect, useCallback, useMemo, useRef } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const abortRef = useRef(null);

  useEffect(() => {
    const controller = new AbortController();
    abortRef.current = controller;

    const fetchUser = async () => {
      try {
        setLoading(true);
        const res = await fetch(`/api/users/${userId}`, {
          signal: controller.signal
        });
        if (!res.ok) throw new Error('Foydalanuvchi topilmadi');
        setUser(await res.json());
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err.message);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
    return () => controller.abort();  // Cleanup
  }, [userId]);

  // Memoized qiymat
  const fullName = useMemo(() =>
    user ? `${user.first_name} ${user.last_name}` : '',
  [user]);

  if (loading) return <Spinner />;
  if (error) return <Error message={error} />;
  return <div>{fullName}</div>;
}
</pre>

<b>📌 CUSTOM HOOK:</b>

<pre>
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(url).then(r => r.json()).then(setData).finally(() => setLoading(false));
  }, [url]);

  return { data, loading };
}
</pre>

<b>✅ VAZIFA:</b> Infinite scroll custom hook yarating!""",

            """<b>🌈 DARS 2: REACT PERFORMANCE OPTIMALLASHTIRISH</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 MEMO, USECALLBACK, USEMEMO:</b>

<pre>
import { memo, useCallback, useMemo } from 'react';

// Component memoization
const ExpensiveChild = memo(({ data, onSelect }) => {
  // Faqat data yoki onSelect o'zgarganda re-render
  return <div>{data.map(item => <Item key={item.id} {...item} onSelect={onSelect} />)}</div>;
});

function Parent() {
  const [items] = useState(bigList);
  const [selected, setSelected] = useState(null);

  // onSelect funksiya reference o'zgarmaydi
  const handleSelect = useCallback((id) => {
    setSelected(id);
  }, []);

  // Qimmat hisob faqat items o'zgarganda
  const filtered = useMemo(() =>
    items.filter(item => item.active),
  [items]);

  return <ExpensiveChild data={filtered} onSelect={handleSelect} />;
}
</pre>

<b>📌 VIRTUALIZATSIYA (katta ro'yxatlar):</b>

<pre>
import { FixedSizeList } from 'react-window';

function BigList({ items }) {
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {({ index, style }) => (
        <div style={style}>{items[index].name}</div>
      )}
    </FixedSizeList>
  );
}
</pre>

<b>📌 CODE SPLITTING:</b>

<pre>
const HeavyComponent = lazy(() => import('./HeavyComponent'));

<Suspense fallback={<Loader />}>
  <HeavyComponent />
</Suspense>
</pre>

<b>✅ VAZIFA:</b> 10,000 element ro'yxatni virtualizatsiya bilan render qiling!""",

            """<b>🌈 DARS 3: TYPESCRIPT — PROFESSIONAL DARAJASI</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📌 ADVANCED TYPES:</b>

<pre>
// Utility types
type Partial<T> = { [K in keyof T]?: T[K] };
type Required<T> = { [K in keyof T]-?: T[K] };
type Readonly<T> = { readonly [K in keyof T]: T[K] };

// Conditional types
type IsArray<T> = T extends any[] ? true : false;

// Template literal types
type EventName = `on${Capitalize<string>}`;
type ApiRoute = `/api/${string}`;

// Infer
type ReturnType<T extends (...args: any) => any> =
  T extends (...args: any) => infer R ? R : never;

// Discriminated union
type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E };

function processResult<T>(result: Result<T>): T {
  if (result.success) return result.data;  // Type narrowing
  throw result.error;
}
</pre>

<b>📌 GENERIC CONSTRAINTS:</b>

<pre>
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

interface Repository<T extends { id: number }> {
  findById(id: number): Promise<T | null>;
  findAll(): Promise<T[]>;
  save(entity: Omit<T, 'id'>): Promise<T>;
  delete(id: number): Promise<void>;
}
</pre>

<b>✅ VAZIFA:</b> Generic React hook <code>useLocalStorage<T></code> yozing!""",
        ],
    },

}

# Quiz savollari yangi mavzular uchun
NEW_QUIZZES = {
    "linux_advanced": [
        {
            "question": "Linux'da cgroup'lar qanday maqsadda ishlatiladi?",
            "options": [
                "Faqat Docker uchun",
                "Jarayonlar guruhiga resurs cheklovlarini qo'yish",
                "Kernel modullarini boshqarish",
                "Fayl tizimini shifrlash"
            ],
            "correct": 1,
            "explanation": "cgroups (control groups) jarayonlar guruhiga CPU, xotira, I/O va tarmoq resurslarini cheklash va monitoring qilish uchun ishlatiladi."
        },
        {
            "question": "PID namespace nima qiladi?",
            "options": [
                "Process ID'larni shifrlaydi",
                "Jarayonlar uchun izolyatsiyalangan PID ko'rinishini yaratadi",
                "PID'larni avtomatik optimallashtiradi",
                "Faqat root jarayonlar uchun ishlaydi"
            ],
            "correct": 1,
            "explanation": "PID namespace konteyner ichidagi jarayonlarga host tizimidan alohida PID ko'rinishini beradi. Bu Docker konteynerlarining asosi."
        },
        {
            "question": "systemd service'da 'Restart=always' nima qiladi?",
            "options": [
                "Service har daqiqada qayta ishga tushadi",
                "Service har qanday holatda (hatto success) qayta ishga tushadi",
                "Faqat xato bo'lsa qayta ishga tushadi",
                "Boot'da avtomatik ishga tushadi"
            ],
            "correct": 1,
            "explanation": "Restart=always service qanday holatda to'xtamasin (hatto exit code 0 bilan ham) uni qayta ishga tushiradi."
        },
        {
            "question": "inode nimani saqlaydi?",
            "options": [
                "Fayl nomini va mazmunini",
                "Fayl mazmunini va meta-ma'lumotlarni",
                "Fayl meta-ma'lumotlarini (hajm, huquqlar, egasi) va disk bloklarini ko'rsatadi",
                "Faqat fayl hajmini"
            ],
            "correct": 2,
            "explanation": "Inode fayl haqidagi meta-ma'lumotlarni (hajm, huquqlar, egasi, vaqt va disk bloklar ro'yxatini) saqlaydi. Fayl nomi esa directory'da saqlanadi."
        },
        {
            "question": "sysctl vm.swappiness=10 nima qiladi?",
            "options": [
                "Swap'ni o'chiradi",
                "Tizimni kamroq swap ishlatishga undaydi",
                "Swap hajmini 10 GB ga o'rnatadi",
                "10 ta swap fayl yaratadi"
            ],
            "correct": 1,
            "explanation": "swappiness 0-100 oraliqda. Kichik qiymat (masalan 10) tizimni RAM to'lgunga qadar swap ishlatmaslikka undaydi. Default 60."
        },
    ],

    "docker_mastery": [
        {
            "question": "Docker multi-stage build qanday muammo hal qiladi?",
            "options": [
                "Ko'p platform uchun build qilish",
                "Build vositalarini production image'ga kirmasdan kichik image yaratish",
                "Parallel build qilish",
                "Cache'ni optimallashtirish"
            ],
            "correct": 1,
            "explanation": "Multi-stage build'da bir stage'da build qilinib, faqat kerakli artifacts keyingi kichik production image'ga ko'chiriladi. Bu image hajmini sezilarli kamaytiradi."
        },
        {
            "question": "Docker volume va bind mount farqi nima?",
            "options": [
                "Hech qanday farq yo'q",
                "Volume Docker boshqaradi, bind mount host papkasini to'g'ridan-to'g'ri ko'rsatadi",
                "Bind mount tezroq, volume sekinroq",
                "Volume faqat Windows'da ishlaydi"
            ],
            "correct": 1,
            "explanation": "Named volume'larni Docker o'zi boshqaradi (/var/lib/docker/volumes/). Bind mount esa host fayl tizimidagi aniq papkani konteynerga ulaydi."
        },
        {
            "question": "Docker network 'bridge' mode nima?",
            "options": [
                "Konteyner host tarmoqni to'g'ridan-to'g'ri ishlatadi",
                "Konteynerlar izolyatsiyalangan virtual tarmoqda ishlaydi",
                "Tarmoqsiz izolyatsiya",
                "Ko'p host uchun overlay tarmoq"
            ],
            "correct": 1,
            "explanation": "Bridge mode default. Har bir konteyner izolyatsiyalangan virtual tarmoqda ishlaydi. Port mapping (-p) orqali tashqaridan kirish ta'minlanadi."
        },
        {
            "question": "docker-compose 'depends_on' bilan 'condition: service_healthy' farqi nima?",
            "options": [
                "Hech qanday farq yo'q",
                "condition: service_healthy servis healthcheck'dan o'tguncha kutadi",
                "depends_on servis ishga tushguncha kutadi",
                "condition faqat production uchun"
            ],
            "correct": 1,
            "explanation": "Oddiy depends_on container ishga tushishi bilanoq davom etadi. condition: service_healthy esa healthcheck muvaffaqiyatli bo'lguncha kutadi — bu to'g'ri yo'l."
        },
    ],

    "python_pro": [
        {
            "question": "Python asyncio.gather() va ketma-ket await farqi?",
            "options": [
                "Hech qanday farq yo'q",
                "gather() coroutine'larni parallel ishga tushiradi",
                "gather() faqat 2 ta coroutine bilan ishlaydi",
                "gather() CPU intensiv vazifalar uchun"
            ],
            "correct": 1,
            "explanation": "asyncio.gather() bir necha coroutine'ni bir vaqtda (concurrent) ishga tushiradi. Ketma-ket await esa har birini bittama-bitta kutadi — bu I/O intensive vazifalar uchun to'g'ri."
        },
        {
            "question": "Python __slots__ nima uchun ishlatiladi?",
            "options": [
                "Method'larni qulflash",
                "Attribute'larni cheklash va xotira tejash",
                "Class'ni meros olishdan himoya",
                "Faqat type checking uchun"
            ],
            "correct": 1,
            "explanation": "__slots__ instance attribute'larni saqlash uchun dict o'rniga C struct ishlatadi. Bu ~50-80% kam xotira sarflaydi, ayniqsa ko'p instance yaratganda."
        },
        {
            "question": "Python Generator nima afzalligi bor?",
            "options": [
                "Har doim function'dan tezroq",
                "Lazy evaluation — qiymatlar kerak bo'lganda hisoblanadi, xotira tejaydi",
                "Faqat async bilan ishlaydi",
                "Thread-safe"
            ],
            "correct": 1,
            "explanation": "Generator lazy evaluation qiladi — barcha qiymatlarni xotirada saqlamaydi, balki kerak bo'lganda hisoblab beradi. Bu katta ma'lumotlar bilan ishlashda muhim."
        },
        {
            "question": "functools.wraps(func) nima qiladi?",
            "options": [
                "Funksiyani tezlashtiradi",
                "Wrapper funksiya original funksiya metadata'sini saqlaydi",
                "Funksiyani cache'laydi",
                "Exception'larni tutib oladi"
            ],
            "correct": 1,
            "explanation": "@functools.wraps(func) dekoratorda wrapper funksiyaga original funksiya __name__, __doc__, __module__ kabi atributlarini ko'chiradi. Bu debugging va introspection uchun muhim."
        },
    ],

    "sql_mastery": [
        {
            "question": "SQL Window Function RANK() va ROW_NUMBER() farqi?",
            "options": [
                "Hech qanday farq yo'q",
                "RANK() teng qiymatlar uchun bir xil raqam beradi (bo'shliq qoldiradi), ROW_NUMBER() har doim unikal",
                "ROW_NUMBER() tezroq",
                "RANK() faqat NUMBER ustunlar uchun"
            ],
            "correct": 1,
            "explanation": "RANK() teng qiymatlar uchun bir xil raqam beradi va keyingi raqamni o'tkazib yuboradi (1,1,3). ROW_NUMBER() esa har qatorga unikal raqam beradi (1,2,3)."
        },
        {
            "question": "PostgreSQL Partial Index qachon foydali?",
            "options": [
                "Har doim oddiy index'dan yaxshi",
                "Ma'lum shartga mos qatorlar uchun kichikroq, tezroq index",
                "Faqat STRING ustunlar uchun",
                "Hech qachon foydali emas"
            ],
            "correct": 1,
            "explanation": "Partial index WHERE sharti bilan faqat muayyan qatorlarga index quriladi. Masalan, faqat active foydalanuvchilar uchun index — bu ancha kichik va tezroq."
        },
        {
            "question": "Redis Sorted Set asosiy foydalanish holati?",
            "options": [
                "Faqat string saqlash",
                "Leaderboard — score bo'yicha tartiblangan ro'yxat",
                "Database backup",
                "Session saqlash"
            ],
            "correct": 1,
            "explanation": "Sorted Set har elementga score beradi va ularni doim tartibda saqlaydi. ZADD/ZRANGE O(log N) — leaderboard, reytinglar, vaqt oralig'i bo'yicha qidirish uchun ideal."
        },
    ],
}
