"""src/mega_quizzes.py — Barcha mavzular uchun quizlar (v11)"""

MEGA_QUIZZES = {

    "kubernetes": [
        {
            "question": "Kubernetes'da Pod va Container farqi nima?",
            "options": [
                "Pod va Container bir xil narsa",
                "Pod — eng kichik deploy birligi, bir yoki ko'p container o'z ichiga oladi",
                "Container — eng kichik deploy birligi",
                "Pod faqat Linux'da ishlaydi"
            ],
            "correct": 1,
            "explanation": "Pod K8s'dagi eng kichik ishga tushiriladigan birlik. Bir pod ichida sidecar pattern bilan bir necha container bo'lishi mumkin."
        },
        {
            "question": "Kubernetes Service turlari qaysilar?",
            "options": [
                "Faqat ClusterIP va NodePort",
                "ClusterIP, NodePort, LoadBalancer, ExternalName",
                "Faqat LoadBalancer",
                "HTTP, HTTPS, TCP"
            ],
            "correct": 1,
            "explanation": "K8s'da 4 turdagi Service bor: ClusterIP (ichki), NodePort (tashqi port), LoadBalancer (bulut LB), ExternalName (DNS alias)."
        },
        {
            "question": "ConfigMap va Secret farqi nima?",
            "options": [
                "Hech qanday farq yo'q",
                "ConfigMap oddiy config, Secret base64 encoded (maxfiy) ma'lumot",
                "Secret shifrlangan, ConfigMap emas",
                "ConfigMap faqat env uchun, Secret faqat fayl uchun"
            ],
            "correct": 1,
            "explanation": "ConfigMap oddiy konfiguratsiya (non-sensitive), Secret esa base64 encoded maxfiy ma'lumotlar (parol, token). Diqqat: Secret base64 — bu shifrlash emas!"
        },
        {
            "question": "kubectl get pods -n prod buyrug'ida -n nima?",
            "options": [
                "Node nomini belgilaydi",
                "Namespace'ni belgilaydi",
                "Network policy",
                "Replica sonini belgilaydi"
            ],
            "correct": 1,
            "explanation": "-n yoki --namespace flagi qaysi namespace'da ishlashni belgilaydi. Har bir namespace izolyatsiyalangan resurslar to'plamiga ega."
        },
        {
            "question": "HPA (Horizontal Pod Autoscaler) nima qiladi?",
            "options": [
                "Pod hajmini (CPU/RAM) oshiradi",
                "Pod sonini metrikaga qarab avtomatik o'zgartiradi",
                "Node'larni avtomatik qo'shadi",
                "Faqat memory metrikasi asosida ishlaydi"
            ],
            "correct": 1,
            "explanation": "HPA CPU, memory yoki custom metrika asosida pod replikalar sonini avtomatik oshiradi yoki kamaytiradi. VPA esa pod hajmini o'zgartiradi."
        },
    ],

    "rust_lang": [
        {
            "question": "Rust'da Ownership (egalik) qoidasi nima?",
            "options": [
                "Har qiymatning bir necha egasi bo'lishi mumkin",
                "Har qiymatning faqat bitta egasi bor, scope'dan chiqsa drop bo'ladi",
                "Barcha qiymatlar global",
                "Egalik faqat struct'lar uchun"
            ],
            "correct": 1,
            "explanation": "Rust'da har qiymatning bitta egasi (owner) bo'ladi. Ega scope'dan chiqganda qiymat avtomatik yo'q qilinadi (drop). Bu GC'siz xotira xavfsizligini ta'minlaydi."
        },
        {
            "question": "Rust'da &T va &mut T farqi nima?",
            "options": [
                "Hech qanday farq yo'q",
                "&T immutable borrow, &mut T mutable borrow — bir vaqtda bitta mutable borrow",
                "&mut T faqat thread'lar uchun",
                "&T faqat primitiv tiplar uchun"
            ],
            "correct": 1,
            "explanation": "Rust'da bir vaqtda cheksiz immutable borrow (&T) yoki bitta mutable borrow (&mut T) bo'lishi mumkin — ikkalasi bir vaqtda bo'lmaydi. Bu data race'ni compile vaqtida oldini oladi."
        },
        {
            "question": "Rust'da Result<T, E> nima uchun ishlatiladi?",
            "options": [
                "Faqat async funksiyalar uchun",
                "Muvaffaqiyatli qiymat (Ok) yoki xato (Err) qaytarish uchun",
                "Faqat fayl operatsiyalari uchun",
                "Thread xatoliklar uchun"
            ],
            "correct": 1,
            "explanation": "Result<T, E> — Rust'da xatoliklarni boshqarish asosiy mexanizmi. Ok(value) yoki Err(error) qaytaradi. ? operatori bilan qisqartirish mumkin."
        },
        {
            "question": "Rust trait nima?",
            "options": [
                "C++ class'iga o'xshash",
                "Tiplarga xulq-atvor (method) belgilaydigan interfeys",
                "Faqat standart kutubxona uchun",
                "Python decorator'ga o'xshash"
            ],
            "correct": 1,
            "explanation": "Trait — tiplaarga umumiy xulq-atvor belgilaydigan interfeys. Go'dagi interface, Java'dagi interface'ga o'xshash. Polimorfizm uchun ishlatiladi."
        },
        {
            "question": "Rust'da String va &str farqi?",
            "options": [
                "Bir xil",
                "String — owned, heap'da o'suvchi; &str — borrowed, o'zgarmas string slice",
                "&str faqat static string uchun",
                "String faqat UTF-16"
            ],
            "correct": 1,
            "explanation": "String — heap'da saqlanadigan, o'sishi mumkin bo'lgan owned string. &str — ixtiyoriy joyda (stack, heap, binary) saqlanadigan string slice (borrow)."
        },
    ],

    "golang": [
        {
            "question": "Go'da goroutine nima?",
            "options": [
                "Java Thread'iga o'xshash og'ir jarayon",
                "Go runtime tomonidan boshqariladigan yengil vaznli concurrent ijro birligi",
                "Faqat network uchun",
                "OS thread'i"
            ],
            "correct": 1,
            "explanation": "Goroutine — Go runtime boshqaradigan yengil vaznli thread. Boshlang'ich stack ~2KB, OS thread'i esa ~1MB. Bir dasturda millionlab goroutine bo'lishi mumkin."
        },
        {
            "question": "Go'da channel nima uchun ishlatiladi?",
            "options": [
                "Faqat error xabarlar uchun",
                "Goroutine'lar o'rtasida xavfsiz ma'lumot uzatish uchun",
                "Faqat HTTP uchun",
                "Database ulanish uchun"
            ],
            "correct": 1,
            "explanation": "Channel — goroutine'lar o'rtasida ma'lumot almashish va sinxronizatsiya uchun. 'Do not communicate by sharing memory; share memory by communicating' — Go falsafasi."
        },
        {
            "question": "Go'da defer nima qiladi?",
            "options": [
                "Funksiyani keyinga qoldiradi",
                "Funksiya qaytishidan oldin bajariladigan kod qo'shadi (LIFO tartibida)",
                "Goroutine yaratadi",
                "Xatoni ushlaydi"
            ],
            "correct": 1,
            "explanation": "defer — funksiya qaytishidan oldin bajariladigan operatsiyalarni ro'yxatga qo'shadi. Bir necha defer LIFO tartibida bajariladi. Resurs tozalash (file.Close()) uchun ideal."
        },
        {
            "question": "Go'da interface nima?",
            "options": [
                "Faqat struct uchun",
                "Method to'plamini belgilaydigan tip; implicit implementation",
                "Java interface'i bilan bir xil",
                "Faqat error uchun"
            ],
            "correct": 1,
            "explanation": "Go interface'i — method to'plamini belgilaydi. Eng muhimi: implementation implicit (implements kalit so'zi yo'q). Biror tip kerakli methodlarni implement qilsa, u interface'ni qondiradi."
        },
        {
            "question": "Go'da slice va array farqi?",
            "options": [
                "Bir xil",
                "Array o'lcham fixed, slice — dinamik o'lchamli array'ga reference",
                "Slice faqat string uchun",
                "Array heap'da, slice stack'da"
            ],
            "correct": 1,
            "explanation": "Array'ning o'lchami aniq va o'zgarmas ([5]int). Slice esa array'ga pointer + len + cap. append() bilan o'sishi mumkin. Amalda ko'pincha slice ishlatiladi."
        },
    ],

    "microservices": [
        {
            "question": "Microservices va Monolith asosiy farqi nima?",
            "options": [
                "Microservices har doim tezroq",
                "Microservices — mustaqil deploy qilinadigan kichik servislar; Monolith — yagona yirik ilova",
                "Monolith faqat eski texnologiya",
                "Microservices faqat bulutda ishlaydi"
            ],
            "correct": 1,
            "explanation": "Monolith — bir butun ilova. Microservices — har biri mustaqil deploy, scale, develop qilinadigan kichik servislar to'plami. Murakkablik oshadi, lekin mustaqillik kuchayadi."
        },
        {
            "question": "API Gateway nima vazifa bajaradi?",
            "options": [
                "Faqat load balancing",
                "Barcha client so'rovlari uchun yagona kirish nuqtasi: routing, auth, rate limit, logging",
                "Database ulanishlarini boshqarish",
                "Faqat SSL termination"
            ],
            "correct": 1,
            "explanation": "API Gateway — client va mikroservislar orasidagi vositachi. Routing, authentication, rate limiting, logging, SSL termination, response caching kabi vazifalarni bajaradi."
        },
        {
            "question": "Circuit Breaker pattern nima?",
            "options": [
                "Elektr simlarni himoya qilish",
                "Xato beruvchi servislarga so'rov yuborishni vaqtincha to'xtatib, kaskad xatoni oldini oluvchi pattern",
                "Faqat timeout boshqarish",
                "Database connection pool"
            ],
            "correct": 1,
            "explanation": "Circuit Breaker — bir servis ishlamay qolganda boshqa servislar ham xisorat ko'rmasligi uchun. Closed→Open→Half-Open holatlari. Hystrix, Resilience4j kutubxonalari."
        },
        {
            "question": "Event Sourcing pattern nima?",
            "options": [
                "Real-time event streaming",
                "Tizim holatini o'zgarishlar (event'lar) ketma-ketligi sifatida saqlash",
                "Faqat Kafka uchun",
                "Database trigger'lar"
            ],
            "correct": 1,
            "explanation": "Event Sourcing — joriy holatni saqlash o'rniga barcha o'zgarishlarni (event) ketma-ketligini saqlaydi. Audit log, time travel, event replay imkoniyati."
        },
        {
            "question": "Saga pattern qaysi muammoni hal qiladi?",
            "options": [
                "Tezlikni oshirish",
                "Distributed transaction — bir necha mikroservis bo'ylab atomik operatsiyalarni boshqarish",
                "Faqat read operatsiyalar uchun",
                "Database sharding"
            ],
            "correct": 1,
            "explanation": "Saga — distributed tizimda 2PC (two-phase commit) o'rniga. Har bir qadam lokal transaction, muvaffaqiyatsizlikda compensating transaction bajaradi. Choreography va Orchestration turlari bor."
        },
    ],

    "system_design": [
        {
            "question": "CAP teoremasi nima?",
            "options": [
                "CPU, Aniq, Parallel",
                "Consistency, Availability, Partition tolerance — distributed tizim uchburchak kompromis",
                "Cache, API, Protocol",
                "Cloud, Architecture, Performance"
            ],
            "correct": 1,
            "explanation": "CAP teoremasi: distributed tizimda Consistency (barcha node bir xil ma'lumot ko'radi), Availability (har doim javob beradi), Partition tolerance (tarmoq uzilishda ishlaydi) — faqat ikkitasini kafolatlash mumkin."
        },
        {
            "question": "Horizontal va Vertical scaling farqi?",
            "options": [
                "Bir xil narsa",
                "Vertical: kuchliroq server; Horizontal: ko'proq server qo'shish",
                "Horizontal faqat cloud uchun",
                "Vertical database uchun, Horizontal web uchun"
            ],
            "correct": 1,
            "explanation": "Vertical scaling (scale up) — mavjud serverga ko'proq CPU/RAM. Horizontal scaling (scale out) — ko'proq server qo'shish. Horizontal cheksiz o'sadi, Vertical chekli."
        },
        {
            "question": "CDN (Content Delivery Network) nima uchun?",
            "options": [
                "Database tezlashtirish",
                "Statik kontentni foydalanuvchiga yaqin edge server'lardan xizmat qilish, kechikishni kamaytirish",
                "Faqat video streaming uchun",
                "API gateway o'rniga"
            ],
            "correct": 1,
            "explanation": "CDN — statik fayllarni (HTML, CSS, JS, rasm, video) dunyo bo'ylab edge server'larda keshlaydi. Foydalanuvchi eng yaqin serverdan oladi → kam latency, kam origin server yuki."
        },
        {
            "question": "Database sharding nima?",
            "options": [
                "Database'ni zaxiralash",
                "Ma'lumotlarni bir necha database'ga bo'lib joylashtirish (gorizontal partitioning)",
                "Database replikatsiyasi",
                "Database shifrlash"
            ],
            "correct": 1,
            "explanation": "Sharding — katta dataset'ni bir necha database server'ga (shard) bo'lish. Har shard ma'lumotning bir qismini saqlaydi. User_id % N kabi sharding key ishlatiladi."
        },
        {
            "question": "Rate Limiting nima uchun kerak?",
            "options": [
                "Serverlarni yangilash uchun",
                "API suiiste'molidan himoya — foydalanuvchi ma'lum vaqt oralig'ida cheklangan so'rov yuboradi",
                "Faqat pullik API uchun",
                "Database ulanishlarni cheklash"
            ],
            "correct": 1,
            "explanation": "Rate Limiting — DDoS, brute force hujumlardan himoya va resurslarni adolatli taqsimlash. Token Bucket, Sliding Window, Fixed Window algoritmlari. Redis bilan implementatsiya."
        },
    ],

    "graphql": [
        {
            "question": "GraphQL va REST API asosiy farqi nima?",
            "options": [
                "GraphQL faqat mobile uchun",
                "GraphQL — client kerakli fieldlarni o'zi belgilaydi (over/under-fetching yo'q)",
                "REST tezroq",
                "GraphQL faqat Facebook uchun"
            ],
            "correct": 1,
            "explanation": "REST'da endpoint ma'lum ma'lumot qaytaradi (over-fetching yoki under-fetching). GraphQL'da client query'da aynan kerakli fieldlarni so'raydi — ortiqcha ma'lumot yo'q."
        },
        {
            "question": "GraphQL Schema'da Mutation nima?",
            "options": [
                "Ma'lumot o'qish operatsiyasi",
                "Ma'lumotni o'zgartirish (create, update, delete) operatsiyasi",
                "Subscription bilan bir xil",
                "Faqat autentifikatsiya uchun"
            ],
            "correct": 1,
            "explanation": "GraphQL'da: Query — o'qish, Mutation — yozish/o'zgartirish/o'chirish, Subscription — real-time yangilanishlar (WebSocket). REST'dagi POST/PUT/DELETE ekvivalenti."
        },
        {
            "question": "N+1 muammosi GraphQL'da nima?",
            "options": [
                "N ta field qaytarish",
                "Asosiy so'rovdan so'ng har bir element uchun alohida so'rov yuborilishi — samarasiz",
                "N ta foydalanuvchi uchun 1 ta so'rov",
                "GraphQL versiya muammosi"
            ],
            "correct": 1,
            "explanation": "N+1: 1 ta query barcha userlarni olib, har bir user uchun alohida query yuboradi = N+1 query. DataLoader (batching) bilan hal qilinadi: barcha ID'lar yig'ilib, bitta so'rovda olinadi."
        },
        {
            "question": "GraphQL Fragment nima?",
            "options": [
                "Xato fragmentlari",
                "Qayta ishlatiladigan field to'plamlari — bir necha query'da ishlatish uchun",
                "GraphQL server komponenti",
                "Cache fragment"
            ],
            "correct": 1,
            "explanation": "Fragment — qayta ishlatiladigan field to'plami. Masalan: fragment UserFields on User { id name email } — bir necha query'da ishlatish mumkin. DRY prinsipi."
        },
    ],

    "postgres_pro": [
        {
            "question": "PostgreSQL MVCC nima?",
            "options": [
                "Multi-Version Concurrency Control — har bir transaction ma'lumotning o'z versiyasini ko'radi",
                "Multiple Virtual CPU Control",
                "Master-Version Cache Control",
                "Faqat read operatsiyalar uchun"
            ],
            "correct": 0,
            "explanation": "MVCC — PostgreSQL'ning asosiy concurrency mexanizmi. Har bir transaction o'z snapshot'ini ko'radi. Write'lar read'larni bloklamaydi. Eski versiyalar VACUUM bilan tozalanadi."
        },
        {
            "question": "EXPLAIN ANALYZE nima qiladi?",
            "options": [
                "Faqat query matnini ko'rsatadi",
                "Query execution plan'ini ko'rsatadi VA aslida bajaradi — real vaqt va qator soni bilan",
                "Index yaratadi",
                "Query'ni optimallashtiradi"
            ],
            "correct": 1,
            "explanation": "EXPLAIN — faqat plan ko'rsatadi (bajarmaydi). EXPLAIN ANALYZE — rejani ham ko'rsatadi, ham bajaradi, real vaqt va qator sonini o'lchaydi. Index ishlatyaptimi, Seq Scan bormi?"
        },
        {
            "question": "PostgreSQL GIN index qachon ishlatiladi?",
            "options": [
                "Oddiy integer ustunlar uchun",
                "Full-text search, JSONB, array va composite tiplar uchun — ko'p qiymatli tuzilmalar",
                "Faqat primary key uchun",
                "Faqat geometry ma'lumotlar uchun"
            ],
            "correct": 1,
            "explanation": "GIN (Generalized Inverted Index) — bir qiymat ichida ko'p element bo'lgan holatlar uchun: tsvector (full-text), JSONB, array. B-tree'dan sekin yaratiladim, lekin tezroq qidiradi."
        },
        {
            "question": "PostgreSQL autovacuum nima qiladi?",
            "options": [
                "Disk tozalash",
                "Dead tuple'larni va bloated'larni tozalab, statistikani yangilab, query plannerga yordam beradi",
                "Faqat index defragmentatsiya",
                "Kunlik backup"
            ],
            "correct": 1,
            "explanation": "MVCC tufayli yangilangan va o'chirilgan qatorlar 'dead tuple' bo'lib qoladi. Autovacuum ularni tozalaydi, statistikani yangilaydi, table bloating oldini oladi."
        },
        {
            "question": "pg_stat_statements nima uchun?",
            "options": [
                "Server statistikasi",
                "Barcha SQL so'rovlar statistikasini yig'ib, sekin query'larni aniqlashga yordam beradi",
                "Faqat DBA uchun",
                "Replikatsiya statistikasi"
            ],
            "correct": 1,
            "explanation": "pg_stat_statements extension — har bir unique query uchun calls, total_time, mean_time, rows statistikasini yig'adi. Sekin query'larni topishning eng yaxshi yo'li."
        },
    ],

    "redis_deep": [
        {
            "question": "Redis Pub/Sub va Stream farqi nima?",
            "options": [
                "Bir xil narsa",
                "Pub/Sub — fire-and-forget (tarix saqlanmaydi); Stream — persistent, consumer group bilan",
                "Stream faqat Redis 6+ da",
                "Pub/Sub tezroq, Stream ishonchliroq"
            ],
            "correct": 1,
            "explanation": "Pub/Sub: xabar subscribe bo'lmaganlarga yo'qoladi, tarix yo'q. Redis Stream: Kafka'ga o'xshash persistent log, consumer group, message acknowledge, replay imkoniyati."
        },
        {
            "question": "Redis persistence qanday ishlaydi?",
            "options": [
                "Faqat RAM'da saqlaydi",
                "RDB (snapshot) va AOF (append-only log) — ikki xil persistence mexanizmi",
                "Faqat SSD'da",
                "Har daqiqada avtomatik backup"
            ],
            "correct": 1,
            "explanation": "RDB — ma'lum vaqt oralig'ida snapshot. AOF — har write operatsiyani logga yozadi. Ikkalasini birga ishlatish: AOF = ishonchlilik, RDB = tez restart. Redis 7+ da RDB+AOF."
        },
        {
            "question": "Redis Sentinel nima uchun?",
            "options": [
                "Redis monitoring faqat",
                "High Availability: master monitoring, automatic failover, client'larga yangi master haqida xabar",
                "Redis cluster'ni boshqarish",
                "Redis xavfsizligi"
            ],
            "correct": 1,
            "explanation": "Sentinel — HA (High Availability) uchun. Master'ni kuzatadi, ishlamay qolsa replica'ni master'ga ko'taradi (failover), client'larni yangi master haqida xabardor qiladi."
        },
        {
            "question": "Redis Cluster nima imkoniyat beradi?",
            "options": [
                "Faqat replikatsiya",
                "Horizontal scaling — ma'lumotlarni bir necha node bo'ylab tarqatish (sharding) + HA",
                "Faqat read performance",
                "Faqat Linux'da ishlaydi"
            ],
            "correct": 1,
            "explanation": "Redis Cluster — 16384 hash slot'ni bir necha master node'ga bo'lib, horizontal sharding ta'minlaydi. Har master'ga replica'lar ham qo'shiladi. Sentinel'siz mustaqil HA."
        },
        {
            "question": "Redis MULTI/EXEC nima?",
            "options": [
                "Multi-threading",
                "Transaction: MULTI boshlanadi, EXEC bilan atomik bajariladi — oradagi buyruqlar queue'da turadi",
                "Faqat Lua script uchun",
                "Parallel execution"
            ],
            "correct": 1,
            "explanation": "MULTI/EXEC — Redis transaction. MULTI dan EXEC gacha buyruqlar queue'ga qo'yiladi, EXEC bilan hammasi atomik bajariladi. WATCH bilan optimistic locking ham mumkin."
        },
    ],

    "terraform": [
        {
            "question": "Terraform state nima uchun kerak?",
            "options": [
                "Faqat log saqlash",
                "Haqiqiy infrastruktura holati bilan Terraform konfiguratsiyasini solishtirish uchun xotira",
                "Faqat AWS uchun",
                "Terraform versiyasini saqlash"
            ],
            "correct": 1,
            "explanation": "State — Terraform'ning infrastruktura haqidagi xotirasi. Remote state (S3+DynamoDB) — jamoa bilan ishlashda lock va sharing uchun. State olmasa, Terraform nima bor-yo'qni bilmaydi."
        },
        {
            "question": "terraform plan va terraform apply farqi?",
            "options": [
                "Bir xil narsa",
                "plan — o'zgarishlarni preview ko'rsatadi (hech narsa yaratmaydi); apply — aslida yaratadi",
                "plan faqat delete uchun",
                "apply faqat CI/CD uchun"
            ],
            "correct": 1,
            "explanation": "terraform plan — dry-run, nima yaratiladi/o'zgaradi/o'chirilishini ko'rsatadi. terraform apply — plan'ni bajarib, haqiqatan infrastruktura yaratadi/o'zgartiradi."
        },
        {
            "question": "Terraform module nima?",
            "options": [
                "Plugin",
                "Qayta ishlatiladigan infrastruktura kodi to'plami — bir necha resurslrni birga paketlash",
                "Faqat AWS uchun modul",
                "Terraform versiya boshqarish"
            ],
            "correct": 1,
            "explanation": "Module — qayta ishlatiladigan Terraform kodi. Masalan: VPC module bir marta yoziladi, bir necha environment'da chaqiriladi. Terraform Registry'da ommaviy modullar bor."
        },
        {
            "question": "Terraform import nima qiladi?",
            "options": [
                "Boshqa cloud provayderdan ko'chirish",
                "Mavjud (Terraform tashqarisida yaratilgan) resursni Terraform state'ga qo'shish",
                "Terraform fayllarni import qilish",
                "Provider'ni o'rnatish"
            ],
            "correct": 1,
            "explanation": "terraform import — allaqachon mavjud bo'lgan (masalan, qo'lda yaratilgan) cloud resursini Terraform state'ga qo'shadi. Shundan keyin Terraform uni boshqara oladi."
        },
    ],

    "cicd_github": [
        {
            "question": "GitHub Actions workflow trigger'lari qanday belgilanadi?",
            "options": [
                "Faqat push uchun",
                "on: kalit so'zi bilan: push, pull_request, schedule, workflow_dispatch va boshqalar",
                "Faqat YAML'da emas",
                "Faqat main branch uchun"
            ],
            "correct": 1,
            "explanation": "GitHub Actions on: bilan trigger'lar belgilanadi: push (branch/tag), pull_request, schedule (cron), workflow_dispatch (qo'lda), release, issues va boshqalar."
        },
        {
            "question": "GitHub Actions artifact nima?",
            "options": [
                "GitHub badge",
                "Workflow steps o'rtasida yoki run'lar o'rtasida saqlanadigan fayl/ma'lumot",
                "Faqat Docker image",
                "GitHub package"
            ],
            "correct": 1,
            "explanation": "Artifact — workflow ichida yaratilgan fayllar (test report, build output, binary). actions/upload-artifact va download-artifact bilan job'lar yoki run'lar o'rtasida almashish mumkin."
        },
        {
            "question": "CI/CD'da 'Shift Left' nima?",
            "options": [
                "Pipeline'ni chapga siljitish",
                "Xato topish va xavfsizlik tekshiruvlarini rivojlanish jarayonining ilk bosqichlariga o'tkazish",
                "Kodni chapdan o'ngga o'qish",
                "CI server'ni local'ga ko'chirish"
            ],
            "correct": 1,
            "explanation": "Shift Left — xatolarni iloji boricha erta topish. Developer kompyuterida linting, test, SAST — production'ga yetib kelishidan avval muammolarni hal qilish. Arzonroq va tezroq."
        },
        {
            "question": "Blue-Green deployment nima?",
            "options": [
                "Rang-barang UI",
                "Ikki identik muhit: Blue (joriy), Green (yangi) — trafikni bir zumda o'tkazish va rollback imkoniyati",
                "Faqat Kubernetes uchun",
                "A/B testing"
            ],
            "correct": 1,
            "explanation": "Blue-Green: ikkala muhit tayyor turadi. Yangi versiya Green'ga deploy qilinadi, test o'tilgach trafikni Green'ga o'tkazish bir zumda bo'ladi. Muammo bo'lsa Blue'ga qaytish oson."
        },
    ],

    "pytorch_basics": [
        {
            "question": "PyTorch Tensor nima?",
            "options": [
                "Python list'i",
                "GPU'da ham ishlaydigan ko'p o'lchamli array — deep learning hisoblash asosi",
                "Faqat 2D matrix",
                "NumPy array bilan bir xil"
            ],
            "correct": 1,
            "explanation": "Tensor — ko'p o'lchamli (n-dimensional) array. NumPy'ga o'xshash, lekin GPU (CUDA) da ishlaydi va autograd (avtomatik differensiatsiya) qo'llab-quvvatlaydi."
        },
        {
            "question": "Backpropagation nima?",
            "options": [
                "Ma'lumot o'qish jarayoni",
                "Xato gradientini chiqishdan kirishga qarab hisoblash — model parametrlarini yangilash uchun",
                "Faqat CNN uchun",
                "Forward pass ning teskarisi"
            ],
            "correct": 1,
            "explanation": "Backpropagation — zanjir qoidasi (chain rule) yordamida har bir parametrning xatoga hissasini (gradient) hisoblaydi. PyTorch'da loss.backward() bilan avtomatik bajariladi."
        },
        {
            "question": "PyTorch'da model.eval() nima uchun?",
            "options": [
                "Modelni o'chirish",
                "Modelni inference rejimiga o'tkazish: Dropout o'chiriladi, BatchNorm inference holatida ishlaydi",
                "Faqat evaluation metrikasi hisoblash",
                "GPU'dan CPU'ga o'tkazish"
            ],
            "correct": 1,
            "explanation": "model.eval() — inference/test uchun. Dropout (training'da random neuron o'chiradi) to'xtatiladi, BatchNorm training statistikasi o'rniga running stats ishlatadi. model.train() training uchun."
        },
        {
            "question": "Overfitting nima va qanday oldini olish mumkin?",
            "options": [
                "Model xato",
                "Model train data'ni yod olib, yangi ma'lumotlarga umumlashmasligi — Dropout, Regularization, Data Augmentation bilan oldini olish",
                "Faqat katta modellarda",
                "GPU muammosi"
            ],
            "correct": 1,
            "explanation": "Overfitting — model training data'ga juda moslashib, test/validation data'da yomon ishlaydi. Oldini olish: Dropout, L1/L2 regularization, data augmentation, early stopping, ko'proq data."
        },
    ],

    "mlops_intro": [
        {
            "question": "MLOps nima?",
            "options": [
                "Machine Learning optimizatsiya",
                "ML modellarni production'ga deploy va boshqarishni avtomatlashtirish: CI/CD + monitoring + retraining",
                "Faqat model training",
                "Data engineering"
            ],
            "correct": 1,
            "explanation": "MLOps = ML + DevOps + Data Engineering. Model training'dan production'gacha: versioning, CI/CD pipeline, serving, monitoring, drift detection, retraining avtomatsiyasi."
        },
        {
            "question": "Model Registry nima uchun?",
            "options": [
                "Model litsenziya",
                "Trained model'larni versiyalash, metadata saqlash, lifecycle boshqarish uchun markaziy omborxona",
                "Faqat MLflow uchun",
                "Model download qilish"
            ],
            "correct": 1,
            "explanation": "Model Registry — MLflow, DVC, W&B kabi. Har model versiyasi uchun: metrics, parameters, artifacts saqlanadi. Staging→Production lifecycle boshqariladi."
        },
        {
            "question": "Data Drift nima?",
            "options": [
                "Ma'lumot o'chirilishi",
                "Production'dagi input ma'lumotlar taqsimoti training ma'lumotlardan farq qila boshlashi — model degradatsiyasi",
                "Database migratsiyasi",
                "Faqat NLP'da"
            ],
            "correct": 1,
            "explanation": "Data Drift — production'da model ko'rgan ma'lumotlar training'dan farq qilishi. Model accuracy tushadi. Evidently, WhyLabs kabi monitoring vositalar drift'ni aniqlaydi va retraining trigger qiladi."
        },
        {
            "question": "Feature Store nima?",
            "options": [
                "Model do'koni",
                "ML feature'larni markazlashgan saqlash, hisoblash va serving uchun platforma — training/inference uchun bir xil feature'lar",
                "Faqat real-time feature'lar uchun",
                "Data warehouse"
            ],
            "correct": 1,
            "explanation": "Feature Store — Feast, Tecton kabi. Feature'larni bir marta hisoblaydi, training va inference'da bir xil qiymatlar ishlatiladi. Training-serving skew'ni oldini oladi."
        },
    ],

    "zero_trust": [
        {
            "question": "Zero Trust xavfsizlik modeli asosi nima?",
            "options": [
                "Hamma'ga ishon",
                "'Hech kimga ishonma, hammasini tekshir' — tarmoq perimetri o'rniga identifikatsiya asosida kirish",
                "Faqat tashqi foydalanuvchilarni tekshirish",
                "VPN ga tayanish"
            ],
            "correct": 1,
            "explanation": "Zero Trust: 'Never trust, always verify'. Ichki tarmoqdagi foydalanuvchi ham tekshiriladi. Micro-segmentation, least privilege, MFA, continuous verification asosiy prinsiplar."
        },
        {
            "question": "Least Privilege prinsipi nima?",
            "options": [
                "Kam huquq berish yaxshi emas",
                "Har foydalanuvchi/servisga faqat kerakli minimal ruxsatlar berish",
                "Admin huquqlarini kamaytirish",
                "Faqat cloud uchun"
            ],
            "correct": 1,
            "explanation": "Least Privilege (minimal ruxsat) — foydalanuvchi yoki servisga faqat vazifasi uchun kerakli minimal huquqlar beriladi. Buzg'unchi kirsa, zarar minimallashtriladi."
        },
        {
            "question": "mTLS (Mutual TLS) nima?",
            "options": [
                "Faqat server sertifikat taqdim etadi",
                "Ikki tomon ham sertifikat taqdim etadi — servislar o'rtasida ikki tomonlama autentifikatsiya",
                "Multi-threaded TLS",
                "Faqat HTTPS uchun"
            ],
            "correct": 1,
            "explanation": "mTLS — oddiy TLS'da faqat server sertifikat ko'rsatadi. mTLS'da client ham sertifikat ko'rsatadi. Mikroservislar o'rtasida (service mesh: Istio, Linkerd) keng ishlatiladi."
        },
        {
            "question": "SIEM nima?",
            "options": [
                "Dasturlash tili",
                "Security Information and Event Management — log yig'ish, tahlil, real-time alert uchun platforma",
                "Faqat firewall boshqaruv",
                "Antivirus dastur"
            ],
            "correct": 1,
            "explanation": "SIEM (Splunk, QRadar, Microsoft Sentinel) — barcha tizimlardan log'larni yig'adi, korrelyatsiya qiladi, anomaliya aniqlaydi va real-time alert beradi. SOC jamoasining asosiy vositasi."
        },
    ],

    "devops_cicd": [
        {
            "question": "DORA metrikalaridan 'Lead Time for Changes' nima?",
            "options": [
                "Xato tuzatish vaqti",
                "Kod commit'dan production'ga yetguncha o'tgan vaqt",
                "Deployment soni",
                "Server downtime"
            ],
            "correct": 1,
            "explanation": "Lead Time for Changes — developer kod yozgandan production'da ishlagunicha qancha vaqt o'tishi. Elite teams: < 1 soat. Bu CI/CD pipeline samaradorligini o'lchaydi."
        },
        {
            "question": "Infrastructure as Code (IaC) asosiy afzalligi?",
            "options": [
                "Serverlarni arzonlashtirish",
                "Infrastrukturani kod orqali boshqarish: versiyalash, takrorlanish, audit, avtomatizatsiya",
                "Faqat AWS uchun",
                "Manual server sozlash o'rniga GUI"
            ],
            "correct": 1,
            "explanation": "IaC (Terraform, Ansible, Pulumi) — infrastrukturani kod sifatida: Git'da versiyalanadi, review qilinadi, bir xil muhit takrorlanadi, manual xato kamayadi."
        },
        {
            "question": "Canary deployment nima?",
            "options": [
                "Juda tez deploy",
                "Yangi versiyani avval kichik foydalanuvchilar guruhiga chiqarish, muammo yo'q bo'lsa kengaytirish",
                "Blue-green bilan bir xil",
                "Faqat mobile uchun"
            ],
            "correct": 1,
            "explanation": "Canary: yangi versiyani avval 1-5% trafikka chiqarish (canary = kanar qushi, konchilar uni xavfli gaz aniqlash uchun ishlatgan). Metrikalar yaxshi bo'lsa, foiz oshiriladi."
        },
        {
            "question": "Prometheus'da PromQL rate() funksiyasi nima qiladi?",
            "options": [
                "O'rtacha qiymat hisoblaydi",
                "Counter metrika o'sish tezligini sekundiga hisoblaydi (so'nggi N daqiqada)",
                "Maksimal qiymatni topadi",
                "Metrika nomini o'zgartiradi"
            ],
            "correct": 1,
            "explanation": "rate(http_requests_total[5m]) — so'nggi 5 daqiqadagi so'rovlar tezligini sekundiga hisoblaydi. Counter uchun (monoton o'suvchi). irate() — instant rate, oxirgi 2 nuqta asosida."
        },
    ],

    "networking_pro": [
        {
            "question": "TCP Flow Control nima?",
            "options": [
                "Trafikni to'xtatish",
                "Receiver'ning buffer sig'imiga qarab sender tezligini boshqarish — overflow oldini olish",
                "Firewall qoidalari",
                "Faqat UDP uchun"
            ],
            "correct": 1,
            "explanation": "TCP Flow Control — receiver o'zining receive window (rwnd) ni sender'ga bildiradi. Sender window'dan ko'p yubormas. Buffer to'lib qolishidan saqlaydi (receiver overflow)."
        },
        {
            "question": "BGP (Border Gateway Protocol) nima?",
            "options": [
                "LAN protokoli",
                "Internet'dagi AS (Autonomous System) lar o'rtasida routing ma'lumot almashish protokoli",
                "Faqat VPN uchun",
                "DNS protokoli"
            ],
            "correct": 1,
            "explanation": "BGP — internet'ning 'yapıştırıcısı'. ISP'lar, CDN'lar, katta korporatsiyalar o'rtasida qaysi yo'nalishga qaysi AS orqali borish kerakligini hal qiladi. Path vector protokol."
        },
        {
            "question": "HTTPS'da TLS handshake qanday ishlaydi?",
            "options": [
                "Faqat sertifikat almashadi",
                "ClientHello→ServerHello→Certificate→Key Exchange→Finished — session key o'rnatish",
                "Faqat password almashadi",
                "TCP'ning bir qismi"
            ],
            "correct": 1,
            "explanation": "TLS 1.3: ClientHello (cipher suites) → ServerHello+Certificate+Verify → Client Finished → Encrypted application data. TLS 1.3 da 1-RTT (yoki 0-RTT resume) — tezroq."
        },
        {
            "question": "Nginx upstream least_conn nima qiladi?",
            "options": [
                "Eng yaqin serverni tanlaydi",
                "Eng kam active ulanishi bo'lgan serverga yangi so'rov yo'naltiradi",
                "Random server tanlaydi",
                "IP hash asosida"
            ],
            "correct": 1,
            "explanation": "least_conn — load balancing strategiyasi: yangi so'rov eng kam faol ulanishi bo'lgan server'ga yuboriladi. Uzoq davom etuvchi ulanishlar (WebSocket) uchun round-robin'dan yaxshiroq."
        },
    ],

    "git_mastery": [
        {
            "question": "git rebase va git merge farqi?",
            "options": [
                "Bir xil natija, bir xil tarix",
                "merge — branch tarixini saqlaydi (merge commit); rebase — o'zgarishlarni boshqa branch tepasiga ko'chiradi (chiziqli tarix)",
                "rebase xavfli, merge xavfsiz",
                "merge faqat main uchun"
            ],
            "correct": 1,
            "explanation": "merge — ikki branch'ni birlashtiradi, merge commit yaratadi, tarix saqlanadi. rebase — branch'ning bazasini o'zgartiradi, commit'larni qayta yozadi, chiziqli tarix. Shared branch'da rebase xavfli!"
        },
        {
            "question": "git stash nima uchun ishlatiladi?",
            "options": [
                "Commit tarixini tozalash",
                "Uncommitted o'zgarishlarni vaqtincha saqlab, keyinchalik qayta qo'llash uchun",
                "Remote'dan o'chirish",
                "Branch yaratish"
            ],
            "correct": 1,
            "explanation": "git stash — uncommitted o'zgarishlarni stack'ga saqlaydi (clean working dir). git stash pop — oxirgi stash'ni qayta qo'llaydi. Branch'lar o'rtasida o'tishdan oldin qulay."
        },
        {
            "question": "git bisect nima qiladi?",
            "options": [
                "Commit'larni ikki qismga bo'ladi",
                "Ikkilik qidiruv bilan qaysi commit bug'ni kiritganini topadi",
                "Branch'ni ikki qismga ajratadi",
                "Faqat test uchun"
            ],
            "correct": 1,
            "explanation": "git bisect — O(log N) da bug kiritgan commit'ni topadi. git bisect start, git bisect bad (hozir), git bisect good (avval ishlagan) → Git avtomatik commit'larni tekshiradi."
        },
    ],

    "cloud_aws": [
        {
            "question": "AWS IAM Role va User farqi?",
            "options": [
                "Bir xil narsa",
                "User — permanent credentials; Role — vaqtinchalik, servislar yoki cross-account uchun assume qilinadigan",
                "Role faqat EC2 uchun",
                "User faqat CLI uchun"
            ],
            "correct": 1,
            "explanation": "IAM User — doimiy access key/secret. IAM Role — assume qilinadi (EC2, Lambda, boshqa AWS account), vaqtinchalik credentials beradi. Servislar uchun Role ishlatish best practice."
        },
        {
            "question": "AWS S3 versioning nima beradi?",
            "options": [
                "Fayl versiyasini ko'rsatadi",
                "Ob'ektlarning barcha versiyalarini saqlaydi — tasodifiy o'chirish yoki yozib ketishdan himoya",
                "Faqat backup uchun",
                "Faqat yangi fayllar uchun"
            ],
            "correct": 1,
            "explanation": "S3 versioning yoqilganda, har o'zgartirishda yangi versiya ID yaratiladi. O'chirilganda delete marker qo'yiladi (aslida saqlanib qoladi). MFA Delete bilan qo'shimcha himoya."
        },
        {
            "question": "AWS Lambda cold start nima?",
            "options": [
                "Lambda sovuq haroratda ishlaydi",
                "Birinchi yoki uzoq vaqt chaqirilmagan Lambda'ning ishga tushishida kechikish — container initialize qilish",
                "Faqat Python Lambda'da",
                "Lambda timeout"
            ],
            "correct": 1,
            "explanation": "Cold start — Lambda'ning yangi container yaratib, runtime va kod'ni yuklashi. Bir necha millisekund-soniya. Provisioned Concurrency bilan cold start yo'q qilinadi (ammo narxi yuqori)."
        },
    ],

    "security_pro": [
        {
            "question": "SQL injection qanday oldini olinadi?",
            "options": [
                "Input'ni faqat uzunligi tekshiriladi",
                "Parametrized query/prepared statement ishlatish — user input SQL'ga qo'shilmaydi",
                "Faqat HTTPS ishlatish",
                "Admin paroli kuchli bo'lishi"
            ],
            "correct": 1,
            "explanation": "Parametrized query (prepared statement) — SQL skeleti va ma'lumotlar alohida yuboriladi. Ma'lumot hech qachon SQL sifatida talqin qilinmaydi. ORM ham himoya qiladi (to'g'ri ishlatilsa)."
        },
        {
            "question": "XSS (Cross-Site Scripting) nima?",
            "options": [
                "CSS bilan hujum",
                "Saytga zararli script kiritish — boshqa foydalanuvchilar brauzerida bajarilishi",
                "Faqat server tomonidan",
                "SQL injection turi"
            ],
            "correct": 1,
            "explanation": "XSS — foydalanuvchi kiritgan ma'lumot HTML'ga unsafe qo'shilganda, boshqa foydalanuvchilar brauzerida JavaScript bajariladi. Cookie o'g'irlash, defacement. Himoya: output encoding, CSP."
        },
        {
            "question": "CSRF (Cross-Site Request Forgery) nima?",
            "options": [
                "XSS bilan bir xil",
                "Foydalanuvchi autentifikatsiyasidan foydalanib, boshqa saytdan uning nomidan so'rov yuborish",
                "Faqat GET so'rovlarga",
                "Server tomonidan hujum"
            ],
            "correct": 1,
            "explanation": "CSRF — authenticated user boshqa saytdagi zararli linkni bosganda, uning cookie'si bilan haqiqiy saytga so'rov ketadi. Himoya: CSRF token, SameSite cookie, Origin header tekshirish."
        },
        {
            "question": "bcrypt parol xeshlashda nima uchun yaxshi?",
            "options": [
                "SHA-256 dan tezroq",
                "Qasddan sekin (cost factor), salt avtomatik, brute-force qimmatlashtiradi",
                "Reversible",
                "Faqat Linux'da"
            ],
            "correct": 1,
            "explanation": "bcrypt — parol uchun maxsus sekin hash (work factor sozlanadi). Salt avtomatik qo'shiladi (rainbow table yo'q). Hardware tezlashsa, cost factor oshiriladi. MD5/SHA1 parol uchun YAROQSIZ."
        },
    ],

    "web_frontend": [
        {
            "question": "React useMemo va useCallback farqi?",
            "options": [
                "Bir xil narsa",
                "useMemo — qiymat hisoblashni, useCallback — funksiya reference'ni memoize qiladi",
                "useCallback faqat async uchun",
                "useMemo faqat array uchun"
            ],
            "correct": 1,
            "explanation": "useMemo(() => expensiveCalc(a,b), [a,b]) — a yoki b o'zgargandagina qayta hisoblanadi. useCallback(() => fn, [deps]) — deps o'zgarmasa funksiya reference o'zgarmaydi. React.memo bilan birga ishlatiladi."
        },
        {
            "question": "TypeScript 'unknown' va 'any' farqi?",
            "options": [
                "Bir xil narsa",
                "any — type checking yo'q; unknown — type tekshirilmagunicha operatsiya qilolmaydi (xavfsizroq)",
                "unknown faqat function uchun",
                "any faqat library uchun"
            ],
            "correct": 1,
            "explanation": "any — TypeScript'ni o'chiradi, hamma narsa ruxsat. unknown — type narrowing (typeof, instanceof tekshiruvi) qilmagunicha ishlatib bo'lmaydi. Tashqi ma'lumotlar uchun unknown afzal."
        },
        {
            "question": "React Suspense nima uchun?",
            "options": [
                "Animation uchun",
                "Async komponentlar yuklangunicha fallback UI ko'rsatish — lazy loading va data fetching uchun",
                "Faqat React Native uchun",
                "Error handling uchun"
            ],
            "correct": 1,
            "explanation": "Suspense — React.lazy() bilan code splitting, yoki server component'lar yuklanayotganda fallback={<Spinner/>} ko'rsatadi. React 18 da concurrent rendering bilan yanada kuchliroq."
        },
    ],
}
