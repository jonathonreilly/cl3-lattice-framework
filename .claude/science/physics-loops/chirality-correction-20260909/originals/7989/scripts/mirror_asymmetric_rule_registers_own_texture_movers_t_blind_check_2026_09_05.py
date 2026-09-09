#!/usr/bin/env python3
"""A mirror-asymmetric admissibility rule registers its own parity-odd texture and nothing else;
the emergent fermion's movers are time-reversal images with identical record laws.

Self-contained class-A runner: no seed, no random number, no external input file, no import of any
repository module.  Every enumeration below is complete or a declared sub-family, and every
eigenproblem is a deterministic LAPACK call.

Copied source blocks (the probe scripts of 2026-09-05; each copy names the block it reproduces):
  signed_perms / offperm / act / flip / orbits / joint_orbits / count_assignments
                                     <- h4_census.py, "the profile orbits" and "Counting tables"
  burnside_cycles / bulk_rate        <- h4_census_burnside.py
  templates / pat_sym / tval / trole / realised_roles / map_profile / the 5x5x5 entry set
                                     <- h4_designed_law.py D1-D3
  M2_matrix / cycles4 / loop_products / the T_h census
                                     <- h4_designed_law.py D5 and diag_m2b.py
  cluster / sea / all_patterns / det_law / tv / cluster_syms / permute / gauge_between /
  chiral_capable / profile / tilt_factor / chiral_subsets / superset_sums / podd_fast /
  edge_mask / h_free / star_G / rotated_kernel               <- h4_common.py
  current / mover / mirror_perm / region_sym_pairs / fast_weights / finished_battery
                                     <- h4_registration.py
  tick_tilt (vectorised here) / tick_family        <- h4_common.py and h4_registration_tickfamily.py
  string_build / sector_basis / plane_syms / current_z       <- h4_string.py
  wall_H / M2_op / weights_signed / wall_battery             <- h4_wall.py

Groups: A the chirality census; B the designed law; C the sea's record statistics;
        D registration handedness; E the mirror wall.

Declared reductions (everything else is recomputed from scratch):
  * The 12x12x24 string is solved in its 12 cell-momentum sectors (288 x 288 each) rather than by one
    dense 3456 x 3456 eigh; the sector decomposition is certified by [H, T^2] = 0 and by orthonormality.
    Its P-odd occupation-minor density map over the whole plane is not recomputed (quoted:
    h4_string.py -> out_string.txt:13, ST3.2d, whole-plane sum -2.4e-17, max |rho| 3.96e-4), and the
    2x2x5 core column is quoted (out_string.txt:39-44, ST4.col5); columns L = 2, 3, 4 are recomputed.
  * The slab's tick reading recomputes the identity and even-first 16-image families; the deg4-first
    and rshift3 families are quoted (out_tickfamily.txt:17-32).
  * The 6^3 torus recomputes the 2x2x2, 2x2x3 and 2x2x4 regions; 2x2x5 and the 3x3xL rods are quoted
    (out_registration.txt:102-110 and out_registration_rod.txt:2-20).
  * The wall spectrum is scanned at the declared points (dq_y, dq_z) = (0, 0) and dq_y in
    {0.1, 0.2, 0.3, 0.4} at dq_z = 0, rather than over the full 13 x 13 grid.

Output: one PASS/FAIL line per check, and a final `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import math
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp

AUDIT_TIMEOUT_SEC = 200

T0 = time.time()
PASS = 0
FAIL = 0


def check(msg, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("%s %s" % ("PASS" if ok else "FAIL", msg))


# =============================================================== point group and profile machinery
OFFS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
OIDX = {d: i for i, d in enumerate(OFFS)}
OPEN = 2


def signed_perms():                                   # h4_census.py / h4_common.py
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            m = np.zeros((3, 3), dtype=int)
            for r in range(3):
                m[r, perm[r]] = signs[r]
            out.append(m)
    return out


G48 = signed_perms()
DET = [int(round(np.linalg.det(g))) for g in G48]
INV = -np.eye(3, dtype=int)


def gapply(m, d):
    return tuple(int(sum(m[r][c] * d[c] for c in range(3))) for r in range(3))


def offperm(m):
    return tuple(OIDX[gapply(m, d)] for d in OFFS)


PERM_O = [offperm(g) for g, d in zip(G48, DET) if d == 1]
PERM_IMP = [offperm(g) for g, d in zip(G48, DET) if d == -1]
PERM_SIGMA = offperm(INV)
PROFILES = list(itertools.product((2, 0, 1), repeat=6))


def act(perm, p):
    q = [None] * 6
    for i in range(6):
        q[perm[i]] = p[i]
    return tuple(q)


def flipp(p):
    return tuple((1 - v) if v in (0, 1) else v for v in p)


def orbits_of(perms):
    seen, orbs = {}, []
    for p in PROFILES:
        if p in seen:
            continue
        orb, stack = set(), [p]
        while stack:
            x = stack.pop()
            if x in orb:
                continue
            orb.add(x)
            for g in perms:
                stack.append(act(g, x))
        for x in orb:
            seen[x] = len(orbs)
        orbs.append(frozenset(orb))
    return orbs, seen


# =============================================================== A -- the chirality census (T1)
ORB_O, OID = orbits_of(PERM_O)
ORB_H, HID = orbits_of(PERM_O + PERM_IMP)
nO, nH = len(ORB_O), len(ORB_H)
sig_of = [OID[act(PERM_SIGMA, next(iter(o)))] for o in ORB_O]
sig_ok = all(all(OID[act(PERM_SIGMA, x)] == sig_of[k] for x in o) for k, o in enumerate(ORB_O))
same_pairing = all(OID[act(gp, next(iter(o)))] == sig_of[k]
                   for gp in PERM_IMP for k, o in enumerate(ORB_O))
achiral = [k for k in range(nO) if sig_of[k] == k]
chiral = [k for k in range(nO) if sig_of[k] != k]
pairs_c = sorted(set(tuple(sorted((k, sig_of[k]))) for k in chiral))


def burnside_cycles(m):                               # h4_census_burnside.py
    img = {d: gapply(m, d) for d in OFFS}
    seen, c = set(), 0
    for d in OFFS:
        if d in seen:
            continue
        c += 1
        x = d
        while x not in seen:
            seen.add(x)
            x = img[x]
    return c


bn = {}
for k in (3, 2):
    bn[k] = (Fraction(sum(k ** burnside_cycles(g) for g, d in zip(G48, DET) if d == 1), 24),
             Fraction(sum(k ** burnside_cycles(g) for g in G48), 48))
check("A1 [exact] 729 ternary profiles: %d proper orbits, %d full, %d achiral + %d chiral pair; "
      "Burnside %s/%s; the inversion's pairing is well defined and all 24 improper elements induce "
      "it: %s"
      % (nO, nH, len(achiral), len(pairs_c), bn[3][0], bn[3][1], sig_ok and same_pairing),
      (nO, nH, len(achiral), len(pairs_c)) == (57, 56, 55, 1) and sig_ok and same_pairing
      and bn[3] == (57, 56))

SYMC = {2: '.', 0: '0', 1: '1'}


def nrec(p):
    return sum(1 for v in p if v in (0, 1))


shape = sorted({(nrec(p), sum(1 for a in range(3) if p[2 * a] in (0, 1) or p[2 * a + 1] in (0, 1)),
                 sum(1 for a in range(3) if p[2 * a] in (0, 1) and p[2 * a + 1] in (0, 1)))
                for k in chiral for p in [next(iter(ORB_O[k]))]})
a0, b0 = pairs_c[0]
exA = min(p for p in ORB_O[a0] if nrec(p) == 4)
exB = act(PERM_SIGMA, exA)
full_orb = [k for k in range(nO) if nrec(next(iter(ORB_O[k]))) == 6]
full_chi = [k for k in full_orb if k in chiral]
check("A2 [exact] the chiral pair %s <-> %s (+x-x+y-y+z-z, '.' = open): shape (records, axes, full "
      "axes) %s, four records and two open ends; of the 64 fully recorded profiles %d orbits, %d "
      "chiral (Burnside %s/%s)"
      % ("".join(SYMC[v] for v in exA), "".join(SYMC[v] for v in exB), shape, len(full_orb),
         len(full_chi), bn[2][0], bn[2][1]),
      shape == [(4, 3, 1)] and exB in ORB_O[b0] and len(full_orb) == 10 and not full_chi
      and bn[2] == (10, 10))

flip_of = [OID[flipp(next(iter(o)))] for o in ORB_O]
flip_pairs = sorted(set(tuple(sorted((k, flip_of[k]))) for k in range(nO) if flip_of[k] != k))
JO, seenj = [], set()
for k in range(nO):                                   # h4_census.py joint_orbits
    if k in seenj:
        continue
    orb, stack = set(), [k]
    while stack:
        x = stack.pop()
        if x in orb:
            continue
        orb.add(x)
        stack += [sig_of[x], flip_of[x]]
    seenj |= orb
    JO.append(sorted(orb))


def count_assignments(orb, need_flip, need_sigma):    # h4_census.py
    cnt = 0
    for menus in itertools.product((0, 1, 2), repeat=len(orb)):
        m = dict(zip(orb, menus))
        ok = True
        for k in orb:
            if need_flip and m[flip_of[k]] != {0: 1, 1: 0, 2: 2}[m[k]]:
                ok = False
                break
            if need_sigma and m[sig_of[k]] != m[k]:
                ok = False
                break
        if ok:
            cnt += 1
    return cnt


def total(need_flip, need_sigma):
    t = 1
    for orb in JO:
        t *= count_assignments(orb, need_flip, need_sigma)
    return t


tot_B, sym_B = total(False, False), total(False, True)
tot_A, sym_A = total(True, False), total(True, True)
digit_kind = {}
for (a, b) in flip_pairs:
    sa, sb = sig_of[a], sig_of[b]
    kind = ('fixed-same' if sa == a else 'fixed-crossed') if {sa, sb} == {a, b} else 'paired'
    digit_kind[kind] = digit_kind.get(kind, 0) + 1
check("A3 [exact] PR #7934's readable class: 3^%d = %d label-equivariant tables, mirror-asymmetric "
      "%d: every table is its own mirror image; all %d digits are 'fixed-same' under the inversion "
      "%s, forcing both chiral orbits to the menu {0,1}; nearest chiral neighbours here: %d"
      % (len(flip_pairs), tot_A, tot_A - sym_A, len(flip_pairs), sorted(digit_kind.items()),
         2 * digit_kind.get('paired', 0)),
      tot_A == 3 ** 24 and sym_A == tot_A and digit_kind == {'fixed-same': 24})
check("A4 [exact] PR #7982's wider class: 3^%d tables, mirror-symmetric 3^%d, asymmetric %d = "
      "exactly two thirds (1 - 3^-%d), in 3^56 chiral pairs {T, T^sigma}; nearest chiral neighbours "
      "of the all-permissive table: %d"
      % (nO, nH, tot_B - sym_B, len(pairs_c), 2 * len(chiral)),
      tot_B == 3 ** 57 and sym_B == 3 ** 56 and tot_B - sym_B == 2 * 3 ** 56
      and Fraction(tot_B - sym_B, tot_B) == Fraction(2, 3) and 2 * len(chiral) == 4)

ORB_OF = {p: k for k, o in enumerate(ORB_O) for p in o}
CHIRAL_A = ORB_OF[(0, 1, 0, OPEN, 1, OPEN)]
CHIRAL_B = sig_of[CHIRAL_A]
assert CHIRAL_B == ORB_OF[(0, 1, 0, OPEN, OPEN, 1)] and CHIRAL_A != CHIRAL_B


def chiral_sign(prof):                                # h4_common.py
    k = ORB_OF[tuple(prof)]
    return 1 if k == CHIRAL_A else (-1 if k == CHIRAL_B else 0)


def chiral_capable(present):                          # h4_common.py
    full = [present[2 * a] and present[2 * a + 1] for a in range(3)]
    single = [present[2 * a] != present[2 * a + 1] for a in range(3)]
    return sum(full) == 1 and sum(single) == 2


def tilt_factor(prof, a, kind, lam=1.0):              # h4_common.py
    if kind == 'none':
        return 1.0
    k = ORB_OF[tuple(prof)]
    if kind[0] == 'tilt':
        s = kind[1] if k == CHIRAL_A else (kind[2] if k == CHIRAL_B else 0)
        return float(np.exp(lam * s * (2 * a - 1)))
    if k == CHIRAL_A:
        return 1.0 if a in kind[1] else 0.0
    if k == CHIRAL_B:
        return 1.0 if a in kind[2] else 0.0
    return 1.0


# =============================================================== B -- the designed law (T2)
C0, C1, EE, FF, QQ = 0, 1, 2, 3, 4


def pat_sym(site, ax):                                # h4_designed_law.py D1
    odd = (site[0] & 1) + (site[1] & 1) + (site[2] & 1)
    return (C0 + ((site[ax] // 2) % 2)) if odd == 0 else (EE if odd == 1 else (FF if odd == 2 else QQ))


def pat_bit(site, ax):
    r = pat_sym(site, ax)
    return None if r == EE else (1 if r in (C1, QQ) else 0)


TPL = []
for ax in (0, 1, 2):
    for shift in itertools.product(range(4), range(2), range(2)):
        o = [0, 0, 0]
        o[ax], o[(ax + 1) % 3], o[(ax + 2) % 3] = shift
        TPL.append((ax, tuple(o)))
DOM = [(x, y, z) for x in range(4) for y in range(4) for z in range(4)]


def tval(t, s):
    ax, o = t
    return pat_bit((s[0] + o[0], s[1] + o[1], s[2] + o[2]), ax)


def trole(t, s):
    ax, o = t
    return pat_sym((s[0] + o[0], s[1] + o[1], s[2] + o[2]), ax)


def ginv(g):
    return [[int(g[c][r]) for c in range(3)] for r in range(3)]


SIG = {tuple(tval(t, s) for s in DOM): k for k, t in enumerate(TPL)}
stab, relabel = [], {}
for gi, g in enumerate(G48):
    gi_inv = ginv(g)
    perm, ok = [], True
    for t in TPL:
        sig = tuple(tval(t, gapply(gi_inv, s)) for s in DOM)
        if sig in SIG:
            perm.append(SIG[sig])
        else:
            ok = False
            break
    if ok:
        stab.append(gi)
        relabel[gi] = tuple(perm)
p_inv = next(relabel[gi] for gi, g in enumerate(G48) if (g == INV).all())
fixed_sec = sum(1 for k in range(48) if p_inv[k] == k)
cyc2 = sum(1 for k in range(48) if p_inv[p_inv[k]] == k and p_inv[k] != k) // 2
check("B1 [exact] the 48 sectors of the superlattice role pattern: stabiliser %d (%d improper); the "
      "inversion relabels them with %d fixed sectors and %d two-cycles, keeping every axis family"
      % (len(stab), sum(1 for gi in stab if DET[gi] == -1), fixed_sec, cyc2),
      len(SIG) == 48 and len(stab) == 48 and fixed_sec == 24 and cyc2 == 12
      and all(TPL[p_inv[k]][0] == TPL[k][0] for k in range(48)))

NN6 = OFFS
WIN12 = NN6 + [(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)]
role_rows = []
for name, win in (("NN", NN6), ("NN+2e", WIN12)):     # h4_designed_law.py D2
    R = set()
    for t in TPL:
        for s in DOM:
            R.add((trole(t, s), tuple(trole(t, (s[0] + o[0], s[1] + o[1], s[2] + o[2])) for o in win)))
    bad = 0
    for g in G48:
        gi_inv = ginv(g)
        img = set((r, tuple(p[win.index(gapply(gi_inv, o))] for o in win)) for (r, p) in R)
        bad += (img != R)
    role_rows.append((name, len(R), bad))
check("B2 [exact] PR #7939's role support rule: %d realised (role, profile) pairs at nearest "
      "neighbour, %d on NN + {+-2 e_d}; elements of O_h failing to preserve them %d and %d"
      % (role_rows[0][1], role_rows[1][1], role_rows[0][2], role_rows[1][2]),
      [r[1:] for r in role_rows] == [(18, 0), (22, 0)])

W125 = [(x, y, z) for x in range(-2, 3) for y in range(-2, 3) for z in range(-2, 3) if (x, y, z) != (0, 0, 0)]
WPOS = {o: i for i, o in enumerate(W125)}
ENT = set()
for t in TPL:                                         # h4_designed_law.py D3
    for s in DOM:
        cv = tval(t, s)
        if cv is not None:
            ENT.add((cv, tuple(tval(t, (s[0] + o[0], s[1] + o[1], s[2] + o[2])) for o in W125)))
badD3 = 0
for g in G48:
    gi_inv = ginv(g)
    if set((cv, tuple(pat[WPOS[gapply(gi_inv, o)]] for o in W125)) for (cv, pat) in ENT) != ENT:
        badD3 += 1
sample = [tuple(((i * 7919 + j * 104729) >> 3) & 1 for j in range(124)) for i in range(50)]
par_ok = all(sum(p) % 2 == sum(p[WPOS[gapply(ginv(g), o)]] for o in W125) % 2
             for p in sample for g in G48)
n_free = sum(1 for s in DOM if tval(TPL[0], s) is None)
check("B3 [exact] the 5x5x5 record table: %d wild-marked exercised entries at pinned centres (%d "
      "free edge centres of 64), elements of O_h not preserving them %d; the parity completion is "
      "permutation-invariant on 50 x 48 declared patterns: %s"
      % (len(ENT), n_free, badD3, par_ok),
      len(ENT) == 30 and badD3 == 0 and par_ok and n_free == 24)


# ---------------------------------------------------------------- clusters (h4_common.py)
def cluster(Lx, Ly, Lz, periodic=(False, False, False), twist=(0, 0, 0)):
    L = (Lx, Ly, Lz)
    idx = {(x, y, z): (x * Ly + y) * Lz + z for x in range(Lx) for y in range(Ly) for z in range(Lz)}
    V = len(idx)
    coords = {v: k for k, v in idx.items()}
    raw = []
    for (x, y, z) in idx:
        for a in range(3):
            q = [x, y, z]
            q[a] += 1
            wrap = False
            if q[a] == L[a]:
                if periodic[a] and L[a] > 2:
                    q[a] = 0
                    wrap = True
                else:
                    continue
            eta = 1 if a == 0 else ((-1) ** x if a == 1 else (-1) ** (x + y))
            if wrap and twist[a]:
                eta = -eta
            i, j = idx[(x, y, z)], idx[tuple(q)]
            raw.append((min(i, j), max(i, j), a, eta))
    raw.sort(key=lambda t: (t[0], t[1]))
    EDGES = [(i, j) for (i, j, a, s) in raw]
    h = np.zeros((V, V))
    for q, (i, j) in enumerate(EDGES):
        h[i, j] = h[j, i] = -float(raw[q][3])
    STAR = {v: [] for v in range(V)}
    for q, (i, j) in enumerate(EDGES):
        STAR[i].append(q)
        STAR[j].append(q)
    NBO = {}
    for (x, y, z), v in idx.items():
        row = []
        for d in OFFS:
            q = [x + d[0], y + d[1], z + d[2]]
            for a in range(3):
                if periodic[a] and L[a] > 2:
                    q[a] %= L[a]
            row.append(idx.get(tuple(q)))
        NBO[v] = row
    sub = np.array([sum(coords[v]) % 2 for v in range(V)])
    return dict(L=L, periodic=periodic, twist=twist, V=V, E=len(EDGES), EDGES=EDGES, h=h, idx=idx,
                coords=coords, STAR=STAR, NBO=NBO, sub=sub, name="%dx%dx%d" % L)


def sea(h, N=None):
    V = h.shape[0]
    N = V // 2 if N is None else N
    w, U = np.linalg.eigh(h)
    W = U[:, :N]
    return W, float(w[N] - w[N - 1]), w, U


def all_patterns(V):
    n = np.arange(1 << V)
    return ((n[:, None] >> np.arange(V)[None, :]) & 1).astype(bool)


def det_law(K, bits=None, chunk=1 << 13):
    V = K.shape[0]
    bits = all_patterns(V) if bits is None else bits
    I = np.eye(V, dtype=K.dtype)
    out = np.zeros(len(bits))
    for s in range(0, len(bits), chunk):
        b = bits[s:s + chunk]
        M = np.where(b[:, :, None], K[None, :, :], (I - K)[None, :, :])
        out[s:s + chunk] = np.linalg.det(M).real
    out[np.abs(out) < 1e-15] = 0.0
    return out


def tv(p, q):
    return 0.5 * float(np.abs(p - q).sum())


def cluster_syms(C, centre=None):
    L = C["L"]
    out = []
    if centre is None:
        centre = tuple(1 if C["periodic"][a] else (L[a] - 1) for a in range(3))
    for g, d in zip(G48, DET):
        perm = np.zeros(C["V"], dtype=int)
        ok = True
        for (x, y, z), v in C["idx"].items():
            c = np.array([2 * x - centre[0], 2 * y - centre[1], 2 * z - centre[2]])
            gc = g @ c
            s = [gc[a] + centre[a] for a in range(3)]
            if any(t % 2 for t in s):
                ok = False
                break
            s = [t // 2 for t in s]
            for a in range(3):
                if C["periodic"][a]:
                    s[a] %= L[a]
                elif not (0 <= s[a] < L[a]):
                    ok = False
            if not ok:
                break
            perm[v] = C["idx"][tuple(s)]
        if ok:
            out.append((g, d, perm))
    return out


def permute(A, perm):
    B = np.zeros_like(A)
    B[np.ix_(perm, perm)] = A
    return B


def gauge_between(H, Hp):
    V = H.shape[0]
    if np.any((np.abs(H) > 1e-12) != (np.abs(Hp) > 1e-12)):
        return np.ones(V, dtype=complex), float("inf")
    D = np.zeros(V, dtype=complex)
    D[0] = 1.0
    stack, seen = [0], {0}
    while stack:
        u = stack.pop()
        for v in np.flatnonzero(np.abs(H[u]) > 1e-12):
            if v not in seen:
                seen.add(v)
                D[v] = np.conj(Hp[u, v] / (D[u] * H[u, v]))
                D[v] /= abs(D[v])
                stack.append(v)
    return D, float(np.max(np.abs(Hp - np.outer(D, np.conj(D)) * H)))


def profile(C, v, n, determined=None):
    out = []
    for u in C["NBO"][v]:
        out.append(OPEN if (u is None or (determined is not None and not determined[u])) else int(n[u]))
    return tuple(out)


def chiral_subsets(C, k, syms):
    props = [perm for (g, d, perm) in syms if d == 1]
    imps = [perm for (g, d, perm) in syms if d == -1]
    seen, orbs = {}, []
    for s in [frozenset(t) for t in itertools.combinations(range(C["V"]), k)]:
        if s in seen:
            continue
        orb = set(frozenset(int(perm[v]) for v in s) for perm in props)
        for t in orb:
            seen[t] = len(orbs)
        orbs.append(sorted(orb, key=sorted))
    pairs, achiral_n, done = [], 0, set()
    for k0, orb in enumerate(orbs):
        if k0 in done:
            continue
        img = seen[frozenset(int(imps[0][v]) for v in orb[0])] if imps else k0
        if img == k0:
            achiral_n += 1
            done.add(k0)
        else:
            pairs.append((orb, orbs[img]))
            done.add(k0)
            done.add(img)
    return pairs, achiral_n


def superset_sums(P, V):
    Z = np.array(P, dtype=float).copy()
    for i in range(V):
        Zr = Z.reshape(-1, 2, 1 << i)
        Zr[:, 0, :] += Zr[:, 1, :]
        Z = Zr.reshape(-1)
    return Z


def podd_fast(P, V, pairs):
    Z = superset_sums(P, V)
    tot = 0.0
    for op, om in pairs:
        tot += sum(Z[sum(1 << v for v in S)] for S in op) - sum(Z[sum(1 << v for v in S)] for S in om)
    return float(tot)


# ---------------------------------------------------------------- B4/B5/B6: KS gauge and M2
worst_d4 = {}
for L in ((2, 2, 2), (2, 2, 3), (4, 4, 4)):
    C = cluster(*L)
    syms = cluster_syms(C)
    W, gap, w, U = sea(C["h"])
    P = W @ W.T
    bits = all_patterns(C["V"]) if C["V"] <= 12 else None
    law = det_law(P, bits) if bits is not None else None
    res_h, dev = 0.0, 0.0
    for g, d, perm in syms:
        hg = permute(C["h"], perm)
        D, r = gauge_between(C["h"].astype(complex), hg.astype(complex))
        res_h = max(res_h, r, float(np.max(np.abs(D.imag))))
        Pg = permute(P, perm)
        dev = max(dev, float(np.max(np.abs(Pg - np.outer(D, np.conj(D)) * P))))
        if law is not None:
            wg, Ug = np.linalg.eigh(hg)
            Pg2 = Ug[:, :C["V"] // 2] @ Ug[:, :C["V"] // 2].T
            dev = max(dev, tv(det_law(Pg, bits), law), tv(det_law(Pg2, bits), det_law(Pg, bits)),
                      float(np.max(np.abs(Pg2 - Pg))))
    worst_d4[C["name"]] = (len(syms), sum(1 for g, d, p in syms if d == -1), res_h, dev)
check("B4 [1e-14] the Kawamoto-Smit field on the open 2x2x2, 2x2x3 and 4x4x4 blocks (%d/%d/%d box "
      "symmetries): every mirror image is D eta D for a Z2 gauge D at residual %.1e; kernel and corner "
      "record law mirror-invariant pattern by pattern, worst %.1e (cube) and %.1e (slab)"
      % (worst_d4["2x2x2"][0], worst_d4["2x2x3"][0], worst_d4["4x4x4"][0],
         max(v[2] for v in worst_d4.values()), worst_d4["2x2x2"][3], worst_d4["2x2x3"][3]),
      max(v[2] for v in worst_d4.values()) == 0.0 and max(v[3] for v in worst_d4.values()) < 1e-14
      and worst_d4["2x2x2"][:2] == (48, 24) and worst_d4["2x2x3"][:2] == (16, 8))


def M2_matrix(C):                                     # h4_designed_law.py D5
    M = np.zeros((C["V"], C["V"]), dtype=complex)
    for (x, y, z), i in C["idx"].items():
        if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
            for b in itertools.product((0, 1), repeat=3):
                s = (x + b[0], y + b[1], z + b[2])
                sb = (x + 1 - b[0], y + 1 - b[1], z + 1 - b[2])
                if C["periodic"][0]:
                    s = tuple(v % C["L"][a] for a, v in enumerate(s))
                    sb = tuple(v % C["L"][a] for a, v in enumerate(sb))
                if s in C["idx"] and sb in C["idx"]:
                    M[C["idx"][sb], C["idx"][s]] = 1j * (-1) ** b[1]
    return M


def cycles4(A):
    nz = [set(np.flatnonzero(A[i])) - {i} for i in range(A.shape[0])]
    out = set()
    for a in range(A.shape[0]):
        for b in nz[a]:
            if b < a:
                continue
            for c in nz[b]:
                if c <= a or c == b:
                    continue
                for d in nz[c]:
                    if d <= a or d in (b, c) or a not in nz[d]:
                        continue
                    out.add((a, b, c, d) if b < d else (a, d, c, b))
    return sorted(out)


def loop_products(A, cyc):
    return np.array([A[c[1], c[0]] * A[c[2], c[1]] * A[c[3], c[2]] * A[c[0], c[3]] for c in cyc])


BLK = cluster(4, 4, 4)
M2 = M2_matrix(BLK)
m2v = 0.4
hks = BLK["h"].astype(complex)
hfull = hks + m2v * M2
CYC = cycles4(hfull)
ndiag = sum(1 for c in CYC if any(M2[c[(k + 1) % 4], c[k]] != 0 for k in range(4)))
Wf, Wk = loop_products(hfull, CYC), loop_products(hks, CYC)
r_ks = r_imp = r_prop = 0.0
for g, d, perm in cluster_syms(BLK):
    Hg = permute(hfull, perm)
    dv = float(np.max(np.abs(loop_products(Hg, CYC) - Wf)))
    if d == -1:
        r_ks = max(r_ks, float(np.max(np.abs(loop_products(permute(hks, perm), CYC) - Wk))))
        r_imp = max(r_imp, dv)
    else:
        r_prop = max(r_prop, dv)
check("B5 [1e-9] PR #7949's M2 on the 4x4x4 block: %d purely imaginary entries; %d four-cycles, %d "
      "through a body diagonal; the gauge-invariant products of h_KS are mirror-invariant at %.1e, "
      "those of h_KS + m2 M2 change by %.3f under the improper AND %.3f under the PROPER rotations: "
      "not covariant under the axiom's rotations"
      % (int(np.sum(M2 != 0)), len(CYC), ndiag, r_ks, r_imp, r_prop),
      int(np.sum(M2 != 0)) == 64 and np.max(np.abs(M2.real)) == 0.0 and len(CYC) == 348
      and ndiag == 240 and r_ks == 0.0 and abs(r_imp - 0.8) < 1e-9 and abs(r_prop - 0.8) < 1e-9)

TOR = cluster(4, 4, 4, periodic=(True, True, True))
M2t = M2_matrix(TOR)
ht = TOR["h"].astype(complex) + m2v * M2t
CYT = cycles4(ht)
Wt = loop_products(ht, CYT)
keep = flipg = other = 0
keep_det = []
for g, d, perm in cluster_syms(TOR, centre=(1, 1, 1)):
    Lp = loop_products(permute(ht, perm), CYT)
    if np.max(np.abs(Lp - Wt)) < 1e-9:
        keep += 1
        keep_det.append(d)
    elif np.max(np.abs(Lp - np.conj(Wt))) < 1e-9:
        flipg += 1
    else:
        other += 1
eps = np.diag([(-1.0) ** sum(TOR["coords"][v]) for v in range(TOR["V"])])
check("B6 [1e-9] the same medium on the 4^3 torus: %d elements preserve it (%d proper + %d improper "
      "= T_h, the inversion included), the other %d send m2 -> -m2 (90-degree rotations and diagonal "
      "mirrors), none neither; eps M2 eps = -M2 at %.1e: PR #7949's P-oddness is eps-conjugation"
      % (keep, keep_det.count(1), keep_det.count(-1), flipg, np.max(np.abs(eps @ M2t @ eps + M2t))),
      keep == 24 and flipg == 24 and other == 0 and keep_det.count(1) == 12
      and np.max(np.abs(eps @ M2t @ eps + M2t)) == 0.0)

# =============================================================== C -- the sea's record statistics (T3)
CUBE, SLAB = cluster(2, 2, 2), cluster(2, 2, 3)
TOR4 = cluster(4, 4, 4, periodic=(True, True, True), twist=(1, 1, 1))
row = []
for C in (CUBE, SLAB, TOR4):
    W, gap, w, U = sea(C["h"])
    P = W @ W.T
    syms = cluster_syms(C)
    bits = all_patterns(C["V"]) if C["V"] <= 12 else None
    law = det_law(P, bits) if bits is not None else None
    wh = wp = wl = 0.0
    for g, d, perm in syms:
        D, r = gauge_between(C["h"].astype(complex), permute(C["h"], perm).astype(complex))
        wh = max(wh, r)
        Pg = permute(P, perm)
        wp = max(wp, float(np.max(np.abs(Pg - np.outer(D, np.conj(D)) * P))))
        if law is not None:
            gidx = (bits[:, perm].astype(int) * (1 << np.arange(C["V"]))).sum(axis=1)
            wl = max(wl, tv(law[gidx], law), tv(det_law(Pg, bits), law))
    row.append((C["name"], gap, len(syms), wh, wp, wl))
check("C1 [1e-15] the pi-flux sea on the cube, slab and 4^3 torus at twist (1,1,1) (%d/%d/%d "
      "symmetries, gaps %.4f/%.4f/%.4f): improper elements send the KS field to a gauge copy at %.1e "
      "and the kernel to D P D at %.1e; the record law is fixed, TV %.1e (cube), %.1e (slab)"
      % (row[0][2], row[1][2], row[2][2], row[0][1], row[1][1], row[2][1],
         max(r[3] for r in row), max(r[4] for r in row), row[0][5], row[1][5]),
      max(r[3] for r in row) == 0.0 and max(r[4] for r in row) < 1e-15
      and max(r[5] for r in row) < 1e-15 and [r[2] for r in row] == [48, 16, 48])

CHI = {}
kk_rows = []
for C in (CUBE, SLAB):
    W, gap, w, U = sea(C["h"])
    law = det_law(W @ W.T)
    bits = all_patterns(C["V"])
    syms = cluster_syms(C)
    CHI[C["name"]] = {}
    npairs, vals = [], []
    for k in (2, 3, 4, 5, 6):
        pr, ach = chiral_subsets(C, k, syms)
        CHI[C["name"]][k] = pr
        npairs.append(len(pr))
        vals.append(podd_fast(law, C["V"], pr))
    kk_rows.append((C["name"], npairs, max(abs(v) for v in vals)))
check("C2 [1e-15] chi_k, the signed sum of P(S occupied) over chiral orbit pairs of k-subsets, k = "
      "2..6: pairs cube %s, slab %s; on the sea all vanish, |chi_k| <= %.1e (cube), %.1e (slab)"
      % (kk_rows[0][1], kk_rows[1][1], kk_rows[0][2], kk_rows[1][2]),
      kk_rows[0][1] == [0, 0, 1, 0, 0] and kk_rows[1][1] == [2, 9, 23, 39, 46]
      and max(r[2] for r in kk_rows) < 1e-15)


def ursell(K, S):                                     # h4_sea_parity.py S2
    m = len(S)
    tot = 0.0
    for perm in itertools.permutations(range(1, m)):
        cyc = (0,) + perm
        prod = 1.0
        for i in range(m):
            prod *= K[S[cyc[i]], S[cyc[(i + 1) % m]]]
        tot += prod
    return (-1) ** (m - 1) * tot


def cumulant_from_law(law, bits, S):
    S = list(S)
    x = bits[:, S].astype(float)

    def E(idxs):
        return float((law * np.prod(x[:, idxs], axis=1)).sum())

    def parts(s):
        if not s:
            yield []
            return
        for smaller in parts(s[1:]):
            for n, sub in enumerate(smaller):
                yield smaller[:n] + [[s[0]] + sub] + smaller[n + 1:]
            yield [[s[0]]] + smaller
    tot = 0.0
    for part in parts(list(range(len(S)))):
        b = len(part)
        tot += (-1) ** (b - 1) * math.factorial(b - 1) * np.prod([E(p) for p in part])
    return tot


W8, g8, w8, U8 = sea(CUBE["h"])
P8 = W8 @ W8.T
law8 = det_law(P8)
bits8 = all_patterns(8)
w_cum = max(abs(ursell(P8, S) - cumulant_from_law(law8, bits8, S))
            for k in (2, 3, 4) for S in itertools.combinations(range(8), k))
W64, g64, w64, U64 = sea(TOR4["h"])
P64 = W64 @ W64.T
HELIX = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]
props = [g for g, d in zip(G48, DET) if d == 1]
imps = [g for g, d in zip(G48, DET) if d == -1]
OH = sorted(set(frozenset(tuple(g @ np.array(s)) for s in HELIX) for g in props), key=sorted)
OHM = sorted(set(frozenset(tuple(g @ np.array(s)) for s in HELIX) for g in imps), key=sorted)


def torus_shape(C, K, shape):
    L = C["L"]
    tot = 0.0
    for (x, y, z) in C["idx"]:
        S = [C["idx"][((x + s[0]) % L[0], (y + s[1]) % L[1], (z + s[2]) % L[2])] for s in shape]
        tot += ursell(K, S)
    return tot / C["V"]


chi_hel = (sum(torus_shape(TOR4, P64, list(s)) for s in OH)
           - sum(torus_shape(TOR4, P64, list(s)) for s in OHM))
mag_hel = sum(abs(torus_shape(TOR4, P64, list(s))) for s in OH)
check("C3 [1e-16] on the 4^3 torus the helix has %d proper and %d mirror images, disjoint; its "
      "translation-averaged P-odd 4-point Ursell function is %.1e against a magnitude sum %.1e; the "
      "cumulant formula matches the cube's exact law to %.1e"
      % (len(OH), len(OHM), chi_hel, mag_hel, w_cum),
      not set(OH) & set(OHM) and abs(chi_hel) < 1e-17 and w_cum < 1e-15 and len(OH) == 24)


def edge_mask(C, edges):                              # h4_common.py star tick
    m = 0
    for q in edges:
        m |= 1 << q
    return m


def h_free(C, recmask):
    hR = C["h"].copy()
    for q, (i, j) in enumerate(C["EDGES"]):
        if (recmask >> q) & 1:
            hR[i, j] = hR[j, i] = 0.0
    return hR


def star_G(C, order, tau, cache=None):
    G = np.eye(C["V"], dtype=complex)
    rec = 0
    for v in order:
        mask = edge_mask(C, C["STAR"][v])
        new = mask & ~rec
        rec |= mask
        if new == 0:
            continue
        if tau > 0 and bin(rec).count("1") < C["E"]:
            if cache is None:
                Uk = sla.expm(-1j * tau * h_free(C, rec))
            else:
                if rec not in cache:
                    cache[rec] = sla.expm(-1j * tau * h_free(C, rec))
                Uk = cache[rec]
            G = Uk @ G
    return G


def rotated_kernel(G, W):
    GW = G @ W
    return GW @ GW.conj().T


TAU = 0.5
ALL8 = list(itertools.permutations(range(8)))
cacheG = {}
KS8 = np.empty((len(ALL8), 8, 8), dtype=complex)
for oi, o in enumerate(ALL8):
    KS8[oi] = rotated_kernel(star_G(CUBE, o, TAU, cacheG), W8)
plus4 = [sorted(S) for S in CHI["2x2x2"][4][0][0]]
minus4 = [sorted(S) for S in CHI["2x2x2"][4][0][1]]


def minor_sum(Karr, subsets):
    tot = np.zeros(len(Karr))
    for S in subsets:
        tot += np.linalg.det(Karr[:, S][:, :, S]).real
    return tot


chi4 = minor_sum(KS8, plus4) - minor_sum(KS8, minus4)
law_one = det_law(KS8[137])
chi4_law = podd_fast(law_one, 8, CHI["2x2x2"][4])
nz = int(np.sum(np.abs(chi4) > 1e-12))
A8 = np.array(ALL8, dtype=np.int16)
FACT = [math.factorial(k) for k in range(9)]


def rank_perm(Parr):
    r = np.zeros(len(Parr), dtype=np.int64)
    for i in range(8):
        r += (Parr[:, i + 1:] < Parr[:, i:i + 1]).sum(axis=1) * FACT[7 - i]
    return r


wm = wr = 0.0
for g, d, perm in cluster_syms(CUBE):
    idx_img = rank_perm(np.asarray(perm)[A8])
    if d == -1:
        wm = max(wm, float(np.max(np.abs(chi4[idx_img] + chi4))))
    else:
        wr = max(wr, float(np.max(np.abs(chi4[idx_img] - chi4))))
check("C4 [1e-6] the star tick on the cube at tau = 0.5, ALL 40320 orders: max |chi_4| = %.6f, mean "
      "%.6f, nonzero in %d of 40320; the uniform-order average has chi_4 = %.1e and chi_3 vanishes "
      "identically; over all orders x 48 symmetries a mirrored order carries -chi_4 (%.1e), a rotated "
      "one +chi_4 (%.1e); minors against the exact law %.1e"
      % (np.max(np.abs(chi4)), np.mean(np.abs(chi4)), nz, chi4.mean(), wm, wr,
         abs(chi4[137] - chi4_law)),
      abs(np.max(np.abs(chi4)) - 0.088127) < 1e-6 and nz == 29376 and abs(chi4.mean()) < 1e-14
      and wm < 1e-14 and wr < 1e-14 and abs(chi4[137] - chi4_law) < 1e-14)

DECL8 = {"identity": list(range(8)), "antipodal": [0, 7, 1, 6, 2, 5, 3, 4],
         "even-first": [0, 3, 5, 6, 1, 2, 4, 7], "closed-star-first": [1, 2, 4, 0, 3, 5, 6, 7],
         "shift1": list(range(8))[1:] + [0]}
wT = 0.0
for name, o in DECL8.items():
    K = rotated_kernel(star_G(CUBE, o, TAU, cacheG), W8)
    wT = max(wT, tv(det_law(K), det_law(np.conj(K))))
WS, gapS, wS, US = sea(SLAB["h"])
bits12 = all_patterns(12)
ID12 = list(range(12))
DECL12 = {"identity": ID12, "reverse": ID12[::-1], "rshift3": ID12[::-1][3:] + ID12[::-1][:3]}
slab_chi = {}
for name, o in DECL12.items():
    K = rotated_kernel(star_G(SLAB, o, TAU), WS)
    lw = det_law(K, bits12)
    wT = max(wT, tv(lw, det_law(np.conj(K), bits12)))
    slab_chi[name] = (podd_fast(lw, 12, CHI["2x2x3"][3]), podd_fast(lw, 12, CHI["2x2x3"][4]))
check("C5 [exact] T-blindness: TV(law of K, law of K*) = %.1e over the declared cube and slab "
      "orders; the slab's identity order has (chi_3, chi_4) = (%+.4f, %+.5f), its reverse the "
      "negatives, rshift3 chi_3 = %+.4f"
      % (wT, slab_chi["identity"][0], slab_chi["identity"][1], slab_chi["rshift3"][0]),
      wT == 0.0 and abs(slab_chi["identity"][0] + 0.0426) < 1e-3
      and abs(slab_chi["reverse"][0] + slab_chi["identity"][0]) < 1e-14
      and abs(slab_chi["rshift3"][0] - 0.0842) < 1e-3)

cap_rows = []
for C in (CUBE, SLAB, TOR4):
    cap = [v for v in range(C["V"]) if chiral_capable([u is not None for u in C["NBO"][v]])]
    cap_rows.append(len(cap))
Wsl, gsl, wsl, Usl = sea(SLAB["h"])
lawsl = det_law(Wsl @ Wsl.T, bits12)
cap_sl = [v for v in range(12) if chiral_capable([u is not None for u in SLAB["NBO"][v]])]
ex_any = ex_num = 0.0
for i in range(len(bits12)):
    m = sum(1 for v in cap_sl if chiral_sign(profile(SLAB, v, bits12[i])) != 0)
    if m:
        ex_any += lawsl[i]
    ex_num += lawsl[i] * m
blocks = [(L, sum(1 for v in range(cluster(L, L, L)["V"])
                  if chiral_capable([u is not None for u in cluster(L, L, L)["NBO"][v]])))
          for L in (3, 4, 5, 6, 8)]
capable_pat = sum(1 for s in itertools.product((0, 1), repeat=6) if chiral_capable(s))
p_shape = Fraction(capable_pat, 7) / math.comb(6, 4)
check("C6 [exact] chiral-capable corners with complete records: cube %d, 4^3 torus %d, slab %d; some "
      "slab corner realises the chiral orbit with probability %.6f, expected number exactly %.6f; an "
      "open L^3 block has 12(L-2) capable sites (%s); bulk formation-time rate %s"
      % (cap_rows[0], cap_rows[2], cap_rows[1], ex_any, ex_num,
         ", ".join("L=%d: %d" % b for b in blocks), p_shape),
      cap_rows == [0, 4, 0] and abs(ex_any - 0.539063) < 1e-6 and abs(ex_num - 1.0) < 1e-12
      and all(c == 12 * (L - 2) for L, c in blocks) and p_shape == Fraction(4, 35)
      and capable_pat == 12)


# =============================================================== D -- registration handedness (T4)
KINDS = [("none", 'none', 1.0),
         ("A->{0}", ('rule', (0,), (0, 1)), 1.0),
         ("A->{1}", ('rule', (1,), (0, 1)), 1.0),
         ("max", ('rule', (0,), (1,)), 1.0),
         ("control A,B->{0}", ('rule', (0,), (0,)), 1.0),
         ("tilt lam=0.5", ('tilt', 1, -1), 0.5),
         ("tilt lam=1.0", ('tilt', 1, -1), 1.0),
         ("tilt control", ('tilt', 1, 1), 1.0)]


def current(C, axis):                                 # h4_registration.py
    J = np.zeros((C["V"], C["V"]), dtype=complex)
    for (x, y, z), u in C["idx"].items():
        v = C["NBO"][u][2 * axis]
        if v is None:
            continue
        if C["periodic"][axis] and C["coords"][v][axis] != C["coords"][u][axis] + 1:
            continue
        J[v, u] += 1j * C["h"][u, v]
        J[u, v] += -1j * C["h"][u, v]
    return J


def mover(C, U, w, axis, band=False):
    N = C["V"] // 2
    cols = ([k for k in range(N, C["V"]) if abs(w[k] - w[N]) < 1e-9] if band
            else list(range(N, C["V"])))
    B = U[:, cols]
    Jp = B.conj().T @ current(C, axis) @ B
    ev, vec = np.linalg.eigh((Jp + Jp.conj().T) / 2)
    psi = B @ vec[:, -1]
    return psi / np.linalg.norm(psi), float(ev[-1]), len(cols)


def mirror_perm(C, g, centre=None):
    for gg, d, perm in cluster_syms(C, centre):
        if np.array_equal(gg, g):
            return perm, d
    raise ValueError("not a symmetry")


def region_sym_pairs(C, region, k, centre=None):
    syms = [(g, d, perm) for (g, d, perm) in cluster_syms(C, centre)
            if set(int(perm[v]) for v in region) == set(region)]
    loc = {v: i for i, v in enumerate(region)}
    lsyms = [(g, d, np.array([loc[int(perm[v])] for v in region])) for (g, d, perm) in syms]
    pairs, ach = chiral_subsets({"V": len(region)}, k, lsyms)
    return pairs, ach, len(syms), sum(1 for g, d, p in syms if d == -1)


def fast_weights(C, region, bits, kind, lam):         # h4_registration.py
    loc = {v: i for i, v in enumerate(region)}
    w = np.ones(len(bits))
    nex = np.zeros(len(bits), dtype=int)
    for v in region:
        nb = C["NBO"][v]
        pres = [k for k, u in enumerate(nb) if u is not None and u in loc]
        code = bits[:, loc[v]].astype(int)
        for j, k in enumerate(pres):
            code |= bits[:, loc[nb[k]]].astype(int) << (j + 1)
        table = np.ones(1 << (len(pres) + 1))
        extab = np.zeros(1 << (len(pres) + 1), dtype=int)
        for c in range(1 << (len(pres) + 1)):
            prof = [OPEN] * 6
            for j, k in enumerate(pres):
                prof[k] = (c >> (j + 1)) & 1
            table[c] = tilt_factor(tuple(prof), c & 1, kind, lam)
            extab[c] = 1 if chiral_sign(tuple(prof)) else 0
        w *= table[code]
        nex += extab[code]
    return w, nex


def finished_battery(C, Ksea, psiR, perm_sigma, Dg, region=None, centre=None, kinds=KINDS):
    R = list(range(C["V"])) if region is None else list(region)
    bits = all_patterns(len(R))
    psiL = np.conj(Dg) * psiR[np.argsort(perm_sigma)]
    KR = Ksea + np.outer(psiR, np.conj(psiR))
    KL = Ksea + np.outer(psiL, np.conj(psiL))
    sub = np.ix_(R, R)
    laws = {"sea": det_law(Ksea[sub], bits), "R": det_law(KR[sub], bits), "L": det_law(KL[sub], bits)}
    loc = {v: i for i, v in enumerate(R)}
    sperm = np.array([loc[int(perm_sigma[v])] for v in R])
    gidx = (bits[:, sperm].astype(int) * (1 << np.arange(len(R)))).sum(axis=1)
    mdev = tv(laws["L"], laws["R"][gidx])
    SR = laws["R"] > laws["L"] + 1e-14
    SL = laws["L"] > laws["R"] + 1e-14
    pairs3 = region_sym_pairs(C, R, 3, centre)[0]
    out = {"mirror_dev": mdev, "base": float(laws["R"][SR].sum()),
           "ncap": sum(1 for v in R if chiral_capable([u is not None and u in loc for u in C["NBO"][v]]))}
    for name, kind, lam in kinds:
        wts, nex = fast_weights(C, R, bits, kind, lam)
        res = {}
        for st in ("sea", "R", "L"):
            Pw = laws[st] * wts
            Z = Pw.sum()
            res[st] = (Pw / Z if Z > 0 else Pw, float(Z))
        out[name] = (float(res["R"][0][SR].sum()) - float(res["L"][0][SL].sum()),
                     podd_fast(res["sea"][0], len(R), pairs3),
                     float((laws["sea"] * (nex > 0)).sum()))
    return out


W2, gap2, w2, U2 = sea(CUBE["h"])
psiR2, j2, nb2 = mover(CUBE, U2, w2, 2)
gz = np.diag([1, 1, -1]).astype(int)
perm2, d2 = mirror_perm(CUBE, gz)
D2g, r2 = gauge_between(CUBE["h"].astype(complex), permute(CUBE["h"], perm2).astype(complex))
cub = finished_battery(CUBE, (W2 @ W2.T).astype(complex), psiR2, perm2, D2g)
dvals_c = [cub[n][0] for n, k, l in KINDS]
tick_c = {}
for oname, o in (("identity", list(range(8))), ("closed-star-first", [1, 2, 4, 0, 3, 5, 6, 7])):
    G = star_G(CUBE, o, TAU, cacheG)
    KRr = G @ ((W2 @ W2.T).astype(complex) + np.outer(psiR2, np.conj(psiR2))) @ G.conj().T
    psiL2 = np.conj(D2g) * psiR2[np.argsort(perm2)]
    KLr = G @ ((W2 @ W2.T).astype(complex) + np.outer(psiL2, np.conj(psiL2))) @ G.conj().T
    lR, lL = det_law(KRr), det_law(KLr)
    tick_c[oname] = float(lR[lR > lL + 1e-14].sum()) - float(lL[lL > lR + 1e-14].sum())
check("D1 [1e-15] the cube: E>0 modes carry no current (%+.1e), no corner can realise the chiral "
      "profile, all eight tables give one finished law, Delta = %.1e, chi_3 = chi_4 = 0; the single "
      "formation orders are handed with no rule (identity %+.3e, closed-star-first %+.3e)"
      % (j2, max(abs(v) for v in dvals_c), tick_c["identity"], tick_c["closed-star-first"]),
      abs(j2) < 1e-12 and cub["ncap"] == 0 and max(abs(v) for v in dvals_c) < 1e-15
      and abs(tick_c["identity"] - 2.76e-2) < 1e-4)

psiRS, jS, nbS = mover(SLAB, US, wS, 2)
permS, dS = mirror_perm(SLAB, gz)
DS, rS = gauge_between(SLAB["h"].astype(complex), permute(SLAB["h"], permS).astype(complex))
PS = (WS @ WS.T).astype(complex)
slab = finished_battery(SLAB, PS, psiRS, permS, DS)
dsl = {n: slab[n][0] for n, k, l in KINDS}
csl = {n: slab[n][1] for n, k, l in KINDS}
check("D2 [numerical] the slab, finished reading (12 corners, 4096 patterns): right-mover <J> = %+.6f, "
      "TV(P_L, P_R o sigma) = %.1e, P_R(S_R) = %.6f; chiral tables give Delta = %+.2e, %+.2e, %+.2e, "
      "%+.3f, %+.3f with chi_3(sea) to %+.3f; the controls give %.1e and %.1e"
      % (jS, slab["mirror_dev"], slab["base"], dsl["A->{0}"], dsl["A->{1}"], dsl["max"],
         dsl["tilt lam=0.5"], dsl["tilt lam=1.0"], min(csl.values()),
         dsl["control A,B->{0}"], dsl["tilt control"]),
      abs(jS - 0.541196) < 1e-5 and slab["mirror_dev"] < 1e-14 and abs(slab["base"] - 0.253160) < 1e-6
      and abs(dsl["A->{0}"] + 1.32e-2) < 1e-4 and abs(dsl["tilt lam=1.0"] - 0.273) < 1e-3
      and abs(dsl["control A,B->{0}"]) < 1e-15 and abs(dsl["tilt control"]) < 1e-15
      and min(csl.values()) < -0.43 and abs(csl["none"]) < 1e-14
      and abs(slab["A->{0}"][2] - 0.5391) < 1e-4)


def tick_tilt(C, K, order, kind, lam, bits, pl):      # vectorised h4_common.py tick_tilt
    V = C["V"]
    P = np.ones(len(bits))
    nex = 0
    for k, v in enumerate(order):
        prev = list(order[:k])
        lawS = pl[k]
        idx_prev = np.zeros(len(bits), dtype=np.int64)
        for j, u in enumerate(prev):
            idx_prev |= bits[:, u].astype(np.int64) << j
        law_prev = pl[k - 1] if k else np.ones(1)
        cur = bits[:, v].astype(np.int64)
        denom = np.maximum(law_prev[idx_prev], 1e-300)
        good = law_prev[idx_prev] > 0
        q = np.where(good, lawS[idx_prev | (cur << k)] / denom, 0.0)
        q_alt = np.where(good, lawS[idx_prev | ((1 - cur) << k)] / denom, 0.0)
        pres = [i for i, u in enumerate(C["NBO"][v]) if u is not None and u in prev]
        code = np.zeros(len(bits), dtype=np.int64)
        for j, i in enumerate(pres):
            code |= bits[:, C["NBO"][v][i]].astype(np.int64) << j
        t0 = np.ones(1 << len(pres))
        t1 = np.ones(1 << len(pres))
        nchi = 0
        for c in range(1 << len(pres)):
            prof = [OPEN] * 6
            for j, i in enumerate(pres):
                prof[i] = (c >> j) & 1
            t0[c] = tilt_factor(tuple(prof), 0, kind, lam)
            t1[c] = tilt_factor(tuple(prof), 1, kind, lam)
            nchi += 1 if chiral_sign(tuple(prof)) else 0
        f = np.where(cur.astype(bool), t1[code], t0[code])
        f_alt = np.where(cur.astype(bool), t0[code], t1[code])
        Z = q * f + q_alt * f_alt
        P *= np.where(Z > 0, q * f / np.maximum(Z, 1e-300), 0.0)
        nex += nchi * (1 << (k - len(pres)))
    Zt = P.sum()
    return (P / Zt if Zt > 0 else P), float(1 - Zt), nex


def prefix_laws(K, order):
    return [det_law(K[np.ix_(list(order[:k]), list(order[:k]))]) for k in range(1, len(order) + 1)]


TICK_KINDS = [KINDS[0], KINDS[1], KINDS[3], KINDS[4], KINDS[6]]
syms12 = cluster_syms(SLAB)
psiLS = np.conj(DS) * psiRS[np.argsort(permS)]
KRS = PS + np.outer(psiRS, np.conj(psiRS))
KLS = PS + np.outer(psiLS, np.conj(psiLS))
gidx12 = (bits12[:, permS].astype(int) * (1 << np.arange(12))).sum(axis=1)
pairs3s = CHI["2x2x3"][3]
EVEN12 = [v for v in range(12) if SLAB["sub"][v] == 0]
ODD12 = [v for v in range(12) if SLAB["sub"][v] == 1]
fam_rows = {}
for oname, order in (("identity", ID12), ("even-first", EVEN12 + ODD12)):
    family = sorted(set(tuple(int(pm[v]) for v in order) for (gg, dd, pm) in syms12))
    store = {}
    for o in family:
        G = star_G(SLAB, list(o), TAU)
        Ks = {"sea": rotated_kernel(G, WS), "R": G @ KRS @ G.conj().T, "L": G @ KLS @ G.conj().T}
        store[o] = (Ks, {st: prefix_laws(Ks[st], list(o)) for st in Ks})
    lawR = np.mean([det_law(store[o][0]["R"], bits12) for o in family], axis=0)
    lawL = np.mean([det_law(store[o][0]["L"], bits12) for o in family], axis=0)
    SR = lawR > lawL + 1e-14
    SL = lawL > lawR + 1e-14
    rows = {"nfam": len(family), "mdev": tv(lawL, lawR[gidx12])}
    for name, kind, lam in TICK_KINDS:
        acc = {st: np.zeros(4096) for st in ("sea", "R", "L")}
        nev = 0
        for o in family:
            Ks, pls = store[o]
            for st in acc:
                Pt, lo, ev = tick_tilt(SLAB, Ks[st], list(o), kind, lam, bits12, pls[st])
                acc[st] += Pt / len(family)
                if st == "sea":
                    nev += ev
        rows[name] = (float(acc["R"][SR].sum()) - float(acc["L"][SL].sum()),
                      podd_fast(acc["sea"], 12, pairs3s), nev)
    fam_rows[oname] = rows
fi, fe = fam_rows["identity"], fam_rows["even-first"]
check("D3 [1e-15] the slab, formation-time reading (Model A star tick, tau = 0.5), the identity "
      "order's mirror-closed family of %d images: untilted laws exact mirror images (%.1e), the chiral "
      "profile exposed at %d formation events, every table Delta = %.1e and chi_3(sea) = %.1e"
      % (fi["nfam"], fi["mdev"], fi["A->{0}"][2], max(abs(fi[n][0]) for n, k, l in TICK_KINDS),
         max(abs(fi[n][1]) for n, k, l in TICK_KINDS)),
      fi["nfam"] == 16 and fi["mdev"] < 1e-15 and fi["A->{0}"][2] == 0
      and max(abs(fi[n][0]) for n, k, l in TICK_KINDS) < 1e-15
      and max(abs(fi[n][1]) for n, k, l in TICK_KINDS) < 1e-15)
check("D4 [numerical] the even-first family, which does expose the shape (%d events over %d images): "
      "the rules act, Delta = %+.2e (A->{0}), %+.2e (max), chi_3(sea) %+.3f and %+.3f, the tilt %+.2e; "
      "the mirror-symmetric control gives Delta = %.1e, chi_3(sea) = %.1e"
      % (fe["A->{0}"][2], fe["nfam"], fe["A->{0}"][0], fe["max"][0], fe["A->{0}"][1], fe["max"][1],
         fe["tilt lam=1.0"][0], fe["control A,B->{0}"][0], fe["control A,B->{0}"][1]),
      fe["A->{0}"][2] == 8448 and abs(fe["A->{0}"][0] - 4.33e-3) < 1e-4
      and abs(fe["max"][0] - 5.28e-3) < 1e-4 and abs(fe["A->{0}"][1] + 0.139) < 1e-3
      and abs(fe["control A,B->{0}"][0]) < 1e-15 and abs(fe["control A,B->{0}"][1]) < 1e-14)

T6 = cluster(6, 6, 6, periodic=(True, True, True))
W6, gap6, w6, U6 = sea(T6["h"])
P6 = (W6 @ W6.T).astype(complex)
psiR6, j6, nb6 = mover(T6, U6, w6, 0, band=True)
gx = np.diag([-1, 1, 1]).astype(int)
perm6, d6 = mirror_perm(T6, gx)
D6g, r6 = gauge_between(T6["h"].astype(complex), permute(T6["h"], perm6).astype(complex))
REG_KINDS = [KINDS[0], KINDS[1], KINDS[3], KINDS[6]]
cols = {}
for Lc in (2, 3, 4):
    region = [T6["idx"][(x, y, z)] for x in (0, 1) for y in (0, 1) for z in range(Lc)]
    cols[Lc] = finished_battery(T6, P6, psiR6, perm6, D6g, region=region, kinds=REG_KINDS)
check("D5 [numerical] the 6^3 torus, region growth (records inside, open outside; x-mover %+.6f, "
      "partner %+.6f): the fully recorded 2x2x2 block has no capable site and gives Delta = %.1e for "
      "every table; 2x2x3 and 2x2x4 give %+.2e and %+.2e (A->{0}), falling, against chi_3(sea) %+.3f "
      "and %+.3f on %d and %d capable sites"
      % (j6, -j6, max(abs(cols[2][n][0]) for n, k, l in REG_KINDS), cols[3]["A->{0}"][0],
         cols[4]["A->{0}"][0], cols[3]["A->{0}"][1], cols[4]["A->{0}"][1], cols[3]["ncap"],
         cols[4]["ncap"]),
      abs(j6 - 0.833333) < 1e-5 and cols[2]["ncap"] == 0
      and max(abs(cols[2][n][0]) for n, k, l in REG_KINDS) < 1e-15
      and abs(cols[3]["A->{0}"][0] - 1.10e-2) < 1e-4 and abs(cols[4]["A->{0}"][0] - 6.62e-3) < 1e-4
      and cols[4]["A->{0}"][1] < cols[3]["A->{0}"][1] < 0 and (cols[3]["ncap"], cols[4]["ncap"]) == (4, 8))

# ---------------------------------------------------------------- the string of PR #7949
NSTR, LZ = 12, 24
M0, XI, EMAX = 0.7, 2.0, 0.686
core = ((NSTR - 1) / 2.0, (NSTR - 1) / 2.0)
sidx = {(x, y, z): (x * NSTR + y) * LZ + z for x in range(NSTR) for y in range(NSTR) for z in range(LZ)}
VS = len(sidx)
scoord = {v: k for k, v in sidx.items()}


def string_build(n_wind, m2_on=True, uniform_phase=None):   # h4_string.py build, sparse
    rows, colsA, vals = [], [], []

    def add(i, j, val):
        rows.append(i)
        colsA.append(j)
        vals.append(val)
    for (x, y, z), i in sidx.items():
        if x + 1 < NSTR:
            j = sidx[(x + 1, y, z)]
            add(i, j, 1.0)
            add(j, i, 1.0)
        if y + 1 < NSTR:
            j = sidx[(x, y + 1, z)]
            add(i, j, float((-1) ** x))
            add(j, i, float((-1) ** x))
        j = sidx[(x, y, (z + 1) % LZ)]
        add(i, j, float((-1) ** (x + y)))
        add(j, i, float((-1) ** (x + y)))

    def mass(px, py):
        r = np.hypot(px - core[0], py - core[1])
        mag = M0 * np.tanh(r / XI) if uniform_phase is None else M0
        ph = n_wind * np.arctan2(py - core[1], px - core[0]) if uniform_phase is None else uniform_phase
        return mag, ph
    for (x, y, z), i in sidx.items():
        mag, ph = mass(x, y)
        add(i, i, mag * np.cos(ph) * (-1) ** (x + y + z))
    if m2_on:
        for X in range(NSTR // 2):
            for Y in range(NSTR // 2):
                mag, ph = mass(2 * X + 0.5, 2 * Y + 0.5)
                m2c = mag * np.sin(ph)
                for Z in range(LZ // 2):
                    for b in itertools.product((0, 1), repeat=3):
                        s = sidx[(2 * X + b[0], 2 * Y + b[1], 2 * Z + b[2])]
                        sb = sidx[(2 * X + 1 - b[0], 2 * Y + 1 - b[1], 2 * Z + 1 - b[2])]
                        add(sb, s, m2c * 1j * (-1) ** b[1])
    H = sp.csr_matrix((np.array(vals, dtype=complex), (rows, colsA)), shape=(VS, VS))
    H.sum_duplicates()
    return H


Hs = string_build(+1)
Ha = string_build(-1)
herm = abs(Hs - Hs.getH()).max() if Hs.nnz else 0.0
anti_dev = abs(Ha - Hs.conjugate()).max()
T2z = sp.csr_matrix((np.ones(VS), ([sidx[(x, y, (z + 2) % LZ)] for (x, y, z) in sidx],
                                   [sidx[(x, y, z)] for (x, y, z) in sidx])), shape=(VS, VS))
comm = abs(Hs @ T2z - T2z @ Hs).max()


def plane_syms():                                     # h4_string.py plane_syms
    out = []
    cz = (LZ - 1) / 2.0
    for g, d in zip(G48, DET):
        perm = np.zeros(VS, dtype=int)
        ok = True
        for (x, y, z), v in sidx.items():
            c = np.array([x - core[0], y - core[1], z - cz])
            gc = g @ c
            s = (gc[0] + core[0], gc[1] + core[1], gc[2] + cz)
            si = tuple(int(round(t)) for t in s)
            if any(abs(si[a] - s[a]) > 1e-9 for a in range(3)):
                ok = False
                break
            si = (si[0], si[1], si[2] % LZ)
            if si not in sidx:
                ok = False
                break
            perm[v] = sidx[si]
        if ok:
            out.append((g, d, perm))
    return out


def permute_sp(A, perm):
    P = sp.csr_matrix((np.ones(len(perm)), (perm, np.arange(len(perm)))), shape=A.shape)
    return (P @ A @ P.T).tocsr()


def gauge_between_sp(H, Hp):                          # h4_common.py gauge_between, sparse
    H, Hp = H.tocsr().copy(), Hp.tocsr().copy()
    for A in (H, Hp):
        A.data[np.abs(A.data) < 1e-12] = 0.0
        A.eliminate_zeros()
        A.sort_indices()
    if not (np.array_equal(H.indptr, Hp.indptr) and np.array_equal(H.indices, Hp.indices)):
        return float("inf")
    D = np.zeros(VS, dtype=complex)
    D[0] = 1.0
    stack, seen = [0], {0}
    while stack:
        u = stack.pop()
        for t in range(H.indptr[u], H.indptr[u + 1]):
            v = H.indices[t]
            if v not in seen and abs(H.data[t]) > 1e-12:
                seen.add(v)
                D[v] = np.conj(Hp.data[t] / (D[u] * H.data[t]))
                D[v] /= abs(D[v])
                stack.append(v)
    rowsi = np.repeat(np.arange(VS), np.diff(H.indptr))
    return float(np.max(np.abs(Hp.data - D[rowsi] * np.conj(D[H.indices]) * H.data)))


syms_str = plane_syms()
verdicts = []
for g, d, perm in syms_str:
    Hg = permute_sp(Hs, perm)
    r_self = gauge_between_sp(Hs, Hg)
    r_anti = gauge_between_sp(Ha, Hg)
    verdicts.append(("string" if r_self < 1e-9 else ("anti-string" if r_anti < 1e-9 else "neither"), d))
n_self = sum(1 for v, d in verdicts if v == "string")
n_self_imp = sum(1 for v, d in verdicts if v == "string" and d == -1)
n_anti = sum(1 for v, d in verdicts if v == "anti-string")
check("D6 [exact] PR #7949's string on 12x12x24 (open plane, periodic axis, M0 = 0.7, xi = 2): "
      "anti-string = conj(H_string) at %.1e, Hermitian %.1e, [H, T^2] = %.1e; of the %d elements about "
      "the core %d give a gauge copy of the string (%d improper: the x-mirror), %d the anti-string, %d "
      "neither: its handedness is T-odd, not mirror-odd"
      % (anti_dev, herm, comm, len(syms_str), n_self, n_self_imp, n_anti,
         len(syms_str) - n_self - n_anti),
      anti_dev == 0.0 and herm < 1e-12 and comm == 0.0 and len(syms_str) == 16
      and (n_self, n_self_imp, n_anti) == (2, 1, 2))

NC = LZ // 2


def sector_basis(q):                                  # h4_string.py sector_basis
    B = np.zeros((VS, 2 * NSTR * NSTR), dtype=complex)
    col = 0
    for x in range(NSTR):
        for y in range(NSTR):
            for b in range(2):
                for Z in range(NC):
                    B[sidx[(x, y, 2 * Z + b)], col] = np.exp(1j * q * Z) / np.sqrt(NC)
                col += 1
    return B


def current_z(H):                                     # h4_string.py current_z
    rows, colsA, vals = [], [], []
    for (x, y, z), u in sidx.items():
        v = sidx[(x, y, (z + 1) % LZ)]
        hv = H[v, u]
        rows += [v, u]
        colsA += [u, v]
        vals += [1j * hv, -1j * np.conj(hv)]
    return sp.csr_matrix((np.array(vals, dtype=complex), (rows, colsA)), shape=(VS, VS))


Jz = current_z(Hs)
xs = np.array([scoord[v][0] for v in range(VS)], dtype=float)
ys = np.array([scoord[v][1] for v in range(VS)], dtype=float)
rho = np.hypot(xs - core[0], ys - core[1])
core_mask = rho < 3.5
ring_mask = np.minimum.reduce([xs, ys, NSTR - 1 - xs, NSTR - 1 - ys]) < 2
REGS = {Lc: [sidx[(x, y, z)] for x in (5, 6) for y in (5, 6) for z in range(Lc)] for Lc in (2, 3, 4)}
allreg = sorted(set(v for r in REGS.values() for v in r))
P_reg = np.zeros((len(allreg), len(allreg)), dtype=complex)
Pa_reg = np.zeros_like(P_reg)
ortho = 0.0
resid = 0.0
in_gap = []
PsiR = None
P0 = np.pi / 6
for jq in range(NC):
    q = 2 * np.pi * jq / NC
    p = (q - np.pi + np.pi) % (2 * np.pi) - np.pi
    B = sector_basis(q)
    if jq == 0:
        ortho = float(np.max(np.abs(B.conj().T @ B - np.eye(B.shape[1]))))
    Hq = B.conj().T @ (Hs @ B)
    wq, Uq = np.linalg.eigh((Hq + Hq.conj().T) / 2)
    Bq = B[allreg, :] @ Uq
    P_reg += Bq[:, wq < 0] @ Bq[:, wq < 0].conj().T
    Hqa = B.conj().T @ (Ha @ B)
    wa, Ua = np.linalg.eigh((Hqa + Hqa.conj().T) / 2)
    Ba = B[allreg, :] @ Ua
    Pa_reg += Ba[:, wa < 0] @ Ba[:, wa < 0].conj().T
    for k in np.flatnonzero(np.abs(wq) < EMAX):
        psi = B @ Uq[:, k]
        resid = max(resid, float(np.linalg.norm(Hs @ psi - wq[k] * psi)))
        dens = np.abs(psi) ** 2
        in_gap.append((float(wq[k]), p, float(dens[core_mask].sum()), float(dens[ring_mask].sum()),
                       float(np.real(np.vdot(psi, Jz @ psi)))))
    if abs(p - P0) < 1e-9:
        ks = [k for k in range(len(wq)) if wq[k] > 0 and abs(wq[k]) < EMAX
              and (np.abs(B @ Uq[:, k]) ** 2)[core_mask].sum() > 0.6]
        PsiR = (B[allreg, :] @ Uq[:, ks], [float(wq[k]) for k in ks],
                [float(np.real(np.vdot(B @ Uq[:, k], Jz @ (B @ Uq[:, k])))) for k in ks])
        anti_res = max(float(np.linalg.norm(Ha @ np.conj(B @ Uq[:, k]) - wq[k] * np.conj(B @ Uq[:, k])))
                       for k in ks)
        anti_J = [float(np.real(np.vdot(np.conj(B @ Uq[:, k]), Jz @ np.conj(B @ Uq[:, k])))) for k in ks]
core_rows = [r for r in in_gap if r[2] > 0.6]
net_core = sum(1 if r[4] > 0 else -1 for r in core_rows if abs(r[4]) > 1e-9)
net_ring = sum(1 if r[4] > 0 else -1 for r in in_gap if r[3] > 0.6 and abs(r[4]) > 1e-9)
n_zero = sum(1 for r in in_gap if abs(r[4]) > 1e-9)
zero_J = max([abs(r[4]) for r in in_gap if abs(r[4]) <= 1e-9] or [0.0])
check("D7 [1e-12] the string in its %d cell-momentum sectors of dimension %d (orthonormal %.1e, "
      "residual %.1e): a core doublet at p = +pi/6, E = %+.5f, velocity %.4f, <J_z> = %+.3f; %d of the "
      "16 in-gap states carry a current, net %+d core against %+d ring, the other 8 at p = 0 with "
      "<J_z> = 0 to %.1e; conj(psi_R) solves the anti-string at %.1e with <J_z> = %+.3f"
      % (NC, 2 * NSTR * NSTR, ortho, resid, PsiR[1][0], PsiR[1][0] / P0, PsiR[2][0], n_zero, net_core,
         net_ring, zero_J, anti_res, anti_J[0]),
      ortho < 1e-13 and resid < 1e-12 and len(PsiR[1]) == 2 and abs(PsiR[1][0] - 0.51019) < 1e-4
      and abs(PsiR[2][0] + 1.861) < 1e-2 and (net_core, net_ring) == (-4, +4) and len(in_gap) == 16
      and n_zero == 8 and zero_J < 1e-9 and anti_res < 1e-12 and abs(anti_J[0] - 1.861) < 1e-2)

lp = {v: i for i, v in enumerate(allreg)}
KRs = P_reg + PsiR[0] @ PsiR[0].conj().T
KLs = np.conj(KRs)
Cd = {"NBO": {}, "V": VS}
for v in allreg:
    x, y, z = scoord[v]
    Cd["NBO"][v] = [sidx.get((x + d[0], y + d[1], (z + d[2]) % LZ)) for d in OFFS]
STR_KINDS = [KINDS[0], KINDS[1], KINDS[3], KINDS[6], KINDS[7]]
tvmax = 0.0
exrows = []
for Lc in (2, 3, 4):
    reg = REGS[Lc]
    loc = [lp[v] for v in reg]
    bits = all_patterns(len(reg))
    lawR = det_law(KRs[np.ix_(loc, loc)], bits)
    lawL = det_law(KLs[np.ix_(loc, loc)], bits)
    tvmax = max(tvmax, tv(lawR, lawL))
    for name, kind, lam in STR_KINDS:
        wts, nex = fast_weights(Cd, reg, bits, kind, lam)
        PR, PL = lawR * wts, lawL * wts
        tvmax = max(tvmax, tv(PR / PR.sum(), PL / PL.sum()))
    exrows.append(float((lawR * (nex > 0)).sum()))
check("D8 [exact] the string's core right-mover against the anti-string's core left-mover on the "
      "2x2xL core columns, L = 2, 3, 4 (chiral profile exercised at %s): the anti-string's sea kernel "
      "is conj(P) at %.1e and the two record laws are IDENTICAL, TV(P_R, P_L) = %.1e untilted and "
      "under every chiral rule and odds table: S_R = S_L = empty, Delta = 0"
      % (", ".join("%.3f" % e for e in exrows), float(np.max(np.abs(Pa_reg - np.conj(P_reg)))), tvmax),
      float(np.max(np.abs(Pa_reg - np.conj(P_reg)))) < 1e-15 and tvmax == 0.0
      and abs(exrows[1] - 0.594) < 1e-2 and abs(exrows[2] - 0.825) < 1e-2)


# =============================================================== E -- the mirror wall (T5)
def wall_H(Nx, qy, qz, m1, m2_of_x, periodic=False):  # h4_wall.py wall_H (final construction)
    D = 4 * Nx
    H = np.zeros((D, D), dtype=complex)

    def ind(x, b2, b3):
        return (x * 2 + b2) * 2 + b3
    for x in range(Nx):
        for b2 in range(2):
            for b3 in range(2):
                i = ind(x, b2, b3)
                xn = x + 1
                if xn == Nx and periodic:
                    xn = 0
                if xn < Nx:
                    H[ind(xn, b2, b3), i] += 1.0
                if b2 == 0:
                    j = ind(x, 1, b3)
                    H[j, i] += (-1) ** x
                    H[i, j] += (-1) ** x * np.exp(-1j * qy)
                if b3 == 0:
                    j = ind(x, b2, 1)
                    H[j, i] += (-1) ** (x + b2)
                    H[i, j] += (-1) ** (x + b2) * np.exp(-1j * qz)
                H[i, i] += m1 * (-1) ** (x + b2 + b3)
    H = H + H.conj().T - np.diag(np.diag(H))
    for X in range(Nx // 2):
        m2c = m2_of_x(2 * X + 0.5)
        for b in itertools.product((0, 1), repeat=3):
            H[ind(2 * X + 1 - b[0], 1 - b[1], 1 - b[2]), ind(2 * X + b[0], b[1], b[2])] += \
                m2c * 1j * (-1) ** b[1]
    return H


def M2_op(Nx):
    D = 4 * Nx
    M = np.zeros((D, D), dtype=complex)
    for X in range(Nx // 2):
        for b in itertools.product((0, 1), repeat=3):
            M[((2 * X + 1 - b[0]) * 2 + 1 - b[1]) * 2 + 1 - b[2],
              ((2 * X + b[0]) * 2 + b[1]) * 2 + b[2]] += 1j * (-1) ** b[1]
    return M


NXW = 48
theta = np.pi / 4
m1w, m2w = M0 * np.cos(theta), M0 * np.sin(theta)
Hu = wall_H(NXW, np.pi, np.pi, m1w, lambda x: m2w, periodic=True)
node_gap = float(np.min(np.abs(np.linalg.eigvalsh(Hu))))
xsw = np.repeat(np.arange(NXW), 4)
M2o = M2_op(NXW)
wall_rows = []
for geom, per, m2f, wcol in (("one wall", False, lambda x: m2w if x < NXW / 2 else -m2w, 3),
                             ("wall+anti", True,
                              lambda x: m2w if NXW / 4 <= x < 3 * NXW / 4 else -m2w, 4),
                             ("no wall", False, lambda x: m2w, 5)):
    best, ncnt, disp = [], 0, []
    for dqy in (0.0, 0.1, 0.2, 0.3, 0.4):
        H = wall_H(NXW, np.pi + dqy, np.pi, m1w, m2f, per)
        w, Uw = np.linalg.eigh(H)
        sel = np.flatnonzero(np.abs(w) < M0 - 0.02)
        if dqy == 0.0:
            ncnt = len(sel)
        for k in sel:
            dens = np.abs(Uw[:, k]) ** 2
            ww = float(dens[np.abs(xsw - NXW / 2 + 0.5) < 4].sum())
            aw = float(dens[(np.abs(xsw - NXW / 4 + 0.5) < 4)
                            | (np.abs(xsw - 3 * NXW / 4 + 0.5) < 4)].sum()) if per else 0.0
            ew = float(dens[(xsw < 4) | (xsw >= NXW - 4)].sum())
            m2e = float(np.real(np.vdot(Uw[:, k], M2o @ Uw[:, k])))
            best.append((abs(w[k]), float(w[k]), dqy, ww, aw, ew, m2e))
    best.sort()
    disp = sorted(set(round(t[1], 4) for t in best if t[2] == 0.4 and t[wcol] > 0.5))
    wall_rows.append((geom, ncnt, best[0], max(disp) if disp else 0.0))
check("E1 [1e-4] the m2-sign wall (48-site x-chain, transverse bits by Bloch, (m1, m2) = (%.4f, "
      "%.4f), node gap %.6f): one wall binds %d in-gap states at the node, the one nearest zero at E = "
      "%+.5f = -|m1| with <M2> = %+.3f, dispersing to %+.4f at dq_y = 0.4; anti-wall and open ends "
      "carry the same band, %+.5f and %+.5f, <M2> = 0: no handed interface mode"
      % (m1w, m2w, node_gap, wall_rows[0][1], wall_rows[0][2][1], wall_rows[0][2][6], wall_rows[0][3],
         wall_rows[1][2][1], wall_rows[2][2][1]),
      abs(node_gap - 0.7) < 1e-6 and abs(abs(wall_rows[0][2][1]) - m1w) < 1e-4
      and all(abs(r[2][6]) < 1e-3 for r in wall_rows)
      and all(abs(abs(r[2][1]) - m1w) < 1e-4 for r in wall_rows)
      and abs(wall_rows[0][3] - 0.6298) < 1e-3)


def weights_signed(C, region, bits, kind, lam, sign_of):     # h4_wall.py weights_signed
    loc = {v: i for i, v in enumerate(region)}
    w = np.ones(len(bits))
    for v in region:
        nb = C["NBO"][v]
        pres = [k for k, u in enumerate(nb) if u is not None and u in loc]
        code = bits[:, loc[v]].astype(int)
        for j, k in enumerate(pres):
            code |= bits[:, loc[nb[k]]].astype(int) << (j + 1)
        table = np.ones(1 << (len(pres) + 1))
        kk = kind
        if sign_of[v] < 0 and kind != 'none':
            kk = (kind[0], kind[2], kind[1])
        for c in range(1 << (len(pres) + 1)):
            prof = [OPEN] * 6
            for j, k in enumerate(pres):
                prof[k] = (c >> (j + 1)) & 1
            table[c] = tilt_factor(tuple(prof), c & 1, kk, lam)
        w *= table[code]
    return w


def wall_battery(C, Ksea, region, sign_of, movers, centre=None):
    R = list(region)
    bits = all_patterns(len(R))
    sub = np.ix_(R, R)
    lawS = det_law(Ksea[sub], bits)
    pairs3 = region_sym_pairs(C, R, 3, centre)[0]
    pairs4 = region_sym_pairs(C, R, 4, centre)[0]
    mv = {}
    for mname, (pR, pL) in movers.items():
        lawR = det_law((Ksea + np.outer(pR, np.conj(pR)))[sub], bits)
        lawL = det_law((Ksea + np.outer(pL, np.conj(pL)))[sub], bits)
        mv[mname] = (lawR, lawL, lawR > lawL + 1e-14, lawL > lawR + 1e-14)
    out = {}
    for name, kind, lam in [KINDS[0], KINDS[1], KINDS[3], KINDS[6]]:
        wts = weights_signed(C, R, bits, kind, lam, sign_of)
        Pw = lawS * wts
        Pw = Pw / Pw.sum()
        row = {"chi": max(abs(podd_fast(Pw, len(R), pairs3)), abs(podd_fast(Pw, len(R), pairs4)))}
        for mname, (lawR, lawL, SR, SL) in mv.items():
            PR, PL = lawR * wts, lawL * wts
            PR, PL = PR / PR.sum(), PL / PL.sum()
            row[mname] = float(PR[SR].sum()) - float(PL[SL].sum())
        out[name] = row
    return out


movers_slab = {}
for ax in (2, 0):
    pR, jj, nbb = mover(SLAB, US, wS, ax)
    g = np.diag([1, 1, 1]).astype(int)
    g[ax, ax] = -1
    pm, dd = mirror_perm(SLAB, g)
    Dm, rr = gauge_between(SLAB["h"].astype(complex), permute(SLAB["h"], pm).astype(complex))
    movers_slab["xyz"[ax]] = (pR, np.conj(Dm) * pR[np.argsort(pm)])
sign_x = {v: (1 if SLAB["coords"][v][0] == 0 else -1) for v in range(12)}
sign_eps = {v: (1 if SLAB["sub"][v] == 0 else -1) for v in range(12)}
wx = wall_battery(SLAB, PS, range(12), sign_x, movers_slab)
we = wall_battery(SLAB, PS, range(12), sign_eps, movers_slab)
check("E2 [1e-15] a rule/mirror-rule wall in the records, slab, wall plane x = 1/2: the total P-odd "
      "correlators stay zero (|chi| <= %.1e over four tables), wall-plane-mirror partners Delta = "
      "%.1e, perpendicular-mirror partners %+.2e (A->{0}), %+.2e (max), %+.2e (tilt)"
      % (max(r["chi"] for r in wx.values()), max(abs(r["x"]) for r in wx.values()),
         wx["A->{0}"]["z"], wx["max"]["z"], wx["tilt lam=1.0"]["z"]),
      max(r["chi"] for r in wx.values()) < 1e-14 and max(abs(r["x"]) for r in wx.values()) < 1e-15
      and abs(wx["A->{0}"]["z"] - 1.46e-2) < 1e-4 and abs(wx["tilt lam=1.0"]["z"] + 7.28e-2) < 1e-4)

movers6 = {}
CEN6 = (1, 1, 3)
for ax in (2, 0):
    pR, jj, nbb = mover(T6, U6, w6, ax, band=True)
    g = np.diag([1, 1, 1]).astype(int)
    g[ax, ax] = -1
    pm, dd = mirror_perm(T6, g, centre=CEN6)
    Dm, rr = gauge_between(T6["h"].astype(complex), permute(T6["h"], pm).astype(complex))
    movers6["xyz"[ax]] = (pR, np.conj(Dm) * pR[np.argsort(pm)])
region6 = [T6["idx"][(x, y, z)] for x in (0, 1) for y in (0, 1) for z in range(4)]
sign_z = {v: (1 if T6["coords"][v][2] < 2 else -1) for v in region6}
wz = wall_battery(T6, P6, region6, sign_z, movers6, centre=CEN6)
check("E3 [1e-14] the same control: rule and mirror rule on the two sublattices of the slab give "
      "Delta = %.1e for both mover types, |chi| <= %.1e; on the 6^3 torus a 2x2x4 column with a z-wall "
      "keeps |chi| <= %.1e, through-plane partners %.1e, perpendicular %+.2e, %+.2e, %+.2e"
      % (max(abs(r[m]) for r in we.values() for m in ("x", "z")), max(r["chi"] for r in we.values()),
         max(r["chi"] for r in wz.values()), max(abs(r["z"]) for r in wz.values()),
         wz["A->{0}"]["x"], wz["max"]["x"], wz["tilt lam=1.0"]["x"]),
      max(abs(r[m]) for r in we.values() for m in ("x", "z")) < 1e-14
      and max(r["chi"] for r in we.values()) < 1e-14 and max(r["chi"] for r in wz.values()) < 1e-14
      and max(abs(r["z"]) for r in wz.values()) < 1e-14
      and abs(wz["A->{0}"]["x"] - 2.28e-2) < 1e-4 and abs(wz["tilt lam=1.0"]["x"] + 7.58e-2) < 1e-4)

print("SUMMARY: handedness is law content on one four-record profile pair the readable class cannot "
      "use; a chiral rule registers a P-odd texture of its own where records are missing, and nothing "
      "that separates a mover from its time-reversed partner.  [%.1f s]" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
