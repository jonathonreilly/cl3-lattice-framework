#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.py
"""Block 143: staggered Hermiticity and a definite-symmetrizer bound.

On the displayed exact fixture this runner checks the mass/skew split,
staggered-parity Hermiticity, fixture-level uniqueness, the adapted scout,
the half-exchange anticommutation rank, and the chart-indexed spectrum of
``R``.  The spectral argument bounds the positive index of a real symmetric
symmetrizer ``S`` by six and therefore excludes positive-definite ``S``.
It does not exclude positive-semidefinite symmetrizers or, without a separate
mass-specific argument, positive-semidefinite physical blocks
``P(m)=S(m I+R)``.  Zero and nonzero PSD symmetrizers are checked explicitly.

The metric-complement existence and uniqueness statement is supplied by a
polar-decomposition proof in the paired note.  All scientific arithmetic is
exact SymPy arithmetic on the named fixture; the integer monotonic clock is
used only for the runtime gate.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
import sys
import time

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix


R = sp.Rational
MASS = sp.symbols("m", real=True)
LAM = sp.Symbol("lambda")

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10 as fixture


NOTE_INPUT = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
NOTE_PATH = ROOT / NOTE_INPUT
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK142_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK142_RUNNER = (
    "scripts/admissibility_dirac_kahler_carrier_reflection_blocker_"
    "2026_08_19.py"
)
BLOCK105_RUNNER = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)
HELPER_RUNNER = (
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_"
    "2026_09_10.py"
)
NO_GO_PATH = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block143-staggered-hermitian-pairing-20260819/"
    "NO_GO_LEDGER.md"
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py",
    ".claude/science/physics-loops/toe-axiom-closure-block143-staggered-hermitian-pairing-20260819/NO_GO_LEDGER.md",
)

RUNNER_BUDGET_SEC = 180
INPUT_SHA256 = {
    NOTE_INPUT: "9ed28242d97423deeb14aec71146c6bc0c94dd6226719655d6f4d7910ca5c520",
    AXIOM_PATH: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    REGISTRY_PATH: "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    BLOCK105_RUNNER: "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    HELPER_RUNNER: "0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87",
    BLOCK142_NOTE: "2329f133b90fefffc4270e37bfb581867c6280d47c4bb6280a148f0d7ad66cdc",
    BLOCK142_RUNNER: "651a921f79ed68e5c2c9c9a8be809a77bf39117d850b78717c44d04b9d649916",
    NO_GO_PATH: "00022146cb762adde7ea5d312a8997fa52914a8b6dac09cfaa200199c770af24",
}

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "break_squarefree_count",
    "claim_skew_mass_dependent",
    "break_x0_anticommutation",
    "break_anticommutant_dimension",
    "claim_x0_pairing_nonhermitian",
    "claim_adapted_hermitian",
    "break_half_exchange_rank",
    "wrong_jordan_type",
    "wrong_nonreal_count",
    "claim_positive_semidefinite_edge",
    "claim_census_weight_fixed",
    "break_metric_determinant",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "break_squarefree_count": "B",
    "claim_skew_mass_dependent": "B",
    "break_x0_anticommutation": "C",
    "break_anticommutant_dimension": "C",
    "claim_x0_pairing_nonhermitian": "C",
    "claim_adapted_hermitian": "D",
    "break_half_exchange_rank": "D",
    "wrong_jordan_type": "E",
    "wrong_nonreal_count": "E",
    "claim_positive_semidefinite_edge": "E",
    "claim_census_weight_fixed": "F",
    "break_metric_determinant": "G",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print(
            "GATES "
            + " ".join(
                f"{key}={'PASS' if value else 'FAIL'}"
                for key, _, value in self.results
            )
        )

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


def file_sha256(path: str) -> str | None:
    target = ROOT / path
    return hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else None


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def compact_note(text: str) -> str:
    return "".join(text.lower().split())


def no_float(value: object) -> bool:
    if isinstance(value, sp.MatrixBase):
        return not value.has(sp.Float)
    if isinstance(value, (tuple, list, set, frozenset)):
        return all(no_float(item) for item in value)
    if isinstance(value, dict):
        return all(no_float(key) and no_float(item) for key, item in value.items())
    return not sp.sympify(value).has(sp.Float)


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(value) == 0 for value in matrix)


def qrank(matrix: sp.MatrixBase) -> int:
    """Exact rank over QQ.

    The adapted involution and the operator-space systems below carry very
    long rationals, and SymPy's generic expression-level elimination is
    minutes slower on their products; the domain computation is the same
    exact arithmetic done in the rational field.
    """
    return DomainMatrix.from_Matrix(sp.expand(matrix)).convert_to(QQ).rank()


def charpoly(matrix: sp.MatrixBase) -> sp.Poly:
    """Exact characteristic polynomial over QQ."""
    coefficients = list(
        DomainMatrix.from_Matrix(sp.expand(matrix)).convert_to(QQ).charpoly()
    )
    return sp.Poly(coefficients, LAM, domain="QQ")


def inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) of a rational symmetric matrix."""
    roots = charpoly(matrix).real_roots()
    positive = sum(1 for root in roots if root > 0)
    negative = sum(1 for root in roots if root < 0)
    return (positive, matrix.rows - positive - negative, negative)


def flatten(matrix: sp.MatrixBase) -> list:
    return list(matrix)


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class AuthorityCertificate:
    actual_sha256: dict[str, str | None]
    all_inputs_present: bool


def authority_certificate() -> AuthorityCertificate:
    actual = {path: file_sha256(path) for path in INPUT_SHA256}
    return AuthorityCertificate(
        actual_sha256=actual,
        all_inputs_present=all(value is not None for value in actual.values()),
    )


# ---------------------------------------------------------------------------
# carrier machinery, reconstructed by the bounded fixture helper
# ---------------------------------------------------------------------------
LX = fixture.SPACE_EXTENT                 # 4
PHYS = fixture.PHYSICAL_TIME_EXTENT * LX  # 16 quotient sites
HALF = PHYS // 2                          # 8 sites in the positive-time half
ORIGINS = fixture.ORIGINS                 # ((0,0),(0,1),(1,0),(1,1))
INDEX = {origin: position for position, origin in enumerate(ORIGINS)}
DISPLAYED = fixture.DISPLAYED             # ((1,0),(1,1))
HEALING_WEIGHTS = fixture.HEALING_WEIGHTS # x  = (0, 0, 1/2, -1/3)
ALT_WEIGHTS = (sp.Integer(0), R(7, 3), R(-5, 11), sp.Integer(2))
IDENTITY = sp.eye(PHYS)

PLUS_SITES = list(range(HALF))           # the carrier half p = 0,1
MINUS_SITES = list(range(HALF, PHYS))    # p = 2,3
COVER_TIME_EVEN = tuple(
    origin for origin in ORIGINS if origin[0] % 2 == 0
)
# the anchor edge whose J is used as the Krylov base for the uniqueness cut
ANCHOR_EDGE = (0, 0)
NILPOTENT_PROBE = (0, 0)                 # a zero-dressing cover-time-even edge
SPLIT_PROBE = (INDEX[DISPLAYED[0]], INDEX[DISPLAYED[1]])   # the displayed edge

# the certificate constants this runner is claiming
DET_OFFDIAGONAL_BLOCK = R(1, 26542080)
NILPOTENT_JORDAN_TYPE = (3, 3, 1, 1)
NILPOTENT_INDEX = 3
CORNER_JORDAN_TYPE = (2, 2, 2, 2)
CORNER_INDEX = 2
ISOTROPIC_DIMENSION = 2
MAX_POSITIVE_INDEX = 6
NONREAL_PER_SPLIT_EDGE = 4
ADAPTED_ANTICOMMUTATOR_RANK = 16
HALF_EXCHANGE_RANK = 128
ATTAINED_INERTIA = (6, 0, 2)
BLOCK_INERTIA = (8, 0, 0)


def site(index: int) -> tuple[int, int]:
    return (index // LX, index % LX)


def site_index(time_coordinate: int, space_coordinate: int) -> int:
    return (time_coordinate % fixture.PHYSICAL_TIME_EXTENT) * LX + (
        space_coordinate % LX
    )


def staggered_parity() -> sp.Matrix:
    """X_0 = diag((-1)^(t+x)) on the 16 quotient sites, t = i//4, x = i%4."""
    return sp.diag(
        *[(-1) ** (index // LX + index % LX) for index in range(PHYS)]
    )


def is_diagonal(matrix: sp.MatrixBase) -> bool:
    return zero(
        matrix - sp.diag(*[matrix[k, k] for k in range(matrix.rows)])
    )


def build_carrier(metric: dict, shear_x, shear_t, weights) -> dict:
    """The 16 dressed edge actions of one (fixture, weight) pair.

    The Hodge carrier is the committed Block 105 staircase and does not depend
    on the connection fixture, so it is built once by the caller and threaded
    through in `metric`; only the connection data and the dressings move.
    """
    data = fixture.connection_data(shear_x, shear_t)
    differentials = data["d"]
    hodge = metric["hodge"]
    hodge_quotient = metric["H"]
    star = sp.expand(differentials[(0, 0)] - differentials[(1, 0)])
    weight = {origin: weights[INDEX[origin]] for origin in ORIGINS}
    edges: dict[tuple[int, int], sp.Matrix] = {}
    for left in ORIGINS:
        for right in ORIGINS:
            dressing = sp.expand((weight[right] - weight[left]) * star)
            edges[(INDEX[left], INDEX[right])] = sp.expand(
                fixture.quotient_action(
                    sp.expand(differentials[left] + dressing), hodge, MASS
                )
            )
    skew = {
        key: sp.expand(value - MASS * hodge_quotient)
        for key, value in edges.items()
    }
    return {
        "star": star,
        "edges": edges,
        "K": skew,
        "J": {
            key: sp.expand(metric["Hinv"] * value)
            for key, value in skew.items()
        },
        "zero_dressing_cover_time_even": tuple(
            sorted(
                (INDEX[left], INDEX[right])
                for left in COVER_TIME_EVEN
                for right in ORIGINS
                if weight[right] == weight[left]
            )
        ),
        "global_form": sum(
            1
            for value in edges.values()
            if zero(
                sp.expand(
                    value + value.H - 2 * MASS * hodge_quotient
                )
            )
        ),
    }


def nilpotency(
    matrix: sp.Matrix,
) -> tuple[bool, int, tuple[int, ...], tuple[int, ...]]:
    """(nilpotent?, index, Jordan block sizes, the full rank profile).

    The number of blocks of size >= j is rank(R^(j-1)) - rank(R^j), which is
    the exact rank profile; no eigenvalue extraction is needed.
    """
    size = matrix.rows
    ranks = [size]
    power = sp.eye(size)
    for _ in range(size):
        power = sp.expand(power * matrix)
        ranks.append(qrank(power))
    if ranks[-1] != 0:
        return (False, 0, (), ())
    index = min(j for j in range(1, size + 1) if ranks[j] == 0)
    blocks_at_least = [ranks[j - 1] - ranks[j] for j in range(1, size + 1)]
    sizes: list[int] = []
    for j in range(1, size + 1):
        exact = blocks_at_least[j - 1] - (
            blocks_at_least[j] if j < size else 0
        )
        sizes.extend([j] * exact)
    return (True, index, tuple(sorted(sizes, reverse=True)), tuple(ranks))


def spectral_report(current: sp.Matrix) -> dict:
    """The chart-indexed census entry of one edge's R = beta^-1 K[-,+].

    Both arms carry a two-dimensional totally isotropic subspace for every
    real symmetric symmetrizer S satisfying S*R = R^T*S:

      * nilpotent of index k, taking a = ceil(k/2) so that 2a >= k.  For
        u = R^a w and u' = R^a v the pairing u^T S u' = w^T S R^(2a) v
        = 0, so im(R^a) is isotropic; at the measured k = 3 that is im(R^2),
        of dimension 2.
      * squarefree with exactly 4 non-real eigenvalues, i.e. 2 conjugate
        pairs.  Taking one eigenvector from each pair, (lam - conj(lam))
        v^dagger S v = 0 forces v^dagger S v = 0, and the cross term vanishes
        because the two chosen eigenvalues are never conjugate.

    Their complex span is totally isotropic for the Hermitian extension
    z^dagger*S*w, whose inertia is the same (p, z, n) as the real form S.
    A real symmetric form of inertia (p, z, n) on an 8-space admits a totally
    isotropic subspace of dimension at most min(p, n) + z, so a 2-dimensional
    one forces p <= 6.  This excludes positive-definite S.  It does not exclude
    positive-semidefinite S, whose radical may contain the measured
    two-dimensional isotropic subspace.
    """
    poly = charpoly(current)
    size = current.rows
    if poly.as_expr() == LAM ** size:
        _, index, sizes, ranks = nilpotency(current)
        isotropic = ranks[(index + 1) // 2]
        return {
            "kind": "nilpotent",
            "index": index,
            "jordan": sizes,
            "nonreal": 0,
            "isotropic": isotropic,
            "squarefree": False,
            "bound": size - isotropic,
        }
    # ``real_roots`` retains algebraic multiplicity, including on degenerate
    # control fixtures; ``count_roots()`` would count only distinct roots.
    real_roots = len(poly.real_roots())
    nonreal = size - real_roots
    return {
        "kind": "split",
        "index": 0,
        "jordan": (),
        "nonreal": nonreal,
        "isotropic": nonreal // 2,
        "squarefree": sp.gcd(poly, poly.diff(LAM)).degree() == 0,
        "bound": size - nonreal // 2,
    }


def census_of(skews: dict, beta_inverse: sp.Matrix) -> dict:
    return {
        key: spectral_report(
            sp.expand(beta_inverse * value[MINUS_SITES, PLUS_SITES])
        )
        for key, value in skews.items()
    }


# ---------------------------------------------------------------------------
# tightness and PSD controls for exact symmetrizers
# ---------------------------------------------------------------------------
def nilpotent_jordan_change(current: sp.Matrix) -> sp.Matrix | None:
    """Exact C with current = C*diag(J3,J3,0,0)*C^-1, when available."""
    size = current.rows
    square = sp.expand(current * current)
    seeds: list[sp.Matrix] = []
    for column in range(size):
        vector = sp.zeros(size, 1)
        vector[column] = 1
        trial = seeds + [vector]
        images = sp.Matrix.hstack(*[sp.expand(square * v) for v in trial])
        if qrank(images) == len(trial):
            seeds.append(vector)
        if len(seeds) == 2:
            break
    if len(seeds) != 2:
        return None
    basis = []
    for vector in seeds:
        basis.extend(
            [sp.expand(square * vector), sp.expand(current * vector), vector]
        )
    for vector in current.nullspace():
        trial = basis + [vector]
        if qrank(sp.Matrix.hstack(*trial)) == len(trial):
            basis.append(vector)
        if len(basis) == size:
            break
    if len(basis) != size:
        return None
    change = sp.Matrix.hstack(*basis)
    jordan3 = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    if not zero(
        sp.expand(
            change * sp.diag(jordan3, jordan3, sp.zeros(2, 2)) * change.inv()
            - current
        )
    ):
        return None
    return change


def nilpotent_attainer(current: sp.Matrix) -> sp.Matrix | None:
    """An exact S with S=S^T, S*R=R^T*S and inertia (6,0,2)."""
    change = nilpotent_jordan_change(current)
    if change is None:
        return None
    swap3 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    inverse = change.inv()
    return sp.expand(
        inverse.T * sp.diag(swap3, swap3, sp.eye(2)) * inverse
    )


def nilpotent_psd_counterexample(current: sp.Matrix) -> sp.Matrix | None:
    """A nonzero PSD S for the measured (3,3,1,1) nilpotent probe."""
    change = nilpotent_jordan_change(current)
    if change is None:
        return None
    canonical = sp.diag(0, 0, 1, 0, 0, 1, 1, 1)
    inverse = change.inv()
    return sp.expand(inverse.T * canonical * inverse)


def split_attainer(current: sp.Matrix) -> sp.Matrix | None:
    """An exact S with S = S^T, S*R = R^T*S and inertia (6,0,2), R split.

    The Hankel matrix of the trace functional, S[i,j] = trace(R^(i+j)), obeys
    S*C = C^T*S for the companion matrix C of a nonderogatory R, and Hermite's
    theorem makes its signature the number of real roots.  Here that is
    4 real against 4 non-real, so the inertia is (6,0,2) and pulling S back
    through a Krylov basis gives a compatible form in the original basis.
    """
    size = current.rows
    powers = [sp.eye(size)]
    for _ in range(2 * size - 2):
        powers.append(sp.expand(powers[-1] * current))
    traces = [sp.trace(power) for power in powers]
    hankel = sp.Matrix(size, size, lambda i, j: traces[i + j])
    for seed in range(size):
        vector = sp.zeros(size, 1)
        vector[seed] = 1
        columns = [vector]
        for _ in range(size - 1):
            columns.append(sp.expand(current * columns[-1]))
        krylov = sp.Matrix.hstack(*columns)
        if krylov.det() != 0:
            inverse = krylov.inv()
            return sp.expand(inverse.T * hankel * inverse)
    return None


def admissible(symmetrizer: sp.Matrix, current: sp.Matrix) -> bool:
    """S is symmetric and symmetrizes R: S*R = R^T*S."""
    return bool(
        zero(symmetrizer - symmetrizer.T)
        and zero(sp.expand(symmetrizer * current - current.T * symmetrizer))
    )


def physical_block_bridge(symmetrizer: sp.Matrix, current: sp.Matrix) -> bool:
    """The algebraic P(m)=S(mI+R) is symmetric and also symmetrizes R."""
    physical = sp.expand(
        symmetrizer * (MASS * sp.eye(current.rows) + current)
    )
    return admissible(physical, current)


def symmetric_symmetrizer_dimension(current: sp.Matrix) -> int:
    """Dimension of real symmetric {S=S^T: S*R=R^T*S} over rational data."""
    basis = []
    for row in range(current.rows):
        for column in range(row, current.cols):
            unit = sp.zeros(current.rows)
            unit[row, column] = 1
            unit[column, row] = 1
            basis.append(unit)
    images = [flatten(sp.expand(unit * current - current.T * unit)) for unit in basis]
    system = sp.Matrix([list(row) for row in zip(*images)])
    return len(basis) - qrank(system)


# ---------------------------------------------------------------------------
# the metric-adapted scout Theta_ad and the half-exchange exclusion
# ---------------------------------------------------------------------------
def reflection_pairs() -> tuple[tuple[int, int], ...]:
    """The 8 two-cycles of the fixed-point-free site map (p,x) -> (3-p,-x)."""
    image = {
        index: site_index(
            3 - site(index)[0], -site(index)[1]
        )
        for index in range(PHYS)
    }
    return tuple(
        sorted({tuple(sorted((index, image[index]))) for index in range(PHYS)})
    )


def adapted_involution(hodge_quotient: sp.Matrix) -> sp.Matrix:
    """Theta_ad = 2*Pi_+ - I, Pi_+ the H_q-orthogonal projector on V_+."""
    plus_basis = sp.zeros(PHYS, HALF)
    for column, (left, right) in enumerate(reflection_pairs()):
        plus_basis[left, column] = 1
        plus_basis[right, column] = -1
    projector = sp.expand(
        plus_basis
        * (plus_basis.T * hodge_quotient * plus_basis).inv()
        * plus_basis.T
        * hodge_quotient
    )
    return sp.expand(2 * projector - IDENTITY)


def half_exchange_rank(current: sp.Matrix) -> int:
    """Rank of {X, J} = 0 on the 128-dim block-antidiagonal space.

    For X = [[0, U], [V, 0]] the two DIAGONAL blocks of {X, J} decouple into
    the Sylvester conditions U*J22 + J11*U = 0 and V*J11 + J22*V = 0.  Their
    joint rank already saturates the 128 unknowns, so the full 256-equation
    system has rank 128 too and the kernel is exactly zero; solving the two
    64x64 blocks instead of one 256x128 system is the cheap exact route.
    """
    upper = current[:HALF, :HALF]
    lower = current[HALF:, HALF:]
    total = 0
    for left, right in ((upper, lower), (lower, upper)):
        columns = []
        for row in range(HALF):
            for column in range(HALF):
                unit = sp.zeros(HALF, HALF)
                unit[row, column] = 1
                columns.append(flatten(sp.expand(unit * right + left * unit)))
        total += qrank(sp.Matrix([list(r) for r in zip(*columns)]))
    return total


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    # B: the skew split
    global_form_edges: int
    skew_real_antisymmetric: bool
    skew_mass_free: bool
    charpoly_even_edges: int
    charpoly_invertible_edges: int
    charpoly_squarefree_edges: int
    # C: the staggered involution
    x0_is_staggered_parity: bool
    x0_involution: bool
    x0_metric_symmetric: bool
    x0_anticommuting_edges: int
    x0_hermitian_pairing_edges: int
    krylov_span_dimension: int
    krylov_anticommutes: bool
    common_anticommutant_dimension: int
    common_anticommutant_is_x0: bool
    selfadjoint_anticommutant_dimension: int
    # D: the adapted scout and the half-exchange exclusion
    adapted_rational: bool
    adapted_involution: bool
    adapted_metric_selfadjoint: bool
    adapted_isometry: bool
    adapted_eigen_dimensions: tuple
    adapted_anticommutator_ranks: tuple
    adapted_is_diagonal: bool
    x0_is_diagonal: bool
    half_exchange_ranks: tuple
    # E: the definite-symmetrizer bound and PSD controls
    pairing_factorisation_edges: int
    nilpotent_edges: tuple
    predicted_nilpotent_edges: tuple
    nilpotent_jordan_types: frozenset
    nilpotent_indices: frozenset
    split_edge_count: int
    split_all_squarefree: bool
    nonreal_counts: frozenset
    isotropic_dimensions: frozenset
    positive_index_bounds: frozenset
    attained_inertias: tuple
    attainers_admissible: bool
    # F: the second weight control
    alt_nilpotent_edges: tuple
    alt_predicted_nilpotent_edges: tuple
    alt_split_edge_count: int
    alt_nilpotent_jordan_types: frozenset
    alt_nonreal_counts: frozenset
    alt_isotropic_dimensions: frozenset
    alt_positive_index_bounds: frozenset
    alt_x0_hermitian_pairing_edges: int
    census_is_weight_fixed: bool
    # G: metric complement and corners
    block_pp_inertia: tuple
    block_mm_inertia: tuple
    offdiagonal_determinant: sp.Expr
    corner_st0_nilpotent_edges: int
    corner_st0_jordan_types: frozenset
    corner_st0_indices: frozenset
    corner_sx0_split_edge_count: int
    corner_sx0_nonreal_counts: frozenset
    corner_sx0_jordan_types: frozenset
    corners_no_positive_definite: bool
    zero_psd_symmetrizer_admissible: bool
    nonzero_psd_symmetrizer_admissible: bool
    nonzero_psd_symmetrizer_inertia: tuple
    nilpotent_symmetrizer_dimension: int
    split_probe_symmetrizer_dimension: int
    physical_probe_bridge: bool
    # global
    exact_no_float: bool
    scope: dict


def measure() -> Facts:
    authority = authority_certificate()

    hodge = fixture.curved_hodge_cover()
    hodge_quotient = sp.expand(fixture.antiperiodic_quotient(hodge))
    metric = {
        "hodge": hodge,
        "H": hodge_quotient,
        "Hinv": hodge_quotient.inv(),
    }
    # beta = H_q[+,-]^T = H_q[-,+]; it is the mass-level pairing block and the
    # denominator of every R below, so it is inverted exactly once.
    beta = hodge_quotient[MINUS_SITES, PLUS_SITES]
    beta_inverse = beta.inv()

    # The four (fixture, weight) carriers below are the ONLY places a quotient
    # action is built; every later gate reads these cached dictionaries.
    primary = build_carrier(metric, fixture.S_X, fixture.S_T, HEALING_WEIGHTS)
    control = build_carrier(metric, fixture.S_X, fixture.S_T, ALT_WEIGHTS)
    corner_st0 = build_carrier(metric, fixture.S_X, sp.Integer(0), HEALING_WEIGHTS)
    corner_sx0 = build_carrier(metric, sp.Integer(0), fixture.S_T, HEALING_WEIGHTS)

    edges = primary["edges"]
    skews = primary["K"]
    currents = primary["J"]
    keys = sorted(edges)

    # --- B: the skew split -------------------------------------------------
    skew_real_antisymmetric = all(
        (not value.has(sp.I)) and zero(sp.expand(value + value.T))
        for value in skews.values()
    )
    skew_mass_free = all(
        MASS not in value.free_symbols for value in skews.values()
    )
    charpoly_even_edges = 0
    charpoly_invertible_edges = 0
    charpoly_squarefree_edges = 0
    for key in keys:
        poly = charpoly(currents[key])
        coefficients = poly.all_coeffs()
        if all(
            value == 0
            for position, value in enumerate(coefficients)
            if (PHYS - position) % 2
        ):
            charpoly_even_edges += 1
        if coefficients[-1] != 0:
            charpoly_invertible_edges += 1
        if sp.gcd(poly, poly.diff(LAM)).degree() == 0:
            charpoly_squarefree_edges += 1

    # --- C: the staggered involution ---------------------------------------
    parity = staggered_parity()
    x0_is_staggered_parity = all(
        parity[index, index]
        == (-1) ** (site(index)[0] + site(index)[1])
        for index in range(PHYS)
    ) and is_diagonal(parity)
    metric_parity = sp.expand(hodge_quotient * parity)
    x0_anticommuting_edges = sum(
        1
        for key in keys
        if zero(sp.expand(parity * currents[key] + currents[key] * parity))
    )
    x0_hermitian_pairing_edges = sum(
        1
        for key in keys
        if zero(
            sp.expand(parity.H * edges[key] - (parity.H * edges[key]).H)
        )
    )

    # Uniqueness.  charpoly(J_anchor) is squarefree (measured above), so
    # J_anchor is NONDEROGATORY and its centraliser is exactly the 16-
    # dimensional polynomial algebra Q[J_anchor].  X_0 is invertible and
    # anticommutes with J_anchor, so X -> X_0 X is a bijection from that
    # centraliser onto the FULL anticommutant of J_anchor inside the
    # 256-dimensional operator space.  Cutting that 16-dimensional space by
    # the anticommutation conditions of all sixteen J_ij is therefore an exact
    # rank certificate for the common anticommutant, and it leaves dimension 1.
    anchor = currents[ANCHOR_EDGE]
    powers = [IDENTITY]
    for _ in range(PHYS - 1):
        powers.append(sp.expand(powers[-1] * anchor))
    krylov = [sp.expand(parity * power) for power in powers]
    krylov_span_dimension = qrank(
        sp.Matrix([flatten(member) for member in krylov]).T
    )
    krylov_anticommutes = all(
        zero(sp.expand(member * anchor + anchor * member)) for member in krylov
    )
    rows = []
    for key in keys:
        current = currents[key]
        images = [
            sp.expand(member * current + current * member) for member in krylov
        ]
        for entry in range(PHYS * PHYS):
            rows.append(
                [image[entry // PHYS, entry % PHYS] for image in images]
            )
    cut = sp.Matrix(rows)
    common_anticommutant_dimension = len(krylov) - qrank(cut)
    nullspace = cut.nullspace()
    common_anticommutant_is_x0 = bool(
        len(nullspace) == 1
        and nullspace[0][0] != 0
        and all(value == 0 for value in list(nullspace[0])[1:])
    )

    # The independent checker route: impose H_q-self-adjointness first, i.e.
    # solve for the SYMMETRIC Y = H_q X directly.  136 unknowns instead of 256,
    # and it must land on the same one-dimensional answer.
    columns = []
    for row in range(PHYS):
        for column in range(row, PHYS):
            candidate = sp.zeros(PHYS, PHYS)
            candidate[row, column] = 1
            candidate[column, row] = 1
            image = []
            for key in keys:
                current = currents[key]
                product = sp.expand(candidate * current - current.T * candidate)
                image.extend(
                    product[i, j]
                    for i in range(PHYS)
                    for j in range(i + 1, PHYS)
                )
            columns.append(image)
    selfadjoint_system = sp.Matrix([list(r) for r in zip(*columns)])
    selfadjoint_anticommutant_dimension = (
        len(columns) - qrank(selfadjoint_system)
    )

    # --- D: the adapted scout and the half-exchange exclusion --------------
    adapted = adapted_involution(hodge_quotient)
    metric_adapted = sp.expand(hodge_quotient * adapted)
    adapted_anticommutator_ranks = tuple(
        sorted(
            {
                qrank(sp.expand(adapted * currents[key] + currents[key] * adapted))
                for key in keys
            }
        )
    )
    half_exchange_ranks = tuple(
        sorted({half_exchange_rank(currents[key]) for key in keys})
    )

    # --- E: the definite-symmetrizer bound ---------------------------------
    pairing_factorisation_edges = sum(
        1
        for key in keys
        if zero(
            sp.expand(
                edges[key][MINUS_SITES, PLUS_SITES]
                - beta
                * (
                    MASS * sp.eye(HALF)
                    + beta_inverse * skews[key][MINUS_SITES, PLUS_SITES]
                )
            )
        )
    )
    census = census_of(skews, beta_inverse)
    nilpotent_edges = tuple(
        sorted(key for key, value in census.items() if value["kind"] == "nilpotent")
    )
    split_keys = [key for key in keys if census[key]["kind"] == "split"]
    nilpotent_probe_current = sp.expand(
        beta_inverse * skews[NILPOTENT_PROBE][MINUS_SITES, PLUS_SITES]
    )
    split_probe_current = sp.expand(
        beta_inverse * skews[SPLIT_PROBE][MINUS_SITES, PLUS_SITES]
    )
    nilpotent_block = nilpotent_attainer(nilpotent_probe_current)
    split_block = split_attainer(split_probe_current)
    attainers_admissible = bool(
        nilpotent_block is not None
        and split_block is not None
        and admissible(nilpotent_block, nilpotent_probe_current)
        and admissible(split_block, split_probe_current)
        and census[NILPOTENT_PROBE]["kind"] == "nilpotent"
        and census[SPLIT_PROBE]["kind"] == "split"
    )
    attained_inertias = (
        inertia(nilpotent_block) if nilpotent_block is not None else (0, 0, 0),
        inertia(split_block) if split_block is not None else (0, 0, 0),
    )

    # The old inference from a two-dimensional isotropic subspace to
    # non-existence of PSD symmetrizers was false: an isotropic subspace may
    # lie in the radical.  Exhibit both the zero solution and a nonzero PSD
    # solution for the measured nilpotent Jordan type.  The nonzero example
    # is pulled from Jordan coordinates into the actual probe by congruence.
    # Neither example says that W=(S*beta^-1)^T is an admissible involution or
    # that the physical block P(m)=S*(m I+R) is PSD.
    jordan3 = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    canonical_nilpotent = sp.diag(jordan3, jordan3, sp.zeros(2, 2))
    zero_symmetrizer = sp.zeros(HALF)
    nonzero_psd_symmetrizer = nilpotent_psd_counterexample(
        nilpotent_probe_current
    )
    zero_psd_symmetrizer_admissible = admissible(
        zero_symmetrizer, nilpotent_probe_current
    )
    nonzero_psd_symmetrizer_admissible = bool(
        nonzero_psd_symmetrizer is not None
        and admissible(nonzero_psd_symmetrizer, nilpotent_probe_current)
    )
    nonzero_psd_symmetrizer_inertia = (
        inertia(nonzero_psd_symmetrizer)
        if nonzero_psd_symmetrizer is not None
        else (0, 0, 0)
    )
    nilpotent_symmetrizer_dimension = symmetric_symmetrizer_dimension(
        nilpotent_probe_current
    )
    split_probe_symmetrizer_dimension = symmetric_symmetrizer_dimension(
        split_probe_current
    )
    physical_probe_bridge_ok = bool(
        nonzero_psd_symmetrizer is not None
        and nilpotent_block is not None
        and split_block is not None
        and physical_block_bridge(nonzero_psd_symmetrizer, nilpotent_probe_current)
        and physical_block_bridge(nilpotent_block, nilpotent_probe_current)
        and physical_block_bridge(split_block, split_probe_current)
    )

    # --- F: weight robustness ----------------------------------------------
    alt_census = census_of(control["K"], beta_inverse)
    alt_nilpotent_edges = tuple(
        sorted(
            key for key, value in alt_census.items() if value["kind"] == "nilpotent"
        )
    )
    alt_split_keys = [
        key for key in sorted(alt_census) if alt_census[key]["kind"] == "split"
    ]
    alt_x0_hermitian_pairing_edges = sum(
        1
        for value in control["edges"].values()
        if zero(sp.expand(parity.H * value - (parity.H * value).H))
    )

    # --- G: metric complement and corners ----------------------------------
    st0_census = census_of(corner_st0["K"], beta_inverse)
    sx0_census = census_of(corner_sx0["K"], beta_inverse)
    corner_sx0_split = [
        key for key in sorted(sx0_census) if sx0_census[key]["kind"] == "split"
    ]
    # A nonzero nilpotent or a matrix with non-real spectrum cannot be
    # self-adjoint for a positive-definite symmetrizer.  This is only a no-PD
    # statement; singular PSD symmetrizers remain possible.
    corners_no_positive_definite = all(
        entry["kind"] == "split" and entry["nonreal"] > 0
        or entry["kind"] == "nilpotent" and entry["index"] > 1
        for corner in (st0_census, sx0_census)
        for entry in corner.values()
    )

    exact_no_float = no_float(
        (
            hodge_quotient,
            parity,
            adapted,
            beta,
            tuple(edges.values()),
            tuple(skews.values()),
            tuple(control["edges"].values()),
            tuple(corner_st0["edges"].values()),
            tuple(corner_sx0["edges"].values()),
            nilpotent_block if nilpotent_block is not None else sp.Integer(0),
            split_block if split_block is not None else sp.Integer(0),
            canonical_nilpotent,
            zero_symmetrizer,
            nonzero_psd_symmetrizer
            if nonzero_psd_symmetrizer is not None
            else sp.Integer(0),
            hodge_quotient[PLUS_SITES, MINUS_SITES].det(),
        )
    )

    return Facts(
        authority=authority,
        global_form_edges=primary["global_form"],
        skew_real_antisymmetric=skew_real_antisymmetric,
        skew_mass_free=skew_mass_free,
        charpoly_even_edges=charpoly_even_edges,
        charpoly_invertible_edges=charpoly_invertible_edges,
        charpoly_squarefree_edges=charpoly_squarefree_edges,
        x0_is_staggered_parity=x0_is_staggered_parity,
        x0_involution=zero(sp.expand(parity * parity - IDENTITY)),
        x0_metric_symmetric=zero(metric_parity - metric_parity.T),
        x0_anticommuting_edges=x0_anticommuting_edges,
        x0_hermitian_pairing_edges=x0_hermitian_pairing_edges,
        krylov_span_dimension=krylov_span_dimension,
        krylov_anticommutes=krylov_anticommutes,
        common_anticommutant_dimension=common_anticommutant_dimension,
        common_anticommutant_is_x0=common_anticommutant_is_x0,
        selfadjoint_anticommutant_dimension=selfadjoint_anticommutant_dimension,
        adapted_rational=not adapted.has(sp.I),
        adapted_involution=zero(sp.expand(adapted * adapted - IDENTITY)),
        adapted_metric_selfadjoint=zero(metric_adapted - metric_adapted.T),
        adapted_isometry=zero(
            sp.expand(adapted.H * hodge_quotient * adapted - hodge_quotient)
        ),
        adapted_eigen_dimensions=(
            PHYS - qrank(adapted - IDENTITY),
            PHYS - qrank(adapted + IDENTITY),
        ),
        adapted_anticommutator_ranks=adapted_anticommutator_ranks,
        adapted_is_diagonal=is_diagonal(adapted),
        x0_is_diagonal=is_diagonal(parity),
        half_exchange_ranks=half_exchange_ranks,
        pairing_factorisation_edges=pairing_factorisation_edges,
        nilpotent_edges=nilpotent_edges,
        predicted_nilpotent_edges=primary["zero_dressing_cover_time_even"],
        nilpotent_jordan_types=frozenset(
            census[key]["jordan"] for key in nilpotent_edges
        ),
        nilpotent_indices=frozenset(
            census[key]["index"] for key in nilpotent_edges
        ),
        split_edge_count=len(split_keys),
        split_all_squarefree=all(census[key]["squarefree"] for key in split_keys),
        nonreal_counts=frozenset(census[key]["nonreal"] for key in split_keys),
        isotropic_dimensions=frozenset(
            value["isotropic"] for value in census.values()
        ),
        positive_index_bounds=frozenset(
            value["bound"] for value in census.values()
        ),
        attained_inertias=attained_inertias,
        attainers_admissible=attainers_admissible,
        alt_nilpotent_edges=alt_nilpotent_edges,
        alt_predicted_nilpotent_edges=control["zero_dressing_cover_time_even"],
        alt_split_edge_count=len(alt_split_keys),
        alt_nilpotent_jordan_types=frozenset(
            alt_census[key]["jordan"] for key in alt_nilpotent_edges
        ),
        alt_nonreal_counts=frozenset(
            alt_census[key]["nonreal"] for key in alt_split_keys
        ),
        alt_isotropic_dimensions=frozenset(
            value["isotropic"] for value in alt_census.values()
        ),
        alt_positive_index_bounds=frozenset(
            value["bound"] for value in alt_census.values()
        ),
        alt_x0_hermitian_pairing_edges=alt_x0_hermitian_pairing_edges,
        census_is_weight_fixed=alt_nilpotent_edges == nilpotent_edges,
        block_pp_inertia=inertia(hodge_quotient[PLUS_SITES, PLUS_SITES]),
        block_mm_inertia=inertia(hodge_quotient[MINUS_SITES, MINUS_SITES]),
        offdiagonal_determinant=hodge_quotient[PLUS_SITES, MINUS_SITES].det(),
        corner_st0_nilpotent_edges=sum(
            1 for value in st0_census.values() if value["kind"] == "nilpotent"
        ),
        corner_st0_jordan_types=frozenset(
            value["jordan"]
            for value in st0_census.values()
            if value["kind"] == "nilpotent"
        ),
        corner_st0_indices=frozenset(
            value["index"]
            for value in st0_census.values()
            if value["kind"] == "nilpotent"
        ),
        corner_sx0_split_edge_count=len(corner_sx0_split),
        corner_sx0_nonreal_counts=frozenset(
            sx0_census[key]["nonreal"] for key in corner_sx0_split
        ),
        corner_sx0_jordan_types=frozenset(
            value["jordan"]
            for value in sx0_census.values()
            if value["kind"] == "nilpotent"
        ),
        corners_no_positive_definite=corners_no_positive_definite,
        zero_psd_symmetrizer_admissible=zero_psd_symmetrizer_admissible,
        nonzero_psd_symmetrizer_admissible=nonzero_psd_symmetrizer_admissible,
        nonzero_psd_symmetrizer_inertia=nonzero_psd_symmetrizer_inertia,
        nilpotent_symmetrizer_dimension=nilpotent_symmetrizer_dimension,
        split_probe_symmetrizer_dimension=split_probe_symmetrizer_dimension,
        physical_probe_bridge=physical_probe_bridge_ok,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = (
    "N5: per_element: on the primary displayed fixture Q_ij=m H_q+K_ij with K_ij real antisymmetric and m-free on all sixteen edges; H_q-skewness of J_ij structurally gives purely imaginary semisimple spectrum in conjugate plus/minus pairs and an even characteristic polynomial, while invertibility and squarefreeness are separate sixteen-edge fixture computations and are not structural consequences\n"
    "per_site: the fixed staggered site parity X_0 is H_q-self-adjoint, anticommutes with all sixteen primary-fixture J_ij, and makes X_0^dagger Q_ij Hermitian on all 16 primary-fixture edges; the one-dimensional common anticommutant proves uniqueness up to sign on the primary fixture only\n"
    "per_mode: the specified adapted scout fails the primary-fixture Hermiticity test and the primary block-antidiagonal system excludes a half-exchanging anticommutant; on the +1 eigenspace the mass contribution is m H and is positive only for m>0, while the paired polar-decomposition construction proves the unique positive-cross-block H-isometric half exchange from the stated A,B,C hypotheses\n"
    "per_block: for a real H-isometric half exchange whose physical block is symmetric, S=W^T beta is a real symmetric symmetrizer satisfying S R=R^T S, whereas the physical block is P(m)=S(m I+R); P(m) also symmetrizes R, so the positive index of either form is at most 6 on every primary edge, but zero and nonzero PSD algebraic S exist for the nilpotent Jordan form, whose real symmetric symmetrizer space has dimension 16 rather than 8, while the tested split probe has dimension 8 and two probes attain (6,0,2)\n"
    "lattice_wide: the chart-indexed census is 4 nilpotent plus 12 split at the primary weights and 2 plus 14 at the second tested weights; the two assignments and the s_t=0 and s_x=0 corner fixtures retain only the no-positive-definite bound, and neither an all-weight claim nor positivity of P(m) follows\n"
    "RESULT: the displayed primary fixture has a staggered Hermitian pairing and excludes positive-definite symmetrizers through the measured R spectra and positive-index bound; it does not exclude positive-semidefinite symmetrizers, does not turn S into P(m), and does not establish reflection positivity or a curved OS result\n"
    "DECISION_CUT: test the physical block P(m), admissible involution constraints, other weights and carriers, completions, the forced self-edges, coboundary admissibility, and the joint-lane program; no premise or audit disposition is adopted here\n"
    "TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero"
)


SCOPE_KEYS = (
    "staggered_parity",
    "fixture_uniqueness",
    "hermitian_fixture",
    "structural_spectral_limit",
    "census_chart_indexed",
    "census_zero_dressing",
    "census_cover_time_even",
    "two_weight_control",
    "isotropic_mechanism",
    "symmetrizer_not_physical_block",
    "positive_index_bound",
    "psd_counterexamples",
    "symmetrizer_dimensions",
    "polar_proof",
    "metric_complement_determinant",
    "corner_no_pd",
    "half_exchange_exclusion",
    "independence_disclosure",
    "os_no_go",
    "curved_os_no_go",
    "axiom",
    "firewalls",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_verbatim",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    compact = compact_note(note_text)
    return {
        "staggered_parity": "staggered site parity" in note,
        "fixture_uniqueness": (
            "unique up to sign on the primary fixture" in note
        ),
        "hermitian_fixture": (
            "hermitian on all 16 primary-fixture edges" in note
        ),
        "structural_spectral_limit": (
            "does not imply invertibility or squarefreeness" in note
        ),
        "census_chart_indexed": "chart-indexed" in note,
        "census_zero_dressing": "zero dressing" in note,
        "census_cover_time_even": "cover-time-even" in note,
        "two_weight_control": (
            "two tested weight assignments" in note
        ),
        "isotropic_mechanism": "totally isotropic" in note,
        "symmetrizer_not_physical_block": (
            "s=w^tbeta" in compact
            and "p(m) = s(m i + r)" in note
        ),
        "positive_index_bound": (
            "positive index" in note and "at most 6" in note
        ),
        "psd_counterexamples": (
            "zero psd symmetrizer" in note
            and "nonzero psd symmetrizer" in note
        ),
        "symmetrizer_dimensions": (
            "dimension 16" in note and "dimension 8" in note
        ),
        "polar_proof": (
            "polar decomposition" in note and "unique" in note
        ),
        "metric_complement_determinant": "26542080" in compact,
        # Whitespace-insensitive so the note may write s_t = 0 or s_t=0.
        "corner_no_pd": (
            "no-positive-definite bound survives" in note
            and ("s_t = 0" in note or "s_t=0" in compact)
        ),
        "half_exchange_exclusion": "no half-exchanging operator" in note,
        "independence_disclosure": "cross-context" in note,
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "firewalls": "firewall" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": (
            "no toe percentage moves" in note
            or "no toe percentage movement" in note
        ),
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        # Raw substring membership makes the printed eight-line fence
        # byte-identical to its note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
    }


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict[str, object]:
    expected_inputs = dict(INPUT_SHA256)
    claims: dict[str, object] = {
        "input_sha256": expected_inputs,
        "squarefree_edges": 16,
        "skew_is_mass_free": True,
        "x0_anticommuting_edges": 16,
        "common_anticommutant_dimension": 1,
        "x0_hermitian_edges": 16,
        "adapted_anticommutator_rank": ADAPTED_ANTICOMMUTATOR_RANK,
        "half_exchange_rank": HALF_EXCHANGE_RANK,
        "nilpotent_jordan_type": NILPOTENT_JORDAN_TYPE,
        "nonreal_per_split_edge": NONREAL_PER_SPLIT_EDGE,
        "positive_index_upper_bound": MAX_POSITIVE_INDEX,
        "census_is_weight_fixed": False,
        "offdiagonal_determinant": DET_OFFDIAGONAL_BLOCK,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        # Historical mutation name retained: corrupt the actual axiom-file pin.
        expected_inputs[AXIOM_PATH] = "0" * 64
    elif mutation == "stale_parent_authority":
        # Historical mutation name retained: corrupt the actual Block 142 pin.
        expected_inputs[BLOCK142_RUNNER] = "0" * 64
    elif mutation == "break_squarefree_count":
        claims["squarefree_edges"] = 15
    elif mutation == "claim_skew_mass_dependent":
        claims["skew_is_mass_free"] = False
    elif mutation == "break_x0_anticommutation":
        claims["x0_anticommuting_edges"] = 15
    elif mutation == "break_anticommutant_dimension":
        claims["common_anticommutant_dimension"] = 2
    elif mutation == "claim_x0_pairing_nonhermitian":
        claims["x0_hermitian_edges"] = 15
    elif mutation == "claim_adapted_hermitian":
        claims["adapted_anticommutator_rank"] = 0
    elif mutation == "break_half_exchange_rank":
        claims["half_exchange_rank"] = 127
    elif mutation == "wrong_jordan_type":
        claims["nilpotent_jordan_type"] = CORNER_JORDAN_TYPE
    elif mutation == "wrong_nonreal_count":
        claims["nonreal_per_split_edge"] = 2
    elif mutation == "claim_positive_semidefinite_edge":
        # Historical mutation name retained.  The corrected claim is the
        # positive-index bound, not a no-PSD claim.
        claims["positive_index_upper_bound"] = HALF
    elif mutation == "claim_census_weight_fixed":
        claims["census_is_weight_fixed"] = True
    elif mutation == "break_metric_determinant":
        claims["offdiagonal_determinant"] = R(1, 26542081)
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
def evaluate_gates(
    facts: Facts, claims: dict[str, object], elapsed_ns: int
) -> dict[str, bool]:
    authority = facts.authority
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
            "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py",
            ".claude/science/physics-loops/toe-axiom-closure-block143-staggered-hermitian-pairing-20260819/NO_GO_LEDGER.md",
        )
        and set(INPUT_SHA256) == set(AUDIT_INPUT_PATHS)
        and authority.all_inputs_present
        and authority.actual_sha256 == claims["input_sha256"]
    )

    gate_b = bool(
        facts.global_form_edges == PHYS
        and facts.skew_real_antisymmetric
        and facts.skew_mass_free == bool(claims["skew_is_mass_free"])
        and facts.charpoly_even_edges == PHYS
        and facts.charpoly_invertible_edges == PHYS
        and facts.charpoly_squarefree_edges == claims["squarefree_edges"]
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.x0_is_staggered_parity
        and facts.x0_involution
        and facts.x0_metric_symmetric
        and facts.x0_anticommuting_edges == claims["x0_anticommuting_edges"]
        and facts.x0_hermitian_pairing_edges == claims["x0_hermitian_edges"]
        and facts.krylov_span_dimension == PHYS
        and facts.krylov_anticommutes
        and facts.common_anticommutant_dimension
        == claims["common_anticommutant_dimension"]
        and facts.common_anticommutant_is_x0
        and facts.selfadjoint_anticommutant_dimension == 1
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.adapted_rational
        and facts.adapted_involution
        and facts.adapted_metric_selfadjoint
        and facts.adapted_isometry
        and facts.adapted_eigen_dimensions == (HALF, HALF)
        and facts.adapted_anticommutator_ranks
        == (claims["adapted_anticommutator_rank"],)
        and not facts.adapted_is_diagonal
        and facts.x0_is_diagonal
        and facts.half_exchange_ranks == (claims["half_exchange_rank"],)
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.pairing_factorisation_edges == PHYS
        and facts.nilpotent_edges == facts.predicted_nilpotent_edges
        and len(facts.nilpotent_edges) == 4
        and facts.nilpotent_jordan_types
        == frozenset({tuple(claims["nilpotent_jordan_type"])})
        and facts.nilpotent_indices == frozenset({NILPOTENT_INDEX})
        and facts.split_edge_count == 12
        and facts.split_all_squarefree
        and facts.nonreal_counts
        == frozenset({claims["nonreal_per_split_edge"]})
        and facts.isotropic_dimensions == frozenset({ISOTROPIC_DIMENSION})
        and facts.positive_index_bounds
        == frozenset({claims["positive_index_upper_bound"]})
        and facts.attainers_admissible
        and facts.attained_inertias == (ATTAINED_INERTIA, ATTAINED_INERTIA)
        and facts.zero_psd_symmetrizer_admissible
        and facts.nonzero_psd_symmetrizer_admissible
        and facts.nonzero_psd_symmetrizer_inertia == (4, 4, 0)
        and facts.nilpotent_symmetrizer_dimension == 16
        and facts.split_probe_symmetrizer_dimension == 8
        and facts.physical_probe_bridge
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.alt_nilpotent_edges == facts.alt_predicted_nilpotent_edges
        and len(facts.alt_nilpotent_edges) == 2
        and facts.alt_split_edge_count == 14
        and facts.alt_nilpotent_jordan_types
        == frozenset({NILPOTENT_JORDAN_TYPE})
        and facts.alt_nonreal_counts == frozenset({NONREAL_PER_SPLIT_EDGE})
        and facts.alt_isotropic_dimensions == frozenset({ISOTROPIC_DIMENSION})
        and facts.alt_positive_index_bounds
        == frozenset({MAX_POSITIVE_INDEX})
        and facts.alt_x0_hermitian_pairing_edges == PHYS
        and facts.census_is_weight_fixed
        == bool(claims["census_is_weight_fixed"])
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.block_pp_inertia == BLOCK_INERTIA
        and facts.block_mm_inertia == BLOCK_INERTIA
        and facts.offdiagonal_determinant == claims["offdiagonal_determinant"]
        and facts.corner_st0_nilpotent_edges == PHYS
        and facts.corner_st0_jordan_types == frozenset({CORNER_JORDAN_TYPE})
        and facts.corner_st0_indices == frozenset({CORNER_INDEX})
        and facts.corner_sx0_split_edge_count == 12
        and facts.corner_sx0_nonreal_counts
        == frozenset({NONREAL_PER_SPLIT_EDGE})
        and facts.corner_sx0_jordan_types == frozenset({CORNER_JORDAN_TYPE})
        and facts.corners_no_positive_definite
        and facts.exact_no_float
    )

    required = tuple(claims["required_scope_keys"])
    gate_h = bool(
        set(facts.scope) == set(required)
        and all(facts.scope.values())
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and N5_FENCE.count("\n") == 7
        and elapsed_ns <= RUNNER_BUDGET_SEC * 1_000_000_000
    )

    return {
        "A": gate_a,
        "B": gate_b,
        "C": gate_c,
        "D": gate_d,
        "E": gate_e,
        "F": gate_f,
        "G": gate_g,
        "H": gate_h,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted,
    # so a mutation can only rewrite a CLAIM.  No gate can cascade into
    # another because no gate feeds a measurement.
    facts = measure()
    elapsed_ns = time.monotonic_ns() - started_ns

    raw_gates = evaluate_gates(facts, build_claims(""), elapsed_ns)
    gate_values = dict(raw_gates)
    if mutation:
        target = MUTATION_GATE[mutation]
        gate_values = evaluate_gates(
            facts, build_claims(mutation), elapsed_ns
        )
        changed = {
            key for key in raw_gates if raw_gates[key] != gate_values[key]
        }
        if changed - {target} or gate_values[target]:
            raise AssertionError(
                "mutation did not fail exactly its own gate"
            )

    checks = Checks()
    checks.check(
        "A-authority",
        "every literal audit input is present and bound to its actual filesystem SHA-256, without a moving ref or ancestry premise",
        gate_values["A"],
    )
    checks.check(
        "B-skew-split",
        "on the primary fixture every healed edge action splits as Q_ij=m*H_q+K_ij with K_ij real antisymmetric and m-free on 16/16; the measured J_ij=H_q^{-1}K_ij characteristic polynomials are even, invertible and squarefree on 16/16, while only purely imaginary semisimple spectrum in conjugate plus/minus pairs and an even characteristic polynomial are structural",
        gate_values["B"],
    )
    checks.check(
        "C-staggered-involution",
        "on the primary fixture the staggered site parity X_0=diag((-1)^(t+x)) is H_q-self-adjoint, anticommutes with all 16 J_ij and makes X_0^dagger*Q_ij Hermitian on all 16 edges; its common anticommutant is one-dimensional, so uniqueness up to sign is fixture-level",
        gate_values["C"],
    )
    checks.check(
        "D-adapted-scout-and-half-exchange",
        "the specified metric-adapted scout is a rational H_q-isometry of eigendimensions 8/8 and fails the fixture Hermiticity test with rank 16; the primary-fixture block-antidiagonal anticommutation system has rank 128, so no half-exchanging operator in that tested space anticommutes with J",
        gate_values["D"],
    )
    checks.check(
        "E-positivity-obstruction",
        "Q_ij[-,+]=beta*(m*I+R_ij) on 16/16; for a real H-isometric half exchange with symmetric physical block, S=W^T*beta obeys S*R=R^T*S, while P(m)=S*(m*I+R) is separately checked symmetric and also symmetrizes R; the primary census bounds positive index by 6, two probes attain (6,0,2), explicit zero and nonzero PSD algebraic S counterexamples refute a generic no-PSD inference, and the real symmetric symmetrizer spaces have dimensions 16 and 8 on the nilpotent and split probes",
        gate_values["E"],
    )
    checks.check(
        "F-weight-robustness",
        "at the second tested weight assignment the chart-indexed census shifts to 14 split plus 2 nilpotent, exactly the new zero-dressing cover-time-even locus, while X_0 remains Hermitian on 16/16 and the positive-index-at-most-6 bound reproduces; no all-weight theorem is claimed",
        gate_values["F"],
    )
    checks.check(
        "G-metric-complement-and-corners",
        "H_q[+,+] and H_q[-,-] are positive definite with det H_q[+,-]=1/26542080 exactly; at the two tested shear corners the spectral census still excludes positive-definite symmetrizers, without excluding singular PSD symmetrizers or deciding P(m)=S*(m*I+R)",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the note states fixture and structural scopes separately, distinguishes S from P(m), records the PSD counterexamples and 16/8 symmetrizer dimensions, proves the polar construction, preserves the firewalls, and contains the exact N5 fence",
        gate_values["H"],
    )
    checks.report()
    print(N5_FENCE)
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
