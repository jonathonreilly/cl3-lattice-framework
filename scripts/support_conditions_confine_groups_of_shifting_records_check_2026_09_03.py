#!/usr/bin/env python3
"""Supplied support sets, finite centroid certificates and conditional kernels.

The complete connected-start n<=6 companion closure has an exact centroid
coboundary. It does not bound the whole group in a4/3 box, preserve original
companions or prove arbitrary-n immobility. Simultaneous admissible sets do
not select probabilities: free/6 refers only to six uniform translation
proposals with rejected stay. The ten isometry cases form a separate census.
Fixed parity cosets differ from the union of 28 N=2 sectors. Formal complements
are not all dynamic hopping events or permanent fine-site Record changes.
The L=6,8 KT calculation is global adjacency postselection with supplied
probabilities. Its Poisson rate is for a centered modulo-sum additive proxy,
not physical CoM. Finite g=32 adjacent-detuning leakage has no all-g implication.
All original check IDs and finite data are retained; exact certificates and
actual floating comparison bounds are distinguished. No runtime helper.
"""

from __future__ import annotations

import itertools
import sys
import hashlib
from pathlib import Path
from fractions import Fraction

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 150
AUDIT_INPUT_PATHS = ('docs/SUPPORT_CONDITIONS_CONFINE_GROUPS_OF_SHIFTING_RECORDS_ENERGY_COSTS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
INPUT_SHA256 = {'docs/SUPPORT_CONDITIONS_CONFINE_GROUPS_OF_SHIFTING_RECORDS_ENERGY_COSTS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-09-03.md': '8ef06463c3185db30e425de36c2c26b7623f2a40c19134de93e0260d2da79bfd', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


def verify_inputs():
    root = Path(__file__).resolve().parents[1]
    failures = []
    for relative in AUDIT_INPUT_PATHS:
        try:
            actual = hashlib.sha256((root/relative).read_bytes()).hexdigest()
        except OSError:
            actual = None
        if actual != INPUT_SHA256[relative]:
            failures.append(relative)
    check("I1 [source binding] final own note and current memo match declared input hashes", not failures)
    if failures:
        print("INPUT_FAILURE " + ", ".join(failures))
        print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
        raise SystemExit(1)

verify_inputs()
# END_INPUT_GUARD


def _tq(q, p=4):
    return ", ".join(("%." + str(p) + "f") % x for x in q)


# ======================================================== Z^3 and its groups

NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(p, d):
    return (p[0] + d[0], p[1] + d[1], p[2] + d[2])


def canon(S):
    """Translation class of a finite set of sites."""
    m = [min(p[a] for p in S) for a in range(3)]
    return frozenset((p[0] - m[0], p[1] - m[1], p[2] - m[2]) for p in S)


def ok_comp(S):
    """C_comp: every occupied site has at least one adjacent occupied site."""
    return all(any(add(p, d) in S for d in NB) for p in S)


def shifts_comp(S):
    """Every admissible one-step shift (x, y, S') of the group S under C_comp."""
    out = []
    S = set(S)
    for x in S:
        for d in NB:
            y = add(x, d)
            if y in S:
                continue
            S2 = (S - {x}) | {y}
            if ok_comp(S2):
                out.append((x, y, frozenset(S2)))
    return out


def components(S):
    S = set(S)
    out = []
    while S:
        s = S.pop()
        c, st = {s}, [s]
        while st:
            u = st.pop()
            for d in NB:
                v = add(u, d)
                if v in S:
                    S.discard(v)
                    c.add(v)
                    st.append(v)
        out.append(frozenset(c))
    return out


def polycubes(n):
    """Fixed polycubes of size n in Z^3, as translation classes."""
    cur = {canon(frozenset({(0, 0, 0)}))}
    for _ in range(n - 1):
        nxt = set()
        for S in cur:
            for p in S:
                for d in NB:
                    q = add(p, d)
                    if q not in S:
                        nxt.add(canon(S | {q}))
        cur = nxt
    return sorted(cur, key=lambda s: sorted(s))


def shape48(S):
    """Canonical form of a shape under the 48 cubic isometries and translation."""
    best = None
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            T = canon(frozenset(tuple(sg[i] * p[perm[i]] for i in range(3)) for p in S))
            k = tuple(sorted(T))
            if best is None or k < best:
                best = k
    return best


def reachable(n):
    """The whole C_comp-reachable set of n-record groups mod translation, and
    the list of admissible one-step shifts on it."""
    seen = set(polycubes(n))
    st = list(seen)
    edges = []
    while st:
        S = st.pop()
        for x, y, S2 in shifts_comp(S):
            c = canon(S2)
            edges.append((S, x, y, c))
            if c not in seen:
                seen.add(c)
                st.append(c)
    # a state discovered late still needs its own outgoing shifts recorded
    done = {S for S, _, _, _ in edges}
    for S in seen - done:
        for x, y, S2 in shifts_comp(S):
            edges.append((S, x, y, canon(S2)))
    return seen, edges


SHAPES = [
    ("dimer", [(0, 0, 0), (1, 0, 0)]),
    ("straight trimer", [(0, 0, 0), (1, 0, 0), (2, 0, 0)]),
    ("bent trimer", [(0, 0, 0), (1, 0, 0), (1, 1, 0)]),
    ("square", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]),
    ("straight-4", [(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)]),
    ("L", [(0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0)]),
    ("T", [(0, 0, 0), (1, 0, 0), (2, 0, 0), (1, 1, 0)]),
    ("S", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 0)]),
    ("skew", [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 1)]),
    ("tripod", [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]),
]


# ===================================================================== group A

def group_A():
    """The bipartite lemma: a shift severs every companion at once."""
    L = 6
    sites = list(itertools.product(range(L), repeat=3))
    col = {v: (v[0] + v[1] + v[2]) % 2 for v in sites}

    def nb(v):
        return [tuple((v[i] + d[i]) % L for i in range(3)) for d in NB]

    bonds = [(v, w) for v in sites for w in nb(v)]
    bad_col = sum(1 for v, w in bonds if col[v] == col[w])
    tri = sum(1 for v in sites for w1 in nb(v) for w2 in nb(v)
              if w1 != w2 and w2 in nb(w1))
    check("A1 [exact] the L = %d torus is bipartite by coordinate-sum parity: all %d bonds join "
          "opposite classes (%d violations), so no triangle closes -- two neighbours of a "
          "site are never adjacent (%d over %d pairs)"
          % (L, len(bonds), bad_col, tri, len(sites) * 6 * 5),
          bad_col == 0 and tri == 0 and len(bonds) == 6 * L ** 3)

    worst = -1
    lone = 0
    for v in sites:
        Nv = set(nb(v))
        for w in Nv:
            Nw = set(nb(w))
            worst = max(worst, len(Nv & Nw))
            lone += sum(1 for z in Nv if z != w and z in Nw)
    check("A2 [exact] so at each of the %d shifts x -> y there N(x), N(y) are DISJOINT (max overlap "
          "%d) and no companion of x survives at y (%d): an occupied member shifted one step loses EVERY "
          "companion at once"
          % (len(sites) * 6, worst, lone),
          worst == 0 and lone == 0)


# ===================================================================== group B

def group_B():
    """C_comp: the census, the invariants, the splitting threshold, the cage."""
    npoly = [len(polycubes(n)) for n in range(1, 7)]
    named = {}
    for nm, S in SHAPES:
        named[nm] = len(shifts_comp(frozenset(S)))
    check("B1 [exact] fixed polycubes of size 1..6 in Z^3: %s. Admissible ONE-STEP shifts under "
          "C_comp, by shape: %s"
          % (", ".join(str(x) for x in npoly),
             ", ".join("%s %d" % (nm, named[nm]) for nm, _ in SHAPES)),
          npoly == [1, 3, 15, 86, 534, 3481]
          and named["dimer"] == 0 and named["straight trimer"] == 0
          and named["bent trimer"] == 2 and named["straight-4"] == 0
          and named["square"] == 0 and named["L"] == 1 and named["T"] == 4
          and named["S"] == 2 and named["skew"] == 2 and named["tripod"] == 6)

    REACH = {}
    for n in (2, 3, 4, 5, 6):
        REACH[n] = reachable(n)
    ns = [len(REACH[n][0]) for n in (2, 3, 4, 5, 6)]
    nsh = [len(REACH[n][1]) for n in (2, 3, 4, 5, 6)]
    badn = sum(1 for n in REACH for S, x, y, c in REACH[n][1] if len(c) != n)
    badc = sum(1 for n in REACH for S in REACH[n][0] if not ok_comp(S))
    check("B2 [exact] C_comp admits NO singleton configuration -- no isolated occupied site; over the %s "
          "groups reachable mod translation at n = 2..6 and their %s shifts occupation number is "
          "conserved (%d violations, %d off-condition)"
          % ("/".join(str(x) for x in ns), "/".join(str(x) for x in nsh), badn, badc),
          ns == [3, 15, 86, 990, 11851] and nsh == [0, 24, 192, 3372, 52320]
          and badn == 0 and badc == 0 and not ok_comp(frozenset({(0, 0, 0)})))

    split = {}
    merge = {}
    minpart = 99
    for n in (2, 3, 4, 5, 6):
        sp_ = mg = 0
        for S, x, y, c in REACH[n][1]:
            a, b = len(components(S)), len(components(c))
            if b > a:
                sp_ += 1
                minpart = min(minpart, min(len(p) for p in components(c)))
            elif b < a:
                mg += 1
        split[n], merge[n] = sp_, mg
    W = frozenset({(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 1, 0)})
    wit = [(x, y, sorted(len(p) for p in components(S2)))
           for x, y, S2 in shifts_comp(W) if len(components(S2)) > 1]
    check("B3 [exact] splitting shifts: %s at n = 2, 3, 4 -- a group of size <= 4 can NEVER split. At "
          "n = 5 there are %d, witness %s splitting into %s; every part of a split at n <= 6 holds "
          ">= %d occupied sites; merges are as many (%d/%d at n = 5/6)"
          % (", ".join(str(split[n]) for n in (2, 3, 4)), split[5],
             str(sorted(W)).replace(" ", ""), str(wit[0][2]).replace(" ", "") if wit else "none",
             minpart, merge[5], merge[6]),
          split[2] == 0 and split[3] == 0 and split[4] == 0 and split[5] > 0
          and len(wit) > 0 and minpart >= 2 and merge[5] == split[5] and merge[6] == split[6])

    # ---- the CAGE: an exact rational potential of the shape
    ncomp, ninc, spreads, tot = {}, {}, {}, {}
    for n in (3, 4, 5, 6):
        states, edges = REACH[n]
        adjm = {}
        for S, x, y, c in edges:
            adjm.setdefault(S, []).append((c, tuple(Fraction(y[a] - x[a], n) for a in range(3))))
            adjm.setdefault(c, []).append((S, tuple(Fraction(x[a] - y[a], n) for a in range(3))))
        Psi, nc, inc, spread = {}, 0, 0, Fraction(0)
        for root in states:
            if root in Psi:
                continue
            nc += 1
            Psi[root] = (Fraction(0), Fraction(0), Fraction(0))
            st = [root]
            comp = [root]
            while st:
                u = st.pop()
                for w, d in adjm.get(u, []):
                    val = tuple(Psi[u][a] + d[a] for a in range(3))
                    if w not in Psi:
                        Psi[w] = val
                        st.append(w)
                        comp.append(w)
                    elif Psi[w] != val:
                        inc += 1
            for a in range(3):
                spread = max(spread, max(Psi[s][a] for s in comp) - min(Psi[s][a] for s in comp))
        bad = 0
        for S, x, y, c in edges:
            d = tuple(Fraction(y[a] - x[a], n) for a in range(3))
            if tuple(Psi[c][a] - Psi[S][a] for a in range(3)) != d:
                bad += 1
        ncomp[n], ninc[n], spreads[n], tot[n] = nc, inc + bad, spread, len(edges)
    check("B4 [exact] the CAGE: for n = 3, 4, 5, 6 an exact RATIONAL potential Phi of the SHAPE has "
          "physical (y-x)/n = Phi(c)-Phi(S) on the complete n<=6 closure -- %s inconsistencies over "
          "%s shifts, %s components -- so the lab centre of mass takes finitely many values: "
          "D_group = 0 EXACTLY"
          % ("/".join(str(ninc[n]) for n in (3, 4, 5, 6)),
             "/".join(str(tot[n]) for n in (3, 4, 5, 6)),
             "/".join(str(ncomp[n]) for n in (3, 4, 5, 6))),
          all(ninc[n] == 0 for n in (3, 4, 5, 6))
          and [tot[n] for n in (3, 4, 5, 6)] == [24, 192, 3372, 52320]
          and [ncomp[n] for n in (3, 4, 5, 6)] == [6, 13, 34, 40])
    check("B5 [exact] CENTROID coordinate range: Phi is fixed up to a constant per component, so its "
          "within-component spread bounds centroid excursion, not group diameter -- %s lattice units at n = 3, 4, 5, 6. "
          "The BENT TRIMER\'s orbit is %d configurations in one FIXED unit square: three of its "
          "corners, forever"
          % (", ".join(str(spreads[n]) for n in (3, 4, 5, 6)), _bent_orbit()[0]),
          spreads[3] == Fraction(1, 3) and spreads[4] == Fraction(1, 2)
          and spreads[5] == Fraction(4, 5) and spreads[6] == Fraction(4, 3)
          and max(spreads.values()) <= Fraction(3, 2)
          and _bent_orbit() == (4, (1, 1, 0)))


def _bent_orbit():
    """Lab-coordinate orbit of the bent trimer under C_comp one-step shifts."""
    S0 = frozenset({(0, 0, 0), (1, 0, 0), (1, 1, 0)})
    seen, st = {S0}, [S0]
    while st:
        S = st.pop()
        for _, _, S2 in shifts_comp(S):
            if S2 not in seen:
                seen.add(S2)
                st.append(S2)
    pts = [p for S in seen for p in S]
    box = tuple(max(p[a] for p in pts) - min(p[a] for p in pts) for a in range(3))
    return len(seen), box


# ===================================================================== group C

def group_C():
    """C_rig: one-step shifts frozen, simultaneous shifts rigid."""
    tot = 0
    for n in (2, 3, 4):
        for S in polycubes(n):
            Sl = sorted(S)
            adj = [(p, q) for p in Sl for q in Sl if p < q
                   and sum(abs(p[a] - q[a]) for a in range(3)) == 1]
            for x in Sl:
                for d in NB:
                    y = add(x, d)
                    if y in S:
                        continue
                    good = True
                    for p, q in adj:
                        p2 = y if p == x else p
                        q2 = y if q == x else q
                        if sum(abs(p2[a] - q2[a]) for a in range(3)) != 1:
                            good = False
                    if good:
                        tot += 1
    check("C1 [exact] under C_rig a ONE-STEP shift is frozen: over ALL %d connected groups of size "
          "2, 3, 4 they number %d -- by A1 the target is non-adjacent to "
          "x\'s other neighbours, so an occupied member with a companion cannot move alone"
          % (sum(len(polycubes(n)) for n in (2, 3, 4)), tot),
          tot == 0)

    def simul(S, strict, stay):
        Sl = sorted(S)
        n = len(Sl)
        opts = list(NB) + ([(0, 0, 0)] if stay else [])
        adj = [(i, j) for i in range(n) for j in range(i + 1, n)
               if sum(abs(Sl[i][a] - Sl[j][a]) for a in range(3)) == 1]
        res = []
        for dd in itertools.product(opts, repeat=n):
            NEW = [add(Sl[i], dd[i]) for i in range(n)]
            if len(set(NEW)) != n:
                continue
            if strict and any(dd[i] != (0, 0, 0) and NEW[i] in set(Sl) for i in range(n)):
                continue
            if all(sum(abs(NEW[i][a] - NEW[j][a]) for a in range(3)) == 1 for i, j in adj):
                res.append(dd)
        return res

    CL = [(nm, S) for nm, S in SHAPES if nm not in ("S", "skew")]
    nontr = 0
    counts = []
    for nm, S in CL:
        r = simul(frozenset(S), True, True)
        t = [d for d in r if len(set(d)) == 1]
        nontr += len(r) - len(t)
        counts.append(len(t) - 1)
    check("C2 [exact] under C_rig with the SIMULTANEOUS tick and STRICT occupancy the only admissible "
          "whole-group moves are RIGID UNIT TRANSLATIONS: %d non-translations over the %d named "
          "groups; free directions %s"
          % (nontr, len(CL), "/".join(str(c) for c in counts)),
          nontr == 0 and counts[0] == 4 and counts[2] == 2)

    bad_iso = 0
    iso = []
    for nm, S in SHAPES:
        Sl = sorted(S)
        n = len(Sl)
        D2 = [[sum((Sl[i][a] - Sl[j][a]) ** 2 for a in range(3)) for j in range(n)]
              for i in range(n)]
        res = []
        for dd in itertools.product(NB + [(0, 0, 0)], repeat=n):
            NEW = [add(Sl[i], dd[i]) for i in range(n)]
            if len(set(NEW)) != n:
                continue
            if all(sum((NEW[i][a] - NEW[j][a]) ** 2 for a in range(3)) == D2[i][j]
                   for i in range(n) for j in range(i + 1, n)):
                res.append(NEW)
        for NEW in res:
            if shape48(frozenset(NEW)) != shape48(frozenset(Sl)):
                bad_iso += 1
        iso.append((nm, len(res), sum(1 for NEW in res
                                      if len({tuple(NEW[i][a] - Sl[i][a] for a in range(3))
                                              for i in range(n)}) == 1)))
    check("C3 [exact] the ISOMETRY form with PERMISSIVE occupancy enumerates the admitted rigid rotations "
          "and reflections: all %d admissible assignments over %d groups land on a CONGRUENT copy "
          "(%d violations), %d of them translations, 7 per group"
          % (sum(k for _, k, _ in iso), len(iso), bad_iso, sum(t for _, _, t in iso)),
          bad_iso == 0 and all(t == 7 for _, _, t in iso)
          and iso == [("dimer",16,7),("straight trimer",7,7),("bent trimer",25,7),
                      ("square",19,7),("straight-4",7,7),("L",12,7),("T",12,7),
                      ("S",14,7),("skew",26,7),("tripod",22,7)]
          and sum(k for _, k, _ in iso) == 160 and sum(t for _, _, t in iso) == 70)

    # Support does not fix the probability law. Enumerate a labelled dimer law.
    old = [(0,0,0),(1,0,0)]
    dimer_steps = []
    for da, db in itertools.product(NB + [(0,0,0)], repeat=2):
        new = [add(old[0], da), add(old[1], db)]
        if len(set(new)) == 2 and sum((new[0][a]-new[1][a])**2 for a in range(3)) == 1:
            dimer_steps.append(tuple(Fraction(da[a]+db[a],2) for a in range(3)))
    mu = tuple(sum(d[a] for d in dimer_steps)/len(dimer_steps) for a in range(3))
    ratio = sum(sum((d[a]-mu[a])**2 for a in range(3)) for d in dimer_steps)/len(dimer_steps)
    check("C5 [exact] same permissive support, explicit uniform16 labelled-isometry law: D/D1=%s, not1; translations+stay=6/7, six-only=1, stay=0"
          % ratio, len(dimer_steps)==16 and mu==(0,0,0) and ratio==Fraction(5,8))

    BLK = [(i, j, k) for i in range(2) for j in range(2) for k in range(2)]
    free = {}
    for nm, S in SHAPES + [("2x2x2 block", BLK)]:
        Ss = set(S)
        free[nm] = len([t for t in NB if not (set(add(p, t) for p in S) & Ss)])
    check("C4 [exact] the OCCUPANCY convention is load-bearing: PERMISSIVE admits all 6 unit "
          "translations; under SIX UNIFORM PROPOSALS/rejected stay D_group=D_1; STRICT blocks "
          "ones -- dimer %d/6, bent trimer %d/6, 2x2x2 block %d/6, i.e. D_group/D_1 %.3f, %.3f, %.3f"
          % (free["dimer"], free["bent trimer"], free["2x2x2 block"],
             free["dimer"] / 6, free["bent trimer"] / 6, free["2x2x2 block"] / 6),
          free["dimer"] == 4 and free["bent trimer"] == 2 and free["2x2x2 block"] == 0)


# ===================================================================== group D

def group_D():
    """The cube: the parity sectors as support conditions on record patterns."""
    V = 8
    EDGES = [(i, j) for i in range(8) for j in range(i + 1, 8)
             if bin(i ^ j).count("1") == 1]
    NQ = len(EDGES)
    DIM = 1 << NQ
    SMASK = {v: sum(1 << q for q, (i, j) in enumerate(EDGES) if v in (i, j))
             for v in range(V)}

    def odd(z):
        return tuple(v for v in range(V) if bin(z & SMASK[v]).count("1") & 1)

    SEC = {}
    for z in range(DIM):
        SEC.setdefault(odd(z), []).append(z)
    vac = set(SEC[()])
    single = sum(1 for q in range(NQ) if any(odd(z ^ (1 << q)) == () for z in vac))
    W = [w for w in range(DIM) if all((z ^ w) in vac for z in vac)]
    wt = {}
    for w in W:
        wt[bin(w).count("1")] = wt.get(bin(w).count("1"), 0) + 1
    check("D1 [exact] the cube\'s %d patterns split into %d parity sectors of %d. In the "
          "VACUUM no single edge-BIT complement is admissible (%d of %d): one complement flips "
          "BOTH its corners. The sector-preserving sets are a subspace of %d, weights %s"
          % (DIM, len(SEC), len(vac), single, NQ, len(W), str({k: wt[k] for k in sorted(wt)})),
          single == 0 and len(W) == 32 and wt == {0: 1, 4: 6, 6: 16, 8: 9}
          and len(SEC) == 128 and len(vac) == 32)

    FACES = []
    for a in range(3):
        bit = 1 << a
        for val in (0, bit):
            cs = [s for s in range(8) if (s & bit) == val]
            cyc = [cs[0], cs[1], cs[3], cs[2]]
            FACES.append(cyc)
    EIX = {}
    for q, (i, j) in enumerate(EDGES):
        EIX[(i, j)] = q
        EIX[(j, i)] = q
    FSP = {0}
    for f in FACES:
        m = 0
        for i in range(4):
            m |= 1 << EIX[(f[i], f[(i + 1) % 4])]
        FSP = {s ^ m for s in FSP} | FSP
    CYC = {w for w in range(DIM) if all(bin(w & SMASK[v]).count("1") % 2 == 0 for v in range(V))}
    check("D2 [exact] that subspace is EXACTLY the span of the six face 4-cycles (%d elements, %s) "
          "and EXACTLY the cube\'s cycle space, dim E - V + 1 = %d (%s): admissible "
          "fixed-coset complement masks are cycles; no physical Record update inferred"
          % (len(FSP), set(FSP) == set(W), NQ - V + 1, CYC == set(W)),
          set(FSP) == set(W) and CYC == set(W) and len(FSP) == 32)

    fixed_moves = sum(1 for key, zs in SEC.items() for q in range(NQ)
                      if odd(zs[0] ^ (1 << q)) == key)
    check("D6 [exact] all128 FIXED parity cosets admit zero single-edge complements; N=2 union is different",
          fixed_moves == 0 and len(SEC) == 128)
    bad = 0
    rows = {}
    for u in range(V):
        for w in range(u + 1, V):
            z = SEC[tuple(sorted((u, w)))][0]
            hop = {q for q in range(NQ) if len(odd(z ^ (1 << q))) == 2}
            ann = sum(1 for q in range(NQ) if len(odd(z ^ (1 << q))) == 0)
            T = {q for q, (i, j) in enumerate(EDGES) if (u in (i, j)) ^ (w in (i, j))}
            if hop != T:
                bad += 1
            d = bin(u ^ w).count("1")
            rows.setdefault(d, [0, len(hop), ann])
            rows[d][0] += 1
    check("D3 [exact] in the N=2 UNION (initial odd corners u,w), the retained single "
          "complements are EXACTLY the edges incident to exactly one of u, w -- %d mismatches over %d "
          "pairs: %d N=2 hops; %d formal annihilation OUTSIDE N=2 at distance1 (%d pairs), %d hops at distance 2 (%d) "
          "and 3 (%d)"
          % (bad, V * (V - 1) // 2, rows[1][1], rows[1][2], rows[1][0],
             rows[2][1], rows[2][0], rows[3][0]),
          bad == 0 and rows[1][1] == 4 and rows[1][2] == 1
          and rows[2][1] == 6 and rows[2][2] == 0 and rows[3][1] == 6 and rows[3][2] == 0)

    chg = set()
    star = set()
    for u in range(V):
        for w in range(u + 1, V):
            z = SEC[tuple(sorted((u, w)))][0]
            for q in range(NQ):
                o = odd(z ^ (1 << q))
                if len(o) == 2 and set(o) != {u, w}:
                    chg.add(bin((z ^ (1 << q)) ^ z).count("1"))
                    moved = ({u, w} | set(o)) - ({u, w} & set(o))
                    star.add(len(moved))
    check("D4 [exact] at every such hop exactly %d edge BIT changes its VALUE and exactly %d odd "
          "corner moves, to an adjacent corner: the geometric star does NOT "
          "translate -- the odd corner does, and what moves is the parity pattern"
          % (min(chg), min(k // 2 for k in star)),
          chg == {1} and star == {2})

    padj = [(q, r) for q in range(NQ) for r in range(q + 1, NQ)
            if set(EDGES[q]) & set(EDGES[r])]
    z0 = SEC[()][0]
    outc = {}
    for q, r in padj:
        k = len(odd(z0 ^ (1 << q) ^ (1 << r)))
        outc[k] = outc.get(k, 0) + 1
    check("D5 [exact] and all %d adjacent TWO-edge complements -- formal algebraic operations, not asserted hopping -- LEAVE the vacuum sector: odd-corner counts %s"
          % (len(padj), str({k: outc[k] for k in sorted(outc)})),
          len(padj) == 24 and outc == {2: 24})


# ===================================================================== group E

EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    """Kogut-Susskind staggered (pi-flux) link sign of the bond (v, v + e_a)."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def torus(L):
    sites = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(sites)}
    r, c, d = [], [], []
    for v in sites:
        for a in range(3):
            w = tuple((v[i] + EX[a][i]) % L for i in range(3))
            s = float(eta_ks(v, a))
            r += [idx[w], idx[v]]
            c += [idx[v], idx[w]]
            d += [s, s]
    return sp.csr_matrix((d, (r, c)), shape=(L ** 3, L ** 3)), sites, idx


def minimal(x, L):
    x %= L
    return x - L if x > L // 2 else x


def two_record(L):
    """The two-record hopping generator H = -T on the L^3 torus, its
    configuration index, and the adjacency data.  Sparse throughout."""
    M1, sites, idx = torus(L)
    V = L ** 3
    M1d = M1.toarray()
    nbr = [[idx[tuple((v[i] + e[i]) % L for i in range(3))] for e in NB] for v in sites]
    pid = -np.ones((V, V), dtype=np.int64)
    cfg = []
    for a in range(V):
        for b in range(a + 1, V):
            pid[a, b] = pid[b, a] = len(cfg)
            cfg.append((a, b))
    nc = len(cfg)
    cfg = np.array(cfg)
    r2, c2, v2 = [], [], []
    for ci, (a, b) in enumerate(cfg):
        for (v, u) in ((a, b), (b, a)):
            for w in nbr[v]:
                if w == u:
                    continue
                amp = M1d[w, v]
                if amp == 0:
                    continue
                sgn = -1.0 if (min(v, w) < u < max(v, w)) else 1.0
                r2.append(pid[w, u])
                c2.append(ci)
                v2.append(-amp * sgn)
    H2 = sp.csr_matrix((v2, (r2, c2)), shape=(nc, nc))
    P0 = np.array([sites[a] for a in cfg[:, 0]])
    P1 = np.array([sites[b] for b in cfg[:, 1]])
    MIND = np.array([minimal(x, L) for x in range(L)])
    REL = np.stack([MIND[(P1[:, a] - P0[:, a]) % L] for a in range(3)], 1)
    DIST = np.abs(REL).sum(1)
    ADJ = np.where(DIST == 1)[0]
    AX = -np.ones(nc, dtype=np.int64)
    AX[ADJ] = np.argmax(np.abs(REL[ADJ]), axis=1)
    SUMC = (P0 + P1) % L
    return dict(L=L, M1=M1, sites=sites, idx=idx, pid=pid, cfg=cfg, nc=nc, H2=H2,
                ADJ=ADJ, AX=AX, SUMC=SUMC, MIND=MIND, DIST=DIST)


def pair_chain(T, tau):
    """One KT tick of the hard-adjacency pair, reduced to the 3 relative-axis
    classes by translation covariance.  Returns the orientation chain, the
    asymptotic centered modulo-sum PROXY rate, and the joint-move census."""
    L, idx, pid, nc = T["L"], T["idx"], T["pid"], T["nc"]
    ADJ, AX, SUMC, MIND = T["ADJ"], T["AX"], T["SUMC"], T["MIND"]
    reps = [pid[idx[(0, 0, 0)], idx[tuple(EX[a])]] for a in range(3)]
    B = np.zeros((nc, 3), dtype=complex)
    for k in range(3):
        B[reps[k], k] = 1.0
    OUT = spla.expm_multiply(-1j * tau * T["H2"], B)
    Pm = np.zeros((3, 3))
    MU = np.zeros((3, 3))
    adm = np.zeros(3)
    wrap = 0.0
    joint = []
    for k in range(3):
        p = np.abs(OUT[:, k]) ** 2
        p /= p.sum()
        adm[k] = p[ADJ].sum()
        q = p[ADJ] / p[ADJ].sum()
        s0 = SUMC[reps[k]]
        dS = np.stack([MIND[(SUMC[ADJ, i] - s0[i]) % L] for i in range(3)], 1).astype(float) / 2.0
        wrap = max(wrap, float(q[np.max(np.abs(dS), axis=1) >= L / 4.0].sum()))
        kk = AX[ADJ]
        for k2 in range(3):
            Pm[k, k2] = q[kk == k2].sum()
        MU[k] = q @ dS
        joint.append((q, dS, kk))
    w_, v_ = np.linalg.eig(Pm.T)
    k0 = int(np.argmin(np.abs(w_ - 1)))
    pi = np.real(v_[:, k0])
    pi /= pi.sum()
    m = pi @ MU
    A = np.vstack([np.eye(3) - Pm, pi[None, :]])
    bb = np.vstack([MU - m[None, :], np.zeros((1, 3))])
    h, *_ = np.linalg.lstsq(A, bb, rcond=None)
    poisson_error = float(np.max(np.abs(A@h-bb)))
    sig = 0.0
    for k in range(3):
        q, dS, kk = joint[k]
        M = dS + h[kk] - h[k] - m[None, :]
        sig += pi[k] * float(q @ (M * M).sum(1))
    # free single-record reference on the same torus
    e0 = np.zeros(L ** 3, dtype=complex)
    e0[idx[(0, 0, 0)]] = 1.0
    ps = np.abs(spla.expm_multiply(-1j * tau * (-T["M1"]), e0)) ** 2
    D = np.array([[minimal(s[i], L) for i in range(3)] for s in T["sites"]], float)
    m1 = ps @ D
    D1 = float((ps @ D ** 2).sum() - (m1 ** 2).sum()) / (6 * tau)
    # joint-move census from an axis-1 pair
    q, dS, kk = joint[0]
    old = {idx[(0, 0, 0)], idx[tuple(EX[0])]}
    cls = {}
    sites = T["sites"]
    for t, ci in enumerate(ADJ):
        a, b = T["cfg"][ci]
        new = {int(a), int(b)}
        if new == old:
            nm = "same sites"
        elif len(new & old) == 1:
            nm = "one record shifts"
        else:
            o = sorted(old)
            n2 = sorted(new)
            t1 = tuple((np.array(sites[n2[0]]) - np.array(sites[o[0]])) % L)
            t2 = tuple((np.array(sites[n2[1]]) - np.array(sites[o[1]])) % L)
            t3 = tuple((np.array(sites[n2[1]]) - np.array(sites[o[0]])) % L)
            t4 = tuple((np.array(sites[n2[0]]) - np.array(sites[o[1]])) % L)
            nm = "rigid translation" if (t1 == t2 or t3 == t4) else "non-rigid"
        cls[nm] = cls.get(nm, 0.0) + float(q[t])
    return dict(adm=adm, Pm=Pm, pi=pi, D=sig / (6 * tau), D1=D1, drift=float(np.abs(m).max()),
                wrap=wrap, census=cls, poisson_error=poisson_error, rowerr=float(np.abs(Pm.sum(1) - 1).max()))


def group_E():
    """KT: the hard-adjacency pair, against PR #7889's energetic pair."""
    T6 = two_record(6)
    T8 = two_record(8)

    # translation covariance of the tick kernel
    L = 6
    worst = 0.0
    sites, idx, pid, cfg = T6["sites"], T6["idx"], T6["pid"], T6["cfg"]
    o1, o2 = idx[(0, 0, 0)], idx[(1, 0, 0)]
    for shift in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (2, 3, 1)]:
        s1 = idx[tuple(shift)]
        s2 = idx[tuple((shift[i] + EX[0][i]) % L for i in range(3))]
        B = np.zeros((T6["nc"], 2), dtype=complex)
        B[pid[o1, o2], 0] = 1.0
        B[pid[s1, s2], 1] = 1.0
        O = spla.expm_multiply(-1j * 1.0 * T6["H2"], B)
        p0 = np.abs(O[:, 0]) ** 2
        p1 = np.abs(O[:, 1]) ** 2
        perm = np.array([pid[idx[tuple((sites[a][i] + shift[i]) % L for i in range(3))],
                             idx[tuple((sites[b][i] + shift[i]) % L for i in range(3))]]
                         for a, b in cfg])
        worst = max(worst, float(np.abs(p1[perm] - p0).max()))
    check("E1 [numerical, 1e-9] the HARD-ADJACENCY pair: on the L = 6 and L = 8 pi-flux tori the %d "
          "and %d non-adjacent two-record configurations carry odds 0, leaving %d and %d; the tick "
          "kernel is translation covariant to %.1e, so the class chain is exact"
          % (T6["nc"] - len(T6["ADJ"]), T8["nc"] - len(T8["ADJ"]),
             len(T6["ADJ"]), len(T8["ADJ"]), worst),
          T6["nc"] == 23220 and T8["nc"] == 130816 and len(T6["ADJ"]) == 648
          and len(T8["ADJ"]) == 1536 and worst < 1e-9)

    R = {}
    for T in (T6, T8):
        for tau in (0.5, 1.0):
            R[(T["L"], tau)] = pair_chain(T, tau)
    check("E6 [numerical, 1e-10] postselection masses/orientation entries positive; Poisson/centering residual small in all four cases",
          all(np.all(R[k]["adm"] > 0) and R[k]["poisson_error"] < 1e-10 and np.min(R[k]["Pm"]) > 0 for k in R))
    src = pid[idx[(0,0,0)], idx[(1,0,0)]]
    dst = pid[idx[(3,0,0)], idx[(4,0,0)]]
    alias = T6["MIND"][(T6["SUMC"][dst]-T6["SUMC"][src])%6]/2
    seed = np.zeros(T6["nc"], complex)
    seed[src] = 1
    flight = spla.expm_multiply(-.5j*T6["H2"], seed)
    alias_weight = abs(flight[dst])**2 / np.sum(np.abs(flight[T6["ADJ"]])**2)
    zero_dst = pid[idx[(0,1,1)], idx[(2,1,1)]]
    check("E7 [numerical] actual half-period event has positive conditional weight %.9f but proxy0; one separated free amplitude is zero"
          % alias_weight, np.array_equal(alias, np.zeros(3)) and alias_weight > 1e-5
          and abs(flight[zero_dst])**2 < 1e-25)
    rat = [R[(k, t)]["D"] / R[(k, t)]["D1"] for t in (0.5, 1.0) for k in (6, 8)]
    check("E2 [numerical, 1e-3 targets, 5e-3 masses] POSTSELECTED modulo-sum PROXY ratio = "
          "%.4f, %.4f at tau = 0.5 and %.4f, %.4f at tau = 1 (L = 6, 8) against the "
          "reference1/2 (no half-speed theorem); the odds on the admissible set before renormalising, %.2f and "
          "%.2f (wrap <= %.1e, drift <= %.1e)"
          % (rat[0], rat[1], rat[2], rat[3],
             R[(6, 0.5)]["adm"][0], R[(6, 1.0)]["adm"][0],
             max(R[k]["wrap"] for k in R), max(R[k]["drift"] for k in R)),
          abs(rat[0] - 0.5016) < 1e-3 and abs(rat[1] - 0.5075) < 1e-3
          and abs(rat[2] - 0.1058) < 1e-3 and abs(rat[3] - 0.1453) < 1e-3
          and abs(R[(6, 0.5)]["adm"][0] - 0.31) < 5e-3
          and abs(R[(6, 1.0)]["adm"][0] - 0.28) < 5e-3
          and max(R[k]["wrap"] for k in R) < 2e-2)

    pierr = max(float(np.abs(R[k]["pi"] - 1.0 / 3).max()) for k in R)
    chg = [1 - float(sum(R[(k, t)]["pi"][a] * R[(k, t)]["Pm"][a, a] for a in range(3)))
           for t in (0.5, 1.0) for k in (6, 8)]
    check("E3 [numerical, 1e-9 stationary/rows, 1e-3 change targets] P(adjacent) = 1 at EVERY tick by construction -- absolute, not "
          "statistical (rows sum to 1 to %.1e); the orientation is a 3-state chain on the relative "
          "axis, stationary odds exactly (1/3, 1/3, 1/3) (%.1e), P(axis changes) %.3f, %.3f at "
          "tau = 0.5 and %.3f, %.3f at 1"
          % (max(R[k]["rowerr"] for k in R), pierr, chg[0], chg[1], chg[2], chg[3]),
          pierr < 1e-9 and max(R[k]["rowerr"] for k in R) < 1e-9
          and abs(chg[1] - 0.4760) < 1e-3 and abs(chg[3] - 0.0717) < 1e-3)

    c = R[(8, 0.5)]["census"]
    check("E4 [numerical, 2e-3 targets, 1e-9 normalization] finite joint-move weights: the joint-move census at "
          "L = 8, tau = 0.5 from an axis-1 pair reads one member shifts %.3f, rigid translation %.3f, "
          "same sites %.3f, non-rigid %.3f (sum %.6f)"
          % (c["one record shifts"], c["rigid translation"], c["same sites"], c["non-rigid"],
             sum(c.values())),
          abs(c["one record shifts"] - 0.540) < 2e-3 and abs(c["rigid translation"] - 0.239) < 2e-3
          and abs(c["same sites"] - 0.218) < 2e-3 and abs(c["non-rigid"] - 0.002) < 2e-3
          and abs(sum(c.values()) - 1) < 1e-9)

    seq, unif = _energetic_pair(T6, 0.5, 32.0)
    check("E5 [numerical, 1e-3 endpoints] finite independently redeclared pair contrast: with "
          "positive ADJACENT DETUNING g=32 and no support condition P(adjacent) at ticks 1, 2, 5, 10, 20, 40 "
          "runs %s toward uniform %.4f -- sampled leakage only, no all-strength claim"
          % (_tq(seq, 3), unif),
          abs(seq[0] - 0.9783) < 1e-3 and abs(seq[-1] - 0.4235) < 1e-3
          and all(a > b for a, b in zip(seq, seq[1:])))


def _energetic_pair(T, tau, g):
    """Redeclared finite M4: two particles under positive adjacent detuning, on the exact
    111-class relative chain of the 6^3 torus."""
    L, nc, cfg, sites, idx = T["L"], T["nc"], T["cfg"], T["sites"], T["idx"]
    pid, DIST = T["pid"], T["DIST"]
    H2 = T["H2"] + sp.diags((DIST == 1).astype(float) * g)

    def relkey(a, b):
        va, vb = sites[a], sites[b]
        r1 = tuple((vb[i] - va[i]) % L for i in range(3))
        return min(r1, tuple((-x) % L for x in r1))

    keys = sorted({relkey(int(a), int(b)) for a, b in cfg})
    kid = {k: i for i, k in enumerate(keys)}
    nk = len(keys)
    ckey = np.array([kid[relkey(int(a), int(b))] for a, b in cfg], dtype=np.int64)
    kdist = np.array([sum(min(x, L - x) for x in k) for k in keys])
    rep = {kid[k]: pid[idx[(0, 0, 0)], idx[k]] for k in keys}
    csize = np.bincount(ckey, minlength=nk).astype(float)
    unif = float((csize / csize.sum())[kdist == 1].sum())
    B = np.zeros((nc, nk), dtype=complex)
    for k in range(nk):
        B[rep[k], k] = 1.0
    Q = np.zeros((nk, nk))
    for s in range(0, nk, 24):
        out = spla.expm_multiply(-1j * tau * H2, B[:, s:s + 24])
        for k in range(out.shape[1]):
            Q[s + k] = np.bincount(ckey, weights=np.abs(out[:, k]) ** 2, minlength=nk)
    p = np.zeros(nk)
    p[[k for k in range(nk) if kdist[k] == 1][0]] = 1.0
    seq = []
    for n in range(1, 41):
        p = p @ Q
        if n in (1, 2, 5, 10, 20, 40):
            seq.append(float(p[kdist == 1].sum()))
    return seq, unif


def main():
    group_A()
    group_B()
    group_C()
    group_D()
    group_E()
    print("SUMMARY: complete n<=6 CENTROID certificate, named support censuses and explicit "
          "probability laws; N=2 union differs from fixed cosets. KT is global postselection "
          "with a modulo-sum PROXY rate. No all-strength, arbitrary-n or physical Record theorem.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
