#!/usr/bin/env python3
"""Exact checks: the static strip at widths 4 and 5, rigorously enclosed; the separation from the formation value.

Scope.  The menu is the six Bloch-axis projectors inside M_2(C); the rule is the covariant positive product rule
with orbit weights (p, q, r) at the declared exact triples (3, 1, 2) and (5, 2, 4).  On the open-boundary strips of
widths 4 and 5 the row transfer matrix T(rho, rho') = V(rho, rho') A(rho') is reduced by the row symmetry group G
(24 proper rotations acting on the menu, times the row reversal) to the orbit quotient Q (38 and 178 orbits).
Q is self-adjoint for the weights w_O = |O| A_O (S2), so its spectrum is real and the sum of the squared eigenvalues
is tr(Q^2).  The deep-row pair-parallel statistics s_edge (pair (0, 1)) and s_inner (the innermost pair) are enclosed
in exact rational intervals of width below 10^-50 by an elementary route (S3): the two-sided ratio bounds on the
Perron root from y = Q^40 1, the trace bound on every other eigenvalue, the residual-gap bound on the angle between
y and the Perron vector, and a Cauchy-Schwarz step on the statistic.  Every enclosure excludes the formation value
f = p/(p + q + 4r).  The Krylov dimension of Q on the all-ones vector is 8, 30, 16, 111 (modular ranks with two
Mersenne primes, the exact integer dependency verified on every orbit); where it is at most 16 the statistics are
identified as algebraic numbers by their minimal polynomials (S4).  The separation s - f > 0 is executed at widths
2, 3, 4, 5 (S5).  Nothing is said about wider strips or the plane, no monotonicity in the width is claimed, no order
is selected as physical.  Exact integer, rational and symbolic arithmetic only: the runner scans its own source and
fails if a floating-point literal or conversion appears, and every decimal label it prints is an integer-arithmetic
expansion of a rational, rounded outward.
"""

from __future__ import annotations

import re
import sys
import time
from fractions import Fraction
from itertools import permutations, product
from math import isqrt, prod
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_STATIC_STRIP_WIDTHS_4_5_RIGOROUS_ENCLOSURE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-09-07.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
PARENT_NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[2]
CLAIM_ID = "admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_bounded_theorem_note_2026-09-07"
PARENT_CLAIM_ID = "admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06"
PARENT_FRAGMENT = "so the deep-row law is `w` whatever the end records"
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
    "orbit_count_wrong": "B",
    "commutation_broken": "B",
    "sector_full_mismatch": "B",
    "quotient_row_identity_broken": "B",
    "self_adjointness_broken": "C",
    "krylov_dimension_off": "C",
    "dependency_not_verified": "C",
    "cw_interval_forged": "C",
    "charpoly_factor_mismatch": "C",
    "largest_root_outside_interval": "C",
    "trace_bound_forged": "D",
    "residual_gap_ignored": "D",
    "residual_forged": "D",
    "s_enclosure_contains_formation_value": "D",
    "finite_n_sequence_shuffled": "D",
    "boundary_dependence_forged": "D",
    "resultant_factor_wrong": "D",
    "w2_w3_literals_off": "D",
    "field_vector_not_eigen": "D",
    "separation_sign_flipped": "E",
    "ratio_bound_too_small": "E",
    "inner_edge_order_flipped": "E",
    "claim_plane_limit": "F",
    "claim_monotone_in_W": "F",
    "claim_washes_out": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


# ------------------------------------------------------------------- output
OUT_LINES: list[str] = []
DEC_LABELS: set[str] = set()


def say(line: str) -> None:
    OUT_LINES.append(line)
    print(line)


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
        say(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        say(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def dec(x: Fraction, digits: int, up: bool = False) -> str:
    """Exact decimal expansion of a rational, rounded down (up=True: up); integer arithmetic; a label, not evidence."""
    sign = "-" if x < 0 else ""
    x = abs(x)
    scaled = (x.numerator * 10 ** digits) // x.denominator
    if up and scaled * x.denominator != x.numerator * 10 ** digits:
        scaled += 1
    s = str(scaled).rjust(digits + 1, "0")
    label = f"{sign}{s[:-digits]}.{s[-digits:]}"
    DEC_LABELS.add(label.lstrip("-"))
    return label


def dec_sci(x: Fraction, mant_digits: int = 2) -> str:
    """Upper label m x 10^-e of a small positive rational, m rounded up (integer arithmetic)."""
    e = 0
    while x * 10 ** e < 1:
        e += 1
    return f"{dec(x * 10 ** e, mant_digits, up=True)} x 10^-{e}"


def floor_scaled(x: Fraction, digits: int) -> int:
    return (x.numerator * 10 ** digits) // x.denominator


def ceil_scaled(x: Fraction, digits: int) -> int:
    return -((-x.numerator * 10 ** digits) // x.denominator)


def sqrt_upper(x: Fraction) -> Fraction:
    """A rational upper bound of sqrt(x) for x >= 0: integer square root at scale 10^80, rounded up."""
    assert x >= 0
    scale = 10 ** 80
    n = x.numerator * scale * scale // x.denominator + 1
    return Fraction(isqrt(n) + 1, scale)


# --------------------------------------------------------------------- menu
# Menu order: P(+e_x), P(-e_x), P(+e_y), P(-e_y), P(+e_z), P(-e_z); rebuilt here, not imported.
MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
PAR, ANTI, ORTH = 0, 1, 2
TRIPLES = ((3, 1, 2), (5, 2, 4))
E_Y = 2  # the menu index of P(+e_y), the end-row record of the boundary check


def vdot(a: int, b: int) -> int:
    return sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))


def pair_orbit(a: int, b: int) -> int:
    d = vdot(a, b)
    return PAR if d == 1 else (ANTI if d == -1 else ORTH)


def phi_table(triple):
    return tuple(tuple(triple[pair_orbit(a, b)] for b in range(M)) for a in range(M))


def formation_value(triple) -> Fraction:
    p, q, r = triple
    return Fraction(p, p + q + 4 * r)


def rotation_images():
    """The 24 proper rotations of the cube as maps on the menu indices: signed axis permutations of determinant +1."""
    out = []
    for perm in permutations((0, 1, 2)):
        for signs in product((1, -1), repeat=3):
            mat = [[0] * 3 for _ in range(3)]
            for i in range(3):
                mat[i][perm[i]] = signs[i]
            det = sum(
                sgn * mat[0][c0] * mat[1][c1] * mat[2][c2]
                for (c0, c1, c2), sgn in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1))
            )
            if det != 1:
                continue
            img = []
            for v in MENU_VECTORS:
                w = tuple(sum(mat[i][j] * v[j] for j in range(3)) for i in range(3))
                img.append(MENU_VECTORS.index(w))
            out.append(tuple(img))
    return tuple(out)


ROTATIONS = rotation_images()
GROUP = tuple((g, flip) for g in ROTATIONS for flip in (False, True))


def act(elem, row):
    g, flip = elem
    rr = tuple(g[a] for a in row)
    return rr[::-1] if flip else rr


class Strip:
    """The width-W strip's row objects at one triple: rows, A, V, orbits, the quotients Q and R, sizes, pair fractions."""

    def __init__(self, W: int, triple) -> None:
        self.W = W
        self.triple = triple
        self.phi = phi_table(triple)
        self.rows = list(product(range(M), repeat=W))
        self.index = {r: i for i, r in enumerate(self.rows)}
        phi = self.phi
        self.Avec = [prod(phi[r[j]][r[j + 1]] for j in range(W - 1)) for r in self.rows]
        seen: dict = {}
        reps: list = []
        sizes: list = []
        for r in self.rows:
            if r in seen:
                continue
            imgs = {act(e, r) for e in GROUP}
            k = len(reps)
            reps.append(r)
            sizes.append(len(imgs))
            for x in imgs:
                seen[x] = k
        self.reps, self.orbit_of, self.sizes = reps, seen, sizes
        n = len(reps)
        self.n = n
        self.A_orb = [self.Avec[self.index[rep]] for rep in reps]
        self.w = [sizes[o] * self.A_orb[o] for o in range(n)]
        Q = [[0] * n for _ in range(n)]
        R = [[0] * n for _ in range(n)]
        for i, rep in enumerate(reps):
            for k, r2 in enumerate(self.rows):
                v = self.V(rep, r2)
                Q[i][seen[r2]] += v * self.Avec[k]
                R[seen[r2]][i] += v * self.Avec[self.index[rep]]
        self.Q, self.R = Q, R
        self.inner = (W // 2 - 1, W // 2)
        self.edge = (0, 1)
        self.n_inner = [0] * n
        self.n_edge = [0] * n
        for r in self.rows:
            o = seen[r]
            self.n_inner[o] += int(r[self.inner[0]] == r[self.inner[1]])
            self.n_edge[o] += int(r[0] == r[1])
        self.c_inner = [Fraction(self.n_inner[o], sizes[o]) for o in range(n)]
        self.c_edge = [Fraction(self.n_edge[o], sizes[o]) for o in range(n)]

    def V(self, r, r2) -> int:
        phi = self.phi
        return prod(phi[r[j]][r2[j]] for j in range(self.W))

    def T_row(self, r):
        return [self.V(r, r2) * self.Avec[k] for k, r2 in enumerate(self.rows)]

    # full-state transfer through the tensor structure V = phi (x) ... (x) phi (W factors)
    def kron_apply(self, u):
        W, phi = self.W, self.phi
        n = len(u)
        for j in range(W):
            stride = M ** (W - 1 - j)
            out = [0] * n
            for base in range(0, n, M * stride):
                for t in range(stride):
                    vals = [u[base + b * stride + t] for b in range(M)]
                    for a in range(M):
                        out[base + a * stride + t] = sum(phi[a][b] * vals[b] for b in range(M))
            u = out
        return u

    def T_apply(self, v):
        """(T v)(rho) = sum_rho' V(rho, rho') A(rho') v(rho')."""
        return self.kron_apply([a * x for a, x in zip(self.Avec, v)])

    def T_left(self, a):
        """(a T)(rho') = A(rho') sum_rho a(rho) V(rho, rho') (V symmetric)."""
        return [av * x for av, x in zip(self.Avec, self.kron_apply(a))]

    def pair_indicator(self, pair):
        return [int(r[pair[0]] == r[pair[1]]) for r in self.rows]


def matvec(Mx, v):
    return [sum(a * b for a, b in zip(row, v)) for row in Mx]


def vecmat(v, Mx):
    n = len(Mx)
    return [sum(v[i] * Mx[i][j] for i in range(n)) for j in range(len(Mx[0]))]


# ------------------------------------------------------- modular linear algebra
MERSENNE = (2 ** 61 - 1, 2 ** 89 - 1)


class ModEchelon:
    """Incremental reduced echelon form mod p; add() reports whether the new vector is independent of the earlier ones."""

    def __init__(self, p: int) -> None:
        self.p = p
        self.rows: list = []  # (pivot column, normalized row)

    def add(self, vec) -> bool:
        p = self.p
        v = [x % p for x in vec]
        for c, row in self.rows:
            f = v[c]
            if f:
                v = [(a - f * b) % p for a, b in zip(v, row)]
        piv = next((i for i, x in enumerate(v) if x), None)
        if piv is None:
            return False
        inv = pow(v[piv], p - 2, p)
        v = [(x * inv) % p for x in v]
        new_rows = []
        for c, row in self.rows:
            f = row[piv]
            new_rows.append((c, [(a - f * b) % p for a, b in zip(row, v)] if f else row))
        new_rows.append((piv, v))
        self.rows = new_rows
        return True


def solve_mod(rows_mat, rhs, p):
    """Solve the square system rows_mat c = rhs mod p by Gauss-Jordan; None if singular mod p."""
    d = len(rows_mat)
    aug = [[x % p for x in row] + [r % p] for row, r in zip(rows_mat, rhs)]
    for col in range(d):
        piv = next((i for i in range(col, d) if aug[i][col]), None)
        if piv is None:
            return None
        aug[col], aug[piv] = aug[piv], aug[col]
        inv = pow(aug[col][col], p - 2, p)
        aug[col] = [(x * inv) % p for x in aug[col]]
        for i in range(d):
            if i != col and aug[i][col]:
                f = aug[i][col]
                aug[i] = [(a - f * b) % p for a, b in zip(aug[i], aug[col])]
    return [aug[i][d] for i in range(d)]


def crt_symmetric(residues, moduli):
    x, mod = 0, 1
    for r, m in zip(residues, moduli):
        t = ((r - x) * pow(mod, -1, m)) % m
        x += mod * t
        mod *= m
    if 2 * x > mod:
        x -= mod
    return x


def large_primes(count: int, bits: int = 512):
    out = []
    q = 2 ** bits
    while len(out) < count:
        q = int(sp.nextprime(q))
        out.append(q)
    return out


def krylov_dimension(Q, v0, maxk: int):
    """The least d with Q^d v0 dependent on the earlier powers mod both Mersenne primes; the vectors v_0..v_d."""
    ech = [ModEchelon(p) for p in MERSENNE]
    vecs = [list(v0)]
    for k in range(maxk + 1):
        indep = [e.add(vecs[-1]) for e in ech]
        if not all(indep):
            assert not any(indep), "the two modular ranks disagree"
            return len(vecs) - 1, vecs
        vecs.append(matvec(Q, vecs[-1]))
    raise RuntimeError("no dependency found")


def relative_minimal_polynomial(vecs, d: int, coeff_bound: int):
    """Integer coefficients c_0..c_{d-1} with sum_k c_k v_k + v_d = 0: found by a multi-modular solve on d rows
    independent mod 2^61-1 and then verified exactly on every coordinate (the verification is the certificate)."""
    n = len(vecs[0])
    p = MERSENNE[0]
    ech = ModEchelon(p)
    chosen = []
    for i in range(n):
        if ech.add([vecs[k][i] for k in range(d)]):
            chosen.append(i)
        if len(chosen) == d:
            break
    assert len(chosen) == d
    sub = [[vecs[k][i] for k in range(d)] for i in chosen]
    rhs = [-vecs[d][i] for i in chosen]
    primes = []
    residues = []
    modulus = 1
    for q in large_primes(64):
        sol = solve_mod(sub, rhs, q)
        if sol is None:
            continue
        primes.append(q)
        residues.append(sol)
        modulus *= q
        if modulus > 2 * coeff_bound:
            break
    coeffs = [crt_symmetric([res[k] for res in residues], primes) for k in range(d)]
    verified = all(sum(coeffs[k] * vecs[k][i] for k in range(d)) + vecs[d][i] == 0 for i in range(n))
    return coeffs, verified, len(primes)


# ------------------------------------------------------- the enclosure route (S3)
def ratio_bounds(Q, k: int):
    n = len(Q)
    y = [1] * n
    for _ in range(k):
        y = matvec(Q, y)
    Qy = matvec(Q, y)
    ratios = [Fraction(Qy[o], y[o]) for o in range(n)]
    return min(ratios), max(ratios), y, Qy


def enclosure(S: Strip, k: int = 40) -> dict:
    """S3 executed: the ratio bounds, the trace bound, the residual-gap bound and the 2*eps enclosures of both statistics."""
    n, w, Q = S.n, S.w, S.Q
    lo, hi, y, Qy = ratio_bounds(Q, k)
    ny = sum(w[o] * y[o] * y[o] for o in range(n))
    mu = Fraction(sum(w[o] * y[o] * Qy[o] for o in range(n)), ny)
    res2 = Fraction(sum(w[o] * (Qy[o] - mu * y[o]) ** 2 for o in range(n)), ny)
    trQ2 = sum(Q[o][q] * Q[q][o] for o in range(n) for q in range(n))
    lam2b = sqrt_upper(Fraction(trQ2) - lo * lo)
    delta = mu - lam2b
    r_up = sqrt_upper(res2)
    eps = sqrt_upper(Fraction(2)) * r_up / delta if delta > 0 else None
    s_in = sum(Fraction(w[o] * y[o] * y[o], ny) * S.c_inner[o] for o in range(n))
    s_ed = sum(Fraction(w[o] * y[o] * y[o], ny) * S.c_edge[o] for o in range(n))
    out = {"lo": lo, "hi": hi, "y": y, "Qy": Qy, "mu": mu, "res2": res2, "trQ2": trQ2, "lam2b": lam2b, "delta": delta,
           "r_up": r_up, "eps": eps, "s_inner_y": s_in, "s_edge_y": s_ed, "sin_bound": (r_up / delta if delta > 0 else None)}
    if eps is not None:
        out["inner"] = (s_in - 2 * eps, s_in + 2 * eps)
        out["edge"] = (s_ed - 2 * eps, s_ed + 2 * eps)
    return out


def sector_center_value(S: Strip, n_rows: int, left0=None, right0=None):
    """The center-row pair statistics of the n-row strip in the orbit sector: left = b_L R^c, right = Q^(n-1-c) b_R."""
    c = n_rows // 2
    left = list(S.A_orb) if left0 is None else list(left0)
    for _ in range(c):
        left = vecmat(left, S.R)
    right = [1] * S.n if right0 is None else list(right0)
    for _ in range(n_rows - 1 - c):
        right = matvec(S.Q, right)
    wts = [S.sizes[o] * left[o] * right[o] for o in range(S.n)]
    Z = sum(wts)
    return Fraction(sum(wts[o] * S.c_inner[o] for o in range(S.n)), Z), Fraction(sum(wts[o] * S.c_edge[o] for o in range(S.n)), Z)


def full_center_value(S: Strip, n_rows: int, left0=None, right0=None):
    """The same statistics on the full row-state space through the tensor structure of V (no sector)."""
    c = n_rows // 2
    left = list(S.Avec) if left0 is None else list(left0)
    for _ in range(c):
        left = S.T_left(left)
    right = [1] * len(S.rows) if right0 is None else list(right0)
    for _ in range(n_rows - 1 - c):
        right = S.T_apply(right)
    wts = [a * b for a, b in zip(left, right)]
    Z = sum(wts)
    ind_in, ind_ed = S.pair_indicator(S.inner), S.pair_indicator(S.edge)
    return Fraction(sum(x * i for x, i in zip(wts, ind_in)), Z), Fraction(sum(x * i for x, i in zip(wts, ind_ed)), Z)


def distance_to(x: Fraction, interval) -> Fraction:
    a, b = interval
    return max(a - x, x - b, Fraction(0))


# ------------------------------------------------------- the field route (S4, where d <= 16)
lam, yy = sp.symbols("lam y")


def rat_of(x: Fraction):
    return sp.Rational(x.numerator, x.denominator)


class Field:
    """Q[lam]/(m_1) for a monic integer m_1 = lam^d + sum_k mc[k] lam^k; elements are lists of d Fractions."""

    def __init__(self, mc) -> None:
        self.mc = [Fraction(c) for c in mc]  # mc[0..d-1]; monic
        self.d = len(mc)

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
                for i in range(d):
                    r[k - d + i] -= c * self.mc[i]
        return r[:d]

    def is_zero(self, a) -> bool:
        return all(x == 0 for x in a)

    def to_expr(self, a):
        return sum(rat_of(x) * lam ** i for i, x in enumerate(a)) + sp.Integer(0)


def horner_interval(coeffs, lo: Fraction, hi: Fraction):
    """Rigorous rational bounds of sum c_k t^k over t in [lo, hi] with 0 < lo (monotone powers)."""
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


def poly_eval(coeffs, t: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in reversed(coeffs):
        acc = acc * t + c
    return acc


def bisect_simple_root(coeffs, lo: Fraction, hi: Fraction, steps: int):
    flo = poly_eval(coeffs, lo)
    fhi = poly_eval(coeffs, hi)
    assert flo != 0 and fhi != 0 and (flo > 0) != (fhi > 0)
    for _ in range(steps):
        mid = (lo + hi) / 2
        fm = poly_eval(coeffs, mid)
        if fm == 0:
            return mid, mid
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return lo, hi


def interpolate(points):
    """Exact Lagrange interpolation: the coefficient list (low to high) of the polynomial through the points."""
    n = len(points)
    coeffs = [Fraction(0)] * n
    for i, (xi, yi) in enumerate(points):
        basis = [Fraction(1)]
        denom = Fraction(1)
        for j, (xj, _) in enumerate(points):
            if j == i:
                continue
            basis = [Fraction(0)] + basis
            for k in range(len(basis) - 1):
                basis[k] -= xj * basis[k + 1]
            denom *= xi - xj
        for k in range(len(basis)):
            coeffs[k] += yi * basis[k] / denom
    return coeffs


def identify(S: Strip, mc, vecs, E: dict, cap_sec: int = 60) -> dict:
    """x = p(Q) 1 with p = m_1/(lam - lam_1) by Horner in Q[lam]/(m_1); Q x = lam_1 x on every orbit; s = N/D; the
    minimal polynomial of each statistic as the irreducible factor of Res_lam(m_1, y D - N) with one root in the enclosure."""
    F = Field(mc)
    d = F.d
    n = S.n
    t = F.el([0, 1])
    p = [None] * d
    p[d - 1] = F.el([1])
    for k in range(d - 1, 0, -1):
        p[k - 1] = F.add(F.el([mc[k]]), F.mul(t, p[k]))
    x = [F.el([0]) for _ in range(n)]
    for k in range(d):
        for o in range(n):
            x[o] = F.add(x[o], F.scal(Fraction(vecs[k][o]), p[k]))
    if mut("field_vector_not_eigen"):
        x[1] = F.add(x[1], F.el([1]))
    qx = [F.el([0]) for _ in range(n)]
    for k in range(d):
        for o in range(n):
            qx[o] = F.add(qx[o], F.scal(Fraction(vecs[k + 1][o]), p[k]))
    eigen_ok = all(F.is_zero(F.sub(qx[o], F.mul(t, x[o]))) for o in range(n))
    lo, hi = E["lo"], E["hi"]
    signs = [horner_interval(x[o], lo, hi) for o in range(n)]
    one_signed = all(a > 0 for a, b in signs) or all(b < 0 for a, b in signs)
    D = F.el([0])
    N_in = F.el([0])
    N_ed = F.el([0])
    for o in range(n):
        sq = F.scal(Fraction(S.w[o]), F.mul(x[o], x[o]))
        D = F.add(D, sq)
        N_in = F.add(N_in, F.scal(S.c_inner[o], sq))
        N_ed = F.add(N_ed, F.scal(S.c_edge[o], sq))
    out = {"eigen_ok": eigen_ok, "one_signed": one_signed, "d": d}
    m1_poly = sp.Poly(lam ** d + sum(sp.Integer(c) * lam ** k for k, c in enumerate(mc)), lam, domain="ZZ")
    t_start = time.monotonic_ns()
    for name, N in (("inner", N_in), ("edge", N_ed)):
        den = 1
        for c in N + D:
            den = den * c.denominator // sp.igcd(den, c.denominator)
        Ni = [int(c * den) for c in N]
        Di = [int(c * den) for c in D]
        Npoly = sp.Poly(sum(sp.Integer(c) * lam ** k for k, c in enumerate(Ni)) + sp.Integer(0), lam, domain="ZZ")
        Dpoly = sp.Poly(sum(sp.Integer(c) * lam ** k for k, c in enumerate(Di)) + sp.Integer(0), lam, domain="ZZ")
        pts = []
        for j in range(d + 1):
            g = Dpoly * sp.Integer(j) - Npoly
            r = sp.resultant(m1_poly, g, lam) if g.degree() >= 0 else (sp.Integer(0) if False else sp.Integer(0))
            pts.append((Fraction(j), Fraction(int(r))))
        rc = interpolate(pts)
        res_poly = sp.Poly(sum(rat_of(c) * yy ** k for k, c in enumerate(rc)) + sp.Integer(0), yy, domain="QQ")
        factors = [sp.Poly(f, yy, domain="QQ") for f, _m in sp.factor_list(res_poly.as_expr())[1]]
        glo, ghi = E[name]
        if mut("resultant_factor_wrong"):
            glo, ghi = glo + Fraction(1, 10 ** 3), ghi + Fraction(1, 10 ** 3)
        counts = [P_.count_roots(rat_of(glo), rat_of(ghi)) for P_ in factors]
        hits = [P_ for P_, c in zip(factors, counts) if c >= 1]
        out[name] = {
            "res_degree": res_poly.degree(),
            "factor_degrees": [P_.degree() for P_ in factors],
            "identified": len(hits) == 1 and sum(counts) == 1,
            "minpoly": hits[0] if len(hits) == 1 else None,
            "N": Ni,
            "D": Di,
        }
        elapsed = (time.monotonic_ns() - t_start) // 10 ** 9
        out[name]["elapsed_s"] = elapsed
        if elapsed > cap_sec:
            out[name]["identified"] = False
            out[name]["skipped"] = True
    # the block-02 route as a cross-check: the interval image of N/D on a refined isolating interval meets the enclosure
    images = {}
    lo_r, hi_r = bisect_simple_root([Fraction(c) for c in mc] + [Fraction(1)], lo, hi, 700)
    for name, N in (("inner", N_in), ("edge", N_ed)):
        nlo, nhi = horner_interval(N, lo_r, hi_r)
        dlo, dhi = horner_interval(D, lo_r, hi_r)
        if dlo > 0 and nlo > 0:
            images[name] = (nlo / dhi, nhi / dlo)
        else:
            images[name] = None
    out["images"] = images
    return out


# ==================================================================== family A
def family_a(checks: Checks, note_text: str, axiom_text: str, parent_text: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3, "the three declared audit inputs exist (this note, the axiom memo, block 02's note)")
    flat_ax = normalize_text(axiom_text)
    checks.check("A2", all(nd in flat_ax for nd in AXIOM_NEEDLES), "the six axiom sentences used are present verbatim in the axiom memo")
    flat_parent = normalize_text(parent_text)
    checks.check("A3", PARENT_CLAIM_ID in flat_parent and PARENT_FRAGMENT in flat_parent and "deep-row" in PARENT_FRAGMENT, "block 02's claim id and its deep-row-law fragment are present in block 02's note")
    flat_note = normalize_text(note_text)
    checks.check("A4", CLAIM_ID in flat_note and Path(__file__).name in flat_note, "this note carries its claim id and names this runner")
    checks.check("A5", not any("TWO_SITE_BLOCK" in p or "MONOTONE_ORDER" in p or "UNIQUENESS_REGION" in p for p in AUDIT_INPUT_PATHS), "blocks 03-05 are not inputs (the premises are blocks 01-02's only)")


# ==================================================================== family B
def family_b(checks: Checks, strips: dict) -> None:
    counts = {W: strips[(W, TRIPLES[0])].n for W in (2, 3, 4, 5)}
    same = all(strips[(W, TRIPLES[0])].n == strips[(W, TRIPLES[1])].n for W in (2, 3, 4, 5))
    if mut("orbit_count_wrong"):
        counts[5] += 1
    checks.check("B1", counts == {2: 3, 3: 8, 4: 38, 5: 178} and same, f"row orbits under G (order 48): {counts[2]}, {counts[3]}, {counts[4]}, {counts[5]} at widths 2, 3, 4, 5, the same at both triples")
    comm = True
    for tr in TRIPLES:
        S = strips[(4, tr)]
        T = [S.T_row(r) for r in S.rows]
        if mut("commutation_broken"):
            T[0][1] += 1
        maps = [[S.index[act(e, r)] for r in S.rows] for e in GROUP]
        for o, rep in enumerate(S.reps):
            i = S.index[rep]
            for mp in maps:
                gi = mp[i]
                if any(T[gi][mp[j]] != T[i][j] for j in range(len(S.rows))):
                    comm = False
        S5 = strips[(5, tr)]
        for rep in S5.reps[:2]:
            base = S5.T_row(rep)
            for e in GROUP:
                img = S5.T_row(act(e, rep))
                if any(img[S5.index[act(e, r2)]] != base[k] for k, r2 in enumerate(S5.rows)):
                    comm = False
    checks.check("B2", comm, "T(g rho, g rho') = T(rho, rho') for all 48 maps: every orbit representative against all 1296 rows at width 4; two representatives against all 7776 rows at width 5; both triples")
    rid = True
    for W in (4, 5):
        for tr in TRIPLES:
            S = strips[(W, tr)]
            n = S.n
            if not all(S.R[o][q] * S.sizes[q] == S.sizes[o] * S.Q[o][q] for o in range(n) for q in range(n)):
                rid = False
            # representative independence of Q: rebuild each row of Q from a second representative (the orbit's last state)
            last = {}
            for r in S.rows:
                last[S.orbit_of[r]] = r
            for o in range(n):
                row = [0] * n
                for k, r2 in enumerate(S.rows):
                    row[S.orbit_of[r2]] += S.V(last[o], r2) * S.Avec[k]
                if mut("quotient_row_identity_broken") and o == 0:
                    row[0] += 1
                if row != S.Q[o]:
                    rid = False
            if sum(S.sizes) != M ** W or sum(S.n_edge) != M ** (W - 1) or sum(S.n_inner) != M ** (W - 1):
                rid = False
    checks.check("B3", rid, "Q is representative-independent (rebuilt from a second representative of every orbit), R_OO' |O'| = |O| Q_OO' on every pair, orbit sizes sum to 6^W, parallel counts to 6^(W-1); widths 4, 5, both triples")
    sec_ok = True
    kron_ok = True
    for tr in TRIPLES:
        S4 = strips[(4, tr)]
        T = [S4.T_row(r) for r in S4.rows]
        for v in ([1] * len(S4.rows), S4.Avec, [prod(S4.phi[r[j]][E_Y] for j in range(4)) for r in S4.rows]):
            if matvec(T, v) != S4.T_apply(v) or vecmat(v, T) != S4.T_left(v):
                kron_ok = False
        for n_rows in (3, 5, 7):
            si, se = sector_center_value(S4, n_rows)
            fi, fe = full_center_value(S4, n_rows)
            if mut("sector_full_mismatch") and n_rows == 5:
                fi += Fraction(1, 10 ** 9)
            if si != fi or se != fe:
                sec_ok = False
        S5 = strips[(5, tr)]
        for n_rows in (3, 5):
            si, se = sector_center_value(S5, n_rows)
            fi, fe = full_center_value(S5, n_rows)
            if si != fi or se != fe:
                sec_ok = False
    checks.check("B4", kron_ok, "the tensor-structured full-state transfer equals the explicit T on three vectors (left and right actions), width 4, both triples")
    checks.check("B5", sec_ok, "the sector's finite-n center-row statistics equal the full-state ones: width 4 at n = 3, 5, 7 and width 5 at n = 3, 5; edge and innermost pairs; both triples (20 exact equalities)")


# ================================================== the contract's literals (integers at a stated scale; no floats)
CASES = ((4, (3, 1, 2)), (4, (5, 2, 4)), (5, (3, 1, 2)), (5, (5, 2, 4)))
LAM_LIT = {  # floor(lo * 10^18), ceil(hi * 10^18)
    (4, (3, 1, 2)): (167095549094439124072551, 167095549094439124072552),
    (4, (5, 2, 4)): (15805546058271708040967862, 15805546058271708040967863),
    (5, (3, 1, 2)): (4020095963367139908549070, 4020095963367139908549071),
    (5, (5, 2, 4)): (1394779038040295659739675096, 1394779038040295659739675097),
}
S_LIT = {  # (edge, inner): floor(lower * 10^22), ceil(upper * 10^22)
    (4, (3, 1, 2)): ((2561162479042062541091, 2561162479042062541092), (2562841851395883553318, 2562841851395883553319)),
    (4, (5, 2, 4)): ((2199158620242067557423, 2199158620242067557424), (2199567765176185248607, 2199567765176185248608)),
    (5, (3, 1, 2)): ((2561164296010283514028, 2561164296010283514029), (2562896288160817584176, 2562896288160817584177)),
    (5, (5, 2, 4)): ((2199158748550207694373, 2199158748550207694374), (2199574883712355711334, 2199574883712355711335)),
}
TRQ2_LIT = {(4, (3, 1, 2)): 28006524928, (4, (5, 2, 4)): 250087391159985, (5, (3, 1, 2)): 16238809878528, (5, (5, 2, 4)): 1948759036672266913}
RATIO_LIT = {(4, (3, 1, 2)): 5538, (4, (5, 2, 4)): 3301, (5, (3, 1, 2)): 6932, (5, (5, 2, 4)): 4150}  # ceil(lam2b/lo * 10^5)
KRYLOV_LIT = {(4, (3, 1, 2)): 8, (4, (5, 2, 4)): 30, (5, (3, 1, 2)): 16, (5, (5, 2, 4)): 111}
CHARPOLY_DEGREES_LIT = {(3, 1, 2): [1, 1, 2, 8], (5, 2, 4): [1, 1, 1, 5, 30]}
SEP_LIT = {  # floor((s - f) * 10^8) for (edge, inner)
    (4, (3, 1, 2)): (611624, 628418), (4, (5, 2, 4)): (252455, 256547), (5, (3, 1, 2)): (611642, 628962), (5, (5, 2, 4)): (252457, 256618),
}
B02_LIT = {  # block 02's F4 enclosures: floor(lower * 10^k), ceil(upper * 10^k), k
    (3, (3, 1, 2)): (2561109872857786908612, 2561109872857786908613, 22),
    (3, (5, 2, 4)): (2199151616870197815075, 2199151616870197815076, 22),
    (2, (3, 1, 2)): (255943088901618766, 255943088901618767, 18),
    (2, (5, 2, 4)): (219874176124090031, 219874176124090032, 18),
}


# ==================================================================== family C
def family_c(checks: Checks, strips: dict, enc: dict, report: dict) -> None:
    sa = True
    for W, tr in CASES:
        S = strips[(W, tr)]
        Q = [row[:] for row in S.Q]
        if mut("self_adjointness_broken") and W == 4:
            Q[0][1] += 1
        if not all(S.w[o] * Q[o][q] == S.w[q] * Q[q][o] for o in range(S.n) for q in range(S.n)):
            sa = False
    checks.check("C1", sa, "w_O Q_OO' = w_O' Q_O'O on every pair of orbits (38^2 and 178^2), both triples: Q is self-adjoint for the weights w = |O| A")
    checks.check("C2", all(enc[c]["trQ2"] == TRQ2_LIT[c] for c in CASES), "tr(Q^2) = 28006524928, 250087391159985, 16238809878528, 1948759036672266913")
    cw = True
    for c in CASES:
        E = enc[c]
        lo, hi, mu = E["lo"], E["hi"], E["mu"]
        if mut("cw_interval_forged"):
            lo, hi = hi + 1, hi + 2
        if not (lo > 0 and lo <= mu <= hi and floor_scaled(lo, 18) == LAM_LIT[c][0] and ceil_scaled(hi, 18) == LAM_LIT[c][1]):
            cw = False
    checks.check("C3", cw, "the two-sided ratio bounds after 40 powers: 0 < lo <= mu <= hi, and the 18-digit outward labels of lambda_1 are the contract's at all four cases")
    kr = True
    for c in CASES:
        W, tr = c
        S = strips[c]
        d, vecs = krylov_dimension(S.Q, [1] * S.n, S.n + 1)
        bound = (1 + ceil_scaled(enc[c]["hi"], 0)) ** d
        mc, verified, nprimes = relative_minimal_polynomial(vecs, d, bound)
        if mut("dependency_not_verified"):
            mc2 = mc[:]
            mc2[0] += 1
            verified = all(sum(mc2[k] * vecs[k][i] for k in range(d)) + vecs[d][i] == 0 for i in range(S.n))
        d_rep = d + 1 if mut("krylov_dimension_off") else d
        report[("krylov", c)] = {"d": d, "mc": mc, "vecs": vecs, "verified": verified, "primes": nprimes, "digits": max(len(str(abs(x))) for x in mc)}
        if d_rep != KRYLOV_LIT[c] or not verified:
            kr = False
    checks.check("C4", kr, "the Krylov dimension of Q on 1 is 8, 30, 16, 111 (independence mod 2^61-1 and 2^89-1; the integer dependency m_1(Q) 1 = 0 verified exactly on every orbit at all four cases)")
    cp_ok = True
    for tr in TRIPLES:
        S = strips[(4, tr)]
        cp = sp.Poly(sp.Matrix(S.Q).charpoly(lam).as_expr(), lam, domain="QQ")
        factors = [sp.Poly(f, lam, domain="QQ") for f, _m in sp.factor_list(cp.as_expr())[1]]
        degs = sorted(P_.degree() for P_ in factors)
        K = report[("krylov", (4, tr))]
        m1 = sp.Poly(lam ** K["d"] + sum(sp.Integer(x) * lam ** k for k, x in enumerate(K["mc"])), lam, domain="QQ")
        if mut("charpoly_factor_mismatch"):
            m1 = m1 + sp.Poly(lam ** (K["d"] - 1), lam, domain="QQ")
        if degs != sorted(CHARPOLY_DEGREES_LIT[tr]) or not any(P_ == m1 for P_ in factors):
            cp_ok = False
    checks.check("C5", cp_ok, "width 4: the characteristic polynomial of Q factors with degrees [1, 1, 2, 8] and [1, 1, 1, 5, 30], and the relative minimal polynomial m_1 is its factor of degree d")
    irr = True
    for c in CASES:
        K = report[("krylov", c)]
        if K["d"] > 30:
            K["irreducible"] = None
            continue
        m1 = sp.Poly(lam ** K["d"] + sum(sp.Integer(x) * lam ** k for k, x in enumerate(K["mc"])), lam, domain="QQ")
        K["m1"] = m1
        fl = sp.factor_list(m1.as_expr())[1]
        K["irreducible"] = len(fl) == 1 and sp.Poly(fl[0][0], lam).degree() == K["d"]
        if not K["irreducible"]:
            irr = False
    checks.check("C6", irr and report[("krylov", (5, (5, 2, 4)))]["irreducible"] is None, "m_1 is irreducible over Q at d = 8, 30, 16 (executed); at d = 111 factorization is not attempted and nothing is claimed")
    roots_ok = True
    for c in CASES:
        K = report[("krylov", c)]
        if K["d"] > 30:
            continue
        lo, hi = enc[c]["lo"], enc[c]["hi"]
        if mut("largest_root_outside_interval"):
            lo, hi = hi + 1, hi + 2
        inside = K["m1"].count_roots(rat_of(lo), rat_of(hi))
        above = K["m1"].count_roots(rat_of(hi), None)
        K["root_counts"] = (inside, above)
        if inside != 1 or above != 0:
            roots_ok = False
    checks.check("C7", roots_ok, "at d = 8, 30, 16 exactly one real root of m_1 lies in [lo, hi] and none lies above hi (Sturm counts): the largest root is the Perron root")


# ==================================================================== family D
def family_d(checks: Checks, strips: dict, enc: dict, report: dict, exact: bool) -> None:
    side = True
    for c in CASES:
        E = enc[c]
        S = strips[c]
        lam2b = E["lam2b"] / (2 if mut("trace_bound_forged") else 1)
        delta = E["mu"] if mut("residual_gap_ignored") else E["delta"]
        y, Qy, mu = E["y"], E["Qy"], E["mu"]
        ny = sum(S.w[o] * y[o] * y[o] for o in range(S.n))
        res2_re = Fraction(sum(S.w[o] * (Qy[o] - mu * y[o]) ** 2 for o in range(S.n)), ny)
        res2 = Fraction(0) if mut("residual_forged") else E["res2"]
        conds = (delta > 0, E["lo"] > lam2b, lam2b * lam2b >= Fraction(E["trQ2"]) - E["lo"] ** 2, E["r_up"] ** 2 >= E["res2"],
                 sqrt_upper(Fraction(2)) ** 2 >= 2, delta == mu - lam2b, res2 == res2_re, all(v > 0 for v in y))
        if not all(conds):
            side = False
        if exact:
            say(f"exact W={c[0]} {c[1]}: lambda_1 in [{E['lo']}, {E['hi']}]; mu = {E['mu']}; r^2 = {E['res2']}; lambda_2 bound = {E['lam2b']}; eps = {E['eps']}")
    checks.check("D1", side, "side conditions at all four cases: y > 0, delta = mu - lambda_2bound > 0, lo > lambda_2bound, the square-root bounds are upper bounds, the residual is the recomputed one")
    lit = True
    for c in CASES:
        E = enc[c]
        for name, idx in (("edge", 0), ("inner", 1)):
            a, b = E[name]
            if not (b - a < Fraction(1, 10 ** 50) and floor_scaled(a, 22) == S_LIT[c][idx][0] and ceil_scaled(b, 22) == S_LIT[c][idx][1]):
                lit = False
            if exact:
                say(f"exact W={c[0]} {c[1]}: s_{name} in [{a}, {b}]")
    checks.check("D2", lit, "every enclosure [s(y) - 2 eps, s(y) + 2 eps] has width below 10^-50 and its 22-digit outward labels are the contract's (four cases, both pairs)")
    excl = True
    for c in CASES:
        f = formation_value(c[1])
        for name in ("edge", "inner"):
            a, b = enc[c][name]
            if mut("s_enclosure_contains_formation_value"):
                a, b = a - Fraction(1, 10), b + Fraction(1, 10)
            if a <= f <= b:
                excl = False
    checks.check("D3", excl, "no enclosure contains the formation value f = 1/4 or 5/23 (eight enclosures)")
    seq_ok = True
    for c in CASES:
        S = strips[c]
        vals = [(n_, *sector_center_value(S, n_)) for n_ in (3, 5, 9, 17, 33, 65)]
        if mut("finite_n_sequence_shuffled"):
            vals[0], vals[-1] = (vals[0][0], vals[-1][1], vals[-1][2]), (vals[-1][0], vals[0][1], vals[0][2])
        report[("finite_n", c)] = vals
        for idx, name in ((1, "inner"), (2, "edge")):
            dist = [distance_to(v[idx], enc[c][name]) for v in vals]
            if not all(dist[i + 1] < dist[i] for i in range(len(dist) - 1)):
                seq_ok = False
        if exact:
            say(f"exact W={c[0]} {c[1]}: finite n (n, s_inner, s_edge): {[(n_, str(a), str(b)) for n_, a, b in vals]}")
    checks.check("D4", seq_ok, "the sector's center-row statistics at n = 3, 5, 9, 17, 33, 65 have strictly decreasing distances to the enclosure, both pairs, all four cases")
    bnd = True
    for c in CASES:
        S = strips[c]
        h = [prod(S.phi[r[j]][E_Y] for j in range(S.W)) for r in S.rows]
        fi, fe = full_center_value(S, 33, left0=[a * x for a, x in zip(S.Avec, h)], right0=h)
        hbar = [Fraction(sum(h[S.index[r]] for r in S.rows if S.orbit_of[r] == o), S.sizes[o]) for o in range(S.n)]
        si, se = sector_center_value(S, 33, left0=[S.A_orb[o] * hbar[o] for o in range(S.n)], right0=hbar)
        if mut("boundary_dependence_forged"):
            fi += Fraction(1, 100)
        dists = [distance_to(fi, enc[c]["inner"]), distance_to(fe, enc[c]["edge"]), distance_to(si, enc[c]["inner"]), distance_to(se, enc[c]["edge"])]
        report[("boundary", c)] = (fi, fe, si, se, dists)
        if not all(x < Fraction(1, 10 ** 6) for x in dists):
            bnd = False
    checks.check("D5", bnd, "boundary independence at n = 33: P(e_y) records on every site of both end rows (full state through the tensor structure) and the orbit-averaged record in the sector; all within 10^-6 of the enclosures")
    b02 = True
    for (W, tr), (la, lb, k) in B02_LIT.items():
        E = enc[(W, tr)]
        a, b = E["edge"]
        if mut("w2_w3_literals_off"):
            la += 1
        if not (floor_scaled(a, k) == la and ceil_scaled(b, k) == lb and not (a <= formation_value(tr) <= b) and E["inner"] == E["edge"]):
            b02 = False
    checks.check("D6", b02, "widths 2 and 3 by the same route: the enclosures carry block 02's F4 digits (18 and 22 digits) and exclude f; the innermost pair is the edge pair there")
    ident = True
    for c in CASES:
        K = report[("krylov", c)]
        if K["d"] > 16:
            continue
        I = identify(strips[c], K["mc"], K["vecs"], enc[c])
        report[("identify", c)] = I
        for name in ("inner", "edge"):
            img = I["images"][name]
            meets = img is not None and not (img[1] < enc[c][name][0] or img[0] > enc[c][name][1])
            if not (I[name]["identified"] and meets):
                ident = False
        if not (I["eigen_ok"] and I["one_signed"]):
            ident = False
        if exact:
            for name in ("inner", "edge"):
                say(f"exact W={c[0]} {c[1]}: minimal polynomial of s_{name} (degree {I[name]['minpoly'].degree() if I[name]['minpoly'] is not None else None}) = {I[name]['minpoly'].as_expr() if I[name]['minpoly'] is not None else None}")
                say(f"exact W={c[0]} {c[1]}: N_{name} = {I[name]['N']}; D = {I[name]['D']}; image of N/D on the refined interval = {I['images'][name]}")
    checks.check("D7", ident, "where d <= 16: x = p(Q) 1 satisfies Q x = lambda_1 x in Q[lam]/(m_1) on every orbit and is one-signed; the resultant's irreducible factor with exactly one root in the enclosure identifies s_inner and s_edge; the field image meets the enclosure")


# ==================================================================== family E
def family_e(checks: Checks, enc: dict, report: dict) -> None:
    sep = True
    rows_out = []
    for W in (2, 3, 4, 5):
        for tr in TRIPLES:
            E = enc[(W, tr)]
            f = formation_value(tr)
            d_ed = (f - E["edge"][1]) if mut("separation_sign_flipped") else (E["edge"][0] - f)
            d_in = (f - E["inner"][1]) if mut("separation_sign_flipped") else (E["inner"][0] - f)
            if not (d_ed > Fraction(1, 10 ** 3) and d_in > Fraction(1, 10 ** 3)):
                sep = False
            if (W, tr) in SEP_LIT and (floor_scaled(d_ed, 8), floor_scaled(d_in, 8)) != SEP_LIT[(W, tr)]:
                sep = False
            rows_out.append(f"W={W} {tr}: s_edge {dec(E['edge'][0], 12)}.. s_inner {dec(E['inner'][0], 12)}.. s_edge-f {dec(d_ed, 8)}.. s_inner-f {dec(d_in, 8)}..")
    for line in rows_out:
        say(line)
    checks.check("E1", sep, "s - f > 10^-3 at every executed width 2, 3, 4, 5, both pairs, both triples; the 8-digit labels of s - f at widths 4, 5 are the contract's")
    order = True
    for c in CASES:
        E = enc[c]
        gap = (E["edge"][0] - E["inner"][1]) if mut("inner_edge_order_flipped") else (E["inner"][0] - E["edge"][1])
        report[("inner_minus_edge", c)] = gap
        if not gap > 0:
            order = False
    checks.check("E2", order, "s_inner > s_edge strictly at widths 4 and 5, both triples (lower endpoint of s_inner above the upper endpoint of s_edge)")
    e4, e5 = enc[(4, (3, 1, 2))], enc[(5, (3, 1, 2))]
    din = (e5["inner"][0] - e4["inner"][1], e5["inner"][1] - e4["inner"][0])
    ded = (e5["edge"][0] - e4["edge"][1], e5["edge"][1] - e4["edge"][0])
    report["w45_diff"] = (din, ded)
    diff_ok = floor_scaled(din[0], 10) == 54437 and ceil_scaled(din[1], 10) == 54438 and floor_scaled(ded[0], 11) == 18170 and ceil_scaled(ded[1], 11) == 18171
    checks.check("E3", diff_ok, f"the width-4 and width-5 values differ at (3,1,2) by s_inner: [{dec(din[0], 10)}, {dec(din[1], 10, up=True)}] and s_edge: [{dec(ded[0], 11)}, {dec(ded[1], 11, up=True)}] (outward labels; two data points, no statement about other widths)")
    rb = True
    for c in CASES:
        E = enc[c]
        ratio = E["lam2b"] / E["lo"] / (2 if mut("ratio_bound_too_small") else 1)
        report[("ratio", c)] = ratio
        if ceil_scaled(ratio, 5) != RATIO_LIT[c]:
            rb = False
    checks.check("E4", rb, "lambda_2bound/lo <= 0.05538, 0.03301, 0.06932, 0.04150 (rounded up from the exact rationals; a bound on the executed ratio, not the true lambda_2/lambda_1)")


# ==================================================================== family F
FENCES = (
    "This note encloses the static strip's deep-row pair statistics exactly at widths four and five and compares them with the formation value; it states nothing about the plane's static law beyond these widths, and no monotonicity in the width is claimed.",
    "No order is selected as physical; no plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "The transfer-matrix and Perron–Frobenius machinery is cited from block 02, and the Collatz–Wielandt, trace, Davis–Kahan and Krylov steps are proved here at the scope used; the spectral theorem for self-adjoint operators is cited scaffolding; no value, constant or theorem is imported as authority.",
)
FORBIDDEN = (
    "the plane's static law is", "toward the plane", "approaches", "converges", "convergence", "the plane's value",
    "in the limit", "extrapolate", "the trend", "trending", "increasing in W", "the deep-strip value",
    "consistent with the plane", "unique on the lattice", "washes out", "certif", "phase transition",
    "several static laws", "the physical order", "irreducible at d = 111", "irreducible at degree 111",
)
CLAIM_INJECTIONS = {
    "claim_plane_limit": "In the limit of large width the static law of the plane is reached.",
    "claim_monotone_in_W": "The statistic is increasing in W.",
    "claim_washes_out": "The separation washes out at large width.",
}
CLASSICAL_NAMES = ("Perron–Frobenius", "Perron-Frobenius", "Collatz–Wielandt", "Collatz-Wielandt", "Davis–Kahan", "Davis-Kahan")
ALLOWED_NAME_SECTIONS = ("Prior art", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Falsifiers", "By the Davis–Kahan theorem the bound follows.\n\n## Falsifiers", 1)
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase (hits: {hits})")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    nsimp = "nsimp" + "lify("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or nsimp in ln or "numpy" in ln]
    checks.check("F3", not bad and len(scan) > 600, f"runner source: no floating-point literal, conversion, evaluation call or numpy ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.splitlines()[0].strip()
        body = sec
        if title.startswith("Boundaries"):
            body = body.replace(FENCES[2], "")
        if any(nm in body for nm in CLASSICAL_NAMES) and not any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            offenders.append(title[:30])
    checks.check("F4", not offenders and any(nm in text for nm in CLASSICAL_NAMES), f"the classical names appear only in the Prior art and Imports sections (and the verbatim fence); theorem sections use the object names (offenders: {offenders})")
    decimals = set()
    for ln in OUT_LINES:
        for m_ in re.finditer(r"\d+\.\d+", ln):
            decimals.add(m_.group(0))
    stray = sorted(x for x in decimals if x not in DEC_LABELS)
    checks.check("F5", not stray and len(decimals) > 20, f"every decimal label in this stdout was produced by the integer-arithmetic dec() ({len(decimals)} labels; stray: {stray[:3]})")


# ==================================================================== family G
N5_LINES = (
    "per_element: executed — every row state of the width-2, 3, 4 and 5 strips enters the orbit reduction, the quotients and the full-state transfer checks, both triples, exact",
    "per_site: executed — the edge pair (0, 1) and the innermost pair of every row; the end-row records on every site of both end rows in the boundary check",
    "per_mode: executed — the Perron root by the two-sided ratio bounds, every other eigenvalue by the trace bound, the Perron vector by the residual-gap bound, the Krylov degree by modular ranks and an exact dependency; the minimal polynomials where the degree allows",
    "per_block: executed — the finite-n center rows for n = 3 to 65 in the sector and n = 3 to 7 (width 4) and 3 to 5 (width 5) on the full state; the characteristic polynomial at width 4",
    "lattice_wide: checked and not executed — strips of widths 2 to 5 only; the plane and wider strips are named, not computed, and no monotonicity in the width is stated",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        say(line)
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
    say("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        say(f"  {p}")
    say(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    say("scope: the six-projector menu, the product rule at two exact triples; the static strips of widths 4 and 5 (widths 2, 3 as controls); exact arithmetic; no plane, no wider strip, no monotonicity in the width, no order selected")
    say(f"mutation: {ACTIVE_MUTATION or 'none'}")
    t0 = time.monotonic_ns()
    strips = {(W, tr): Strip(W, tr) for W in (2, 3, 4, 5) for tr in TRIPLES}
    enc = {key: enclosure(S, 40) for key, S in strips.items()}
    report: dict = {}
    family_a(checks, note_text, axiom_text, parent_text)
    family_b(checks, strips)
    family_c(checks, strips, enc, report)
    family_d(checks, strips, enc, report, exact)
    family_e(checks, enc, report)
    if exact:
        for c in CASES:
            K = report[("krylov", c)]
            say(f"exact W={c[0]} {c[1]}: m_1 of degree {K['d']} (coefficients low to high, monic): {K['mc']}")
    family_f(checks, note_text)
    family_g(checks)
    say(f"elapsed_s: {(time.monotonic_ns() - t0) // 10 ** 9}")
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        say(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        say(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
