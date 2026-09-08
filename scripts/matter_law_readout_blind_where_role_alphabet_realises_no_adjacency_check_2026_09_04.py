#!/usr/bin/env python3
"""Conditional static role-table fibres and binary template censuses.
Missing cross-symbol adjacencies provide the stated persistent obstruction;
the finite partial catalogs respect aliases. Formal complement families and
static membership do not provide physical preparation or readable histories.

Self-contained definitions. The following source-block names are preserved
historical provenance labels; exact original probe files are not bound here.
The present implemented definitions and proofs, not a claimed copy identity,
are the reviewable inputs:

  * the role pattern, the proper cubic rotations, the offset sets NN and
    NN u {+-2e}, the tori, the minimal covariant support tables and the
    Burnside orbit counts        -- source block `r5_common.py`;
  * T1, the role census and the entry counts, the 12-offset census and the
    covariance identity          -- source block `r5_census.py` sections A, B;
  * T2, the solver-free admissible-set search, the excitation families read
    back to roles through the 5x5x5 template match, and the partial exercised
    set of the sectors           -- source block `r5_census.py` sections C, D, E;
  * T3, the visibility decision for every unexercised entry, the star
    certificate, the reciprocal obstruction and the solver-free search on the
    smallest torus               -- source blocks `r5_visibility.py`,
                                    `r5_witnesses.py`;
  * T3, the certified fibre bounds and the double stars
                                 -- source block `r5_fibre.py`;
  * T3, the 12-offset partial table and its type-ii Burnside count
                                 -- source block `r5_ax2_partial.py`;
  * T4, the record-level tables, the closing window, the minimal defect
    number and the 2-, 3- and 4-record censuses
                                 -- source blocks `r5_records.py`,
                                    `r5_records4.py`.

One census is too large to redo inside the runner's budget and is reduced to a
declared sub-family, with the remainder quoted from the source output line
named in the historical note, without the original producer/log in this unit: the 512-window sweep. A declared inclusion-minimal
window and its maximal proper rotation-closed sub-windows are recomputed here
and the 201/17 totals are unverified historical quotations.

Every unexercised entry of the nearest-neighbour role table is decided on the
smallest torus without a solver: the type-ii entries by the reciprocal
obstruction, which is torus-independent, and the type-i and type-iii entries by
the depth-first search, in every run.  CaDiCaL re-decides them on 4x2x2, 4x4x2
and 4x4x4, and decides a declared type-ii sub-family. These solver paths are required;
unavailable or indeterminate decisions fail the complete run.  No sampling, no seed and no random number generator is used
anywhere.
"""

from __future__ import annotations

import itertools
import math
import time
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 300

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THE_DESIGNED_MATTER_LAW_IS_READ_FROM_RECORDS_ONLY_WHERE_ITS_ROLE_"
    "ALPHABET_REALISES_AN_ADJACENCY_THE_ROLE_TABLE_IS_BLIND_ON_95_PERCENT_OF_"
    "PARTIAL_ENTRIES_WHILE_EVERY_TWO_AND_THREE_SITE_RECORD_PATTERN_IS_"
    "EXERCISED_BOUNDED_NOTE_2026-09-04.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PROBE_REL = "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md"
Q8_REL = (
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)

AUDIT_INPUT_PATHS = (
    "docs/THE_DESIGNED_MATTER_LAW_IS_READ_FROM_RECORDS_ONLY_WHERE_ITS_ROLE_"
    "ALPHABET_REALISES_AN_ADJACENCY_THE_ROLE_TABLE_IS_BLIND_ON_95_PERCENT_OF_"
    "PARTIAL_ENTRIES_WHILE_EVERY_TWO_AND_THREE_SITE_RECORD_PATTERN_IS_"
    "EXERCISED_BOUNDED_NOTE_2026-09-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md",
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md",
)

assert AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL, PROBE_REL, Q8_REL)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL
PROBE_PATH = ROOT / PROBE_REL
Q8_PATH = ROOT / Q8_REL

CURRENT_INPUT_SHA256 = {'docs/THE_DESIGNED_MATTER_LAW_IS_READ_FROM_RECORDS_ONLY_WHERE_ITS_ROLE_ALPHABET_REALISES_AN_ADJACENCY_THE_ROLE_TABLE_IS_BLIND_ON_95_PERCENT_OF_PARTIAL_ENTRIES_WHILE_EVERY_TWO_AND_THREE_SITE_RECORD_PATTERN_IS_EXERCISED_BOUNDED_NOTE_2026-09-04.md': 'e91d69dd7f92176d7906f7b332fe9238f07a5ea366b41c197f72efcba5269357', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md': 'c277ca66054a47ac0183e1a7d806acf0fee01167915d8b70746125d73a5a56f4', 'docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md': 'c08d7a351c2ae40d921b0e996ca817b4f789c51072fbf2b6eb9a2de6f6fe8967'}

CELL_CAP = 16_000_000          # no dense array above 4096 x 4096 entries

# the one quoted row of the source computation (out_records.txt:15); every
# other number below is recomputed here
QUOTED_WINDOW_SWEEP_PINNING = 201
QUOTED_WINDOW_SWEEP_MINIMAL = 17

# ---- role alphabet (source block r5_common.py) -----------------------------
C0, C1, E, F, Q = 0, 1, 2, 3, 4
NAME = ("C0", "C1", "E", "F", "Q", "open")
ROLES = (C0, C1, E, F, Q)
OPEN = 5


def sat_decision(solver, **kwargs):
    """Only a proved SAT/UNSAT Boolean is a decision; unknown is not UNSAT."""
    value = solver.solve(**kwargs)
    if type(value) is not bool:
        raise RuntimeError("required solver returned no SAT/UNSAT decision")
    return value


def require_inputs():
    """Bind the actual text inputs, separately from their mathematical meaning."""
    import hashlib
    if set(CURRENT_INPUT_SHA256) != set(AUDIT_INPUT_PATHS):
        raise RuntimeError("declared/current input union differs")
    for rel, expected in CURRENT_INPUT_SHA256.items():
        if hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() != expected:
            raise RuntimeError("current input changed: " + rel)


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool,
              residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


# ---- the pattern (source block r5_common.py) -------------------------------
def pat_sym(site, ax: int) -> int:
    """Role of a fine site in the period-(4,2,2) pattern laid along `ax`."""
    odd = (site[0] & 1) + (site[1] & 1) + (site[2] & 1)
    if odd == 0:
        return C0 + ((site[ax] // 2) % 2)
    if odd == 1:
        return E
    if odd == 2:
        return F
    return Q


def pat_bit(site, ax: int):
    """Record value at a fine site; None on the free edge sites."""
    role = pat_sym(site, ax)
    if role == E:
        return None
    return 1 if role in (C1, Q) else 0


def proper_cubic_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            m = [[0, 0, 0] for _ in range(3)]
            for row in range(3):
                m[row][perm[row]] = signs[row]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                   - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                   + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1:
                out.append(tuple(tuple(r) for r in m))
    return tuple(out)


ROTATIONS = proper_cubic_rotations()
assert len(ROTATIONS) == 24


def act(m, v):
    return tuple(sum(m[i][k] * v[k] for k in range(3)) for i in range(3))


def transpose(m):
    return tuple(tuple(m[j][i] for j in range(3)) for i in range(3))


def axial(radius):
    return [tuple(s * radius * e for e in b)
            for b in ((1, 0, 0), (0, 1, 0), (0, 0, 1)) for s in (1, -1)]


NN = sorted(axial(1))
AX2 = sorted(NN + axial(2))


def rot_maps(support):
    index = {o: i for i, o in enumerate(support)}
    return [tuple(index[act(transpose(m), support[i])] for i in range(len(support)))
            for m in ROTATIONS]


def canon(profile, maps):
    return min(tuple(profile[m[i]] for i in range(len(profile))) for m in maps)


def realised_complete(support, ax=0):
    maps = rot_maps(support)
    base = set()
    for site in itertools.product(range(4), range(2), range(2)):
        role = pat_sym(site, ax)
        prof = tuple(pat_sym(tuple(site[k] + o[k] for k in range(3)), ax)
                     for o in support)
        base.add((role, prof))
    out = set()
    for role, prof in base:
        for m in maps:
            out.add((role, tuple(prof[m[i]] for i in range(len(support)))))
    return out


def realised_partial(support, ax=0):
    maps = rot_maps(support)
    n = len(support)
    out = set()
    for site in itertools.product(range(4), range(2), range(2)):
        role = pat_sym(site, ax)
        full = [pat_sym(tuple(site[k] + o[k] for k in range(3)), ax)
                for o in support]
        for mask in range(1 << n):
            prof = tuple(full[i] if (mask >> i) & 1 else OPEN for i in range(n))
            for m in maps:
                out.add((role, tuple(prof[m[i]] for i in range(n))))
    return out


def sites(box):
    return list(itertools.product(range(box[0]), range(box[1]), range(box[2])))


def neighbour_table(box, support):
    index = {s: i for i, s in enumerate(sites(box))}
    return [[index[tuple((s[k] + o[k]) % box[k] for k in range(3))]
             for o in support] for s in sites(box)]


def sector_role_configs(box):
    out = set()
    for ax in (0, 1, 2):
        period = [2, 2, 2]
        period[ax] = 4
        if any(box[i] % period[i] for i in range(3)):
            continue
        for shift in itertools.product(range(4), repeat=3):
            out.add(tuple(pat_sym(tuple(s[k] + shift[k] for k in range(3)), ax)
                          for s in sites(box)))
    return sorted(out)


def sector_templates(box):
    seen = {}
    for ax in (0, 1, 2):
        period = [2, 2, 2]
        period[ax] = 4
        if any(box[i] % period[i] for i in range(3)):
            continue
        for shift in itertools.product(range(4), repeat=3):
            cfg = tuple(pat_sym(tuple(s[k] + shift[k] for k in range(3)), ax)
                        for s in sites(box))
            seen.setdefault(cfg, (ax, shift))
    return sorted(seen.values())


def burnside_orbits(support, alphabet_size):
    maps = rot_maps(support)
    n = len(support)
    total = 0
    for m in maps:
        seen = [False] * n
        cycles = 0
        for i in range(n):
            if not seen[i]:
                cycles += 1
                j = i
                while not seen[j]:
                    seen[j] = True
                    j = m[j]
        total += alphabet_size ** cycles
    assert total % len(maps) == 0
    return total // len(maps)


def pair_orbits(pairs, support):
    maps = rot_maps(support)
    return {(r, canon(p, maps)) for r, p in pairs}


# ---- the two minimal covariant support tables ------------------------------
MAPS6 = rot_maps(NN)
TC = realised_complete(NN)
TP = realised_partial(NN)
ADJ = {(r, s) for r, p in TC for s in p}
BAD_ADJ = sorted(set(itertools.product(ROLES, ROLES)) - ADJ)
CROSS_BAD = sorted({tuple(sorted((r, s))) for r, s in BAD_ADJ if r != s})


def entry_type(r, P):
    """Source block r5_visibility.py: i -- every recorded symbol is a realised
    adjacency of r; ii -- some recorded symbol s != r is never adjacent to r;
    iii -- the only never-realised adjacency in P is r itself."""
    bad = {s for s in P if s != OPEN and (r, s) not in ADJ}
    if not bad:
        return "i"
    if bad - {r}:
        return "ii"
    return "iii"


def bad_set(r, P):
    return {s for s in P if s != OPEN and (r, s) not in ADJ}


def all_entries(partial):
    alphabet = 6 if partial else 5
    seen = set()
    out = []
    for P in itertools.product(range(alphabet), repeat=6):
        c = canon(P, MAPS6)
        if c in seen:
            continue
        seen.add(c)
        for r in ROLES:
            out.append((r, c))
    return out


def orbit_profiles(P):
    return sorted({tuple(P[m[i]] for i in range(6)) for m in MAPS6})


# ---- T2: solver-free admissible sets (source block r5_census.py C) ---------
def dfs_admissible(box, support, pairs):
    nb = neighbour_table(box, support)
    n = len(nb)
    by_role = {}
    for r, p in pairs:
        by_role.setdefault(r, []).append(p)
    involved = [[] for _ in range(n)]
    for u in range(n):
        involved[u].append(u)
        for j in nb[u]:
            if u not in involved[j]:
                involved[j].append(u)
    assign = [-1] * n
    found = []

    def ok(u):
        r = assign[u]
        if r == -1:
            return True
        for p in by_role.get(r, ()):
            good = True
            for i, j in enumerate(nb[u]):
                a = assign[j]
                if a != -1 and a != p[i]:
                    good = False
                    break
            if good:
                return True
        return False

    def rec(v):
        if v == n:
            found.append(tuple(assign))
            return
        for r in ROLES:
            assign[v] = r
            if all(ok(u) for u in involved[v]):
                rec(v + 1)
        assign[v] = -1

    rec(0)
    return found


def exercised_pairs(cfgs, box, support):
    nb = neighbour_table(box, support)
    out = set()
    for cfg in cfgs:
        for v in range(len(nb)):
            out.add((cfg[v], tuple(cfg[j] for j in nb[v])))
    return out


def partial_exercised(rc, nb):
    """Finite partial restrictions: all aliases of a site share its open status."""
    out = set()
    for v, neighbours in enumerate(nb):
        unique = sorted(set(neighbours))
        for mask in range(1 << len(unique)):
            recorded = {u for j, u in enumerate(unique) if (mask >> j) & 1}
            out.add((rc[v], tuple(rc[u] if u in recorded else OPEN for u in neighbours)))
    return out


# ---- T2: the excitations (source block r5_census.py D) ---------------------
W555 = [o for o in itertools.product(range(-2, 3), repeat=3)]


def torus_templates(box):
    out = []
    for ax, shift in sector_templates(box):
        pins, roles = {}, {}
        for s in sites(box):
            t = tuple(s[k] + shift[k] for k in range(3))
            pins[s] = pat_bit(t, ax)
            roles[s] = pat_sym(t, ax)
        out.append((ax, shift, pins, roles))
    return out


def role_from_records(cfg, box, templates):
    """R4 T4: the centre role is a function of the window's record values."""
    roles = []
    for s in sites(box):
        matched = set()
        for ax, shift, pins, troles in templates:
            good = True
            for o in W555:
                w = tuple((s[k] + o[k]) % box[k] for k in range(3))
                if pins[w] is not None and cfg[w] != pins[w]:
                    good = False
                    break
            if good:
                matched.add(troles[s])
        roles.append(matched)
    return roles


def excitation_families(box, templ):
    """Legacy keys sea/hop mean zero free-edge bits/single complements, not
    a quantum sea or guaranteed nonzero hopping. All double
    complements, and one representative of each vertex-parity class."""
    ax, shift, pins, roles = templ
    es = [s for s, v in pins.items() if v is None]
    base = {s: (pins[s] if pins[s] is not None else 0) for s in sites(box)}
    fam = {}

    def add(name, flips):
        cfg = dict(base)
        for s in flips:
            cfg[s] ^= 1
        fam.setdefault(name, []).append(cfg)

    add("sea", [])
    for e in es:
        add("hop", [e])
    for e1, e2 in itertools.combinations(es, 2):
        add("double", [e1, e2])
    corners = [s for s in sites(box) if roles[s] in (C0, C1)]
    star = {c: sorted({tuple((c[k] + d[k]) % box[k] for k in range(3))
                       for d in NN}) for c in corners}

    def parity(cfg):
        return tuple(sum(cfg[e] for e in star[c] if pins[e] is None) % 2
                     for c in corners)

    classes = {parity(base): base}
    frontier = [dict(base)]
    while frontier and len(classes) < 1 << (len(corners) - 1):
        nxt = []
        for cfg in frontier:
            for e in es:
                c2 = dict(cfg)
                c2[e] ^= 1
                p = parity(c2)
                if p not in classes:
                    classes[p] = c2
                    nxt.append(c2)
        frontier = nxt
    for _, cfg in sorted(classes.items()):
        fam.setdefault("parity class", []).append(cfg)
    return fam, corners, es


# ---- T3: visibility (source blocks r5_visibility.py, r5_witnesses.py) ------
class Instance:
    """CNF for: every recorded site realises a pair of T0 (or T0^p) or of
    orb(r, P); site 0 realises orb(r, P)."""

    def __init__(self, box, partial):
        self.partial = partial
        self.nb = neighbour_table(box, NN)
        self.n = len(self.nb)
        self.k = 6 if partial else 5
        self.nv = 0
        self.x = [[self.new() for _ in range(self.k)] for _ in range(self.n)]
        self.pairs = sorted(TC)
        clauses = []
        for v in range(self.n):
            clauses.append([self.x[v][a] for a in range(self.k)])
            for a in range(self.k):
                for b in range(a + 1, self.k):
                    clauses.append([-self.x[v][a], -self.x[v][b]])
        self.y = [[self.new() for _ in self.pairs] for _ in range(self.n)]
        for v in range(self.n):
            for kk, (rho, P) in enumerate(self.pairs):
                y = self.y[v][kk]
                clauses.append([-y, self.x[v][rho]])
                for i, j in enumerate(self.nb[v]):
                    if partial:
                        clauses.append([-y, self.x[j][P[i]], self.x[j][OPEN]])
                    else:
                        clauses.append([-y, self.x[j][P[i]]])
        self.base = clauses

    def new(self):
        self.nv += 1
        return self.nv

    def solve(self, solver_cls, r, P, want_model=False):
        clauses = list(self.base)
        top = self.nv
        variants = orbit_profiles(P)
        z = [[0] * len(variants) for _ in range(self.n)]
        for v in range(self.n):
            for jj, Pv in enumerate(variants):
                top += 1
                z[v][jj] = top
                clauses.append([-top, self.x[v][r]])
                for i, j in enumerate(self.nb[v]):
                    clauses.append([-top, self.x[j][Pv[i]]])
            clause = [self.y[v][kk] for kk in range(len(self.pairs))] + z[v]
            if self.partial:
                clause.append(self.x[v][OPEN])
            clauses.append(clause)
        clauses.append(z[0])
        with solver_cls(bootstrap_with=clauses) as s:
            ok = sat_decision(s)
            model = s.get_model() if (ok and want_model) else None
        if model is None:
            return ok, None
        ms = {lit for lit in model if lit > 0}
        cfg = []
        for v in range(self.n):
            for a in range(self.k):
                if self.x[v][a] in ms:
                    cfg.append(a)
        return ok, cfg


def dfs_visible(box, partial, r, P):
    """Solver-free: is some configuration admissible under T0 u orb(r, P)
    with site 0 realising orb(r, P)?  Depth-first search, forward checking."""
    nb = neighbour_table(box, NN)
    n = len(nb)
    k = 6 if partial else 5
    table = set(TP if partial else TC)
    variants = {(r, Pv) for Pv in orbit_profiles(P)}
    by_role, by_role0 = {}, {}
    for rr, pp in table | variants:
        by_role.setdefault(rr, []).append(pp)
    for rr, pp in variants:
        by_role0.setdefault(rr, []).append(pp)
    involved = [[] for _ in range(n)]
    for u in range(n):
        involved[u].append(u)
        for j in nb[u]:
            if u not in involved[j]:
                involved[j].append(u)
    assign = [-1] * n

    def ok(u):
        a = assign[u]
        if a == -1 or (partial and a == OPEN):
            return True
        cands = by_role0 if u == 0 else by_role
        for p in cands.get(a, ()):
            good = True
            for i, j in enumerate(nb[u]):
                b = assign[j]
                if b != -1 and b != p[i]:
                    good = False
                    break
            if good:
                return True
        return False

    def rec(v):
        if v == n:
            return True
        for a in range(k):
            if v == 0 and a != r:
                continue
            assign[v] = a
            if all(ok(u) for u in involved[v]):
                if rec(v + 1):
                    return True
        assign[v] = -1
        return False

    return rec(0)


def star_witness(box, r, P):
    """Source block r5_fibre.py: the all-else-open star of (r, P) on a torus
    with no side of length 2.  Returns the configuration when it certifies
    (r, P) visible -- admissible under T0^p u orb(r, P), using the entry --
    and None otherwise."""
    nb = neighbour_table(box, NN)
    cfg = [OPEN] * len(nb)
    cfg[0] = r
    for i, _ in enumerate(NN):
        j = nb[0][i]
        if P[i] != OPEN:
            if cfg[j] not in (OPEN, P[i]):
                return None
            cfg[j] = P[i]
    orb = {(r, Pv) for Pv in orbit_profiles(P)}
    used = False
    for v in range(len(nb)):
        if cfg[v] == OPEN:
            continue
        pair = (cfg[v], tuple(cfg[j] for j in nb[v]))
        if pair in TP:
            continue
        if pair in orb:
            used = True
            continue
        return None
    return cfg if used else None


def verify_witness(box, partial, r, P, cfg):
    """Scalar re-verification: admissible under T0 u orb(r, P), not under T0,
    and the entry is used (source block r5_witnesses.py)."""
    nb = neighbour_table(box, NN)
    table = TP if partial else TC
    orb = {(r, Pv) for Pv in orbit_profiles(P)}
    used = False
    for v in range(len(nb)):
        if partial and cfg[v] == OPEN:
            continue
        pair = (cfg[v], tuple(cfg[j] for j in nb[v]))
        if pair in table:
            continue
        if pair in orb:
            used = True
            continue
        return False
    return used


def reciprocal_certificate(r, P):
    """Source block r5_ax2_partial.py / results.md 3.1(B): a recorded symbol
    s != r at an offset the pattern never shows from r.  Any configuration
    realising (r, P) puts at that offset a site of role s whose own profile
    shows r at the reciprocal offset -- the same never-realised adjacency, so
    that site's entry is unexercised, and it cannot be orb(r, P) because its
    role is s != r.  Hence (r, P) is blind on every torus."""
    for i, s in enumerate(P):
        if s == OPEN or s == r:
            continue
        if (r, s) not in ADJ:
            return i, s
    return None


# ---- T3: the fibre (source block r5_fibre.py) ------------------------------
def best_order_bound(blind):
    best = (0, None)
    for order in itertools.permutations(ROLES):
        rank = {r: i for i, r in enumerate(order)}
        count = 0
        for r, P in blind:
            bs = bad_set(r, P)
            if bs and r not in bs and all(rank[s] > rank[r] for s in bs):
                count += 1
        if count > best[0]:
            best = (count, order)
    return best


def star_entry(r, s):
    P = tuple([s] + [OPEN] * 5)
    return (r, canon(P, MAPS6))


def realises_edge(box, ell, hub):
    r, P = ell
    nb = neighbour_table(box, NN)
    cfg = [OPEN] * len(nb)
    cfg[0] = r
    for i, _ in enumerate(NN):
        j = nb[0][i]
        if P[i] != OPEN:
            if cfg[j] not in (OPEN, P[i]):
                return False
            cfg[j] = P[i]
    allowed = set(TP)
    for rr, PP in (ell, hub):
        for Pv in orbit_profiles(PP):
            allowed.add((rr, Pv))
    used = False
    for v in range(len(nb)):
        if cfg[v] == OPEN:
            continue
        pair = (cfg[v], tuple(cfg[j] for j in nb[v]))
        if pair not in allowed:
            return False
        if pair not in TP:
            used = True
    return used


# ---- T3: the 12-offset law (source block r5_ax2_partial.py) ---------------
MAPS12 = rot_maps(AX2)
NN_SLOTS = [i for i, o in enumerate(AX2) if max(map(abs, o)) == 1]
AX_SLOTS = [i for i, o in enumerate(AX2) if max(map(abs, o)) == 2]


def burnside_restricted(alpha_nn, alpha_ax):
    total = 0
    for m in MAPS12:
        seen = [False] * 12
        c_nn = c_ax = 0
        for i in range(12):
            if not seen[i]:
                j = i
                while not seen[j]:
                    seen[j] = True
                    j = m[j]
                if i in NN_SLOTS:
                    c_nn += 1
                else:
                    c_ax += 1
        total += alpha_nn ** c_nn * alpha_ax ** c_ax
    assert total % 24 == 0
    return total // 24


# ---- T4: the record level (source blocks r5_records.py, r5_records4.py) ----
ORBIT_SEEDS = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0),
               (2, 1, 1), (2, 2, 0), (2, 2, 1), (2, 2, 2)]
ORBITS = [sorted({act(m, s) for m in ROTATIONS}) for s in ORBIT_SEEDS]
assert sum(len(o) for o in ORBITS) == 124


def window_from_mask(mask):
    w = [(0, 0, 0)]
    for i, ob in enumerate(ORBITS):
        if (mask >> i) & 1:
            w += ob
    return w


LADDER = {
    "star": 0b000000001,
    "NN+AX2": 0b000001001,
    "L1<=2": 0b000001011,
    "3x3x3": 0b000000111,
    "5x5x5": 0b111111111,
}
SMALLEST_CLOSING = 0b000011100     # historical identifier; inclusion-minimal witness, {(1,1,1), (2,0,0), (2,1,0)}, 39 offsets


def record_templates():
    out = []
    for ax in (0, 1, 2):
        for shift in itertools.product(range(4), range(2), range(2)):
            origin = [0, 0, 0]
            origin[ax] = shift[0]
            origin[(ax + 1) % 3] = shift[1]
            origin[(ax + 2) % 3] = shift[2]
            out.append((ax, tuple(origin)))
    return out


TEMPLATES = record_templates()
assert len(TEMPLATES) == 48


def template_window(window, ax, origin):
    pins = {}
    for o in window:
        v = pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
        if v is not None:
            pins[o] = v
    return pins


def marker_clauses(box, window, exact=False):
    grid = sites(box)
    idx = {s: i for i, s in enumerate(grid)}
    clauses = []
    nxt = len(grid) + 1
    markers = []
    for s in grid:
        ms = []
        for ax, origin in TEMPLATES:
            demand, ok = {}, True
            for o in window:
                v = pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
                if v is None:
                    continue
                u = idx[tuple((s[k] + o[k]) % box[k] for k in range(3))]
                if demand.get(u, v) != v:
                    ok = False
                    break
                demand[u] = v
            if not ok:
                continue
            m = nxt
            nxt += 1
            ms.append(m)
            lits = [(u + 1) if v == 1 else -(u + 1) for u, v in demand.items()]
            for lit in lits:
                clauses.append([-m, lit])
            if exact:
                clauses.append([m] + [-lit for lit in lits])
        markers.append(ms)
    return clauses, markers, nxt, grid, idx


def cylinder_clauses(box, grid):
    out = []
    for ax, origin in TEMPLATES:
        period = [2, 2, 2]
        period[ax] = 4
        if any(box[i] % period[i] for i in range(3)):
            continue
        clause = []
        for i, s in enumerate(grid):
            v = pat_bit(tuple(s[k] + origin[k] for k in range(3)), ax)
            if v is not None:
                clause.append(-(i + 1) if v == 1 else (i + 1))
        out.append(clause)
    return out


def window_pins(solver_cls, box, window):
    clauses, markers, _, grid, _ = marker_clauses(box, window)
    for ms in markers:
        clauses.append(ms)
    clauses.extend(cylinder_clauses(box, grid))
    with solver_cls(bootstrap_with=clauses) as s:
        return not sat_decision(s)


def enumerate_422(window):
    """R4's solver-free path on 4x2x2 (source block r5_records.py R2)."""
    box = (4, 2, 2)
    grid = sites(box)
    idx = {s: i for i, s in enumerate(grid)}
    n = len(grid)
    assert (1 << n) * n <= CELL_CAP
    bits = ((np.arange(1 << n, dtype=np.int64)[:, None]
             >> np.arange(n)) & 1).astype(np.int8)
    adm = np.ones(1 << n, dtype=bool)
    for s in grid:
        matched = np.zeros(1 << n, dtype=bool)
        for ax, origin in TEMPLATES:
            demand, ok = {}, True
            for o in window:
                v = pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
                if v is None:
                    continue
                u = idx[tuple((s[k] + o[k]) % box[k] for k in range(3))]
                if demand.get(u, v) != v:
                    ok = False
                    break
                demand[u] = v
            if not ok:
                continue
            hit = np.ones(1 << n, dtype=bool)
            for u, v in demand.items():
                hit &= bits[:, u] == v
            matched |= hit
        adm &= matched
    outside = np.ones(1 << n, dtype=bool)
    for ax, origin in TEMPLATES:
        period = [2, 2, 2]
        period[ax] = 4
        if any(box[i] % period[i] for i in range(3)):
            continue
        cyl = np.ones(1 << n, dtype=bool)
        for i, s in enumerate(grid):
            v = pat_bit(tuple(s[k] + origin[k] for k in range(3)), ax)
            if v is not None:
                cyl &= bits[:, i] == v
        outside &= ~cyl
    return int(adm.sum()), int((adm & outside).sum())


def k_min(solver_cls, card_enc, enc_type, box, window, kmax):
    clauses, markers, nxt, _, _ = marker_clauses(box, window, exact=True)
    viol = []
    for ms in markers:
        w = nxt
        nxt += 1
        viol.append(w)
        clauses.append([w] + ms)
        for m in ms:
            clauses.append([-w, -m])
    for k in range(1, kmax + 1):
        card = card_enc.equals(lits=viol, bound=k, top_id=nxt,
                               encoding=enc_type)
        with solver_cls(bootstrap_with=clauses + card.clauses) as s:
            if sat_decision(s):
                return k
    return None


def main() -> int:                                          # noqa: C901
    t0 = time.time()
    checks = Checks()
    require_inputs()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    probe = PROBE_PATH.read_text(encoding="utf-8")
    law_pair = Q8_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    try:
        from pysat.card import CardEnc, EncType
        from pysat.solvers import Cadical153
        have_sat = True
    except Exception:
        CardEnc = EncType = Cadical153 = None
        have_sat = False
        raise RuntimeError("complete claim coverage requires CaDiCaL")

    print("external_scientific_inputs: none; recomputed here bar the declared "
          "quoted rows")
    print("integrity_reads: axioms, deep probe, law pair, this note")
    print("construction: exact enumeration over roles and over binary records")
    print("negative_scope: finite blindness statements on the named tori")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("interpretation_guard: minimal_axioms Lattice, Qubit, "
          "Admissibility, Record")
    print("declared_math: cubic rotations, role subshifts, binary record "
          "windows, Burnside counts")
    print("unverified_historical_rows: the 201/17 totals of the 512-window sweep")
    if have_sat:
        print("solver_mode: pysat present; CaDiCaL on 4x2x2, 4x4x2, 4x4x4, "
              "8x4x4, and the solver-free search on 4x2x2")
    else:
        print("solver_mode: pysat absent; the solver-free search decides every "
              "entry of 4x2x2 and the CaDiCaL rows are not run")

    checks.check("audit-input-paths", "declared inputs exist and are unique",
                 all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS)
                 and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)))
    checks.check("audit-timeout", "the declared timeout is 300 seconds",
                 AUDIT_TIMEOUT_SEC == 300)

    # ---------- supplied surface -------------------------------------------
    checks.check(
        "axiom-admissibility", "the one fixed nearest-neighbor rule is quoted",
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations." in axiom_flat
        and "one fixed nearest-neighbor admissibility rule" in note_flat)
    checks.check(
        "axiom-support", "admissible read as the support",
        "denotes its support -- on finite menus, exactly the possibilities of "
        "nonzero probability" in axiom_flat
        and "denotes its support" in note_flat)
    checks.check(
        "axiom-record", "only records are readable is quoted",
        "Only records are readable. A readout value is determined by record "
        "content alone." in axiom_flat
        and "Only records are readable" in note_flat)
    checks.check(
        "parent-deep-probe", "the declared historical deep-probe comparator is present",
        "number of covariant label-equivariant tables = 3^24" in probe)
    checks.check(
        "parent-law-pair", "the conditional law-pair boundary is present",
        "claim_type: bounded_theorem" in law_pair
        and "It selects neither rule as the framework's physical law."
        in normalize(law_pair))

    # ---------- T1 : the census --------------------------------------------
    prof_c = {p for _, p in TC}
    orb_c = {canon(p, MAPS6) for p in prof_c}
    ent_c = pair_orbits(TC, NN)
    n_orb5 = burnside_orbits(NN, 5)
    prof_p = {p for _, p in TP}
    orb_p = {canon(p, MAPS6) for p in prof_p}
    ent_p = pair_orbits(TP, NN)
    n_orb6 = burnside_orbits(NN, 6)
    checks.check(
        "T1-complete", "18 pairs, 17 of 15,625 profiles, 6 of 800 orbits",
        (len(TC), len(prof_c), len(orb_c), n_orb5, 5 ** 6) == (18, 17, 6, 800, 15625))
    checks.check(
        "T1-partial", "794 pairs, 655 of 46,656, 61 of 2,226 = 2.74 %",
        (len(TP), len(prof_p), len(orb_p), n_orb6, 6 ** 6)
        == (794, 655, 61, 2226, 46656)
        and abs(len(orb_p) / n_orb6 - 0.0274) < 0.0001)
    by_c = {NAME[r]: sum(1 for rr, _ in ent_c if rr == r) for r in ROLES}
    by_p = {NAME[r]: sum(1 for rr, _ in ent_p if rr == r) for r in ROLES}
    checks.check(
        "T1-entries", "7 of 4,000 complete and 84 of 11,130 partial entries",
        (len(ent_c), 5 * n_orb5, len(ent_p), 5 * n_orb6) == (7, 4000, 84, 11130)
        and by_c == {"C0": 1, "C1": 1, "E": 3, "F": 1, "Q": 1}
        and by_p == {"C0": 10, "C1": 10, "E": 36, "F": 18, "Q": 10})
    union = set()
    for ax in (0, 1, 2):
        for site in itertools.product(range(4), repeat=3):
            union.add((pat_sym(site, ax),
                       tuple(pat_sym(tuple(site[k] + o[k] for k in range(3)), ax)
                             for o in NN)))
    checks.check("T1-covariance", "rotation closure equals the union of local template pairs",
                 TC == union)
    tc12 = realised_complete(AX2)
    tp12 = realised_partial(AX2)
    ent_c12 = pair_orbits(tc12, AX2)
    ent_p12 = pair_orbits(tp12, AX2)
    n12c, n12p = burnside_orbits(AX2, 5), burnside_orbits(AX2, 6)
    checks.check(
        "T1-12-offset", "22 pairs, 7 of 10,229,375, 3,404 of 454,664,880",
        (len(tc12), len(ent_c12), n12c, len(tp12), len(ent_p12), 5 * n12p)
        == (22, 7, 10229375, 65792, 3404, 454664880))

    # ---------- T2 : the exercised set is the law ---------------------------
    boxes = ((4, 2, 2), (4, 4, 2), (4, 4, 4))
    adm_nn, adm_12, sec_n, ex_nn = {}, {}, {}, {}
    for box in boxes:
        a6 = dfs_admissible(box, NN, TC)
        a12 = dfs_admissible(box, AX2, tc12)
        sec = sector_role_configs(box)
        adm_nn[box], adm_12[box], sec_n[box] = len(a6), set(a12) == set(sec), len(sec)
        ex_nn[box] = exercised_pairs(a6, box, NN)
    checks.check(
        "T2-admissible", "NN admits 32 / 128 / 2,048; 12 offsets = the sectors",
        [adm_nn[b] for b in boxes] == [32, 128, 2048]
        and all(adm_12[b] for b in boxes)
        and [sec_n[b] for b in boxes] == [16, 32, 48])
    checks.check(
        "T2-law", "the 2,048 admissible configurations exercise exactly T0",
        ex_nn[(4, 4, 4)] == TC
        and all(ex_nn[b] <= TC for b in boxes)
        and (len(ex_nn[(4, 2, 2)]), len(ex_nn[(4, 4, 2)])) == (14, 16))
    nb444 = neighbour_table((4, 4, 4), NN)
    ex_sec_p = set()
    for rc in sector_role_configs((4, 4, 4)):
        ex_sec_p |= partial_exercised(rc, nb444)
    checks.check(
        "T2-partial-law", "the sectors' sub-configurations exercise exactly T0^p",
        ex_sec_p == TP and len(pair_orbits(ex_sec_p, NN)) == 84)
    alias_entry_counts = {}
    for box in boxes:
        actual = set()
        for rc in sector_role_configs(box):
            actual |= partial_exercised(rc, neighbour_table(box, NN))
        alias_entry_counts[box] = len(pair_orbits(actual, NN))
    checks.check("C-aliased-exercised", "58/77/84 realizable partial entry orbits",
                 [alias_entry_counts[b] for b in boxes] == [58, 77, 84], alias_entry_counts)
    templ422 = torus_templates((4, 2, 2))
    nb422 = neighbour_table((4, 2, 2), NN)
    roles422, ex422, n422 = set(), set(), 0
    unique422 = True
    for ax, shift, pins, troles in templ422:
        es = [s for s, v in pins.items() if v is None]
        for fill in itertools.product((0, 1), repeat=len(es)):
            cfg = dict(pins)
            for e, b in zip(es, fill):
                cfg[e] = b
            rr = role_from_records(cfg, (4, 2, 2), templ422)
            if any(len(x) != 1 for x in rr):
                unique422 = False
                continue
            rc = tuple(next(iter(x)) for x in rr)
            roles422.add(rc)
            for v in range(len(nb422)):
                ex422.add((rc[v], tuple(rc[j] for j in nb422[v])))
            n422 += 1
    checks.check(
        "T2-cylinders", "all 1,024 cylinder configurations read to the 16 sectors",
        n422 == 1024 and unique422
        and roles422 == set(sector_role_configs((4, 2, 2)))
        and len(ex422) == 12)
    templ444 = torus_templates((4, 4, 4))
    fam, corners, es444 = excitation_families((4, 4, 4), templ444[0])
    fam_sizes = {k: len(v) for k, v in fam.items()}
    fam_roles, fam_ex = {}, {}
    for name, cfgs in fam.items():
        rcs, ex = set(), set()
        for cfg in cfgs:
            rr = role_from_records(cfg, (4, 4, 4), templ444)
            if any(len(x) != 1 for x in rr):
                rcs.add(None)
                continue
            rc = tuple(next(iter(x)) for x in rr)
            rcs.add(rc)
            for v in range(len(nb444)):
                ex.add((rc[v], tuple(rc[j] for j in nb444[v])))
        fam_roles[name] = rcs
        fam_ex[name] = ex
    checks.check(
        "T2-excitations",
        "zero-bit, single/double complements, 128 parity classes: one role configuration each",
        fam_sizes == {"sea": 1, "hop": 24, "double": 276, "parity class": 128}
        and all(len(v) == 1 and None not in v for v in fam_roles.values())
        and all(len(fam_ex[k]) == 12 for k in fam_ex))
    census = {n: math.comb(len(corners), n) * 2 ** (len(es444) - len(corners) + 1)
              for n in range(0, len(corners) + 1, 2)}
    checks.check(
        "T2-cylinder-count", "48 x 2^24 = 805,306,368 edge-bit assignments",
        len(templ444) * 2 ** len(es444) == 805306368
        and (len(corners), len(es444)) == (8, 24)
        and sum(census.values()) == 2 ** 24
        and census == {0: 131072, 2: 3670016, 4: 9175040, 6: 3670016,
                       8: 131072})
    union_ex = set()
    for ex in fam_ex.values():
        union_ex |= ex
    checks.check(
        "T2-union-growth", "union growth of the exercised set is zero",
        union_ex == fam_ex["sea"] and len(union_ex) == 12)
    one = sector_role_configs((4, 4, 4))[0]
    pairs_one = {(one[v], tuple(one[j] for j in nb444[v]))
                 for v in range(len(nb444))}
    checks.check(
        "T2-one-sector", "one sector realises all 7 complete entries",
        len(pairs_one) == 12 and pair_orbits(pairs_one, NN) == ent_c)
    checks.check(
        "T2-cover", "2 to 84 partial configurations cover the 84 entries",
        -(-len(ent_p) // 64) == 2 and len(ent_p) == 84)

    # ---------- T3 : the reading theorem ------------------------------------
    checks.check(
        "T3-adjacency", "17 of 25 ordered role adjacencies never realised",
        len(BAD_ADJ) == 17 and len(ADJ) == 8
        and all((s, r) in ADJ for r, s in ADJ)
        and len(CROSS_BAD) == 6)
    unex, types = {}, {}
    for partial in (False, True):
        ex = ent_p if partial else ent_c
        unex[partial] = [(r, P) for r, P in all_entries(partial)
                         if (r, P) not in ex]
        types[partial] = {}
        for r, P in unex[partial]:
            types[partial].setdefault(entry_type(r, P), []).append((r, P))
    checks.check(
        "T3-types", "11,046 and 3,993 unexercised entries; 9,919 type ii",
        (len(unex[True]), len(unex[False])) == (11046, 3993)
        and [len(types[True][t]) for t in "i ii iii".split()] == [243, 9919, 884]
        and [len(types[False][t]) for t in "i ii iii".split()] == [63, 3673, 257])
    recip_ok = all(reciprocal_certificate(r, P) is not None
                   for t in ("ii",) for r, P in types[True][t])
    recip_ok &= all(reciprocal_certificate(r, P) is not None
                    for r, P in types[False]["ii"])
    recip_ok &= all(reciprocal_certificate(r, P) is None
                    for t in ("i", "iii") for r, P in types[True][t])
    checks.check(
        "T3-reciprocal",
        "the reciprocal obstruction certifies 13,592 entries blind everywhere",
        recip_ok and len(types[True]["ii"]) + len(types[False]["ii"]) == 13592)

    # the star certificate: solver-free visibility on a torus with no side 2
    stars = {}
    for r, P in types[True]["i"]:
        stars[(r, P)] = star_witness((4, 4, 4), r, P)
    n_star = sum(1 for v in stars.values() if v is not None)
    checks.check(
        "T3-star-certificate",
        "243 type-i entries visible by an explicit star on 4x4x4",
        n_star == 243)

    # the solver-free search on the smallest torus: every type-i and type-iii
    # entry of 4x2x2 decided by depth-first search, every type-ii entry by the
    # reciprocal obstruction, so all 15,039 entries are decided without a solver
    dfs_dec = {}
    for partial in (False, True):
        dfs_dec[partial] = {(r, P): dfs_visible((4, 2, 2), partial, r, P)
                            for r, P in types[partial]["i"] + types[partial]["iii"]}
        for r, P in types[partial]["ii"]:
            dfs_dec[partial][(r, P)] = False
    dfs_vis = {p: sum(dfs_dec[p].values()) for p in (False, True)}
    checks.check(
        "T3-solver-free",
        "all 15,039 entries of 4x2x2 decided without a solver: 12 and 136 seen",
        len(dfs_dec[False]) + len(dfs_dec[True]) == 15039
        and (dfs_vis[False], dfs_vis[True]) == (12, 136))

    vis_444_partial = {e for e, v in stars.items() if v is not None}
    witnesses = {e: v for e, v in stars.items() if v is not None}
    sat_counts, sat_vis = {}, {}
    if have_sat:
        for box in boxes:
            for partial in (False, True):
                inst = Instance(box, partial)
                todo = types[partial]["i"] + types[partial]["iii"]
                if box == (4, 4, 4) and partial:
                    todo = types[partial]["iii"]
                res = {}
                for r, P in todo:
                    ok, cfg = inst.solve(Cadical153, r, P,
                                         want_model=(box == (4, 4, 4)))
                    res[(r, P)] = ok
                    if ok and box == (4, 4, 4):
                        if partial:
                            witnesses[(r, P)] = cfg
                            vis_444_partial.add((r, P))
                        else:
                            witnesses[("c", r, P)] = cfg
                sat_counts[(box, partial)] = sum(res.values())
                sat_vis[(box, partial)] = {e for e, v in res.items() if v}
                if box == (4, 2, 2):
                    agree = all(res[e] == dfs_dec[partial][e] for e in res)
                    checks.check(
                        f"T3-agree-{'partial' if partial else 'complete'}",
                        "CaDiCaL and the solver-free search agree on 4x2x2",
                        agree)
        checks.check(
            "T3-visible-444",
            "partial 4x4x4: 84 exercised, 435 visible, 10,611 blind = 95.34 %",
            n_star + sat_counts[((4, 4, 4), True)] == 435
            and 11046 - 435 == 10611
            and abs(10611 / 11130 - 0.9534) < 0.0001)
        checks.check(
            "T3-complete-444", "complete 4x4x4: 18 visible, 3,975 blind",
            sat_counts[((4, 4, 4), False)] == 18 and 3993 - 18 == 3975)
        checks.check(
            "T3-torus-442", "4x4x2: 286 visible partial, 12 complete",
            sat_counts[((4, 4, 2), True)] == 286
            and sat_counts[((4, 4, 2), False)] == 12)
        checks.check(
            "T3-torus-422", "4x2x2: 136 visible partial, 12 complete",
            sat_counts[((4, 2, 2), True)] == 136
            and sat_counts[((4, 2, 2), False)] == 12)
        wit_p = {k: v for k, v in witnesses.items() if len(k) == 2}
        wit_c = {k: v for k, v in witnesses.items() if len(k) == 3}
        cross = [(True, e) for e in types[True]["ii"]
                 if sum(1 for x in e[1] if x != OPEN) <= 2]
        cross += [(False, (r, (s,) * 6)) for r in ROLES for s in ROLES
                  if (r, s) not in ADJ and r != s]
        inst_p = Instance((4, 4, 4), True)
        inst_c = Instance((4, 4, 4), False)
        cross_ok = not any(
            (inst_p if partial else inst_c).solve(Cadical153, r, P)[0]
            for partial, (r, P) in cross)
        checks.check(
            "T3-type-ii-solved",
            "CaDiCaL finds the 124 declared type-ii entries blind on 4x4x4",
            cross_ok and len(cross) == 124)
        checks.check(
            "T3-witnesses", "435 partial and 18 complete witnesses re-verified",
            len(wit_p) == 435 and len(wit_c) == 18
            and all(verify_witness((4, 4, 4), True, r, P, cfg)
                    for (r, P), cfg in wit_p.items())
            and all(verify_witness((4, 4, 4), False, r, P, cfg)
                    for (_, r, P), cfg in wit_c.items()))
        blind_444 = set(unex[True]) - vis_444_partial
        blind_422 = {e for e, v in dfs_dec[True].items() if not v}
        checks.check(
            "T3-never-shrinks",
            "the blind addition set shrinks by 299 from 4x2x2 to 4x4x4",
            blind_444 <= blind_422 and len(blind_422 - blind_444) == 299
            and len(blind_444) == 10611)
        blind_c444 = set(unex[False]) - sat_vis[((4, 4, 4), False)]
        checks.check(
            "T3-fibre-lower", "certified lower bounds 2^1580 and 2^478",
            best_order_bound(blind_444)[0] == 1580
            and best_order_bound(blind_c444)[0] == 478
            and len(blind_c444) == 3975)
        hubs, leaves, factor, edges_ok, edges = set(), 0, 0.0, 0, 0
        integer_factor, star_sizes, used_vertices = 1, [], set()
        for r, s in CROSS_BAD:
            h_rs, h_sr = star_entry(r, s), star_entry(s, r)
            hubs |= {h_rs, h_sr}
            a_rs = [(rr, P) for rr, P in blind_444
                    if rr == r and bad_set(rr, P) == {s} and (rr, P) != h_rs]
            a_sr = [(rr, P) for rr, P in blind_444
                    if rr == s and bad_set(rr, P) == {r} and (rr, P) != h_sr]
            for ell in a_rs:
                edges += 1
                edges_ok += realises_edge((4, 4, 4), ell, h_sr)
            for ell in a_sr:
                edges += 1
                edges_ok += realises_edge((4, 4, 4), ell, h_rs)
            edges += 1
            edges_ok += realises_edge((4, 4, 4), h_rs, h_sr)
            vertices = {h_rs, h_sr} | set(a_rs) | set(a_sr)
            assert not (vertices & used_vertices)
            used_vertices |= vertices
            a, b = len(a_rs), len(a_sr)
            star_sizes.append((a, b))
            integer_factor *= (1 << a) + (1 << b) + (1 << (a + b))
            leaves += a + b
            factor += math.log2(2 ** a + 2 ** b + 2 ** (a + b))
        ub = factor + (len(blind_444) - len(hubs) - leaves)
        free_vertices = len(blind_444) - len(hubs) - leaves
        integer_upper = (1 << free_vertices) * integer_factor
        print(f"fibre_exact_upper_integer: {integer_upper}")
        print(f"historical_rounded_log2_diagnostic: {ub}; not an exact exponent bound")
        checks.check(
            "T3-fibre-upper", "exact integer product lies between 2^10599 and 2^10600",
            edges == edges_ok == 1343 and len(hubs) == 12 and leaves == 1337
            and free_vertices == 9262
            and star_sizes == [(46, 46), (46, 182), (46, 46), (46, 182), (46, 46), (559, 46)]
            and (1 << 10599) < integer_upper < (1 << 10600))
    else:
        checks.check("T3-solver-rows",
                     "CaDiCaL rows are not run without pysat", True)

    # ---------- T3 : the 12-offset law --------------------------------------
    good = {r: {1: set(), 2: set()} for r in ROLES}
    for r, p in tc12:
        for i, s in enumerate(p):
            good[r][1 if i in NN_SLOTS else 2].add(s)
    type_ii_12 = 0
    rest12 = {}
    for r in ROLES:
        n_rest = burnside_restricted(len(good[r][1] | {r, OPEN}),
                                     len(good[r][2] | {r, OPEN}))
        rest12[r] = n_rest
        type_ii_12 += n12p - n_rest
    checks.check(
        "T3-12-type-ii", "454,560,782 of 454,664,880 blind everywhere = 99.977 %",
        type_ii_12 == 454560782 and sum(rest12.values()) == 104098
        and abs(type_ii_12 / (5 * n12p) - 0.999771) < 1e-6)
    bad12 = {r: {1: set(ROLES) - good[r][1], 2: set(ROLES) - good[r][2]}
             for r in ROLES}
    ex12 = set(ent_p12)

    def star_visible_12(r, P):
        cfg = {(0, 0, 0): r}
        for i, o in enumerate(AX2):
            if P[i] != OPEN:
                cfg[o] = P[i]
        orb = {tuple(P[m[i]] for i in range(12)) for m in MAPS12}
        used = False
        for site, role in cfg.items():
            prof = tuple(cfg.get(tuple(site[k] + o[k] for k in range(3)), OPEN)
                         for o in AX2)
            if (role, prof) in tp12:
                continue
            if role == r and prof in orb:
                used = True
                continue
            return False
        return used

    def forced_blind_12(r, P):
        cfg = {(0, 0, 0): r}
        for i, o in enumerate(AX2):
            if P[i] != OPEN:
                cfg[o] = P[i]
        for site, role in cfg.items():
            if site == (0, 0, 0) or role == r:
                continue
            for o in AX2:
                w = tuple(site[k] + o[k] for k in range(3))
                if w in cfg:
                    cls = 1 if max(map(abs, o)) == 1 else 2
                    if cfg[w] in bad12[role][cls]:
                        return True
        return False

    tally = {"exercised": 0, "star-visible": 0, "forced-blind": 0,
             "undecided": 0}
    for r in ROLES:
        alpha_nn = sorted(good[r][1] | {r, OPEN})
        alpha_ax = sorted(good[r][2] | {r, OPEN})
        seen = set()
        for nnv in itertools.product(alpha_nn, repeat=6):
            for axv in itertools.product(alpha_ax, repeat=6):
                P = [OPEN] * 12
                for k, i in enumerate(NN_SLOTS):
                    P[i] = nnv[k]
                for k, i in enumerate(AX_SLOTS):
                    P[i] = axv[k]
                c = canon(tuple(P), MAPS12)
                if c in seen:
                    continue
                seen.add(c)
                if (r, c) in ex12:
                    tally["exercised"] += 1
                elif star_visible_12(r, c):
                    tally["star-visible"] += 1
                elif forced_blind_12(r, c):
                    tally["forced-blind"] += 1
                else:
                    tally["undecided"] += 1
        assert len(seen) == rest12[r]
    forced_total = tally["forced-blind"]
    blind12 = type_ii_12 + forced_total
    checks.check(
        "T3-12-census", "the 104,098 remaining entries: 3,404 of them exercised",
        tally == {"exercised": 3404, "star-visible": 7627,
                  "forced-blind": 76734, "undecided": 16333}
        and sum(tally.values()) == 104098)
    checks.check(
        "T3-12-blind", "the pinning law is blind on 99.994 % of its entries",
        blind12 == 454637516
        and round(100 * blind12 / (5 * n12p), 3) == 99.994)

    # ---------- T4 : records only -------------------------------------------
    ladder_counts = {}
    for name, mask in LADDER.items():
        window = window_from_mask(mask)
        tw = [template_window(window, ax, o) for ax, o in TEMPLATES]
        consistent = sum(
            1 for a in range(48) for b in range(a + 1, 48)
            if all(tw[a][o] == tw[b][o] for o in tw[a] if o in tw[b]))
        if len(window) <= 27:
            seen = set()
            for pins in tw:
                free = [o for o in window if o not in pins]
                for fill in itertools.product((0, 1), repeat=len(free)):
                    pat = dict(pins)
                    pat.update(zip(free, fill))
                    seen.add(tuple(pat[o] for o in window))
            ladder_counts[name] = (consistent, len(seen), len(window))
        else:
            ladder_counts[name] = (
                consistent, sum(2 ** (len(window) - len(p)) for p in tw),
                len(window))
    ex555 = ladder_counts["5x5x5"][1]
    free555 = sorted({125 - len(template_window(window_from_mask(LADDER["5x5x5"]),
                                                ax, o))
                      for ax, o in TEMPLATES})
    checks.check(
        "T4-cylinders", "the 48 cylinders are disjoint on 5x5x5: 2^57.05 of 2^125",
        ladder_counts["5x5x5"][0] == 0
        and ex555 == 148935859368886272
        and abs(math.log2(ex555) - 57.05) < 0.01
        and free555 == [36, 44, 51, 54])
    checks.check(
        "T4-record-table", "star 128 of 128, 3x3x3 101,626 of 2^27",
        ladder_counts["star"][1] == 128
        and ladder_counts["NN+AX2"][1] == 1638
        and ladder_counts["L1<=2"][1] == 391233
        and ladder_counts["3x3x3"][1] == 101626)
    row422 = [enumerate_422(window_from_mask(LADDER[n]))
              for n in ("star", "NN+AX2", "L1<=2", "3x3x3", "5x5x5")]
    checks.check(
        "T4-ladder-422", "outside every cylinder 64,512 / 13,981 / 186 / 154 / 0",
        [o for _, o in row422] == [64512, 13981, 186, 154, 0]
        and [a for a, _ in row422] == [65536, 15005, 1210, 1178, 1024])
    w39 = window_from_mask(SMALLEST_CLOSING)
    checks.check(
        "T4-window-39",
        "the declared closing window has 39 positions and no nearest neighbour",
        len(w39) == 39 and (1, 0, 0) not in w39
        and sorted(ORBIT_SEEDS[i] for i in range(9)
                   if (SMALLEST_CLOSING >> i) & 1)
        == [(1, 1, 1), (2, 0, 0), (2, 1, 0)])
    if have_sat:
        subs = [SMALLEST_CLOSING & ~(1 << i) for i in range(9)
                if (SMALLEST_CLOSING >> i) & 1]
        checks.check(
            "T4-window-pins", "it pins on 4x4x4 and again on 8x4x4",
            window_pins(Cadical153, (4, 4, 4), w39)
            and window_pins(Cadical153, (8, 4, 4), w39))
        checks.check(
            "T4-window-minimal",
            "each maximal proper rotation-closed sub-window fails to pin",
            not any(window_pins(Cadical153, (4, 4, 4), window_from_mask(m))
                    for m in subs))
        checks.check(
            "T4-ladder-pins", "of the ladder only 5x5x5 pins on 4x4x4",
            [window_pins(Cadical153, (4, 4, 4), window_from_mask(LADDER[n]))
             for n in ("star", "NN+AX2", "L1<=2", "3x3x3", "5x5x5")]
            == [False, False, False, False, True])
        checks.check(
            "T4-sweep-quoted", "historical unverified sweep quotation preserved: 201/512 and 17",
            (QUOTED_WINDOW_SWEEP_PINNING, QUOTED_WINDOW_SWEEP_MINIMAL)
            == (201, 17) and QUOTED_WINDOW_SWEEP_MINIMAL <= 512)
        km5 = k_min(Cadical153, CardEnc, EncType.seqcounter, (8, 4, 4),
                    window_from_mask(LADDER["5x5x5"]), 6)
        km3 = k_min(Cadical153, CardEnc, EncType.seqcounter, (8, 4, 4),
                    window_from_mask(LADDER["3x3x3"]), 6)
        checks.check(
            "T4-kmin", "k_min > 6 on 8x4x4 for 5x5x5, and 1 for 3x3x3",
            km5 is None and km3 == 1)
    tw555 = [template_window(W555, ax, o) for ax, o in TEMPLATES]

    def exercised_pattern(pattern):
        for pins in tw555:
            if all(pins.get(o, v) == v for o, v in pattern.items()):
                return True
        return False

    two, two_ok = 0, 0
    for o in W555:
        if o == (0, 0, 0):
            continue
        for a in (0, 1):
            for b in (0, 1):
                two += 1
                two_ok += exercised_pattern({(0, 0, 0): a, o: b})
    checks.check("T4-two-site", "496 of 496 two-record patterns exercised",
                 (two, two_ok) == (496, 496))
    offs = [o for o in W555 if o != (0, 0, 0)]
    three, three_ok = 0, 0
    for o1, o2 in itertools.combinations(offs, 2):
        for a, b, c in itertools.product((0, 1), repeat=3):
            three += 1
            three_ok += exercised_pattern({(0, 0, 0): a, o1: b, o2: c})
    checks.check("T4-three-site", "61,008 of 61,008 three-record patterns",
                 (three, three_ok) == (61008, 61008))
    wi = {o: i for i, o in enumerate(W555)}
    pin = np.full((48, 125), -1, dtype=np.int8)
    for t, (ax, origin) in enumerate(TEMPLATES):
        for i, o in enumerate(W555):
            v = pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
            if v is not None:
                pin[t, i] = v
    vals = np.array(list(itertools.product((0, 1), repeat=4)), dtype=np.int8)

    def single_ok(pattern):
        for t in range(48):
            if all(pin[t, wi[o]] in (-1, v) for o, v in pattern.items()):
                return True
        return False

    tot4 = ex4 = vis4 = und4 = 0
    for o1, o2, o3 in itertools.combinations(offs, 3):
        idx = [wi[(0, 0, 0)], wi[o1], wi[o2], wi[o3]]
        pins = pin[:, idx]
        ok = np.ones((48, 16), dtype=bool)
        for j in range(4):
            pj = pins[:, j][:, None]
            ok &= (pj == -1) | (pj == vals[:, j][None, :])
        ok = ok.any(axis=0)
        tot4 += 16
        ex4 += int(ok.sum())
        for kk in np.nonzero(~ok)[0]:
            recs = {(0, 0, 0): int(vals[kk][0]), o1: int(vals[kk][1]),
                    o2: int(vals[kk][2]), o3: int(vals[kk][3])}
            good4 = True
            for s in (o1, o2, o3):
                pat = {}
                for w, v in recs.items():
                    rel = tuple(w[m] - s[m] for m in range(3))
                    if max(map(abs, rel)) <= 2:
                        pat[rel] = v
                if not single_ok(pat):
                    good4 = False
                    break
            if good4:
                vis4 += 1
            else:
                und4 += 1
    checks.check(
        "T4-four-site", "4,814,888 of 4,961,984 four-record patterns = 97.04 %",
        (tot4, ex4, vis4, und4) == (4961984, 4814888, 96128, 50968)
        and abs(ex4 / tot4 - 0.9704) < 0.0001)

    # A formal complement from the zero-edge assignment is not a nonzero hop.
    zero_cfg = fam["sea"][0]
    zero_parity = {c: (-1) ** sum(zero_cfg[e] for e in es444
                                   if e in {tuple((c[k] + d[k]) % 4 for k in range(3)) for d in NN})
                   for c in corners}
    hop_coefficients = []
    for e in es444:
        ends = [c for c in corners if e in {tuple((c[k] + d[k]) % 4 for k in range(3)) for d in NN}]
        assert len(ends) == 2
        hop_coefficients.append((zero_parity[ends[0]] - zero_parity[ends[1]]) / 2)
    checks.check("C-zero-bit-not-hopping", "all 24 supplied hop coefficients vanish at zero edge bits",
                 len(hop_coefficients) == 24 and all(v == 0 for v in hop_coefficients))

    # ---------- note hygiene ------------------------------------------------
    lines = len(note.splitlines())
    checks.check("note-length", "the note stays under 330 lines", lines < 330,
                 lines)
    checks.check(
        "note-registry-id", "the note declares its registry id",
        "matter_law_readout_blind_where_role_alphabet_realises_no_adjacency"
        "_2026_09_04" in note)
    scan = "\n".join(
        ln for ln in note.lower().splitlines()
        if not ln.startswith(("audit_required_before_effective_retained",
                              "bare_retained_allowed")))
    banned = ("measurement", "observer", "collapse", "exhausted", "exhaustive",
              "crystal", "swap", "layers", "closes the route", "only route",
              "last route", "no-go", "retained")
    hits = [w for w in banned if w in scan]
    checks.check("note-vocabulary", "the note avoids the banned vocabulary",
                 not hits, hits)
    checks.check(
        "note-wording", "and says superlattice role pattern",
        "superlattice role pattern" in note_flat)
    checks.check(
        "note-scope", "no law selected; bounded scope stated",
        "no physical law is selected" in note_flat and "claim_scope:" in note
        and "promoted" not in note.lower() and "new axiom" not in note.lower())
    checks.check(
        "note-interfaces", "the note names its six parent pull requests",
        all(tok in note for tok in
            ("#7939", "#7928", "#7929", "#7934", "#7885", "#7889", "#7891")))
    checks.check(
        "note-numbers", "the note carries its counts",
        all(tok in note for tok in
            ("2,048", "794", "11,130", "10,611", "95.34", "9,919", "2^1580",
             "2^10599", "454,664,880", "61,008", "39")))
    checks.check(
        "note-boundary", "the undecided items are named",
        all(tok in note for tok in ("16,333", "50,968", "exact fibre"))
        and "nothing is derived from the axioms" in note_flat)

    print("per_element: 5 role symbols, 800 and 2,226 profile orbits")
    print("per_site: every site of every named torus, at every rung")
    print("per_mode: checked and not executed - no spectral decomposition here")
    print("per_block: 48 sectors, 18 pairs, 12 pinning offsets of 124")
    print("lattice_wide: 4x2x2, 4x4x2, 4x4x4, 8x4x4; Z^3 for the censuses")
    print(f"elapsed_sec: {time.time() - t0:.1f}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
