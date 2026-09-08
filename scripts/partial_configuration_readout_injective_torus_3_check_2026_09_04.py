#!/usr/bin/env python3
"""Conditional injectivity of a finite static partial-configuration map.

The runner recomputes, with no sampling, no seed and no random number
generator:

T1  the encoding -- the covariant label-equivariant census (729 ternary
    profiles, 57 proper-cubic orbits, 9 flip-fixed, 24 flip-pairs, 3^24
    tables, a 48-bit demand word), the fact that `mask(c) subset of S` is a
    local condition on 7-site stars (a subshift of finite type), its CNF form
    with one-hot ternary site variables and forbidden profile codes as
    clauses, and the translation x 24-rotation x flip reduction that pins the
    demanding site at the origin;
T2  72 finite digit-confined targets: 50 direct witnesses and 22 negative
    decisions requiring three actual complete solvers. The original 55-leaf
    seed-component search is retained without whole-space completeness.
    Emitted DRUP trace length is not independent proof checking;
T3  the injectivity criterion and its closure over a declared pool of
    verified realisable masks -- 96 requirements, decided twice, once by a
    from-scratch subcube-cover procedure and once by SAT;
T4  the 4^3 and 5^3 readout from declared witness configurations;
T5  the 3-cycle mirror identity and two specified centered-box comparisons,
    with both original and additional witness occupancies, not minima.

Open is a supplied configuration-domain symbol, not a readout of an absent
site. No physical preparation, membership oracle or full probability law is
derived. Only the declared finite domains and finite pool coverage are tested.
"""

from __future__ import annotations

import sys
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 300

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THE_PARTIAL_CONFIGURATION_READOUT_IS_INJECTIVE_ON_THE_3_TORUS_"
    "EVERY_LAW_IS_VISIBLE_TO_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-04.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PROBE_REL = "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md"
Q8_REL = (
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
TIME_REL = (
    "docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_"
    "BOUNDED_NOTE_2026-07-03.md"
)

AUDIT_INPUT_PATHS = (
    "docs/THE_PARTIAL_CONFIGURATION_READOUT_IS_INJECTIVE_ON_THE_3_TORUS_"
    "EVERY_LAW_IS_VISIBLE_TO_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md",
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_"
    "BOUNDED_NOTE_2026-07-03.md",
)

assert AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL, PROBE_REL, Q8_REL, TIME_REL)

EXPECTED_INPUT_SHA256 = {'docs/THE_PARTIAL_CONFIGURATION_READOUT_IS_INJECTIVE_ON_THE_3_TORUS_EVERY_LAW_IS_VISIBLE_TO_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-04.md': '012936153e56ea7667e0db0ea9fd2d0b680f595110374c548dd00ecd975acd54', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md': 'c277ca66054a47ac0183e1a7d806acf0fee01167915d8b70746125d73a5a56f4', 'docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md': 'c08d7a351c2ae40d921b0e996ca817b4f789c51072fbf2b6eb9a2de6f6fe8967', 'docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md': '3dab4d91c2fd016f00bdab64beb0376c0e800c1026f5cfb862233e34927f6d9f'}

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL
PROBE_PATH = ROOT / PROBE_REL
Q8_PATH = ROOT / Q8_REL
TIME_PATH = ROOT / TIME_REL

OPEN = -1
DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}
POW3 = [3 ** j for j in range(6)]
CELL_CAP = 16_000_000          # no dense array above 4096 x 4096 entries

# Storage code for a site: 0 = unrecorded (open), 1 = record 0, 2 = record 1.
# Digit-confined targets, in the canonical order every declared witness block
# uses: index 0 = {2i}, 1 = {2i+1}, 2 = {2i,2i+1}.

# The declared pair-23 witness on the 3^3 torus: a complete configuration,
# every one of the 27 sites recorded, whose demand mask is exactly {46, 47}.
PAIR23_WITNESS = "101000110011010110001111100"

# Declared joint witnesses for the three digits that no digit-confined mask
# reaches on the 3^3 torus: pair, target, and the configuration. Each mask is
# recomputed here; none is asserted.
JOINT_WITNESSES = (
    (11, 0, "101...0...........0........"),
    (11, 1, "001...0...........0........"),
    (16, 0, "1110..0...........0........"),
    (16, 1, "0110..0...........0........"),
    (17, 0, "1010..1...........0........"),
    (17, 1, "0010..1...........0........"),
)

# Declared configuration index set for the mask-invariance cross-check: the
# first 4096 integers of the base-3 expansion over the 27 sites, plus the
# arithmetic progression of step 1021 (a prime) and length 4096.
INVARIANCE_BLOCK = 4096
INVARIANCE_STEP = 1021
INVARIANCE_TERMS = 4096

# Declared block-set family for the antitonicity cross-check: nested pairs
# built from the base-2 expansions of j * floor(2^24 / 32), j = 0..31.
ANTITONE_FAMILY = 32


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


# ------------------------------------------------------------- census -------
def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations():
    """Return (direction permutation, 3x3 matrix) for each proper rotation."""
    out = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            det = permutation_sign(perm)
            for value in signs:
                det *= value
            if det != 1:
                continue
            matrix = [[0, 0, 0] for _ in range(3)]
            for row in range(3):
                matrix[row][perm[row]] = signs[row]
            image = []
            for direction in DIRECTIONS:
                rotated = tuple(
                    sum(matrix[r][c] * direction[c] for c in range(3)) for r in range(3)
                )
                image.append(DIR_INDEX[rotated])
            out.append((tuple(image), tuple(tuple(row) for row in matrix)))
    return tuple(out)


ROTATIONS = proper_cubic_rotations()


def rotate_profile(profile, rotation):
    return tuple(profile[rotation[i]] for i in range(6))


def flip_profile(profile):
    return tuple(v if v == OPEN else 1 - v for v in profile)


def canonical(profile):
    return min(rotate_profile(profile, r) for r, _ in ROTATIONS)


def census(profiles):
    """Return (canonical map, orbit reps, flip-fixed orbits, flip-pairs)."""
    cmap = {p: canonical(p) for p in profiles}
    reps = sorted(set(cmap.values()))
    self_flip, pairs, seen = [], [], set()
    for rep in reps:
        if rep in seen:
            continue
        partner = cmap[flip_profile(rep)]
        if partner == rep:
            self_flip.append(rep)
            seen.add(rep)
        else:
            pairs.append((rep, partner))
            seen.update({rep, partner})
    return cmap, reps, self_flip, pairs


def code_to_profile(code: int):
    out = []
    for j in range(6):
        digit = (code // POW3[j]) % 3
        out.append(OPEN if digit == 0 else digit - 1)
    return tuple(out)


def profile_to_code(profile) -> int:
    return sum((0 if v == OPEN else v + 1) * POW3[j] for j, v in enumerate(profile))


TERNARY = [code_to_profile(c) for c in range(729)]
TMAP, TREPS, TSELF, TPAIRS = census(TERNARY)
REP_INDEX = {rep: i for i, rep in enumerate(TREPS)}
ORBIT_OF = np.array([REP_INDEX[TMAP[TERNARY[c]]] for c in range(729)], dtype=np.int16)

SIDE_OF_ORBIT = {}
for _i, (_a, _b) in enumerate(TPAIRS):
    SIDE_OF_ORBIT[REP_INDEX[_a]] = (_i, 0)
    SIDE_OF_ORBIT[REP_INDEX[_b]] = (_i, 1)

NPAIR = len(TPAIRS)
NBITS = 2 * NPAIR

# DEMAND[code, value] = the demand bit a record of `value` on profile `code`
# raises, or -1 when the orbit is flip-fixed (its menu is {0,1} for every
# table in the family, so such a record asks nothing of any table).
#   bit 2i   raised by (A_i, 1) and (B_i, 0)  -> forbids digit i = 0
#   bit 2i+1 raised by (A_i, 0) and (B_i, 1)  -> forbids digit i = 1
DEMAND = np.full((729, 2), -1, dtype=np.int8)
for _c in range(729):
    _o = int(ORBIT_OF[_c])
    if _o in SIDE_OF_ORBIT:
        _i, _s = SIDE_OF_ORBIT[_o]
        DEMAND[_c, 0] = 2 * _i + 1 if _s == 0 else 2 * _i
        DEMAND[_c, 1] = 2 * _i if _s == 0 else 2 * _i + 1


def allowed_codes(bits):
    """(G0, G1): the profile codes on which a record of value v may sit when
    every demand bit raised must lie in `bits` (flip-fixed orbits ask
    nothing)."""
    wanted = set(bits)
    out = []
    for v in (0, 1):
        out.append({p for p in range(729)
                    if int(DEMAND[p, v]) < 0 or int(DEMAND[p, v]) in wanted})
    return out[0], out[1]


PINNED_CODES = {p for p in range(729) if int(DEMAND[p, 0]) < 0}


# -------------------------------------------------------------- torus -------
class Torus:
    """The L^3 torus, its neighbour table, and two mask paths."""

    def __init__(self, size: int) -> None:
        self.L = size
        self.N = size ** 3
        self.coord = [None] * self.N
        for x in range(size):
            for y in range(size):
                for z in range(size):
                    self.coord[self.sid(x, y, z)] = (x, y, z)
        table = np.zeros((self.N, 6), dtype=np.int64)
        for site in range(self.N):
            x, y, z = self.coord[site]
            for d, (dx, dy, dz) in enumerate(DIRECTIONS):
                table[site, d] = self.sid(x + dx, y + dy, z + dz)
        self.NBR = table

    def sid(self, x: int, y: int, z: int) -> int:
        size = self.L
        return (size * size) * (x % size) + size * (y % size) + (z % size)

    def profile_at(self, config, site: int):
        return tuple(
            OPEN if config[self.NBR[site, d]] == 0
            else int(config[self.NBR[site, d]]) - 1
            for d in range(6)
        )

    def mask_scalar(self, config) -> int:
        """Scalar path: rebuild each profile tuple and re-canonicalise."""
        mask = 0
        for site in range(self.N):
            if config[site] == 0:
                continue
            orbit = REP_INDEX[canonical(self.profile_at(config, site))]
            if orbit not in SIDE_OF_ORBIT:
                continue
            pair, side = SIDE_OF_ORBIT[orbit]
            value = int(config[site]) - 1
            if side == 0:
                mask |= 1 << (2 * pair + (1 if value == 0 else 0))
            else:
                mask |= 1 << (2 * pair + (0 if value == 0 else 1))
        return mask

    def masks_vectorised(self, configs: np.ndarray) -> np.ndarray:
        """configs: (B, N) uint8 storage codes. Returns (B,) int64 masks."""
        batch = configs.shape[0]
        out = np.zeros(batch, dtype=np.int64)
        one = np.int64(1)
        for site in range(self.N):
            column = configs[:, site]
            recorded = column != 0
            if not recorded.any():
                continue
            acc = np.zeros(batch, dtype=np.int32)
            for d in range(6):
                acc += configs[:, self.NBR[site, d]].astype(np.int32) * POW3[d]
            bit = DEMAND[acc, np.clip(column.astype(np.int64) - 1, 0, 1)]
            good = recorded & (bit >= 0)
            if good.any():
                out[good] |= one << bit[good].astype(np.int64)
        return out

    def star_legal(self, config, bits) -> bool:
        """The local test: every recorded site's 7-site star is allowed."""
        good0, good1 = allowed_codes(bits)
        for site in range(self.N):
            if config[site] == 0:
                continue
            code = profile_to_code(self.profile_at(config, site))
            if code not in (good0, good1)[int(config[site]) - 1]:
                return False
        return True


def parse_config(text: str) -> np.ndarray:
    return np.array([0 if ch == "." else int(ch) + 1 for ch in text], dtype=np.uint8)


def bits_of(mask: int) -> set:
    return {b for b in range(NBITS) if (mask >> b) & 1}


# ---------------------------------------------------------- CNF encoder -----
class CNF:
    def __init__(self) -> None:
        self.n = 0
        self.clauses = []

    def new(self, count: int = 1):
        first = self.n + 1
        self.n += count
        return first if count == 1 else list(range(first, first + count))

    def add(self, clause) -> None:
        self.clauses.append(list(clause))


def forbid_trie(cnf, head, litfun, allowed) -> None:
    """Forbid every 6-digit ternary code outside `allowed`, via a prefix trie
    so that a wholly forbidden subtree costs one short clause."""
    stack = [(0, 0, [])]
    while stack:
        depth, base, lits = stack.pop()
        if depth == 6:
            if base not in allowed:
                cnf.add([head] + lits)
            continue
        step = POW3[depth]
        whole = True
        for k in range(3 ** (6 - depth)):
            if (base + k * step) in allowed:
                whole = False
                break
        if whole:
            cnf.add([head] + lits)
            continue
        for digit in range(3):
            stack.append((depth + 1, base + digit * step,
                          lits + [-litfun(depth, digit)]))


def bit_realisers(bit: int):
    return [(v, p) for v in (0, 1) for p in range(729) if int(DEMAND[p, v]) == bit]


def build_cnf(tor: Torus, bits, seed=None, require=()):
    """CNF for: some partial configuration on `tor` has mask contained in
    `bits`, agrees with `seed`, and realises every bit in `require`."""
    good0, good1 = allowed_codes(bits)
    cnf = CNF()
    variables = [cnf.new(3) for _ in range(tor.N)]
    for site in range(tor.N):
        a, b, c = variables[site]
        cnf.add([a, b, c])
        cnf.add([-a, -b])
        cnf.add([-a, -c])
        cnf.add([-b, -c])
    for site in range(tor.N):
        nbr = tor.NBR[site]

        def litfun(j, digit, nbr=nbr):
            return variables[int(nbr[j])][digit]

        for value, allowed in ((0, good0), (1, good1)):
            forbid_trie(cnf, -variables[site][value + 1], litfun, allowed)
    if seed:
        for site, code in seed.items():
            cnf.add([variables[site][code]])
    for bit in require:
        selectors = []
        for site in range(tor.N):
            nbr = tor.NBR[site]
            for value, code in bit_realisers(bit):
                sel = cnf.new()
                selectors.append(sel)
                cnf.add([-sel, variables[site][value + 1]])
                for j in range(6):
                    cnf.add([-sel, variables[int(nbr[j])][(code // POW3[j]) % 3]])
        cnf.add(selectors)
    return cnf, variables


def sat_solve(cnf, name="cadical195", with_proof=False):
    from pysat.solvers import Solver

    kwargs = dict(name=name, bootstrap_with=cnf.clauses)
    if with_proof:
        kwargs["with_proof"] = True
    solver = Solver(**kwargs)
    sat = solver.solve()
    if sat is not True and sat is not False:
        solver.delete()
        raise RuntimeError(f"indeterminate result from required solver {name}")
    model = solver.get_model() if sat else None
    proof = solver.get_proof() if (with_proof and not sat) else None
    solver.delete()
    return sat, model, proof


def decode(model, variables, count) -> np.ndarray:
    positive = {lit for lit in model if lit > 0}
    config = np.zeros(count, dtype=np.uint8)
    for site in range(count):
        for code in range(3):
            if variables[site][code] in positive:
                config[site] = code
    return config


def seed_for(tor: Torus, pair: int, bit: int):
    """The demanding site pinned at the origin, carrying the canonical side-A
    representative of its flip-pair. Bit 2i is raised by (A_i, 1)."""
    rep = TPAIRS[pair][0]
    value = 1 if bit % 2 == 0 else 0
    seed = {0: value + 1}
    for j in range(6):
        seed[int(tor.NBR[0, j])] = 0 if rep[j] == OPEN else rep[j] + 1
    return seed


# ------------------------------- seed-component enumeration ----------------
def enumerate_legal(tor: Torus, bits, seed):
    """Enumerate only the seed's connected recorded component.

    Unvisited sites are left open. Disconnected recorded extensions are omitted;
    the count is not whole-space enumeration and cannot certify target absence.
    """
    allowed = [sorted(s) for s in allowed_codes(bits)]
    config = np.full(tor.N, -1, dtype=np.int8)
    for site, code in seed.items():
        config[site] = code
    masks, count = set(), 0

    def feasible(site: int) -> bool:
        value = config[site] - 1
        known = [(j, int(config[int(tor.NBR[site, j])])) for j in range(6)
                 if config[int(tor.NBR[site, j])] >= 0]
        for code in allowed[value]:
            if all((code // POW3[j]) % 3 == d for j, d in known):
                return True
        return False

    def frontier():
        best, key = None, None
        for site in range(tor.N):
            if config[site] < 1:
                continue
            for j in range(6):
                target = int(tor.NBR[site, j])
                if config[target] < 0:
                    undecided = sum(1 for jj in range(6)
                                    if config[int(tor.NBR[site, jj])] < 0)
                    if key is None or (undecided, target) < key:
                        key, best = (undecided, target), target
        return best

    def walk():
        nonlocal count
        for site in range(tor.N):
            if config[site] >= 1 and not feasible(site):
                return
        target = frontier()
        if target is None:
            full = np.where(config < 0, 0, config).astype(np.uint8)
            masks.add(tor.mask_scalar(full))
            count += 1
            return
        for value in (0, 1, 2):
            config[target] = value
            walk()
            config[target] = -1

    sys.setrecursionlimit(10000)
    walk()
    return masks, count


# ----------------------- the criterion, decided without a solver ------------
def subcubes(pool, pair: int, value: int, strict: bool):
    """Each realisable mask that carries bit 2*pair+value serves a subcube of
    the deterministic laws on the other 23 digits: at every other pair the
    mask fixes the one digit value it does not forbid, and a mask carrying
    both bits of some other pair serves none."""
    out = []
    for mask in pool:
        own = (mask >> (2 * pair)) & 3
        if strict:
            if own != (1 << value):
                continue
        elif not (own >> value) & 1:
            continue
        fixed = held = 0
        blocked = False
        for other in range(NPAIR):
            if other == pair:
                continue
            here = (mask >> (2 * other)) & 3
            if here == 3:
                blocked = True
                break
            if here == 1:
                fixed |= 1 << other
                held |= 1 << other
            elif here == 2:
                fixed |= 1 << other
        if not blocked:
            out.append((fixed, held))
    return out


def cube_covered(cubes) -> bool:
    """Do the subcubes cover every deterministic law on the free pairs?
    Split on the most frequently fixed coordinate; a subcube fixing nothing
    covers everything, and an empty list leaves a law unserved."""
    if not cubes:
        return False
    if any(fixed == 0 for fixed, _ in cubes):
        return True
    tally = Counter()
    for fixed, _ in cubes:
        rest = fixed
        while rest:
            low = rest & -rest
            tally[low.bit_length() - 1] += 1
            rest ^= low
    pick = max(tally, key=tally.get)
    bit = 1 << pick
    for side in (0, 1):
        narrowed = [(fixed & ~bit, held & ~bit) for fixed, held in cubes
                    if not fixed & bit or bool(held & bit) == bool(side)]
        if not cube_covered(narrowed):
            return False
    return True


def criterion_var(pair: int, value: int) -> int:
    return 1 + 3 * pair + value


def criterion_clauses(pool, pair: int, kind: str):
    """The abstraction CNF: a satisfying assignment is a legal block set that
    no mask in the pool serves, so UNSAT is the requirement."""
    maximal = kind.startswith("C")
    value = int(kind[1])
    clauses = []
    for other in range(NPAIR):
        clauses += [[criterion_var(other, 0), criterion_var(other, 1),
                     criterion_var(other, 2)],
                    [-criterion_var(other, 0), -criterion_var(other, 1)],
                    [-criterion_var(other, 0), -criterion_var(other, 2)],
                    [-criterion_var(other, 1), -criterion_var(other, 2)]]
        if maximal and other != pair:
            clauses.append([-criterion_var(other, 2)])
    if not maximal:
        clauses.append([criterion_var(pair, 2)])
    for mask in pool:
        own = (mask >> (2 * pair)) & 3
        if maximal:
            if own != (1 << value):
                continue
        elif not (own >> value) & 1:
            continue
        clause = [criterion_var(b // 2, b % 2) for b in bits_of(mask)
                  if not (maximal and b // 2 == pair)]
        if not clause:
            return None
        clauses.append(clause)
    return clauses


# ------------------------------------------------- declared witnesses ------
# Declared 3^3 witnesses, in the canonical order (pair 0..23) x (target
# {2i}, {2i+1}, {2i,2i+1}); "-" marks a slot no configuration realises.
# 27 trits: "." unrecorded, "0"/"1" a record carrying that value.
L3_WITNESS_BLOCK = """
1.0........................ 0.0........................
1.0.0........0............. 100........................
000........................ 100.........111.........111
1.0...0.............0...0.1 0.0...0.............0...0.0
1.0...0.............0...0.0 100.110....01.10...0...0.11
000.1001....01.0.1......111 100.1.00...000......11.1.11
- 001..1001.1...0.1......0...
101...0...0..1..1..0..1.01. 111...00...011.00...0..0111
011...0.1..0.....0....00.11 111...0.....1..0...00100.11
1000..0.................... 000011011..................
- 1010..0...1.100.1..0.1....1
001001001..0..0..0..1..1..1 101011001.0..1..1..0..1..0.
1.0.1100..11......00....... 0.0.1001..10......01.......
1.0..00......0.0.100...1.11 1.1...00...01..1.00..0...11
0.1.010...0110.1..0..1...1. 1.1.1000..11.10...00.......
100...0.....1000..0..0....1 000...000.....0...000...000
100..000..1111..0.0..001.00 -
- -
111.01000.10....10000.01111 011..001..0.....000.1.00.11
111.0.0.0..01...1000..01.11 100...1...........0.....0..
000...111.....1...000...111 100.01100.100...10011.01011
- 000000000.........000000000
- 10100.011.....1...01011.100
001001001..0..0..0001001001 10101100..00011.0000.011101
- -
- -
- -
- 01100.101.........01011.100
- 111111111.........000000000
0111..1...000110110111..1.. -
1000..0..0........0........ 000000000000000000000000000
- 10101101.01010001.00.11...1
- -
- 0110010010101..1..0101..1..
111001001010......010...... -
- 101000110011010110001111100
"""

# Declared 4^3 witnesses, same order, 64 trits, site index 16x + 4y + z.
L4_WITNESS_BLOCK = """
1..0............................................................
0..0............................................................
1.00............................................................
1010............................................................
0000............................................................
10.0.............................................0.0.........111
1..0........0......................................0........0..1
0..0........0......................................0........0..0
1..0........0......................................0........0..0
1000.1.1..000.....1.01.0..1..010............10.0.0101....1..0...
0000..0...0.0....0.011.1........0...1....00.0........001.1111111
10.0.10.010.011....01..0..0.0100....1....00011......01.1...1.01.
10.1........0....................................0.0....1..10110
00.1........0....................................1.1....1..01100
10.1........0....................................0.0........0110
1101..0.110.0.0...1...1.1...0.101.001...10001.1...0.0...0...011.
0101.101....0101.001.1.101.0....1010.010....1010.110.0.010.1....
1101....11..00...1..0...1......010010.1.1...10....0...1.0.00..11
1010001101010011........1..10..01100010111001010........0..01..1
0000000.1111000....111.....0.11..1.1..00.1.01..0...1.111...011.0
10.00100.0.00001.0100.1.10.00.1......0................0..111..0.
10.10.......0.......................1..1.0..11...0.00110.0..0.1.
00110.0.01110110.0.11100.....1.0.0.11100.0.10.......1100.0.1.0.0
10010.1.1.0.0110.0..011.0.0.011.100111001.0.1.0....10.101.1.0.10
1..0.....1.100.1.011..0011000011......111..0.1.00...0..1.....1..
0.00....0...0......1.1...0..1..1.1...1..10...0010.1100.11.0.11..
1.00.10.01..0....10.............01..............0...............
1..1........0.............................1.110.0..01...1.1.0.0.
0.11..0001..01.1..00....0..01.01.0.0.110....10.10.111...1.010.0.
1.01.10.01..0....10.............01..............0...............
10.0........0...............0...1.0...01....1...0010.1.1.10...0.
00.0.000.1..0110.110.110.00..00.1..11.110.100..00...0.10111.1111
10.0.0..110001...000..0...11.1.00100.0.0.0111...0.1.0...1.001.1.
1001.1..01..0....1..............01..............0...............
0011.0..11..0....0..............11..............0...............
1001.110.1..0....1101.010.0........0....0.11.0110....1.0.0110011
1111.....0..0000....0..0.10..1....111.11.100..000000..00..111111
0111..0..1010.01..1.....110...0.1..1100.00110.1.0.0011..0.1..1..
11.1......000.00.....1....11..110...1.....00..0000..1.....11..11
10.0.1000101110..01.11..0.1..0111....00....010000...0.11..01011.
00.0.0..1.0.11.........0...1..010.0....01...110.011111.100.00.1.
1000..1.00.01.....0.1.1.0...0...0...1...1.0..0000...01.0.1111111
1000001..00.0101.11.110.011110101..1101011010.11001001010..01.00
0010011101.10.10.0000010001.0000.010011.011100100.11111111.10111
10100111.1110110..0010100110.00000.0011001010010011011.111..0101
1001011011000110.0.111000011.0.111000110100101100011.0.1.0.11100
00.10..1.10.01.0.........100111...0.....10.1.0..0..1..0..0......
100100.100..01...01.01001100100...10...011011011010010010.111111
1111000011110000.0001.1100.0111..000111.00.01.1101110.0.11010.0.
01.10.......0.......1.......1..10...1..01.10...001.1......10....
11110..0...00..0.00..0.1...1.0.1.1.1110.0.00011.000.....1.11....
10.10.......1.......0.......0...11..100100..01..00.0....110..10.
00110.11..0.1001.1.01.001..0.1..1...10.1.01...100.100...1...1..0
100101..01.010.1...0...00.0...11..1000111001...00...01.111...0.0
11010.......1.....0.........0.1......10.1.0.01100.0.01..1.....1.
01.10.......1.......1.......1..00.1.11000.....1001.1..0.0.11....
11.100.10..01100..100.1.1..11.00..10.100.1010011001.1.01110.0011
11.11.......1...................................00.00.......0...
01.11.......1...................................01.11.......1...
1101110110001000.1.100.0.111.0.0110111011000100000.0.1.1.0.0.111
1010011111010111011111011010110110000010010100100101100000101000
0000001111110011000000000011000000000011111100110011111111111111
1010011111110111011111111111111110100111111101110101101001111010
1011001101000000001000111101111111011100001000000100110010111111
0001001111110100000100010111010000010000000001110011111111111111
1011011111110111011111111111111100010000000000000010000100000001
1111011110000000000000011110111111111101001000000000010010111111
0111011100000000010001001111111111011101000000000001000111111111
1111000..1..000.0100....01.0....01010.01...10.010100....01.0....
100101.10110100.0.1.01.10...1...0.1.1.0.10.010..0..01.0.1.10..1.
0011001111001100011101110100010011011101000100010000000011111111
1011011100001000010111100000000101001000111101110000000011111111
"""

# Declared 5^3 witnesses, same order, 125 trits, site index 25x + 5y + z.
L5_WITNESS_BLOCK = """
1...0........................................................................................................................
0...0........................................................................................................................
1.0.0......................0.................................................................................................
10100........................................................................................................................
00..0................................................................................................1..1................1001
10..0................................................................................................0..0................1111
1...0...............0...................................................................................0...............0...1
0...0...............0...................................................................................0...............0...0
1...0...............0...................................................................................0...............0...0
100.0............01.0..10..10....0.........0..0111..10...11...010.111..000.0...1100.1....0.....110.....1.1..10.11..00011.1.0.
00..0............1..0......01..0110.0100..101..001.001..........1....1.11...................0.1..11..11.1...0.111.0.10001.001
10.00..11..1.11.0.1.00.0..1..0...0.001.11..0....11.1....1.000011.1..1..001.1001.1..111.00..1.0....0..0.11.00.0.0..1..11...001
10001..1............0.1....1....1....0...................0....0....1....10..11.0.0.....1101..1....0...0..10...1..00.1..10.1.1
00..1...............0................................................................................1..1....0..110.00..11.0.
100.1..1.0.....0...10..01...10.....11...00..10.0..0..100.0....1..1.1.01......1..11001.001110010..110.1...0.1.0..1..1.0.0.100.
11..1........10....00..................0........................1.....11....01...110.0.001.1...00.11.0..0....000.11110010..0.
01..1...............0................................................................................1..1.0..01011010..01..0.
110.1...............0...0.10.01...0...01...01....1...1010.10.0..1......00.1..1..1...0.110.0.0.1011...00.11011...100..0.1.1..0
10..00..............0................................................................................01100....1.01.1.01.0....
001100....1....1....0........................................................................................................
10..00..............0................................................................................011000101111101011101010
10..10..............0................................................................................01000.1..1.0..1.0..0.1..
00..10....111.......0...............0........................0....1..........000...1.0.01101..01..1..11.1......1001...0.1..1.
10..10..............0................................................................................01000.1..1.0..110010.0..
1.100.00..11...0....0.....00......................11.......................0........................0........................
0.110.01..10...1....0.....01......................10.......................1........................0........................
1...0...............0...............................................................................0.1101.0.1.10...1.0.00...
1...1...............0...............................................................................0...01...1.0...1.001011..
0...1...............0.......01..001..110...101....0..00.00.1.11.00..1011.11.1..0..1.1.1..1.0.0100.0.01.....1000...01..01.....
1...1...101....0....0.....11.10..101..00.00...00..1....1...1...11.11...11..0.....00...00.....00...000.....11...11.....11...11
10..0...............0......................................................1.............1.001111.100011011.......0...000...1
00..0...............0......................................................0...1.....11.00...10.001.011.10.001.0..11001.11...
100.0.1110.100...0..0.......10.0....0.11....00....1..1....0.0.1...0..01..0.00011.0.00.1...1..01...0.00.11...1.11.0.011.1.0.1.
100.1...0.001...110.01..0.01....0..1....10.0.001...1..1..001..10.0011.11.....100..11...0100.01.1..0.0....01....1.10..0.......
00..1...............0...1....0........................0....................0...1..............0....101101.1.0..0.1..0110...0.
10.01..00...........0............0........................1.................1001.1.1..0.0.......0.0100...1.11.10.001.10.001..
11..1.......1.......0................1........................0............1......1..110.0....01....00.001.1.1..0..1.0.10.11.
01..1...............0......................................................0...................1....01..10....1.11.100001.11.
11..1...0..1.111001.0...0.0.1..0.0..11..1.000...1...1.......00.11..1..........0.00111...0.1010010..10..0......1..00101100..1.
10..0.......1....10.100.0.1.....11...0010.10101101...1.0...0........1....1.01.0.1..01.00...11.10..0101.1.01..1...1.....0..110
00..0...............1......................................................0............0...11.1..1.011110.001...01.000.1100.
10..0...............1...............................................................................00110.1..1.1001.....0....
10.000.110......110.00....0.0.0......11...00.010.....111........0.0.1..0....0..010.00.1....1.1.1..0001011100111..00..1.01.0.1
00..00..............0.........1..............1.........1..............1....00..00..0..0110.01100.0..01111.1001..0.....0..1001
10..00..............0.........0..............0.........1..............1..011....1..000....01......0.00010.0.1..1..0.100..0.11
10..10.1.0..0.......0.00....00.0..1...01.......11.....0..0.1.110..0.0..0.11....0..00...11......1100.001.1..1.0.001.110..01..0
00..10..............0.........1..............1.........1..............1....00..10..............0....01101.1.0..0.1..0.1..1.0.
10..10..............0........................0........................1....0..........10......11..1.000.00111.1100..1....0...
110010..1.00.111.10001100.0..1..100...0.11...00.11....0.01...0...0..10..0...11.01..0..1100.0.1..0..10.0.....1..1..11....0..11
01..10..1.1..1..1...0......001..1..1.100.....110...11...0.1..0.0.11.......1........1.0.1.10.0....0..0110..0000..1.1.......1.0
1101101..0..1..11.0.00010..00.0.1..10..1.0..0..110.0001..1..1..0......0.1.1.111......0.0.......0...10.0.0.....0...1.1001...1.
10..10..............1.........0..............0.........1..............0...11....1...001.1001.1...001001.0.....1.0.1......110.
00..10.........0.1001..0..1.011.0..10.....1.11....1100....1..0..11.00100..0...1....1011100.....0.1..0.0........0.0..0.1111.1.
10.11011.00.0..1.0.010.00.01.....0.011.1.....1...01.1..0...00...1..001...0.1100.1....1..000011.0..110.0..01...1.0.01.1..0.1..
111.10..1...0...0...100...0.1..0....11.1.1.......0....01....00.0......0.0.......1..........1......0.01..00....110.....0......
011110...01.1..1..1.1......00.110.......001.0..11.00.0....110.0..1...11.0...1..0....001......1..10..0.001......1.1.00......01
11..10..............1.........0..............0.........1..............0....10..11...00.11001..01..0100110...101.0.1.10.1...0.
11..11..............1...............................................................................00..00..............0....
01..11..............1...............................................................................01..11..............1....
11..11..............1.........................................................1..0.....1...101...1..001.00..1...1.11101.001..
10..00....01..101..10....00110....................11..1....................0........................0........................
001100....1....1....0....0........................1........................1........................0........................
1011000.00110.01.0..001100.0....0.0..11..1.0..1.0.01..1.1.01.01...0........0....1..01.0...0...0110010.....1..0.10...........1
10..1011.0..0...1.1100...0011.......10..01000.11....000..1....1.0.0.110.0.1.0.1.1....1...0.01..0...10..1.01..........1....00.
001.10..........1...00..101..01...11.........110..01..0.....0.........1.0.1....1110..0.0....1..0011.0.101...0....1101..0...0.
10..10011.......100.011.00..0..1.00..11.0.0.100.11..0...10.11.....1...0.....11......1.11.01...01....00.........00.....1..1.10
110.10....0....1....0....00...11.010....1..0.0.....01..0..0.0..1110...101..11..0.0..1.0........1...0010.00.01111...1.1000.1..
01..10..............0...10..............1...011..0...........11...0...100.0..1....0.1..0.0...0.1.1..01.0.1..011...0..1.00..11
11..10..............0....0........................0........................1....1..............1....00..00....1....1....0....
1001100..1011...0...1..000.0.0..1.1.1.0.10.1..0110.001...11....0.1......1.1010...100..0..10.....0.0101110.1..0.00..0..11.0.0.
00..10..............1....0....1....1....00..011..100..11.0....110.....0..0.01.01.10.1....011.10..0.001.01.....10..1.001..1...
100.10.1....1....01.1001.0..1..00..11..0...0.0.1....0...........01..01..1.1110..100.1..1..0.1..0...001110001.01...1..01.110..
"""

# Declared block-confined witnesses: torus size : block side : pair :
# target index : configuration. Every record sits inside a wrap-free block
# of that side centred on the demanding site at the origin.
BOX_WITNESS_BLOCK = """
4:3:4:0:10.1...0....0....1..1.......01...................0..11.0.......1
5:4:4:0:10..1....1......0..00...0.0.0............1...01.............................1......1.........0.0...0...00.1..0......0..111.11
5:4:6:2:10.100..10.....11..000.00...1.1...1..........11.0..........................00.01.1.01........00....1.....01........1..1.0..1.
5:4:11:0:10..1.0.1......01..001........11.00.....1....1.............................11................01.....00..0...10........01.1..1
5:4:11:1:00..1...01......1.0001..0.0................11.1............................01..0...11.....10...1..0001..101.0.......0..01..11
5:4:11:2:10.01...10........0.0..0..0..011.00......0.1....1...........................1.01...0......01.10...110..1....11......1..100.11
5:4:14:2:10.000..1.......0..00...0...110...1.....0..0..0..0..........................1..11.........00..101.1.00.0....1......1...1.1..0
5:4:16:0:11.1101..0......0.1000..0...0.01............11..01.........................0...10...1........0.1..0.00....0.0.......1.1011.1.
5:4:16:1:01.010...1.....1....0........1.1........1...0.1..0.........................00.11.0.1......1...011.0001.01.1.0.........1......
5:4:16:2:11..101.10.....0....00........01............111.1...........................1..1.............1..1.1.00....0.10.....11.0..0.0.
5:4:17:0:10.010.........0...010......010...1..........0...0.........................01.1.1...1..........01..00...0.0..0.........11...1
5:4:17:1:00.110..........0..01...1.1.001...1......0.1..1..0..........................0...11..0.....0.....0.000...1....0......1..0.1.11
5:4:17:2:10.010..........1.1.10.0..........0.....01..0...11............................0111.0......01..0.1..10....00.11........1..0.0.
5:4:18:0:11.1100.........1...1..00.1..1...1.......0....0..0.........................1..1..1.........0..010...00..0...0.......1........
5:4:18:2:11..100..1.........11..00...000..11.........11...0..........................0.1111.00.....11.00.0...0........0........1.0..1.
5:4:19:2:11.011..0......0...01........10...0...........0............................10..1.1...........0.10...00..0.1.11.........1....1
5:4:22:0:11.110...0........0.0...00...0...........0......1..........................10..1...1......00...1....00.00...........1..1.1...
5:4:23:0:10.010...0.....0...010.010...0.0.........1.0.....................................0..1.....1.....1.0.0...0...1.........0......
5:4:23:1:00.110...1.....1...011.000.....0.0.......0.1.1..............................1.1.01.10.....10..1.0.000...................1....
"""

# The declared mask pool: 3117 witness configurations on the 3^3 torus,
# each carried with the configuration that realises its mask. The mask is
# recomputed here by two paths; none is asserted. The pool is a verified
# subset of the realisable masks, not a census of them.
POOL_BLOCK = """
1.0........................ 0.0........................ 1.0.0........0.............
100........................ 000........................ 100.........111.........111
1.0...0.............0...0.1 0.0...0.............0...0.0 1.0...0.............0...0.0
100.110....01.10...0...0.11 000.1001....01.0.1......111 100.1.00...000......11.1.11
001..1001.1...0.1......0... 101...0...0..1..1..0..1.01. 111...00...011.00...0..0111
011...0.1..0.....0....00.11 111...0.....1..0...00100.11 1000..0....................
000011011.................. 1010..0...1.100.1..0.1....1 001001001..0..0..0..1..1..1
101011001.0..1..1..0..1..0. 1.0.1100..11......00....... 0.0.1001..10......01.......
1.0..00......0.0.100...1.11 1.1...00...01..1.00..0...11 0.1.010...0110.1..0..1...1.
1.1.1000..11.10...00....... 100...0.....1000..0..0....1 000...000.....0...000...000
100..000..1111..0.0..001.00 111.01000.10....10000.01111 011..001..0.....000.1.00.11
111.0.0.0..01...1000..01.11 100...1...........0.....0.. 000...111.....1...000...111
100.01100.100...10011.01011 000000000.........000000000 10100.011.....1...01011.100
001001001..0..0..0001001001 10101100..00011.0000.011101 01100.101.........01011.100
111111111.........000000000 0111..1...000110110111..1.. 1000..0..0........0........
000000000000000000000000000 10101101.01010001.00.11...1 0110010010101..1..0101..1..
111001001010......010...... 101000110011010110001111100 101...0...........0........
001...0...........0........ 101..10....1......0........ 1000..0...........0........
0000..0...........0........ 10000.00.....0....0...0.... 1110..0...........0........
0110..0...........0........ 11101.0...0.......00....... 1010..1...........0........
0010..1...........0........ 1010.11....1......0.0...... 1110..1...........0........
0110..1...........0........ 11100.1.....1.....0..0..... 1010..0..0........0........
0010..0..0........0........ 1010..0..0........0000..0.. 1010..1..0........0........
0010..1..0........0........ 1010.11.00.1......0.1...... 101.11011.1111111101111.111
111011011.11111111011111011 101011111.111111110111111.1 101011111011111111011111111
101...0...........00....0.. 101...0...........00.0..0.. 101...0...........00.1.10..
101...00..........00....... 101.0.00..........00....... 101.0.000.0....0..000......
101.01000......0..0..0.0... 101.0.000...1111110.0111111 101..101..00..10010.0111111
101..101..00...0010.0111111 101.1.01..010..0.10.0111111 101.01001.1..11.110.0111111
101.110.1.0.0.00.10.0111111 101.110.1.0.0..0.10.0111111 101.01000.0000....000.00...
101...0...........01....... 101.0.0.0...0.0.0.010111111 101..00...1.00..00000111111
101.0.0.0.10...1.00.0011111 101..00...1.00..00001111111 101.0.0.0.0.0.0.0.001111111
101.0.0...0.0...0.00.111111 101...0...........00....000 101...0...........0.....0.0
101...0...........0.....0.. 101...0...........01..000.. 101...0.0.1.000.0.010111111
101.0.000..10.0..0010111111 101...0...........00.1.10.1 101...0...........0.....1..
101..00...111111110..111111 101.0.0...0.0.1.110.1.11.11 101.00001.00.11.11001.11.11
101.0.00..0.......00....... 101.1.0.0.0....1.10.0111111 101..101..0.0..01.0.0111111
101.00000.0....0..011.1.... 101.00000.0....0..0.1.1..0. 101.000.....1.01010.1111111
101.0.00....1.10.10.1111111 101...0...........01....1.. 101...0.0.010.0...0.1111111
101.00000.00....11010..1... 101.0.000.10000..0000111111 101...0...........00....101
101..00...1000..0.001111111 101.1000..10......00....... 101..00...1000..00001111111
101.0.000.10.000..001111111 101..00.0.00.0.0..001111111 101...0...........00....01.
101..00.0.1000..0.000111111 101.0.000.10..0...001111111 101.0.000.11.0...0000111111
101.0.000.1100.0..000111111 101.01000.00......01..10111 101.01000.00......01...1.1.
101.1001......00..0.0111111 101..0010.0.0100..0.0111111 101...0...00..00..001111111
101...0...........01....0.0 101...0...00.000..001111111 101.0.0.0......000010111111
101...0.0.010.0.0.010111111 101...0.0.00..0...001111111 101...0...........01....000
101.0000..10.....0010111111 101.01000..0......010.10111 101.000...0.1.00.00.1011111
101.00000..0......0....1.1. 101.0.0...0...0..00.1111111 101..00...00.....0001111111
101..00...1..0.0000.1111111 101..00...00.0...0001111111 101.00000..0......0....1..1
101.0.0...000.0.0.0.1111111 101...0...10000.00001111111 101...0...00000.0.001111111
101...0...00001.0.001111111 101..00...0.1..0..011111111 101...0...0.1.....011111111
101.01000..0000...0........ 101.0.00....0..0..011111111 101.00000..11..0..0.1111111
101.1.0...00.1.000001.11111 101..00........0..011111111 101..00.....00.000011111111
101.0000.......0.0011111111 101.0.00......00.0011111111 101.0000..1.10..01000111111
101..00...11.11.110..111111 101.1.01..00.1.0.0001.11111 101..1000..01.100.00..11111
101.11011.111111..00..11..0 101.0.00..101....10.1111111 101..00...1.01..10000111111
101...01..110.0.010.1111111 101.1.0...10.1...10.1111111 101.1.0...00.1...10.1111111
101.1.0...11111..10.1111111 101.0.0.......0.00011111111 101.0.0.....0.....011111111
101..001..0.01.0.10.0111111 101.000...1..10.110.0111111 101.0.0.0......0..011111111
101.0.001....1001.0.0111111 101.000...1001...10.1111111 101.1.001..111001.0.1111111
101.100...0.000.110.0111111 101.000...1.010.110.0111111 101.010...........0........
101.1.00..110.1..1000111111 101.0.0.0...1.000.011111111 101...01..101...010.1111111
101.0000...100..110.1111111 101.0.010..111000.0.1111111 101.0100..01.0.0100.1111111
101..00.....00..00011111111 101.0.000.0.0.0...011111111 101.1.0...0.0.1.110.0111111
101.1001....010.110.0111111 101.1.0...0.1.0.110.0111111 101...00..00..00.0001011111
101...0...0...0.11001.11111 101.01000..0000...0......1. 101.0.00..0.0.0..10.1111111
101.0000..0.1..0.0011111111 101...00...00.0.110.1111111 101.1.01..1..1.0.0001001111
101.1.00..00.000.0001011111 101.1001...0..00000.1001111 101..00...1..0.001001011111
101..00...0....001001011111 101.1001..1..1...1001.11111 101..00...0..00.01001.11111
101..10.1....0001.0010.1111 101..00...0...0011001011111 101...000.0...10..001011111
101.0.00..0..010100.1001111 101.0.0.0.0..1.0..0010.1111 101.0.010.1..1.01.0010.1111
101.0.00..1..11010001001111 101.1.0...........0........ 101...0...........01.0..00.
101.10000...0.0.110..111111 101.01000.10000...00..01100 101.0.001..0.01.110..111111
101.0.000.100.10..001111111 101...0...........01.0..000 101.01000.10......0010.0..0
101.0.000.100.0...001111111 101.0.000.110.0...010111111 101.00000.100..0..001111111
101.0000......00110.1011111 101.00000.100000..010.0001. 101...00...0..10110.1011111
101.0.00...0111.010.1111111 101...0...0.00..01001111111 101.0.00....0.00..0.1111111
101...0...0.00..0.001111111 101..00...0......1001111111 101.0.00......00.00.1111111
101...0...0...0..0001111111 101..00...0.00..01001111111 101.0.000...0.0...0.1111111
101..00...0.00..0.001111111 101..00...0....000001111111 101..00...0.....00001111111
101...00..0.00.0.1001111111 101.0.0...0.0.0.0.001111111 101.000...0...0.0.001.11111
101...0...1000..00001111111 101.010...0001...10.1111111 101.110...0010...10.1111111
101..0000.111..01.0.1111111 101.01000.000000.00.0.0.00. 101.1001....0.0.110.0111111
101.0.0.....0.0.00011111111 101.010...1000...10.1111111 101.0.00....0.00100.1111111
101.0000..0...00.00.1011111 101.01000..0000...0.0....1. 101.0.00..0...00.0011111111
101.11011.10.1.10.0...11111 101.11011..00.01..0...01111 101.11011.10...1..0...01111
101.000.0.00.100..0.1011111 101.01000.0000000.0.1.....0 101.0.00...0..10110.1011111
101.1.00..00.1000.001.11111 101.0000..1..0..0.000111111 101...01..100...010.1111111
101.100.0.000..01.010111111 101...0.0.0.0.0...0.0111111 101..00.0.101.010.001.11111
101...0...10...100000011111 101...0...1...1100001.11111 101.100....010.1..000.11111
101.100....01011.0000.11111 101.0.000.1..000..001111111 101..00...10.0..0.010111111
101..00...0....0..001111111 101.00000.01......010.01.11 101.00000.01......010.11.11
101.0.00..010110010.1111111 101..000....1..0..011111111 101.1.0...01.00..00.1111111
101.0.001.1..10.1.0.0111111 101..00.0.0.0..01.010111111 101..10.1..01.100.00..11111
101...0...0.0.0...0.1111111 101.100.0.00.0.0..001.11111 101.010.1..0..10..00..11111
101.01000.00......010.0001. 101..00.0.01000.0.010111111 101.1.0...11.010.10.1111111
101.00000.00....1.0110110.. 101.1001..111.00..000111111 101.0.0.0....0.0..0.1.11111
101..0001.0...0.0.001.11111 101.0.00.....1.0..001.111.1 101.0000.....100110.1011111
101.0000....000000001011111 101.1000.....000..0.1011111 101..00.0.0...00..0.1011111
101.000...0..100.10.1011111 101..00...0....0.1001111111 101.00000..0......00.01101.
101..00.0......0..001111111 101.0.0.0....000..001111111 101.0.0.0.0..0.0..001111111
101.0.0.0.0....000010111111 101.0000......00..0.1011111 101.000.1.101100..0.0111111
101..0001.1.1.001.0.0111111 101..0001.101.001.0.0111111 101.1.00....1..00.00.111111
101.0.01...01010.10.0111111 101.1.0.0.0...10.00.0111111 101...0.1.00..10..001111111
101.1.0.0.0....0.00.0111111 101..00.0.0....0..001111111 101.1100..1.1..00.000111111
101.00010.0111.00.0.1111111 101..1010.0..110.10..111111 101..000..0.1..0..011111111
101.00000.001000..0.11010.. 101.0001..00.110.10..111111 101.0.00...1.0.01.0.1111111
101.0.00....11.00.0.0111111 101.0.0.0.0.1..0..011111111 101..001...0.110.10..111111
101.0.00....10.01.0.0111111 101.1100...110.01.0.1111111 101.0.00...0...0110.0011111
101.1100..10.0..0.001.11111 101..0010.....1..00.0.11111 101..001....11000.001101111
101.1000.....10..0001..1111 101.1.0.0....0.1100.0011111 101..00...1..10010001101111
101.1.0.0.111100.000.101111 101.1.00..100..010001.01111 101.1.0.0...1..1.00.0001111
101.01000.10......0010.0110 101...00..0.1000.0011111111 101.0000...11100010..111111
101.01000.1..0001.01.10.0.0 101.1.0...0....0.10.0111111 101.010...0..1.0.10.0111111
101.000...1..100.10.0111111 101.000.0.1101.0.100.011111 101.00000.0..00.0.011110...
101..000..0.1..0.00.1111111 101.000.0.01...0..0.1111111 101.000.0..101.01.00.011111
101.00000.10.000..0.0.000.0 101.1.01..0011.0.0001.11111 101.00010..0..10100.0011111
101.00011.....00..0.1011111 101.0000....1.00.10.1011111 101.000...0..10..00.1011111
101.00000..0......0..1.101. 101.0.0.0...1..0..0.1011111 101.0000..01..00..01..11111
101.01000.00......01..00.11 101.1100..10...0..0...11111 101.0001.....101000.10111.1
101.1.00..1..01.00001.11111 101.1.00...1.11..10...11111 101.1.00..0..10..00.1.11111
101.000.0.0..100..0.1011111 101.0000......00.10..011111 101.1.001...00010.00.011111
101.01000.10......0....0.1. 101.0000....1..0.10.1111111 101.0000..1..0000.000111111
101.010.1...00101.00..11111 101.1.01...1.000010.1111111 101.000.0..1.1.0..0.1111111
101.01000.0..00.0.01..0.... 101.0.0.0.0....0..011111111 101.0.0.0.1.10.0.00.0.11111
101...0...00..00.1001111111 101..00.0.00...0..001111111 101.010.1.1110101.00..11111
101.0000....1100.00.1011111 101.110.1...1..00.0..111111 101.11011.111111..0..000...
101.0.00..01.010.10.1111111 101.0100...00.101.0..011111 101.000.0.000110100.0011111
101..00.0.01..00.000.111111 101.0.0.1....0.00.01.011111 101.0.01......0..0001.01111
101.1000.....100.00011.1111 101.000.0.0....0..0.1.11111 101...0.0.10...010010.11111
101...0.0.0....0.0010.11111 101.01000.00.....00111.0.11 101.0.00...1..00.10.1111111
101.0.0...00..00000..111111 101.1.0......110010...11111 101.1.0.1..01.101.00.111111
101.010...0.11.0.10.0111111 101.10001..0.100..0...11111 101.10001.10.100..0...11111
101.010.0..1..00100.0011111 101.0.0.0.0110.0100.0011111 101.0.00..010.00..0.0011111
101.0.0....11.001.0.0011111 101.0.0...010.001.0.0011111 101.0.0...011.001.0.0011111
101.0000..0.1..0..0..011111 101.0000....1..0..0..011111 101.0.001.10000.1.0.0011111
101.1.01...01010.10.0111111 101.1001..0.1.00.10.0111111 101.0.00..1..1.00.00.011111
101.010.1...1..00.0.1111111 101.010.1.1010.0..000111111 101.0000..1..0..01000.11111
101...0...00.010.1001.11111 101.010...10..10..010.11111 101.0.00..110.1..10.0011111
101.100.1.10..1...010.11111 101.0.00..1..0.001000111111 101.0.01..1010.0..00.111111
101.100...0...001.0.0111111 101..00.1.011.00..0.0111111 101.1.0...001010.10.0111111
101.10010.0......101.011111 101...0...0.1..0..01.111111 101.00010..011...0000.11111
101.00001...10001.0.0111111 101...0.0.100111000.00.1111 101.0.0.1.1.10101.000111111
101.0001..1..000..000111111 101.0.0.1.1..010..000111111 101.1000..101.100.00.111111
101.0.00..11.0.00.00.111111 101.010.0.11.1.0.00.0111111 101.1001..1..000010.0111111
101.11001.0.1000100..111111 101.1001..1.1000010.0111111 101...0.0.10..1.1100..11111
101.010.0.1..1.0.00.0111111 101.010.0.1110.0.0000111111 101..10.0.11.0..000.0.01111
101..10.0.11.101000.0001111 101.110.0.11.000.0000.11111 101.0.0.0.110..1.00.0011111
101.0.0.0.0.1..0.00.0011111 101.0.0.0.1.1..0.00.0011111 101.1000..1.10100.0.0011111
101...0...0....0..0.0111111 101...0...01...0..0.0111111 101..00...0...00..00.111111
101.1001..0...00..0.0111111 101.1.0...1..000..000.11111 101.1000..1.10.00.000.11111
101.010...11.000..000.11111 101.1.00..1..0..0.00..11111 101.1000..10.01.0.00.011111
101..0010.0.....100.0.11111 101.1000..11.01.0.00.011111 101.1000..1110.00.00.011111
101.1000..11..010.00.011111 101...0.0.100.0.1100.011111 101..0001.1.110.0.00.011111
101.1.010....0.0100.0111111 101.11001.01.000100..111111 101.0.011.10.10..000.011111
101.01000.00......010.1010. 101.100.0.0..1...00.0.11111 101.1100..10.01.0.00..11111
101.1.0.1.0..10...0...11111 101..0001.11.10.0.00.011111 101.0.0...11..0...0...11111
101.1.00..1..0000.00.011111 101.1.000.1000...0000.11111 101.10000.10001...000.11111
101.100...101000..0.0011111 101.000....0110..000.011111 101.0.0...1..1.0..0.00.1111
101.100.0..11..0.00.00.1111 101...010.0.0.0...0.0111111 101..0010.010.0..00.0111111
101...0.0.110...00000.11111 101.0.0.0.111..1.00.0011111 101.100.0.0.0..0100.0111111
101.1.0.0.0.0.00100.0111111 101.0.00.....000.00..111111 101.1.010..0.....00.0.11111
101...0.0.11.0.0100.0011111 101.110.0..1.10.000.0.11111 101.1000..10.0000100.011111
101.100.1.....000.0..111111 101.0000...0..00.00..111111 101.01010.100..1.00.0011111
101.100.0.101010.000.011111 101...0.0.1..1.010010111111 101.1.00..1..1.0..0.1111111
101.1.0...11..0...0...11111 101.010...1.0.1...010..1111 101.00010.101.1...0....1111
101.0.00...100.0..0.0011111 101.00010.........0...11111 101.1100..0..11..00...11111
101.01000.00......010.011.1 101.01000.00......010.000.1 101.01010..1..0..00.0011111
101.10001.1.000.0.00.011111 101.0.00..110..0..0.0011111 101.0.0.0..111.0.000.011111
101.0.0.0..11..0.000.011111 101.0.0.0.011..0.00.0011111 101.0.0...010.1.0.0.0011111
101.0.00...1.0.0..0.0.11111 101.0.000.10.00..000..0..0. 101.0.00..11.0.00.000111111
101.0.00...10.10110.0011111 101...01...1.100..01.111111 101.0.0...11000.1.000.11111
101.1.0.1..0..001.0..111111 101..0011....1.0..0..111111 101.100...101000..000.11111
101.100...10.010..000.11111 101.0.0...0...00..010.11111 101.0.00...11000..0.0011111
101.1.0...0.1.00..010.11111 101..00.1.1..0.01.0..111111 101.10001.1.00010.00.011111
101.000...0...0...010.11111 101.1.0...0....0..010111111 101.0000....0.00110.1011111
101.0.00....0000.10..011111 101.1.0.0...1..01.01.111111 101.010...10.01...000.11111
101.00000.00.00000010..0... 101.010...1100001.000.11111 101.1101..10.11...010.11111
101..1000.1.00110.00.011111 101...0...000.10.1001011111 101..1000.1000110.00.011111
101.00001.110.001.0.0011111 101.01001.000...1.0...11111 101.1.010.10.10.000...11111
101.000...0...0.11001.11111 101.1.01...1.10...000.11111 101.10011.0...11.000.011111
101.100...11000...0.0111111 101...0...0.0.....011111111 101.100.1.1.10.0..0.0111111
101.100.1.1.00....0.0111111 101.010.1.0110001000.111111 101...0...0.0.0..0010111111
101.1.0.1..0.100010..111111 101.11011.1001010.0.0011111 101..0011...01.0..0..111111
101.1.0.1..00.001.0..111111 101.0100...1..00.00.0011111 101.1.00..101000.0000011111
101.0.00......0..00..111111 101.0.00......00.00..111111 101.1000..101010.0000011111
101.0.00....1..0.10.1111111 101.010.1.0..0.00.0.1111111 101.0.00....00000000.011111
101.0.00...0.01.010.1111111 101.0100...0.0.0010.1111111 101.00001....01.100..111111
101.100.1...10101.0..111111 101.01010...00..110..111111 101..00.1.1.01001.0..111111
101.01000.10......00111010. 101...00..0.0010.1001111111 101...0.0.011..0.000.011111
101.1.00..0..0.0.000.011111 101.0.00.....1.0.000.011111 101.0.00....1000.000.011111
101.0.00....00....0.1111111 101.1001...11101.000..11111 101.1.01...100....000.11111
101.1.01...1.10..1000.11111 101.1.011.0.1011.000..11111 101.1001...0.101..00..11111
101...01..1.1.010.0....1111 101..1001.0....01.0.1111111 101.010.1.0.1..0..0.1111111
101.110.1.100101..0.0011111 101..00.0.0...101100.011111 101.00010.111..1.00.0011111
101.10001..0.001010.0011111 101.0.001..0..0.100..011111 101.1001....1000010.0111111
101.110.0..01.10.101.111111 101...011.1000..10001111111 101..10.0.10000.01001111111
101.00011.1000101.001111111 101.10000...00..1.010111111 101.1.010.1.000.0.010111111
101.01000.10001001001111111 101.010.0.1001.0.10.1111111 101..1011.1.1...1.0.0111111
101.1.0.0.1.101000000011111 101..00.0.1..1.01.010111111 101.01010.1...101.0..111111
101.0.001.1..010..000111111 101.01010.0..010.000.011111 101.1101..0..11..00...11111
101.11011.1001.10.0...11111 101...0...0......1001.11111 101.01000.10000...01.....0.
101.01011...1...1.0.1111111 101.01000.10000...000....01 101.01011...0...1.0.1111111
101.1.000...000.110..111111 101.110...0.10.0.10.0111111 101.1001....0...110.0111111
101...01..01111.110.0111111 101..101..0.01.0.10.0111111 101.1.0.....1..01.01.111111
101...0.0.1.110000000111111 101.1.0.1.......1101.111111 101.1.01..0....0..01.111111
101..00.1.1.10000.000111111 101.1.010.0.101.0.0.0111111 101...0.1.1.10101.000111111
101.01010.1000...0000111111 101.00010.00...0..010.11111 101.1101..1.00.0000000.1111
101.1001..1100.0000001.1111 101.1.00..000100..001.11111 101.0.00...1..00..0...11111
101.01010..1.1.1..0.0011111 101..000....1..0.000.011111 101.1.001..0.100..0..011111
101.1.001..0.1001.0..011111 101.0.001..0..001.0..011111 101..00.1..0.0101.000011111
101...0.1.00.0001000.011111 101...0.1.1.00001.000111111 101..00.1.0...101.00.011111
101.010.1..0..001.0..011111 101...0...00.01.01001.11111 101.1.01..001010.1001.11111
101.0.00..11.01.01000111111 101.000.0.10...0..010.11111 101.01001.10.10.1000.0.1111
101.1001..0.11....0.1.11111 101.1001..0.01....0.1.11111 101.1101..10.11..00...11111
101.01010.111..1.00.0011111 101.0.00.....1.0000..0.1111 101.1001..0...00..0.1001111
101..1011.1.1101..01...1111 101.11010..1..10000.0001111 101..1011.1.0011..01...1111
101.010....0..00..0.10.1111 101.01000..0000...0.0...... 101..10.1..0..00..000001111
101..10.1.01...0..00.001111 101.0000..1..10..1001.11111 101..1000..0..10010.10.1111
101.11000.0..100.1001111111 101.1.01...0.010.10.10.1111 101..001...01010.10..111111
101.01000.10....01001111111 101.01001..1.10.10011111111 101.00000.01....01001.11111
101..0001.1.....01001.11111 101..0001.1.01010.00.011111 101.01001..0001.110..111111
101.11011.11110.11011.11101 101.01001..1.01.110.1111111 101.0.001..1.00.110.1111111
101..00...010000.1001111111 101..0000.00.0.0..0..111111 101..00...0...0..1001111111
101..00...0...00..001111111 101.1000..101011.0000011111 101..10.0.0...00.1001111111
101..00...1..010010.1111111 101.1.010...1110100.1111111 101.00011.1...001.0.1111111
101..00...1..1001.010111111 101.000...110101.000.011111 101...0...1..000000..111111
101.0000...1...0.00..111111 101..00.0.01..00.0001111111 101...0...1..001000..011111
101..000..0.1110.10..111111 101.1.010..0.1001.01.111111 101...0.0.01.0...000..11111
101.000.0..11100.0001..1111 101.01000.1.....0.00.0.0... 101..00.0.001100.0000111111
101.1.00..0.1110.10..111111 101.11001..0111.0.000.11111 101...0.0.0.0101.000.011111
101...01..10.0.1010.0011111 101...010.01.01.10001111111 101.1.010.01.1..1.0.0111111
101.0.00...0...1010.0011111 101.0.01..1..0.0..000111111 101..00...0...00..000111111
101.100...1000110.0.0011111 101..00...1000110.0.0011111 101.00011.01.000110...11111
101.010...10.00...011011111 101..10.0.10.001.1001101111 101..1010..1.00101010101111
101.1100..0.10.101000111111 101.1100..0010.101000111111 101..0000.....110100.011111
101.1100....10.1010.0111111 101.1.0.0.0.1.1010000111111 101..0011..0.00..000.011111
101.01000...0.....0....0... 101.01000.01001.10001111111 101.10000.01000.10001111111
101.01010.1.0..01.0..111111 101.01001.10010110011111111 101.00000.01....10001.11111
101.10000...0.0.010.0111111 101..00.0.1000110.000111111 101..1010.0.010...0.0111111
101.10000...1.0.100..111111 101.00000....10.10001.11111 101...00...00001.0011111111
101...0.0.0.0.0...001111111 101.00000.0....0..01...1010 101.1.0.0.0.0.0.1.010111111
101...0...111111110..111111 101...001.1011.010000111111 101.01000.0....0..01.0.000.
101.0.00..110.10.10..111111 101.0.010..0.00.11001.11111 101.110.0.10.0010.011011111
101.00000.00000..10..101.00 101.010.0.0110....011011.10 101...0........1..011111111
101.10011..0.01.01011111111 101.01001...000.0.0.0111111 101.01001..0.10.100.1111111
101.01001..0.10.100..111111 101.1.011.01.1.110010111111 101.100.0..110100.0..011111
101...001.1..0..10000.11111 101.0.011.0...0.10000.11111 101.0.001.0...0.10000.11111
101.0.000.1...0.01000.11111 101...010.10....01000.11111 101.1.011.11.00.00000.11111
101...001.11.00.00000.11111 101.0.001.11..0.00000.11111 101.0.001.1..1.110000111111
101.1.011.001010.00.0011111 101.1.011..01010.00.0011111 101.010.0.0110.0.00.0011111
101...0...0.....01001.11111 101..1001..0..0110001111111 101.1.011..11010.00.0011111
101.01010.101.....0...11111 101.00010.101.....0...11111 101.1.01...1.1....0.0.11111
101.11001.00.0.00.001001111 101.010.1.0..0.0..00.001111 101.10000..1000.01011111111
101.10011.10.01000011111111 101..0011..0.0.111011111111 101..00...1000..00011111111
101...0.0..1.00101011111111 101..001...01.110.000011111 101.10011..0011.01011111111
101..10.0.01..01.1001111111 101.00001.00011111001111111 101.000...01.10.01001111111
101.10000..1.01001011111111 101.110.0.01.001.1011111111 101.1.010.0..1.111001111111
101.00011.0.001010001111111 101.0.01..00.01101001111111 101.01001.10010.10011111111
101...011.10001.100.1111111 101.01001.10010.10000111111 101.00000..10..0.1011111111
101...01..10000010000111111 101.0.00...00.0..0011111111 101...010.1.000.0.000111111
101.00000.0101...1011111111 101.0.000..0000...000....01 101.0.0...000.0.00001111111
101.00001.10111.11011111111 101.01001...10001.0.0111111 101.000.0.0...10..0.1011111
101.01001..00.0..00.1111111 101.0.00...0..00..0..011111 101...0.0.00.0.101001111111
101..10.0.00.0.101001111111 101...010.1..00.01000.11111 101.0.01...0.01.01001.11111
101...010.00.0..01001.11111 101...001.1..00.10000.11111 101.0.01...0.01.10001.11111
101..101..10.01.0.00..11111 101.0.01...0.01010001.11111 101..0010.0......00.0.11111
101...0...0....0..01..11111 101...010.10.00.01000.11111 101.01001.10.10.10000111111
101..10.1.1.01.000000111111 101.010.1.1.0001.00.0111111 101.000.0...01010000.111111
101..000..0.00.0.1001111111 001...0...........0.1...... 001..1001.11111111011111111
001.00000.0..000000010000.0 001.11011.1111111101111111. 001.11011.111111110111111..
001.1.011.1.111111011111111 001..10.1.0...10..011111111 001.11011.111111110111..1..
001.1.011.1...11..011111111 001.00000.00.000.00.0...0.. 001..1001..1111111001111111
001.11011.11111111001111001 001...0...........0.....1.. 001...0...........0.....0..
001...0...........0.1...0.. 001..0001.11111111011111111 001...0...........0.00..1..
001...0....10.0..00.1111111 001.1.01...0000.100.1101111 001...0...........0.1...1..
001...0...........0.1...10. 001...0.0..1..00..0.1111111 001.0.01...1...0000.11.1111
001.0.0....10.0.000.1101111 001...0....10.00.00.1111111 001.1.01...1.00.000.1101111
001...0.0.00..00..0.1111111 001.000.0....0.0..00.111111 001..00....00..0..00.111111
001.00010.00001...01.....0. 001..10.1...0..00.00.111111 001.000....0.0.0..00.111111
001.000....0.0...000.111111 001.010.1...0..00.00.111111 001.0.0.0..00..00.00.111111
001.000....010.00000.011111 001.0.0.0..0..000.00.011111 001.00010.00001...01....10.
001..0000...00....00.111111 001.0000..10...1.001.011111 001..000...000..0000.111111
001..00.0.00.0.0..01.011111 001.000.0...00.00.00.111111 001..00.0..0.0000.00..11111
001..100...1.1.0..00..11111 001.000.0..0.0.0..00.111111 001..000...0.0010.00..11111
001.010.1...00.00.00.111111 001...0....0.10..00.1011111 001.0.0...010.....0..111111
001...0...1111...00.1011111 001...0....110...00.1011111 001...00..011000.00.1011111
001...0...1111..1.0.1011111 001..00....0110.100.1011111 001...0....111..1.0.1011111
001...000..111....0.1011111 001...0....111....0.1011111 001...0....1110.000.1011111
001..10.1.10.1.01.000.11111 001..10.1.00...00.010.11111 001...000.11......0.1.11111
001.00000.000000..0.00..111 001.01000..1.1....0.1.11111 001.00000.000000..0.0.00010
001.110.1.10.11.1.001.11111 001...0....00.1..10.1111111 001.1.0...01111..10.1111111
001.010.1...0.0.0000.111111 001.0.0....01000100.1111111 001.0.0....1.000100.1111111
001...0....10.0..10.1111111 001...0....0.10...000111111 001..00.0.1101001.000111111
001...0....00..0..000111111 001...0.0..10..0..000111111 001.0.0....10.0.00000111111
001.0.0.0..0...0..000111111 001.11011.1111101.00...1000 001.0.0.0..1...0..000111111
001...0.0..0...0.0000111111 001...000..10.....000111111 001...000..1......000111111
001..00.0..0..00..000111111 001...0.1..100000100.111111 001.0.0.0..100.0..0.1.11111
001.0.00...1110..00.1011111 001.0.0....01...11000111111 001..000..1000000.000111111
001.000.0..100..1.000111111 001.0.00...00..0.1000111111 001.000.0..1.0.01.000111111
001.010.1.10..1.0.001.11111 001.1100..........00....... 001.01001..0..0..001.111111
001.1.0...010100.10.1111111 001.00010.00000...0.0...00. 001.00010.00000...010....0.
001...0....1...0..0.1111111 001...0.0.00.0.000010111111 001.1.011.00..10..001111111
001.00000.00.000..0.00111.0 001.00000.00.000..0.0011110 001.1.01...11..0.00.1111111
001.100...011..0.00.1111111 001.00000.00.0001.0.01010.0 001...0....11..0.00.1111111
001.010....01.000.01.111111 001...0...01.1.0.00.1.11111 001...0....1...0.00.1.11111
001..00.1..1.000..0..011111 001.000....0.000..0..011111 001.11011.11111.1.00.1.100.
001.0.001.0.111111001111111 001...001.0.111111001111111 001.000......0.0.0001111111
001.11011.11111.1.00...1.0. 001...0.0.00..00..001111111 001.00000.00.000..0.001.110
001.0.00....10.00.001111111 001..00.0.001..0..001111111 001...0.0.0...00..001111111
001...00......0000001111111 001..00.0.00...0..001111111 001..100...0...10.00.011111
001..00.1.1.11001000.111111 001..100..0.0..00.0.10.1111 001...0....1.11...0.1.11111
001...0.0..1...01.0.1.11111 001...0....1......0.1.11111 001..101....0..0.00.10.1111
001.1.00..111000100.1111111 001.0.01..1..0..0.001.111.1 001..000......00..001.111.1
001...0.1...1..0.00..111111 001.1.011.00..00..001111111 001.00000.00.0001.0.01110..
001..1001....1.00.001111111 001..10.1.0....0..001111111 001..10.0..01..0.00.0111111
001...000..1.11001001111111 001..000...0...000001111111 001...0.1..0..00..001111111
001..00....0...0.0001111111 001.00000.00.0001.0.0.0.0.. 001.00000.00.0000.0.0...0..
001.0.011.10.000..001111111 001...0.1.00..10..001111111 001.0.0.0......000010111111
001.11011.111111..000...... 001..001.....1.0.1001111111 001..101..10.1.0.1001111111
001.01000.00.00.110.1.01... 001.0.01...01010.0001111111 001..001...11..0.00.1111111
001..00.0..11..0..0.1111111 001...00...0111001001111111 001.00000.10.000110101101.1
001.11011...1..0..001111111 001..1001..111.00.000111111 001.11011..11..0..000111111
001...0....1.1..000.1.11111 001..00.0..1...01.0.1111111 001.1.00...0.01.01001.11111
001...00...0.11001001.11111 001.110.0.1......0010.11111 001.1.00...0.01001001.11111
001.0001..11..00.10...11111 001..000..11.1000100..11111 001...0.0.10.01..00.0.11111
001...0.0..0.01..00.0.11111 001.010.0.0..1...00.0.11111 001.1.0.0.01.0.01.0.1.11111
001.0001...1..001.0...11111 001..000...0....0.00.011111 001.00010.00001...010...0.1
001..000...1..0.0.00.011111 001.0001..01.0001.0...11111 001...0.0.0...1010010.11111
001.1.0.0..1...0..0.1.11111 001.0001...0.11.1.0...11111 001...0.0..1...0..0.1.11111
001...00...0.0.0..010111111 001.0.00..10...0..010111111 001.000.1.1..100..0...11111
001...00...0.00.00001.11111 001.10001.10.00.0.00.011111 001.00010.00000...010...1..
001.1.0....1.1...00.1.11111 001..000.......000001111111 001...0.0...0100.00.0011111
001..000......0001001011111 001...00...1..100100.011111 001..000...001000.00.011111
001..00.0..1.000..0.1011111 001..00.0.00...0..00.111111 001...0.0.0..0.000010111111
001..00.1....100..0.1011111 001..000...000.00.00.011111 001.0.0.0.101..0.00.0011111
001...0.......1.000.1.11111 001...0......1..000.1.11111 001...0....1..1...01..11111
001...0.0.0...0010010.11111 001.1101...0......01..11111 001...0....1.11...0...11111
001..000...110000.00.011111 001.100.....0.1...0.0011111 001..10...00.1....01..11111
001..101..00..10.10...11111 001.00000.00.000..0.001.100 001.00000.00.00..10..110..1
001..1011.0.1..00.0.0111111 001.00011....11.000...11111 001.10001.10.00.0.00.01.111
001..000..100.000.001011111 001.100...00..1...0...11111 001...011.00.1....01..11111
001.1101...0..00.101..11111 001...011.00.1.0..01.111111 001.1101...0..10..01.111111
001.00010.00.0000.010..0001 001.00010.00.0000.010..000. 001.00010.00.0000.010.0000.
001...011.0.1..0..011111111 001.1.0.1.101..01000.111111 001...0.0..1.0.0100.0011111
001..1011.0..1.0..011111111 001.010...10.10...0...11111 001..10.0..1..10.000.111111
001..10....00.1...01.111111 001..00.0....10.1001.111111 001..00....1..0...0..111111
001...0.0..00..0.001.111111 001.0.0.0..0..0..0000111111 001..1011.011..00.0.0111111
001..000...0..0001000111111 001.110.0..10....0000.11111 001...0.0.1010.0.00.0011111
001...0.0.1011.0.00.0011111 001...011..01110..000111111 001..0000.1.1.1111011111111
001.1100..0.11.111011111111 001..100..1.1.0111011111111 001.0.011.001011.1011111111
001.00000.0.111111011111111 001.11000.0.110100011111111 001.1.0.0..0....000...11111
001.11001....1..0.0...11111 001..000...0.0010.00.011111 001.000.0.00..11000.0011111
001...0.0..1.1.0100.0011111 001..000...0...00000.111111 001.1.0.0..1.1.0100.0111111
001.00000..00000..0.1...0.. 001.010.1....0.0..00.111111 001.000...00.001.1011011111
001.00001.11.1110.011011111 001.1100..00.0011.011011111 001.00011.01.011..011011111
001...0.0..1...0.101.111111 001.10001.11..1.0000..11111 001...0.0..1.110000.0.11111
001..00....0.0..000...11111 001.1.0.0..1001.000.0.11111 001..001..0..100..010111111
001..0001.10.11..10...11111 001..001..1...00..010111111 001...01..10.1.0..010111111
001..001..1.000...010.11111 001..001..11.000..010.11111 001...0.0.00...0.0010111111
001.0100...0.1.0..0.0.11111 001.1000..11..100.00..11111 001.000...110.0...0..011111
001...0.0.00...0.00.0111111 001...001.10..100.001111111 001..10....1..10..00.111111
001.1.0.1.10..101.01.111111 001.110...00..1.1101.111111 001...0.1..0.1.01.01.111111
001..10....0.1..1.010.11111 001...0.1..0...01.0..111111 001...0.1..0...0..01.111111
001...0.1..0..10..01.111111 001...011.00.1....0...11111 001...011..0.0....0...11111
001...011..0.00...0...11111 001..00....01.....01.011111 001..00...10.0....0...11111
001.1.0...000.1.110.1111111 001.1.0...000...1.0.1111111 001.0.0.1..00..00.00.111111
001...001..100....00.111111 001..10.0.0.0.0.1101.111111 001.000.1.10..101.001.11111
001..10.0...0.0..101.111111 001.0.01..10.101.0000011111 001...0.0.01...0.101.111111
001...011....1110.0.0.11111 001.0.011.1...010.0.0.11111 001.00010......0000.0.11111
001.11011.11.00...000011111 001.000...010.1...0...11111 001.0.011.1...110.0.0.11111
001.000...011.1...0...11111 001..10....0..10..00.111111 001...01..00.1.0..010111111
001...0.0.0....0.0010111111 001.1.01...0...0..010111111 001..10.0.1000.0.0000.11111
001.1.01..000..0..0.0011111 001.1.0.0.11...0.0010111111 001.00000.00.0000.0.0..0...
001..10.0.001..0.0010111111 001.1.01..00...0..010111111 001..10.1.1..1..1.000.11111
001.100...000.10.00...11111 001..10.1.001.....0..011111 001..00.1.001.1...0...11111
001.100...000..0..010.11111 001..10...000..0..010.11111 001..00.0.000010..01..11111
001..10.1......00.0...11111 001.000.1...1.100.0...11111 001.1.000..1101..00.0.11111
001.000...01..0.000.0011111 001..10.1...0000..0...11111 001...00..10..0.00000.11111
001..10...00.0.0.0010.11111 001..00........0.00.0111111 001...0...010.00.00.0111111
001...0.0...0..0.00.0111111 001..10......00..00.0011111 001..00...1.0....00.0111111
001..00...1.0.0..00.0111111 001..00.....0.0..00.0111111 001.1000..1010...1001.11111
001..10.1.10.010..001.11111 001..10....0.0....010.11111 001.1000...0101..00...11111
001..10.1...00000.0...11111 001..10.1..1...0..0.0.11111 001..10....000....010.11111
001.0.00..1001.0.10.1.11111 001...0...00..1..10.1.11111 001.1.0...00..1.01001.11111
001..001..1110.0.0010.11111 001..001..1111...0010.11111 001..001..1111.0.0010.11111
001..00...10.0...1001.11111 001...0.0.1..0000.000.11111 001..10...1010...0000.11111
001..00.1.101.1.010...11111 001.100...101...01001.11111 001.100....0..1..00...11111
001.1000..001010.00...11111 001.1000...01010.00...11111 001.100....0..1...0...11111
001.00010.00000...010...000 001..00...1000..0.000.11111 001.00000.10000...0.....1..
001..00...10.0..0.000.11111 001..00.1.10..1.1.0...11111 001..10.1...0..01.0...11111
001..10.1......01.0...11111 001.1.0...00.01.010.1.11111 001...001..000....00.111111
001..00.1..0.000110.1011111 001.100.1..0..00.10.1011111 001.10001..0.00001001011111
001...01..100.001.010.11111 001..1000..0.1...0000111111 001..1000..0.....0000111111
001.01010..0.11...0...11111 001..00.1.01.1101.011111111 001.1.010.01.0..01011111111
001.11000..1.1..11011111111 001.00000.0.0000..001.00000 001.0001...0000...0....0.01
001.0001..10000...0....010. 001.110.1.11.11.11000111111 001..10.1.11.11.11000111111
001.0001...0000...0....0.00 001.00010.0..000..01...0.0. 001.00011.0..11000011111111
001.1.01..01.1.00.011111111 001.1.010.01...001011111111 001..10.0.0...10.0010111111
001..10.1..1.0.001000111111 001.00011.10.01010001111111 001...01..01...0..011111111
001.110.1..1.110.1000111111 001.00000...0000..01....00. 001.0.0....00.....000111111
001.0.0....0......000111111 001..1000.00.00..0001.11111 001.0.000..0....1.0...11111
001.01000.1..0...0010.11111 001.11000.1.01...0010.11111 001.01000.1.0....0010.11111
001..10.1.0...10.1001111111 001..1000..0..0000001111111 001...00...111.00.001111111
001.00010.00.000..0.1...10. 001.1101...11.00..001111111 001..101....1110..001111111
001..1011..11110..001111111 001.0.01...110.0..001111111 001.000.0..00..01.000111111
001.11000.10111..0010.11111 001...000.000...1.0...11111 001.11000..0.111.00.1011111
001..000...000...1000111111 001.1001..000..0.0000111111 001.11001.1.01..0.001.11111
001.11001.1.11..0.001.11111 001.11010..01.10.0001111111 001.0001....10.0.0001111111
001..101...01110.0001111111 001.1.0....01.1.11000111111 001.11011.1111111100000000.
001..0011..01110.0001111111 001..0001.0011000.000111111 001.0.011...1000.0001111111
001.10011.001..0.0001111111 001.010.0.1..0.1.0010011111 001.010.0.11.0.1.001001111.
001..100..01.1110.0.1011111 001.1100......11.00.1011111 001.10001.10.0010.00.011111
001.11011.1111111100.1.1001 001.11001.01.1110.011011111 001..0001.0..101..0.1011111
001..0001.11.101.00.1011111 001..0001.1.0101.10.1011111 001...0...01110...001.11111
001...000..0..0..00.1.11111 001...0.0...1.10.00.0.11111 001.1.0.0...1.10.00.0.11111
001..000..1001.00.00..11111 001.00010.00001...011...01. 001..1000.00..0..0001.11111
001.1.0.0..00.0.1000.111111 001..1000.00.00.00001.11111 001.0000..000.00.0000111111
001.0.000..00.0...000111111 001.100...001...01000111111 001..001..0001...1000111111
001...0.0.1000000.000111111 001...0.0..000..0000.111111 001..10...1000..00000.11111
001...000..1.0.1..0.0011111 001...000.01.1.1..0.0011111 001.00010.11.0...0010.11111
001...000.011101.00.0011111 001.0.001..1.11.11011111111 001...0....1..1.11011111111
001...00...10.1001011111111 001.0.00...1.11.11011111111 001..00....1.0..1.0.0.11111
001.01001..100..11011111111 001.010.0..100..11011111111 001..0000..000....000111111
001.000.0.0.00000.0.1...... 001.1101..010.0.01011111111 001.0.0...1000...10.1111111
001...0....00.10.10.1111111 001...0.0.001001.00.1011111 001...0.0..10..0.0011111111
001..0000..100....00.111111 001..100..1..1110.0.1011111 001..100..1..1.10.0.10.1111
001.1100.....1.1..0.10.1111 001.0.0.0.10...1.00.0011111 001..100...1...10.00.011111
001...0.0.00.111000..011111 001.10001..1.001000.1011111 001.11010....0.1..001001111
001.000.0....001000.1011111 001..00.1.0.1.00.0011111111 001...00...1...001001.11111
001..0000...11100100.111111 001..1000...11000.00.111111 001..1000.11.001.00.0011111
001...0.0.10.1.1.00.0011111 001..00.0.0.1.00.0011111111 001.000.0.0..00010011111111
001..000......0001001111111 001..000...110010.00.011111 001.11011.11111111001.11001
001.11010.0.1.00.0011111111 001.00010...1000.0001111111 001.11010..01.00.0001111111
001..0001.1..10100001011111 001..0001.1.11010.001011111 001..00.1..1.001..0.1011111
001..000...010.10.0..011111 001.00010.00001...010..1011 001..000...110.10.0..011111
001.11011.1111101000...1.00 001..100...110.10.00.011111 001..100...010.10.00.011111
001.1000.....1111.001001111 001..1000......110001001111 001.0.011.10.0.010001.11111
001..100..00...00.01..11111 001.000.1.0..0.11.0..011111 001.1100......11..0.1011111
001..0001.11.001..0.1011111 001.010.0.0....1000..011111 001.11001.1..1....0.1.11111
001.00010.1..1...00.1.11111 001...00..11.1.00.001.11111 001...00...0..1001001.11111
001.10001.11.0.00.001.11111 001.00010..0.....0010.11111 001..0001.....1..10...11111
001...00...1...00.001.11111 001..0001.....0...0.1.11111 001...000.00......0...11111
001.00011.01.10000011111111 001.1.0.0.011.11.00..011111 001.00011.0.110010011111111
001.00011..11000.0001111111 001.00010.00001..001....011 001.00010.00001..001.0..101
001.1.0.0.010.0100001.11111 001..10.0.0.0..1000.10.1111 001..0001....001..0.1011111
001..1010..0...010001.11111 001...00..11.1000.00..11111 001.1.00...1..000.00..11111
001.11010.00...010001.11111 001.1100...1..000100..11111 001.01001...101..100.111111
001..00.0.1..101000.1011111 001..0001.1..101..0.1011111 001.11010....0.1..0.1001111
001..1001....0..01001.11111 001..10.1..110.0..0.0.11111 001.10010..1..1010010.11111
001.0.01...0.0.01.010111111 001...0.0..10.10.0010.11111 001.10001.01000.01011111111
001.00010........00.1011111 001...00...0111001000111111 001..0001.....1...0...11111
001..1000..0.0...00.0.11111 001..1000.10.0...00.0.11111 001.01000.0.....00001.11111
001..1001.1..0....0...11111 001.00000.0000.0000..0...0. 001..00...1000..00000111111
001..1001.1.0.1...0...11111 001...000..0.11...000.11111 001...000.111.01..0.0.11111
001.11010.100...1.010.11111 001.100.1..0.11...0...11111 001...0.1.01...0.1011111111
001.00000.0.000...000...... 001.10010.111.01.00.0011111 001.00000.000000..01.....1.
001..00.0.11..00100.0111111 001.11011.111111..0111..10. 001.11011.111111..0111..1..
001..1000.....1110001111111 001.000.0....101.0001111111 001.10001..1.00001001111111
001.11011.111111..0.01..10. 001..1011..0..0000001111111 001..1001..0..0000001111111
001.10000.....1110001011111 001..1001..0..0110001111111 001.1.011....0110.001111111
001..0000..0..0110001111111 001.1.010......1.1010111111 001..100...0..1001001111111
001..10.0.0....0.0010.11111 001..0000..0110.00011111111 001..0000.0.011111011111111
001..0000..0011111000111111 001...01...0101.11000111111 001...000.10.1.11.0..011111
001.1.0....00.1.01000111111 001..1000.0010..00000111111 001.110.1.00000.000.1.11111
001..1000.00000.00000111111 001.1.000.00.1011000.011111 001..0000.0..001.00.1011111
001..0001.0..110.10.1011111 001.11001...100100001111111 001...010..1.0.001001.11111
001..00.0......0..0...11111 001..10.1...11....0..011111 001.1.01...1..1..1011111111
001.01001.000.0..0001.11111 001.0000...110110100.111111 001.010.1.0..010.1001111111
001.010.1.01111111001111111 001.00001..1.00101001111111 001...0...000.1.11011111111
001.1.0...000.1.11011111111 001..1001.00..1001011111111 001.10010..0..0.10011111111
001.110.0.1......1010.11111 001.000.1.1...101.0...11111 001.1.010..11001.0001111111
001..0010...1...100.1.11111 001..10...10.0..0.000.11111 001.01001.00..0..0001.11111
001...0....1..1..1011111111 001.0101..1011000.000.11111 001.1001...11.....010.11111
1000..0...........0.....1.. 1000..0...1.......00....... 1000110...........00.......
1000.10.....1.000.010011111 1000..0...11.00...000.11111 1000000........000011111111
1000.00.0....0..0.0..111111 1000..0...101000..000.11111 1000..0....1100.0.0.0011111
1000..0...........0.....000 1000..0...........0.....0.. 100000000.11111111011111111
100011010.00001011011111111 100001010.000..0..00.0.0.0. 1000.000..000.000.011111111
1000..00..1101.00.000111111 100011011.111110..00000.1.1 1000..0.0..00....1011111111
1000.00....000.00.011111111 100001010.0000.0..00.0.0.0. 10000.0....0..0000011111111
10000.0.......0.00011111111 1000..0...10......00....... 1000..0...0.......00.......
1000..0...0000.000011111111 100011011.111110..000000.00 100001010.0000.0.0011110101
1000..0.0.010..1.1011111111 100011011.11111111011111111 10000.0.0..110..00001111011
1000..0.0........1011111111 1000..0....0...0..011111111 1000..0...1...0..0001111111
1000..0...0...0..0001111111 100001010.0000.101011110101 1000..0...10..0..0001111111
1000..01..10000100001111011 100000000.........011111111 10001.00..1010.1..00.0.1111
1000..0...........0.....0.0 1000..0.0.011.....001011111 1000..0.0.0..0....001.11111
1000.10.1..001.01.0..111111 1000..00..110100.10..111111 1000..0....001.01.0.0111111
100011010...0.0010010.11111 10000.0.0.0001.0.1011111111 100001010..1.1.1.00.0011111
1000..0....1001.1.0.0011111 1000..0....101.01.0.0111111 10001.0.1.0.0.101.0..111111
1000..0...1.0.00.100.011111 1000..0...........0.....011 100001010.0000000.0...0.0.0
100001010.0000000.0...1.0.0 1000..0...1000...00.1011111 1000.10...11.000..0.0011111
1000..0.0.1.1.....001011111 1000..0...0.10.0.0001011111 1000.10........0.00010.1111
1000100...1110.0100...01111 10000.0...10..00..0...11111 1000..0......0..0.01..11111
1000..0.....1000..0..011111 10001.00..101011.00010.1111 1000..0...011..00.010011111
10001.0...101.10.0001001111 10001.01..1010.1.0001001111 1000..0...1010.00.0.0011111
1000..0...1010000.0.0011111 10000.0.0.110.101.0..111111 100010011.0..01...0..011111
100011010.0.0001.00..011111 1000.00.0.1.01.01.0..111111 1000..0...110100010..111111
100000000.00011011011111111 100011011.1111000.0....101. 100001010.0000....0.....0..
100000000.01011111011111111 1000100...001.10.00.1001111 1000010.0.10.100..011001111
1000.10.0.1...00..00.011111 10000.00..101.00..010.11111 1000..0...1.10.00.0.1011111
1000..0....111000.0.0.11111 1000..0....110000.010.11111 10001000..1..0000.00.011111
1000..0...000..0..011111111 10001000...1.....00....1111 10001000...1.....00...01111
1000..0.0.01000...0...11111 100011011.110..0..000111111 1000.0001.11.0000.000111111
1000.10.1..0......0.0111111 1000..0...11...100000.11111 1000..0...11100...000.11111
10001.00...1..1.1.0.00.1111 10001.00..11..1...0.00.1111 1000..0....010.0..010.01111
1000.10.....10.0..010.01111 1000..0....110.0..010.01111 10000.0...101.....011001111
10000.0...101..0..011001111 10001000..01.000..0.0011111 1000..011.11.110..0..111111
1000100.1.....001.0..111111 1000.00.1..0010.1.0..111111 100010001...00001.0.0111111
10001100..1.10.0.0000011111 1000.10....11100..010001111 10001.0...01.0..0.0.0011111
100001010..000....0.....0.. 1000..0...10100...000.11111 1000.10......010.00.1011111
10001.00..10...00.00.011111 100011000...000.11011111111 100000000....00.11011111111
1000..001.000.....000111111 1000100.0.0...1.0000.111111 1000..0...0....00100.111111
1000..0...01..1..100.111111 1000.10.1.1...1..1001111111 1000..0...000.....000111111
1000..01..011.010.0.00.1111 1000110...010.0...010..1111 1000..0.0.010..1..001011111
10001.0.0..1.0.1..001011111 10001.00..1.1011.001.0.1111 100011010.1101..00001.01111
1000..000.110001..0..011111 1000..0....0..0...0.0.11111 1000..0...10.00.0.000.11111
10001.00..10..01..0100.1111 1000..0.1..010010.0..011111 100011000.011.0...010101111
1000.0001.1100.1.00..011111 10001.010.100..11.010011111 100010001.111..10.010.11111
1000..011..10..1..000011111 100010001.111..10.010011111 10001.01..100.011.010.11111
100011000..100111.0..0.1111 1000..0...0.001..100.111111 100001010.000...110111...00
1000.1010.111101000.00.1111 1000..01..100..10.010011111 10001.010..1.111..00.0.1111
10001.01..00..11..0.00.1111 10001.001....1..01010011111 1000..01..010.0.0001.011111
10001.001..111..01010011111 1000..01...100....0.0011111 1000..0....100....0.0011111
10001.001.1.10010.00.011111 10000101..1110010.010011111 1000..0....0..001.0.01.1111
100001010.000...110111.0.0. 100011011.11111111000000000 10000.0.0.........0.1.11111
10001000..111..10.00.011111 1000..010.0110.0.00.01.1111 1000.10.0..1.101000.0001111
1000100.1..0.001010.10.1111 10001.010.01.011100.00.1111 1000.1010.1..0.0000..1.1111
100001000.000.011.0.0011111 1000..011...0.01..00.011111 1000..011..100.1..000011111
10001.0.1...00.000000011111 1000..0.1........00.1.11111 1000.00.0..1..1..10.1111111
1000..0.1...00.0000.1011111 100000010.0001.011011111111 100011010.000..0..0.0..101.
100000000.101..0..011111111 100010010.00011011001111111 10000.00...11.01.00..111111
10001.00...010.11.001111111 10001.01...000.00.001111111 10000.00....1.01.00..111111
1000..0.0.100.01..00.011111 10001.0....010.0..001111111 10001.0...1010.0..011101111
1000.0001.1.1.000.00.111111 1000110.1.1..001.0010011111 10001.00...010.10.001111111
100001000.10.01.0.0.0111111 100011011....00.00011111111 100000010.01..0..000.111111
100000010.0...0..100.111111 10000.001.1..1101.0.0111111 10000.001....0101.0.0111111
1000..01....0..10.001111111 10001000..110.000.000111111 100010001.110.000.000111111
100011011.11111.000...100.. 1000.1011.0.1.0.10001111111 100011011.0..10.10001111111
1000..011....11...0..111111 1000..0.1.11.00000000111111 10000.001.11....11000111111
100000001.11.01.0.000111111 1000..011.11.111..000111111 100010001.11000000000111111
10000.001.11..0.10000111111 1000..001..0..10..00.111111 1000..011.110...00000111111
1000.00.1..10.01.00.0111111 1110..0...........0.....0.. 11100000...000100.000111111
1110..0...........000...... 11100.0.0.0.11..0.0.0.0.111 111000010.0.1..0..01.1.0...
111000010.00......0..1.1... 111000010.00......0..1.11.. 1110..0...........011...100
111000000.00......000111111 11100.0.0..0..0.0.001111111 1110010...........00.......
111000000..0......001111111 11100000...1..0..0000111111 1110..0...........0.....1..
11100.0....0.010.1001111111 1110..0...10..00.1001111111 11101.0...........00.......
11100001..10.1.0010.1111111 111011011.111111110..1..1.. 111000010.1..1.01.0.0111111
11100101..10.1.0010.1111111 1110.000..0..0...10.1111111 1110.000..01.0...10.1111111
1110.000..10.0...10.1111111 11100000...0.1...10.1111111 11100100...00....10.1111111
1110.000..........011111111 11101.0.1.110000000..111111 1110000.........00011111111
111000010..0....0.0.1111111 1110..00..0.....00011101111 1110..0........0..011111111
111000011....110000..111111 1110.00.0.1.....1.0.0111111 111010000...000.1.0.0111111
11101.01...10110110.1111111 111011011.111111000..1..100 111010010...00.00.0..111111
11101.01...10.10.1000111111 11100.00..010110110.1111111 11100100..........00.......
111000000.0....1.1010000101 1110..0...........0.....011 11100.0...........00.......
111000010.1.......0..010..1 1110.10.1.0.01.01.000111111 1110.00.0.0.010010000111111
111000000...1111110..111111 1110000.0..00..0..01100.011 111001010.010000.100.111111
11100.00..000110110.0111111 11101001..01100.100.1001111 111010010..0..000.001.01111
111010010..0..000.001101111 11101001...1..00100.1..1111 111010010..01..10.001001111
11101001...11.00100.1001111 11101.0...1......10..0.1111 111011011.11111011011011011
111000000.00.1..1.0.1111111 1110.10.0.10.0..100.00.1111 111010010.1000.0.00..1..1.1
1110..0.0..01.1..00.00.1111 1110010.1.0.1.00010..001111 1110010.1.001.00010..001111
111010010..011000.001101111 1110010.1.00..0..100.001111 1110.00.0.00.100..001.01111
1110.00.0.00.1000.001.01111 11101100..01..000100.011111 11101100..011.0.0100.011111
1110.00.0.000100..001101111 11100.0.0..0....00000..1111 1110..011.11.100..01..11111
1110110...110..0110..111111 1110110.0.101...100.0011111 1110.1000.00...1.00.0001111
1110010.1.00..010100.001111 1110.00.0.001000..001101111 1110.00.0.001100..001.01111
1110..0...000.00.1001111111 1110..0...000..0.1001111111 1110..0...000..0..001111111
1110010.0.0010.1.00.00.1111 111010010.100.....0.01..101 1110..0.0...1.1.000.0001111
1110010.0.001...000.0001111 1110.000....11..00000...111 111000000..1010100001111111
1110100.0.0.1..10.0..011111 111000010.001.110.00.1.1011 111001001.0.01110000.110011
1110.00.0.0...111.00.0.1.11 11100.01..00.1.01.0.1111111 11100.00..00.11.1.0.01..1.1
1110110...00100.000..011111 111000011.11011100000111111 111000000..0100100001111111
111000000.00011011011111111 11101.0.1.10.0100101.1.1111 1110..0.1.10.00.0101.0.1111
11101.0...10.0..01010100.11 111010010...1.1.000..100.11 1110.00.0.1.101.0101010..11
11100.0.1..0.0100101.1.1111 1110.100...01...0001.001111 1110..0.1.001.001100.0.1111
111010010.1.1.1.000.00.1.11 11100.0.1..01.000101...1111 1110.0010.001..0..0..101111
11100.00...0.....00.0....11 1110..0...000.10.1001111111 111000000.0.......00.......
11100.00..00..1...0.0....11 11100.00..00.11.1.0.0....11 1110.100..00....0000.011111
1110010.0.10.1.1000.0011111 111001010..0..01100.0011111 1110..0.0.010.01..00.011111
1110000.0.1000..1.0.1...101 11101.0....0.0.0..001.11111 1110..0...00.010.1001111111
1110..0...000...0.001111111 1110..0...10...0.1001111111 11100.00...0...0..0.1111111
11101.0....0.010..001.11111 11100.00...0......001111111 1110.00.0.10......000111111
111011011.11111100000.110.. 1110010...010..001001111111 1110.00.0.01.00.00001111111
111000000.00.11.110.1111111 111000000..0.11.110..111111 11100.010.00..1011001111111
11100000..10..0.01001111111 11100000...0..0...001111111 111000000.........000111111
1110..0...000..0..000111111 11100.00...001.011001111111 0110..0...........0..0..0..
011011011.11111111011011011 01101101...00.....0.1...011 01101101...00....00.....01.
011011011.111111110000..0.. 0110.100....0..001011111111 01101.001.110...110.1111111
0110.100..0..10100010.01111 0110.1001.10.00110000111111 011010010.001.....0.....1..
0110..0....01....00...0.111 0110..0...........0.01..1.. 0110..0...........0.0......
011011011.1111111100.011011 011000000..1111111011111111 011000000...111111011111111
0110000...11.000..000111111 011000011...1.....00....... 011000000.01......000111111
0110.101..........0........ 0110..0...........0.11.01.1 01101.01..........01.......
01101.01..........00....... 01101.01..0001.01.0.1111111 0110.10.....01.0.1011111111
0110..0...0011.011011111111 0110.101...001.0..0.1111111 0110..0...000.10.1011111111
0110..01...001.0..0.1111111 011011011.111111110..1..1.. 0110..0...11011011001111111
011011011.111111110110..0.. 0110..01..010100.10.1111111 0110..01...10100.10.1111111
0110..0....00100100.1111111 01101.001.10010.0.0.1111111 01101.01..00.10.100.1111111
01101.001.10.10..10..111111 01101.01...00000000.1111111 011011000...0...110..111111
0110.00...1.01.011001111111 0110.00...1.01.010001111111 0110..0...........0001..1..
0110.101..00.1.10.0..100.11 011000011.0.1.....01....... 0110..0...110..0..000111111
0110.0001.1.0.01.10..011111 0110.0001.0.0.01.10..011111 011000001....1010.0.1011111
011011011.111111000..1..100 011000010.0..0111001.0.1111 011000011...1.....01.......
0110.00.0.0001.01.001111111 0110.00.0.1.01.01.001111111 011000011...10....0........
01100.001.00.1.10.01.0.1111 011011000..0.0.1010.001..11 0110110.0...1.01.000.001111
0110.100..00..11.001.0.1111 01101.00..00.1.10001.0.1111 01101.00...0...10001.001111
01101.0...0...01000..0.1111 01101.00..0..1110001.0.1111 0110110.0....001000..011111
01100000....11..00001.11111 0110110.0.00.0.11.001001111 0110110.0.0...01000..001111
01100.011.111.00.0000100111 01101100..011..10.0100.0111 0110..0...........0111.010.
0110.101..........00....... 0110.10...0...010001.0.1111 0110.00.0...1..10.0..101101
0110..0...........0.11.1100 0110.101..........01....... 01101.0.1...10..0.0.0.00111
01100.0.0.01.0.1100..011111 0110100.1...10..0.0...01111 011011011.111111..0..1..110
011010011.1...10..0..111111 011010011.0...10..0..111111 011011011...0..0..011111111
011001001..0.0..0.0..111111 0110.001..00.1.0010..001111 01101.0.1...0.101.0..111111
01101.0.0..011.1.000..01111 0110.000..00.1.1010..0.1111 0110.10.0.0.1..10.010.01111
0110..0.1..01..1.00..11..11 0110.001...010.10100110..11 0110.101....11010000..01.11
0110..0.0...0000000..111111 011011010.0.1001.000.001111 01101.0.0.1.00..0.0...11111
0110.10.0..101..000...11111 0110110.0.01..01000.0011111 0110..0...0110.00.0.0011111
0110..0....00010010..111111 0110.100..11.1010.0.0011111 0110..0.....0110110..111111
0110..0....00.10.1001111111 0110..0....101.00.0.0011111 0110..0...1.0.00.000.111111
01100.00....0000000..111111 01100.00..0.1....00...11111 0110.001..01100.1.0.0.11111
0110.101..001.1..00...11111 01100101..00..1..00...11111 0110.10...00...00001.0.1111
0110..0.0.0.10.1.001.001111 0110..0.0.0.1101.001.001111 0110.00.1...10.1..00.10..11
0110.101..0..101000.0100.11 01100.01..1.01..0100..01111 0110.000..00.1.10101.0.1111
01100.0.0.0...011001.0.1111 0110100.1.0.10.1..0..10..11 011011001.100...0.000111111
011001010.11110.0.000101111 0110..0...0001.01.0.1111111 0110100.1.0..1001.0..111111
01100.0.1..0..00010..111111 0110.00....0.000010..111111 01100.00......0..10..111111
0110.00......0.0010..111111 0110100.0.0..11..0010.11111 01101.001.10...10.001011111
011011000.1.0.1.0000.1.0.11 0110.00.0..010.10.0.0101101 011000011.00.11.000...00.11
011000011.00....00011.00011 01100.0.....1.010.0..110101 011001010...11010.0.0.01111
01100.00......0..00..111111 01101.001..0010..10..111111 0110..00...010010.0.1011111
01101.01...00100100.1111111 011010000..0.010110.1111111 011010000..01.0011001101111
011000000..0.0000.0.1...1.0 011010000..0.0.0110.1111111 0110.00....0.0.0000..111111
0110.00....1.000000..111111 011010001..0.00.110.1111111 01100.00...00000000.1111111
011010001....10.01011111111 011011000...000000011111111 011001010....10.010..111111
0110..0...........0.1...... 011010000...1.10010.01.0111 011000001..0.10.110.1111111
01100001...0.0..0.0.1111111 0110.000....0.000.011111111 011000000.00......000111111
01100.00...000.00.0.1111111 011000000.00......011.00.00 01101.0.0.1.100.000.1.11111
0110110.0.010.01000.0011111 0110.100..0.10..0.010.11111 01101000..00.00.0.0.0.11111
011010010.00.10.100.1111111 0110000...00.000..000111111 011000000.0.......0.0.11.11
011000000.1.......00..11.11 0110.1000.1.1101.000..11111 01101.00..1.1.01..001011111
011001010.0110011001..11111 01101001...0..1.000001.1111 0110000....1.0.1.0010.11111
0110.100..1.0001000.0011111 0110.1000.1.1..1.000.011111 011010001..0100.110.1101111
01101.0.0...10.1.000.001111 01101.00..00111110010011111 011001000.000101100.10.1111
011001000.10100110010.11111 011001000.00..01100.1..1111 0110..0.0.1.1.01.0001011111
011011010..1...11000..01111 0110..0.....0..0..011111111 0110.00.0.1.010010001111111
011000000..0...0..01.0..1.. 011000000..00..0..011...... 011000010.00.0111001.0.1111
0110.00...1010101.000101111 0110..0...1.0..0..001111111 01100100..1..00.0.010.11111
0110.100......010.010011111 0110.100...1..010.010011111 0110..00....1.110001.0.1111
0110.00.0.1010....00..11111 0110000...101..1000..011111 011010010.0.......001......
011010010.1.0000000..111111 011011011.11111111011000000 011011000.11000100011111111
01100.0.1..0101.1.0..111111 0110..01..0.11.0..0.0111111 0110..001..00.1.0100.111111
011001001..0.01.010.1111111 01101.000.00.0110001.1.1111 01101.010..111..0000..01111
01100.0.0.001..1..000111111 011000000.001..1..000111111 011000000.0.1..10.0.0.11111
011000000.11000111011111111 011000000...10.10.0.0111111 011011010.01100.0.000111111
011011011.00011011011111111 0110..0...000..1..011111111 0110..0.0.100..1.0000111111
011000000.11100100011111111 0110.0011.111.1100000111111 0110.0011.1001.0.1001111111
0110.00.0.1.0..1..001111111 011011011.11111111000111111 011011011..10000000.1111111
011000000...011011001111111 0110.0010.001000..0..11110. 011000011.1.011001001011111
01101.0.1.0111..000.0.01111 0110.00.0.0.1101100..111111 011010010.001000..00.00.1..
0110..0.1..1....000.0.01111 01100.00...011.11.001111111 0110..00..000.111.001001111
011001011..11..100010001111 0110010.0.111..1010.0001111 0110.0011...1101..0..111111
011010010.0.1001.000.001111 011000000...100011001111111 011000011.00100011011111111
011000000.101001000..111111 0110..001...100010010101111 1010..1...........00.0.....
1010..1...........00.0..1.. 1010001.1.........00....... 101000101.........00.......
101000111.........00....... 1010.01.1.0.111111000111111 101000111.0.......00.......
1010.01.1.1.111111000111111 1010..1.1.1.011.11000111111 1010111...0000.011000111111
1010111...0.0...11000111111 1010001...11101.11000111111 1010..1.1.1.011.1.000111111
101001110.00......00......0 101001111..1001111001111111 1010..1...........0.....0..
1010111...1.10.0.00.0.11111 10100.1...........0........ 101010100.00......00.......
101000100.10......00011.0.. 1010..1...........01.1.11.0 1010..1...........0.....1..
101000100.10......0....1.1. 1010.11...010100..0...11111 1010.11.0.1.11.00.000.11111
1010101.0.11...000000.11111 10101.1...........0........ 101010110.00......010101001
1010101.0.0.1.00.00.0011111 101000100.10......010111011 1010..111.0.0.1.1.0.0111111
1010..1.0.0.0.1.100.0111111 1010..1...........00.0.0.01 1010..10....011.110.0111111
1010..10.....11.110..111111 1010..1...........0101..0.. 101010111...010...0.0111111
1010101...0.0...110.0111111 101011111.111111.100.10..0. 1010..111...011.110..111111
1010..111....11.110..111111 1010.010..1..1..110.0111111 1010001...0.1...01001011111
10100010...00....10.1111111 10100.1...........00....... 10100.10..00.1..010.1111111
10100111....01...10.0111111 10100.10.....00.010.0111111 1010..1...........00.0.1.1.
1010..1...........00.0.1.10 1010.010..1.....010.0111111 101001110.10.00..001..10..0
1010001...0.......00....... 101001101.11110000000111111 10100.1.0.1.011.10000111111
101011111.11111110011101111 101001111...0.01000.1111111 10100.1.0.0.011..00.1111111
1010..1...........00.0..10. 10100.10...0.00.010.1111111 1010001...1.010.110.0111111
1010..1...........00.0..000 101000100.10......01...1.1. 10101010..1..10.0.0.1.11111
10100.1.0....0....0.1.11111 10100110...0110..00...11111 101010100.1001.1.00.0.11111
101010100.1..01...0...11111 1010.110...0110.0000..11111 10100111...001...10...11111
1010011.0.0001..100.0.11111 1010001...........00....... 1010.110..1111000100.0.1111
1010.010......0.0.001011111 1010..1.0.01.00.100..011111 1010..1...........01.1.....
101010110.00000...010001.00 101010100.01001.110..111111 1010.111..1.1.1.1.0.1.11111
101010100.101...00000.11111 1010..1...........00.0..100 1010..1...11.11.110..111111
10101.11..00.11.110.1111111 10100111.....0....0.1.11111 1010..1...1101.011010011111
1010001.1.0110..0.0.0.11111 1010..1...110..011000011111 101000110..111.0000.0.11111
101011111.11111..101.00.01. 1010.111..1.....010.1111111 1010.111..1.....1.0.1111111
1010.11.0.1..1..1.000111111 101011111.11111...01.00.01. 101011111.111111.100.00..0.
101011111.111111.101.00..1. 10101.11..00.0..110.1111111 10100.10...0.01.010.1111111
101000100.10......010101011 1010101.0.1110.000000011111 1010101...10101000000011111
10100.1.1.1..11.110..111111 1010..1...........01.1.0.00 1010..1...........01.1.111.
10101011..01010.110.0111111 1010..1......11.110..111111 1010..1...1..11.110..111111
1010011...........0........ 1010.01.1.1..1..1.000111111 101001110.10......001...0..
1010..1...0.0.....011111111 10101111..0.001.110.1111111 10100.111...011.010.1111111
1010..1...0.0.1011001011111 101001110.10......0......10 1010101.1.00.1....01..11111
1010001.1.1...1.1.01..11111 10101111....00...0000..1111 1010111...1.0.....000.11111
10100.1...0101101.0.0.11111 10101.1....1.11.1.0.0.11111 1010101...01110000001010111
10101.11..0..10.10011111111 101011111.111111.00..00..1. 1010001...1100...10.0111111
1010.11..........10.0111111 10101011...1010.1.01.111111 1010.01....1.....10.0111111
1010001.1.00..0.11001011111 101010110..0...0000.0011111 101010100.11.11.0.00..11111
101010100.1..0.00100.011111 101001110.10......0.......1 1010..101..01.100.00.011111
1010..101.111.100.00.011111 101001110..1.00010010011111 101001110.00......00...0..1
10101.1......11.110...11111 10100.1...101..0.0001011111 1010.11...11.11.110...11111
10101.101..010100.00.011111 1010..10...01.1.0.001.11111 1010..1...0..0...1001.11111
1010101.0.1.10...00...11111 10100111.....11.110...11111 10100011..1.010.110.1.11111
1010.11...10......00....... 10101.1...111.1.0.0...11111 10101111..0.001.1.0.1.11111
101010100...0..0110..011111 1010.01...0.0.0..1001.11111 10100.10..1.0.0.01001.11111
1010001...0......1001.11111 1010..1...01..1..000..11111 1010001...0.0.0..1001.11111
10100.1.0.100...10010.11111 10101.1.0.01.10.10010.11111 10100.1...0.01...1001011111
1010..1...0.0....1001011111 1010.11.0.0..10.1100.111111 10101.1......1....011111111
1010..1...........011111111 10100.10..11.00...000111111 101010110.00.....1011101000
10100.1...0.00...1001011111 1010..1.1.0.0.0.01001011111 10101010..11100.0.000011111
1010..1....10..0110.0011111 10100.1.0..0.00..00.1.0.... 1010.111..10......00.......
1010111......11...011111111 1010.010.....0...0011111111 1010011.1...0.0.0000.111111
10101.11...1.1..1.01.111111 10100.10..11.01.0.000111111 1010..1......00.000..111111
1010..1...1..00.000..111111 10100110..1.0...00000111111 1010..1.0.0.0....1011111111
101000100.1.......0....0.01 1010..111..001.1.101.111111 10100110...0010.1001.111111
10100.1.1.0101.1.1011111111 10101010..1.0....1000111111 1010.0111.0.0.0111010111111
1010.0111.0.0.01.1010111111 101010100.11010100000111111 1010..10..0.001101001111111
101010111.0001.111001111111 101010100.10.1.1.1001111111 1010..100.0.0001.1001111111
1010111.0.10.10101001111111 10101010..0..11101001111111 10101010..10.101000..111111
101010100..0..011001.111111 101010100.11.1010.0.0111111 1010.1111.11..11110.1111111
101000100..10011110.1111111 10101010..01010.0100.111111 10101.11.....01.110.1111111
10101.11...0.01.110.1111111 101001111.0.00...1001011111 101011111.1111111001.101.11
101001110.000.....00.0..... 10100111..0.011.11001011111 1010..1.1.0.0.1.11001011111
101011111....01110011111111 1010.11.1.1..00.000.1111111 10100111..000.0.000..111111
101000100.010011110.1111111 101001111.0.001.11011111111 101001110....001100..0110..
101000100.0.011.10011111111 10100.11....111111001011111 101001111...01.10.0.1111111
1010..1...........00.0..101 101001111..100.11.001111111 1010.0111.1.0.01110.0111111
1010.0111.0.0101110.0111111 1010.0111.0.0.01110.0111111 1010..10..0.00.101001111111
101010111.01010.110.0111111 1010.0100.01001.110..111111 1010.0100.0100.1..0.1111111
10101.100..001.1.0010011111 1010..111...0011110..111111 101000100...101010010011111
1010.01...0.0.0.11001011111 1010.1111.01..11110.1111111 101000100..1.1.1110.1111111
1010.01....1.....10.1111111 101000100..0.1.1110.1111111 10100111..1000...001.11000.
10100010...1.10.1.0.1111111 10100010..0.0...01000111111 10100010....0...000.1111111
1010001.0.0100..0.0.1111111 10101.1.0.11.00..00.1111111 10100111..1.00111.01.011111
101001111.0.000.00011111111 1010111.0..0.00.0.0..111111 1010111.0...000.0.0..111111
101000111.0.0.0111000111111 1010111...0.0...01000111111 1010101.1.0.0.0.1.000111111
1010111......11.00011111111 1010001...01100.11001011111 10100111..010.1111001011111
1010..1...0.0.0.01001011111 101001110.1000.1.1001010001 101001111.010.1111001111111
10100010..1.0.0101001111111 10100110..1....101001111111 1010..1...01100..1001.11111
101001110.10......00111000. 1010001...000...0.000.11111 1010101...1.100..1001011111
101001111.0.011.10011111111 1010..1.1.010.1111001011111 1010.010..0.0.0.01001011111
101001110.10......001110.01 1010..1...........0111.111. 10100010..01..0..1001.11111
1010.010..01000.01001.11111 1010..1.0.0.....00001.11111 1010001...000.....000.11111
1010101.0.10.0..000.0.11111 1010.11...101.000000.0.1111 1010.1100.0011....0...11111
101010100..01011.00.0001111 1010.010..101.000.001011111 1010..10....0.000100.011111
1010.010......000100.011111 10101.100..1010100010.11111 1010.0110.0.1010.00.0011111
101011100.0.0.0.110..111111 10100010...0.....00...11111 1010.010..0.0.0.0.001011111
1010.0111.010.001.0.1111111 1010..1.0.1.100.0.011111111 101001111.10101011011111111
1010.1111.10101011011111111 10100.101.0.00.0010.1111111 101000111...11000.0.0111111
1010.11.0.1.110011000111111 101011111..0.01.11011111111 1010.110..01110...00..11111
1010.010..11..000001..11111 101001101.10.10010000111111 1010.0101.000.1011011111111
101011111..0100010001111111 101001100...11..110.0111111 101000111.00101001001111111
101001110.10100..001.110... 101001110.10100..101.110..0 101011111.111111110.0.11.11
101001110.10100..101.1000.1 101010101..10.11100.0011111 10101010..11..0.0001..11111
1010..1...00000000011111111 10100.101...11100.00.111111 10101.110..1.1001101.111111
10100.111.000.0..000.011111 101001111..0.00000011111111 1010.1110.0.1100.00.0111111
10101.10....100010001111111 101001111..0.01011011111111 101011111..0.00000011111111
1010.11.0...11.0100..111111 1010.1110...01.0.00..111111 101001111.00.01001001111111
10100010..0.0101.1001111111 1010..10..00.010.1001111111 1010001.0.010.1000001111111
10100110..0..110.1001111111 1010..1...00.00000001111111 10100111....0..1..0..0.0.00
1010..10..0.1.1111001111111 1010.01.0.1.11.010010111111 10101.110.01110010010111111
1010..1....101....0.0011111 101001101.10.10011011111111 101011111.00110010001111111
1010..111...1010..0..111111 1010..1.0.1.001.010.1111111 1010..1......000000..111111
1010..1...1..000000..111111 10101.1...11....000.0.11111 1010001.0.0101.00.001111111
1010.010...00.1.00000011111 101001101.01.1.100001111111 1010.010..011.00.1001111111
10101010..00.0.001001111111 1010.010..0....011001111111 1010111.0..0..0...00.01.100
101001100.1.11..110.0111111 1010101...011..0.00.0111111 10100010..1.01.0110.0111111
1010.010..011.1.110.0111111 1010.01....11111110.0111111 101011110.0.0000110.0111111
1010.01......10.110.0111111 1010.0101.10..1111011111111 101011111..0.11.11011111111
10100.10..1.1...110.1111111 10100.10...01.....0.1111111 101001110.1000101.01.001.1.
101001101.1.11001.000111111 1010.1110.0.1100.1000111111 101001101.001.0000000111111
10101.1...1.11....011111111 10100.10...01..1..0.1111011 10100010..11001.01000111111
101000101.1..1.000000111111 10100010..1..100110.1111111 101010111.11.01.0.000.01111
10101.1.0.00.01101001111111 1010101...10.1.100000111111 101001101.10110010000111111
10100010..10.01110000111111 1010..100.000.01.1011111111 1010..1.0.000.00.1011111111
101001110.000.00.100......1 1010.01.1.1.1111110..111111 101000111.00111.000..111111
10100.111.01011.110.1111111 101000100..1010.1.0.1111111 10100010..11..1.1.000111111
10100.10...1.100000.1111111 10100.10...111..010.0111111 10100.10...1.10.010.0111111
1010.01...1.100.010.1111111 1010.01.0.1.00..000..111111 10100010..110110110..111111
1010..10..0.1000.10.1111111 10100.110..010.0..0.00..1.. 101000111..0101001001111111
0010..1...........0.10..1.. 001001111.........0........ 001000100.0.......0...0....
0010.010..00010001011111111 0010..1...........01....... 001001101...0111.0010011111
0010..1...........0.....0.. 0010..1...........0..1.0... 001011110..0.0.0..0.1.11111
001011100.1010.00.001.11111 0010..1.0.00..10..001.11111 0010.110..000100.101..11111
001011110....0.0..0.0.11111 0010111.0.111..000010.11111 0010..1...........0..0.....
0010.0100..11..0.0010.11111 0010..1...........0.0...0.. 0010.0100...1..0.0010.11111
001001111.........00....... 0010.11.0......000010.11111 0010..1...........0.01..0..
0010..1...........0.11..1.1 0010..1....1..0000010.11111 0010..1...........0.1...1..
0010..1...11...000010.11111 0010.010....1.10.0010.11111 0010.010..........00.......
0010011.0...1.00.00.0011111 0010.010..........01....... 001001101...0.1100010011111
00100.1...10.11000001.11111 0010.0100..00..0.0010.11111 001001100.1.1.00..010011111
0010.1111.........01....... 001011111...1.....01....... 00100111.....1...00.1.11111
0010001.1..0......00..11111 0010.010..10110000001011111 0010..1...........0101..0..
0010.01.0..1......0.1111111 0010..10...10.0.1.0.1111111 0010..10..110...1.0.1111111
00100010..11..1...01.111111 0010..1.0..10.0...0.1111111 0010..1.0..1.0..0101.111111
0010..1.1...0.....0.0111111 00100.1.0.1.01....0.0111111 00100011...0..1...00.111111
0010001....0..110.01..11111 00100.100.111.001.0.1011111 0010.0100..0.0.1.10...11111
0010011.1...0.0.0000.111111 0010..1.0.00...1.10...11111 001000110....111010...11111
00100.100.011.001.0.1011111 00100.100.101.001.0..011111 001000101.110..1..010.11111
0010..1....1000.000..111111 001011111.111111110101..0.. 0010..1...........0.....1..
0010..1...........0..100... 0010..1...........0..1.1..0 001000111..1..0...000111111
00100.11...0..1..1000111111 001000111..0..0...000111111 0010.111..........0........
0010101.1.00.00.0.001.11111 0010..11..10..0..0010.11111 0010.1111.1.0.1.1.0.1.11111
00100011..101.0...01..11111 0010.11.1.0..01...001.11111 0010..10..10110.01001011111
00100.11...0.00.110.1.11111 00100.11..1010...0010.11111 0010.010..1.110.01001011111
0010011.0.11.0..00010011111 00101.1.1...000...001.11111 0010..101.11011.0.000111111
001011110..10....0000111111 0010.01.1.00000...010111111 001011101..10...0.000111111
0010..1...0.0.1.11011111111 0010..1...0.0...1.011111111 001001110..1000...00.111111
00101111..0.0.....011111111 0010.0100.1101...00.0.11111 0010.0100.1010...10...11111
0010.1100.10.0..00000.11111 001000110..11..0000.0.11111 001010100..1.01.110...11111
0010..1.0..0.....101.111111 001000100.00.000..0.0...0.0 001011110.101.00.0010011111
001011110.1110.0.0000011111 0010.111..........01....... 0010.111..........00.......
0010.0100.1.11...00...11111 001011111.111111110.1.11.11 001011111.111111110...11.11
0010..10...00.000.000111111 0010101.1...000...001.11111 0010.0101.1..00.0.001.11111
0010.0101.1.110.0.001011111 001010100.1...1.0001.0.1111 0010.010.....10.0.001011111
0010.010..1..10.0.001011111 0010.010..1011000.001011111 001010100.11.11000010001111
0010..1.0..10.01..0.1111111 0010.010..11..1.100.1111111 0010.01....1..11.00.1111111
001001110.10111011001011111 001011111.111110.100000.0.. 0010.1111...11100001..11111
0010.0100..0.0.1.0010.11111 001011110.1010.0.1001011111 001001101..0..0011010.11111
00100.101.0.0..1110..111111 0010..1...1011101.001011111 0010..1....00.0111000111111
0010..1....0000111000111111 001011111.111111100000.1011 0010.01.1..10..1.00.1111111
001001100..0000.1.0...0..10 001011110.01.001.1011111111 001011110.01..01.1011111111
0010..1....1..1111011111111 0010011.1..0.00011010011111 001011110.0.0....1011111111
001011110..1...1.1011111111 001011110.010.0101011111111 0010.01.0...1.00.10.1011111
0010..1.0.0.0....1011111111 0010..111..0......01....... 0010001.1..1.111.0011111111
0010001.1..1..0111000111111 0010.11...10.0110.000111111 001000100.0..011.000.111111
0010..1...........0.00.0001 00100.11...000.11.000111111 001001110..00001010.1111111
00100.101..0.1.11001.111111 0010011.1.00000..1001111111 001010100..1.111110.1.11111
001000100....0....0.1.0.1.. 001011111.111110.1000001.0. 0010001.1....0..1100.111111
0010..1...111110000.1011111 0010011.1...000.1100.111111 001011111.1010.0.1001011111
001001101.000001010...01111 0010.010..01.111100.1111111 0010..10..110.01110.1111111
00101.1.1..1.11111011111111 001011111.1111111100000.0.0 0010..101.000.0.01001111111
0010.010..........0........ 001011111.1111111100.001.11 001011111.0.001.11011111111
001000100.01000..0001...1.. 001000100.0100....0..0..1.0 001000100.0100....0..00.1.0
0010001.0.0..0....011.0.110 001000100.0..0....001000100 001000100.....11.101..11111
001000100...1..1.10...11111 0010.01....0..11.10.1111111 0010..101..100.1..00.111111
0010.110...00..01101.011111 0010..101.0000.01.01.011111 0010.11....00..0110..011111
0010..101..000.1..00.111111 0010.11....00..01.0..011111 0010..1....10..1..011111111
0010..1....1...1..011111111 0010.01....10..1110.1111111 001000100.00.00...00..00...
0010..101..0...1..00.111111 0010..101..0.0.1..00.111111 0010..1...11.111..0..111111
0010111........1..0..111111 0010.110..0000.01.01.011111 0010..1.0.....01..0.0111111
0010.010...11.101.01..11111 00101010..1011101.01.011111 0010.01........1.00.0111111
0010.010...01.101.01..11111 0010.0111.1.1..001010.11111 001011111.11111111001001111
001000100.000000010000.0000 00100.110..000011.000111111 001011110..00.01.1001111111
0010..1....10.01.00.1111111 001001111..0101.10001011111 001010101.010.0100011111111
00100.1...000.0111000111111 00100.11...0000111000111111 001000101..1.00100011111111
001001111.01000100011111111 0010.0111..10..1010.1111111 001000110..0...11.000111111
001000101.0...010.00.111111 00100.110..0..011.00.111111 001000100.0000....00.000010
0010.1111....1111100.111111 0010.1111.01011111001011111 0010..1.0..00.00.10.1111111
001011111.111110010...111.1 0010011.0.010010.10.1111111 0010.010...0..00000.1111111
0010111.0.01..00110.1111111 0010.01.0..1...0110.1111111 0010.01.0..10..0.10.1111111
001011111..0.01011011111111 001011101..0.111.0000111111 0010001.0.1011100.000111111
001001111.00001011011111111 001001101..10..110000111111 001001100.0.......0...0..1.
00101010..00011011011111111 00100.11..0.01.00.010111111 0010.01....010010.0.0111111
0010.01....01.01..0.0111111 001011111....11000010011111 001011111..0..0010001011111
0010.1111....0.01100.111111 001000100.1010.00100.10..10 001011111.111111100.0.0000.
001000110...01.11.00.111111 001010111....1.000010.11111 0010..10..10.00000000.11111
001000100.10...0..0..1.1.1. 00100010..01111111001111111 001000111.0111.011001111111
001001101..0010.10001111111 00100.1.0..1.1.1.1011111111 001011111.111110000.0.01111
001011111..0.10001011111111 0010..101..1.0011.00.111111 001000110...11.11.00.111111
0010..1...111..1..011111111 0010..10..0.00.01.01.011111 0010.0111.1..11000010.11111
0010.01.0.1..1.001010.11111 0010..1.0.1..10001000.11111 0010..1.0.1..1.001000.11111
001000101.1....1.10..111111 001011111..0.010110.1.11111 0010.01...1..1.000000.11111
001000111...1..0000...11111 001001101.1..10111000.11111 001000111..1.110000.1.11111
001001101...00011100.111111 001000100.10......0..010010 001000100.0....0..01.111.1.
001000100.0....0..01.010.10 001000100.0....0.00...1..00 0010.1111....1.0000...11111
001001101.1..101.10...11111 0010..1...10.00000000.11111 0010..1...10...000000.11111
00100.1...101.0000000.11111 001001101.10010110000.11111 001000100.101000.10..001.10
001000100.0.0.....0...1..0. 001011110.01011111001011111 0010.1111..0..0000011111111
0010.0100.1.1.1.10011111111 0010011....1.10101010.11111 0010.110..011101..010.11111
0010.0100.01.1.1.0010.11111 00100.101.111.....010111111 00100.111.0001000.001111111
0010001.1.11101.1000.111111 0010011.1...0.1..100.111111 0010..1...01011111001011111
0010.0111..11111.0001111111 00101.1.0.010..0.10.0011111 0010..1.0...0.01..0.0111111
0010..1...010.00.00.0111111 001011110..1.00101011111111 001000111.01100000011111111
0010.010....1.1010010.11111 0010..1...011.00.00.0111111 001011111.111110000.0.01.11
001011111.11111.000.0.01.11 0010..1.0.00.1.0.10.10.1111 0010..1.0.000..0.1001011111
00100.100...1...11010.11111 00100.100.......11010.11111 001011111.111111100.0.01011
001000111.01.00000011111111 001011111....110000...11111 0010..100.10.0..0.000..1111
0010.1101.10..01100.1111111 0010.0100.1000...0000.11111 0010.0100.10.0...0000.11111
001001100.1.......0...1.10. 0010.1111......0000000.1111 001001100.0.......01..0..0.
0010001.0.10.01...000111111 001001100.0.0.....0.1.011.0 001001101...010.10001111111
0010..1...010..1..011111111 0010001.1.111111.0011111111 00101111..101..0.1011111111
001011111.1.1.....011111111 0010..1...00011011011111111 0010..1...000.1011011111111
0010.0111..0001000000111111 00101.10...010.01.000111111 001000111..0001000000111111
0010.01.1.001.10.0000111111 001000100.1.01001000.111111 0010.0100..00.1000000111111
001001100.1..0.001010011111 0010.0100..00.0.00001111111 0010.0100..0110.00001111111
001000100..0.10.100.1111111 0010.0100.110....00.0111111 001011110.000101.0000011111
001000100.10010.100.1111111 001000100.1.010.100.0111111 0010..100.1..00.0.000.11111
00100.111.01.000110.1111111 001000100.0000101.0101..0.. 0010001.0.10.1.001000111111
00100.10..10..0000000111111 00100.111.010..00.00.111111 0010..111.0100100.00.111111
00100.111..1..100100.111111 0010..1...111.00.00.1111111 001001100..100100.0.1111111
001000111..0..0000000111111 001001111..00010.10.1111111 0010.01...10...0100.1111111
0010..1...110.00.00.1111111 0010111....1.1.0110.1111111 00100.1.0..0..0001000111111
0010..10..11..00000.1111111 0010..1....10.00.00.1111111 00100.1...01...00.0..111111
0010111.1...1.....00.111111 00100011...0111..000.111111 001000100.0010001.011001.00
0010..1.0..10.001.0.1111111 0010.11.0..111.0.00.1111111 00100.111..000.00.00.111111
0010..111..000100.00.111111 0010.110..000..00.01.011111 00100.111..100100.00.111111
00100.111.00001001001111111 0010.11....1.0.1000...11111 00101.10...10000.00.1011111
001000100..1..10000.0..1111 001000111.00.110000.0011111 001011111.000..0.1001011111
00100010...101..100.1111111 0010.01....01001..0...11111 001000111.101.000.000001111
0010.01.....0.10.00.0111111 0010..100...1.0001010.11111 0010..1....11.00.00.0111111
0010.010....1..000010.11111 0010..1.0...1000.10.0.11111 001001101...001100010011111
001001100.1..11.110...11111 0010.0111...1.10000...11111 001010100...100000000001111
0010.0100.1100..00000.11111 0010.0111..0111000000..1111 1110..1...........000......
1110..1...........0..1..... 1110..1...........0..0..... 11100110..........0........
111000100.0.......00.0110.. 111000111.10000...0...11111 1110..111...100...0..011111
1110001.0.10101.10000011111 11101.1.0.011.....000011111 11101.1.0.011....0000011111
1110.11.0.0011....000011111 1110..1...........011...1.. 1110001...........0........
11100011..........00....... 111011111.111111110110...11 11100111..00001.110.1111111
11101011....100.110.1.11111 1110.01...0.000..1001011111 111001111......111001111111
111001111..0...110001111111 1110.1111..0..01000.1111111 1110001.0...00000.0.....11.
11101.111..1.011110.1111111 1110..111.11.111110..111111 111011111.11111.1101.0..111
111011111.111111110..1..... 1110..111.0.0.1111001011111 111011111.111111110001...0.
11100011..0.100111001011111 111000100...0.11110.1111111 111000111.........00.......
111011111.11111.110..0..111 11101.111..1.01.110.1111111 1110001.0.0100.0..0.0..0..0
11100110..00101.0001.011111 1110..1...........0..0.0... 1110..1...........0..0.1..1
111000110.0.......00...1..1 11100.10....0....10.1.11111 11100010..1...0...001.11111
1110001.0....0...00.1.11111 11100110..111.1.01001.11111 111000100.010...1.01..1101.
111000100.010...1.01..11... 111010100....101.1001111111 1110.01.0...01...00...11111
1110001.0..1....00001.11111 11100.1.0.1.0.1.00001.11111 1110001...........00.......
0010..0..0........0.1...0.. 0010010..0........0........ 0010100..0........0........
001001001001111111001111111 0010..0..0.....1..0..1..... 001001001010010010011111111
001011011011111010000001100 001011011011111010000.01100 00101.0000.10.0011011111111
0010..0..0........0.0...1.. 0010..0..0.....1..0..1..1.. 0010..0..0........0.0...1.1
00100101100.0.00.101.0.01.. 0010110000.1000011011111111 0010100100....0...0101011.1
00100001.00011....01....... 0010.10000.1000011011111111 001011000001000011011111111
00101.01.011011011001111111 00100.00.00.......00....... 001010000010...10.0.01..101
00101100.0........0........ 0010.10.1010000000001111111 0010..0..0.....1..0..1..0..
0010..0..011011011001111111 00100.00000100000.001111111 0010110110.100.00.0.1111111
0010.001000000.1100.0011111 00100.00.0.0000000001111111 00101100100111110.011011111
0010..0..0100..0..000111111 00100001.0........0........ 00100000000000.11.00011.00.
001010010000000110000011111 0010.00..0010.00..001111111 0010..0..0010..0..001111111
001011001001111101011011111 00101.010001111111001111111 00101.000001111111001111111
1010.010.0...0...0011111111 1010.010.0...1...1011111111 1010.111.0...0...0011111111
10100010.0.......1011111111 1010..1..0........01.1..0.. 1010101..0........0........
10100010.0........011111111 1010.111.0...1...1011111111 1010..1.100.0.1.0.011111111
10100.1.00.0.00...00.0000.. 1010011..0........0........ 1010..1..0........00.0..000
10100.1..0....0..1011111111 1010..1..0........00.0..011 10101.10.00...0..1011111111
1010001010........0........ 10100.1..0........0........ 10100.1.00000.....0....0001
10100.1..0....1.11011111111 10100.1.00000.....0....1001 1010.11110...1....011111111
1010001..0000.1..10..111111 10101110.01..111..01..11111 1010..1.100.000.0.011111111
10100011.001..0..0010111111 10100010.0.......0011111111 1010..1.000.000.0.011111111
10100111.00.0....0011111111 10100111.00.0....1011111111 10100010.00.0....0011111111
10101.1..0........0........ 101010100011100100001011111 10100010.00.0....1011111111
1010..1..0........01.1.0.0. 1010..1..0........01.1.1.11 1010..1..0........01.101.1.
10101.1.00000.....0...00001 101001110000000...00111101. 1010.01.00000...1.001111111
1010.010.00.01...1011111111 1010.010.00.01...0011111111 1010.01.000001....001111111
10101110.010.11...010.11111 1010001000....1.1.0.1.11111 101000100010......00..1.1..
101000100000......01..0.0.. 1010101000.101.1.0010.11111 10101010.0...1...00.1.11111
10100.1.00........0.1.11111 1010.01000...0....0.1.11111 10101010.0...1...10.1.11111
1010.01000...1....0.1.11111 1010.010.010.0..01001.11111 1010101000.0.0000.001011111
1010101..0110.00..0..011111 1010.010.010100001001011111 10100.10.010.01.01001111111
1010..1..0........00.0.0.01 101000100010......01..01.1. 1010.010.00.0....1001011111
1010.010.00.0.0..1001011111 1010..1.100.0.0.0.001011111 10100.11.0.00.0.110..011111
1010.010.00.00..01001.11111 1010.110.0.0100..000..11111 10100.10.0.00...0.00..11111
10100.10.0.0010.0.0...11111 10101010.011.01.0.0...11111 10101.1..0....1.11011111111
1010111..0..0...11011111111 10101.11.010..1..1001111111 1010001.10000.1.010..111111
10101111.00.00....0..111111 10101111.00000....0..111111 10100011.010..1..1001.11111
10101.11.001..0..0010111111 1010..1..01.0.001.01.011111 1010001.1000.00.0.0...11111
10101010.010100001001011111 1010101000111...000.0.11111 10100.10.0.10.....0..011111
10100.1..01.1.0...0..011111 1010..10.01.10..0.0..011111 1010.01.001100..00010.11111
1010.010.0....0.00001011111 10101010001.100.0.001011111 10101.1..01010.0.0001011111
1010.01..01.1..00.010011111 10100010.0....0.000.1.11111 1010001.000011....001011111
1010.110.0.0100.0000..11111 1010001..00...0.00001.11111 1010..1..0........00.0.1.1.
1010..1.100.0....1001011111 1010.01..00.000.01001011111 1010.01..00.0....0001011111
1010.01..0101.101.010011111 101000100000......011.0.0.. 1010011..0.0..1.0000..11111
10100110000001..100.0111111 1010011..00001....0.0111111 10100.10.0.10.1...0.0111111
1010.010.01101..0000.111111 1010.11.0010.1..1.010111111 1010101000.10.1.0.00.111111
101001110011000010010011111 0010..1..00.......00....... 0010011110........0........
0010.010.0...0...0011111111 0010001000.10.10..010111111 0010..1..0.....1..0.....1..
0010.010.0........0........ 0010.11.00..1.00.10.0111111 001000100011...0..010111111
00100.1.00.0..000.011111111 0010..1110.100100.00.111111 0010..1..010100000011111111
001000100011...0.0010111111 00100010.0101.00000..111111 00100010001.0..0.00..111111
00100010001....0000..111111 0010.01.000....00000.111111 00100.100010.0.0000..111111
0010001000....00000..111111 0010..1.000.000.0.011111111 0010.010.00.....00001111111
00100010.00.0....0011111111 0010.010.001..1.1100.111111 00100010.011..1...01.111111
0010.010.00.01...1011111111 00100010.01......0011111111 00100010.01.1....1011111111
0010..1..0........0.1...1.. 0010111110111111110101..0.. 0010011..00.......00.......
0010.010001011.0..011111111 0010.11.100.00.00.011111111 0010011010..01..1.001111111
0010..1..0........0.01..0.. 0010111010001...1.001111111 0010001010010.1.100..111111
0010.110101000..0.0.0111111 00101.1.00..000...001111111 00100011.00.11.000001111111
00100011100111100000.111111 0010..1000.10.00..0.1111111 00100011.00111.0000.1111111
0010.01000011000.0010111111 0010111..0101..011011111111 0010.010.01010.0.1011111111
0010..1000101000..011111111 0010.010.01011.0.1011111111 0010.111.01010.0.0011111111
0010.111.01011.0.0011111111 0010001.10.10....10..111111 0010.011.0000...1.0..111111
00100111.0........0........ 0010.11.100001..1.011111111 0010.111100.01.0..01.111111
00101.1.100.0.1.1.011111111 0010101.0001..0.10010111111 0010..1..0.....0..0..1..1..
0010..11100.1110..011111111 0010..11100.0.10..0.1111111 0010.111.0..00...10.1111111
0010.11.100000....001111111 0010.11110.001.0..0..111111 0010.111100.0..0..0..111111
0010.010001.......0..111111 0010.010.011..1.110..111111 0010001.101...1.1.0..111111
0010001.100...1.1.0..111111 0010011.101.....1.0..111111 0010.11.10..01..1.0..111111
0010.010001..1...00..111111 0010.010000..1...00..111111 0010101000.......00..111111
0010..1..00.0.....011111111 0010111.10011...1.0..111111 00100.11101...00..0..111111
00100.11101...10..0..111111 0010..11100..010..00.111111 0010011.101.0.0.000..111111
001010100010000.0.0..111111 001010100001000..000.111111 00101.1..0101..0.1011111111
0010..1..01011101.011111111 0010..1..0.....0..0.....0.. 001001111000...00.001111111
0010..1..0.1..00000.0111111 0010..1.00011.001.0.0111111 0010.110000.0010..0..111111
00100.1..0.1.000000.0111111 00101.1.000.0..011010111111 0010001.00111.00.10.0111111
0010001.00.11.00.10.0111111 00101010.0........0........ 00100.10.01...00000..111111
0010.010.011.0.0000.0111111 0010.010.01..000000..111111 0010..1..0101..0..011111111
00101.1000011....001.001111 0010101.00101...0001.001111 0010101000011.0..001.001111
0010.110.0.0...00.0..111111 00100111.01010011.000000... 0010..1..0000.10.10.1111111
0010.111100000.001001111111 00100010.0.01.00010...01.11 00100010.0.01.000100..01.11
0010101000000.0.00001111111 0010001000000.1...01010..1. 001000100010111000000111111
0010.111100.001001001111111 00101.10.00.001001001111111 00100111.00.001001001111111
0010.11.10011.10.1001111111 00100111100.001001001111111 0010001.1001000.11001111111
00100.1..0.0100011001111111 0010011110.1001001001111111 0010111110111110110101..1..
101...0............0.....1. 101...0............0....0.. 101...0.................0..
101...0.................... 1110..0.000.1....00.0.01111 1110..0000001001..0..011111
1110..0..0........0........ 1110..0..0.00..0..011111111 1110..0100110100..00.111111
11100001100.10110100.111111 1110.000.0........0........ 1110..0..0........011......
11100000000.......001111111 1110.000.001.101000.1011111 1110100100..10110.001001111
1110.000.011..01000.1011111 11101000.0011.110000.011111 1110100.000.11011.001001111
1110.00.000.1100..001101111 1110010..01010110001.0.1111 1110..0..0........011...100
1110..0..0110..0..000111111 1110000000000001..0..111000 1110000000000001..000.11000
1110.000.0011..0.00.1.01111 1110.000.00111.0.00.1.01111 1110.000.0011100.00.1101111
11100.0.000.1..1000.0001111 11101001.0........0........ 1110100..0101010110..011111
1110.00.000.1....00.0001111 1110..0.00011..0.0001100111 1110100100.000.00.0..111111
1110110..0..1...00011011111 1110.000.0...10..0011011111 1110.00..00..000000.1011111
1110100..0011.0.000.1011111 1110.00100101..0..001.11111 1110.001.00..000110.1011111
1110110..0111..0110..011111 1110100..00.1.01000.1011111 1110100..0011.01000.1011111
1110.000.001.101000.10.1111 1110..0..0........011....00 1110100100.01..10.001001111
1110..0.00011.01..0.1001111 1110..0.00011..1..0.1001111 1110.00..001..0.000.10.1111
11100.0.00.00...000.0..1111 1110..00.0.010..000..0..111 11100.0.00.0111..000..0.111
1110.00..0..1110..00.100111 11100.00.0.0.111..0.01...11 11100.00.0.0..111.0.011...1
"""

def assignment_of(config, variables):
    return {variables[site][int(code)] for site, code in enumerate(config)}


def cnf_satisfied(cnf, variables, config) -> bool:
    positive = assignment_of(config, variables)
    for clause in cnf.clauses:
        if not any((lit > 0 and lit in positive) or
                   (lit < 0 and -lit not in positive) for lit in clause):
            return False
    return True


def declared_invariance_configs() -> np.ndarray:
    codes = list(range(INVARIANCE_BLOCK))
    codes += [(1 + j) * INVARIANCE_STEP for j in range(INVARIANCE_TERMS)]
    out = np.zeros((len(codes), 27), dtype=np.uint8)
    for row, value in enumerate(codes):
        rest = value
        for site in range(27):
            out[row, site] = rest % 3
            rest //= 3
    return out


def rotation_site_permutations(tor: Torus):
    out = []
    for _image, matrix in ROTATIONS:
        perm = np.zeros(tor.N, dtype=np.int64)
        for site in range(tor.N):
            x, y, z = tor.coord[site]
            moved = tuple(sum(matrix[r][c] * (x, y, z)[c] for c in range(3))
                          for r in range(3))
            perm[site] = tor.sid(*moved)
        out.append(perm)
    return out


def parse_block(text: str):
    return tuple(text.split())


# Additional September-8 controls; all original literal witness blocks remain exact.
# These four bounded-search witnesses are not optimized minimum-cardinality claims.
LOWER_OCCUPANCY_WITNESSES = (
    (14, 0, 25, '10.00.......0......00.11.0..0.....1..101..1.1..1001..1....10...0'),
    (20, 2, 20, '10000.0.01110.0.0.0.............0111............0.0.............'),
    (21, 1, 30, '00110..1.1..0..10..1....10.1.01......11..000..110..1....11.0.00.'),
    (21, 2, 48, '100100.0110000.00001.1.11110.1.1011001.1001101.10011....1100....'),
)

DISCONNECTED_SEED_WITNESSES = (
    (6, 2, '1000..0......0.............'),
    (20, 2, '1000..0..0...0....0........'),
    (21, 2, '10100.01001...001.01111.100'),
)


def current_input_identity():
    return (set(EXPECTED_INPUT_SHA256) == set(AUDIT_INPUT_PATHS)
            and all((ROOT / p).is_file()
                    and sha256((ROOT / p).read_bytes()).hexdigest() == digest
                    for p, digest in EXPECTED_INPUT_SHA256.items()))


def required_solver_probe():
    """Calibrate actual positive and contradictory CNFs through every engine."""
    rows = []
    try:
        for engine in ("cadical195", "glucose42", "minisat22"):
            positive = CNF(); positive.n = 1; positive.clauses = [[1]]
            negative = CNF(); negative.n = 1; negative.clauses = [[1], [-1]]
            yes, model, _ = sat_solve(positive, engine)
            no, _, _ = sat_solve(negative, engine)
            rows.append((engine, yes is True and 1 in (model or []) and no is False))
    except Exception as exc:
        return False, {"completed": rows, "error": f"{type(exc).__name__}: {exc}"}
    return len(rows) == 3 and all(ok for _, ok in rows), rows


def static_membership(mask, digits):
    """Membership of a supplied mask, without claiming physical access."""
    if len(digits) != NPAIR or any(d not in (0, 1, 2) for d in digits):
        raise ValueError("outside the declared ternary support-table family")
    block = sum(1 << (2 * j + d) for j, d in enumerate(digits) if d != 2)
    return (mask & block) == 0


def disconnected_seed_controls(tor):
    rows = []
    for pair, target, text in DISCONNECTED_SEED_WITNESSES:
        config = parse_config(text)
        allowed = {2 * pair, 2 * pair + 1}
        seed = seed_for(tor, pair, 2 * pair)
        cnf, variables = build_cnf(tor, allowed, seed=seed)
        mask = tor.mask_scalar(config)
        connected, stack = {0}, [0]
        while stack:
            site = stack.pop()
            for neighbor in tor.NBR[site]:
                neighbor = int(neighbor)
                if config[neighbor] != 0 and neighbor not in connected:
                    connected.add(neighbor); stack.append(neighbor)
        remote = [i for i in range(tor.N) if config[i] != 0 and i not in connected]
        positive = CNF(); positive.n = cnf.n
        positive.clauses = cnf.clauses + [[variables[i][int(config[i])]] for i in range(tor.N)]
        sat, model, _ = sat_solve(positive, "minisat22")
        ok = (target == 2 and bool(remote) and all(int(config[i]) == v for i, v in seed.items())
              and mask == int(tor.masks_vectorised(config[None, :])[0])
              and bits_of(mask) <= allowed and cnf_satisfied(cnf, variables, config)
              and sat is True and np.array_equal(decode(model, variables, tor.N), config))
        rows.append((pair, mask, remote, ok))
    return len(rows) == 3 and all(row[-1] for row in rows), rows


def lower_occupancy_controls():
    tor = Torus(4); rows = []
    for pair, target, count, text in LOWER_OCCUPANCY_WITNESSES:
        config = parse_config(text)
        want = ({2 * pair} if target == 0 else
                {2 * pair + 1} if target == 1 else {2 * pair, 2 * pair + 1})
        mask = tor.mask_scalar(config)
        ok = (len(config) == tor.N and int((config != 0).sum()) == count
              and mask == int(tor.masks_vectorised(config[None, :])[0])
              and bits_of(mask) == want)
        rows.append((pair, target, count, mask, ok))
    return (len(rows) == 4 and [row[2] for row in rows] == [25, 20, 30, 48]
            and all(row[-1] for row in rows)), rows


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    probe = PROBE_PATH.read_text(encoding="utf-8")
    q8 = Q8_PATH.read_text(encoding="utf-8")
    history = TIME_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    have_sat, solver_preflight = required_solver_probe()

    print("external_scientific_inputs: finite support scaffold and declared witnesses; physical access remains unsupplied")
    print("integrity_reads: axioms, deep probe, law pair, history-index note")
    print("construction: finite static target decisions require complete solvers; declared witnesses and pool checked")
    print("negative_scope: required finite target/centered-box solver decisions; no global geometry or pool-negative inference")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: minimal_axioms Admissibility and Record clauses")
    print("declared_math: cubic rotations, ternary support tables, 48-bit demand masks")
    print("solver_mode: required CaDiCaL, Glucose and MiniSat; emitted DRUP lengths are not proof checking")
    checks.check("required-solver-engines", "all required actual engines pass positive/negative calibration", have_sat, solver_preflight)
    if not have_sat:
        return checks.finish()

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and are unique",
        all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS)
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )
    checks.check("audit-timeout", "the declared timeout is 300 seconds",
                 AUDIT_TIMEOUT_SEC == 300)
    inputs_ok = current_input_identity()
    checks.check("current-input-identities", "all declared current input bytes match", inputs_ok)
    if not inputs_ok:
        return checks.finish()

    # ---------- supplied surface -------------------------------------------
    checks.check(
        "axiom-record-readable",
        "the Record clauses on readability and absence are quoted",
        "Only records are readable." in axiom
        and "A readout value is determined by record content" in axiom
        and "A site with no record cannot be read." in axiom
        and "Only records are readable" in note
        and "A site with no record cannot be read" in note,
    )
    checks.check(
        "axiom-record-state",
        "the Record clauses on formation and states are quoted",
        "Records form." in axiom and "A state is a configuration of records." in axiom
        and "Records form" in note and "A state is a configuration of records" in note,
    )
    checks.check(
        "axiom-admissibility",
        "the live Admissibility sentence is quoted in the note",
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
        in axiom_flat
        and "determined by, and varies with, the nearest-neighbor conditions"
        in note_flat,
    )
    checks.check(
        "axiom-support",
        "reading note (3) equating availability with support is quoted",
        "denotes its support -- on finite menus, exactly the possibilities of "
        "nonzero probability" in axiom_flat and "denotes its support" in note_flat,
    )
    checks.check(
        "axiom-partial-licence",
        "absence and supplied order do not establish a static membership oracle",
        "every site carries a record" not in axiom_flat
        and "order of formation" not in axiom
        and "A site need not carry a record" in note_flat
        and "this supplies no static membership oracle" in note_flat,
    )
    checks.check(
        "parent-deep-probe",
        "the deep probe's 3^24 census is live and cited",
        "number of covariant label-equivariant tables = 3^24" in probe
        and "282,429,536,481" in note_flat,
    )
    checks.check(
        "parent-law-pair",
        "the 2026-08-13 law pair is live",
        "claim_type: bounded_theorem" in q8
        and "It selects neither rule as the framework's physical law."
        in normalize(q8),
    )
    checks.check(
        "parent-history-index",
        "the history-index note is live and named",
        "Record-Monotone" in history
        and "TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_"
            "BOUNDED_NOTE_2026-07-03.md" in note,
    )

    # ---------- T1: the encoding -------------------------------------------
    tor3 = Torus(3)
    checks.check(
        "T1-census",
        "729 profiles, 57 orbits, 9 flip-fixed, 24 flip-pairs",
        len(TERNARY) == 729 and len(TREPS) == 57 and len(TSELF) == 9
        and NPAIR == 24 and len(TSELF) + 2 * NPAIR == 57,
        (len(TREPS), len(TSELF), NPAIR),
    )
    checks.check(
        "T1-tables",
        "the table space is 3^24 = 282429536481, the demand word 48 bits",
        3 ** 24 == 282429536481 and NBITS == 48 and len(PINNED_CODES) == sum(
            1 for c in range(729) if int(ORBIT_OF[c]) not in SIDE_OF_ORBIT),
    )
    star_bits = (0, 2, 22, 46, 47)
    inv_configs = declared_invariance_configs()
    vec_masks = tor3.masks_vectorised(inv_configs)
    checks.check(
        "T1-two-paths",
        "vectorised and scalar mask paths agree on 8192 configurations",
        all(int(vec_masks[i]) == tor3.mask_scalar(inv_configs[i])
            for i in range(inv_configs.shape[0])),
    )
    checks.check(
        "T1-local",
        "mask(c) inside S is exactly a 7-site-star condition",
        all((bits_of(int(vec_masks[i])) <= set(star_bits))
            == tor3.star_legal(inv_configs[i], star_bits)
            for i in range(0, inv_configs.shape[0], 7)),
    )
    cnf_probe, vars_probe = build_cnf(tor3, set(star_bits))
    checks.check(
        "T1-cnf",
        "the CNF holds on a configuration exactly when its mask is inside S",
        all(cnf_satisfied(cnf_probe, vars_probe, inv_configs[i])
            == (bits_of(int(vec_masks[i])) <= set(star_bits))
            for i in range(0, inv_configs.shape[0], 61)),
    )
    perms = rotation_site_permutations(tor3)
    sample = inv_configs[:512]
    base = tor3.masks_vectorised(sample)
    inv_ok = True
    for shift in range(27):
        rolled = np.zeros_like(sample)
        for site in range(27):
            x, y, z = tor3.coord[site]
            dx, dy, dz = tor3.coord[shift]
            rolled[:, tor3.sid(x + dx, y + dy, z + dz)] = sample[:, site]
        inv_ok &= bool((tor3.masks_vectorised(rolled) == base).all())
    for perm in perms:
        inv_ok &= bool((tor3.masks_vectorised(sample[:, perm]) == base).all())
    flipped = np.where(sample == 0, 0, 3 - sample).astype(np.uint8)
    inv_ok &= bool((tor3.masks_vectorised(flipped) == base).all())
    checks.check(
        "T1-invariance",
        "the mask is fixed by 27 translations, 24 rotations and the flip",
        inv_ok,
    )
    wlog_ok = True
    for pair, (rep_a, rep_b) in enumerate(TPAIRS):
        codes_a = [c for c in range(729)
                   if int(ORBIT_OF[c]) == REP_INDEX[rep_a]]
        codes_b = [c for c in range(729)
                   if int(ORBIT_OF[c]) == REP_INDEX[rep_b]]
        for code in codes_a:
            wlog_ok &= any(rotate_profile(TERNARY[code], r) == rep_a
                           for r, _ in ROTATIONS)
        for code in codes_b:
            wlog_ok &= any(flip_profile(rotate_profile(TERNARY[code], r)) == rep_a
                           for r, _ in ROTATIONS)
    checks.check(
        "T1-wlog",
        "on the full torus every realiser maps onto the pinned origin star; boxes retain an extra pin restriction",
        wlog_ok,
    )

    # ---------- T2: the digit-confined decision on the 3^3 torus -----------
    l3_witnesses = parse_block(L3_WITNESS_BLOCK)
    keys = [(pair, t) for pair in range(NPAIR) for t in range(3)]
    bits_of_target = {0: lambda i: (2 * i,), 1: lambda i: (2 * i + 1,),
                      2: lambda i: (2 * i, 2 * i + 1)}
    declared_sat, declared_ok = [], True
    for slot, (pair, target) in enumerate(keys):
        text = l3_witnesses[slot]
        if text == "-":
            continue
        want = set(bits_of_target[target](pair))
        config = parse_config(text)
        declared_ok &= (tor3.mask_scalar(config) == sum(1 << b for b in want))
        declared_ok &= (int(tor3.masks_vectorised(config[None, :])[0])
                        == sum(1 << b for b in want))
        declared_sat.append((pair, target))
    checks.check(
        "T2-witnesses",
        "50 declared 3^3 witnesses carry exactly their target mask",
        declared_ok and len(declared_sat) == 50,
        (len(declared_sat), declared_ok),
    )
    unsat_slots = [k for slot, k in enumerate(keys) if l3_witnesses[slot] == "-"]
    enum_solutions, enum_hits = 0, 0
    for pair, target in unsat_slots:
        bits = bits_of_target[target](pair)
        masks, count = enumerate_legal(tor3, set(bits), seed_for(tor3, pair, bits[0]))
        enum_solutions += count
        enum_hits += sum(1 for m in masks if bits_of(m) == set(bits))
    checks.check(
        "T2-enumeration",
        "historical seed-component-only enumeration has 55 leaves and zero target hits; no whole-space proof",
        len(unsat_slots) == 22 and enum_hits == 0 and enum_solutions == 55,
        (len(unsat_slots), enum_hits, enum_solutions),
    )
    missing = Counter(pair for pair, _t in unsat_slots)
    blind = sorted(p for p in range(NPAIR) if missing[p] == 3)
    half = sorted(p for p in range(NPAIR) if missing[p] == 2)
    checks.check(
        "T2-blind",
        "pairs 11, 16 and 17 admit no digit-confined mask on 3^3",
        blind == [11, 16, 17],
        blind,
    )
    checks.check(
        "T2-half",
        "pairs 14, 18, 21 and 23 are read to a binary choice on 3^3",
        half == [14, 18, 21, 23],
        half,
    )
    pair23 = parse_config(PAIR23_WITNESS)
    checks.check(
        "T2-pair-23",
        "pair 23 is realised by a complete 27-record configuration",
        bits_of(tor3.mask_scalar(pair23)) == {46, 47}
        and int((pair23 != 0).sum()) == 27,
        (sorted(bits_of(tor3.mask_scalar(pair23))), int((pair23 != 0).sum())),
    )
    exact = NPAIR - len(blind) - len(half)
    fibre = 3 ** len(blind) * 2 ** len(half)
    checks.check(
        "T2-table",
        "17 digits exact, 4 to a binary choice, 3 blind; fibre 432 = 3^3 x 2^4",
        exact == 17 and fibre == 432 == 3 ** 3 * 2 ** 4
        and 3 ** exact * 2 ** len(half) == 2066242608,
        (exact, fibre),
    )
    solver_rows = {}
    if have_sat:
        drup = []
        confirmed = 0
        for pair, target in keys:
            bits = bits_of_target[target](pair)
            cnf, variables = build_cnf(tor3, set(bits),
                                       seed=seed_for(tor3, pair, bits[0]),
                                       require=bits[1:])
            sat, model, _ = sat_solve(cnf, "cadical195")
            solver_rows[(pair, target)] = bool(sat)
            if sat:
                config = decode(model, variables, tor3.N)
                assert bits_of(tor3.mask_scalar(config)) == set(bits)
            else:
                second, _m, proof = sat_solve(cnf, "glucose42", with_proof=True)
                third, _m2, _p2 = sat_solve(cnf, "minisat22")
                confirmed += int((not second) and (not third))
                drup.append(len(proof or []))
        checks.check(
            "T2-solver-verdicts",
            "CaDiCaL reproduces the 50 satisfiable and 22 unsatisfiable rows",
            sorted(k for k, v in solver_rows.items() if v) == sorted(declared_sat)
            and sorted(k for k, v in solver_rows.items() if not v)
            == sorted(unsat_slots),
        )
        checks.check(
            "T2-second-third-solver",
            "Glucose and MiniSat confirm all 22 unsatisfiable instances",
            confirmed == 22,
            confirmed,
        )
        checks.check(
            "T2-drup",
            "each negative instance emits a DRUP trace; its length is not independent proof checking",
            len(drup) == 22 and all(n > 1000 for n in drup),
            (min(drup), max(drup)) if drup else None,
        )

    disconnected_ok, disconnected_rows = disconnected_seed_controls(tor3)
    checks.check("T2-disconnected-controls", "three actual same-seed legal remote extensions pass complete fixed-configuration CNFs", disconnected_ok, disconnected_rows)

    # ---------- T3: the injectivity criterion ------------------------------
    pool_texts = parse_block(POOL_BLOCK)
    pool_masks, pool_seen = [], set()
    pool_ok = True
    batch = np.stack([parse_config(t) for t in pool_texts])
    assert batch.size <= CELL_CAP        # memory discipline, checked in place
    batch_masks = tor3.masks_vectorised(batch)
    for row, text in enumerate(pool_texts):
        scalar = tor3.mask_scalar(batch[row])
        pool_ok &= (scalar == int(batch_masks[row]))
        if scalar not in pool_seen:
            pool_seen.add(scalar)
            pool_masks.append(scalar)
    for slot, (pair, target) in enumerate(keys):
        if l3_witnesses[slot] == "-":
            continue
        mask = tor3.mask_scalar(parse_config(l3_witnesses[slot]))
        if mask not in pool_seen:
            pool_seen.add(mask)
            pool_masks.append(mask)
    checks.check(
        "T3-pool",
        "3117 declared masks re-verified from their witness configurations",
        pool_ok and len(pool_texts) == 3117,
        (len(pool_texts), pool_ok),
    )
    pool_array = np.array(pool_masks, dtype=np.int64)
    antitone_ok = True
    for j in range(ANTITONE_FAMILY):
        held = (j * (2 ** 24 // ANTITONE_FAMILY)) & ((1 << 24) - 1)
        wide = sum(1 << (2 * k + ((held >> k) & 1)) for k in range(NPAIR))
        narrow = sum(1 << (2 * k + ((held >> k) & 1))
                     for k in range(NPAIR) if k % 3 != 0)
        clear_wide = (pool_array & wide) == 0
        clear_narrow = (pool_array & narrow) == 0
        for bit in range(NBITS):
            if (wide >> bit) & 1:
                continue
            carries = (pool_array & (np.int64(1) << np.int64(bit))) != 0
            if bool((carries & clear_wide).any()):
                antitone_ok &= bool((carries & clear_narrow).any())
    checks.check(
        "T3-antitone",
        "visibility is antitone in the block set on the declared chains",
        antitone_ok,
    )
    verdicts = {}
    for pair in range(NPAIR):
        for kind in ("A0", "A1", "C0", "C1"):
            verdicts[(pair, kind)] = cube_covered(
                subcubes(pool_masks, pair, int(kind[1]), kind[0] == "C"))
    met = sum(1 for value in verdicts.values() if value)
    injective = all(verdicts[(p, "A0")] and verdicts[(p, "A1")]
                    and (verdicts[(p, "C0")] or verdicts[(p, "C1")])
                    for p in range(NPAIR))
    failing = sorted(k for k, v in verdicts.items() if not v)
    checks.check(
        "T3-requirements",
        "96 declared-pool requirements decided; 95 met and pool C0(22) fails, global C0(22) unresolved",
        met == 95 and failing == [(22, "C0")] and injective,
        (met, failing),
    )
    if have_sat:
        agree = True
        for (pair, kind), value in verdicts.items():
            clauses = criterion_clauses(pool_masks, pair, kind)
            if clauses is None:
                agree &= value
                continue
            holder = CNF()
            holder.n = 3 * NPAIR
            holder.clauses = clauses
            first, _m, _p = sat_solve(holder, "cadical195")
            second, _m2, _p2 = sat_solve(holder, "glucose42")
            agree &= (first == second) and ((not first) == value)
        checks.check(
            "T3-requirements-sat",
            "CaDiCaL and Glucose reproduce all 96 finite pool-coverage verdicts",
            agree,
        )
    checks.check(
        "T3-injective",
        "the static membership map separates all 3^24 = 282429536481 finite support tables; fibre 1",
        injective and 3 ** 24 == 282429536481,
    )
    outside_config = parse_config("1110..010001......0........")
    outside_mask = tor3.mask_scalar(outside_config)
    uncovered_block = 80649380013721
    checks.check(
        "T3-pool-boundary",
        "a realizable mask outside the pool serves its uncovered C0(22) block without proving global coverage",
        outside_mask == 17592320264448
        and outside_mask == int(tor3.masks_vectorised(outside_config[None, :])[0])
        and outside_mask not in pool_masks and not verdicts[(22, "C0")]
        and (outside_mask & uncovered_block) == 0
        and bits_of(outside_mask) & {44, 45} == {44},
        outside_mask,
    )
    joint_ok = True
    for pair, value, text in JOINT_WITNESSES:
        mask = bits_of(tor3.mask_scalar(parse_config(text)))
        joint_ok &= (2 * pair + value in mask)
        joint_ok &= all(b // 2 in (0, 1, pair) for b in mask)
        joint_ok &= int((parse_config(text) != 0).sum()) <= 6
    reads_11 = bits_of(tor3.mask_scalar(parse_config(JOINT_WITNESSES[0][2])))
    checks.check(
        "T3-joint",
        "six small joint masks are preserved as nuisance-gated examples",
        joint_ok and reads_11 == {0, 2, 22}
        and int((parse_config(JOINT_WITNESSES[0][2]) != 0).sum()) == 5,
        sorted(reads_11),
    )

    joint_mask = tor3.mask_scalar(parse_config(JOINT_WITNESSES[0][2]))
    responses = []
    for d0, d1, d11 in product((0, 1, 2), repeat=3):
        digits = [2] * NPAIR
        digits[0], digits[1], digits[11] = d0, d1, d11
        responses.append((d0, d1, d11, static_membership(joint_mask, digits)))
    checks.check(
        "T3-nuisance-gates",
        "all 27 actual joint-mask responses obey the conjunction; a known blocked nuisance hides every target choice",
        all(response == (d0 != 0 and d1 != 0 and d11 != 0)
            for d0, d1, d11, response in responses)
        and not any(response for d0, _d1, _d11, response in responses if d0 == 0),
        responses,
    )

    # ---------- T4: the 4^3 and 5^3 readout --------------------------------
    for size, block in ((4, L4_WITNESS_BLOCK), (5, L5_WITNESS_BLOCK)):
        tor = Torus(size)
        texts = parse_block(block)
        good, counts = 0, []
        for slot, (pair, target) in enumerate(keys):
            want = set(bits_of_target[target](pair))
            config = parse_config(texts[slot])
            scalar = tor.mask_scalar(config)
            vector = int(tor.masks_vectorised(config[None, :])[0])
            good += int(bits_of(scalar) == want and scalar == vector)
            counts.append(int((config != 0).sum()))
        checks.check(
            f"T4-torus-{size}",
            f"72 declared {size}^3 witnesses carry exactly their target mask",
            good == 72 and len(texts) == 72 and min(counts) == 2 and max(counts) == 64,
            (good, min(counts), max(counts)),
        )
        if size == 4:
            holdouts = all(bits_of(tor.mask_scalar(parse_config(
                texts[pair * 3 + target]))) == set(bits_of_target[target](pair))
                for pair, target in unsat_slots)
            checks.check(
                "T4-holdouts",
                "each 3^3 hold-out is read by an isolated mask at L = 4",
                holdouts and len(unsat_slots) == 22,
            )

    # ---------- T5: mirror identity and specified centered boxes ------------
    line_ok = True
    for size in (3, 4, 5):
        tor = Torus(size)
        for site in range(tor.N):
            for axis in range(0, 6, 2):
                plus = int(tor.NBR[site, axis])
                minus = int(tor.NBR[site, axis + 1])
                mutual = (int(tor.NBR[plus, axis]) == minus
                          and int(tor.NBR[minus, axis + 1]) == plus)
                line_ok &= (mutual == (size == 3))
    checks.check(
        "T5-mirror",
        "the three sites of an axis line are mutually adjacent at L = 3 only",
        line_ok,
    )
    mirror_ok = True
    for value in (0, 1):
        for openslot in range(3):
            line = [value + 1] * 3
            line[openslot] = 0
            seen = []
            for slot in range(3):
                if line[slot] == 0:
                    continue
                seen.append(sorted((line[(slot + 1) % 3], line[(slot + 2) % 3])))
            mirror_ok &= (len(seen) == 2 and seen[0] == seen[1] == [0, value + 1])
    checks.check(
        "T5-mirror-pairs",
        "one open site of a 3-cycle gives both partners the same mixed axis",
        mirror_ok,
    )
    box_texts = parse_block(BOX_WITNESS_BLOCK)
    box_declared, box_ok = {}, True
    for entry in box_texts:
        size_s, box_s, pair_s, target_s, text = entry.split(":")
        size, box, pair, target = int(size_s), int(box_s), int(pair_s), int(target_s)
        tor = Torus(size)
        config = parse_config(text)
        want = set(bits_of_target[target](pair))
        low = -(box // 2)
        inside = set(range(low, low + box))
        fits = all(
            all((c if c <= size // 2 else c - size) in inside
                for c in tor.coord[site])
            for site in range(tor.N) if config[site] != 0)
        box_ok &= fits and bits_of(tor.mask_scalar(config)) == want
        box_declared.setdefault((size, box), set()).add((pair, target))
    checks.check(
        "T5-box-witnesses",
        "19 declared witnesses sit inside a wrap-free block and hit their target",
        box_ok and len(box_texts) == 19
        and box_declared[(4, 3)] == {(4, 0)}
        and len(box_declared[(5, 4)]) == 18,
        {k: len(v) for k, v in sorted(box_declared.items())},
    )
    periodic = {(14, 0), (20, 2), (21, 1), (21, 2)}
    checks.check(
        "T5-split",
        "specified centered boxes: one positive, seventeen additional positives, four residual finite targets",
        set(unsat_slots) - box_declared[(5, 4)] == periodic
        and box_declared[(4, 3)] == {(4, 0)},
        sorted(set(unsat_slots) - box_declared[(5, 4)]),
    )
    periodic_k = sorted(
        int((parse_config(parse_block(L4_WITNESS_BLOCK)[p * 3 + t]) != 0).sum())
        for p, t in periodic)
    checks.check(
        "T5-periodic-density",
        "the four original torus witnesses have 52 to 64 records; these are not necessary bounds",
        periodic_k == [52, 64, 64, 64],
        periodic_k,
    )
    lower_ok, lower_rows = lower_occupancy_controls()
    checks.check("T5-lower-occupancy-controls", "the same four targets have verified 25/20/30/48-record witnesses, not claimed minima", lower_ok, lower_rows)
    if have_sat:
        box_ok_sat = True
        for size, box in ((4, 3), (5, 4)):
            tor = Torus(size)
            low = -(box // 2)
            inside = set(range(low, low + box))
            realised = set()
            for pair, target in unsat_slots:
                bits = bits_of_target[target](pair)
                seed = dict(seed_for(tor, pair, bits[0]))
                escapes = False
                for site in range(tor.N):
                    if all((c if c <= size // 2 else c - size) in inside
                           for c in tor.coord[site]):
                        continue
                    if seed.get(site, 0) != 0:
                        escapes = True
                        break
                    seed[site] = 0
                if escapes:
                    continue
                cnf, variables = build_cnf(tor, set(bits), seed=seed,
                                           require=bits[1:])
                sat, model, _ = sat_solve(cnf, "cadical195")
                if sat:
                    config = decode(model, variables, tor.N)
                    assert bits_of(tor.mask_scalar(config)) == set(bits)
                    realised.add((pair, target))
            box_ok_sat &= (realised == box_declared[(size, box)])
        checks.check(
            "T5-box-decision",
            "the complete solver reproduces both specified centered-box sets at the retained canonical pin",
            box_ok_sat,
        )

    # ---------- note hygiene -----------------------------------------------
    checks.check(
        "note-length", "the note stays under 330 lines",
        len(note.splitlines()) < 330, len(note.splitlines()),
    )
    checks.check(
        "note-registry-id", "the note declares its registry id",
        "partial_configuration_readout_injective_torus_3_every_law_visible" in note,
    )
    banned = ("measurement", "collapse", "observer", "exhaustive", "exhausted",
              "no-go", "closes the route", "only route", "invisible")
    hits = [word for word in banned if word in note.lower()]
    import re as _re
    hits += _re.findall(
        r"\b(?:swap|swaps|swapped|move|moves|moved|fill|fills|filled)\b",
        note.lower())
    checks.check(
        "note-vocabulary",
        "the note avoids process, closure and site-rewriting vocabulary",
        not hits, hits,
    )
    checks.check(
        "note-scope",
        "the note selects no law and states its bounded scope",
        "no physical law is selected" in note_flat
        and "promoted" not in note.lower() and "new axiom" not in note.lower()
        and "claim_scope:" in note,
    )
    checks.check(
        "note-correction",
        "the earlier static bound is preserved with its interpretation narrowed",
        "stands" in note_flat and "understates" in note_flat,
    )
    checks.check(
        "note-numbers",
        "the note carries the decided counts it claims",
        all(token in note for token in
            ("282,429,536,481", "3117", "432", "2,066,242,608", "96")),
    )

    print("per_element: 729 profiles, 48 demand bits, 3117 declared masks classified")
    print("per_site: each site of the 3^3, 4^3 and 5^3 tori evaluated in both paths")
    print("per_mode: checked and not executed - no spectral decomposition here")
    print("per_block: 24 flip-pairs, 96 requirements, 19 block-confined witnesses")
    print("lattice_wide: all 72 finite 3^3 targets require solvers; 4^3 and 5^3 witnesses and two specified centered-box comparisons")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
