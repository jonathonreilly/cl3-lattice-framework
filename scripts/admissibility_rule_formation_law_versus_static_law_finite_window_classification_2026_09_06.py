#!/usr/bin/env python3
"""Exact checks: the formation law of a nearest-neighbor rule versus its static law.

Finite scope only.  The menu is the six Bloch-axis projectors inside M_2(C);
the windows are the three-site path, the four-site path, the four-site star,
the four-cycle (one plaquette) and the open 2x2x2 cube; the rules are the
product class (P) at declared exact weight triples and the sum rule (S) at
declared exact couplings.  The static law is the joint law whose full
conditionals are the rule with every neighbor recorded; the formation law is
the chain of the rule's conditionals along a formation order under the
records-only reading.  Theorem B (classification): the two laws coincide for
an order exactly when every site forms with at most one recorded neighbor.
Nothing infinite-volume is computed or claimed; no rule, coupling, order or
reading is selected.  Exact integer, rational and symbolic arithmetic only:
the runner scans its own source and fails if a floating-point literal or a
floating-point conversion call appears.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
UPSTREAM_BINARY_NOTE = (
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
CLAIM_ID = (
    "admissibility_rule_formation_law_versus_static_law_finite_window_"
    "classification_bounded_theorem_note_2026-09-06"
)

# ---------------------------------------------------------------- mutations
MUTATION_GATE = {
    "menu_drop_projector": "B",
    "rotation_improper": "B",
    "orbit_census_wrong": "B",
    "psi_nonconstant_passes": "B",
    "edge_flip_not_in_group": "B",
    "positivity_zero_entry_passes": "B",
    "static_mu_wrong_edge_weight": "C",
    "static_conditional_uses_two_hops": "C",
    "exterior_factor_dropped": "C",
    "compat_rank_off_by_one": "C",
    "sum_rule_pretends_consistent": "C",
    "brook_cycle_sign_flip": "C",
    "single_edge_sum_rule_inconsistent": "C",
    "formation_identity_drop_Zk": "D",
    "formation_uses_all_neighbors": "D",
    "formation_equals_static_on_cycle": "D",
    "one_neighbor_normalizer_wrong": "D",
    "fj_factorization_wrong": "D",
    "fj_j4_wrong": "D",
    "plaquette_lemma_skips_order": "D",
    "single_site_variation_constant": "D",
    "distinct_law_count_wrong": "D",
    "p4_census_wrong": "D",
    "constant_rule_varies": "D",
    "weights_collapsed_to_constant": "D",
    "menu_witness_varies_on_menu": "D",
    "asymmetric_identity_holds": "D",
    "absence_blind_nonconstant_passes": "E",
    "absence_extension_solution_forged": "E",
    "order_mixture_equals_static": "E",
    "marginal_reading_is_fixed_rule": "E",
    "marginal_chain_rule_broken": "E",
    "psi_rank_deficient": "E",
    "z2_rank_one": "E",
    "claim_rule_selected": "F",
    "claim_born_derived": "F",
    "claim_gate_explained": "F",
    "claim_infinite_volume": "F",
    "claim_action_identified": "F",
    "claim_axiom_amended": "F",
    "claim_order_physical": "F",
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


# --------------------------------------------------------------------- menu
# Menu order: P(+e_x), P(-e_x), P(+e_y), P(-e_y), P(+e_z), P(-e_z).
MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
MENU_LABELS = ("P(+x)", "P(-x)", "P(+y)", "P(-y)", "P(+z)", "P(-z)")
PAR, ANTI, ORTH = 0, 1, 2
ORBIT_NAMES = ("par", "anti", "orth")


def vdot(a: int, b: int) -> int:
    return sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))


def orbit(a: int, b: int) -> int:
    d = vdot(a, b)
    return PAR if d == 1 else (ANTI if d == -1 else ORTH)


def phi_table(triple):
    return tuple(tuple(triple[orbit(a, b)] for b in range(M)) for a in range(M))


TRIPLES = ((3, 1, 2), (5, 2, 4))
CONSTANT_TRIPLE = (2, 2, 2)
REF = 0  # the reference value P(+e_x)

# ---------------------------------------------------------------- rotations
def permutation_sign(perm) -> int:
    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inv % 2 else 1


def signed_permutations(proper: bool):
    out = []
    for perm in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            det = permutation_sign(perm) * signs[0] * signs[1] * signs[2]
            if (det == 1) == proper:
                out.append((perm, signs))
    return tuple(out)


ROTATIONS = signed_permutations(True)


def rotate_vector(rot, vec):
    perm, signs = rot
    out = [0, 0, 0]
    for i in range(3):
        out[perm[i]] = signs[i] * vec[i]
    return tuple(out)


def rotate_menu(rot, a: int) -> int:
    return MENU_VECTORS.index(rotate_vector(rot, MENU_VECTORS[a]))


def compose(r1, r2):
    """r1 after r2 as signed permutations."""
    p1, s1 = r1
    p2, s2 = r2
    perm = tuple(p1[p2[i]] for i in range(3))
    signs = tuple(s2[i] * s1[p2[i]] for i in range(3))
    return (perm, signs)


# ------------------------------------------------------------------ windows
def cube_edges():
    return tuple((a, b) for a in range(8) for b in range(a + 1, 8) if bin(a ^ b).count("1") == 1)


WINDOWS = {
    "path3": ((0, 1), (1, 2)),
    "P4": ((0, 1), (1, 2), (2, 3)),
    "star4": ((0, 1), (0, 2), (0, 3)),
    "cycle4": ((0, 1), (1, 2), (2, 3), (3, 0)),
    "cube8": cube_edges(),
}
SIZES = {"path3": 3, "P4": 4, "star4": 4, "cycle4": 4, "cube8": 8}
# cycle4 exterior: two exterior neighbors per site carrying P(+e_x) and P(-e_y)
CYCLE4_EXTERIOR = {x: (0, 3) for x in range(4)}
# cube8 exterior: the exterior neighbor along axis a carries P(+e_a)
CUBE8_EXTERIOR = {x: (0, 2, 4) for x in range(8)}


def neighbors(edges, n):
    N = {i: [] for i in range(n)}
    for i, j in edges:
        N[i].append(j)
        N[j].append(i)
    return {i: tuple(sorted(v)) for i, v in N.items()}


def static_weight(v, edges, phi, exterior=None):
    w = 1
    for i, j in edges:
        w *= phi[v[i]][v[j]]
    if exterior:
        for x, vals in exterior.items():
            for o in vals:
                w *= phi[v[x]][o]
    return w


def rule_numerators(s_values, recorded_values, phi):
    """Product-rule numerators Prod_y phi(s, eta_y) for each s (psi constant)."""
    out = []
    for s in s_values:
        t = 1
        for e in recorded_values:
            t *= phi[s][e]
        out.append(t)
    return out


def formation_law(edges, n, phi, order, all_neighbors=False, drop_Zk=False):
    """mu_sigma under the records-only reading; returns dict config -> Fraction."""
    N = neighbors(edges, n)
    law = {}
    for v in product(range(M), repeat=n):
        num = 1
        den = 1
        formed = set()
        for x in order:
            A = N[x] if all_neighbors else tuple(y for y in N[x] if y in formed)
            vals = tuple(v[y] for y in A)
            num *= rule_numerators((v[x],), vals, phi)[0]
            if not drop_Zk:
                den *= sum(rule_numerators(range(M), vals, phi))
            formed.add(x)
        law[v] = Fraction(num, den)
    return law


def normalizer_product(edges, n, phi, order, v):
    N = neighbors(edges, n)
    formed = set()
    tot = 1
    for x in order:
        vals = tuple(v[y] for y in N[x] if y in formed)
        tot *= sum(rule_numerators(range(M), vals, phi))
        formed.add(x)
    return tot


def max_recorded(edges, n, order, skip_previous=False):
    N = neighbors(edges, n)
    formed = []
    mx = 0
    for x in order:
        pool = formed[:-1] if skip_previous else formed
        c = sum(1 for y in N[x] if y in pool)
        mx = max(mx, c)
        formed.append(x)
    return mx


def bareiss_rank(rows, ncols):
    """Exact rank of an integer matrix by fraction-free elimination."""
    A = [list(r) for r in rows]
    m = len(A)
    rank = 0
    prev = 1
    for col in range(ncols):
        piv = None
        for i in range(rank, m):
            if A[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        pr = A[rank]
        pv = pr[col]
        for i in range(rank + 1, m):
            ri = A[i]
            f = ri[col]
            A[i] = [(pv * a - f * b) // prev for a, b in zip(ri, pr)]
        prev = pv
        rank += 1
        if rank == ncols:
            break
    return rank


def normalize_text(text: str) -> str:
    return " ".join(text.split())


# ==================================================================== family A
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "is determined by, and varies with, the nearest-neighbor conditions",
    "Records form.",
    "records are permanent",
    "Only records are readable.",
    "A site with no record cannot be read.",
)


def family_a(checks: Checks, note_text: str, axiom_text: str) -> None:
    checks.check(
        "A1",
        all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 2,
        "both declared audit inputs exist",
    )
    flat = normalize_text(axiom_text)
    for k, needle in enumerate(AXIOM_NEEDLES, start=2):
        checks.check(
            f"A{k}",
            needle in flat,
            f"axiom memo contains: {needle[:38]}",
        )
    checks.check("A8", CLAIM_ID in note_text, "the note carries its claim id")
    checks.check(
        "A9",
        (ROOT / UPSTREAM_BINARY_NOTE).is_file(),
        "upstream binary note exists (presence only)",
    )


# ==================================================================== family B
def sympy_projectors():
    one = sp.Integer(1)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    half = sp.Rational(1, 2)
    P = []
    for sig in (sx, sy, sz):
        P.append(half * (ident + sig) * one)
        P.append(half * (ident - sig) * one)
    return P, (sx, sy, sz), ident


def conj_map(U, P):
    return sp.simplify(U * P * U.H)


def nullity_of_equations(eq_rows, nunk) -> int:
    rank = bareiss_rank(eq_rows, nunk) if eq_rows else 0
    return nunk - rank


def family_b(checks: Checks) -> None:
    P, (sx, sy, sz), ident = sympy_projectors()
    checks.check(
        "B1",
        all(sp.simplify(p - p.H) == sp.zeros(2) and sp.simplify(p * p - p) == sp.zeros(2) and sp.simplify(p.trace()) == 1 for p in P),
        "six projectors Hermitian, idempotent, trace one (sympy exact)",
    )
    menu_b = list(range(M if not mut("menu_drop_projector") else M - 1))
    census = {}
    trace_by_orbit = {}
    for a in menu_b:
        for b in menu_b:
            tr = sp.simplify((P[a] * P[b]).trace())
            o = orbit(a, b)
            if mut("orbit_census_wrong") and o == ANTI:
                o = ORTH
            census[o] = census.get(o, 0) + 1
            trace_by_orbit.setdefault(o, set()).add(tr)
    checks.check(
        "B2",
        census == {PAR: 6, ANTI: 6, ORTH: 24}
        and trace_by_orbit == {PAR: {1}, ANTI: {0}, ORTH: {sp.Rational(1, 2)}},
        f"pair orbits by Tr(PP') in (1, 0, 1/2): census {tuple(census.get(o, 0) for o in (PAR, ANTI, ORTH))}",
    )
    rots_b = signed_permutations(not mut("rotation_improper"))
    dets = {permutation_sign(pm) * s[0] * s[1] * s[2] for pm, s in rots_b}
    closed = all(compose(r1, r2) in rots_b for r1 in rots_b for r2 in rots_b)
    checks.check(
        "B3",
        len(rots_b) == 24 and len(set(rots_b)) == 24 and dets == {1} and closed,
        "24 proper signed axis permutations: det +1, closed, order 24",
    )
    images = {a: {rotate_menu(r, a) for r in rots_b} for a in menu_b}
    checks.check(
        "B4",
        all({rotate_menu(r, a) for a in menu_b} == set(menu_b) for r in rots_b)
        and all(images[a] == set(range(M)) for a in menu_b),
        "every rotation permutes the menu; action transitive",
    )
    Uz = sp.diag(sp.exp(-sp.I * sp.pi / 4), sp.exp(sp.I * sp.pi / 4))
    checks.check(
        "B5",
        conj_map(Uz, P[0]) == P[2] and conj_map(Uz, P[2]) == P[1]
        and conj_map(Uz, P[4]) == P[4] and conj_map(Uz, P[5]) == P[5]
        and sp.simplify(Uz * Uz.H) == ident,
        "U_z spinor: P(e_x)->P(e_y), P(e_y)->P(-e_x), fixes P(+-e_z)",
    )
    U3 = (ident - sp.I * (sx + sy + sz)) / 2
    checks.check(
        "B6",
        conj_map(U3, P[0]) == P[2] and conj_map(U3, P[2]) == P[4] and conj_map(U3, P[4]) == P[0]
        and sp.simplify(U3 * U3.H) == ident,
        "U_3 = (I - i(sx+sy+sz))/2 unitary, cycles P(e_x)->P(e_y)->P(e_z)",
    )
    rots_psi = rots_b[:1] if mut("psi_nonconstant_passes") else rots_b
    rows = []
    for r in rots_psi:
        for a in range(M):
            row = [0] * M
            row[a] += 1
            row[rotate_menu(r, a)] -= 1
            if any(row):
                rows.append(row)
    checks.check(
        "B7",
        nullity_of_equations(rows, M) == 1,
        "covariant site weight: solution space dimension 1 (constant)",
    )
    idx = {(a, b): a * M + b for a in range(M) for b in range(M)}
    rows = []
    for r in rots_b:
        for a in range(M):
            for b in range(M):
                row = [0] * (M * M)
                row[idx[(a, b)]] += 1
                row[idx[(rotate_menu(r, a), rotate_menu(r, b))]] -= 1
                if any(row):
                    rows.append(row)
    for a in range(M):
        for b in range(M):
            row = [0] * (M * M)
            row[idx[(a, b)]] += 1
            row[idx[(b, a)]] -= 1
            if any(row):
                rows.append(row)
    checks.check(
        "B8",
        nullity_of_equations(rows, M * M) == 3,
        "covariant symmetric pair weight: exactly three orbit values",
    )
    R_flip = ((0, 1, 2), (-1, 1, -1)) if not mut("edge_flip_not_in_group") else ((0, 1, 2), (-1, 1, 1))
    e1 = (1, 0, 0)
    g0 = tuple(x + y for x, y in zip(rotate_vector(R_flip, (0, 0, 0)), e1))
    g1 = tuple(x + y for x, y in zip(rotate_vector(R_flip, e1), e1))
    sym_ok = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        for a in range(M):
            for b in range(M):
                ra, rb = rotate_menu(R_flip, a), rotate_menu(R_flip, b)
                sym_ok = sym_ok and phi[a][b] == phi[rb][ra] == phi[b][a]
    checks.check(
        "B9",
        R_flip in ROTATIONS and g0 == e1 and g1 == (0, 0, 0) and sym_ok,
        "edge flip t_{e1} o R_{e2,pi} is in the group, swaps 0 and e1; phi(a,b) = phi(rho b, rho a) = phi(b,a) on 36 pairs",
    )
    positive = True
    for triple in TRIPLES:
        phi = [list(r) for r in phi_table(triple)]
        if mut("positivity_zero_entry_passes"):
            phi[1][2] = 0
        for name in ("path3", "star4", "cycle4"):
            N = neighbors(WINDOWS[name], SIZES[name])
            for x in range(SIZES[name]):
                nb = N[x]
                for mask in range(1 << len(nb)):
                    A = [nb[i] for i in range(len(nb)) if mask >> i & 1]
                    for eta in product(range(M), repeat=len(A)):
                        nums = rule_numerators(range(M), eta, phi)
                        positive = positive and all(t > 0 for t in nums)
    checks.check(
        "B10",
        positive,
        "positivity: every r(s | eta) > 0 for every partial eta at the declared triples",
    )


# ==================================================================== family C
def full_conditionals_match(name, phi, configs, exterior_mu=None, exterior_rule=None, two_hops=False, bad_edge=False):
    edges = WINDOWS[name]
    n = SIZES[name]
    N = neighbors(edges, n)
    N2 = {x: tuple(sorted({z for y in N[x] for z in N[y] if z != x} | set(N[x]))) for x in range(n)}
    for v in configs:
        for x in range(n):
            ws = []
            for s in range(M):
                vs = v[:x] + (s,) + v[x + 1:]
                w = static_weight(vs, edges, phi, exterior_mu)
                if bad_edge:
                    i, j = edges[0]
                    w *= phi[vs[i]][vs[j]]
                ws.append(w)
            recorded = [v[y] for y in (N2[x] if two_hops else N[x])]
            if exterior_rule:
                recorded += list(exterior_rule[x])
            nums = rule_numerators(range(M), recorded, phi)
            Zs, Zr = sum(ws), sum(nums)
            for s in range(M):
                if Fraction(ws[s], Zs) != Fraction(nums[s], Zr):
                    return False
    return True


def cube_configuration_family():
    fam = {(REF,) * 8}
    for i in range(8):
        for s in range(M):
            if s != REF:
                v = [REF] * 8
                v[i] = s
                fam.add(tuple(v))
    for i in range(8):
        for j in range(i + 1, 8):
            for s in range(M):
                for t in range(M):
                    if s != REF and t != REF:
                        v = [REF] * 8
                        v[i], v[j] = s, t
                        fam.add(tuple(v))
    state = 20260906
    sample = []
    for _ in range(300):
        v = []
        for _k in range(8):
            state = (1103515245 * state + 12345) % (2 ** 31)
            v.append((state >> 16) % M)
        sample.append(tuple(v))
    return tuple(sorted(fam)) + tuple(sample)


def compat_rows(edges, n, numerators_of):
    """Rows of the homogeneous system mu(v) Z_x - num_x(v) sum_t mu(v^{x->t}) = 0."""
    N = neighbors(edges, n)
    configs = list(product(range(M), repeat=n))
    idx = {v: i for i, v in enumerate(configs)}
    rows = []
    for v in configs:
        for x in range(n):
            nums = numerators_of([v[y] for y in N[x]])
            Z = sum(nums)
            row = [0] * len(configs)
            row[idx[v]] += Z
            for t in range(M):
                row[idx[v[:x] + (t,) + v[x + 1:]]] -= nums[v[x]]
            rows.append(row)
    return rows, configs


def sum_rule_numerators(lam_num, lam_den):
    def f(recorded):
        nums = [lam_den + lam_num * sum(vdot(s, y) for y in recorded) for s in range(M)]
        assert all(t > 0 for t in nums), "sum rule positivity bound |lambda| < 1/deg violated"
        return nums
    return f


def brook_cycle(rule):
    """Brook cycle at sites 1-2 of path3: a=P(e_x)->a'=P(-e_x) at the end site, b=P(e_x)->b'=P(-e_x) at the middle, c=P(e_x)."""
    a, a2, b, b2, c = 0, 1, 0, 1, 0
    num = rule(a2, [b]) * rule(b2, [a2, c]) * rule(a, [b2]) * rule(b, [a, c])
    den = rule(a, [b]) * rule(b, [a2, c]) * rule(a2, [b2]) * rule(b2, [a, c])
    if mut("brook_cycle_sign_flip"):
        num, den = num * rule(a, [b]) ** 2, den * rule(a2, [b]) ** 2
    return sp.cancel(num / den)


def family_c(checks: Checks) -> None:
    cube_family = cube_configuration_family()
    ok_exh = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        for name in ("path3", "P4", "star4", "cycle4"):
            configs = list(product(range(M), repeat=SIZES[name]))
            ok_exh = ok_exh and full_conditionals_match(
                name, phi, configs,
                two_hops=mut("static_conditional_uses_two_hops"),
                bad_edge=mut("static_mu_wrong_edge_weight"),
            )
    checks.check(
        "C1",
        ok_exh,
        "Theorem A: full conditionals of the static law equal the rule on path3/P4/star4/cycle4 (all v, x, s; both triples)",
    )
    ok_ext = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        configs = list(product(range(M), repeat=4))
        ok_ext = ok_ext and full_conditionals_match(
            "cycle4", phi, configs,
            exterior_mu=None if mut("exterior_factor_dropped") else CYCLE4_EXTERIOR,
            exterior_rule=CYCLE4_EXTERIOR,
        )
    checks.check(
        "C2",
        ok_ext,
        "cycle4 with exterior records P(+e_x), P(-e_y): full conditionals equal the rule with exterior records",
    )
    ok_cube = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        ok_cube = ok_cube and full_conditionals_match("cube8", phi, cube_family)
        ok_cube = ok_cube and full_conditionals_match("cube8", phi, cube_family, exterior_mu=CUBE8_EXTERIOR, exterior_rule=CUBE8_EXTERIOR)
    checks.check(
        "C3",
        ok_cube and len(cube_family) == 1041,
        "cube8: full-conditional identity on the family (741 near-reference + 300 LCG), with and without exterior",
    )
    ok_pos = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        for name in ("path3", "P4", "star4", "cycle4"):
            ok_pos = ok_pos and all(static_weight(v, WINDOWS[name], phi) > 0 for v in product(range(M), repeat=SIZES[name]))
        ok_pos = ok_pos and all(static_weight(v, WINDOWS["cube8"], phi) > 0 for v in cube_family)
    checks.check("C4", ok_pos, "positive rule => positive static law on the declared windows (cube8 on its family)")
    phi = phi_table(TRIPLES[0])
    rows, configs = compat_rows(WINDOWS["path3"], 3, lambda rec: rule_numerators(range(M), rec, phi))
    if mut("compat_rank_off_by_one"):
        rows.append([1] + [0] * (len(configs) - 1))
    witness = [static_weight(v, WINDOWS["path3"], phi) for v in configs]
    rank = bareiss_rank(rows, len(configs))
    in_null = all(sum(a * b for a, b in zip(row, witness)) == 0 for row in rows)
    checks.check(
        "C5",
        len(rows) >= 648 and len(configs) == 216 and rank == 215 and in_null and all(w > 0 for w in witness),
        f"Brook uniqueness on path3 (3,1,2): {len(rows)}x216 compatibility system, exact rank {rank} (Bareiss), mu spans the nullspace, positive",
    )
    ranks = {}
    for lam in ((1, 4), (-1, 8)):
        f = (lambda rec: rule_numerators(range(M), rec, phi)) if mut("sum_rule_pretends_consistent") else sum_rule_numerators(*lam)
        rows_s, _ = compat_rows(WINDOWS["path3"], 3, f)
        ranks[lam] = bareiss_rank(rows_s, 216)
    checks.check(
        "C6",
        ranks == {(1, 4): 216, (-1, 8): 216},
        f"sum rule inconsistent on path3: compatibility rank {tuple(ranks.values())} = 216 at lambda 1/4, -1/8 (|lambda| < 1/deg)",
    )
    ok_edge = True
    for lam in ((1, 4), (-1, 8)):
        edges, n = (WINDOWS["path3"], 3) if mut("single_edge_sum_rule_inconsistent") else (((0, 1),), 2)
        rows_e, configs_e = compat_rows(edges, n, sum_rule_numerators(*lam))
        nullity = len(configs_e) - bareiss_rank(rows_e, len(configs_e))
        law = [lam[1] + lam[0] * vdot(v[0], v[1]) for v in configs_e]
        in_null_e = all(sum(a * b for a, b in zip(row, law)) == 0 for row in rows_e)
        ok_edge = ok_edge and nullity == 1 and in_null_e and sum(law) == 36 * lam[1]
    checks.check(
        "C7",
        ok_edge,
        "single edge: the sum rule is consistent (nullity 1, law (1 + lambda<s,t>)/36) at both couplings",
    )
    lam = sp.symbols("lambda")

    def rule_sum(s, rec):
        w = [1 + lam * sum(vdot(t, y) for y in rec) for t in range(M)]
        return w[s] / sum(w)

    Rl = brook_cycle(rule_sum)
    numer, denom = sp.fraction(sp.factor(Rl - 1))
    poly = sp.Poly(numer, lam)
    other_roots = [rt for rt in sp.roots(poly, lam) if rt != 0]
    checks.check(
        "C8",
        Rl.subs(lam, sp.Rational(1, 4)) == sp.Rational(27, 25)
        and sp.rem(poly, sp.Poly(lam ** 2, lam)).is_zero
        and all(abs(rt) >= sp.Rational(1, 6) for rt in other_roots)
        and denom.subs(lam, sp.Rational(1, 4)) != 0,
        f"sum-rule Brook cycle: R(1/4) = 27/25, R - 1 = {sp.factor(Rl - 1)}; lambda^2 divides, no other root in |lambda| < 1/6",
    )
    P_, Q_, R_ = sp.symbols("p q r", positive=True)
    phis = [[(P_, Q_, R_)[orbit(a, b)] for b in range(M)] for a in range(M)]

    def rule_prod(s, rec):
        w = [sp.Mul(*[phis[t][y] for y in rec]) if rec else sp.Integer(1) for t in range(M)]
        return w[s] / sum(w)

    checks.check(
        "C9",
        sp.simplify(brook_cycle(rule_prod) - 1) == 0,
        "the same Brook cycle for the product rule with symbolic (p, q, r) is exactly 1",
    )


# ==================================================================== family D
FAMILY_D_WINDOWS = ("path3", "P4", "star4", "cycle4")
EXPECTED_EQUAL = {"path3": 4, "P4": 8, "star4": 12, "cycle4": 0}
EXPECTED_CLASSES = {"path3": 2, "P4": 3, "star4": 5, "cycle4": 4}


def fj_symbolic(j, P_, Q_, R_):
    phis = [[(P_, Q_, R_)[orbit(a, b)] for b in range(M)] for a in range(M)]
    out = {}
    for v in range(M):
        expo = j + 2 if (mut("fj_j4_wrong") and j == 4) else j
        out.setdefault(orbit(v, REF), sp.expand(sum(phis[s][v] * phis[s][REF] ** expo for s in range(M))))
    return out


def cube_order_family():
    N = neighbors(WINDOWS["cube8"], 8)
    bfs, seen, queue = [], {0}, [0]
    while queue:
        x = queue.pop(0)
        bfs.append(x)
        for y in N[x]:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    dfs, seen = [], set()

    def visit(x):
        seen.add(x)
        dfs.append(x)
        for y in N[x]:
            if y not in seen:
                visit(y)

    visit(0)
    return {
        "identity": tuple(range(8)),
        "reverse": tuple(range(7, -1, -1)),
        "bfs0": tuple(bfs),
        "dfs0": tuple(dfs),
        "declared_a": (0, 3, 5, 6, 1, 2, 4, 7),
        "declared_b": (0, 7, 1, 6, 2, 5, 3, 4),
    }


def family_d(checks: Checks, report: dict) -> None:
    triples = TRIPLES if not mut("weights_collapsed_to_constant") else (CONSTANT_TRIPLE, TRIPLES[1])
    windows = dict(WINDOWS)
    if mut("p4_census_wrong"):
        windows["P4"] = ((0, 1), (1, 2), (1, 3))
    ok_ident = ok_norm = ok_cons = ok_class = ok_census = True
    census_lines = []
    for triple in triples:
        phi = phi_table(triple)
        for name in FAMILY_D_WINDOWS:
            edges, n = windows[name], SIZES[name]
            configs = list(product(range(M), repeat=n))
            ZW = sum(static_weight(v, edges, phi) for v in configs)
            mu = {v: Fraction(static_weight(v, edges, phi), ZW) for v in configs}
            classes: dict = {}
            equal_orders = []
            for order in permutations(range(n)):
                law = formation_law(edges, n, phi, order, all_neighbors=mut("formation_uses_all_neighbors"), drop_Zk=mut("formation_identity_drop_Zk"))
                if mut("formation_equals_static_on_cycle") and name == "cycle4":
                    law = dict(mu)
                prods = {v: normalizer_product(edges, n, phi, order, v) for v in configs}
                ok_ident = ok_ident and all(law[v] * prods[v] == mu[v] * ZW for v in configs)
                ok_norm = ok_norm and sum(law.values()) == 1
                ok_cons = ok_cons and sum(law[v] * prods[v] for v in configs) == ZW
                equal = law == mu
                ok_class = ok_class and (equal == (max_recorded(edges, n, order) <= 1))
                if equal:
                    equal_orders.append(order)
                key = sum(law.values()) if mut("distinct_law_count_wrong") else tuple(law[v] for v in configs)
                classes.setdefault(key, []).append(order)
            expected_orders = None
            if name == "path3":
                expected_orders = [(0, 1, 2), (1, 0, 2), (1, 2, 0), (2, 1, 0)]
            if name == "star4":
                expected_orders = [o for o in permutations(range(4)) if o.index(0) <= 1]
            ok_class = ok_class and len(equal_orders) == EXPECTED_EQUAL[name]
            if expected_orders is not None:
                ok_class = ok_class and sorted(equal_orders) == sorted(expected_orders)
            ok_census = ok_census and len(classes) == EXPECTED_CLASSES[name]
            sizes = sorted((len(v) for v in classes.values()), reverse=True)
            census_lines.append(f"{name}{triple}: {len(equal_orders)} equal, {len(classes)} laws, class sizes {sizes}")
            report.setdefault("classes", {})[(name, triple)] = sorted(classes.values(), key=len, reverse=True)
    checks.check("D1", ok_ident, "B1 identity mu_sigma prod Z_k = mu Z_W for every order, v, window, triple")
    checks.check("D2", ok_norm, "every formation law sums to one")
    checks.check("D3", ok_cons, "consistency line Z_W = sum_v mu_sigma prod Z_k (not a theorem)")
    checks.check("D4", ok_class, f"B2: mu_sigma = mu iff max|A_k| <= 1; equal orders path3/P4/star4/cycle4 = {tuple(EXPECTED_EQUAL.values())}")
    checks.check("D5", ok_census, "B5 census of distinct formation laws path3/P4/star4/cycle4 = (2, 3, 5, 4); class sizes " + "; ".join(l.split("class sizes ")[1] for l in census_lines[:4]))
    report["census_lines"] = census_lines
    P_, Q_, R_ = sp.symbols("p q r", positive=True)
    ok_fj = True
    for j in range(1, 6):
        f = fj_symbolic(j, P_, Q_, R_)
        pred = {
            PAR: P_ ** (j + 1) + Q_ ** (j + 1) + 4 * R_ ** (j + 1),
            ANTI: P_ * Q_ ** j + Q_ * P_ ** j + 4 * R_ ** (j + 1),
            ORTH: (P_ + Q_) * R_ ** j + R_ * (P_ ** j + Q_ ** j) + 2 * R_ ** (j + 1),
        }
        fac1 = (P_ - Q_) * (P_ ** j - Q_ ** j) if not mut("fj_factorization_wrong") else (P_ - Q_) * (P_ ** j + Q_ ** j)
        fac2 = (P_ - R_) * (Q_ ** j - R_ ** j) + (Q_ - R_) * (P_ ** j - R_ ** j)
        ok_fj = ok_fj and all(sp.expand(f[o] - pred[o]) == 0 for o in (PAR, ANTI, ORTH))
        ok_fj = ok_fj and sp.expand(f[PAR] - f[ANTI] - fac1) == 0 and sp.expand(f[ANTI] - f[ORTH] - fac2) == 0
        ok_fj = ok_fj and sp.expand((f[ANTI] - f[ORTH]).subs(Q_, P_) - 2 * (P_ - R_) * (P_ ** j - R_ ** j)) == 0
    checks.check("D6", ok_fj, "f_j formulas and factorizations symbolic, j = 1..5; at p = q: 2(p-r)(p^j-r^j)")
    phis = [[(P_, Q_, R_)[orbit(a, b)] for b in range(M)] for a in range(M)]
    if mut("one_neighbor_normalizer_wrong"):
        phis[4][0] = Q_
    Z1 = {sp.expand(sum(phis[s][t] for s in range(M))) for t in range(M)}
    checks.check("D7", Z1 == {P_ + Q_ + 4 * R_}, "one-neighbor normalizer p + q + 4r for every menu value (symbolic)")
    edges8, N8 = WINDOWS["cube8"], neighbors(WINDOWS["cube8"], 8)
    dist: dict = {}
    for order in permutations(range(8)):
        mx = max_recorded(edges8, 8, order, skip_previous=mut("plaquette_lemma_skips_order"))
        dist[mx] = dist.get(mx, 0) + 1
    checks.check("D8", dist == {3: 40320}, f"cube8: all 40320 orders have some |A_k| >= 2; max|A_k| distribution {dist}")
    report["cube_dist"] = dist
    family = cube_configuration_family()
    orders8 = cube_order_family()
    ok_cube_ident = ok_var = True
    var_lines = []
    for triple in TRIPLES:
        phi = phi_table(triple)
        ZW8 = None
        for oname, order in orders8.items():
            for v in family:
                law_num = 1
                formed = set()
                for x in order:
                    vals = tuple(v[y] for y in N8[x] if y in formed)
                    law_num *= rule_numerators((v[x],), vals, phi)[0]
                    formed.add(x)
                ok_cube_ident = ok_cube_ident and law_num == static_weight(v, edges8, phi)
            formed, m_site, y_site, js = [], None, None, []
            for x in order:
                A = tuple(yy for yy in N8[x] if yy in formed)
                if len(A) >= 2 and m_site is None:
                    m_site, y_site = x, A[0]
                formed.append(x)
            formed = []
            for x in order:
                A = tuple(yy for yy in N8[x] if yy in formed)
                if y_site in A and len(A) >= 2:
                    js.append(len(A) - 1)
                formed.append(x)
            values = {}
            for t in range(M):
                v = [REF] * 8
                v[y_site] = REF if mut("single_site_variation_constant") else t
                values[orbit(t, REF)] = normalizer_product(edges8, 8, phi, order, tuple(v))
            v0 = [REF] * 8
            base = normalizer_product(edges8, 8, phi, order, tuple(v0))
            fj_num = {}
            for o in (PAR, ANTI, ORTH):
                tot = 1
                for j in js:
                    f = fj_symbolic(j, P_, Q_, R_)[o]
                    tot *= f.subs({P_: triple[0], Q_: triple[1], R_: triple[2]})
                fj_num[o] = tot
            const = Fraction(base, int(fj_num[PAR]))
            predicted = {o: const * int(fj_num[o]) for o in (PAR, ANTI, ORTH)}
            distinct = len(set(values.values()))
            ok_var = ok_var and distinct == 3 and all(Fraction(values[o]) == predicted[o] for o in values)
            var_lines.append(f"{oname}{triple}: m={m_site} y={y_site} js={js} values={tuple(values[o] for o in (PAR, ANTI, ORTH))}")
    report["var_lines"] = var_lines
    checks.check("D9", ok_cube_ident and ok_var, "cube8 six declared orders: identity on the family; single-site variation: three values = const * prod f_j")
    ctriple = CONSTANT_TRIPLE if not mut("constant_rule_varies") else (2, 2, 3)
    phic = phi_table(ctriple)
    uniform = True
    for k in (1, 2):
        for eta in product(range(M), repeat=k):
            nums = rule_numerators(range(M), eta, phic)
            uniform = uniform and len(set(nums)) == 1
    all_equal = True
    for name in ("path3", "cycle4"):
        edges, n = WINDOWS[name], SIZES[name]
        configs = list(product(range(M), repeat=n))
        ZW = sum(static_weight(v, edges, phic) for v in configs)
        mu = {v: Fraction(static_weight(v, edges, phic), ZW) for v in configs}
        all_equal = all_equal and all(formation_law(edges, n, phic, order) == mu for order in permutations(range(n)))
    checks.check("D10", uniform and all_equal, "B4 constant rule (2,2,2): uniform under every 1- and 2-neighbor condition; mu_sigma = mu for all orders of path3, cycle4")

    def f_witness(x):
        val = 1 + x * x * (1 - x * x)
        return val + x * x if mut("menu_witness_varies_on_menu") else val

    vals = tuple(f_witness(Fraction(x)) for x in (1, -1, 0)) + (f_witness(Fraction(1, 2)),)
    half_sq = 1 + Fraction(1, 2) * (1 - Fraction(1, 2))
    induced = tuple(int(v) for v in vals[:3]) if all(v.denominator == 1 for v in vals[:3]) else vals[:3]
    ok_menu = vals == (1, 1, 1, Fraction(19, 16)) and half_sq == Fraction(5, 4) and induced == (1, 1, 1)
    if ok_menu:
        phi1 = phi_table(induced)
        configs = list(product(range(M), repeat=4))
        mu1 = {v: Fraction(1, 6 ** 4) for v in configs}
        ok_menu = all(formation_law(WINDOWS["cycle4"], 4, phi1, order) == mu1 for order in permutations(range(4)))
    checks.check("D11", ok_menu, f"menu witness f(x) = 1 + x^2(1-x^2) at (1,-1,0,1/2) = {tuple(str(v) for v in vals)}, x^2 = 1/2: {half_sq}; induced (1,1,1); mu_sigma = mu on cycle4")
    phi_a = [[phi_table(TRIPLES[0])[a][b] + (1 if a < b else 0) for b in range(M)] for a in range(M)]
    if mut("asymmetric_identity_holds"):
        phi_a = [list(r) for r in phi_table(TRIPLES[0])]
    edges, n = WINDOWS["path3"], 3
    configs = list(product(range(M), repeat=n))
    ZWa = sum(static_weight(v, edges, phi_a) for v in configs)
    fails = 0
    for order in permutations(range(n)):
        law = formation_law(edges, n, phi_a, order)
        if any(law[v] * normalizer_product(edges, n, phi_a, order, v) != Fraction(static_weight(v, edges, phi_a), ZWa) * ZWa for v in configs):
            fails += 1
    checks.check("D12", fails > 0 and any(phi_a[a][b] != phi_a[b][a] for a in range(M) for b in range(M)), f"asymmetric pair weight on path3: the identity fails for {fails} of 6 orders")


# ==================================================================== family E
PLAQUETTE_POS = {0: (0, 0, 0), 1: (1, 0, 0), 2: (1, 1, 0), 3: (0, 1, 0)}
PATH3_POS = {0: (0, 0, 0), 1: (1, 0, 0), 2: (2, 0, 0)}


def absence_factor(s, d, A_, B_, C_):
    dd = sum(x * y for x, y in zip(MENU_VECTORS[s], d))
    return A_ if dd == 1 else (B_ if dd == -1 else C_)


def absence_ratio_equations(name, pos, order, phis, absym, ZW):
    """Equations Z_W * prod alpha_k - prod Z_k = 0 for mu_sigma = mu on the declared configuration set."""
    edges, n = WINDOWS[name], SIZES[name]
    N = neighbors(edges, n)
    A_, B_, C_ = absym
    configs = set()
    for s in range(M):
        for t in range(M):
            v = [REF] * n
            v[order[0]], v[order[1]] = s, t
            configs.add(tuple(v))
    for i in range(n):
        for s in range(M):
            v = [REF] * n
            v[i] = s
            configs.add(tuple(v))
    eqs = set()
    for v in sorted(configs):
        formed = set()
        num = sp.Integer(1)
        den = sp.Integer(1)
        for x in order:
            rec = [y for y in N[x] if y in formed]
            dirs = [tuple(pos[y][i] - pos[x][i] for i in range(3)) for y in N[x] if y not in formed]
            num *= sp.Mul(*[absence_factor(v[x], d, A_, B_, C_) for d in dirs])
            den *= sum(sp.Mul(*[phis[s][v[y]] for y in rec]) * sp.Mul(*[absence_factor(s, d, A_, B_, C_) for d in dirs]) for s in range(M))
            formed.add(x)
        e = sp.expand(ZW * num - den)
        if e != 0:
            eqs.add(e)
    return sorted(eqs, key=sp.default_sort_key), sorted(configs)


def formation_law_absence(name, pos, phi, order, abc):
    edges, n = WINDOWS[name], SIZES[name]
    N = neighbors(edges, n)
    law = {}
    for v in product(range(M), repeat=n):
        num, den, formed = 1, 1, set()
        for x in order:
            rec = [y for y in N[x] if y in formed]
            dirs = [tuple(pos[y][i] - pos[x][i] for i in range(3)) for y in N[x] if y not in formed]
            terms = []
            for s in range(M):
                t = 1
                for y in rec:
                    t *= phi[s][v[y]]
                for d in dirs:
                    t *= absence_factor(s, d, *abc)
                terms.append(t)
            num *= terms[v[x]]
            den *= sum(terms)
            formed.add(x)
        law[v] = Fraction(num, den)
    return law


def static_law(name, phi):
    edges, n = WINDOWS[name], SIZES[name]
    configs = list(product(range(M), repeat=n))
    ZW = sum(static_weight(v, edges, phi) for v in configs)
    return {v: Fraction(static_weight(v, edges, phi), ZW) for v in configs}


def family_e(checks: Checks, report: dict) -> None:
    phi = phi_table(TRIPLES[0])
    r_x = rule_numerators(range(M), (0,), phi)
    r_y = rule_numerators(range(M), (2,), phi)
    phic = phi_table(CONSTANT_TRIPLE)
    checks.check(
        "E1",
        [Fraction(t, sum(r_x)) for t in r_x] != [Fraction(t, sum(r_y)) for t in r_y]
        and rule_numerators(range(M), (0,), phic) == rule_numerators(range(M), (2,), phic),
        "route 1: the (3,1,2) rule varies between the conditions P(+e_x) and P(+e_y) on the menu; the constant rule does not",
    )
    psi_bad = (2, 1, 1, 1, 1, 1)
    breaks = any(psi_bad[rotate_menu(r, a)] != psi_bad[a] for r in ROTATIONS for a in range(M))
    ranks = []
    for triple in TRIPLES:
        ph = phi_table(CONSTANT_TRIPLE if mut("psi_rank_deficient") else triple)
        base = [ph[s][0] * ph[s][0] for s in range(M)]
        rows = []
        for b in range(M):
            for c in range(M):
                row = [ph[s][b] * ph[s][c] - base[s] for s in range(M)]
                if any(row):
                    rows.append(row)
        ranks.append(bareiss_rank(rows, M) if rows else 0)
    checks.check("E2", breaks and ranks == [6, 6], f"route 2: non-constant psi breaks covariance; Z_2-constant system in psi has rank {ranks} (both triples)")
    rots = ROTATIONS[:1] if mut("absence_blind_nonconstant_passes") else ROTATIONS
    rows = []
    for r in rots:
        for a in range(M):
            row = [0] * M
            row[a] += 1
            row[rotate_menu(r, a)] -= 1
            if any(row):
                rows.append(row)
    checks.check("E3", nullity_of_equations(rows, M) == 1, "route 3: a direction-blind absence factor is forced constant by covariance (dimension 1)")
    P_, Q_, R_, A_, B_, C_ = sp.symbols("p q r a b c", positive=True)
    phis = [[(P_, Q_, R_)[orbit(a, b)] for b in range(M)] for a in range(M)]
    ZW3 = sp.expand(sum(sp.Mul(*[phis[v[i]][v[j]] for i, j in WINDOWS["path3"]]) for v in product(range(M), repeat=3)))
    eqs, _ = absence_ratio_equations("path3", PATH3_POS, (0, 2, 1), phis, (A_, B_, C_), ZW3)
    eqs1 = sorted({sp.expand(e.subs({R_: 1, C_: 1})) for e in eqs} - {sp.Integer(0)}, key=sp.default_sort_key)
    G = sp.groebner(eqs1, A_, B_, P_, Q_, order="lex")
    u = (P_ + Q_ + 4) ** 2
    contained = all(G.contains(sp.expand(g * u)) for g in (A_ - 1, B_ - 1, (P_ - Q_) ** 2, (Q_ - 1) ** 3))
    solutions = [{A_: 1, B_: 1, P_: 1, Q_: 1}]
    if mut("absence_extension_solution_forged"):
        solutions.append({A_: 2, B_: 1, P_: 3, Q_: 1})
    verified = True
    for sol in solutions:
        abc = (int(sol[A_]), int(sol[B_]), 1)
        trip = (int(sol[P_]), int(sol[Q_]), 1)
        ph = phi_table(trip)
        verified = verified and formation_law_absence("path3", PATH3_POS, ph, (0, 2, 1), abc) == static_law("path3", ph)
    checks.check(
        "E4a",
        len(eqs1) >= 8 and contained and verified,
        f"route 4 path3 (0,2,1): {len(eqs1)} eqs, r=c=1; Groebner basis contains (a-1)u,(b-1)u,(p-q)^2u,(q-1)^3u, u=(p+q+4)^2: a=b=c, p=q=r; verified",
    )
    alpha0 = [sp.Mul(absence_factor(s, (1, 0, 0), A_, B_, C_), absence_factor(s, (0, 1, 0), A_, B_, C_)) for s in range(M)]
    marg = {}
    for v in product(range(M), repeat=4):
        marg[v[0]] = marg.get(v[0], 0) + sp.Mul(*[phis[v[i]][v[j]] for i, j in WINDOWS["cycle4"]])
    uniform = len({sp.expand(m) for m in marg.values()}) == 1
    sol_abc = sp.solve([alpha0[s] - alpha0[0] for s in range(1, M)], [A_, B_], dict=True)
    reduced_ok = sol_abc == [{A_: C_, B_: C_}]
    ZW4 = sp.expand(sum(marg.values()))
    eqs4, _ = absence_ratio_equations("cycle4", PLAQUETTE_POS, (0, 1, 2, 3), phis, (C_, C_, C_), ZW4)
    eqs4 = sorted({sp.expand(e.subs({R_: 1, C_: 1})) for e in eqs4} - {sp.Integer(0)}, key=sp.default_sort_key)
    sol_pq = sp.solve(eqs4, [P_, Q_], dict=True)
    ph1 = phi_table((1, 1, 1))
    verified4 = formation_law_absence("cycle4", PLAQUETTE_POS, ph1, (0, 1, 2, 3), (1, 1, 1)) == static_law("cycle4", ph1)
    ronly_same = formation_law_absence("cycle4", PLAQUETTE_POS, phi, (0, 1, 2, 3), (7, 7, 7)) == formation_law(WINDOWS["cycle4"], 4, phi, (0, 1, 2, 3))
    checks.check(
        "E4b",
        uniform and reduced_ok and sol_pq == [{P_: 1, Q_: 1}] and verified4 and ronly_same,
        f"route 4 cycle4 (0,1,2,3): uniform static marginal vs first-site marginal (ac,bc,ac,bc,c^2,c^2) forces a=b=c; reduced {len(eqs4)} eqs give p=q=r; verified",
    )
    ranks2 = []
    for triple in TRIPLES:
        ph = phi_table(triple)
        Z2 = [[sum(ph[s][b] * ph[s][c] for s in range(M)) for c in range(M)] for b in range(M)]
        if mut("z2_rank_one"):
            Z2 = [[Z2[b][0] * Z2[0][c] for c in range(M)] for b in range(M)]
        ranks2.append(bareiss_rank(Z2, M))
    Z2s = {}
    for b in range(M):
        for c in range(M):
            Z2s.setdefault(orbit(b, c), sp.expand(sum(phis[s][b] * phis[s][c] for s in range(M))))
    minor1 = sp.factor(Z2s[PAR] ** 2 - Z2s[ANTI] ** 2)
    minor2 = sp.factor(Z2s[PAR] ** 2 - Z2s[ORTH] ** 2)
    m1 = sp.expand(minor1 - (P_ - Q_) ** 2 * (P_ ** 2 + 2 * P_ * Q_ + Q_ ** 2 + 8 * R_ ** 2)) == 0
    m2 = sp.expand(minor2 - ((P_ - R_) ** 2 + (Q_ - R_) ** 2) * (P_ ** 2 + 2 * P_ * R_ + Q_ ** 2 + 2 * Q_ * R_ + 6 * R_ ** 2)) == 0
    Phi = sp.Matrix(6, 6, lambda a, b: phis[a][b])
    detPhi = sp.factor(Phi.det())
    det_ok = sp.expand(detPhi - (P_ + Q_ + 4 * R_) * (P_ + Q_ - 2 * R_) ** 2 * (P_ - Q_) ** 3) == 0
    checks.check("E4c", ranks2 == [4, 6] and det_ok and m1 and m2, f"route 4 factorized: rank Z_2 = {ranks2} at (3,1,2),(5,2,4); det Phi = (p+q+4r)(p+q-2r)^2(p-q)^3; minors symbolic: rank >= 2 unless p=q=r")
    diffs = {}
    for triple in TRIPLES + ((2, 3, 5),):
        ph = phi_table(triple)
        mu = static_law("cycle4", ph)
        configs = list(mu)
        acc = {v: Fraction(0) for v in configs}
        for order in permutations(range(4)):
            law = dict(mu) if mut("order_mixture_equals_static") else formation_law(WINDOWS["cycle4"], 4, ph, order)
            for v in configs:
                acc[v] += law[v]
        diffs[triple] = max(abs(acc[v] / 24 - mu[v]) for v in configs)
    report["mixture"] = diffs
    checks.check("E5", all(d > 0 for d in diffs.values()) and diffs[(2, 3, 5)] == Fraction(1585133, 10007780364), f"route 5 cycle4 mixture: max |avg - mu| = {diffs[TRIPLES[0]]} (3,1,2), {diffs[TRIPLES[1]]} (5,2,4); control (2,3,5) 1585133/10007780364")
    mu_p = static_law("path3", phi)
    mu_c = static_law("cycle4", phi)

    def one_nbr_cond(mu, n):
        out = {}
        for t in range(M):
            acc = [Fraction(0)] * M
            for v, w in mu.items():
                if v[1] == t:
                    acc[v[0]] += w
            tot = sum(acc)
            out[t] = tuple(x / tot for x in acc)
        return out

    rule_one = {t: tuple(Fraction(x, sum(rule_numerators(range(M), (t,), phi))) for x in rule_numerators(range(M), (t,), phi)) for t in range(M)}
    cond_p = one_nbr_cond(mu_p, 3)
    cond_c = dict(cond_p) if mut("marginal_reading_is_fixed_rule") else one_nbr_cond(mu_c, 4)
    expected_c = (Fraction(219, 866), Fraction(71, 866)) + (Fraction(72, 433),) * 4
    checks.check("E6a", cond_p == rule_one and cond_c != rule_one and cond_c[0] == expected_c and rule_one[0] == (Fraction(1, 4), Fraction(1, 12)) + (Fraction(1, 6),) * 4, "route 6: static one-neighbor conditional = rule on path3, not on cycle4 (219/866, 71/866, 72/433 x4 vs 1/4, 1/12, 1/6 x4)")
    configs4 = list(mu_c)
    marginals = {}
    for mask in range(16):
        S = tuple(i for i in range(4) if mask >> i & 1)
        acc = {}
        for v, w in mu_c.items():
            key = tuple(v[i] for i in S)
            acc[key] = acc.get(key, Fraction(0)) + w
        marginals[S] = acc
    N4 = neighbors(WINDOWS["cycle4"], 4)

    def chain_product(order, v, condition_on_all_records, break_last):
        prob = Fraction(1)
        formed = []
        for k, x in enumerate(order):
            E_set = tuple(sorted(formed)) if condition_on_all_records else tuple(sorted(y for y in N4[x] if y in formed))
            if break_last and k == 1:
                A = tuple(sorted(y for y in N4[x] if y in formed))
                nums = rule_numerators(range(M), tuple(v[y] for y in A), phi)
                prob *= Fraction(nums[v[x]], sum(nums))
            else:
                S_with = tuple(sorted(E_set + (x,)))
                prob *= marginals[S_with][tuple(v[i] for i in S_with)] / marginals[E_set][tuple(v[i] for i in E_set)]
            formed.append(x)
        return prob

    chain_all = all(chain_product(order, v, True, mut("marginal_chain_rule_broken")) == mu_c[v] for order in permutations(range(4)) for v in configs4)  # the mutation swaps the second step for the R-only rule (the last step would be vacuous by Theorem A)
    orders_nbr_only = sum(1 for order in permutations(range(4)) if all(chain_product(order, v, False, False) == mu_c[v] for v in configs4))
    checks.check("E6b", chain_all and orders_nbr_only == 0, f"route 6 chain rule on cycle4: given all earlier records mu_sigma = mu for 24/24 orders; given recorded neighbors only {orders_nbr_only}/24")


# ==================================================================== family F
FENCES = (
    "This note selects no physical rule, no coupling value, no formation order and no reading of the axioms; the records-only reading is a named premise and its two alternatives are computed.",
    "No statement is made about the infinite lattice beyond naming the specification; existence or uniqueness of an infinite-volume law is outside this note, and this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "This note does not derive, explain, bear on or decide the parked statistical bridge, the Born form, or the gravity lane's action; the 2026-08-26 gate measurement is a float measurement on one fixture, cited by path only.",
    "Every negative sentence in this note is an exact finite statement on the declared windows and menu or a corollary of Theorem B; none is a route no-go beyond that scope.",
)
FORBIDDEN = (
    "selects the physical rule", "derives the Born", "explains the gate", "bears on the gate",
    "infinite-lattice law", "the framework's action is", "the order is physical", "certified",
    "closed the gate", "axiom is amended", "fires wake condition",
    "distinct orders give distinct laws", "witnesses the variation clause",
)
CLAIM_INJECTIONS = {
    "claim_rule_selected": "This note selects the physical rule.",
    "claim_born_derived": "This note derives the Born form.",
    "claim_gate_explained": "This note explains the gate measurement.",
    "claim_infinite_volume": "The infinite-lattice law is identified here.",
    "claim_action_identified": "The framework's action is the static action.",
    "claim_axiom_amended": "The Admissibility axiom is amended by this note.",
    "claim_order_physical": "Therefore the order is physical.",
}
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the four fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase (hits: {hits})")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln]
    checks.check("F3", not bad and len(scan) > 500, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")


# ==================================================================== family G
N5_LINES = (
    "per_element: executed — every menu value, every configuration of path3/P4/star4/cycle4, every order, both triples, exact",
    "per_site: executed — the full conditional at every site of every declared window; cube8 on the declared configuration family",
    "per_mode: checked and not executed — no spectral decomposition in the theorem; det Phi factorization is symbolic",
    "per_block: executed — every order's normalizer history block by block; cube8: 40320 orders combinatorially, six exactly",
    "lattice_wide: checked and not executed — finite windows only; the infinite-volume specification is named, not computed",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", all(len(l) >= 40 for l in N5_LINES) and len(N5_LINES) == 5, "the five N5 resolution lines are printed (each >= 40 characters)")


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
    checks = Checks()
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8") if AXIOM_PATH.is_file() else ""
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: finite windows, six-projector menu, exact arithmetic; no infinite-volume claim")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, note_text, axiom_text)
    family_b(checks)
    family_c(checks)
    family_d(checks, report)
    family_e(checks, report)
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
