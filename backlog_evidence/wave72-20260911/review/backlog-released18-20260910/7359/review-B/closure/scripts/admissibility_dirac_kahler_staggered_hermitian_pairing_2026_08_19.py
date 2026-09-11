#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.py
"""Block 143: the staggered Hermitian pairing on the Block 141 healed atlas.

Block 142 certified that the healed action carries an exact positive-definite
atlas-global quadratic form H_q that NO signed lattice reflection preserves,
and named the metric-adapted involutions as the live next question: H_q is
positive definite, so H_q-self-adjoint involutions exist -- do they give the
healed formulation an OS structure?  This runner answers it, and the answer
splits cleanly:

  * HERMITICITY IS ACHIEVED, and by an object nobody had to search for.  On
    the healed atlas Q_ij + Q_ij^dagger = 2*m*H_q, so Q_ij = m*H_q + K_ij, and
    K_ij is REAL ANTISYMMETRIC and m-free on all 16 ordered edges.  Writing
    J_ij = H_q^{-1} K_ij, the charpoly of every J_ij is even, squarefree and
    invertible.  The staggered site parity X_0 = diag((-1)^(t+x)) is then an
    exact rational involution with H_q X_0 symmetric and {X_0, J_ij} = 0, so
    X_0^dagger Q_ij is Hermitian on ALL 16 edges: the arc's first exactly
    Hermitian curved pairing, and it is Hermitian atlas-globally.  It is also
    the ONLY one: the common anticommutant of the sixteen J_ij inside the
    256-dimensional operator space is exactly one-dimensional, so X_0 is
    unique up to sign;
  * the metric-adapted scout fails where X_0 succeeds.  Theta_ad = 2*Pi_+ - I,
    built from the H_q-orthogonal projector onto ker(theta - I), is a rational
    H_q-self-adjoint involution with eigendimensions 8/8, but {Theta_ad, J_ij}
    has rank 16 on every edge, so its pairing is never Hermitian.  And no
    reflection with a geometric half-space reading can repair that: on the
    128-dimensional block-antidiagonal space the anticommutation conditions
    have rank 128 on all 16 edges, i.e. no half-exchanging operator
    anticommutes with J.  X_0 buys Hermiticity by being diagonal, which is
    exactly what a time reflection is not;
  * POSITIVITY IS NOT ACHIEVED, and the obstruction is chart-indexed.  Every
    Hermitian block factors through Q_ij[-,+] = beta*(m*I + R_ij) with
    beta = H_q[+,-]^T, and R_ij is P-self-adjoint for every admissible P.  On
    the healing family R_ij is nilpotent with Jordan type (3,3,1,1) and index
    exactly 3 on precisely the four edges with ZERO DRESSING and a
    COVER-TIME-EVEN left chart, and on the other twelve it is squarefree with
    exactly four non-real eigenvalues.  Either way there is a two-dimensional
    totally isotropic subspace -- im(R^2) in the nilpotent case, one
    eigenvector from each conjugate pair in the split case -- so the maximum
    positive index of any admissible Hermitian block is 6 < 8 on 16/16 edges,
    and the bound is tight: exact constructions attain (6,0,2) on both a
    nilpotent and a split edge.  A positive-definite block is impossible and
    a positive-semidefinite one is impossible too, because the isotropic
    directions are exact null directions of every admissible block;
  * the census is chart-indexed, not weight-fixed, and the conclusion is
    weight-robust.  At Block 142's control weights x' = (0,7/3,-5/11,2) the
    nilpotent locus shrinks from four edges to two -- exactly the zero-dressing
    cover-time-even edges of the new weights -- while X_0 keeps 16/16
    Hermiticity and the maximum-positive-index-6 conclusion reproduces
    verbatim; and
  * the corners survive.  H_q[+,+] and H_q[-,-] are positive definite with
    det H_q[+,-] = 1/26542080 exactly, so the metric complement is nowhere
    degenerate and the whole obstruction sits in the skew part.  At s_t = 0,
    where the Block 141 healing itself dies, every edge R becomes nilpotent of
    Jordan type (2,2,2,2) and index 2, and at s_x = 0 the non-real split
    persists on twelve edges: the obstruction survives both corners.

Every scientific comparison below is exact SymPy arithmetic at the committed
fixture s_x = 3/5, s_t = 4/5 with a symbolic real mass m; the integer monotonic
clock is used only for the runtime gate.

HYPOTHESES, named and not imported: (H1) "metric-adapted" means H_q-self-adjoint,
i.e. H_q*Theta Hermitian, equivalently Theta^dagger H_q Theta = H_q for an
involution.  (H2) the pairing operator of an involution Theta is
Theta^dagger Q_ij, and the block-level pairing of a half-exchanging
Theta = [[0, W^{-1}],[W, 0]] is P = W^dagger Q_ij[-,+]; no swap completion and
no normalisation is applied.  (H3) the carrier, the atlas and the healing
weights are the committed Block 105/141 ones; nothing is re-optimised here.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys
import time

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix


R = sp.Rational
MASS = sp.symbols("m", real=True)
LAM = sp.Symbol("lambda")

_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# This fallback keeps the scratchpad draft executable before it is moved to
# scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path(
        "/Users/jonBridger/Projects/Physics-baremetal-probes/"
        ".claude/worktrees/gravity-toe-lane-work-427b0b"
    )
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19 as b142

b141 = b142.b141
b137 = b142.b137
b134 = b142.b134


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
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
BLOCK142_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_carrier_reflection_blocker_"
    "2026_08_19.txt"
)
BLOCK141_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK141_RUNNER = (
    "scripts/admissibility_dirac_kahler_coboundary_healing_family_"
    "2026_08_19.py"
)
PARENT_ARTIFACTS = (
    BLOCK142_NOTE,
    BLOCK142_RUNNER,
    BLOCK142_CACHE,
    BLOCK141_NOTE,
    BLOCK141_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py",
    "logs/runner-cache/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 142 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block142-carrier-reflection-blocker-20260819"
)
# Landing supervisor: replace this placeholder with the Block 142 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF, which is
# a real and verifiable binding; the immutable commit pin lands with the block.
PARENT_COMMIT = "503cf8dabdfca5d6adc962cdc047846d1d417a77"
# Block 141's tip: a real ancestor that predates the Block 142 artifacts and is
# therefore the honest "stale pin" control for the authority mutation.
STALE_PARENT_COMMIT = "2d92a7252bb85ed4090e0fc76032f674e51c6236"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

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


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    """The blob at a path in a commit, or "" when the path is absent there.

    Absence is a real answer here: the stale-pin control deliberately probes a
    commit that predates some of the pinned artifacts.
    """
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def is_hash(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{40}", value) is not None


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
    return b142.no_float(value)


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
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool


def resolved_parent_commit() -> str:
    return PARENT_COMMIT if is_hash(PARENT_COMMIT) else git_output(
        "rev-parse", PARENT_REF
    )


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB
    )

    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(
        commit_blob(parent, path) for path in PARENT_ARTIFACTS
    )
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, path) for path in PARENT_ARTIFACTS
    )
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT),
        bool(
            is_hash(parent)
            and is_ancestor(parent, "HEAD")
            and (
                not is_hash(PARENT_COMMIT)
                or git_output("rev-parse", PARENT_REF) == PARENT_COMMIT
            )
        ),
        bool(
            len(committed_blobs) == 5
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
        ),
        bool(
            len(stale_blobs) == 5
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
    )


# ---------------------------------------------------------------------------
# carrier machinery, imported wholesale from the committed Blocks 142/141/137/134
# ---------------------------------------------------------------------------
LX = b134.SPACE_EXTENT                   # 4
PHYS = b142.PHYS                         # 16 quotient sites
HALF = b142.HALF                         # 8 sites in the positive-time half
ORIGINS = b142.ORIGINS                   # ((0,0),(0,1),(1,0),(1,1))
INDEX = b142.INDEX
DISPLAYED = b142.DISPLAYED               # ((1,0),(1,1))
HEALING_WEIGHTS = b141.HEALING_WEIGHTS   # x  = (0, 0, 1/2, -1/3)
ALT_WEIGHTS = b142.ALT_WEIGHTS           # x' = (0, 7/3, -5/11, 2)
IDENTITY = b142.IDENTITY

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
    data = b137.connection_data(shear_x, shear_t)
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
                b137.quotient_action(
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

    Both arms carry a two-dimensional totally isotropic subspace for EVERY
    admissible Hermitian block P (one with P Hermitian and P*R = R^dagger*P):

      * nilpotent of index k, taking a = ceil(k/2) so that 2a >= k.  For
        u = R^a w and u' = R^a v the pairing u^dagger P u' = w^dagger P R^(2a) v
        = 0, so im(R^a) is isotropic; at the measured k = 3 that is im(R^2),
        of dimension 2.
      * squarefree with exactly 4 non-real eigenvalues, i.e. 2 conjugate
        pairs.  Taking one eigenvector from each pair, (lam - conj(lam))
        v^dagger P v = 0 forces v^dagger P v = 0, and the cross term vanishes
        because the two chosen eigenvalues are never conjugate.

    A Hermitian form of inertia (p, z, n) on an 8-space admits a totally
    isotropic subspace of dimension at most min(p, n) + z, so a 2-dimensional
    one forces p <= 6: no admissible block is positive definite, and none is
    positive semidefinite either, because the isotropic vectors are exact null
    directions.
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
    real_roots = poly.count_roots()
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
# tightness: exact admissible blocks of inertia (6,0,2)
# ---------------------------------------------------------------------------
def nilpotent_attainer(current: sp.Matrix) -> sp.Matrix | None:
    """An exact P with P = P^T, P*R = R^T*P and inertia (6,0,2), R ~ (3,3,1,1).

    Two length-3 Jordan chains plus two kernel vectors put R in the canonical
    form diag(J3, J3, 0, 0); the canonical compatible form of a size-3
    nilpotent block is the antidiagonal S3 (inertia (2,0,1)), so
    diag(S3, S3, I2) has inertia (6,0,2) and pulls back to a compatible P.
    This is the checker's targeted construction, not a random search.
    """
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
    swap3 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    if not zero(
        sp.expand(
            change * sp.diag(jordan3, jordan3, sp.zeros(2, 2)) * change.inv()
            - current
        )
    ):
        return None
    inverse = change.inv()
    return sp.expand(
        inverse.T * sp.diag(swap3, swap3, sp.eye(2)) * inverse
    )


def split_attainer(current: sp.Matrix) -> sp.Matrix | None:
    """An exact P with P = P^T, P*R = R^T*P and inertia (6,0,2), R split.

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


def admissible(block: sp.Matrix, current: sp.Matrix) -> bool:
    """P is a legitimate pairing block for R: symmetric and R-self-adjoint."""
    return bool(
        zero(block - block.T)
        and zero(sp.expand(block * current - current.T * block))
    )


# ---------------------------------------------------------------------------
# the metric-adapted scout Theta_ad and the half-exchange exclusion
# ---------------------------------------------------------------------------
def reflection_pairs() -> tuple[tuple[int, int], ...]:
    """The 8 two-cycles of the fixed-point-free site map (p,x) -> (3-p,-x)."""
    image = {
        index: b142.site_index(
            3 - b142.site(index)[0], -b142.site(index)[1]
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
    main_head: str
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
    # E: the PSD obstruction
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
    # F: weight robustness
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
    corners_blocked: bool
    # global
    exact_no_float: bool
    scope: dict


def measure() -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)

    hodge = b134.curved_hodge_cover()
    hodge_quotient = sp.expand(b134.antiperiodic_quotient(hodge))
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
    primary = build_carrier(metric, b134.S_X, b134.S_T, HEALING_WEIGHTS)
    control = build_carrier(metric, b134.S_X, b134.S_T, ALT_WEIGHTS)
    corner_st0 = build_carrier(metric, b134.S_X, sp.Integer(0), HEALING_WEIGHTS)
    corner_sx0 = build_carrier(metric, sp.Integer(0), b134.S_T, HEALING_WEIGHTS)

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
        == (-1) ** (b142.site(index)[0] + b142.site(index)[1])
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

    # --- E: the PSD obstruction --------------------------------------------
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
    # "blocked" = no admissible block can be positive semidefinite, because
    # every edge is either non-real-split or nilpotent of index > 1.
    corners_blocked = all(
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
            hodge_quotient[PLUS_SITES, MINUS_SITES].det(),
        )
    )

    return Facts(
        main_head=main_head,
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
        corners_blocked=corners_blocked,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = "N5: per_element: on the Block 142 atlas-global form every dressed edge action splits exactly as Q_ij = m H_q + K_ij with K_ij REAL ANTISYMMETRIC and m-FREE on all 16 ordered edges, so J_ij = H_q^{-1} K_ij is H_q-skew and charpoly(J_ij) is EVEN, INVERTIBLE and SQUAREFREE on 16/16, forced structurally because H_q is positive definite and K_ij is real antisymmetric, giving simple purely imaginary spectrum\nper_site: the involution X_0 = diag((-1)^(t+x)) -- THE STAGGERED SITE PARITY, entries in {-1,+1} on the diagonal -- is H_q-self-adjoint and satisfies {X_0, J_ij} = 0 EXACTLY on all 16 edges, so X_0^dagger Q_ij is HERMITIAN atlas-globally, the arc's first Hermitian curved pairing, and X_0 is UNIQUE UP TO SIGN because the common anticommutant of all sixteen J_ij is exactly one-dimensional, and it is weight- and shear-independent\nper_mode: the adapted-involution scout Theta_ad = 2 Pi_+ - I built from the H_q-orthogonal projector onto ker(theta - I) is rational and H_q-orthogonal with eigendimensions 8/8, but its half-space reading FAILS -- delocalized diagonal blocks, and the V_+ restriction is OS-VACUOUS, positive for every involution -- and adapted involutions of theta's type FAIL Hermiticity with anticommutator rank 16 on 16/16, so the Hermiticity criterion is {Theta, J} = 0 and X_0 is its essentially unique solution\nper_block: every Hermitian block pairing P makes R = beta^{-1} K[-,+] P-self-adjoint with beta = H_q[+,-]^T, from Q[-,+] = beta(m I + R) and P R = R^T P, so a positive-DEFINITE P would force R real-diagonalizable while the SEMIDEFINITE case closes via exact isotropic/null directions -- each conjugate pair of non-real eigenvalues forcing v^dag P v = 0, the nilpotent case supplying the exact P-null direction R^2 w -- and the CHART-INDEXED census has R nilpotent of Jordan type (3,3,1,1) at index 3 exactly on the edges with ZERO DRESSING AND LEFT CHART cover-time-even and squarefree with exactly 4 non-real eigenvalues (two conjugate pairs) elsewhere, giving 12 split + 4 nilpotent at x = (0,0,1/2,-1/3) and 14 + 2 at x' = (0,7/3,-5/11,2), so the census is WEIGHT-DEPENDENT while the CONCLUSION IS WEIGHT-ROBUST: a two-dimensional totally isotropic subspace exists on every edge, the maximum positive index is 6 < 8 on all 16 edges with 6 attained at inertia (6,0,2) on both a split and a nilpotent edge, and NO Hermitian block pairing is positive semidefinite\nlattice_wide: H_q[+,+] and H_q[-,-] are positive definite with inertia (8,0,0) each and det H_q[+,-] = 1/26542080 = 1/(2^16 3^4 5) != 0, so the geometric-mean theorem gives a UNIQUE half-exchanging H_q-adapted involution with positive-definite mass block and THE OBSTRUCTION LIVES ENTIRELY IN THE SKEW/K SECTOR, not in the metric, while at operator level charpoly(J) squarefree makes J nonderogatory (commutant = Q[J], dim 16; anticommutant = X_0 Q[J], dim 16) and the anticommutation conditions on the 128-dimensional block-antidiagonal space have full rank 128, so NO half-exchanging operator anticommutes with J -- X_0 itself is diagonal, the extreme opposite of half-exchanging -- though at BLOCK level an 8-real-dimensional family of half-exchanging Hermitian pairings exists, all blocked by the same R-spectrum certificate\nRESULT: on the displayed atlas, fixtures and staircase carrier the staggered site parity is the unique-up-to-sign metric-adapted involution making the healed pairing Hermitian atlas-globally, and no Hermitian block pairing of the displayed construction is positive semidefinite; K_ij is m-free and the certificates are m-independent, at s_t = 0 every edge's R becomes nilpotent of Jordan type (2,2,2,2) at index 2 so the obstruction SURVIVES with the sharper bound of positive index at most 4, and at s_x = 0 the non-real split persists with the nilpotent locus degrading to (2,2,2,2), so like Block 142's blocker this obstruction does not collapse at s_t -> 0 and the skew sector joins the carrier as non-shear-reducible structure\nDECISION_CUT: execute the skew-sector program by curing or circumventing the R spectrum; test shear-free and alternative carriers as constructions rather than controls; apply a completion; decide the two forced self-edges and the admissibility class of coboundary dressings; execute the joint-lane program; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero"


SCOPE_KEYS = (
    "staggered_parity",
    "staggered_unique",
    "hermitian_headline",
    "census_chart_indexed",
    "census_zero_dressing",
    "census_cover_time_even",
    "weight_robust_bound",
    "isotropic_mechanism",
    "metric_complement_determinant",
    "metric_complement_skew",
    "corner_survival",
    "half_exchange_exclusion",
    "definite_and_semidefinite",
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
        "staggered_unique": "unique up to sign" in note,
        "hermitian_headline": (
            "first hermitian curved pairing" in note
            or "hermitian atlas-globally" in note
        ),
        "census_chart_indexed": "chart-indexed" in note,
        "census_zero_dressing": "zero dressing" in note,
        "census_cover_time_even": "cover-time-even" in note,
        "weight_robust_bound": (
            "maximum positive index" in note and "6" in note
        ),
        "isotropic_mechanism": "totally isotropic" in note,
        "metric_complement_determinant": "26542080" in compact,
        "metric_complement_skew": "skew" in note,
        # Whitespace-insensitive so the note may write s_t = 0 or s_t=0.
        "corner_survival": (
            "survives" in note
            and ("s_t = 0" in note or "s_t=0" in compact)
        ),
        "half_exchange_exclusion": "no half-exchanging operator" in note,
        "definite_and_semidefinite": (
            "positive-definite" in note
            and ("null direction" in note or "null vector" in note)
        ),
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
    claims: dict[str, object] = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "squarefree_edges": 16,
        "skew_is_mass_free": True,
        "x0_anticommuting_edges": 16,
        "common_anticommutant_dimension": 1,
        "x0_hermitian_edges": 16,
        "adapted_anticommutator_rank": ADAPTED_ANTICOMMUTATOR_RANK,
        "half_exchange_rank": HALF_EXCHANGE_RANK,
        "nilpotent_jordan_type": NILPOTENT_JORDAN_TYPE,
        "nonreal_per_split_edge": NONREAL_PER_SPLIT_EDGE,
        "max_positive_index": MAX_POSITIVE_INDEX,
        "census_is_weight_fixed": False,
        "offdiagonal_determinant": DET_OFFDIAGONAL_BLOCK,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
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
        claims["max_positive_index"] = HALF
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
    parent_blobs_ok = (
        authority.parent_artifact_blobs
        if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs
    )
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py",
            "logs/runner-cache/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.txt",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py",
        )
        and PARENT_ARTIFACTS
        == (
            BLOCK142_NOTE,
            BLOCK142_RUNNER,
            BLOCK142_CACHE,
            BLOCK141_NOTE,
            BLOCK141_RUNNER,
        )
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
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
        == frozenset({claims["max_positive_index"]})
        and facts.attainers_admissible
        and facts.attained_inertias == (ATTAINED_INERTIA, ATTAINED_INERTIA)
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
        and facts.corners_blocked
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
        and elapsed_ns <= 500 * 1_000_000_000
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
        "main plus the committed Block 142 note/runner/cache and Block 141 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-skew-split",
        "every healed edge action splits as Q_ij=m*H_q+K_ij with K_ij real antisymmetric and m-free on 16/16, and J_ij=H_q^{-1}K_ij has an even, invertible and squarefree characteristic polynomial on 16/16",
        gate_values["B"],
    )
    checks.check(
        "C-staggered-involution",
        "the staggered site parity X_0=diag((-1)^(t+x)) satisfies X_0^2=I with H_q*X_0 symmetric and {X_0,J_ij}=0 on 16/16, making X_0^dagger*Q_ij Hermitian on 16/16, and it is unique up to sign: the common anticommutant of the sixteen J_ij inside the 256-dimensional operator space has dimension exactly 1",
        gate_values["C"],
    )
    checks.check(
        "D-adapted-scout-and-half-exchange",
        "the metric-adapted Theta_ad=2*Pi_+-I is a rational H_q-orthogonal involution of eigendimensions 8/8 whose anticommutator with every J_ij has rank 16, so its pairing is never Hermitian, and on the 128-dimensional block-antidiagonal space the anticommutation conditions have rank 128 on 16/16 edges: no half-exchanging operator anticommutes with J, while X_0 is diagonal",
        gate_values["D"],
    )
    checks.check(
        "E-positivity-obstruction",
        "Q_ij[-,+]=beta*(m*I+R_ij) with beta=H_q[+,-]^T on 16/16, R_ij is nilpotent of Jordan type (3,3,1,1) and index 3 exactly on the chart-indexed zero-dressing cover-time-even locus (4 edges) and squarefree with exactly 4 non-real eigenvalues on the other 12, every edge carries a two-dimensional totally isotropic subspace, and the maximum positive index of an admissible Hermitian block is 6<8 on 16/16, attained at (6,0,2) on both a nilpotent and a split edge",
        gate_values["E"],
    )
    checks.check(
        "F-weight-robustness",
        "at the control weights x'=(0,7/3,-5/11,2) the chart-indexed census shifts to 14 split plus 2 nilpotent, exactly the new zero-dressing cover-time-even locus, while X_0 keeps Hermiticity on 16/16 and the maximum-positive-index-6 conclusion reproduces",
        gate_values["F"],
    )
    checks.check(
        "G-metric-complement-and-corners",
        "H_q[+,+] and H_q[-,-] are positive definite with det H_q[+,-]=1/26542080 exactly, and the obstruction survives both corners: all 16 edges nilpotent of Jordan type (2,2,2,2) and index 2 at s_t=0, and the 4-non-real split persisting on 12 edges at s_x=0",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the staggered parity and its uniqueness, the Hermitian headline, the chart-indexed census, the weight-robust bound, the isotropic mechanism, the metric complement, the corner survival, the half-exchange exclusion, the definite/semidefinite wording, the disclosures, the firewalls, and the exact N5 fence are present",
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
