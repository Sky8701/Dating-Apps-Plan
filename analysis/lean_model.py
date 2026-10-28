# Model KLOP v2 (lean-first): founder tanpa gaji di awal, 1 AI agent, marketing organik-first, belum PKP.
# Semua angka Rupiah dan ASUMSI kecuali disebut lain. Jalankan: python3 analysis/lean_model.py
import math

USD = 16_500                 # kurs [asumsi]
PPH_FINAL = 0.005            # PPh final UMKM 0,5% dari omzet (belum PKP, tanpa PPN)
PAY_FEE = 0.015              # campuran QRIS ~0,7%, VA Rp 4.000, e-wallet 1,5-1,8% [asumsi]
OPS_SEAT = 8_000             # kartu ice-breaker cetak, name tag, buffer no-show
HOST_NIGHT = 300_000         # host berbayar / founding host bagi hasil, pegang 3 meja = 18 kursi
FREE_HOST_SEATS = 232        # 3 co-founder inti host 1 malam/minggu: 3 x 4,3 x 18 kursi

# --- 1. Anggaran Fase 0 (minggu 1-8) ---
PHASE0 = [
    ("Merek DJKI kelas 45, tarif UMKM", 500_000),
    ("Domain + email bisnis", 300_000),
    ("AI agent: Claude Max 5x, 2 bulan", 2 * 100 * USD),
    ("Iklan TikTok/IG (uji kuis)", 6_000_000),
    ("Materi 2 dinner pilot (kartu, name tag, reservasi)", 2_000_000),
    ("Produksi konten (transport, properti)", 1_000_000),
    ("Cadangan refund & tak terduga", 1_900_000),
]

# --- 2. Biaya tetap bulanan lean (bulan ke-m) ---
def fixed_cost(m):
    c = 100 * USD                       # AI agent (Claude Max 5x)
    c += 500_000                        # tools: domain, Canva/Google gratis, buffer
    if m >= 6: c += 25 * USD            # Supabase Pro (backup harian) setelah ada data nyata
    if m >= 7: c += 1_000_000           # WhatsApp Business API (pesan utility/marketing)
    if m >= 4: c += 1_000_000           # konsultan pajak/akuntan retainer
    return c

ONE_OFF = {3: 7_000_000 + 1_500_000}    # M3: akta PT biasa via notaris [asumsi] + merek 3 kelas tambahan (9, 41, 42)
ADS = 3_000_000                          # iklan minimum per bulan, sisanya organik/referral/komunitas
ADS_REINVEST = 0.15                      # atau 15% revenue diinvestasikan ulang ke iklan, mana yang lebih besar

def seat_economics(price):
    pay = price * PAY_FEE
    tax = price * PPH_FINAL
    host_paid = HOST_NIGHT / 18
    cm_free = price - pay - tax - OPS_SEAT                # kursi yang di-host co-founder
    cm_paid = cm_free - host_paid                         # kursi dengan host berbayar
    return pay, tax, host_paid, cm_free, cm_paid

S = {
  "Bear": dict(seats_mature=150, ramp=14, price=149_000, prem_rate=0.004, prem_price=3_500_000, b2b=0,          partner_from=None),
  "Base": dict(seats_mature=500, ramp=12, price=169_000, prem_rate=0.006, prem_price=5_000_000, b2b=5_000_000,  partner_from=None),
  "Bull": dict(seats_mature=900, ramp=10, price=179_000, prem_rate=0.010, prem_price=7_500_000, b2b=15_000_000, partner_from=13),
}
MATCHMAKER_SHARE = 0.20      # komisi untuk founder/konsultan yang menjalankan matchmaking
PARTNER_RATIO = 0.40         # kota city-partner = 40% volume Jakarta
PARTNER_TAKE = 0.30          # KLOP ambil 30% tiket kota partner (platform, brand, engine)

def seats_curve(age, mature, ramp):
    if age <= 0: return 0
    return mature / (1 + math.exp(-6 * (age / ramp - 0.5)))

def run(name, p, verbose=True):
    phase0 = sum(v for _, v in PHASE0)
    cum = -phase0; low = cum; be = None; rows = []
    _, _, host_paid, cm_free, cm_paid = seat_economics(p["price"])
    for m in range(1, 25):
        seats = seats_curve(m, p["seats_mature"], p["ramp"])
        free = min(seats, FREE_HOST_SEATS); paid = seats - free
        rev_seat = seats * p["price"]
        prem = seats * p["prem_rate"] if m >= 7 else 0
        rev_prem = prem * p["prem_price"]
        rev_b2b = p["b2b"] if m >= 9 else 0
        rev_partner = 0
        if p["partner_from"] and m >= p["partner_from"]:
            pseats = seats_curve(m - p["partner_from"] + 1, p["seats_mature"] * PARTNER_RATIO, p["ramp"])
            rev_partner = pseats * p["price"] * PARTNER_TAKE
        rev = rev_seat + rev_prem + rev_b2b + rev_partner
        var = (rev_seat - free * cm_free - paid * cm_paid) + rev_prem * (MATCHMAKER_SHARE + PAY_FEE + PPH_FINAL) \
              + (rev_b2b + rev_partner) * PPH_FINAL
        cost = var + fixed_cost(m) + max(ADS, rev * ADS_REINVEST) + ONE_OFF.get(m, 0)
        profit = rev - cost                                   # laba sebelum kompensasi founder
        cum += profit; low = min(low, cum)
        if be is None and profit > 0: be = m
        rows.append(dict(m=m, seats=seats, rev=rev, rev_seat=rev_seat, rev_prem=rev_prem, rev_b2b=rev_b2b,
                         rev_partner=rev_partner, profit=profit, cum=cum))
    if verbose:
        print(f"\n=== {name} === laba bulanan pertama: M{be} | kas keluar maksimum: Rp{-low/1e6:,.1f} jt")
        for r in rows:
            if r["m"] in (3, 6, 9, 12, 18, 24):
                print(f"M{r['m']:2d} kursi {r['seats']:5,.0f} | rev Rp{r['rev']/1e6:6,.1f} jt | laba Rp{r['profit']/1e6:6,.1f} jt"
                      f" | per founder (3) Rp{r['profit']/3/1e6:5,.1f} jt | (5) Rp{r['profit']/5/1e6:5,.1f} jt | kum Rp{r['cum']/1e6:7,.1f} jt")
        for i, (a, b) in enumerate([(0, 12), (12, 24)], 1):
            pr = sum(r["profit"] for r in rows[a:b])
            print(f"Tahun {i}: revenue Rp{sum(r['rev'] for r in rows[a:b])/1e9:.2f} M | laba sebelum kompensasi founder Rp{pr/1e6:,.0f} jt"
                  f" | per founder/bln: 3 org Rp{pr/12/3/1e6:.1f} jt, 5 org Rp{pr/12/5/1e6:.1f} jt")
    return rows, be, low

# --- 3. Pendapatan tambahan dari restoran (dihitung terpisah dari model inti) ---
AVG_SPEND = 200_000          # belanja makan/minum per peserta di venue $$ Senopati/Kemang [asumsi]
WEEKNIGHT_SHARE = 0.60       # porsi kursi di slot Senin-Kamis (slot yang mau dibayar venue) [asumsi]
RESTO_START = 4              # bulan mulai menagih restoran (setelah ritme & data rating ada)
RESTO_OPTIONS = {
    "A. Per-cover fee Rp 15 rb (malam sepi)": dict(kind="cover", fee=15_000),
    "B. Komisi 10% tagihan (bocor 30%)":       dict(kind="pct", pct=0.10, leak=0.30),
    "C. Set menu 'Dinner Plus' (30% ambil)":  dict(kind="bundle", take=0.30, sell=225_000, buy=185_000),
    "D. Venue partner Rp 2,5 jt/bln/venue":   dict(kind="partner", fee=2_500_000),
}

def partner_venues(m):
    return 0 if m < 6 else (3 if m < 10 else 5)

def restaurant_income(p, opt):
    out = []
    for m in range(1, 25):
        seats = seats_curve(m, p["seats_mature"], p["ramp"])
        extra = gross = 0.0
        if m >= RESTO_START:
            if opt["kind"] == "cover":
                gross = seats * WEEKNIGHT_SHARE * opt["fee"]
                extra = gross * (1 - PPH_FINAL)
            elif opt["kind"] == "pct":
                gross = seats * AVG_SPEND * opt["pct"] * (1 - opt["leak"])
                extra = gross * (1 - PPH_FINAL)
            elif opt["kind"] == "bundle":
                plus = seats * opt["take"]
                gross = plus * opt["sell"]                      # omzet KLOP ikut naik (makanan ikut ditagih)
                extra = plus * (opt["sell"] - opt["buy"]) - gross * (PAY_FEE + PPH_FINAL)
            elif opt["kind"] == "partner":
                gross = partner_venues(m) * opt["fee"]
                extra = gross * (1 - PPH_FINAL)
        out.append((m, gross, extra))
    return out

def print_restaurant(name, p):
    rows, _, _ = run(name, p, verbose=False)
    base_y1 = sum(r["profit"] for r in rows[:12]); base_y2 = sum(r["profit"] for r in rows[12:])
    print(f"\n== Pendapatan restoran: {name} (laba inti thn 1 Rp{base_y1/1e6:,.0f} jt, thn 2 Rp{base_y2/1e6:,.0f} jt) ==")
    for k, opt in RESTO_OPTIONS.items():
        r = restaurant_income(p, opt)
        y1 = sum(x[2] for x in r[:12]); y2 = sum(x[2] for x in r[12:]); m12 = r[11][2]; g2 = sum(x[1] for x in r[12:])
        print(f"{k:40s} | M12 +Rp{m12/1e6:5.1f} jt/bln | thn1 +Rp{y1/1e6:5.0f} jt | thn2 +Rp{y2/1e6:5.0f} jt (+{y2/base_y2*100:4.1f}% laba)"
              f" | omzet tambahan thn2 Rp{g2/1e6:,.0f} jt")
    # porsi yang diambil dari belanja tamu di venue: pembanding beban bagi restoran (opsi tidak ditumpuk)
    seats24 = seats_curve(24, p["seats_mature"], p["ramp"])
    spend_per_venue = seats24 / partner_venues(24) * AVG_SPEND
    print(f"Beban restoran (% belanja tamu): A {15_000/AVG_SPEND:.1%} di malam sepi | B {0.10:.0%} tertagih {0.10*0.7:.0%}"
          f" | C diskon grup {(225_000-185_000)/225_000:.0%} | D {2_500_000/spend_per_venue:.1%} ({seats24/partner_venues(24):.0f} kursi/venue/bln)")

if __name__ == "__main__":
    print("== Anggaran Fase 0 ==")
    for k, v in PHASE0:
        print(f"{k:52s} Rp{v:>12,.0f}")
    print(f"{'TOTAL':52s} Rp{sum(v for _, v in PHASE0):>12,.0f}")
    print(f"Offset tiket pilot (2 dinner x 24 kursi x Rp149rb): Rp{2*24*149_000:,.0f}")
    print("\n== Biaya tetap bulanan ==")
    for m in (1, 4, 7):
        print(f"M{m}: Rp{fixed_cost(m) + ADS:,.0f} (termasuk iklan minimum Rp{ADS:,}; naik ke 15% revenue saat omzet > Rp 20 jt)")
    print("\n== Unit economics per kursi ==")
    for price in (149_000, 169_000, 179_000):
        pay, tax, host, cf, cp = seat_economics(price)
        print(f"Rp{price:,}: payment Rp{pay:,.0f} | PPh final Rp{tax:,.0f} | ops Rp{OPS_SEAT:,} | kontribusi host co-founder Rp{cf:,.0f} ({cf/price*100:.0f}%)"
              f" | host berbayar Rp{cp:,.0f} ({cp/price*100:.0f}%)")
    print(f"Kapasitas host co-founder gratis: {FREE_HOST_SEATS} kursi/bulan")
    for k, p in S.items():
        run(k, p)
    print(f"\nAsumsi restoran: belanja Rp{AVG_SPEND:,}/orang, {WEEKNIGHT_SHARE:.0%} kursi di malam sepi, mulai M{RESTO_START}")
    for k in ("Base", "Bull"):
        print_restaurant(k, S[k])
