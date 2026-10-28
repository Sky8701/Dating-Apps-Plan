# KLOP — Pitch untuk Calon Rekan

> Ketemu orang yang klop, secara langsung.
> **Deck:** https://claude.ai/artifact/Xt3qgxT2zKdTpa99wA93uJ · **Prototype:** https://claude.ai/artifact/QZ6QRha8SN8iq8cLHhEimg (salinan: [`prototype/klop-prototype.html`](prototype/klop-prototype.html))
> **Blueprint lengkap:** [`PIVOT_PLAN.md`](PIVOT_PLAN.md) · **Model:** [`analysis/lean_model.py`](analysis/lean_model.py)
> Link artifact bersifat privat sampai dibagikan lewat menu Share.

---

## 1. Masalahnya

| Angka | Artinya | Sumber |
|---|---|---|
| **69%** | dating app di-uninstall dalam bulan pertama | Global Dating Insights |
| **−8,7%** | paying users Bumble (Q2 2025); Tinder −5% YoY | Nasdaq, Barchart |
| **1,48 jt** | pernikahan di Indonesia 2024, turun 6,3% setahun dan −28,6% dalam 10 tahun | BPS via Katadata |

Orang tidak berhenti ingin bertemu. Yang gagal adalah cara bertemunya.

## 2. Kenapa sekarang

1. **Uang ada di niat serius.** Matchmaking adalah segmen dating terbesar di Indonesia berdasarkan revenue (Statista). Biro jodoh premium memasang tarif Rp 3–129 jt.
2. **Modelnya sudah terbukti.** Timeleft mempertemukan orang asing lewat kuis dan dinner 6 orang: ±90 kota, lebih dari 400 rb user, Series A US$7 jt (2024).
3. **Membangunnya kini murah.** Satu AI agent (±Rp 1,65 jt/bulan) mengerjakan pekerjaan developer. Fase validasi cukup Rp 15 jt.

## 3. Solusinya

| Anak tangga | Produk | Harga | Peran |
|---|---|---:|---|
| Akuisisi | Kuis KLOP (20 soal, kartu hasil, bandingkan dengan teman) | Gratis | Konten yang menyebar sendiri |
| Arus kas | KLOP Dinner: meja 6 orang dipilih algoritma, dipandu host | Rp 169 rb | Makan dibayar peserta ke venue |
| Retensi | Mutual match: kontak WhatsApp terbuka hanya kalau saling pilih | – | Data pertemuan melatih algoritma |
| Margin | KLOP Serius: matchmaker, verifikasi KTP, 2–6 perkenalan 1-on-1 | Rp 3,5–7,5 jt | Untuk yang siap berkomitmen |

Tanpa swipe, tanpa chat in-app, tanpa lokasi real-time.

**Cara kerja satu malam:** main kuis 4 menit → pilih jadwal & bayar QRIS → info meja H-1 via WhatsApp → dinner 2–3 jam (3 pria + 3 perempuan, usia ±5 tahun, dipandu host) → pilih secara rahasia "mau ketemu lagi" → saling pilih, kontak dibuka.

## 4. Prototype

Mockup sembilan layar yang bisa diklik: sambutan, profil, kuis (skor dihitung sungguhan), kartu hasil, pilih dinner, QRIS (simulasi), tiket & meja dengan kartu ice-breaker, pilihan setelah dinner, mutual match + tawaran KLOP Serius. Panel samping menampilkan dashboard ops contoh: susunan meja dan laba per malam. Semua nama dan angka peserta adalah data contoh.

## 5. Kenapa kami bisa menang

Format dinner bisa ditiru dalam sebulan. Yang sulit ditiru adalah tumpukan ini: **merek** terdaftar sejak minggu pertama, **rahasia dagang** (bobot soal & aturan meja hanya di server), **data pertemuan nyata**, **komunitas alumni**, **kontrak venue**, **reputasi aman untuk perempuan**, dan **ritme** dinner tiap minggu.

## 6. Unit economics

| Per kursi (tiket Rp 169 rb, belum PKP) | Rp |
|---|---:|
| Payment 1,5% + PPh final 0,5% + kartu/buffer | −11.380 |
| **Kontribusi, host co-founder (93%)** | **157.620** |
| Kontribusi, host berbayar (83%) | 140.953 |

- **Titik impas:** 33–48 kursi per bulan (≈ 2–3 meja per minggu).
- **Biaya tetap:** Rp 5–8 jt per bulan.
- **Tiket dibayar di muka**, makanan dibayar peserta ke venue.

## 7. Pendapatan tambahan dari restoran

| Opsi | +Laba tahun 2 (base) | Beban restoran | Sikap |
|---|---:|---|---|
| A. Per-cover fee Rp 15 rb, Senin–Kamis | +Rp 53 jt (+6%) | 7,5% belanja tamu | **Mulai bulan 4** |
| B. Komisi 10% tagihan | +Rp 83 jt (+10%) | 10% | Tidak: sulit diverifikasi |
| C. Dinner Plus (tiket + set menu) | +Rp 63 jt (+8%) | diskon grup 18% | Opsional, tahun 2 |
| D. Venue partner Rp 2,5 jt/bln | +Rp 149 jt (+18%) | 12,5% belanja tamu | **Bulan 6–10, menggantikan A** |
| E. Natura (welcome drink, meja terjamin) | hemat biaya | rendah | Sejak pilot |

Pembanding: Timeleft sengaja tidak menarik komisi agar netral; OpenTable menarik ±US$1–1,5 per tamu. **Aturan netralitas:** venue dipilih dari rating peserta, komisi tidak pernah memengaruhi meja.

## 8. Pasar

Jabodetabek: 34 jt penduduk → 5,78 jt usia 25–35 → 2,02 jt belum menikah → 607 rb profesional → **121 rb orang dengan niat serius dan mau ikut event** (faktor tiap lapisan adalah asumsi). Itu ±30.300 kursi/bulan potensi. Base case cukup **500 kursi/bulan (≈ 1,7%)**.

## 9. Pesaing

| Pemain | Cara bertemu | Fokus | Celah |
|---|---|---|---|
| Tinder · Bumble · Omi | Swipe & chat | Campuran | Lelah swipe; 69% uninstall < 1 bulan |
| Timeleft | Dinner 6 orang via kuis | Pertemanan | Bukan untuk niat serius |
| Biro jodoh premium | Konsultan 1-on-1 | Serius | Rp 10–129 jt, manual |
| Setipe · Taaruf ID | Profil & tes online | Serius | Tanpa pertemuan terkurasi |
| **KLOP** | **Kuis → dinner 6 → match** | **Serius, terjangkau** | Komunitas harus dibangun |

## 10. Rencana bergate

| Tahap | Waktu & kas | Lanjut jika |
|---|---|---|
| Validasi | Minggu 1–8, Rp 15 jt | Waitlist ≥ 1.000, perempuan ≥ 40%, kursi pilot terjual ≥ 70% |
| Ritme Jakarta | Bulan 1–6, dari tiket | ≥ 200 kursi/bln, repeat ≥ 30%, NPS ≥ 50 |
| Monetisasi | Bulan 7–12, dari laba | ≥ 400 kursi/bln, ≥ 3 klien premium/bln |
| Replikasi | Bulan 13–24 | Format baru, city partner kota ke-2; funding hanya setelah angka terbukti |

## 11. Proyeksi 24 bulan (Jakarta)

| Metrik | Bear | **Base** | Bull |
|---|---:|---:|---:|
| Kursi/bulan matang | 150 | **500** | 900 |
| Kas keluar maksimum | Rp 34 jt | **Rp 15 jt** | Rp 15 jt |
| Laba bulanan pertama | bulan 5 | **bulan 1** | bulan 1 |
| Revenue tahun 2 | Rp 288 jt | **Rp 1,25 M** | Rp 3,06 M |
| Laba tahun 2 (sebelum kompensasi founder) | Rp 165 jt | **Rp 844 jt** | Rp 2,11 M |
| Per founder/bulan, tahun 1 (3 orang) | Rp 0,9 jt | **Rp 11,5 jt** | Rp 30,5 jt |

Komisi restoran menambah +6–18% laba base. Variabel paling tidak pasti: kecepatan tumbuh organik.

## 12. Tim yang kami cari

| Peran | Status | Komitmen |
|---|---|---|
| Produk, tech & keuangan | Terisi (Hendri) | 8–12 jam/minggu |
| **Komunitas & operasional** | **Dicari, paling kritis** | 20–25 jam/minggu → full-time |
| **Growth & konten** | **Dicari** | 10–15 jam/minggu |
| 2 founding host | Rp 300 rb/malam + ESOP 1–2% | 1–2 malam/minggu |
| 1 AI agent | ±Rp 1,65 jt/bulan | Developer, analis data, draft konten |

Equity (ilustrasi, dibahas bersama): 40 / 30 / 20 + ESOP 10, vesting 4 tahun dengan cliff 1 tahun, IP milik PT.

## 13. Risiko & jawabannya

| Risiko | Jawaban |
|---|---|
| Rasio gender timpang | Kursi dirilis 50:50, marketing women-first |
| Co-founder kelelahan | Batas jam realistis, stipend saat laba ≥ Rp 30 jt/bln |
| Ditiru EO atau Timeleft | Data pertemuan, komunitas, niat serius, premium |
| Insiden keamanan | Host di tiap meja, verifikasi, venue publik, SOP insiden |
| Tumbuh terlalu lambat | Reinvest 15% revenue ke iklan, gate bulan ke-6 |

## 14. Ajakan

**Yang kami minta:** 20–25 jam/minggu selama 6 bulan pertama, memimpin komunitas & operasional atau growth & konten, ikut hosting 1 malam per minggu.
**Yang kamu dapat:** equity co-founder dengan vesting, stipend saat laba ≥ Rp 30 jt/bulan, bisnis dengan risiko modal kecil.
**Langkah berikut:** ngopi 1 jam · main prototype · datang ke dinner pilot #1.

---

**Sumber:** lihat bagian Sumber di [`PIVOT_PLAN.md`](PIVOT_PLAN.md) dan [`REPORT.md`](REPORT.md).
