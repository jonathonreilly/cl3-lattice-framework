#!/usr/bin/env python3
"""Exact finite adjudication of supplied edge/face linear-generator premises.

The canonical note defines items 1--7, including the load-bearing real-linear
first-order generator premise 2L in both conditional redundancy directions.
Nondegenerate classification/stabilizer claims use positive even side >= 4;
side 2 is retained only as a degenerate countercontrol. The parity compilation,
orientation, time law, metric and payload are supplied mathematical structures.
This runner proves no formal independence from the four axioms.

Original exact classification, conservation, chain, covariance, spectrum and
alternative-law checks are retained. Alternatives can relax several bundled
premises. The ordered conditional-mean sweep is deterministic relaxation, not
an Admissibility sampler or a derived diffusive process. Each tick shear has
radius one, while the complete tick has radius three and a non-onsite conserved
modified metric; it differs from exp(h G) for the original generator without
excluding other flow embeddings. The nonlinear witness conserves a quartic
energy, not the declared diagonal quadratic form.

Runtime read: the approved axiom memo (verbatim textual checks). The canonical
note is additionally pinned as the claim/proof scope of this receipt; its text
is not executed. All mathematical constructions are local to this runner;
NumPy/SymPy and the standard library are the only software imports.
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
                     "docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md")

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
# exact linear algebra over Q (own implementation; independent of every member)
# ---------------------------------------------------------------------------


def frac_rows(matrix) -> list[list[Fraction]]:
    return [[Fraction(int(v)) if not isinstance(v, Fraction) else v for v in row] for row in matrix]


def rank_q(matrix) -> int:
    rows = frac_rows(matrix)
    if not rows:
        return 0
    ncols = len(rows[0])
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
                rows[r] = [a - factor * b for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def nullspace_q(matrix) -> list[list[Fraction]]:
    rows = frac_rows(matrix)
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
                rows[r] = [a - factor * b for a, b in zip(rows[r], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        vec = [Fraction(0)] * ncols
        vec[f] = Fraction(1)
        for r, p in enumerate(pivots):
            vec[p] = -rows[r][f]
        basis.append(vec)
    return basis


def matvec_q(matrix: np.ndarray, vec: list[Fraction]) -> list[Fraction]:
    out = []
    for row in matrix:
        acc = Fraction(0)
        for coeff, value in zip(row.tolist(), vec):
            if coeff:
                acc += coeff * value
        out.append(acc)
    return out


def dot_q(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def rational_vector(n: int, rng: random.Random) -> list[Fraction]:
    return [Fraction(rng.randint(-9, 9), rng.randint(1, 5)) for _ in range(n)]


# ---------------------------------------------------------------------------
# the supplied role compilation: parity roles on the even torus (sector 0)
# ---------------------------------------------------------------------------

AXES = (0, 1, 2)
UNIT = {0: (1, 0, 0), 1: (0, 1, 0), 2: (0, 0, 1)}
# face normal k and the ordered plane pair (i, j) with e_i x e_j = e_k
CYCLIC = {2: (0, 1), 0: (1, 2), 1: (2, 0)}


class Compilation:
    """Physical torus of even side, roles by coordinate parity (sector 0)."""

    def __init__(self, side: int) -> None:
        assert isinstance(side, int) and side >= 2 and side % 2 == 0, "positive even side >= 2; structural theorems require >= 4"
        self.side = side
        self.sites = list(itertools.product(range(side), repeat=3))
        self.vertices, self.edges, self.faces, self.cubes = [], [], [], []
        for x in self.sites:
            bits = tuple(c % 2 for c in x)
            w = sum(bits)
            if w == 0:
                self.vertices.append(x)
            elif w == 1:
                self.edges.append(x)
            elif w == 2:
                self.faces.append(x)
            else:
                self.cubes.append(x)
        self.vidx = {x: i for i, x in enumerate(self.vertices)}
        self.eidx = {x: i for i, x in enumerate(self.edges)}
        self.fidx = {x: i for i, x in enumerate(self.faces)}
        self.cidx = {x: i for i, x in enumerate(self.cubes)}
        self.d0 = self._gradient()
        self.curl = self._curl(signed=True)
        self.unsigned = self._curl(signed=False)
        self.d2 = self._divergence()

    # geometry -----------------------------------------------------------
    def shift(self, x, axis: int, step: int):
        y = list(x)
        y[axis] = (y[axis] + step) % self.side
        return tuple(y)

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

    # incidence ----------------------------------------------------------
    def _gradient(self) -> np.ndarray:
        m = np.zeros((len(self.edges), len(self.vertices)), dtype=np.int64)
        for e, x in enumerate(self.edges):
            i = self.edge_axis(x)
            m[e, self.vidx[self.shift(x, i, 1)]] += 1
            m[e, self.vidx[self.shift(x, i, -1)]] -= 1
        return m

    def face_stencil(self, x, signed: bool) -> list[tuple[tuple[int, int, int], int]]:
        """Boundary edges of face x with the oriented-curl signs (or all +1)."""
        k = self.face_normal(x)
        i, j = CYCLIC[k]
        entries = [
            (self.shift(x, j, -1), 1),   # E_i at x - e_j
            (self.shift(x, j, 1), -1),   # E_i at x + e_j
            (self.shift(x, i, 1), 1),    # E_j at x + e_i
            (self.shift(x, i, -1), -1),  # E_j at x - e_i
        ]
        if not signed:
            entries = [(site, 1) for site, _ in entries]
        return entries

    def _curl(self, signed: bool) -> np.ndarray:
        m = np.zeros((len(self.faces), len(self.edges)), dtype=np.int64)
        for f, x in enumerate(self.faces):
            for site, sign in self.face_stencil(x, signed):
                m[f, self.eidx[site]] += sign
        return m

    def _divergence(self) -> np.ndarray:
        m = np.zeros((len(self.cubes), len(self.faces)), dtype=np.int64)
        for c, x in enumerate(self.cubes):
            for k in AXES:
                m[c, self.fidx[self.shift(x, k, 1)]] += 1
                m[c, self.fidx[self.shift(x, k, -1)]] -= 1
        return m


# ---------------------------------------------------------------------------
# proper cubic rotations and the field representations
# ---------------------------------------------------------------------------


def proper_rotations() -> list[np.ndarray]:
    out = []
    for perm in itertools.permutations(AXES):
        for signs in itertools.product((1, -1), repeat=3):
            m = np.zeros((3, 3), dtype=np.int64)
            for col, (row, s) in enumerate(zip(perm, signs)):
                m[row, col] = s
            if round(np.linalg.det(m)) == 1:
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


# A real one-component payload on the edge (face) sites carries a signed
# permutation representation of the lattice symmetries; every such
# representation is induced from a character of the site stabilizer (a D_4),
# and the four characters are realized by tensor transport:
#   edge: sigma_a = sign of the transported edge axis (vector component),
#         sigma_t = sign of the transported transverse quadratic form
#                   x_j^2 - x_k^2, (j, k) = CYCLIC[axis];
#   face: sigma_n = sign of the transported normal (vector component),
#         sigma_d = sign of the transported in-plane quadratic form
#                   x_i^2 - x_j^2, (i, j) = CYCLIC[normal].
# A character is (alpha, beta) with sign = sigma_(a|n)^alpha * sigma_(t|d)^beta.
ORIENTED = (1, 0)   # vector component (oriented link value / oriented face value)
SCALAR = (0, 0)     # unoriented value
CHARACTERS = tuple(itertools.product((0, 1), repeat=2))


def edge_sign(rot: np.ndarray, axis: int, char: tuple[int, int]) -> int:
    new_axis, sigma_a = image_axis_sign(rot, axis)
    j, _k = CYCLIC[axis]
    j_image, _ = image_axis_sign(rot, j)
    sigma_t = 1 if j_image == CYCLIC[new_axis][0] else -1
    return (sigma_a ** char[0]) * (sigma_t ** char[1])


def face_sign(rot: np.ndarray, normal: int, char: tuple[int, int]) -> int:
    new_normal, sigma_n = image_axis_sign(rot, normal)
    i, _j = CYCLIC[normal]
    i_image, _ = image_axis_sign(rot, i)
    sigma_d = 1 if i_image == CYCLIC[new_normal][0] else -1
    return (sigma_n ** char[0]) * (sigma_d ** char[1])


def field_rotation(comp: Compilation, rot: np.ndarray, e_char: tuple[int, int],
                   b_char: tuple[int, int], with_vertex: bool = False) -> np.ndarray:
    """Signed permutation matrix on the field vector (rotation about the origin).

    Field order: [phi at vertices (optional, scalar)] + E at edges + B at faces.
    """
    ne, nf, nv = len(comp.edges), len(comp.faces), len(comp.vertices)
    off_v = nv if with_vertex else 0
    n = off_v + ne + nf
    m = np.zeros((n, n), dtype=np.int64)
    if with_vertex:
        for v, x in enumerate(comp.vertices):
            m[comp.vidx[rotate_site(comp, rot, x)], v] = 1
    for e, x in enumerate(comp.edges):
        m[off_v + comp.eidx[rotate_site(comp, rot, x)], off_v + e] = edge_sign(rot, comp.edge_axis(x), e_char)
    for f, x in enumerate(comp.faces):
        m[off_v + ne + comp.fidx[rotate_site(comp, rot, x)], off_v + ne + f] = face_sign(rot, comp.face_normal(x), b_char)
    return m


def translation(comp: Compilation, shift, with_vertex: bool = False) -> np.ndarray:
    """Permutation of the field vector under a lattice translation (even shifts keep the sector)."""
    ne, nf, nv = len(comp.edges), len(comp.faces), len(comp.vertices)
    off_v = nv if with_vertex else 0
    n = off_v + ne + nf
    m = np.zeros((n, n), dtype=np.int64)

    def moved(x):
        return tuple((a + b) % comp.side for a, b in zip(x, shift))

    if with_vertex:
        for v, x in enumerate(comp.vertices):
            m[comp.vidx[moved(x)], v] = 1
    for e, x in enumerate(comp.edges):
        m[off_v + comp.eidx[moved(x)], off_v + e] = 1
    for f, x in enumerate(comp.faces):
        m[off_v + ne + comp.fidx[moved(x)], off_v + ne + f] = 1
    return m


# ---------------------------------------------------------------------------
# generic tools for a real linear law on the (E, B) payload
# ---------------------------------------------------------------------------


def block_generator(comp: Compilation, u: Fraction, v: Fraction, edge_from_face: np.ndarray,
                    face_from_edge: np.ndarray, scale_ef: Fraction = Fraction(1),
                    scale_fe: Fraction = Fraction(1)):
    """Exact generator as a list of Fraction rows: [[u I, scale_ef*EF],[scale_fe*FE, v I]]."""
    ne, nf = len(comp.edges), len(comp.faces)
    n = ne + nf
    g = [[Fraction(0)] * n for _ in range(n)]
    for e in range(ne):
        g[e][e] = u
        for f in range(nf):
            val = int(edge_from_face[e, f])
            if val:
                g[e][ne + f] = scale_ef * val
    for f in range(nf):
        g[ne + f][ne + f] = v
        for e in range(ne):
            val = int(face_from_edge[f, e])
            if val:
                g[ne + f][e] = scale_fe * val
    return g


def apply(g, vec: list[Fraction]) -> list[Fraction]:
    return [dot_q(row, vec) for row in g]


def support_radius(comp: Compilation, g, with_vertex: bool = False) -> int:
    """Largest torus distance between two sites coupled by a nonzero generator entry."""
    order = (comp.vertices if with_vertex else []) + comp.edges + comp.faces
    worst = 0
    for r, row in enumerate(g):
        for c, val in enumerate(row):
            if val != 0 and r != c:
                worst = max(worst, comp.distance(order[r], order[c]))
    return worst


def is_covariant(g, perm: np.ndarray) -> bool:
    """Exact test perm * g * perm^T == g for a signed permutation perm."""
    n = len(g)
    # perm is a signed permutation: image[c] = (row, sign)
    image = {}
    for c in range(n):
        rows = np.nonzero(perm[:, c])[0]
        image[c] = (int(rows[0]), int(perm[rows[0], c]))
    for r in range(n):
        ir, sr = image[r]
        for c in range(n):
            ic, sc = image[c]
            if g[ir][ic] != sr * sc * g[r][c]:
                return False
    return True


def energy_derivative(g, vec: list[Fraction], w_e: Fraction, w_b: Fraction, ne: int) -> Fraction:
    rate = apply(g, vec)
    return sum((w_e if i < ne else w_b) * vec[i] * rate[i] for i in range(len(vec)))


def metric_skew_defect(g, w_e: Fraction, w_b: Fraction, ne: int) -> Fraction:
    """Sum of |(M G + G^T M)_ij| for M = diag(w_e I, w_b I); zero iff energy is conserved."""
    n = len(g)
    total = Fraction(0)
    for i in range(n):
        wi = w_e if i < ne else w_b
        for j in range(n):
            wj = w_e if j < ne else w_b
            total += abs(wi * g[i][j] + wj * g[j][i])
    return total


def int_matrix(g) -> np.ndarray:
    return np.array([[int(v) for v in row] for row in g], dtype=np.int64)


def torus_momentum_count(side: int) -> int:
    coarse = side // 2
    return coarse ** 3 - 1


# ---------------------------------------------------------------------------
# covariant classification of nearest-neighbor real linear generators
# ---------------------------------------------------------------------------


def nn_basis(comp: Compilation, with_vertex: bool):
    """Translation-covariant nearest-neighbor generator patterns on the payload.

    Returns (labels, matrices, representatives) where each pattern is one
    (role type, axis label, relative offset) family with unit coefficient at
    every translate; representatives are (row, col) index pairs used to read a
    pattern's coefficient off any translation-covariant nearest-neighbor matrix.
    """
    ne, nf, nv = len(comp.edges), len(comp.faces), len(comp.vertices)
    off_v = nv if with_vertex else 0
    n = off_v + ne + nf
    labels, mats, reps = [], [], []

    def add(label, entries):
        m = np.zeros((n, n), dtype=np.int64)
        for r, c in entries:
            m[r, c] += 1
        labels.append(label)
        mats.append(m)
        reps.append(entries[0])

    for a in AXES:
        add(("edge_onsite", a), [(off_v + e, off_v + e) for e, x in enumerate(comp.edges) if comp.edge_axis(x) == a])
        for b in AXES:
            if b == a:
                continue
            for s in (1, -1):
                add(("edge_from_face", a, b, s),
                    [(off_v + e, off_v + ne + comp.fidx[comp.shift(x, b, s)])
                     for e, x in enumerate(comp.edges) if comp.edge_axis(x) == a])
        if with_vertex:
            for s in (1, -1):
                add(("edge_from_vertex", a, s),
                    [(off_v + e, comp.vidx[comp.shift(x, a, s)])
                     for e, x in enumerate(comp.edges) if comp.edge_axis(x) == a])
    for k in AXES:
        i, j = CYCLIC[k]
        add(("face_onsite", k), [(off_v + ne + f, off_v + ne + f) for f, x in enumerate(comp.faces) if comp.face_normal(x) == k])
        for c in (i, j):
            for s in (1, -1):
                add(("face_from_edge", k, c, s),
                    [(off_v + ne + f, off_v + comp.eidx[comp.shift(x, c, s)])
                     for f, x in enumerate(comp.faces) if comp.face_normal(x) == k])
    if with_vertex:
        add(("vertex_onsite",), [(v, v) for v in range(nv)])
        for a in AXES:
            for s in (1, -1):
                add(("vertex_from_edge", a, s),
                    [(v, off_v + comp.eidx[comp.shift(x, a, s)]) for v, x in enumerate(comp.vertices)])
    return labels, mats, reps


def covariant_subspace(comp: Compilation, e_char: tuple[int, int], b_char: tuple[int, int],
                       with_vertex: bool = False):
    """Exact nullspace of the rotation-covariance constraints on the pattern coefficients."""
    labels, mats, reps = nn_basis(comp, with_vertex)
    rows = []
    consistent = True
    for rot in proper_rotations():
        perm = field_rotation(comp, rot, e_char, b_char, with_vertex)
        for i, mat in enumerate(mats):
            conj = perm @ mat @ perm.T
            coeffs = [int(conj[r, c]) for (r, c) in reps]
            rebuilt = sum((coef * m for coef, m in zip(coeffs, mats)), np.zeros_like(conj))
            consistent = consistent and bool(np.array_equal(rebuilt, conj))
            rows.append((i, coeffs))
    # assemble the linear system A theta = 0 with A[(rot,j), i] = c_{rot,i,j} - delta_{ij}
    nrot = 24
    npat = len(mats)
    system = []
    for r in range(nrot):
        block = rows[r * npat:(r + 1) * npat]
        for j in range(npat):
            row = [Fraction(0)] * npat
            for i, coeffs in block:
                row[i] += coeffs[j]
            row[j] -= 1
            system.append(row)
    basis = nullspace_q(system)
    return labels, mats, basis, consistent


def span_contains(basis_vectors: list[list[Fraction]], target: list[Fraction]) -> bool:
    return rank_q(basis_vectors + [target]) == rank_q(basis_vectors)


def vectorize(mat) -> list[Fraction]:
    return [Fraction(int(v)) for v in np.asarray(mat).ravel().tolist()]


def assemble(mats, coeffs: list[Fraction]) -> np.ndarray:
    total = np.zeros_like(mats[0])
    for coef, m in zip(coeffs, mats):
        if coef:
            assert coef.denominator == 1
            total = total + int(coef) * m
    return total


def block_matrix(comp: Compilation, edge_from_face: np.ndarray, face_from_edge: np.ndarray,
                 u: int = 0, v: int = 0) -> np.ndarray:
    ne, nf = len(comp.edges), len(comp.faces)
    m = np.zeros((ne + nf, ne + nf), dtype=np.int64)
    m[:ne, :ne] = u * np.eye(ne, dtype=np.int64)
    m[ne:, ne:] = v * np.eye(nf, dtype=np.int64)
    m[:ne, ne:] = edge_from_face
    m[ne:, :ne] = face_from_edge
    return m


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def conditional_mean_sweep(Q, values):
    """Ordered deterministic coordinate minimizers; no Gaussian draws."""
    out = list(values)
    for e in range(len(out)):
        acc = sum((int(Q[e, j]) * out[j] for j in range(len(out)) if j != e and Q[e, j]), Fraction(0))
        out[e] = -acc / int(Q[e, e])
    return out


def main() -> int:
    print("U(1) dynamics class against the four axioms: per-item adjudication (exact)")
    print("=" * 76)
    rng = random.Random(20260905)

    # ---------------------------------------------------------------- A
    section("A. Axiom memo runtime read (canonical note additionally pinned for claim scope)")
    memo = (ROOT / AXIOM_REL).read_text(encoding="utf-8")
    sentences = {
        "lattice sites": "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor\nadjacency, standard translations, and proper cubic rotations about each site.",
        "no site privileged": "No site is privileged. Sites are distinguished by the supplied lattice\nstructure alone.",
        "qubit domain": "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "no possibility privileged": "No possibility is privileged. Possibilities are distinguished by the supplied\nalgebraic structure alone.",
        "one fixed covariant rule": "There is one fixed nearest-neighbor admissibility rule, covariant under lattice\ntranslations and proper cubic rotations.",
        "distribution sentence": "For each site, the probability distribution over the possibilities is\ndetermined by, and varies with, the nearest-neighbor conditions.",
        "records form": "Records form.",
        "one record, permanent": "A\nsite never carries more than one record; records are permanent.",
        "readout": "Only records are readable. A readout value is determined by record content\nalone. A site with no record cannot be read.",
        "law sentence": "A law privileges no states. Its domain is a supplied condition, and at every\nstate where the condition holds it gives exactly one answer.",
        "not a dynamics axiom": "Admissibility is not a dynamics axiom.",
        "no Hamiltonian / time metric": "choose a Hamiltonian or transfer operator, supply transition-probability or\nweight values, select a scalar or nonzero kinetic branch, assert a Dirac-square\ncarrier, define a time metric, or provide a record-production process or\nphysical persistence dynamics.",
        "open gates: time": "arrow, record-production dynamics, physical persistence dynamics, time metric,\n  and local observability of records;",
        "2026-08-13 removal": "The 2026-08-13 owner-approved revision removed the named scalar functional\n`I`, finite additivity over disjoint record collections, and `I(empty)=0` from\nRecord.",
    }
    for name, text in sentences.items():
        check(f"memo carries verbatim: {name}", text in memo)

    # ---------------------------------------------------------------- B
    section("B. The supplied compilation: parity roles, doubled incidence (sides 4, 6)")
    comps = {side: Compilation(side) for side in (4, 6, 8)}
    for side in (4, 6):
        comp = comps[side]
        n = side ** 3
        coarse = (side // 2) ** 3
        check(f"side {side}: role census vertices/edges/faces/cubes = {coarse}/{3*coarse}/{3*coarse}/{coarse}",
              (len(comp.vertices), len(comp.edges), len(comp.faces), len(comp.cubes)) == (coarse, 3 * coarse, 3 * coarse, coarse)
              and len(comp.sites) == n)
        census_ok = True
        same_role_pair = False
        for x in comp.sites:
            kinds = [comp.weight(y) for y in comp.neighbors(x)]
            w = comp.weight(x)
            if w == 1:
                census_ok = census_ok and kinds.count(0) == 2 and kinds.count(2) == 4
            if w == 2:
                census_ok = census_ok and kinds.count(1) == 4 and kinds.count(3) == 2
            if w == 0:
                census_ok = census_ok and kinds.count(1) == 6
            if w == 3:
                census_ok = census_ok and kinds.count(2) == 6
            same_role_pair = same_role_pair or (w in kinds)
        check(f"side {side}: edge shell = 2 vertices + 4 faces; face shell = 4 edges + 2 cubes; vertex/cube shells", census_ok)
        check(f"side {side}: no same-role nearest-neighbor pair exists (compilation fact)", not same_role_pair)
        parity_ok = all(comp.distance(x, y) % 2 == 1 for x in comp.edges for y in comp.faces) and \
            all(comp.distance(x, y) % 2 == 0 for x in comp.edges for y in comp.edges) and \
            all(comp.distance(x, y) % 2 == 0 for x in comp.faces for y in comp.faces)
        check(f"side {side}: edge-face torus distances are all odd; same-role distances all even (parity theorem)", parity_ok)
    comp4 = comps[4]
    # the eight sector translates satisfy the neighbor-flip rule; propagation from the origin fixes the sector
    sectors_ok = True
    for s in itertools.product((0, 1), repeat=3):
        role = {x: tuple((c % 2) ^ b for c, b in zip(x, s)) for x in comp4.sites}
        for x in comp4.sites:
            for i in AXES:
                for step in (1, -1):
                    y = comp4.shift(x, i, step)
                    expect = tuple(role[x][a] ^ (1 if a == i else 0) for a in AXES)
                    sectors_ok = sectors_ok and role[y] == expect
    check("all eight parity translates satisfy the neighbor bit-flip rule (translation permutes sectors)", sectors_ok)
    # rotations about a site of each role type: sector-0 preserved or mapped to another sector
    preserve_counts = {}
    mapped_to_sector = True
    for name, center in (("vertex", (0, 0, 0)), ("edge_x", (1, 0, 0)), ("face_xy", (1, 1, 0)), ("cube", (1, 1, 1))):
        kept = 0
        for rot in proper_rotations():
            image_role = {}
            for x in comp4.sites:
                y = rotate_site(comp4, rot, x, center)
                # relabel the role bits by the rotation's axis permutation
                bits = [x[a] % 2 for a in AXES]
                new_bits = [0, 0, 0]
                for a in AXES:
                    j, _ = image_axis_sign(rot, a)
                    new_bits[j] = bits[a]
                image_role[y] = tuple(new_bits)
            # which sector is the image role field?
            found = None
            for s in itertools.product((0, 1), repeat=3):
                if all(image_role[y] == tuple((c % 2) ^ b for c, b in zip(y, s)) for y in comp4.sites):
                    found = s
            mapped_to_sector = mapped_to_sector and found is not None
            if found == (0, 0, 0):
                kept += 1
        preserve_counts[name] = kept
    check("every proper rotation about every role type maps the role field onto one of the eight sectors",
          mapped_to_sector)
    check("rotations about a vertex or cube site fix the sector (24 each); about an edge or face site exactly 8 do",
          preserve_counts == {"vertex": 24, "edge_x": 8, "face_xy": 8, "cube": 24}, preserve_counts)

    # ---------------------------------------------------------------- C
    section("C. Incidence of the compilation: exact chain identities and covariance")
    for side in (4, 6, 8):
        comp = comps[side]
        check(f"side {side}: C d0 = 0 and d2 C = 0 over the integers",
              not np.any(comp.curl @ comp.d0) and not np.any(comp.d2 @ comp.curl))
        rows_ok = all(sorted(row[row != 0].tolist()) == [-1, -1, 1, 1] for row in comp.curl)
        cols_ok = all(sorted(col[col != 0].tolist()) == [-1, -1, 1, 1] for col in comp.curl.T)
        check(f"side {side}: every face row and every edge column of the oriented curl has entries (+1,+1,-1,-1)", rows_ok and cols_ok)
        nn_ok = all(comp.distance(comp.faces[f], comp.edges[e]) == 1
                    for f, e in zip(*np.nonzero(comp.curl)))
        check(f"side {side}: every curl entry couples a face to a physical nearest-neighbor edge", nn_ok)
    comp = comps[4]
    rots = proper_rotations()
    cov_c = all(np.array_equal(field_rotation(comp, r, ORIENTED, ORIENTED)[len(comp.edges):, len(comp.edges):] @ comp.curl
                               @ field_rotation(comp, r, ORIENTED, ORIENTED)[:len(comp.edges), :len(comp.edges)].T, comp.curl) for r in rots)
    check("oriented curl is covariant under all 24 proper rotations about a vertex (vector E, vector B)", cov_c)
    cov_s = all(np.array_equal(field_rotation(comp, r, SCALAR, SCALAR)[len(comp.edges):, len(comp.edges):] @ comp.unsigned
                               @ field_rotation(comp, r, SCALAR, SCALAR)[:len(comp.edges), :len(comp.edges)].T, comp.unsigned) for r in rots)
    check("unsigned incidence is covariant under all 24 proper rotations (scalar E, scalar B)", cov_s)
    cov_d0 = all(np.array_equal(field_rotation(comp, r, ORIENTED, ORIENTED, True)[len(comp.vertices):len(comp.vertices) + len(comp.edges), len(comp.vertices):len(comp.vertices) + len(comp.edges)] @ comp.d0
                                @ field_rotation(comp, r, ORIENTED, ORIENTED, True)[:len(comp.vertices), :len(comp.vertices)].T, comp.d0) for r in rots)
    check("oriented gradient d0 is covariant under all 24 proper rotations (scalar vertex payload)", cov_d0)
    group_ok = True
    for e_char in CHARACTERS:
        for b_char in CHARACTERS:
            reps_ = {tuple(map(tuple, r)): field_rotation(comp, r, e_char, b_char) for r in rots}
            for r1 in rots:
                for r2 in rots:
                    prod = r1 @ r2
                    group_ok = group_ok and np.array_equal(reps_[tuple(map(tuple, prod))], reps_[tuple(map(tuple, r1))] @ reps_[tuple(map(tuple, r2))])
    check("all 16 signed-permutation payload representations are genuine group representations (composition law on 24 x 24 pairs)", group_ok)

    def axis_parity(rot: np.ndarray) -> int:
        perm = [image_axis_sign(rot, a)[0] for a in AXES]
        inversions = sum(1 for a in range(3) for b in range(a + 1, 3) if perm[a] > perm[b])
        return -1 if inversions % 2 else 1

    global_char = all(
        edge_sign(r, a, (0, 1)) == axis_parity(r) and face_sign(r, a, (0, 1)) == axis_parity(r)
        for r in rots for a in AXES
    ) and all(axis_parity(r1 @ r2) == axis_parity(r1) * axis_parity(r2) for r1 in rots for r2 in rots)
    check("the second character factor is one global sign character of the rotation group (parity of the axis permutation), the same for every edge and face",
          global_char)
    even_ok = True
    for shift in itertools.product((0, 2), repeat=3):
        t = translation(comp, shift)
        ne = len(comp.edges)
        even_ok = even_ok and np.array_equal(t[ne:, ne:] @ comp.curl @ t[:ne, :ne].T, comp.curl)
    check("oriented curl is covariant under all eight even translations of the side-4 torus", even_ok)

    # ---------------------------------------------------------------- D
    section("D. One-face stabilizer: the 90-degree rotation about a face-role site")
    # boundary of the xy-face at c=(1,1,0): values (a,b,c,d) at sites c-e_y, c+e_x, c+e_y, c-e_x
    # (E_x, E_y, E_x, E_y).  The eight sector-preserving proper rotations about c form the D_4
    # stabilizer; a stencil x is covariant iff x^T A_R = sigma_B(R) x^T for each of them.
    center = (1, 1, 0)
    boundary = [comp4.shift(center, 1, -1), comp4.shift(center, 0, 1), comp4.shift(center, 1, 1), comp4.shift(center, 0, -1)]
    stabilizer = [r for r in proper_rotations() if rotate_site(comp4, r, center, center) == center
                  and all(comp4.weight(rotate_site(comp4, r, x, center)) == comp4.weight(x) for x in comp4.sites)]
    check("the sector-preserving stabilizer of a face-role site has exactly eight proper rotations (D_4), all named by the Lattice axiom", len(stabilizer) == 8)
    stencil_by_char = {}
    for e_char in CHARACTERS:
        for b_char in CHARACTERS:
            system = []
            for rot in stabilizer:
                action = [[0] * 4 for _ in range(4)]   # value at image position = sign * value at source
                for src, x in enumerate(boundary):
                    y = rotate_site(comp4, rot, x, center)
                    dst = boundary.index(y)
                    action[dst][src] = edge_sign(rot, comp4.edge_axis(x), e_char)
                sigma_b = face_sign(rot, 2, b_char)
                # x^T A = sigma_b x^T  <=>  (A^T - sigma_b I) x = 0
                for r_ in range(4):
                    system.append([Fraction(action[c_][r_]) - (Fraction(sigma_b) if r_ == c_ else 0) for c_ in range(4)])
            basis = nullspace_q(system)
            stencil_by_char[(e_char, b_char)] = basis
    expected_stencils = {
        (ORIENTED, ORIENTED): (1, 1, -1, -1),   # oriented curl: E_x(c-e_y) + E_y(c+e_x) - E_x(c+e_y) - E_y(c-e_x)
        (SCALAR, SCALAR): (1, 1, 1, 1),
    }
    dims_ok = all(len(stencil_by_char[(e, b)]) == (1 if e[0] == b[0] else 0) for e in CHARACTERS for b in CHARACTERS)
    check("one-face stabilizer: a covariant boundary stencil exists (and is unique up to scale) exactly when the edge and face characters agree on the in-plane 180-degree flip (8 of 16)", dims_ok,
          {k: len(v) for k, v in stencil_by_char.items()})
    for key, expect in expected_stencils.items():
        basis = stencil_by_char[key]
        check(f"one-face stabilizer: characters {key} force the stencil {expect} up to scale",
              len(basis) == 1 and rank_q([basis[0], [Fraction(v) for v in expect]]) == 1, [str(v) for v in basis[0]] if basis else "none")
    # gauge invariance on one face star: the nullspace of the four vertex-gradient constraints (own computation)
    # boundary links a: v0->v1, b: v1->v2, c: v3->v2, d: v0->v3 (circulation a + b - c - d)
    grad = [[-1, 1, 0, 0], [0, -1, 1, 0], [0, 0, 1, -1], [-1, 0, 0, 1]]
    gauge_rows = [[Fraction(grad[e_][v_]) for e_ in range(4)] for v_ in range(4)]
    gauge_basis = nullspace_q(gauge_rows)
    check("gauge invariance on one face star (own row reduction): the invariant stencils are exactly the curl multiples (1,1,-1,-1)",
          len(gauge_basis) == 1 and rank_q([gauge_basis[0], [Fraction(v) for v in (1, 1, -1, -1)]]) == 1)
    gauge_ok_pairs = []
    stencil_classes: dict[tuple, list] = {}
    for (e, b), basis in stencil_by_char.items():
        if basis:
            vec = basis[0]
            scale_ = next(v for v in vec if v != 0)
            key = tuple(v / scale_ for v in vec)
            stencil_classes.setdefault(key, []).append((e, b))
            resid = [sum(vec[e_] * grad[e_][v_] for e_ in range(4)) for v_ in range(4)]
            if all(val == 0 for val in resid):
                gauge_ok_pairs.append((e, b))
    check("the eight compatible character pairs give exactly four distinct one-face stencils (each shared by a pair related by the global sign twist)",
          len(stencil_classes) == 4 and all(len(v) == 2 for v in stencil_classes.values()),
          {tuple(str(x) for x in k): v for k, v in stencil_classes.items()})
    check("exactly the vector/vector pair and its global sign twist give the gauge-invariant curl stencil; the other three stencils fail gauge invariance",
          sorted(gauge_ok_pairs) == sorted([(ORIENTED, ORIENTED), ((1, 1), (1, 1))]))

    # ---------------------------------------------------------------- E
    section("E. Exact covariant classification of nearest-neighbor real linear generators (side 4)")
    ne4, nf4 = len(comp4.edges), len(comp4.faces)
    curl_block = block_matrix(comp4, np.zeros((ne4, nf4), dtype=np.int64), comp4.curl)
    curl_t_block = block_matrix(comp4, comp4.curl.T, np.zeros((nf4, ne4), dtype=np.int64))
    uns_block = block_matrix(comp4, np.zeros((ne4, nf4), dtype=np.int64), comp4.unsigned)
    uns_t_block = block_matrix(comp4, comp4.unsigned.T, np.zeros((nf4, ne4), dtype=np.int64))
    onsite_e = block_matrix(comp4, np.zeros((ne4, nf4), dtype=np.int64), np.zeros((nf4, ne4), dtype=np.int64), u=1)
    onsite_f = block_matrix(comp4, np.zeros((ne4, nf4), dtype=np.int64), np.zeros((nf4, ne4), dtype=np.int64), v=1)
    dims = {}
    gauge_compatible = {}
    couplings = {}
    all_consistent = True
    for e_char in CHARACTERS:
        for b_char in CHARACTERS:
            labels, mats, basis, consistent = covariant_subspace(comp4, e_char, b_char)
            all_consistent = all_consistent and consistent and len(mats) == 30
            dims[(e_char, b_char)] = len(basis)
            span = [vectorize(assemble(mats, [Fraction(c) for c in vec])) for vec in basis]
            onsite_in = span_contains(span, vectorize(onsite_e)) and span_contains(span, vectorize(onsite_f))
            all_consistent = all_consistent and onsite_in
            # the face-from-edge coupling block of the covariant space
            blocks = [assemble(mats, [Fraction(c) for c in vec])[ne4:, :ne4] for vec in basis]
            coupling_rank = rank_q([vectorize(bk) for bk in blocks]) if blocks else 0
            if coupling_rank:
                X = next(bk for bk in blocks if np.any(bk))
                first = X[np.nonzero(X)][0]
                X = X * int(np.sign(first))
                couplings[(e_char, b_char)] = X
                gauge_compatible[(e_char, b_char)] = (not np.any(X @ comp4.d0)) and (not np.any(comp4.d2 @ X))
                if (e_char, b_char) == (ORIENTED, ORIENTED):
                    check("vector/vector characters: covariant generators = span{onsite E, onsite B, curl, curl^T} exactly",
                          len(basis) == 4 and all(span_contains(span, vectorize(m)) for m in (curl_block, curl_t_block)))
                if (e_char, b_char) == (SCALAR, SCALAR):
                    check("scalar/scalar characters: covariant generators = span{onsite E, onsite B, unsigned incidence, its transpose} exactly",
                          len(basis) == 4 and all(span_contains(span, vectorize(m)) for m in (uns_block, uns_t_block)))
            else:
                gauge_compatible[(e_char, b_char)] = None
            all_consistent = all_consistent and coupling_rank == (1 if e_char[0] == b_char[0] else 0)
    check("all 16 payload representations: rotated patterns stay in the 30-pattern span; onsite terms always covariant; one coupling direction iff the flip characters agree", all_consistent)
    check("covariant nearest-neighbor generator space has dimension 4 for the 8 compatible character pairs and 2 for the 8 incompatible pairs",
          all(dims[(e, b)] == (4 if e[0] == b[0] else 2) for e in CHARACTERS for b in CHARACTERS), dims)
    def same_up_to_sign(X, Y) -> bool:
        return bool(np.array_equal(X, Y) or np.array_equal(X, -Y))

    distinct = []
    for X in couplings.values():
        if not any(same_up_to_sign(X, Y) for Y in distinct):
            distinct.append(X)
    check("the 8 compatible pairs carry exactly 4 distinct couplings (up to sign): the curl, the unsigned incidence, and their two sign-twisted partners",
          len(couplings) == 8 and len(distinct) == 4
          and same_up_to_sign(couplings[(ORIENTED, ORIENTED)], comp4.curl) and same_up_to_sign(couplings[((1, 1), (1, 1))], comp4.curl)
          and same_up_to_sign(couplings[(SCALAR, SCALAR)], comp4.unsigned) and same_up_to_sign(couplings[((0, 1), (0, 1))], comp4.unsigned))
    check("exactly the curl is gauge- and chain-compatible (X d0 = 0, d2 X = 0): the vector/vector pair and its global sign twist; the other three couplings are not",
          sorted(k for k, v in gauge_compatible.items() if v) == sorted([(ORIENTED, ORIENTED), ((1, 1), (1, 1))]) and sum(v is not None for v in gauge_compatible.values()) == 8)
    labels_v, mats_v, basis_v, consistent_v = covariant_subspace(comp4, ORIENTED, ORIENTED, with_vertex=True)
    nv4 = len(comp4.vertices)
    ntot = nv4 + ne4 + nf4

    def embed(block, rows, cols):
        m = np.zeros((ntot, ntot), dtype=np.int64)
        m[rows[0]:rows[1], cols[0]:cols[1]] = block
        return m

    V, E, F = (0, nv4), (nv4, nv4 + ne4), (nv4 + ne4, ntot)
    expected_v = [embed(np.eye(nv4, dtype=np.int64), V, V), embed(np.eye(ne4, dtype=np.int64), E, E),
                  embed(np.eye(nf4, dtype=np.int64), F, F), embed(comp4.curl, F, E), embed(comp4.curl.T, E, F),
                  embed(comp4.d0, E, V), embed(comp4.d0.T, V, E)]
    span_v = [vectorize(assemble(mats_v, [Fraction(c) for c in vec])) for vec in basis_v]
    check("with a scalar vertex payload: covariant nearest-neighbor generators = span{onsite x3, curl, curl^T, d0, d0^T} (dim 7)",
          consistent_v and len(mats_v) == 43 and len(basis_v) == 7 and all(span_contains(span_v, vectorize(m)) for m in expected_v)
          and rank_q([vectorize(m) for m in expected_v]) == 7, f"dim={len(basis_v)}")

    # ---------------------------------------------------------------- F
    section("F. Item 6 inside the covariant family: conservation is a two-condition cut (side 6)")
    comp6 = comps[6]
    ne6, nf6 = len(comp6.edges), len(comp6.faces)
    u, v, q, r, wE, wB = sp.symbols("u v q r w_E w_B", real=True)
    # symbolic 2x2 structure: G = [[u, r K^T],[q K, v]] with K = curl; M G + G^T M = 0 blockwise
    diag_e, diag_f, cross = 2 * wE * u, 2 * wB * v, wE * r + wB * q
    check("symbolic: positive diagonal conservation <=> u = 0, v = 0, w_E r + w_B q = 0 (blockwise metric-skew equations)",
          sp.simplify(diag_e) == 2 * wE * u and sp.simplify(diag_f) == 2 * wB * v and sp.simplify(cross) == wE * r + wB * q
          and sp.solve([diag_e, diag_f, cross], [u, v, r], dict=True) == [{u: 0, v: 0, r: -wB * q / wE}])
    maxwell = block_generator(comp6, Fraction(0), Fraction(0), comp6.curl.T, comp6.curl, scale_ef=Fraction(-1), scale_fe=Fraction(1))
    field = rational_vector(ne6 + nf6, rng)
    check("Maxwell member (u=v=0, r=-q): exact metric-skew defect zero; dH/dt = 0 on a random rational field",
          metric_skew_defect(maxwell, Fraction(1), Fraction(1), ne6) == 0 and energy_derivative(maxwell, field, Fraction(1), Fraction(1), ne6) == 0)
    rate = apply(maxwell, field)
    per_site = [field[e] * rate[e] for e in range(ne6)]
    check("per-site energy (1/2)E_e^2 is NOT conserved by the Maxwell member while the lattice-wide sum is",
          any(val != 0 for val in per_site) and sum(field[i] * rate[i] for i in range(ne6 + nf6)) == 0)
    d0t = comp6.d0.T
    gauss_e = matvec_q(d0t, rate[:ne6])
    gauss_b = matvec_q(comp6.d2, rate[ne6:])
    check("both Gauss rows are exactly preserved by the Maxwell member (d0^T dE/dt = 0, d2 dB/dt = 0)",
          all(val == 0 for val in gauss_e) and all(val == 0 for val in gauss_b))
    Q = comp6.curl.T @ comp6.curl
    QF = comp6.curl @ comp6.curl.T
    poly = Q @ (Q - 3 * np.eye(ne6, dtype=np.int64)) @ (Q - 6 * np.eye(ne6, dtype=np.int64)) @ (Q - 9 * np.eye(ne6, dtype=np.int64))
    check("side 6: the edge operator C^T C satisfies Q(Q-3)(Q-6)(Q-9) = 0 exactly (spectrum in {0,3,6,9})", not np.any(poly))
    mult = {lam: ne6 - rank_q(Q - lam * np.eye(ne6, dtype=np.int64)) for lam in (0, 3, 6, 9)}
    mult_f = {lam: nf6 - rank_q(QF - lam * np.eye(nf6, dtype=np.int64)) for lam in (0, 3, 6, 9)}
    check("side 6: exact multiplicities of C^T C are {0:29, 3:12, 6:24, 9:16} = two transverse branches per nonzero momentum",
          mult == {0: 29, 3: 12, 6: 24, 9: 16} and sum(mult.values()) == 81, mult)
    check("side 6: C C^T has the same nonzero multiplicities (frequency^2 spectrum of the conservative law)",
          mult_f == {0: 29, 3: 12, 6: 24, 9: 16}, mult_f)
    check("side 6: 52 = 2 x 26 nonzero momenta transverse modes; the 29 zero modes are 26 gradients + 3 harmonic",
          mult[3] + mult[6] + mult[9] == 2 * torus_momentum_count(6) and mult[0] == (len(comp6.vertices) - 1) + 3)
    # witnesses that keep items 1,2,3,4,5,7 and violate item 6
    damped = block_generator(comp6, Fraction(-1, 3), Fraction(-1, 3), comp6.curl.T, comp6.curl, scale_ef=Fraction(-1), scale_fe=Fraction(1))
    overdamped = block_generator(comp6, Fraction(0), Fraction(-2), comp6.curl.T, comp6.curl, scale_ef=Fraction(-1), scale_fe=Fraction(2))
    same_sign = block_generator(comp6, Fraction(0), Fraction(0), comp6.curl.T, comp6.curl, scale_ef=Fraction(1), scale_fe=Fraction(1))
    witnesses6 = {"damped (u=v=-1/3)": damped, "overdamped (u=0, v=-2, q=2, r=-1)": overdamped, "same-sign (r=+q)": same_sign}
    rots6 = proper_rotations()
    perm6 = [field_rotation(comp6, rot, ORIENTED, ORIENTED) for rot in rots6]
    for name, g in witnesses6.items():
        rate_w = apply(g, field)
        d_energy = sum(field[i] * rate_w[i] for i in range(ne6 + nf6))
        no_positive_diag = all(metric_skew_defect(g, a, b, ne6) != 0 for a in (Fraction(1), Fraction(2), Fraction(1, 3)) for b in (Fraction(1), Fraction(2), Fraction(1, 3)))
        trace = sum(g[i][i] for i in range(ne6 + nf6))
        check(f"witness {name}: nearest-neighbor, covariant, edge-to-face block gauge-compatible, minimal payload",
              support_radius(comp6, g) == 1 and all(is_covariant(g, p) for p in perm6)
              and not np.any(int_matrix([row[:ne6] for row in g[ne6:]]) @ comp6.d0)
              and not np.any(comp6.d2 @ int_matrix([row[:ne6] for row in g[ne6:]])))
        check(f"witness {name}: violates item 6 (no positive diagonal conserved energy; dH/dt or trace nonzero)",
              no_positive_diag and (d_energy != 0 or trace != 0), f"dH/dt={d_energy}, trace={trace}")
    same_sq = int_matrix(same_sign) @ int_matrix(same_sign)
    check("same-sign witness: G^2 = diag(C^T C, C C^T) has eigenvalue 9 > 0, so G has real eigenvalues (no conserved positive form)",
          np.array_equal(same_sq[:ne6, :ne6], Q) and rank_q(Q - 9 * np.eye(ne6, dtype=np.int64)) < ne6)
    s, gam = sp.symbols("s gamma", positive=True)
    over_block = sp.Matrix([[0, -s], [gam * s, -gam]])
    maxwell_block = sp.Matrix([[0, -s], [s, 0]])
    lam = sp.symbols("lambda")
    over_poly = sp.expand(over_block.charpoly(lam).as_expr())
    slow = [root for root in sp.solve(over_poly, lam) if sp.simplify(root.subs(s, 0)) == 0][0]
    series = sp.series(slow, s, 0, 5).removeO()
    check("overdamped witness per mode: characteristic polynomial lambda^2 + gamma lambda + gamma s^2; slow root = -s^2 - s^4/gamma + ... (diffusive)",
          sp.expand(over_poly - (lam ** 2 + gam * lam + gam * s ** 2)) == 0 and sp.expand(series - (-s ** 2 - s ** 4 / gam)) == 0)
    check("Maxwell per mode: eigenvalues +/- i s (propagating at unit speed), not diffusive",
          set(maxwell_block.eigenvals().keys()) == {sp.I * s, -sp.I * s})

    # ---------------------------------------------------------------- G
    section("G. Deterministic ordered conditional-mean relaxation (side 6)")
    A = rational_vector(ne6, rng)
    energy_before = dot_q(A, matvec_q(Q, A)) / 2
    B_field = conditional_mean_sweep(Q, A)
    energy_after = dot_q(B_field, matvec_q(Q, B_field)) / 2
    check("Gauss-Seidel sweep of single-site conditional means of the harmonic static law strictly decreases (1/2) A^T C^T C A",
          energy_after < energy_before, f"{energy_before} -> {energy_after}")
    q_radius = max(comp6.distance(comp6.edges[a], comp6.edges[b]) for a, b in zip(*np.nonzero(Q)) if a != b)
    check("each single-coordinate conditional mean reads Q-coupled edges at physical distance 2; this is not a full-sweep radius bound",
          q_radius == 2 and all(int(Q[e, e]) == 4 for e in range(ne6)))

    # Exact distinction between a proper one-edge conditional and its mean.
    c4 = Compilation(4)
    q4 = c4.curl.T @ c4.curl
    zero4 = [Fraction(0)] * len(c4.edges)
    variance = Fraction(1, int(q4[0, 0]))  # kappa = 1, all other coordinates zero
    check("one-edge Gaussian conditional at zero has variance 1/4 and expected H=1/2, whereas the mean sweep fixes zero",
          variance == Fraction(1, 4) and Fraction(int(q4[0, 0]), 2) * variance == Fraction(1, 2)
          and conditional_mean_sweep(q4, zero4) == zero4)
    check("formal full-space quadratic density has flat gradient and harmonic directions; it is not a normalized Gaussian law",
          not np.any(q4 @ c4.d0) and not np.any(q4 @ np.ones(len(c4.edges), dtype=int)))
    gs = np.array([conditional_mean_sweep(q4, [Fraction(int(i == j)) for i in range(len(c4.edges))])
                   for j in range(len(c4.edges))], dtype=object).T
    tr = translation(c4, (2, 0, 0))[:len(c4.edges), :len(c4.edges)]
    check("actual fixed-order mean sweep fails even-translation covariance (no covariant sampler or time-law identification)",
          np.count_nonzero(gs @ tr - tr @ gs) == 572)

    # ---------------------------------------------------------------- H
    section("H. Item 5 witness: the unoriented covariant law (side 6)")
    unoriented = block_generator(comp6, Fraction(0), Fraction(0), comp6.unsigned.T, comp6.unsigned, scale_ef=Fraction(-1), scale_fe=Fraction(1))
    perm6_u = [field_rotation(comp6, rot, SCALAR, SCALAR) for rot in rots6]
    check("unoriented law: nearest-neighbor, covariant (unoriented representation), conserves (1/2)(|E|^2+|B|^2), minimal payload",
          support_radius(comp6, unoriented) == 1 and all(is_covariant(unoriented, p) for p in perm6_u)
          and metric_skew_defect(unoriented, Fraction(1), Fraction(1), ne6) == 0)
    check("unoriented law violates item 5: S d0 != 0 and d2 S != 0 over the integers",
          np.any(comp6.unsigned @ comp6.d0) and np.any(comp6.d2 @ comp6.unsigned))
    consts = [[Fraction(1 if comp6.edge_axis(x) == a else 0) for x in comp6.edges] for a in AXES]
    images = [matvec_q(comp6.unsigned, c) for c in consts]
    curl_images = [matvec_q(comp6.curl, c) for c in consts]
    check("unoriented law has no soft mode at zero momentum: S maps the three constant edge fields to independent faces (rank 3), while the curl kills them",
          rank_q(images) == 3 and all(all(val == 0 for val in img) for img in curl_images))
    # OL's convention clause is load-bearing (checker finding CK-03): a diagonal sign relabelling of the oriented law —
    # the payload negated at every z-normal face — is a signed-permutation representation with the same site action
    # that is none of the sixteen tensor-transport matrices; its covariant coupling D C is gauge-invariant but not
    # chain-compatible, so "vector-type" must mean the compilation's own sign basis.
    D_signs = np.array([1] * ne6 + [(-1 if comp6.face_normal(x) == 2 else 1) for x in comp6.faces], dtype=np.int64)
    D_mat = np.diag(D_signs)
    rho_prime = [D_mat @ p @ D_mat for p in perm6]
    laws6 = {(e_c, b_c): [field_rotation(comp6, rot, e_c, b_c) for rot in rots6] for e_c in CHARACTERS for b_c in CHARACTERS}
    distinct_from_all = all(any(not np.array_equal(rho_prime[i], law[i]) for i in range(len(rots6))) for law in laws6.values())
    signed_perm_ok = all(np.array_equal(np.abs(m).sum(axis=0), np.ones(ne6 + nf6, dtype=np.int64))
                         and np.array_equal(np.abs(m).sum(axis=1), np.ones(ne6 + nf6, dtype=np.int64)) for m in rho_prime)
    index_of = {tuple(map(tuple, r)): i for i, r in enumerate(rots6)}
    rep_ok = all(np.array_equal(rho_prime[index_of[tuple(map(tuple, r1 @ r2))]], rho_prime[i] @ rho_prime[j])
                 for i, r1 in enumerate(rots6) for j, r2 in enumerate(rots6))
    same_action = all(np.array_equal(np.abs(rho_prime[i]), np.abs(perm6[i])) for i in range(len(rots6)))
    g_relabelled = D_mat @ int_matrix(maxwell) @ D_mat
    DC = g_relabelled[ne6:, :ne6]
    check("sign-relabelled oriented law (payload negated at every z-normal face): a signed-permutation representation with the same site action, distinct from all sixteen tensor-transport laws; the generator it makes covariant has edge-to-face block D C with D C d0 = 0 but d2 D C != 0 — OL's convention clause (the compilation's own sign basis) is load-bearing",
          signed_perm_ok and rep_ok and same_action and distinct_from_all
          and all(np.array_equal(m @ g_relabelled @ m.T, g_relabelled) for m in rho_prime)
          and not same_up_to_sign(DC, comp6.curl) and not np.any(DC @ comp6.d0) and np.any(comp6.d2 @ DC))

    # ---------------------------------------------------------------- I
    section("I. Item 4 witnesses (side 6)")
    even6 = [translation(comp6, sh) for sh in itertools.product((0, 2, 4), repeat=3) if any(sh)]
    scale = np.array([1 + comp6.face_normal(x) for x in comp6.faces], dtype=np.int64)  # 1,2,3 by normal
    aniso_curl = comp6.curl * scale[:, None]
    anisotropic = block_generator(comp6, Fraction(0), Fraction(0), aniso_curl.T, aniso_curl, scale_ef=Fraction(-1), scale_fe=Fraction(1))
    check("anisotropic law (orientation coefficients 1,2,3): nearest-neighbor, conservative, gauge-invariant (L d0 = 0), NOT covariant, and NOT magnetic-Gauss preserving (d2 L != 0)",
          support_radius(comp6, anisotropic) == 1 and metric_skew_defect(anisotropic, Fraction(1), Fraction(1), ne6) == 0
          and not np.any(aniso_curl @ comp6.d0) and np.any(comp6.d2 @ aniso_curl)
          and not all(is_covariant(anisotropic, p) for p in perm6))
    # (nearest-neighbor + L d0 = 0 + d2 L = 0) forces L = q C with one lattice-wide q: exact nullspace, side 4 (general)
    unknowns = [(f, comp4.eidx[site]) for f, x in enumerate(comp4.faces) for site, _ in comp4.face_stencil(x, signed=True)]
    col_of = {pair: i for i, pair in enumerate(unknowns)}
    system4 = []
    for f in range(nf4):
        for v_ in range(nv4):
            row = [Fraction(0)] * len(unknowns)
            for (ff, e) in unknowns:
                if ff == f and comp4.d0[e, v_]:
                    row[col_of[(ff, e)]] += int(comp4.d0[e, v_])
            if any(row):
                system4.append(row)
    for c_ in range(len(comp4.cubes)):
        for e in range(ne4):
            row = [Fraction(0)] * len(unknowns)
            for (ff, ee) in unknowns:
                if ee == e and comp4.d2[c_, ff]:
                    row[col_of[(ff, ee)]] += int(comp4.d2[c_, ff])
            if any(row):
                system4.append(row)
    chain_basis = nullspace_q(system4)
    curl_vec = [Fraction(int(comp4.curl[f, e])) for (f, e) in unknowns]
    check("side 4: nearest-neighbor face rows with L d0 = 0 and d2 L = 0 form exactly the one-dimensional space spanned by the oriented curl (no covariance assumed)",
          len(unknowns) == 96 and len(chain_basis) == 1 and rank_q([chain_basis[0], curl_vec]) == 1)
    # side 6 in full generality: all 324 boundary-edge coefficients free, no per-face reduction (checker finding CK-08)
    unknowns6 = [(f, comp6.eidx[site]) for f, x in enumerate(comp6.faces) for site, _ in comp6.face_stencil(x, signed=True)]
    col6 = {pair: i for i, pair in enumerate(unknowns6)}
    system6_full = []
    for f in range(nf6):
        for v_ in range(len(comp6.vertices)):
            row = [Fraction(0)] * len(unknowns6)
            for (ff, e) in unknowns6:
                if ff == f and comp6.d0[e, v_]:
                    row[col6[(ff, e)]] += int(comp6.d0[e, v_])
            if any(row):
                system6_full.append(row)
    for c_ in range(len(comp6.cubes)):
        for e in range(ne6):
            row = [Fraction(0)] * len(unknowns6)
            for (ff, ee) in unknowns6:
                if ee == e and comp6.d2[c_, ff]:
                    row[col6[(ff, ee)]] += int(comp6.d2[c_, ff])
            if any(row):
                system6_full.append(row)
    chain_basis6 = nullspace_q(system6_full)
    curl_vec6 = [Fraction(int(comp6.curl[f, e])) for (f, e) in unknowns6]
    check("side 6 in full generality (324 free boundary-edge coefficients, no per-face reduction): the gauge-plus-chain nullspace is one-dimensional and spanned by the oriented curl",
          len(unknowns6) == 324 and len(chain_basis6) == 1 and rank_q([chain_basis6[0], curl_vec6]) == 1)
    # side 6: after the per-face gauge reduction (row f = q_f * curl_f) the magnetic Gauss identity forces all q_f equal
    system6 = []
    for c_ in range(len(comp6.cubes)):
        for e in range(ne6):
            row = [Fraction(0)] * nf6
            for f in range(nf6):
                if comp6.d2[c_, f] and comp6.curl[f, e]:
                    row[f] += int(comp6.d2[c_, f]) * int(comp6.curl[f, e])
            if any(row):
                system6.append(row)
    q_basis = nullspace_q(system6)
    check("side 6: with each face row a multiple q_f of its curl, d2 L = 0 forces q_f constant over all 81 faces (nullspace dimension 1, the all-ones vector)",
          len(q_basis) == 1 and all(v == q_basis[0][0] for v in q_basis[0]))
    check("consequence: items 1,2L,3,5,6,7 force the generator to c[[0,-C^T],[C,0]] after normalization, which is covariant; item 4 is implied by the other items",
          all(is_covariant(maxwell, p) for p in perm6) and all(is_covariant(maxwell, t) for t in even6))
    priv_curl = comp6.curl.copy()
    priv_curl[0, :] *= 2
    privileging = block_generator(comp6, Fraction(0), Fraction(0), priv_curl.T, priv_curl, scale_ef=Fraction(-1), scale_fe=Fraction(1))
    check("site-privileging law (one face row doubled): conservative, nearest-neighbor, gauge-compatible, but NOT translation covariant",
          metric_skew_defect(privileging, Fraction(1), Fraction(1), ne6) == 0 and support_radius(comp6, privileging) == 1
          and not np.any(priv_curl @ comp6.d0) and not all(is_covariant(privileging, t) for t in even6))

    # Missing-premise and degenerate-domain controls use actual constructions.
    c2 = Compilation(2)
    l2 = np.zeros_like(c2.curl)
    l2[0, c2.eidx[c2.face_stencil(c2.faces[0], True)[0][0]]] = 1
    check("side 2 is degenerate: d0=C=d2=0 and a nonzero NN map obeys both chain constraints; classification excludes it",
          not np.any(c2.d0) and not np.any(c2.curl) and not np.any(c2.d2)
          and np.any(l2) and not np.any(l2 @ c2.d0) and not np.any(c2.d2 @ l2))
    doubled_face = c4.curl.copy()
    doubled_face[0] *= 2
    check("doubling one face preserves L d0=0 but breaks d2 L=0 (8 entries on side 4); it also relaxes item 5",
          not np.any(doubled_face @ c4.d0) and np.count_nonzero(c4.d2 @ doubled_face) == 8)
    lam4 = np.arange(len(c4.vertices), dtype=np.int64) ** 2
    nonlinear_curl = lambda ev: c4.curl @ (ev ** 3)
    defect = nonlinear_curl(c4.d0 @ lam4)
    probe = np.arange(len(c4.edges), dtype=np.int64) - 7
    ncov = True
    for rot in proper_rotations():
        p = field_rotation(c4, rot, ORIENTED, ORIENTED)
        pe, pb = p[:len(c4.edges), :len(c4.edges)], p[len(c4.edges):, len(c4.edges):]
        ncov = ncov and np.array_equal(nonlinear_curl(pe @ probe), pb @ nonlinear_curl(probe))
    nt = translation(c4, (2, 0, 0))
    ne4 = len(c4.edges)
    check("without 2L, E_dot=0 and B_dot=C(E^3) is oriented-covariant/NN but fails gauge compatibility",
          ncov and np.array_equal(nonlinear_curl(nt[:ne4, :ne4] @ probe), nt[ne4:, ne4:] @ nonlinear_curl(probe))
          and np.count_nonzero(defect) == 24 and max(abs(defect)) == 36864)

    # ---------------------------------------------------------------- J
    section("J. Item 3 witness: improved curl of physical radius three (side 8)")
    comp8 = comps[8]
    ne8, nf8 = len(comp8.edges), len(comp8.faces)
    eps = Fraction(1, 7)
    Q8 = comp8.curl.T @ comp8.curl
    improved = [[Fraction(0)] * ne8 for _ in range(nf8)]
    for f in range(nf8):
        for e in range(ne8):
            val = int(comp8.curl[f, e])
            corr = sum(int(comp8.curl[f, e2]) * int(Q8[e2, e]) for e2 in np.nonzero(comp8.curl[f])[0])
            improved[f][e] = Fraction(val) + eps * corr
    g_imp = [[Fraction(0)] * (ne8 + nf8) for _ in range(ne8 + nf8)]
    for f in range(nf8):
        for e in range(ne8):
            if improved[f][e]:
                g_imp[ne8 + f][e] = improved[f][e]
                g_imp[e][ne8 + f] = -improved[f][e]
    imp_d0 = [dot_q(row, [Fraction(int(v)) for v in comp8.d0[:, c]]) for row in improved for c in range(len(comp8.vertices))]
    d2_imp = [sum(int(comp8.d2[c, f]) * improved[f][e] for f in range(nf8)) for c in range(len(comp8.cubes)) for e in range(ne8)]
    perm8 = [field_rotation(comp8, rot, ORIENTED, ORIENTED) for rot in rots6]
    check("improved-curl law L = C(1 + eps C^T C): conservative, gauge-compatible (L d0 = 0, d2 L = 0), covariant, minimal payload",
          metric_skew_defect(g_imp, Fraction(1), Fraction(1), ne8) == 0 and all(val == 0 for val in imp_d0)
          and all(val == 0 for val in d2_imp) and all(is_covariant(g_imp, p) for p in perm8))
    check("improved-curl law violates item 3: its support radius on the side-8 torus is exactly 3 (edge-face couplings occur only at odd distance)",
          support_radius(comp8, g_imp) == 3)

    # ---------------------------------------------------------------- K
    section("K. Item 7 witness: a scalar vertex payload (side 6)")
    nv6 = len(comp6.vertices)
    n_all = nv6 + ne6 + nf6

    def vertex_law(a: Fraction, a2: Fraction):
        g = [[Fraction(0)] * n_all for _ in range(n_all)]
        for v_ in range(nv6):
            for e in range(ne6):
                val = int(comp6.d0[e, v_])
                if val:
                    g[v_][nv6 + e] = a * val          # dot phi = a d0^T E
                    g[nv6 + e][v_] = a2 * val         # dot E = a2 d0 phi + ...
        for f in range(nf6):
            for e in range(ne6):
                val = int(comp6.curl[f, e])
                if val:
                    g[nv6 + ne6 + f][nv6 + e] = Fraction(val)    # dot B = C E
                    g[nv6 + e][nv6 + ne6 + f] = Fraction(-val)   # dot E = -C^T B
        return g

    vlaw = vertex_law(Fraction(-1), Fraction(1))
    field_v = rational_vector(n_all, rng)
    rate_v = apply(vlaw, field_v)
    perm6_v = [field_rotation(comp6, rot, ORIENTED, ORIENTED, True) for rot in rots6]
    check("vertex-scalar law: dH/dt = 0 for H = (1/2)(|phi|^2+|E|^2+|B|^2); nearest-neighbor (a vertex reads its six edges); covariant",
          sum(field_v[i] * rate_v[i] for i in range(n_all)) == 0 and support_radius(comp6, vlaw, with_vertex=True) == 1
          and all(is_covariant(vlaw, p) for p in perm6_v))
    hodge = comp6.d0 @ comp6.d0.T + Q
    hodge_mult = {lam_: ne6 - rank_q(hodge - lam_ * np.eye(ne6, dtype=np.int64)) for lam_ in (0, 3, 6, 9)}
    check("vertex-scalar law spectrum: -G^2 on edges is the Hodge Laplacian with multiplicities {0:3, 3:18, 6:36, 9:24} = three branches per nonzero momentum",
          hodge_mult == {0: 3, 3: 18, 6: 36, 9: 24} and (hodge_mult[3] + hodge_mult[6] + hodge_mult[9]) == 3 * torus_momentum_count(6), hodge_mult)
    vlaw2 = vertex_law(Fraction(-2), Fraction(2))
    rate_v2 = apply(vlaw2, field_v)
    check("with a vertex payload the conservative covariant class has two independent speeds (a=-2,a2=2 also conserves H): uniqueness up to one speed needs item 7",
          sum(field_v[i] * rate_v2[i] for i in range(n_all)) == 0 and all(is_covariant(vlaw2, p) for p in perm6_v))
    aV, aE, qq, rr, wV, wE2, wB2 = sp.symbols("a a2 q r w_V w_E w_B", real=True)
    sol = sp.solve([wV * aV + wE2 * aE, wE2 * rr + wB2 * qq], [aE, rr], dict=True)
    check("symbolic: the extended conservative family has two free ratios (a2 = -w_V a / w_E, r = -w_B q / w_E), i.e. two speeds",
          sol == [{aE: -wV * aV / wE2, rr: -wB2 * qq / wE2}])

    # ---------------------------------------------------------------- L
    section("L. Item 2 witnesses: finite tick, nonlinear constitutive law; item 1 witness: complex payload (side 6)")
    h = Fraction(1, 2)
    E0 = rational_vector(ne6, rng)
    B0 = rational_vector(nf6, rng)

    def tick(Ev, Bv, step: Fraction):
        B1 = [b + step / 2 * c for b, c in zip(Bv, matvec_q(comp6.curl, Ev))]
        E1 = [e - step * c for e, c in zip(Ev, matvec_q(comp6.curl.T, B1))]
        B2 = [b + step / 2 * c for b, c in zip(B1, matvec_q(comp6.curl, E1))]
        return E1, B2, (B1,)

    def h_energy(Ev, Bv, step: Fraction) -> Fraction:
        ce = matvec_q(comp6.curl, Ev)
        return dot_q(Bv, Bv) / 2 + dot_q(Ev, Ev) / 2 - step * step / 8 * dot_q(ce, ce)

    E1, B1, (Bhalf,) = tick(E0, B0, h)
    Eb, Bb, _ = tick(E1, B1, -h)
    check("finite tick h=1/2: exactly reversible (U(-h) U(h) = identity on a random rational field)", Eb == E0 and Bb == B0)
    check("finite tick: each shear preserves its Gauss row exactly (d2 B after the half shears; d0^T E after the full shear)",
          matvec_q(comp6.d2, Bhalf) == matvec_q(comp6.d2, B0) and matvec_q(comp6.d0.T, E1) == matvec_q(comp6.d0.T, E0)
          and matvec_q(comp6.d2, B1) == matvec_q(comp6.d2, B0))
    check("finite tick: conserves the modified energy H_h = |B|^2/2 + |E|^2/2 - (h^2/8)|C E|^2 exactly; H_h > 0 since spec(C^T C) <= 9 < 4/h^2 = 16",
          h_energy(E1, B1, h) == h_energy(E0, B0, h) and 1 - h * h * 9 / 4 > 0)
    # Actual exponential comparator on a nonzero mode, not forward Euler.
    hs, ss = sp.symbols("h s", positive=True)
    modal_G = sp.Matrix([[0, -ss], [ss, 0]])
    modal_tick = sp.Matrix([[1 - hs**2 * ss**2/2, -hs*ss],
                           [hs*ss*(1 - hs**2 * ss**2/4), 1 - hs**2 * ss**2/2]])
    exponential_taylor3 = sum((hs**k * modal_G**k / sp.factorial(k) for k in range(4)), sp.zeros(2))
    check("tick differs from exp(h G) for the original generator: its modal upper-right h^3 coefficient differs by -s^3/6",
          sp.expand((modal_tick - exponential_taylor3)[0, 1]).coeff(hs, 3) == -ss**3/6)
    # For h=1/2, s^2=3: cos(sqrt(3)/2) >= 1-x^2/2+x^4/24-x^6/720 > 5/8
    # by the alternating decreasing cosine series (0 < x < 1).
    cos_lower = 1-sp.Rational(3, 4)/2+sp.Rational(3, 4)**2/24-sp.Rational(3, 4)**3/720
    check("actual nonzero side-6 mode: tick E=5/8 differs from exp E=cos(sqrt(3)/2), certified by its rational Taylor lower bound",
          cos_lower > sp.Rational(5, 8) and modal_tick[0, 0].subs({hs:sp.Rational(1, 2), ss:sp.sqrt(3)}) == sp.Rational(5, 8))
    tick_columns = []
    for j in range(ne6+nf6):
        unit = [Fraction(int(i == j)) for i in range(ne6+nf6)]
        ue, ub, _ = tick(unit[:ne6], unit[ne6:], h)
        tick_columns.append(ue+ub)
    U = np.array(tick_columns, dtype=object).T
    M = np.zeros_like(U)
    M[:ne6, :ne6] = np.eye(ne6, dtype=object)-h*h*Q/4
    M[ne6:, ne6:] = np.eye(nf6, dtype=object)
    coords = comp6.edges+comp6.faces
    full_radius = max(comp6.distance(coords[i], coords[j]) for i, j in zip(*np.nonzero(U)) if i != j)
    check("actual complete tick has radius 3 and preserves its non-onsite modified metric exactly",
          full_radius == 3 and np.any(M-np.diag(np.diag(M))) and not np.any(U.T @ M @ U-M))
    check("tick does not preserve the onsite unit norm; side-6 modes 3 and 6 need incompatible onsite weight ratios 13/16 and 5/8",
          np.any(U.T @ U-np.eye(ne6+nf6, dtype=object))
          and 1-h*h*3/4 == Fraction(13, 16) and 1-h*h*6/4 == Fraction(5, 8)
          and sp.simplify((modal_tick.T*sp.diag(sp.Symbol('wE'), sp.Symbol('wB'))*modal_tick-sp.diag(sp.Symbol('wE'), sp.Symbol('wB')))[0, 1]
                          - hs*ss*(1-hs**2*ss**2/2)*(sp.Symbol('wB')*(1-hs**2*ss**2/4)-sp.Symbol('wE'))) == 0)

    # the tick's covariance and per-shear locality, executed (checker finding CK-04)
    def signed_permute(perm_matrix: np.ndarray, vec: list[Fraction]) -> list[Fraction]:
        out = [Fraction(0)] * len(vec)
        for c in range(len(vec)):
            rows = np.nonzero(perm_matrix[:, c])[0]
            out[int(rows[0])] += int(perm_matrix[rows[0], c]) * vec[c]
        return out

    tick_cov = True
    for p in perm6:
        pE_, pB_ = p[:ne6, :ne6], p[ne6:, ne6:]
        E1r, B1r, _ = tick(signed_permute(pE_, E0), signed_permute(pB_, B0), h)
        tick_cov = tick_cov and E1r == signed_permute(pE_, E1) and B1r == signed_permute(pB_, B1)
    e0_, f0_ = 0, 0
    E_pert = E0[:]
    E_pert[e0_] += 1
    Bh_pert = [b + h / 2 * c for b, c in zip(B0, matvec_q(comp6.curl, E_pert))]
    changed_faces = [f for f in range(nf6) if Bh_pert[f] != Bhalf[f]]
    B_pert = B0[:]
    B_pert[f0_] += 1
    E_after = [e - h * c for e, c in zip(E0, matvec_q(comp6.curl.T, B_pert))]
    E_base = [e - h * c for e, c in zip(E0, matvec_q(comp6.curl.T, B0))]
    changed_edges = [e for e in range(ne6) if E_after[e] != E_base[e]]
    check("finite tick: covariant under all 24 proper rotations (oriented representation); each shear reads one site and its four opposite-role nearest neighbors only (one edge moves exactly its four faces, one face exactly its four edges, all at physical distance 1)",
          tick_cov and len(changed_faces) == 4 and all(comp6.distance(comp6.faces[f], comp6.edges[e0_]) == 1 for f in changed_faces)
          and len(changed_edges) == 4 and all(comp6.distance(comp6.edges[e], comp6.faces[f0_]) == 1 for e in changed_edges))
    epsn = Fraction(1, 5)

    def nonlinear_rate(Ev, Bv):
        Bc = [b + epsn * b ** 3 for b in Bv]
        return [-c for c in matvec_q(comp6.curl.T, Bc)], matvec_q(comp6.curl, Ev)

    dE, dB = nonlinear_rate(E0, B0)
    d_energy_nl = dot_q(E0, dE) + sum((b + epsn * b ** 3) * db for b, db in zip(B0, dB))
    dE2, dB2 = nonlinear_rate([2 * e for e in E0], [2 * b for b in B0])
    check("nonlinear constitutive law dE/dt = -C^T(B + eps B^3), dB/dt = C E: conserves the positive energy |E|^2/2 + |B|^2/2 + (eps/4)|B|^4 exactly",
          d_energy_nl == 0)
    check("nonlinear constitutive law: violates linearity (rate not homogeneous of degree one)",
          dE2 != [2 * x for x in dE])
    check("nonlinear quartic-energy witness does not conserve the declared unit diagonal quadratic energy",
          dot_q(E0, dE)+dot_q(B0, dB) != 0)
    # its locality, gauge compatibility and covariance, executed (checker finding CK-04)
    Bq = B0[:]
    Bq[f0_] += 1
    dE_q, _ = nonlinear_rate(E0, Bq)
    moved_edges = [e for e in range(ne6) if dE_q[e] != dE[e]]
    Eq = E0[:]
    Eq[e0_] += 1
    _, dB_q = nonlinear_rate(Eq, B0)
    moved_faces = [f for f in range(nf6) if dB_q[f] != dB[f]]
    lam_v = rational_vector(len(comp6.vertices), rng)
    _, dB_gauge = nonlinear_rate([e + g for e, g in zip(E0, matvec_q(comp6.d0, lam_v))], B0)
    nl_cov = True
    for p in perm6:
        pE_, pB_ = p[:ne6, :ne6], p[ne6:, ne6:]
        dEr_, dBr_ = nonlinear_rate(signed_permute(pE_, E0), signed_permute(pB_, B0))
        nl_cov = nl_cov and dEr_ == signed_permute(pE_, dE) and dBr_ == signed_permute(pB_, dB)
    check("nonlinear constitutive law: nearest-neighbor (one face moves exactly its four boundary edges' rates, one edge exactly its four faces', all at distance 1), gauge-compatible (dB/dt invariant under E -> E + d0 lambda), covariant under all 24 proper rotations",
          len(moved_edges) == 4 and all(comp6.distance(comp6.edges[e], comp6.faces[f0_]) == 1 for e in moved_edges)
          and len(moved_faces) == 4 and all(comp6.distance(comp6.faces[f], comp6.edges[e0_]) == 1 for f in moved_faces)
          and dB_gauge == dB and nl_cov)
    theta = Fraction(3, 7)

    def complex_rate(Er, Ei, Br, Bi):
        return ([-c - theta * ei for c, ei in zip(matvec_q(comp6.curl.T, Br), Ei)],
                [-c + theta * er for c, er in zip(matvec_q(comp6.curl.T, Bi), Er)],
                [c - theta * bi for c, bi in zip(matvec_q(comp6.curl, Er), Bi)],
                [c + theta * br for c, br in zip(matvec_q(comp6.curl, Ei), Br)])

    Er, Ei, Br, Bi = rational_vector(ne6, rng), rational_vector(ne6, rng), rational_vector(nf6, rng), rational_vector(nf6, rng)
    dEr, dEi, dBr, dBi = complex_rate(Er, Ei, Br, Bi)
    unit_e0 = [Fraction(1)] + [Fraction(0)] * (ne6 - 1)
    zeros_e, zeros_f = [Fraction(0)] * ne6, [Fraction(0)] * nf6
    check("complex two-component law with onsite phase theta: conserves sum |E|^2 + |B|^2 exactly; the onsite phase couples the two real components of every site (violates item 1: two real components per site)",
          dot_q(Er, dEr) + dot_q(Ei, dEi) + dot_q(Br, dBr) + dot_q(Bi, dBi) == 0
          and complex_rate(unit_e0, zeros_e, zeros_f, zeros_f)[1][0] == theta != 0)
    # the complex law's real generator, assembled column by column: antisymmetric, radius 1, covariant, edge-to-face blocks C (checker finding CK-04)
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
    radius_c = max(comp6.distance(order_c[r], order_c[c]) for r in range(n_c) for c in range(n_c) if gen_c[r][c] != 0)
    antisym_c = all(gen_c[r][c] == -gen_c[c][r] for r in range(n_c) for c in range(n_c))

    def doubled(p: np.ndarray) -> np.ndarray:
        pE_, pB_ = p[:ne6, :ne6], p[ne6:, ne6:]
        m = np.zeros((n_c, n_c), dtype=np.int64)
        m[:ne6, :ne6] = pE_
        m[ne6:2 * ne6, ne6:2 * ne6] = pE_
        m[2 * ne6:2 * ne6 + nf6, 2 * ne6:2 * ne6 + nf6] = pB_
        m[2 * ne6 + nf6:, 2 * ne6 + nf6:] = pB_
        return m

    cov_c = all(is_covariant(gen_c, doubled(p)) for p in perm6)
    block_rr = int_matrix([row[:ne6] for row in gen_c[2 * ne6:2 * ne6 + nf6]])
    block_ii = int_matrix([row[ne6:2 * ne6] for row in gen_c[2 * ne6 + nf6:]])
    block_ri = [row[ne6:2 * ne6] for row in gen_c[2 * ne6:2 * ne6 + nf6]]
    check("complex law: real generator exactly antisymmetric, support radius 1, covariant under the doubled oriented representation, and its edge-to-face blocks are exactly C (gauge- and chain-compatible)",
          antisym_c and radius_c == 1 and cov_c and np.array_equal(block_rr, comp6.curl) and np.array_equal(block_ii, comp6.curl)
          and all(v == 0 for row in block_ri for v in row))

    # ---------------------------------------------------------------- M
    section("M. Qubit capacity bound on linear one-site coordinates")
    # dim_R M_2(C) from an explicit real coordinate basis (real and imaginary parts of the four matrix units);
    # the witness component counts are read off the constructed generators, not declared (checker finding CK-07)
    real_coords = []
    for i in range(2):
        for j in range(2):
            for part in (0, 1):
                vec = [Fraction(0)] * 8
                vec[2 * (2 * i + j) + part] = Fraction(1)
                real_coords.append(vec)
    real_dim_m2c = rank_q(real_coords)
    components_per_site = {"Maxwell member": len(maxwell) // (ne6 + nf6), "vertex-scalar law": n_all // (nv6 + ne6 + nf6),
                           "complex law": n_c // (ne6 + nf6), "finite tick / nonlinear law": len(E0 + B0) // (ne6 + nf6)}
    check("dim_R M_2(C) = 8 (rank of the real coordinate basis): every witness payload fits, with components per site read off the constructed generators (1, 1, 2, 1); a nine-component linear payload cannot",
          real_dim_m2c == 8 and components_per_site == {"Maxwell member": 1, "vertex-scalar law": 1, "complex law": 2, "finite tick / nonlinear law": 1}
          and max(components_per_site.values()) <= real_dim_m2c and 9 > real_dim_m2c, components_per_site)

    # ---------------------------------------------------------------- N
    section("N. Resolution certificate")
    print("per_element: executed — every coefficient of the 30-pattern (43 with vertex payload) translation-covariant nearest-neighbor generator basis is classified exactly under all 24 proper rotations for each orientation law")
    print("per_site: executed — every site of the side-4, side-6 and side-8 compiled tori is role-censused, and per-site field energy is shown not conserved by the conservative law while the lattice-wide sum is")
    print("per_mode: executed — exact eigenvalue multiplicities of the edge, face and Hodge Laplacians on the side-6 torus certify two transverse branches per nonzero momentum and a third branch for the vertex-scalar witness; symbolic per-mode roots for the overdamped witness")
    print("per_block: executed — the edge, face and vertex blocks of every witness generator are checked separately for skewness, Gauss rows, chain identities and orientation covariance")
    print("lattice_wide: executed — every witness law is assembled as a full generator on the side-6 or side-8 torus where its conservation, covariance, support radius and gauge compatibility are decided exactly; no infinite-volume or continuum statement is executed")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
