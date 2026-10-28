# Dating-Apps-Plan

Evaluasi kelayakan bisnis ide dating app Android/iOS dengan fitur "chemistry compatibility" (10 soal per sesi → % kecocokan di fitur nearby).

- **Report kelayakan:** [REPORT.md](REPORT.md) — verdict: **tidak layak dalam bentuk sekarang (skor 2,9/10)**, plus opsi pivot dan rencana validasi ≤ Rp 50 jt.
- **Simulasi:** `python3 analysis/compatibility_math.py` (overlap soal, noise skor, likuiditas) dan `python3 analysis/financial_model.py` (model keuangan 3 skenario, 24 bulan).
- **Rencana kerja pivot:** [PIVOT_PLAN.md](PIVOT_PLAN.md). Konsep "KLOP" (kuis chemistry → dinner grup → matchmaking premium): layak, base case butuh modal ~Rp 0,63 M dan break-even bulan ke-9. Model: `python3 analysis/pivot_model.py`.
