#!/usr/bin/env python3
"""ex2's decisive probe: c_sector_det_power_probe (2026-08-24).

EXERCISE TIER, READ-ONLY.  Nothing here is a claim, registration, adoption or
amendment; every statement is a measurement of already-landed objects.  Exact
rationals/algebraics only; no float enters any decision.

THE QUESTION (ex2_first_principles_reduction.md, sections (a)-(d)): what det
EXPONENT does the record-slice c-sector contribute to the landed 12x6 partition
function Z = integral exp(-phi^dagger Q phi) (H1-170b, closure-audit-two lines
137-141 -- the same measure declaration the ACCEPTED b179 cell consumed)?
Calibrators of known slot count, both read by the b179-accepted operation
(direct restriction of the committed form):
  (i)  the b179 accepted cell  f_(1,0,0): ONE complex slot <-> ONE det factor
       beta = 3193/2240 (2 real integration dims; realified det beta^2);
  (ii) the level-4 singleton fiber (one reflection-class object): ONE 2-dim
       fiber <-> ONE conjugate-pair det factor a4^2+d4^2 (power 1, never 2).
The c-sector is the unique sector where restriction = exact Z-factor (the
disconnection).  Fork: c-factor = (62866/30625)^2 (additive: the measure
carries both orbit-cells) vs (62866/30625)^1 (the sigma-real halved carrier).
"""
from __future__ import annotations

import subprocess
import sys
import time
import types
from pathlib import Path

import sympy as sp

R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_dirac_kahler_closure_audit_two_2026_08_21 as b170  # noqa: E402

CHECKS: list = []


def check(label: str, ok) -> None:
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def zero(m) -> bool:
    return sp.expand(m) == sp.zeros(*m.shape)


def load_arbiter():
    """The fork arbiter, from origin/main exactly as b179 loaded it."""
    rel = "scripts/berezin_detc_detr_fork_2026_06_04.py"
    run = subprocess.run(["git", "-C", str(ROOT), "show", f"origin/main:{rel}"],
                         capture_output=True, text=True)
    src = run.stdout if run.returncode == 0 else (ROOT / rel).read_text()
    mod = types.ModuleType("berezin_arbiter")
    mod.__file__ = str(ROOT / rel)
    sys.modules["berezin_arbiter"] = mod
    exec(compile(src, rel, "exec"), mod.__dict__)
    return mod.__dict__


t0 = time.time()
print("== c_sector_det_power_probe: bench, constant carrier, committed dials ==")
arb = load_arbiter()
CPair, F = arb["CPair"], arb["F"]
bench = b170.Bench("12x6", 12, 6)
fx = bench.fx
# the campaign-record constant carrier: volume 7/5 everywhere; shear 0 on the
# pinned levels {0,1}, 3/5 elsewhere; dials s_x=3/5, s_t=0, m=1 (b180/b181).
field = {(t, x): (sp.Integer(0) if t in (0, 1) else R(3, 5), R(7, 5))
         for (t, x) in fx.CELLS}
env = b170.b166.carrier_substitution(fx, field)
env.update({b170.SX: R(3, 5), b170.ST: sp.Integer(0), b170.MASS: sp.Integer(1)})
Q = sp.expand(bench.Q.subs(env))
N = fx.PHYS
check("Q is 36x36, symbol-free, exact rational, real",
      N == 36 and not Q.free_symbols
      and all(Q[i, j].is_Rational for i in range(N) for j in range(N)))

w = R(-1, 2) + sp.sqrt(3) * I / 2          # omega, disclosed cyclotomic


def site(t: int, x: int) -> int:
    return 6 * (t % 6) + (x % 6)


def f(k: int, t: int, b: int):
    v = sp.zeros(N, 1)
    for j in range(3):
        v[site(t, b + 2 * j), 0] = w ** ((-k * j) % 3) / sp.sqrt(3)
    return v


U = sp.zeros(N, N)
for t in range(6):
    for x in range(6):
        U[site(t, x + 2), site(t, x)] = 1
check("chart symmetry: U^3 = I and [Q, U] = 0",
      sp.expand(U ** 3) == sp.eye(N) and zero(Q * U - U * Q))

S = [site(1, x) for x in range(6)]
comp = [i for i in range(N) if i not in S]
check("the disconnection: full record slice t=1 decouples in Q (both ways)",
      all(Q[i, j] == 0 and Q[j, i] == 0 for i in S for j in comp))

a, d = R(43, 35), R(129, 175)
J2 = sp.Matrix([[0, 1], [-1, 0]])
B1 = f(1, 1, 0).row_join(f(1, 1, 1))
B2 = f(2, 1, 0).row_join(f(2, 1, 1))
check("c-blocks: B_k^dag Q B_k = aI + dJ, a=43/35, d=129/175, both charts",
      zero(B1.H * Q * B1 - (a * sp.eye(2) + d * J2))
      and zero(B2.H * Q * B2 - (a * sp.eye(2) + d * J2))
      and zero(B1.H * B1 - sp.eye(2)) and zero(B2.H * B2 - sp.eye(2)))

s2 = sp.sqrt(2)
u_p, u_m = sp.Matrix([1, I]) / s2, sp.Matrix([1, -I]) / s2
g_p, g_m, h_p, h_m = B1 * u_p, B1 * u_m, B2 * u_p, B2 * u_m
lam_p, lam_m = a + d * I, a - d * I
check("four eigenlines: Q g+- = (a +- di) g+-, Q h+- = (a +- di) h+-",
      zero(Q * g_p - lam_p * g_p) and zero(Q * g_m - lam_m * g_m)
      and zero(Q * h_p - lam_p * h_p) and zero(Q * h_m - lam_m * h_m))

r = bench.r
check("slice reflection acts as identity on the sector columns",
      zero(r * B1 - B1) and zero(r * B2 - B2))
Theta = lambda v: r * v.conjugate()                                # noqa: E731
check("Theta-orbits O+ = {g+, h-}, O- = {g-, h+} (Theta g+- = h-+)",
      zero(Theta(g_p) - h_m) and zero(Theta(g_m) - h_p)
      and zero(Theta(h_m) - g_p) and zero(Theta(h_p) - g_m))

X0 = sp.diag(*[sp.Integer(-1) ** (t + x)
               for t in range(6) for x in range(6)])
env2 = dict(env)
env2[b170.SX] = -R(3, 5)
Qm = sp.expand(bench.Q.subs(env2))
check("landed grading: X0 Q(+3/5) X0 = Q(-3/5); X0 g+ = -g-, X0 h- = -h+",
      zero(X0 * Q * X0 - Qm) and zero(X0 * g_p + g_m) and zero(X0 * h_m + h_p))
sigma = lambda v: -r * X0 * v.conjugate()          # noqa: E731  sigma=-Theta.X0
v1, v2 = g_p + h_p, sp.expand(I * (g_p - h_p))
check("sigma = -Theta o X0: antilinear involution of E+, sigma g+ = h+; "
      "Fix(sigma) = {z g+ + zbar h+} is real-2-dim (the halved carrier)",
      zero(sigma(g_p) - h_p) and zero(sigma(h_p) - g_p)
      and zero(sigma(v1) - v1) and zero(sigma(v2) - v2))

print("== the landed Z, factored over the disconnection (exact dets) ==")
QS = Q[S, S]
Qrest = Q[comp, comp]
detQ, detQS, detQrest = Q.det(), QS.det(), Qrest.det()
check("det Q = det(slice) * det(rest): the c-factor is a true Z-factor",
      sp.expand(detQ - detQS * detQrest) == 0)
E0 = f(0, 1, 0).row_join(f(0, 1, 1))
K0 = sp.expand(E0.H * Q * E0)                       # the k=0 slice fiber
V = g_p.row_join(g_m).row_join(h_p).row_join(h_m)
C4 = sp.expand(V.H * Q * V)
check("the c-sector 4x4 is exactly diag(lam+, lam-, lam+, lam-)",
      zero(C4 - sp.diag(lam_p, lam_m, lam_p, lam_m)))
to_cpair = lambda z: CPair(F(sp.re(z)), F(sp.im(z)))               # noqa: E731
Fc_arb = arb["det_cpair"](tuple(tuple(to_cpair(C4[i, j]) for j in range(4))
                                for i in range(4)))
Fc = sp.nsimplify(F(Fc_arb.re)) + sp.nsimplify(F(Fc_arb.im)) * I
unit = a ** 2 + d ** 2                              # one orbit-cell det content
check("c-factor by the arbiter's det_cpair = det(slice)/det(k=0 fiber) "
      "(site-basis extraction, no basis choice)",
      Fc_arb.im == 0 and sp.expand(Fc - detQS / K0.det()) == 0)

print("== calibrators (both read by the b179-accepted restriction) ==")
beta = sp.expand((f(1, 0, 0).H * Q * f(1, 0, 0))[0, 0])
check("b179 accepted cell reproduces: beta = 3193/2240; one slot <-> ONE det "
      "factor (det_C[[beta]] = beta, realified beta^2, 2 real dims)",
      beta == R(3193, 2240)
      and arb["det_cpair"](((to_cpair(beta),),)).re == F(3193, 2240)
      and arb["det_fraction"](arb["complex_realification"](to_cpair(beta)))
      == F(3193, 2240) ** 2)
B14 = f(1, 4, 0).row_join(f(1, 4, 1))
D4 = sp.expand(B14.H * Q * B14)
a4, d4 = D4[0, 0], D4[0, 1]
check("level-4 singleton fiber: D4 = a4(I + s_x J), a4 = 1817/1120; one "
      "2-dim object <-> ONE pair-det factor a4^2+d4^2 (power 1)",
      a4 == R(1817, 1120) and d4 == a4 * R(3, 5)
      and zero(D4 - (a4 * sp.eye(2) + d4 * J2))
      and sp.expand(D4.det() - (a4 ** 2 + d4 ** 2)) == 0)
check("level-4 fiber is chain-coupled (a restriction cell, NOT a Z-factor); "
      "the c-fiber alone is both",
      any(Q[site(4, x), site(t2, y)] != 0
          for x in range(6) for t2 in (3, 5) for y in range(6)))

print("== the measure-content pin: the committed covariance on the sector ==")
GS, Grest = QS.inv(method="LU"), Qrest.inv(method="LU")
G = sp.zeros(N, N)
for p, i in enumerate(S):
    for q, j in enumerate(S):
        G[i, j] = GS[p, q]
for p, i in enumerate(comp):
    for q, j in enumerate(comp):
        G[i, j] = Grest[p, q]
check("G = Q^{-1} exact (assembled over the disconnection, Q G = I)",
      zero(Q * G - sp.eye(N)))
Ginv_c = (a * sp.eye(2) - d * J2) / unit
check("full unconstrained-Gaussian covariance on ALL FOUR eigenlines: "
      "B_k^dag G B_k = (aI - dJ)/(a^2+d^2), both charts -- no halved carrier",
      zero(sp.expand(B1.H * G * B1) - Ginv_c)
      and zero(sp.expand(B2.H * G * B2) - Ginv_c))
W9 = sp.expand((G + G.T) / 2)
check("landed W9 fiber cross-checks: w_1 = 875/1462, w_4 = "
      "2667060781000/5517939189281",
      zero(sp.expand(B1.H * W9 * B1) - R(875, 1462) * sp.eye(2))
      and zero(sp.expand(B14.H * W9 * B14)
               - R(2667060781000, 5517939189281) * sp.eye(2)))

print("== THE EXPONENT, calibrated ==")
print(f"  one-cell unit  a^2+d^2          = {unit}")
print(f"  measured c-sector factor of Z   = {Fc}")
check("EXPONENT 2: c-factor = (62866/30625)^2 = 3952133956/937890625 exactly",
      unit == R(62866, 30625) and Fc == unit ** 2
      and Fc == R(3952133956, 937890625))
check("NOT the halved carrier: c-factor != (62866/30625)^1",
      Fc != unit)
p_exp = 2 if Fc == unit ** 2 else (1 if Fc == unit else None)
rr = arb["r_from_slot_count"](p_exp)
check("arbiter composition: n = 2 cells -> r = 1 -> Q = 1 committed; the "
      "sigma-reality bit (n=1 -> r=1/2 -> Q=2/3) is NEW input",
      rr == F(1) and arb["q_from_r"](rr) == F(1)
      and arb["q_from_r"](arb["r_from_slot_count"](1)) == F(2, 3))

fails = [lab for lab, ok in CHECKS if not ok]
print(f"\nCHECKS: PASS={len(CHECKS) - len(fails)} FAIL={len(fails)}"
      f"  ({time.time() - t0:.0f}s)")
print("VERDICT: the landed measure integrates the FULL sector -- four "
      "eigenlines, two Theta-orbit cells, det exponent 2 -- additive counting "
      "is what the committed Z contains; quotient counting is FALSE of "
      "committed structure; Q = 2/3 requires the one sigma-reality bit "
      "(carrier = Fix(-Theta o X0)) as new physical input.")
if fails:
    print("FAILURES:", ", ".join(fails))
sys.exit(1 if fails else 0)
