#!/usr/bin/env python3
"""Exact checks: the row-sweep formation law versus the static law on an infinite strip.

Scope.  The menu is the six Bloch-axis projectors inside M_2(C); the rule is
the covariant positive product rule with orbit weights (p, q, r) at the declared
exact triples (3, 1, 2) and (5, 2, 4).  Three exact objects: (C) the family of
finite-window static laws with exterior records is consistent (the conditional
of a sub-window is the sub-window's own static law with the adjacent records as
exterior), executed on the open 2x2x2 cube and the plaquette; (E) on the strips
of width W (rows of W sites, nearest-neighbor edges) the row sweep under the
records-only reading has an exactly solvable formation law: every row has the
path static law p_0, and every horizontal or vertical nearest-neighbor pair has
the single-edge law, executed at widths 2, 3 and 4 and proved for every width
and length by a telescoping identity; (F) the static law of the width-2 and
width-3 strips has a center-row pair-parallel probability s_inf enclosed in an
exact rational interval by transfer-matrix symmetry reduction and algebraic
root isolation; the interval excludes the formation value p/(p+q+4r).  Nothing
is claimed about the plane's static law, about uniqueness of an infinite-volume
static law on the cubic lattice, or about any three-recorded-neighbor sweep; no
order is selected as physical.  Exact integer, rational and symbolic arithmetic
only: the runner scans its own source and fails if a floating-point literal or
a floating-point conversion call appears.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from math import lcm, prod
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
PARENT_NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[2]
CLAIM_ID = (
    "admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_"
    "bounded_theorem_note_2026-09-06"
)
PARENT_CLAIM_ID = (
    "admissibility_rule_formation_law_versus_static_law_finite_window_"
    "classification_bounded_theorem_note_2026-09-06"
)
PARENT_FRAGMENT = "equals its static law exactly when every record forms with at most one recorded neighbor"
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
    "kernel_not_doubly_stochastic": "B",
    "z2_identity_wrong_power": "B",
    "path_law_not_formation": "B",
    "spec_conditional_ignores_exterior": "C",
    "spec_conditional_two_hop": "C",
    "spec_face_wrong_subwindow": "C",
    "row_kernel_formula_wrong_denominator": "D",
    "row_kernel_drops_left_neighbor": "D",
    "invariance_forced_true": "D",
    "pair_law_wrong_column": "D",
    "direct_strip_law_mismatch": "D",
    "asymmetric_control_passes": "D",
    "constant_rule_not_uniform": "D",
    "three_neighbor_witness_forced": "D",
    "orbit_count_wrong": "E",
    "quotient_not_commuting": "E",
    "charpoly_coefficient_off": "E",
    "perron_interval_wrong_root": "E",
    "eigvec_residual_nonzero": "E",
    "limit_law_uses_rho_not_squared": "E",
    "s_inf_enclosure_contains_formation_value": "E",
    "finite_n_sequence_shuffled": "E",
    "second_eigenvalue_bound_too_small": "E",
    "boundary_dependence_forged": "E",
    "restriction_lemma_broken": "D",
    "claim_order_selected": "F",
    "claim_plane_static": "F",
    "claim_z3_uniqueness": "F",
    "claim_washout": "F",
    "claim_gate_fired": "F",
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


# --------------------------------------------------------------------- menu
# Menu order: P(+e_x), P(-e_x), P(+e_y), P(-e_y), P(+e_z), P(-e_z); rebuilt here, not imported.
MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
PAR, ANTI, ORTH = 0, 1, 2
TRIPLES = ((3, 1, 2), (5, 2, 4))
CONSTANT_TRIPLE = (2, 2, 2)


def vdot(a: int, b: int) -> int:
    return sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))


def orbit(a: int, b: int) -> int:
    d = vdot(a, b)
    return PAR if d == 1 else (ANTI if d == -1 else ORTH)


def phi_table(triple):
    return tuple(tuple(triple[orbit(a, b)] for b in range(M)) for a in range(M))


def permutation_sign(perm) -> int:
    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inv % 2 else 1


def proper_rotations():
    out = []
    for perm in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * signs[0] * signs[1] * signs[2] == 1:
                out.append((perm, signs))
    return tuple(out)


ROTATIONS = proper_rotations()


def rotate_menu(rot, a: int) -> int:
    perm, signs = rot
    v = MENU_VECTORS[a]
    out = [0, 0, 0]
    for i in range(3):
        out[perm[i]] = signs[i] * v[i]
    return MENU_VECTORS.index(tuple(out))


# ------------------------------------------------------------------- rule
def rule(s: int, recorded, phi) -> Fraction:
    """r(s | recorded neighbors) for the product rule with constant site weight (records-only reading)."""
    num = prod(phi[s][e] for e in recorded)
    den = sum(prod(phi[t][e] for e in recorded) for t in range(M))
    return Fraction(num, den)


def one_edge_kernel(phi):
    z1 = sum(phi[0])
    return [[Fraction(phi[a][s], z1) for s in range(M)] for a in range(M)]


def formation_law_on_graph(n: int, nbrs, order, phi, all_neighbors: bool = False):
    """Block 01's definition: mu_sigma(v) = prod_k r(v_{x_k} | records on A_k)."""
    law = {}
    for v in product(range(M), repeat=n):
        w = Fraction(1)
        formed: set = set()
        for x in order:
            A = nbrs[x] if all_neighbors else tuple(y for y in nbrs[x] if y in formed)
            w *= rule(v[x], tuple(v[y] for y in A), phi)
            formed.add(x)
        law[v] = w
    return law


# ==================================================================== family A
def family_a(checks: Checks, note_text: str, axiom_text: str, parent_text: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3, "the three declared audit inputs exist")
    flat = normalize_text(axiom_text)
    checks.check("A2", all(n in flat for n in AXIOM_NEEDLES[:2]), "axiom memo: both Admissibility sentences verbatim")
    checks.check("A3", all(n in flat for n in AXIOM_NEEDLES[2:]), "axiom memo: the four Record sentences verbatim")
    checks.check("A4", PARENT_CLAIM_ID in parent_text and PARENT_FRAGMENT in normalize_text(parent_text), "parent note carries its claim id and the parent theorem sentence")
    checks.check("A5", CLAIM_ID in note_text, "this note carries its claim id")


# ==================================================================== family B
def family_b(checks: Checks) -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    tr = (p, q, r)
    phi = [[tr[orbit(a, b)] for b in range(M)] for a in range(M)]
    z1 = sum(phi[0][s] for s in range(M))
    K = [[phi[s][a] / z1 for s in range(M)] for a in range(M)]
    if mut("kernel_not_doubly_stochastic"):
        K[0][1] = K[0][1] + sp.Rational(1, 7)
    sym = all(sp.simplify(K[a][s] - K[s][a]) == 0 for a in range(M) for s in range(M))
    rows_one = all(sp.simplify(sum(K[a][s] for s in range(M)) - 1) == 0 for a in range(M))
    cols_one = all(sp.simplify(sum(K[a][s] for a in range(M)) - 1) == 0 for s in range(M))
    checks.check("B1", sym and rows_one and cols_one and sp.expand(z1 - (p + q + 4 * r)) == 0, "K = phi/Z_1 symmetric, rows and columns sum to one (symbolic), Z_1 = p+q+4r")
    power = 3 if mut("z2_identity_wrong_power") else 2
    e1 = all(sp.cancel(sum(phi[s][a] * phi[s][b] for s in range(M)) - z1**power * sum(K[a][s] * K[s][b] for s in range(M))) == 0 for a in range(M) for b in range(M))
    checks.check("B2", e1, "E1: Z_2(a,b) = Z_1^2 (K^2)(a,b) symbolic for all 36 pairs")
    unif = all(sp.simplify(sum(sp.Rational(1, 6) * K[a][s] for a in range(M)) - sp.Rational(1, 6)) == 0 for s in range(M))
    checks.check("B3", unif, "the uniform law is K-invariant (symbolic)")
    # path static law p_0 equals the formation law of the path swept from an end (block 01 Theorem B instance)
    ok = True
    for triple in TRIPLES:
        ph = phi_table(triple)
        Kn = one_edge_kernel(ph)
        for W in (2, 3):
            nbrs = {j: tuple(k for k in (j - 1, j + 1) if 0 <= k < W) for j in range(W)}
            order = (0, 2, 1) if (mut("path_law_not_formation") and W == 3) else tuple(range(W))
            law = formation_law_on_graph(W, nbrs, order, ph)
            for rho in product(range(M), repeat=W):
                p0 = Fraction(1, 6) * prod((Kn[rho[j - 1]][rho[j]] for j in range(1, W)), start=Fraction(1))
                if law[rho] != p0:
                    ok = False
    checks.check("B4", ok, "p_0 = (1/6) prod K equals the end-swept path formation law, W = 2, 3, both triples")


# ==================================================================== family C
def cube_edges():
    return tuple((a, b) for a in range(8) for b in range(a + 1, 8) if bin(a ^ b).count("1") == 1)


CUBE_EDGES = cube_edges()
# site index i = x + 2y + 4z; the exterior neighbor along axis a carries P(+e_a): menu 0, 2, 4
CUBE_EXTERIOR = {x: (0, 2, 4) for x in range(8)}
CYCLE_EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
CYCLE_EXTERIOR = {x: (0, 3) for x in range(4)}


def neighbors_of(edges, n):
    N = {i: [] for i in range(n)}
    for i, j in edges:
        N[i].append(j)
        N[j].append(i)
    return {i: tuple(sorted(v)) for i, v in N.items()}


def static_table(n, edges, exterior, phi):
    """Static weight of every configuration, indexed by the base-6 code with site 0 most significant."""
    out = []
    for v in product(range(M), repeat=n):
        out.append(prod(phi[v[i]][v[j]] for i, j in edges) * prod(phi[v[x]][o] for x in range(n) for o in exterior[x]))
    return out


def subwindow_law(delta, edges, exterior, phi, comp_sites, comp_vals, n):
    """mu_Delta^{omega'}: internal edges of Delta, exterior records of Lambda at Delta, records of Lambda\\Delta adjacent to Delta."""
    N = neighbors_of(edges, n)
    dpos = {x: i for i, x in enumerate(delta)}
    internal = [(dpos[a], dpos[b]) for a, b in edges if a in dpos and b in dpos]
    if mut("spec_face_wrong_subwindow") and len(delta) == 4:
        internal = [(0, 1), (1, 2), (2, 3), (3, 0)]
    cval = dict(zip(comp_sites, comp_vals))
    ext = {i: [] for i in range(len(delta))}
    for x in delta:
        if not mut("spec_conditional_ignores_exterior"):
            ext[dpos[x]].extend(exterior[x])
        for y in N[x]:
            if y in cval:
                ext[dpos[x]].append(cval[y])
        if mut("spec_conditional_two_hop"):
            for y in N[x]:
                for z in N[y]:
                    if z in cval and z not in N[x] and z != x:
                        ext[dpos[x]].append(cval[z])
    law = []
    for u in product(range(M), repeat=len(delta)):
        law.append(prod(phi[u[a]][u[b]] for a, b in internal) * prod(phi[u[i]][o] for i in range(len(delta)) for o in ext[i]))
    return law


def conditional_matches(n, edges, exterior, phi, delta, table):
    """C1 on one sub-window (Delta = the leading sites 0..k-1 in index order): every complement configuration."""
    k = len(delta)
    comp = tuple(range(k, n))
    block = M ** (n - k)
    ok = True
    N = neighbors_of(edges, n)
    adjacent = tuple(y for y in comp if any(y in N[x] for x in delta))
    groups: dict = {}
    for c_code, cv in enumerate(product(range(M), repeat=n - k)):
        full = [table[d * block + c_code] for d in range(M ** k)]
        sub = subwindow_law(delta, edges, exterior, phi, comp, cv, n)
        sf, ss = sum(full), sum(sub)
        if any(full[d] * ss != sub[d] * sf for d in range(M ** k)):
            ok = False
            break
        key = tuple(cv[comp.index(y)] for y in adjacent)
        if key in groups:
            g = groups[key]
            if any(full[d] * g[1] != g[0][d] * sf for d in range(M ** k)):
                ok = False
                break
        else:
            groups[key] = (full, sf)
    return ok, len(groups), len(comp) - len(adjacent)


def family_c(checks: Checks) -> None:
    res = {}
    for triple in TRIPLES:
        phi = phi_table(triple)
        tab = static_table(8, CUBE_EDGES, CUBE_EXTERIOR, phi)
        res[("cube", triple)] = {k: conditional_matches(8, CUBE_EDGES, CUBE_EXTERIOR, phi, tuple(range(k)), tab) for k in (4, 2, 1)}
        del tab
        tab = static_table(4, CYCLE_EDGES, CYCLE_EXTERIOR, phi)
        res[("cycle", triple)] = {k: conditional_matches(4, CYCLE_EDGES, CYCLE_EXTERIOR, phi, tuple(range(k)), tab) for k in (2, 1)}
    face = all(res[("cube", t)][4][0] for t in TRIPLES)
    checks.check("C1", face, "cube face (sites 0-3): conditional = mu_Delta^{omega'} for all 6^4 complements, both triples")
    checks.check("C2", all(res[("cube", t)][2][0] for t in TRIPLES), "cube edge (sites 0,1): all 6^6 complements, both triples")
    checks.check("C3", all(res[("cube", t)][1][0] for t in TRIPLES), "cube site 0: all 6^7 complements, both triples")
    checks.check("C4", all(res[("cycle", t)][2][0] for t in TRIPLES), "plaquette edge with exterior (P(e_x), P(-e_y)): all 36 complements, both triples")
    checks.check("C5", all(res[("cycle", t)][1][0] for t in TRIPLES), "plaquette site with exterior: all 216 complements, both triples")
    grp = res[("cube", TRIPLES[0])]
    fr = grp[2][1] == 6 ** 4 and grp[2][2] == 2 and grp[1][1] == 6 ** 3 and grp[1][2] == 4 and res[("cycle", TRIPLES[0])][1][2] == 1
    checks.check("C6", fr, "finite range: cube edge 1296 adjacent-record classes (2 non-adjacent sites), site 216 classes (4), plaquette site (1)")


# ==================================================================== family D
def strip_rows(W):
    return list(product(range(M), repeat=W))


def row_law_p0(rows, K):
    return [Fraction(1, 6) * prod((K[r[j - 1]][r[j]] for j in range(1, len(r))), start=Fraction(1)) for r in rows]


def row_kernel_definition(rows, phi, drop_left=False):
    W = len(rows[0])
    out = []
    for b in rows:
        line = []
        for a in rows:
            w = Fraction(1)
            for j in range(W):
                rec = (b[j],) + (() if (j == 0 or drop_left) else (a[j - 1],))
                w *= rule(a[j], rec, phi)
            line.append(w)
        out.append(line)
    return out


def row_kernel_formula(rows, K, wrong_den=False):
    W = len(rows[0])
    K2 = [[sum(K[a][s] * K[s][b] for s in range(M)) for b in range(M)] for a in range(M)]
    out = []
    for b in rows:
        line = []
        for a in rows:
            w = K[b[0]][a[0]]
            for j in range(1, W):
                den = K2[a[j - 1]][a[j]] if wrong_den else K2[a[j - 1]][b[j]]
                w *= K[a[j - 1]][a[j]] * K[a[j]][b[j]] / den
            line.append(w)
        out.append(line)
    return out


def invariant(p0, P) -> int:
    """Number of row states alpha with (p0 P)(alpha) != p0(alpha)."""
    if mut("invariance_forced_true"):
        return 0
    R = len(p0)
    return sum(1 for k in range(R) if sum(p0[i] * P[i][k] for i in range(R)) != p0[k])


def strip_edges(W, n):
    edges = []
    for i in range(n):
        for j in range(W):
            if j + 1 < W:
                edges.append((i * W + j, i * W + j + 1))
            if i + 1 < n:
                edges.append((i * W + j, (i + 1) * W + j))
    return tuple(edges)


def family_d(checks: Checks, report: dict) -> None:
    d1 = d2 = d3 = d4 = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        K = one_edge_kernel(phi)
        K2 = [[sum(K[a][s] * K[s][b] for s in range(M)) for b in range(M)] for a in range(M)]
        for W in (2, 3):
            rows = strip_rows(W)
            R = len(rows)
            p0 = row_law_p0(rows, K)
            P = row_kernel_definition(rows, phi, drop_left=mut("row_kernel_drops_left_neighbor"))
            Pf = row_kernel_formula(rows, K, wrong_den=mut("row_kernel_formula_wrong_denominator"))
            d1 = d1 and P == Pf and all(sum(P[i]) == 1 for i in range(R))
            d2 = d2 and invariant(p0, P) == 0
            report[("P", triple, W)] = (rows, p0, P)
            joint = {(i, k): p0[i] * P[i][k] for i in range(R) for k in range(R)}
            for j in range(W):
                jj = j + 1 if (mut("pair_law_wrong_column") and j + 1 < W) else j
                vert = {}
                for (i, k), w in joint.items():
                    key = (rows[i][j], rows[k][jj])
                    vert[key] = vert.get(key, Fraction(0)) + w
                d3 = d3 and all(vert[(a, b)] == Fraction(1, 6) * K[a][b] for a in range(M) for b in range(M))
                if j >= 1:
                    hor = {}
                    for (i, k), w in joint.items():
                        key = (rows[k][j - 1], rows[k][j])
                        hor[key] = hor.get(key, Fraction(0)) + w
                    d3 = d3 and all(hor[(a, b)] == Fraction(1, 6) * K[a][b] for a in range(M) for b in range(M))
            # the telescoping premise on the strip: joint law of (alpha_0, beta_1) is (1/6) K^2
            if W >= 2:
                diag = {}
                for (i, k), w in joint.items():
                    key = (rows[k][0], rows[i][1])
                    diag[key] = diag.get(key, Fraction(0)) + w
                d3 = d3 and all(diag[(a, b)] == Fraction(1, 6) * K2[a][b] for a in range(M) for b in range(M))
            # direct finite-strip formation law from block 01's definition versus p0 P^(n-1)
            for n in ((2, 3) if W == 2 else (2,)):
                edges = strip_edges(W, n)
                nbrs = neighbors_of(edges, W * n)
                law = formation_law_on_graph(W * n, nbrs, tuple(range(W * n)), phi, all_neighbors=mut("direct_strip_law_mismatch"))
                marg = [dict() for _ in range(n)]
                pair = {}
                for v, w in law.items():
                    for i in range(n):
                        key = v[i * W:(i + 1) * W]
                        marg[i][key] = marg[i].get(key, Fraction(0)) + w
                    key = (v[(n - 2) * W:(n - 1) * W], v[(n - 1) * W:])
                    pair[key] = pair.get(key, Fraction(0)) + w
                law_i = list(p0)
                chain_rows = [law_i]
                for i in range(1, n):
                    law_i = [sum(law_i[a] * P[a][k] for a in range(R)) for k in range(R)]
                    chain_rows.append(law_i)
                for i in range(n):
                    d4 = d4 and all(marg[i][rows[k]] == chain_rows[i][k] for k in range(R))
                d4 = d4 and all(pair[(rows[a], rows[k])] == chain_rows[n - 2][a] * P[a][k] for a in range(R) for k in range(R))
    d9 = True
    for triple in TRIPLES:
        rows3, p03, P3 = report[("P", triple, 3)]
        rows2, p02, P2 = report[("P", triple, 2)]
        cols = (0, 2) if mut("restriction_lemma_broken") else (0, 1)
        restricted: dict = {}
        for i, b in enumerate(rows3):
            for k, a in enumerate(rows3):
                key = (tuple(b[c] for c in cols), tuple(a[c] for c in cols))
                restricted[key] = restricted.get(key, Fraction(0)) + p03[i] * P3[i][k]
        idx2 = {r: i for i, r in enumerate(rows2)}
        d9 = d9 and all(restricted[(b, a)] == p02[idx2[b]] * P2[idx2[b]][idx2[a]] for b in rows2 for a in rows2)
    checks.check("D9", d9, "restriction lemma: width-3 two-row joint on columns 0,1 equals the width-2 joint, both triples")
    checks.check("D1", d1, "E2 row kernel from the formula equals the kernel from the definition entrywise, W = 2, 3, both triples; rows sum to one")
    checks.check("D2", d2, "E3: p_0 P = p_0 exactly for W = 2, 3, both triples (all 6^W row states)")
    checks.check("D3", d3, "E4: every vertical and horizontal nearest-neighbor pair has law (1/6) K; the diagonal pair (alpha_0, beta_1) has law (1/6) K^2")
    checks.check("D4", d4, "direct finite-strip formation law (W=2: n=2,3; W=3: n=2) = p_0 P^(n-1) on every row marginal and row-pair joint")


def width4_invariance(triple) -> bool:
    """p_0 P = p_0 at W = 4 with integer numerators over a common denominator (1296 x 1296 kernel, from the definition)."""
    phi = phi_table(triple)
    W = 4
    z1 = sum(phi[0])
    z2 = {(a, b): sum(phi[s][a] * phi[s][b] for s in range(M)) for a in range(M) for b in range(M)}
    L = lcm(*set(z2.values()))
    rows = strip_rows(W)
    p0n = [prod(phi[r[j - 1]][r[j]] for j in range(1, W)) for r in rows]  # p_0 = p0n / (6 Z_1^(W-1))
    ok = True
    for ia, a in enumerate(rows):
        tot = 0
        for ib, b in enumerate(rows):
            x = p0n[ib] * phi[a[0]][b[0]]
            for j in range(1, W):
                x *= phi[a[j]][a[j - 1]] * phi[a[j]][b[j]] * (L // z2[(a[j - 1], b[j])])
            tot += x
        # (p_0 P)(a) = tot / (6 Z_1^(W-1) Z_1 L^(W-1)); equality with p_0(a) iff tot == p0n(a) Z_1 L^(W-1)
        if tot != p0n[ia] * z1 * L ** (W - 1):
            ok = False
            break
    return ok


def family_d_controls(checks: Checks, report: dict) -> None:
    checks.check("D5", all(width4_invariance(t) for t in TRIPLES), "width 4: p_0 P = p_0 exactly on all 1296 row states (integer numerators), both triples")
    # constant rule: K uniform, p_0 uniform, invariance trivial
    ctr = (2, 2, 3) if mut("constant_rule_not_uniform") else CONSTANT_TRIPLE
    phi_c = phi_table(ctr)
    Kc = one_edge_kernel(phi_c)
    okc = True
    for W in (2, 3):
        rows = strip_rows(W)
        p0 = row_law_p0(rows, Kc)
        okc = okc and all(x == Fraction(1, M ** W) for x in p0) and invariant(p0, row_kernel_definition(rows, phi_c)) == 0
    checks.check("D6", okc, "constant rule (2,2,2): K uniform, p_0 uniform on 6^W states, p_0 P = p_0, W = 2, 3")
    # asymmetric control: phi(a,b) = weights + [a < b]; K(a -> s) = phi(s,a)/sum_t phi(t,a)
    base = phi_table(TRIPLES[0])
    phi_asym = tuple(tuple(base[a][b] + (0 if mut("asymmetric_control_passes") else (1 if a < b else 0)) for b in range(M)) for a in range(M))
    viol = {}
    for W in (2, 3):
        rows = strip_rows(W)
        Ka = [[Fraction(phi_asym[s][a], sum(phi_asym[t][a] for t in range(M))) for s in range(M)] for a in range(M)]
        p0 = row_law_p0(rows, Ka)
        viol[W] = invariant(p0, row_kernel_definition(rows, phi_asym))
    report["asym_violations"] = viol
    checks.check("D7", viol[2] > 0 and viol[3] > 0, f"asymmetric-weight control: p_0 P != p_0 on {viol[2]}/36 (W=2) and {viol[3]}/216 (W=3) row states")
    # three-recorded-neighbor remark: cube, order 0..7, last site 7 has recorded neighbors 3, 5, 6
    phi = phi_table(TRIPLES[0])
    nbrs = neighbors_of(CUBE_EDGES, 8)
    marg: dict = {}
    for v in product(range(M), repeat=7):
        num = 1
        den = 1
        for x in range(7):
            rec = tuple(v[y] for y in nbrs[x] if y < x)
            num *= prod(phi[v[x]][e] for e in rec)
            den *= sum(prod(phi[t][e] for e in rec) for t in range(M))
        key = (v[3], v[5], v[6])
        marg[key] = marg.get(key, Fraction(0)) + Fraction(num, den)
    z3 = {k: sum(phi[s][k[0]] * phi[s][k[1]] * phi[s][k[2]] for s in range(M)) for k in marg}
    if mut("three_neighbor_witness_forced"):
        marg = {k: Fraction(z3[k]) for k in marg}
    keys = sorted(marg)
    k0 = keys[0]
    proportional = all(marg[k] * z3[k0] == marg[k0] * z3[k] for k in keys)
    n_bad = sum(1 for k in keys if marg[k] * z3[k0] != marg[k0] * z3[k])
    checks.check("D8", not proportional and n_bad > 0, f"cube sweep 0..7 at (3,1,2): joint law of the last site's three recorded neighbors is not proportional to Z_3 ({n_bad}/216 triples off)")


# ==================================================================== family E
lam, yy = sp.symbols("lam y")


def frac_of(x) -> Fraction:
    x = sp.Rational(x)
    return Fraction(int(x.p), int(x.q))


def rat_of(x: Fraction):
    return sp.Rational(x.numerator, x.denominator)


def dec(x: Fraction, digits: int, up: bool = False) -> str:
    """Exact decimal expansion of a rational rounded down (or up when up=True); integer arithmetic; a label, not evidence."""
    sign = "-" if x < 0 else ""
    x = abs(x)
    scaled = (x.numerator * 10 ** digits) // x.denominator
    if up and scaled * x.denominator != x.numerator * 10 ** digits:
        scaled += 1
    s = str(scaled).rjust(digits + 1, "0")
    return f"{sign}{s[:-digits]}.{s[-digits:]}"


class Field:
    """Q(lam_1) = Q[lam]/(m) for a monic irreducible m; elements are coefficient lists of Fractions."""

    def __init__(self, m_poly: sp.Poly) -> None:
        self.m = m_poly
        self.d = m_poly.degree()
        self.mc = [frac_of(c) for c in m_poly.all_coeffs()]
        assert self.mc[0] == 1

    def el(self, coeffs):
        return [Fraction(c) for c in coeffs] + [Fraction(0)] * (self.d - len(coeffs))

    def add(self, a, b):
        return [x + y for x, y in zip(a, b)]

    def sub(self, a, b):
        return [x - y for x, y in zip(a, b)]

    def scal(self, c, a):
        return [c * x for x in a]

    def mul(self, a, b):
        d = self.d
        r = [Fraction(0)] * (2 * d - 1)
        for i, x in enumerate(a):
            if x:
                for j, z in enumerate(b):
                    if z:
                        r[i + j] += x * z
        for k in range(2 * d - 2, d - 1, -1):
            c = r[k]
            if c:
                r[k] = Fraction(0)
                for i in range(1, d + 1):
                    r[k - i] -= c * self.mc[i]
        return r[:d]

    def to_poly(self, a) -> sp.Poly:
        return sp.Poly(sum(rat_of(x) * lam ** i for i, x in enumerate(a)) + sp.Integer(0), lam, domain="QQ")

    def from_poly(self, p: sp.Poly):
        return self.el([frac_of(c) for c in p.all_coeffs()[::-1]])

    def inv(self, a):
        return self.from_poly(self.to_poly(a).invert(self.m))

    def is_zero(self, a) -> bool:
        return all(x == 0 for x in a)


def horner_interval(coeffs, lo: Fraction, hi: Fraction):
    """Rigorous rational bounds of g(t) = sum c_k t^k over t in [lo, hi] with 0 < lo (monotone powers)."""
    glo = Fraction(0)
    ghi = Fraction(0)
    for k, c in enumerate(coeffs):
        if c > 0:
            glo += c * lo ** k
            ghi += c * hi ** k
        elif c < 0:
            glo += c * hi ** k
            ghi += c * lo ** k
    return glo, ghi


def bisect_root(poly: sp.Poly, lo: Fraction, hi: Fraction, width: Fraction):
    """Bisect a sign-change interval of a simple real root down to the given width (exact rationals)."""
    flo = poly.eval(rat_of(lo))
    assert flo != 0 and poly.eval(rat_of(hi)) != 0 and (flo > 0) != (poly.eval(rat_of(hi)) > 0)
    while hi - lo >= width:
        mid = (lo + hi) / 2
        fm = poly.eval(rat_of(mid))
        if fm == 0:
            return mid, mid
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return lo, hi


def row_orbits(rows):
    seen: dict = {}
    orbits = []
    for r in rows:
        if r in seen:
            continue
        O = set()
        for g in ROTATIONS:
            rr = tuple(rotate_menu(g, a) for a in r)
            O.add(rr)
            O.add(rr[::-1])
        for x in O:
            seen[x] = len(orbits)
        orbits.append(sorted(O))
    return orbits, seen


def transfer_pieces(W, phi):
    def A(r):
        return prod((phi[r[j]][r[j + 1]] for j in range(W - 1)), start=1)

    def V(r, r2):
        return prod(phi[r[j]][r2[j]] for j in range(W))

    return A, V


def commutes(rows, A, V, reps) -> bool:
    """T(g rho, g rho') = T(rho, rho') for every g in G (24 rotations x reflection) on the declared row sample."""
    gens = [(g, flip) for g in ROTATIONS for flip in (False, True)]

    def act(g, flip, r):
        rr = tuple(rotate_menu(g, a) for a in r)
        return rr[::-1] if flip else rr

    def T(r, r2):
        base = V(r, r2) * A(r2)
        if mut("quotient_not_commuting") and r == rows[0] and r2 == rows[1]:
            base += 1
        return base

    return all(T(act(g, f, r), act(g, f, r2)) == T(r, r2) for r in reps for r2 in rows for g, f in gens)


def perron_data(Q, K):
    """Characteristic polynomial (factored), the Perron factor, an isolating interval of width < 10^-30."""
    cp = sp.Poly(sp.Matrix(Q).charpoly(lam).as_expr(), lam, domain="QQ")
    factors = [(sp.Poly(f, lam, domain="QQ"), m) for f, m in sp.factor_list(cp.as_expr())[1]]
    cands = []
    for P_, _m in factors:
        for (a, b), _k in P_.intervals():
            cands.append((frac_of(a), frac_of(b), P_))
    cands.sort(key=lambda c: c[1])
    lo, hi, mp = cands[-2] if mut("perron_interval_wrong_root") else cands[-1]
    if lo == hi:
        return cp, factors, mp, lo, hi
    lo, hi = bisect_root(mp, lo, hi, Fraction(1, 10 ** 30))
    return cp, factors, mp, lo, hi


CHARPOLY_312_W3 = lam**5 * (lam**3 - 7312 * lam**2 + 2578432 * lam - 221134848)


def center_row_value(rows, T, Avec, n: int, left0=None, right0=None) -> Fraction:
    """Center-row pair-parallel probability of the n-row static strip: w = (b_L T^c)(rho) (T^(n-1-c) b_R)(rho); default b_L = A, b_R = 1 (open ends)."""
    R = len(rows)
    c = n // 2
    left = list(Avec) if left0 is None else list(left0)
    for _ in range(c):
        left = [sum(left[i] * T[i][k] for i in range(R)) for k in range(R)]
    right = [1] * R if right0 is None else list(right0)
    for _ in range(n - 1 - c):
        right = [sum(T[i][k] * right[k] for k in range(R)) for i in range(R)]
    w = [left[k] * right[k] for k in range(R)]
    return Fraction(sum(w[k] for k in range(R) if rows[k][0] == rows[k][1]), sum(w))


def static_strip(checks: Checks, report: dict, W: int, triple, exact: bool) -> dict:
    phi = phi_table(triple)
    rows = strip_rows(W)
    R = len(rows)
    A, V = transfer_pieces(W, phi)
    orbits, seen = row_orbits(rows)
    Kn = len(orbits)
    reps = [O[0] for O in orbits] if W == 3 else rows
    T = [[V(r, r2) * A(r2) for r2 in rows] for r in rows]
    Q = [[sum(V(orbits[a][0], r2) * A(r2) for r2 in orbits[b]) for b in range(Kn)] for a in range(Kn)]
    out = {"orbits": Kn, "commutes": commutes(rows, A, V, reps)}
    cp, factors, mp, lo, hi = perron_data(Q, Kn)
    out["cp"] = cp
    out["cp_literal_ok"] = sp.expand(cp.as_expr() - CHARPOLY_312_W3) == 0 if (W == 3 and triple == (3, 1, 2)) else True
    if mut("charpoly_coefficient_off") and W == 3 and triple == (3, 1, 2):
        out["cp_literal_ok"] = sp.expand(cp.as_expr() - (CHARPOLY_312_W3 + lam**7)) == 0
    out["mp_degree"] = mp.degree()
    out["lam_interval"] = (lo, hi)
    F = Field(mp)
    d = F.d
    lam1 = F.el([0, 1])
    n = Kn - 1
    Mx = [[F.sub(F.el([Q[i][j]]), lam1 if i == j else F.el([0])) for j in range(1, Kn)] + [F.scal(Fraction(-1), F.el([Q[i][0]]))] for i in range(1, Kn)]
    for col in range(n):
        piv = next(r for r in range(col, n) if not F.is_zero(Mx[r][col]))
        Mx[col], Mx[piv] = Mx[piv], Mx[col]
        pinv = F.inv(Mx[col][col])
        Mx[col] = [F.mul(pinv, x) for x in Mx[col]]
        for r in range(n):
            if r != col and not F.is_zero(Mx[r][col]):
                f_ = Mx[r][col]
                Mx[r] = [F.sub(a_, F.mul(f_, b_)) for a_, b_ in zip(Mx[r], Mx[col])]
    x = [F.el([1])] + [Mx[i][n] for i in range(n)]
    qx_ok = all(F.is_zero(F.sub([sum(Q[i][j] * x[j][k] for j in range(Kn)) for k in range(d)], F.mul(lam1, x[i]))) for i in range(Kn))
    positive = all(horner_interval(x[i], lo, hi)[0] > 0 for i in range(Kn))
    out["perron_vector_ok"] = qx_ok and positive
    rho1 = [list(x[seen[r]]) for r in rows]
    if mut("eigvec_residual_nonzero"):
        rho1[1] = F.add(rho1[1], F.el([1]))
    t_ok = True
    left_ok = True
    for i in range(R):
        acc = [sum(T[i][j] * rho1[j][k] for j in range(R)) for k in range(d)]
        if not F.is_zero(F.sub(acc, F.mul(lam1, rho1[i]))):
            t_ok = False
            break
    Avec = [A(r) for r in rows]
    for j in range(R):
        acc = [sum(Avec[i] * rho1[i][k] * T[i][j] for i in range(R)) for k in range(d)]
        if not F.is_zero(F.sub(acc, F.scal(Fraction(Avec[j]), F.mul(lam1, rho1[j])))):
            left_ok = False
            break
    out["lift_ok"] = t_ok and left_ok
    num = F.el([0])
    den = F.el([0])
    for k, r in enumerate(rows):
        sq = rho1[k] if mut("limit_law_uses_rho_not_squared") else F.mul(rho1[k], rho1[k])
        t = F.scal(Fraction(Avec[k]), sq)
        den = F.add(den, t)
        if r[0] == r[1]:
            num = F.add(num, t)
    s = F.mul(num, F.inv(den))
    res = sp.Poly(sp.resultant(mp.as_expr(), yy - F.to_poly(s).as_expr(), lam), yy, domain="QQ")
    rfactors = [sp.Poly(f, yy, domain="QQ") for f, _m in sp.factor_list(res.as_expr())[1]]
    glo, ghi = horner_interval(s, lo, hi)
    while ghi - glo >= Fraction(1, 10 ** 30):
        lo, hi = bisect_root(mp, lo, hi, (hi - lo) / 2)
        glo, ghi = horner_interval(s, lo, hi)
    if mut("s_inf_enclosure_contains_formation_value"):
        glo, ghi = glo - Fraction(1, 10), ghi + Fraction(1, 10)
    minpolys = [P_ for P_ in rfactors if P_.count_roots(rat_of(glo), rat_of(ghi)) >= 1]
    out["s_minpoly"] = minpolys[0] if len(minpolys) == 1 else None
    out["s_identified"] = len(minpolys) == 1 and minpolys[0].count_roots(rat_of(glo), rat_of(ghi)) == 1 and ghi - glo < Fraction(1, 10 ** 30)
    out["s_enclosure"] = (glo, ghi)
    form = Fraction(triple[0], triple[0] + triple[1] + 4 * triple[2])
    out["excludes_formation"] = not (glo <= form <= ghi)
    seq = [(n_, center_row_value(rows, T, Avec, n_)) for n_ in (3, 5, 7, 9, 11, 13)]
    if mut("finite_n_sequence_shuffled"):
        seq[0], seq[-1] = (seq[0][0], seq[-1][1]), (seq[-1][0], seq[0][1])
    dist = [max(glo - v, v - ghi, Fraction(0)) for _n, v in seq]
    out["finite_n"] = seq
    out["finite_n_ok"] = all(dist[i + 1] < dist[i] for i in range(len(dist) - 1)) and dist[-1] < Fraction(1, 10 ** 6)
    # boundary independence of the deep-row limit: exterior records P(e_y) on the first and last rows (a positive boundary vector h)
    hvec = [prod(phi[r[j]][2] for j in range(W)) for r in rows]
    bval = center_row_value(rows, T, Avec, 13, left0=[Avec[k] * hvec[k] for k in range(R)], right0=hvec)
    if mut("boundary_dependence_forged"):
        bval = bval + Fraction(1, 100)
    out["boundary_ok"] = max(glo - bval, bval - ghi, Fraction(0)) < Fraction(1, 10 ** 6)
    out["boundary_value"] = bval
    # second eigenvalue: every root of every factor real; m = max modulus of the non-Perron roots (exact rational bound)
    all_real = all(P_.count_roots() == P_.degree() for P_, _m in factors)
    bounds = []
    for P_, _m in factors:
        for (a, b), _k in P_.intervals():
            a, b = frac_of(a), frac_of(b)
            if a != b:
                a, b = bisect_root(P_, a, b, Fraction(1, 10 ** 20))
            if not (P_ == mp and b >= lo):
                bounds.append(max(abs(a), abs(b)))
    m_bound = max(bounds) / (2 if mut("second_eigenvalue_bound_too_small") else 1)
    inside = all(P_.count_roots(rat_of(-m_bound), rat_of(m_bound)) == P_.degree() - (1 if P_ == mp else 0) for P_, _m in factors)
    out["second_ok"] = all_real and inside and m_bound < lo
    out["m_bound"] = m_bound
    out["ratio_bound"] = m_bound / lo
    if exact:
        print(f"exact W={W} {triple}: charpoly={cp.as_expr()}")
        print(f"exact W={W} {triple}: lam1 in [{lo}, {hi}]")
        print(f"exact W={W} {triple}: s_inf minimal polynomial = {out['s_minpoly'].as_expr() if out['s_minpoly'] is not None else None}")
        print(f"exact W={W} {triple}: s_inf in [{glo}, {ghi}]")
        print(f"exact W={W} {triple}: finite n: {[(n_, str(v)) for n_, v in seq]}")
        print(f"exact W={W} {triple}: m = {m_bound}; ratio bound = {out['ratio_bound']}")
    return out


def family_e(checks: Checks, report: dict, exact: bool) -> None:
    res = {(W, t): static_strip(checks, report, W, t, exact) for W in (3, 2) for t in TRIPLES}
    n3 = 9 if mut("orbit_count_wrong") else 8
    checks.check("E1", all(res[(3, t)]["orbits"] == n3 for t in TRIPLES) and all(res[(2, t)]["orbits"] == 3 for t in TRIPLES), f"row orbits under G: {res[(3, TRIPLES[0])]['orbits']} at W = 3, {res[(2, TRIPLES[0])]['orbits']} at W = 2")
    checks.check("E2", all(r["commutes"] for r in res.values()), "T(g rho, g rho') = T(rho, rho') for all 48 g: exhaustive at W = 2, orbit representatives x all rows at W = 3")
    checks.check("E3", all(r["cp_literal_ok"] for r in res.values()), "charpoly of Q at W = 3, (3,1,2) = lam^5 (lam^3 - 7312 lam^2 + 2578432 lam - 221134848)")
    degs = {(W, t): res[(W, t)]["mp_degree"] for W in (3, 2) for t in TRIPLES}
    checks.check("E4", all(r["lam_interval"][1] - r["lam_interval"][0] < Fraction(1, 10 ** 30) and r["lam_interval"][0] > 0 for r in res.values()), f"Perron root: minimal polynomial degrees W3 {degs[(3, TRIPLES[0])]},{degs[(3, TRIPLES[1])]} W2 {degs[(2, TRIPLES[0])]},{degs[(2, TRIPLES[1])]}; isolating widths < 10^-30")
    checks.check("E5", all(r["perron_vector_ok"] for r in res.values()), "Perron vector of Q over Q(lam_1): Q x = lam_1 x on every row, all entries positive on the interval")
    checks.check("E6", all(r["lift_ok"] for r in res.values()), "lift: T rho_1 = lam_1 rho_1 and (A rho_1)^T T = lam_1 (A rho_1)^T exactly in Q(lam_1), 216 and 36 rows")
    checks.check("E7", all(r["s_identified"] for r in res.values()), "s_inf: one irreducible factor of the resultant has exactly one root in the enclosure; width < 10^-30")
    for t in TRIPLES:
        r = res[(3, t)]
        glo, ghi = r["s_enclosure"]
        print(f"info W=3 {t}: lam_1 = {dec(r['lam_interval'][0], 12)}..; s_inf in [{dec(glo, 22)}, {dec(ghi, 22, True)}] (rounded outward), formation value {Fraction(t[0], t[0] + t[1] + 4 * t[2])}")
        print(f"info W=3 {t}: finite n center row: " + ", ".join(f"n={n_} {dec(v, 10)}" for n_, v in r["finite_n"]))
        print(f"info W=3 {t}: |lam_j| <= m = {dec(r['m_bound'], 6, True)} for all non-Perron roots (all roots real); |lam_2/lam_1| <= {dec(r['ratio_bound'], 10, True)}")
    for t in TRIPLES:
        r = res[(2, t)]
        print(f"info W=2 {t}: s_inf in [{dec(r['s_enclosure'][0], 18)}, {dec(r['s_enclosure'][1], 18, True)}]; |lam_2/lam_1| <= {dec(r['ratio_bound'], 8, True)}; min poly degree {r['mp_degree']}")
    checks.check("E8", all(r["excludes_formation"] for r in res.values()), "the enclosure of s_inf excludes the formation value p/(p+q+4r) at W = 2, 3, both triples")
    checks.check("E9", all(r["finite_n_ok"] for r in res.values()), "finite-n center-row values n = 3..13: distance to the enclosure strictly decreasing, final < 10^-6")
    checks.check("E10", all(r["second_ok"] for r in res.values()), "second eigenvalue: all charpoly roots real; every non-Perron root in [-m, m] with rational m < lam_1 (Sturm)")
    checks.check("E11", all(r["boundary_ok"] for r in res.values()), "boundary independence: end records P(e_y) on both end rows, n = 13 center-row value within 10^-6 of the enclosure, W = 2, 3, both triples")
    report["E"] = res


# ==================================================================== family F
FENCES = (
    "This note selects no physical formation order; the row sweep is a declared order whose exact solvability is a property of sweeps in which each site forms with one in-row predecessor and the site below it as its recorded neighbors, on two-dimensional windows with an unrecorded exterior.",
    "No statement is made about the static law of the plane, about uniqueness of an infinite-volume static law on the cubic lattice, or about any three-recorded-neighbor sweep; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "This note does not derive, explain, bear on or decide the parked statistical bridge, the Born form, or the gravity lane's action.",
    "Every negative sentence in this note is an exact statement on the declared strips and windows or a corollary of Theorems E and F at their stated scope; none is a route no-go beyond that scope.",
)
FORBIDDEN = (
    "selects the physical rule", "derives the Born", "explains the gate", "bears on the gate",
    "infinite-lattice law", "the framework's action is", "the order is physical", "certified",
    "closed the gate", "axiom is amended", "fires wake condition",
    "distinct orders give distinct laws", "witnesses the variation clause",
    "washes out", "the physical order", "unique on the lattice", "Dobrushin", "the plane's static law is",
)
CLAIM_INJECTIONS = {
    "claim_order_selected": "Therefore the row sweep is the physical order.",
    "claim_plane_static": "The plane's static law is the limit law computed here.",
    "claim_z3_uniqueness": "The infinite-volume static law is unique on the lattice.",
    "claim_washout": "Along the sweep the normalizer history washes out.",
    "claim_gate_fired": "This note fires wake condition 1 of the parked decision.",
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
    evalf = "eva" + "lf("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln]
    checks.check("F3", not bad and len(scan) > 500, f"runner source: no floating-point literal, conversion or evaluation call ({len(bad)} hits)")


# ==================================================================== family G
N5_LINES = (
    "per_element: executed — every row state of the width-2, 3 and 4 strips, every configuration of the cube and plaquette sub-window checks, both triples, exact",
    "per_site: executed — the sub-window conditional at every site class (face, edge, site) of the cube and the plaquette; every column of every row of the strip pair laws",
    "per_mode: executed — the quotient transfer matrix's characteristic polynomial, its Perron root, eigenvector and second-eigenvalue bound, all exact (Sturm, resultant, Q(lam_1))",
    "per_block: executed — the row-to-row kernel block by block for widths 2, 3, 4; the finite-n center-row values for n = 3..13; the cube's three-neighbor witness",
    "lattice_wide: checked and not executed — strips of widths 2 and 3 only for the static law; the plane and the cubic lattice's infinite-volume law are named, not computed",
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
    exact = "--exact" in argv
    checks = Checks()
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8") if AXIOM_PATH.is_file() else ""
    parent_text = PARENT_NOTE_PATH.read_text(encoding="utf-8") if PARENT_NOTE_PATH.is_file() else ""
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the six-projector menu, the product rule at two exact triples; strips of widths 2, 3, 4 (sweep) and 2, 3 (static); exact arithmetic; no plane, no cubic-lattice uniqueness, no order selected")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, note_text, axiom_text, parent_text)
    family_b(checks)
    family_c(checks)
    family_d(checks, report)
    family_d_controls(checks, report)
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
