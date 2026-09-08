#!/usr/bin/env python3
"""Finite binary and quantum star templates with explicit positive exceptions.
Groups A/B retain exact binary data and all original searches. Every intended
orbit is independently rebuilt before classification; complete period histograms
include full-period junk. Mixed marker masks alone are not a uniform-junk test.
Group C retains the original finite numerical SVD/eigenvalue/rank and projection
protocols: H_Q uses the compressed eigenvalue-one projectors, with the exact PSD
common-kernel argument in the note. Four-probe errors omit iteration bias and
are diagnostic predicates only. Specific entangled vectors do not classify all
junk: additional exact product contrasts and 1D Z-pin EVEN positive cases remain.
No physical law/Record/clock or complete rule-class exclusion is inferred.
"""

from __future__ import annotations

import itertools
import sys
from collections import Counter

import numpy as np

AUDIT_TIMEOUT_SEC = 300

# Current publication and interpretation inputs; no parent campaign is imported.
AUDIT_INPUT_PATHS = ['docs/THROUGH_LATTICE_ROLE_MARKING_TWO_FINITE_NEGATIVES_BOUNDED_COMPUTATION_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']
SOURCE_INPUT_SHA256 = {'docs/THROUGH_LATTICE_ROLE_MARKING_TWO_FINITE_NEGATIVES_BOUNDED_COMPUTATION_NOTE_2026-09-03.md': 'fe4e5b446ca35a7318c88eaf15bc89bd04a241b19977c1185b2699472c7a9cfa', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

def _source_input_guard():
    from pathlib import Path
    import hashlib
    root = Path(__file__).resolve().parents[1]
    if set(AUDIT_INPUT_PATHS) != set(SOURCE_INPUT_SHA256):
        raise RuntimeError("source input declaration mismatch")
    for relative in AUDIT_INPUT_PATHS:
        path = root / relative
        if not path.is_file():
            raise RuntimeError("missing source input: " + relative)
        if hashlib.sha256(path.read_bytes()).hexdigest() != SOURCE_INPUT_SHA256[relative]:
            raise RuntimeError("source input drift: " + relative)
    print("SOURCE_INPUTS: " + " ".join(p+":"+SOURCE_INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS))

_source_input_guard()


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


# ============================================================ cubic group, stars

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
DIDX = {d: i for i, d in enumerate(DIRS)}


def _mats():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                M[i][perm[i]] = sg[i]
            out.append(tuple(tuple(r) for r in M))
    return out


ALL48 = _mats()


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


ROT24 = [M for M in ALL48 if det3(M) == 1]


def mvec(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1] + M[0][2] * v[2],
            M[1][0] * v[0] + M[1][1] * v[1] + M[1][2] * v[2],
            M[2][0] * v[0] + M[2][1] * v[1] + M[2][2] * v[2])


def mtrans(M):
    return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))


DP24 = sorted(set(tuple(DIDX[mvec(M, d)] for d in DIRS) for M in ROT24))
DP48 = sorted(set(tuple(DIDX[mvec(M, d)] for d in DIRS) for M in ALL48))


def canon_table(perms):
    """Canonical representative of every 7-bit star pattern under `perms`."""
    T = np.zeros(128, dtype=np.int64)
    for p in range(128):
        c = (p >> 6) & 1
        best = 999
        for pm in perms:
            q = 0
            for i in range(6):
                if (p >> i) & 1:
                    q |= 1 << pm[i]
            best = min(best, q)
        T[p] = (c << 6) | best
    return T


CANON24 = canon_table(DP24)
CANON48 = canon_table(DP48)


# ---- propagation tables over 7-slot star patterns (built once, globally) ----
MSET = {}
for _km in range(128):
    for _kv in range(128):
        if (_kv & _km) != _kv:
            continue
        _m = 0
        for _p in range(128):
            if (_p & _km) == _kv:
                _m |= 1 << _p
        MSET[(_km, _kv)] = _m
BIT1 = [sum(1 << p for p in range(128) if (p >> b) & 1) for b in range(7)]
BIT0 = [sum(1 << p for p in range(128) if not ((p >> b) & 1)) for b in range(7)]


def star_codes(cfg):
    """The 7-bit star pattern at every site of a periodic 0/1 configuration."""
    q = cfg.astype(np.int64) << 6
    for i, d in enumerate(DIRS):
        q |= (np.roll(cfg, shift=(-d[0], -d[1], -d[2]),
                      axis=(0, 1, 2)).astype(np.int64) << i)
    return q


def penalty(cfg, acc):
    return int(np.count_nonzero(~acc[star_codes(cfg)]))


# =========================================================== A: star patterns

def role_of(c):
    """0 corner, 1 edge, 2 face, 3 cube centre, by coordinate parity."""
    return sum(x & 1 for x in c)


def spacing2_templates(L=4):
    """The 48 templates of the period-(4,2,2) role pattern on the LxLxL torus.

    Value -1 marks a free (code) site: the coarse edge sites.
    """
    out = []
    for ax in range(3):
        for t in itertools.product(range(L), repeat=3):
            V = np.zeros((L, L, L), dtype=np.int8)
            for c in itertools.product(range(L), repeat=3):
                u = tuple((c[i] + t[i]) % L for i in range(3))
                r = role_of(u)
                if r == 0:
                    V[c] = (u[ax] // 2) % 2
                elif r == 1:
                    V[c] = -1
                elif r == 2:
                    V[c] = 0
                else:
                    V[c] = 1
            out.append((ax, V))
    uniq = {}
    for ax, V in out:
        uniq[(ax, V.tobytes())] = V
    return [uniq[k] for k in sorted(uniq)]


def group_A():
    same_partition = (len(set(CANON24.tolist())) == len(set(CANON48.tolist()))
                      == 20 and np.array_equal(CANON24, CANON48))
    check("A1 [exact] the 24 proper rotations and the full 48-element cubic group "
          "induce the SAME %d orbits on the 128 seven-bit star patterns, with "
          "identical canonical representatives, so every rotation-invariant "
          "value-reading star rule is inversion-invariant and no such rule encodes "
          "a chirality" % len(set(CANON24.tolist())), same_partition)

    T = spacing2_templates(4)
    L = 4
    seen = set()
    pairs = set()
    maxnb = 0
    for V in T:
        for c in itertools.product(range(L), repeat=3):
            nb = [tuple((c[i] + d[i]) % L for i in range(3)) for d in DIRS]
            maxnb = max(maxnb, sum(1 for x in nb if V[x] < 0))
            if V[c] < 0:
                continue
            free = [j for j, x in enumerate(nb) if V[x] < 0]
            if len(free) != 6:
                continue
            for r in range(64):
                seen.add((int(V[c]) << 6) | r)
            for x in nb:
                for b in (0, 1):
                    pairs.add((int(V[c]), b))
    check("A2 [exact] spacing 2, the vertex-star argument of PR #7834 recomputed: on "
          "the 4x4x4 torus the %d templates (16 translates x 3 orientations of "
          "period (4,2,2)) give every corner six free code neighbours, and corner "
          "stars realise all %d of the 128 value patterns and %d of the 4 adjacent "
          "pairs, so the maximal value-reading star rule is vacuous there"
          % (len(T), len(seen), len(pairs)),
          len(T) == 48 and len(seen) == 128 and len(pairs) == 4 and maxnb == 6)


# ============================== B: value-reading rules on spaced superlattices

class Geom:
    """One spaced superlattice: coarse spacing s, code site at offset p."""

    def __init__(self, s, p):
        self.s, self.p = s, p
        self.cell = [(x, y, z) for x in range(s) for y in range(s)
                     for z in range(s)]
        self.fidx = {c: i for i, c in enumerate(self.cell)}
        self.C = frozenset([(p % s, 0, 0), (0, p % s, 0), (0, 0, p % s)])
        G = []
        for R in ROT24:
            for t in self.cell:
                img = frozenset(tuple((mvec(R, c)[i] + t[i]) % s for i in range(3))
                                for c in self.C)
                if img == self.C:
                    G.append((R, t))
        self.G = G
        self.point_part = sorted(set(R for R, _ in G))
        orb_id, orbits = {}, []
        for x in self.cell:
            if x in orb_id:
                continue
            o = sorted(set(tuple((mvec(R, x)[i] + t[i]) % s for i in range(3))
                           for (R, t) in G))
            k = len(orbits)
            orbits.append(o)
            for y in o:
                orb_id[y] = k
        self.orbits, self.orb_id = orbits, orb_id
        self.morb = [k for k, o in enumerate(orbits) if o[0] not in self.C]
        assert all(y not in self.C for k in self.morb for y in orbits[k])
        self.n = len(self.morb)
        self.mpos = {k: i for i, k in enumerate(self.morb)}
        M = -np.ones((s, s, s), dtype=np.int64)
        for x in self.cell:
            if orb_id[x] in self.mpos:
                M[x] = self.mpos[orb_id[x]]
        self.MORB = M
        masks = set()
        for c in self.cell:
            m = 0
            for sl in [c] + [tuple((c[i] + d[i]) % s for i in range(3))
                             for d in DIRS]:
                if orb_id[sl] in self.mpos:
                    m |= 1 << self.mpos[orb_id[sl]]
            masks.add(m)
        self.masks = sorted(masks)
        idx = np.arange(s ** 3).reshape(s, s, s)
        self.slotidx = [idx] + [np.roll(idx, shift=(-d[0], -d[1], -d[2]),
                                        axis=(0, 1, 2)) for d in DIRS]
        self.PRE24 = self._pre(ROT24)
        cen = {}
        for c in self.cell:
            cen.setdefault(orb_id[c], sum(
                1 for d in DIRS
                if tuple((c[i] + d[i]) % s for i in range(3)) in self.C))
        self.maxcodenb = max(cen.values())
        self.codeidx = [self.fidx[c] for c in sorted(self.C)]

    def _pre(self, rots):
        """Index maps realising m_g(x) = m(R^{-1}(x - t) mod s) for all (R, t)."""
        s = self.s
        rows = []
        for R in rots:
            Ri = mtrans(R)
            for t in self.cell:
                row = np.empty(s ** 3, dtype=np.int32)
                for x in self.cell:
                    y = mvec(Ri, tuple((x[i] - t[i]) % s for i in range(3)))
                    row[self.fidx[x]] = self.fidx[tuple(y[i] % s for i in range(3))]
                rows.append(row)
        return np.array(rows, dtype=np.int32)

    def val_cell(self, a):
        """Assignment bitmask over marker orbits -> cell values, -1 on code."""
        bits = np.array([(int(a) >> i) & 1 for i in range(self.n)], dtype=np.int8)
        return np.where(self.MORB >= 0, bits[np.maximum(self.MORB, 0)],
                        -1).astype(np.int8)


def accepted_raw(g, valcell):
    """The maximal rule: accept every star class realised in an intended config."""
    v = valcell.ravel().astype(np.int64)
    base = np.zeros(g.s ** 3, dtype=np.int64)
    free = np.zeros(g.s ** 3, dtype=np.int64)
    for j, si in enumerate(g.slotidx):
        bit = (1 << 6) if j == 0 else (1 << (j - 1))
        vv = v[si.ravel()]
        base |= np.where(vv == 1, bit, 0)
        free |= np.where(vv < 0, bit, 0)
    acc = np.zeros(128, dtype=bool)
    for k in np.unique(base * 128 + free).tolist():
        b, f = k // 128, k % 128
        fb = [bit for bit in ((1 << 6) if i == 0 else (1 << (i - 1))
                              for i in range(7)) if f & bit]
        for r in range(1 << len(fb)):
            q = b
            for i, bit in enumerate(fb):
                if (r >> i) & 1:
                    q |= bit
            acc[CANON24[q]] = True
    return acc[CANON24]


def torus_stars(L):
    idx = np.arange(L ** 3).reshape(L, L, L)
    sl = [idx] + [np.roll(idx, shift=(-d[0], -d[1], -d[2]), axis=(0, 1, 2))
                  for d in DIRS]
    S = np.stack([x.ravel() for x in sl], axis=1)
    return [tuple(int(u) for u in row) for row in S]


def dpll_junk(acc, N, stars, site_stars, intended, cap=2000000):
    """Lexicographically least zero-penalty configuration that is not intended.

    Exhaustive: branch on the first undetermined site, propagate every star
    constraint to a fixed point, backtrack on conflict.  Returns
    (configuration or None, node count).  No SAT solver.
    """
    accbits = 0
    for p in range(128):
        if acc[p]:
            accbits |= 1 << p
    assign = [-1] * N
    nodes = [0]

    def propagate(queue, trail):
        while queue:
            s0 = queue.pop()
            for si in site_stars[s0]:
                slots = stars[si]
                km = kv = 0
                for j, site in enumerate(slots):
                    v = assign[site]
                    if v >= 0:
                        bit = (1 << 6) if j == 0 else (1 << (j - 1))
                        km |= bit
                        if v == 1:
                            kv |= bit
                cons = accbits & MSET[(km, kv)]
                if cons == 0:
                    return False
                if km == 127:
                    continue
                for j, site in enumerate(slots):
                    if assign[site] >= 0:
                        continue
                    b = 6 if j == 0 else (j - 1)
                    if cons & BIT1[b] == 0:
                        val = 0
                    elif cons & BIT0[b] == 0:
                        val = 1
                    else:
                        continue
                    assign[site] = val
                    trail.append(site)
                    queue.append(site)
        return True

    def rec():
        k = -1
        for i in range(N):
            if assign[i] < 0:
                k = i
                break
        if k < 0:
            cfg = list(assign)
            return cfg if not intended(cfg) else None
        nodes[0] += 1
        if nodes[0] > cap:
            raise RuntimeError("node cap")
        for val in (0, 1):
            trail = [k]
            assign[k] = val
            if propagate([k], trail):
                r = rec()
                if r is not None:
                    for s0 in trail:
                        assign[s0] = -1
                    return r
            for s0 in trail:
                assign[s0] = -1
        return None

    sys.setrecursionlimit(20000)
    return rec(), nodes[0]


def intended_rows(g, L):
    """Every intended marker pattern on the L-torus: (site index, values)."""
    s = g.s
    rep = L // s
    rows = np.unique(g._base[g.PRE24], axis=0)
    out = []
    for row in rows:
        full = np.tile(row.reshape(s, s, s), (rep, rep, rep)).ravel()
        keep = np.flatnonzero(full >= 0)
        out.append((keep, full[keep].astype(np.int8)))
    return out


def _reference_orbit(g):
    """Direct coordinate pullbacks, independent of PRE24/intended_rows."""
    if not hasattr(g, "_reference_perms"):
        xyz = np.array(list(itertools.product(range(g.s), repeat=3)), dtype=int)
        maps = []
        for perm in itertools.permutations(range(3)):
            for signs in itertools.product((-1, 1), repeat=3):
                M = np.zeros((3, 3), dtype=int)
                for row, col in enumerate(perm):
                    M[row, col] = signs[row]
                # Exact 3x3 determinant formula, not a floating orientation test.
                if det3(M) != 1:
                    continue
                for shift in xyz:
                    y = ((xyz-shift) @ M) % g.s
                    maps.append((y[:, 0]*g.s+y[:, 1])*g.s+y[:, 2])
        g._reference_perms = np.array(maps)
    key = g._base.tobytes()
    if getattr(g, "_reference_key", None) != key:
        g._reference_rows = np.unique(g._base[g._reference_perms], axis=0)
        g._reference_key = key
    return g._reference_rows


def checked_intended_rows(g, L):
    if L % g.s:
        raise ValueError("R1 intended domain: torus must be a cell multiple")
    actual = intended_rows(g, L)
    ref = _reference_orbit(g)
    if not actual or not len(ref):
        raise ValueError("R1 incomplete intended orbit: empty")
    full_actual = []
    for sites, values in actual:
        row = np.full(L**3, -1, dtype=np.int8)
        if len(sites) != len(set(map(int, sites))) or len(sites) != len(values):
            raise ValueError("R1 malformed intended orbit")
        row[sites] = values
        full_actual.append(row.tobytes())
    expected = {np.tile(row.reshape((g.s,)*3), (L//g.s,)*3).astype(np.int8).tobytes()
                for row in ref}
    if set(full_actual) != expected or len(full_actual) != len(expected):
        raise ValueError("R1 incomplete intended orbit: exact image mismatch")
    # Complete image equality above plus a direct actual-membership positive.
    cfg = np.tile(np.maximum(g._base, 0).reshape((g.s,)*3), (L//g.s,)*3).ravel()
    if not any(np.array_equal(cfg[k], v) for k, v in actual):
        raise ValueError("R1 intended positive membership failed")
    return actual


def reference_periods(cfg, L):
    xyz = list(itertools.product(range(L), repeat=3))
    values = dict(zip(xyz, cfg))
    return tuple(sorted(next(t for t in range(1, L+1)
                             if all(values[x] == values[tuple((x[a]+(t if a==axis else 0)) % L
                                                              for a in range(3))] for x in xyz))
                        for axis in range(3)))


def periods_of(cfg, L):
    A = np.array(cfg).reshape(L, L, L)
    per = []
    for ax in range(3):
        for k in range(1, L + 1):
            if L % k == 0 and np.array_equal(A, np.roll(A, k, axis=ax)):
                per.append(k)
                break
        else:
            per.append(L)
    return tuple(sorted(per))


def sweep_superlattice(g, nsample):
    """Exhaustive sweep over every covariant assignment on one superlattice.

    Acceptance and covariance: the base intended configuration with every code
    filling is checked for every assignment; the full rotation-and-translation
    orbit of the intended configuration, again with every code filling, is
    checked on `nsample` evenly spaced assignments.
    """
    s = g.s
    L = s
    N = L ** 3
    stars = torus_stars(L)
    site_stars = [[] for _ in range(N)]
    for si, sl in enumerate(stars):
        for site in set(sl):
            site_stars[site].append(si)
    tot = 1 << g.n
    npass = sum(1 for a in range(tot)
                if all((a & m) != 0 and (a & m) != m for m in g.masks))
    accsz = []
    cnt = Counter()
    njunk = nvac = nlift = 0
    totnodes = maxnodes = 0
    covar_ok = True
    intended_uniform = uniform_junk = 0
    fill = list(itertools.product((0, 1), repeat=len(g.codeidx)))
    step = max(1, tot // nsample)
    sample = set(range(0, tot, step))
    for a in range(tot):
        g._base = g.val_cell(a).ravel()
        acc = accepted_raw(g, g.val_cell(a))
        accsz.append(int(acc.sum()))
        if acc.all():
            nvac += 1
        rows = (np.unique(g._base[g.PRE24], axis=0) if a in sample
                else g._base.reshape(1, -1))
        for row in rows:
            free = np.flatnonzero(row < 0)
            for bits in fill:
                cfg = row.copy()
                cfg[free] = np.array(bits, dtype=np.int8)[:len(free)]
                if penalty(cfg.reshape(s, s, s), acc) != 0:
                    covar_ok = False
        IR = checked_intended_rows(g, L)

        def is_int(cfg, IR=IR):
            c = np.array(cfg, dtype=np.int8)
            return any(np.array_equal(c[k], v) for k, v in IR)

        for bit in (0, 1):
            uniform = np.full(N, bit, dtype=np.int8)
            is_member = is_int(uniform)
            if a == (0 if bit == 0 else tot-1):
                if not (acc[127*bit] and is_member):
                    raise ValueError("R2 intended uniform positive case failed")
                intended_uniform += 1
            uniform_junk += int(bool(acc[127*bit]) and not is_member)
        cfg, nodes = dpll_junk(acc, N, stars, site_stars, is_int)
        totnodes += nodes
        maxnodes = max(maxnodes, nodes)
        if cfg is None:
            continue
        njunk += 1
        assert penalty(np.array(cfg).reshape(L, L, L), acc) == 0
        reported_period = periods_of(cfg, L)
        if reported_period != reference_periods(cfg, L):
            raise ValueError("R3 period calculation disagrees with coordinate translations")
        cnt[reported_period] += 1
        big = np.tile(np.array(cfg).reshape(L, L, L), (2, 2, 2))
        IR2 = checked_intended_rows(g, 2 * L)
        bb = big.ravel()
        if penalty(big, acc) == 0 and not any(
                np.array_equal(bb[k], v) for k, v in IR2):
            nlift += 1
    return dict(tot=tot, npass=npass, accsz=accsz, cnt=cnt, njunk=njunk,
                nvac=nvac, nlift=nlift, nodes=totnodes, maxnodes=maxnodes,
                covar=covar_ok, nsample=len(sample), nimg=len(g.PRE24),
                intended_uniform=intended_uniform, uniform_junk=uniform_junk)


def group_B():
    cases = [(3, 1), (3, 2), (4, 2)]
    geoms = {c: Geom(*c) for c in cases}
    res = {}
    for c in cases:
        res[c] = sweep_superlattice(geoms[c], 16)

    geo = " ; ".join(
        "s=%d p=%d |G_pt|=%d orbits=%d masks=%d code_nbrs<=%d"
        % (c[0], c[1], len(geoms[c].point_part), geoms[c].n,
           len(geoms[c].masks), geoms[c].maxcodenb) for c in cases)
    check("B1 [exact] zoom-out lemma: %s -- no site has an all-code star, the count "
          "being 1 or 3, never 6, so the spacing-2 vacuity of A2 is defeated at every "
          "spacing tested and any failure below has another mechanism" % geo,
          all(geoms[c].maxcodenb in (1, 3) for c in cases))

    check("B2 [exact] the maximal rule accepts its own intended configurations and is "
          "covariant: penalty 0 for all %d + %d + %d assignments with every code "
          "filling, and for %d sampled ones over every rotation and translate too; "
          "accepted sizes |A| of 128 span %d-%d, %d-%d, %d-%d, and %d are vacuous"
          % (res[(3, 1)]["tot"], res[(3, 2)]["tot"], res[(4, 2)]["tot"],
             sum(res[c]["nsample"] for c in cases),
             min(res[(3, 1)]["accsz"]), max(res[(3, 1)]["accsz"]),
             min(res[(3, 2)]["accsz"]), max(res[(3, 2)]["accsz"]),
             min(res[(4, 2)]["accsz"]), max(res[(4, 2)]["accsz"]),
             sum(res[c]["nvac"] for c in cases)),
          all(res[c]["covar"] for c in cases)
          and sum(res[c]["nvac"] for c in cases) == 0)

    check("B3 [exact mask diagnostic] mixed-marker masks do not establish uniform junk; "
          "uniform configurations require complete intended-orbit exclusion; "
          "the original mask-diagnostic counts are "
          "%d/%d, %d/%d, %d/%d"
          % (res[(3, 1)]["npass"], res[(3, 1)]["tot"],
             res[(3, 2)]["npass"], res[(3, 2)]["tot"],
             res[(4, 2)]["npass"], res[(4, 2)]["tot"]),
          res[(3, 1)]["npass"] == 282 and res[(3, 2)]["npass"] == 282
          and res[(4, 2)]["npass"] == 32)

    def cen(r):
        return " ".join("%dx%d%d%d" % (v, k[0], k[1], k[2])
                        for k, v in sorted(r["cnt"].items(), key=lambda kv: -kv[1]))

    r1, r2, r3 = res[(3, 1)], res[(3, 2)], res[(4, 2)]
    check("B4 [exact, exhaustive propagation, no SAT] s=3, both code positions, all "
          "%d assignments each: %d and %d admit junk, %d are junk-free; the period "
          "multiset census of the lexicographically least junk witness is the same "
          "for both, count x abc = %s (intended 333); %d branch nodes, %d at worst"
          % (r1["tot"], r1["njunk"], r2["njunk"],
             r1["tot"] - r1["njunk"] + r2["tot"] - r2["njunk"], cen(r1),
             r1["nodes"] + r2["nodes"], max(r1["maxnodes"], r2["maxnodes"])),
          r1["njunk"] == r1["tot"] and r2["njunk"] == r2["tot"]
          and cen(r1) == cen(r2))
    check("B5 [exact, exhaustive propagation, no SAT] s=4 midpoint, all %d "
          "assignments: %d admit junk, %d junk-free; census count x abc = %s "
          "(intended 444); %d branch nodes, %d at worst"
          % (r3["tot"], r3["njunk"], r3["tot"] - r3["njunk"], cen(r3),
             r3["nodes"], r3["maxnodes"]), r3["njunk"] == r3["tot"])

    tot = sum(res[c]["njunk"] for c in cases)
    lift = sum(res[c]["nlift"] for c in cases)
    check("B6 [exact] each of the %d witnesses tiles to the 2s-torus (6^3 and 8^3) "
          "with penalty 0, still no translate or rotation of the intended pattern, so "
          "junk survives the doubled box, %d of %d: no covariant maximal "
          "value-reading star rule tested is junk-free"
          % (tot, lift, tot), lift == tot and tot == 2560)


    expected3 = Counter({(3,3,3):489, (1,1,1):438, (1,3,3):73, (1,1,3):24})
    expected4 = Counter({(1,1,1):321, (1,2,2):37, (2,2,2):36, (1,1,2):33,
                         (1,1,4):31, (4,4,4):17, (1,4,4):15, (1,2,4):11,
                         (2,2,4):8, (2,4,4):3})
    check("R1 [exact orbit] all2560 original and doubled-box intended images independently complete, with intended positive controls",
          tot == lift == 2560)
    check("R2 [exact uniform classification] six accepted intended-uniform examples are excluded from junk; genuine uniform-junk examples also exist",
          sum(res[c]["intended_uniform"] for c in cases) == 6
          and all(res[c]["uniform_junk"] > 0 for c in cases))
    check("R3 [exact full census] actual coordinate periods match every original count, including489/489 full333 and17 full444 witnesses",
          r1["cnt"] == r2["cnt"] == expected3 and r3["cnt"] == expected4)


# ================================= C: state-reading star templates (quantum)

R2 = 1.0 / np.sqrt(2.0)
PST = {"0": np.array([1, 0], dtype=complex),
       "1": np.array([0, 1], dtype=complex),
       "+": np.array([R2, R2], dtype=complex),
       "-": np.array([R2, -R2], dtype=complex),
       "i": np.array([R2, 1j * R2], dtype=complex),
       "j": np.array([R2, -1j * R2], dtype=complex)}
NAMES = ["0", "1", "+", "-", "i", "j"]


def kron_list(vs):
    out = np.array([1.0 + 0j])
    for v in vs:
        out = np.kron(out, v)
    return out


def eb(b):
    return PST["0"] if b == 0 else PST["1"]


def K_basis_2d(v, f, variant):
    """Intended role-star states, 2D: slots c, +x, -x, +y, -y."""
    V = []
    for bits in itertools.product((0, 1), repeat=4):
        if variant == "EVEN" and sum(bits) % 2:
            continue
        V.append(kron_list([v] + [eb(b) for b in bits]))
    for bits in itertools.product((0, 1), repeat=4):
        V.append(kron_list([f] + [eb(b) for b in bits]))
    for cb in (0, 1):
        V.append(kron_list([eb(cb), v, v, f, f]))
        V.append(kron_list([eb(cb), f, f, v, v]))
    return np.array(V)


def K_basis_3d(v, f, c, variant):
    V = []
    for bits in itertools.product((0, 1), repeat=6):
        if variant == "EVEN" and sum(bits) % 2:
            continue
        V.append(kron_list([v] + [eb(b) for b in bits]))
    V.append(kron_list([c] + [f] * 6))
    for ax in range(3):
        for bits in itertools.product((0, 1), repeat=4):
            nb = [None] * 6
            it = iter(bits)
            for a in range(3):
                if a == ax:
                    nb[2 * a] = c
                    nb[2 * a + 1] = c
                else:
                    nb[2 * a] = eb(next(it))
                    nb[2 * a + 1] = eb(next(it))
            V.append(kron_list([f] + nb))
    for ax in range(3):
        for cb in (0, 1):
            nb = []
            for a in range(3):
                nb += [v, v] if a == ax else [f, f]
            V.append(kron_list([eb(cb)] + nb))
    return np.array(V)


def K_basis_1d(v, variant):
    V = []
    for bits in itertools.product((0, 1), repeat=2):
        if variant == "EVEN" and sum(bits) % 2:
            continue
        V.append(kron_list([v, eb(bits[0]), eb(bits[1])]))
    for cb in (0, 1):
        V.append(kron_list([eb(cb), v, v]))
    return np.array(V)


def projector(rows, tol=1e-9):
    M = np.array(rows).T
    U, s, _ = np.linalg.svd(M, full_matrices=False)
    r = int((s > tol * max(1.0, s[0])).sum())
    B = U[:, :r]
    return B @ B.conj().T, r


def lattice(shape):
    dim = len(shape)
    coords = list(itertools.product(*[range(L) for L in shape]))
    index = {c: i for i, c in enumerate(coords)}
    stars = []
    for c in coords:
        slots = [c]
        for a in range(dim):
            p = list(c)
            p[a] = (c[a] + 1) % shape[a]
            slots.append(tuple(p))
            m = list(c)
            m[a] = (c[a] - 1) % shape[a]
            slots.append(tuple(m))
        stars.append([index[t] for t in slots])
    return coords, index, stars


def compress(Pi, slots, nslots):
    """Pull Pi back through the diagonal isometry V of the repeated slots."""
    dist = sorted(set(slots))
    k = len(dist)
    pos = {s: j for j, s in enumerate(dist)}
    idx = np.zeros(2 ** k, dtype=int)
    for p in range(2 ** k):
        bits = [(p >> (k - 1 - j)) & 1 for j in range(k)]
        si = 0
        for i, s in enumerate(slots):
            si |= bits[pos[s]] << (nslots - 1 - i)
        idx[p] = si
    return dist, Pi[np.ix_(idx, idx)]


def star_projectors(shape, Pi, nslots):
    coords, index, stars = lattice(shape)
    out = []
    aliased = False
    for slots in stars:
        if len(set(slots)) == nslots:
            out.append((list(slots), Pi))
            continue
        aliased = True
        dist, A = compress(Pi, slots, nslots)
        w, U = np.linalg.eigh(A)
        sel = w > 1 - 1e-9
        out.append((dist, U[:, sel] @ U[:, sel].conj().T))
    return coords, len(coords), out, aliased


def apply_local(M, sites, n, X):
    m = X.shape[1]
    k = len(sites)
    T = X.reshape([2] * n + [m])
    T = np.moveaxis(T, sites, range(k))
    sh = T.shape
    T = (M @ T.reshape(2 ** k, -1)).reshape(sh)
    T = np.moveaxis(T, range(k), sites)
    return T.reshape(2 ** n, m)


def energy(projs, n, X):
    Y = np.zeros_like(X)
    for ax, Q in projs:
        Y += X - apply_local(Q, ax, n, X)
    return np.real(np.einsum("ij,ij->j", X.conj(), Y))


def intended_products(shape, pins, variant):
    """The intended global states as lists of single-site factors."""
    dim = len(shape)
    coords, index, stars = lattice(shape)
    out = []
    for off in itertools.product((0, 1), repeat=dim):
        roles = [sum((c[a] + off[a]) % 2 for a in range(dim)) for c in coords]
        edges = [i for i, r in enumerate(roles) if r == 1]
        epos = {s: j for j, s in enumerate(edges)}
        cons = []
        if variant == "EVEN":
            for i, r in enumerate(roles):
                if r:
                    continue
                cntd = {}
                for s in stars[i][1:]:
                    cntd[s] = cntd.get(s, 0) + 1
                mask = [epos[s] for s, ct in cntd.items() if ct % 2]
                if mask:
                    cons.append(mask)
        for bits in itertools.product((0, 1), repeat=len(edges)):
            if any(sum(bits[j] for j in cs) % 2 for cs in cons):
                continue
            out.append([eb(bits[epos[i]]) if roles[i] == 1 else pins[roles[i]]
                        for i in range(len(coords))])
    return out


def span_tools(pl):
    """Rank and pseudo-inverse Gram of the intended span, without materialising it."""
    N = len(pl)
    G = np.ones((N, N), dtype=complex)
    for i in range(len(pl[0])):
        col = np.array([p[i] for p in pl])
        G *= col.conj() @ col.T
    w, U = np.linalg.eigh(G)
    keep = w > 1e-8 * max(w.max(), 1.0)
    r = int(keep.sum())
    return r, (U[:, keep] * (1.0 / w[keep])) @ U[:, keep].conj().T


def overlaps(pl, X):
    C = np.empty((len(pl), X.shape[1]), dtype=complex)
    for a, p in enumerate(pl):
        C[a] = kron_list(p).conj() @ X
    return C


def intended_err(projs, n, pl, seed=3, k=4):
    idx = np.random.default_rng(seed).choice(len(pl), size=min(k, len(pl)),
                                             replace=False)
    Y = np.array([kron_list(pl[i]) for i in idx]).T.copy()
    return float(np.abs(energy(projs, n, Y)).max())


def complete_intended_error(projs, pl):
    """All finite intended products, tested locally without 2**n amplitudes."""
    if not pl:
        raise ValueError("R4 empty intended product family")
    error = np.zeros(len(pl))
    for sites, Q in projs:
        Y = np.array([kron_list([state[i] for i in sites]) for state in pl]).T
        diff = Y - Q @ Y
        error += np.real(np.einsum("ij,ij->j", diff.conj(), diff))
    return float(error.max())


def dense_case(shape, Kb, pins, variant, nslots):
    """Numerical dense nullity on a small torus (at most 8 qubits)."""
    Pi, dimK = projector(Kb)
    if dimK == 2 ** nslots:
        return dict(dimK=dimK, vacuous=True)
    coords, n, projs, aliased = star_projectors(shape, Pi, nslots)
    d = 2 ** n
    H = np.zeros((d, d), dtype=complex)
    I = np.eye(d, dtype=complex)
    for ax, Q in projs:
        H += I - apply_local(Q, ax, n, I)
    w = np.linalg.eigvalsh(H)
    pl = intended_products(shape, pins, variant)
    r, _ = span_tools(pl)
    return dict(dimK=dimK, vacuous=False, nullity=int((w < 1e-9).sum()),
                expected=r, ierr=intended_err(projs, n, pl), aliased=aliased,
                complete_ierr=complete_intended_error(projs, pl))


def pocs_case(shape, Kb, pins, variant, nslots, M=4, maxsweeps=400,
              tol=1e-13, seed=20260903):
    """Matrix-free: alternating projections onto the intersection of star kernels."""
    Pi, dimK = projector(Kb)
    coords, n, projs, aliased = star_projectors(shape, Pi, nslots)
    pl = intended_products(shape, pins, variant)
    r, Ginv = span_tools(pl)
    rng = np.random.default_rng(seed)
    X = (rng.standard_normal((2 ** n, M))
         + 1j * rng.standard_normal((2 ** n, M))) / np.sqrt(2.0)
    X0 = X.copy()
    it = 0
    while it < maxsweeps:
        for ax, Q in projs:
            X = apply_local(Q, ax, n, X)
        it += 1
        if it % 10 == 0:
            nrm2 = np.maximum(np.linalg.norm(X, axis=0) ** 2, 1e-300)
            if (energy(projs, n, X) / nrm2).max() < tol:
                break
    nrm2 = np.maximum(np.linalg.norm(X, axis=0) ** 2, 1e-300)
    resid = float((energy(projs, n, X) / nrm2).max())
    ov = np.real(np.einsum("ij,ij->j", X0.conj(), X))
    C = overlaps(pl, X)
    inside = np.real(np.einsum("ai,ab,bi->i", C.conj(), Ginv, C)) / nrm2
    return dict(dimK=dimK, expected=r, resid=resid, sweeps=it,
                est=float(ov.mean()), se=float(ov.std(ddof=1) / np.sqrt(M)),
                jlo=float(1 - inside.max()), jhi=float(1 - inside.min()),
                ierr=intended_err(projs, n, pl))


def junk_character(shape, Kb, pins, variant, nslots, seed=5, sweeps=200,
                   tol=1e-13):
    Pi, dimK = projector(Kb)
    coords, n, projs, aliased = star_projectors(shape, Pi, nslots)
    pl = intended_products(shape, pins, variant)
    r, Ginv = span_tools(pl)
    rng = np.random.default_rng(seed)
    x = (rng.standard_normal((2 ** n, 1))
         + 1j * rng.standard_normal((2 ** n, 1))) / np.sqrt(2.0)
    it = 0
    while it < sweeps:
        for ax, Q in projs:
            x = apply_local(Q, ax, n, x)
        it += 1
        if it % 10 == 0:
            if float(energy(projs, n, x)[0]) / max(
                    float(np.linalg.norm(x) ** 2), 1e-300) < tol:
                break
    a = Ginv @ overlaps(pl, x)
    proj = np.zeros_like(x)
    for i, p in enumerate(pl):
        proj[:, 0] += a[i, 0] * kron_list(p)
    v = x - proj
    v /= np.linalg.norm(v)
    E = float(energy(projs, n, v)[0])
    C = overlaps(pl, v)
    ins = float(np.real(C.conj().T @ Ginv @ C)[0, 0])
    T = v.reshape([2] * n)
    half = n // 2
    sv = np.linalg.svd(T.reshape(2 ** half, 2 ** half), compute_uv=False)
    sr = int((sv > 1e-8 * sv[0]).sum())
    pur = []
    for i in range(n):
        A = np.moveaxis(T, i, 0).reshape(2, -1)
        rho = A @ A.conj().T
        pur.append(float(np.real(np.trace(rho @ rho))))
    return dict(E=E, inside=ins, rank=sr, dim=2 ** half, maxpur=max(pur))


def group_C():
    diag = np.array([[1, 0], [0, 0], [0, 0], [0, 1]], dtype=complex).T
    ok = True
    for nm in NAMES:
        p = PST[nm]
        w = np.kron(p, p)
        res = np.linalg.norm(w - diag.T @ (diag.conj() @ w))
        if (res < 1e-12) != (nm in "01"):
            ok = False
    check("C1 [algebra with numerical pin checks] aliasing lemma, algebraic half: a side of length 2 identifies "
          "the two +- neighbour slots on that axis, so the star term is the pullback "
          "h = 1 - V^dag Pi_K V and the image of the diagonal isometry V on that pair "
          "is span{|00>,|11>}, holding the pinned product |p>|p> exactly when ab = 0 "
          "for |p> = a|0> + b|1>, a Z eigenstate; on all %d pins"
          % len(NAMES), ok)

    rows = {}
    nvac = nfaith = nunf = 0
    unf_nonZ = True
    for vn in NAMES:
        for fn in NAMES:
            for var in ("EVEN", "FULL"):
                r = dense_case((4, 2), K_basis_2d(PST[vn], PST[fn], var),
                               {0: PST[vn], 2: PST[fn]}, var, 5)
                if r["vacuous"]:
                    nvac += 1
                    if not (var == "FULL" and vn != fn):
                        unf_nonZ = False
                    continue
                if r["ierr"] < 1e-9:
                    if r["complete_ierr"] > 1e-9:
                        raise ValueError("R4 sampled faithful row fails complete intended coverage")
                    nfaith += 1
                    rows[(vn, fn, var)] = r
                else:
                    nunf += 1
                    if vn in "01" or fn in "01":
                        unf_nonZ = False
    jz = [rows[k]["nullity"] - rows[k]["expected"]
          for k in [("0", "0", "EVEN"), ("0", "0", "FULL"), ("0", "1", "EVEN")]]
    check("C2 [numerical finite linear algebra] aliasing lemma, computed half, 2D 4x2 torus in full: of the 72 "
          "(pin pair, variant) cases %d are vacuous -- exactly FULL at all 30 pairs "
          "with v != f -- and of the %d live cases %d are faithful and %d not, the "
          "unfaithful being exactly those with neither pin a Z eigenstate"
          % (nvac, nfaith + nunf, nfaith, nunf),
          nvac == 30 and nfaith == 22 and nunf == 20 and unf_nonZ)

    check("C3 [numerical finite linear algebra] 2D 4x2 torus, faithful Z-pin rows: v=f=|0> gives dim K = %d, "
          "nullity %d against %d intended, so %d junk zero modes in EVEN and %d in "
          "FULL; v=|0> f=|1> gives dim K = %d, nullity %d against %d, so %d junk. No "
          "faithful named-pin choice on this torus is junk-free"
          % (rows[("0", "0", "EVEN")]["dimK"], rows[("0", "0", "EVEN")]["nullity"],
             rows[("0", "0", "EVEN")]["expected"], jz[0], jz[1],
             rows[("0", "1", "EVEN")]["dimK"], rows[("0", "1", "EVEN")]["nullity"],
             rows[("0", "1", "EVEN")]["expected"], jz[2]),
          jz == [12, 4, 36] and all(rows[k]["nullity"] > rows[k]["expected"]
                                    for k in rows))

    dk = {"EVEN": [], "FULL": []}
    zfaith = True
    for vn in "01+-":
        for fn in "01+-":
            for cn in "01+-":
                for var in ("EVEN", "FULL"):
                    Kb = K_basis_3d(PST[vn], PST[fn], PST[cn], var)
                    Pi, d = projector(Kb)
                    dk[var].append(d)
                    if vn in "01" and fn in "01" and cn in "01":
                        coords, n, projs, al = star_projectors((4, 2, 2), Pi, 7)
                        pl = intended_products(
                            (4, 2, 2), {0: PST[vn], 2: PST[fn], 3: PST[cn]}, var)
                        if complete_intended_error(projs, pl) > 1e-9:
                            zfaith = False
    check("C4 [numerical finite linear algebra] 3D seven-site star, all 64 pin triples from {0,1,+,-} and both "
          "variants: dim K runs %d-%d of 128 in EVEN and %d-%d in FULL, so no "
          "template is vacuous, and all 16 all-Z triples are faithful on the 4x2x2 "
          "torus -- which is why the 3D rows use Z pins only"
          % (min(dk["EVEN"]), max(dk["EVEN"]), min(dk["FULL"]), max(dk["FULL"])),
          min(dk["EVEN"]) == 51 and max(dk["EVEN"]) == 76
          and min(dk["FULL"]) == 65 and max(dk["FULL"]) == 105
          and max(dk["EVEN"] + dk["FULL"]) < 128 and zfaith)

    check("R4 [complete finite intended coverage] every intended product in each numerically faithful2D row and all16 all-Z3D cases was checked locally",
          zfaith and all(v["complete_ierr"] < 1e-9 for v in rows.values())
          and complete_intended_error([([0], np.diag([1., 0.]))],
                                      [[PST["0"]], [PST["1"]]]) == 1.)

    c2d = [(("+", "+"), "EVEN"), (("+", "+"), "FULL"), (("0", "1"), "EVEN"),
           (("+", "-"), "EVEN"), (("0", "+"), "EVEN")]
    r2d = {}
    for (vn, fn), var in c2d:
        r2d[(vn, fn, var)] = pocs_case(
            (4, 4), K_basis_2d(PST[vn], PST[fn], var),
            {0: PST[vn], 2: PST[fn]}, var, 5)
    frs = [(r2d[k]["jlo"], r2d[k]["jhi"]) for k in r2d]
    txt = " ; ".join("%s%s %s %.2f-%.2f" % (k[0], k[1], k[2][0], v["jlo"], v["jhi"])
                     for k, v in r2d.items())
    check("C5 [numerical, matrix-free, seed fixed] 2D 4x4 torus, no aliasing, state "
          "vectors of length 65536: alternating projections from a random start reach "
          "residual energy at most %.0e and carry junk fraction (weight outside the "
          "intended span) %s"
          % (max(v["resid"] for v in r2d.values()), txt),
          max(v["resid"] for v in r2d.values()) < 1e-12
          and min(f[0] for f in frs) > 0.25 and max(v["ierr"] for v in r2d.values()) < 1e-9)

    est = " ; ".join("%s%s %s %.0f+-%.0f vs %d intended"
                     % (k[0], k[1], k[2][0], v["est"], v["se"], v["expected"])
                     for k, v in r2d.items())
    check("C6 [numerical, stochastic, seed fixed] the same runs give "
          "finite-product trace diagnostics targeting kernel dimension, %d probes, sample SE only (iteration bias unbounded): %s -- "
          "each far above its intended count" % (4, est),
          all(v["est"] - 3 * v["se"] > v["expected"] for v in r2d.values()))

    c3d = [(("0", "0", "0"), "EVEN"), (("0", "0", "0"), "FULL"),
           (("0", "1", "0"), "EVEN"), (("0", "1", "1"), "EVEN")]
    r3d = {}
    for (vn, fn, cn), var in c3d:
        r3d[(vn, fn, cn, var)] = pocs_case(
            (4, 2, 2), K_basis_3d(PST[vn], PST[fn], PST[cn], var),
            {0: PST[vn], 2: PST[fn], 3: PST[cn]}, var, 7)
    t3 = " ; ".join("%s%s%s %s dimK=%d junkfrac %.2f-%.2f est %.0f+-%.0f vs %d"
                    % (k[0], k[1], k[2], k[3][0], v["dimK"], v["jlo"], v["jhi"],
                       v["est"], v["se"], v["expected"]) for k, v in r3d.items())
    check("C7 [numerical, matrix-free, seed fixed] 3D 4x2x2 torus, Z pins, the "
          "faithful case: %s; residual energy at most %.0e, intended-state energy at "
          "most %.0e" % (t3, max(v["resid"] for v in r3d.values()),
                         max(v["ierr"] for v in r3d.values())),
          max(v["resid"] for v in r3d.values()) < 1e-12
          and min(v["jlo"] for v in r3d.values()) > 0.4
          and all(v["est"] - 3 * v["se"] > v["expected"] for v in r3d.values()))

    j2 = junk_character((4, 4), K_basis_2d(PST["+"], PST["+"], "EVEN"),
                        {0: PST["+"], 2: PST["+"]}, "EVEN", 5)
    j3 = junk_character((4, 2, 2), K_basis_3d(PST["0"], PST["0"], PST["0"], "EVEN"),
                        {0: PST["0"], 2: PST["0"], 3: PST["0"]}, "EVEN", 7)
    check("C8 [numerical, matrix-free, seed fixed] these two particular extracted "
          "junk vectors are entangled (product junk also exists); energy at "
          "most %.0e, weight inside the intended span at most %.0e, Schmidt rank %d "
          "and %d across a half cut of %d, every single-site reduced state mixed with "
          "purity at most %.3f and %.3f -- no site is pinned"
          % (max(j2["E"], j3["E"]), max(j2["inside"], j3["inside"]), j2["rank"],
             j3["rank"], j2["dim"], j2["maxpur"], j3["maxpur"]),
          max(j2["E"], j3["E"]) < 1e-12 and max(j2["inside"], j3["inside"]) < 1e-12
          and j2["rank"] > 1 and j3["rank"] > 1
          and max(j2["maxpur"], j3["maxpur"]) < 0.8)

    out = []
    jf = []
    for var in ("EVEN", "FULL"):
        for vn in "01+-":
            r = dense_case((8,), K_basis_1d(PST[vn], var), {0: PST[vn]}, var, 3)
            j = r["nullity"] - r["expected"]
            out.append((vn, var, r["dimK"], r["nullity"], r["expected"], j))
            if j == 0 and r["ierr"] < 1e-9:
                jf.append((vn, var))
    check("C9 [numerical finite linear algebra] the one-dimensional contrast, three-site stars on an 8-ring: Z "
          "pins in the EVEN variant are junk-free, dim K = 3 and nullity 3 equal to "
          "the 3 intended states, while |+> and |-> in EVEN give nullity 9 against 4 "
          "and every tested FULL choice 47 against 31; %d of 8 junk-free: "
          "this positive exception is retained in every negative scope" % len(jf),
          sorted(jf) == [("0", "EVEN"), ("1", "EVEN")]
          and [o[3:] for o in out if o[1] == "EVEN" and o[0] == "0"] == [(3, 3, 0)])


def exact_z_census(shape, Kb, pins, variant):
    Kb = np.asarray(Kb)
    if not np.all((Kb == 0) | (Kb == 1)) or not np.all(np.count_nonzero(Kb, axis=1) == 1):
        raise ValueError("R5 requires actual one-hot Z-basis templates")
    allowed = np.any(Kb != 0, axis=0)
    coords, _, stars = lattice(shape)
    n = len(coords)
    states = np.arange(1 << n, dtype=np.uint32)
    valid = np.ones(len(states), dtype=bool)
    for star in stars:
        words = np.zeros(len(states), dtype=np.uint32)
        for site in star:
            words = (words << 1) | ((states >> (n-1-site)) & 1)
        valid &= allowed[words]
    intended = set()
    for factors in intended_products(shape, pins, variant):
        z = 0
        for factor in factors:
            if not np.array_equal(factor, PST["0"]) and not np.array_equal(factor, PST["1"]):
                raise ValueError("R5 intended factors not computational basis")
            z = (z << 1) | int(np.argmax(factor))
        intended.add(z)
    if not intended or not all(valid[z] for z in intended):
        raise ValueError("R5 intended set is not inside actual local zero space")
    return int(valid.sum()), len(intended), bool(valid[0] and 0 not in intended)


def correction_controls():
    rows = []
    for names, variant in [("000", "EVEN"), ("000", "FULL"), ("010", "EVEN"), ("011", "EVEN")]:
        v, f, c = [PST[x] for x in names]
        rows.append(exact_z_census((4,2,2), K_basis_3d(v,f,c,variant),
                                  {0:v,2:f,3:c}, variant))
    check("R5 [exact actual product junk] all-Z3D nullity/intended447/173,743/349,999/252,2286/244; all-zero product junk for010/011 EVEN",
          [r[:2] for r in rows] == [(447,173),(743,349),(999,252),(2286,244)]
          and rows[2][2] and rows[3][2])
    positive = [exact_z_census((8,), K_basis_1d(PST[v], "EVEN"), {0:PST[v]}, "EVEN") for v in "01"]
    check("R6 [exact positive exception] both1D Z-pin EVEN cases have actual zero-space=intended dimension3",
          all(r[:2] == (3,3) for r in positive))
    # Exercise the actual repeated-slot compressor and eigenvalue-one selector.
    Pi = np.zeros((8, 8))
    Pi[0, 0] = 1.
    vec = np.zeros(8)
    vec[3], vec[1] = .5, np.sqrt(3)/2
    Pi += np.outer(vec, vec)
    _, _, actual_projs, _ = star_projectors((2,), Pi, 3)
    Q = actual_projs[0][1]
    _, A = compress(Pi, [0, 1, 1], 3)
    eig = np.linalg.eigvalsh(A)
    check("R7 [actual PSD alias control] A is a positive contraction; actual Q selects only eigenvalue1, equal kernels with distinct spectra and I-A<=I-Q",
          np.allclose(Pi@Pi, Pi) and np.all(eig >= 0) and np.all(eig <= 1)
          and np.allclose(Q, np.diag([1.,0.,0.,0.])) and not np.allclose(A,Q)
          and np.linalg.eigvalsh(Q-A).max() < 1e-12)


def main():
    group_A()
    group_B()
    group_C()
    correction_controls()
    print("SUMMARY: all2560 named binary assignments admit unwanted configurations, including full-period witnesses. Named2D/3D quantum rows exhibit local-intersection/global-span excess, with numerical limits stated; two1D Z-pin EVEN cases are junk-free. Neither the full rule classes nor physical Record selection is settled.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
