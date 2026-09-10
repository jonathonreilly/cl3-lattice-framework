#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py
"""Block 142: finite carrier and signed-reflection certificates.

The runner reconstructs the displayed 4x4 quotient fixture from one bounded
helper.  It proves the atlas-global mass form, the two-dimensional chart-tail
span, the absence of a signed-lattice Hodge preserver in the enumerated
256-map family, and a nonzero-mass negative principal minor for the specified
compressed pairing.  The three carrier variants are diagnostic fixtures:
global Hodge invariance is not asserted to be necessary for compressed
Hermiticity, and no general shear/nonconstancy implication is claimed.

At zero mass the runner records only one specified ``s_x=3/5, s_t=0`` corner
and the explicit all-zero action counterexample.  Parent propagator, gluing-
tail, nilpotency, and curvature counts are historical context and are not
reproduced here.  All scientific arithmetic is exact SymPy arithmetic.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
import sys
import time

import sympy as sp


R = sp.Rational
MASS = sp.symbols("m", real=True)
SX, ST = sp.symbols("s_x s_t", real=True)
WEIGHT = sp.symbols("w", real=True)
LAM = sp.Symbol("lambda")

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10 as fixture

b105 = fixture.block105


NOTE_INPUT = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
NOTE_PATH = ROOT / NOTE_INPUT
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
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
    "toe-axiom-closure-block142-carrier-reflection-blocker-20260819/"
    "NO_GO_LEDGER.md"
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    ".claude/science/physics-loops/toe-axiom-closure-block142-carrier-reflection-blocker-20260819/NO_GO_LEDGER.md",
)

RUNNER_BUDGET_SEC = 120

# Every file read by the authority gate is pinned by content rather than a
# moving ref or ancestry relation.  The paired note does not contain the
# runner's content hash, so binding the note here creates no hash cycle.
INPUT_SHA256 = {
    NOTE_INPUT: "2329f133b90fefffc4270e37bfb581867c6280d47c4bb6280a148f0d7ad66cdc",
    AXIOM_PATH: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    REGISTRY_PATH: "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    BLOCK105_RUNNER: "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    HELPER_RUNNER: "0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87",
    NO_GO_PATH: "0395ea9c967e12b73509cf86137c6d9d558459c21e875a5f7f1523f69e2932d1",
}

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
    return fixture.matrix_zero(matrix)


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.expand((matrix + matrix.H) / 2)


def anti(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.expand((matrix - matrix.H) / 2)


def inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact multiplicity-aware inertia of a rational Hermitian matrix.

    ``Poly.count_roots`` counts distinct roots, so applying it directly to a
    characteristic polynomial loses repeated eigenvalue multiplicities.  A
    square-free factorisation keeps the efficient exact root count while its
    exponents restore those multiplicities.
    """
    if matrix.rows != matrix.cols or not zero(sp.expand(matrix - matrix.H)):
        raise ValueError("inertia requires a square Hermitian matrix")
    polynomial = sp.Poly(
        sp.expand(matrix.charpoly(LAM).as_expr()), LAM, domain=sp.QQ
    )
    zero_factor = sp.Poly(LAM, LAM, domain=sp.QQ)
    nullity = 0
    while polynomial.degree() > 0 and polynomial.eval(0) == 0:
        polynomial = polynomial.exquo(zero_factor)
        nullity += 1
    positive = 0
    negative = 0
    for factor, multiplicity in polynomial.sqf_list()[1]:
        positive += multiplicity * int(factor.count_roots(0, sp.oo))
        negative += multiplicity * int(factor.count_roots(-sp.oo, 0))
    if nullity != matrix.rows - matrix.rank():
        raise AssertionError("zero-root multiplicity disagrees with nullity")
    if min(positive, nullity, negative) < 0:
        raise AssertionError("inertia counts exceed the matrix dimension")
    if positive + nullity + negative != matrix.rows:
        raise AssertionError("inertia counts do not sum to the matrix dimension")
    return (positive, nullity, negative)


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
# carrier machinery reconstructed by the bounded fixture helper
# ---------------------------------------------------------------------------
SIZE = fixture.SIZE                     # 32 cover sites
COVER_T = fixture.COVER_TIME_EXTENT     # 8
PHYS_T = fixture.PHYSICAL_TIME_EXTENT   # 4
LX = fixture.SPACE_EXTENT               # 4
PHYS = PHYS_T * LX                   # 16 quotient sites
HALF = PHYS // 2                     # 8 sites in the positive-time half
ORIGINS = fixture.ORIGINS
DISPLAYED = fixture.DISPLAYED
INDEX = {origin: position for position, origin in enumerate(ORIGINS)}
HEALING_WEIGHTS = fixture.HEALING_WEIGHTS             # x  = (0,0,1/2,-1/3)
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
                fixture.cover_index(
                    (shift_t - time_coordinate) % COVER_T,
                    (shift_x - space_coordinate) % LX,
                ),
                fixture.cover_index(time_coordinate, space_coordinate),
            ] = overall * (-1) ** (alpha * time_coordinate + beta * space_coordinate)
    return matrix


def descend(cover_operator: sp.Matrix) -> sp.Matrix | None:
    """Push a cover operator through the antiperiodic quotient, or None."""
    candidate = SELECT * cover_operator * LIFT
    if zero(sp.expand(cover_operator * LIFT - LIFT * candidate)):
        return candidate
    return None


def hodge_from_field(field: dict) -> sp.Matrix:
    """The extracted curved-Hodge builder on an arbitrary overlap field."""
    result = sp.zeros(SIZE)
    for time_coordinate in range(COVER_T):
        for space_coordinate in range(LX):
            shear, volume = field[
                (time_coordinate % PHYS_T, space_coordinate)
            ]
            embedding = fixture.cover_embedding(time_coordinate, space_coordinate)
            result += (
                embedding * b105.shear_hodge(shear, volume) * embedding.T / 4
            )
    return sp.simplify(result)


def pairing(theta: sp.Matrix, action: sp.Matrix) -> sp.Matrix:
    """The compressed block [theta*Q]_{++} on the half carrier {p=0,1}."""
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
    # D: three diagnostic carrier controls
    staircase_law: bool
    staircase_indices: tuple
    staircase_distinct_values: int
    shear_free_symmetry: bool
    shear_free_hermitian_count: int
    constant_symmetry: bool
    constant_hermitian_count: int
    staircase_symmetry: bool
    staircase_hermitian_count: int
    controls_distinguish_properties: bool
    # E: the nonzero-mass minor and separately scoped fixture counts
    anti_hermitian_ranks: tuple
    pairing_diagonal_entry: sp.Expr
    pairing_offdiagonal_entry: sp.Expr
    pairing_minor: sp.Expr
    pairing_entry_free_symbols: frozenset
    inertia_census: frozenset
    psd_edge_count: int
    displayed_edge_inertia: tuple
    corner_inertia: tuple
    zero_parameter_pairing_is_zero: bool
    inertia_multiplicity_control: bool
    # F: the second weight control
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
    authority = authority_certificate()

    fixture_data = fixture.connection_data(fixture.S_X, fixture.S_T)
    symbolic = fixture.connection_data(SX, ST)
    differentials = fixture_data["d"]
    hodge = fixture.curved_hodge_cover()
    hodge_quotient = sp.expand(fixture.antiperiodic_quotient(hodge))
    theta = canonical_theta()

    star = sp.expand(differentials[(0, 0)] - differentials[(1, 0)])
    delta_star = sp.expand(fixture.quotient_correction(star, hodge))
    symbolic_star = sp.expand(
        symbolic["d"][(0, 0)] - symbolic["d"][(1, 0)]
    )
    symbolic_delta = sp.expand(
        fixture.quotient_correction(symbolic_star, hodge)
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
                fixture.quotient_action(
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
                - fixture.quotient_action(differentials[origin], hodge, MASS)
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

    # --- D: three diagnostic carrier controls ------------------------------
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
            fixture.antiperiodic_quotient(carrier_hodge)
        )
        symmetry = zero(
            sp.expand(
                theta.H * carrier_quotient * theta - carrier_quotient
            )
        )
        carrier_delta = sp.expand(
            fixture.quotient_correction(star, carrier_hodge)
        )
        hermitian = 0
        for left in ORIGINS:
            base = sp.expand(
                fixture.quotient_action(differentials[left], carrier_hodge, MASS)
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
    # These direct fixture controls distinguish global Hodge symmetry from
    # compressed-pairing Hermiticity.  They do not establish a general causal
    # law for shear or nonconstancy.
    controls_distinguish_properties = bool(
        constant_symmetry
        and not shear_free_symmetry
        and shear_free_hermitian_count > constant_hermitian_count
    )

    # --- E: the nonzero-mass minor and fixture counts -----------------------
    anti_hermitian_ranks = tuple(
        sorted({anti(pairing(theta, action)).rank() for action in edges.values()})
    )
    inertias = {
        key: inertia(herm(pairing(theta, action)).subs(MASS, fixture.MASS))
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
    corner_inertia = (0, 0, 0)
    for left in ORIGINS:
        action = sp.expand(
            fixture.quotient_action(
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
        if left == (0, 0):
            corner_inertia = inertia(
                sp.expand(
                    block.subs({MASS: 0, ST: 0, SX: fixture.S_X})
                )
            )
    pairing_diagonal_entry = (
        diagonal_entries.pop() if len(diagonal_entries) == 1 else sp.nan
    )
    pairing_offdiagonal_entry = (
        offdiagonal_entries.pop() if len(offdiagonal_entries) == 1 else sp.nan
    )
    pairing_minor = minors.pop() if len(minors) == 1 else sp.nan

    # --- F: the second weight control --------------------------------------
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
        inertia(herm(pairing(theta, action)).subs(MASS, fixture.MASS))
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

    zero_data = fixture.connection_data(sp.Integer(0), sp.Integer(0))
    zero_action = fixture.quotient_action(
        zero_data["d"][ORIGINS[0]], hodge, sp.Integer(0)
    )
    zero_parameter_pairing_is_zero = zero(pairing(theta, zero_action))

    return Facts(
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
        controls_distinguish_properties=controls_distinguish_properties,
        anti_hermitian_ranks=anti_hermitian_ranks,
        pairing_diagonal_entry=pairing_diagonal_entry,
        pairing_offdiagonal_entry=pairing_offdiagonal_entry,
        pairing_minor=pairing_minor,
        pairing_entry_free_symbols=pairing_entry_free_symbols,
        inertia_census=inertia_census,
        psd_edge_count=psd_edge_count,
        displayed_edge_inertia=displayed_edge_inertia,
        corner_inertia=corner_inertia,
        zero_parameter_pairing_is_zero=zero_parameter_pairing_is_zero,
        inertia_multiplicity_control=(
            inertia(sp.diag(1, 1, -2, -2, 0)) == (2, 1, 2)
            and inertia(sp.zeros(5)) == (0, 5, 0)
        ),
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
N5_FENCE = (
    "N5: per_element: on the displayed 4x4 quotient fixture the sixteen dressed edge actions obey Q_ij + Q_ij^dagger = 2 m H_q, and the extracted coboundary correction is anti-Hermitian and rank 16 at the primary connection fixture, while its symbolic expression is s_t-only and zero at s_t=0\n"
    "per_site: the parameter-free H_q has 15 absolute-row fingerprints and only the identity preserves its absolute profile; the separately enumerated 256 signed lattice reflections all descend and none preserves H_q, which is a finite-family statement rather than a classification of metric-adapted involutions\n"
    "per_mode: the shear-free, constant, and staircase carrier calculations are three fixture controls that distinguish compressed-pairing Hermiticity from global Hodge invariance; herm(theta Delta)=(theta Delta-Delta theta)/2 for skew Delta, so neither global invariance nor shear/nonconstancy is promoted to a general implication\n"
    "per_block: for the specified compression the symbolic minor is -361 m^2/25600 and excludes positive semidefiniteness whenever m is nonzero; the three-inertia census is only at mass 2/7, the (0,4,4) result is only at m=0, s_t=0, s_x=3/5 for the named chart, and the all-zero parameter action gives an explicit zero positive-semidefinite counterexample\n"
    "lattice_wide: the displayed chart tails span dimension two with the exact sum rule, and the alternative-weight calculation is one second control rather than an all-weight theorem; historical parent propagator, tail-rank, nilpotency, and curvature counts are archived but not executed by this runner\n"
    "RESULT: the displayed fixture has positive-definite H_q and an exact global mass split, no preserver in the tested signed-reflection family, and a nonzero-mass negative-minor certificate for the named compression; no necessity of global Hodge symmetry, generic carrier law, zero-mass no-PSD theorem, OS theorem, or curved OS theorem follows\n"
    "DECISION_CUT: metric-adapted involutions, other carriers, completions, the forced self-edges, coboundary admissibility, and the joint-lane program remain live; no premise or audit disposition is adopted here\n"
    "TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero"
)


SCOPE_KEYS = (
    "global_form_mass_hodge",
    "global_form_positive_definite",
    "global_form_sum_rule",
    "blocker_only_identity",
    "blocker_no_signed_reflection",
    "blocker_full_family",
    "fixture_controls",
    "compressed_not_global",
    "skew_compression_formula",
    "certificate_pairing_entry",
    "certificate_nonzero_mass",
    "zero_psd_counterexample",
    "zero_mass_narrow",
    "certificate_inertia_census",
    "two_weight_control",
    "historical_counts_not_executed",
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
        "fixture_controls": (
            "three fixture controls" in note
            and "shear-free" in note
            and "constant carrier" in note
            and "staircase" in note
        ),
        "compressed_not_global": (
            "global hodge invariance is not necessary" in note
        ),
        "skew_compression_formula": (
            "herm(thetadelta)=(thetadelta-deltatheta)/2" in compact
        ),
        # Whitespace-insensitive so the note may write -19m/160, -19 m/160 or
        # -19*m/160 without changing the certificate.
        "certificate_pairing_entry": (
            "-19m/160" in compact or "-19*m/160" in compact
        ),
        "certificate_nonzero_mass": (
            "excludes positive semidefiniteness whenever m is nonzero" in note
        ),
        "zero_psd_counterexample": (
            "all-zero parameter action" in note
            and "zero positive-semidefinite counterexample" in note
        ),
        "zero_mass_narrow": (
            "onlyatm=0,s_t=0,s_x=3/5" in compact
        ),
        "certificate_inertia_census": (
            "(2,0,6)" in compact
            and "(4,0,4)" in compact
            and "(6,0,2)" in compact
        ),
        "two_weight_control": (
            "two tested weight assignments" in note
        ),
        "historical_counts_not_executed": (
            "historical parent counts are not executed" in note
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
    expected_inputs = dict(INPUT_SHA256)
    claims: dict[str, object] = {
        "input_sha256": expected_inputs,
        "sum_rule_holds": True,
        "hodge_inertia": HODGE_INERTIA,
        "absolute_preserver_count": 1,
        "fingerprint_count": 15,
        "theta_defect_rank": 16,
        "controls_distinguish_properties": True,
        "shear_free_hermitian_count": 16,
        "pairing_offdiagonal_entry": PAIRING_ENTRY,
        "psd_edge_count": 0,
        "inertia_census": INERTIA_CENSUS,
        "two_weight_controls_match": True,
        "blocker_is_st_only": False,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        # Historical mutation name retained: corrupt the actual axiom-file pin.
        expected_inputs[AXIOM_PATH] = "0" * 64
    elif mutation == "stale_parent_authority":
        # Historical mutation name retained: corrupt the extracted-helper pin.
        expected_inputs[HELPER_RUNNER] = "0" * 64
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
        claims["controls_distinguish_properties"] = False
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
        claims["two_weight_controls_match"] = False
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
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
            "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
            ".claude/science/physics-loops/toe-axiom-closure-block142-carrier-reflection-blocker-20260819/NO_GO_LEDGER.md",
        )
        and set(INPUT_SHA256) == set(AUDIT_INPUT_PATHS)
        and authority.all_inputs_present
        and authority.actual_sha256 == claims["input_sha256"]
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
        and facts.controls_distinguish_properties
        == bool(claims["controls_distinguish_properties"])
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
        and facts.inertia_census == claims["inertia_census"]
        and facts.psd_edge_count == claims["psd_edge_count"]
        and facts.displayed_edge_inertia == (6, 0, 2)
        and facts.corner_inertia == CORNER_INERTIA
        and facts.zero_parameter_pairing_is_zero
        and facts.inertia_multiplicity_control
        and facts.exact_no_float
    )

    two_weight_controls_match = bool(
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
        two_weight_controls_match == bool(claims["two_weight_controls_match"])
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
        "B-atlas-global-quadratic-form",
        "on the displayed fixture Q_ij+Q_ij^dagger=2*m*H_q on all 16 edges, Delta* is anti-Hermitian and s_t-only, H_q has inertia (16,0,0), and the displayed chart differences span dimension 2 with the exact sum rule",
        gate_values["B"],
    )
    checks.check(
        "C-reflection-blocker",
        "for the displayed H_q exact backtracking leaves the identity as the sole absolute-profile preserver, all 256 enumerated signed lattice reflections descend and zero preserve H_q, and the named theta defect has rank 16 with maximum entry 3/16; the result is limited to this finite family",
        gate_values["C"],
    )
    checks.check(
        "D-decoupled-cause-controls",
        "the shear-free, constant, and staircase fixture controls give distinct compressed-Hermiticity and global-Hodge-invariance outcomes; they are diagnostic controls and do not establish a general implication or causal law",
        gate_values["D"],
    )
    checks.check(
        "E-non-positivity-certificate",
        "on the specified compression the Hermitian part has A[1,1]=0, A[1,2]=-19*m/160 and minor -361*m^2/25600 for all symbolic (m,w,s_x,s_t), excluding PSD when m is nonzero; the fixture-mass census is {(2,0,6),(4,0,4),(6,0,2)}, the narrow m=0,s_t=0,s_x=3/5 corner is (0,4,4), the all-zero action is PSD, and the inertia routine passes a repeated-root control",
        gate_values["E"],
    )
    checks.check(
        "F-weight-freedom",
        "one alternative weight assignment reproduces the named entries, symbolic rank and fixture-mass inertia census, and both tested assignments leave self-edge dressings zero; this is a two-weight control, not an all-weight theorem",
        gate_values["F"],
    )
    checks.check(
        "G-rider-break",
        "Delta* is s_t-only and vanishes at s_t=0 while the finite Hodge-preserver result and the symbolic negative minor remain independent of s_t; the zero-mass statement remains restricted to its named corner",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the note separates compressed Hermiticity from global Hodge invariance, distinguishes symbolic and fixture claims, records the all-zero PSD counterexample, limits the weight and zero-mass controls, preserves the firewalls, and contains the exact N5 fence",
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
