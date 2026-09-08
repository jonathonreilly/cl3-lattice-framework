#!/usr/bin/env python3
"""Bounded checks for supplied indexed-effect menu families.

The original 49 check identities, census, grids, matrices and flip patterns are
preserved. Exact rational checks and the labelled float64 model are distinct;
finite certificates do not establish the continuum theorem in the note's appendix.

The historical b7_census.py, b7_rank.py, b7_sign.py and h3_helpers.py names below
are authoring-trace labels, not imported files or files landed by this packet.
All used implementations are inline. The declared laws are restated here;
no physical formation, outcome-index registration or joint resampling law follows.
The float block specializes the open-plane branch of PR #7973's original runner
at 5b080fca1ebaee23ea4d4e1eccfd08a8b001e60b, rather than copying it verbatim:
it removes the periodic branch, unused returns/method, and renames locals. Its
fixed matrix/relaxation operations are preserved; the corrected window routine
now computes the complete finite eigensystem. Exact proof/source identities and
the self-contained continuum proof are in the paired note. No parent campaign
is imported or accepted through these provenance references.
"""

import math
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, permutations, product
from math import factorial

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    'docs/THE_BORN_PRICE_WORDINGS_HOMOGENEITY_IS_PAYABLE_ON_THE_CONTINUUM_LAW_AS_IT_STANDS_THE_COLLINEAR_MENUS_NEED_A_SCALE_READING_RULE_THE_FOUR_OUTCOME_MENU_PAYS_WITH_NO_CLAUSE_AND_NONE_REMOVES_THE_FAIR_COIN_BOUNDED_NOTE_2026-09-05.md',
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


PASS = 0
FAIL = 0


def check(label, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS " + label)
    else:
        FAIL += 1
        print("FAIL " + label)


# These are premise/proof-context inputs, not numerical data. Bind the current
# paired proof and governing interpretation to the cache; all numeric inputs
# remain inline. Missing/unreadable paths fail before the census.
_INPUT_BYTES = {rel: (Path(__file__).resolve().parents[1] / rel).read_bytes()
                for rel in AUDIT_INPUT_PATHS}
print("INPUT_SHA256 " + json.dumps({rel: hashlib.sha256(body).hexdigest()
                                    for rel, body in _INPUT_BYTES.items()}, sort_keys=True))
check("Q0 [source] paired proof readable; current Record memo retains permanence",
      bool(_INPUT_BYTES[AUDIT_INPUT_PATHS[0]])
      and b"records are permanent" in _INPUT_BYTES[AUDIT_INPUT_PATHS[1]].lower())


# ===================================================================== T1, the census
# --- exact vector helpers (b7_census.py:41-115) -------------------------------
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def smul(s, a):
    return tuple(s * x for x in a)


def solve_exact(A, b):
    """Unique exact solution of an overdetermined rational system, else None."""
    n = len(A[0])
    m = [list(r) + [bb] for r, bb in zip(A, b)]
    pivots = []
    rank = 0
    for col in range(n):
        sel = None
        for i in range(rank, len(m)):
            if m[i][col] != 0:
                sel = i
                break
        if sel is None:
            continue
        m[rank], m[sel] = m[sel], m[rank]
        piv = m[rank][col]
        m[rank] = [x / piv for x in m[rank]]
        for i in range(len(m)):
            if i != rank and m[i][col] != 0:
                f = m[i][col]
                m[i] = [x - f * y for x, y in zip(m[i], m[rank])]
        pivots.append(col)
        rank += 1
    for i in range(rank, len(m)):
        if m[i][n] != 0:
            return None
    if rank < n:
        return None
    x = [F(0)] * n
    for r, pc in enumerate(pivots):
        x[pc] = m[r][n]
    return tuple(x)


def ternary_weights(n1, n2, n3):
    A = [[n1[0], n2[0], n3[0]], [n1[1], n2[1], n3[1]], [n1[2], n2[2], n3[2]],
         [F(1), F(1), F(1)]]
    c = solve_exact(A, [F(0), F(0), F(0), F(2)])
    if c is None or any(x <= 0 for x in c):
        return None
    return c


def circle_dir(t):
    d = 1 + t * t
    return ((1 - t * t) / d, 2 * t / d, F(0))


def unit_from_stereo(p, q):
    d = p * p + q * q + 1
    return (2 * p / d, 2 * q / d, (p * p + q * q - 1) / d)


# --- the laws (b7_census.py:118-181) ------------------------------------------
def dirs_of(cond):
    """Reading R1 of PR #7973: a `cI` record carries no Bloch direction."""
    return [rec[2] for rec in cond if rec[0] == "P"]


def recs_P(cond):
    return [(rec[1], rec[2]) for rec in cond if rec[0] == "P"]


ONE_I = (("I", F(1)),)


def L_CONT(cond):
    """PR #7926's record-echo law, verbatim in its branch structure."""
    ms = dirs_of(cond)
    if len(ms) == 1:
        m = ms[0]
        return (("P", F(1), m), ("P", F(1), neg(m)))
    if len(ms) == 3:
        c = ternary_weights(*ms)
        if c is not None:
            return tuple(("P", c[k], ms[k]) for k in range(3))
        return ONE_I
    if len(ms) == 2:
        a = (1 + dot(ms[0], ms[1])) / 2
        if 0 < a < 1:
            return (("I", a), ("I", 1 - a))
        return ONE_I
    return ONE_I


def L_MOD(cond, m3=False):
    """`L_CONT` with the record scales read on the collinear conditions.

    M1  one record `cP(m)`:                {cP(m), (1-c)P(m), P(-m)}
    M2  antipodal `c1P(m), c2P(-m)`:       {cP(m), cP(-m), (1-c)I}, c = (c1+c2)/2
    M3  (`L_4` only) equal `c1P(m), c2P(m)` with c1 + c2 <= 1:
                                           {c1P(m), c2P(m), (1-c1-c2)P(m), P(-m)}
    Every other branch is `L_CONT`'s; the degenerate member is dropped at c = 1."""
    ps = recs_P(cond)
    if len(ps) == 1:
        c, m = ps[0]
        if c == 1:
            return (("P", F(1), m), ("P", F(1), neg(m)))
        return (("P", c, m), ("P", 1 - c, m), ("P", F(1), neg(m)))
    if len(ps) == 2:
        (c1, m1), (c2, m2) = ps
        if m2 == neg(m1):
            c = (c1 + c2) / 2
            if c == 1:
                return (("P", F(1), m1), ("P", F(1), neg(m1)))
            return (("P", c, m1), ("P", c, neg(m1)), ("I", 1 - c))
        if m3 and m2 == m1 and c1 + c2 <= 1:
            if c1 + c2 == 1:
                return (("P", c1, m1), ("P", c2, m1), ("P", F(1), neg(m1)))
            return (("P", c1, m1), ("P", c2, m1), ("P", 1 - c1 - c2, m1),
                    ("P", F(1), neg(m1)))
    return L_CONT(cond)


def L_A(cond):
    return L_MOD(cond, m3=False)


def L_4(cond):
    return L_MOD(cond, m3=True)


LAWS = [("L_CONT", L_CONT), ("L_A", L_A), ("L_4", L_4)]


# --- menu classifier (b7_census.py:184-233) -----------------------------------
def resolves(S):
    tr = sum(2 * it[1] if it[0] == "I" else it[1] for it in S)
    v = (F(0), F(0), F(0))
    for it in S:
        if it[0] == "P":
            v = add(v, smul(it[1], it[2]))
    return tr == 2 and v == (F(0), F(0), F(0)) and all(0 < it[1] <= 1 for it in S)


def menu_type(S):
    if not resolves(S):
        return "NOT-A-RESOLUTION"
    Ps = [it for it in S if it[0] == "P"]
    Is = [it for it in S if it[0] == "I"]
    if not Ps:
        if len(Is) == 1:
            return "I"
        if len(Is) == 2:
            return "coin"
        return "coin-arity-%d" % len(Is)
    if not Is:
        ds = [it[2] for it in Ps]
        if len(Ps) == 2 and ds[1] == neg(ds[0]) and Ps[0][1] == 1 and Ps[1][1] == 1:
            return "binary"
        if len(Ps) == 3:
            same = [i for i in range(3) if sum(1 for j in range(3) if ds[j] == ds[i]) == 2]
            if len(same) == 2:
                k = [i for i in range(3) if i not in same][0]
                if ds[k] == neg(ds[same[0]]) and Ps[k][1] == 1:
                    return "collinear3"
            if len({ds[0], ds[1], ds[2]}) == 3 and ternary_weights(*ds) is not None:
                return "balanced3"
        if len(Ps) == 4:
            cnt = {}
            for d in ds:
                cnt[d] = cnt.get(d, 0) + 1
            if sorted(cnt.values()) == [1, 3]:
                mm = [d for d, c in cnt.items() if c == 3][0]
                k = [i for i in range(4) if ds[i] == neg(mm)]
                if k and Ps[k[0]][1] == 1:
                    return "collinear4"
        return "rank-one-other-%d" % len(Ps)
    if len(Ps) == 2 and len(Is) == 1 and Ps[1][2] == neg(Ps[0][2]) \
            and Ps[0][1] == Ps[1][1] and Is[0][1] == 1 - Ps[0][1]:
        return "mixed3"
    return "mixed-other"


# --- the declared alphabet (b7_census.py:236-252) -----------------------------
m1 = circle_dir(F(0))
m2 = circle_dir(F(2))
m3d = circle_dir(F(-2))
ez = (F(0), F(0), F(1))
D6 = [m1, m2, m3d, neg(m1), ez, neg(ez)]
SCALES = [F(1), F(1, 2), F(1, 4)]
LETTERS = [None, ("I", F(1)), ("I", F(1, 2))] + [("P", c, d) for c in SCALES for d in D6]
NL = len(LETTERS)
SLOTS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

check("C0 [exact] alphabet: %d letters per slot (blank, I, I/2, cP(d), c in {1,1/2,1/4}, "
      "6 unit directions)" % NL,
      NL == 21 and all(dot(d, d) == 1 for d in D6))


# --- the complete multiset census (b7_census.py:255-330) ----------------------
def multiplicity(idx):
    cnt = {}
    for i in idx:
        cnt[i] = cnt.get(i, 0) + 1
    mm = factorial(6)
    for v in cnt.values():
        mm //= factorial(v)
    return mm


tab = {name: {} for name, _ in LAWS}
echo_fail = {name: 0 for name, _ in LAWS}
bulk_bad = {name: 0 for name, _ in LAWS}
scale_blind_fail = 0
diff_A = {}
diff_4 = {}
nms = 0
ncond = 0
for idx in combinations_with_replacement(range(NL), 6):
    cond = [LETTERS[i] for i in idx if LETTERS[i] is not None]
    mult = multiplicity(idx)
    nms += 1
    ncond += mult
    ms = dirs_of(cond)
    kP = len(ms)
    S = {}
    for name, law in LAWS:
        S[name] = law(cond)
        t = menu_type(S[name])
        tab[name][(kP, t)] = tab[name].get((kP, t), 0) + mult
        if not all(it[2] in ms or neg(it[2]) in ms for it in S[name] if it[0] == "P"):
            echo_fail[name] += mult
        if kP == 6 and S[name] != ONE_I:
            bulk_bad[name] += mult
    unit = [("P", F(1), r[2]) if r[0] == "P" else r for r in cond]
    if L_CONT(unit) != S["L_CONT"]:
        scale_blind_fail += mult
    if S["L_A"] != S["L_CONT"]:
        ps = recs_P(cond)
        if kP == 1:
            cls = "1 record, c < 1"
        elif kP == 2 and ps[1][1] == neg(ps[0][1]):
            cls = "2 antipodal records"
        else:
            cls = "OTHER"
        diff_A[cls] = diff_A.get(cls, 0) + mult
    if S["L_4"] != S["L_A"]:
        ps = recs_P(cond)
        if kP == 2 and ps[1][1] == ps[0][1] and ps[0][0] + ps[1][0] <= 1:
            cls = "2 equal-direction records, c1 + c2 <= 1"
        else:
            cls = "OTHER"
        diff_4[cls] = diff_4.get(cls, 0) + mult

by_type = {}
for name, _ in LAWS:
    d = {}
    for (kP, t), v in tab[name].items():
        d[t] = d.get(t, 0) + v
    by_type[name] = d
print("     counts over 21^6: L_CONT bin %d coin %d bal3 %d | L_A +col3 %d +mix3 %d (bin %d) | "
      "L_4 +col4 %d" % (by_type["L_CONT"]["binary"], by_type["L_CONT"]["coin"],
                        by_type["L_CONT"]["balanced3"], by_type["L_A"]["collinear3"],
                        by_type["L_A"]["mixed3"], by_type["L_A"]["binary"],
                        by_type["L_4"]["collinear4"]))

check("C1 [exact] complete census: %d multisets of 6 letters = 21^6 = %d conditions"
      % (nms, ncond), nms == 230230 and ncond == 21 ** 6)
types = {name: {t for (_, t) in tab[name]} for name, _ in LAWS}
check("C2 [exact] L_CONT realises exactly {I, binary, coin, balanced3}: col3, mix3, col4 "
      "never occur",
      types["L_CONT"] == {"I", "binary", "coin", "balanced3"})
check("C3 [exact] L_CONT is scale-blind: indexed output tuple unchanged with all scales set to 1, "
      "%d/%d failures" % (scale_blind_fail, ncond), scale_blind_fail == 0)
check("C4 [exact] L_A realises exactly {I, binary, coin, balanced3, collinear3, mixed3}",
      types["L_A"] == {"I", "binary", "coin", "balanced3", "collinear3", "mixed3"})
check("C5 [exact] L_4 realises that family plus collinear4",
      types["L_4"] == {"I", "binary", "coin", "balanced3", "collinear3", "mixed3", "collinear4"})
check("C6 [exact] L_A differs from L_CONT exactly on 1-record c<1 (%d) and 2-antipodal (%d)"
      % (diff_A.get("1 record, c < 1", -1), diff_A.get("2 antipodal records", -1)),
      set(diff_A) == {"1 record, c < 1", "2 antipodal records"}
      and diff_A["1 record, c < 1"] == 17496 and diff_A["2 antipodal records"] == 43740)
check("C7 [exact] L_4 differs from L_A exactly on 2-equal-direction c1+c2<=1 conditions (%d)"
      % diff_4.get("2 equal-direction records, c1 + c2 <= 1", -1),
      set(diff_4) == {"2 equal-direction records, c1 + c2 <= 1"}
      and diff_4["2 equal-direction records, c1 + c2 <= 1"] == 29160)
check("C8 [exact] echo lemma, all three laws: every indexed-output direction is recorded or its "
      "antipode, 0 fails", all(v == 0 for v in echo_fail.values()))
check("C9 [exact] all 18^6 = %d fully direction-recorded conditions give {I}, all three laws"
      % tab["L_CONT"].get((6, "I"), 0),
      all(v == 0 for v in bulk_bad.values()) and tab["L_CONT"].get((6, "I"), 0) == 18 ** 6)
check("C10 [exact] every realised indexed output tuple of every law resolves I_2 exactly",
      all(t in {"I", "binary", "coin", "balanced3", "collinear3", "mixed3", "collinear4"}
          for name, _ in LAWS for t in types[name]))
kA = {(k, t): v for (k, t), v in tab["L_A"].items() if t in ("collinear3", "mixed3")}
k4 = {(k, t): v for (k, t), v in tab["L_4"].items() if t == "collinear4"}
check("C11 [exact] L_A: col3 only at kP=1 (%d), mix3 only at kP=2 (%d); L_4: col4 only at "
      "kP=2 (%d)" % (kA.get((1, "collinear3"), -1),
                                            kA.get((2, "mixed3"), -1),
                                            k4.get((2, "collinear4"), -1)),
      set(k for k, _ in kA) == {1, 2}
      and all(t == "collinear3" for (k, t) in kA if k == 1)
      and all(t == "mixed3" for (k, t) in kA if k == 2)
      and set(k for k, _ in k4) == {2})


# --- covariance (b7_census.py:333-372) ----------------------------------------
def _rots():
    out = []
    for perm in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        for signs in product([1, -1], repeat=3):
            R = [[F(0)] * 3 for _ in range(3)]
            for i in range(3):
                R[i][perm[i]] = F(signs[i])
            det = (R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1])
                   - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
                   + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0]))
            if det == 1:
                out.append(R)
    return out


ROTS = _rots()


def matvec(R, v):
    return tuple(sum(R[i][j] * v[j] for j in range(3)) for i in range(3))


def rot_rec(R, rec):
    if rec[0] == "P":
        return ("P", rec[1], matvec(R, rec[2]))
    return rec


D5 = [m1, neg(m1), m2, m3d, ez]
COVLET = [("P", c, d) for c in (F(1), F(1, 2)) for d in D5] + [("I", F(1))]
cov = {}
for name, law in (("L_A", L_A), ("L_4", L_4)):
    nchk = 0
    mism = 0
    for kk in (1, 2, 3):
        for slots in combinations(range(6), kk):
            for recs in product(COVLET, repeat=kk):
                cond = {SLOTS[s]: r for s, r in zip(slots, recs)}
                S = law(list(cond.values()))
                for R in ROTS:
                    condR = {tuple(int(x) for x in matvec(R, tuple(F(a) for a in sl))):
                             rot_rec(R, rc) for sl, rc in cond.items()}
                    nchk += 1
                    if Counter(law(list(condR.values()))) != Counter(rot_rec(R, it) for it in S):
                        mism += 1
    cov[name] = (nchk, mism)
check("C12 [exact] multiplicity-preserving indexed-menu covariance S(g.n) = g.S(n): %d checks, %d mismatches, L_A and L_4"
      % (cov["L_A"][0], cov["L_A"][1]),
      cov["L_A"][1] == 0 and cov["L_4"][1] == 0
      and cov["L_A"][0] == cov["L_4"][0] == 24 * (6 * 11 + 15 * 121 + 20 * 1331))

# --- abundance kept, and the new grid sweeps (b7_census.py:375-455) -----------
STEREO_P = [F(0), F(1), F(-1), F(1, 2), F(2), F(-1, 3), F(3, 2), F(1, 4), F(-2, 3), F(5, 2)]
STEREO_Q = [F(0), F(1), F(-1), F(1, 3), F(2), F(-3, 2), F(1, 5), F(4, 3)]
SAMPLE_DIRS = []
for p in STEREO_P:
    for q in STEREO_Q:
        u = unit_from_stereo(p, q)
        if u not in SAMPLE_DIRS:
            SAMPLE_DIRS.append(u)
check("C13a [exact] %d declared rational unit directions (PR #7926's table)"
      % len(SAMPLE_DIRS), len(SAMPLE_DIRS) == 80 and all(dot(u, u) == 1 for u in SAMPLE_DIRS))

bin_ok = sum(1 for u in SAMPLE_DIRS for law in (L_A, L_4)
             if law([("P", F(1), u)]) == (("P", F(1), u), ("P", F(1), neg(u))))
check("C13b [exact] abundance kept: every binary is the unit-record output tuple, L_A and L_4, "
      "%d/160" % bin_ok, bin_ok == 160)

TPAR = [F(0), F(1), F(-1), F(1, 2), F(-1, 2), F(2), F(-2), F(1, 3), F(3)]


def plane_pts(e, f):
    pts = []
    for t in TPAR:
        d = 1 + t * t
        co, si = (1 - t * t) / d, 2 * t / d
        pts.append(add(smul(co, e), smul(si, f)))
    pts += [neg(p) for p in pts]
    return pts


E1 = (F(1), F(0), F(0))
E2 = (F(0), F(1), F(0))
E3 = (F(0), F(0), F(1))
ternaries = []
for e, f in ((E1, E2), ((F(3, 5), F(0), F(4, 5)), E2), (E2, E3)):
    pts = plane_pts(e, f)
    for i, j, k in combinations(range(len(pts)), 3):
        n1, n2, n3 = pts[i], pts[j], pts[k]
        if len({n1, n2, n3}) < 3:
            continue
        c = ternary_weights(n1, n2, n3)
        if c is not None:
            ternaries.append(((c[0], n1), (c[1], n2), (c[2], n3)))
ter_ok = 0
ter_scaled_ok = 0
for mn in ternaries:
    cond = [("P", F(1), n) for _, n in mn]
    cond_scaled = [("P", F(1, 3), n) for _, n in mn]
    target = set(("P", c, n) for c, n in mn)
    for law in (L_A, L_4):
        ter_ok += set(law(cond)) == target
        ter_scaled_ok += set(law(cond_scaled)) == target
check("C13c [exact] abundance kept: %d balanced ternaries, %d/%d at unit and %d/%d at 1/3 "
      "scales" % (len(ternaries), ter_ok, 2 * len(ternaries),
                                      ter_scaled_ok, 2 * len(ternaries)),
      len(ternaries) == 378 and ter_ok == 756 and ter_scaled_ok == 756)

coin_vals = set()
coin_ok = True
for u in SAMPLE_DIRS[:20]:
    for v in SAMPLE_DIRS[:20]:
        a = (1 + dot(u, v)) / 2
        if 0 < a < 1:
            coin_vals.add(min(a, 1 - a))
            for law in (L_A, L_4):
                coin_ok &= set(law([("P", F(1), u), ("P", F(1, 2), v)])) == {("I", a), ("I", 1 - a)}
check("C13d [exact] abundance kept: coin branch unchanged and scale-blind, %d distinct "
      "exact a" % len(coin_vals), coin_ok and len(coin_vals) == 77)

GRID = [F(j, 24) for j in range(1, 24)]
col_ok = sum(1 for a in GRID for u in SAMPLE_DIRS
             if L_A([("P", a, u)]) == (("P", a, u), ("P", 1 - a, u), ("P", F(1), neg(u))))
check("C13e [exact] col3 sweeps the grid: %d/1840 over 23 scales j/24 x 80 directions"
      % col_ok, col_ok == 1840)
mix_ok = 0
mix_vals = set()
for c1 in GRID:
    for c2 in GRID:
        c = (c1 + c2) / 2
        mix_vals.add(c)
        u = SAMPLE_DIRS[(24 * int(c1 * 24) + int(c2 * 24)) % 80]
        if L_A([("P", c1, u), ("P", c2, neg(u))]) == (("P", c, u), ("P", c, neg(u)), ("I", 1 - c)):
            mix_ok += 1
check("C13f [exact] mix3 at c = (c1+c2)/2: %d/529 grid pairs, %d distinct c"
      % (mix_ok, len(mix_vals)), mix_ok == 529 and len(mix_vals) == 45)
four_ok = 0
four_n = 0
for a in GRID:
    for b in GRID:
        if a + b < 1:
            four_n += 1
            u = SAMPLE_DIRS[(int(a * 24) * 7 + int(b * 24)) % 80]
            if L_4([("P", a, u), ("P", b, u)]) == (("P", a, u), ("P", b, u),
                                                   ("P", 1 - a - b, u), ("P", F(1), neg(u))):
                four_ok += 1
check("C13g [exact] col4 under L_4: %d/%d grid pairs with a+b<1" % (four_ok, four_n),
      four_ok == four_n and four_n == 253)


# --- the lattice-dipole fibres (b7_census.py:458-500) -------------------------
def lam(slots):
    v = (0, 0, 0)
    for d in slots:
        v = tuple(a + b for a, b in zip(v, d))
    return v


KP_OF = {"binary": 1, "collinear3": 1, "coin": 2, "mixed3": 2, "collinear4": 2, "balanced3": 3}
fib_pad = {t: set() for t in KP_OF}
fib_nopad = {t: set() for t in KP_OF}
for r in range(7):
    for sub in combinations(SLOTS, r):
        d = lam(sub)
        for t, kp in KP_OF.items():
            if r == kp:
                fib_nopad[t].add(d)
            if r >= kp:
                fib_pad[t].add(d)
EX = (1, 0, 0)
ZERO = (0, 0, 0)
check("C14a [exact] parity: dipole sum = recorded slots mod 2; unpadded e_x reaches only the "
      "odd-arity menus",
      all(sum(d) % 2 == KP_OF[t] % 2 for t in KP_OF for d in fib_nopad[t])
      and all((EX in fib_nopad[t]) == (KP_OF[t] % 2 == 1) for t in KP_OF))
check("C14b [exact] with one I-record pad every menu type reaches fibre e_x and the invariant "
      "fibre 0", all(EX in fib_pad[t] and ZERO in fib_pad[t] for t in KP_OF))
w_ex = {SLOTS[0]: ("P", F(1, 3), m2), SLOTS[2]: ("P", F(1, 2), neg(m2)), SLOTS[3]: ("I", F(1))}
w_ex4 = {SLOTS[0]: ("P", F(1, 3), m2), SLOTS[2]: ("P", F(1, 2), m2), SLOTS[3]: ("I", F(1))}
w_ex1 = {SLOTS[0]: ("P", F(1, 3), m2)}
w_0 = {SLOTS[0]: ("P", F(1, 3), m2), SLOTS[1]: ("I", F(1)), SLOTS[2]: ("I", F(1)),
       SLOTS[3]: ("I", F(1)), SLOTS[4]: ("I", F(1)), SLOTS[5]: ("I", F(1))}
check("C14c [exact] witnesses: mix3 and col4 at e_x with an I pad, col3 at e_x unpadded and "
      "at fibre 0",
      lam(w_ex) == EX and menu_type(L_A(list(w_ex.values()))) == "mixed3"
      and lam(w_ex4) == EX and menu_type(L_4(list(w_ex4.values()))) == "collinear4"
      and lam(w_ex1) == EX and menu_type(L_A(list(w_ex1.values()))) == "collinear3"
      and lam(w_0) == ZERO and menu_type(L_A(list(w_0.values()))) == "collinear3")
S_col = L_A([("P", F(1, 4), m2)])
sc = [it for it in S_col if it[0] == "P" and it[2] == m2]
check("C15 [exact] col3 outcomes %s and %s share the direction: the record registers a scale, "
      "and a sampled sign, not a forced sign" % (sc[0][1], sc[1][1]),
      len(sc) == 2 and sc[0][1] == F(1, 4) and sc[1][1] == F(3, 4))


# ============================================================ T2, the rank certificates
# --- exact elimination over Q and Chebyshev (b7_rank.py:44-104) ---------------
def rref_nullspace(rows, ncols):
    """Reduced row echelon form over `Q` with an explicit nullspace basis."""
    piv_rows = []
    piv_cols = []
    for r in rows:
        r = [F(x) for x in r]
        for pr, pc in zip(piv_rows, piv_cols):
            if r[pc] != 0:
                f = r[pc]
                r = [a - f * b for a, b in zip(r, pr)]
        pc = next((j for j in range(ncols) if r[j] != 0), None)
        if pc is None:
            continue
        f = r[pc]
        r = [a / f for a in r]
        for i in range(len(piv_rows)):
            if piv_rows[i][pc] != 0:
                g = piv_rows[i][pc]
                piv_rows[i] = [a - g * b for a, b in zip(piv_rows[i], r)]
        piv_rows.append(r)
        piv_cols.append(pc)
        if len(piv_rows) == ncols:
            break
    rank = len(piv_rows)
    free = [j for j in range(ncols) if j not in piv_cols]
    basis = []
    for fcol in free:
        v = [F(0)] * ncols
        v[fcol] = F(1)
        for pr, pc in zip(piv_rows, piv_cols):
            v[pc] = -pr[fcol]
        basis.append(v)
    return rank, basis


def in_span(vec, basis, n):
    rk0, _ = rref_nullspace([list(b) for b in basis], n)
    rk1, _ = rref_nullspace([list(b) for b in basis] + [list(vec)], n)
    return rk0 == rk1


def cheb_T(k, x):
    a, b = F(1), x
    if k == 0:
        return a
    for _ in range(k - 1):
        a, b = b, 2 * x * b - a
    return b


def cheb_U(k, x):
    a, b = F(1), 2 * x
    if k == 0:
        return a
    for _ in range(k - 1):
        a, b = b, 2 * x * b - a
    return b


# --- the angle-mode rows and the four families (b7_rank.py:107-232) -----------
NG = 24
RGRID = [F(j, NG) for j in range(1, NG + 1)]
IDX = {c: i for i, c in enumerate(RGRID)}
ONE = IDX[F(1)]
INTERIOR = [c for c in RGRID if c < 1]

TRI = []
for s1, s2 in combinations_with_replacement(INTERIOR, 2):
    s3 = 2 - s1 - s2
    if s3 in IDX and 0 < s3 < 1 and s3 >= s2:
        TRI.append((s1, s2, s3))
check("R0 [exact] %d perimeter-2 triangles on the grid j/24 (PR #7950's 44 plus %d isosceles)"
      % (len(TRI), len(TRI) - 44), len(TRI) == 48)


def mode_rows(k, fam):
    """Rows of the mode-k system: unknowns h_k(c) on the grid, plus utilde(c) at k = 0."""
    n = 2 * NG if k == 0 else NG
    rows = []
    sgn = F(1) if k % 2 == 0 else F(-1)

    def new():
        return [F(0)] * n

    for s1, s2, s3 in TRI:
        if k == 0:
            r = new()
            r[IDX[s1]] += 1
            r[IDX[s2]] += 1
            r[IDX[s3]] += 1
            rows.append(r)
        else:
            cA3 = (s1 * s1 + s2 * s2 - s3 * s3) / (2 * s1 * s2)
            cA2 = (s1 * s1 + s3 * s3 - s2 * s2) / (2 * s1 * s3)
            sA3, sA2 = 2 / (s1 * s2), 2 / (s1 * s3)
            re = new()
            im = new()
            re[IDX[s1]] += 1
            re[IDX[s2]] += sgn * cheb_T(k, cA3)
            re[IDX[s3]] += sgn * cheb_T(k, cA2)
            im[IDX[s2]] += -sA3 * cheb_U(k - 1, cA3)
            im[IDX[s3]] += sA2 * cheb_U(k - 1, cA2)
            rows.append(re)
            rows.append(im)
    if "binary" in fam and k % 2 == 0:
        r = new()
        r[ONE] += 2
        rows.append(r)
    if "coin" in fam and k == 0:
        for a in INTERIOR:
            if (1 - a) in IDX:
                r = new()
                r[NG + IDX[a]] += 1
                r[NG + IDX[1 - a]] += 1
                rows.append(r)
        r = new()
        r[NG + ONE] += 1
        rows.append(r)
    if "collinear" in fam:
        for a in INTERIOR:
            if (1 - a) in IDX:
                r = new()
                r[IDX[a]] += 1
                r[IDX[1 - a]] += 1
                r[ONE] += sgn
                rows.append(r)
    if "mixed" in fam and k % 2 == 0:
        for c in INTERIOR:
            r = new()
            r[IDX[c]] += 2
            if k == 0:
                r[NG + IDX[1 - c]] += 1
            rows.append(r)
    if "four" in fam:
        for a, b in combinations_with_replacement(INTERIOR, 2):
            c3 = 1 - a - b
            if c3 in IDX and 0 < c3 < 1:
                r = new()
                r[IDX[a]] += 1
                r[IDX[b]] += 1
                r[IDX[c3]] += 1
                r[ONE] += sgn
                rows.append(r)
    if "terncoin" in fam and k == 0:
        for a, b in combinations_with_replacement(INTERIOR, 2):
            c3 = 1 - a - b
            if c3 in IDX and 0 < c3 < 1:
                r = new()
                r[NG + IDX[a]] += 1
                r[NG + IDX[b]] += 1
                r[NG + IDX[c3]] += 1
                rows.append(r)
    return rows, n


FAMS = {
    "F_CONT": {"binary", "coin"},
    "F_A": {"binary", "coin", "collinear", "mixed"},
    "F_4": {"binary", "coin", "collinear", "mixed", "four"},
    "M_all": {"binary", "coin", "collinear", "mixed", "terncoin"},
}
BORN1 = [c for c in RGRID]
ROGUE0 = [(c - F(2, 3)) if c < 1 else F(0) for c in RGRID]
KMAX = 12
null = {}
kern = {}
for fam in FAMS:
    for k in range(KMAX + 1):
        rows, n = mode_rows(k, FAMS[fam])
        rk, ker = rref_nullspace(rows, n)
        null[(fam, k)] = len(ker)
        kern[(fam, k)] = ker
print("     mode nullity k=0..12: F_CONT %s | F_A = F_4 = M_all %s"
      % (" ".join(str(null[("F_CONT", k)]) for k in range(KMAX + 1)),
         " ".join(str(null[("F_A", k)]) for k in range(KMAX + 1))))

ctrl = []
for k in (0, 1, 3, 5, 7):
    rows, n = mode_rows(k, set())
    rows = [r[:NG] for r in rows]
    rk, ker = rref_nullspace(rows, NG)
    ctrl.append(len(ker))
check("R1 [exact] control, triangle rows alone: nullities %s at k = 0, 1, 3, 5, 7" % ctrl, ctrl == [3, 3, 2, 2, 2])
rog = [F(0)] * (2 * NG)
for i in range(NG):
    rog[i] = ROGUE0[i]
check("R2 [exact] F_CONT k=0 nullity %d holds the counting rogue c - 2/3; 11 are free coin "
      "values" % null[("F_CONT", 0)],
      in_span(rog, kern[("F_CONT", 0)], 2 * NG) and null[("F_CONT", 0)] == 13
      and [null[("F_CONT", k)] for k in range(1, 6)] == [3, 1, 2, 1, 2])
check("R3 [exact] F_A: nullity 0 at every mode k <= 12 but k = 1, kernel exactly the Born "
      "vector h_1(c) = c",
      all(null[("F_A", k)] == 0 for k in range(KMAX + 1) if k != 1)
      and null[("F_A", 1)] == 1 and in_span(BORN1, kern[("F_A", 1)], NG))
check("R4 [exact] F_4: the same, nullity 0 at every mode but the Born vector at k = 1",
      all(null[("F_4", k)] == 0 for k in range(KMAX + 1) if k != 1)
      and null[("F_4", 1)] == 1 and in_span(BORN1, kern[("F_4", 1)], NG))
check("R5 [exact] M_all agrees with F_A mode by mode: the ternary coin adds nothing",
      all(null[("M_all", k)] == null[("F_A", k)] for k in range(KMAX + 1)))
check("R6 [exact] the rogue is outside F_A's k=0 kernel; radius 1/24 is covered by the "
      "collinear row",
      not in_span(rog, kern[("F_A", 0)], 2 * NG) and null[("F_A", 0)] == 0)

# --- the per-point ray certificate (b7_rank.py:296-330) -----------------------
rows = []
for a in INTERIOR:
    if (1 - a) in IDX:
        r = [F(0)] * NG
        r[IDX[a]] += 1
        r[IDX[1 - a]] += 1
        r[ONE] -= 1
        rows.append(r)
ncol = len(rows)
for a, b in combinations_with_replacement(INTERIOR, 2):
    c3 = 1 - a - b
    if c3 in IDX and 0 < c3 < 1:
        r = [F(0)] * NG
        r[IDX[a]] += 1
        r[IDX[b]] += 1
        r[IDX[c3]] += 1
        r[ONE] -= 1
        rows.append(r)
rk, ker = rref_nullspace(rows, NG)
hom = len(ker) == 1 and all(ker[0][i] * RGRID[ONE] == ker[0][ONE] * RGRID[i] for i in range(NG))
check("R9 [exact] F_4 on one ray, no ansatz: %d + %d rows, 24 unknowns, rank %d, nullity %d, "
      "kernel W(c) = cW(1)"
      % (ncol, len(rows) - ncol, rk, len(ker)),
      hom and rk == NG - 1 and ncol == 23 and len(rows) - ncol == 132)
rk_c, ker_c = rref_nullspace(rows[:ncol], NG)
check("R10 [exact] the collinear rows alone leave nullity %d: F_A's ray content fixes no "
      "scale law" % len(ker_c), len(ker_c) == 12)


# --- PR #7950's 52-direction stage (b7_rank.py:333-378) -----------------------
def pyth_pairs(maxmn):
    pts = set()
    for mm in range(1, maxmn + 1):
        for nn in range(0, mm):
            d = mm * mm + nn * nn
            c, s = F(mm * mm - nn * nn, d), F(2 * mm * nn, d)
            for (a, b) in [(c, s), (s, c)]:
                for sa in (1, -1):
                    for sb in (1, -1):
                        pts.add((sa * a, sb * b))
    return sorted(pts)


def cross2(u, v):
    return u[0] * v[1] - u[1] * v[0]


def balanced_weights2(n1, n2, n3):
    p = [cross2(n2, n3), cross2(n3, n1), cross2(n1, n2)]
    if all(x > 0 for x in p) or all(x < 0 for x in p):
        s = sum(p)
        return [x / s for x in p]
    return None


PTS5 = pyth_pairs(5)
trips = []
for n1, n2, n3 in combinations(PTS5, 3):
    p = balanced_weights2(n1, n2, n3)
    if p is not None:
        trips.append(((n1, n2, n3), p))
pidx = {p: i for i, p in enumerate(PTS5)}
rows = []
for ns, p in trips:
    r = [F(0)] * len(PTS5)
    for ni, x in zip(ns, p):
        r[pidx[ni]] += 2 * x
    rows.append(r)
rk, ker = rref_nullspace(rows, len(PTS5))
xs = [n[0] for n in PTS5]
ys = [n[1] for n in PTS5]
check("R12 [exact] 52 directions, %d balanced ternaries, rank %d, nullity %d, kernel "
      "span{x, y}" % (len(trips), rk, len(ker)),
      len(PTS5) == 52 and len(trips) == 5200 and rk == 50 and len(ker) == 2
      and in_span(xs, ker, 52) and in_span(ys, ker, 52))


# ================================================================== T3, the fair coin
# --- the invariant fibre (b7_sign.py:103-160) ---------------------------------
def born(r, it):
    """tr(rho E) with rho = (I + r.sigma)/2."""
    if it[0] == "I":
        return it[1]
    return it[1] * (1 + dot(r, it[2])) / 2


def rank_exact(rws):
    M = [list(r) for r in rws]
    rk = 0
    for c in range(len(M[0])):
        p = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        pv = M[rk][c]
        M[rk] = [x / pv for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk


rows = []
for R in ROTS:
    for i in range(3):
        rows.append([R[i][j] - (F(1) if i == j else F(0)) for j in range(3)])
rk = rank_exact(rows)
check("S1 [exact] every fully recorded condition has dipole %s; stacked R - 1 has rank %d, so "
      "the bulk fibre is rho = I/2" % (lam(SLOTS), rk), lam(SLOTS) == (0, 0, 0) and rk == 3 and len(ROTS) == 24)

# --- bulk odds of each new menu (b7_sign.py:163-205) --------------------------
mB = m2
R0 = (F(0), F(0), F(0))
fair = True
for c in (F(1, 4), F(1, 2), F(3, 4)):
    S = L_A([("P", c, mB)] + [("I", F(1))] * 5)
    odds = [born(R0, it) for it in S]
    plus = sum(o for o, it in zip(odds, S) if it[0] == "P" and it[2] == mB)
    minus = sum(o for o, it in zip(odds, S) if it[0] == "P" and it[2] == neg(mB))
    fair &= plus == F(1, 2) and minus == F(1, 2) and odds == [c / 2, (1 - c) / 2, F(1, 2)]
check("S2a [exact] L_A bulk {cP(m), five I}: col3 odds (c/2, (1-c)/2, 1/2); +m total 1/2, "
      "-m 1/2", fair)
S = L_A([("P", F(1, 4), mB), ("P", F(3, 4), neg(mB))] + [("I", F(1))] * 4)
check("S2b [exact] L_A bulk {(1/4)P(m), (3/4)P(-m), four I}: mix3 odds %s"
      % [str(born(R0, it)) for it in S],
      [born(R0, it) for it in S] == [F(1, 4), F(1, 4), F(1, 2)])
S = L_4([("P", F(1, 4), mB), ("P", F(1, 2), mB)] + [("I", F(1))] * 4)
odds = [born(R0, it) for it in S]
check("S2c [exact] L_4 bulk {(1/4)P(m), (1/2)P(m), four I}: odds %s, +m total %s"
      % ([str(o) for o in odds], sum(odds[:3])),
      odds == [F(1, 8), F(1, 4), F(1, 8), F(1, 2)] and sum(odds[:3]) == F(1, 2))
S = L_A([("P", F(1), mB)] * 6)
check("S2d [exact] six direction records give {I}: no direction and no sign is registered", S == ONE_I and L_4([("P", F(1), mB)] * 6) == ONE_I)

# --- the sign lemma, every state (b7_sign.py:208-232) -------------------------
GRIDC = [F(j, 8) for j in range(1, 8)]
STATES = [R0, (F(2, 3), F(0), F(0)), (F(0), F(0), F(2, 3)), (F(1, 3), F(1, 5), F(2, 7)),
          (F(3, 5), F(0), F(4, 5))]
ok = True
for r in STATES:
    pb = born(r, ("P", F(1), mB))
    for c in GRIDC:
        S3 = L_A([("P", c, mB)])
        plus = sum(born(r, it) for it in S3 if it[0] == "P" and it[2] == mB)
        ok &= plus == pb and born(r, ("P", F(1), neg(mB))) == 1 - pb
        for c2 in GRIDC:
            if c + c2 < 1:
                S4 = L_4([("P", c, mB), ("P", c2, mB)])
                ok &= sum(born(r, it) for it in S4 if it[0] == "P" and it[2] == mB) == pb
        S5 = L_A([("P", c, mB), ("P", c, neg(mB))])
        ok &= born(r, S5[0]) + born(r, S5[1]) == c and born(r, S5[0]) / c == pb
check("S3 [exact] 5 states x 7 scales: rank-one refinements have raw +m odds "
      "tr(rho P(m)); mixed menus have those odds only conditional on a directional outcome", ok)

# --- auxiliary independent one-shot readout arithmetic and the tilt bound (b7_sign.py:235-258) ------------------
pw = {N: N * N * math.log10(2) for N in (24, 32, 48)}
check("S4 [supplied independent readout, float log10] (1/2)^(N^2) = 10^-%.1f, 10^-%.1f, 10^-%.1f "
      "at N = 24, 32, 48"
      % (pw[24], pw[32], pw[48]),
      abs(pw[24] - 173.4) < 0.1 and abs(pw[32] - 308.3) < 0.1 and abs(pw[48] - 693.6) < 0.1)
okt = True
for t in (F(0), F(2, 3), F(9, 10), F(99, 100)):
    r = (t * mB[0], t * mB[1], t * mB[2])
    wp = born(r, ("P", F(1), mB))
    wm = born(r, ("P", F(1), neg(mB)))
    okt &= wp == (1 + t) / 2 and wm == (1 - t) / 2 and wm > 0
check("S5 [exact] tilt t: sign odds (1+t)/2, antipode (1-t)/2 > 0 at t = 0, 2/3, 9/10, 99/100, "
      "so t < 1", okt)
pt = {N: -N * N * math.log10(F(5) / 6) for N in (24, 32, 48)}
check("S5a [supplied independent readout, float log10] at t = 2/3 the all-plus event has probability (5/6)^N^2 = 10^-%.1f, 10^-%.1f, "
      "10^-%.1f" % (pt[24], pt[32], pt[48]),
      abs(pt[24] - 45.6) < 0.1 and abs(pt[32] - 81.1) < 0.1 and abs(pt[48] - 182.4) < 0.1)


# --- float64 fixed open-plane model; provenance specialization explained above.
# No random-field sampling, sequential formation, or thermodynamic extrapolation.
import numpy as np                                                       # noqa: E402
import scipy.sparse as sp                                                # noqa: E402

I2 = np.eye(2)
Xp = np.array([[0, 1], [1, 0]], complex)
Yp = np.array([[0, -1j], [1j, 0]])
Zp = np.diag([1.0, -1.0]).astype(complex)
PAULI = {"I": I2, "X": Xp, "Y": Yp, "Z": Zp}


def P3(s):
    return np.kron(np.kron(PAULI[s[0]], PAULI[s[1]]), PAULI[s[2]])


M2S = P3("XYX")
M0 = 0.7
WGAP = 0.98 * M0


class Plane:
    """Transverse (x, y) plane of coarse sites with the z cell bit b."""

    def __init__(self, Nx, Ny, periodic=False):
        assert Nx % 2 == 0 and Ny % 2 == 0
        self.Nx, self.Ny, self.periodic = Nx, Ny, periodic
        self.D = 2 * Nx * Ny
        xs, ys, bs = np.meshgrid(np.arange(Nx), np.arange(Ny), np.arange(2), indexing="ij")
        self.x = xs.ravel()
        self.y = ys.ravel()
        self.b = bs.ravel()
        self.cells = [(X, Y) for X in range(Nx // 2) for Y in range(Ny // 2)]

    def idx(self, x, y, b):
        return (x * self.Ny + y) * 2 + b

    def cell_sites(self, X, Y):
        return [self.idx(2 * X + b1, 2 * Y + b2, b3)
                for b1 in range(2) for b2 in range(2) for b3 in range(2)]

    def hop_matrices(self):
        Nx, Ny, idx = self.Nx, self.Ny, self.idx
        rows, cols, vals = [], [], []
        zr, zc, zv = [], [], []
        for x in range(Nx):
            for y in range(Ny):
                for b in range(2):
                    i = idx(x, y, b)
                    if x + 1 < Nx or self.periodic:
                        j = idx((x + 1) % Nx, y, b)
                        rows += [j, i]
                        cols += [i, j]
                        vals += [1.0, 1.0]
                    if y + 1 < Ny or self.periodic:
                        amp = (-1.0) ** x
                        j = idx(x, (y + 1) % Ny, b)
                        rows += [j, i]
                        cols += [i, j]
                        vals += [amp, amp]
                eta3 = (-1.0) ** (x + y)
                i0, i1 = idx(x, y, 0), idx(x, y, 1)
                rows += [i1, i0]
                cols += [i0, i1]
                vals += [eta3, eta3]
                zr += [i0]
                zc += [i1]
                zv += [eta3]
        H0 = sp.csr_matrix((vals, (rows, cols)), shape=(self.D, self.D), dtype=complex)
        Zi = sp.csr_matrix((zv, (zr, zc)), shape=(self.D, self.D), dtype=complex)
        return H0, Zi

    def m2_hop_operator(self, m2_site):
        """The body-diagonal hop M2, each amplitude the mean of the two endpoint records."""
        rows, cols, vals = [], [], []
        nz = np.argwhere(np.abs(M2S) > 0)
        for (X, Y) in self.cells:
            s = self.cell_sites(X, Y)
            for i, j in nz:
                rows.append(s[i])
                cols.append(s[j])
                vals.append(0.5 * (m2_site[s[i]] + m2_site[s[j]]) * M2S[i, j])
        return sp.csr_matrix((vals, (rows, cols)), shape=(self.D, self.D), dtype=complex)

    def neighbours_inplane(self, i):
        x, y, b = self.x[i], self.y[i], self.b[i]
        out = []
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if self.periodic:
                xx %= self.Nx
                yy %= self.Ny
            elif not (0 <= xx < self.Nx and 0 <= yy < self.Ny):
                continue
            out.append(self.idx(xx, yy, b))
        return out


def build_H(pl, rvec, M0, H0, Zi, e1=(1, 0, 0), e2=(0, 1, 0)):
    """The dressed one-particle Hamiltonian read from the record Bloch vectors."""
    e1 = np.asarray(e1, float)
    e2 = np.asarray(e2, float)
    m1v = M0 * (rvec @ e1)
    m2v = M0 * (rvec @ e2)
    eps = (-1.0) ** (pl.x + pl.y + pl.b)
    Hstat = (H0 + sp.diags(eps * m1v) + pl.m2_hop_operator(m2v)).tocsr()

    def H(q):
        return (Hstat + Zi * np.exp(-1j * q) + Zi.conj().T * np.exp(1j * q)).tocsr()

    def V(q):
        return (-1j * Zi * np.exp(-1j * q) + 1j * Zi.conj().T * np.exp(1j * q)).tocsr()

    return H, V


def ingap_modes(Hq, window):
    """Complete finite window, not a nearest-zero subset.

    Residuals and orthogonality certify the computed full numerical basis to the
    stated tolerances. Individual core weights in degenerate eigenspaces remain
    basis dependent; this is not a basis-independent localization theorem.
    """
    A = Hq.toarray()
    herm_error = float(np.max(np.abs(A - A.conj().T)))
    E, U = np.linalg.eigh(A)
    residual = float(np.max(np.abs(A @ U - U * E)))
    orth_error = float(np.max(np.abs(U.conj().T @ U - np.eye(A.shape[0]))))
    sel = np.abs(E) < window
    certificate = {"dimension": int(A.shape[0]), "eigenpairs": len(E),
                   "window": float(window), "window_count": int(sel.sum()),
                   "hermiticity_max_abs": herm_error,
                   "residual_max_abs": residual, "orthogonality_max_abs": orth_error}
    return E[sel], U[:, sel], certificate


def relax_xy_fast(pl, n0, pinned, zterm=2.0, tol=1e-14, maxit=200000):
    n = n0.copy()
    nbl = np.array([pl.neighbours_inplane(i) + [i] * (4 - len(pl.neighbours_inplane(i)))
                    for i in range(pl.D)])
    cnt = np.array([len(pl.neighbours_inplane(i)) for i in range(pl.D)])
    pad = 4 - cnt
    free = ~pinned
    for it in range(maxit):
        s = n[nbl].sum(1) - pad[:, None] * n + zterm * n
        norm = np.linalg.norm(s, axis=1)
        new = n.copy()
        mk = free & (norm > 0)
        new[mk] = s[mk] / norm[mk, None]
        delta = np.max(np.abs(new - n))
        n = new
        if delta < tol:
            return n, it + 1
    return n, maxit


def support_residual(pl, n, zterm=2.0):
    nbl = [pl.neighbours_inplane(i) for i in range(pl.D)]
    res = np.zeros(pl.D)
    dotp = np.zeros(pl.D)
    for i in range(pl.D):
        v = n[nbl[i]].sum(0) + zterm * n[i]
        vn = np.linalg.norm(v)
        if vn > 0:
            res[i] = np.linalg.norm(np.cross(n[i], v)) / vn
            dotp[i] = n[i] @ v / vn
    return res, dotp


def analytic_field(pl, cores):
    r = np.zeros((pl.D, 3))
    for i in range(pl.D):
        ph = 0.0
        for (xc, yc, n) in cores:
            ph += n * np.arctan2(pl.y[i] - yc, pl.x[i] - xc)
        r[i] = [np.cos(ph), np.sin(ph), 0.0]
    return r


def relaxed_field(pl, cores):
    """The L_HYB fixed point on the open plane: XY relaxation from the analytic field with
    the boundary ring and the four plaquette corners about each core pinned."""
    n0 = analytic_field(pl, cores)
    pinned = np.minimum.reduce([pl.x, pl.y, pl.Nx - 1 - pl.x, pl.Ny - 1 - pl.y]) < 0.5
    for (xc, yc, _) in cores:
        pinned |= (np.abs(pl.x - xc) < 0.75) & (np.abs(pl.y - yc) < 0.75)
    n, _ = relax_xy_fast(pl, n0, pinned)
    res, dotp = support_residual(pl, n)
    free = ~pinned
    return n, float(res[free].max()), float(dotp[free].min()), int(free.sum())


Nf = 24
plf = Plane(Nf, Nf)
H0f, Zif = plf.hop_matrices()
cf = ((Nf - 1) / 2, (Nf - 1) / 2)
nf, res, mind, nfree = relaxed_field(plf, [(cf[0], cf[1], 1)])
check("S6a [float64, model] the 24x24 relaxed vortex is an L_HYB fixed point: residual %.1e, "
      "%d sites, min n.vhat %+.4f" % (res, nfree, mind),
      res < 1e-13 and nfree == 960 and mind > 0.999999)
golden = (1 + 5 ** 0.5) / 2
qr = (plf.x * golden + plf.y * 2 ** 0.5) % 1.0
FLIPS = [("none", np.ones(plf.D)),
         ("1/9", np.where((plf.x % 3 == 0) & (plf.y % 3 == 0), -1.0, 1.0)),
         ("1/2", np.where(qr < 0.5, -1.0, 1.0)),
         ("1/6", np.where(qr < 1 / 6, -1.0, 1.0))]
flipres = {}
for nm, s in FLIPS:
    Hf, Vf = build_H(plf, nf * s[:, None], M0, H0f, Zif)
    Ef, Uf, cert = ingap_modes(Hf(np.pi + 0.1), WGAP)
    core = np.hypot(plf.x - cf[0], plf.y - cf[1]) < 5
    sel = [j for j in range(len(Ef)) if (np.abs(Uf[:, j]) ** 2)[core].sum() > 0.6]
    flipres[nm] = (float(np.mean(s)), len(sel))
    cert.update(pattern=nm, flip_count=int((s < 0).sum()), core_count=len(sel),
                energies=Ef.tolist(), core_weights=(np.abs(Uf[core, :]) ** 2).sum(axis=0).tolist())
    print("FULL_WINDOW " + json.dumps(cert, sort_keys=True))
    check("S6c_%s [float64] full 1152-state eigensystem and complete fixed window" % nm,
          cert["dimension"] == cert["eigenpairs"] == 1152
          and cert["window_count"] == len(Ef)
          and cert["hermiticity_max_abs"] < 1e-12
          and cert["residual_max_abs"] < 1e-10
          and cert["orthogonality_max_abs"] < 1e-10)
check("S6b [float64, model] flip density 1/2 (mean %+.3f) leaves %d core modes; none, 1/9, "
      "~1/6 keep %d, %d, %d"
      % (flipres["1/2"][0], flipres["1/2"][1], flipres["none"][1], flipres["1/9"][1],
         flipres["1/6"][1]),
      flipres["1/2"][1] == 0 and flipres["none"][1] == 2 and flipres["1/9"][1] == 2
      and flipres["1/6"][1] == 2)


# ======================================================= T4, homogeneity as a clause
# (b7_rank.py:381-430)
TP = [F(0), F(1), F(-1), F(1, 2), F(-1, 2), F(2), F(-2), F(1, 3), F(3)]
cpts = [circle_dir(t) for t in TP]
cpts += [neg(p) for p in cpts]
TERN = []
for i, j, k in combinations(range(len(cpts)), 3):
    n1, n2, n3 = cpts[i], cpts[j], cpts[k]
    if len({n1, n2, n3}) < 3:
        continue
    q = balanced_weights2((n1[0], n1[1]), (n2[0], n2[1]), (n3[0], n3[1]))
    if q is not None:
        TERN.append(((2 * q[0], n1), (2 * q[1], n2), (2 * q[2], n3)))
T_PARAM = F(2, 3)
EXV = (F(1), F(0), F(0))


def w_fib(c, n, l):
    """L_FIB of PR #7926: rho_l = (I + t l.sigma)/2 on a unit lattice dipole l."""
    return c * (1 + T_PARAM * dot(l, n)) / 2


check("R13 [exact] L_CONT + L_FIB satisfies the clause in fibre e_x on all %d ternaries and "
      "their binaries" % len(TERN),
      len(TERN) == 126
      and all(w_fib(c, n, EXV) / c == w_fib(F(1), n, EXV) for mn in TERN for c, n in mn)
      and all(sum(w_fib(c, n, EXV) for c, n in mn) == 1 for mn in TERN))


def rogue(c):
    return F(1, 2) if c == 1 else F(1, 3)


check("R14 [exact] the counting rogue violates it, %s against %s, while normalised on all %d "
      "ternaries"
      % (rogue(F(1, 2)) / F(1, 2), rogue(F(1)), len(TERN)),
      rogue(F(1, 2)) / F(1, 2) != rogue(F(1))
      and all(sum(rogue(c) for c, _ in mn) == 1 for mn in TERN))


def w_cubic(c, n):
    return c * (1 + n[2] ** 3) / 2


u35 = (F(3, 5), F(0), F(4, 5))
check("R15 [exact] L_BIN with c(1 + u_z^3)/2: homogeneous, normalised on every binary, not "
      "Born (%s against 4/5)" % (u35[2] ** 3),
      all(w_cubic(F(1), n) + w_cubic(F(1), neg(n)) == 1 for n in cpts + [u35])
      and all(w_cubic(c, n) / c == w_cubic(F(1), n)
              for c in (F(1, 2), F(1, 3), F(1, 7)) for n in cpts + [u35])
      and u35[2] ** 3 != u35[2])
check("R17 [exact] finite certificates only: F_CONT rogue, F_A mode kernels, F_4 ray rank; "
      "continuum conclusions require the separate stated proof and hypotheses",
      null[("F_CONT", 0)] == 13 and in_span(rog, kern[("F_CONT", 0)], 2 * NG)
      and null[("F_A", 1)] == 1 and all(null[("F_A", k)] == 0
                                        for k in range(KMAX + 1) if k != 1)
      and hom and rk_c == NG - 12)

# --- correction controls: actual indexed laws and raw/joint semantics --------
def content_pushforward(menu, r):
    """Sum indexed Born weights at equal unindexed matrix contents."""
    weights = {}
    for effect in menu:
        weights[effect] = weights.get(effect, F(0)) + born(r, effect)
    return weights


DUPLICATE_CASES = [
    ("L_CONT", L_CONT([("P", F(1), EXV), ("P", F(1), (F(0), F(1), F(0)))]), F(1, 2)),
    ("L_A", L_A([("P", F(1, 2), EXV)]), F(3, 4)),
    ("L_4", L_4([("P", F(1, 4), EXV), ("P", F(1, 2), EXV)]), F(7, 8)),
]
for name, menu, collapsed in DUPLICATE_CASES:
    masses = content_pushforward(menu, R0)
    check("Q1_%s [exact] indexed mass 1; content mass 1 after multiplicity pushforward; "
          "one-grade-per-distinct-effect mass %s" % (name, collapsed),
          sum(born(R0, effect) for effect in menu) == 1
          and sum(masses.values()) == 1
          and sum(born(R0, effect) for effect in set(menu)) == collapsed < 1
          and any(mass != born(R0, effect) for effect, mass in masses.items()))
check("Q2 [exact] actual duplicate menu detects the multiplicity lost by set comparison",
      Counter(DUPLICATE_CASES[0][1]) != Counter(set(DUPLICATE_CASES[0][1]))
      and all(Counter(rot_rec(R, it) for it in DUPLICATE_CASES[0][1])
              != Counter(rot_rec(R, it) for it in set(DUPLICATE_CASES[0][1])) for R in ROTS))


def direction_only_collinear(recs):
    """Counterexample to universal scale-reading necessity, not a selected law.

    With exactly three directional records, a unique repeated direction m and a
    distinct spectator n supply a=(1+m.n)/2. Multiplicities, not record scales,
    choose the branch. Other conditions retain L_CONT exactly.
    """
    directions = dirs_of(recs)
    counts = Counter(directions)
    if len(directions) == 3 and sorted(counts.values()) == [1, 2]:
        m = next(n for n, count in counts.items() if count == 2)
        n = next(n for n, count in counts.items() if count == 1)
        a = (1 + dot(m, n)) / 2
        if 0 < a < 1:
            return (("P", a, m), ("P", 1 - a, m), ("P", F(1), neg(m)))
    return L_CONT(recs)


DIR_WITNESS = [("P", F(1, 4), EXV), ("P", F(2, 3), EXV), ("P", F(1, 5), m2)]
DIR_EXPECTED = (("P", F(1, 5), EXV), ("P", F(4, 5), EXV), ("P", F(1), neg(EXV)))
dir_ok = Counter(direction_only_collinear(DIR_WITNESS)) == Counter(DIR_EXPECTED)
for order in permutations(DIR_WITNESS):
    for R in ROTS:
        actual = direction_only_collinear([rot_rec(R, rec) for rec in order])
        unit_scales = direction_only_collinear([("P", F(1), rot_rec(R, rec)[2]) for rec in order])
        dir_ok &= (Counter(actual) == Counter(rot_rec(R, it) for it in DIR_EXPECTED)
                   == Counter(unit_scales) and resolves(actual))
check("Q3 [exact] scale-blind collinear competitor: a=1/5, all 6 orders x 24 rotations; "
      "not a classification or physical selection", dir_ok)

mixed = L_A([("P", F(1, 2), EXV), ("P", F(1, 2), neg(EXV))])
raw = [born(R0, effect) for effect in mixed]
check("Q4 [exact] actual mixed menu raw odds 1/4,1/4,1/2; conditional + is 1/2",
      raw == [F(1, 4), F(1, 4), F(1, 2)]
      and raw[0] / (raw[0] + raw[1]) == F(1, 2)
      and raw[0] != born(R0, ("P", F(1), EXV)))

PARITY_STATES = [bits for bits in product((0, 1), repeat=8) if sum(bits) % 2 == 0]
local_fair = True
for target in range(8):
    others = [i for i in range(8) if i != target]
    for observed in combinations(others, 6):
        for values in product((0, 1), repeat=6):
            compatible = [bits for bits in PARITY_STATES
                          if all(bits[i] == val for i, val in zip(observed, values))]
            local_fair &= (len(compatible) == 2
                           and sum(bits[target] for bits in compatible) == 1)
check("Q5 [exact] every bit conditional on any six is fair, but even-parity all-zero "
      "mass 1/128 differs from independent 1/256", local_fair
      and len(PARITY_STATES) == 128 and (0,) * 8 in PARITY_STATES
      and F(1, len(PARITY_STATES)) == F(1, 128) != F(1, 2) ** 8)

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(int(FAIL != 0))
