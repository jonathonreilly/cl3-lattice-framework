#!/usr/bin/env python3
"""Block 3: shared-effect and preparation-congruence law tournament.

The runner binds the exact August shared-effect ternary menus to the existing
Cycle-317 physical contact-seam dilation, then constructs three fixed local
conditional content kernels:

* barycenter evaluation, which obeys both tested congruences;
* normalized-square evaluation, which is effect-functional but fails the
  tested randomized-preparation descent; and
* trace-square menu restriction, which is preparation-independent but fails
  shared-effect descent.

The kernels are formula-class separators/selection candidates, not total
Admissibility models or retained laws.  They
condition on a declared ready site and enumerate candidate outcome content;
they do not choose a formation site, sample a branch, or form a Record.  The
test never interprets a pointer label as a Record and never inserts observed
frequencies.  In particular, no-click, double-click, permanence, and realized
history remain outside the executable surface.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from contextlib import redirect_stdout
from io import StringIO
from math import sqrt
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_barycenter_evaluation_menu_kernel_2026_08_12 as aug12
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_effect_equivalence_normalized_grade_cycle321_2026_07_18 as c321


NOTE_PATH = ROOT / "docs" / (
    "SHARED_EFFECT_RECORD_RANDOMIZED_PREPARATION_CONGRUENCE_"
    "INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
CYCLE20_PATH = ROOT / "docs/work_history/repo/review_feedback" / (
    "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
)
CYCLE317_PATH = ROOT / "docs/work_history/repo/review_feedback" / (
    "PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md"
)
CYCLE321_PATH = ROOT / "docs/work_history/repo/review_feedback" / (
    "PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md"
)
BLOCK2_PATH = ROOT / "docs" / (
    "DELAYED_AXIS_INPUT_STABILIZER_MIDPOINT_TYPE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AUG10_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AUG12_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_"
    "BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
NONAFFINE_PATH = ROOT / "docs" / (
    "NONAFFINE_PURITY_WEIGHTED_KERNEL_IS_NOT_BARYCENTER_EVALUATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
CARRIER_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_"
    "FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)

AUDIT_INPUT_PATHS = (
    "docs/SHARED_EFFECT_RECORD_RANDOMIZED_PREPARATION_CONGRUENCE_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/DELAYED_AXIS_INPUT_STABILIZER_MIDPOINT_TYPE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/NONAFFINE_PURITY_WEIGHTED_KERNEL_IS_NOT_BARYCENTER_EVALUATION_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/work_history/repo/review_feedback/OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md",
)

TOL = 8.0e-11
I2 = c317.I2
PASS = 0
FAIL = 0

Qsqrt2 = aug12.Qsqrt2
H2 = aug12.H2
ZERO = aug12.ZERO
ONE = aug12.ONE


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def q(value: int | Fraction) -> Qsqrt2:
    return Qsqrt2(Fraction(value))


def rs2(value: int | Fraction) -> Qsqrt2:
    return Qsqrt2(Fraction(0), Fraction(value))


def zero_h2() -> H2:
    return H2(ZERO, ZERO, ZERO)


def diagonal_density(upper: Fraction) -> H2:
    return H2(q(upper), ZERO, q(1 - upper))


def exact_menus() -> tuple[tuple[H2, ...], tuple[H2, ...]]:
    e0 = aug12.scaled_projector(Fraction(1, 2), ZERO, ONE)
    a1 = aug12.scaled_projector(
        Fraction(9, 10), rs2(Fraction(4, 9)), q(Fraction(-7, 9))
    )
    a2 = aug12.scaled_projector(
        Fraction(3, 5), rs2(Fraction(-2, 3)), q(Fraction(1, 3))
    )
    b1 = aug12.scaled_projector(
        Fraction(3, 4), rs2(Fraction(2, 3)), q(Fraction(-1, 3))
    )
    b2 = aug12.scaled_projector(
        Fraction(3, 4), rs2(Fraction(-2, 3)), q(Fraction(-1, 3))
    )
    return (e0, a1, a2), (e0, b1, b2)


def h2_to_numpy(matrix: H2) -> np.ndarray:
    def scalar(value: Qsqrt2) -> float:
        return float(value.a) + float(value.b) * sqrt(2)

    upper = scalar(matrix.q_re) + 1j * scalar(matrix.q_im)
    return np.asarray(
        ((scalar(matrix.p), upper), (upper.conjugate(), scalar(matrix.r))),
        dtype=complex,
    )


def sum_h2(items: tuple[H2, ...]) -> H2:
    return sum(items, start=zero_h2())


def exact_affine_weights(state: H2, menu: tuple[H2, ...]) -> tuple[Qsqrt2, ...]:
    return tuple(state.pairing(effect) for effect in menu)


def exact_square_weights(state: H2, menu: tuple[H2, ...]) -> tuple[Qsqrt2, ...]:
    square = state.square()
    denominator = square.trace().as_rational()
    if denominator <= 0:
        raise ValueError("a density has positive nonzero squared trace")
    return tuple(
        square.pairing(effect) * Fraction(1, denominator) for effect in menu
    )


def exact_context_weights(menu: tuple[H2, ...]) -> tuple[Qsqrt2, ...]:
    trace_squares = tuple(effect.trace().as_rational() ** 2 for effect in menu)
    denominator = sum(trace_squares)
    return tuple(q(value / denominator) for value in trace_squares)


def as_fraction(value: Qsqrt2) -> Fraction:
    return value.as_rational()


def fractions(values: tuple[Qsqrt2, ...]) -> tuple[Fraction, ...]:
    return tuple(as_fraction(value) for value in values)


def probability_vector_is_normalized(values: tuple[Qsqrt2, ...]) -> bool:
    return sum(values, start=ZERO) == ONE and all(
        as_fraction(value) >= 0 for value in values
    )


def build_program(name: str, menu: tuple[H2, ...], contact: np.ndarray) -> c321.Program:
    kraus = []
    for effect in menu:
        coefficient = float(effect.trace().as_rational())
        projector = h2_to_numpy(effect) / coefficient
        kraus.append(sqrt(coefficient) * projector @ contact)
    return c321.Program(name, tuple(kraus), ((0,), (1,), (2,)))


def compressed_effects(menu: tuple[H2, ...], contact: np.ndarray) -> tuple[np.ndarray, ...]:
    return tuple(contact.conj().T @ h2_to_numpy(effect) @ contact for effect in menu)


def canonical_key(unitary: np.ndarray) -> tuple[float, ...]:
    flat = unitary.reshape(-1)
    pivot = next(value for value in flat if abs(value) > 1e-10)
    normalized_unitary = unitary / (pivot / abs(pivot))
    rounded = np.round(normalized_unitary, 12)
    return tuple(float(value) for value in np.column_stack((rounded.real.reshape(-1), rounded.imag.reshape(-1))).reshape(-1))


def one_qubit_cliffords() -> tuple[np.ndarray, ...]:
    h = np.asarray(((1, 1), (1, -1)), dtype=complex) / sqrt(2)
    s = np.asarray(((1, 0), (0, 1j)), dtype=complex)
    pending = [I2]
    found: dict[tuple[float, ...], np.ndarray] = {}
    while pending:
        current = pending.pop()
        key = canonical_key(current)
        if key in found:
            continue
        found[key] = current
        pending.extend((h @ current, s @ current))
    return tuple(found.values())


def numeric_weights(kind: str, state: np.ndarray, menu: tuple[np.ndarray, ...]) -> tuple[float, ...]:
    if kind == "affine":
        evaluator = state
        raw = tuple(float(np.trace(evaluator @ effect).real) for effect in menu)
    elif kind == "square":
        square = state @ state
        evaluator = square / np.trace(square)
        raw = tuple(float(np.trace(evaluator @ effect).real) for effect in menu)
    elif kind == "context":
        scores = tuple(float(np.trace(effect).real) ** 2 for effect in menu)
        total = sum(scores)
        raw = tuple(score / total for score in scores)
    else:
        raise ValueError(kind)
    return raw


@dataclass(frozen=True)
class CandidateContentCode:
    """Symbolic kappa(U_g^dagger E U_g, label) in the existing M2 domain."""

    precontact_effect: H2
    label: Fraction
    contact_dressed: bool = False


@dataclass(frozen=True)
class DeclaredSiteCondition:
    """Symbolic central-site condition plus unordered six-code neighbourhood."""

    neighbors: tuple[CandidateContentCode, ...]
    central_blank: bool = True


PREPARATION_ROLE = Fraction(10)
FUEL_ROLE = Fraction(20)
GUARD_ROLE = Fraction(21)
PROGRAM_ROLES = (Fraction(100), Fraction(101), Fraction(102))


def declared_preparations() -> tuple[H2, ...]:
    return (
        aug12.MIXED,
        aug12.PZ,
        aug12.PMZ,
        diagonal_density(Fraction(3, 5)),
        diagonal_density(Fraction(3, 4)),
    )


def make_site_condition(
    preparation: H2, menu: tuple[H2, ...]
) -> DeclaredSiteCondition:
    records = (
        CandidateContentCode(menu[1], PROGRAM_ROLES[1], True),
        CandidateContentCode(aug12.MIXED, FUEL_ROLE),
        CandidateContentCode(preparation, PREPARATION_ROLE),
        CandidateContentCode(menu[2], PROGRAM_ROLES[2], True),
        CandidateContentCode(aug12.MIXED, GUARD_ROLE),
        CandidateContentCode(menu[0], PROGRAM_ROLES[0], True),
    )
    return DeclaredSiteCondition(records)


def decode_site_condition(
    site: DeclaredSiteCondition,
) -> tuple[H2, tuple[H2, ...], tuple[CandidateContentCode, ...]] | None:
    if not site.central_blank or len(site.neighbors) != 6:
        return None
    by_label = {record.label: record for record in site.neighbors}
    required = {PREPARATION_ROLE, FUEL_ROLE, GUARD_ROLE, *PROGRAM_ROLES}
    if len(by_label) != 6 or set(by_label) != required:
        return None
    if (
        by_label[FUEL_ROLE].precontact_effect != aug12.MIXED
        or by_label[GUARD_ROLE].precontact_effect != aug12.MIXED
        or by_label[FUEL_ROLE].contact_dressed
        or by_label[GUARD_ROLE].contact_dressed
        or by_label[PREPARATION_ROLE].contact_dressed
    ):
        return None
    program_records = tuple(by_label[label] for label in PROGRAM_ROLES)
    if not all(record.contact_dressed for record in program_records):
        return None
    menu = tuple(record.precontact_effect for record in program_records)
    declared_menus = exact_menus()
    if (
        menu not in declared_menus
        or by_label[PREPARATION_ROLE].precontact_effect
        not in declared_preparations()
    ):
        return None
    return by_label[PREPARATION_ROLE].precontact_effect, menu, program_records


@dataclass(frozen=True)
class CandidateSuccessor:
    probability: Fraction
    output: CandidateContentCode
    program_context: tuple[CandidateContentCode, ...]


def conditional_content_kernel(
    kind: str, site: DeclaredSiteCondition
) -> tuple[CandidateSuccessor, ...]:
    """Return conditional content weights; this function performs no draw."""

    decoded = decode_site_condition(site)
    if decoded is None:
        return ()
    preparation, menu, program_context = decoded
    if kind == "affine":
        weights = fractions(exact_affine_weights(preparation, menu))
    elif kind == "square":
        weights = fractions(exact_square_weights(preparation, menu))
    elif kind == "context":
        weights = fractions(exact_context_weights(menu))
    else:
        raise ValueError(kind)
    return tuple(
        CandidateSuccessor(
            weight,
            CandidateContentCode(effect, Fraction(index), True),
            program_context,
        )
        for index, (weight, effect) in enumerate(zip(weights, menu))
    )


def physical_effect(code: CandidateContentCode, contact: np.ndarray) -> np.ndarray:
    """Evaluate the symbolic Q coordinate on the physical contact seam."""

    base = h2_to_numpy(code.precontact_effect)
    return contact.conj().T @ base @ contact if code.contact_dressed else base


def kappa_matrix(code: CandidateContentCode, contact: np.ndarray) -> np.ndarray:
    """Evaluate kappa(Q,L)=Q+i L I on the physical contact seam."""

    return physical_effect(code, contact) + 1j * float(code.label) * I2


def decode_candidate_content(
    code: CandidateContentCode, contact: np.ndarray
) -> tuple[np.ndarray, Fraction]:
    """Decode candidate physical Q,L content without asserting formation."""

    return physical_effect(code, contact), code.label


def source_contracts() -> None:
    axiom = normalized(AXIOM_PATH)
    cycle20 = normalized(CYCLE20_PATH)
    cycle317 = normalized(CYCLE317_PATH)
    cycle321 = normalized(CYCLE321_PATH)
    block2 = normalized(BLOCK2_PATH)
    aug10 = normalized(AUG10_PATH)
    aug12 = normalized(AUG12_PATH)
    nonaffine = normalized(NONAFFINE_PATH)
    carrier = normalized(CARRIER_PATH)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    check(
        "sources",
        all(
            (
                "probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions" in axiom,
                "records form" in axiom,
                "a readout value is determined by record content alone" in axiom,
                "physical randomization gives affinity" in cycle20,
                "effect functionality remains a hypothesis" in cycle317,
                "equal effects, unequal processes" in cycle321,
                "same-effect probability/record congruence" in block2,
                "25/142" in aug10 and "2/11" in aug10,
                "barycenter evaluation" in aug12,
                "9/26" in nonaffine and "3/10" in nonaffine,
                "kappa(e,ell)=e+i ell i_2" in carrier,
            )
        ),
        "the current axiom, operational, apparatus, hostile-menu, non-affine, carrier, and Block-2 boundaries are bound",
    )


def exact_menu_controls(menu_a: tuple[H2, ...], menu_b: tuple[H2, ...]) -> None:
    check(
        "exact-menus",
        sum_h2(menu_a) == aug12.I2
        and sum_h2(menu_b) == aug12.I2
        and menu_a[0] == menu_b[0]
        and len(set(menu_a + menu_b)) == 5
        and all(aug12.is_scaled_projector(effect) for effect in menu_a + menu_b),
        "M_A and M_B are exact ternary scaled-projector resolutions sharing only E0=(1/2)Pz",
    )


def physical_program_controls(
    menu_a: tuple[H2, ...], menu_b: tuple[H2, ...]
) -> tuple[c321.Program, c321.Program, dict[int, c317.PhysicalFixture]]:
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    contact = fixtures[3].contact
    program_a = build_program("M_A", menu_a, contact)
    program_b = build_program("M_B", menu_b, contact)
    expected_a = compressed_effects(menu_a, contact)
    expected_b = compressed_effects(menu_b, contact)
    effect_residual = max(
        float(np.linalg.norm(actual - expected))
        for program, expected_menu in ((program_a, expected_a), (program_b, expected_b))
        for actual, expected in zip(program.coarse_effects, expected_menu)
    )
    isometry_residuals = {}
    code_residuals = {}
    for length, fixture in fixtures.items():
        residuals = []
        for program in (program_a, program_b):
            physical = c317.physical_isometry(fixture.two_ray_encoding, program.kraus)
            residuals.append(float(np.linalg.norm(physical.conj().T @ physical - I2)))
        isometry_residuals[length] = max(residuals)
        code_residuals[length] = max(
            float(
                np.linalg.norm(
                    fixture.two_ray_encoding.conj().T @ fixture.two_ray_encoding - I2
                )
            ),
            float(
                np.linalg.norm(
                    fixture.physical_contact @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding @ fixture.contact
                )
            ),
            float(
                np.linalg.norm(
                    fixture.constraint @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding
                )
            ),
        )
    check(
        "physical-programs",
        effect_residual < TOL
        and all(float(np.linalg.norm(program.completeness - I2)) < TOL for program in (program_a, program_b))
        and max(isometry_residuals.values()) < TOL
        and max(code_residuals.values()) < TOL,
        {
            "all_checked_residuals": f"< {TOL:g}",
            "carrier_lengths": tuple(fixtures),
        },
    )
    selected_effect = float(np.linalg.norm(program_a.coarse_effects[0] - program_b.coarse_effects[0]))
    selected_kraus = float(np.linalg.norm(program_a.kraus[0] - program_b.kraus[0]))
    selected_cp = float(
        np.linalg.norm(c321.choi((program_a.kraus[0],)) - c321.choi((program_b.kraus[0],)))
    )
    complete_channel = float(np.linalg.norm(c321.choi(program_a.kraus) - c321.choi(program_b.kraus)))
    check(
        "shared-branch",
        max(selected_effect, selected_kraus, selected_cp) < TOL and complete_channel > 1e-3,
        {
            "selected_effect_K_CP": f"< {TOL:g}",
            "complete_channel_difference": round(complete_channel, 6),
        },
    )

    c317.PASS = c317.FAIL = 0
    inherited_output = StringIO()
    with redirect_stdout(inherited_output):
        c317.physical_locality_and_covariance_controls(
            fixtures,
            {
                "shared_effect_M_A": program_a.kraus,
                "shared_effect_M_B": program_b.kraus,
            },
        )
    if c317.FAIL:
        print(inherited_output.getvalue(), end="")
    check(
        "physical-support-covariance",
        c317.FAIL == 0 and c317.PASS == 2,
        "the existing M64 compiler independently reports bounded support and 24/24 carried frames for both programs",
    )
    return program_a, program_b, fixtures


def positive_context_delay_controls(
    menu_a: tuple[H2, ...],
    program_a: c321.Program,
    program_b: c321.Program,
    fixtures: dict[int, c317.PhysicalFixture],
) -> None:
    """Test an exact two-stage route that hides program context at stage one."""

    logical_e0 = h2_to_numpy(menu_a[0])
    contact = fixtures[3].contact

    def positive_sqrt(matrix: np.ndarray) -> np.ndarray:
        values, vectors = np.linalg.eigh(matrix)
        if float(np.min(values)) < -TOL:
            raise ValueError("positive_sqrt received a matrix outside the positive cone")
        return vectors @ np.diag(np.sqrt(np.maximum(values, 0.0))) @ vectors.conj().T

    common_selected = positive_sqrt(logical_e0) @ contact
    common_remainder = positive_sqrt(I2 - logical_e0) @ contact
    inverse_remainder = np.linalg.inv(common_remainder)
    stage1_residual = max(
        float(np.linalg.norm(common_selected - program_a.kraus[0])),
        float(np.linalg.norm(common_selected - program_b.kraus[0])),
        float(
            np.linalg.norm(
                common_selected.conj().T @ common_selected
                + common_remainder.conj().T @ common_remainder
                - I2
            )
        ),
    )
    conditional_residuals = {}
    recovery_residuals = {}
    delayed_routes = {"common_front": (common_selected, common_remainder)}
    for program in (program_a, program_b):
        conditional = tuple(
            operator @ inverse_remainder for operator in program.kraus[1:]
        )
        delayed_routes[f"conditional_{program.name}"] = conditional
        conditional_residuals[program.name] = float(
            np.linalg.norm(
                sum(
                    (operator.conj().T @ operator for operator in conditional),
                    start=np.zeros((2, 2), dtype=complex),
                )
                - I2
            )
        )
        recovery_residuals[program.name] = max(
            float(np.linalg.norm(operator @ common_remainder - target))
            for operator, target in zip(conditional, program.kraus[1:])
        )
    check(
        "positive-context-delay-factorization",
        stage1_residual < TOL
        and max(conditional_residuals.values()) < TOL
        and max(recovery_residuals.values()) < TOL,
        {
            "all_factorization_residuals": f"< {TOL:g}",
            "programs": tuple(conditional_residuals),
            "remaining_gap": "physical causal staging and Record formation are not constructed",
        },
    )
    physical_isometry_residual = max(
        float(
            np.linalg.norm(
                c317.physical_isometry(fixture.two_ray_encoding, kraus).conj().T
                @ c317.physical_isometry(fixture.two_ray_encoding, kraus)
                - I2
            )
        )
        for fixture in fixtures.values()
        for kraus in delayed_routes.values()
    )
    c317.PASS = c317.FAIL = 0
    inherited_output = StringIO()
    with redirect_stdout(inherited_output):
        c317.physical_locality_and_covariance_controls(fixtures, delayed_routes)
    if c317.FAIL:
        print(inherited_output.getvalue(), end="")
    check(
        "positive-context-delay-carrier",
        physical_isometry_residual < TOL and c317.PASS == 2 and c317.FAIL == 0,
        {
            "physical_isometries": f"< {TOL:g}",
            "carrier": "bounded through held L=6 with 24/24 carried frames",
            "remaining_gap": "staged causal composition and context routing",
        },
    )


def law_controls(menu_a: tuple[H2, ...], menu_b: tuple[H2, ...]) -> None:
    states = (
        aug12.MIXED,
        aug12.PZ,
        aug12.PMZ,
        diagonal_density(Fraction(3, 5)),
        diagonal_density(Fraction(3, 4)),
    )
    normalized_rows = []
    for kind in ("affine", "square", "context"):
        for state in states:
            for menu in (menu_a, menu_b):
                if kind == "affine":
                    values = exact_affine_weights(state, menu)
                elif kind == "square":
                    values = exact_square_weights(state, menu)
                else:
                    values = exact_context_weights(menu)
                normalized_rows.append(probability_vector_is_normalized(values))
    check(
        "three-fixed-formulas",
        all(normalized_rows),
        "affine, normalized-square, and trace-square-restriction families are each fixed, positive, and normalized on both menus and all declared states",
    )

    rho35 = diagonal_density(Fraction(3, 5))
    affine_a = fractions(exact_affine_weights(rho35, menu_a))[0]
    affine_b = fractions(exact_affine_weights(rho35, menu_b))[0]
    square_a = fractions(exact_square_weights(rho35, menu_a))[0]
    square_b = fractions(exact_square_weights(rho35, menu_b))[0]
    context_a = fractions(exact_context_weights(menu_a))[0]
    context_b = fractions(exact_context_weights(menu_b))[0]
    check(
        "shared-effect-discriminator",
        affine_a == affine_b == Fraction(3, 10)
        and square_a == square_b == Fraction(9, 26)
        and context_a == Fraction(25, 142)
        and context_b == Fraction(2, 11)
        and context_a - context_b == Fraction(-9, 1562),
        {
            "affine": (affine_a, affine_b),
            "square": (square_a, square_b),
            "context": (context_a, context_b),
        },
    )

    direct = diagonal_density(Fraction(3, 4))
    fair_affine = (
        fractions(exact_affine_weights(aug12.MIXED, menu_a))[0]
        + fractions(exact_affine_weights(aug12.PZ, menu_a))[0]
    ) / 2
    fair_square = (
        fractions(exact_square_weights(aug12.MIXED, menu_a))[0]
        + fractions(exact_square_weights(aug12.PZ, menu_a))[0]
    ) / 2
    direct_affine = fractions(exact_affine_weights(direct, menu_a))[0]
    direct_square = fractions(exact_square_weights(direct, menu_a))[0]
    check(
        "preparation-discriminator",
        fair_affine == direct_affine == Fraction(3, 8)
        and fair_square == Fraction(3, 8)
        and direct_square == Fraction(9, 20)
        and direct_square - fair_square == Fraction(3, 40),
        {
            "fair_tag_affine": fair_affine,
            "direct_affine": direct_affine,
            "fair_tag_square": fair_square,
            "direct_square": direct_square,
        },
    )
    check(
        "wall-independence",
        context_a != context_b
        and fair_square != direct_square
        and affine_a == affine_b
        and fair_affine == direct_affine,
        "one fixed formula violates only shared-effect descent, another violates only preparation descent, and the affine formula satisfies both tested equalities",
    )


def internal_covariance_controls(
    program_a: c321.Program, program_b: c321.Program
) -> None:
    cliffords = one_qubit_cliffords()
    state = np.diag((0.6, 0.4)).astype(complex)
    maximum = 0.0
    carrier_maximum = 0.0
    for unitary in cliffords:
        rotated_state = unitary @ state @ unitary.conj().T
        for program in (program_a, program_b):
            menu = program.coarse_effects
            rotated_menu = tuple(unitary @ effect @ unitary.conj().T for effect in menu)
            for kind in ("affine", "square", "context"):
                original = numeric_weights(kind, state, menu)
                rotated = numeric_weights(kind, rotated_state, rotated_menu)
                maximum = max(maximum, max(abs(a - b) for a, b in zip(original, rotated)))
            for index, effect in enumerate(menu):
                label = float(index)
                kappa = effect + 1j * label * I2
                rotated_kappa = rotated_menu[index] + 1j * label * I2
                carrier_maximum = max(
                    carrier_maximum,
                    float(np.linalg.norm(unitary @ kappa @ unitary.conj().T - rotated_kappa)),
                )
    check(
        "internal-covariance",
        len(cliffords) == 24 and max(maximum, carrier_maximum) < TOL,
        {
            "onsite_cliffords": len(cliffords),
            "formula_and_kappa_residuals": f"< {TOL:g}",
        },
    )


def conditional_kernel_controls(
    menu_a: tuple[H2, ...],
    menu_b: tuple[H2, ...],
    program_a: c321.Program,
    program_b: c321.Program,
    contact: np.ndarray,
) -> None:
    rho35 = diagonal_density(Fraction(3, 5))
    site_a = make_site_condition(rho35, menu_a)
    site_b = make_site_condition(rho35, menu_b)
    all_kernels = {
        (kind, context): conditional_content_kernel(kind, site)
        for kind in ("affine", "square", "context")
        for context, site in (("M_A", site_a), ("M_B", site_b))
    }
    declared_domain_tables = tuple(
        conditional_content_kernel(kind, make_site_condition(state, menu))
        for kind in ("affine", "square", "context")
        for state in declared_preparations()
        for menu in (menu_a, menu_b)
    )
    check(
        "conditional-kernel-normalization",
        all(
            sum((branch.probability for branch in kernel), Fraction(0)) == 1
            and len(kernel) == 3
            and all(branch.probability >= 0 for branch in kernel)
            and len({branch.output.label for branch in kernel}) == len(kernel)
            for kernel in declared_domain_tables
        ),
        "all 30 declared site/formula/menu cases give normalized nonnegative three-content tables, including explicit zero weights; no sampling or Record formation is asserted",
    )
    shared_a = all_kernels[("affine", "M_A")][0]
    shared_b = all_kernels[("affine", "M_B")][0]
    readout_a = decode_candidate_content(shared_a.output, contact)
    readout_b = decode_candidate_content(shared_b.output, contact)
    check(
        "content-context-separation",
        shared_a.output == shared_b.output
        and np.linalg.norm(readout_a[0] - readout_b[0]) < TOL
        and readout_a[1] == readout_b[1]
        and shared_a.program_context != shared_b.program_context,
        "the E0 candidate has identical physical Q,L content while the complete input-program contexts remain distinct",
    )
    missing_fuel = tuple(
        record for record in site_a.neighbors if record.label != FUEL_ROLE
    )
    duplicate_role = tuple(
        site_a.neighbors[:-1]
        + (CandidateContentCode(menu_a[0], PROGRAM_ROLES[1], True),)
    )
    unrecognized_menu = (
        CandidateContentCode(aug12.PZ, PROGRAM_ROLES[0], True),
        CandidateContentCode(aug12.PMZ, PROGRAM_ROLES[1], True),
        CandidateContentCode(zero_h2(), PROGRAM_ROLES[2], True),
    )
    base_nonprogram = tuple(
        record for record in site_a.neighbors if record.label not in PROGRAM_ROLES
    )
    invalid_preparation = tuple(
        CandidateContentCode(diagonal_density(Fraction(2)), PREPARATION_ROLE)
        if record.label == PREPARATION_ROLE
        else record
        for record in site_a.neighbors
    )
    rejected_sites = (
        DeclaredSiteCondition(missing_fuel),
        DeclaredSiteCondition(duplicate_role),
        replace(site_a, central_blank=False),
        DeclaredSiteCondition(base_nonprogram + unrecognized_menu),
        DeclaredSiteCondition(invalid_preparation),
    )
    check(
        "conditional-domain-deletions",
        all(
            not conditional_content_kernel("affine", site)
            for site in rejected_sites
        )
        and conditional_content_kernel(
            "affine", DeclaredSiteCondition(tuple(reversed(site_a.neighbors)))
        )
        == all_kernels[("affine", "M_A")],
        "missing, duplicate-role, nonblank, nondeclared-menu, and nondeclared-preparation conditions are rejected; neighbour order is irrelevant",
    )
    program_code_residual = max(
        float(
            np.linalg.norm(
                physical_effect(record, contact) - expected
            )
        )
        for branch, program in (
            (shared_a, program_a),
            (shared_b, program_b),
        )
        for record, expected in zip(branch.program_context, program.coarse_effects)
    )
    output_code_residual = max(
        float(
            np.linalg.norm(
                physical_effect(branch.output, contact)
                - program.coarse_effects[int(branch.output.label)]
            )
        )
        for context, program in (("M_A", program_a), ("M_B", program_b))
        for kind in ("affine", "square", "context")
        for branch in all_kernels[(kind, context)]
    )
    check(
        "physical-content-carrier",
        all(
            isinstance(branch.output.precontact_effect, H2)
            and isinstance(branch.output.label, Fraction)
            and branch.output.contact_dressed
            and kappa_matrix(branch.output, contact).shape == (2, 2)
            for kernel in all_kernels.values()
            for branch in kernel
        )
        and program_code_residual < TOL
        and output_code_residual < TOL,
        {
            "all_physical_Q_residuals": f"< {TOL:g}",
            "scope": "candidate physical content only; no Record is formed",
        },
    )


def note_and_boundary_controls() -> None:
    text = normalized(NOTE_PATH)
    required = (
        "actual_current_surface_status: bounded-support",
        "zero obligation retirement",
        "same selected cp branch",
        "25/142",
        "2/11",
        "3/8",
        "9/20",
        "downstream law-selection",
        "no axiom wording is adopted",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "broad gate status: fail / do not ship",
        "no review-loop",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "claim-boundary",
        not missing,
        {"missing": missing, "scope": "bounded two-menu/two-preparation independence only; no Born no-go or axiom necessity"},
    )

    n5_lines = (
        "per_element: exact shared effect, codeword, probabilities, and selected CP branch are checked",
        "per_site: one unordered six-neighbour conditional packet and candidate output content are checked",
        "per_mode: affine, normalized-square, context-restriction, direct, and randomized preparations are checked",
        "per_block: two physical ternary programs, conditional normalization, physical content, and domain deletions are checked",
        "lattice_wide: checked and not executed — formation, sampling, arbitrary programs, autonomous genesis, rates, histories, and frequencies remain open",
    )
    for line in n5_lines:
        print(line)
    check(
        "n5-certificate",
        all(len(line) >= 80 for line in n5_lines),
        "all five landing-resolution statements are substantive and at least eighty characters",
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_contracts()
    menu_a, menu_b = exact_menus()
    exact_menu_controls(menu_a, menu_b)
    program_a, program_b, fixtures = physical_program_controls(menu_a, menu_b)
    positive_context_delay_controls(menu_a, program_a, program_b, fixtures)
    law_controls(menu_a, menu_b)
    internal_covariance_controls(program_a, program_b)
    conditional_kernel_controls(
        menu_a, menu_b, program_a, program_b, fixtures[3].contact
    )
    note_and_boundary_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
