#!/usr/bin/env python3
"""Exact checks: the uniqueness region of the covariant product rule's static law on the cubic lattice, by the one-site contraction criterion re-proved by coupling.

Scope.  The menu is the six Bloch-axis projectors inside M_2(C); the rule is
the covariant positive product rule with orbit weights (p, q, r).  (G) The
one-neighbor interdependence coefficient c_1(p, q, r) of the one-site
conditional on the six-neighbor shell of Z^3, exactly: the same number for the
six directions, symmetric under p <-> q, zero exactly at the constant rule; its
exact value at the seven declared triples, on the grid r = 4, p, q in 1..12,
and along the three lines (t,1,1), (t,t,1), (1,1,t), where the crossing
6 c_1 = 1 is isolated by Sturm's theorem as the unique positive root of an
explicit degree-7 polynomial, with the maximizing shell pattern identified and
the supremum over all 7776 x 15 pattern-and-pair choices re-executed at both
endpoints of the isolating interval; each line crosses 6 c_1 = 1 a second time
(t^2 + 10t - 5, t^5 + 7t - 5, 5t^5 - 7t^4 - 1), and on each isolating interval
every competitor is certified below by an exact Lipschitz bound (constant 6/t
along a line) or is identical to the displayed maximizer, while 6 c_1 < 1 is
certified for every real t between the two thresholds (G6); the (1,1,t) line
is the (t,t,1) line under scale invariance (reciprocal polynomials).  (H) The finite-window comparison bound
proved by coupling in the note and executed here on the plaquette with eight
exterior slots (the one-step inequality and the maximal-coupling identity on a
declared configuration family) and on the 3x3 planar window with twelve
exterior slots (the influence matrix D = (I - C)^{-1} exactly over the
rationals, the damped fixed-point iterates, the exact center-site marginals by
integer row transfer and their total variation against the bound).  (I) The
arithmetic of the corollary on Z^3: the path-count identity and the table
alpha^L / (1 - alpha).  Uniqueness of the infinite-volume static law on Z^3 is
stated only where 6 c_1 < 1 is executed (the four region triples and the
declared rational points on the lines); at (3, 1, 2) and (5, 2, 4) the
criterion is silent and nothing is stated there about one law or several.
Exact integer, rational and symbolic arithmetic only: the runner scans its own
source and fails if a floating-point literal or conversion call appears.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import lcm
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
BLOCK01_PATH = ROOT / AUDIT_INPUT_PATHS[2]
BLOCK02_PATH = ROOT / AUDIT_INPUT_PATHS[3]
CLAIM_ID = "admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "is the unique law with those full conditionals"
BLOCK02_CLAIM_ID = "admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06"
BLOCK02_FRAGMENT = "an infinite-volume static law"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "records are permanent",
    "Only records are readable.",
    "A site with no record cannot be read.",
)

# ---------------------------------------------------------------- mutations
MUTATION_GATE = {
    "coefficient_direction_dependent": "B",
    "relabeling_identity_broken": "B",
    "constant_rule_nonzero": "B",
    "c1_literal_off": "C",
    "region_triple_misclassified": "C",
    "grid_symmetry_broken": "C",
    "grid_region_cells_wrong": "C",
    "sign_pattern_not_fixed": "C",
    "line_polynomial_wrong_coefficient": "C",
    "threshold_wrong_root": "C",
    "endpoint_sup_pattern_forged": "C",
    "second_crossing_wrong_root": "C",
    "competitor_identity_forged": "C",
    "region_certificate_forged": "C",
    "reciprocity_broken": "C",
    "c4_c1_inversion_denied": "C",
    "one_step_inequality_drops_b": "D",
    "one_step_inequality_wrong_coefficient": "D",
    "maximal_coupling_identity_broken": "D",
    "row_sum_ignored": "D",
    "D_matrix_wrong_inverse": "D",
    "fixed_point_not_fixed": "D",
    "center_tv_exceeds_bound_forged": "D",
    "path_count_wrong": "E",
    "alpha_table_wrong_exponent": "E",
    "line_points_misclassified": "E",
    "claim_nonunique_at_silent": "F",
    "claim_unique_at_silent": "F",
    "claim_phase_transition": "F",
    "claim_physical_rule": "F",
    "claim_author_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


# ------------------------------------------------------------------- checks
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


def dec(x: Fraction, digits: int, up: bool = False) -> str:
    """Exact decimal expansion of a rational rounded down (or up when up=True); integer arithmetic; a label, not evidence."""
    sign = "-" if x < 0 else ""
    x = abs(x)
    scaled = (x.numerator * 10 ** digits) // x.denominator
    if up and scaled * x.denominator != x.numerator * 10 ** digits:
        scaled += 1
    s = str(scaled).rjust(digits + 1, "0")
    return f"{sign}{s[:-digits]}.{s[-digits:]}"


# --------------------------------------------------------------------- menu
# Menu order: P(+e_x), P(-e_x), P(+e_y), P(-e_y), P(+e_z), P(-e_z); rebuilt here, not imported.
MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
PAIRS = tuple((t, t2) for t in range(M) for t2 in range(t + 1, M))
REGION_TRIPLES = ((2, 1, 2), (3, 2, 2), (5, 4, 4), (11, 10, 10))
SILENT_TRIPLES = ((3, 1, 2), (5, 2, 4))
CONSTANT_TRIPLE = (2, 2, 2)
C1_LITERALS = {
    (3, 1, 2): Fraction(270, 989),
    (5, 2, 4): Fraction(8650000, 40615109),
    (2, 1, 2): Fraction(2, 13),
    (3, 2, 2): Fraction(2079, 15566),
    (5, 4, 4): Fraction(4000000, 61385721),
    (11, 10, 10): Fraction(98241110000, 4544062780611),
    (7, 3, 5): Fraction(6391462, 29948925),
    (2, 2, 2): Fraction(0),
}
C1_253 = Fraction(1629375, 6780002)
C4_253 = Fraction(14250, 59251)
DIAMOND = frozenset({(2, 4), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 3), (5, 4), (5, 5), (5, 6), (6, 4), (6, 5)})
GRID_MAX = 12


def orbit(a: int, b: int) -> int:
    d = sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))
    return 0 if d == 1 else (1 if d == -1 else 2)


def antipode(a: int) -> int:
    return a ^ 1


def phi_table(triple):
    return [[triple[orbit(a, b)] for b in range(M)] for a in range(M)]


def scaled_triple(triple):
    """A rational triple scaled to integers by the common denominator; the conditional is homogeneous of degree zero in phi."""
    fr = tuple(Fraction(x) for x in triple)
    L = lcm(*[x.denominator for x in fr])
    return tuple(int(x * L) for x in fr)


def weights(phi, shell):
    """Unnormalized one-site conditional given the recorded shell values (a tuple of menu indices)."""
    w = [1] * M
    for s in range(M):
        acc = 1
        for e in shell:
            acc *= phi[s][e]
        w[s] = acc
    return w


def tv_int(wa, Za, wb, Zb):
    """Total variation as (numerator, denominator) in integers: (1/2) sum_s |wa_s/Za - wb_s/Zb|."""
    n = 0
    for s in range(M):
        n += abs(wa[s] * Zb - wb[s] * Za)
    return n, 2 * Za * Zb


def coefficient(triple, deg: int):
    """The interdependence coefficient c_1^{(deg)}: the supremum over the other deg-1 slots' values and over a pair of
    values at one slot of the total variation between the two one-site conditionals; integer hot loop; returns
    (Fraction, (eta, t, t2)) with the lexicographically first maximizer."""
    phi = phi_table(triple)
    best_n, best_d, arg = 0, 1, None
    for eta in product(range(M), repeat=deg - 1):
        base = weights(phi, eta)
        w = [[base[s] * phi[s][t] for s in range(M)] for t in range(M)]
        Z = [sum(w[t]) for t in range(M)]
        for t, t2 in PAIRS:
            n, d = tv_int(w[t], Z[t], w[t2], Z[t2])
            if n * best_d > best_n * d:
                best_n, best_d, arg = n, d, (eta, t, t2)
    return Fraction(best_n, best_d), arg


SHELL_MULTISETS = tuple(combinations_with_replacement(range(M), 5))


def coefficient_multiset(triple, deg: int = 6):
    """The same supremum over the 252 shell multisets x 15 pairs (the conditional is a symmetric function of the shell,
    so the 7776 x 15 choices collapse to these); returns (Fraction, lexicographically first maximizer, tie count)."""
    phi = phi_table(triple)
    shells = SHELL_MULTISETS if deg == 6 else tuple(combinations_with_replacement(range(M), deg - 1))
    best_n, best_d, arg, ties = 0, 1, None, 0
    for eta in shells:
        base = weights(phi, eta)
        w = [[base[s] * phi[s][t] for s in range(M)] for t in range(M)]
        Z = [sum(w[t]) for t in range(M)]
        for t, t2 in PAIRS:
            n, d = tv_int(w[t], Z[t], w[t2], Z[t2])
            if n * best_d > best_n * d:
                best_n, best_d, arg, ties = n, d, (eta, t, t2), 1
            elif n * best_d == best_n * d:
                ties += 1
    return Fraction(best_n, best_d), arg, ties


def coefficient_at_slot(triple, deg: int, slot: int):
    """The same supremum with the varied neighbor placed explicitly at position `slot` of the shell tuple (G1)."""
    phi = phi_table(triple)
    best = Fraction(0)
    for eta in product(range(M), repeat=deg - 1):
        conds = []
        for t in range(M):
            shell = eta[:slot] + (t,) + eta[slot:]
            w = weights(phi, shell)
            conds.append((w, sum(w)))
        for t, t2 in PAIRS:
            n, d = tv_int(conds[t][0], conds[t][1], conds[t2][0], conds[t2][1])
            if Fraction(n, d) > best:
                best = Fraction(n, d)
    return best


def tv_of_pattern(triple, eta, ta, tb) -> Fraction:
    phi = phi_table(triple)
    base = weights(phi, eta)
    wa = [base[s] * phi[s][ta] for s in range(M)]
    wb = [base[s] * phi[s][tb] for s in range(M)]
    n, d = tv_int(wa, sum(wa), wb, sum(wb))
    return Fraction(n, d)


def sign_pattern(triple, eta, ta, tb):
    phi = phi_table(triple)
    base = weights(phi, eta)
    wa = [base[s] * phi[s][ta] for s in range(M)]
    wb = [base[s] * phi[s][tb] for s in range(M)]
    Za, Zb = sum(wa), sum(wb)
    return tuple(1 if wa[s] * Zb - wb[s] * Za >= 0 else -1 for s in range(M))


# ==================================================================== family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b01_text: str, b02_text: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4, "the four declared audit inputs exist")
    flat = normalize_text(axiom_text)
    checks.check("A2", all(n in flat for n in AXIOM_NEEDLES[:2]), "axiom memo: both Admissibility sentences verbatim")
    checks.check("A3", all(n in flat for n in AXIOM_NEEDLES[2:]), "axiom memo: the four Record sentences verbatim")
    checks.check("A4", BLOCK01_CLAIM_ID in b01_text and BLOCK01_FRAGMENT in normalize_text(b01_text), "block 01's note: claim id and the finite-window uniqueness fragment")
    checks.check("A5", BLOCK02_CLAIM_ID in b02_text and BLOCK02_FRAGMENT in normalize_text(b02_text), "block 02's note: claim id and the existence fragment")
    checks.check("A6", CLAIM_ID in note_text, "this note carries its claim id")


# ==================================================================== family B
def family_b(checks: Checks, report: dict) -> None:
    base = (3, 1, 2)
    per_slot = []
    for k in range(6):
        tr = (3, 1, 3) if (mut("coefficient_direction_dependent") and k == 2) else base
        per_slot.append(coefficient_at_slot(tr, 6, k))
    checks.check("B1", len(set(per_slot)) == 1 and per_slot[0] == C1_LITERALS[base], f"G1: the same coefficient {per_slot[0]} with the flipped neighbor in each of the six directions, (3,1,2)")
    swapped = all(coefficient(tr, 6)[0] == coefficient((tr[1], tr[0], tr[2]), 6)[0] for tr in ((3, 1, 2), (5, 2, 4)))
    phi_a, phi_b = phi_table((3, 1, 2)), phi_table((1, 3, 2))
    identity = True
    for shell in product(range(M), repeat=6):
        wa, wb = weights(phi_a, shell), weights(phi_b, shell)
        Za, Zb = sum(wa), sum(wb)
        for s in range(M):
            s_img = s if mut("relabeling_identity_broken") else antipode(s)
            if wa[s_img] * Zb != wb[s] * Za:
                identity = False
                break
        if not identity:
            break
    checks.check("B2", swapped, "G2: c_1(3,1,2) = c_1(1,3,2) and c_1(5,2,4) = c_1(2,5,4) exactly")
    checks.check("B3", identity, "G2: r_(3,1,2)(-s | eta) = r_(1,3,2)(s | eta) on all 46656 shells and six values")
    const = (2, 2, 3) if mut("constant_rule_nonzero") else CONSTANT_TRIPLE
    c_const = coefficient(const, 6)[0]
    positive = all(coefficient(tr, 6)[0] > 0 for tr in REGION_TRIPLES + SILENT_TRIPLES)
    checks.check("B4", c_const == 0 and positive, "G3: c_1 = 0 at (2,2,2); c_1 > 0 at the six non-constant triples")
    report["B"] = {"per_slot": per_slot}


# ==================================================================== family C
T = sp.symbols("t")
# name, symbolic weights, declared rational scan, declared bracket of the crossing, sign of 6c_1 - 1 above the crossing, contract polynomial
LINES = (
    ("(t,1,1)", (T, sp.Integer(1), sp.Integer(1)), tuple(1 + Fraction(k, 8) for k in range(1, 9)), (Fraction(3, 2), Fraction(13, 8)), 1,
     T ** 7 - 2 * T ** 5 + 5 * T ** 4 - 8 * T ** 3 - T ** 2 - 4),
    ("(t,t,1)", (T, T, sp.Integer(1)), tuple(1 + Fraction(k, 8) for k in range(1, 9)), (Fraction(11, 8), Fraction(3, 2)), 1,
     4 * T ** 7 - 8 * T ** 5 + 5 * T ** 4 - 8 * T ** 3 - T ** 2 - 1),
    ("(1,1,t)", (sp.Integer(1), sp.Integer(1), T), tuple(Fraction(k, 8) for k in range(1, 9)), (Fraction(5, 8), Fraction(3, 4)), -1,
     T ** 7 + T ** 5 + 8 * T ** 4 - 5 * T ** 3 + 8 * T ** 2 - 4),
)
ISOLATION_WIDTH = Fraction(1, 10 ** 20)
# the second crossing on each line: the descending scan t = 1 - k/40 on (t,1,1) and (t,t,1); the ascending scan t = 1 + k/20 on (1,1,t)
LINES2 = (
    ("(t,1,1)", (T, sp.Integer(1), sp.Integer(1)), tuple(1 - Fraction(k, 40) for k in range(1, 40)), (Fraction(1, 2), Fraction(19, 40)), -1,
     T ** 2 + 10 * T - 5),
    ("(t,t,1)", (T, T, sp.Integer(1)), tuple(1 - Fraction(k, 40) for k in range(1, 40)), (Fraction(7, 10), Fraction(27, 40)), -1,
     T ** 5 + 7 * T - 5),
    ("(1,1,t)", (sp.Integer(1), sp.Integer(1), T), tuple(1 + Fraction(k, 20) for k in range(1, 20)), (Fraction(7, 5), Fraction(29, 20)), 1,
     5 * T ** 5 - 7 * T ** 4 - 1),
)
COPIES_EXPECTED = (30, 288, 288, 60, 72, 72)


def dyadic_mid(a: Fraction, b: Fraction) -> Fraction:
    k = 0
    while True:
        m = Fraction(int(((a + b) / 2) * 2 ** k), 2 ** k)
        if a < m < b:
            return m
        k += 1


def region_certificate(line_sym, u: Fraction, v: Fraction) -> int:
    """Certify 6 c_1(t) - 1 < 0 for every real t in [u, v] (G6).  On a line every weight is t or 1, so the one-site weights
    are monomials t^{k_s}, 0 <= k_s <= 6, t a_s'(t) = a_s (k_s - sum_s' k_s' a_s'), hence sum_s |a_s'| <= 6/t; the total
    variation of any shell-and-pair and its maximum c_1 are Lipschitz with constant 6/u on [u, v].  Exact endpoint values
    plus 6 * (6/a) * (b - a) certify a subinterval [a, b]; bisection at dyadic midpoints otherwise.  Returns the number of
    certified subintervals, or -1."""
    cache: dict = {}

    def val(tval: Fraction) -> Fraction:
        if tval not in cache:
            cache[tval] = 6 * coefficient_multiset(line_triple(line_sym, tval))[0] - 1
        return cache[tval]

    stack, count = [(u, v)], 0
    while stack:
        a, b = stack.pop()
        va, vb = val(a), val(b)
        if va >= 0 or vb >= 0:
            return -1
        if max(va, vb) + 36 * (b - a) / a < 0:
            count += 1
            continue
        if b - a < Fraction(1, 10 ** 40):
            return -1
        m = dyadic_mid(a, b)
        stack.append((a, m))
        stack.append((m, b))
    return count


def difference_numerators(line_sym, eta, ta, tb):
    """The numerator polynomials of a_s(t) - b_s(t), s in M, for the shell eta and the pair (ta, tb) on the line (integer monomials)."""
    phi = [[line_sym[orbit(x, y)] for y in range(M)] for x in range(M)]
    base = [sp.Integer(1)] * M
    for s in range(M):
        for e in eta:
            base[s] = base[s] * phi[s][e]
    wa = [base[s] * phi[s][ta] for s in range(M)]
    wb = [base[s] * phi[s][tb] for s in range(M)]
    Za, Zb = sum(wa), sum(wb)
    return [sp.Poly(sp.expand(wa[s] * Zb - wb[s] * Za), T, domain="QQ") for s in range(M)]


def sign_constant(line_sym, eta, ta, tb, a: Fraction, b: Fraction) -> bool:
    """No difference a_s - b_s changes sign on [a, b]: each nonzero numerator has no root there (Sturm), so the sign pattern at a
    holds on the whole interval and the signed sum equals the total variation on [a, b]."""
    return all(d.is_zero or d.count_roots(inf=rat(a), sup=rat(b)) == 0 for d in difference_numerators(line_sym, eta, ta, tb))


def competitor_sweep(line_sym, a: Fraction, b: Fraction, displayed: sp.Poly):
    """On the isolating interval [a, b] of a threshold: each of the 252 x 15 shell-multiset-and-pair choices is either verified
    below (6 TV - 1 < 0 on [a, b] by the endpoint values and the Lipschitz constant 6/a) or is a copy of the displayed maximizer:
    the same rational function with its sign pattern at a, that sign pattern constant on [a, b] (so its total variation equals the
    displayed function on all of [a, b]); returns (verified, copies, distinct)."""
    tra, trb = line_triple(line_sym, a), line_triple(line_sym, b)
    certified = identical = distinct = 0
    for eta in SHELL_MULTISETS:
        for t, t2 in PAIRS:
            va = 6 * tv_of_pattern(tra, eta, t, t2) - 1
            vb = 6 * tv_of_pattern(trb, eta, t, t2) - 1
            if max(va, vb) + 36 * (b - a) / a < 0:
                certified += 1
                continue
            signs = sign_pattern(tra, eta, t, t2)
            num, _den = sp.fraction(sp.cancel(6 * tv_symbolic(line_sym, eta, t, t2, signs) - 1))
            Pq = sp.Poly(num, T, domain="QQ")
            target = displayed + sp.Poly(T, T, domain="QQ") if mut("competitor_identity_forged") else displayed
            if Pq.degree() == target.degree() and (Pq * target.LC() - target * Pq.LC()).is_zero and sign_constant(line_sym, eta, t, t2, a, b):
                identical += 1
            else:
                distinct += 1
    return certified, identical, distinct


def reciprocal(P: sp.Poly) -> sp.Poly:
    return sp.Poly(sp.expand(T ** P.degree() * P.as_expr().subs(T, 1 / T)), T, domain="QQ")


def proportional(P: sp.Poly, Q: sp.Poly) -> bool:
    return P.degree() == Q.degree() and (P * Q.LC() - Q * P.LC()).is_zero


def rat(x: Fraction):
    return sp.Rational(x.numerator, x.denominator)


def frac(x) -> Fraction:
    x = sp.Rational(x)
    return Fraction(int(x.p), int(x.q))


def line_triple(line_sym, tval: Fraction):
    return scaled_triple(tuple(frac(v.subs(T, rat(tval))) for v in line_sym))


def tv_symbolic(line_sym, eta, ta, tb, signs):
    """(1/2) sum_s signs_s (r(s | eta, ta) - r(s | eta, tb)) as a rational function of t: equals TV wherever the sign pattern holds."""
    phi = [[line_sym[orbit(a, b)] for b in range(M)] for a in range(M)]
    base = [sp.Integer(1)] * M
    for s in range(M):
        for e in eta:
            base[s] = base[s] * phi[s][e]
    wa = [base[s] * phi[s][ta] for s in range(M)]
    wb = [base[s] * phi[s][tb] for s in range(M)]
    Za, Zb = sum(wa), sum(wb)
    return sp.cancel(sum(signs[s] * (wa[s] / Za - wb[s] / Zb) for s in range(M)) / 2)


def analyze_line(index: int, name, line_sym, scan, bracket, sign_above, contract_poly, second: bool = False) -> dict:
    out: dict = {"name": name}
    prev = None
    for tval in scan:
        c, arg = coefficient(line_triple(line_sym, tval), 6)
        if prev is not None and (6 * prev[0] < 1) != (6 * c < 1):
            out["bracket"] = (prev[1], tval)
            out["pattern"] = arg
            break
        prev = (c, tval)
    lo, hi = out["bracket"]
    eta, ta, tb = out["pattern"]
    signs_lo = sign_pattern(line_triple(line_sym, lo), eta, ta, tb)
    signs_hi = sign_pattern(line_triple(line_sym, hi), eta, ta, tb)
    if mut("sign_pattern_not_fixed") and not second:
        signs_hi = (-signs_hi[0],) + signs_hi[1:]
    out["signs_fixed"] = signs_lo == signs_hi and out["bracket"] == bracket
    out["signs"] = signs_hi
    expr = tv_symbolic(line_sym, eta, ta, tb, signs_hi)
    num, den = sp.fraction(sp.cancel(6 * expr - 1))
    P = sp.Poly(num, T, domain="QQ")
    contract = contract_poly + (T ** 2 if (mut("line_polynomial_wrong_coefficient") and index == 0 and not second) else 0)
    Pc = sp.Poly(contract, T, domain="QQ")
    out["numerator"] = sp.factor(num)
    out["P"] = P
    out["poly_match"] = P.degree() == Pc.degree() and (P * Pc.LC() - Pc * P.LC()).is_zero
    out["positive_roots"] = P.count_roots(inf=0)
    out["real_roots"] = P.count_roots()
    ivs = P.intervals(eps=rat(ISOLATION_WIDTH), inf=0)
    have_root = len(ivs) >= 1
    a, b = (frac(ivs[0][0][0]), frac(ivs[0][0][1])) if have_root else (Fraction(1), Fraction(1))
    if mut("second_crossing_wrong_root" if second else "threshold_wrong_root"):
        a, b = a + Fraction(1, 8), b + Fraction(1, 8)
    pa, pb = frac(P.eval(rat(a))), frac(P.eval(rat(b)))
    out["interval"] = (a, b)
    out["isolated"] = have_root and len(ivs) == 1 and out["positive_roots"] == 1 and a > 0 and b - a < ISOLATION_WIDTH and pa * pb < 0
    pattern = ((0, 0, 0, 0, 0), 0, 1) if (mut("endpoint_sup_pattern_forged") and not second) else (eta, ta, tb)
    sup_ok, sign_ok = True, True
    for end, expected_sign in ((a, -sign_above), (b, sign_above)):
        tr_end = line_triple(line_sym, end)
        sup_end, _ = coefficient(tr_end, 6)
        tv_pat = tv_of_pattern(tr_end, *pattern)
        rf_val = frac(expr.subs(T, rat(end)))
        sup_ok = sup_ok and sup_end == tv_pat and rf_val == tv_of_pattern(tr_end, eta, ta, tb)
        v = 6 * sup_end - 1
        sign_ok = sign_ok and ((v < 0) if expected_sign < 0 else (v > 0))
    out["endpoint_sup_ok"] = sup_ok and have_root
    out["sign_change_ok"] = sign_ok and have_root
    return out


def family_c(checks: Checks, report: dict, exact: bool) -> None:
    vals = {tr: coefficient(tr, 6) for tr in C1_LITERALS}
    literals = dict(C1_LITERALS)
    if mut("c1_literal_off"):
        literals[(3, 1, 2)] = Fraction(271, 989)
    multiset_same = all(coefficient_multiset(tr)[0] == vals[tr][0] for tr in literals)
    checks.check("C1", all(vals[tr][0] == literals[tr] for tr in literals) and multiset_same, "G4: exact c_1 at the eight triples = the literals; the 252-multiset supremum agrees")
    order = ((3, 1, 2), (5, 2, 4), (2, 1, 2), (3, 2, 2), (5, 4, 4), (11, 10, 10), (7, 3, 5))
    print("info c_1: " + " ".join(f"({tr[0]},{tr[1]},{tr[2]})={vals[tr][0]}" for tr in order[:4]))
    print("info c_1: " + " ".join(f"({tr[0]},{tr[1]},{tr[2]})={vals[tr][0]}" for tr in order[4:]))
    for tr in order:
        c, arg = vals[tr]
        ties = coefficient_multiset(tr)[2]
        if exact:
            print(f"exact c_1{tr}={c} 6c_1={dec(6 * c, 6)} max eta={''.join(map(str, arg[0]))} pair={arg[1]}{arg[2]} multiset ties={ties}")
    region_expected = set(REGION_TRIPLES)
    silent_expected = set(SILENT_TRIPLES)
    if mut("region_triple_misclassified"):
        region_expected.add((5, 2, 4))
        silent_expected.discard((5, 2, 4))
    classified = all(6 * vals[tr][0] < 1 for tr in region_expected) and all(6 * vals[tr][0] >= 1 for tr in silent_expected)
    checks.check("C2", classified, "G4: 6c_1 < 1 at the four region triples; >= 1 at (3,1,2), (5,2,4)")
    grid = {}
    for p in range(1, GRID_MAX + 1):
        for q in range(1, GRID_MAX + 1):
            tr = (7, 2, 5) if (mut("grid_symmetry_broken") and (p, q) == (7, 2)) else (p, q, 4)
            grid[(p, q)] = coefficient(tr, 6)[0]
    symmetric = all(grid[(p, q)] == grid[(q, p)] for p in range(1, GRID_MAX + 1) for q in range(1, GRID_MAX + 1))
    cells = {pq for pq, c in grid.items() if 6 * c < 1}
    expected_cells = set(DIAMOND) - ({(6, 5)} if mut("grid_region_cells_wrong") else set())
    checks.check("C3", symmetric, f"G2/G4: c_1(p,q,4) = c_1(q,p,4) on all {GRID_MAX * GRID_MAX} grid points, p, q in 1..{GRID_MAX}")
    checks.check("C4", cells == expected_cells, f"G4: the r = 4 grid's 6c_1 < 1 cells are the diamond ({len(cells)} cells)")
    if exact:
        for p in range(1, GRID_MAX + 1):
            print(f"exact grid p={p:2d}: " + " ".join("U" if 6 * grid[(p, q)] < 1 else "." for q in range(1, GRID_MAX + 1)))
    lines = [analyze_line(i, *spec) for i, spec in enumerate(LINES)]
    for ln in lines:
        a, b = ln["interval"]
        print(f"info line {ln['name']}: {ln['bracket'][0]}..{ln['bracket'][1]} eta={''.join(map(str, ln['pattern'][0]))} pair={ln['pattern'][1]}{ln['pattern'][2]} t*=[{dec(a, 14)},{dec(b, 14, True)}]")
        if exact:
            print(f"exact line {ln['name']}: numerator of 6TV-1 = {ln['numerator']}; signs {ln['signs']}; interval [{a}, {b}]; real roots {ln['real_roots']}, positive {ln['positive_roots']}")
    checks.check("C5", all(ln["signs_fixed"] for ln in lines), "G5: crossings at the declared brackets; sign pattern of the six differences fixed at both")
    checks.check("C6", all(ln["poly_match"] for ln in lines), "G5: numerator of 6TV(t) - 1 at the pattern = the contract's degree-7 polynomial up to a constant")
    checks.check("C7", all(ln["isolated"] for ln in lines), "G5: Sturm: one positive root each, isolated to width < 10^-20, sign change at the endpoints")
    checks.check("C8", all(ln["endpoint_sup_ok"] for ln in lines), "G5: at both endpoints the sup over all 7776 x 15 choices is the displayed pattern's value")
    checks.check("C9", all(ln["sign_change_ok"] for ln in lines), "G5: 6c_1 - 1 negative below, positive above t* on (t,1,1), (t,t,1); reversed on (1,1,t)")
    lines2 = [analyze_line(i, *spec, second=True) for i, spec in enumerate(LINES2)]
    for ln in lines2:
        a, b = ln["interval"]
        print(f"info line2 {ln['name']}: {ln['bracket'][0]}..{ln['bracket'][1]} eta={''.join(map(str, ln['pattern'][0]))} pair={ln['pattern'][1]}{ln['pattern'][2]} t2=[{dec(a, 14)},{dec(b, 14, True)}]")
        if exact:
            print(f"exact line2 {ln['name']}: numerator of 6TV-1 = {ln['numerator']}; signs {ln['signs']}; interval [{a}, {b}]; real roots {ln['real_roots']}, positive {ln['positive_roots']}")
    keys = ("signs_fixed", "poly_match", "isolated", "endpoint_sup_ok", "sign_change_ok")
    checks.check("C10", all(ln[k] for ln in lines2 for k in keys), "G5: second crossing per line at its bracket; numerator = the displayed polynomial; one positive root isolated to width < 10^-20; endpoint suprema; sign change")
    sweeps = [competitor_sweep(spec[1], ln["interval"][0], ln["interval"][1], ln["P"]) for spec, ln in zip(LINES + LINES2, lines + lines2)]
    copies = tuple(s[1] for s in sweeps)
    checks.check("C11", all(s[2] == 0 and s[0] + s[1] == len(SHELL_MULTISETS) * len(PAIRS) for s in sweeps) and copies == COPIES_EXPECTED, f"G5: six isolating intervals: every 252 x 15 choice verified below (Lipschitz) or a sign-constant copy of the displayed maximizer ({list(copies)})")
    regions = []
    for spec, ln1, ln2 in zip(LINES, lines, lines2):
        lo, hi = sorted([ln1["interval"], ln2["interval"]])
        u, v = lo[1], hi[0]
        if mut("region_certificate_forged"):
            v = hi[1] + Fraction(1, 100)
        regions.append(region_certificate(spec[1], u, v))
    checks.check("C12", all(n > 0 for n in regions), f"G6: 6c_1 < 1 verified for every real t between the two thresholds, each line (subintervals {regions})")
    P3a = LINES[2][5] + (T if mut("reciprocity_broken") else 0)
    recip_ok = proportional(reciprocal(sp.Poly(LINES[1][5], T, domain="QQ")), sp.Poly(P3a, T, domain="QQ")) and proportional(reciprocal(sp.Poly(LINES2[1][5], T, domain="QQ")), sp.Poly(LINES2[2][5], T, domain="QQ"))
    scale_ok = all(coefficient_multiset(line_triple(LINES[1][1], tv_))[0] == coefficient_multiset(line_triple(LINES[2][1], 1 / tv_))[0] for tv_ in (Fraction(5, 4), Fraction(3, 2), Fraction(7, 10))) and vals[(2, 1, 2)][0] == coefficient((4, 2, 4), 6)[0]
    checks.check("C13", recip_ok and scale_ok, "G2/G6: c_1(t,t,1) = c_1(1,1,1/t) executed; the (1,1,t) polynomials are the (t,t,1) reciprocals")
    c1_253, c4_253 = coefficient((2, 5, 3), 6)[0], coefficient((2, 5, 3), 4)[0]
    inversion = (c4_253 <= c1_253) if mut("c4_c1_inversion_denied") else (c4_253 > c1_253)
    silent735 = 6 * vals[(7, 3, 5)][0] >= 1
    checks.check("C14", inversion and c1_253 == C1_253 and c4_253 == C4_253 and silent735, f"c_1^(4)(2,5,3) = {c4_253} > c_1(2,5,3) = {c1_253}: a window coefficient can exceed c_1; (7,3,5) silent")
    report["C"] = {"vals": vals, "grid": grid, "lines": lines, "lines2": lines2, "sweeps": sweeps, "regions": regions}


# ==================================================================== family D
WINDOW_TRIPLES = ((2, 1, 2), (3, 2, 2), (5, 4, 4), (3, 1, 2))
WINDOW_REGION = ((2, 1, 2), (3, 2, 2), (5, 4, 4))
C4_LITERALS = {(2, 1, 2): Fraction(1, 8), (3, 2, 2): Fraction(1404, 11431), (5, 4, 4): Fraction(10000, 175641), (3, 1, 2): Fraction(918, 3431)}
CENTER_BOUND_LITERALS = {(2, 1, 2): Fraction(1, 56), (3, 2, 2): Fraction(1971216, 114898033), (5, 4, 4): Fraction(100000000, 30049760881)}
CENTER_TV_LITERAL_212 = Fraction(691410442136477999520, 76730168638463067377251)
CENTER_TV_LABELS = {(2, 1, 2): "0090109", (3, 2, 2): "0073929", (5, 4, 4): "0016901"}  # seven digits after "0."
ITERATIONS = 200
TOLERANCE = Fraction(1, 10 ** 4)
LCG_PAIRS = 2000
W3_SITES = tuple((i, j) for i in range(3) for j in range(3))
W3_INDEX = {s: k for k, s in enumerate(W3_SITES)}
W3_CENTER = W3_INDEX[(1, 1)]
W3_FLIP_SITE = W3_INDEX[(1, 0)]


def lcg_pairs(count: int):
    """Block 01's fixed generator: seed 20260906, multiplier 1103515245, increment 12345, modulus 2^31; eight draws per pair."""
    state = 20260906
    out = []
    for _ in range(count):
        v = []
        for _k in range(8):
            state = (1103515245 * state + 12345) % (2 ** 31)
            v.append((state >> 16) % M)
        out.append((tuple(v[:4]), tuple(v[4:])))
    return out


def plaquette_family():
    fam = []
    for eta in product(range(M), repeat=4):
        for eta2 in product(range(M), repeat=4):
            if sum(a != b for a, b in zip(eta, eta2)) <= 2:
                fam.append((eta, eta2))
    return fam + lcg_pairs(LCG_PAIRS)


def plaquette_checks(triple, fam) -> dict:
    """Plaquette sites 0-1-2-3-0; site x has interior neighbors x-1, x+1 and two exterior slots; base exterior all P(e_x);
    flipped exterior: the slot (site 0, left) carries P(-e_x).  Returns the one-step inequality and coupling-identity verdicts."""
    phi = phi_table(triple)
    c4 = coefficient(triple, 4)[0]
    coef = c4 / 4 if mut("one_step_inequality_wrong_coefficient") else c4
    ext = {x: (0, 0) for x in range(4)}
    ext_p = dict(ext)
    ext_p[0] = (1, 0)
    tabs = []
    coupling_ok = True
    for x in range(4):
        tab = {}
        for a, b in product(range(M), repeat=2):
            wa = weights(phi, (a, b) + ext[x])
            Za = sum(wa)
            for a2, b2 in product(range(M), repeat=2):
                wb = weights(phi, (a2, b2) + ext_p[x])
                Zb = sum(wb)
                n, d = tv_int(wa, Za, wb, Zb)
                tv = Fraction(n, d)
                pick = max if mut("maximal_coupling_identity_broken") else min
                agree = sum(pick(wa[s] * Zb, wb[s] * Za) for s in range(M))
                coupling_ok = coupling_ok and Fraction(agree, Za * Zb) == 1 - tv
                tab[(a, b, a2, b2)] = tv
        tabs.append(tab)
    bx = [Fraction(0)] * 4
    if not mut("one_step_inequality_drops_b"):
        bx[0] = coef
    bounds = [coef * k for k in range(3)]
    ineq_ok = True
    for eta, eta2 in fam:
        for x in range(4):
            a, b = eta[(x - 1) % 4], eta[(x + 1) % 4]
            a2, b2 = eta2[(x - 1) % 4], eta2[(x + 1) % 4]
            if tabs[x][(a, b, a2, b2)] > bounds[(a != a2) + (b != b2)] + bx[x]:
                ineq_ok = False
                break
        if not ineq_ok:
            break
    return {"c4": c4, "ineq_ok": ineq_ok, "coupling_ok": coupling_ok, "instances": 4 * len(tabs[0])}


def window_exteriors():
    ext0 = {}
    for i in range(3):
        ext0[(i, 0, "L")] = 0
        ext0[(i, 2, "R")] = 0
    for j in range(3):
        ext0[(0, j, "B")] = 0
        ext0[(2, j, "T")] = 0
    ext1 = dict(ext0)
    ext1[(1, 0, "L")] = 1
    return ext0, ext1


def window_center_marginal(phi, ext):
    """Exact center-site marginal of the 3x3 planar window with exterior records ext, by integer row transfer."""
    rows = list(product(range(M), repeat=3))

    def A(i, r):
        w = 1
        for j in range(2):
            w *= phi[r[j]][r[j + 1]]
        for j in range(3):
            for side in "LRBT":
                if (i, j, side) in ext:
                    w *= phi[r[j]][ext[(i, j, side)]]
        return w

    Vm = [[phi[r[0]][r2[0]] * phi[r[1]][r2[1]] * phi[r[2]][r2[2]] for r2 in rows] for r in rows]
    A0 = [A(0, r) for r in rows]
    A1 = [A(1, r) for r in rows]
    A2 = [A(2, r) for r in rows]
    R = len(rows)
    left = [sum(A0[i0] * Vm[i0][i1] for i0 in range(R)) for i1 in range(R)]
    right = [sum(Vm[i1][i2] * A2[i2] for i2 in range(R)) for i1 in range(R)]
    marg = [0] * M
    for i1, r1 in enumerate(rows):
        marg[r1[1]] += left[i1] * A1[i1] * right[i1]
    Z = sum(marg)
    return [Fraction(x, Z) for x in marg]


def window_influence(c4: Fraction):
    C = [[Fraction(0)] * 9 for _ in range(9)]
    for (i, j) in W3_SITES:
        for (i2, j2) in W3_SITES:
            if abs(i - i2) + abs(j - j2) == 1:
                C[W3_INDEX[(i, j)]][W3_INDEX[(i2, j2)]] = c4
    return C


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def window_analysis(triple) -> dict:
    phi = phi_table(triple)
    c4 = coefficient(triple, 4)[0]
    ext0, ext1 = window_exteriors()
    m0, m1 = window_center_marginal(phi, ext0), window_center_marginal(phi, ext1)
    tv = sum(abs(a - b) for a, b in zip(m0, m1)) / 2
    C = window_influence(c4)
    row_sums = [sum(row) for row in C]
    out = {"c4": c4, "tv": tv, "row_max": max(row_sums), "row_sums": sorted(set(row_sums))}
    if 4 * c4 >= 1:
        return out
    Cm = sp.Matrix(9, 9, lambda a, b: rat(C[a][b]))
    Dm = (sp.eye(9) + Cm).inv() if mut("D_matrix_wrong_inverse") else (sp.eye(9) - Cm).inv()
    D = [[frac(Dm[a, b]) for b in range(9)] for a in range(9)]
    I_minus_C = [[(Fraction(1) if a == b else Fraction(0)) - C[a][b] for b in range(9)] for a in range(9)]
    prod_ = matmul(D, I_minus_C)
    out["inverse_ok"] = all(prod_[a][b] == (1 if a == b else 0) for a in range(9) for b in range(9)) and all(D[a][b] >= 0 for a in range(9) for b in range(9))
    b = [Fraction(0)] * 9
    b[W3_FLIP_SITE] = c4
    ustar = [sum(D[x][y] * b[y] for y in range(9)) for x in range(9)]
    u = [Fraction(1)] * 9
    monotone, above = True, True
    for _ in range(ITERATIONS):
        Cu = [sum(C[x][y] * u[y] for y in range(9)) for x in range(9)]
        u_new = [Fraction(8, 9) * u[x] + Fraction(1, 9) * (Cu[x] + b[x]) for x in range(9)]
        monotone = monotone and all(u_new[x] <= u[x] for x in range(9))
        above = above and all(u_new[x] >= ustar[x] for x in range(9))
        u = u_new
    out["iterates_ok"] = monotone and above and max(u[x] - ustar[x] for x in range(9)) < TOLERANCE
    u_check = list(ustar)
    if mut("fixed_point_not_fixed"):
        u_check[W3_CENTER] += Fraction(1, 1000)
    Cu = [sum(C[x][y] * u_check[y] for y in range(9)) for x in range(9)]
    out["fixed_ok"] = all(Fraction(8, 9) * u_check[x] + Fraction(1, 9) * (Cu[x] + b[x]) == u_check[x] for x in range(9))
    bound = ustar[W3_CENTER]
    if mut("center_tv_exceeds_bound_forged"):
        bound = bound / 10
    out["bound"] = bound
    out["ustar"] = ustar
    out["D_center_row"] = D[W3_CENTER]
    return out


def family_d(checks: Checks, report: dict, exact: bool) -> None:
    fam = plaquette_family()
    plaq = {tr: plaquette_checks(tr, fam) for tr in WINDOW_TRIPLES}
    checks.check("D1", all(p["ineq_ok"] for p in plaq.values()), f"H1: plaquette one-step inequality TV <= c_1^(4) sum[differ] + b_x, {len(fam)} pairs x 4 sites")
    checks.check("D2", all(p["coupling_ok"] for p in plaq.values()), f"H1: maximal coupling identity sum_s min(a_s,b_s) = 1 - TV on {plaq[(2, 1, 2)]['instances']} instances, four triples")
    win = {tr: window_analysis(tr) for tr in WINDOW_TRIPLES}
    c4_ok = all(win[tr]["c4"] == C4_LITERALS[tr] for tr in WINDOW_TRIPLES)
    rs312 = win[(3, 1, 2)]["row_max"] / 4 if mut("row_sum_ignored") else win[(3, 1, 2)]["row_max"]
    checks.check("D3", c4_ok and all(win[tr]["row_max"] < 1 for tr in WINDOW_REGION) and rs312 >= 1, "H2: c_1^(4) = 1/8, 1404/11431, 10000/175641, 918/3431; 3x3 row sums < 1 at region triples, >= 1 at (3,1,2)")
    checks.check("D4", all(win[tr]["inverse_ok"] for tr in WINDOW_REGION), "H2: D = (I - C)^{-1} exact: D(I - C) = I, D >= 0, three region triples")
    checks.check("D5", all(win[tr]["iterates_ok"] for tr in WINDOW_REGION), f"H2: damped iterates from u^0 = 1 nonincreasing, >= u* = D b, within 10^-4 at step {ITERATIONS}")
    checks.check("D6", all(win[tr]["fixed_ok"] for tr in WINDOW_REGION), "H2: fixed-point identity u* = (8/9) u* + (1/9)(C u* + b) exact")
    tv_ok = win[(2, 1, 2)]["tv"] == CENTER_TV_LITERAL_212 and all(dec(win[tr]["tv"], 7) == "0." + CENTER_TV_LABELS[tr] for tr in WINDOW_REGION)
    bound_ok = all(win[tr]["bound"] == CENTER_BOUND_LITERALS[tr] and win[tr]["tv"] <= win[tr]["bound"] for tr in WINDOW_REGION)
    print("info 3x3 TV<=bound: " + "; ".join(f"({tr[0]},{tr[1]},{tr[2]}) {dec(win[tr]['tv'], 7)}<={win[tr]['bound']}" for tr in WINDOW_REGION))
    for tr in WINDOW_REGION:
        if exact:
            print(f"exact 3x3 {tr}: TV = {win[tr]['tv']}; u* = {[str(x) for x in win[tr]['ustar']]}; D center row = {[str(x) for x in win[tr]['D_center_row']]}")
    checks.check("D7", tv_ok and bound_ok, "H3: center-site TV <= (D b)_center at the three region triples; the literals")
    w = win[(3, 1, 2)]
    checks.check("D8", w["row_max"] >= 1 and 0 < w["tv"] < 1, f"H3: (3,1,2): 4c_1^(4) = {4 * w['c4']} > 1; window bound not asserted; TV(center)={dec(w['tv'], 7)} recorded only")
    report["D"] = {"plaquette": plaq, "window": win, "family_size": len(fam)}


# ==================================================================== family E
LINE_POINTS = (
    ("(t,1,1)", (T, sp.Integer(1), sp.Integer(1)), (Fraction(9, 8), Fraction(5, 4), Fraction(11, 8), Fraction(3, 2))),
    ("(t,t,1)", (T, T, sp.Integer(1)), (Fraction(9, 8), Fraction(5, 4), Fraction(11, 8))),
    ("(1,1,t)", (sp.Integer(1), sp.Integer(1), T), (Fraction(3, 4), Fraction(7, 8), Fraction(1))),
)
TABLE_L = 12
SMALL = Fraction(1, 1000)


def path_counts(n: int, directions: int):
    counts: dict = {}
    for seq in product(range(directions), repeat=n):
        pos = (0, 0, 0)
        for d in seq:
            v = MENU_VECTORS[d]
            pos = (pos[0] + v[0], pos[1] + v[1], pos[2] + v[2])
        counts[pos] = counts.get(pos, 0) + 1
    return counts


def family_e(checks: Checks, report: dict, exact: bool) -> None:
    directions = 5 if mut("path_count_wrong") else 6
    sums = {n: sum(path_counts(n, directions).values()) for n in range(1, 5)}
    checks.check("E1", all(sums[n] == 6 ** n for n in range(1, 5)), "I: sum_y N_n(0,y) = 6^n on Z^3, n = 1..4, by walk enumeration")
    vals = report["C"]["vals"]
    table_ok, least, tbl_parts = True, {}, []
    shift = 1 if mut("alpha_table_wrong_exponent") else 0
    for tr in REGION_TRIPLES:
        alpha = 6 * vals[tr][0]
        table = [alpha ** (L + shift) / (1 - alpha) for L in range(1, TABLE_L + 1)]
        table_ok = table_ok and table[0] == alpha / (1 - alpha) and all(table[L] == alpha * table[L - 1] for L in range(1, TABLE_L))
        power, L = alpha, 1
        while power / (1 - alpha) >= SMALL:
            power *= alpha
            L += 1
        least[tr] = (L, power / (1 - alpha), (power / alpha) / (1 - alpha))
        tbl_parts.append(f"({tr[0]},{tr[1]},{tr[2]}) a={dec(alpha, 4)} L12={dec(table[11], 6)} L={L}")
        if exact:
            print(f"exact table {tr}: alpha = {alpha}; " + "; ".join(f"L={L_ + 1} {v}" for L_, v in enumerate(table)))
    if exact:
        print("exact tbl a, L12, least L<10^-3: " + "; ".join(tbl_parts))
    checks.check("E2", table_ok, f"I: table alpha^L/(1-alpha), L = 1..{TABLE_L}, exact at the four region triples")
    checks.check("E3", all(v[1] < SMALL <= v[2] for v in least.values()), "I: least L with alpha^L/(1-alpha) < 10^-3 (>= at L-1): " + ", ".join(f"L={v[0]}" for v in least.values()))
    points_ok = True
    lines_out, pts_parts = [], []
    for name, line_sym, pts in LINE_POINTS:
        if mut("line_points_misclassified") and name == "(t,1,1)":
            pts = pts + (Fraction(13, 8),)
        vals_line = [(tval, coefficient(line_triple(line_sym, tval), 6)[0]) for tval in pts]
        points_ok = points_ok and all(6 * c < 1 for _, c in vals_line)
        lines_out.append((name, vals_line))
        pts_parts.append(f"{name} " + " ".join(f"{tval}:{dec(6 * c, 4)}" for tval, c in vals_line))
        if exact:
            print(f"exact region points {name}: " + ", ".join(f"t={tval} c_1={c}" for tval, c in vals_line))
    if exact:
        print("exact pts 6c_1: " + "; ".join(pts_parts))
    region_ok = all(6 * vals[tr][0] < 1 for tr in REGION_TRIPLES) and all(6 * vals[tr][0] >= 1 for tr in SILENT_TRIPLES)
    checks.check("E4", points_ok and region_ok, "region: 6c_1 < 1 at the region triples and the line points; >= 1 at (3,1,2), (5,2,4)")
    report["E"] = {"least": least, "points": lines_out}


# ==================================================================== family F
FENCES = (
    "This note states uniqueness only where the one-neighbor influence sum is less than one, at the declared points and throughout the verified intervals; at the three silent triples the criterion decides nothing, and nothing is stated there about one law or several.",
    "No formation order, formation law, plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "The criterion and the coupling method are classical references re-proved here at the scope used; no value, constant or theorem is imported as authority.",
    "Every negative sentence in this note is an exact statement on the declared windows, triples and lines or the scope sentence about the silent triples; none is a route no-go beyond that scope.",
)
FORBIDDEN = (
    "selects the physical rule", "derives the Born", "explains the gate", "bears on the gate",
    "infinite-lattice law", "the framework's action is", "the order is physical", "certified",
    "closed the gate", "axiom is amended", "fires wake condition",
    "distinct orders give distinct laws", "witnesses the variation clause",
    "washes out", "the physical order", "unique on the lattice", "the plane's static law is",
    "non-unique", "nonunique", "phase transition", "several static laws", "the physical rule", "outside every criterion",
    "unique at (3,1,2)", "unique at (5,2,4)", "unique at the silent", "exactly one static law at (3,1,2)", "exactly one static law at (5,2,4)",
)
CLAIM_INJECTIONS = {
    "claim_nonunique_at_silent": "At (3,1,2) the static law is non-unique.",
    "claim_unique_at_silent": "Hence the static law is unique at (3,1,2).",
    "claim_phase_transition": "The silent triples lie beyond a phase transition.",
    "claim_physical_rule": "The region triples give the physical rule.",
}
AUTHOR_NAME = "dobrushin"
AUTHOR_SECTIONS = ("Prior art", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def author_outside_allowed(note_text: str) -> list:
    parts = re.split(r"(?m)^## ", note_text)
    bad = []
    if AUTHOR_NAME in parts[0].lower():
        bad.append("<front matter or title>")
    for part in parts[1:]:
        heading = part.split("\n", 1)[0].strip()
        if AUTHOR_NAME in part.lower() and not heading.startswith(AUTHOR_SECTIONS):
            bad.append(heading)
    return bad


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    if mut("claim_author_in_theorem"):
        text = text.replace("\n## Theorem I", "\nBy Dobrushin's theorem the bound holds.\n## Theorem I", 1)
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the four fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase (hits: {hits})")
    bad = author_outside_allowed(text)
    checks.check("F3", not bad and len(text) > 0, f"the criterion's author is named only in the Prior art and Imports sections (violations: {bad})")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad_lines = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F4", not bad_lines and len(scan) > 500, f"runner source: no floating-point literal or conversion call ({len(bad_lines)} hits)")


# ==================================================================== family G
N5_LINES = (
    "per_element: executed — all 7776 x 15 pattern-and-pair choices at every triple, grid point, scan point and endpoint (252 multisets x 15 pairs in the certificates); every plaquette pair",
    "per_site: executed — the flipped neighbor in each of six directions; the plaquette inequality at each site; the 3x3 row sums and center marginals",
    "per_mode: executed — D = (I - C)^{-1} exactly with the damped iterates; Sturm isolation of each threshold as the unique positive root",
    "per_block: executed — the 3x3 window by integer row transfer under two exterior assignments; walk counts n <= 4; the table alpha^L/(1-alpha)",
    "lattice_wide: proved, not executed — uniqueness on Z^3 where 6c_1 < 1 is the corollary of the window and walk-count bounds; the silent triples are named, not decided",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", all(len(l) >= 40 for l in N5_LINES) and len(N5_LINES) == 5, "the five N5 resolution lines are printed (each >= 40 chars)")


# ======================================================================= main
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
    print("scope: six-projector menu, covariant product rule; c_1 exactly, the lines' two thresholds with certificates; the coupling bound on two windows; uniqueness only where 6c_1 < 1; silent at (3,1,2), (5,2,4)")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, note_text, axiom_text, b01_text, b02_text)
    family_b(checks, report)
    family_c(checks, report, exact)
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
