#!/usr/bin/env python3
"""Exact checks: the Hermitian Gaussian instance of the static/formation distinction.

Scope.  A declared Hermitian positive-definite nearest-neighbor precision P over the Gaussian rationals on the path 1x3,
the plaquette 2x2 and the rectangle 2x3.  The static law is the complex Gaussian with precision P; the formation law along
an order draws each site from the rule's conditional given its RECORDED neighbors only (block 01's definition, the
records-only reading).  G1: the formation law is the complex Gaussian with precision P_sigma = L^dagger D L (L unit lower
triangular in the order with L_ky = P_ky/P_kk on the recorded neighbors, D = diag P_kk), normalizer prod P_kk.  G2: P_sigma
depends on the order only through the recorded sets; the monotone class of the rectangle gives one law.  G3: P_sigma = P +
diag(c) + F with c_x = sum over later recording sites of |P_kx|^2/P_kk and the fill-in F between pairs recorded together;
P_sigma = P never on a window with an edge; if every site records at most one neighbor then support(P_sigma) = support(P)
(block 01's Theorem B condition), and on the declared grid instances the converse holds as an executed fact, while in
general it is false (the checker's exact witnesses: cancelling fill-in on a plaquette; fill-in on an edge of a triangle);
on the grid the fill-in sits on the anti-diagonal pairs of the plaquettes.  G4: det P_sigma = prod
P_kk > det P (Hadamard), equality iff P is diagonal.  G5: the three read-slice covariances (static marginal, pinned-static
conditional, formation) are pairwise different on 2x3; the formation law given the pinned row is not the static
conditional; for a non-Hermitian Q, herm(Q^-1) != (herm Q)^-1.  Exact rational-complex arithmetic only (sympy Rational and
I); the runner scans its own source for floating-point literals and conversion calls.  The instance is self-made; nothing
about any external fixture is claimed.
"""

from __future__ import annotations

import re
import sys
from itertools import permutations
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_HERMITIAN_GAUSSIAN_INSTANCE_FORMATION_PRECISION_LDL_BOUNDED_THEOREM_NOTE_2026-09-07.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
BLOCK01_PATH = ROOT / AUDIT_INPUT_PATHS[2]
BLOCK05_PATH = ROOT / AUDIT_INPUT_PATHS[3]
CLAIM_ID = "admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_bounded_theorem_note_2026-09-07"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "at most one recorded neighbor"
BLOCK05_CLAIM_ID = "admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07"
BLOCK05_FRAGMENT = "for every nearest-neighbor rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "pd_certificate_forged": "B",
    "quadratic_form_mismatch": "B",
    "normalizer_wrong": "B",
    "class_equality_broken": "B",
    "monotone_class_split": "B",
    "separation_formula_wrong": "C",
    "support_condition_forged": "C",
    "fillin_pairs_wrong": "C",
    "correction_literal_off": "C",
    "equality_with_static_claimed": "C",
    "cancellation_witness_denied": "C",
    "hadamard_reversed": "D",
    "hadamard_equality_case_wrong": "D",
    "read_slices_equal_claimed": "E",
    "conditional_block_equal_claimed": "E",
    "herm_inverse_commutes_claimed": "E",
    "claim_lane_fixture": "F",
    "claim_formation_equals_static": "F",
    "claim_bridge": "F",
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


I = sp.I
R = sp.Rational


def is_zero_matrix(Mx) -> bool:
    return all(sp.simplify(x) == 0 for x in Mx)


# ------------------------------------------------------------------ the graphs and the instances
def grid(n: int, W: int):
    sites = [(i, j) for i in range(n) for j in range(W)]
    idx = {s: k for k, s in enumerate(sites)}
    edges = []
    for (i, j) in sites:
        if j + 1 < W:
            edges.append(((i, j), (i, j + 1), "h"))
        if i + 1 < n:
            edges.append(((i, j), (i + 1, j), "v"))
    return sites, idx, edges


INSTANCES = {
    "declared": (R(3), (1 + 2 * I) / 4, (2 - I) / 4),
    "real": (R(3), R(1, 2), R(1, 2)),
}
WINDOWS = ((1, 3), (2, 2), (2, 3))


def precision(n: int, W: int, inst: str):
    diag, ch, cv = INSTANCES[inst]
    sites, idx, edges = grid(n, W)
    N = len(sites)
    P = sp.zeros(N, N)
    for k in range(N):
        P[k, k] = diag
    for a, b, t in edges:
        c = ch if t == "h" else cv
        P[idx[a], idx[b]] = c
        P[idx[b], idx[a]] = sp.conjugate(c)
    return sites, idx, edges, P


def neighbors(edges, s):
    out = []
    for a, b, _ in edges:
        if a == s:
            out.append(b)
        if b == s:
            out.append(a)
    return out


def recorded_sets(sites, edges, order):
    pos = {s: t for t, s in enumerate(order)}
    return {s: tuple(y for y in neighbors(edges, s) if pos[y] < pos[s]) for s in sites}


def ldl_factors(P, sites, idx, edges, order):
    """L unit lower triangular in the order (L_ky = P_ky/P_kk on the recorded neighbors), D = diag P_kk, P_sigma = L^H D L."""
    N = len(sites)
    rec = recorded_sets(sites, edges, order)
    L = sp.eye(N)
    D = sp.zeros(N, N)
    for s in order:
        k = idx[s]
        D[k, k] = P[k, k]
        for y in rec[s]:
            L[k, idx[y]] = P[k, idx[y]] / P[k, k]
    return L, D, rec


def formation_precision_from_conditionals(P, sites, idx, edges, order):
    """The quadratic form of the product of the conditional densities, built term by term: sum_k P_kk (e_k + sum_y (P_ky/P_kk) e_y)(...)^H."""
    N = len(sites)
    rec = recorded_sets(sites, edges, order)
    Q = sp.zeros(N, N)
    for s in order:
        k = idx[s]
        v = sp.zeros(N, 1)
        v[k, 0] = 1
        for y in rec[s]:
            v[idx[y], 0] = P[k, idx[y]] / P[k, k]
        Q += P[k, k] * (sp.conjugate(v) * v.T)
    return Q, rec


def support(Mx):
    return frozenset((i, j) for i in range(Mx.rows) for j in range(Mx.cols) if i != j and sp.simplify(Mx[i, j]) != 0)


def leading_minors_positive(Mx) -> bool:
    for k in range(1, Mx.rows + 1):
        d = sp.simplify(Mx[:k, :k].det())
        if sp.im(d) != 0 or sp.re(d) <= 0:
            return False
    return True


def is_extension(sites, order) -> bool:
    pos = {s: t for t, s in enumerate(order)}
    return all((j == 0 or pos[(i, j - 1)] < pos[(i, j)]) and (i == 0 or pos[(i - 1, j)] < pos[(i, j)]) for (i, j) in sites)


def separation_formula(P, sites, idx, rec):
    """diag(c) + F: c_x = sum_{k: x in A_k} |P_kx|^2/P_kk; F_xy = sum_{k: x,y in A_k} P_xk P_ky / P_kk."""
    N = len(sites)
    C = sp.zeros(N, N)
    F = sp.zeros(N, N)
    for s, A in rec.items():
        k = idx[s]
        for y in A:
            C[idx[y], idx[y]] += P[k, idx[y]] * sp.conjugate(P[k, idx[y]]) / P[k, k]
        for y in A:
            for y2 in A:
                if y != y2:
                    F[idx[y], idx[y2]] += P[idx[y], k] * P[k, idx[y2]] / P[k, k]
    return C, F


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b01_text: str, b05_text: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4, "the four declared audit inputs exist")
    checks.check("A2", all(n in normalize_text(axiom_text) for n in AXIOM_NEEDLES), "axiom memo: the Admissibility and Record sentences verbatim")
    checks.check("A3", BLOCK01_CLAIM_ID in b01_text and BLOCK01_FRAGMENT in normalize_text(b01_text), "block 01's note: claim id and the one-recorded-neighbor fragment")
    checks.check("A4", BLOCK05_CLAIM_ID in b05_text and BLOCK05_FRAGMENT in normalize_text(b05_text), "block 05's note: claim id and the every-rule fragment")
    checks.check("A5", CLAIM_ID in note_text, "this note carries its claim id")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    pd_ok = True
    for inst in INSTANCES:
        for (n, W) in WINDOWS:
            sites, idx, edges, P = precision(n, W, inst)
            herm = is_zero_matrix(P - P.H)
            Pt = P.copy()
            if mut("pd_certificate_forged"):
                Pt[0, 0] = R(-3)
            pd_ok = pd_ok and herm and leading_minors_positive(Pt)
    checks.check("B1", pd_ok, "both instances on the three windows are Hermitian with positive leading principal minors (positive definite)")
    qf_ok, norm_ok = True, True
    for inst in INSTANCES:
        for (n, W) in WINDOWS:
            sites, idx, edges, P = precision(n, W, inst)
            orders = list(permutations(sites)) if len(sites) <= 4 else [tuple(sites), tuple(reversed(sites))]
            for order in orders:
                L, D, rec = ldl_factors(P, sites, idx, edges, order)
                Ps = L.H * D * L
                Qc, _ = formation_precision_from_conditionals(P, sites, idx, edges, order)
                if mut("quadratic_form_mismatch"):
                    Qc = Qc + sp.eye(len(sites)) / 7
                qf_ok = qf_ok and is_zero_matrix(Ps - Qc) and is_zero_matrix(Ps - Ps.H)
                prodd = sp.prod([P[k, k] for k in range(len(sites))])
                dPs = sp.simplify(Ps.det())
                if mut("normalizer_wrong"):
                    dPs = dPs + 1
                norm_ok = norm_ok and sp.simplify(dPs - prodd) == 0 and sp.simplify(L.det() - 1) == 0
    checks.check("B2", qf_ok, "G1: the product of the conditional densities has the quadratic form L^H D L, Hermitian, on every order of the path and plaquette and two orders of 2x3, both instances")
    checks.check("B3", norm_ok, "G1: det L = 1 and det P_sigma = prod_k P_kk (the formation normalizer is order-independent)")
    sites, idx, edges, P = precision(2, 2, "declared")
    classes: dict = {}
    for order in permutations(sites):
        L, D, rec = ldl_factors(P, sites, idx, edges, order)
        key = tuple(sorted((s, tuple(sorted(rec[s]))) for s in sites))
        classes.setdefault(key, []).append(L.H * D * L)
    within = all(is_zero_matrix(x - lst[0]) for lst in classes.values() for x in lst)
    if mut("class_equality_broken"):
        within = within and len(classes) == 24
    checks.check("B4", within and len(classes) == 14, f"G2: the 24 orders of the plaquette fall into {len(classes)} recorded-set classes and P_sigma is constant on each")
    sites, idx, edges, P = precision(2, 3, "declared")
    exts = [o for o in permutations(sites) if is_extension(sites, o)]
    Pm = []
    for o in exts:
        L, D, rec = ldl_factors(P, sites, idx, edges, o)
        Pm.append(L.H * D * L)
    snake = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0)]
    mirror = [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0)]
    L, D, _ = ldl_factors(P, sites, idx, edges, snake)
    Ps_snake = L.H * D * L
    L, D, _ = ldl_factors(P, sites, idx, edges, mirror)
    Ps_mirror = L.H * D * L
    ref = Ps_snake if mut("monotone_class_split") else Pm[0]
    one = all(is_zero_matrix(x - ref) for x in Pm)
    differ = (not is_zero_matrix(Ps_snake - ref)) and (not is_zero_matrix(Ps_mirror - ref))
    checks.check("B5", len(exts) == 5 and one and differ, "G2: the 5 monotone orders of 2x3 give one P_sigma; the snake and the mirror give different ones")
    report["P23"] = (sites, idx, edges, P, Pm[0], exts)


# ============================================================================================ family C
CORRECTION_UNIT = R(5, 48)
CORRECTIONS_23 = [R(5, 24), R(5, 24), R(5, 48), R(5, 48), R(5, 48), R(0)]
FILLIN_PAIRS_23 = (((0, 1), (1, 0)), ((0, 2), (1, 1)))


def family_c(checks: Checks, report: dict, exact: bool) -> None:
    formula_ok, never_equal, support_ok = True, True, True
    n_orders = 0
    for inst in INSTANCES:
        for (n, W) in WINDOWS:
            sites, idx, edges, P = precision(n, W, inst)
            orders = list(permutations(sites)) if len(sites) <= 4 else [tuple(sites)]
            for order in orders:
                n_orders += 1
                L, D, rec = ldl_factors(P, sites, idx, edges, order)
                Ps = L.H * D * L
                C, F = separation_formula(P, sites, idx, rec)
                if mut("separation_formula_wrong"):
                    F = F * 2
                formula_ok = formula_ok and is_zero_matrix(Ps - (P + C + F))
                if mut("equality_with_static_claimed"):
                    never_equal = never_equal and is_zero_matrix(Ps - P)
                else:
                    never_equal = never_equal and (not is_zero_matrix(Ps - P)) and any(len(A) > 0 for A in rec.values())
                le1 = max(len(A) for A in rec.values()) <= 1
                same = support(Ps) == support(P)
                if mut("support_condition_forged"):
                    same = not same
                # G3(b): <= 1 recorded neighbor => same support and F = 0 (a theorem); on the declared instances of the grid
                # the converse holds as an executed fact (no cancellation); the general converse is false (C6).
                support_ok = support_ok and (same == le1) and (not le1 or is_zero_matrix(F))
    checks.check("C1", formula_ok, f"G3: P_sigma = P + diag(c) + F on {n_orders} (instance, window, order) cases")
    checks.check("C2", never_equal, "G3(a): P_sigma differs from P on every order of every window (each has a recorded neighbor)")
    checks.check("C3", support_ok, "G3(b): <= 1 recorded neighbor => support(P_sigma) = support(P) and F = 0 (theorem); on the declared grid instances the converse holds too (executed)")
    sites, idx, edges, P = precision(1, 3, "declared")
    ends = ldl_factors(P, sites, idx, edges, ((0, 0), (0, 1), (0, 2)))
    mid = ldl_factors(P, sites, idx, edges, ((0, 0), (0, 2), (0, 1)))
    Ps_e = ends[0].H * ends[1] * ends[0]
    Ps_m = mid[0].H * mid[1] * mid[0]
    unit = CORRECTION_UNIT + (R(1, 1000) if mut("correction_literal_off") else 0)
    path_ok = support(Ps_e) == support(P) and support(Ps_m) != support(P) and [sp.simplify(Ps_e[k, k] - P[k, k]) for k in range(3)] == [unit, unit, 0]
    checks.check("C4", path_ok, "G3: on the path, the end-to-end order keeps P's support with corrections [5/48, 5/48, 0]; the middle-out order fills in the end pair")
    sites, idx, edges, P, Pm0, exts = report["P23"]
    corr = [sp.simplify(Pm0[k, k] - P[k, k]) for k in range(6)]
    edge_set = {(idx[a], idx[b]) for a, b, _ in edges}
    fill = tuple(sorted((sites[i], sites[j]) for i in range(6) for j in range(i + 1, 6) if (i, j) not in edge_set and sp.simplify(Pm0[i, j]) != 0))
    expected_fill = FILLIN_PAIRS_23 if not mut("fillin_pairs_wrong") else (((0, 0), (1, 1)),)
    checks.check("C5", corr == CORRECTIONS_23 and fill == expected_fill, f"G3(c): 2x3 monotone class: corrections {corr}; fill-in on the anti-diagonal pairs {fill}")
    # C6: the boundary of G3(b) — the refuting checker's exact witnesses: the general converse is false
    def custom(N, entries):
        Pc = sp.zeros(N, N)
        for k in range(N):
            Pc[k, k] = R(3)
        for (a, b), v in entries.items():
            Pc[a, b] = v
            Pc[b, a] = sp.conjugate(v)
        return Pc
    def ldl_custom(Pc, order, adj):
        N = Pc.rows
        pos = {x: t for t, x in enumerate(order)}
        L = sp.eye(N)
        D = sp.zeros(N, N)
        rec = {}
        for x in order:
            D[x, x] = Pc[x, x]
            A = [y for y in adj[x] if pos[y] < pos[x]]
            rec[x] = A
            for y in A:
                L[x, y] = Pc[x, y] / Pc[x, x]
        return L.H * D * L, rec
    # (i) plaquette a=0,b=1,c=2,d=3 with edges ab, ac, bd, cd and P_cd = -1/2: order (a, d, b, c) records two neighbors at b and at c, the fill-in on (a, d) cancels
    Pw = custom(4, {(0, 1): R(1, 2), (0, 2): R(1, 2), (1, 3): R(1, 2), (2, 3): R(-1, 2)})
    adj4 = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    Psw, recw = ldl_custom(Pw, (0, 3, 1, 2), adj4)
    w1 = leading_minors_positive(Pw) and max(len(A) for A in recw.values()) == 2 and support(Psw) == support(Pw) and is_zero_matrix(Psw - Pw - sp.diag(R(1, 6), 0, 0, R(1, 6)))
    # (ii) the triangle K3: fill-in on an adjacent pair, support unchanged with two recorded neighbors
    Pt = custom(3, {(0, 1): R(1, 2), (0, 2): R(1, 2), (1, 2): R(1, 2)})
    Pst, rect = ldl_custom(Pt, (0, 1, 2), {0: [1, 2], 1: [0, 2], 2: [0, 1]})
    w2 = leading_minors_positive(Pt) and len(rect[2]) == 2 and support(Pst) == support(Pt) and sp.simplify(Pst[0, 1] - Pt[0, 1]) != 0
    # (iii) a triangle where the fill-in cancels an existing edge entry: the support shrinks
    Ps3 = custom(3, {(0, 1): R(1, 4), (0, 2): R(1, 2), (1, 2): R(-3, 2)})
    Pss, recs = ldl_custom(Ps3, (0, 1, 2), {0: [1, 2], 1: [0, 2], 2: [0, 1]})
    w3 = leading_minors_positive(Ps3) and sp.simplify(Pss[0, 1]) == 0 and sp.simplify(Ps3[0, 1]) != 0
    if mut("cancellation_witness_denied"):
        w1 = not w1
    checks.check("C6", w1 and w2 and w3, "the boundary of G3(b): a plaquette precision with P_cd = -1/2 keeps P's support under an order recording two neighbors (fill-in cancels); on K3 the fill-in lands on an edge; a triangle precision loses an edge entry (checker's witnesses)")
    if exact:
        print(f"exact 2x3 monotone P_sigma = {Pm0.tolist()}")
        print(f"exact 2x3 P = {P.tolist()}")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    ok, eq_ok = True, True
    for inst in INSTANCES:
        for (n, W) in WINDOWS:
            sites, idx, edges, P = precision(n, W, inst)
            dP = sp.simplify(P.det())
            prodd = sp.prod([P[k, k] for k in range(len(sites))])
            if mut("hadamard_reversed"):
                dP, prodd = prodd, dP
            ok = ok and sp.im(dP) == 0 and sp.re(dP) > 0 and sp.re(dP) < prodd
    Pd = sp.diag(R(3), R(3), R(3))
    d_eq = sp.simplify(Pd.det() - sp.prod([Pd[k, k] for k in range(3)])) == 0
    if mut("hadamard_equality_case_wrong"):
        d_eq = not d_eq
    checks.check("D1", ok, "G4: det P < prod_k P_kk (Hadamard) on the three windows, both instances; det P real and positive")
    checks.check("D2", d_eq, "G4: equality det P = prod P_kk for a diagonal P")


# ============================================================================================ family E
COND_DIAG_23 = [R(149, 48), R(149, 48), R(3)]


def family_e(checks: Checks, report: dict, exact: bool) -> None:
    sites, idx, edges, P, Pm0, exts = report["P23"]
    row0 = [idx[(0, j)] for j in range(3)]
    row1 = [idx[(1, j)] for j in range(3)]
    Cstat = sp.simplify(P.inv())
    Cform = sp.simplify(Pm0.inv())
    m_static = Cstat.extract(row1, row1)
    m_pinned = sp.simplify(P.extract(row1, row1).inv())
    m_form = Cform.extract(row1, row1)
    pairwise = (not is_zero_matrix(m_static - m_pinned)) and (not is_zero_matrix(m_static - m_form)) and (not is_zero_matrix(m_pinned - m_form))
    if mut("read_slices_equal_claimed"):
        pairwise = is_zero_matrix(m_static - m_form)
    checks.check("E1", pairwise, "G5: on 2x3 the static marginal, the pinned-static conditional and the formation read-slice covariances of row 1 are pairwise different")
    blk = Pm0.extract(row1, row1)
    diag = [sp.simplify(blk[k, k]) for k in range(3)]
    cond_ok = (not is_zero_matrix(blk - P.extract(row1, row1))) and diag == COND_DIAG_23
    if mut("conditional_block_equal_claimed"):
        cond_ok = is_zero_matrix(blk - P.extract(row1, row1))
    checks.check("E2", cond_ok, f"G5: the formation precision's row-1 block differs from P_11: diagonal {diag} against [3, 3, 3]")
    Qn = sp.Matrix([[1, 1], [-1, 1]])
    lhs = (Qn.inv() + Qn.inv().H) / 2
    rhs = ((Qn + Qn.H) / 2).inv()
    commutes = is_zero_matrix(lhs - rhs)
    if mut("herm_inverse_commutes_claimed"):
        commutes = not commutes
    checks.check("E3", not commutes, "G5 remark: herm(Q^-1) != (herm Q)^-1 for the non-Hermitian witness Q = [[1,1],[-1,1]]")
    if exact:
        print(f"exact read slice static marginal = {m_static.tolist()}")
        print(f"exact read slice pinned-static conditional = {m_pinned.tolist()}")
        print(f"exact read slice formation = {m_form.tolist()}")


# ============================================================================================ family F
FENCES = (
    "This note states the static/formation distinction for a self-made Hermitian positive-definite nearest-neighbor precision on three small windows; the instance is declared, not derived, and nothing is claimed about any external fixture or committed action.",
    "No order is selected as physical; no plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "Hadamard's inequality and the Gaussian conditional formulas are elementary results re-proved here at the scope used; no value, constant or theorem is imported as authority.",
)
FORBIDDEN = (
    "the gravity lane's action", "the committed action", "the Bridge weights", "the Bridge conjecture", "fires wake condition",
    "certified", "phase transition", "several static laws", "the physical order", "washes out",
    "formation law equals the static law", "formation law is the static law", "the lane's fixture is", "on the gravity fixture",
)
CLAIM_INJECTIONS = {
    "claim_lane_fixture": "This instance is the gravity lane's action, and the result holds on the gravity fixture.",
    "claim_formation_equals_static": "On the path the formation law equals the static law.",
    "claim_bridge": "The formation odds equal the Bridge weights.",
}
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    nsimp = "nsimp" + "lify("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln or nsimp in ln]
    checks.check("F3", not bad and len(scan) > 280, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — every order of the path (6) and the plaquette (24), the five monotone orders, the snake and the mirror of 2x3, both instances",
    "per_site: executed — the recorded set of every site in every order; the diagonal correction and the fill-in at every site and pair",
    "per_mode: executed — the quadratic form of the conditional product against L^H D L; det L = 1; the leading principal minors; the three read-slice covariances",
    "per_block: executed — the row-1 block of P, of P_sigma and of the three covariances on 2x3; the determinants on the three windows",
    "lattice_wide: not claimed — three finite windows of a declared instance; nothing about larger windows, the plane or any external fixture",
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
    b05_text = BLOCK05_PATH.read_text(encoding="utf-8") if BLOCK05_PATH.is_file() else ""
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: a self-made Hermitian Gaussian instance on the path, the plaquette and the 2x3 rectangle: the formation law's precision L^H D L, the recorded-set class, the separation from P, Hadamard, the three read-slice covariances; exact; no external fixture")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, note_text, axiom_text, b01_text, b05_text)
    family_b(checks, report)
    family_c(checks, report, exact)
    family_d(checks)
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
