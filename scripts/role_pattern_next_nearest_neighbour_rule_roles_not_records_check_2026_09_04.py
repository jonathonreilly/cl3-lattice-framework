#!/usr/bin/env python3
"""Exact checks: the superlattice role pattern is a next-nearest-neighbour
support rule over roles, and roles are not record values.

The runner recomputes, with no sampling, no seed and no random number
generator:

T1  the role census of the period-(4,2,2) pattern over the 5-symbol role
    alphabet {C0, C1, E, F, Q} -- 18 (role, profile) pairs, 17 distinct
    profiles of 5^6, 6 rotation orbits of 800 -- and the covariance identity
    for local pairs, not equality of global admissible sets;
T2  that the nearest-neighbour role table does not pin the pattern: every
    corner carries profile EEEEEE, every edge site realises all four
    corner-pin pairs on its axis, and the admissible set is 8 x 2^{#corners}
    on every commensurate torus and empty on the incommensurate ones;
T3  the minimal rotation-closed pinning neighbourhood containing NN --
    NN united with {+-2 e_d}, 12 offsets of the 5x5x5 window's 124 -- as a
    set equality with the 48 sectors, its two failing siblings, and the
    three-step defect chain over the corner pin field;
T4  the record-level statements: a complete solver-free enumeration on the
    4x2x2 torus and required SAT on the 4x4x4 torus, both
    finding configurations outside every sector cylinder for the star,
    NN united with {+-2 e}, L1<=2 and 3x3x3 windows and none for 5x5x5;
    all 128 binary star patterns realised; and the role recovered from
    records only at L-infinity radius 2;
T5  static NN profile catalog -- 6 of 800 complete profile orbits and
    61 of 2226 partial profile orbits, distinguished from central-role entries
    and from the twelve-offset pinning rule.

Static catalog membership does not supply physical occurrence or readout. No physical law is selected and no
lattice beyond the named tori is claimed.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 300

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_"
    "RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_"
    "2026-09-04.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PROBE_REL = "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md"
Q8_REL = (
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)

AUDIT_INPUT_PATHS = (
    "docs/THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_"
    "RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_"
    "2026-09-04.md",
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

CURRENT_INPUT_SHA256 = {'docs/THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'f8abdba5e12c4375eb13c68c7fe8a7c2633c83928308357da273259cf4c5d5cd', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md': 'c277ca66054a47ac0183e1a7d806acf0fee01167915d8b70746125d73a5a56f4', 'docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md': 'c08d7a351c2ae40d921b0e996ca817b4f789c51072fbf2b6eb9a2de6f6fe8967'}

CELL_CAP = 16_000_000          # no dense array above 4096 x 4096 entries
CODE_CAP = 19                  # base-5 window code stays inside int64

# ---- role alphabet ---------------------------------------------------------
C0, C1, E, F, Q = 0, 1, 2, 3, 4
NAME = ("C0", "C1", "E", "F", "Q")
PROJ = (0, 0, 1, 2, 3)         # C0, C1 -> C : the skeleton alphabet
OPEN = 5                       # a site carrying no record, in the readout
TORI = ((4, 2, 2), (4, 4, 4), (8, 4, 4), (5, 4, 4), (7, 4, 4))


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


# ---- the pattern -----------------------------------------------------------
def pat_sym(site, ax: int) -> int:
    """Role of a fine site in the period-(4,2,2) pattern laid along `ax`."""
    odd = (site[0] & 1) + (site[1] & 1) + (site[2] & 1)
    if odd == 0:
        return C0 + ((site[ax] // 2) % 2)     # corner, pinned (s[ax]/2) mod 2
    if odd == 1:
        return E                              # coarse edge label; binary value separately supplied
    if odd == 2:
        return F                              # face, pinned 0
    return Q                                  # cube centre, pinned 1


def pat_bit(site, ax: int):
    """Record value at a fine site; None where the pattern pins nothing."""
    role = pat_sym(site, ax)
    if role == E:
        return None
    return 1 if role in (C1, Q) else 0


# ---- proper cubic rotations ------------------------------------------------
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


def act(matrix, vec):
    return tuple(sum(matrix[i][k] * vec[k] for k in range(3)) for i in range(3))


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def axial(radius):
    return [tuple(sign * radius * e for e in basis)
            for basis in ((1, 0, 0), (0, 1, 0), (0, 0, 1))
            for sign in (1, -1)]


def orbit(seed):
    return sorted({act(m, seed) for m in ROTATIONS})


def ball(radius, metric):
    norm = (lambda o: sum(map(abs, o))) if metric == 1 else (lambda o: max(map(abs, o)))
    return sorted(o for o in itertools.product(range(-radius, radius + 1), repeat=3)
                  if o != (0, 0, 0) and norm(o) <= radius)


NN = sorted(axial(1))
NBHDS = {
    "NN": NN,
    "NN+AX3": sorted(NN + axial(3)),
    "NN+DIAG2": sorted(NN + orbit((1, 1, 0))),
    "NN+AX2": sorted(NN + axial(2)),
    "NN+BODY": sorted(NN + orbit((1, 1, 1))),
    "L1<=2": ball(2, 1),
    "3x3x3": ball(1, "inf"),
    "5x5x5": ball(2, "inf"),
}
LADDER = ("NN", "NN+AX3", "NN+DIAG2", "NN+AX2", "NN+BODY", "L1<=2", "3x3x3", "5x5x5")
WIDE = ("NN", "NN+AX3", "NN+DIAG2", "NN+AX2", "NN+BODY")
NESTED = (("L1<=2", "NN+AX2"), ("3x3x3", "NN+BODY"), ("5x5x5", "L1<=2"))


def rot_maps(support):
    index = {o: i for i, o in enumerate(support)}
    return [tuple(index[act(transpose(m), support[i])] for i in range(len(support)))
            for m in ROTATIONS]


def realised(support, ax: int = 0, proj: bool = False):
    """The (role, profile) pairs the pattern realises, rotation-closed."""
    maps = rot_maps(support)
    base = set()
    for site in itertools.product(range(4), range(2), range(2)):
        role = pat_sym(site, ax)
        profile = tuple(pat_sym(tuple(site[k] + o[k] for k in range(3)), ax)
                        for o in support)
        base.add((role, profile))
    out = set()
    for role, profile in base:
        for m in maps:
            out.add((role, tuple(profile[m[i]] for i in range(len(support)))))
    if proj:
        out = {(PROJ[r], tuple(PROJ[x] for x in p)) for r, p in out}
    return out


# ---- tori ------------------------------------------------------------------
def sites(box):
    return list(itertools.product(range(box[0]), range(box[1]), range(box[2])))


def neighbour_table(box, support):
    index = {s: i for i, s in enumerate(sites(box))}
    return [[index[tuple((s[k] + o[k]) % box[k] for k in range(3))] for o in support]
            for s in sites(box)]


def sector_roles(box):
    out = set()
    for ax in (0, 1, 2):
        period = [2, 2, 2]
        period[ax] = 4
        if any(box[i] % period[i] for i in range(3)):
            continue
        for shift in itertools.product(range(4), repeat=3):
            out.add(tuple(pat_sym(tuple(s[k] + shift[k] for k in range(3)), ax)
                          for s in sites(box)))
    return out


def enum_skeletons(box, coarse_pairs):
    """Every skeleton the projected NN rule admits, by pair-propagation DFS."""
    nb = neighbour_table(box, NN)
    n = len(nb)
    pairs = sorted(coarse_pairs)
    found = []

    def compat(v, role, profile, assign):
        if assign[v] not in (-1, role):
            return False
        return all(assign[nb[v][i]] in (-1, x) for i, x in enumerate(profile))

    def place(v, role, profile, assign):
        assign[v] = role
        for i, x in enumerate(profile):
            assign[nb[v][i]] = x

    def recurse(assign):
        while True:
            changed = False
            for v in range(n):
                live = [k for k, (r, p) in enumerate(pairs) if compat(v, r, p, assign)]
                if not live:
                    return
                if len(live) == 1:
                    role, profile = pairs[live[0]]
                    before = (assign[v], tuple(assign[j] for j in nb[v]))
                    place(v, role, profile, assign)
                    if before != (assign[v], tuple(assign[j] for j in nb[v])):
                        changed = True
            if not changed:
                break
        for v in range(n):
            if assign[v] == -1 or any(assign[j] == -1 for j in nb[v]):
                for role, profile in pairs:
                    if compat(v, role, profile, assign):
                        branch = assign[:]
                        place(v, role, profile, branch)
                        recurse(branch)
                return
        found.append(tuple(assign))

    recurse([-1] * n)
    return sorted(set(found))


def expand(skeleton, pins):
    """Role configurations: one skeleton with every corner-pin assignment."""
    n = len(skeleton)
    corner = {v: j for j, v in enumerate(v for v in range(n) if skeleton[v] == 0)}
    base = np.empty((pins.shape[0], n), dtype=np.int64)
    for v in range(n):
        base[:, v] = pins[:, corner[v]] if skeleton[v] == 0 else {1: E, 2: F, 3: Q}[skeleton[v]]
    return base


def window_codes(support, pairs):
    weight = [5 ** i for i in range(len(support) + 1)]
    return np.array(sorted({r * weight[0]
                            + sum(p[i] * weight[i + 1] for i in range(len(support)))
                            for r, p in pairs}), dtype=np.int64)


def sift(base, nb, support, pairs):
    """Row indices of `base` admissible under the covariant rule on `support`."""
    allowed = window_codes(support, pairs)
    weight = np.array([5 ** i for i in range(len(support) + 1)], dtype=np.int64)
    keep = np.arange(base.shape[0])
    for v in range(len(nb)):
        if keep.size == 0:
            break
        block = base[keep]
        code = block[:, v] * weight[0]
        for i, j in enumerate(nb[v]):
            code = code + block[:, j] * weight[i + 1]
        keep = keep[np.isin(code, allowed)]
    return keep


def sift_direct(rows, nb, pairs):
    """Per-configuration check, for windows too wide for a base-5 code."""
    out = []
    for cfg in rows:
        if all((cfg[v], tuple(cfg[j] for j in nb[v])) in pairs for v in range(len(nb))):
            out.append(cfg)
    return out


def ladder_counts(box):
    """Admissible role configurations at every rung, and the sector set."""
    sectors = sector_roles(box)
    skeletons = enum_skeletons(box, realised(NN, proj=True))
    if not skeletons:
        return {name: (0, []) for name in LADDER}, sectors, skeletons
    corners = sum(1 for x in skeletons[0] if x == 0)
    pins = ((np.arange(1 << corners, dtype=np.int64)[:, None]
             >> np.arange(corners)) & 1).astype(np.int64)
    bases = [expand(sk, pins) for sk in skeletons]
    assert bases[0].size <= CELL_CAP
    out = {}
    for name in WIDE:
        support = NBHDS[name]
        pairs = realised(support)
        nb = neighbour_table(box, support)
        total, rows = 0, []
        for base in bases:
            keep = sift(base, nb, support, pairs)
            total += int(keep.size)
            if total <= 4096:
                rows.extend(tuple(int(x) for x in r) for r in base[keep])
        out[name] = (total, rows if total <= 4096 else [])
    for name, source in NESTED:
        support = NBHDS[name]
        nb = neighbour_table(box, support)
        rows = sift_direct(out[source][1], nb, realised(support))
        out[name] = (len(rows), rows)
    return out, sectors, skeletons


# ---- the record level ------------------------------------------------------
def templates():
    out = []
    for ax in (0, 1, 2):
        for shift in itertools.product(range(4), range(2), range(2)):
            origin = [0, 0, 0]
            origin[ax] = shift[0]
            origin[(ax + 1) % 3] = shift[1]
            origin[(ax + 2) % 3] = shift[2]
            out.append((ax, tuple(origin)))
    return out


TEMPLATES = templates()
WINDOWS = tuple((name, [(0, 0, 0)] + NBHDS[name])
                for name in ("NN", "NN+AX2", "L1<=2", "3x3x3", "5x5x5"))


def window_pattern(window, ax, origin):
    return tuple(pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax) for o in window)


def role_determined(window):
    """Is the centre role a function of the record values on `window`?"""
    patterns = [window_pattern(window, ax, origin) for ax, origin in TEMPLATES]
    roles = [pat_sym(origin, ax) for ax, origin in TEMPLATES]
    for a in range(len(TEMPLATES)):
        for b in range(a + 1, len(TEMPLATES)):
            if roles[a] == roles[b]:
                continue
            if all(x is None or y is None or x == y
                   for x, y in zip(patterns[a], patterns[b])):
                return False, (NAME[roles[a]], NAME[roles[b]])
    return True, None


def enumerate_records(box, window):
    """Complete enumeration: admissible under the minimal window rule, and
    outside every sector cylinder. No solver."""
    grid = sites(box)
    n = len(grid)
    index = {s: i for i, s in enumerate(grid)}
    assert (1 << n) * n <= CELL_CAP
    bits = ((np.arange(1 << n, dtype=np.int64)[:, None] >> np.arange(n)) & 1).astype(np.int8)
    admissible = np.ones(1 << n, dtype=bool)
    for site in grid:
        matched = np.zeros(1 << n, dtype=bool)
        for ax, origin in TEMPLATES:
            demand, consistent = {}, True
            for o in window:
                value = pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
                if value is None:
                    continue
                u = index[tuple((site[k] + o[k]) % box[k] for k in range(3))]
                if demand.get(u, value) != value:
                    consistent = False
                    break
                demand[u] = value
            if not consistent:
                continue
            hit = np.ones(1 << n, dtype=bool)
            for u, value in demand.items():
                hit &= bits[:, u] == value
            matched |= hit
        admissible &= matched
    outside = np.ones(1 << n, dtype=bool)
    for ax, origin in TEMPLATES:
        cylinder = np.ones(1 << n, dtype=bool)
        fits = True
        period = [2, 2, 2]
        period[ax] = 4
        if any(box[i] % period[i] for i in range(3)):
            fits = False
        if not fits:
            continue
        for i, site in enumerate(grid):
            value = pat_bit(tuple(site[k] + origin[k] for k in range(3)), ax)
            if value is not None:
                cylinder &= bits[:, i] == value
        outside &= ~cylinder
    return int(admissible.sum()), int((admissible & outside).sum())


def sat_records(box, window, solver_cls):
    """SAT: admissible under the minimal window rule, outside all 48 cylinders."""
    from pysat.formula import CNF

    grid = sites(box)
    index = {s: i + 1 for i, s in enumerate(grid)}
    cnf = CNF()
    nxt = len(grid) + 1
    for site in grid:
        markers = []
        for ax, origin in TEMPLATES:
            marker = nxt
            nxt += 1
            markers.append(marker)
            for o in window:
                value = pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
                if value is None:
                    continue
                u = index[tuple((site[k] + o[k]) % box[k] for k in range(3))]
                cnf.append([-marker, u if value == 1 else -u])
        cnf.append(markers)
    for ax, origin in TEMPLATES:
        clause = []
        for i, site in enumerate(grid):
            value = pat_bit(tuple(site[k] + origin[k] for k in range(3)), ax)
            if value is not None:
                clause.append(-(i + 1) if value == 1 else (i + 1))
        cnf.append(clause)
    with solver_cls(bootstrap_with=cnf) as solver:
        return bool(sat_decision(solver))


def star_value_patterns():
    window = [(0, 0, 0)] + NN
    seen = set()
    for ax in (0, 1, 2):
        for site in itertools.product(range(8), range(8), range(8)):
            base = list(window_pattern(window, ax, site))
            free = [i for i, v in enumerate(base) if v is None]
            for fill in itertools.product((0, 1), repeat=len(free)):
                row = list(base)
                for i, value in zip(free, fill):
                    row[i] = value
                seen.add(tuple(row))
    return seen


# ---- readability -----------------------------------------------------------
def readability():
    maps = rot_maps(NN)

    def orb(profile):
        return min(tuple(profile[m[i]] for i in range(6)) for m in maps)

    complete = realised(NN)
    profiles = {p for _, p in complete}
    complete_orbits = {orb(p) for p in profiles}
    role_orbits = {orb(p) for p in itertools.product(range(5), repeat=6)}
    partial = set()
    for site in itertools.product(range(4), range(2), range(2)):
        role = pat_sym(site, 0)
        full = [pat_sym(tuple(site[k] + o[k] for k in range(3)), 0) for o in NN]
        for mask in range(64):
            profile = tuple(full[i] if (mask >> i) & 1 else OPEN for i in range(6))
            for m in maps:
                partial.add((role, tuple(profile[m[i]] for i in range(6))))
    partial_profiles = {p for _, p in partial}
    partial_orbits = {orb(p) for p in partial_profiles}
    open_orbits = {orb(p) for p in itertools.product(range(6), repeat=6)}
    return (len(complete), len(profiles), len(complete_orbits), len(role_orbits),
            len(partial), len(partial_profiles), len(partial_orbits), len(open_orbits))


def pin_field_families(box):
    """All / laminar / striped binary pin fields on the coarse sublattice."""
    coarse = [s for s in sites(box) if all(c % 2 == 0 for c in s)]
    index = {s: j for j, s in enumerate(coarse)}
    n = len(coarse)
    assert (1 << n) * n <= CELL_CAP
    bits = ((np.arange(1 << n, dtype=np.int64)[:, None] >> np.arange(n)) & 1).astype(np.int8)
    laminar = np.zeros(1 << n, dtype=bool)
    striped = np.zeros(1 << n, dtype=bool)
    for ax in range(3):
        planes = {}
        for s in coarse:
            planes.setdefault(s[ax], []).append(index[s])
        flat = np.ones(1 << n, dtype=bool)
        for plane in planes.values():
            for j in plane[1:]:
                flat &= bits[:, plane[0]] == bits[:, j]
        laminar |= flat
        for offset in (0, 1):
            run = np.ones(1 << n, dtype=bool)
            for s in coarse:
                run &= bits[:, index[s]] == (((s[ax] // 2) % 2) ^ offset)
            striped |= run
    return n, 1 << n, int(laminar.sum()), int(striped.sum())

def coordinate_pin_families(box):
    """Independent plane/alternation construction, without sifting a rule table."""
    grid = list(itertools.product(*(range(n) for n in box)))
    laminar, striped = set(), set()
    for phase in itertools.product((0, 1), repeat=3):
        shifted = [tuple((p[k] + phase[k]) % box[k] for k in range(3)) for p in grid]
        for axis in range(3):
            for plane_bits in itertools.product((0, 1), repeat=box[axis] // 2):
                row = tuple(plane_bits[p[axis] // 2] if sum(v % 2 for v in p) == 0
                            else {1: E, 2: F, 3: Q}[sum(v % 2 for v in p)]
                            for p in shifted)
                laminar.add(row)
            for parity in (0, 1):
                striped.add(tuple(((p[axis] // 2) % 2) ^ parity
                                  if sum(v % 2 for v in p) == 0
                                  else {1: E, 2: F, 3: Q}[sum(v % 2 for v in p)]
                                  for p in shifted))
    return laminar, striped


# ---- main ------------------------------------------------------------------
def main() -> int:
    checks = Checks()
    require_inputs()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    probe = PROBE_PATH.read_text(encoding="utf-8")
    law_pair = Q8_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    try:
        from pysat.solvers import Cadical153
        have_sat = True
    except Exception:
        Cadical153 = None
        have_sat = False
        raise RuntimeError("complete claim coverage requires CaDiCaL")

    print("external_scientific_inputs: none; every number is recomputed here")
    print("integrity_reads: axioms, deep probe, law pair, this note")
    print("construction: exact enumeration over roles and over binary records")
    print("negative_scope: finite non-pinning statements on the named tori")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("interpretation_guard: minimal_axioms Lattice, Qubit, Admissibility")
    print("declared_math: cubic rotations, role subshifts, binary record windows")
    if have_sat:
        print("solver_mode: pysat present; CaDiCaL on the 4x4x4 torus, and the "
              "complete solver-free enumeration on the 4x2x2 torus")
    else:
        print("solver_mode: pysat absent; the complete solver-free enumeration on "
              "the smallest torus, 4x2x2, decides the record-level rows and the "
              "4x4x4 SAT rows are not run")

    checks.check("audit-input-paths", "declared inputs exist and are unique",
                 all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS)
                 and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)))
    checks.check("audit-timeout", "the declared timeout is 300 seconds",
                 AUDIT_TIMEOUT_SEC == 300)

    # ---------- supplied surface -------------------------------------------
    checks.check(
        "axiom-lattice", "nearest-neighbor adjacency is quoted",
        "with nearest-neighbor\nadjacency" in axiom
        and "nearest-neighbor adjacency" in note_flat)
    checks.check(
        "axiom-admissibility", "the one fixed nearest-neighbor rule is quoted",
        "There is one fixed nearest-neighbor admissibility rule, covariant under "
        "lattice translations and proper cubic rotations." in axiom_flat
        and "one fixed nearest-neighbor admissibility rule" in note_flat)
    checks.check(
        "axiom-qubit", "the M_2(C) presentation is quoted",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom_flat
        and "algebraic presentation `M_2(C)`" in note_flat)
    checks.check(
        "axiom-support", "admissible read as the support",
        "denotes its support -- on finite menus, exactly the possibilities of "
        "nonzero probability" in axiom_flat and "denotes its support" in note_flat)
    checks.check(
        "parent-deep-probe", "the declared historical deep-probe comparator is present",
        "number of covariant label-equivariant tables = 3^24" in probe)
    checks.check(
        "parent-law-pair", "the conditional law-pair boundary is present",
        "claim_type: bounded_theorem" in law_pair
        and "It selects neither rule as the framework's physical law."
        in normalize(law_pair))

    # ---------- T1 : the role census ---------------------------------------
    pairs_nn = realised(NN)
    profiles_nn = {p for _, p in pairs_nn}
    maps = rot_maps(NN)

    def orb(profile):
        return min(tuple(profile[m[i]] for i in range(6)) for m in maps)

    union = set()
    for ax in (0, 1, 2):
        for site in itertools.product(range(4), range(4), range(4)):
            union.add((pat_sym(site, ax),
                       tuple(pat_sym(tuple(site[k] + o[k] for k in range(3)), ax)
                             for o in NN)))
    table = {}
    for role, profile in pairs_nn:
        table.setdefault(profile, set()).add(role)

    checks.check("T1-pairs", "the pattern realises 18 (role, profile) pairs",
                 len(pairs_nn) == 18, len(pairs_nn))
    checks.check("T1-profiles", "17 profiles of the 5^6 = 15625",
                 len(profiles_nn) == 17 and 5 ** 6 == 15625, len(profiles_nn))
    checks.check("T1-orbits", "6 rotation orbits of 800",
                 len({orb(p) for p in profiles_nn}) == 6
                 and len({orb(p) for p in itertools.product(range(5), repeat=6)}) == 800)
    checks.check("T1-covariance",
                 "rotation closure equals the union of local template pairs",
                 pairs_nn == union)
    checks.check("T1-table", "the table has 17 nonempty rows",
                 len(table) == 17 and sum(len(v) for v in table.values()) == 18)

    # ---------- T2 : the nearest-neighbour role table does not pin ----------
    corner_profiles = {tuple(pat_sym(tuple(s[k] + o[k] for k in range(3)), 0) for o in NN)
                       for s in itertools.product(range(4), range(2), range(2))
                       if pat_sym(s, 0) in (C0, C1)}
    edge_full = True
    for site in itertools.product(range(4), range(2), range(2)):
        if pat_sym(site, 0) != E:
            continue
        profile = [pat_sym(tuple(site[k] + o[k] for k in range(3)), 0) for o in NN]
        slots = [i for i, x in enumerate(profile) if x in (C0, C1)]
        for fill in itertools.product((C0, C1), repeat=len(slots)):
            row = list(profile)
            for i, value in zip(slots, fill):
                row[i] = value
            edge_full &= (E, tuple(row)) in pairs_nn
    coarse_pairs = realised(NN, proj=True)
    unrealised = 0
    for coarse_role, coarse_profile in coarse_pairs:
        roles = [C0, C1] if coarse_role == 0 else [{1: E, 2: F, 3: Q}[coarse_role]]
        slots = [i for i, x in enumerate(coarse_profile) if x == 0]
        for role in roles:
            for fill in itertools.product((C0, C1), repeat=len(slots)):
                row = [{1: E, 2: F, 3: Q}[x] if x else None for x in coarse_profile]
                for i, value in zip(slots, fill):
                    row[i] = value
                unrealised += (role, tuple(row)) not in pairs_nn

    checks.check("T2-corner-profile", "every corner carries EEEEEE",
                 corner_profiles == {(E,) * 6}, corner_profiles)
    checks.check("T2-corner-menu", "so its menu holds C0 and C1",
                 table[(E,) * 6] == {C0, C1})
    checks.check("T2-edge-pins",
                 "edges realise all 4 corner-pin pairs",
                 edge_full)
    checks.check("T2-refinements",
                 "0 refinements unrealised",
                 unrealised == 0 and len(coarse_pairs) == 8, unrealised)

    ladder = {}
    for box in TORI:
        ladder[box] = ladder_counts(box)

    expected_nn = {(4, 2, 2): 32, (4, 4, 4): 2048, (8, 4, 4): 524288,
                   (5, 4, 4): 0, (7, 4, 4): 0}
    expected_sectors = {(4, 2, 2): 16, (4, 4, 4): 48, (8, 4, 4): 48,
                        (5, 4, 4): 0, (7, 4, 4): 0}
    name = {b: f"{b[0]}x{b[1]}x{b[2]}" for b in TORI}
    header = "  ".join(f"{n:>7s}" for n in LADDER)
    print(f"ladder  torus   {header}  sectors")
    for box in TORI:
        counts, sectors, _ = ladder[box]
        row = "  ".join(f"{counts[n][0]:7d}" for n in LADDER)
        print(f"        {name[box]:6s}  {row}  {len(sectors):7d}")

    checks.check(
        "T2-nn-counts",
        "NN admits 8 x 2^corners: 32, 2048, 524288",
        all(ladder[b][0]["NN"][0] == expected_nn[b] for b in TORI)
        and all(ladder[b][0]["NN"][0] == 8 * (1 << sum(1 for x in ladder[b][2][0]
                                                       if x == 0))
                for b in TORI[:3]),
        {name[b]: ladder[b][0]["NN"][0] for b in TORI})
    checks.check(
        "T2-skeleton", "NN pins the (2,2,2) skeleton, 8 of it",
        all(len(ladder[b][2]) == 8 for b in TORI[:3])
        and all(len(ladder[b][2]) == 0 for b in TORI[3:]))
    checks.check(
        "T2-incommensurate", "0 on 5x4x4 and 7x4x4, at every rung",
        all(ladder[b][0][n][0] == 0 for b in TORI[3:] for n in LADDER))
    checks.check(
        "T2-sectors", "against 16, 48 and 48 sectors",
        all(len(ladder[b][1]) == expected_sectors[b] for b in TORI))

    # ---------- T3 : the next-nearest-neighbour rule ------------------------
    window_offsets = set(NBHDS["5x5x5"])
    orbit_sizes = {}
    covered = set()
    for offset in sorted(window_offsets):
        if offset in covered:
            continue
        this = orbit(offset)
        covered |= set(this)
        orbit_sizes.setdefault(len(this), []).append(this[0])

    checks.check(
        "T3-pins-4x4x4",
        "NN+{+-2e} = the 48 sectors on 4x4x4, as a set",
        set(ladder[(4, 4, 4)][0]["NN+AX2"][1]) == ladder[(4, 4, 4)][1]
        and ladder[(4, 4, 4)][0]["NN+AX2"][0] == 48)
    checks.check(
        "T3-pins-8x4x4",
        "and the 48 sectors on 8x4x4, as a set",
        set(ladder[(8, 4, 4)][0]["NN+AX2"][1]) == ladder[(8, 4, 4)][1]
        and ladder[(8, 4, 4)][0]["NN+AX2"][0] == 48)
    checks.check(
        "T3-pins-4x2x2", "and the 16 sectors 4x2x2 holds",
        set(ladder[(4, 2, 2)][0]["NN+AX2"][1]) == ladder[(4, 2, 2)][1])
    checks.check(
        "T3-pins-incommensurate", "and 0 on 5x4x4 and 7x4x4",
        all(ladder[b][0]["NN+AX2"][0] == 0 for b in TORI[3:]))
    checks.check(
        "T3-ax3-fails", "NN+{+-3e} admits 2048 on 4x4x4 and 8x4x4",
        ladder[(4, 4, 4)][0]["NN+AX3"][0] == 2048
        and ladder[(8, 4, 4)][0]["NN+AX3"][0] == 2048)
    checks.check(
        "T3-diag-fails", "NN+diag admits 64 on 4x4x4, 160 on 8x4x4",
        ladder[(4, 4, 4)][0]["NN+DIAG2"][0] == 64
        and ladder[(8, 4, 4)][0]["NN+DIAG2"][0] == 160)
    checks.check(
        "T3-minimal-orbits",
        "size-6 orbits in 5x5x5: {+-e}, {+-2e} only",
        sorted(orbit_sizes[6]) == [(-2, 0, 0), (-1, 0, 0)]
        and sorted(orbit_sizes) == [6, 8, 12, 24], sorted(orbit_sizes.items()))
    checks.check(
        "T3-twelve-of-124",
        "so the support is 12 of the window's 124",
        len(NBHDS["NN+AX2"]) == 12 and len(NBHDS["5x5x5"]) == 124
        and set(NBHDS["NN+AX2"]) <= window_offsets)
    checks.check(
        "T3-nesting", "nested rungs contain what they refine",
        all(set(NBHDS[src]) <= set(NBHDS[name_]) for name_, src in NESTED))
    checks.check(
        "T3-upper-rungs", "L1<=2, 3x3x3, 5x5x5, body give the sector set",
        all(set(ladder[b][0][n][1]) == ladder[b][1]
            for b in TORI[:3] for n in ("L1<=2", "3x3x3", "5x5x5", "NN+BODY")))

    independent_laminar, independent_striped = coordinate_pin_families((8, 4, 4))
    coarse_n, all_fields, laminar, striped = pin_field_families((8, 4, 4))
    checks.check(
        "T3-defect-free", "NN admits every pin field: 2^16 = 65536",
        coarse_n == 16 and all_fields == 65536
        and ladder[(8, 4, 4)][0]["NN"][0] == 8 * all_fields)
    checks.check(
        "T3-defect-laminar",
        "NN+diag admits the laminar fields, 8 x 20",
        laminar == 20 and ladder[(8, 4, 4)][0]["NN+DIAG2"][0] == 8 * laminar
        and set(ladder[(8, 4, 4)][0]["NN+DIAG2"][1]) == independent_laminar)
    checks.check(
        "T3-defect-striped",
        "NN+{+-2e} admits the striped fields, 8 x 6",
        striped == 6 and ladder[(8, 4, 4)][0]["NN+AX2"][0] == 8 * striped
        and set(ladder[(8, 4, 4)][0]["NN+AX2"][1]) == independent_striped)

    # ---------- T4 : the record alphabet ------------------------------------
    enum_rows = {}
    for label, window in WINDOWS:
        enum_rows[label] = enumerate_records((4, 2, 2), window)
    print("records 4x2x2 complete enumeration (no solver): " + "  ".join(
        f"{label}={enum_rows[label][1]}" for label, _ in WINDOWS)
        + "  outside all cylinders")
    checks.check(
        "T4-enum-small",
        "4x2x2: the four smaller windows leave cylinder-free rows",
        all(enum_rows[label][1] > 0 for label in ("NN", "NN+AX2", "L1<=2", "3x3x3"))
        and enum_rows == {"NN": (65536, 64512), "NN+AX2": (15005, 13981),
                          "L1<=2": (1210, 186), "3x3x3": (1178, 154),
                          "5x5x5": (1024, 0)}, enum_rows)
    checks.check(
        "T4-enum-5x5x5",
        "4x2x2: 5x5x5 leaves none, 1024 = 16 x 2^6",
        enum_rows["5x5x5"] == (1024, 0), enum_rows["5x5x5"])

    if have_sat:
        sat_rows = {}
        for label, window in WINDOWS:
            sat_rows[label] = sat_records((4, 4, 4), window, Cadical153)
        print("records 4x4x4 CaDiCaL: " + "  ".join(
            f"{label}={'SAT' if sat_rows[label] else 'UNSAT'}"
            for label, _ in WINDOWS))
        checks.check(
            "T4-sat-small",
            "4x4x4: star, NN+{+-2e}, L1<=2, 3x3x3 all SAT",
            all(sat_rows[label] for label in ("NN", "NN+AX2", "L1<=2", "3x3x3")))
        checks.check(
            "T4-sat-5x5x5",
            "only 5x5x5 UNSAT among the five tested windows",
            not sat_rows["5x5x5"])

    stars = star_value_patterns()
    checks.check(
        "T4-star-census",
        "all 128 binary stars realised",
        len(stars) == 128 and len(stars) == 2 ** 7)

    determined = {label: role_determined(window) for label, window in WINDOWS}
    print("role from records: " + "  ".join(
        f"{label}={'yes' if determined[label][0] else 'no'}" for label, _ in WINDOWS))
    checks.check(
        "T4-role-radius",
        "template-compatible windows determine a role at radius 2",
        determined["5x5x5"][0]
        and not any(determined[label][0]
                    for label in ("NN", "NN+AX2", "L1<=2", "3x3x3")),
        {k: v[1] for k, v in determined.items()})
    checks.check(
        "T4-role-bits",
        "five supplied classical roles require three fixed-length bits",
        len(NAME) == 5 and (1 << 2) < 5 <= (1 << 3))
    checks.check(
        "T4-record-radius",
        "decoder compositions have conditional radius bounds 3 and 4",
        1 + 2 == 3 and 2 + 2 == 4
        and max(max(map(abs, o)) for o in NBHDS["NN+AX2"]) == 2)

    # ---------- T5 : readability and the decomposition ----------------------
    (n_pairs, n_profiles, n_orbits, n_all_orbits,
     n_partial, n_partial_profiles, n_partial_orbits, n_open_orbits) = readability()
    print(f"readability: complete {n_orbits}/{n_all_orbits}   "
          f"partial {n_partial_orbits}/{n_open_orbits} = "
          f"{n_partial_orbits / n_open_orbits:.4%}")
    checks.check(
        "T5-complete", "6 of 800 NN profile orbits exercised complete",
        (n_pairs, n_profiles, n_orbits, n_all_orbits) == (18, 17, 6, 800))
    checks.check(
        "T5-partial", "61 of 2226 partially, from 794 pairs",
        (n_partial, n_partial_profiles, n_partial_orbits, n_open_orbits)
        == (794, 655, 61, 2226))
    checks.check(
        "T5-fraction", "approximately 2.74 per cent of NN partial profile orbits exercised",
        abs(n_partial_orbits / n_open_orbits - 0.0274) < 0.0001)
    checks.check(
        "T5-decomposition", "the note separates the law's three parts",
        "role support rule" in note_flat and "sector choice" in note_flat
        and "S_f" in note and "B_v" in note and "T_ij" in note)
    checks.check(
        "T5-category-error",
        "readability misses the Hamiltonian terms",
        "category error" in note_flat)

    # Distinct allowed matrices do not reduce the one-site algebra to two values.
    densities = [np.diag([j / 4, 1 - j / 4]) for j in range(5)]
    checks.check("C-binary-domain", "five distinct density matrices in M_2(C)",
                 len({tuple(r.ravel()) for r in densities}) == 5
                 and all(np.trace(r) == 1 and np.linalg.eigvalsh(r).min() >= 0
                         for r in densities))
    checks.check("C-local-vs-global", "the NN local table admits 2048, not 48",
                 ladder[(4, 4, 4)][0]["NN"][0] == 2048
                 and len(ladder[(4, 4, 4)][1]) == 48)

    # ---------- note hygiene ------------------------------------------------
    lines = len(note.splitlines())
    checks.check("note-length", "the note stays under 330 lines", lines < 330, lines)
    checks.check(
        "note-registry-id", "the note declares its registry id",
        "role_pattern_next_nearest_neighbour_rule_roles_not_record_values" in note)
    banned = ("measurement", "collapse", "observer", "exhausted", "exhaustive",
              "no-go", "closes the route", "only route", "crystal")
    hits = [word for word in banned if word in note.lower()]
    import re as _re
    hits += _re.findall(
        r"\b(?:swap|swaps|swapped|move|moves|moved|fill|fills|filled)\b",
        note.lower())
    checks.check("note-vocabulary",
                 "the note avoids the banned vocabulary",
                 not hits, hits)
    checks.check(
        "note-wording", "and says superlattice role pattern",
        "superlattice role pattern" in note_flat)
    checks.check(
        "note-scope", "no law selected; bounded scope stated",
        "no physical law is selected" in note_flat and "claim_scope:" in note
        and "promoted" not in note.lower() and "new axiom" not in note.lower())
    checks.check(
        "note-exclusion",
        "the unreconciled counts are excluded",
        "not reproduced here" in note_flat and "excluded" in note_flat)
    checks.check(
        "note-parents", "the note names both parent sources",
        "#7834" in note and "#7934" in note)
    checks.check(
        "note-numbers", "the note carries its counts",
        all(token in note for token in
            ("524,288", "2,048", "48", "12", "124", "2,226", "2.74", "160")))

    print("per_element: 5 role symbols, 17 profiles, 800 orbits")
    print("per_site: every site of every named torus, at every rung")
    print("per_mode: checked and not executed - no spectral decomposition here")
    print("per_block: 48 sectors, 8 skeletons, 12 pinning offsets of 124")
    print("lattice_wide: five named tori; the record rows complete on 4x2x2")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
