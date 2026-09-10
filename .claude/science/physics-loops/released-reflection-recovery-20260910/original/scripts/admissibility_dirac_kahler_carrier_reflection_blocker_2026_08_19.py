#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py
"""Block 142: the carrier reflection blocker for the Block 141 healed atlas.

Block 141 landed the coboundary healing family Omega_ij = (x_j-x_i)*Omega* with
Omega* = d_(0,0)-d_(1,0) and x = (0,0,1/2,-1/3) on the committed four-chart
Block 105 atlas, and named reflection positivity of the HEALED action as its
next question.  This runner answers it, and the answer is a blocker with an
exact cause:

  * the healed atlas does carry an atlas-global quadratic form.  Every dressed
    edge action obeys Q_ij + Q_ij^dagger = 2*m*H_q on all 16 ordered edges,
    because the coboundary correction Delta* = quotient_correction(Omega*) is
    exactly anti-Hermitian of rank 16 and s_t-only; H_q is positive definite
    with inertia (16,0,0) and every leading principal minor positive.  What
    fails to glue is the skew part, and the obstruction is now exact and
    complete: dim span{Q_i - Q_0} = 2 with the sum rule
    Q_(0,0) + Q_(0,1) - Q_(1,0) - Q_(1,1) = 0, a dimension-2 versus
    dimension-1 count that no weight vector can close;
  * no reflection symmetry survives.  H_q is parameter-free and has 15
    distinct absolute-row fingerprints whose sole repeat is {(1,1),(3,3)}; a
    backtracking search over the necessary condition |H_q[pi i, pi j]| =
    |H_q[i,j]| returns the identity and nothing else, while every physical
    time reflection of the 16 quotient sites moves at least 12 of them.
    Independently, all 256 signed lattice reflections (t,x) -> (b-t, a-x) with
    sign twists descend through the antiperiodic quotient and exactly 0 of
    them preserve H_q; the canonical theta has a defect of rank 16 with
    maximum entry 3/16 and no free symbols;
  * the cause is the curved carrier, and it splits into TWO DECOUPLED
    properties.  A shear-free but non-constant carrier (0, nu(t)) gives 16/16
    Hermitian healed pairings even though theta is not a Hodge symmetry there;
    a constant carrier makes theta an exact Hodge symmetry yet leaves only
    1/16 Hermitian at nonzero constant shear; the committed staircase
    v_{(3t+x) mod 8}, which hits all 8 indices with 8 distinct values, gives
    0/16 and no symmetry;
  * below the blocker the pairing is never positive semidefinite.  With
    P_ij = [theta*Q_ij]_{++} on the half carrier {p=0,1} the anti-Hermitian
    part has rank 8 on all 16 edges, and the Hermitian part has A[1,1] = 0 and
    A[1,2] = -19*m/160 identically in (m, w, s_x, s_t), so the {1,2} principal
    minor is exactly -361*m^2/25600; the fixture-mass inertia census is exactly
    {(2,0,6),(4,0,4),(6,0,2)} and the m=0 corner closes through the
    vanishing-diagonal row, with inertia (0,4,4) at (m,s_t) = (0,0);
  * the certificate is weight-free: the alternative weights
    x' = (0, 7/3, -5/11, 2) reproduce every number, and the self-edges keep
    Omega_ii = 0 and therefore the undressed chart actions; and
  * the rider breaks.  The healing itself is s_t-only and dies at s_t = 0, but
    H_q, the theta-defect and A[1,2] carry no s_t at all, so the blocker
    survives s_t -> 0.

Every scientific comparison below is exact SymPy arithmetic at the committed
fixture s_x = 3/5, s_t = 4/5 with a symbolic real mass m; the integer monotonic
clock is used only for the runtime gate.

HYPOTHESES, named and not imported: (H1) the OS pairing convention is
P = [theta*Q]_{++} with the half carrier {p=0,1}.  (H2) no swap completion or
normalization is applied.  (H3) theta ranges over signed site maps of the
cover; metric-adapted involutions are not searched.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys
import time

import sympy as sp


R = sp.Rational
MASS = sp.symbols("m", real=True)
SX, ST = sp.symbols("s_x s_t", real=True)
WEIGHT = sp.symbols("w", real=True)
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

import admissibility_dirac_kahler_twisted_scouting_record_2026_08_19 as b137
import admissibility_dirac_kahler_connection_residual_theorem_2026_08_17 as b134
import admissibility_dirac_kahler_coboundary_healing_family_2026_08_19 as b141

b105 = b134.block105


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK141_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK141_RUNNER = (
    "scripts/admissibility_dirac_kahler_coboundary_healing_family_"
    "2026_08_19.py"
)
BLOCK141_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_coboundary_healing_family_"
    "2026_08_19.txt"
)
BLOCK134_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
BLOCK134_RUNNER = (
    "scripts/admissibility_dirac_kahler_connection_residual_theorem_"
    "2026_08_17.py"
)
PARENT_ARTIFACTS = (
    BLOCK141_NOTE,
    BLOCK141_RUNNER,
    BLOCK141_CACHE,
    BLOCK134_NOTE,
    BLOCK134_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py",
    "logs/runner-cache/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 141 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block141-coboundary-healing-family-20260819"
)
# Landing supervisor: replace this placeholder with the Block 141 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF, which is
# a real and verifiable binding; the immutable commit pin lands with the block.
PARENT_COMMIT = "2d92a7252bb85ed4090e0fc76032f674e51c6236"
# Block 140's tip: a real ancestor that predates the Block 141 artifacts and is
# therefore the honest "stale pin" control for the authority mutation.
STALE_PARENT_COMMIT = "2d92a7252bb85ed4090e0fc76032f674e51c6236"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "break_sum_rule",
    "break_hodge_inertia",
    "claim_preserver_exists",
    "break_fingerprint_count",
    "break_theta_defect_rank",
    "conflate_the_causes",
    "break_hermitian_count",
    "break_pairing_entry",
    "claim_positive_semidefinite_edge",
    "break_inertia_census",
    "claim_weight_dependence",
    "claim_blocker_is_st_only",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "break_sum_rule": "B",
    "break_hodge_inertia": "B",
    "claim_preserver_exists": "C",
    "break_fingerprint_count": "C",
    "break_theta_defect_rank": "C",
    "conflate_the_causes": "D",
    "break_hermitian_count": "D",
    "break_pairing_entry": "E",
    "claim_positive_semidefinite_edge": "E",
    "break_inertia_census": "E",
    "claim_weight_dependence": "F",
    "claim_blocker_is_st_only": "G",
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
    if isinstance(value, sp.MatrixBase):
        return not value.has(sp.Float)
    if isinstance(value, (tuple, list, set, frozenset)):
        return all(no_float(item) for item in value)
    if isinstance(value, dict):
        return all(
            no_float(key) and no_float(item) for key, item in value.items()
        )
    return not sp.sympify(value).has(sp.Float)


def canonical(value: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.expand(value))


def zero(matrix: sp.MatrixBase) -> bool:
    """Exact vanishing: expand first, fall back to the committed test."""
    if all(sp.expand(value) == 0 for value in matrix):
        return True
    return b134.matrix_zero(matrix)


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.expand((matrix + matrix.H) / 2)


def anti(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.expand((matrix - matrix.H) / 2)


def inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) of a Hermitian matrix."""
    coefficients = sp.Poly(
        sp.expand(matrix.charpoly(LAM).as_expr()), LAM
    ).all_coeffs()
    n_zero = 0
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
        n_zero += 1
    if len(coefficients) <= 1:
        return (0, n_zero, 0)
    reduced = sp.Poly(coefficients, LAM)
    return (
        sp.polys.polytools.count_roots(reduced, 0, sp.oo),
        n_zero,
        sp.polys.polytools.count_roots(reduced, -sp.oo, 0),
    )


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
# carrier machinery, imported wholesale from the committed Blocks 141/137/134
# ---------------------------------------------------------------------------
SIZE = b134.SIZE                     # 32 cover sites
COVER_T = b134.COVER_TIME_EXTENT     # 8
PHYS_T = b134.PHYSICAL_TIME_EXTENT   # 4
LX = b134.SPACE_EXTENT               # 4
PHYS = PHYS_T * LX                   # 16 quotient sites
HALF = PHYS // 2                     # 8 sites in the positive-time half
ORIGINS = b134.ORIGINS
DISPLAYED = b134.DISPLAYED
INDEX = {origin: position for position, origin in enumerate(ORIGINS)}
COVER_TIME_ODD = tuple(origin for origin in ORIGINS if origin[0] % 2 == 1)
HEALING_WEIGHTS = b141.HEALING_WEIGHTS               # x  = (0,0,1/2,-1/3)
ALT_WEIGHTS = (sp.Integer(0), R(7, 3), R(-5, 11), sp.Integer(2))

IDENTITY = sp.eye(PHYS)
LIFT = sp.Matrix.vstack(-IDENTITY, IDENTITY)          # 32x16, image = quotient
SELECT = sp.Matrix.hstack(sp.zeros(PHYS), IDENTITY)   # 16x32
PLUS = sp.zeros(PHYS, HALF)                           # carrier: slices p=0,1
for _k in range(HALF):
    PLUS[_k, _k] = 1

# the certificate constants this runner is claiming
HODGE_INERTIA = (16, 0, 0)
PAIRING_ENTRY = -R(19, 160) * MASS
MINOR_CERTIFICATE = -R(361, 25600) * MASS**2
INERTIA_CENSUS = frozenset({(2, 0, 6), (4, 0, 4), (6, 0, 2)})
CORNER_INERTIA = (0, 4, 4)
THETA_DEFECT_MAX_ENTRY = R(3, 16)
FINGERPRINT_REPEAT = ((1, 1), (3, 3))
GLUING_SPAN_DIMENSION = 2
SIGNED_REFLECTION_FAMILY = 256


def site(index: int) -> tuple[int, int]:
    return (index // LX, index % LX)


def site_index(time_coordinate: int, space_coordinate: int) -> int:
    return (time_coordinate % PHYS_T) * LX + (space_coordinate % LX)


def canonical_theta() -> sp.Matrix:
    """theta = -P[(p,x) -> (3-p,-x)]: the descended link reflection."""
    matrix = sp.zeros(PHYS)
    for index in range(PHYS):
        time_coordinate, space_coordinate = site(index)
        matrix[
            site_index(3 - time_coordinate, -space_coordinate), index
        ] = -1
    return matrix


def signed_cover_reflection(
    shift_t: int, shift_x: int, overall: int, alpha: int, beta: int
) -> sp.Matrix:
    """(t,x) -> (shift_t-t, shift_x-x) with the sign twist (-1)^(al t + be x)."""
    matrix = sp.zeros(SIZE)
    for time_coordinate in range(COVER_T):
        for space_coordinate in range(LX):
            matrix[
                b134.cover_index(
                    (shift_t - time_coordinate) % COVER_T,
                    (shift_x - space_coordinate) % LX,
                ),
                b134.cover_index(time_coordinate, space_coordinate),
            ] = overall * (-1) ** (alpha * time_coordinate + beta * space_coordinate)
    return matrix


def descend(cover_operator: sp.Matrix) -> sp.Matrix | None:
    """Push a cover operator through the antiperiodic quotient, or None."""
    candidate = SELECT * cover_operator * LIFT
    if zero(sp.expand(cover_operator * LIFT - LIFT * candidate)):
        return candidate
    return None


def hodge_from_field(field: dict) -> sp.Matrix:
    """b134.curved_hodge_cover's builder on an arbitrary overlap field."""
    result = sp.zeros(SIZE)
    for time_coordinate in range(COVER_T):
        for space_coordinate in range(LX):
            shear, volume = field[
                (time_coordinate % PHYS_T, space_coordinate)
            ]
            embedding = b134.cover_embedding(time_coordinate, space_coordinate)
            result += (
                embedding * b105.shear_hodge(shear, volume) * embedding.T / 4
            )
    return sp.simplify(result)


def pairing(theta: sp.Matrix, action: sp.Matrix) -> sp.Matrix:
    """P = [theta*Q]_{++} on the half carrier {p=0,1}."""
    return sp.expand(PLUS.T * theta * action * PLUS)


def preservers_of_absolute_value(
    absolute: list[list[sp.Expr]],
) -> tuple[tuple[int, ...], ...]:
    """Every 16-site permutation pi with |H[pi i, pi j]| = |H[i,j]| for all i,j.

    Ported from the independent block-142 checker.  Preserving H_q with any
    diagonal sign twist forces this entrywise absolute-value condition, so the
    search is a sound over-approximation of the signed stabiliser: whatever it
    fails to find cannot exist.  Backtracking extends pi one site at a time and
    prunes on the diagonal and on every already-assigned column, which is what
    keeps the 16! space to a few hundred nodes.
    """
    solutions: list[tuple[int, ...]] = []

    def extend(assignment: list[int], used: set[int], position: int) -> None:
        if position == PHYS:
            solutions.append(tuple(assignment))
            return
        for candidate in range(PHYS):
            if candidate in used:
                continue
            if absolute[position][position] != absolute[candidate][candidate]:
                continue
            if any(
                absolute[position][other] != absolute[candidate][assignment[other]]
                for other in range(position)
            ):
                continue
            assignment.append(candidate)
            used.add(candidate)
            extend(assignment, used, position + 1)
            assignment.pop()
            used.discard(candidate)

    extend([], set(), 0)
    return tuple(solutions)


def minimum_sites_moved_by_a_time_reflection() -> int:
    """min over (a,b) of |{sites moved by (p,x) -> (b-p, a-x)}|."""
    return min(
        sum(
            1
            for index in range(PHYS)
            if site_index(
                shift_t - site(index)[0], shift_x - site(index)[1]
            )
            != index
        )
        for shift_t in range(PHYS_T)
        for shift_x in range(LX)
    )


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # B: the global form
    global_form_edges: int
    affine_edges: int
    delta_anti_hermitian: bool
    delta_rank: int
    delta_symbolic_free_symbols: frozenset
    delta_vanishes_at_zero_st: bool
    hodge_inertia: tuple
    leading_minors_positive: bool
    gluing_span_dimension: int
    sum_rule_holds: bool
    chart_differences_nonzero: bool
    # C: the reflection blocker
    hodge_free_symbols: frozenset
    fingerprint_count: int
    fingerprint_repeat: tuple
    absolute_preservers: tuple
    minimum_reflection_moves: int
    reflection_family_size: int
    reflection_family_descending: int
    reflection_family_preserving: int
    theta_is_involution: bool
    theta_exchanges_halves: bool
    theta_defect_rank: int
    theta_defect_max_entry: sp.Expr
    theta_defect_free_symbols: frozenset
    # D: the decoupled cause controls
    staircase_law: bool
    staircase_indices: tuple
    staircase_distinct_values: int
    shear_free_symmetry: bool
    shear_free_hermitian_count: int
    constant_symmetry: bool
    constant_hermitian_count: int
    staircase_symmetry: bool
    staircase_hermitian_count: int
    causes_decoupled: bool
    # E: the positivity certificate
    anti_hermitian_ranks: tuple
    pairing_diagonal_entry: sp.Expr
    pairing_offdiagonal_entry: sp.Expr
    pairing_minor: sp.Expr
    pairing_entry_free_symbols: frozenset
    vanishing_row_impossible: bool
    inertia_census: frozenset
    psd_edge_count: int
    displayed_edge_inertia: tuple
    corner_inertia: tuple
    # F: weight freedom
    alt_pairing_diagonal_entry: sp.Expr
    alt_pairing_offdiagonal_entry: sp.Expr
    alt_anti_hermitian_ranks: tuple
    alt_inertia_census: frozenset
    self_edge_dressings_vanish: bool
    self_edge_actions_undressed: bool
    # G: the rider break
    blocker_is_st_only: bool
    # global
    exact_no_float: bool
    scope: dict


def measure() -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)

    fixture = b137.connection_data(b134.S_X, b134.S_T)
    symbolic = b137.connection_data(SX, ST)
    differentials = fixture["d"]
    hodge = b134.curved_hodge_cover()
    hodge_quotient = sp.expand(b134.antiperiodic_quotient(hodge))
    theta = canonical_theta()

    star = sp.expand(differentials[(0, 0)] - differentials[(1, 0)])
    delta_star = sp.expand(b137.quotient_correction(star, hodge))
    symbolic_star = sp.expand(
        symbolic["d"][(0, 0)] - symbolic["d"][(1, 0)]
    )
    symbolic_delta = sp.expand(
        b137.quotient_correction(symbolic_star, hodge)
    )

    weights = {origin: HEALING_WEIGHTS[INDEX[origin]] for origin in ORIGINS}
    alt_weights = {origin: ALT_WEIGHTS[INDEX[origin]] for origin in ORIGINS}

    # --- B: the atlas-global quadratic form -------------------------------
    # The 16 dressed edge actions are built ONCE here with symbolic mass and
    # reused by every later gate; nothing below recomputes a quotient action
    # on the committed carrier.
    edges: dict[tuple[int, int], sp.Matrix] = {}
    global_form_edges = 0
    affine_edges = 0
    charts: dict[tuple[int, int], sp.Matrix] = {}
    self_edge_dressings_vanish = True
    for left in ORIGINS:
        for right in ORIGINS:
            dressing = sp.expand((weights[right] - weights[left]) * star)
            action = sp.expand(
                b137.quotient_action(
                    sp.expand(differentials[left] + dressing), hodge, MASS
                )
            )
            edges[(INDEX[left], INDEX[right])] = action
            if left == right:
                charts[left] = action
                self_edge_dressings_vanish &= zero(dressing)
            if zero(
                sp.expand(
                    action + action.H - 2 * MASS * hodge_quotient
                )
            ):
                global_form_edges += 1
    # the affine identity Q_ij = Q_i + (x_j-x_i)*Delta*, checked on all 16
    for left in ORIGINS:
        for right in ORIGINS:
            if zero(
                sp.expand(
                    edges[(INDEX[left], INDEX[right])]
                    - charts[left]
                    - (weights[right] - weights[left]) * delta_star
                )
            ):
                affine_edges += 1
    self_edge_actions_undressed = all(
        zero(
            sp.expand(
                charts[origin]
                - b137.quotient_action(differentials[origin], hodge, MASS)
            )
        )
        for origin in ORIGINS
    )

    hodge_inertia = inertia(hodge_quotient)
    leading_minors_positive = all(
        sp.sign(hodge_quotient[:size, :size].det()) == 1
        for size in range(1, PHYS + 1)
    )
    differences = [
        sp.expand(charts[origin] - charts[ORIGINS[0]]) for origin in ORIGINS[1:]
    ]
    span = sp.Matrix.hstack(
        *(sp.Matrix(PHYS**2, 1, list(entry)) for entry in differences)
    )
    gluing_span_dimension = span.rank()
    sum_rule_holds = zero(
        sp.expand(
            charts[(0, 0)] + charts[(0, 1)] - charts[(1, 0)] - charts[(1, 1)]
        )
    )
    chart_differences_nonzero = all(
        not zero(entry) for entry in differences
    )

    # --- C: the reflection blocker ----------------------------------------
    absolute = [
        [sp.Abs(hodge_quotient[row, column]) for column in range(PHYS)]
        for row in range(PHYS)
    ]
    fingerprints = [
        tuple(sorted(absolute[row]))
        for row in range(PHYS)
    ]
    classes = Counter(fingerprints)
    fingerprint_repeat = tuple(
        sorted(
            site(row)
            for row in range(PHYS)
            if classes[fingerprints[row]] > 1
        )
    )
    absolute_preservers = preservers_of_absolute_value(absolute)
    minimum_reflection_moves = minimum_sites_moved_by_a_time_reflection()

    family_size = 0
    family_descending = 0
    family_preserving = 0
    for shift_t in range(COVER_T):
        for shift_x in range(LX):
            for overall in (1, -1):
                for alpha in (0, 1):
                    for beta in (0, 1):
                        family_size += 1
                        descended = descend(
                            signed_cover_reflection(
                                shift_t, shift_x, overall, alpha, beta
                            )
                        )
                        if descended is None:
                            continue
                        family_descending += 1
                        if zero(
                            sp.expand(
                                descended.H * hodge_quotient * descended
                                - hodge_quotient
                            )
                        ):
                            family_preserving += 1

    theta_defect = sp.expand(
        theta.H * hodge_quotient * theta - hodge_quotient
    )
    theta_defect_max_entry = max(sp.Abs(value) for value in theta_defect)

    # --- D: the decoupled cause controls ----------------------------------
    field = b105.overlap_field()
    staircase_law = all(
        field[(time_coordinate, space_coordinate)]
        == b105.OVERLAP_SHEARS[(3 * time_coordinate + space_coordinate) % 8]
        for time_coordinate in range(PHYS_T)
        for space_coordinate in range(LX)
    )
    staircase_indices = tuple(
        sorted(
            {
                (3 * time_coordinate + space_coordinate) % 8
                for time_coordinate in range(PHYS_T)
                for space_coordinate in range(LX)
            }
        )
    )
    staircase_distinct_values = len(set(field.values()))

    def carrier_report(carrier_field: dict) -> tuple[bool, int]:
        """(theta a Hodge symmetry?, how many of 16 healed pairings Hermitian)."""
        carrier_hodge = hodge_from_field(carrier_field)
        carrier_quotient = sp.expand(
            b134.antiperiodic_quotient(carrier_hodge)
        )
        symmetry = zero(
            sp.expand(
                theta.H * carrier_quotient * theta - carrier_quotient
            )
        )
        carrier_delta = sp.expand(
            b137.quotient_correction(star, carrier_hodge)
        )
        hermitian = 0
        for left in ORIGINS:
            base = sp.expand(
                b137.quotient_action(differentials[left], carrier_hodge, MASS)
            )
            for right in ORIGINS:
                action = sp.expand(
                    base + (weights[right] - weights[left]) * carrier_delta
                )
                block = pairing(theta, action)
                if zero(sp.expand(block - block.H)):
                    hermitian += 1
        return symmetry, hermitian

    shear_free_field = {
        (time_coordinate, space_coordinate): (
            sp.Integer(0),
            b105.OVERLAP_SHEARS[time_coordinate][1],
        )
        for time_coordinate in range(PHYS_T)
        for space_coordinate in range(LX)
    }
    constant_field = {
        (time_coordinate, space_coordinate): (R(3, 5), R(4, 5))
        for time_coordinate in range(PHYS_T)
        for space_coordinate in range(LX)
    }
    shear_free_symmetry, shear_free_hermitian_count = carrier_report(
        shear_free_field
    )
    constant_symmetry, constant_hermitian_count = carrier_report(
        constant_field
    )
    staircase_symmetry = zero(theta_defect)
    staircase_hermitian_count = sum(
        1
        for key in edges
        if zero(
            sp.expand(
                pairing(theta, edges[key]) - pairing(theta, edges[key]).H
            )
        )
    )
    # the two properties order the two control carriers oppositely, so they
    # are not the same property: theta-invariance of the Hodge is neither
    # necessary nor sufficient for a Hermitian healed pairing.
    causes_decoupled = bool(
        constant_symmetry
        and not shear_free_symmetry
        and shear_free_hermitian_count > constant_hermitian_count
    )

    # --- E: the positivity certificate ------------------------------------
    anti_hermitian_ranks = tuple(
        sorted({anti(pairing(theta, action)).rank() for action in edges.values()})
    )
    inertias = {
        key: inertia(herm(pairing(theta, action)).subs(MASS, b134.MASS))
        for key, action in edges.items()
    }
    inertia_census = frozenset(inertias.values())
    psd_edge_count = sum(
        1 for value in inertias.values() if value[2] == 0
    )
    displayed_edge_inertia = inertias[
        (INDEX[DISPLAYED[0]], INDEX[DISPLAYED[1]])
    ]

    diagonal_entries = set()
    offdiagonal_entries = set()
    minors = set()
    entry_free_symbols: set = set()
    vanishing_row_impossible = True
    corner_inertia = (0, 0, 0)
    for left in ORIGINS:
        action = sp.expand(
            b137.quotient_action(
                sp.expand(symbolic["d"][left] + WEIGHT * symbolic_star),
                hodge,
                MASS,
            )
        )
        block = herm(pairing(theta, action))
        diagonal_entries.add(sp.simplify(block[1, 1]))
        offdiagonal_entries.add(sp.simplify(block[1, 2]))
        minors.add(
            sp.simplify(
                block[1, 1] * block[2, 2] - block[1, 2] * block[2, 1]
            )
        )
        entry_free_symbols |= sp.simplify(block[1, 2]).free_symbols
        row = [sp.simplify(block[1, column]) for column in range(HALF)]
        vanishing_row_impossible &= (
            sp.solve(row, [MASS, WEIGHT], dict=True) == []
        )
        if left == (0, 0):
            corner_inertia = inertia(
                sp.expand(
                    block.subs({MASS: 0, ST: 0, SX: b134.S_X})
                )
            )
    pairing_diagonal_entry = (
        diagonal_entries.pop() if len(diagonal_entries) == 1 else sp.nan
    )
    pairing_offdiagonal_entry = (
        offdiagonal_entries.pop() if len(offdiagonal_entries) == 1 else sp.nan
    )
    pairing_minor = minors.pop() if len(minors) == 1 else sp.nan

    # --- F: weight freedom -------------------------------------------------
    # The affine identity certified above makes the alternative-weight edges
    # exact linear combinations of already-measured objects; no new quotient
    # action is built, and nothing is assumed.
    alt_edges = {
        (INDEX[left], INDEX[right]): sp.expand(
            charts[left]
            + (alt_weights[right] - alt_weights[left]) * delta_star
        )
        for left in ORIGINS
        for right in ORIGINS
    }
    alt_diagonal = set()
    alt_offdiagonal = set()
    for action in alt_edges.values():
        block = herm(pairing(theta, action))
        alt_diagonal.add(sp.simplify(block[1, 1]))
        alt_offdiagonal.add(sp.simplify(block[1, 2]))
    alt_anti_hermitian_ranks = tuple(
        sorted(
            {anti(pairing(theta, action)).rank() for action in alt_edges.values()}
        )
    )
    alt_inertia_census = frozenset(
        inertia(herm(pairing(theta, action)).subs(MASS, b134.MASS))
        for action in alt_edges.values()
    )
    alt_pairing_diagonal_entry = (
        alt_diagonal.pop() if len(alt_diagonal) == 1 else sp.nan
    )
    alt_pairing_offdiagonal_entry = (
        alt_offdiagonal.pop() if len(alt_offdiagonal) == 1 else sp.nan
    )

    # --- G: the rider break ------------------------------------------------
    hodge_free_symbols = frozenset(hodge_quotient.free_symbols)
    theta_defect_free_symbols = frozenset(theta_defect.free_symbols)
    pairing_entry_free_symbols = frozenset(entry_free_symbols)
    blocker_is_st_only = bool(
        ST in hodge_free_symbols
        or ST in theta_defect_free_symbols
        or ST in pairing_entry_free_symbols
    )

    exact_no_float = no_float(
        (
            hodge_quotient,
            theta,
            theta_defect,
            star,
            delta_star,
            symbolic_delta,
            tuple(edges.values()),
            tuple(alt_edges.values()),
            pairing_diagonal_entry,
            pairing_offdiagonal_entry,
            pairing_minor,
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        global_form_edges=global_form_edges,
        affine_edges=affine_edges,
        delta_anti_hermitian=zero(sp.expand(delta_star + delta_star.H)),
        delta_rank=delta_star.rank(),
        delta_symbolic_free_symbols=frozenset(symbolic_delta.free_symbols),
        delta_vanishes_at_zero_st=zero(sp.expand(symbolic_delta.subs(ST, 0))),
        hodge_inertia=hodge_inertia,
        leading_minors_positive=leading_minors_positive,
        gluing_span_dimension=gluing_span_dimension,
        sum_rule_holds=sum_rule_holds,
        chart_differences_nonzero=chart_differences_nonzero,
        hodge_free_symbols=hodge_free_symbols,
        fingerprint_count=len(classes),
        fingerprint_repeat=fingerprint_repeat,
        absolute_preservers=absolute_preservers,
        minimum_reflection_moves=minimum_reflection_moves,
        reflection_family_size=family_size,
        reflection_family_descending=family_descending,
        reflection_family_preserving=family_preserving,
        theta_is_involution=bool(
            zero(sp.expand(theta * theta - IDENTITY))
            and zero(sp.expand(theta.T * theta - IDENTITY))
            and zero(sp.expand(theta - theta.T))
        ),
        theta_exchanges_halves=zero(sp.expand(PLUS.T * theta * PLUS)),
        theta_defect_rank=theta_defect.rank(),
        theta_defect_max_entry=theta_defect_max_entry,
        theta_defect_free_symbols=theta_defect_free_symbols,
        staircase_law=staircase_law,
        staircase_indices=staircase_indices,
        staircase_distinct_values=staircase_distinct_values,
        shear_free_symmetry=shear_free_symmetry,
        shear_free_hermitian_count=shear_free_hermitian_count,
        constant_symmetry=constant_symmetry,
        constant_hermitian_count=constant_hermitian_count,
        staircase_symmetry=staircase_symmetry,
        staircase_hermitian_count=staircase_hermitian_count,
        causes_decoupled=causes_decoupled,
        anti_hermitian_ranks=anti_hermitian_ranks,
        pairing_diagonal_entry=pairing_diagonal_entry,
        pairing_offdiagonal_entry=pairing_offdiagonal_entry,
        pairing_minor=pairing_minor,
        pairing_entry_free_symbols=pairing_entry_free_symbols,
        vanishing_row_impossible=vanishing_row_impossible,
        inertia_census=inertia_census,
        psd_edge_count=psd_edge_count,
        displayed_edge_inertia=displayed_edge_inertia,
        corner_inertia=corner_inertia,
        alt_pairing_diagonal_entry=alt_pairing_diagonal_entry,
        alt_pairing_offdiagonal_entry=alt_pairing_offdiagonal_entry,
        alt_anti_hermitian_ranks=alt_anti_hermitian_ranks,
        alt_inertia_census=alt_inertia_census,
        self_edge_dressings_vanish=self_edge_dressings_vanish,
        self_edge_actions_undressed=self_edge_actions_undressed,
        blocker_is_st_only=blocker_is_st_only,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = "N5: per_element: the Block 141 coboundary correction Delta* is exactly anti-Hermitian of rank 16, s_t-only and zero at s_t=0, so every dressed edge action is exactly Q_ij = Q_i + (x_j-x_i)Delta* on all 16 ordered edges\nper_site: H_q is a real symmetric 16x16 with NO free symbols, identical for symbolic s_x and s_t, with 15 distinct absolute-row fingerprints whose sole repeat is sites (1,1),(3,3), and exact backtracking over ALL 16-site permutations leaves the IDENTITY as the only permutation preserving abs(H_q) entrywise, the (1,1)<->(3,3) swap failing on the pinned neighbours\nper_mode: the cause is two DECOUPLED carrier properties -- a shear-free carrier, even a non-constant one with profile (0,nu(t)), makes ALL 16 healed pairings Hermitian while theta is still not a Hodge symmetry, and a constant carrier makes theta an exact Hodge symmetry while nonzero constant shear leaves only 1/16 pairings Hermitian -- so the SHEAR breaks Hermiticity and the NON-CONSTANCY breaks the theta-symmetry, and the displayed staircase v_{(3t+x) mod 8} with 8 distinct values has both, at 0/16 and no theta-symmetry\nper_block: with the pairing [theta Q]_++ on the half carrier {p=0,1} the anti-Hermitian part has rank 8 on all 16 edges, and on the Hermitian part A[1,1]=0 and A[1,2]=-19m/160 identically in the coboundary weight w and in (s_x,s_t), so the {1,2} principal minor is -361 m^2/25600 <= 0 and the pairing is NEVER positive semidefinite for m != 0, the m=0 corner closing via the vanishing-diagonal row with inertia (0,4,4) at the (m,s_t)=(0,0) corner and all 16 edges indefinite at the fixture mass 2/7 with inertias {(2,0,6),(4,0,4),(6,0,2)}\nlattice_wide: Q_ij + Q_ij^dagger = 2 m H_q exactly on all 16 edges with H_q positive definite, inertia (16,0,0) and all 16 leading principal minors positive, so the atlas-global quadratic form EXISTS and improves Block 137's rank-8 tail verdict for the selector class, while span{Q_i-Q_0} is two-dimensional with the exact sum rule Q_(0,0)+Q_(0,1)=Q_(1,0)+Q_(1,1) so no single coboundary generator glues the skew parts, and NO signed lattice reflection preserves H_q, zero of the full 256-map family (t,x)->(b-t,a-x) with all sign twists doing so, the canonical theta t->7-t, x->-x descending to p->3-p with an overall minus having defect of rank 16 with max entry 3/16 free of m, s_x and s_t\nRESULT: on the displayed atlas, fixtures and staircase carrier the healed action carries an exact positive-definite atlas-global quadratic form that no signed lattice reflection preserves, and below that blocker the [theta Q]_++ pairing is never positive semidefinite, with alternative weights x'=(0,7/3,-5/11,2) reproducing every entry, rank and inertia so the blocker and the certificate never see the coboundary weights; the healing is s_t-only but the blocker is NOT, being the arc's first obstruction that does not collapse at s_t=0\nDECISION_CUT: search metric-adapted involutions beyond lattice reflections, which are live because H_q is positive definite; test shear-free and alternative carriers; apply a swap completion; decide the two forced self-edges and the admissibility class of coboundary dressings; execute the joint-lane program; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero"


SCOPE_KEYS = (
    "global_form_mass_hodge",
    "global_form_positive_definite",
    "global_form_sum_rule",
    "blocker_only_identity",
    "blocker_no_signed_reflection",
    "blocker_full_family",
    "cause_shear_free",
    "cause_constant_carrier",
    "cause_staircase",
    "certificate_pairing_entry",
    "certificate_never_positive",
    "certificate_inertia_census",
    "weight_freedom",
    "rider_break",
    "hypothesis_metric_adapted",
    "hypothesis_not_searched",
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
        "global_form_mass_hodge": (
            "2 m h_q" in note or "2m h_q" in note or "2*m*h_q" in note
        ),
        "global_form_positive_definite": "positive definite" in note,
        "global_form_sum_rule": "sum rule" in note,
        "blocker_only_identity": "only the identity" in note,
        "blocker_no_signed_reflection": (
            "no signed lattice reflection" in note
        ),
        "blocker_full_family": "256" in note,
        "cause_shear_free": "shear-free" in note,
        "cause_constant_carrier": "constant carrier" in note,
        "cause_staircase": "staircase" in note,
        # Whitespace-insensitive so the note may write -19m/160, -19 m/160 or
        # -19*m/160 without changing the certificate.
        "certificate_pairing_entry": (
            "-19m/160" in compact or "-19*m/160" in compact
        ),
        "certificate_never_positive": (
            "never positive semidefinite" in note
        ),
        "certificate_inertia_census": (
            "(2,0,6)" in compact
            and "(4,0,4)" in compact
            and "(6,0,2)" in compact
        ),
        "weight_freedom": (
            "weight-freedom" in note
            or "weight-free" in note
            or "any coboundary weight" in note
        ),
        "rider_break": (
            "does not collapse at s_t = 0" in note
            or "doesnotcollapseats_t=0" in compact
        ),
        "hypothesis_metric_adapted": "metric-adapted involutions" in note,
        "hypothesis_not_searched": "not searched" in note,
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
        "sum_rule_holds": True,
        "hodge_inertia": HODGE_INERTIA,
        "absolute_preserver_count": 1,
        "fingerprint_count": 15,
        "theta_defect_rank": 16,
        "causes_are_decoupled": True,
        "shear_free_hermitian_count": 16,
        "pairing_offdiagonal_entry": PAIRING_ENTRY,
        "psd_edge_count": 0,
        "inertia_census": INERTIA_CENSUS,
        "weights_are_free": True,
        "blocker_is_st_only": False,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "break_sum_rule":
        claims["sum_rule_holds"] = False
    elif mutation == "break_hodge_inertia":
        claims["hodge_inertia"] = (15, 1, 0)
    elif mutation == "claim_preserver_exists":
        claims["absolute_preserver_count"] = 2
    elif mutation == "break_fingerprint_count":
        claims["fingerprint_count"] = 16
    elif mutation == "break_theta_defect_rank":
        claims["theta_defect_rank"] = 15
    elif mutation == "conflate_the_causes":
        claims["causes_are_decoupled"] = False
    elif mutation == "break_hermitian_count":
        claims["shear_free_hermitian_count"] = 8
    elif mutation == "break_pairing_entry":
        claims["pairing_offdiagonal_entry"] = -R(19, 161) * MASS
    elif mutation == "claim_positive_semidefinite_edge":
        claims["psd_edge_count"] = 1
    elif mutation == "break_inertia_census":
        claims["inertia_census"] = frozenset(
            {(2, 0, 6), (4, 0, 4), (6, 0, 2), (8, 0, 0)}
        )
    elif mutation == "claim_weight_dependence":
        claims["weights_are_free"] = False
    elif mutation == "claim_blocker_is_st_only":
        claims["blocker_is_st_only"] = True
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py",
            "logs/runner-cache/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.txt",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
        )
        and PARENT_ARTIFACTS
        == (
            BLOCK141_NOTE,
            BLOCK141_RUNNER,
            BLOCK141_CACHE,
            BLOCK134_NOTE,
            BLOCK134_RUNNER,
        )
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.global_form_edges == 16
        and facts.affine_edges == 16
        and facts.delta_anti_hermitian
        and facts.delta_rank == PHYS
        and facts.delta_symbolic_free_symbols == frozenset({ST})
        and facts.delta_vanishes_at_zero_st
        and facts.hodge_inertia == claims["hodge_inertia"]
        and facts.leading_minors_positive
        and facts.gluing_span_dimension == GLUING_SPAN_DIMENSION
        and facts.chart_differences_nonzero
        and facts.sum_rule_holds == bool(claims["sum_rule_holds"])
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.hodge_free_symbols == frozenset()
        and facts.fingerprint_count == claims["fingerprint_count"]
        and facts.fingerprint_repeat == FINGERPRINT_REPEAT
        and len(facts.absolute_preservers) == claims["absolute_preserver_count"]
        and facts.absolute_preservers == (tuple(range(PHYS)),)
        and facts.minimum_reflection_moves == 12
        and facts.reflection_family_size == SIGNED_REFLECTION_FAMILY
        and facts.reflection_family_descending == SIGNED_REFLECTION_FAMILY
        and facts.reflection_family_preserving == 0
        and facts.theta_is_involution
        and facts.theta_exchanges_halves
        and facts.theta_defect_rank == claims["theta_defect_rank"]
        and facts.theta_defect_max_entry == THETA_DEFECT_MAX_ENTRY
        and facts.theta_defect_free_symbols == frozenset()
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.staircase_law
        and facts.staircase_indices == tuple(range(8))
        and facts.staircase_distinct_values == 8
        and not facts.shear_free_symmetry
        and facts.shear_free_hermitian_count
        == claims["shear_free_hermitian_count"]
        and facts.constant_symmetry
        and facts.constant_hermitian_count == 1
        and not facts.staircase_symmetry
        and facts.staircase_hermitian_count == 0
        and facts.causes_decoupled == bool(claims["causes_are_decoupled"])
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.anti_hermitian_ranks == (HALF,)
        and facts.pairing_diagonal_entry == 0
        and canonical(
            facts.pairing_offdiagonal_entry
            - claims["pairing_offdiagonal_entry"]
        )
        == 0
        and canonical(facts.pairing_minor - MINOR_CERTIFICATE) == 0
        and facts.vanishing_row_impossible
        and facts.inertia_census == claims["inertia_census"]
        and facts.psd_edge_count == claims["psd_edge_count"]
        and facts.displayed_edge_inertia == (6, 0, 2)
        and facts.corner_inertia == CORNER_INERTIA
        and facts.exact_no_float
    )

    weights_are_free = bool(
        facts.alt_pairing_diagonal_entry == facts.pairing_diagonal_entry
        and canonical(
            facts.alt_pairing_offdiagonal_entry
            - facts.pairing_offdiagonal_entry
        )
        == 0
        and facts.alt_anti_hermitian_ranks == facts.anti_hermitian_ranks
        and facts.alt_inertia_census == facts.inertia_census
    )
    gate_f = bool(
        weights_are_free == bool(claims["weights_are_free"])
        and facts.alt_pairing_diagonal_entry == 0
        and facts.alt_anti_hermitian_ranks == (HALF,)
        and facts.self_edge_dressings_vanish
        and facts.self_edge_actions_undressed
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.delta_symbolic_free_symbols == frozenset({ST})
        and facts.delta_vanishes_at_zero_st
        and facts.hodge_free_symbols == frozenset()
        and facts.theta_defect_free_symbols == frozenset()
        and facts.pairing_entry_free_symbols == frozenset({MASS})
        and facts.blocker_is_st_only == bool(claims["blocker_is_st_only"])
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
        "main plus the committed Block 141 note/runner/cache and Block 134 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-atlas-global-quadratic-form",
        "Q_ij+Q_ij^dagger=2*m*H_q on all 16 healed edges with Delta* anti-Hermitian of rank 16 and s_t-only, H_q of inertia (16,0,0) with positive leading principal minors, and the residual obstruction exactly dim span{Q_i-Q_0}=2 with the sum rule Q_(0,0)+Q_(0,1)-Q_(1,0)-Q_(1,1)=0",
        gate_values["B"],
    )
    checks.check(
        "C-reflection-blocker",
        "H_q is parameter-free with 15 absolute-row fingerprints repeating only on {(1,1),(3,3)}, backtracking leaves the identity as the sole |H_q|-preserving permutation against a 12-site minimum for any time reflection, all 256 signed lattice reflections descend and 0 preserve H_q, and the canonical theta defect has rank 16 with maximum entry 3/16",
        gate_values["C"],
    )
    checks.check(
        "D-decoupled-cause-controls",
        "the two properties are decoupled: a shear-free non-constant carrier gives 16/16 Hermitian healed pairings with no theta Hodge symmetry, a constant sheared carrier gives an exact theta Hodge symmetry with 1/16, and the committed staircase over all 8 indices with 8 distinct values gives 0/16 and no symmetry",
        gate_values["D"],
    )
    checks.check(
        "E-non-positivity-certificate",
        "[theta*Q]_{++} has anti-Hermitian part of rank 8 on all 16 edges and Hermitian part with A[1,1]=0, A[1,2]=-19*m/160 and minor -361*m^2/25600 identically in (m,w,s_x,s_t), a fixture-mass inertia census of exactly {(2,0,6),(4,0,4),(6,0,2)} with no positive semidefinite edge, and an m=0 corner of inertia (0,4,4)",
        gate_values["E"],
    )
    checks.check(
        "F-weight-freedom",
        "the alternative weights x'=(0,7/3,-5/11,2) reproduce A[1,1]=0, A[1,2]=-19*m/160, the rank-8 anti-Hermitian part and the same inertia census, and the self-edges keep Omega_ii=0 and the undressed chart actions",
        gate_values["F"],
    )
    checks.check(
        "G-rider-break",
        "the healing correction Delta* is s_t-only and vanishes at s_t=0 while H_q, the theta-defect and A[1,2] carry no s_t at all, so the blocker survives s_t -> 0",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the global form, the reflection blocker, the decoupled causes, the non-positivity certificate, weight-freedom, the rider break, the named hypotheses, the disclosures, the firewalls, and the exact N5 fence are present",
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
