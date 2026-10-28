# Model pivot: kuis chemistry (akuisisi) -> dinner grup berbayar -> matchmaking premium -> B2B/sponsor.
# Semua angka Rupiah dan ASUMSI kecuali disebut lain. Jalankan: python3 analysis/pivot_model.py
import math

PPN = 1.11            # harga jual termasuk PPN 11%
PAY_FEE = 0.03        # payment gateway (QRIS/VA/e-wallet), konservatif

# --- 1. Sizing pasar bottom-up: Jabodetabek ---
def sizing():
    pop = 34_000_000          # penduduk Jabodetabek [asumsi, ~SP2020]
    age = 0.17                # porsi usia 25-35 [asumsi]
    single = 0.35             # belum menikah di kelompok usia tsb, urban [asumsi]
    income = 0.30             # profesional, penghasilan >= Rp 7 jt/bln [asumsi]
    intent = 0.20             # serius cari pasangan & mau ikut event offline [asumsi]
    events_per_year = 3
    steps = [("Penduduk Jabodetabek", pop), ("Usia 25-35", pop*age), ("Belum menikah", pop*age*single),
             ("Profesional (>= Rp 7 jt/bln)", pop*age*single*income), ("Niat serius + mau event (SAM)", pop*age*single*income*intent)]
    print("== Sizing Jabodetabek ==")
    for k, v in steps:
        print(f"{k:32s} {v:12,.0f}")
    sam = steps[-1][1]
    print(f"Potensi kursi/bulan (SAM x {events_per_year} event/thn / 12): {sam*events_per_year/12:,.0f}")
    return sam

# --- 2. Unit economics per kursi dinner ---
def seat_economics(price):
    net = price / PPN
    pay = price * PAY_FEE
    host = 300_000 / 18       # 1 host freelance pegang 3 meja x 6 orang per malam
    ops = 10_000              # kartu soal, name tag, reservasi, buffer no-show
    cm = net - pay - host - ops
    return net, pay, host, ops, cm

# --- 3. Model 36 bulan, 3 skenario ---
S = {
  "Bear": dict(seats_mature=500,  ramp=14, price=179_000, prem_rate=0.004, prem_price=5_000_000,  b2b=0,          cities=[1]),
  "Base": dict(seats_mature=1200, ramp=12, price=199_000, prem_rate=0.008, prem_price=7_500_000,  b2b=15_000_000, cities=[1, 13]),
  "Bull": dict(seats_mature=2200, ramp=10, price=229_000, prem_rate=0.012, prem_price=10_000_000, b2b=40_000_000, cities=[1, 13, 19]),
}
SETUP = 200_000_000          # validasi Rp 50 jt + MVP PWA & ops awal Rp 150 jt (bulan 0)
TEAM_EARLY = 45_000_000      # M1-6: ops lead, dev freelance, konten, lain-lain
TEAM_LATER = 95_000_000      # M7+: + matchmaker, CS, koordinator host, marketing lead
CITY_FIXED = 35_000_000      # per kota tambahan: city manager + ops
MKT_CITY = 40_000_000        # marketing per kota aktif per bulan
MKT_LAUNCH = 60_000_000      # tambahan di bulan launch kota baru
TECH = 5_000_000
MATCHMAKER_COST = 0.25       # porsi revenue premium untuk konsultan/matchmaker
NEW_SHARE = 0.40             # porsi kursi dari pembeli baru (sisanya repeat)
PAID_SHARE = 0.50            # porsi pembeli baru yang datang dari iklan (sisanya referral/organik)
CAC = 111_111                # dari funnel kuis: Rp 4.000/kuis selesai / (30% waitlist x 12% beli)
OPS_PER_1000 = 15_000_000    # tambahan koordinator event + CS per 1.000 kursi/bulan
OVERHEAD = 0.10              # legal, akuntan, refund/no-show, asuransi event, coworking (% revenue)

def seats_in_city(age_months, p):
    # kurva-S menuju kapasitas matang dalam `ramp` bulan
    x = age_months / p["ramp"]
    return p["seats_mature"] / (1 + math.exp(-6 * (x - 0.5))) if age_months > 0 else 0

def run(name, p, verbose=True):
    cum = -SETUP; low = cum; be = None; rows = []
    for m in range(1, 37):
        active = [c for c in p["cities"] if m >= c]
        seats = sum(seats_in_city(m - c + 1, p) for c in active)
        _, pay, host, ops, cm = seat_economics(p["price"])
        rev_seat = seats * p["price"] / PPN
        prem_clients = seats * p["prem_rate"] if m >= 7 else 0   # premium dibuka bulan 7
        rev_prem = prem_clients * p["prem_price"] / PPN
        rev_b2b = p["b2b"] * len(active) if m >= 9 else 0
        rev = rev_seat + rev_prem + rev_b2b
        var = seats * (pay + host + ops) + rev_prem * MATCHMAKER_COST + prem_clients * p["prem_price"] * PAY_FEE
        fixed = (TEAM_EARLY if m <= 6 else TEAM_LATER) + CITY_FIXED * (len(active) - 1) + TECH + OPS_PER_1000 * seats / 1000
        mkt = max(MKT_CITY * len(active), seats * NEW_SHARE * PAID_SHARE * CAC) + MKT_LAUNCH * sum(1 for c in p["cities"] if c == m)
        net = rev - var - fixed - mkt - rev * OVERHEAD
        cum += net; low = min(low, cum)
        if be is None and net > 0: be = m
        rows.append(dict(m=m, seats=seats, rev=rev, rev_seat=rev_seat, rev_prem=rev_prem, rev_b2b=rev_b2b, net=net, cum=cum))
    y = lambda a, b: sum(r["rev"] for r in rows[a:b])
    yn = lambda a, b: sum(r["net"] for r in rows[a:b])
    if verbose:
        print(f"\n=== {name} === kota: {len(p['cities'])} | BEP bulanan pertama: M{be} | kebutuhan modal: Rp{-low/1e9:.2f} M")
        for r in rows:
            if r["m"] in (3, 6, 12, 18, 24, 36):
                print(f"M{r['m']:2d} kursi {r['seats']:6,.0f} | rev Rp{r['rev']/1e6:6,.0f} jt (dinner {r['rev_seat']/1e6:4,.0f}, premium {r['rev_prem']/1e6:4,.0f}, b2b {r['rev_b2b']/1e6:3,.0f}) | net Rp{r['net']/1e6:6,.0f} jt | kum Rp{r['cum']/1e9:5.2f} M")
        for i, (a, b) in enumerate([(0, 12), (12, 24), (24, 36)], 1):
            print(f"Tahun {i}: revenue Rp{y(a,b)/1e9:5.2f} M | laba operasional Rp{yn(a,b)/1e9:5.2f} M")
    return rows, be, low

if __name__ == "__main__":
    sizing()
    print("\n== Unit economics per kursi ==")
    for price in (179_000, 199_000, 229_000):
        net, pay, host, ops, cm = seat_economics(price)
        print(f"Tiket Rp{price:,} | net PPN Rp{net:,.0f} | payment Rp{pay:,.0f} | host Rp{host:,.0f} | ops Rp{ops:,.0f} | kontribusi Rp{cm:,.0f} ({cm/net*100:.0f}%)")
    # CAC dari funnel kuis
    cpq, q2w, w2b = 4_000, 0.30, 0.12   # biaya per kuis selesai, kuis->waitlist, waitlist->beli
    cac = cpq / (q2w * w2b)
    _, _, _, _, cm = seat_economics(199_000)
    print(f"\nCAC pembeli pertama: Rp{cac:,.0f} | payback: {cac/cm:.2f} event | LTV (3 event/thn, 1,5 thn): Rp{cm*4.5:,.0f} -> LTV/CAC {cm*4.5/cac:.1f}")
    prem_net = 7_500_000 / PPN
    print(f"Premium Rp7,5 jt: net Rp{prem_net:,.0f} | kontribusi Rp{prem_net*(1-MATCHMAKER_COST)-7_500_000*PAY_FEE:,.0f}")
    for k, p in S.items():
        run(k, p)
    print("\n== Sensitivitas: Base tanpa premium ==")
    p = dict(S["Base"]); p["prem_rate"] = 0
    rows, be, low = run("Base tanpa premium", p, verbose=False)
    print(f"BEP M{be} | modal Rp{-low/1e9:.2f} M | laba thn 3 Rp{sum(r['net'] for r in rows[24:36])/1e9:.2f} M")
