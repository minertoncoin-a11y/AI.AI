"""src/extended_lessons.py — PRO mavzular va TIL darslari"""

# Murakkab PRO mavzular: dars matnlari (qisqa, lekin texnik chuqurlik).
# extended_curriculum.py faylida QUIZZES bilan birga birlashtiriladi.

EXTENDED_LESSONS = {
    "kubernetes": {
        "title": "☸️ Kubernetes — konteyner orkestratsiyasi (PRO)",
        "lessons": [
            "🎯 DARS 1: Nega Kubernetes?\n"
            "Bare metal → VM → konteyner → pod. K8s podlarni joylashtiradi (scheduling), "
            "sog‘lig‘ini tekshiradi (liveness/readiness), trafikni taqsimlaydi.\n"
            "Asosiy obyektlar: Pod, Deployment, Service, Namespace.\n"
            "Control plane: API server, etcd, scheduler, controller-manager.",

            "🎯 DARS 2: Pod va Deployment\n"
            "Pod — eng kichik ishga tushirish birligi; bir podda bir nechta konteyner (sidecar pattern).\n"
            "Deployment — deklarativ yangilanish: replicas, rolling update, rollback.\n"
            "`kubectl get pods -n prod` — namespace muhitini ajratish.",

            "🎯 DARS 3: Service va DNS\n"
            "ClusterIP — ichki tarmoq; NodePort — tashqi port; LoadBalancer — bulut LB.\n"
            "CoreDNS: `service-name.namespace.svc.cluster.local`.\n"
            "Headless Service (ClusterIP=None) — StatefulSet uchun stabil tarmoq.",

            "🎯 DARS 4: ConfigMap va Secret\n"
            "Konfiguratsiyani imagedan ajratish — 12-factor prinsipi.\n"
            "Secret base64 saqlaydi (shifrlash emas!); etcd shifrlangan bo‘lishi kerak.\n"
            "Env vs volume mount — yangilanish va xavfsizlik farqi.",

            "🎯 DARS 5: Resource limits\n"
            "requests — scheduler uchun; limits — cgroup cheklovi.\n"
            "CPU throttling, OOMKill — noto‘g‘ri limitlar oqibati.\n"
            "Vertical vs Horizontal Pod Autoscaler (VPA/HPA) — metrikaga asoslangan masshtab.",

            "🎯 DARS 6: Tarmoq siyosatlari\n"
            "NetworkPolicy — podlar o‘rtasida firewall (Calico, Cilium).\n"
            "Ingress — HTTP marshrutlash, TLS terminatsiyasi.\n"
            "Service mesh (Istio/Linkerd) — mTLS va observability.",

            "🎯 DARS 7: Saqlash\n"
            "PV/PVC — disk hayotiy sikli; StorageClass — dinamik provision.\n"
            "StatefulSet — barqaror identifikator va tartibli deploy.\n"
            "Backup: Velero, etcd snapshot — feloyat tiklash strategiyasi.",

            "🎯 DARS 8: Amaliyot yo‘nalishi\n"
            "Helm chart — paketlash; Kustomize — overlay.\n"
            "GitOps (Argo CD, Flux) — kerakli holat = Gitdagi manba.\n"
            "Kuzatuv: Prometheus + Grafana; loglar: Loki/ELK.",
        ],
    },
    "rust_lang": {
        "title": "🦀 Rust — xotira xavfsizligi va tezlik",
        "lessons": [
            "🎯 DARS 1: Ownership\n"
            "Har qiymat bitta egaga tegishli; `move` — egalik o‘tkazish.\n"
            "Stack tez, heap — Box/Rc/Arc bilan boshqariladi.\n"
            "Dangling pointer va double-free compile vaqtida yo‘qoladi.",

            "🎯 DARS 2: Borrowing\n"
            "`&T` — immutable borrow; `&mut T` — mutable; bir vaqtda bitta yozuv.\n"
            "Lifetimes — referens qachon yaroqli ekanini belgilaydi.\n"
            "`'static` — dastur boshiga qadar yashaydi.",

            "🎯 DARS 3: Traitlar\n"
            "Polimorfizm: trait object (`dyn Trait`) vs monomorfizatsiya (generik).\n"
            "`Copy`, `Clone`, `Send`, `Sync` — concurrency bilan bog‘liq markerlar.\n"
            "Trait boundlar: `T: Display + Debug`.",

            "🎯 DARS 4: Xatoliklar\n"
            "`Result<T,E>` va `Option<T>` — `?` operatori bilan qisqa yo‘l.\n"
            "`panic!` — tiklanmaydigan; `unwrap` faqat prototipda.\n"
            "Custom error type — `thiserror` / `anyhow` ekotizomi.",

            "🎯 DARS 5: Concurrency\n"
            "Threadlar va `Arc<Mutex<T>>` — ehtiyotkorlik bilan deadlock.\n"
            "`tokio` async — Future va executor.\n"
            "`Send` bo‘lmagan turlar threadlar orasida cheklangan.",

            "🎯 DARS 6: FFI va xavfsizlik\n"
            "`unsafe` — minimal zona; C bilan bog‘lash.\n"
            "Buffer overflow Rustda kam, lekin `unsafe` ichida mumkin.\n"
            "Constant-time qiyoslash — kripto uchun muhim.",

            "🎯 DARS 7: Modul va Cargo\n"
            "Workspace — bir nechta crate; semver — versiya qoidalari.\n"
            "`cargo test`, `bench`, `miri` — xotira modeli tekshiruvi.\n"
            "Feature flaglar — ixtiyoriy funksionallik.",

            "🎯 DARS 8: Ishlab chiqarish\n"
            "Profiling: `perf`, flamegraph.\n"
            "Cross-compile — musbat/ARM.\n"
            "wasm32 — brauzer va edge uchun Rust.",
        ],
    },
    "golang": {
        "title": "🐹 Go — soddalik va yuqori parallelizm",
        "lessons": [
            "🎯 DARS 1: Goroutine\n"
            "`go f()` — yengil thread; scheduler GMP modeli.\n"
            "Minglab goroutine — real OS threadlar emas.\n"
            "Stack dinamik o‘sadi.",

            "🎯 DARS 2: Channel\n"
            "`chan T` — sinxronizatsiya va ma’lumot oqimi.\n"
            "Buffered vs unbuffered; `close` va `range`.\n"
            "Pattern: fan-in, fan-out, pipeline.",

            "🎯 DARS 3: Interface\n"
            "Implicit implementation — `duck typing` uslubi.\n"
            "Kichik interfeyslar — `io.Reader`, `io.Writer`.\n"
            "Interface nil — tur va qiymat juftligi.",

            "🎯 DARS 4: Xatoliklar\n"
            "`error` interfeysi; `errors.Is`, `errors.As`.\n"
            "Defer — stack tartibida bajarilish; `panic/recover` cheklangan foydalanish.",

            "🎯 DARS 5: Modul va test\n"
            "Go modules — `go.mod`, semver.\n"
            "Table-driven test; `httptest`.\n"
            "Race detector — `go test -race`.",

            "🎯 DARS 6: Memory va GC\n"
            "Escape analysis — stack vs heap.\n"
            "GC pauzalari — allaqachon past latensiya.\n"
            "Pointer receiver vs value receiver.",

            "🎯 DARS 7: Standart kutubxona\n"
            "`context.Context` — vaqt va bekor qilish.\n"
            "`net/http` — server va klient; middleware.\n"
            "Protobuf + gRPC — servislararo shartnoma.",

            "🎯 DARS 8: Ishlab chiqarish\n"
            "Docker multi-stage build — kichik image.\n"
            "Graceful shutdown — signal va `Shutdown`.\n"
            "pprof — CPU va heap profiling.",
        ],
    },
    "microservices": {
        "title": "🧩 Microservices — arxitektura va tuzilish",
        "lessons": [
            "🎯 DARS 1: Monolitdan ajralish\n"
            "Bounded context (DDD) — servis chegaralari.\n"
            "Ma’lumotlar bazasini bo‘lish — eng qiyin qadam.\n"
            "Yomon ajralish: nano-servislar va tarmoq shovqin.",

            "🎯 DARS 2: Sinchron vs asinxron\n"
            "REST/gRPC — sinxron so‘rov; message broker — voqealar.\n"
            "Idempotent API — takroriy so‘rovlar xavfsiz.\n"
            "Timeout, retry, backoff.",

            "🎯 DARS 3: Service discovery\n"
            "DNS, Consul, etcd — ro‘yxatdan o‘tish.\n"
            "Health check — faqat HTTP 200 emas, semantika.\n"
            "Client-side vs server-side load balancing.",

            "🎯 DARS 4: Circuit breaker\n"
            "Kaskad muvaffaqiyatsizliklarni to‘xtatish.\n"
            "Bulkhead — resurs ajratish.\n"
            "Rate limiting — token bucket, sliding window.",

            "🎯 DARS 5: Distributed transactions\n"
            "2PC — sekin va nozik; Saga — kompensatsiya bosqichlari.\n"
            "Outbox pattern — broker va DB atrofida izchillik.\n"
            "Eventual consistency — foydalanuvchiga tushuntirish.",

            "🎯 DARS 6: API Gateway\n"
            "Bitta kirish nuqtasi: auth, marshrut, throttling.\n"
            "BFF (Backend for Frontend) — mobil va web alohida.\n"
            "GraphQL gateway — so‘rov birlashtirish.",

            "🎯 DARS 7: Observability\n"
            "Logging, metrics, tracing — uchta ustun.\n"
            "OpenTelemetry — standart.\n"
            "Correlation ID — so‘rov zanjirini kuzatish.",

            "🎯 DARS 8: DevOps bilan bog‘liqlik\n"
            "CI/CD — servis bo‘yicha pipeline.\n"
            "Feature flags — deploy va yoqish alohida.\n"
            "Contract testing — Pact.",
        ],
    },
    "system_design": {
        "title": "🏛️ System Design — masshtab va ishonchlilik",
        "lessons": [
            "🎯 DARS 1: Talablar\n"
            "Funksional va nofunksional: latensiya, throughput, mavjudlik.\n"
            "CAP — consistency, availability, partition tolerance — tanlov.\n"
            "Back-of-the-envelope hisob — tartib magnitudasi.",

            "🎯 DARS 2: Load balancing\n"
            "L4 vs L7; round-robin, least connections.\n"
            "Sticky sessions — holatli dasturlar uchun.\n"
            "Global LB — geoDNS, Anycast.",

            "🎯 DARS 3: Keshlash\n"
            "CDN — statik kontent; edge.\n"
            "Redis/Memcached — ilova kesh; TTL strategiyasi.\n"
            "Cache invalidation — ataylik muammo.",

            "🎯 DARS 4: Ma’lumotlar bazasi\n"
            "Replication — master-slave, quorum.\n"
            "Sharding — partition key tanlash; resharding.\n"
            "SQL vs NoSQL — qachon nima.",

            "🎯 DARS 5: Xabarlashuv navbatlari\n"
            "Kafka — log-asosli oqim; partition va consumer group.\n"
            "Ordering va idempotency producer.\n"
            "Dead letter queue — xato xabarlarni ajratish.",

            "🎯 DARS 6: Rate limiting va DDoS\n"
            "Edge da filtrlash; WAF.\n"
            "Challenge — botlarni kamaytirish.\n"
            "Autoscaling — CPU/RAM/custom metric.",

            "🎯 DARS 7: Monitoring\n"
            "SLI/SLO/SLA — xizmat sifat shartlari.\n"
            "Alert fatigue — noto‘g‘ri eshiklar.\n"
            "Chaos engineering — barqarorlik sinovi.",

            "🎯 DARS 8: Real loyiha sxemasi\n"
            "URL qisqartiruvchi, yangilik lentasi, chat — komponentlar.\n"
            "Har birida: bottleneck va yechim.\n"
            "Hujjatlashtirish — arxitektura ADR.",
        ],
    },
    "graphql": {
        "title": "◈ GraphQL — API va so‘rov grafi",
        "lessons": [
            "🎯 DARS 1: REST dan farq\n"
            "Bitta endpoint; klient kerakli maydonlarni so‘raydi.\n"
            "Over-fetching va under-fetching kamayadi.\n"
            "Schema — kontrakt manbai.",

            "🎯 DARS 2: Schema va resolver\n"
            "Query, Mutation, Subscription.\n"
            "Resolver daraxti — N+1 muammosi.\n"
            "DataLoader — batch va cache.",

            "🎯 DARS 3: Type tizimi\n"
            "Scalar, Object, Interface, Union, Enum.\n"
            "Nullable vs non-null — `!` belgisi.\n"
            "Validation — input cheklovlari.",

            "🎯 DARS 4: Xavfsizlik\n"
            "Chuqur so‘rov — DoS; chuqurlik cheklovi.\n"
            "AuthZ — maydon darajasida ruxsat.\n"
            "Introspection — prod da cheklash.",

            "🎯 DARS 5: Federation\n"
            "Mikroservislar o‘z subgraphini taqdim etadi.\n"
            "Gateway — umumiy graf.\n"
            "Entity va `@key`.",

            "🎯 DARS 6: Performance\n"
            "Persisted queries — faqat ruxsat etilgan so‘rovlar.\n"
            "HTTP/2 multiplexing.\n"
            "Subscription — WebSocket va Redis pub/sub.",

            "🎯 DARS 7: Versiyalash\n"
            "GraphQLda URL versiyasi kam; schema evolyutsiyasi.\n"
            "Deprecation — `@deprecated`.\n"
            "Mijozlar bilan kelishuvchi o‘zgarishlar.",

            "🎯 DARS 8: Amaliyot\n"
            "Apollo, Strawberry, gqlgen — stack tanlash.\n"
            "Testing — snapshot va contract.\n"
            "Error format — kengaytirilgan xatolar.",
        ],
    },
    "postgres_pro": {
        "title": "🐘 PostgreSQL — PRO darajada SQL",
        "lessons": [
            "🎯 DARS 1: MVCC\n"
            "Har transaksiya o‘z snapshotini ko‘radi.\n"
            "VACUUM — dead tuple va bloat.\n"
            "Isolation darajalari — read committed, repeatable read, serializable.",

            "🎯 DARS 2: Indekslar\n"
            "B-tree — standart; GIN/GiST — to‘liq matn, geometriya.\n"
            "Partial index — shart bilan.\n"
            "`EXPLAIN ANALYZE` — reja va haqiqiy vaqt.",

            "🎯 DARS 3: Locking\n"
            "Row lock vs table lock; deadlock aniqlash.\n"
            "`SELECT FOR UPDATE` — navbatlar.\n"
            "Advisory locks — ilova darajasida.",

            "🎯 DARS 4: Replikatsiya\n"
            "Streaming replication — WAL.\n"
            "Logical replication — jadval tanlash.\n"
            "Failover — Patroni, repmgr.",

            "🎯 DARS 5: Partitioning\n"
            "Range, list, hash.\n"
            "Partition pruning — so‘rov optimallashtirish.\n"
            "Foreign data wrapper — tashqi manbalar.",

            "🎯 DARS 6: JSON va NoSQL xususiyatlari\n"
            "`jsonb` — indeks va operatorlar.\n"
            "Array va GIN.\n"
            "Full text search — `tsvector`.",

            "🎯 DARS 7: Operatsion\n"
            "Connection pooling — PgBouncer.\n"
            "Autovacuum sozlamalari.\n"
            "Monitoring — pg_stat_statements.",

            "🎯 DARS 8: Dizayn qoidalari\n"
            "Normalizatsiya vs denormalizatsiya.\n"
            "Surrogate key — UUID vs BIGSERIAL.\n"
            "Soft delete — `deleted_at`.",
        ],
    },
    "redis_deep": {
        "title": "🔴 Redis — kesh, navbat, real-time",
        "lessons": [
            "🎯 DARS 1: Ma’lumot turlari\n"
            "String, List, Set, Sorted Set, Hash, Stream.\n"
            "TTL — muddati o‘tgan kalitlar.\n"
            "HyperLogLog — cardinality.",

            "🎯 DARS 2: Persistence\n"
            "RDB — snapshot; AOF — journal.\n"
            "fsync siyosati — tezlik vs yo‘qolish riski.\n"
            "Replication — async, partial resync.",

            "🎯 DARS 3: Cluster\n"
            "Hash slot — 16384; resharding.\n"
            "CROSSSLOT — bir so‘rovda bir slot.\n"
            "Sentinel — master tanlash.",

            "🎯 DARS 4: Xavfsizlik\n"
            "ACL — foydalanuvchi va buyruq.\n"
            "TLS — klient ulanishi.\n"
            "`EVAL` — Lua cheklangan vaqt.",

            "🎯 DARS 5: Kesh strategiyasi\n"
            "Cache-aside, write-through, write-behind.\n"
            "Dogpile/stampede — qulflash.\n"
            "Bloom filter — mavjudlik tekshiruvi.",

            "🎯 DARS 6: Redis Streams\n"
            "Consumer group — ishlov berish navbati.\n"
            "Kafka bilan solishtirish — hajm va kafolatlar.\n"
            "Trim — xotira boshqaruvi.",

            "🎯 DARS 7: Performance\n"
            "Pipelining — RTT kamaytirish.\n"
            "Single-threaded model — CPU bir yadro.\n"
            "Memory policy — LRU, LFU.",

            "🎯 DARS 8: Qachon Redis emas\n"
            "Murakkab so‘rovlar — PostgreSQL.\n"
            "Uzoq muddatli arxiv — obyekt saqlash.\n"
            "Strong consistency klaster — ehtiyotkorlik.",
        ],
    },
    "terraform": {
        "title": "🏗️ Terraform — infrastruktura kod sifatida",
        "lessons": [
            "🎯 DARS 1: Asoslar\n"
            "HCL sintaksisi; provider — bulut API.\n"
            "`terraform plan` — oldindan ko‘rish.\n"
            "State — haqiqat manbai.",

            "🎯 DARS 2: State boshqaruv\n"
            "Remote backend — S3 + locking (DynamoDB).\n"
            "State split — workspace va modullar.\n"
            "Sensitive output.",

            "🎯 DARS 3: Modul\n"
            "Qayta ishlatiladigan bloklar; input/output.\n"
            "Registry — versiyalangan modullar.\n"
            "Composition over inheritance.",

            "🎯 DARS 4: Lifecycle\n"
            "`create_before_destroy` — uzilishsiz yangilanish.\n"
            "`prevent_destroy` — muhim resurslar.\n"
            "Tainted — qayta yaratish.",

            "🎯 DARS 5: Import va drift\n"
            "Mavjud resursni import qilish.\n"
            "Drift detection — Terraform vs bulut.\n"
            "Policy as code — Sentinel, OPA.",

            "🎯 DARS 6: Workspace va muhitlar\n"
            "dev/stage/prod — alohida state yoki workspace.\n"
            "Variable files — `tfvars`.\n"
            "Secrets — Vault integratsiyasi, emas gitda!",

            "🎯 DARS 7: Testing\n"
            "Terratest — infratest.\n"
            "`terraform validate`, `fmt`.\n"
            "Cost estimation — Infracost.",

            "🎯 DARS 8: Terraform vs boshqalar\n"
            "Pulumi — umumiy til.\n"
            "CloudFormation — vendor lock.\n"
            "Crossplane — Kubernetesda CRD.",
        ],
    },
    "cicd_github": {
        "title": "⚙️ CI/CD — GitHub Actions va yetkazib berish",
        "lessons": [
            "🎯 DARS 1: CI/CD nima?\n"
            "Integratsiya — har commit tekshiruv.\n"
            "Yetkazib berish — muhitlarga avtomatik joylash.\n"
            "Pipeline — bosqichlar zanjiri.",

            "🎯 DARS 2: GitHub Actions\n"
            "Workflow YAML — `on`, `jobs`, `steps`.\n"
            "Runner — hosted yoki self-hosted.\n"
            "Matrix build — bir nechta OS/Python.",

            "🎯 DARS 3: Secretlar\n"
            "GitHub Secrets — shifrlangan.\n"
            "Environment protection — tasdiqlovchilar.\n"
            "OIDC — bulutga vaqtinchalik kalit.",

            "🎯 DARS 4: Konteyner pipeline\n"
            "Build → scan → push registry.\n"
            "Multi-arch image — buildx.\n"
            "Image signing — cosign.",

            "🎯 DARS 5: Test strategiyasi\n"
            "Unit → integration → e2e.\n"
            "Parallel jobs; cache — pip/npm.\n"
            "Coverage threshold.",

            "🎯 DARS 6: Deploy strategiyasi\n"
            "Blue-green, canary, rolling.\n"
            "Feature flags — LaunchDarkly.\n"
            "Database migration — alohida bosqich.",

            "🎯 DARS 7: Monitoring pipeline\n"
            "Build vaqt metrikalari.\n"
            "Artefakt saqlash — muddati.\n"
            "Failed deploy rollback.",

            "🎯 DARS 8: Boshqa vositalar\n"
            "GitLab CI, Jenkins, CircleCI.\n"
            "Dagger — pipeline kodlanadi.\n"
            "Platform team — standart shablonlar.",
        ],
    },
    "pytorch_basics": {
        "title": "🔥 PyTorch — tensorlar va neural tarmoq",
        "lessons": [
            "🎯 DARS 1: Tensor\n"
            "ndarray ga o‘xshash, GPU da hisoblash.\n"
            "`device`, `dtype`, `requires_grad`.\n"
            "Broadcasting — shakllarni moslash.",

            "🎯 DARS 2: Autograd\n"
            "Hisob grafi; `backward()`.\n"
            "Gradient to‘planishi — `.zero_grad()`.\n"
            "Detaching — inference rejimi.",

            "🎯 DARS 3: nn.Module\n"
            "Katlam sifatida obyekt; parametrlar ro‘yxati.\n"
            "Sequential vs custom `forward`.\n"
            "GPU ga ko‘chirish — `.to(device)`.",

            "🎯 DARS 4: O‘qitish tsikli\n"
            "DataLoader — batch, shuffle, num_workers.\n"
            "Loss funksiyasi; optimizer (Adam, SGD).\n"
            "Overfitting — dropout, weight decay.",

            "🎯 DARS 5: CNN asoslari\n"
            "Konvolyutsiya, pooling, padding.\n"
            "Receptive field.\n"
            "Transfer learning — torchvision modellari.",

            "🎯 DARS 6: Sequence modellar\n"
            "RNN/LSTM — vaqt qatori.\n"
            "Attention — fokus mexanizmi.\n"
            "Transformer blok — zamonaviy NLP/vision.",

            "🎯 DARS 7: Baholash\n"
            "Train/val split; metrikalar — accuracy, F1.\n"
            "Confusion matrix.\n"
            "Early stopping.",

            "🎯 DARS 8: Ishlab chiqarish\n"
            "TorchScript, ONNX eksport.\n"
            "Inference optimallashtirish — half precision.\n"
            "Monitoring — drift va latensiya.",
        ],
    },
    "mlops_intro": {
        "title": "📈 MLOps — model hayoti sikli",
        "lessons": [
            "🎯 DARS 1: ML va dastur farqi\n"
            "Model va ma’lumot ham versiyalanadi.\n"
            "Retraining — yangi ma’lumot bilan.\n"
            "Monitoring — ma’lumot va model drift.",

            "🎯 DARS 2: Eksperiment kuzatuv\n"
            "MLflow, Weights & Biases — metrik va artefaktlar.\n"
            "Hyperparameter search — Optuna.\n"
            "Reproducibility — seed, environment.",

            "🎯 DARS 3: Feature store\n"
            "Onlayn va oflayn xususiyatlar.\n"
            "Izchillik — train va serving bir xil hisoblash.\n"
            "Point-in-time correctness.",

            "🎯 DARS 4: Model registry\n"
            "Staging → production.\n"
            "Model kartochkasi — ma’lumot va cheklovlar.\n"
            "Rollback — oldingi versiya.",

            "🎯 DARS 5: Serving\n"
            "REST/gRPC endpoint; batch vs real-time.\n"
            "Autoscaling — RPS bo‘yicha.\n"
            "GPU scheduling.",

            "🎯 DARS 6: Testlash\n"
            "Model unit test — tensor shakllari.\n"
            "Contract test — kirish/ chiqish sxemasi.\n"
            "A/B test — biznes metrikasi.",

            "🎯 DARS 7: Xavfsizlik va etika\n"
            "PII — shaxsiy ma’lumot.\n"
            "Adversarial misollar.\n"
            "Bias va adolat.",

            "🎯 DARS 8: Amaliyot\n"
            "Kubeflow, SageMaker, Vertex — platformalar.\n"
            "CI/CD + CT (continuous training).\n"
            "Hujjat va audit izi.",
        ],
    },
    "zero_trust": {
        "title": "🛡️ Zero Trust — identifikatsiya va segmentatsiya",
        "lessons": [
            "🎯 DARS 1: Paranoya emas, model\n"
            "\"Ichkaridagi tarmoq ishonchli\" — eski fikr.\n"
            "Har so‘rov tekshiriladi: kim, nima, qayerdan.\n"
            "Least privilege — minimal ruxsat.",

            "🎯 DARS 2: Identifikatsiya\n"
            "MFA — asosiy himoya qatlami.\n"
            "SSO va SAML/OIDC.\n"
            "Device posture — sanoqli qurilma.",

            "🎯 DARS 3: Mikrosegmentatsiya\n"
            "Workload o‘rtasida firewall.\n"
            "Kubernetes NetworkPolicy + service mesh.\n"
            "Lateral movement qiyinlashadi.",

            "🎯 DARS 4: Tashqi kirish\n"
            "VPN o‘rniga ZTNA — per-app access.\n"
            "Bastion host kamaytirish.\n"
            "Logging har bir autentifikatsiya.",

            "🎯 DARS 5: Ma’lumot himoyasi\n"
            "Shifrlash — damg‘ada ham.\n"
            "DLP — chiqishni nazorat.\n"
            "KMS — kalit rotatsiyasi.",

            "🎯 DARS 6: SOC\n"
            "SIEM — voqealar korelatsiyasi.\n"
            "IR playbooks — tezkor javob.\n"
            "Purple team — hujum va himoya mashg‘uloti.",

            "🎯 DARS 7: Compliance\n"
            "ISO 27001, SOC2 — nazorat nuqtalari.\n"
            "Audit log — o‘zgartirishsiz.\n"
            "Vendor risk — uchinchi tomon.",

            "🎯 DARS 8: Amalga oshirish\n"
            "Boshlash: inventarizatsiya va klassifikatsiya.\n"
            "Pilotsiz emas — bosqichma-bosqich.\n"
            "Xodimlar o‘qituvi — eng zaif halqa.",
        ],
    },
}


def _build_quizzes() -> dict:
    """Har mavzu uchun 4 ta murakkab savol."""
    q = {}
    q["kubernetes"] = [
        {
            "question": "Kubernetesda eng kichik ishga tushirish birligi nima?",
            "options": ["Deployment", "Pod", "Service", "Volume"],
            "correct": 1,
            "explanation": "Pod — bitta yoki bir nechta konteyner guruhlash birligi.",
        },
        {
            "question": "Ichki klaster DNS nomi qanday tuziladi?",
            "options": [
                "pod.local",
                "service.namespace.svc.cluster.local",
                "kube.dns",
                "cluster.internal",
            ],
            "correct": 1,
            "explanation": "Standart DNS: service-name.namespace.svc.cluster.local",
        },
        {
            "question": "Deployment nimani boshqaradi?",
            "options": [
                "Faqat bitta pod",
                "Pod replikalari va yangilanish strategiyasi",
                "Faqat tarmoq siyosati",
                "Faqat secret",
            ],
            "correct": 1,
            "explanation": "Deployment deklarativ ravishda replikalar va rolling updateni boshqaradi.",
        },
        {
            "question": "ConfigMap maqsadi nima?",
            "options": [
                "Konteyner imageni build qilish",
                "Konfiguratsiyani kod/imagedan ajratish",
                "Faqat parollarni saqlash",
                "Podni avtomatik masshtablash",
            ],
            "correct": 1,
            "explanation": "ConfigMap konfiguratsiya qiymatlarini tashqi manbadan beradi.",
        },
    ]
    q["rust_lang"] = [
        {
            "question": "Ownership qachon compile xatoga olib keladi?",
            "options": [
                "Ikki mutable borrow bir vaqtda",
                "Faqat print qilishda",
                "Faqat integer qo‘shishda",
                "Hech qachon",
            ],
            "correct": 0,
            "explanation": "Bir vaqtda faqat bitta faol `&mut` borrow ruxsat etiladi.",
        },
        {
            "question": "`Result<T,E>` uchun qaysi operator qulay?",
            "options": ["?", "!", "#", "$"],
            "correct": 0,
            "explanation": "`?` xatolikni qisqa yo‘l bilan qaytaradi.",
        },
        {
            "question": "Rustda GC bormi?",
            "options": [
                "Ha, to‘liq avtomatik GC",
                "Yo‘q, ownership/RAII bilan boshqariladi",
                "Faqat nightly da",
                "Faqat async da",
            ],
            "correct": 1,
            "explanation": "Rustda an’anaviy GC yo‘q; xotira compile vaqtida tekshiriladi.",
        },
        {
            "question": "Trait obyekt qanday yoziladi?",
            "options": ["Box<dyn Trait>", "dyn Box<Trait>", "Trait::box()", "only struct"],
            "correct": 0,
            "explanation": "Heap’da trait object odatda `Box<dyn Trait>` orqali.",
        },
    ]
    q["golang"] = [
        {
            "question": "Goroutine qanday ishga tushadi?",
            "options": ["spawn()", "go f()", "thread f()", "async f()"],
            "correct": 1,
            "explanation": "`go` kalit so‘zi goroutine yaratadi.",
        },
        {
            "question": "Buffered channel yaratish:",
            "options": [
                "make(chan int)",
                "make(chan int, 10)",
                "chan int{}",
                "new(chan int)",
            ],
            "correct": 1,
            "explanation": "Ikkinchi argument bufer hajmini beradi.",
        },
        {
            "question": "Interface nil qachon xavfli?",
            "options": [
                "Hech qachon",
                "Tur nil, lekin qiymat nil emas — type assertion kerak",
                "Faqat string da",
                "Faqat int da",
            ],
            "correct": 1,
            "explanation": "Go’da `interface` nil — tur va qiymat juftligi muhim.",
        },
        {
            "question": "Context asosan nim uchun?",
            "options": [
                "Faqat logging",
                "Timeout va bekor qilish signalini uzatish",
                "Faqat config",
                "Faqat test",
            ],
            "correct": 1,
            "explanation": "`context` muddat va cancelni servislar bo‘ylab uzatadi.",
        },
    ]
    q["microservices"] = [
        {
            "question": "Saga pattern nimani hal qiladi?",
            "options": [
                "Faqat loglarni",
                "Taqsimlangan transaksiyalarni kompensatsiya bosqichlari bilan",
                "Faqat UI",
                "Faqat DNS",
            ],
            "correct": 1,
            "explanation": "Saga uzun jarayonlarni kompensatsiya qadamlari bilan boshqaradi.",
        },
        {
            "question": "Circuit breaker maqsadi?",
            "options": [
                "Kriptografiya",
                "Xato servisga yukni to‘xtatish",
                "Faqat kesh",
                "Faqat load balancer",
            ],
            "correct": 1,
            "explanation": "Circuit breaker kaskad xatoliklarni oldini oladi.",
        },
        {
            "question": "API Gateway odatda nimani bajaradi?",
            "options": [
                "Faqat DB",
                "Auth, marshrut, limit",
                "Faqat DNS",
                "Faqat CI",
            ],
            "correct": 1,
            "explanation": "Gateway yagona kirish va siyosatlarni markazlashtiradi.",
        },
        {
            "question": "Outbox pattern nim uchun?",
            "options": [
                "UI animatsiya",
                "DB va message broker o‘rtasida izchillik",
                "Faqat test",
                "Faqat grafika",
            ],
            "correct": 1,
            "explanation": "Outbox bir transaksiyada yozuv va event yuborishni bog‘laydi.",
        },
    ]
    q["system_design"] = [
        {
            "question": "CAP teoremasida tarmoq bo‘linganda nima bo‘lishi kerak?",
            "options": [
                "C va A ikkalasi ham doimiy",
                "C yoki A dan biri tanlanadi (P bilan)",
                "Hech narsa",
                "Faqat latensiya",
            ],
            "correct": 1,
            "explanation": "Partition paytida consistency va availability o‘rtasida tanlov.",
        },
        {
            "question": "CDN asosan nimani tezlashtiradi?",
            "options": [
                "SQL so‘rovlar",
                "Statik kontentni foydalanuvchiga yaqin joydan",
                "Faqat CPU",
                "Faqat RAM",
            ],
            "correct": 1,
            "explanation": "CDN edge cache orqali kechikishni kamaytiradi.",
        },
        {
            "question": "Sharding nimani anglatadi?",
            "options": [
                "Faqat indeks",
                "Ma’lumotlarni partition bo‘yicha bo‘lish",
                "Faqat backup",
                "Faqat log",
            ],
            "correct": 1,
            "explanation": "Sharding katta jadvalni gorizontal bo‘laklash.",
        },
        {
            "question": "Kafka partition maqsadi?",
            "options": [
                "Faqat UI",
                "Parallel o‘qish/yozish va tartibni bo‘lish",
                "Faqat grafik",
                "Faqat DNS",
            ],
            "correct": 1,
            "explanation": "Partitionlar orqali throughput oshadi; tartib partition ichida.",
        },
    ]
    q["graphql"] = [
        {
            "question": "N+1 muammosi nimada?",
            "options": [
                "Faqat CSS",
                "Bog‘langan obyektlar uchun har bir uchun alohida so‘rov",
                "Faqat DNS",
                "Faqat RAM",
            ],
            "correct": 1,
            "explanation": "Resolver har bog‘lanish uchun alohida DB chaqirishi mumkin.",
        },
        {
            "question": "DataLoader yordam beradi:",
            "options": [
                "Faqat CSS",
                "Batch va cache bilan N+1 ni kamaytirish",
                "Faqat audio",
                "Faqat video",
            ],
            "correct": 1,
            "explanation": "DataLoader bir nechta ID ni bir so‘rovda birlashtiradi.",
        },
        {
            "question": "GraphQLda GET-only bo‘lishi shartmi?",
            "options": ["Ha", "Yo‘q — mutation va subscription bor", "Faqat FTP", "Faqat UDP"],
            "correct": 1,
            "explanation": "Mutation o‘zgartirish, subscription real-time voqealar.",
        },
        {
            "question": "Introspection prod da nima uchun xavf?",
            "options": [
                "Hech narsa",
                "Sxema va maydonlar ochilishi",
                "Faqat rang",
                "Faqat shrift",
            ],
            "correct": 1,
            "explanation": "Hujumchi API tuzilishini o‘rganishi mumkin.",
        },
    ]
    q["postgres_pro"] = [
        {
            "question": "MVCC nimaga xizmat qiladi?",
            "options": [
                "Faqat backup",
                "Parallel o‘qish/yozishni bloklarsiz boshqarish",
                "Faqat indeks",
                "Faqat user",
            ],
            "correct": 1,
            "explanation": "Har transaksiya o‘z snapshotida ishlaydi.",
        },
        {
            "question": "`EXPLAIN ANALYZE` nima beradi?",
            "options": [
                "Faqat jadval ro‘yxati",
                "Reja va haqiqiy bajarilish vaqti",
                "Faqat user ro‘yxati",
                "Faqat rol",
            ],
            "correct": 1,
            "explanation": "ANALYZE haqiqiy statistikani yig‘adi.",
        },
        {
            "question": "Deadlock qachon?",
            "options": [
                "Hech qachon",
                "Resurslarni turli tartibda kutish",
                "Faqat SELECT",
                "Faqat COUNT",
            ],
            "correct": 1,
            "explanation": "Circular wait deadlock paydo qiladi.",
        },
        {
            "question": "Partial index — ...",
            "options": [
                "Barcha qatorlar",
                "WHERE sharti bilan indeks",
                "Faqat UUID",
                "Faqat TEXT",
            ],
            "correct": 1,
            "explanation": "Partial index faqat shartga mos qatorlarni indekslaydi.",
        },
    ]
    q["redis_deep"] = [
        {
            "question": "Redis asosan qanday model?",
            "options": [
                "Multi-threaded har operatsiya",
                "Asosan single-threaded event loop",
                "Faqat disk",
                "Faqat batch",
            ],
            "correct": 1,
            "explanation": "Asosiy buyruqlar bitta threadda ketadi (IO versiyalar bilan boyitilgan).",
        },
        {
            "question": "AOF nimani anglatadi?",
            "options": [
                "Faqat snapshot",
                "Append-only fayl — har yozuv journal",
                "Faqat grafik",
                "Faqat audio",
            ],
            "correct": 1,
            "explanation": "AOF yozuvlar jurnalini saqlaydi.",
        },
        {
            "question": "Cache stampede oldini olish usuli?",
            "options": [
                "Hech narsa",
                "Qulflash yoki probabilistik yangilanish",
                "Faqat DELETE",
                "Faqat TRUNCATE",
            ],
            "correct": 1,
            "explanation": "TTL tugaganda bir vaqtda ko‘p so‘rov — stampede.",
        },
        {
            "question": "Redis Cluster slotlar soni?",
            "options": ["256", "4096", "16384", "65536"],
            "correct": 2,
            "explanation": "16384 hash slot — standart.",
        },
    ]
    q["terraform"] = [
        {
            "question": "`terraform plan` nimani ko‘rsatadi?",
            "options": [
                "Faqat log",
                "State ga nisbatan o‘zgarishlar rejasini",
                "Faqat user",
                "Faqat DNS",
            ],
            "correct": 1,
            "explanation": "Plan kerakli add/change/destroy ro‘yxatini chiqaradi.",
        },
        {
            "question": "State locking nimaga kerak?",
            "options": [
                "Faqat UI",
                "Parallel `apply` dan state buzilishini oldini olish",
                "Faqat test",
                "Faqat lint",
            ],
            "correct": 1,
            "explanation": "Remote backend lock bilan bitta apply.",
        },
        {
            "question": "Module inputlari qanday uzatiladi?",
            "options": [
                "Faqat env",
                "O‘zgaruvchilar va module block",
                "Faqat SSH",
                "Faqat FTP",
            ],
            "correct": 1,
            "explanation": "Terraform `variable` va module argumentlari orqali.",
        },
        {
            "question": "`prevent_destroy` nimani qiladi?",
            "options": [
                "Avtomatik o‘chirish",
                "Resurs o‘chirishni xavfli deb to‘xtatadi",
                "Faqat log",
                "Faqat plan",
            ],
            "correct": 1,
            "explanation": "Lifecycle bilan o‘chirishni bloklash.",
        },
    ]
    q["cicd_github"] = [
        {
            "question": "GitHub Actions workflow qayerda?",
            "options": [
                ".github/workflows/*.yml",
                "Dockerfile only",
                "package.json only",
                "Makefile only",
            ],
            "correct": 0,
            "explanation": "Workflow fayllari odatda `.github/workflows` da.",
        },
        {
            "question": "Matrix build nima?",
            "options": [
                "Faqat bitta OS",
                "Bir nechta kombinatsiyalarni parallel sinash",
                "Faqat DNS",
                "Faqat SSL",
            ],
            "correct": 1,
            "explanation": "Matrix turli OS/Python versiyalarida test.",
        },
        {
            "question": "OIDC bilan bulutga ulanish afzalligi?",
            "options": [
                "Uzun muddatli kalitni gitga qo‘yish",
                "Vaqtinchalik token, maxfiy kalitni repo da saqlamaslik",
                "Hech narsa",
                "Faqat FTP",
            ],
            "correct": 1,
            "explanation": "OIDC short-lived credentials.",
        },
        {
            "question": "Canary deploy — ...",
            "options": [
                "Barcha trafik birdaniga",
                "Trafikning bir qismini yangi versiyaga",
                "Faqat DB",
                "Faqat cache",
            ],
            "correct": 1,
            "explanation": "Canary asta-sekin yangi versiyani sinash.",
        },
    ]
    q["pytorch_basics"] = [
        {
            "question": "`requires_grad=True` nimani yoqadi?",
            "options": [
                "Faqat print",
                "Autograd hisob grafi",
                "Faqat CPU",
                "Faqat save",
            ],
            "correct": 1,
            "explanation": "Gradient hisoblash uchun tensor kuzatiladi.",
        },
        {
            "question": "Overfitting belgisi?",
            "options": [
                "Train yuqori, val past",
                "Train va val ikkalasi ham yuqori",
                "Hech qachon",
                "Faqat loss 0",
            ],
            "correct": 0,
            "explanation": "Train juda yaxshi, lekin val yomon — overfitting.",
        },
        {
            "question": "Dropout qachon ishlaydi?",
            "options": [
                "Har doim bir xil",
                "Odatda train, eval da o‘chiriladi",
                "Faqat test",
                "Faqat save",
            ],
            "correct": 1,
            "explanation": "model.train() vs model.eval() rejimlari muhim.",
        },
        {
            "question": "Adam optimizer — ...",
            "options": [
                "Faqat SGD",
                "Adaptive learning rate bilan gradient usuli",
                "Faqat CPU",
                "Faqat Excel",
            ],
            "correct": 1,
            "explanation": "Adam — keng tarqalgan adaptive optimizer.",
        },
    ]
    q["mlops_intro"] = [
        {
            "question": "Model drift nima?",
            "options": [
                "Server o‘chishi",
                "Ma’lumot taqsimoti o‘zgarib, model eskirishi",
                "Faqat DNS",
                "Faqat SSL",
            ],
            "correct": 1,
            "explanation": "Input taqsimoti o‘zgarsa, model aniqligi pasayishi mumkin.",
        },
        {
            "question": "Feature store afzalligi?",
            "options": [
                "Faqat log",
                "Train va serving bir xil xususiyat hisobi",
                "Faqat UI",
                "Faqat DNS",
            ],
            "correct": 1,
            "explanation": "Izchillik va qayta ishlatish.",
        },
        {
            "question": "A/B test nimani solishtiradi?",
            "options": [
                "Faqat kod hajmi",
                "Biznes metrikalari (conversion va hokazo)",
                "Faqat CPU",
                "Faqat RAM",
            ],
            "correct": 1,
            "explanation": "Model versiyalari real foydalanuvchida sinovdan o‘tadi.",
        },
        {
            "question": "CI/CD dan keyingi CT — ...",
            "options": [
                "Faqat dizayn",
                "Continuous training — model qayta o‘qitish",
                "Faqat backup",
                "Faqat email",
            ],
            "correct": 1,
            "explanation": "CT — avtomatik retraining pipeline.",
        },
    ]
    q["zero_trust"] = [
        {
            "question": "Zero Trust asosiy g‘oya?",
            "options": [
                "Ichki tarmoq ishonchli",
                "Hech qayerga ishonmaslik, har bosqichda tekshirish",
                "Faqat parolsiz",
                "Faqat VPN",
            ],
            "correct": 1,
            "explanation": "Har ulanish va so‘rov alohida tekshiriladi.",
        },
        {
            "question": "MFA nimani kuchaytiradi?",
            "options": [
                "Faqat UI rang",
                "Autentifikatsiya — bir nechta omil",
                "Faqat disk",
                "Faqat audio",
            ],
            "correct": 1,
            "explanation": "Parol + qo‘shimcha omil (OTP, biometriya).",
        },
        {
            "question": "Mikrosegmentatsiya — ...",
            "options": [
                "Barcha portlar ochiq",
                "Workload o‘rtasida tor ruxsatlar",
                "Faqat DNS",
                "Faqat SSL",
            ],
            "correct": 1,
            "explanation": "Minimal lateral movement uchun segmentatsiya.",
        },
        {
            "question": "ZTNA VPN dan farqi?",
            "options": [
                "Butun tarmoq emas, ilova darajasida kirish",
                "Hech qanday farq yo‘q",
                "Faqat email",
                "Faqat FTP",
            ],
            "correct": 0,
            "explanation": "Zero Trust Network Access — per-application access.",
        },
    ]
    return q


EXTENDED_QUIZZES = _build_quizzes()

EXTENDED_LESSONS = {
    key: {"title": val["title"], "lessons": val["lessons"]}
    for key, val in EXTENDED_LESSONS.items()
}


# -*- coding: utf-8 -*-
"""
Til va tilshunoslik — 67 PRO dars (o‘zbek tili, ingliz grammatikasi, amaliy lingvistika).
main_v2 LESSONS / QUIZZES ga qo‘shiladi.
"""

# ----- 1–15: O‘zbek tili — fonetika, grammatika, yozuv -----
_UZ_BLOCKS = [
    """📚 DARS 1: Til va nutq haqida
Til — jamiyatning eng muhim ijtimoiy kodi. U fikr, munosabat va madaniyatni o‘tkazadi.
Nutq — tilning jonli shakli; yozuv — saqlanadigan shakl.
Fonetika tovushlarni, grafika harflarni, morfologiya so‘z shakllarini o‘rganadi.
Bu kursda biz o‘zbek va inglizni bir-birini boyitadigan qilib ko‘ramiz.""",
    """📚 DARS 2: O‘zbek alifbosi va tovushlar
O‘zbek lotin alifbosi 29 harfdan iborat (a, b, d, … o‘, g‘, …).
Undoshlar va unli farqi: unli tovush og‘iz bo‘shlig‘i ochiq, undosh to‘siq bilan.
O‘ va u farqi muhim: qotma “o‘” lablari dumaloq, “u” tor.
Shuhrat, shuhrat emas — ma’no farqi fonetik bilan bog‘liq.""",
    """📚 DARS 3: Bo‘g‘in va urg‘u
So‘z bir yoki bir nechta bo‘g‘inga bo‘linadi: ta-lim, kom-pyu-ter.
O‘zbekda urg‘u odatda oxirgi bo‘g‘inda: taLIM, kompyUter.
Noto‘g‘ri urg‘u tinglovchida chalkashlik keltiradi; xorijiy so‘zlarda lug‘atdan tekshiring.""",
    """📚 DARS 4: So‘z va uning tuzilishi
Morfema — eng kichik ma’noli birlik (ildiz, qo‘shimcha).
So‘z ildiz + affiks: o‘q-i-ta-miz → o‘q + i + ta + miz.
Yasama so‘zlar: qo‘shma (temiryo‘l), qo‘shma ildiz (kitob-do‘kon).""",
    """📚 DARS 5: So‘z turkumi — ot
Ot — buyum, tushuncha, jonli nom: kitob, talaba, Toshkent.
Jins (erkak/ayol/umumiy) va son (birlik/ko‘plik) kategoriyalari.
Kelishiklar otga bog‘lanadi: yopiq qo‘shimchalar bilan (ning, ga, da…).""",
    """📚 DARS 6: Sifat va son
Sifat — belgi bildiradi: qizil, tez, katta.
Daraja: qizil → qiziroq → eng qizil.
Son — tartib (birinchi) va miqdor (bir, ikki, ko‘p).""",
    """📚 DARS 7: Olmosh va son
Olmosh — o‘rnini bosadi: u, bu, shu, o‘zi.
Shaxs olmoshlari: men, sen, u — egalik va ob’ekt rollariga qarab o‘zgaradi.
Ko‘rsatish olmoshlari jumlada ma’lumotni bog‘laydi.""",
    """📚 DARS 8: Fe’l va zamon
Fe’l — harakat yoki holat: o‘qimoq, yozmoq, bo‘lmoq.
Zamonlar: hozirgi, o‘tgan, kelasi; tugallanish (o‘qidim) va tuganmagan (o‘qiyapman).
Shart mayli va buyruq mayli shakllar nutqda tez-tez uchraydi.""",
    """📚 DARS 9: Ravish va bog‘lovchi
Ravish — fe’l/sifatni aniqlaydi: tez, juda, erta.
Bog‘lovchi ikki qismni birlashtiradi: va, lekin, chunki, agar.
Qarama-qarshilik bog‘lovlari (lekin, ammo) matn logikasini aniqlaydi.""",
    """📚 DARS 10: Gap tuzilishi
Oddiy gap: egalik + kesim (Men o‘qiyman).
So‘roq: so‘z tartibi yoki -mi qo‘shimchasi.
Buyruq: kesimsiz yoki nol egalik (Kel!).
Murakkab gap: ergashtiruvchi va qo‘shma gaplar.""",
    """📚 DARS 11: Tinish belgilari
Nuqta — to‘liq to‘xtash; vergul — qisqa pauza.
Undov va so‘roq belgilari intonatsiyani yozuvda uzatadi.
Qavs ichki izoh; tire — qo‘shma so‘z yoki dialog.""",
    """📚 DARS 12: Leksikografiya va sinonim
Lug‘at — til boyligining kartotekasi.
Sinonimlar ma’no yaqin, lekin uslub yoki yo‘nalish farqi bor.
Antonimlar qarama-qarshi: yaxshi — yomon.""",
    """📚 DARS 13: Frazeologizm
Barakalla, yurakdan, bosh qotirmoq — barqaror birikmlar.
O‘zbek tilida ko‘p metaforik ifodalar madaniy kod saqlaydi.
Tarjimalarda shunchaki so‘zma-so‘z emas, ma’noni topish kerak.""",
    """📚 DARS 14: Uslub va registro
Rasmiy hujjat: qisqa, aniq, “men”dan kam foydalanish.
Ilmiy uslub: atama aniqligi, iqtiboslar.
Og‘zaki nutq: qisqa gaplar, tovushli takrorlar.""",
    """📚 DARS 15: Dialekt va standart til
O‘zbekning mintaqaviy shivasi — boylik, lekin maktab va media standart tilni talab qiladi.
Standart — qoidalari kodlashtirilgan variant.
Ikki tillilik: o‘zbek + ingliz — leksikani alohida “qalflar”da saqlang.""",
]

# ----- 16–45: Ingliz tili (CER ga yaqin ketma-ketlik) -----
_EN_TITLES = [
    ("Present Simple / to be", "Hozirgi oddiy va to be: I am, you are, he is. Do/does savollar. Har kungi harakatlar."),
    ("Present Continuous", "Hozirgi davomiy: am/is/are + -ing. Vaqt chegarasi: now, at the moment."),
    ("Past Simple", "O‘tgan oddiy: V2 (regular -ed, irregular ro‘yxat). Yesterday, ago, last week."),
    ("Past Continuous", "O‘tgan davomiy: was/were + -ing. Uzoq davom etgan harakat fonida boshqa voqea."),
    ("Present Perfect", "have/has + V3: natija hozir muhim. ever/never, just, already, yet."),
    ("Present Perfect Continuous", "have been + -ing: davomiylik vaqt bilan. How long…?"),
    ("Past Perfect", "had + V3: o‘tmishdagi o‘tmish. After/before bilan."),
    ("Future: will / going to", "will — qaror yoki bashorat; going to — reja yoki aniq izlar."),
    ("Future Continuous & Perfect", "will be + -ing; will have + V3 — kelajakdagi tugallanish nuqtasi."),
    ("Modal: can / could", "Imkoniyat, ruxsat, xushmuomalalik so‘rovlari: Could you…?"),
    ("Modal: may / might", "Ehtimollik darajasi: might < may. I might call you."),
    ("Modal: must / have to", "Majburiyat va xulosaviy: mustn't vs don't have to farqi."),
    ("Modal: should / ought to", "Maslahat va moral norma: You should rest."),
    ("Passive voice", "be + V3: ob’ekt fokus. by-agent ixtiyoriy. Present passive misollar."),
    ("Reported speech", "So‘zlashtirish: said/told, vaqt siljishi (now→then)."),
    ("Conditionals 0–1", "If + present, present (ilmiy); If + present, will (haqiqiy shart)."),
    ("Conditionals 2–3", "If + past, would (gipoteza); If + past perfect, would have + V3."),
    ("Relative clauses", "who, which, that, whose. Defining vs non-defining (vergul!)."),
    ("Noun clauses", "that, if/whether, wh-words: I think that…, I don't know if…"),
    ("Gerund vs infinitive", "enjoy + -ing; want + to; remember doing vs remember to do."),
    ("Phrasal verbs (1)", "look for, give up, turn on — ularni jumlada yodlang, ro‘yxat emas."),
    ("Phrasal verbs (2)", "Separability: pick it up. Ma’no kontekstda o‘zgaradi."),
    ("Articles a/an/the", "Aniq va noaniq; the — unique yoki oldin tilga kiritilgan."),
    ("Countable / Uncountable", "much/many, a little/a few; advice — uncountable."),
    ("Comparatives / Superlatives", "short adj + -er; long — more beautiful; than / the most."),
    ("Adjective order", "opinion → size → age → shape → color → origin → material → noun."),
    ("Adverbs of frequency", "always, usually, often, sometimes, never — fe’ldan oldin (be dan keyin)."),
    ("Question tags", "You’re tired, aren’t you? Positive tag — negative gap."),
    ("Word order (basics)", "Subject–Verb–Object; zamon bo‘yicha yordamchi fe’llar."),
    ("Linking words", "however, therefore, although, because — paragraf bog‘lovchilari."),
]

# ----- 46–55: Amaliy yozish va o‘qish -----
_PRACT = [
    """📚 DARS 46: Inglizda paragraf tuzilishi
Topic sentence — birinchi gap asos fikr. Keyingi gaplar dalillar va misollar.
Xulosa gap qisqa takror yoki natija. IELTS/CEFR yozishda bu skelet ishlaydi.""",
    """📚 DARS 47: Formal xat va email
Salutation: Dear Sir/Madam; yopuv: Yours faithfully/sincerely.
Mavzuni birinchi jumlada ayting; so‘rov yoki ilovani aniq belgilang.""",
    """📚 DARS 48: Og‘zaki imtihon strategiyasi
30 soniya tayyorlanish: struktura (kirish–tanqid–xulosa).
To‘xtash va “well, let me think” tabiiy; asosiy — aniqlik.""",
    """📚 DARS 49: Tinglash (listening)
Kalit so‘zlarni oldindan toping; birinchi eshitishda umumiy ma’no, ikkinchisida detal.""",
    """📚 DARS 50: O‘qish (reading)
Skimming — umumiy fikr; scanning — raqam, sana, ism qidirish.
Savol turiga qarab matnga qaytish.""",
    """📚 DARS 51: So‘zlash (speaking)
STAR usuli: Situation, Task, Action, Result — ish suhbatlarida.
Oddiy gaplarda ham bog‘lovchilar: first, then, finally.""",
    """📚 DARS 52: Yozish xatolari
Run-on sentence — nuqta qo‘ying; fragment — to‘liq egalik+kesim kerak.
Subject-verb agreement: The data are… (ilmiy uslubda muhokama).""",
    """📚 DARS 53: Ko‘p tillilik (bilingualism)
Ikki til miyada alohida “yo‘llar”; aralashuv (code-switching) tabiiy.
Bolalarga bir tilda barqaror muhit muhim.""",
    """📚 DARS 54: Tarjima texnikasi
So‘zma-so‘z emas, ma’no birliklari (sense units).
Atamalarni bir tilda qotirish: terminologiya lug‘ati yarating.""",
    """📚 DARS 55: Korpus va til resurslari
Korpus — katta matnlar to‘plami; collocations (so‘z birikmasi) statistikasi.
Sketch Engine, COCA — ingliz uchun namuna.""",
]

# ----- 56–67: Lingvistika va nutq san’ati -----
_LING = [
    """📚 DARS 56: Fonologiya va fonema
Fonema — ma’noni ajratuvchi minimal tovush birligi (p/b farqi).
Allofon — fonemaning variantlari; transkripsiya IPA yordam beradi.""",
    """📚 DARS 57: Morfologiya va so‘z yasalishi
Affiks: prefiks, suffiks; ildiz va o‘zak tahlili.
Agglutinativ tillar (o‘zbek) — ko‘p qo‘shimcha zanjir.""",
    """📚 DARS 58: Sintaksis va daraxt
Sozlam (Phrase) → gap (Sentence). SVO — ingliz; SOV — o‘zbekda kesim oxirida.
Transformatsiyalar: so‘roq, inkor, passiv.""",
    """📚 DARS 59: Semantika
Polisemiya — bir so‘zning bir necha ma’nosi; sinonimiya va antonimiya.
Komponent tahlil: bachelor = +erkak +kuyov bo‘lmagan +yetuk.""",
    """📚 DARS 60: Pragmatika
Kontekst: kim, kimga, qachon. Indirekt nutq: “Xona sovuq” — deraza yop degani.
Grice maxims: miqdor, sifat, munosiblik, usul.""",
    """📚 DARS 61: Sotsiolingvistika
Til va sinf, gender, etnik guruh. Tabu va eufemizm.
Politika va til — rasmiy til tanlovi davlatda institutsional.""",
    """📚 DARS 62: Psixolingvistika
Nutqni qabul qilish va ishlab chiqarish modellari.
Ikki tillilikda “switching cost” va yosh omili.""",
    """📚 DARS 63: Diskurs tahlili
Matnning koherentligi — bog‘lovchilar va mavzu progressiyasi.
Genre: yangilik, ilmiy maqola, blog — har biri o‘z qoidasi.""",
    """📚 DARS 64: Leksikografiya va lug‘at loyihalari
Definitsiya yozish qoidalari: circular definitiondan qoching.
Elektron lug‘atlar va API — dasturchilar uchun integratsiya.""",
    """📚 DARS 65: Stilistik vositalar
Metafora, metonimiya, ironiya, hiperbola — badiiy va publicistik matn.
Uslubiy belgililik kontekstga bog‘liq.""",
    """📚 DARS 66: Nutq san’ati va persuasiya
Ethos, pathos, logos — klassik murojaat modellari.
Argument struktura: da’vo → dalil → misol → xulosa.""",
    """📚 DARS 67: Yakun: tilni o‘rganish rejasi
SMART maqsad: haftada 5 soat, 4 ko‘nikma (tinglash-o‘qish-yozish-gapirish).
O‘lchov: mini-test, dictation, shadowing. Muvaffaqiyat — barqarorlik!""",
]


def _build_en_lessons():
    out = []
    for i, (title, body) in enumerate(_EN_TITLES, start=16):
        out.append(
            f"📚 DARS {i}: {title}\n"
            f"{body}\n\n"
            "Amaliyot: 5 ta o‘zingiz yozilgan jumla (affirmative, negative, question). "
            "Xatolarni ertasi kuni qayta o‘qing — til miyani shakllantiradi."
        )
    return out


def _all_67_lessons():
    return list(_UZ_BLOCKS) + _build_en_lessons() + _PRACT + _LING


# Tekshiruv: aynan 67 ta
_LESSONS = _all_67_lessons()
assert len(_LESSONS) == 67, len(_LESSONS)

TIL_LESSONS = {
    "til_mega": {
        "title": "🌐 Til va tilshunoslik — 67 PRO dars (o‘zbek + ingliz + lingvistika)",
        "lessons": _LESSONS,
    }
}

# 20 ta quiz — til mavzusi bo‘yicha chuqur
TIL_QUIZZES = {
    "til_mega": [
        {
            "question": "O‘zbekda urg‘u odatda qayerda tushadi?",
            "options": ["Har doim birinchi bo‘g‘inda", "Ko‘pincha oxirgi bo‘g‘inda", "Faqat undoshda", "Faqat unlida"],
            "correct": 1,
            "explanation": "O‘zbek nutqida urg‘u odatda oxirgi bo‘g‘inda tushadi.",
        },
        {
            "question": "Present Perfect qachon ishlatiladi?",
            "options": [
                "Faqat o‘tmishda aniq vaqt bilan",
                "O‘tmishdagi harakat hozirgi natija bilan bog‘liq bo‘lganda (have/has + V3)",
                "Faqat kelajak",
                "Faqat hozirgi davomiy",
            ],
            "correct": 1,
            "explanation": "Present Perfect — o‘tmishdagi voqea, lekin hozirgi relevans muhim.",
        },
        {
            "question": "‘Must not’ va ‘don’t have to’ farqi?",
            "options": [
                "Farqi yo‘q",
                "must not — taqiq; don’t have to — majbur emas",
                "Ikkalasi ham majburiyat",
                "Faqat ikkalasi ham taqiq",
            ],
            "correct": 1,
            "explanation": "must not taqiq; don’t have to — shart emas.",
        },
        {
            "question": "Defining relative clause uchun qaysi vergul to‘g‘ri?",
            "options": [
                "The book, that I bought, … har doim",
                "Defining clause odatda vergulsiz; non-defining — vergul bilan",
                "which faqat vergulsiz",
                "who faqat inson emas",
            ],
            "correct": 1,
            "explanation": "Aniqlovchi qo‘shma gapda vergul ixtiyor emas; izohlovchi — vergul bilan ajratiladi.",
        },
        {
            "question": "Passive voice tuzilishi?",
            "options": ["have + V1", "be + V3", "will + V1", "do + V1"],
            "correct": 1,
            "explanation": "Passive: be + past participle (V3).",
        },
        {
            "question": "Second conditional tuzilishi?",
            "options": [
                "If + past, would + bare infinitive",
                "If + present, will",
                "If + will, would",
                "If + past perfect, would have",
            ],
            "correct": 0,
            "explanation": "If + past simple, would + V1 — hozirgi/yoki kelajakdagi gipoteza.",
        },
        {
            "question": "‘Advice’ so‘zi inglizcha?",
            "options": ["Countable", "Uncountable — a piece of advice", "Faqat plural", "Faqat gerund"],
            "correct": 1,
            "explanation": "advice — uncountable; ‘maslahatlar’ uchun a piece of advice / some advice.",
        },
        {
            "question": "Fonema nima?",
            "options": [
                "Har bir harf",
                "Ma’noni ajratuvchi minimal tovush birligi",
                "Faqat unli",
                "Faqat urg‘u",
            ],
            "correct": 1,
            "explanation": "Fonema — til tizimida ma’noni farqlaydigan minimal tovush.",
        },
        {
            "question": "Grice pragmatikasida ‘sifat maxsi’ nimani anglatadi?",
            "options": [
                "Ko‘p gapirish",
                "Haqiqiy va ishonchli ma’lumot berish",
                "Faqat qisqa gap",
                "Faqat rasmiy til",
            ],
            "correct": 1,
            "explanation": "Quality — haqiqiy dalillar; Grice maxsimalaridan biri.",
        },
        {
            "question": "O‘zbek gapida odatdagi tartib?",
            "options": ["SVO har doim", "Aniq kesim odatda oxirida (SOV tendentsiya)", "VSO", "OSV har doim"],
            "correct": 1,
            "explanation": "O‘zbekda kesim va to‘ldiruvchilar tartibi SOV ga yaqin.",
        },
        {
            "question": "Reported speech: ‘I am tired’ → u aytdi…",
            "options": [
                "he is tired",
                "he was tired (vaqt siljishi)",
                "he be tired",
                "he has tired",
            ],
            "correct": 1,
            "explanation": "O‘tmishda xabar berilganda zamon va vaqt holatlari siljiydi.",
        },
        {
            "question": "Gerund qaysi shakl?",
            "options": ["to + V1", "V-ing", "V3", "V2"],
            "correct": 1,
            "explanation": "Gerund — -ing shakli, fe’l ism sifatida.",
        },
        {
            "question": "‘However’ qanday bog‘lovchi?",
            "options": [
                "Faqat sabab",
                "Qarama-qarshilik / kontrast (rasmiy yozuvda)",
                "Faqat vaqt",
                "Faqat shart",
            ],
            "correct": 1,
            "explanation": "However — kontrast; odatda nuqta-vergul yoki yangi gap bilan.",
        },
        {
            "question": "Polisemiya — …",
            "options": [
                "Bir so‘zning bir necha bog‘liq ma’nosi",
                "Ikki so‘z bir ma’no",
                "Faqat antonim",
                "Faqat fonema",
            ],
            "correct": 0,
            "explanation": "Polisemiya — bir leksemaning bir necha ma’nosi.",
        },
        {
            "question": "STAR usuli qaysi kontekstda mashhur?",
            "options": [
                "Faqat matematika",
                "Ish suhbati — vaziyat bo‘yicha javob",
                "Faqat sport",
                "Faqat shifokorlik",
            ],
            "correct": 1,
            "explanation": "STAR — Situation, Task, Action, Result (behavioral interview).",
        },
        {
            "question": "Code-switching — …",
            "options": [
                "Faqat xato",
                "Ikki til o‘rtasida o‘tish (tabiiy ko‘p tillilik)",
                "Faqat grammatika",
                "Faqat yozuv",
            ],
            "correct": 1,
            "explanation": "Code-switching — bir nutqda tillar o‘rtasida o‘tish.",
        },
        {
            "question": "‘Few’ va ‘a few’ farqi?",
            "options": [
                "Farqi yo‘q",
                "few — kam (yetarli emas); a few — biroz bor (musbat)",
                "ikkisi ham ko‘p",
                "faqat sanalmas",
            ],
            "correct": 1,
            "explanation": "few — kam, yetishmaydi; a few — ozroq, lekin bor.",
        },
        {
            "question": "IPA transkripsiya nimaga xizmat qiladi?",
            "options": [
                "Faqat yozuv",
                "Tovushlarni xalqaro belgilar bilan aniq yozish",
                "Faqat tarix",
                "Faqat grammatika",
            ],
            "correct": 1,
            "explanation": "IPA — fonetik transkripsiya standarti.",
        },
        {
            "question": "Diskurs kогерентligi uchun nima muhim?",
            "options": [
                "Faqat uzun gap",
                "Mavzu, bog‘lovchilar va mantiqiy zanjir",
                "Faqat sinonim",
                "Faqat undov",
            ],
            "correct": 1,
            "explanation": "Koherentlik — gaplar o‘rtasida mantiqiy va leksik bog‘liqlik.",
        },
        {
            "question": "Agglutinativ tilga misol?",
            "options": ["Ingliz", "O‘zbek — ko‘p qo‘shimcha zanjiri bilan", "Xitoy", "Faqat fransuz"],
            "correct": 1,
            "explanation": "O‘zbek agglutinativ — affikslar zanjiri bilan so‘z yasaladi.",
        },
    ]
}

__all__ = ["TIL_LESSONS", "TIL_QUIZZES"]


# ── Barcha extended darslarni birlashtirish ──────────────
ALL_EXTENDED = {}
try:
    ALL_EXTENDED.update(EXTENDED_LESSONS)
except Exception as _e:
    pass
try:
    ALL_EXTENDED.update(TIL_LESSONS)
except Exception as _e:
    pass

EXTENDED_QUIZZES = {}
try:
    EXTENDED_QUIZZES.update(TIL_QUIZZES)
except Exception as _e:
    pass
