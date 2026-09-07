#!/usr/bin/env python3
"""Exact checks: the formation law of the monotone-order class on rectangles.

Scope.  Block 02 solved the row sweep on strips (every row the path chain p_0, the row kernel P, p_0 P = p_0).  Here the
whole class of monotone orders (the linear extensions of the product partial order on an n x W rectangle) is shown to give
ONE formation law mu_P (P1, for every rule), whose two-neighbor factor is the bridge of a two-step K-chain (P2), which is
transpose-symmetric (P3), whose rows AND columns are K-chains (P4), and whose every 2 x 2 block carries the corner law
pi(c, b, a, d) = (1/6) K(c,a) K(c,b) K(a,d) K(d,b) / K^2(a,b) with a, b independent given the corner c (P5).  From P5, no
staircase with a turn is a Markov chain (P6; the minimal staircase's conditional 227/858 against 1/4 at (3,1,2)); the
mirror class gives a different law and the snake keeps the rows but loses the columns (P7; the snake proper on 3 x 3 has
column 0 a chain and columns 1, 2 not, on 4 x 3 no column a chain).  All marginals are computed by projected row transfers
with integer numerators over common denominators; every comparison is an exact rational identity; the runner scans its own
source for floating-point literals and conversion calls.  No order is selected as physical.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import lcm
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
BLOCK01_PATH = ROOT / AUDIT_INPUT_PATHS[2]
BLOCK02_PATH = ROOT / AUDIT_INPUT_PATHS[3]
CLAIM_ID = "admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "FORMATION law of a rule for a formation order"
BLOCK02_CLAIM_ID = "admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06"
BLOCK02_FRAGMENT = "p_0 P = p_0"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "extension_count_wrong": "B",
    "recorded_set_forged": "B",
    "nonmonotone_order_accepted": "B",
    "antidiagonal_sweep_accepted": "B",
    "bridge_identity_broken": "C",
    "transpose_symmetry_broken": "C",
    "product_formula_mismatch": "C",
    "asymmetric_bridge_symmetry_forged": "C",
    "column_chain_forged": "D",
    "corner_law_wrong_denominator": "D",
    "corner_independence_forged": "D",
    "diagonal_pair_law_wrong": "D",
    "row_kernel_wrong": "D",
    "staircase_claimed_chain": "E",
    "mirror_law_equal_claimed": "E",
    "snake_column_claimed_chain": "E",
    "snake_row_kernel_not_invariant": "E",
    "minimal_staircase_conditional_off": "E",
    "constant_rule_defect_claimed": "E",
    "claim_static_equals_formation": "F",
    "claim_all_orders_same_law": "F",
    "claim_staircases_chains": "F",
    "claim_unilateral-field_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def dec(x: Fraction, digits: int) -> str:
    """Exact decimal expansion rounded down; integer arithmetic; a label, not evidence."""
    sign = "-" if x < 0 else ""
    x = abs(x)
    scaled = (x.numerator * 10 ** digits) // x.denominator
    s = str(scaled).rjust(digits + 1, "0")
    return f"{sign}{s[:-digits]}.{s[-digits:]}"


# --------------------------------------------------------------------- menu and rule (rebuilt, not imported)
MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
TRIPLES = ((3, 1, 2), (5, 2, 4))
CONSTANT = (2, 2, 2)


def orbit(a: int, b: int) -> int:
    d = sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))
    return 0 if d == 1 else (1 if d == -1 else 2)


def phi_table(triple):
    return [[triple[orbit(a, b)] for b in range(M)] for a in range(M)]


def phi_asymmetric():
    """Block 02's asymmetric control: phi(a, b) = phi_(3,1,2)(a, b) + [a < b]."""
    base = phi_table((3, 1, 2))
    return [[base[a][b] + (1 if a < b else 0) for b in range(M)] for a in range(M)]


class Kernels:
    """K(a -> s) = phi(s, a)/Z_1 (symmetric phi), K^2, and the integer forms used by the transfers."""

    def __init__(self, phi) -> None:
        self.phi = phi
        self.Z1 = sum(phi[0])
        self.K = [[Fraction(phi[b][a], self.Z1) for b in range(M)] for a in range(M)]
        self.K2n = [[sum(phi[a][s] * phi[s][b] for s in range(M)) for b in range(M)] for a in range(M)]
        self.K2 = [[Fraction(self.K2n[a][b], self.Z1 ** 2) for b in range(M)] for a in range(M)]
        self.L = lcm(*sorted({x for line in self.K2n for x in line}))
        self.mult = [[self.L // self.K2n[a][b] for b in range(M)] for a in range(M)]

    def bridge(self, s: int, a: int, b: int) -> Fraction:
        return self.K[a][s] * self.K[s][b] / self.K2[a][b]

    def corner(self, c: int, b: int, a: int, d: int) -> Fraction:
        """The corner law pi(c, b, a, d) on a 2 x 2 block: top-left c, top-right b, bottom-left a, bottom-right d."""
        K = self.K
        return Fraction(1, 6) * K[c][a] * K[c][b] * K[a][d] * K[d][b] / self.K2[a][b]

    def chain(self, values) -> Fraction:
        p = Fraction(1, 6)
        for u, v in zip(values, values[1:]):
            p *= self.K[u][v]
        return p


def row_states(W: int):
    return list(product(range(M), repeat=W))


def p0_num(ker: Kernels, W: int):
    """The path chain p_0 on rows of width W: integer numerators over 6 Z_1^(W-1)."""
    nums = []
    for rho in row_states(W):
        n = 1
        for j in range(1, W):
            n *= ker.phi[rho[j - 1]][rho[j]]
        nums.append(n)
    return nums, 6 * ker.Z1 ** (W - 1)


def row_kernel_num(ker: Kernels, W: int, direction: str):
    """Block 02's row-to-row kernel P(beta -> alpha), rebuilt with integer numerators over Z_1 L^(W-1): the first site of
    the row (column 0 for 'lr', column W-1 for 'rl') has the single recorded neighbor above it, every later site has its
    in-row predecessor and the site above, whose factor is the bridge phi(s,a) phi(s,b)/K2n(a,b) (E1, E2)."""
    phi, mult = ker.phi, ker.mult
    rows = row_states(W)
    mat = []
    for b in rows:
        line = []
        for a in rows:
            if direction == "lr":
                num = phi[b[0]][a[0]]
                for j in range(1, W):
                    num *= phi[a[j - 1]][a[j]] * phi[a[j]][b[j]] * mult[a[j - 1]][b[j]]
            else:
                num = phi[b[W - 1]][a[W - 1]]
                for j in range(W - 2, -1, -1):
                    num *= phi[a[j + 1]][a[j]] * phi[a[j]][b[j]] * mult[a[j + 1]][b[j]]
            line.append(num)
        mat.append(line)
    return mat, ker.Z1 * ker.L ** (W - 1)


def _key_order(sites, grouped):
    return [grouped.index(site) for site in sites]


def three_row_marginal(p0, P01, P12, W: int, sites):
    """Marginal of p_0(r0) P01(r0 -> r1) P12(r1 -> r2) on `sites` (pairs (i, j), i in 0..2) by the middle-row contraction:
    U[s0][r1] = sum over r0 agreeing with s0 on the row-0 selection of p_0(r0) P01(r0, r1); V[s2][r1] = sum over r2 agreeing
    with s2 on the row-2 selection of P12(r1, r2); m(s0, s1, s2) = sum over r1 agreeing with s1 of U[s0][r1] V[s2][r1].
    Integer numerators throughout; the result is a dict from the value tuple (in the order of `sites`) to a Fraction."""
    (p0n, p0d), (Pa, Pad), (Pb, Pbd) = p0, P01, P12
    rows = row_states(W)
    R = len(rows)
    S = [[j for (i, j) in sites if i == k] for k in range(3)]
    proj = [[tuple(r[j] for j in S[k]) for r in rows] for k in range(3)]
    U: dict = {}
    for i0 in range(R):
        w0 = p0n[i0]
        if w0 == 0:
            continue
        acc = U.setdefault(proj[0][i0], [0] * R)
        line = Pa[i0]
        for i1 in range(R):
            acc[i1] += w0 * line[i1]
    V: dict = {}
    p2 = proj[2]
    for i1 in range(R):
        line = Pb[i1]
        for i2 in range(R):
            acc = V.get(p2[i2])
            if acc is None:
                acc = V[p2[i2]] = [0] * R
            acc[i1] += line[i2]
    out: dict = {}
    for i1 in range(R):
        s1 = proj[1][i1]
        for s0, u in U.items():
            x = u[i1]
            if x == 0:
                continue
            for s2, v in V.items():
                if v[i1]:
                    key = s0 + s1 + s2
                    out[key] = out.get(key, 0) + x * v[i1]
    grouped = [(k, j) for k in range(3) for j in S[k]]
    order = _key_order(sites, grouped)
    den = p0d * Pad * Pbd
    return {tuple(k[t] for t in order): Fraction(v, den) for k, v in out.items()}


def n_row_marginal(p0, kernels, W: int, sites):
    """Marginal of p_0(r0) prod_i kernels[i](r_i -> r_(i+1)) on `sites` by the column-projected row transfer: the state
    after row i is the dict (values of the selected sites in rows < i, the full row state r_i) -> integer weight; the last
    row enters only through Q[r][sel] = sum of its kernel over the row states agreeing with sel on the last row's
    selection.  Used for two-row and four-row rectangles (the snake on 4 x 3); three-row rectangles use the middle-row
    contraction, and the two agree where both apply (checked)."""
    p0n, p0d = p0
    rows = row_states(W)
    R = len(rows)
    n = len(kernels) + 1
    S = [[j for (i, j) in sites if i == k] for k in range(n)]
    proj = [[tuple(r[j] for j in S[k]) for r in rows] for k in range(n)]
    state = {((), r): p0n[r] for r in range(R) if p0n[r]}
    den = p0d
    for i in range(n - 1):
        Pn, Pd = kernels[i]
        den *= Pd
        if i == n - 2:
            last = proj[n - 1]
            Q: list = []
            for r in range(R):
                q: dict = {}
                line = Pn[r]
                for r2 in range(R):
                    q[last[r2]] = q.get(last[r2], 0) + line[r2]
                Q.append(q)
            out: dict = {}
            for (carried, r), w in state.items():
                c2 = carried + proj[i][r]
                for sel, q in Q[r].items():
                    out[c2 + sel] = out.get(c2 + sel, 0) + w * q
            state = out
        else:
            new: dict = {}
            for (carried, r), w in state.items():
                c2 = carried + proj[i][r]
                line = Pn[r]
                for r2 in range(R):
                    x = line[r2]
                    if x:
                        key = (c2, r2)
                        new[key] = new.get(key, 0) + w * x
            state = new
    grouped = [(k, j) for k in range(n) for j in S[k]]
    order = _key_order(sites, grouped)
    return {tuple(k[t] for t in order): Fraction(v, den) for k, v in state.items()}


def tv(law: dict, target) -> Fraction:
    """Total variation between a computed marginal and a target given as a function of the value tuple."""
    keys = set(law)
    return sum(abs(law.get(k, 0) - target(k)) for k in keys) / 2


# --------------------------------------------------------------------- block 01's formation law from its definition
def rule_function(kind: str, phi):
    """r(s | recorded values): the product rule prod_y phi(s, eta_y) or the sum rule sum_y phi(s, eta_y); r(s | none) = 1/6."""

    @lru_cache(maxsize=None)
    def r(s: int, recorded: tuple) -> Fraction:
        if kind == "product":
            w = []
            for t in range(M):
                acc = 1
                for y in recorded:
                    acc *= phi[t][y]
                w.append(acc)
        else:
            w = [sum(phi[t][y] for y in recorded) if recorded else 1 for t in range(M)]
        return Fraction(w[s], sum(w))

    return r


def neighbors(n: int, W: int, i: int, j: int):
    return [(a, b) for (a, b) in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)) if 0 <= a < n and 0 <= b < W]


def recorded_sets(n: int, W: int, order):
    """A_k for every site of the order: its neighbors that formed earlier (block 01's definition)."""
    pos = {site: k for k, site in enumerate(order)}
    return {(i, j): tuple(sorted(nb for nb in neighbors(n, W, i, j) if pos[nb] < pos[(i, j)])) for (i, j) in order}


def formation_law(n: int, W: int, order, r) -> dict:
    """mu_sigma(v) = prod_k r(v_(x_k) | v on A_k) on every configuration of the n x W rectangle (site (i, j) at i W + j)."""
    rec = recorded_sets(n, W, order)
    plan = [(i * W + j, tuple(a * W + b for (a, b) in rec[(i, j)])) for (i, j) in order]
    law = {}
    for conf in product(range(M), repeat=n * W):
        p = Fraction(1)
        for idx, nb in plan:
            p *= r(conf[idx], tuple(conf[t] for t in nb))
        law[conf] = p
    return law


def marginal(law: dict, n: int, W: int, sites) -> dict:
    out: dict = {}
    idx = [i * W + j for (i, j) in sites]
    for conf, p in law.items():
        key = tuple(conf[t] for t in idx)
        out[key] = out.get(key, 0) + p
    return out


def transpose_conf(conf, n: int, W: int):
    return tuple(conf[i * W + j] for j in range(W) for i in range(n))


# --------------------------------------------------------------------- the monotone class
def left_above(n: int, W: int, i: int, j: int):
    return tuple(sorted(s for s in ((i, j - 1), (i - 1, j)) if s[0] >= 0 and s[1] >= 0))


def is_extension(n: int, W: int, order) -> bool:
    pos = {site: k for k, site in enumerate(order)}
    return len(pos) == n * W and all(pos[s] < pos[(i, j)] for (i, j) in order for s in left_above(n, W, i, j))


def linear_extensions(n: int, W: int):
    """Every linear extension of the product order on the n x W rectangle, by recursion on the next admissible site."""
    sites = [(i, j) for i in range(n) for j in range(W)]
    out = []

    def rec(chosen, chosen_set):
        if len(chosen) == len(sites):
            out.append(tuple(chosen))
            return
        for s in sites:
            if s not in chosen_set and all(t in chosen_set for t in left_above(n, W, *s)):
                chosen.append(s)
                chosen_set.add(s)
                rec(chosen, chosen_set)
                chosen.pop()
                chosen_set.discard(s)

    rec([], set())
    return out


def count_extensions(n: int, W: int) -> int:
    """The number of linear extensions by memoized recursion on the set of formed sites (a bitmask)."""
    sites = [(i, j) for i in range(n) for j in range(W)]
    bit = {s: 1 << k for k, s in enumerate(sites)}
    full = (1 << len(sites)) - 1

    @lru_cache(maxsize=None)
    def rec(mask: int) -> int:
        if mask == full:
            return 1
        total = 0
        for s in sites:
            if not mask & bit[s] and all(mask & bit[t] for t in left_above(n, W, *s)):
                total += rec(mask | bit[s])
        return total

    return rec(0)


def row_order(n: int, W: int):
    return [(i, j) for i in range(n) for j in range(W)]


def column_order(n: int, W: int):
    return [(i, j) for j in range(W) for i in range(n)]


def antidiagonal_sweep(n: int, W: int):
    """The sweep by increasing i + j (within a level by i): a linear extension."""
    return sorted(row_order(n, W), key=lambda s: (s[0] + s[1], s[0]))


def diagonal_sweep(n: int, W: int, sign: int):
    """The sweep by increasing i - j (sign = +1) or j - i (sign = -1), ties by i: NOT a linear extension."""
    return sorted(row_order(n, W), key=lambda s: (sign * (s[0] - s[1]), s[0]))


def snake_order(n: int, W: int):
    """Rows in order; row 0 left to right, row 1 right to left, and so on."""
    out = []
    for i in range(n):
        cols = range(W) if i % 2 == 0 else range(W - 1, -1, -1)
        out.extend((i, j) for j in cols)
    return out


def mirror_order(n: int, W: int):
    """The left-right mirror of the row sweep: rows in order, each right to left (the corner class of the top-right)."""
    return [(i, j) for i in range(n) for j in range(W - 1, -1, -1)]


def product_formula_num(ker: Kernels, n: int, W: int, conf) -> int:
    """P2's product formula as an integer numerator over 6 Z_1^((W-1)+(n-1)) L^((W-1)(n-1)): the first row and the first
    column are K-chains, every other site carries the bridge of its left and above neighbors."""
    phi, mult = ker.phi, ker.mult
    num = 1
    for j in range(1, W):
        num *= phi[conf[j - 1]][conf[j]]
    for i in range(1, n):
        num *= phi[conf[(i - 1) * W]][conf[i * W]]
    for i in range(1, n):
        for j in range(1, W):
            s, a, b = conf[i * W + j], conf[i * W + j - 1], conf[(i - 1) * W + j]
            num *= phi[s][a] * phi[s][b] * mult[a][b]
    return num


def product_formula_den(ker: Kernels, n: int, W: int) -> int:
    return 6 * ker.Z1 ** ((W - 1) + (n - 1)) * ker.L ** ((W - 1) * (n - 1))


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b01_text: str, b02_text: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4, "the four declared audit inputs exist")
    checks.check("A2", all(n in normalize_text(axiom_text) for n in AXIOM_NEEDLES), "axiom memo: the Admissibility and Record sentences verbatim")
    checks.check("A3", BLOCK01_CLAIM_ID in b01_text and BLOCK01_FRAGMENT in normalize_text(b01_text), "block 01's note: claim id and the formation-law fragment")
    checks.check("A4", BLOCK02_CLAIM_ID in b02_text and BLOCK02_FRAGMENT in normalize_text(b02_text), "block 02's note: claim id and the invariance fragment p_0 P = p_0")
    checks.check("A5", CLAIM_ID in note_text, "this note carries its claim id")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    exts = {(n, W): linear_extensions(n, W) for (n, W) in ((2, 3), (3, 3), (3, 4))}
    counts = {k: len(v) for k, v in exts.items()}
    counts[(4, 4)] = count_extensions(4, 4)
    expected = {(2, 3): 5, (3, 3): 42, (3, 4): 462, (4, 4): 24024}
    if mut("extension_count_wrong"):
        expected[(3, 4)] = 461
    checks.check("B1", counts == expected and all(count_extensions(n, W) == counts[(n, W)] for (n, W) in exts), f"linear extensions: {counts[(2,3)]}, {counts[(3,3)]}, {counts[(3,4)]}, {counts[(4,4)]} for 2x3, 3x3, 3x4, 4x4 (enumerated and counted)")
    sets_ok = True
    for (n, W), lst in exts.items():
        for e in lst:
            rec = recorded_sets(n, W, e)
            for (i, j), A in rec.items():
                target = left_above(n, W, i, j)
                if mut("recorded_set_forged"):
                    target = tuple(sorted(s for s in ((i, j - 1),) if s[1] >= 0))
                if A != target:
                    sets_ok = False
    checks.check("B2", sets_ok, f"every site of every extension ({sum(counts[k] for k in exts)} orders) forms with exactly its left and above neighbors")
    laws_ok, one_law = True, {}
    for tr in TRIPLES:
        r = rule_function("product", phi_table(tr))
        laws = [formation_law(2, 3, e, r) for e in exts[(2, 3)]]
        laws_ok = laws_ok and all(l == laws[0] for l in laws)
        one_law[tr] = laws[0]
    report["muP_2x3"] = one_law
    checks.check("B3", laws_ok, "P1 executed: the 5 extensions of 2x3 give one formation law on all 46656 configurations at both declared triples")
    other_ok = True
    for kind, phi in (("sum", phi_table((3, 1, 2))), ("product", phi_asymmetric())):
        r = rule_function(kind, phi)
        laws = [formation_law(2, 3, e, r) for e in exts[(2, 3)]]
        other_ok = other_ok and all(l == laws[0] for l in laws)
        report[f"law_2x3_{kind}_{'asym' if phi is not None and phi[0][1] != phi[1][0] else 'sym'}"] = laws[0]
    checks.check("B4", other_ok, "P1 for every rule: the sum rule and the asymmetric phi also give one law on the 5 extensions of 2x3")
    anti = antidiagonal_sweep(3, 3)
    diag_p, diag_m = diagonal_sweep(3, 3, +1), diagonal_sweep(3, 3, -1)
    rec_p, rec_m = recorded_sets(3, 3, diag_p), recorded_sets(3, 3, diag_m)
    anti_ok = is_extension(3, 3, anti) and tuple(anti) in set(exts[(3, 3)])
    diag_not = (not is_extension(3, 3, diag_p)) and (not is_extension(3, 3, diag_m)) and rec_p[(0, 1)] == ((0, 2),) and rec_m[(1, 0)] == ((2, 0),)
    if mut("antidiagonal_sweep_accepted"):
        diag_not = is_extension(3, 3, diag_p)
    checks.check("B5", anti_ok and diag_not, "the i+j sweep of 3x3 is a linear extension; the i-j and j-i sweeps are not: (0,1) records {(0,2)}, (1,0) records {(2,0)}")
    snake = snake_order(2, 3)
    rec_s = recorded_sets(2, 3, snake)
    snake_not = (not is_extension(2, 3, snake)) and rec_s[(1, 1)] == ((0, 1), (1, 2))
    if mut("nonmonotone_order_accepted"):
        snake_not = is_extension(2, 3, snake) or rec_s[(1, 1)] == left_above(2, 3, 1, 1)
    checks.check("B6", snake_not, "the snake on 2x3 is outside the class: site (1,1) records {(0,1), (1,2)}")


# ============================================================================================ family C
def family_c(checks: Checks, report: dict) -> None:
    ok = True
    for tr in TRIPLES:
        ker = Kernels(phi_table(tr))
        r = rule_function("product", ker.phi)
        for a in range(M):
            for b in range(M):
                for s in range(M):
                    rhs = ker.K[a][s] * ker.K[s][b] / (ker.K2[a][a] if mut("bridge_identity_broken") else ker.K2[a][b])
                    ok = ok and r(s, (a, b)) == rhs
    checks.check("C1", ok, "P2: r(s | a, b) = K(a->s) K(s->b) / K^2(a, b) on all 216 triples at (3,1,2) and (5,2,4)")
    ra = rule_function("product", phi_asymmetric())
    sym = all(ra(s, (a, b)) == ra((s + 1) % M if mut("asymmetric_bridge_symmetry_forged") else s, (b, a)) for a in range(M) for b in range(M) for s in range(M))
    checks.check("C2", sym, "r(s | a, b) = r(s | b, a) by the product form alone: executed on 216 triples for the asymmetric phi")
    trans_ok = True
    for tr in TRIPLES:
        r = rule_function("product", phi_table(tr))
        law23 = report["muP_2x3"][tr]
        law32 = formation_law(3, 2, row_order(3, 2), r)
        trans_ok = trans_ok and all(law23[c] == law32[c if mut("transpose_symmetry_broken") else transpose_conf(c, 2, 3)] for c in law23)
    ra_law23 = formation_law(2, 3, row_order(2, 3), ra)
    ra_law32 = formation_law(3, 2, row_order(3, 2), ra)
    trans_asym = all(ra_law23[c] == ra_law32[transpose_conf(c, 2, 3)] for c in ra_law23)
    checks.check("C3", trans_ok and trans_asym, "P3: mu_P(2x3)(v) = mu_P(3x2)(v^T) on all 46656 configurations at both triples and for the asymmetric phi")
    pf_ok = True
    for tr in TRIPLES:
        ker = Kernels(phi_table(tr))
        den = product_formula_den(ker, 2, 3)
        law = report["muP_2x3"][tr]
        for c, p in law.items():
            num = product_formula_num(ker, 2, 3, c)
            if mut("product_formula_mismatch"):
                num *= ker.mult[c[4]][c[1]]
            if Fraction(num, den) != p:
                pf_ok = False
                break
    checks.check("C4", pf_ok, "P2: the product formula (first row and column K-chains, bridges elsewhere) equals block 01's definition on 2x3 entrywise at both triples")
    ker = Kernels(phi_table((3, 1, 2)))
    p04, P4 = p0_num(ker, 4), row_kernel_num(ker, 4, "lr")
    p02, P2 = p0_num(ker, 2), row_kernel_num(ker, 2, "lr")
    rows4, rows2 = row_states(4), row_states(2)
    idx2 = {r: k for k, r in enumerate(rows2)}
    total, ok24 = 0, True
    for i0, r0 in enumerate(rows4):
        w0 = p04[0][i0]
        line = P4[0][i0]
        for i1, r1 in enumerate(rows4):
            lhs = w0 * line[i1]
            total += lhs
            c = [idx2[(r0[j], r1[j])] for j in range(4)]
            rhs = p02[0][c[0]] * P2[0][c[0]][c[1]] * P2[0][c[1]][c[2]] * P2[0][c[2]][c[3]]
            if lhs != rhs:
                ok24 = False
                break
        if not ok24:
            break
    den_ok = p04[1] * P4[1] == p02[1] * P2[1] ** 3 == product_formula_den(ker, 2, 4) and total == p04[1] * P4[1]
    checks.check("C5", ok24 and den_ok, "P3: mu_P(2x4)(v) = mu_P(4x2)(v^T) on all 1679616 configurations by the row-kernel form of the product formula (one denominator; sums to one)")


# ============================================================================================ family D
def family_d(checks: Checks, report: dict, exact: bool) -> None:
    kern_ok = True
    for tr in TRIPLES:
        ker = Kernels(phi_table(tr))
        r = rule_function("product", ker.phi)
        Pn, Pd = row_kernel_num(ker, 3, "rl" if mut("row_kernel_wrong") else "lr")
        rows = row_states(3)
        for ib, b in enumerate(rows):
            if sum(Pn[ib]) != Pd:
                kern_ok = False
            for ia, a in enumerate(rows):
                d = r(a[0], (b[0],)) * r(a[1], (a[0], b[1])) * r(a[2], (a[1], b[2]))
                if Fraction(Pn[ib][ia], Pd) != d:
                    kern_ok = False
                    break
            if not kern_ok:
                break
    checks.check("D1", kern_ok, "the row kernel P (block 02's E2, rebuilt) equals the definition entrywise on 216 x 216 at both triples; every row sums to one")
    data = {}
    for tr, W in (((3, 1, 2), 3), ((5, 2, 4), 3), ((3, 1, 2), 4)):
        ker = Kernels(phi_table(tr))
        p0, P = p0_num(ker, W), row_kernel_num(ker, W, "lr")
        cols = {j: three_row_marginal(p0, P, P, W, [(0, j), (1, j), (2, j)]) for j in range(W)}
        blocks = {(i, j): three_row_marginal(p0, P, P, W, [(i - 1, j - 1), (i - 1, j), (i, j - 1), (i, j)]) for i in (1, 2) for j in range(1, W)}
        rows_m = {i: three_row_marginal(p0, P, P, W, [(i, j) for j in range(W)]) for i in range(3)}
        data[(tr, W)] = (ker, p0, P, cols, blocks, rows_m)
    report["D"] = data
    col_ok = all(all(m[k] == (ker.chain((k[0], k[1])) * ker.K[k[0]][k[2]] if mut("column_chain_forged") else ker.chain(k)) for k in m) for (ker, _, _, cols, _, _) in data.values() for m in cols.values())
    checks.check("D2", col_ok, "P4: every column of 3x3 (both triples) and of 3x4 is the K-chain on its three-site joint (middle-row contraction)")
    row_ok = all(all(m[k] == ker.chain(k) for k in m) for (ker, _, _, _, _, rows_m) in data.values() for m in rows_m.values())
    ker2 = Kernels(phi_table((3, 1, 2)))
    law23 = report["muP_2x3"][(3, 1, 2)]
    two_ok = all(marginal(law23, 2, 3, [(0, j), (1, j)])[k] == Fraction(1, 6) * ker2.K[k[0]][k[1]] for j in range(3) for k in product(range(M), repeat=2)) and all(marginal(law23, 2, 3, [(i, 0), (i, 1), (i, 2)])[k] == ker2.chain(k) for i in range(2) for k in product(range(M), repeat=3))
    checks.check("D3", row_ok and two_ok, "every row of 3x3 and 3x4 (rows 1, 2 by the transfer: p_0 P = p_0) and every row and column of 2x3 (from the definition) is the K-chain")
    corner_ok = True
    for (ker, _, _, _, blocks, _) in data.values():
        for m in blocks.values():
            for k, p in m.items():
                c, b, a, d = k
                target = ker.corner(c, b, a, d)
                if mut("corner_law_wrong_denominator"):
                    target = target * ker.K2[a][b] / ker.K2[c][d]
                if p != target:
                    corner_ok = False
    checks.check("D4", corner_ok, "P5: the corner law pi(c,b,a,d) = (1/6) K(c,a) K(c,b) K(a,d) K(d,b)/K^2(a,b) at all 4 block positions of 3x3 (both triples) and 6 of 3x4")
    indep_ok, bridge_ok = True, True
    for (ker, _, _, _, blocks, _) in data.values():
        for m in blocks.items():
            _, mm = m
            for c in range(M):
                pc = sum(mm[(c, b, a, d)] for b in range(M) for a in range(M) for d in range(M))
                for a in range(M):
                    for b in range(M):
                        pab = sum(mm[(c, b, a, d)] for d in range(M))
                        target = ker.K[c][a] * (ker.K[a][b] if mut("corner_independence_forged") else ker.K[c][b])
                        indep_ok = indep_ok and pc == Fraction(1, 6) and pab / pc == target
                        bridge_ok = bridge_ok and all(mm[(c, b, a, d)] / pab == ker.bridge(d, a, b) for d in range(M))
    checks.check("D5", indep_ok and bridge_ok, "P5: from the computed blocks, P(a, b | c) = K(c->a) K(c->b) (independent given the corner; P(c) = 1/6) and P(d | c, b, a) is the bridge")
    diag_ok = True
    for (ker, _, _, _, blocks, _) in data.values():
        for mm in blocks.values():
            for a in range(M):
                for b in range(M):
                    pab = sum(mm[(c, b, a, d)] for c in range(M) for d in range(M))
                    target = Fraction(1, 6) * (ker.K[a][b] if mut("diagonal_pair_law_wrong") else ker.K2[a][b])
                    diag_ok = diag_ok and pab == target
            diag_ok = diag_ok and any(ker.K2[a][b] != ker.K[a][b] for a in range(M) for b in range(M))
    orth_note = "K^2 = K on the orthogonal orbit iff p + q = 2r: true at (3,1,2), false at (5,2,4)"
    orth_ok = Kernels(phi_table((3, 1, 2))).K2[0][2] == Kernels(phi_table((3, 1, 2))).K[0][2] and Kernels(phi_table((5, 2, 4))).K2[0][2] != Kernels(phi_table((5, 2, 4))).K[0][2]
    checks.check("D6", diag_ok and orth_ok, f"E4 recovered from pi: the diagonal pair (a, b) has the law (1/6) K^2(a, b), a different law from (1/6) K ({orth_note})")
    ker, p0, P, cols, _, _ = data[((3, 1, 2), 3)]
    alt = n_row_marginal(p0, [P, P], 3, [(0, 1), (1, 1), (2, 1)])
    checks.check("D7", alt == cols[1], "the column-projected row transfer (carried values) and the middle-row contraction agree on column 1 of 3x3")
    if exact:
        for (tr, W), (ker, _, _, _, _, _) in data.items():
            print(f"exact K at {tr}: rows " + "; ".join(" ".join(str(ker.K[a][b]) for b in range(M)) for a in range(M)) + f"; K^2 numerators over {ker.Z1 ** 2}: par {ker.K2n[0][0]} anti {ker.K2n[0][1]} orth {ker.K2n[0][2]}")


# ============================================================================================ family E
STAIRCASES = {
    "RDRD": ((0, 0), (0, 1), (1, 1), (1, 2), (2, 2)), "DRDR": ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2)),
    "RRDD": ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)), "DDRR": ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    "RDDR": ((0, 0), (0, 1), (1, 1), (2, 1), (2, 2)), "DRRD": ((0, 0), (1, 0), (1, 1), (1, 2), (2, 2)),
}
SNAKE_LITERALS = (Fraction(0), Fraction(3161, 7227792), Fraction(3583442207, 7981260404832))


def minimal_staircase_conditional(ker: Kernels, c: int, b: int, d: int) -> Fraction:
    """P(d | c, b) along the minimal staircase (0,0)(0,1)(1,1) from the corner law: sum_a K(c,a) K(a,d) K(d,b)/K^2(a,b)."""
    return sum(ker.K[c][a] * ker.K[a][d] * ker.K[d][b] / ker.K2[a][b] for a in range(M))


def family_e(checks: Checks, report: dict, exact: bool) -> None:
    ker, p0, P, cols, blocks, _ = report["D"][((3, 1, 2), 3)]
    mm = blocks[(1, 1)]
    cond_ok = True
    for c in range(M):
        for b in range(M):
            pcb = sum(mm[(c, b, a, d)] for a in range(M) for d in range(M))
            for d in range(M):
                direct = sum(mm[(c, b, a, d)] for a in range(M)) / pcb
                cond_ok = cond_ok and pcb == Fraction(1, 6) * ker.K[c][b] and direct == minimal_staircase_conditional(ker, c, b, d)
    lit = Fraction(227, 859) if mut("minimal_staircase_conditional_off") else Fraction(227, 858)
    v0 = minimal_staircase_conditional(ker, 0, 0, 0)
    checks.check("E1", cond_ok and v0 == lit and v0 != ker.K[0][0] == Fraction(1, 4), f"P6: the minimal staircase's conditional P(d | c, b) from the corner law equals the direct marginal (216 triples); at c = b = d = P(e_x) it is {v0} against K(b->d) = {ker.K[0][0]}")
    defects: dict = {}
    pairs_ok = True
    for tr in TRIPLES:
        kr, q0, Q, _, _, _ = report["D"][(tr, 3)]
        for name, sites in STAIRCASES.items():
            m = three_row_marginal(q0, Q, Q, 3, list(sites))
            defects[(tr, name)] = tv(m, kr.chain)
            for t in range(4):
                pair: dict = {}
                for k, p in m.items():
                    pair[(k[t], k[t + 1])] = pair.get((k[t], k[t + 1]), 0) + p
                pairs_ok = pairs_ok and all(pair[(u, v)] == Fraction(1, 6) * kr.K[u][v] for u in range(M) for v in range(M))
            for t in range(5):
                site: dict = {}
                for k, p in m.items():
                    site[k[t]] = site.get(k[t], 0) + p
                pairs_ok = pairs_ok and all(site[u] == Fraction(1, 6) for u in range(M))
    report["staircase_defects"] = defects
    fail_ok = all((d == 0) if mut("staircase_claimed_chain") else (d > 0) for d in defects.values())
    checks.check("E2", fail_ok, "P6 executed: all six staircases of 3x3 have a positive total-variation defect from the K-chain at both triples")
    checks.check("E3", pairs_ok, "the premise of P6: along every staircase every consecutive pair has the law (1/6) K and every site marginal is uniform (a chain along it would have kernel K)")
    muP = report["muP_2x3"][(3, 1, 2)]
    lawM = formation_law(2, 3, mirror_order(2, 3), rule_function("product", ker.phi))
    diff = sum(1 for k in muP if muP[k] != lawM[k])
    tvm = sum(abs(muP[k] - lawM[k]) for k in muP) / 2
    mirror_cols = all(marginal(lawM, 2, 3, [(0, j), (1, j)])[k] == Fraction(1, 6) * ker.K[k[0]][k[1]] for j in range(3) for k in product(range(M), repeat=2))
    mirror_rows = all(marginal(lawM, 2, 3, [(i, 0), (i, 1), (i, 2)])[k] == ker.chain(k) for i in range(2) for k in product(range(M), repeat=3))
    report["mirror"] = (diff, tvm)
    mirror_ok = (diff == 0) if mut("mirror_law_equal_claimed") else (diff == 32616 and len(muP) == 46656 and tvm > 0)
    checks.check("E4", mirror_ok and mirror_cols and mirror_rows, f"P7(a): the mirror class's law differs from mu_P on {diff} of {len(muP)} configurations of 2x3 (TV {tvm}); rows p_0, columns (1/6) K")
    inv_ok, snake_def_ok = True, True
    snake_data = {}
    for tr in TRIPLES:
        kr = Kernels(phi_table(tr))
        q0, Qlr, Qrl = p0_num(kr, 3), row_kernel_num(kr, 3, "lr"), row_kernel_num(kr, 3, "rl")
        rows = row_states(3)
        for ib in range(len(rows)):
            inv_ok = inv_ok and sum(Qrl[0][ib]) == Qrl[1]
        for ia in range(len(rows)):
            lhs = sum(q0[0][ib] * Qrl[0][ib][ia] for ib in range(len(rows)))
            rhs = q0[0][(ia + 1) % len(rows) if mut("snake_row_kernel_not_invariant") else ia] * Qrl[1]
            inv_ok = inv_ok and lhs == rhs
        r = rule_function("product", kr.phi)
        law_s = formation_law(2, 3, snake_order(2, 3), r)
        idx = {rr: k for k, rr in enumerate(rows)}
        snake_def_ok = snake_def_ok and all(law_s[c] == Fraction(q0[0][idx[c[:3]]] * Qrl[0][idx[c[:3]]][idx[c[3:]]], q0[1] * Qrl[1]) for c in law_s)
        cols3 = {j: three_row_marginal(q0, Qrl, Qlr, 3, [(0, j), (1, j), (2, j)]) for j in range(3)}
        cols4 = {j: n_row_marginal(q0, [Qrl, Qlr, Qrl], 3, [(0, j), (1, j), (2, j), (3, j)]) for j in range(3)}
        vert = True
        for j in range(3):
            for t in (0, 1):
                pair: dict = {}
                for k, p in cols3[j].items():
                    pair[(k[t], k[t + 1])] = pair.get((k[t], k[t + 1]), 0) + p
                vert = vert and all(pair[(u, v)] == Fraction(1, 6) * kr.K[u][v] for u in range(M) for v in range(M))
        snake_data[tr] = (kr, {j: tv(cols3[j], kr.chain) for j in range(3)}, {j: tv(cols4[j], kr.chain) for j in range(3)}, vert)
    report["snake"] = snake_data
    checks.check("E5", inv_ok, "P7(b): the reversed row kernel P_rl is row-stochastic and p_0 P_rl = p_0 on all 216 row states at both triples")
    checks.check("E6", snake_def_ok, "the snake's law on 2x3 from block 01's definition equals p_0(row 0) P_rl(row 0 -> row 1) entrywise at both triples")
    d3 = snake_data[(3, 1, 2)][1]
    lits = tuple(SNAKE_LITERALS)
    if mut("snake_column_claimed_chain"):
        lits = (Fraction(0), Fraction(0), Fraction(0))
    snake3_ok = tuple(d3[j] for j in range(3)) == lits and d3[0] == 0 and d3[1] > 0 and d3[2] > 0 and all(snake_data[tr][3] for tr in TRIPLES) and snake_data[(5, 2, 4)][1][0] == 0 and snake_data[(5, 2, 4)][1][1] > 0 and snake_data[(5, 2, 4)][1][2] > 0
    checks.check("E7", snake3_ok, f"P7(b): snake proper on 3x3 (rows left-to-right, right-to-left, left-to-right): column 0 is the K-chain, columns 1, 2 are not: TV defects {d3[0]}, {d3[1]}, {d3[2]} at (3,1,2); vertical pairs (1/6) K")
    snake4_ok = all(snake_data[tr][2][j] > 0 for tr in TRIPLES for j in range(3))
    checks.check("E8", snake4_ok, "P7(b): snake proper on 4x3 (rows alternating): no column is the K-chain at either triple (column-projected row transfer carrying the column values so far)")
    kc = Kernels(phi_table(CONSTANT))
    q0, Qlr, Qrl = p0_num(kc, 3), row_kernel_num(kc, 3, "lr"), row_kernel_num(kc, 3, "rl")
    const_defects = [tv(three_row_marginal(q0, Qlr, Qlr, 3, list(s)), kc.chain) for s in STAIRCASES.values()]
    const_defects += [tv(three_row_marginal(q0, Qrl, Qlr, 3, [(0, j), (1, j), (2, j)]), kc.chain) for j in range(3)]
    const_defects += [tv(n_row_marginal(q0, [Qrl, Qlr, Qrl], 3, [(0, j), (1, j), (2, j), (3, j)]), kc.chain) for j in range(3)]
    rc = rule_function("product", kc.phi)
    const_mirror = formation_law(2, 3, mirror_order(2, 3), rc) == formation_law(2, 3, row_order(2, 3), rc)
    const_ok = (any(d > 0 for d in const_defects)) if mut("constant_rule_defect_claimed") else (all(d == 0 for d in const_defects) and const_mirror)
    checks.check("E9", const_ok, "the variation clause: at (2,2,2) every staircase and snake-column defect is zero and the mirror law equals mu_P")
    if exact:
        for (tr, name), d in defects.items():
            print(f"exact staircase {name} at {tr}: TV defect {d}")
        for tr, (kr, d3, d4, _) in snake_data.items():
            print(f"exact snake at {tr}: 3x3 columns {d3[0]}, {d3[1]}, {d3[2]}; 4x3 columns {d4[0]}, {d4[1]}, {d4[2]}")
        print(f"exact mirror on 2x3 at (3,1,2): {report['mirror'][0]} of 46656 differ; TV {report['mirror'][1]}")
        print("exact minimal staircase at (3,1,2), c = b = P(e_x): P(d | c, b) = " + " ".join(str(minimal_staircase_conditional(ker, 0, 0, d)) for d in range(M)) + "; K(b -> d) = " + " ".join(str(ker.K[0][d]) for d in range(M)))


# ============================================================================================ family F
FENCES = (
    "This note describes the formation law of the monotone-order class on finite rectangles, the infinite strip and the quadrant; it states nothing about the static law beyond block 01's and block 02's separation, and nothing about orders outside the class beyond the executed snake and mirror witnesses.",
    "No order is selected as physical; no plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "The unilateral Markov field of the literature is a reference re-proved here at the scope used; no value, constant or theorem is imported as authority.",
)
# The forbidden phrases are assembled from pieces so that neither this source nor its stdout carries them whole.
FORBIDDEN = (
    "the physical " + "order", "washes " + "out", "unique on " + "the lattice", "cert" + "ified", "phase " + "transition",
    "several " + "static laws", "formation law equals " + "the static law", "formation law is " + "the static law",
    "every order gives " + "the same law", "all orders give " + "the same law", "every staircase is " + "a chain",
    "staircases are " + "chains", "staircases are " + "K-chains", "selects the " + "physical", "fires wake " + "condition",
)
CLAIM_INJECTIONS = {
    "claim_static_equals_formation": "On the strip the formation law equals the static law.",
    "claim_all_orders_same_law": "Every order gives the same law on the rectangle.",
    "claim_staircases_chains": "Under mu_P all staircases are chains.",
}
# The literature surname of the unilateral-field structure, assembled from character codes so that it does not appear in
# this source; it may appear in the note only inside the Prior art and Imports sections (checked in F3).
AUTHOR_NEEDLE = "".join(chr(c) for c in (112, 105, 99, 107, 97, 114, 100))
LABEL_NEEDLE = "unilateral-field"
AUTHOR_SECTIONS = ("Prior art", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def needle_outside_allowed(note_text: str, needle: str) -> list:
    parts = re.split(r"(?m)^## ", note_text)
    bad = []
    if needle in parts[0].lower():
        bad.append("<front matter or title>")
    for part in parts[1:]:
        heading = part.split("\n", 1)[0].strip()
        if needle in part.lower() and not heading.startswith(AUTHOR_SECTIONS):
            bad.append(heading)
    return bad


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    if mut("claim_unilateral-field_in_theorem"):
        text = text.replace("\n## Falsifiers", f"\nBy the {AUTHOR_NEEDLE} field theorem the corner law holds.\n## Falsifiers", 1)
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    bad = needle_outside_allowed(text, AUTHOR_NEEDLE) + needle_outside_allowed(text, LABEL_NEEDLE)
    named = AUTHOR_NEEDLE in text.lower()
    checks.check("F3", not bad and named, f"the literature name of the structure appears only in the Prior art and Imports sections (violations: {bad})")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad_lines = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F4", not bad_lines and len(scan) > 300, f"runner source: no floating-point literal or conversion call ({len(bad_lines)} hits)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — every configuration of 2x3 (46656) for the 5 extensions, the mirror, the snake, the sum rule and the asymmetric phi; every configuration of 2x4 against 4x2; every (a, b, s) triple for the bridge",
    "per_site: executed — every site of every linear extension of 2x3, 3x3, 3x4 (509 orders) records exactly its left and above neighbors; the declared sites of the i-j, j-i sweeps and the snake",
    "per_mode: executed — every column and row of 3x3 (both triples) and 3x4 as three-site joints; every 2x2 block position against the corner law; the six staircases and the snake columns as exact defects",
    "per_block: executed — the row kernels P and P_rl on all 216 x 216 entries against the definition; p_0 P = p_0 and p_0 P_rl = p_0 on all 216 row states; the 4x3 snake by the carried-value transfer",
    "lattice_wide: not claimed — P1 is proved for every rectangle and every rule; P4, P5 on the infinite strip and the quadrant follow from finite rectangles by block 02's limit arguments; nothing on the static law, the plane or orders outside the class beyond the witnesses",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    exact = "--exact" in argv
    checks = Checks()
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8") if AXIOM_PATH.is_file() else ""
    b01_text = BLOCK01_PATH.read_text(encoding="utf-8") if BLOCK01_PATH.is_file() else ""
    b02_text = BLOCK02_PATH.read_text(encoding="utf-8") if BLOCK02_PATH.is_file() else ""
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the monotone-order class on rectangles: one law mu_P (P1), bridge factor (P2), transpose (P3), rows and columns chains (P4), corner law (P5), staircases (P6), mirror and snake (P7); exact")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, note_text, axiom_text, b01_text, b02_text)
    family_b(checks, report)
    family_c(checks, report)
    family_d(checks, report, exact)
    family_e(checks, report, exact)
    family_f(checks, note_text)
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
