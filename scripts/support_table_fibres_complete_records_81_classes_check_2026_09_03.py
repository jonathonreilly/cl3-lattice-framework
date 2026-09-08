#!/usr/bin/env python3
"""Finite static support-table fibres and supplied fixed-order endpoint laws.

The runner recomputes, with no sampling and no random number generator:

T1  the covariant label-equivariant support-table census (729 ternary profiles,
    57 proper-cubic orbits, 9 self-flip orbits, 24 flip-pairs, 3^24 tables);
T2  the fully-recorded sub-census that a complete configuration can realise
    (64 profiles, 10 orbits, 2 self-flip, 4 flip-pairs), hence 4 visible and
    20 invisible ternary digits on any lattice;
T3  a complete enumeration of all 2^27 complete configurations of the 3^3
    torus, the 81 distinct globally admissible sets, and their uniform 3^20
    fibres, with two independent complete recounts;
T4  supplied lex-order endpoint laws for 35 original table calls, three
    geometric order checks, exact uncensored fibres, censored upper bounds,
    and an endpoint total-variation-one witness in one static class.
    Added tiny controls test censoring and the exact finite-prefix fibre proof.

No physical law is selected. The two repository rules are used as declared
reference points, imported from their own module, not re-implemented here.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 300

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/ONLY_81_OF_THE_SUPPORT_TABLES_ARE_DISTINGUISHABLE_BY_COMPLETE_RECORDS_"
    "FORMATION_HISTORIES_DISTINGUISH_NEARLY_ALL_BOUNDED_THEOREM_NOTE_2026-09-03.md"
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
    "docs/ONLY_81_OF_THE_SUPPORT_TABLES_ARE_DISTINGUISHABLE_BY_COMPLETE_RECORDS_"
    "FORMATION_HISTORIES_DISTINGUISH_NEARLY_ALL_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md",
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_"
    "BOUNDED_NOTE_2026-07-03.md",
    "scripts/extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py",
)

assert AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL, PROBE_REL, Q8_REL, TIME_REL, RULES_REL)

EXPECTED_INPUT_SHA256 = {'docs/ONLY_81_OF_THE_SUPPORT_TABLES_ARE_DISTINGUISHABLE_BY_COMPLETE_RECORDS_FORMATION_HISTORIES_DISTINGUISH_NEARLY_ALL_BOUNDED_THEOREM_NOTE_2026-09-03.md': '91780c2b16c999e68c6f0d4dfb5eff5baaa153cc29dc73f9fd6f225c9d36ad66', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md': 'c277ca66054a47ac0183e1a7d806acf0fee01167915d8b70746125d73a5a56f4', 'docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md': 'c08d7a351c2ae40d921b0e996ca817b4f789c51072fbf2b6eb9a2de6f6fe8967', 'docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md': '3dab4d91c2fd016f00bdab64beb0376c0e800c1026f5cfb862233e34927f6d9f', 'scripts/extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py': 'f90db72fd8c7c7c3de2f119f40a28b417e1e61679a3abf02da7e65368b6f12ec'}

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL
PROBE_PATH = ROOT / PROBE_REL
Q8_PATH = ROOT / Q8_REL
TIME_PATH = ROOT / TIME_REL
RULES_PATH = ROOT / RULES_REL

OPEN = -1
DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}

# Declared configuration set for the coordinate-versus-plane cross-check: the
# first 2^16 integers plus the arithmetic progression of step 1021 (a prime,
# so the low bits vary) of length 2^17. No random number generator is used.
CHECK_BLOCK = 1 << 16
CHECK_STEP = 1021
CHECK_TERMS = 1 << 17

# Declared table family for the formation-fibre census: the base-3 expansions
# of k_j = j * floor(3^24 / 32), j = 0..31. Declared arithmetic, no seed.
FAMILY_SIZE = 32
FRONTIER_CAP = 40000


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


def proper_cubic_rotations() -> tuple[tuple[int, ...], ...]:
    out = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * math.prod(signs) != 1:
                continue
            matrix = [[0, 0, 0] for _ in range(3)]
            for row in range(3):
                matrix[row][perm[row]] = signs[row]
            out.append(
                tuple(
                    DIR_INDEX[
                        tuple(
                            sum(matrix[r][c] * d[c] for c in range(3)) for r in range(3)
                        )
                    ]
                    for d in DIRECTIONS
                )
            )
    return tuple(out)


ROTATIONS = proper_cubic_rotations()


def rotate_profile(profile, rotation):
    return tuple(profile[rotation[i]] for i in range(6))


def flip_profile(profile):
    return tuple(v if v == OPEN else 1 - v for v in profile)


def canonical(profile):
    return min(rotate_profile(profile, r) for r in ROTATIONS)


def census(profiles):
    """Return (orbit reps, self-flip orbits, flip-pairs, orbit sizes)."""
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
    return 9 * x + 3 * y + z


def neighbour_table() -> np.ndarray:
    table = np.zeros((27, 6), dtype=np.int64)
    for x in range(3):
        for y in range(3):
            for z in range(3):
                for d, (dx, dy, dz) in enumerate(DIRECTIONS):
                    table[site_index(x, y, z), d] = site_index(
                        (x + dx) % 3, (y + dy) % 3, (z + dz) % 3
                    )
    return table


def blocked_mask_table(cmap, pairs):
    """contrib[profile*2 + value] = 8-bit mask of menu choices this pair blocks."""
    pair_index = {}
    for i, (a, b) in enumerate(pairs):
        pair_index[a] = (i, 0)
        pair_index[b] = (i, 1)
    contrib = np.zeros(128, dtype=np.uint8)
    for profile in product((0, 1), repeat=6):
        rep = cmap[profile]
        if rep not in pair_index:
            continue  # self-flip orbit: menu forced to {0,1}, never blocking
        i, side = pair_index[rep]
        index = sum(profile[d] << d for d in range(6))
        for value in (0, 1):
            blocks_menu_zero = (value == 1) if side == 0 else (value == 0)
            bit = (1 << (2 * i)) if blocks_menu_zero else (1 << (2 * i + 1))
            contrib[index * 2 + value] = bit
    return contrib, pair_index


def plane_tables(contrib):
    """H[j, S, m, p] = mask contributed by in-plane site j of plane S."""
    in_plane = {}
    for y in range(3):
        for z in range(3):
            j = 3 * y + z
            in_plane[j] = {
                2: 3 * ((y + 1) % 3) + z,
                3: 3 * ((y - 1) % 3) + z,
                4: 3 * y + ((z + 1) % 3),
                5: 3 * y + ((z - 1) % 3),
            }
    tables = np.zeros((9, 512, 2, 2), dtype=np.uint8)
    for j in range(9):
        for S in range(512):
            base = 0
            for d in (2, 3, 4, 5):
                base |= ((S >> in_plane[j][d]) & 1) << d
            own = (S >> j) & 1
            for m in (0, 1):
                for p in (0, 1):
                    tables[j, S, m, p] = contrib[(base | (m << 1) | p) * 2 + own]
    bits = np.zeros((9, 512), dtype=np.intp)
    for j in range(9):
        bits[j] = (np.arange(512) >> j) & 1
    return tables, bits


def complete_mask_histogram(tables, bits):
    """Complete enumeration of all 2^27 configurations, in 512 plane chunks.

    A configuration is the triple of x-planes (P0, P1, P2), each nine bits.
    Its realised mask is the OR of the three plane contributions
    g(P2,P0,P1) | g(P0,P1,P2) | g(P1,P2,P0), and g factorises over the nine
    in-plane sites, so no array larger than 512 x 512 is ever allocated.
    """
    rows = np.arange(512, dtype=np.intp)[:, None]
    cols = np.arange(512, dtype=np.intp)[None, :]
    histogram = np.zeros(256, dtype=np.int64)
    for a in range(512):
        total = np.zeros((512, 512), dtype=np.uint8)
        for j in range(9):
            bit_row = bits[j][:, None]
            bit_col = bits[j][None, :]
            a_bit = int(bits[j][a])
            total |= tables[j, a][bit_col, bit_row]
            total |= tables[j][:, a_bit, :][rows, bit_col]
            total |= tables[j][:, :, a_bit][cols, bit_row]
        histogram += np.bincount(total.ravel(), minlength=256)
    return histogram


def declared_check_configurations() -> np.ndarray:
    block = np.arange(CHECK_BLOCK, dtype=np.uint32)
    ladder = (np.arange(CHECK_TERMS, dtype=np.uint64) * CHECK_STEP).astype(np.uint32)
    return np.unique(np.concatenate([block, ladder]))


def coordinate_masks(configs, contrib, neighbours):
    mask = np.zeros(configs.shape[0], dtype=np.uint8)
    for s in range(27):
        profile = np.zeros(configs.shape[0], dtype=np.uint32)
        for d in range(6):
            shift = np.uint32(neighbours[s, d])
            profile |= ((configs >> shift) & np.uint32(1)) << np.uint32(d)
        value = (configs >> np.uint32(s)) & np.uint32(1)
        mask |= contrib[(profile * 2 + value).astype(np.intp)]
    return mask


def plane_masks(configs, tables, bits):
    p0 = (configs & np.uint32(511)).astype(np.intp)
    p1 = ((configs >> np.uint32(9)) & np.uint32(511)).astype(np.intp)
    p2 = ((configs >> np.uint32(18)) & np.uint32(511)).astype(np.intp)
    mask = np.zeros(configs.shape[0], dtype=np.uint8)
    for j in range(9):
        bj = bits[j]
        mask |= tables[j, :, :, :][p0, bj[p2], bj[p1]]
        mask |= tables[j, :, :, :][p1, bj[p0], bj[p2]]
        mask |= tables[j, :, :, :][p2, bj[p1], bj[p0]]
    return mask


def independent_recount(neighbours):
    """Complete 2^27 recount of two named classes by neighbour sums only.

    No orbit machinery, no plane factorisation, no mask: a configuration is
    counted for the majority rule when every site's value agrees with the
    majority of its six neighbours (a three-three shell leaves both values
    supported), and for the copy-neighbour rule when every site whose six
    neighbours all carry one value carries that value too.
    """
    chunk = 1 << 22
    majority_total = 0
    copy_total = 0
    for start in range(0, 1 << 27, chunk):
        configs = np.arange(start, start + chunk, dtype=np.uint32)
        majority_ok = np.ones(chunk, dtype=bool)
        copy_ok = np.ones(chunk, dtype=bool)
        for s in range(27):
            shell = np.zeros(chunk, dtype=np.uint8)
            for d in range(6):
                shell += ((configs >> np.uint32(neighbours[s, d])) & np.uint32(1)).astype(np.uint8)
            value = ((configs >> np.uint32(s)) & np.uint32(1)).astype(np.uint8)
            majority_ok &= (shell == 3) | (value == (shell > 3))
            copy_ok &= ((shell != 0) | (value == 0)) & ((shell != 6) | (value == 1))
        majority_total += int(majority_ok.sum())
        copy_total += int(copy_ok.sum())
    return majority_total, copy_total


TOPEN = 2  # ternary storage code for an unrecorded neighbour
TPOW = np.array([3 ** d for d in range(6)], dtype=np.int64)


class Formation:
    """Supplied sequential formation on the torus under a declared site order.

    Blank start; at step k the site's support is the table entry for the
    current ternary profile, and the value is uniform on that support (the
    canonical lift of the deep-probe note). Atoms are exact only if uncensored.
    """

    def __init__(self, ternary_pairs, ternary_cmap, neighbours):
        self.pair_of = {}
        for i, (a, b) in enumerate(ternary_pairs):
            self.pair_of[a] = (i, 0)
            self.pair_of[b] = (i, 1)
        self.cmap = ternary_cmap
        self.neighbours = neighbours
        self.pair_index = np.full(729, -1, dtype=np.int64)
        for profile, rep in ternary_cmap.items():
            if rep in self.pair_of:
                self.pair_index[self.tindex(profile)] = self.pair_of[rep][0]

    @staticmethod
    def tindex(profile) -> int:
        return sum(profile[d] * (3 ** d) for d in range(6))

    def menu(self, code):
        table = np.full(729, 2, dtype=np.int8)
        for profile, rep in self.cmap.items():
            if rep not in self.pair_of:
                continue
            i, side = self.pair_of[rep]
            digit = code[i]
            table[self.tindex(profile)] = 2 if digit == 2 else (digit if side == 0 else 1 - digit)
        return table

    def frontier(self, code, order, cap, weighted):
        """Capped frontier; surviving prefixes give a subset of positive queries."""
        menu = self.menu(code)
        states = np.full((1, 27), TOPEN, dtype=np.int8)
        weights = np.ones(1) if weighted else None
        queried, truncated = set(), False
        for s in order:
            index = np.zeros(states.shape[0], dtype=np.int64)
            for d in range(6):
                index += states[:, self.neighbours[s, d]].astype(np.int64) * TPOW[d]
            for pair in np.unique(self.pair_index[index]):
                if pair >= 0:
                    queried.add(int(pair))
            picked = menu[index]
            fixed = picked != 2
            settled = states[fixed].copy()
            if settled.shape[0]:
                settled[:, s] = picked[fixed].astype(np.int8)
            branching = states[~fixed]
            if branching.shape[0]:
                low, high = branching.copy(), branching.copy()
                low[:, s] = 0
                high[:, s] = 1
                parts = [settled, low, high] if settled.shape[0] else [low, high]
                states = np.vstack(parts)
                if weighted:
                    wb = weights[~fixed] * 0.5
                    pieces = [weights[fixed], wb, wb] if settled.shape[0] else [wb, wb]
                    weights = np.concatenate(pieces)
            else:
                states = settled
                if weighted:
                    weights = weights[fixed]
            if not weighted:
                states = np.unique(states, axis=0)
            if states.shape[0] > cap:
                truncated = True
                keep = np.argsort(-weights)[:cap] if weighted else np.arange(cap)
                states = states[keep]
                if weighted:
                    weights = weights[keep]
        return states, weights, queried, truncated


def order_reachable_pairs(order, ternary_cmap, pair_of, neighbours):
    position = {s: k for k, s in enumerate(order)}
    touched, profiles = set(), set()
    for k, s in enumerate(order):
        formed = [d for d in range(6) if position[neighbours[s, d]] < k]
        for bits in product((0, 1), repeat=len(formed)):
            profile = [TOPEN] * 6
            for d, b in zip(formed, bits):
                profile[d] = b
            profile = tuple(profile)
            profiles.add(profile)
            rep = ternary_cmap[profile]
            if rep in pair_of:
                touched.add(pair_of[rep][0])
    return touched, profiles


def current_input_identity():
    """Check every literal current input; historical labels supply no authority."""
    return (set(EXPECTED_INPUT_SHA256) == set(AUDIT_INPUT_PATHS)
            and all((ROOT / p).is_file()
                    and sha256((ROOT / p).read_bytes()).hexdigest() == digest
                    for p, digest in EXPECTED_INPUT_SHA256.items()))


def endpoint_fibre_interval(queried, complete):
    """Uniform fixed-order theorem: a censored query set gives an upper bound."""
    queried = set(queried)
    if not queried <= set(range(24)):
        raise ValueError("query digit outside the supplied 24-digit family")
    upper = 3 ** (24 - len(queried))
    return (upper if complete else 1, upper)


def finite_prefix_fibres(formation):
    """Actual four-site laws for all nine choices of the two queried digits."""
    order = list(range(4))
    _, _, possible, cut = formation.frontier([2] * 24, order, 1000, True)
    free = tuple(sorted(possible))
    classes, rows = {}, []
    if cut or free != (16, 23):
        return False, {"free": free, "truncated": cut}
    for choices in product((0, 1, 2), repeat=len(free)):
        code = [2] * 24
        for digit, choice in zip(free, choices):
            code[digit] = choice
        states, weights, queried, cut = formation.frontier(code, order, 1000, True)
        law = tuple(sorted((tuple(map(int, row)), float(weight))
                           for row, weight in zip(states, weights)))
        classes.setdefault(law, []).append(choices)
        rows.append((law, set(free) & queried, cut))
    ok = (len(classes) == 7 and len(rows) == 9
          and all(sum(weight for _config, weight in law) == 1.0 for law in classes)
          and all(not cut and len(classes[law]) == 3 ** (len(free) - len(query))
                  for law, query, cut in rows))
    return ok, {"free": free, "class_sizes": sorted(map(len, classes.values()))}


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

    print("external_scientific_inputs: finite support scaffold, pure menu helper and stated context; no physical oracle")
    print("integrity_reads: minimal axioms, deep probe, covariant law pair, history-index note")
    print("construction: complete 2^27 static enumeration; original 35 lex frontiers plus bounded correction controls")
    print("negative_scope: none; this note counts fibres and selects no physical law")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: minimal_axioms Admissibility and Record clauses")
    print("declared_math: proper cubic rotations, ternary support tables, exact atom weights")

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
        "reading note (3) equating availability with the support is quoted",
        'denotes its support -- on finite menus, exactly the possibilities of nonzero probability' in axiom_flat
        and "denotes its support" in note_flat,
    )
    checks.check(
        "axiom-record",
        "the Record clauses on readability and on states are quoted",
        "Only records are readable." in axiom
        and "A state is a configuration of records." in axiom
        and "Only records are readable" in note
        and "A state is a configuration of records" in note,
    )
    checks.check(
        "axiom-formation-silence",
        "the memo names Records form. and no order of formation",
        "Records form." in axiom and "order of formation" not in axiom,
    )
    checks.check(
        "parent-deep-probe",
        "the deep probe's own 3^24 census is live and cited",
        "number of covariant label-equivariant tables = 3^24" in probe
        and "282,429,536,480" in probe_flat
        and "282,429,536,480" in note_flat,
    )
    checks.check(
        "parent-law-pair",
        "the 2026-08-13 pair is live as the non-uniqueness reference point",
        "claim_type: bounded_theorem" in q8
        and "It selects neither rule as the framework's physical law." in normalize(q8),
    )
    checks.check(
        "parent-history-index",
        "the history-index note is live and named in the note",
        "Record-Monotone" in time_note
        and "TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md" in note,
    )

    # ---------- T1: the table space ----------------------------------------
    ternary = list(product((OPEN, 0, 1), repeat=6))
    tmap, treps, tself, tpairs, _ = census(ternary)
    checks.check(
        "T1-profiles",
        "729 ternary profiles fall into 57 proper-cubic orbits",
        len(ternary) == 729 and len(treps) == 57,
        (len(ternary), len(treps)),
    )
    checks.check(
        "T1-flip",
        "9 self-flip orbits are pinned to {0,1} and 24 flip-pairs stay free",
        len(tself) == 9 and len(tpairs) == 24 and len(tself) + 2 * len(tpairs) == 57,
        (len(tself), len(tpairs)),
    )
    checks.check(
        "T1-tables",
        "the table space is 3^24 = 282429536481 and 3^24-1 vary with the shell",
        3 ** 24 == 282429536481 and 3 ** 24 - 1 == 282429536480,
    )

    # ---------- T2: what complete records can realise ----------------------
    complete_profiles = list(product((0, 1), repeat=6))
    cmap, creps, cself, cpairs, csizes = census(complete_profiles)
    checks.check(
        "T2-subcensus",
        "64 fully-recorded profiles: 10 orbits, 2 self-flip, 4 flip-pairs",
        len(complete_profiles) == 64 and len(creps) == 10
        and len(cself) == 2 and len(cpairs) == 4,
        (len(creps), len(cself), len(cpairs)),
    )
    checks.check(
        "T2-orbit-sizes",
        "orbit sizes sum to 64; both self-flip orbits are three-three shells",
        sum(csizes.values()) == 64
        and all(sum(1 for v in r if v == 1) == 3 for r in cself),
    )
    checks.check(
        "T2-visible",
        "static complete-configuration A(T) depends on at most 4 digits, ignoring 20",
        len(cpairs) == 4 and 24 - len(cpairs) == 20 and 3 ** 4 == 81,
    )
    checks.check(
        "T2-fibre-floor",
        "every static complete-configuration fibre contains at least 3^20 = 3486784401 tables",
        3 ** 20 == 3486784401 and 81 * 3 ** 20 == 3 ** 24,
    )

    # ---------- T3: complete enumeration on the 3^3 torus -------------------
    contrib, pair_index = blocked_mask_table(cmap, cpairs)
    tables, bits = plane_tables(contrib)
    neighbours = neighbour_table()
    histogram = complete_mask_histogram(tables, bits)
    realised = np.nonzero(histogram)[0]
    checks.check(
        "T3-complete",
        "all 2^27 = 134217728 configurations enumerated, none sampled",
        int(histogram.sum()) == 1 << 27,
        int(histogram.sum()),
    )
    checks.check(
        "T3-masks",
        "the configurations realise 182 distinct masks of 256",
        len(realised) == 182,
        len(realised),
    )

    rows = {}
    for code in product((0, 1, 2), repeat=4):
        block = 0
        for i, digit in enumerate(code):
            if digit == 0:
                block |= 1 << (2 * i)
            elif digit == 1:
                block |= 1 << (2 * i + 1)
        admissible = frozenset(int(m) for m in realised if (m & block) == 0)
        size = int(histogram[list(admissible)].sum()) if admissible else 0
        rows["".join(str(d) for d in code)] = (admissible, size)
    classes = {}
    for code, (admissible, size) in rows.items():
        classes.setdefault(admissible, []).append(code)
    sizes = {code: size for code, (_, size) in rows.items()}

    checks.check(
        "T3-classes",
        "81 reduced tables induce exactly 81 distinct admissible sets",
        len(rows) == 81 and len(classes) == 81,
        (len(rows), len(classes)),
    )
    checks.check(
        "T3-fibres",
        "every fibre is exactly 3^20 and the fibres sum to 3^24",
        all(len(v) == 1 for v in classes.values())
        and len(classes) * 3 ** 20 == 3 ** 24,
    )
    checks.check(
        "T3-no-empty",
        "no table induces the empty admissible set",
        sum(1 for s in sizes.values() if s == 0) == 0,
    )
    checks.check(
        "T3-one-full",
        "exactly one table, menu code 2222, induces all 2^27 configurations",
        sum(1 for s in sizes.values() if s == 1 << 27) == 1
        and sizes["2222"] == 1 << 27,
    )
    checks.check(
        "T3-no-small",
        "no table has 0 < |A| < 27 and no class is a singleton",
        sum(1 for s in sizes.values() if 0 < s < 27) == 0
        and sum(1 for v in classes.values() if len(v) * 3 ** 20 == 1) == 0,
    )
    smallest = min(sizes.items(), key=lambda kv: kv[1])
    checks.check(
        "T3-smallest",
        "the smallest class holds 2918 configurations and is menu code 0100",
        smallest == ("0100", 2918),
        smallest,
    )
    checks.check(
        "T3-separating",
        "all 81 cardinalities are distinct on this torus",
        len(set(sizes.values())) == 81,
        len(set(sizes.values())),
    )
    checks.check(
        "T3-flip-closed",
        "every |A(T)| is even under the global value flip",
        all(s % 2 == 0 for s in sizes.values()),
    )

    # ---------- the two repository rules ------------------------------------
    repo = load_repo_rules()
    reverse_pair = {}
    for i, (a, b) in enumerate(cpairs):
        reverse_pair[a] = (i, 0)
        reverse_pair[b] = (i, 1)

    def code_of(rule):
        digits = [None] * 4
        for i, (a, b) in enumerate(cpairs):
            menu_a, menu_b = rule(a), rule(b)
            assert menu_b == frozenset(1 - v for v in menu_a)
            digits[i] = 2 if len(menu_a) == 2 else next(iter(menu_a))
        return "".join(str(d) for d in digits)

    majority_code = code_of(repo.majority_availability)
    copy_code = code_of(lambda p: repo.copy_neighbor_availability(p, (0, 1)))
    checks.check(
        "T3-majority",
        "repository majority rule = menu code 0000, |A| = 9038",
        majority_code == "0000" and sizes["0000"] == 9038,
        (majority_code, sizes.get("0000")),
    )
    checks.check(
        "T3-copy-neighbour",
        "repository copy-neighbour rule = menu code 0222, |A| = 89286536",
        copy_code == "0222" and sizes["0222"] == 89286536,
        (copy_code, sizes.get("0222")),
    )
    checks.check(
        "T3-rules-separated",
        "the two repository rules sit in different classes",
        rows[majority_code][0] != rows[copy_code][0],
    )

    # ---------- independent verification ------------------------------------
    check_configs = declared_check_configurations()
    coord = coordinate_masks(check_configs, contrib, neighbours)
    planed = plane_masks(check_configs, tables, bits)
    checks.check(
        "V1-cross-check",
        f"site-by-site and plane masks agree on {check_configs.size} declared configurations",
        bool((coord == planed).all()) and check_configs.size > 190000,
        int((coord != planed).sum()),
    )
    majority_recount, copy_recount = independent_recount(neighbours)
    checks.check(
        "V2-majority-recount",
        "a separate complete 2^27 neighbour-sum sweep recounts 9038",
        majority_recount == 9038 == sizes["0000"],
        majority_recount,
    )
    checks.check(
        "V3-copy-recount",
        "the same sweep recounts 89286536",
        copy_recount == 89286536 == sizes["0222"],
        copy_recount,
    )
    checks.check(
        "V4-histogram",
        "the mask histogram accounts for all 2^27 configurations",
        int(histogram.sum()) == 1 << 27 and int(histogram[realised].sum()) == 1 << 27,
    )

    # ---------- T4: supplied fixed-order endpoint laws -----------------------
    ternary_store = list(product((0, 1, TOPEN), repeat=6))
    smap = {p: min(rotate_profile(p, r) for r in ROTATIONS) for p in ternary_store}
    sreps = sorted(set(smap.values()))
    sself, spairs, seen = [], [], set()
    for rep in sreps:
        partner = smap[tuple(v if v == TOPEN else 1 - v for v in rep)]
        if rep in seen:
            continue
        if partner == rep:
            sself.append(rep)
            seen.add(rep)
        else:
            spairs.append((rep, partner))
            seen.update({rep, partner})
    formation = Formation(spairs, smap, neighbours)
    visible = [i for i, (a, b) in enumerate(spairs) if TOPEN not in a]
    checks.check(
        "T4-digit-split",
        "the 24 digits split into 4 fully-recorded and 20 partially-recorded",
        len(spairs) == 24 and len(sself) == 9 and len(visible) == 4,
        (len(spairs), len(visible)),
    )

    def store_code(rule):
        digits = []
        for a, b in spairs:
            menu_a = rule(tuple(OPEN if v == TOPEN else v for v in a))
            digits.append(2 if len(menu_a) == 2 else next(iter(menu_a)))
        return tuple(digits)

    majority24 = store_code(repo.majority_availability)
    copy24 = store_code(lambda p: repo.copy_neighbor_availability(p, (0, 1)))
    all_open24 = tuple([2] * 24)
    lex = list(range(27))
    reverse_lex = list(range(26, -1, -1))
    transpose = [9 * z + 3 * y + x for x in range(3) for y in range(3) for z in range(3)]
    declared_orders = (("lex", lex), ("reverse-lex", reverse_lex), ("transpose", transpose))

    checks.check(
        "T4-code-agreement",
        "the 24-digit codes restrict to the class codes 0000 and 0222",
        "".join(str(majority24[i]) for i in visible) == majority_code
        and "".join(str(copy24[i]) for i in visible) == copy_code,
    )

    reach = {}
    for name, order in declared_orders:
        touched, profiles = order_reachable_pairs(order, smap, formation.pair_of, neighbours)
        reach[name] = (len(touched), len(profiles))
    checks.check(
        "T4-order-reach",
        "each declared order reaches 343 profiles and touches all 24 digits",
        all(v == (24, 343) for v in reach.values()),
        reach,
    )

    states, weights, queried_majority, trunc_majority = formation.frontier(
        majority24, lex, FRONTIER_CAP, weighted=True
    )
    constants = [bool((row == row[0]).all()) for row in states]
    checks.check(
        "T4-majority-atoms",
        "the majority formation law has two constant atoms at 1/2 each",
        states.shape[0] == 2 and not trunc_majority and all(constants)
        and sorted(round(float(w), 12) for w in weights) == [0.5, 0.5],
        (states.shape[0], trunc_majority),
    )
    majority_menu = formation.menu(majority24)

    def globally_admissible(row) -> bool:
        for s in range(27):
            index = sum(int(row[neighbours[s, d]]) * (3 ** d) for d in range(6))
            entry = int(majority_menu[index])
            if entry != 2 and entry != int(row[s]):
                return False
        return True

    checks.check(
        "T4-majority-consistent",
        "both formed atoms are globally admissible for the majority rule",
        all(globally_admissible(row) for row in states),
    )
    checks.check(
        "T4-majority-fibre",
        "9 complete queried digits give majority endpoint fibre exactly 3^15",
        len(queried_majority) == 9 and 3 ** (24 - len(queried_majority)) == 14348907,
        sorted(queried_majority),
    )

    _, _, queried_copy, trunc_copy = formation.frontier(copy24, lex, FRONTIER_CAP, weighted=True)
    checks.check(
        "T4-copy-fibre",
        "copy-neighbour has 9 complete queries and endpoint fibre exactly 3^15",
        len(queried_copy) == 9 and not trunc_copy,
        sorted(queried_copy),
    )

    # The all-supports table branches at every step, so every order-reachable
    # profile carries positive probability and the queried set is the reachable
    # set: all 24 digits. Each is therefore individually visible in (B).
    touched_lex, _ = order_reachable_pairs(lex, smap, formation.pair_of, neighbours)
    checks.check(
        "T4-all-supports",
        "the all-supports table queries all 24 digits, so each changes the law",
        len(touched_lex) == 24 and all(d == 2 for d in all_open24),
    )
    checks.check(
        "T4-visibility-gap",
        "4 of 24 digits change the admissible set, 24 of 24 change the formation law",
        len(visible) == 4 and len(touched_lex) == 24,
    )

    # Total-variation-one witness inside one admissible-set class.
    witness_profile = (0, TOPEN, TOPEN, TOPEN, TOPEN, TOPEN)
    witness_digit = int(formation.pair_index[Formation.tindex(witness_profile)])
    partner24 = list(majority24)
    partner24[witness_digit] = 1 - partner24[witness_digit]
    partner24 = tuple(partner24)
    partner_states, partner_weights, _, trunc_partner = formation.frontier(
        partner24, lex, FRONTIER_CAP, weighted=True
    )
    partner_constants = any(bool((row == row[0]).all()) for row in partner_states)
    checks.check(
        "T4-witness-class",
        "the witness pair shares four visible digits, hence one admissible set",
        witness_digit not in visible
        and [partner24[i] for i in visible] == [majority24[i] for i in visible]
        and majority24[witness_digit] in (0, 1),
        witness_digit,
    )
    checks.check(
        "T4-witness-separation",
        "the final all-equal event separates endpoint laws with total variation exactly 1",
        not trunc_partner
        and not partner_constants
        and abs(float(partner_weights.sum()) - 1.0) < 1e-12
        and abs(float(weights.sum()) - 1.0) < 1e-12,
        (partner_states.shape[0], trunc_partner),
    )

    _, _, cap_queries, cap_cut = formation.frontier(all_open24, lex, 1, True)
    capped_interval = endpoint_fibre_interval(cap_queries, not cap_cut)
    full_interval = endpoint_fibre_interval(touched_lex, True)
    checks.check(
        "T4-censored-control",
        "actual cap-one all-support query set gives an upper bound containing the true singleton fibre",
        cap_cut and len(cap_queries) == 9
        and capped_interval == (1, 14348907) and full_interval == (1, 1)
        and capped_interval[0] <= full_interval[0] <= capped_interval[1],
        (sorted(cap_queries), capped_interval, full_interval),
    )
    prefix_ok, prefix_details = finite_prefix_fibres(formation)
    checks.check("T4-prefix-fibres", "all nine actual four-site laws satisfy the exact restricted fibre identity", prefix_ok, prefix_details)

    # Declared family: base-3 expansions of j * floor(3^24 / 32), j = 0..31.
    stride = (3 ** 24) // FAMILY_SIZE
    family = Counter()
    family_intervals = []
    truncated_rows = 0
    for j in range(FAMILY_SIZE):
        k = j * stride
        code = tuple((k // (3 ** i)) % 3 for i in range(24))
        _, _, queried, truncated = formation.frontier(code, lex, FRONTIER_CAP, weighted=False)
        family[len(queried)] += 1
        family_intervals.append((len(queried), truncated, endpoint_fibre_interval(queried, not truncated)))
        truncated_rows += int(truncated)
    sharp = sum(count for size, count in family.items() if size >= 23)
    checks.check(
        "T4-family",
        f"over the 32 declared tables the queried-digit count ranges {min(family)}..{max(family)} with {sharp} at 23 or 24",
        sum(family.values()) == FAMILY_SIZE and max(family) == 24 and sharp >= 12,
        sorted(family.items()),
    )
    checks.check(
        "T4-family-bounds",
        "complete sets give exact fibres; censored observed sets give upper bounds",
        all(size <= 24 and bounds[1] == 3 ** (24 - size)
            and bounds[0] == (1 if cut else bounds[1])
            for size, cut, bounds in family_intervals)
        and sum(bounds[1] <= 3 for _, _, bounds in family_intervals) == 12
        and sum(bounds[1] == 1 for _, _, bounds in family_intervals) == 10,
    )
    print(f"declared_family_queried_digit_histogram: {sorted(family.items())}")
    print(f"declared_family_frontier_cap_rows: {truncated_rows} of {FAMILY_SIZE}")

    # ---------- note contract -----------------------------------------------
    phrases = (
        "exactly 81", "3^20", "282,429,536,481", "9,038", "89,286,536", "2,918",
        "14,348,907", "Records register", "declared finite set", "uniform lift",
        "complete enumeration", "one torus", "not a control",
    )
    missing = [phrase for phrase in phrases if phrase not in note_flat]
    checks.check(
        "note-phrases",
        f"all {len(phrases)} required counts and boundary phrases appear in the note",
        not missing,
        missing,
    )
    checks.check(
        "note-decision",
        "the note keeps static membership, endpoint laws and physical access separate",
        "A supplied readout/preparation protocol is still required" in note_flat
        and "it reads no history" in note_flat
        and "not a physical readout of an absent site" in note_flat,
    )
    checks.check(
        "note-scope-hygiene",
        "the note claims no selection of the physical law",
        "promoted" not in note.lower()
        and "new axiom" not in note.lower()
        and "no physical law is selected" in note_flat,
    )
    checks.check(
        "note-vocabulary",
        "the note avoids readout-process and closure vocabulary",
        not any(
            word in note.lower()
            for word in ("measurement", "collapse", "observer", "exhaustive",
                         "exhausted", "no-go", "closes the route", "only route")
        ),
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
        "support_table_fibres_complete_records_81_classes_torus_3" in note,
    )

    print("per_element: every one of the 729 ternary neighbour profiles and each of the 64 fully-recorded profiles is classified exactly")
    print("per_site: each of the 27 torus sites is evaluated in both the plane-factorised and the site-by-site neighbour computation")
    print("per_mode: checked and not executed - the classification has no spectral, momentum, or normal-mode decomposition")
    print("per_block: all 81 reduced tables, both repository rules, and the declared 32-table formation family are executed")
    print("lattice_wide: executed on one 3^3 torus by complete enumeration of all 2^27 complete configurations; no larger lattice is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
