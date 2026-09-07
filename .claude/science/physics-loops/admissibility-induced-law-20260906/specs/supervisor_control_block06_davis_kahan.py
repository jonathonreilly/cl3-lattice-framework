"""Control 4 (revised after the lens): the self-adjoint residual-gap route to rigorous rational enclosures of the deep-row
pair statistics; exact outward-rounded decimal labels (integer arithmetic only); the sector-vs-full-state execution (S1);
tr(Q^2) printed. Float appears nowhere in a reported digit."""
import sys; sys.argv=['x']
exec(open('supervisor_control_block06_feasibility.py').read().split("for W in (4,5):")[0])
from fractions import Fraction as F
from math import isqrt
import time
def dec_down(x: F, digits: int) -> str:
    n = x.numerator * 10**digits // x.denominator; s = str(n).rjust(digits+1, "0"); return s[:-digits] + "." + s[-digits:]
def dec_up(x: F, digits: int) -> str:
    n = -((-x.numerator * 10**digits) // x.denominator); s = str(n).rjust(digits+1, "0"); return s[:-digits] + "." + s[-digits:]
def sqrt_upper(x: F) -> F:
    scale = 10**80; n = x.numerator * scale * scale // x.denominator + 1; return F(isqrt(n) + 1, scale)
out = []
table = []
for W in (4, 5):
    for tr in [(3,1,2),(5,2,4)]:
        t0 = time.time(); rows, idx, A, V, reps, orbit_of, Q = build(tr, W); n = len(reps)
        size = [0]*n
        for r in rows: size[orbit_of[r]] += 1
        Avec = [A(rep) for rep in reps]; w = [size[o]*Avec[o] for o in range(n)]
        sa = all(w[o]*Q[o][p] == w[p]*Q[p][o] for o in range(n) for p in range(n))
        inner = (W//2 - 1, W//2)
        cin = [F(sum(1 for r in rows if orbit_of[r]==o and r[inner[0]]==r[inner[1]]), size[o]) for o in range(n)]
        ced = [F(sum(1 for r in rows if orbit_of[r]==o and r[0]==r[1]), size[o]) for o in range(n)]
        trQ2 = sum(Q[o][p]*Q[p][o] for o in range(n) for p in range(n))
        y = [1]*n
        for _ in range(40): y = [sum(Q[i][j]*y[j] for j in range(n)) for i in range(n)]
        Qy = [sum(Q[i][j]*y[j] for j in range(n)) for i in range(n)]
        ny = sum(w[o]*y[o]*y[o] for o in range(n))
        mu = F(sum(w[o]*y[o]*Qy[o] for o in range(n)), ny)
        res2 = F(sum(w[o]*(Qy[o]-mu*y[o])**2 for o in range(n)), ny)
        lo = min(F(Qy[o], y[o]) for o in range(n)); hi = max(F(Qy[o], y[o]) for o in range(n))
        lam2b = sqrt_upper(F(trQ2) - lo*lo); delta = mu - lam2b; assert delta > 0 and lo > lam2b
        eps = sqrt_upper(F(2)) * sqrt_upper(res2) / delta
        sin_b = sqrt_upper(res2) / delta
        s_in = sum(F(w[o]*y[o]*y[o], ny)*cin[o] for o in range(n)); s_ed = sum(F(w[o]*y[o]*y[o], ny)*ced[o] for o in range(n))
        f = F(tr[0], tr[0]+tr[1]+4*tr[2])
        encl = {"inner": (s_in-2*eps, s_in+2*eps), "edge": (s_ed-2*eps, s_ed+2*eps)}
        ex = all(not (a <= f <= b) for a, b in encl.values())
        out.append(f"W={W} {tr}: orbits {n}; self-adjoint {sa}; tr(Q^2) = {trQ2}; lambda_1 in [{lo}, {hi}] = [{dec_down(lo,21)}, {dec_up(hi,21)}] (width < 10^-{len(str((hi-lo).denominator))-len(str((hi-lo).numerator))-1}); mu in CW interval: {lo<=mu<=hi}")
        out.append(f"   lambda_2 bound {lam2b} <= {dec_up(lam2b, 6)}; ratio bound <= {dec_up(lam2b/lo, 7)}; sin theta <= {dec_up(sin_b*10**int(len(str(sin_b.denominator))-len(str(sin_b.numerator))), 3)} x 10^-{len(str(sin_b.denominator))-len(str(sin_b.numerator))}")
        out.append(f"   s_edge in [{dec_down(encl['edge'][0],25)}, {dec_up(encl['edge'][1],25)}]; s_inner in [{dec_down(encl['inner'][0],25)}, {dec_up(encl['inner'][1],25)}]; f = {f}; excluded: {ex}; s_inner - s_edge = {dec_down(s_in-s_ed,10)}..; s_edge - f = {dec_down(s_ed-f,8)}.., s_inner - f = {dec_down(s_in-f,8)}..  [{time.time()-t0:.0f}s]")
        table.append((W, tr, dec_down(lo,18), dec_up(hi,18), dec_down(encl['edge'][0],22), dec_up(encl['edge'][1],22), dec_down(encl['inner'][0],22), dec_up(encl['inner'][1],22), f, dec_up(lam2b/lo,5), dec_up(sin_b*10**int(len(str(sin_b.denominator))-len(str(sin_b.numerator))),2), len(str(sin_b.denominator))-len(str(sin_b.numerator))))
        if W == 4:
            # S1: sector finite-n values against the full-state computation, both pairs
            R = [[0]*n for _ in range(n)]
            for r in rows:
                o = orbit_of[r]
                for j, rep2 in enumerate(reps): R[o][j] += V(r, rep2)*A(rep2)
            N = len(rows); Afull = [A(r) for r in rows]
            Tm = [[V(r, r2)*Afull[idx[r2]] for r2 in rows] for r in rows]
            for nrows in (3, 5, 7):
                c = nrows//2
                left = Avec[:]
                for _ in range(c): left = [sum(left[o]*R[o][j] for o in range(n)) for j in range(n)]
                right = [1]*n
                for _ in range(nrows-1-c): right = [sum(Q[i][j]*right[j] for j in range(n)) for i in range(n)]
                Z = sum(left[o]*right[o]*size[o] for o in range(n))
                sec_in = F(sum(left[o]*right[o]*size[o]*cin[o] for o in range(n)), Z); sec_ed = F(sum(left[o]*right[o]*size[o]*ced[o] for o in range(n)), Z)
                lf = Afull[:]
                for _ in range(c): lf = [sum(lf[i]*Tm[i][j] for i in range(N)) for j in range(N)]
                rf = [1]*N
                for _ in range(nrows-1-c): rf = [sum(Tm[i][j]*rf[j] for j in range(N)) for i in range(N)]
                wf = [lf[i]*rf[i] for i in range(N)]; Zf = sum(wf)
                full_in = F(sum(wf[i] for i, r in enumerate(rows) if r[inner[0]]==r[inner[1]]), Zf); full_ed = F(sum(wf[i] for i, r in enumerate(rows) if r[0]==r[1]), Zf)
                out.append(f"   S1 n={nrows}: sector == full-state: inner {sec_in==full_in}, edge {sec_ed==full_ed}")
        print("\n".join(out[-4 if W==4 else -3:]), flush=True)
print("\nTABLE (exact outward-rounded decimals):")
print("| W | triple | lambda_1 in | s_edge in | s_inner in | f | ratio bound | sin theta bound |")
for W, tr, a, b, c, d, e, g, f, rb, sb, se in table:
    print(f"| {W} | {tr} | [{a}, {b}] | [{c}, {d}] | [{e}, {g}] | {f} | <= {rb} | <= {sb} x 10^-{se} |")
