# Model 24 bulan, launch 1 kota (Jabodetabek). Semua angka Rupiah, ASUMSI.
S = {
 "Bear": dict(mkt=150e6, cpi=25_000, organic=0.3, act=0.55, m1=0.25, mret=0.70, conv=0.015, arppu=60_000),
 "Base": dict(mkt=150e6, cpi=18_000, organic=0.6, act=0.60, m1=0.35, mret=0.78, conv=0.03,  arppu=80_000),
 "Bull": dict(mkt=150e6, cpi=12_000, organic=1.0, act=0.65, m1=0.45, mret=0.85, conv=0.05,  arppu=100_000),
}
BUILD=750e6        # MVP 5-6 bln (bulan 0, sebelum launch)
OPEX=125e6         # tim inti + moderasi/CS + legal/compliance per bulan
INFRA_PER_MAU=700  # server realtime+chat, OTP, verifikasi selfie (amortisasi), maps, push
NET=0.70           # setelah fee store 15-30%, pajak, payment
rows={}
for name,p in S.items():
    cohorts=[]; cum=-BUILD; be=None; out=[]
    for m in range(1,25):
        paid=p["mkt"]/p["cpi"]; new=paid*(1+p["organic"])*p["act"]
        cohorts.append(new)
        mau=0
        for age,c in enumerate(reversed(cohorts)):
            mau+= c if age==0 else c*p["m1"]*p["mret"]**(age-1)
        rev=mau*p["conv"]*p["arppu"]*NET
        cost=p["mkt"]+OPEX+mau*INFRA_PER_MAU
        net=rev-cost; cum+=net
        if be is None and net>0: be=m
        out.append((m,mau,rev,cost,net,cum))
    rows[name]=(out,be)
    print(f"\n=== {name} === break-even operasional bulan: {be}")
    for m,mau,rev,cost,net,cum in out:
        if m in (3,6,12,18,24):
            print(f"M{m:2d} MAU {mau:8,.0f} | Rev/bln Rp{rev/1e6:7,.0f} jt | Cost Rp{cost/1e6:5,.0f} jt | Net Rp{net/1e6:7,.0f} jt | Kumulatif Rp{cum/1e9:6.2f} M")
    minc=min(r[5] for r in out); print(f"Kebutuhan modal (titik terendah kumulatif): Rp{-minc/1e9:.2f} M")
    # LTV/CAC
    life=1+p["m1"]/(1-p["mret"])  # bulan aktif rata2 per user aktif
    ltv=life*p["conv"]*p["arppu"]*NET
    cac=p["cpi"]/p["act"]
    print(f"LTV/user aktif Rp{ltv:,.0f} | CAC paid/user aktif Rp{cac:,.0f} | LTV/CAC {ltv/cac:.2f}")
    blended=p["mkt"]/((p["mkt"]/p["cpi"])*(1+p["organic"])*p["act"])
    cm=p["conv"]*p["arppu"]*NET-INFRA_PER_MAU
    print(f"Blended CAC Rp{blended:,.0f} | margin kontribusi/MAU/bln Rp{cm:,.0f} | MAU utk BEP (tutup OPEX+mkt) {(OPEX+p['mkt'])/cm if cm>0 else float('inf'):,.0f}")
