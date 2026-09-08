#!/usr/bin/env python3
"""Conditional checks of the supplied record-support tables and parity completions.
Static star-readout injectivity, finite cylinder/extra membership and isolation,
and separate fixed-matrix free spectra. No physical formation or Hamiltonian
encoding is derived. On 8x4x4 the 16 displayed extras give a lower bound;
their historical completeness quotation is not established by this runner.

Self-contained definitions. The following source-block names are preserved
historical provenance labels; exact original probe files are not bound here.
The present implemented definitions and proofs, not a claimed copy identity,
are the reviewable inputs:

  * the role pattern, the proper cubic rotations, the 48 templates, the
    rotation-closed windows, the minimal record table T_min, the six
    completion rules, the torus admissible masks and the CNF encodings
                              -- source block `lib.py`;
  * T1, the role and record censuses, the solver-free role search, the
    4x2x2 ladder, the Burnside counts of never-realised profile orbits and
    the odd-corner census
                              -- source block `s1_census.py`;
  * T2, the complete 4x2x2 admissible sets for the seven rules, the CaDiCaL
    set equality, the pinned-flip counts on 4x4x4, the star flexibility and
    the star readout table
                              -- source block `s2_small_windows.py`;
  * T3, the pinned-flip lemma on Z^3, the flexibility counting bound, the
    extras and the F2 cross-check on 4x4x4 and 8x4x4, the Z^3 exercised-entry
    census and the partial-pattern census
                              -- source block `s3_big_windows.py`;
  * T4, the formal complement families and their support transitions, the structure and isolation
    of the extras, the coarse graph, the KS sign field, the flux-class scan
    and the 8x4x4 odd-corner census
                              -- source block `s4_physics.py`.

Two reductions keep the run inside its budget, both declared:

  * the star flexibility of `s2_small_windows.py` is recomputed by a sparse
    recount -- the realised and exercised profiles are bincounted by overlap
    key, and the completions of each key are counted exactly rather than
    scanned -- which reproduces the source's triple counts entry for entry;
  * the extra configurations of the corrected and parity rules on 8x4x4 with
    the 5x5x5 window are supplied as a declared certificate of 16 weight-24
    configurations, each re-verified here as admissible, outside every
    cylinder and isolated; that the list is complete, 16 for the corrected
    rule and those 16 with the all-0 configuration for the parity rule, is
    an unverified historical quotation from source output lines s3B.005 and s3A.030 and is not
    re-enumerated (each of those rows cost about 1,000 seconds).

Capped enumerations are reported as bounds and never as counts.  No sampling,
no seed and no random number generator is used anywhere.  CaDiCaL is required, and unavailable or indeterminate solver decisions fail
the complete run. The complete solver-free enumeration on the smallest
torus also runs in every run.
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
    "docs/A_READABLE_MATTER_LAW_EXISTS_ON_THE_5X5X5_WINDOW_THE_DESIGNED_LAWS_"
    "RECORD_TABLE_COMPLETED_BY_A_COVARIANT_PARITY_RULE_HAS_EVERY_MENU_"
    "NONEMPTY_IS_READ_FROM_PARTIAL_BLOCKS_AND_KEEPS_THE_FERMION_BOUNDED_"
    "NOTE_2026-09-04.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PROBE_REL = "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md"
BKSF_REL = (
    "docs/FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_"
    "NOTE_2026-09-02.md"
)

AUDIT_INPUT_PATHS = (
    "docs/A_READABLE_MATTER_LAW_EXISTS_ON_THE_5X5X5_WINDOW_THE_DESIGNED_LAWS_"
    "RECORD_TABLE_COMPLETED_BY_A_COVARIANT_PARITY_RULE_HAS_EVERY_MENU_"
    "NONEMPTY_IS_READ_FROM_PARTIAL_BLOCKS_AND_KEEPS_THE_FERMION_BOUNDED_"
    "NOTE_2026-09-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md",
    "docs/FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_"
    "NOTE_2026-09-02.md",
)

assert AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL, PROBE_REL, BKSF_REL)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL
PROBE_PATH = ROOT / PROBE_REL
BKSF_PATH = ROOT / BKSF_REL

CURRENT_INPUT_SHA256 = {'docs/A_READABLE_MATTER_LAW_EXISTS_ON_THE_5X5X5_WINDOW_THE_DESIGNED_LAWS_RECORD_TABLE_COMPLETED_BY_A_COVARIANT_PARITY_RULE_HAS_EVERY_MENU_NONEMPTY_IS_READ_FROM_PARTIAL_BLOCKS_AND_KEEPS_THE_FERMION_BOUNDED_NOTE_2026-09-04.md': '31bbe6cb6d105b8cd2bfb4480159a2b06c722de928d2e6085d1f33d1017c2426', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md': 'c277ca66054a47ac0183e1a7d806acf0fee01167915d8b70746125d73a5a56f4', 'docs/FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-02.md': 'bdaccbb0c4a000d0ae339af2e71dc9f0989be3266488b61050e57ca902c172c9'}

CELL_CAP = 16_000_000          # no dense array above 4096 x 4096 entries
SAT_CAP = 5000                 # capped enumerations are reported as bounds

# unverified historical rows (s3A.030 and s3B.005): the alleged completeness
# of the 8x4x4 extra lists under the parity and corrected rules on the 5x5x5
# window.  Every other number below is recomputed here.
QUOTED_8X4X4_PAR_EXTRAS = 17
QUOTED_8X4X4_CORR_EXTRAS = 16

# the declared certificate: the 16 weight-24 extras of the corrected rule on
# 8x4x4 with the 5x5x5 window, site order itertools.product(range(8),
# range(4), range(4)), bit i of the hex word = site i
EXTRA_CERTIFICATE_8X4X4 = (
    "000050500a0a505000000a0a50500a0a",
    "a0a00505a0a000000505a0a005050000",
    "a0a000000505a0a005050000a0a00505",
    "a0a005050000a0a00505a0a000000505",
    "50500a0a505000000a0a50500a0a0000",
    "00000a0a50500a0a000050500a0a5050",
    "0a0a50500a0a000050500a0a50500000",
    "0000a0a00505a0a000000505a0a00505",
    "50500a0a000050500a0a505000000a0a",
    "0505a0a005050000a0a00505a0a00000",
    "00000505a0a005050000a0a00505a0a0",
    "0a0a505000000a0a50500a0a00005050",
    "05050000a0a00505a0a000000505a0a0",
    "0505a0a000000505a0a005050000a0a0",
    "505000000a0a50500a0a000050500a0a",
    "0a0a000050500a0a505000000a0a5050",
)


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


# ---- the pattern and the templates (source block lib.py) -------------------
C0, C1, E, F, Q = range(5)


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


def sites(box):
    return list(itertools.product(range(box[0]), range(box[1]), range(box[2])))


def wrap(s, box):
    return tuple(s[k] % box[k] for k in range(3))


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


def torus_sectors(box):
    """The distinct (ax, origin) cylinders the torus supports, as pin tuples."""
    seen = {}
    for ax, origin in TEMPLATES:
        period = [2, 2, 2]
        period[ax] = 4
        if any(box[i] % period[i] for i in range(3)):
            continue
        pins = tuple(pat_bit(tuple(s[k] + origin[k] for k in range(3)), ax)
                     for s in sites(box))
        seen.setdefault(pins, (ax, origin))
    return [(k, v) for v, k in sorted((v, k) for k, v in seen.items())]


ORBIT_SEEDS = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0),
               (2, 1, 1), (2, 2, 0), (2, 2, 1), (2, 2, 2),
               (3, 0, 0), (3, 1, 0), (3, 1, 1), (3, 2, 0), (3, 2, 1),
               (3, 2, 2), (3, 3, 0), (3, 3, 1), (3, 3, 2), (3, 3, 3),
               (3, 1, 2)]
ORBITS = [sorted({act(m, s) for m in ROTATIONS}) for s in ORBIT_SEEDS]


def window(*seed_ids):
    w = []
    for i in seed_ids:
        w += ORBITS[i]
    return sorted(w)


WINDOWS = {
    "NN": window(0),                       # 6
    "NN+AX2": window(0, 3),                # 12
    "L1<=2": window(0, 1, 3),              # 24
    "3x3x3": window(0, 1, 2),              # 26
    "W39": window(2, 3, 4),                # 38 offsets + centre
    "5x5x5": window(*range(9)),            # 124
    "7x7x7": window(*range(20)),           # 342
}
TABULATED = ("NN", "NN+AX2", "L1<=2", "3x3x3")


def template_pins(W, ax, origin, with_centre=True):
    """Offset -> pinned value, over the offsets of W (and the centre)."""
    pins = {}
    offs = ([(0, 0, 0)] if with_centre else []) + list(W)
    for o in offs:
        v = pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
        if v is not None:
            pins[o] = v
    return pins


# ---- the minimal table and the completion rules (source block lib.py) ------
def tabulate(W):
    """T_min on W as tmin[v][P] over the 2^|W| offset-indexed profiles."""
    w = len(W)
    assert w <= 26
    pos = {o: i for i, o in enumerate(W)}
    tmin = [np.zeros(1 << w, dtype=bool), np.zeros(1 << w, dtype=bool)]
    for ax, origin in TEMPLATES:
        pins = template_pins(W, ax, origin)
        centre = pins.get((0, 0, 0))
        base = 0
        free = []
        for o in W:
            if o in pins:
                base |= pins[o] << pos[o]
            else:
                free.append(pos[o])
        idx = np.array([base], dtype=np.int64)
        for f in free:
            idx = np.concatenate([idx, idx | (1 << f)])
        for v in ((0, 1) if centre is None else (centre,)):
            tmin[v][idx] = True
    return tmin, tmin[0] | tmin[1]


def popcount(a):
    a = np.asarray(a, dtype=np.uint64)
    c = np.zeros(a.shape, dtype=np.int64)
    while True:
        nz = a != 0
        if not nz.any():
            break
        c += nz
        a = a & (a - np.uint64(1))
    return c


def rule_values(name, W, P):
    """The completion value at never-realised profiles: 0, 1, 2 = both."""
    w = len(W)
    P = np.asarray(P, dtype=np.int64)
    if name == "min":
        return np.full(P.shape, -1, dtype=np.int8)
    if name == "all":
        return np.full(P.shape, 2, dtype=np.int8)
    if name == "c0":
        return np.zeros(P.shape, dtype=np.int8)
    if name == "c1":
        return np.ones(P.shape, dtype=np.int8)
    par = (popcount(P) & 1).astype(np.int8)
    if name == "par":
        return par
    if name == "apar":
        return (1 - par).astype(np.int8)
    if name == "corr":
        out = par.copy()
        out[P == 0] = 1
        out[P == (1 << w) - 1] = 0
        return out
    raise ValueError(name)


RULES = ("min", "c0", "c1", "par", "apar", "corr", "all")


def profile_ints(cfg_bits, box, W):
    grid = sites(box)
    idx = {s: i for i, s in enumerate(grid)}
    N, n = cfg_bits.shape
    out = np.zeros((N, n), dtype=np.int64)
    for j, s in enumerate(grid):
        acc = np.zeros(N, dtype=np.int64)
        for i, o in enumerate(W):
            u = idx[wrap(tuple(s[k] + o[k] for k in range(3)), box)]
            acc |= cfg_bits[:, u].astype(np.int64) << i
        out[:, j] = acc
    return out


def admissible_mask(cfg_bits, box, W, tmin, real, rule):
    """Configurations admissible under T_min(W) completed by `rule`."""
    P = profile_ints(cfg_bits, box, W)
    N, n = cfg_bits.shape
    ok = np.ones(N, dtype=bool)
    for j in range(n):
        c = cfg_bits[:, j].astype(np.int64)
        p = P[:, j]
        ex = np.where(c == 1, tmin[1][p], tmin[0][p])
        rv = rule_values(rule, W, p)
        ok &= ex | ((~real[p]) & ((rv == 2) | (rv == c)))
    return ok


def all_configs(box):
    n = len(sites(box))
    return ((np.arange(1 << n, dtype=np.int64)[:, None]
             >> np.arange(n)) & 1).astype(np.int8)


def cylinder_mask(cfg_bits, box):
    N = cfg_bits.shape[0]
    inside = np.zeros(N, dtype=bool)
    for pins, _ in torus_sectors(box):
        cyl = np.ones(N, dtype=bool)
        for i, v in enumerate(pins):
            if v is not None:
                cyl &= cfg_bits[:, i] == v
        inside |= cyl
    return inside


# ---- CNF encodings (source block lib.py) -----------------------------------
class CNF:
    def __init__(self, nvars: int) -> None:
        self.n = nvars
        self.clauses = []

    def new(self) -> int:
        self.n += 1
        return self.n

    def add(self, cl) -> None:
        self.clauses.append(list(cl))

    def and_gate(self, lits):
        g = self.new()
        for l in lits:
            self.add([-g, l])
        self.add([g] + [-l for l in lits])
        return g

    def or_gate(self, lits):
        g = self.new()
        for l in lits:
            self.add([-l, g])
        self.add([-g] + list(lits))
        return g

    def xor_chain(self, lits):
        if not lits:
            f = self.new()
            self.add([-f])
            return f
        cur = lits[0]
        for l in lits[1:]:
            g = self.new()
            self.add([-g, cur, l])
            self.add([-g, -cur, -l])
            self.add([g, -cur, l])
            self.add([g, cur, -l])
            cur = g
        return cur

    def iff_gate(self, a, b):
        g = self.new()
        self.add([-g, -a, b])
        self.add([-g, a, -b])
        self.add([g, a, b])
        self.add([g, -a, -b])
        return g


def build_cnf(box, W, rule):
    """CNF whose x-models are the configurations admissible under T_min(W)
    completed by `rule`; wrapped offsets, coincident offsets cancel in a
    parity exactly as the record rule's marker clauses apply."""
    grid = sites(box)
    idx = {s: i for i, s in enumerate(grid)}
    n = len(grid)
    cnf = CNF(n)

    def x(s):
        return idx[wrap(s, box)] + 1

    for s in grid:
        ms, ns = [], []
        for ax, origin in TEMPLATES:
            pins = template_pins(W, ax, origin)
            dem_full, dem_prof, ok_full, ok_prof = {}, {}, True, True
            for o, v in pins.items():
                u = x(tuple(s[k] + o[k] for k in range(3)))
                if o != (0, 0, 0):
                    if dem_prof.get(u, v) != v:
                        ok_prof = False
                    dem_prof[u] = v
                if dem_full.get(u, v) != v:
                    ok_full = False
                dem_full[u] = v
            if ok_full:
                ms.append(cnf.and_gate([u if v else -u
                                        for u, v in dem_full.items()]))
            if ok_prof:
                ns.append(cnf.and_gate([u if v else -u
                                        for u, v in dem_prof.items()]))
        if rule == "min":
            cnf.add(ms)
            continue
        if rule == "all":
            for l in ns:
                cnf.add(ms + [-l])
            continue
        mult = {}
        for o in W:
            u = x(tuple(s[k] + o[k] for k in range(3)))
            mult[u] = mult.get(u, 0) + 1
        par = cnf.xor_chain([u for u, m in mult.items() if m % 2 == 1])
        c = x(s)
        if rule == "c0":
            r = -c
        elif rule == "c1":
            r = c
        elif rule == "par":
            r = cnf.iff_gate(c, par)
        elif rule == "apar":
            r = -cnf.iff_gate(c, par)
        elif rule == "corr":
            wins = sorted(mult)
            u0 = cnf.and_gate([-u for u in wins])
            u1 = cnf.and_gate([u for u in wins])
            eq = cnf.iff_gate(c, par)
            r = cnf.or_gate([cnf.and_gate([-u0, -u1, eq]),
                             cnf.and_gate([u0, c]),
                             cnf.and_gate([u1, -c])])
        else:
            raise ValueError(rule)
        for l in ns:
            cnf.add(ms + [-l])
        cnf.add(ms + [r])
    return cnf, n


def cylinder_clauses(box):
    """Clauses excluding every cylinder: what is left are the extras."""
    out = []
    for pins, _ in torus_sectors(box):
        out.append([-(i + 1) if v == 1 else (i + 1)
                    for i, v in enumerate(pins) if v is not None])
    return out


def enumerate_models(solver_cls, cnf, n, extra=(), cap=SAT_CAP):
    models = []
    with solver_cls(bootstrap_with=cnf.clauses + list(extra)) as s:
        while len(models) < cap:
            if not sat_decision(s):
                return models, False
            m = s.get_model()
            bits = tuple(1 if m[i] > 0 else 0 for i in range(n))
            models.append(bits)
            s.add_clause([-(i + 1) if b else (i + 1)
                          for i, b in enumerate(bits)])
    return models, True


def pinned_flip_sat(solver_cls, box, cnf):
    """(admissible pinned-flip configurations, pinned sites tried)."""
    hits = total = 0
    with solver_cls(bootstrap_with=cnf.clauses) as s:
        for pins, _ in torus_sectors(box):
            for f, v in enumerate(pins):
                if v is None:
                    continue
                total += 1
                assum = [((i + 1) if (u if i != f else 1 - u) else -(i + 1))
                         for i, u in enumerate(pins) if u is not None]
                if sat_decision(s, assumptions=assum):
                    hits += 1
    return hits, total


def cylinders_admissible(solver_cls, box, cnf):
    with solver_cls(bootstrap_with=cnf.clauses) as s:
        return all(sat_decision(s, assumptions=[(i + 1) if v else -(i + 1)
                                        for i, v in enumerate(pins)
                                        if v is not None])
                   for pins, _ in torus_sectors(box))


# ---- Burnside (source block lib.py / s1_census.py) -------------------------
def offset_cycles(W, m):
    seen, cycles = set(), []
    for o in W:
        if o in seen:
            continue
        cyc, cur = [], o
        while cur not in seen:
            seen.add(cur)
            cyc.append(cur)
            cur = act(m, cur)
        cycles.append(cyc)
    return cycles


def burnside_all(W):
    tot = sum(1 << len(offset_cycles(W, m)) for m in ROTATIONS)
    assert tot % 24 == 0
    return tot // 24


def orbit_counts(W, tmin, real):
    """(profile orbits, realised orbits, exercised entries, never-realised
    orbits) by Burnside; the identity is counted without materialising the
    2^|W| index array."""
    w = len(W)
    pos = {o: i for i, o in enumerate(W)}
    fix_never = int((~real).sum())
    fix_real = int(real.sum())
    fix_ent = [int(tmin[0].sum()), int(tmin[1].sum())]
    n_orbits = 1 << w
    for m in ROTATIONS[1:]:
        cycles = offset_cycles(W, m)
        k = len(cycles)
        n_orbits += 1 << k
        masks = np.array([sum(1 << pos[o] for o in cyc) for cyc in cycles],
                         dtype=np.int64)
        sel = ((np.arange(1 << k, dtype=np.int64)[:, None]
                >> np.arange(k)) & 1).astype(np.int64)
        P = (sel * masks[None, :]).sum(axis=1)
        fix_never += int((~real[P]).sum())
        fix_real += int(real[P].sum())
        fix_ent[0] += int(tmin[0][P].sum())
        fix_ent[1] += int(tmin[1][P].sum())
    assert n_orbits % 24 == 0 and fix_never % 24 == 0 and fix_real % 24 == 0
    return (n_orbits // 24, fix_real // 24,
            (fix_ent[0] + fix_ent[1]) // 24, fix_never // 24)


# ---- T1 roles (source block s1_census.py) ----------------------------------
def rot_maps(support):
    index = {o: i for i, o in enumerate(support)}
    return [tuple(index[act(transpose(m), support[i])]
                  for i in range(len(support))) for m in ROTATIONS]


def realised_role_pairs(support, ax=0):
    maps = rot_maps(support)
    base = set()
    for site in itertools.product(range(4), range(4), range(4)):
        role = pat_sym(site, ax)
        prof = tuple(pat_sym(tuple(site[k] + o[k] for k in range(3)), ax)
                     for o in support)
        base.add((role, prof))
    out = set()
    for role, prof in base:
        for m in maps:
            out.add((role, tuple(prof[m[i]] for i in range(len(support)))))
    return out


def neighbour_table(box, support):
    index = {s: i for i, s in enumerate(sites(box))}
    return [[index[wrap(tuple(s[k] + o[k] for k in range(3)), box)]
             for o in support] for s in sites(box)]


def dfs_role_admissible(box, support, pairs):
    """Complete solver-free search for the role-rule admissible sets."""
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
            if all(assign[j] in (-1, p[i]) for i, j in enumerate(nb[u])):
                return True
        return False

    def rec(v):
        if v == n:
            found.append(tuple(assign))
            return
        for r in range(5):
            assign[v] = r
            if all(ok(u) for u in involved[v]):
                rec(v + 1)
        assign[v] = -1

    rec(0)
    return found


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
    return out


# ---- T2 the star lemma (source block s2_small_windows.py) ------------------
def overlaps(W):
    """For each offset d the pairs (bit i of the neighbour's profile, index
    in the star) at which the star of the centre already records a value;
    index -1 is the centre itself."""
    star = {(0, 0, 0): -1}
    for i, o in enumerate(W):
        star[o] = i
    ov = {}
    for d in W:
        ov[d] = [(i, star[tuple(d[k] + o2[k] for k in range(3))])
                 for i, o2 in enumerate(W)
                 if tuple(d[k] + o2[k] for k in range(3)) in star]
    return ov


def keyed_counts(W, tmin, real, ov):
    """Sparse recount of the source's flexibility scan: for each offset d,
    the number of realised profiles, of realised profiles of each parity and
    of exercised entries of each value, bincounted by overlap key."""
    w = len(W)
    ridx = np.nonzero(real)[0].astype(np.int64)
    eidx = [np.nonzero(tmin[u])[0].astype(np.int64) for u in (0, 1)]
    rpar = popcount(ridx) & 1
    out = {}
    for d in W:
        bits = [i for i, _ in ov[d]]
        nk = 1 << len(bits)

        def keys(P, bits=bits):
            k = np.zeros(len(P), dtype=np.int64)
            for b, i in enumerate(bits):
                k |= ((P >> i) & 1) << b
            return k

        rk = keys(ridx)
        out[d] = (nk, w - len(bits), np.bincount(rk, minlength=nk),
                  [np.bincount(rk[rpar == u], minlength=nk) for u in (0, 1)],
                  [np.bincount(keys(eidx[u]), minlength=nk) for u in (0, 1)],
                  bits)
    return out


def bad_keys(W, kc, rule, real):
    """(offset -> [bad key mask per neighbour value], triples with no
    completion, triples tried).  A key is good for the value u when some
    completion of the open offsets puts u in the completed menu; the count of
    completions of each parity is exact, so nothing is scanned."""
    w = len(W)
    specials = [s for s in (0, (1 << w) - 1) if not real[s]]
    bm, tot, tried = {}, 0, 0
    for d, (nk, free, cr, crp, ce, bits) in kc.items():
        assert free >= 1
        half = 1 << (free - 1)
        rows = []
        for u in (0, 1):
            zero = np.zeros(nk, dtype=bool)
            if rule == "min":
                good = ce[u] > 0
            elif rule == "all":
                good = (ce[u] > 0) | (cr < (1 << free))
            elif rule == "c0":
                good = (ce[u] > 0) | ((cr < (1 << free)) if u == 0 else zero)
            elif rule == "c1":
                good = (ce[u] > 0) | ((cr < (1 << free)) if u == 1 else zero)
            elif rule == "par":
                good = (ce[u] > 0) | ((half - crp[u]) > 0)
            elif rule == "apar":
                good = (ce[u] > 0) | ((half - crp[1 - u]) > 0)
            elif rule == "corr":
                nev = (half - crp[u]).astype(np.int64)
                for s in specials:
                    ps = bin(s).count("1") & 1
                    cs = 1 if s == 0 else 0
                    if ps == cs:
                        continue
                    key = 0
                    for b, i in enumerate(bits):
                        key |= ((s >> i) & 1) << b
                    nev[key] += (1 if u == cs else 0) - (1 if u == ps else 0)
                good = (ce[u] > 0) | (nev > 0)
            else:
                raise ValueError(rule)
            rows.append(~good)
            tot += int((~good).sum())
            tried += nk
        bm[d] = rows
    return bm, tot, tried


def star_readout(W, tmin, real, ov, bm, rule, chunk=1 << 21):
    """(entries in T* read by their star, entries out of T* read by their
    star).  A star is admissible when every neighbour is OK; the survivors
    are compressed after each offset, so only the first pass is wide."""
    w = len(W)
    idx = {o: i for i, o in enumerate(W)}
    order = sorted(
        W, key=lambda d: (int(bm[d][0].sum()) + int(bm[d][1].sum()))
        / (2 * len(bm[d][0])), reverse=True)
    ok_in = ok_out = 0
    for a in range(0, 1 << w, chunk):
        for v in (0, 1):
            P = np.arange(a, min(a + chunk, 1 << w), dtype=np.int64)
            for d in order:
                if not (bm[d][0].any() or bm[d][1].any()):
                    continue
                u = (P >> idx[d]) & 1
                key = np.zeros(len(P), dtype=np.int64)
                for b, (i, j) in enumerate(ov[d]):
                    bit = (np.full(len(P), v, dtype=np.int64) if j == -1
                           else ((P >> j) & 1))
                    key |= bit << b
                P = P[~np.where(u == 1, bm[d][1][key], bm[d][0][key])]
                if len(P) == 0:
                    break
            if len(P) == 0:
                continue
            in_t = tmin[v][P]
            if rule == "c0":
                in_t = in_t | ((~real[P]) & (v == 0))
            elif rule == "c1":
                in_t = in_t | ((~real[P]) & (v == 1))
            elif rule != "min":
                raise ValueError(rule)
            ok_in += int(in_t.sum())
            ok_out += int((~in_t).sum())
    return ok_in, ok_out


def table_entries(W, tmin, real, rule):
    """Entries of the completed table T*."""
    w = len(W)
    n_ex = int(tmin[0].sum() + tmin[1].sum())
    n_never = (1 << w) - int(real.sum())
    if rule == "min":
        return n_ex
    if rule == "all":
        return n_ex + 2 * n_never
    return n_ex + n_never


# ---- T3 the pinning windows (source block s3_big_windows.py) ---------------
def pinned_flip_pairs(W):
    """Template pairs (tau, tau') agreeing on tau's non-centre pins inside W
    while allowing the other centre value (opposite pin or free centre):
    0 means every realised
    profile at a pinned site has a singleton menu."""
    pins = [template_pins(W, ax, o) for ax, o in TEMPLATES]
    both = 0
    for i, pi in enumerate(pins):
        if (0, 0, 0) not in pi:
            continue
        for j, pj in enumerate(pins):
            if j == i:
                continue
            if all(pj[o] == pi[o] for o in pi if o != (0, 0, 0) and o in pj):
                if ((0, 0, 0) not in pj or pj[(0, 0, 0)] != pi[(0, 0, 0)]):
                    both += 1
    return both


def flexibility_bound(W):
    """The counting certificate of the star lemma on a window too wide to
    tabulate: at every offset d, never-realised non-uniform completions of
    either parity number at least 2^(n_d - 1) - sum_tau 2^(e_tau) - 2."""
    star = {(0, 0, 0)} | set(W)
    rows = []
    for d in W:
        open_offs = [o2 for o2 in W
                     if tuple(d[k] + o2[k] for k in range(3)) not in star]
        n_d = len(open_offs)
        e_max = 0
        real_sum = 0
        for ax, origin in TEMPLATES:
            e = sum(1 for o2 in open_offs
                    if pat_bit(tuple(origin[k] + o2[k] for k in range(3)), ax)
                    is None)
            e_max = max(e_max, e)
            real_sum += 1 << e
        rows.append((d, n_d, e_max, real_sum, (1 << (n_d - 1)) - real_sum - 2))
    worst = min(rows, key=lambda r: r[4])
    return worst, min(r[1] for r in rows), max(r[1] for r in rows)


def f2_rank(M):
    M = M.copy() % 2
    r = 0
    rows, cols = M.shape
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i, c]), None)
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c]:
                M[i] ^= M[r]
        r += 1
        if r == rows:
            break
    return r


def parity_system_rank(box, W):
    """Rank of (I + A_odd) over F2, and whether the wrapped window reaches
    every site at each individual center, including that center. This is a
    necessary geometry check for the conditional nonlinear-to-linear reduction;
    formal matrix rank alone does not prove that reduction."""
    grid = sites(box)
    idx = {s: i for i, s in enumerate(grid)}
    n = len(grid)
    M = np.zeros((n, n), dtype=np.int64)
    whole = True
    for s in grid:
        mult = {}
        for o in W:
            u = idx[wrap(tuple(s[k] + o[k] for k in range(3)), box)]
            mult[u] = mult.get(u, 0) + 1
        whole &= (set(mult) | {idx[s]}) == set(range(n))
        M[idx[s], idx[s]] = 1
        for u, m in mult.items():
            if m % 2 == 1:
                M[idx[s], u] ^= 1
    return f2_rank(M), n, whole


def z3_entry_census(W):
    """Complete entries the zero-edge-bit, single- and double-complement families
    of the 48 templates exercise on Z^3, with their rotation orbits."""
    pos = {o: i for i, o in enumerate(W)}
    bw = {o: 1 << i for i, o in enumerate(W)}
    sea, hop1, hop2 = set(), set(), set()

    def flip(v, P, o):
        return (v ^ 1, P) if o == (0, 0, 0) else (v, P ^ bw[o])

    for ax, origin in TEMPLATES:
        vals = {}
        for o in [(0, 0, 0)] + list(W):
            v = pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
            vals[o] = 0 if v is None else v
        P0 = 0
        for o in W:
            if vals[o]:
                P0 |= bw[o]
        v0 = vals[(0, 0, 0)]
        sea.add((v0, P0))
        edge = [o for o in [(0, 0, 0)] + list(W)
                if pat_bit(tuple(origin[k] + o[k] for k in range(3)), ax)
                is None]
        ones = [flip(v0, P0, o) for o in edge]
        hop1.update(ones)
        for a in range(len(edge)):
            for b in range(a + 1, len(edge)):
                hop2.add(flip(ones[a][0], ones[a][1], edge[b]))
    perms = [[pos[act(m, o)] for o in W] for m in ROTATIONS]

    def orbits(S):
        S = sorted(S)
        n = len(S)
        bits = np.zeros((n, len(W)), dtype=np.uint8)
        vs = np.zeros((n, 1), dtype=np.uint8)
        for r, (v, P) in enumerate(S):
            vs[r, 0] = v
            for i in range(len(W)):
                bits[r, i] = (P >> i) & 1
        best = None
        for pm in perms:
            q = np.zeros_like(bits)
            q[:, pm] = bits
            pk = np.packbits(q, axis=1)
            if best is None:
                best = pk.copy()
                continue
            lt = np.zeros(n, dtype=bool)
            eq = np.ones(n, dtype=bool)
            for c in range(pk.shape[1]):
                lt |= eq & (pk[:, c] < best[:, c])
                eq &= pk[:, c] == best[:, c]
            best[lt] = pk[lt]
        return len({r.tobytes()
                    for r in np.concatenate([vs, best], axis=1)})

    a, b, c = sea, hop1 | sea, hop2 | hop1 | sea
    return ((len(a), len(b), len(c)),
            (orbits(a), orbits(b), orbits(c)))


def partial_pattern_census(W, k):
    """Partial patterns of the centre and k recorded offsets that are
    template-consistent: R5's projection reading, which the marginal reading
    reproduces on the exercised part."""
    off_idx = {(0, 0, 0): 0}
    for i, o in enumerate(W):
        off_idx[o] = i + 1
    A = np.full((48, len(W) + 1), 3, dtype=np.uint8)
    for t, (ax, origin) in enumerate(TEMPLATES):
        for o, v in template_pins(W, ax, origin).items():
            A[t, off_idx[o]] = 1 << v
    npos = k + 1
    n_code = 1 << npos
    C = np.zeros((npos, 4), dtype=np.uint32)
    for p in range(npos):
        for s in range(4):
            m = 0
            for code in range(n_code):
                if (s >> ((code >> p) & 1)) & 1:
                    m |= 1 << code
            C[p, s] = m
    combos = np.array(list(itertools.combinations(range(1, len(W) + 1), k)),
                      dtype=np.int64)
    acc = np.zeros(len(combos), dtype=np.uint32)
    for t in range(48):
        m = np.full(len(combos), C[0, A[t, 0]], dtype=np.uint32)
        for j in range(k):
            m &= C[j + 1, A[t, combos[:, j]]]
        acc |= m
    return int(np.unpackbits(acc.view(np.uint8)).sum()), len(combos) * n_code


# ---- T4 the physics (source block s4_physics.py) ---------------------------
NN6 = WINDOWS["NN"]


def sector_data(box, which=0):
    secs = torus_sectors(box)
    pins, (ax, origin) = secs[which]
    grid = sites(box)
    es = [i for i, v in enumerate(pins) if v is None]
    corners = [i for i, s in enumerate(grid)
               if pat_sym(tuple(s[k] + origin[k] for k in range(3)), ax)
               in (C0, C1)]
    return secs, pins, ax, origin, grid, es, corners


def families(box, pins, grid, es, corners):
    """Legacy sea/hop keys denote zero-edge bits/single complements, not a
    quantum sea or guaranteed nonzero hop. Double complements and one
    representative of each vertex-parity class in breadth-first order."""
    base = [(v if v is not None else 0) for v in pins]
    star = {c: [grid.index(wrap(tuple(grid[c][k] + d[k] for k in range(3)),
                                box)) for d in NN6] for c in corners}
    fam = {"sea": [tuple(base)], "hop": [], "double": []}
    for e in es:
        c = list(base)
        c[e] ^= 1
        fam["hop"].append(tuple(c))
    for a, b in list(itertools.combinations(es, 2))[
            :(276 if len(es) == 24 else 200)]:
        c = list(base)
        c[a] ^= 1
        c[b] ^= 1
        fam["double"].append(tuple(c))

    def parity(cfg):
        return tuple(sum(cfg[e] for e in star[c] if pins[e] is None) % 2
                     for c in corners)

    classes = {parity(base): tuple(base)}
    frontier = [tuple(base)]
    cap = min(1 << (len(corners) - 1), 128)
    while frontier and len(classes) < cap:
        nxt = []
        for cfg in frontier:
            for e in es:
                c2 = list(cfg)
                c2[e] ^= 1
                p = parity(c2)
                if p not in classes:
                    classes[p] = tuple(c2)
                    nxt.append(tuple(c2))
        frontier = nxt
    fam["parity class"] = [classes[k] for k in sorted(classes)][:cap]
    return fam


def hop_transitions(solver_cls, box, cnf, fam, es):
    """Every edge-site complement applied to every family member, re-tested
    under assumptions; actual hopping additionally needs a nonzero amplitude."""
    tested = bad = 0
    with solver_cls(bootstrap_with=cnf.clauses) as s:
        for cfgs in fam.values():
            for cfg in cfgs:
                for e in es:
                    c2 = list(cfg)
                    c2[e] ^= 1
                    tested += 1
                    if not sat_decision(s, assumptions=[(i + 1) if b else -(i + 1)
                                                for i, b in enumerate(c2)]):
                        bad += 1
    return tested, bad


def extra_structure(box, W, extras):
    """Weights, distance to the nearest cylinder in pinned-site mismatches,
    template-consistent sites, and whether any extra is a corner pin-field
    defect."""
    secs = torus_sectors(box)
    grid = sites(box)
    idx = {s: i for i, s in enumerate(grid)}
    tpins = [template_pins(W, ax, o) for ax, o in TEMPLATES]
    wts, dists, cons_counts, pinfield = set(), [], set(), 0
    for x in extras:
        wts.add(sum(x))
        dists.append(min(sum(1 for i, v in enumerate(p)
                             if v is not None and v != x[i])
                         for p, _ in secs))
        cons = 0
        for s in grid:
            for tp in tpins:
                if all(x[idx[wrap(tuple(s[k] + o[k] for k in range(3)),
                                  box)]] == v for o, v in tp.items()):
                    cons += 1
                    break
        cons_counts.add(cons)
        for p, (ax_, o_) in secs:
            if all(x[i] == v for i, v in enumerate(p)
                   if v is not None
                   and pat_sym(tuple(grid[i][k] + o_[k] for k in range(3)),
                               ax_) not in (C0, C1)):
                pinfield += 1
                break
    return sorted(wts), (min(dists), max(dists)), sorted(cons_counts), pinfield


def isolated(solver_cls, cnf, n, extras):
    """Admissible configurations at single-flip distance from an extra."""
    nadj = 0
    with solver_cls(bootstrap_with=cnf.clauses) as s:
        for x in extras:
            for i in range(n):
                y = [b ^ (1 if j == i else 0) for j, b in enumerate(x)]
                if sat_decision(s, assumptions=[(j + 1) if b else -(j + 1)
                                        for j, b in enumerate(y)]):
                    nadj += 1
    return nadj, len(extras) * n


def two_copy_unsat(solver_cls, box, W, rule):
    """Is there an admissible non-cylinder configuration with an admissible
    configuration at Hamming distance 1?  Two copies of the CNF and a one-hot
    selector for the flipped site."""
    cnf1, n = build_cnf(box, W, rule)
    cnf2, _ = build_cnf(box, W, rule)
    off = cnf1.n
    clauses = list(cnf1.clauses)
    for cl in cnf2.clauses:
        clauses.append([(l + off) if l > 0 else (l - off) for l in cl])
    clauses.extend(cylinder_clauses(box))
    top = cnf1.n + cnf2.n
    ys = list(range(top + 1, top + 1 + n))
    clauses.append(ys)
    for i in range(n):
        for j in range(i + 1, n):
            clauses.append([-ys[i], -ys[j]])
    for s in range(n):
        x1, x2, y = s + 1, s + 1 + off, ys[s]
        clauses += [[-y, x1, x2], [-y, -x1, -x2], [y, -x1, x2], [y, x1, -x2]]
    with solver_cls(bootstrap_with=clauses) as s:
        return not sat_decision(s)


def coarse_graph(box, which=0):
    """Corners as vertices, edge sites as bonds; a coarse direction of length
    2 carries doubled bonds."""
    secs, pins, ax, origin, grid, es, corners = sector_data(box, which)
    cidx = {c: i for i, c in enumerate(corners)}
    bonds = []
    for e in es:
        s = grid[e]
        t = tuple(s[k] + origin[k] for k in range(3))
        a = [k for k in range(3) if t[k] & 1][0]
        u = wrap(tuple(s[k] - (1 if k == a else 0) for k in range(3)), box)
        v = wrap(tuple(s[k] + (1 if k == a else 0) for k in range(3)), box)
        bonds.append((cidx[grid.index(u)], cidx[grid.index(v)], a, u))
    return corners, bonds, ax, origin


def ks_matrix(box, twist, which=0):
    """The KS sign field on the coarse graph, with a twist on the wrap."""
    corners, bonds, ax, origin = coarse_graph(box, which)
    V = len(corners)
    M = np.zeros((V, V))
    grid = sites(box)
    L = [box[k] // 2 for k in range(3)]
    for i, j, a, u in bonds:
        cv = [((grid[corners[i]][k] + origin[k]) // 2) % L[k]
              for k in range(3)]
        if a == 0:
            eta = 1
        elif a == 1:
            eta = (-1) ** cv[0]
        else:
            eta = (-1) ** (cv[0] + cv[1])
        if twist[a] and cv[a] == L[a] - 1:
            eta = -eta
        M[i, j] += eta
        M[j, i] += eta
    return M, len(bonds)


def sea_energy(box):
    rows = []
    for twist in itertools.product((0, 1), repeat=3):
        M, nb = ks_matrix(box, twist)
        ev = np.sort(np.linalg.eigvalsh(M))
        V = len(ev)
        half = ev[:V // 2].sum()
        best = min((ev[:N].sum(), N) for N in range(0, V + 1, 2))
        rows.append((half, twist, best, ev[V // 2] - ev[V // 2 - 1], ev, nb))
    rows.sort(key=lambda r: (r[0], r[1]))
    return rows[0]


def flux_scan(box):
    """Every bond-sign class on the coarse graph, gauge fixed to +1 on a
    spanning tree; the minimum half-filled free-fermion energy."""
    corners, bonds, ax, origin = coarse_graph(box)
    V = len(corners)
    tree, seen, frontier = set(), {0}, [0]
    adj = {}
    for b, (i, j, a, u) in enumerate(bonds):
        adj.setdefault(i, []).append((j, b))
        adj.setdefault(j, []).append((i, b))
    while frontier:
        nxt = []
        for i in frontier:
            for j, b in adj[i]:
                if j not in seen:
                    seen.add(j)
                    tree.add(b)
                    nxt.append(j)
        frontier = nxt
    assert len(tree) == V - 1
    free_b = [b for b in range(len(bonds)) if b not in tree]
    pos = {b: i for i, b in enumerate(free_b)}
    nfree = len(free_b)
    hist = {}
    best = None
    chunk = 1 << 17
    assert chunk * V * V <= CELL_CAP * 8
    for start in range(0, 1 << nfree, chunk):
        codes = np.arange(start, min(start + chunk, 1 << nfree))
        Ms = np.zeros((len(codes), V, V))
        for b, (i, j, a, u) in enumerate(bonds):
            sgn = (np.ones(len(codes)) if b in tree
                   else 1.0 - 2.0 * ((codes >> pos[b]) & 1))
            Ms[:, i, j] += sgn
            Ms[:, j, i] += sgn
        ev = np.sort(np.linalg.eigvalsh(Ms), axis=1)
        half = ev[:, :V // 2].sum(axis=1)
        k = int(np.argmin(half))
        if best is None or half[k] < best:
            best = float(half[k])
        for h in np.round(half, 6):
            hist[float(h)] = hist.get(float(h), 0) + 1
    return nfree, best, hist[min(hist)], len(hist)


def odd_corner_census(box):
    """The vertex-parity map of one sector over F2: its rank is corners - 1
    (the product of all B_v is the identity), so the edge assignments split
    as C(corners, N) 2^(edges - rank) over the even N."""
    secs, pins, ax, origin, grid, es, corners = sector_data(box)
    star = {c: [grid.index(wrap(tuple(grid[c][k] + d[k] for k in range(3)),
                                box)) for d in NN6] for c in corners}
    M = np.zeros((len(corners), len(es)), dtype=np.int64)
    for a, c in enumerate(corners):
        for e in star[c]:
            M[a, es.index(e)] = 1
    r = f2_rank(M)
    counts = {N: math.comb(len(corners), N) * (1 << (len(es) - r))
              for N in range(0, len(corners) + 1, 2)}
    return len(es), len(corners), r, counts

def pinned_pair_control():
    """Exercise the actual generic predicate on free/opposite center alternatives."""
    global TEMPLATES, template_pins
    old_templates, old_pins = TEMPLATES, template_pins
    try:
        TEMPLATES = [(0, 0), (1, 0)]
        toy = [{(0, 0, 0): 0, (1, 0, 0): 0}, {(1, 0, 0): 0}]
        template_pins = lambda W, a, o: toy[a]
        free = pinned_flip_pairs([(1, 0, 0)])
        toy[1][(0, 0, 0)] = 1
        opposite = pinned_flip_pairs([(1, 0, 0)])
        return free, opposite
    finally:
        TEMPLATES, template_pins = old_templates, old_pins


def local_coverage(box, W):
    return len({wrap(o, box) for o in W} | {(0, 0, 0)})


# ---- the run ---------------------------------------------------------------
def main() -> int:                                          # noqa: C901
    t0 = time.time()
    checks = Checks()
    require_inputs()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    probe = PROBE_PATH.read_text(encoding="utf-8")
    bksf = BKSF_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    try:
        from pysat.solvers import Cadical153
        have_sat = True
    except Exception:
        Cadical153 = None
        have_sat = False
        raise RuntimeError("complete claim coverage requires CaDiCaL")

    print("external_scientific_inputs: none bar the declared quoted rows")
    print("integrity_reads: axioms, deep probe, BKSF census, this note")
    print("construction: exact enumeration on named tori and over Z^3")
    print("negative_scope: named containing-table classes and finite tori only")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("interpretation_guard: minimal_axioms Lattice, Qubit, "
          "Admissibility, Record")
    print("declared_math: cubic rotations, record windows, Burnside counts, "
          "F2 ranks, spectra")
    print("unverified_historical_rows: 8x4x4 totals 17/16 (s3A.030, s3B.005), "
          "membership/isolation verified; completeness not established here")
    print("solver_mode: pysat present; CaDiCaL on 4x2x2, 4x4x4, 8x4x4"
          if have_sat else
          "solver_mode: pysat absent; the solver-free 4x2x2 enumeration and "
          "the Z^3 censuses still run")

    checks.check("audit-input-paths", "declared inputs exist and are unique",
                 all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS)
                 and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)))
    checks.check("audit-timeout", "the declared timeout is 300 seconds",
                 AUDIT_TIMEOUT_SEC == 300)

    # ---------- supplied surface -------------------------------------------
    checks.check(
        "axiom-admissibility", "the nearest-neighbor rule is quoted",
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations." in axiom_flat
        and "one fixed nearest-neighbor admissibility rule" in note_flat)
    checks.check(
        "axiom-support", "admissible read as the support",
        "denotes its support -- on finite menus, exactly the possibilities of "
        "nonzero probability" in axiom_flat
        and "denotes its support" in note_flat)
    checks.check(
        "axiom-record", "a site with no record cannot be read",
        "Only records are readable. A readout value is determined by record "
        "content alone. A site with no record cannot be read." in axiom_flat
        and "A site with no record cannot be read" in note_flat)
    checks.check(
        "parent-deep-probe", "the declared deep-probe comparator is present, not a physical law",
        "number of covariant label-equivariant tables = 3^24" in probe)
    checks.check(
        "parent-encoding", "the separate finite BKSF/marker context is present",
        "claim_type: bounded_theorem" in bksf
        and "superlattice marker" in normalize(bksf))

    # ---------- T1 : the censuses ------------------------------------------
    boxes = ((4, 2, 2), (4, 4, 2), (4, 4, 4), (8, 4, 4))
    nsec, nfree = [], []
    for box in boxes:
        secs = torus_sectors(box)
        free = {sum(1 for v in pins if v is None) for pins, _ in secs}
        assert len(free) == 1
        nsec.append(len(secs))
        nfree.append(free.pop())
    checks.check(
        "T1-sectors", "16 / 32 / 48 / 48 cylinders, 48 x 2^24 on 4x4x4",
        nsec == [16, 32, 48, 48] and nfree == [6, 12, 24, 48]
        and nsec[0] * (1 << nfree[0]) == 1024
        and nsec[2] * (1 << nfree[2]) == 805306368,
        (nsec, nfree))

    NN = WINDOWS["NN"]
    AX2 = WINDOWS["NN+AX2"]
    pairs_nn = realised_role_pairs(NN)
    profs = {p for _, p in pairs_nn}
    maps_nn = rot_maps(NN)
    orbits_nn = {min(tuple(p[m[i]] for i in range(len(NN))) for m in maps_nn)
                 for p in profs}
    checks.check("T1-role-table", "T0: 18 pairs, 17 profiles of 5^6, 6 orbits",
                 (len(pairs_nn), len(profs), len(orbits_nn)) == (18, 17, 6)
                 and 5 ** 6 == 15625,
                 (len(pairs_nn), len(profs), len(orbits_nn)))
    adj = {(r, s) for r, p in pairs_nn for s in p}
    checks.check("T1-role-adjacency", "8 of 25 role adjacencies realised, 17 never", (len(adj), 25 - len(adj)) == (8, 17), len(adj))
    pairs_ax2 = realised_role_pairs(AX2)
    role_rows = []
    for box in ((4, 2, 2), (4, 4, 2), (4, 4, 4)):
        a_nn = dfs_role_admissible(box, NN, pairs_nn)
        a_ax = dfs_role_admissible(box, AX2, pairs_ax2)
        secs = sector_role_configs(box)
        role_rows.append((len(a_nn), len(a_ax), len(secs),
                          set(a_ax) == secs, secs <= set(a_nn)))
    checks.check(
        "T1-role-rules", "NN admits 32 / 128 / 2,048; 12 offsets give the sectors",
        [r[0] for r in role_rows] == [32, 128, 2048]
        and [r[1] for r in role_rows] == [16, 32, 48]
        and [r[2] for r in role_rows] == [16, 32, 48]
        and all(r[3] and r[4] for r in role_rows)
        and len(pairs_ax2) == 22,
        role_rows)

    TAB = {}
    ex_rows, real_rows, both_rows = [], [], []
    for name in TABULATED:
        tmin, real = tabulate(WINDOWS[name])
        TAB[name] = (tmin, real)
        ex_rows.append(int(tmin[0].sum() + tmin[1].sum()))
        real_rows.append(int(real.sum()))
        both_rows.append(int((tmin[0] & tmin[1]).sum()))
    checks.check(
        "T1-record-tables", "exercised entries 128 / 1,638 / 391,233 / 101,626",
        ex_rows == [128, 1638, 391233, 101626]
        and real_rows == [64, 998, 197633, 98537]
        and both_rows == [64, 640, 193600, 3089],
        (ex_rows, real_rows, both_rows))
    checks.check(
        "T1-nn-permissive", "at NN the minimal law is already all-permissive",
        ex_rows[0] == 2 * (1 << 6) and both_rows[0] == 64
        and bool(TAB["NN"][1].all()))

    disj = {}
    for name in ("W39", "5x5x5"):
        W = WINDOWS[name]
        pins = [template_pins(W, ax, o) for ax, o in TEMPLATES]
        cons = sum(1 for i in range(48) for j in range(i + 1, 48)
                   if all(pins[i][o] == pins[j][o] for o in pins[i]
                          if o in pins[j]))
        free = sorted({len(W) + 1 - len(p) for p in pins})
        tot = sum(1 << (len(W) + 1 - len(p)) for p in pins)
        disj[name] = (cons, free, tot)
    checks.check(
        "T1-5x5x5-disjoint", "5x5x5: 0 of 1,128 pairs, 2^57.05 of 2^125 exercised",
        disj["5x5x5"][0] == 0 and disj["5x5x5"][1] == [36, 44, 51, 54]
        and disj["5x5x5"][2] == 148935859368886272
        and abs(math.log2(disj["5x5x5"][2]) - 57.05) < 0.01,
        disj["5x5x5"])
    checks.check(
        "T1-W39-pairs", "W39: 159 of 1,128 template pairs consistent",
        disj["W39"][0] == 159 and disj["W39"][1] == [0, 7, 24],
        disj["W39"][:2])

    box422 = (4, 2, 2)
    cfg422 = all_configs(box422)
    inside422 = cylinder_mask(cfg422, box422)
    ladder = []
    for name in TABULATED:
        tmin, real = TAB[name]
        adm = admissible_mask(cfg422, box422, WINDOWS[name], tmin, real, "min")
        ladder.append((int(adm.sum()), int((adm & ~inside422).sum()),
                       bool((adm | ~inside422).all())))
    checks.check(
        "T1-ladder-422", "4x2x2 extras 64,512 / 13,981 / 186 / 154",
        [r[1] for r in ladder] == [64512, 13981, 186, 154]
        and [r[0] for r in ladder] == [65536, 15005, 1210, 1178]
        and all(r[2] for r in ladder) and int(inside422.sum()) == 1024,
        ladder)

    orb = [orbit_counts(WINDOWS[n], *TAB[n]) for n in TABULATED]
    checks.check(
        "T1-orbits", "never-realised orbits 0 / 157 / 694,711 / 2,798,417",
        [r[3] for r in orb] == [0, 157, 694711, 2798417]
        and [r[0] for r in orb] == [10, 240, 703360, 2802752]
        and all(burnside_all(WINDOWS[n]) == r[0]
                for n, r in zip(TABULATED, orb)),
        orb)

    e24, c24, r24, cnt24 = odd_corner_census((4, 4, 4))
    checks.check(
        "T1-odd-corner", "4x4x4 odd corners 131,072 / 3,670,016 / 9,175,040",
        (e24, c24, r24) == (24, 8, 7)
        and cnt24 == {0: 131072, 2: 3670016, 4: 9175040, 6: 3670016,
                      8: 131072}
        and sum(cnt24.values()) == 1 << 24,
        (e24, c24, r24))
    # ---------- T2 : the tabulated windows ---------------------------------
    exp422 = {
        "NN+AX2": {"min": 13981, "c0": 13981, "c1": 64512, "par": 40349,
                   "apar": 23056, "corr": 40349, "all": 64512},
        "L1<=2": {"min": 186, "c0": 833, "c1": 699, "par": 725, "apar": 607,
                  "corr": 636, "all": 64512},
        "3x3x3": {"min": 154, "c0": 175, "c1": 883, "par": 187, "apar": 887,
                  "corr": 210, "all": 20714},
    }
    for name in ("NN+AX2", "L1<=2", "3x3x3"):
        W = WINDOWS[name]
        tmin, real = TAB[name]
        got, sets = {}, {}
        for rule in RULES:
            adm = admissible_mask(cfg422, box422, W, tmin, real, rule)
            got[rule] = int((adm & ~inside422).sum())
            sets[rule] = adm
        checks.check(
            f"T2-422-{name}", "the 4x2x2 sets of the seven rules match",
            got == exp422[name]
            and all(bool((sets[r] | ~inside422).all()) for r in RULES),
            got)
        if have_sat:
            eq = []
            for rule in ("min", "c0", "par", "corr"):
                cnf, n = build_cnf(box422, W, rule)
                models, capped = enumerate_models(Cadical153, cnf, n,
                                                  cap=70000)
                want = {tuple(int(b) for b in cfg422[i])
                        for i in np.nonzero(sets[rule])[0]}
                eq.append((not capped) and set(models) == want)
            checks.check(
                f"T2-422-cadical-{name}", "CaDiCaL agrees as sets for min, c0, par, corr",
                all(eq), eq)
    del sets

    if have_sat:
        flips = []
        for name, rule in (("NN+AX2", "min"), ("L1<=2", "min"),
                           ("L1<=2", "par"), ("L1<=2", "corr"),
                           ("3x3x3", "min"), ("3x3x3", "par"),
                           ("3x3x3", "corr")):
            cnf, n = build_cnf((4, 4, 4), WINDOWS[name], rule)
            flips.append(pinned_flip_sat(Cadical153, (4, 4, 4), cnf))
        checks.check(
            "T2-flip-leak", "4x4x4 pinned flips 1,920 / 0 / 384 / 384 / 0 / 768 / 768",
            [h for h, _ in flips] == [1920, 0, 384, 384, 0, 768, 768]
            and {t for _, t in flips} == {1920},
            flips)

    exp_tried = {"NN+AX2": 144, "L1<=2": 74496, "3x3x3": 1624064}
    exp_bad = {"NN+AX2": {"min": 0, "c0": 0, "c1": 0},
               "L1<=2": {"min": 55848, "c0": 28008, "c1": 27840},
               "3x3x3": {"min": 1587236, "c0": 797466, "c1": 789770}}
    exp_read = {
        "NN+AX2": {"min": (1638, 1638, 6554, 6554),
                   "c0": (4736, 4736, 3456, 3456),
                   "c1": (4736, 4736, 3456, 3456)},
        "L1<=2": {"min": (391233, 391233, 33163199, 4132),
                  "c0": (16970816, 414296, 16583616, 45170),
                  "c1": (16970816, 416332, 16583616, 10503)},
        "3x3x3": {"min": (101626, 101626, 134116102, 7486),
                  "c0": (67111953, 127281, 67105775, 1024996),
                  "c1": (67111953, 109097, 67105775, 124785)}}
    tried_got, bad_got, flex_got, read_got, menus = {}, {}, {}, {}, {}
    for name in ("NN+AX2", "L1<=2", "3x3x3"):
        W = WINDOWS[name]
        tmin, real = TAB[name]
        ov = overlaps(W)
        kc = keyed_counts(W, tmin, real, ov)
        bad_got[name], flex_got[name], read_got[name] = {}, {}, {}
        menus[name] = {}
        for rule in RULES:
            bm, tot, tried = bad_keys(W, kc, rule, real)
            tried_got[name] = tried
            menus[name][rule] = (rule != "min") or bool(real.all())
            if rule in ("par", "apar", "corr", "all"):
                flex_got[name][rule] = tot
                continue
            bad_got[name][rule] = tot
            n_in = table_entries(W, tmin, real, rule)
            n_out = 2 * (1 << len(W)) - n_in
            if tot == 0:
                read_got[name][rule] = (n_in, n_in, n_out, n_out)
                continue
            ok_in, ok_out = star_readout(W, tmin, real, ov, bm, rule)
            read_got[name][rule] = (n_in, ok_in, n_out, ok_out)
        del kc
    checks.check(
        "T2-flexibility", "par, apar, corr: 0 of 144 / 74,496 / 1,624,064 fail",
        all(v == 0 for d in flex_got.values() for v in d.values())
        and [tried_got[n] for n in ("NN+AX2", "L1<=2", "3x3x3")]
        == [144, 74496, 1624064],
        (flex_got, tried_got))
    checks.check(
        "T2-flex-min", "min fails 55,848 and 1,587,236; c0 28,008 and 797,466",
        bad_got == exp_bad, bad_got)
    checks.check(
        "T2-readout-min", "the designed law is blind on 134,108,616 of 134,217,728",
        all(read_got[n]["min"] == exp_read[n]["min"]
            for n in ("NN+AX2", "L1<=2", "3x3x3")),
        {n: read_got[n]["min"] for n in read_got})
    checks.check(
        "T2-readout-const", "constant completions blind on 133,065,451 and 133,983,846",
        all(read_got[n][r] == exp_read[n][r]
            for n in ("NN+AX2", "L1<=2", "3x3x3") for r in ("c0", "c1")),
        {n: read_got[n] for n in ("L1<=2", "3x3x3")})
    checks.check(
        "T2-readout-flexible", "par/apar/corr read all 16,970,816 and 67,111,953 entries",
        [table_entries(WINDOWS[n], *TAB[n], "par")
         for n in ("NN+AX2", "L1<=2", "3x3x3")]
        == [4736, 16970816, 67111953]
        and all(v == 0 for d in flex_got.values() for v in d.values()))
    checks.check(
        "T2-menus", "menus nonempty for the six completions, empty for min",
        all(menus[n][r] for n in menus for r in RULES if r != "min")
        and not any(menus[n]["min"] for n in ("NN+AX2", "L1<=2", "3x3x3")),
        menus)

    # ---------- T3 : the pinning windows -----------------------------------
    W555 = WINDOWS["5x5x5"]
    checks.check(
        "T3-pinned-flip-lemma", "0 pairs on W39, 5x5x5 and 7x7x7",
        [pinned_flip_pairs(WINDOWS[n]) for n in ("W39", "5x5x5", "7x7x7")]
        == [0, 0, 0])
    bounds = {n: flexibility_bound(WINDOWS[n])
              for n in ("W39", "5x5x5", "7x7x7")}
    w5, lo5, hi5 = bounds["5x5x5"]
    checks.check(
        "T3-flexibility-bound", "counting margin 16,625,822 at the worst 5x5x5 offset",
        w5[0] == (-1, 0, 0) and (w5[1], w5[2], w5[3], w5[4])
        == (25, 13, 151392, 16625822) and (lo5, hi5) == (25, 98)
        and bounds["W39"][0][4] == 255065528
        and bounds["7x7x7"][0][4] > 2.8e14,
        (w5, lo5, hi5, bounds["W39"][0][4], bounds["7x7x7"][0][4]))

    r4, n4, whole4 = parity_system_rank((4, 4, 4), W555)
    r8, n8, whole8 = parity_system_rank((8, 4, 4), W555)
    checks.check(
        "T3-F2-ranks", "formal F2 ranks 64/128; a local window covers only the smaller torus",
        (r4, n4, whole4, r8, n8, whole8) == (64, 64, True, 128, 128, False),
        (r4, n4, r8, n8))

    if have_sat:
        ex444, cyl444, flip444 = {}, {}, {}
        for rule in ("min", "c0", "c1", "par", "apar", "corr"):
            cnf, n = build_cnf((4, 4, 4), W555, rule)
            models, capped = enumerate_models(
                Cadical153, cnf, n, extra=cylinder_clauses((4, 4, 4)))
            assert not capped
            ex444[rule] = models
            cyl444[rule] = cylinders_admissible(Cadical153, (4, 4, 4), cnf)
            flip444[rule] = pinned_flip_sat(Cadical153, (4, 4, 4), cnf)
        counts444 = [len(ex444[r]) for r in
                     ("min", "c0", "c1", "par", "apar", "corr")]
        zero = tuple([0] * 64)
        one = tuple([1] * 64)
        checks.check(
            "T3-extras-4x4x4", "4x4x4 5x5x5 extras 0 / 1 / 1 / 1 / 1 / 0",
            counts444 == [0, 1, 1, 1, 1, 0]
            and all(cyl444.values())
            and {v for v in flip444.values()} == {(0, 1920)}
            and ex444["c0"][0] == zero and ex444["par"][0] == zero
            and ex444["c1"][0] == one and ex444["apar"][0] == one,
            counts444)
        checks.check(
            "T3-complete-records-blind", "par and c0 share their 4x4x4 admissible set",
            set(ex444["par"]) == set(ex444["c0"])
            and set(ex444["apar"]) == set(ex444["c1"])
            and ex444["corr"] == ex444["min"] == [])
        exW39 = {}
        for rule in ("par", "c0"):
            cnf, n = build_cnf((4, 4, 4), WINDOWS["W39"], rule)
            models, capped = enumerate_models(
                Cadical153, cnf, n, extra=cylinder_clauses((4, 4, 4)))
            exW39[rule] = (len(models), capped,
                           sorted({sum(m) for m in models}))
        checks.check(
            "T3-W39-extras", "W39 on 4x4x4: 3,457 extras under par and c0",
            all(v == (3457, False, [0, 4, 8]) for v in exW39.values()),
            exW39)
        ex844 = {}
        for rule in ("min", "c1"):
            cnf, n = build_cnf((8, 4, 4), W555, rule)
            models, capped = enumerate_models(
                Cadical153, cnf, n, extra=cylinder_clauses((8, 4, 4)))
            ex844[rule] = (len(models), capped,
                           cylinders_admissible(Cadical153, (8, 4, 4), cnf),
                           pinned_flip_sat(Cadical153, (8, 4, 4), cnf))
        checks.check(
            "T3-8x4x4-minimal", "8x4x4: min 0 extras, c1 1, 0 of 3,840 pinned flips",
            ex844["min"][:3] == (0, False, True)
            and ex844["c1"][:3] == (1, False, True)
            and {v[3] for v in ex844.values()} == {(0, 3840)},
            ex844)

    sizes, orbs = z3_entry_census(W555)
    checks.check(
        "T3-z3-census", "Z^3 entries 48 / 2,298 / 54,642",
        sizes == (48, 2298, 54642) and orbs == (9, 114, 2421),
        (sizes, orbs))
    part = [partial_pattern_census(W555, k) for k in (1, 2, 3)]
    checks.check(
        "T3-partial-patterns", "496, 61,008 and 4,814,888 of 4,961,984 patterns",
        part == [(496, 496), (61008, 61008), (4814888, 4961984)], part)

    # ---------- T4 : the physics -------------------------------------------
    if have_sat:
        hops = {}
        cnf844 = {}
        for box in ((4, 4, 4), (8, 4, 4)):
            secs, pins, ax, origin, grid, es, corners = sector_data(box)
            fam = families(box, pins, grid, es, corners)
            for rule in ("par", "corr"):
                cnf, n = build_cnf(box, W555, rule)
                if box == (8, 4, 4):
                    cnf844[rule] = (cnf, n)
                hops[(box, rule)] = hop_transitions(Cadical153, box, cnf,
                                                    fam, es)
        checks.check(
            "T4-hops", "10,296 and 18,096 formal complement tests, 0 leaving",
            [hops[((4, 4, 4), r)] for r in ("par", "corr")]
            == [(10296, 0), (10296, 0)]
            and [hops[((8, 4, 4), r)] for r in ("par", "corr")]
            == [(18096, 0), (18096, 0)],
            hops)

        cert = []
        for word in EXTRA_CERTIFICATE_8X4X4:
            v = int(word, 16)
            cert.append(tuple((v >> i) & 1 for i in range(128)))
        assert len(cert) == len(set(cert)) == 16
        wts, dist, cons, pinfield = extra_structure((8, 4, 4), W555, cert)
        cert_par = cert + [tuple([0] * 128)]
        adm_cert = {}
        for rule, xs in (("corr", cert), ("par", cert_par)):
            cnf, n = cnf844[rule]
            with Cadical153(bootstrap_with=cnf.clauses) as s:
                adm_cert[rule] = sum(
                    sat_decision(s, assumptions=[(i + 1) if b else -(i + 1)
                                         for i, b in enumerate(x)])
                    for x in xs)
        checks.check(
            "T4-extras-8x4x4", "16 specified extras: weight 24, 32 sites, distance 16, no defect",
            adm_cert["corr"] == 16 and adm_cert["par"] == 17
            and wts == [24] and dist == (16, 16) and cons == [32]
            and pinfield == 0
            and all(not any(all(x[i] == v for i, v in enumerate(p)
                                if v is not None)
                            for p, _ in torus_sectors((8, 4, 4)))
                    for x in cert),
            (wts, dist, cons, pinfield, adm_cert))
        checks.check(
            "T4-extras-quoted", "historical 16/17 completeness quotation retained but unverified",
            (QUOTED_8X4X4_CORR_EXTRAS, QUOTED_8X4X4_PAR_EXTRAS) == (16, 17)
            and len(cert) == QUOTED_8X4X4_CORR_EXTRAS
            and len(cert_par) == QUOTED_8X4X4_PAR_EXTRAS)
        iso = {}
        for rule, xs in (("corr", cert), ("par", cert_par)):
            cnf, n = cnf844[rule]
            iso[rule] = isolated(Cadical153, cnf, n, xs)
        cnf, n = build_cnf((4, 4, 4), W555, "par")
        iso444 = isolated(Cadical153, cnf, n, [tuple([0] * 64)])
        checks.check(
            "T4-isolation", "0 admissible neighbours in 2,048 / 2,176 / 64 solves",
            iso["corr"] == (0, 2048) and iso["par"] == (0, 2176)
            and iso444 == (0, 64),
            (iso, iso444))
        checks.check(
            "T4-two-copy", "4x4x4 corr two-copy adjacency SAT: UNSAT",
            two_copy_unsat(Cadical153, (4, 4, 4), W555, "corr"))

    sea4 = sea_energy((4, 4, 4))
    sea8 = sea_energy((8, 4, 4))
    checks.check(
        "T4-sea-4x4x4", "selected coarse KS E = -8 sqrt 3, gap 6.928203, twist (0,0,0)",
        abs(sea4[0] + 8 * math.sqrt(3)) < 1e-9 and sea4[1] == (0, 0, 0)
        and sea4[2][1] == 4 and abs(sea4[3] - 6.928203) < 1e-6
        and sea4[5] == 24 and len(sea4[4]) == 8
        and all(abs(abs(v) - 2 * math.sqrt(3)) < 1e-9 for v in sea4[4]),
        (sea4[0], sea4[1], sea4[3]))
    checks.check(
        "T4-sea-8x4x4", "selected coarse KS E = -8 sqrt 10, gap 6.324555, twist (1,0,0)",
        abs(sea8[0] + 8 * math.sqrt(10)) < 1e-9 and sea8[1] == (1, 0, 0)
        and sea8[2][1] == 8 and abs(sea8[3] - 6.324555) < 1e-6
        and sea8[5] == 48 and len(sea8[4]) == 16
        and all(abs(abs(v) - math.sqrt(10)) < 1e-9 for v in sea8[4]),
        (sea8[0], sea8[1], sea8[3]))
    nfree, best, attain, ndist = flux_scan((4, 4, 4))
    checks.check(
        "T4-flux-classes", "131,072 sign classes: numerical KS minimum, 146 six-decimal energy bins",
        (nfree, attain, ndist) == (17, 1, 146)
        and abs(best + 8 * math.sqrt(3)) < 1e-6,
        (nfree, best, attain, ndist))
    checks.check(
        "T4-extras-energy", "conditional zero-diagonal isolated-state offsets from the two fixed-matrix energies",
        abs(0.0 - sea4[0] - 13.856406) < 1e-5
        and abs(0.0 - sea8[0] - 25.298221) < 1e-5)
    e48, c48, r48, cnt48 = odd_corner_census((8, 4, 4))
    checks.check(
        "T4-odd-corner-8x4x4", "8x4x4 parity-map rank 15, fibre 2^33",
        (e48, c48, r48) == (48, 16, 15)
        and cnt48[0] == 1 << 33 and cnt48[8] == math.comb(16, 8) * (1 << 33)
        and sum(cnt48.values()) == 1 << 48,
        (e48, c48, r48))

    checks.check("C-pinned-free-center", "both free-center and opposite-pinned alternatives prevent the lemma",
                 pinned_pair_control() == (1, 2), pinned_pair_control())
    checks.check("C-local-coverage", "one 5x5x5 window reaches 64/64 but only 80/128 sites",
                 local_coverage((4, 4, 4), W555) == 64
                 and local_coverage((8, 4, 4), W555) == 80)
    tm, real = TAB["NN+AX2"]
    full = [np.ones_like(real), np.ones_like(real)]
    full_real = np.ones_like(real)
    _, full_bad, full_tried = bad_keys(WINDOWS["NN+AX2"],
        keyed_counts(WINDOWS["NN+AX2"], full, full_real, overlaps(WINDOWS["NN+AX2"])), "min", full_real)
    checks.check("C-completion-family", "full table is flexible but adds 358 entries at realised profiles",
                 sum(int(((~tm[v]) & real).sum()) for v in (0, 1)) == 358
                 and full_bad == 0 and full_tried == 144)
    zero_hop_rows = []
    for box in ((4, 4, 4), (8, 4, 4)):
        _, pins, _, _, grid, es, corners = sector_data(box)
        zero_cfg = families(box, pins, grid, es, corners)["sea"][0]
        _, bonds, _, _ = coarse_graph(box)
        parity = [(-1) ** sum(zero_cfg[es[j]] for j, (a, b, _, _) in enumerate(bonds)
                              if a == v or b == v) for v in range(len(corners))]
        coeff = [(parity[a] - parity[b]) / 2 for a, b, _, _ in bonds]
        zero_hop_rows.append((len(coeff), sum(x != 0 for x in coeff)))
    checks.check("C-zero-bit-not-hopping", "24/48 formal complements from zero bits have zero supplied hop amplitudes",
                 zero_hop_rows == [(24, 0), (48, 0)], zero_hop_rows)
    exact_squares = []
    for box, twist, q in [((4, 4, 4), (0, 0, 0), 12), ((8, 4, 4), (1, 0, 0), 10)]:
        matrix, _ = ks_matrix(box, twist)
        integer = matrix.astype(np.int64)
        exact_squares.append(np.array_equal(matrix, integer)
                             and np.array_equal(integer @ integer, q * np.eye(len(integer), dtype=np.int64))
                             and np.trace(integer) == 0)
    checks.check("C-fixed-matrix-squares", "integer H^2=12I/10I and trace zero certify the two chosen spectra",
                 all(exact_squares))

    # ---------- note hygiene ------------------------------------------------
    lines = len(note.splitlines())
    checks.check("note-length", "the note stays under 330 lines", lines < 330,
                 lines)
    checks.check(
        "note-registry-id", "the note declares its registry id",
        "readable_matter_law_on_5x5x5_window_parity_completion_2026_09_04"
        in note)
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
        "note-wording", "superlattice role pattern; nothing overclaimed",
        "superlattice role pattern" in note_flat
        and "the matter law is derived" not in note_flat
        and "readable at nearest neighbour" not in note_flat)
    checks.check(
        "note-scope", "no law selected; bounded scope stated",
        "no physical law is selected" in note_flat and "claim_scope:" in note
        and "promoted" not in note.lower() and "new axiom" not in note.lower())
    checks.check(
        "note-interfaces", "the note names its parent pull requests",
        all(tok in note for tok in
            ("#7977", "#7939", "#7928", "#7934", "#7889", "#7891", "#7885")))
    checks.check(
        "note-numbers", "the note carries its counts",
        all(tok in note for tok in
            ("2,798,417", "1,624,064", "134,108,616", "16,625,822", "3,457",
             "16,970,816", "10,296", "18,096", "54,642", "4,814,888",
             "2^57.05", "131,072")))
    checks.check(
        "note-boundary", "the quoted and undecided rows are named",
        all(tok in note for tok in ("s3B.005", "8x4x4", "7x7x7"))
        and "nothing is derived from the axioms" in note_flat
        and "not computed" in note_flat)

    print("per_element: 2 record values, 48 templates, 124 offsets")
    print("per_site: every site of every named torus and window")
    print("per_mode: 8 and 16 coarse modes, free-fermion spectra")
    print("per_block: support cylinders, 16 verified isolated witnesses; physical encoding not supplied")
    print("lattice_wide: 4x2x2, 4x4x2, 4x4x4, 8x4x4; Z^3 censuses")
    print(f"elapsed_sec: {time.time() - t0:.1f}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
