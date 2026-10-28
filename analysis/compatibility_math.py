from math import comb
# --- 1. Overlap soal random (hypergeometric) ---
print("== Overlap soal: 2 user, masing2 10 soal random dari bank N ==")
for N in [30,50,100,200,500]:
    k=10
    exp=k*k/N
    def p_ge(m):
        return sum(comb(k,i)*comb(N-k,k-i) for i in range(m,k+1))/comb(N,k)
    print(f"N={N:4d} E[overlap]={exp:5.2f}  P(>=5)={p_ge(5)*100:6.2f}%  P(>=3)={p_ge(3)*100:6.2f}%  P(0)={(1-p_ge(1))*100:5.1f}%")

# --- 2. Noise skor dari 10 soal biner ---
import math
print("\n== Noise skor 10 soal A/B: jika true chemistry 50%, 95% CI skor ==")
for n in [10,30,100,230]:
    se=math.sqrt(0.25/n)
    print(f"n={n:3d} soal: 50% ± {1.96*se*100:4.1f} pp")
# pasangan acak total, P(skor>=70%) murni kebetulan
p=sum(comb(10,i) for i in range(7,11))/2**10
print(f"P(skor>=70% murni kebetulan, 10 soal 50/50) = {p*100:.1f}%")
p=sum(comb(10,i) for i in range(8,11))/2**10
print(f"P(skor>=80% murni kebetulan) = {p*100:.1f}%")

# --- 3. Likuiditas nearby ---
print("\n== Likuiditas: MAU DKI Jakarta yg dibutuhkan agar 1 user pria melihat X kandidat aktif ==")
area_city=661; r=5; area_r=math.pi*r*r; share_area=area_r/area_city
for label,conc,fem,age,chem in [("optimis",0.10,0.35,0.6,1.0),("realistis",0.06,0.28,0.5,1.0),("realistis+filter chem>=60%",0.06,0.28,0.5,0.38)]:
    f=share_area*conc*fem*age*chem
    for target in [10,20]:
        print(f"{label:28s} target {target:2d} kandidat -> MAU {target/f:9,.0f}")
