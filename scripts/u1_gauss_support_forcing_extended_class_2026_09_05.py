#!/usr/bin/env python3
"""The two Gauss rows as support forcing on the extended four-role payload class: exact adjudication.

Object: the supplied period-two role compilation of the cubic gauge complex onto physical Z^3
sites (parity roles; oriented d0, C, d2; sector zero, rebuilt here from the parity rule alone),
carrying one real component at every vertex-, edge-, face- and cube-role site (phi, E, B, psi).
The two Gauss rows d0^T E = rho_V and d2 B = rho_C are read as SUPPLIED constraint content whose
shape is Admissibility's support clause: an admissible set that the law's flow must leave
invariant.  The compilation and the rows are named supplies. The canonical block02 note is
a bounded proof dependency for the improved-curl/damped witnesses, not a runtime import.

What this runner establishes, exactly (integers, Fractions and sympy symbols; no float is
evidence):

* the compilation facts used: censuses, the odd-distance parity of every opposite-role coupling,
  the chain identities C d0 = 0 and d2 C = 0, every incidence entry at physical distance one, the
  covariance of d0, C, d2 under all 24 proper rotations about a vertex and all even translations in
  the oriented four-role law, the connectedness lever (ker d0^T d0 and ker d2 d2^T are exactly the
  constants on sides 4 and 6; the image of d0^T is exactly the zero-sum vertex vectors), and the
  odd-shift self-duality (d0, C, d2) -> (-d2^T, C^T, -d0^T) that makes the magnetic argument the
  electric one transported by a lattice translation;
* the exact classification of every translation- and proper-cubic-covariant real linear
  nearest-neighbor generator on the four-role payload in the compilation's sign basis: the
  ten-dimensional span of the four onsite terms and d0, d0^T, C, C^T, d2, d2^T (a 56-pattern
  nullspace under all 24 rotations, side 4);
* the positive-diagonal conservation cut on it (symbolic): the four onsite terms vanish and the
  three coupling ratios are fixed by the weights -- three free speeds;
* the Gauss rates as exact linear functionals of the state, coefficient by coefficient:
  d/dt(d0^T E) = a2 d0^T d0 phi + u_E d0^T E (the B-block d0^T C^T vanishes identically) and
  d/dt(d2 B) = b d2 d2^T psi + u_B d2 B (the E-block d2 C vanishes identically);
* the collapse theorem: the electric surface {d0^T E = rho_V} is invariant under a member iff
  a2 = 0 and u_E rho_V = 0; the magnetic surface iff b = 0 and u_B rho_C = 0; with conservation
  these force a = a2 = 0 and b = b2 = 0, so the invariant conservative members are exactly the
  one-speed edge/face law with the vertex and cube payloads frozen at every state;
* the maximal zero-charge Gauss sector and its branch count for the explicitly
  tested conservative three-speed member a=-2,a2=2,q=1,r=-1,b=-3,b2=3;
  generic non-preserving members need not have both auxiliaries constant;
* the row-specific charged obstruction under CONS, nonzero compatible charge,
  and nonzero longitudinal coupling; without CONS, SF-all only removes outgoing
  auxiliary feedback, not the auxiliary's own rate a rho_V + u_V phi;
* the coin: the exact covariant class on the two-component edge/face payload (dimension 16) and
  its conservative cut (six parameters); the complex law with an onsite phase preserves both
  zero-charge rows, is nearest-neighbor, covariant, conservative and chain-compatible, carries two
  components per site, and is not similar to the specified pair of zero-onsite curl copies (kernel
  dimension 0 against 116); general real mode decompositions remain possible; the all-charge reading of the rows kills only the onsite phases
  and leaves the four-parameter family K (x) C, which mixes the components in the site basis and
  preserves every charged surface;
* hidden time: the complex law's physical pair obeys the closed second-order law
  z1'' = 2 G z1' - (G^2 + theta^2) z1, in which the enlarged payload is the time derivative; at
  the linear level a hidden time payload is an extra coin, and the second-order law has radius two;
* the verbatim presence in the axiom memo of every sentence the note relies on.

Read inventory: the axiom memo is read at runtime. Both canonical notes are
pinned in AUDIT_INPUT_PATHS for present claim scope and the bounded block02 proof
dependency; their text is not executed. Structural arguments require even side
>= 4; side 2 is a degenerate countercontrol. No formal axiom-independence theorem.
"""

from __future__ import annotations

import itertools
import random
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = ("docs/MINIMAL_AXIOMS_2026-06-29.md",
                     "docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md",
                     "docs/U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md")

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> bool:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail != "" else ""
    print(f"  [{tag}] {label}{suffix}")
    return bool(ok)


def section(title: str) -> None:
    print(f"\n{title}\n{'-' * len(title)}")


# ---------------------------------------------------------------------------
# exact linear algebra over Q (own implementation)
# ---------------------------------------------------------------------------


def frac_rows(matrix) -> list[list[Fraction]]:
    out = []
    for row in matrix:
        out.append([v if isinstance(v, Fraction) else Fraction(int(v)) for v in (row.tolist() if hasattr(row, "tolist") else row)])
    return out


def rref_q(matrix):
    """Reduced row echelon form; returns (rows, pivot columns)."""
    rows = frac_rows(matrix)
    if not rows:
        return rows, []
    ncols = len(rows[0])
    pivots: list[int] = []
    rank = 0
    for col in range(ncols):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col] != 0), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = 1 / rows[rank][col]
        rows[rank] = [v * inv for v in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col] != 0:
                factor = rows[r][col]
                rows[r] = [x - factor * y for x, y in zip(rows[r], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break
    return rows, pivots


def rank_q(matrix) -> int:
    return len(rref_q(matrix)[1])


def nullspace_q(matrix) -> list[list[Fraction]]:
    rows, pivots = rref_q(matrix)
    ncols = len(rows[0])
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        vec = [Fraction(0)] * ncols
        vec[f] = Fraction(1)
        for r, p in enumerate(pivots):
            vec[p] = -rows[r][f]
        basis.append(vec)
    return basis


def solve_q(matrix, rhs: list[Fraction]):
    """One exact particular solution of A x = rhs, or None if inconsistent."""
    rows = frac_rows(matrix)
    aug = [row + [b] for row, b in zip(rows, rhs)]
    red, pivots = rref_q(aug)
    ncols = len(rows[0])
    if ncols in pivots:
        return None
    x = [Fraction(0)] * ncols
    for r, p in enumerate(pivots):
        x[p] = red[r][ncols]
    return x


def matvec_q(matrix, vec: list[Fraction]) -> list[Fraction]:
    out = []
    for row in matrix:
        acc = Fraction(0)
        items = row.tolist() if hasattr(row, "tolist") else row
        for coeff, value in zip(items, vec):
            if coeff:
                acc += coeff * value
        out.append(acc)
    return out


def dot_q(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def rational_vector(n: int, rng: random.Random) -> list[Fraction]:
    return [Fraction(rng.randint(-9, 9), rng.randint(1, 5)) for _ in range(n)]


def is_zero(vec) -> bool:
    return all(v == 0 for v in vec)


def frac_matrix_equal(rows, target) -> bool:
    def as_frac(t):
        return t if isinstance(t, Fraction) else Fraction(int(t))
    return all(as_frac(t) == r for row, trow in zip(rows, target) for r, t in zip(row, trow.tolist() if hasattr(trow, "tolist") else trow))


# ---------------------------------------------------------------------------
# the supplied role compilation: parity roles on the even torus (sector 0)
# ---------------------------------------------------------------------------

AXES = (0, 1, 2)
# face normal k and the ordered plane pair (i, j) with e_i x e_j = e_k
CYCLIC = {2: (0, 1), 0: (1, 2), 1: (2, 0)}


class Compilation:
    """Physical torus of even side, roles by coordinate parity (sector 0).

    State order: [phi at vertices] + [E at edges] + [B at faces] + [psi at cubes].
    """

    def __init__(self, side: int) -> None:
        assert isinstance(side, int) and side >= 2 and side % 2 == 0, "positive even side >= 2; structural theorems require >= 4"
        self.side = side
        self.sites = list(itertools.product(range(side), repeat=3))
        self.vertices, self.edges, self.faces, self.cubes = [], [], [], []
        for x in self.sites:
            w = self.weight(x)
            (self.vertices, self.edges, self.faces, self.cubes)[w].append(x)
        self.vidx = {x: i for i, x in enumerate(self.vertices)}
        self.eidx = {x: i for i, x in enumerate(self.edges)}
        self.fidx = {x: i for i, x in enumerate(self.faces)}
        self.cidx = {x: i for i, x in enumerate(self.cubes)}
        self.nv, self.ne, self.nf, self.nc = len(self.vertices), len(self.edges), len(self.faces), len(self.cubes)
        self.offV, self.offE, self.offF, self.offC = 0, self.nv, self.nv + self.ne, self.nv + self.ne + self.nf
        self.n = self.nv + self.ne + self.nf + self.nc
        self.order = self.vertices + self.edges + self.faces + self.cubes
        self.d0 = self._gradient()
        self.curl = self._curl()
        self.d2 = self._divergence()

    # geometry -----------------------------------------------------------
    def shift(self, x, axis: int, step: int):
        y = list(x)
        y[axis] = (y[axis] + step) % self.side
        return tuple(y)

    def translate(self, x, vec):
        return tuple((a + b) % self.side for a, b in zip(x, vec))

    @staticmethod
    def weight(x) -> int:
        return sum(c % 2 for c in x)

    @staticmethod
    def edge_axis(x) -> int:
        return next(i for i in AXES if x[i] % 2 == 1)

    @staticmethod
    def face_normal(x) -> int:
        return next(i for i in AXES if x[i] % 2 == 0)

    def neighbors(self, x):
        return [self.shift(x, i, s) for i in AXES for s in (1, -1)]

    def distance(self, x, y) -> int:
        return sum(min(abs(a - b), self.side - abs(a - b)) for a, b in zip(x, y))

    # incidence (the compilation's oriented conventions) ------------------
    def _gradient(self) -> np.ndarray:
        m = np.zeros((self.ne, self.nv), dtype=np.int64)
        for e, x in enumerate(self.edges):
            i = self.edge_axis(x)
            m[e, self.vidx[self.shift(x, i, 1)]] += 1
            m[e, self.vidx[self.shift(x, i, -1)]] -= 1
        return m

    def face_stencil(self, x):
        k = self.face_normal(x)
        i, j = CYCLIC[k]
        return [
            (self.shift(x, j, -1), 1),   # E_i at x - e_j
            (self.shift(x, j, 1), -1),   # E_i at x + e_j
            (self.shift(x, i, 1), 1),    # E_j at x + e_i
            (self.shift(x, i, -1), -1),  # E_j at x - e_i
        ]

    def _curl(self) -> np.ndarray:
        m = np.zeros((self.nf, self.ne), dtype=np.int64)
        for f, x in enumerate(self.faces):
            for site, sign in self.face_stencil(x):
                m[f, self.eidx[site]] += sign
        return m

    def _divergence(self) -> np.ndarray:
        m = np.zeros((self.nc, self.nf), dtype=np.int64)
        for c, x in enumerate(self.cubes):
            for k in AXES:
                m[c, self.fidx[self.shift(x, k, 1)]] += 1
                m[c, self.fidx[self.shift(x, k, -1)]] -= 1
        return m


# ---------------------------------------------------------------------------
# proper cubic rotations and the oriented four-role transformation law
# ---------------------------------------------------------------------------


def proper_rotations() -> list[np.ndarray]:
    out = []
    for perm in itertools.permutations(AXES):
        for signs in itertools.product((1, -1), repeat=3):
            m = np.zeros((3, 3), dtype=np.int64)
            for col, (row, s) in enumerate(zip(perm, signs)):
                m[row, col] = s
            # exact integer determinant of a signed permutation matrix
            det = 1
            for col in range(3):
                det *= int(m[perm[col], col])
            inversions = sum(1 for a in range(3) for b in range(a + 1, 3) if perm[a] > perm[b])
            det *= -1 if inversions % 2 else 1
            if det == 1:
                out.append(m)
    assert len(out) == 24
    return out


def rotate_site(comp: Compilation, rot: np.ndarray, x, center=(0, 0, 0)):
    rel = np.array(x, dtype=np.int64) - np.array(center, dtype=np.int64)
    y = rot @ rel + np.array(center, dtype=np.int64)
    return tuple(int(v) % comp.side for v in y)


def image_axis_sign(rot: np.ndarray, axis: int) -> tuple[int, int]:
    col = rot[:, axis]
    j = int(np.nonzero(col)[0][0])
    return j, int(col[j])


def field_rotation4(comp: Compilation, rot: np.ndarray) -> np.ndarray:
    """Signed permutation of the four-role state under a proper rotation about the origin (a vertex).

    Oriented law in the compilation's sign basis: phi scalar; E the vector component along the edge
    axis (sign of the transported axis); B the vector component along the face normal (sign of the
    transported normal); psi scalar.
    """
    m = np.zeros((comp.n, comp.n), dtype=np.int64)
    for v, x in enumerate(comp.vertices):
        m[comp.offV + comp.vidx[rotate_site(comp, rot, x)], comp.offV + v] = 1
    for e, x in enumerate(comp.edges):
        _, s = image_axis_sign(rot, comp.edge_axis(x))
        m[comp.offE + comp.eidx[rotate_site(comp, rot, x)], comp.offE + e] = s
    for f, x in enumerate(comp.faces):
        _, s = image_axis_sign(rot, comp.face_normal(x))
        m[comp.offF + comp.fidx[rotate_site(comp, rot, x)], comp.offF + f] = s
    for c, x in enumerate(comp.cubes):
        m[comp.offC + comp.cidx[rotate_site(comp, rot, x)], comp.offC + c] = 1
    return m


def translation4(comp: Compilation, vec) -> np.ndarray:
    """Permutation of the four-role state under an even translation (sector preserved)."""
    assert all(v % 2 == 0 for v in vec)
    m = np.zeros((comp.n, comp.n), dtype=np.int64)
    for v, x in enumerate(comp.vertices):
        m[comp.offV + comp.vidx[comp.translate(x, vec)], comp.offV + v] = 1
    for e, x in enumerate(comp.edges):
        m[comp.offE + comp.eidx[comp.translate(x, vec)], comp.offE + e] = 1
    for f, x in enumerate(comp.faces):
        m[comp.offF + comp.fidx[comp.translate(x, vec)], comp.offF + f] = 1
    for c, x in enumerate(comp.cubes):
        m[comp.offC + comp.cidx[comp.translate(x, vec)], comp.offC + c] = 1
    return m


def block(m: np.ndarray, comp: Compilation, rows: str, cols: str) -> np.ndarray:
    off = {"V": (comp.offV, comp.nv), "E": (comp.offE, comp.ne), "F": (comp.offF, comp.nf), "C": (comp.offC, comp.nc)}
    r0, rn = off[rows]
    c0, cn = off[cols]
    return m[r0:r0 + rn, c0:c0 + cn]


# ---------------------------------------------------------------------------
# generators on the four-role payload
# ---------------------------------------------------------------------------

COEFFS = ("uV", "uE", "uB", "uC", "a", "a2", "q", "r", "b", "b2")


def member(comp: Compilation, **kw) -> list[list[Fraction]]:
    """Exact generator with the ten covariant coefficients.

    d phi/dt = uV phi + a d0^T E
    d E/dt   = a2 d0 phi + uE E + r C^T B
    d B/dt   = q C E + uB B + b d2^T psi
    d psi/dt = b2 d2 B + uC psi
    """
    c = {k: Fraction(0) for k in COEFFS}
    for k, v in kw.items():
        assert k in COEFFS, k
        c[k] = Fraction(v)
    n = comp.n
    g = [[Fraction(0)] * n for _ in range(n)]
    for v in range(comp.nv):
        g[comp.offV + v][comp.offV + v] = c["uV"]
    for e in range(comp.ne):
        g[comp.offE + e][comp.offE + e] = c["uE"]
    for f in range(comp.nf):
        g[comp.offF + f][comp.offF + f] = c["uB"]
    for cc in range(comp.nc):
        g[comp.offC + cc][comp.offC + cc] = c["uC"]
    for e, v in zip(*np.nonzero(comp.d0)):
        val = int(comp.d0[e, v])
        g[comp.offV + v][comp.offE + e] += c["a"] * val
        g[comp.offE + e][comp.offV + v] += c["a2"] * val
    for f, e in zip(*np.nonzero(comp.curl)):
        val = int(comp.curl[f, e])
        g[comp.offF + f][comp.offE + e] += c["q"] * val
        g[comp.offE + e][comp.offF + f] += c["r"] * val
    for cc, f in zip(*np.nonzero(comp.d2)):
        val = int(comp.d2[cc, f])
        g[comp.offC + cc][comp.offF + f] += c["b2"] * val
        g[comp.offF + f][comp.offC + cc] += c["b"] * val
    return g


def int_matrix(g) -> np.ndarray:
    out = np.zeros((len(g), len(g[0])), dtype=np.int64)
    for i, row in enumerate(g):
        for j, v in enumerate(row):
            if v:
                assert v.denominator == 1
                out[i, j] = int(v)
    return out


def apply(g, vec: list[Fraction]) -> list[Fraction]:
    return [dot_q(row, vec) for row in g]


def support_radius(comp: Compilation, g, order=None) -> int:
    order = comp.order if order is None else order
    worst = 0
    for r, row in enumerate(g):
        for c, val in enumerate(row):
            if val != 0 and r != c:
                worst = max(worst, comp.distance(order[r], order[c]))
    return worst


def is_covariant(g, perm: np.ndarray) -> bool:
    """Exact test perm g perm^T == g for a signed permutation matrix perm."""
    n = len(g)
    image = {}
    for c in range(n):
        rows = np.nonzero(perm[:, c])[0]
        image[c] = (int(rows[0]), int(perm[rows[0], c]))
    for r in range(n):
        ir, sr = image[r]
        row = g[r]
        for c in range(n):
            ic, sc = image[c]
            if g[ir][ic] != sr * sc * row[c]:
                return False
    return True


def metric_skew_defect(g, weights: list[Fraction]) -> Fraction:
    """Sum of |(M G + G^T M)_ij| for M = diag(weights); zero iff the weighted energy is conserved."""
    n = len(g)
    total = Fraction(0)
    for i in range(n):
        wi = weights[i]
        for j in range(n):
            total += abs(wi * g[i][j] + weights[j] * g[j][i])
    return total


def role_weights(comp: Compilation, wV, wE, wB, wC) -> list[Fraction]:
    return [Fraction(wV)] * comp.nv + [Fraction(wE)] * comp.ne + [Fraction(wB)] * comp.nf + [Fraction(wC)] * comp.nc


def energy_rate(g, vec, weights) -> Fraction:
    rate = apply(g, vec)
    return sum(w * x * y for w, x, y in zip(weights, vec, rate))


def state(comp: Compilation, phi, E, B, psi) -> list[Fraction]:
    return list(phi) + list(E) + list(B) + list(psi)


def split(comp: Compilation, vec):
    return (vec[comp.offV:comp.offV + comp.nv], vec[comp.offE:comp.offE + comp.ne],
            vec[comp.offF:comp.offF + comp.nf], vec[comp.offC:comp.offC + comp.nc])


# ---------------------------------------------------------------------------
# covariant classification on the four-role payload: the 56 translation-covariant patterns
# ---------------------------------------------------------------------------


def nn_basis4(comp: Compilation):
    """Translation-covariant nearest-neighbor generator patterns on the four-role payload.

    One pattern per (target role and axis label, source role, relative offset) family with unit
    coefficient at every translate.  Returns (labels, integer matrices, representative entries).
    """
    labels, mats, reps = [], [], []

    def add(label, entries):
        m = np.zeros((comp.n, comp.n), dtype=np.int64)
        for r, c in entries:
            m[r, c] += 1
        labels.append(label)
        mats.append(m)
        reps.append(entries[0])

    add(("vertex_onsite",), [(comp.offV + v, comp.offV + v) for v in range(comp.nv)])
    for a in AXES:
        for s in (1, -1):
            add(("vertex_from_edge", a, s),
                [(comp.offV + v, comp.offE + comp.eidx[comp.shift(x, a, s)]) for v, x in enumerate(comp.vertices)])
    for a in AXES:
        add(("edge_onsite", a), [(comp.offE + e, comp.offE + e) for e, x in enumerate(comp.edges) if comp.edge_axis(x) == a])
        for s in (1, -1):
            add(("edge_from_vertex", a, s),
                [(comp.offE + e, comp.offV + comp.vidx[comp.shift(x, a, s)]) for e, x in enumerate(comp.edges) if comp.edge_axis(x) == a])
        for bax in AXES:
            if bax == a:
                continue
            for s in (1, -1):
                add(("edge_from_face", a, bax, s),
                    [(comp.offE + e, comp.offF + comp.fidx[comp.shift(x, bax, s)]) for e, x in enumerate(comp.edges) if comp.edge_axis(x) == a])
    for k in AXES:
        i, j = CYCLIC[k]
        add(("face_onsite", k), [(comp.offF + f, comp.offF + f) for f, x in enumerate(comp.faces) if comp.face_normal(x) == k])
        for cax in (i, j):
            for s in (1, -1):
                add(("face_from_edge", k, cax, s),
                    [(comp.offF + f, comp.offE + comp.eidx[comp.shift(x, cax, s)]) for f, x in enumerate(comp.faces) if comp.face_normal(x) == k])
        for s in (1, -1):
            add(("face_from_cube", k, s),
                [(comp.offF + f, comp.offC + comp.cidx[comp.shift(x, k, s)]) for f, x in enumerate(comp.faces) if comp.face_normal(x) == k])
    add(("cube_onsite",), [(comp.offC + c, comp.offC + c) for c in range(comp.nc)])
    for k in AXES:
        for s in (1, -1):
            add(("cube_from_face", k, s),
                [(comp.offC + c, comp.offF + comp.fidx[comp.shift(x, k, s)]) for c, x in enumerate(comp.cubes)])
    return labels, mats, reps


def covariant_subspace(mats, reps, perms: list[np.ndarray]):
    """Exact nullspace of the covariance constraints perm G perm^T = G on the pattern coefficients.

    Every rotated pattern must lie in the pattern span (checked); the constraint system is then
    A theta = 0 with A[(perm, j), i] = c_{perm, i, j} - delta_{ij}.
    """
    npat = len(mats)
    system = []
    consistent = True
    for perm in perms:
        coeff_rows = []
        for mat in mats:
            conj = perm @ mat @ perm.T
            coeffs = [int(conj[r, c]) for (r, c) in reps]
            rebuilt = sum((cf * m for cf, m in zip(coeffs, mats)), np.zeros_like(conj))
            consistent = consistent and bool(np.array_equal(rebuilt, conj))
            coeff_rows.append(coeffs)
        for j in range(npat):
            row = [Fraction(0)] * npat
            for i in range(npat):
                row[i] += coeff_rows[i][j]
            row[j] -= 1
            system.append(row)
    return nullspace_q(system), consistent


def vectorize(mat) -> list[Fraction]:
    return [Fraction(int(v)) for v in np.asarray(mat).ravel().tolist()]


def assemble(mats, coeffs: list[Fraction]) -> np.ndarray:
    total = np.zeros_like(mats[0])
    for coef, m in zip(coeffs, mats):
        if coef:
            assert coef.denominator == 1
            total = total + int(coef) * m
    return total


def span_contains(basis_vectors, target) -> bool:
    return rank_q(basis_vectors + [target]) == rank_q(basis_vectors)


def embed(comp: Compilation, blk: np.ndarray, rows: str, cols: str) -> np.ndarray:
    off = {"V": (comp.offV, comp.nv), "E": (comp.offE, comp.ne), "F": (comp.offF, comp.nf), "C": (comp.offC, comp.nc)}
    m = np.zeros((comp.n, comp.n), dtype=np.int64)
    r0, rn = off[rows]
    c0, cn = off[cols]
    m[r0:r0 + rn, c0:c0 + cn] = blk
    return m


# ---------------------------------------------------------------------------
# the Gauss rates as linear functionals; invariant subspaces
# ---------------------------------------------------------------------------


def gauss_rate_matrix(comp: Compilation, g, which: str) -> list[list[Fraction]]:
    """The matrix of x -> d/dt(row) = P (G x) as a Fraction matrix (rows: vertices or cubes)."""
    if which == "E":
        P = comp.d0.T
        rows = g[comp.offE:comp.offE + comp.ne]
    else:
        P = comp.d2
        rows = g[comp.offF:comp.offF + comp.nf]
    out = [[Fraction(0)] * comp.n for _ in range(P.shape[0])]
    for col in range(comp.n):
        column = [row[col] for row in rows]
        img = matvec_q(P, column)
        for i, v in enumerate(img):
            out[i][col] = v
    return out


def observability_stack(Q: np.ndarray, G: np.ndarray) -> tuple[np.ndarray, int]:
    """Stack [Q; QG; QG^2; ...] until the row space stops growing (exact ranks)."""
    rows = [Q]
    cur = Q
    r = rank_q(Q)
    steps = 0
    while True:
        cur = cur @ G
        stacked = np.vstack(rows + [cur])
        r_new = rank_q(stacked)
        steps += 1
        if r_new == r:
            return np.vstack(rows), steps
        rows.append(cur)
        r = r_new


def same_row_space(A, B) -> bool:
    ra, rb = rank_q(A), rank_q(B)
    return ra == rb == rank_q(frac_rows(A) + frac_rows(B))


def torus_momentum_count(side: int) -> int:
    return (side // 2) ** 3 - 1


def restricted_multiplicity(A, constraint_rows, lam: Fraction, n: int) -> int:
    """dim ker(A - lam I) inside ker(constraint_rows) = n - rank([A - lam I; constraints])."""
    rows = []
    for i in range(n):
        row = [Fraction(int(v)) for v in A[i].tolist()]
        row[i] -= lam
        rows.append(row)
    rows += frac_rows(constraint_rows)
    return n - rank_q(rows)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main() -> int:
    print("U(1) light lane: the Gauss rows as support forcing on the extended (phi, E, B, psi) payload class (exact)")
    print("=" * 108)
    rng = random.Random(20260905)

    # ---------------------------------------------------------------- A
    section("A. Axiom memo runtime read (two canonical proof/scope inputs additionally pinned)")
    memo = (ROOT / AXIOM_REL).read_text(encoding="utf-8")
    sentences = {
        "lattice sites": "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor\nadjacency, standard translations, and proper cubic rotations about each site.",
        "no site privileged": "No site is privileged. Sites are distinguished by the supplied lattice\nstructure alone.",
        "qubit domain": "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "no possibility privileged": "No possibility is privileged. Possibilities are distinguished by the supplied\nalgebraic structure alone.",
        "one fixed covariant rule": "There is one fixed nearest-neighbor admissibility rule, covariant under lattice\ntranslations and proper cubic rotations.",
        "distribution sentence": "For each site, the probability distribution over the possibilities is\ndetermined by, and varies with, the nearest-neighbor conditions.",
        "support reading note": "\"available\"/\"admissible\" denotes its support --\non finite menus, exactly the possibilities of nonzero probability.",
        "records lock one admissible possibility": "When present, a record locks exactly one admissible local possibility.",
        "one record, permanent": "A\nsite never carries more than one record; records are permanent.",
        "readout": "Only records are readable. A readout value is determined by record content\nalone. A site with no record cannot be read.",
        "qualification: further structure": "Further physical\nstructure requires a retained derivation or bridge, or explicit approved-\nprimitive registration, before use as a premise.",
        "law sentence": "A law privileges no states. Its domain is a supplied condition, and at every\nstate where the condition holds it gives exactly one answer.",
        "not a dynamics axiom": "Admissibility is not a dynamics axiom.",
        "no Hamiltonian / time metric": "choose a Hamiltonian or transfer operator, supply transition-probability or\nweight values, select a scalar or nonzero kinetic branch, assert a Dirac-square\ncarrier, define a time metric, or provide a record-production process or\nphysical persistence dynamics.",
        "2026-08-05 availability as support": "availability became the distribution's support (on finite\nmenus, exactly the possibilities of nonzero probability;",
    }
    for name, text in sentences.items():
        check(f"memo carries verbatim: {name}", text in memo)

    # ---------------------------------------------------------------- B
    section("B. The supplied compilation, rebuilt from the parity rule (sides 4 and 6)")
    comps = {side: Compilation(side) for side in (4, 6)}
    for side, comp in comps.items():
        coarse = (side // 2) ** 3
        check(f"side {side}: role census vertices/edges/faces/cubes = {coarse}/{3 * coarse}/{3 * coarse}/{coarse}; state dimension {comp.n}",
              (comp.nv, comp.ne, comp.nf, comp.nc) == (coarse, 3 * coarse, 3 * coarse, coarse) and comp.n == side ** 3)
        shells_ok = True
        for x in comp.sites:
            kinds = [comp.weight(y) for y in comp.neighbors(x)]
            w = comp.weight(x)
            expect = {0: {1: 6}, 1: {0: 2, 2: 4}, 2: {1: 4, 3: 2}, 3: {2: 6}}[w]
            shells_ok = shells_ok and all(kinds.count(k) == c for k, c in expect.items()) and w not in kinds
        check(f"side {side}: shells -- vertex: 6 edges; edge: 2 vertices + 4 faces; face: 4 edges + 2 cubes; cube: 6 faces; no same-role neighbor", shells_ok)
        parity_ok = True
        for x in comp.sites:
            for y in comp.sites:
                parity_ok = parity_ok and (comp.distance(x, y) % 2 == (comp.weight(x) + comp.weight(y)) % 2)
        check(f"side {side}: parity theorem -- torus distance is odd exactly between roles of opposite parity (vertex-edge, edge-face, face-cube, vertex-cube)", parity_ok)
        check(f"side {side}: chain identities C d0 = 0 and d2 C = 0 over the integers",
              not np.any(comp.curl @ comp.d0) and not np.any(comp.d2 @ comp.curl))
        rows_ok = (all(sorted(row[row != 0].tolist()) == [-1, 1] for row in comp.d0)
                   and all(sorted(row[row != 0].tolist()) == [-1, -1, 1, 1] for row in comp.curl)
                   and all(sorted(row[row != 0].tolist()) == [-1, -1, -1, 1, 1, 1] for row in comp.d2))
        nn_ok = (all(comp.distance(comp.edges[e], comp.vertices[v]) == 1 for e, v in zip(*np.nonzero(comp.d0)))
                 and all(comp.distance(comp.faces[f], comp.edges[e]) == 1 for f, e in zip(*np.nonzero(comp.curl)))
                 and all(comp.distance(comp.cubes[c], comp.faces[f]) == 1 for c, f in zip(*np.nonzero(comp.d2))))
        check(f"side {side}: d0 rows (+1,-1), curl rows (+1,+1,-1,-1), d2 rows (three +1, three -1); every incidence entry at physical distance 1", rows_ok and nn_ok)
        # connectedness lever
        LV = comp.d0.T @ comp.d0
        LC = comp.d2 @ comp.d2.T
        kerLV = nullspace_q(LV)
        kerLC = nullspace_q(LC)
        const_v = all(v == kerLV[0][0] for v in kerLV[0]) if len(kerLV) == 1 else False
        const_c = all(v == kerLC[0][0] for v in kerLC[0]) if len(kerLC) == 1 else False
        check(f"side {side}: connectedness lever -- ker(d0^T d0) and ker(d2 d2^T) are exactly the constants (dimension 1 each); rank d0 = {comp.nv - 1}, rank d2 = {comp.nc - 1}",
              len(kerLV) == 1 and const_v and len(kerLC) == 1 and const_c and rank_q(comp.d0) == comp.nv - 1 and rank_q(comp.d2) == comp.nc - 1)
        ones_v = [Fraction(1)] * comp.nv
        ones_c = [Fraction(1)] * comp.nc
        check(f"side {side}: sum rules d0 1 = 0 and d2^T 1 = 0 -- every electric charge d0^T E and every magnetic charge d2 B sums to zero",
              is_zero(matvec_q(comp.d0, ones_v)) and is_zero(matvec_q(comp.d2.T, ones_c)))
        # image of d0^T is exactly the zero-sum vectors (a charged surface is nonempty iff the charge sums to zero)
        dipole = [Fraction(0)] * comp.nv
        dipole[0], dipole[comp.vidx[comp.shift(comp.vertices[0], 0, 2)]] = Fraction(1), Fraction(-1)
        monopole = [Fraction(0)] * comp.nv
        monopole[0] = Fraction(1)
        sol_dip = solve_q(comp.d0.T, dipole)
        sol_mono = solve_q(comp.d0.T, monopole)
        check(f"side {side}: d0^T E = rho is solvable for a zero-sum dipole charge and unsolvable for a unit monopole (image of d0^T = zero-sum vectors, by connectedness)",
              sol_dip is not None and matvec_q(comp.d0.T, sol_dip) == dipole and sol_mono is None)
        # odd-shift self-duality
        sigma_v = {v: comp.cidx[comp.translate(x, (1, 1, 1))] for v, x in enumerate(comp.vertices)}
        sigma_e = {e: comp.fidx[comp.translate(x, (1, 1, 1))] for e, x in enumerate(comp.edges)}
        sigma_f = {f: comp.eidx[comp.translate(x, (1, 1, 1))] for f, x in enumerate(comp.faces)}
        sigma_c = {c: comp.vidx[comp.translate(x, (1, 1, 1))] for c, x in enumerate(comp.cubes)}
        dual_ok = (all(int(comp.d0[e, v]) == -int(comp.d2[sigma_v[v], sigma_e[e]]) for e in range(comp.ne) for v in range(comp.nv))
                   and all(int(comp.curl[f, e]) == int(comp.curl[sigma_e[e], sigma_f[f]]) for f in range(comp.nf) for e in range(comp.ne))
                   and all(int(comp.d2[c, f]) == -int(comp.d0[sigma_f[f], sigma_c[c]]) for c in range(comp.nc) for f in range(comp.nf)))
        check(f"side {side}: odd-shift self-duality -- the translation by (1,1,1) maps roles V->C, E->F, F->E, C->V and conjugates (d0, C, d2) to (-d2^T, C^T, -d0^T) exactly",
              dual_ok)

    comp4, comp6 = comps[4], comps[6]

    # ---------------------------------------------------------------- C
    section("C. Covariance of the compilation under the oriented four-role law (side 4)")
    rots = proper_rotations()
    perms4 = [field_rotation4(comp4, r) for r in rots]
    cov_ok = True
    for p in perms4:
        pV, pE, pF, pC = block(p, comp4, "V", "V"), block(p, comp4, "E", "E"), block(p, comp4, "F", "F"), block(p, comp4, "C", "C")
        cov_ok = cov_ok and np.array_equal(pE @ comp4.d0 @ pV.T, comp4.d0) and np.array_equal(pF @ comp4.curl @ pE.T, comp4.curl) \
            and np.array_equal(pC @ comp4.d2 @ pF.T, comp4.d2)
    check("d0, C and d2 are each covariant under all 24 proper rotations about a vertex (phi scalar, E vector-along-axis, B vector-along-normal, psi scalar)", cov_ok)
    index_of = {tuple(map(tuple, r)): i for i, r in enumerate(rots)}
    rep_ok = all(np.array_equal(perms4[index_of[tuple(map(tuple, r1 @ r2))]], perms4[i] @ perms4[j])
                 for i, r1 in enumerate(rots) for j, r2 in enumerate(rots))
    signed_ok = all(np.array_equal(np.abs(p).sum(axis=0), np.ones(comp4.n, dtype=np.int64)) and np.array_equal(np.abs(p).sum(axis=1), np.ones(comp4.n, dtype=np.int64)) for p in perms4)
    check("the four-role oriented law is a genuine signed-permutation representation of the rotation group (composition law on all 24 x 24 pairs)", rep_ok and signed_ok)
    even4 = [translation4(comp4, sh) for sh in itertools.product((0, 2), repeat=3) if any(sh)]
    even_ok = all(np.array_equal(block(t, comp4, "E", "E") @ comp4.d0 @ block(t, comp4, "V", "V").T, comp4.d0)
                  and np.array_equal(block(t, comp4, "F", "F") @ comp4.curl @ block(t, comp4, "E", "E").T, comp4.curl)
                  and np.array_equal(block(t, comp4, "C", "C") @ comp4.d2 @ block(t, comp4, "F", "F").T, comp4.d2) for t in even4)
    check("d0, C and d2 are covariant under all seven nontrivial even translations of the side-4 torus", even_ok)

    # ---------------------------------------------------------------- D
    section("D. Exact classification of covariant nearest-neighbor generators on the four-role payload (sides 4 and 6)")
    perms6 = [field_rotation4(comp6, r) for r in rots]
    labels, mats, reps = nn_basis4(comp4)
    for side, comp in comps.items():
        perms = perms4 if side == 4 else perms6
        labels_s, mats_s, reps_s = (labels, mats, reps) if side == 4 else nn_basis4(comp)
        basis, consistent = covariant_subspace(mats_s, reps_s, perms)
        expected = {
            "onsite V": embed(comp, np.eye(comp.nv, dtype=np.int64), "V", "V"),
            "onsite E": embed(comp, np.eye(comp.ne, dtype=np.int64), "E", "E"),
            "onsite B": embed(comp, np.eye(comp.nf, dtype=np.int64), "F", "F"),
            "onsite C": embed(comp, np.eye(comp.nc, dtype=np.int64), "C", "C"),
            "d0 (E from phi)": embed(comp, comp.d0, "E", "V"),
            "d0^T (phi from E)": embed(comp, comp.d0.T, "V", "E"),
            "C (B from E)": embed(comp, comp.curl, "F", "E"),
            "C^T (E from B)": embed(comp, comp.curl.T, "E", "F"),
            "d2 (psi from B)": embed(comp, comp.d2, "C", "F"),
            "d2^T (B from psi)": embed(comp, comp.d2.T, "F", "C"),
        }
        span = [vectorize(assemble(mats_s, vec)) for vec in basis]
        expected_vecs = [vectorize(m) for m in expected.values()]
        check(f"side {side}: the translation-covariant nearest-neighbor pattern basis has 56 patterns and every rotated pattern stays in its span",
              len(mats_s) == 56 and consistent, f"patterns={len(mats_s)}")
        check(f"side {side}: covariant class on (phi, E, B, psi) = span{{onsite x4, d0, d0^T, C, C^T, d2, d2^T}} exactly (nullspace dimension 10 under all 24 rotations; all ten expected members inside; their rank is 10)",
              len(basis) == 10 and all(span_contains(span, v) for v in expected_vecs) and rank_q(expected_vecs) == 10, f"dim={len(basis)}")
        # every member of the class is translation covariant (pattern construction) -- executed on one generic member
        generic = member(comp, uV=Fraction(1, 2), uE=Fraction(-1, 3), uB=2, uC=Fraction(3, 5), a=1, a2=Fraction(-2, 7), q=3, r=Fraction(1, 4), b=-1, b2=Fraction(5, 2))
        evens = [translation4(comp, sh) for sh in itertools.product(range(0, side, 2), repeat=3) if any(sh)]
        check(f"side {side}: a generic member of the ten-parameter class is covariant under all 24 rotations and all {len(evens)} nontrivial even translations, and has support radius exactly 1",
              all(is_covariant(generic, p) for p in perms) and all(is_covariant(generic, t) for t in evens) and support_radius(comp, generic) == 1)

    # ---------------------------------------------------------------- E
    section("E. Positive-diagonal conservation on the class: the symbolic cut (three free speeds)")
    uV, uE, uB, uC, a, a2, q, r, b, b2 = sp.symbols("u_V u_E u_B u_C a a2 q r b b2", real=True)
    wV, wE, wB, wC = sp.symbols("w_V w_E w_B w_C", positive=True)
    # blockwise M G + G^T M with M = diag(w_V, w_E, w_B, w_C) (x) I and the block structure of section D:
    # diagonal blocks 2 w u; (V,E) block (w_V a + w_E a2) d0^T; (E,F) block (w_E r + w_B q) C^T; (F,C) block (w_B b + w_C b2) d2^T
    eqs = [2 * wV * uV, 2 * wE * uE, 2 * wB * uB, 2 * wC * uC, wV * a + wE * a2, wE * r + wB * q, wB * b + wC * b2]
    sol = sp.solve(eqs, [uV, uE, uB, uC, a2, r, b2], dict=True)
    check("symbolic: positive diagonal conservation <=> u_V = u_E = u_B = u_C = 0, a2 = -w_V a / w_E, r = -w_B q / w_E, b2 = -w_B b / w_C (three free coupling scales a, q, b)",
          sol == [{uV: 0, uE: 0, uB: 0, uC: 0, a2: -wV * a / wE, r: -wB * q / wE, b2: -wB * b / wC}])
    check("the block reduction is exact because d0^T, C^T and d2^T are nonzero matrices (a scalar multiple of one vanishes iff the scalar does)",
          np.any(comp4.d0) and np.any(comp4.curl) and np.any(comp4.d2))
    w6 = role_weights(comp6, 1, 1, 1, 1)
    three_speed = member(comp6, a=-2, a2=2, q=1, r=-1, b=-3, b2=3)
    one_speed = member(comp6, q=1, r=-1)
    x6 = rational_vector(comp6.n, rng)
    check("side 6: the three-speed member (a=-2, a2=2; q=1, r=-1; b=-3, b2=3) has metric-skew defect zero and dH/dt = 0 exactly on a random rational state",
          metric_skew_defect(three_speed, w6) == 0 and energy_rate(three_speed, x6, w6) == 0)
    broken = member(comp6, a=-2, a2=1, q=1, r=-1)
    check("side 6: a member violating one cut condition (w_V a + w_E a2 = -1 != 0) has nonzero defect and dH/dt != 0", metric_skew_defect(broken, w6) != 0 and energy_rate(broken, x6, w6) != 0)

    # ---------------------------------------------------------------- F
    section("F. The Gauss rates as exact linear functionals, coefficient by coefficient (side 6)")
    LV6 = comp6.d0.T @ comp6.d0
    LC6 = comp6.d2 @ comp6.d2.T
    zero_VV = np.zeros((comp6.nv, comp6.nv), dtype=np.int64)
    zero_VE = np.zeros((comp6.nv, comp6.ne), dtype=np.int64)
    zero_VF = np.zeros((comp6.nv, comp6.nf), dtype=np.int64)
    zero_VC = np.zeros((comp6.nv, comp6.nc), dtype=np.int64)
    zero_CV = np.zeros((comp6.nc, comp6.nv), dtype=np.int64)
    zero_CE = np.zeros((comp6.nc, comp6.ne), dtype=np.int64)
    zero_CF = np.zeros((comp6.nc, comp6.nf), dtype=np.int64)
    zero_CC = np.zeros((comp6.nc, comp6.nc), dtype=np.int64)
    expect_E = {k: (zero_VV, zero_VE, zero_VF, zero_VC) for k in COEFFS}
    expect_E["a2"] = (LV6, zero_VE, zero_VF, zero_VC)
    expect_E["uE"] = (zero_VV, comp6.d0.T, zero_VF, zero_VC)
    expect_M = {k: (zero_CV, zero_CE, zero_CF, zero_CC) for k in COEFFS}
    expect_M["b"] = (zero_CV, zero_CE, zero_CF, LC6)
    expect_M["uB"] = (zero_CV, zero_CE, comp6.d2, zero_CC)
    all_ok = True
    for k in COEFFS:
        unit = member(comp6, **{k: 1})
        RE = gauss_rate_matrix(comp6, unit, "E")
        RM = gauss_rate_matrix(comp6, unit, "M")
        blocksE = [[row[comp6.offV:comp6.offE] for row in RE], [row[comp6.offE:comp6.offF] for row in RE],
                   [row[comp6.offF:comp6.offC] for row in RE], [row[comp6.offC:] for row in RE]]
        blocksM = [[row[comp6.offV:comp6.offE] for row in RM], [row[comp6.offE:comp6.offF] for row in RM],
                   [row[comp6.offF:comp6.offC] for row in RM], [row[comp6.offC:] for row in RM]]
        ok = all(frac_matrix_equal(bl, ex) for bl, ex in zip(blocksE, expect_E[k])) and all(frac_matrix_equal(bl, ex) for bl, ex in zip(blocksM, expect_M[k]))
        all_ok = all_ok and ok
    check("d/dt(d0^T E) = a2 (d0^T d0) phi + u_E (d0^T E) exactly: the contribution of r is d0^T C^T = 0, and a, u_V, q, u_B, b, b2, u_C contribute nothing (all ten unit members)",
          all_ok and not np.any(comp6.d0.T @ comp6.curl.T))
    check("d/dt(d2 B) = b (d2 d2^T) psi + u_B (d2 B) exactly: the contribution of q is d2 C = 0, and the other coefficients contribute nothing (all ten unit members)",
          all_ok and not np.any(comp6.d2 @ comp6.curl))
    check("side 6: the vertex Laplacian d0^T d0 and the cube Laplacian d2 d2^T are nonzero (rank 26 each), so a2 (d0^T d0) = 0 iff a2 = 0 and b (d2 d2^T) = 0 iff b = 0",
          rank_q(LV6) == comp6.nv - 1 and rank_q(LC6) == comp6.nc - 1)

    # ---------------------------------------------------------------- G
    section("G. The collapse theorem: which members leave the Gauss surfaces invariant (sides 4 and 6)")
    # a state on the zero-charge electric surface with a nonconstant vertex payload
    for side, comp in comps.items():
        delta = [Fraction(0)] * comp.nv
        delta[0] = Fraction(1)
        x_delta = state(comp, delta, [Fraction(0)] * comp.ne, [Fraction(0)] * comp.nf, [Fraction(0)] * comp.nc)
        m3 = member(comp, a=-2, a2=2, q=1, r=-1, b=-3, b2=3)
        m1 = member(comp, q=1, r=-1)
        rateE_m3 = matvec_q(comp.d0.T, split(comp, apply(m3, x_delta))[1])
        check(f"side {side}: the three-speed member does NOT preserve the electric surface: a zero-charge state with phi = delta (E = B = psi = 0) has d/dt(d0^T E) = 2 (d0^T d0) delta != 0",
              not is_zero(rateE_m3) and is_zero(matvec_q(comp.d0.T, split(comp, x_delta)[1])))
        deltaC = [Fraction(0)] * comp.nc
        deltaC[0] = Fraction(1)
        x_deltaC = state(comp, [Fraction(0)] * comp.nv, [Fraction(0)] * comp.ne, [Fraction(0)] * comp.nf, deltaC)
        rateM_m3 = matvec_q(comp.d2, split(comp, apply(m3, x_deltaC))[2])
        check(f"side {side}: nor the magnetic surface: psi = delta (phi = E = B = 0) has d/dt(d2 B) = -3 (d2 d2^T) delta != 0", not is_zero(rateM_m3))
        RE1 = gauss_rate_matrix(comp, m1, "E")
        RM1 = gauss_rate_matrix(comp, m1, "M")
        check(f"side {side}: the one-speed member (a = a2 = b = b2 = 0) has BOTH rate functionals identically zero (every state, every background charge): both surfaces invariant",
              all(is_zero(row) for row in RE1) and all(is_zero(row) for row in RM1))
        # the frozen payloads
        phi_rows_m1 = m1[comp.offV:comp.offE]
        psi_rows_m1 = m1[comp.offC:]
        check(f"side {side}: under the one-speed member d phi/dt = 0 and d psi/dt = 0 identically -- the vertex and cube payloads are frozen at every state, on and off the surfaces",
              all(is_zero(row) for row in phi_rows_m1) and all(is_zero(row) for row in psi_rows_m1))
    # the invariance condition is exactly a2 = 0 (and u_E rho = 0), independent of every other coefficient: a member with a2 = 0 but everything else nonzero
    decoupled = member(comp6, uV=Fraction(1, 2), uC=Fraction(2, 3), a=Fraction(3, 2), q=2, r=Fraction(-1, 5), b2=4)
    RE_dec = gauss_rate_matrix(comp6, decoupled, "E")
    RM_dec = gauss_rate_matrix(comp6, decoupled, "M")
    check("side 6: a member with a2 = 0, b = 0 and u_E = u_B = 0 but every other coefficient nonzero (a, q, r, b2, u_V, u_C) has both rate functionals identically zero -- invariance needs only a2 = 0 / b = 0 (plus u_E rho_V = 0 / u_B rho_C = 0)",
          all(is_zero(row) for row in RE_dec) and all(is_zero(row) for row in RM_dec))
    # conservation then kills a and b2 with a2 and b
    a_s, a2_s, b_s, b2_s = sp.symbols("a a2 b b2", real=True)
    check("symbolic: on the conservative subfamily a2 = -w_V a / w_E and b2 = -w_B b / w_C with positive weights, so a2 = 0 <=> a = 0 and b = 0 <=> b2 = 0: the invariant conservative members are exactly the one-speed edge/face law with frozen phi and psi",
          sp.solve([wV * a_s + wE * a2_s, a2_s], [a_s, a2_s], dict=True) == [{a_s: 0, a2_s: 0}]
          and sp.solve([wB * b_s + wC * b2_s, b_s], [b_s, b2_s], dict=True) == [{b_s: 0, b2_s: 0}])
    # the non-conservative decoupled member: phi drifts linearly by a rho_V on a charged surface
    drift = member(comp6, a=Fraction(3, 2), q=1, r=-1)
    G_drift = drift
    dip6 = [Fraction(0)] * comp6.nv
    dip6[0], dip6[comp6.vidx[comp6.shift(comp6.vertices[0], 0, 2)]] = Fraction(1), Fraction(-1)
    E_part = solve_q(comp6.d0.T, dip6)
    x_ch = state(comp6, rational_vector(comp6.nv, rng), E_part, rational_vector(comp6.nf, rng), rational_vector(comp6.nc, rng))
    rate1 = apply(G_drift, x_ch)
    rate2 = apply(G_drift, rate1)
    phi_dot, _, _, _ = split(comp6, rate1)
    phi_ddot, _, _, _ = split(comp6, rate2)
    check("side 6, non-conservative member a2 = uV = uE = 0, a = 3/2 on a charged surface (dipole rho_V): d phi/dt = a rho_V exactly and d^2 phi/dt^2 = 0 -- the vertex payload drifts linearly in time by a multiple of the charge; in the zero-charge sector it is frozen",
          phi_dot == [Fraction(3, 2) * v for v in dip6] and is_zero(phi_ddot)
          and is_zero(matvec_q(comp6.d0.T, split(comp6, rate1)[1])))
    # u_E rho != 0 breaks a charged surface only
    damped_E = member(comp6, uE=Fraction(-1, 3), q=1, r=-1)
    rateE_damp = matvec_q(comp6.d0.T, split(comp6, apply(damped_E, x_ch))[1])
    x_zero = state(comp6, rational_vector(comp6.nv, rng), matvec_q(comp6.curl.T, rational_vector(comp6.nf, rng)), rational_vector(comp6.nf, rng), rational_vector(comp6.nc, rng))
    rateE_damp0 = matvec_q(comp6.d0.T, split(comp6, apply(damped_E, x_zero))[1])
    check("side 6: a member with u_E = -1/3 (a2 = 0) preserves the zero-charge electric surface but not a charged one: the rate on the dipole surface is u_E rho_V != 0 (the charge decays)",
          rateE_damp == [Fraction(-1, 3) * v for v in dip6] and is_zero(rateE_damp0) and is_zero(matvec_q(comp6.d0.T, split(comp6, x_zero)[1])))

    # Countercontrols prevent exporting the special member's domain to all EC.
    degenerate = Compilation(2)
    check("side 2 has zero incidence/Laplacians and is excluded from the nondegenerate collapse iff theorem",
          not np.any(degenerate.d0) and not np.any(degenerate.curl) and not np.any(degenerate.d2))
    growth = member(comp4, uV=1, q=1, r=-1)
    xd = [Fraction(0)] * comp4.n
    xd[0] = Fraction(1)
    growth_rate = apply(growth, xd)
    check("general SF-all without CONS need not freeze phi: uV=1 preserves both Gauss functionals while phi_dot=phi",
          all(is_zero(row) for row in gauss_rate_matrix(comp4, growth, "E"))
          and all(is_zero(row) for row in gauss_rate_matrix(comp4, growth, "M")) and growth_rate[0] == 1)
    partial = member(comp4, a=-2, a2=2, q=1, r=-1)
    cube_delta = [Fraction(0)] * comp4.n
    cube_delta[-1] = Fraction(1)
    check("a conservative member failing electric SF-all can have arbitrary nonconstant stationary psi when b=b2=0",
          metric_skew_defect(partial, role_weights(comp4, 1, 1, 1, 1)) == 0
          and any(not is_zero(row) for row in gauss_rate_matrix(comp4, partial, "E"))
          and is_zero(apply(partial, cube_delta)))

    # ---------------------------------------------------------------- H
    section("H. The maximal Gauss sector of the specified three-speed member (sides 4 and 6)")
    for side, comp in comps.items():
        G3 = int_matrix(member(comp, a=-2, a2=2, q=1, r=-1, b=-3, b2=3))
        # electric row only
        QE = np.zeros((comp.nv, comp.n), dtype=np.int64)
        QE[:, comp.offE:comp.offF] = comp.d0.T
        stackE, stepsE = observability_stack(QE, G3)
        expectE = np.zeros((comp.nv + comp.nv - 1, comp.n), dtype=np.int64)
        expectE[:comp.nv, comp.offE:comp.offF] = comp.d0.T
        for i in range(1, comp.nv):
            expectE[comp.nv + i - 1, comp.offV + i] = 1
            expectE[comp.nv + i - 1, comp.offV] = -1
        dimE = comp.n - rank_q(stackE)
        check(f"side {side}: the maximal invariant subspace of the three-speed member inside the zero-charge electric surface is exactly {{d0^T E = 0, phi constant}} (dimension {1 + (comp.ne - comp.nv + 1) + comp.nf + comp.nc}; stabilizes after {stepsE} steps)",
              same_row_space(stackE, expectE) and dimE == 1 + (comp.ne - comp.nv + 1) + comp.nf + comp.nc, f"dim={dimE}")
        # both rows
        QB = np.zeros((comp.nv + comp.nc, comp.n), dtype=np.int64)
        QB[:comp.nv, comp.offE:comp.offF] = comp.d0.T
        QB[comp.nv:, comp.offF:comp.offC] = comp.d2
        stackB, stepsB = observability_stack(QB, G3)
        nconst = (comp.nv - 1) + (comp.nc - 1)
        expectB = np.zeros((comp.nv + comp.nc + nconst, comp.n), dtype=np.int64)
        expectB[:comp.nv + comp.nc] = QB
        rowi = comp.nv + comp.nc
        for i in range(1, comp.nv):
            expectB[rowi, comp.offV + i], expectB[rowi, comp.offV] = 1, -1
            rowi += 1
        for i in range(1, comp.nc):
            expectB[rowi, comp.offC + i], expectB[rowi, comp.offC] = 1, -1
            rowi += 1
        dimB = comp.n - rank_q(stackB)
        sector_dim = 2 + (comp.ne - comp.nv + 1) + (comp.nf - comp.nc + 1)
        check(f"side {side}: with both rows, the Gauss sector of the three-speed member is exactly {{d0^T E = 0, d2 B = 0, phi constant, psi constant}} (dimension {sector_dim})",
              same_row_space(stackB, expectB) and dimB == sector_dim, f"dim={dimB}")
        W = nullspace_q(expectB)
        G3q = member(comp, a=-2, a2=2, q=1, r=-1, b=-3, b2=3)
        G1q = member(comp, q=1, r=-1)
        stays = all(is_zero(matvec_q(expectB, apply(G3q, w))) for w in W)
        agrees = all(is_zero([x - y for x, y in zip(apply(G3q, w), apply(G1q, w))]) for w in W)
        frozen = all(is_zero(split(comp, apply(G3q, w))[0]) and is_zero(split(comp, apply(G3q, w))[3]) for w in W)
        check(f"side {side}: the flow maps the Gauss sector into itself, the three-speed and one-speed members agree on it as linear maps (the vertex and cube couplings are invisible there), and phi, psi have zero rate on it (frozen constants)",
              stays and agrees and frozen)
        # charged surface: the invariant subset is {x in U1 : Q x = rho} with U1 = the unobservable subspace of (QG, G),
        # i.e. Q G^k x = 0 for all k >= 1; it is nonempty iff rho lies in Q(U1)
        rho = [Fraction(0)] * comp.nv
        rho[0], rho[comp.vidx[comp.shift(comp.vertices[0], 0, 2)]] = Fraction(1), Fraction(-1)

        def charged_surface_has_invariant_subset(G_int: np.ndarray) -> bool:
            stack1, _ = observability_stack(QE @ G_int, G_int)
            homog = frac_rows(stack1) + frac_rows(QE)
            aug = [row + [Fraction(0)] for row in frac_rows(stack1)] + [row + [v] for row, v in zip(frac_rows(QE), rho)]
            return rank_q(aug) == rank_q(homog)

        U1_stack, _ = observability_stack(QE @ G3, G3)
        U1_expect = np.zeros((comp.nv - 1 + comp.nv, comp.n), dtype=np.int64)
        for i in range(1, comp.nv):
            U1_expect[i - 1, comp.offV + i], U1_expect[i - 1, comp.offV] = 1, -1
        U1_expect[comp.nv - 1:, comp.offE:comp.offF] = comp.d0.T
        check(f"side {side}: for the three-speed member the states whose electric charge is constant in time are exactly {{phi constant, d0^T E = 0}} (exact unobservable subspace of (QG, G)); their charge is zero, so a charged surface (dipole rho_V) contains NO invariant subset, while the one-speed member preserves the whole charged surface",
              same_row_space(U1_stack, U1_expect) and not charged_surface_has_invariant_subset(G3)
              and charged_surface_has_invariant_subset(int_matrix(member(comp, q=1, r=-1))))

    # ---------------------------------------------------------------- I
    section("I. Branch count on the Gauss sector, side 6 (exact multiplicities)")
    Q6 = comp6.curl.T @ comp6.curl
    QF6 = comp6.curl @ comp6.curl.T
    G3i = int_matrix(member(comp6, a=-2, a2=2, q=1, r=-1, b=-3, b2=3))
    G3sq = G3i @ G3i
    minus_sq = -G3sq
    EE = block(minus_sq, comp6, "E", "E")
    FF = block(minus_sq, comp6, "F", "F")
    VV = block(minus_sq, comp6, "V", "V")
    CC = block(minus_sq, comp6, "C", "C")
    off_diag_zero = not np.any(minus_sq - (embed(comp6, VV, "V", "V") + embed(comp6, EE, "E", "E") + embed(comp6, FF, "F", "F") + embed(comp6, CC, "C", "C")))
    check("-G^2 of the three-speed member is block diagonal by the chain identities: E-block 4 d0 d0^T + C^T C, B-block C C^T + 9 d2^T d2, phi-block 4 d0^T d0, psi-block 9 d2 d2^T",
          off_diag_zero and np.array_equal(EE, 4 * comp6.d0 @ comp6.d0.T + Q6) and np.array_equal(FF, QF6 + 9 * comp6.d2.T @ comp6.d2)
          and np.array_equal(VV, 4 * LV6) and np.array_equal(CC, 9 * LC6))
    full_E = {lam: comp6.ne - rank_q(EE - lam * np.eye(comp6.ne, dtype=np.int64)) for lam in (0, 3, 6, 9, 12, 24, 36)}
    full_F = {lam: comp6.nf - rank_q(FF - lam * np.eye(comp6.nf, dtype=np.int64)) for lam in (0, 3, 6, 9, 27, 54, 81)}
    nmom = torus_momentum_count(6)
    check("full space, E-block: multiplicities {0:3, 3:12, 6:24, 9:16, 12:6, 24:12, 36:8} (sum 81 = all eigenvalues of a symmetric matrix): two transverse branches at speed 1 (52 = 2 x 26) and one longitudinal branch at speed 2 (26 = 6+12+8, one per nonzero momentum)",
          full_E == {0: 3, 3: 12, 6: 24, 9: 16, 12: 6, 24: 12, 36: 8} and sum(full_E.values()) == comp6.ne
          and full_E[3] + full_E[6] + full_E[9] == 2 * nmom and full_E[12] + full_E[24] + full_E[36] == nmom, full_E)
    check("full space, B-block: multiplicities {0:3, 3:12, 6:24, 9:16, 27:6, 54:12, 81:8}: on the face side the cube coupling supplies a further branch at speed 3 in place of the longitudinal one",
          full_F == {0: 3, 3: 12, 6: 24, 9: 16, 27: 6, 54: 12, 81: 8} and sum(full_F.values()) == comp6.nf, full_F)
    sector_E = {lam: restricted_multiplicity(Q6, comp6.d0.T, Fraction(lam), comp6.ne) for lam in (0, 3, 6, 9)}
    sector_F = {lam: restricted_multiplicity(QF6, comp6.d2, Fraction(lam), comp6.nf) for lam in (0, 3, 6, 9)}
    check("Gauss sector (d0^T E = 0), E-part: C^T C has multiplicities {0:3, 3:12, 6:24, 9:16} on it (sum 55 = dim ker d0^T): exactly two transverse branches per nonzero momentum, the longitudinal branch absent, three harmonic zero modes",
          sector_E == {0: 3, 3: 12, 6: 24, 9: 16} and sum(sector_E.values()) == comp6.ne - comp6.nv + 1 and sector_E[3] + sector_E[6] + sector_E[9] == 2 * nmom, sector_E)
    check("Gauss sector (d2 B = 0), B-part: C C^T has the same multiplicities {0:3, 3:12, 6:24, 9:16} on it (sum 55)",
          sector_F == {0: 3, 3: 12, 6: 24, 9: 16} and sum(sector_F.values()) == comp6.nf - comp6.nc + 1, sector_F)
    # executed on a basis of ker d0^T itself (55 vectors), not only on im C^T (supervisor finding F-B3-2)
    ker_d0T = nullspace_q(comp6.d0.T)
    ker_d2 = nullspace_q(comp6.d2)
    check("the sector spectrum does not depend on the vertex and cube speeds: 4 d0 d0^T annihilates every vector of a basis of ker d0^T (dimension 55) and 9 d2^T d2 every vector of a basis of ker d2, so the E- and B-blocks of -G^2 restricted to the sector equal C^T C and C C^T there, i.e. the three-speed and one-speed members share the sector spectrum exactly",
          len(ker_d0T) == comp6.ne - comp6.nv + 1 and all(is_zero(matvec_q(4 * comp6.d0 @ comp6.d0.T, v)) for v in ker_d0T)
          and len(ker_d2) == comp6.nf - comp6.nc + 1 and all(is_zero(matvec_q(9 * comp6.d2.T @ comp6.d2, v)) for v in ker_d2))
    check("side 6 momentum census: 26 nonzero coarse momenta; on the sector each carries exactly two propagating modes (52 E-modes paired with 52 B-modes), and the zero modes of the restricted flow are 3 + 3 harmonic fields plus the two frozen constants",
          nmom == 26 and sector_E[0] + sector_F[0] + 2 == 8)

    # ---------------------------------------------------------------- J
    section("J. The coin: exact covariant class on the two-component edge/face payload and its conservative cut (side 4)")
    # doubled payload (E1, E2, B1, B2): 30 edge/face patterns x 4 coin pairs = 120 patterns
    labels_eb, mats_eb, reps_eb = [], [], []
    for lab, m, rep in zip(labels, mats, reps):
        if lab[0] in ("edge_onsite", "edge_from_face", "face_onsite", "face_from_edge"):
            labels_eb.append(lab)
            mats_eb.append(block(m, comp4, "E", "E") if False else m[comp4.offE:comp4.offC, comp4.offE:comp4.offC])
            reps_eb.append((rep[0] - comp4.offE, rep[1] - comp4.offE))
    n_eb = comp4.ne + comp4.nf
    n_coin = 2 * n_eb

    def coin_embed(m: np.ndarray, out_c: int, in_c: int) -> np.ndarray:
        big = np.zeros((n_coin, n_coin), dtype=np.int64)
        # order: E1, E2, B1, B2 -> component c of E at rows c*ne, of B at rows 2*ne + c*nf
        for (rr, cc), val in np.ndenumerate(m):
            if val:
                R = rr + out_c * comp4.ne if rr < comp4.ne else 2 * comp4.ne + (rr - comp4.ne) + out_c * comp4.nf
                Cc = cc + in_c * comp4.ne if cc < comp4.ne else 2 * comp4.ne + (cc - comp4.ne) + in_c * comp4.nf
                big[R, Cc] = val
        return big

    def coin_index(i: int, c: int) -> int:
        return i + c * comp4.ne if i < comp4.ne else 2 * comp4.ne + (i - comp4.ne) + c * comp4.nf

    mats_coin, reps_coin, labels_coin = [], [], []
    for lab, m, rep in zip(labels_eb, mats_eb, reps_eb):
        for out_c in (0, 1):
            for in_c in (0, 1):
                mats_coin.append(coin_embed(m, out_c, in_c))
                reps_coin.append((coin_index(rep[0], out_c), coin_index(rep[1], in_c)))
                labels_coin.append(lab + (out_c, in_c))

    def doubled(p: np.ndarray) -> np.ndarray:
        pE, pF = block(p, comp4, "E", "E"), block(p, comp4, "F", "F")
        big = np.zeros((n_coin, n_coin), dtype=np.int64)
        big[:comp4.ne, :comp4.ne] = pE
        big[comp4.ne:2 * comp4.ne, comp4.ne:2 * comp4.ne] = pE
        big[2 * comp4.ne:2 * comp4.ne + comp4.nf, 2 * comp4.ne:2 * comp4.ne + comp4.nf] = pF
        big[2 * comp4.ne + comp4.nf:, 2 * comp4.ne + comp4.nf:] = pF
        return big

    # two generators of the rotation group (closure verified exactly), then the covariance nullspace
    gen_z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=np.int64)
    gen_x = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=np.int64)
    closure = {tuple(map(tuple, np.eye(3, dtype=np.int64)))}
    frontier = [np.eye(3, dtype=np.int64)]
    while frontier:
        nxt = []
        for m in frontier:
            for g_ in (gen_z, gen_x):
                prod = g_ @ m
                key = tuple(map(tuple, prod))
                if key not in closure:
                    closure.add(key)
                    nxt.append(prod)
        frontier = nxt
    check("the 90-degree rotations about z and about x generate all 24 proper rotations (exact closure), so covariance under both is covariance under the group",
          len(closure) == 24 and closure == set(index_of.keys()))
    perm_gens = [doubled(field_rotation4(comp4, gen_z)), doubled(field_rotation4(comp4, gen_x))]
    basis_coin, consistent_coin = covariant_subspace(mats_coin, reps_coin, perm_gens)
    span_coin = [vectorize(assemble(mats_coin, vec)) for vec in basis_coin]
    curl_eb = np.zeros((n_eb, n_eb), dtype=np.int64)
    curl_eb[comp4.ne:, :comp4.ne] = comp4.curl
    curlT_eb = np.zeros((n_eb, n_eb), dtype=np.int64)
    curlT_eb[:comp4.ne, comp4.ne:] = comp4.curl.T
    onE_eb = np.zeros((n_eb, n_eb), dtype=np.int64)
    onE_eb[:comp4.ne, :comp4.ne] = np.eye(comp4.ne, dtype=np.int64)
    onF_eb = np.zeros((n_eb, n_eb), dtype=np.int64)
    onF_eb[comp4.ne:, comp4.ne:] = np.eye(comp4.nf, dtype=np.int64)
    expected_coin = [vectorize(coin_embed(m, oc, ic)) for m in (onE_eb, onF_eb, curl_eb, curlT_eb) for oc in (0, 1) for ic in (0, 1)]
    check("covariant class on the two-component payload = span{onsite E, onsite B, C, C^T} (x) M_2(R) exactly: 120 patterns, nullspace dimension 16, all sixteen expected members inside with rank 16 (the coin index is inert under rotations)",
          len(mats_coin) == 120 and consistent_coin and len(basis_coin) == 16 and all(span_contains(span_coin, v) for v in expected_coin) and rank_q(expected_coin) == 16,
          f"dim={len(basis_coin)}")
    # conservative cut: unknowns U_E (4), U_B (4), K (4), R (4); M = diag(w1,w2 on E1,E2; w3,w4 on B1,B2)
    for weights in ((1, 1, 1, 1), (1, 2, 3, 5)):
        w1, w2, w3, w4 = (Fraction(w) for w in weights)
        WE = [[w1, 0], [0, w2]]
        WB = [[w3, 0], [0, w4]]
        # linear system in the 16 unknowns ordered [U_E(4), U_B(4), K(4), R(4)] row-major
        rows_sys = []

        def idx(blockname, i, j):
            return {"UE": 0, "UB": 4, "K": 8, "R": 12}[blockname] + 2 * i + j

        # W_E U_E + U_E^T W_E = 0  (2x2 symmetric equations)
        for i in range(2):
            for j in range(2):
                row = [Fraction(0)] * 16
                row[idx("UE", i, j)] += WE[i][i]
                row[idx("UE", j, i)] += WE[j][j]
                rows_sys.append(row)
                row = [Fraction(0)] * 16
                row[idx("UB", i, j)] += WB[i][i]
                row[idx("UB", j, i)] += WB[j][j]
                rows_sys.append(row)
        # W_E R + K^T W_B = 0  (E-from-B block times C^T against B-from-E block times C)
        for i in range(2):
            for j in range(2):
                row = [Fraction(0)] * 16
                row[idx("R", i, j)] += WE[i][i]
                row[idx("K", j, i)] += WB[j][j]
                rows_sys.append(row)
        free_dim = 16 - rank_q(rows_sys)
        sol_basis = nullspace_q(rows_sys)
        # structure: diagonal onsite entries vanish; K free
        diag_zero = all(v[idx("UE", i, i)] == 0 and v[idx("UB", i, i)] == 0 for v in sol_basis for i in range(2))
        k_free = rank_q([[v[idx("K", i, j)] for i in range(2) for j in range(2)] for v in sol_basis]) == 4
        check(f"weights {weights}: the conservative cut on the sixteen-dimensional coin class leaves exactly 6 free parameters -- K (x) C free (4), one skew onsite mixing theta_E on the edges and one theta_B on the faces; every diagonal onsite entry vanishes",
              free_dim == 6 and diag_zero and k_free, f"free={free_dim}")
    # the electric rate functional on the coin payload: (U_E (x) d0^T) E; strong invariance for all charges <=> U_E = 0 <=> theta_E = 0
    ne6, nf6 = comp6.ne, comp6.nf
    theta = Fraction(3, 7)

    def complex_rate(Er, Ei, Br, Bi):
        return ([-c - theta * ei for c, ei in zip(matvec_q(comp6.curl.T, Br), Ei)],
                [-c + theta * er for c, er in zip(matvec_q(comp6.curl.T, Bi), Er)],
                [c - theta * bi for c, bi in zip(matvec_q(comp6.curl, Er), Bi)],
                [c + theta * br for c, br in zip(matvec_q(comp6.curl, Ei), Br)])

    # a random state on the double zero-charge Gauss sector for both components
    Er0 = [x + y for x, y in zip(matvec_q(comp6.curl.T, rational_vector(nf6, rng)), [Fraction(1) if comp6.edge_axis(x) == 0 else Fraction(0) for x in comp6.edges])]
    Ei0 = matvec_q(comp6.curl.T, rational_vector(nf6, rng))
    Br0 = matvec_q(comp6.curl, rational_vector(ne6, rng))
    Bi0 = [x + y for x, y in zip(matvec_q(comp6.curl, rational_vector(ne6, rng)), [Fraction(2) if comp6.face_normal(x) == 1 else Fraction(0) for x in comp6.faces])]
    on_sector = all(is_zero(matvec_q(comp6.d0.T, E_)) for E_ in (Er0, Ei0)) and all(is_zero(matvec_q(comp6.d2, B_)) for B_ in (Br0, Bi0))
    dEr, dEi, dBr, dBi = complex_rate(Er0, Ei0, Br0, Bi0)
    check("side 6: the complex law (onsite phase theta = 3/7) preserves both zero-charge Gauss rows for both components: on a random state of the double sector (with harmonic parts), d/dt(d0^T E) = 0 and d/dt(d2 B) = 0 exactly",
          on_sector and all(is_zero(matvec_q(comp6.d0.T, E_)) for E_ in (dEr, dEi)) and all(is_zero(matvec_q(comp6.d2, B_)) for B_ in (dBr, dBi)))
    # assembled real generator of the complex law: antisymmetric, radius 1, covariant, edge-to-face blocks C, two components per site
    n_c = 2 * ne6 + 2 * nf6
    gen_c = [[Fraction(0)] * n_c for _ in range(n_c)]
    for col in range(n_c):
        unit = [Fraction(0)] * n_c
        unit[col] = Fraction(1)
        parts = complex_rate(unit[:ne6], unit[ne6:2 * ne6], unit[2 * ne6:2 * ne6 + nf6], unit[2 * ne6 + nf6:])
        column = parts[0] + parts[1] + parts[2] + parts[3]
        for row in range(n_c):
            gen_c[row][col] = column[row]
    order_c = comp6.edges + comp6.edges + comp6.faces + comp6.faces

    def doubled6(p: np.ndarray) -> np.ndarray:
        pE, pF = block(p, comp6, "E", "E"), block(p, comp6, "F", "F")
        big = np.zeros((n_c, n_c), dtype=np.int64)
        big[:ne6, :ne6] = pE
        big[ne6:2 * ne6, ne6:2 * ne6] = pE
        big[2 * ne6:2 * ne6 + nf6, 2 * ne6:2 * ne6 + nf6] = pF
        big[2 * ne6 + nf6:, 2 * ne6 + nf6:] = pF
        return big

    antisym_c = all(gen_c[i][j] == -gen_c[j][i] for i in range(n_c) for j in range(n_c))
    blocks_C = (np.array_equal(int_matrix([row[:ne6] for row in gen_c[2 * ne6:2 * ne6 + nf6]]), comp6.curl)
                and np.array_equal(int_matrix([row[ne6:2 * ne6] for row in gen_c[2 * ne6 + nf6:]]), comp6.curl))
    check("side 6: the complex law's real generator is exactly antisymmetric (conserves sum |E|^2 + |B|^2), has support radius 1, is covariant under all 24 rotations in the doubled oriented law, its edge-to-face blocks are exactly C (gauge- and chain-compatible), and it carries two real components per site",
          antisym_c and support_radius(comp6, gen_c, order_c) == 1 and all(is_covariant(gen_c, doubled6(p)) for p in perms6) and blocks_C and n_c == 2 * (ne6 + nf6))
    # Kernel obstruction only to the specified pair of zero-onsite local curl copies.
    ker_theta = restricted_multiplicity(Q6, np.zeros((0, ne6), dtype=np.int64), theta * theta, ne6) + restricted_multiplicity(QF6, np.zeros((0, nf6), dtype=np.int64), theta * theta, nf6)
    ker_maxwell = (ne6 - rank_q(Q6)) + (nf6 - rank_q(QF6))
    harmonic_E = [Fraction(1) if comp6.edge_axis(x) == 0 else Fraction(0) for x in comp6.edges]
    zeros_e, zeros_f = [Fraction(0)] * ne6, [Fraction(0)] * nf6
    h_rate = complex_rate(harmonic_E, zeros_e, zeros_f, zeros_f)
    check("side 6: ker G_theta = ker(C^T C - theta^2) + ker(C C^T - theta^2) has dimension 0 (theta^2 = 9/49 is not an eigenvalue), while two decoupled copies of the one-speed law have kernel dimension 2 x 58 = 116; a harmonic edge field (a zero mode of the one-speed law) has nonzero rate theta under the complex law -- not similar to that pair of zero-onsite local curl copies",
          ker_theta == 0 and ker_maxwell == 58 and 2 * ker_maxwell == 116 and not is_zero(h_rate[1]) and h_rate[1] == [theta * v for v in harmonic_E])
    # on a charged surface the complex law rotates the charge: rate = theta J rho, modulus conserved per vertex
    E_ch_r = solve_q(comp6.d0.T, dip6)
    E_ch_i = [Fraction(0)] * ne6
    dEr_c, dEi_c, _, _ = complex_rate(E_ch_r, E_ch_i, zeros_f, zeros_f)
    rho_r, rho_i = matvec_q(comp6.d0.T, dEr_c), matvec_q(comp6.d0.T, dEi_c)
    check("side 6: on a charged electric surface (dipole) the complex law does NOT preserve the surface: d/dt(d0^T E) = theta J (d0^T E) != 0 rotates the two-component charge, and the per-vertex modulus |rho_v|^2 has zero rate (the charge rotates, it does not decay)",
          is_zero(rho_r) and rho_i == [theta * v for v in dip6] and all(2 * (a_ * b_ + c_ * d_) == 0 for a_, b_, c_, d_ in zip(dip6, rho_r, [Fraction(0)] * comp6.nv, rho_i)))
    # the K (x) C family: theta = 0, K = [[1,1],[0,1]] -- preserves every charged surface, mixes the components in the site basis
    K = [[1, 1], [0, 1]]

    def k_rate(E1, E2, B1, B2):
        # dB_c/dt = sum_d K[c][d] C E_d ; dE_d/dt = - sum_c K[c][d] C^T B_c  (R = -K^T)
        CE1, CE2 = matvec_q(comp6.curl, E1), matvec_q(comp6.curl, E2)
        CtB1, CtB2 = matvec_q(comp6.curl.T, B1), matvec_q(comp6.curl.T, B2)
        dB1 = [K[0][0] * x + K[0][1] * y for x, y in zip(CE1, CE2)]
        dB2 = [K[1][0] * x + K[1][1] * y for x, y in zip(CE1, CE2)]
        dE1 = [-(K[0][0] * x + K[1][0] * y) for x, y in zip(CtB1, CtB2)]
        dE2 = [-(K[0][1] * x + K[1][1] * y) for x, y in zip(CtB1, CtB2)]
        return dE1, dE2, dB1, dB2

    gen_k = [[Fraction(0)] * n_c for _ in range(n_c)]
    for col in range(n_c):
        unit = [Fraction(0)] * n_c
        unit[col] = Fraction(1)
        parts = k_rate(unit[:ne6], unit[ne6:2 * ne6], unit[2 * ne6:2 * ne6 + nf6], unit[2 * ne6 + nf6:])
        column = parts[0] + parts[1] + parts[2] + parts[3]
        for row in range(n_c):
            gen_k[row][col] = column[row]
    antisym_k = all(gen_k[i][j] == -gen_k[j][i] for i in range(n_c) for j in range(n_c))
    # rate functionals of both rows for both components vanish identically (every state, every charge)
    rateE_k = [matvec_q(comp6.d0.T, [gen_k[row][col] for row in range(c * ne6, (c + 1) * ne6)]) for c in (0, 1) for col in range(n_c)]
    rateM_k = [matvec_q(comp6.d2, [gen_k[row][col] for row in range(2 * ne6 + c * nf6, 2 * ne6 + (c + 1) * nf6)]) for c in (0, 1) for col in range(n_c)]
    mixes = np.array_equal(int_matrix([row[ne6:2 * ne6] for row in gen_k[2 * ne6:2 * ne6 + nf6]]), comp6.curl)
    lam_ = sp.symbols("lambda")
    KtK = sp.Matrix(K).T * sp.Matrix(K)
    charpoly = sp.expand(KtK.charpoly(lam_).as_expr())
    disc = sp.discriminant(charpoly, lam_)
    check("side 6: the K (x) C law (theta = 0, K = [[1,1],[0,1]]) is antisymmetric, radius 1, covariant, and BOTH rate functionals vanish identically for both components (every charged surface preserved); its B1-from-E2 block is C (the components mix in the site basis); K^T K has characteristic polynomial lambda^2 - 3 lambda + 1 with discriminant 5, so over R it is two decoupled copies at distinct irrational speeds",
          antisym_k and support_radius(comp6, gen_k, order_c) == 1 and all(is_covariant(gen_k, doubled6(p)) for p in perms6)
          and all(is_zero(v) for v in rateE_k) and all(is_zero(v) for v in rateM_k) and mixes
          and sp.expand(charpoly - (lam_ ** 2 - 3 * lam_ + 1)) == 0 and disc == 5 and not sp.sqrt(disc).is_rational)
    # the coin electric rate is (U_E (x) d0^T) E for a generic conservative coin member: executed on
    # theta_E = 2/3, theta_B = -1/5, K = [[1,2],[3,-1]] (unit weights, R = -K^T)
    thE, thB = Fraction(2, 3), Fraction(-1, 5)
    Kg = [[1, 2], [3, -1]]

    def coin_rate(E1, E2, B1, B2):
        CE1, CE2 = matvec_q(comp6.curl, E1), matvec_q(comp6.curl, E2)
        CtB1, CtB2 = matvec_q(comp6.curl.T, B1), matvec_q(comp6.curl.T, B2)
        dB1 = [Kg[0][0] * x + Kg[0][1] * y - thB * z for x, y, z in zip(CE1, CE2, B2)]
        dB2 = [Kg[1][0] * x + Kg[1][1] * y + thB * z for x, y, z in zip(CE1, CE2, B1)]
        dE1 = [-(Kg[0][0] * x + Kg[1][0] * y) - thE * z for x, y, z in zip(CtB1, CtB2, E2)]
        dE2 = [-(Kg[0][1] * x + Kg[1][1] * y) + thE * z for x, y, z in zip(CtB1, CtB2, E1)]
        return dE1, dE2, dB1, dB2

    gen_g = [[Fraction(0)] * n_c for _ in range(n_c)]
    for col in range(n_c):
        unit = [Fraction(0)] * n_c
        unit[col] = Fraction(1)
        parts = coin_rate(unit[:ne6], unit[ne6:2 * ne6], unit[2 * ne6:2 * ne6 + nf6], unit[2 * ne6 + nf6:])
        column = parts[0] + parts[1] + parts[2] + parts[3]
        for row in range(n_c):
            gen_g[row][col] = column[row]
    antisym_g = all(gen_g[i][j] == -gen_g[j][i] for i in range(n_c) for j in range(n_c))
    # electric rate functional: rows (component c, vertex v); expected (Theta_E (x) d0^T) on the E columns, zero on the B columns
    rateE_g = [[Fraction(0)] * n_c for _ in range(2 * comp6.nv)]
    for col in range(n_c):
        for c in (0, 1):
            img = matvec_q(comp6.d0.T, [gen_g[row][col] for row in range(c * ne6, (c + 1) * ne6)])
            for v, val in enumerate(img):
                rateE_g[c * comp6.nv + v][col] = val
    ThetaE = [[Fraction(0), -thE], [thE, Fraction(0)]]
    expected_rate = [[Fraction(0)] * n_c for _ in range(2 * comp6.nv)]
    for c in (0, 1):
        for d in (0, 1):
            if ThetaE[c][d]:
                for v in range(comp6.nv):
                    for e in range(ne6):
                        expected_rate[c * comp6.nv + v][d * ne6 + e] = ThetaE[c][d] * int(comp6.d0[e, v])
    rho_pair = dip6 + [Fraction(0)] * comp6.nv
    E_pair = solve_q(comp6.d0.T, dip6) + [Fraction(0)] * ne6
    dE1_g, dE2_g, _, _ = coin_rate(E_pair[:ne6], E_pair[ne6:], zeros_f, zeros_f)
    charged_rate = matvec_q(comp6.d0.T, dE1_g) + matvec_q(comp6.d0.T, dE2_g)
    check("side 6: for a generic conservative coin member (theta_E = 2/3, theta_B = -1/5, K = [[1,2],[3,-1]]) the electric rate functional is exactly (Theta_E (x) d0^T) E -- the coupling block contributes R (x) d0^T C^T = 0 -- so a charged surface is preserved iff theta_E = 0 (executed: on a dipole charge in component 1 the rate is theta_E (0, rho) != 0) while every zero-charge surface is preserved: the all-charge reading cuts exactly theta_E and theta_B (6 -> 4 parameters), never the second component",
          antisym_g and rateE_g == expected_rate and charged_rate[:comp6.nv] == [Fraction(0)] * comp6.nv and charged_rate[comp6.nv:] == [thE * v for v in dip6])
    # the SF-all residue K (x) C is orthogonally two decoupled one-speed copies: exact singular value decomposition of K
    # over a real algebraic extension for this unit-weight witness; with E' = (V^T (x) I) E and B' = (U^T (x) I) B the law reads
    # dB'/dt = Sigma (x) C E', dE'/dt = -Sigma (x) C^T B' -- two copies at the singular values, no coin coupling
    Ks = sp.Matrix(K)
    KtK_s = Ks.T * Ks
    sv_sq = sorted(KtK_s.eigenvals().keys(), key=sp.default_sort_key)
    right_vecs = []
    for lam_sq in sv_sq:
        vec = (KtK_s - lam_sq * sp.eye(2)).nullspace()[0]
        right_vecs.append(vec / sp.sqrt((vec.T * vec)[0, 0]))
    V_s = sp.Matrix.hstack(*right_vecs)
    Sigma_s = sp.diag(*[sp.sqrt(lam_sq) for lam_sq in sv_sq])
    U_s = Ks * V_s * Sigma_s.inv()
    orth = lambda M: all(sp.simplify(x) == 0 for x in (M.T * M - sp.eye(2)))
    check("unit-weight witness K = [[1,1],[0,1]]: exact real-algebraic orthogonal SVD U^T K V = Sigma, with distinct positive squared speeds (3 -+ sqrt 5)/2; general weights require whitening",
          orth(U_s) and orth(V_s) and all(sp.simplify(x) == 0 for x in (U_s.T * Ks * V_s - Sigma_s)) and len(sv_sq) == 2 and sp.simplify(sv_sq[0] - sv_sq[1]) != 0
          and sp.simplify(sv_sq[0] * sv_sq[1] - 1) == 0 and sp.simplify(sv_sq[0] + sv_sq[1] - 3) == 0)
    z = sp.symbols("z")
    actual_minpoly = sp.minpoly(V_s[0, 0], z)
    check("actual normalized singular-vector entry has minimal polynomial 5z^4-5z^2+1, not in Q(sqrt(5))",
          sp.expand(actual_minpoly-(5*z**4-5*z**2+1)) == 0 and sp.degree(actual_minpoly, z) == 4)
    # A nontrivial positive metric: whitening is not Euclidean orthogonal.
    WE_s, WB_s = sp.diag(1, 4), sp.diag(9, 16)
    SE, SB = sp.diag(1, 2), sp.diag(3, 4)
    K_weighted = SB.inv()*Ks*SE  # its whitened coupling is the already checked Ks
    R_weighted = -WE_s.inv()*K_weighted.T*WB_s
    TE, TB = V_s.T*SE, U_s.T*SB
    zero = lambda mat: all(sp.simplify(x) == 0 for x in mat)
    check("nontrivial positive weights: whitening followed by orthogonal SVD is a metric isometry in original coordinates",
          zero(TB*K_weighted*SE.inv()*V_s-Sigma_s) and zero(TE*R_weighted*SB.inv()*U_s+Sigma_s)
          and zero(TE*SE.inv()*V_s-sp.eye(2)) and zero(TB*SB.inv()*U_s-sp.eye(2))
          and zero(TE.T*TE-WE_s) and zero(TB.T*TB-WB_s)
          and not zero(TE.T*TE-sp.eye(2)))
    check("general all-charge K can have equal or zero singular values; distinct positive speeds belong only to the explicit witness",
          (sp.eye(2).T*sp.eye(2)).eigenvals() == {sp.Integer(1): 2}
          and sp.diag(1, 0).rank() == 1)
    J = sp.Matrix([[0, -1], [1, 0]])
    omega, th = sp.symbols("omega theta", real=True)
    modal = omega*sp.kronecker_product(J, sp.eye(2))+th*sp.kronecker_product(sp.eye(2), J)
    O = sp.Matrix.hstack(sp.Matrix([1,0,0,1]), sp.Matrix([0,-1,1,0]),
                        sp.Matrix([1,0,0,-1]), sp.Matrix([0,1,1,0]))/sp.sqrt(2)
    reduced = sp.simplify(O.T*modal*O)
    check("a general real mode basis decouples the onsite-phase tensor mode into oscillator blocks omega-theta and omega+theta",
          O.T*O == sp.eye(4) and reduced == sp.diag((omega-th)*J, (omega+th)*J))
    # the Qubit capacity bound, executed here (checker finding CK-03): dim_R M_2(C) = 8 as the rank of the real coordinate basis
    real_coords = []
    for i in range(2):
        for j in range(2):
            for part in (0, 1):
                vec = [Fraction(0)] * 8
                vec[2 * (2 * i + j) + part] = Fraction(1)
                real_coords.append(vec)
    real_dim_m2c = rank_q(real_coords)
    check("dim_R M_2(C) = 8 (rank of the real coordinate basis: real and imaginary parts of the four matrix units): a two-component coin payload fits the one-site domain's capacity, a nine-component linear payload cannot (route R7 of the gate, executed here)",
          real_dim_m2c == 8 and 2 <= real_dim_m2c and 9 > real_dim_m2c)

    # ---------------------------------------------------------------- K
    section("K. Hidden time: the complex law is second order on its physical pair (side 6)")
    GM = member(comp6, q=1, r=-1)  # the one-speed law on the (phi, E, B, psi) state with phi, psi inert
    z1 = state(comp6, [Fraction(0)] * comp6.nv, rational_vector(ne6, rng), rational_vector(nf6, rng), [Fraction(0)] * comp6.nc)
    z2 = state(comp6, [Fraction(0)] * comp6.nv, rational_vector(ne6, rng), rational_vector(nf6, rng), [Fraction(0)] * comp6.nc)
    z1_dot = [x - theta * y for x, y in zip(apply(GM, z1), z2)]
    z2_dot = [x + theta * y for x, y in zip(apply(GM, z2), z1)]
    z1_ddot = [x - theta * y for x, y in zip(apply(GM, z1_dot), z2_dot)]
    rhs = [2 * x - y - theta * theta * z for x, y, z in zip(apply(GM, z1_dot), apply(GM, apply(GM, z1)), z1)]
    recovered = [(x - y) / theta for x, y in zip(apply(GM, z1), z1_dot)]
    check("z1'' = 2 G z1' - (G^2 + theta^2) z1 exactly on a random state: the physical pair (E1, B1) obeys a closed second-order law, and the enlarged payload is its time derivative, z2 = (G z1 - z1') / theta",
          z1_ddot == rhs and recovered == z2)
    GM_i = int_matrix(GM)
    GM2 = GM_i @ GM_i
    radius2 = max(comp6.distance(comp6.order[i], comp6.order[j]) for i, j in zip(*np.nonzero(GM2)) if i != j)
    check("the second-order law is not nearest-neighbor: G^2 has support radius exactly 2 (C^T C reads edges at distance two) -- the hidden time payload trades locality for an extra coin, and at the linear level it IS an extra coin",
          radius2 == 2)

    # ---------------------------------------------------------------- L
    section("L. Item 5's notion on the minimal payload against the constraint-surface notion used here (side 6)")
    minimal_general = member(comp6, uE=Fraction(1, 3), uB=Fraction(-2, 5), q=Fraction(7, 2), r=Fraction(-1, 4))
    RM_min = gauss_rate_matrix(comp6, minimal_general, "M")
    e_block = [row[comp6.offE:comp6.offF] for row in RM_min]
    f_block = [row[comp6.offF:comp6.offC] for row in RM_min]
    check("on the minimal (E, B) payload the magnetic rate functional is u_B (d2 B) exactly: the coupling contributes q d2 C = 0 identically, so 'preserves the magnetic Gauss row' as an identity (d2 L = 0) and as surface invariance coincide on the coupling block; the surface reading additionally cuts u_B only when rho_C != 0",
          all(is_zero(row) for row in e_block) and frac_matrix_equal(f_block, [[Fraction(-2, 5) * int(v) for v in row] for row in comp6.d2]))

    # ---------------------------------------------------------------- M
    section("M. Resolution certificate")
    print("per_element: executed — every coefficient of the 56-pattern four-role basis and of the 120-pattern coin basis is classified exactly under the rotation group, and every Gauss-rate contribution matrix is computed coefficient by coefficient")
    print("per_site: executed — every site of the side-4 and side-6 compiled tori is role-censused and shell-counted; the vertex payload's rate is evaluated vertex by vertex (delta states, dipole charges) and shown frozen or drifting exactly")
    print("per_mode: executed — exact eigenvalue multiplicities on the side-6 torus certify two transverse branches per nonzero momentum on the Gauss sector and the longitudinal and cube branches off it; kernel dimensions 0 and 116 exclude only the specified two zero-onsite curl copies")
    print("per_block: executed — the vertex, edge, face and cube blocks of the rate functionals, of -G^2 and of every witness generator are checked separately (chain identities, skewness, covariance, support radius)")
    print("lattice_wide: executed — the specified three-speed invariant-subspace/sector and dipole tests are decided exactly on the whole side-4 and side-6 tori; no infinite-volume or continuum statement is executed")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
