# Dating-Apps-Plan

Evaluasi kelayakan bisnis ide dating app Android/iOS dengan fitur "chemistry compatibility" (10 soal per sesi → % kecocokan di fitur nearby).

- **Report kelayakan:** [REPORT.md](REPORT.md) — verdict: **tidak layak dalam bentuk sekarang (skor 2,9/10)**, plus opsi pivot dan rencana validasi ≤ Rp 50 jt.
- **Simulasi:** `python3 analysis/compatibility_math.py` (overlap soal, noise skor, likuiditas) dan `python3 analysis/financial_model.py` (model keuangan 3 skenario, 24 bulan).
- **Blueprint KLOP v2 (lean-first):** [PIVOT_PLAN.md](PIVOT_PLAN.md). Kuis chemistry → dinner grup → matchmaking premium, dijalankan 3 co-founder + 2 founding host + 1 AI agent. Base case: kas keluar maksimum Rp 15 jt, laba sejak bulan pertama. Model: `python3 analysis/lean_model.py` (v2) dan `python3 analysis/pivot_model.py` (v1, tim bergaji).
- **Pitch untuk calon rekan:** [PITCH.md](PITCH.md) (versi teks dari deck 16 slide) dan prototype yang bisa diklik di [prototype/klop-prototype.html](prototype/klop-prototype.html). Analisis komisi restoran ada di `PIVOT_PLAN.md` bagian 12 dan `python3 analysis/lean_model.py`.
