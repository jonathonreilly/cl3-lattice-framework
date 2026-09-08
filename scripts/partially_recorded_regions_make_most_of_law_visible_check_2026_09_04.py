#!/usr/bin/env python3
"""Conditional static partial-configuration maps of finite support tables.

The runner recomputes, with no sampling, no seed and no random number
generator:

T1  static partial-configuration membership and its 48-bit mask reduction --
    the covariant label-equivariant census (729 ternary profiles, 57
    proper-cubic orbits, 9 flip-fixed, 24 flip-pairs, 3^24 tables), the
    equivalence of static admissibility with `mask(c) & block(T) == 0`, and
    the invariance of the mask under lattice translation, proper cubic
    rotation and the global value flip;
T2  complete sweeps -- all 729 ternary profiles realised at a recorded site of
    the 3^3 torus; all at-most-eight-record configurations with site 0
    fixed recorded at 0 (mask coverage by translation/flip, not unique orbits); the 3^12 distance-2 shell of
    each of the 48 demand bits; the 13 x 3^9 translation-symmetric family;
T3  the digit-visibility table from a DECLARED witness list of 44 partial
    configurations, each re-verified exactly by two independent code paths,
    and the resulting bounds on the number of classes and on the fibre;
T4  growth compatibility, complete over all 305,659 partial configurations
    with at most 4 records for six declared tables, in both directions, and
    the digit sensitivity of the bare reachable-stage readout.

No physical law is selected. The two repository rules are used as declared
reference points, imported from their own module, not re-implemented here.
"""

from __future__ import annotations

import importlib.util
import itertools
import sys
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 300

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PARTIALLY_RECORDED_REGIONS_MAKE_MOST_OF_THE_LAW_VISIBLE_"
    "WITHOUT_READING_THE_ORDER_OF_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-04.md"
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
RULES_REL = "scripts/extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py"

AUDIT_INPUT_PATHS = (
    "docs/PARTIALLY_RECORDED_REGIONS_MAKE_MOST_OF_THE_LAW_VISIBLE_"
    "WITHOUT_READING_THE_ORDER_OF_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md",
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_"
    "BOUNDED_NOTE_2026-07-03.md",
    "scripts/extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py",
)

assert AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL, PROBE_REL, Q8_REL, TIME_REL, RULES_REL)

EXPECTED_INPUT_SHA256 = {'docs/PARTIALLY_RECORDED_REGIONS_MAKE_MOST_OF_THE_LAW_VISIBLE_WITHOUT_READING_THE_ORDER_OF_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'ab0ad72b21000dca163b8130200faf84f151c57771085dadc1858106a1a1ab32', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md': 'c277ca66054a47ac0183e1a7d806acf0fee01167915d8b70746125d73a5a56f4', 'docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md': 'c08d7a351c2ae40d921b0e996ca817b4f789c51072fbf2b6eb9a2de6f6fe8967', 'docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md': '3dab4d91c2fd016f00bdab64beb0376c0e800c1026f5cfb862233e34927f6d9f', 'scripts/extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py': 'f90db72fd8c7c7c3de2f119f40a28b417e1e61679a3abf02da7e65368b6f12ec'}

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL
PROBE_PATH = ROOT / PROBE_REL
Q8_PATH = ROOT / Q8_REL
TIME_PATH = ROOT / TIME_REL
RULES_PATH = ROOT / RULES_REL

OPEN = -1
DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}

NSITE = 27
KSWEEP = 8          # complete record-count sweep depth
KGROWTH = 4         # complete growth-compatibility depth
CELL_CAP = 16_000_000   # no dense array above 4096 x 4096 entries

# Storage code for a site: 0 = unrecorded (open), 1 = record 0, 2 = record 1.

# --- the declared witness list ------------------------------------------
# 44 partial configurations of the 3^3 torus, written as 27 trits in site
# order (`.` unrecorded, `0`/`1` a record carrying that value). Each is
# declared here as a literal; the runner recomputes its demand mask by two
# independent code paths and checks it against the stated value. The list was
# assembled elsewhere; how it was assembled is not part of any claim, and a
# configuration absent from it is not thereby shown to be unrealisable.
DECLARED_WITNESSES = (
    (1, "01........................."),
    (2, "00........................."),
    (3, "01.0......................."),
    (4, "010........................"),
    (8, "000........................"),
    (12, "010.........000............"),
    (16, "01.10......................"),
    (32, "00.00......................"),
    (48, "01.00......................"),
    (64, "0111........0........0....."),
    (128, "000000....................."),
    (512, "001..1001.....0....1...0.1."),
    (768, "001..1001.1..10......1.01.."),
    (1024, "000111....................."),
    (2048, "0110........1........1....."),
    (4096, "0111..1...................."),
    (8192, "000000000.................."),
    (16384, "1010..0...0.1....1.1.100.1."),
    (32768, "001001001.................."),
    (49152, "001011010.................."),
    (65536, "01.10....10.01............."),
    (131072, "00.00....00.00............."),
    (196608, ".1000.0...0.0.1.000.0..010."),
    (262144, "00.11....11................"),
    (524288, "01.01....01................"),
    (786432, ".1100.0...0.1.1.000.0..011."),
    (1048576, "010100......001010001...100"),
    (2097152, "000000...000000............"),
    (16777216, "000111...111000............"),
    (33554432, "101100......110010001...011"),
    (67108864, "0111.....0..1.............."),
    (134217728, "111111...000000............"),
    (536870912, "000000000000000000........."),
    (1073741824, "01101010..101010011000.1110"),
    (2147483648, "111000000111000000000......"),
    (3221225472, "1001000...0.010010001..0001"),
    (137438953472, "01100.101.....1...01011.100"),
    (274877906944, "111111111000000000........."),
    (549755813888, "0111..1...000110110111..1.."),
    (1099511627776, "0111..1..1........1........"),
    (2199023255552, "000000000000000000000000000"),
    (4398046511104, "10101101.01010001.00.11...."),
    (35184372088832, "0110..0..0..1..1..0..1..1.."),
    (52776558133248, "0110110000..1..1..0..1..1.."),
)

# --- the declared table family -------------------------------------------
# Six tables named by their 24-digit codes (digit i is the menu on the side-A
# representative of flip-pair i: 0 = {0}, 1 = {1}, 2 = {0,1}; the partner is
# forced). Two are the repository rules, re-derived and checked against their
# own module; three are declared literals; one is declared arithmetic.
COUNTEREXAMPLE_CODE = "".join(str((2 * i + 1) % 3) for i in range(24))
DECLARED_TABLE_CODES = (
    ("declared literal A", "212212200002201202012010"),
    ("declared literal B", "202111111222211210202100"),
    ("declared arithmetic (2i+1) mod 3", COUNTEREXAMPLE_CODE),
)

# Declared configuration index set for the mask-invariance cross-check: the
# first 4096 integers of the base-3 expansion over the 27 sites, plus the
# arithmetic progression of step 1021 (a prime) and length 4096. No random
# number generator is used.
INVARIANCE_BLOCK = 4096
INVARIANCE_STEP = 1021
INVARIANCE_TERMS = 4096

# Declared table index set for the mask-versus-menu cross-check: the base-3
# expansions of j * floor(3^24 / 24), j = 0..23. Declared arithmetic.
BLOCK_FAMILY = 24


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


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...]:
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
    """Return (canonical map, orbit reps, flip-fixed orbits, flip-pairs, sizes)."""
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
    sizes = Counter(cmap.values())
    return cmap, reps, self_flip, pairs, sizes


def load_repo_rules():
    spec = importlib.util.spec_from_file_location("_repo_rules", RULES_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["_repo_rules"] = module
    spec.loader.exec_module(module)
    return module


def site_index(x: int, y: int, z: int) -> int:
    return 9 * (x % 3) + 3 * (y % 3) + (z % 3)


def site_coords(index: int) -> tuple[int, int, int]:
    return (index // 9, (index // 3) % 3, index % 3)


def neighbour_table() -> np.ndarray:
    table = np.zeros((NSITE, 6), dtype=np.int64)
    for x in range(3):
        for y in range(3):
            for z in range(3):
                for d, (dx, dy, dz) in enumerate(DIRECTIONS):
                    table[site_index(x, y, z), d] = site_index(x + dx, y + dy, z + dz)
    return table


NEIGHBOURS = neighbour_table()
POW3 = np.array([3 ** j for j in range(6)], dtype=np.int32)


def code_to_profile(code: int) -> tuple[int, ...]:
    out = []
    for j in range(6):
        digit = (code // (3 ** j)) % 3
        out.append(OPEN if digit == 0 else digit - 1)
    return tuple(out)


def profile_to_code(profile) -> int:
    return sum((0 if v == OPEN else v + 1) * (3 ** j) for j, v in enumerate(profile))


def show_profile(profile) -> str:
    return "".join("." if v == OPEN else str(v) for v in profile)


TERNARY = [code_to_profile(c) for c in range(729)]
TMAP, TREPS, TSELF, TPAIRS, TSIZES = census(TERNARY)
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


def masks_vectorised(configs: np.ndarray) -> np.ndarray:
    """configs: (B, 27) uint8 storage codes. Returns (B,) int64 demand masks."""
    batch = configs.shape[0]
    out = np.zeros(batch, dtype=np.int64)
    one = np.int64(1)
    for site in range(NSITE):
        column = configs[:, site]
        recorded = column != 0
        if not recorded.any():
            continue
        acc = np.zeros(batch, dtype=np.int32)
        for d in range(6):
            acc += configs[:, NEIGHBOURS[site, d]].astype(np.int32) * POW3[d]
        bit = DEMAND[acc, np.clip(column.astype(np.int64) - 1, 0, 1)]
        good = recorded & (bit >= 0)
        if good.any():
            out[good] |= one << bit[good].astype(np.int64)
    return out


def mask_scalar(config) -> int:
    """Independent scalar path: rebuild each profile tuple and re-canonicalise."""
    mask = 0
    for site in range(NSITE):
        if config[site] == 0:
            continue
        profile = tuple(
            OPEN if config[NEIGHBOURS[site, d]] == 0 else int(config[NEIGHBOURS[site, d]]) - 1
            for d in range(6)
        )
        orbit = REP_INDEX[canonical(profile)]
        if orbit not in SIDE_OF_ORBIT:
            continue
        pair, side = SIDE_OF_ORBIT[orbit]
        value = int(config[site]) - 1
        if side == 0:
            mask |= 1 << (2 * pair + (1 if value == 0 else 0))
        else:
            mask |= 1 << (2 * pair + (0 if value == 0 else 1))
    return mask


def parse_config(text: str) -> np.ndarray:
    return np.array(
        [0 if ch == "." else int(ch) + 1 for ch in text], dtype=np.uint8
    )


def show_config(config) -> str:
    return "".join("." if v == 0 else str(int(v) - 1) for v in config)


def table_from_code(code: str) -> np.ndarray:
    """729-array of menus: 0 = {0}, 1 = {1}, 2 = {0,1}."""
    digits = [int(ch) for ch in code]
    table = np.full(729, 2, dtype=np.int8)
    for c in range(729):
        orbit = int(ORBIT_OF[c])
        if orbit in SIDE_OF_ORBIT:
            pair, side = SIDE_OF_ORBIT[orbit]
            table[c] = digits[pair] if side == 0 else (
                2 if digits[pair] == 2 else 1 - digits[pair]
            )
    return table


def block_of_code(code: str) -> int:
    """The 48-bit block word of a table: bit 2i iff digit i = 0, bit 2i+1 iff 1."""
    block = 0
    for i, ch in enumerate(code):
        if ch == "0":
            block |= 1 << (2 * i)
        elif ch == "1":
            block |= 1 << (2 * i + 1)
    return block


NB_LIST = [[int(NEIGHBOURS[i, d]) for d in range(6)] for i in range(NSITE)]


def profile_code(config, site: int) -> int:
    n = NB_LIST[site]
    return (config[n[0]] + 3 * config[n[1]] + 9 * config[n[2]]
            + 27 * config[n[3]] + 81 * config[n[4]] + 243 * config[n[5]])


def statically_admissible(config, table) -> bool:
    for site in range(NSITE):
        if config[site]:
            menu = table[profile_code(config, site)]
            if menu != 2 and menu != config[site] - 1:
                return False
    return True


def reachable_levels(table, depth: int) -> list[set]:
    """Append-only formation from no records; records are never re-checked."""
    current = {bytes(NSITE)}
    levels = [current]
    for _ in range(depth):
        nxt = set()
        for config in current:
            for site in range(NSITE):
                if config[site]:
                    continue
                menu = table[profile_code(config, site)]
                for value in ((1, 2) if menu == 2 else (menu + 1,)):
                    grown = bytearray(config)
                    grown[site] = value
                    nxt.add(bytes(grown))
        current = nxt
        levels.append(current)
    return levels


def all_partial_configs(depth: int) -> list[bytes]:
    out = []
    for k in range(depth + 1):
        for sites in itertools.combinations(range(NSITE), k):
            for values in itertools.product((1, 2), repeat=k):
                config = bytearray(NSITE)
                for site, value in zip(sites, values):
                    config[site] = value
                out.append(bytes(config))
    return out


def record_count_sweep(depth: int):
    """Complete sweep of every partial configuration with at most `depth`
    records, site 0 fixed recorded at value 0 by the invariance of T1."""
    masks: set[int] = set()
    single_bit: dict[int, int] = {}
    totals: dict[int, int] = {}
    for k in range(1, depth + 1):
        nv = 1 << (k - 1)
        values = np.zeros((nv, k - 1), dtype=np.uint8)
        for a in range(nv):
            for b in range(k - 1):
                values[a, b] = 1 + ((a >> b) & 1)
        per_chunk = max(1, CELL_CAP // (nv * NSITE))
        combos = itertools.combinations(range(1, NSITE), k - 1)
        total = 0
        while True:
            block = list(itertools.islice(combos, per_chunk))
            if not block:
                break
            nc = len(block)
            comb = np.array(block, dtype=np.int64).reshape(nc, k - 1)
            batch = nc * nv
            configs = np.zeros((batch, NSITE), dtype=np.uint8)
            configs[:, 0] = 1
            rows = np.arange(batch)
            for j in range(k - 1):
                configs[rows, np.repeat(comb[:, j], nv)] = np.tile(values[:, j], nc)
            found = masks_vectorised(configs)
            total += batch
            unique, first = np.unique(found, return_index=True)
            for value, index in zip(unique.tolist(), first.tolist()):
                if value and (value & (value - 1)) == 0:
                    bit = value.bit_length() - 1
                    single_bit.setdefault(bit, k)
            masks.update(unique.tolist())
            del configs, found
        totals[k] = total
    return totals, masks, single_bit


def shell_family_bits() -> dict[int, int]:
    """Family F1: for each demand bit, the complete 3^12 assignment of the
    distance-2 shell around a demanding site at the origin."""
    shell = [i for i in range(NSITE) if sum(1 for t in site_coords(i) if t) == 2]
    assert len(shell) == 12
    trits = np.zeros((3 ** 12, 12), dtype=np.uint8)
    ramp = np.arange(3 ** 12)
    for j in range(12):
        trits[:, j] = (ramp // (3 ** j)) % 3
    hits: dict[int, int] = {}
    for bit in range(NBITS):
        pair, want = bit // 2, (1 if bit % 2 == 0 else 0)
        rep = TPAIRS[pair][0]
        base = np.zeros(NSITE, dtype=np.uint8)
        base[0] = want + 1
        for d in range(6):
            base[NEIGHBOURS[0, d]] = 0 if rep[d] == OPEN else rep[d] + 1
        configs = np.tile(base, (3 ** 12, 1))
        for j, site in enumerate(shell):
            configs[:, site] = trits[:, j]
        found = masks_vectorised(configs)
        where = np.nonzero(found == (np.int64(1) << bit))[0]
        if where.size:
            hits[bit] = int((configs[where[0]] != 0).sum())
        del configs, found
    return hits


def translation_family_bits() -> tuple[int, dict[int, int]]:
    """Family F3: every configuration invariant under a translation subgroup
    of order 3 -- 13 subgroups, 3^9 configurations each."""
    generators = []
    for gx in range(3):
        for gy in range(3):
            for gz in range(3):
                if (gx, gy, gz) == (0, 0, 0):
                    continue
                if tuple((2 * c) % 3 for c in (gx, gy, gz)) in generators:
                    continue
                generators.append((gx, gy, gz))
    trits = np.zeros((3 ** 9, 9), dtype=np.uint8)
    ramp = np.arange(3 ** 9)
    for j in range(9):
        trits[:, j] = (ramp // (3 ** j)) % 3
    hits: dict[int, int] = {}
    for g in generators:
        label = -np.ones(NSITE, dtype=np.int64)
        used = 0
        for i in range(NSITE):
            if label[i] >= 0:
                continue
            x, y, z = site_coords(i)
            for t in range(3):
                label[site_index(x + t * g[0], y + t * g[1], z + t * g[2])] = used
            used += 1
        assert used == 9
        configs = trits[:, label]
        found = masks_vectorised(configs)
        for bit in range(NBITS):
            if bit in hits:
                continue
            where = np.nonzero(found == (np.int64(1) << bit))[0]
            if where.size:
                hits[bit] = int((configs[where[0]] != 0).sum())
        del configs, found
    return len(generators), hits


def rotation_site_permutations() -> list[np.ndarray]:
    out = []
    for _, matrix in ROTATIONS:
        perm = np.zeros(NSITE, dtype=np.int64)
        for i in range(NSITE):
            c = site_coords(i)
            image = tuple(sum(matrix[r][k] * c[k] for k in range(3)) for r in range(3))
            perm[i] = site_index(*image)
        out.append(perm)
    return out


def declared_invariance_configs() -> np.ndarray:
    indices = list(range(INVARIANCE_BLOCK))
    indices += [(j * INVARIANCE_STEP) % (3 ** 15) for j in range(INVARIANCE_TERMS)]
    configs = np.zeros((len(indices), NSITE), dtype=np.uint8)
    for row, value in enumerate(indices):
        for site in range(NSITE):
            configs[row, site] = (value // (3 ** site)) % 3
    return configs


def current_input_identity():
    """Check every literal current input; no broader parent authority follows."""
    return (set(EXPECTED_INPUT_SHA256) == set(AUDIT_INPUT_PATHS)
            and all((ROOT / p).is_file()
                    and sha256((ROOT / p).read_bytes()).hexdigest() == digest
                    for p, digest in EXPECTED_INPUT_SHA256.items()))


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    probe = PROBE_PATH.read_text(encoding="utf-8")
    q8 = Q8_PATH.read_text(encoding="utf-8")
    time_note = TIME_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    probe_flat = normalize(probe)

    print("external_scientific_inputs: finite scaffold, pure menu helper and named context; physical access unsupplied")
    print("integrity_reads: axioms, deep probe, law pair, history-index note")
    print("construction: complete record-count, shell and translation sweeps; declared witnesses")
    print("negative_scope: none; this note counts fibres and selects no physical law")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: minimal_axioms Admissibility and Record clauses")
    print("declared_math: cubic rotations, ternary support tables, 48-bit demand masks")

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and are unique",
        all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS)
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )
    checks.check("audit-timeout", "the declared timeout is 300 seconds", AUDIT_TIMEOUT_SEC == 300)
    inputs_ok = current_input_identity()
    checks.check("current-input-identities", "all declared current input bytes match", inputs_ok)
    if not inputs_ok:
        return checks.finish()

    # ---------- supplied surface -------------------------------------------
    checks.check(
        "axiom-admissibility",
        "the live Admissibility sentence is quoted in the note",
        "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
        in axiom_flat
        and "the probability distribution over the possibilities is determined by, and varies with," in note_flat,
    )
    checks.check(
        "axiom-support",
        "reading note (3) equating availability with support is quoted",
        'denotes its support -- on finite menus, exactly the possibilities of nonzero probability' in axiom_flat
        and "denotes its support" in note_flat,
    )
    checks.check(
        "axiom-record-readable",
        "the Record clauses on readability and absence are quoted",
        "Only records are readable." in axiom
        and "A site with no record cannot be read." in axiom
        and "Only records are readable" in note
        and "A site with no record cannot be read" in note,
    )
    checks.check(
        "axiom-record-state",
        "the Record clauses on states and formation are quoted",
        "A state is a configuration of records." in axiom
        and "Records form." in axiom
        and "A state is a configuration of records" in note
        and "Records form" in note,
    )
    checks.check(
        "axiom-partial-licence",
        "absence and the unsupplied order do not provide a static membership oracle",
        "every site carries a record" not in axiom_flat
        and "order of formation" not in axiom
        and "not a Record-licensed membership oracle" in note_flat,
    )
    checks.check(
        "parent-deep-probe",
        "the deep probe's 3^24 census is live and cited",
        "number of covariant label-equivariant tables = 3^24" in probe
        and "282,429,536,480" in probe_flat
        and "282,429,536,481" in note_flat,
    )
    checks.check(
        "parent-law-pair",
        "the 2026-08-13 law pair is live",
        "claim_type: bounded_theorem" in q8
        and "It selects neither rule as the framework's physical law." in normalize(q8),
    )
    checks.check(
        "parent-history-index",
        "the history-index note is live and named in the note",
        "Record-Monotone" in time_note
        and "TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md" in note,
    )

    # ---------- T1: the readout and its mask reduction ----------------------
    checks.check(
        "T1-profiles",
        "729 ternary profiles fall into 57 proper-cubic orbits",
        len(TERNARY) == 729 and len(TREPS) == 57,
        (len(TERNARY), len(TREPS)),
    )
    checks.check(
        "T1-flip",
        "9 flip-fixed orbits are pinned to {0,1}; 24 flip-pairs carry one digit each",
        len(TSELF) == 9 and NPAIR == 24 and len(TSELF) + 2 * NPAIR == 57,
        (len(TSELF), NPAIR),
    )
    checks.check(
        "T1-tables",
        "the table space is 3^24 = 282429536481 and the demand word is 48 bits",
        3 ** 24 == 282429536481 and NBITS == 48,
    )
    checks.check(
        "T1-pinned-carry-no-bit",
        "records on the 9 flip-fixed orbits raise no demand bit",
        all(
            (DEMAND[c, 0] < 0 and DEMAND[c, 1] < 0)
            == (int(ORBIT_OF[c]) not in SIDE_OF_ORBIT)
            for c in range(729)
        )
        and sum(1 for c in range(729) if DEMAND[c, 0] < 0) == sum(
            TSIZES[rep] for rep in TSELF
        ),
    )

    rotation_perms = rotation_site_permutations()
    invariance_configs = declared_invariance_configs()
    base_masks = masks_vectorised(invariance_configs)
    translation_ok = True
    for shift in range(NSITE):
        sx, sy, sz = site_coords(shift)
        perm = np.array(
            [site_index(*(np.array(site_coords(i)) + np.array([sx, sy, sz])))
             for i in range(NSITE)],
            dtype=np.int64,
        )
        moved_masks = masks_vectorised(invariance_configs[:, perm])
        translation_ok &= bool(np.array_equal(moved_masks, base_masks))
    rotation_ok = True
    for perm in rotation_perms:
        rotation_ok &= bool(
            np.array_equal(masks_vectorised(invariance_configs[:, perm]), base_masks)
        )
    flipped = invariance_configs.copy()
    swapped = flipped == 1
    flipped[flipped == 2] = 1
    flipped[swapped] = 2
    flip_ok = bool(np.array_equal(masks_vectorised(flipped), base_masks))
    checks.check(
        "T1-invariance",
        f"mask invariant under 27 translations, {len(ROTATIONS)} rotations and the flip on "
        f"{invariance_configs.shape[0]} declared configurations",
        translation_ok and rotation_ok and flip_ok and len(ROTATIONS) == 24,
        (translation_ok, rotation_ok, flip_ok),
    )

    scalar_ok = all(
        mask_scalar(invariance_configs[row]) == int(base_masks[row])
        for row in range(0, invariance_configs.shape[0], 8)
    )
    checks.check(
        "T1-two-paths",
        "the vectorised and scalar mask paths agree on the declared set",
        scalar_ok,
    )

    step = (3 ** 24) // BLOCK_FAMILY
    family_codes = []
    for j in range(BLOCK_FAMILY):
        value = j * step
        family_codes.append("".join(str((value // (3 ** i)) % 3) for i in range(24)))
    criterion_ok = True
    sample = invariance_configs[:: max(1, invariance_configs.shape[0] // 256)]
    sample_masks = masks_vectorised(sample)
    for code in family_codes:
        table = table_from_code(code)
        block = block_of_code(code)
        for row in range(sample.shape[0]):
            direct = statically_admissible(sample[row].tolist(), table)
            by_mask = (int(sample_masks[row]) & block) == 0
            if direct != by_mask:
                criterion_ok = False
                break
        if not criterion_ok:
            break
    checks.check(
        "T1-criterion",
        f"admissibility == mask & block == 0 on {sample.shape[0]} configurations x "
        f"{BLOCK_FAMILY} tables",
        criterion_ok,
    )

    # ---------- T2: the complete sweeps ------------------------------------
    realised = 0
    for code in range(729):
        profile = TERNARY[code]
        config = np.zeros(NSITE, dtype=np.uint8)
        config[0] = 1
        for d in range(6):
            config[NEIGHBOURS[0, d]] = 0 if profile[d] == OPEN else profile[d] + 1
        seen = tuple(
            OPEN if config[NEIGHBOURS[0, d]] == 0 else int(config[NEIGHBOURS[0, d]]) - 1
            for d in range(6)
        )
        realised += int(seen == profile)
    checks.check(
        "T2-profiles-realised",
        "all 729 ternary profiles are realised at a recorded site",
        realised == 729 and len(set(int(v) for v in NEIGHBOURS[0])) == 6,
        realised,
    )

    totals, sweep_masks, sweep_bits = record_count_sweep(KSWEEP)
    expected = {
        k: math_comb(NSITE - 1, k - 1) * (1 << (k - 1)) for k in range(1, KSWEEP + 1)
    }
    checks.check(
        "T2-sweep-complete",
        f"complete for k <= {KSWEEP}: {sum(totals.values())} configurations, "
        f"{totals[KSWEEP]} at k = {KSWEEP}",
        totals == expected and totals[8] == 84198400 and sum(totals.values()) == 101299433,
        (totals, expected),
    )
    checks.check(
        "T2-sweep-masks",
        f"{len(sweep_masks)} distinct demand masks; {len(sweep_bits)} of 48 single bits isolated",
        len(sweep_masks) == 7824 and len(sweep_bits) == 17,
        (len(sweep_masks), len(sweep_bits)),
    )

    shell_bits = shell_family_bits()
    checks.check(
        "T2-shell-complete",
        f"the 3^12 = {3 ** 12} distance-2 shell of all 48 bits is complete; {len(shell_bits)} isolated",
        len(shell_bits) == 20,
        sorted(shell_bits),
    )
    ngen, translation_bits = translation_family_bits()
    checks.check(
        "T2-translation-complete",
        f"the {ngen} x 3^9 translation-symmetric family is complete; {len(translation_bits)} isolated",
        ngen == 13 and len(translation_bits) == 27,
        (ngen, sorted(translation_bits)),
    )
    union_bits = set(sweep_bits) | set(shell_bits) | set(translation_bits)
    checks.check(
        "T2-union",
        f"the three families together isolate {len(union_bits)} of 48 demand bits",
        len(union_bits) == 30 and set(sweep_bits) <= union_bits,
        sorted(union_bits),
    )

    # ---------- T3: the declared witness list -------------------------------
    witness_ok = []
    for stated, text in DECLARED_WITNESSES:
        config = parse_config(text)
        vector = int(masks_vectorised(config.reshape(1, NSITE))[0])
        scalar = mask_scalar(config)
        witness_ok.append(vector == stated and scalar == stated)
    checks.check(
        "T3-witnesses",
        f"all {len(DECLARED_WITNESSES)} declared witnesses reproduce their mask by both paths",
        all(witness_ok) and len(DECLARED_WITNESSES) == 44,
        [i for i, ok in enumerate(witness_ok) if not ok],
    )
    confined = {}
    for stated, text in DECLARED_WITNESSES:
        low = (stated & -stated).bit_length() - 1
        high = stated.bit_length() - 1
        if low // 2 != high // 2:
            confined = None
            break
        confined.setdefault(low // 2, set()).add(stated)
    checks.check(
        "T3-confined",
        "every declared witness mask is confined to one flip-pair",
        confined is not None and len(DECLARED_WITNESSES) == sum(
            len(v) for v in confined.values()
        ),
    )
    full = half = none = 0
    classes = 1
    table_rows = []
    for pair in range(24):
        got = confined.get(pair, set())
        kinds = sum(
            [(1 << (2 * pair)) in got, (1 << (2 * pair + 1)) in got, (3 << (2 * pair)) in got]
        )
        separated = 3 if kinds >= 2 else (2 if kinds == 1 else 1)
        classes *= separated
        full += separated == 3
        half += separated == 2
        none += separated == 1
        table_rows.append((pair, show_profile(TPAIRS[pair][0]), show_profile(TPAIRS[pair][1]),
                           kinds, separated))
    unseparated = [pair for pair, _, _, _, sep in table_rows if sep == 1]
    checks.check(
        "T3-visibility",
        f"the witnesses read {full} of 24 digits exactly, {half} to a binary choice, "
        f"{none} unseparated",
        (full, half, none) == (17, 3, 4),
        (full, half, none),
    )
    checks.check(
        "T3-unseparated",
        "pairs not separated by any declared witness: 11, 16, 17, 23",
        unseparated == [11, 16, 17, 23],
        unseparated,
    )
    checks.check(
        "T3-classes",
        f"the readout distinguishes at least 3^17 * 2^3 = {classes} laws",
        classes == 3 ** 17 * 2 ** 3 == 1033121304,
        classes,
    )
    checks.check(
        "T3-fibre",
        "every fibre holds at most 648 tables, against 3^20 for complete records",
        3 ** 4 * 2 ** 3 == 648 and 3 ** 20 == 3486784401
        and 3 ** 20 // 648 == 5380840 and classes // 81 == 12754584
        and classes * 648 >= 3 ** 24,
    )
    checks.check(
        "T3-pinned-menus",
        "the 9 flip-fixed orbits carry menu {0,1} for every table, so a demand can stand alone",
        all(
            table_from_code(code)[profile_to_code(rep)] == 2
            for code in family_codes for rep in TSELF
        ),
    )
    print("digit_visibility (pair:values separated, 24 pairs): "
          + " ".join(f"{p}:{s}" for p, _, _, _, s in table_rows))

    # ---------- T4: growth compatibility ------------------------------------
    rules = load_repo_rules()
    majority_code, copy_code = repo_rule_codes(rules)
    checks.check(
        "T4-repo-rules",
        f"repository codes {majority_code} / {copy_code} rebuild the module's own menus",
        majority_code == "000001000000200000110000"
        and copy_code == "000022020202220222220222",
        (majority_code, copy_code),
    )
    declared_tables = [
        ("majority (repository)", majority_code),
        ("copy-neighbour (repository)", copy_code),
        ("declared literal A", DECLARED_TABLE_CODES[0][1]),
        ("declared literal B", DECLARED_TABLE_CODES[1][1]),
        ("all menus {0,1}", "2" * 24),
        ("declared arithmetic (2i+1) mod 3", DECLARED_TABLE_CODES[2][1]),
    ]
    every = all_partial_configs(KGROWTH)
    checks.check(
        "T4-enumeration",
        f"all {len(every)} configurations with at most {KGROWTH} records enumerated",
        len(every) == 305659 == 1 + 54 + 1404 + 23400 + 280800,
        len(every),
    )
    rows = []
    for name, code in declared_tables:
        table = table_from_code(code)
        reachable = set().union(*reachable_levels(table, KGROWTH))
        admissible = set(c for c in every if statically_admissible(c, table))
        rows.append((name, len(admissible), len(reachable),
                     len(admissible - reachable), len(reachable - admissible)))
        print(f"growth_row {name}: {len(admissible)} {len(reachable)} "
              f"{len(admissible - reachable)} {len(reachable - admissible)}")
    by_name = {row[0]: row for row in rows}
    checks.check(
        "T4-repo-counts",
        "repository |A| = 151489 / 152137 and |R| = 194905 / 196201",
        by_name["majority (repository)"][1:3] == (151489, 194905)
        and by_name["copy-neighbour (repository)"][1:3] == (152137, 196201),
        rows,
    )
    contained = [row[0] for row in rows if row[3] == 0]
    checks.check(
        "T4-containment",
        f"every admissible configuration is reachable for {len(contained)} of {len(rows)} tables",
        len(contained) == 5 and "majority (repository)" in contained
        and "copy-neighbour (repository)" in contained,
        rows,
    )
    breaking = [row for row in rows if row[3] > 0]
    checks.check(
        "T4-containment-not-universal",
        "not universal: one declared table has 1350 admissible configurations no order reaches",
        len(breaking) == 1 and breaking[0][3] == 1350
        and breaking[0][0] == "declared arithmetic (2i+1) mod 3",
        breaking,
    )
    counter_table = table_from_code(COUNTEREXAMPLE_CODE)
    counter_reachable = set().union(*reachable_levels(counter_table, KGROWTH))
    counter_admissible = set(c for c in every if statically_admissible(c, counter_table))
    smallest = sorted(counter_admissible - counter_reachable,
                      key=lambda c: (sum(1 for v in c if v), c))
    exhibit = smallest[0]
    order_exists = False
    sites = [s for s in range(NSITE) if exhibit[s]]
    for order in itertools.permutations(sites):
        stage = bytearray(NSITE)
        ok = True
        for site in order:
            menu = counter_table[profile_code(stage, site)]
            if menu != 2 and menu != exhibit[site] - 1:
                ok = False
                break
            stage[site] = exhibit[site]
        if ok:
            order_exists = True
            break
    checks.check(
        "T4-counterexample",
        f"the smallest witness carries {len(sites)} records, stands, and no order builds it",
        len(sites) == 3 and statically_admissible(exhibit, counter_table)
        and not order_exists,
        show_config(exhibit),
    )
    majority_table = table_from_code(majority_code)
    majority_reachable = set().union(*reachable_levels(majority_table, KGROWTH))
    majority_admissible = set(c for c in every if statically_admissible(c, majority_table))
    converse = sorted(majority_reachable - majority_admissible,
                      key=lambda c: (sum(1 for v in c if v), c))
    checks.check(
        "T4-converse",
        f"converse fails: {len(converse)} reachable under majority are not admissible as they stand",
        len(converse) == 43416 and sum(1 for v in converse[0] if v) == 3,
        len(converse),
    )
    print(f"converse_witness: {show_config(converse[0])}")

    base_table = table_from_code("2" * 24)
    base_depth4 = sum(len(level) for level in reachable_levels(base_table, 4))
    base_depth3 = sum(len(level) for level in reachable_levels(base_table, 3))
    moved4, moved3, shrink4 = set(), set(), 0
    for pair in range(24):
        for value in (0, 1):
            code = list("2" * 24)
            code[pair] = str(value)
            table = table_from_code("".join(code))
            if sum(len(level) for level in reachable_levels(table, 4)) != base_depth4:
                moved4.add(pair)
                shrink4 += 1
            if sum(len(level) for level in reachable_levels(table, 3)) != base_depth3:
                moved3.add(pair)
    checks.check(
        "T4-reachable-readout",
        f"the bare reachable set answers {shrink4} of 48 single-digit restrictions: "
        f"{len(moved4)} of 24 digits at k <= {KGROWTH}, {len(moved3)} at k <= 3",
        len(moved4) == 3 and sorted(moved4) == [0, 1, 2] and shrink4 == 5
        and len(moved3) == 2 and sorted(moved3) == [0, 1]
        and base_depth4 == 305659,
        (sorted(moved4), shrink4, sorted(moved3), base_depth4),
    )

    # ---------- note contract -----------------------------------------------
    phrases = (
        "1,033,121,304", "648", "3^20", "282,429,536,481", "5,380,840",
        "84,198,400", "7,824", "305,659", "43,416", "1,350",
        "records register", "declared witness", "supplied open symbol", "one torus",
        "not separated by any declared witness",
    )
    missing = [phrase for phrase in phrases if phrase not in note_flat]
    checks.check(
        "note-phrases",
        f"all {len(phrases)} required counts and boundary phrases appear",
        not missing,
        missing,
    )
    checks.check(
        "note-open-question",
        "the original unseparated pairs and later joint scope are distinguished",
        "This list leaves their separation open" in note_flat
        and "later conditional full-pool certificate" in note_flat,
    )
    checks.check(
        "note-scope-hygiene",
        "the note claims no law selection and no injectivity",
        "promoted" not in note.lower()
        and "new axiom" not in note.lower()
        and "no physical law is selected" in note_flat
        and "is injective" not in note.lower()
        and "injectivity is not claimed" in note_flat.lower(),
    )
    banned = ("measurement", "collapse", "observer", "exhaustive", "exhausted",
              "no-go", "closes the route", "only route", "invisible")
    banned_hits = [word for word in banned if word in note.lower()]
    import re as _re
    banned_hits += _re.findall(r"\b(?:swap|swaps|swapped|move|moves|moved|fill|fills|filled)\b",
                               note.lower())
    checks.check(
        "note-vocabulary",
        "the note avoids process, closure and site-rewriting vocabulary",
        not banned_hits,
        banned_hits,
    )
    checks.check(
        "note-length",
        "the note stays under 330 lines",
        len(note.splitlines()) < 330,
        len(note.splitlines()),
    )
    checks.check(
        "note-registry-id",
        "the note declares its registry id",
        "partially_recorded_regions_make_most_of_law_visible_torus_3" in note,
    )

    print("per_element: all 729 profiles, 48 demand bits and 44 declared witnesses classified exactly")
    print("per_site: each of the 27 sites evaluated in both mask paths")
    print("per_mode: checked and not executed - no spectral or normal-mode decomposition here")
    print("per_block: 24 flip-pairs, six declared tables, 48 single-digit restrictions")
    print("lattice_wide: one 3^3 torus; site-0/value-0 sweep complete to 8 records with mask-preserving symmetry reduction")
    return checks.finish()


def math_comb(n: int, k: int) -> int:
    import math
    return math.comb(n, k)


def repo_rule_codes(rules) -> tuple[str, str]:
    """Re-derive the two repository rules as 24-digit codes and check the
    729-table each code rebuilds against the module's own menu function."""
    binary = (0, 1)
    menus = (
        lambda profile: rules.majority_availability(profile),
        lambda profile: rules.copy_neighbor_availability(profile, binary),
    )
    codes = []
    for rule in menus:
        digits = []
        for rep_a, _ in TPAIRS:
            menu = set(rule(rep_a))
            digits.append("0" if menu == {0} else ("1" if menu == {1} else "2"))
        code = "".join(digits)
        rebuilt = table_from_code(code)
        for c in range(729):
            menu = set(rule(TERNARY[c]))
            want = 0 if menu == {0} else (1 if menu == {1} else 2)
            assert int(rebuilt[c]) == want, c
        codes.append(code)
    return codes[0], codes[1]


if __name__ == "__main__":
    raise SystemExit(main())
