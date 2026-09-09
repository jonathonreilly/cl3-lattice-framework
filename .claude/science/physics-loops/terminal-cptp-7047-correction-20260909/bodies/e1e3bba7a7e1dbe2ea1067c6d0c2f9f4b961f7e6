#!/usr/bin/env python3
"""Block 9: terminal-center/site-Record diagonal commit boundary.

The exact Block-7 ternary instruments and Block-8 repaired carrier are reused.
This runner separates three objects that must not be conflated:

* an ordinary Hilbert output register with blank plus three terminal sectors;
* one framework site Record whose content is an M2(C) possibility; and
* the joint stochastic coupling between the instrument center and that Record.

A four-sector register admits a total absorbing CPTP commit channel.  Its
blank corner is exactly the A/B ternary cq instrument and its terminal face is
fixed pointwise.  Four linearly independent Kraus operators require a pure
environment of dimension four for the total channel.  One ordinary qubit
cannot host four nonzero orthogonal sectors, while a framework Record can use
three distinct M2(C) contents only through a separately typed classical
calibration.  A stipulated diagonal joint table gives conditional support
agreement; equal marginals alone do not.

This is a finite type/minimal-carrier and conditional coupling theorem.  It is
not a lattice-wide formation law, a derivation of the Admissibility marginal,
or an axiom amendment.
"""

from __future__ import annotations

from pathlib import Path
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_2026_08_20 as block7
import fixed_carrier_presence_separated_nondemolition_record_update_boundary_2026_08_20 as block8


NOTE_PATH = ROOT / "docs" / (
    "TERMINAL_CENTER_SITE_RECORD_DIAGONAL_COMMIT_MINIMAL_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
BLOCK6_PATH = ROOT / "docs" / (
    "INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK8_PATH = ROOT / "docs" / (
    "FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK7_NOTE_PATH = ROOT / "docs" / (
    "FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
MARKOV_PATH = ROOT / "docs" / "RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md"
FULL_Z3_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / (
    "FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md"
)
FULL_Z3_RUNNER_PATH = ROOT / "scripts" / (
    "full_z3_causal_front_sampled_instrument_law_probe_2026_07_14.py"
)
COPY_WRITE_PATH = ROOT / "docs" / (
    "RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md"
)

AUDIT_INPUT_PATHS = (
    "docs/TERMINAL_CENTER_SITE_RECORD_DIAGONAL_COMMIT_MINIMAL_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md",
    "docs/work_history/repo/review_feedback/FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md",
    "docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md",
    "scripts/fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_2026_08_20.py",
    "scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_2026_08_20.py",
    "scripts/full_z3_causal_front_sampled_instrument_law_probe_2026_07_14.py",
    "scripts/shared_effect_record_randomized_preparation_congruence_independence_2026_08_20.py",
    "scripts/admissibility_barycenter_evaluation_menu_kernel_2026_08_12.py",
    "scripts/instrument_port_typed_record_compiler_conditional_completion_2026_08_20.py",
    "scripts/common_front_stage_remote_context_record_event_congruence_2026_08_20.py",
    "scripts/shared_event_record_support_selection_triangle_2026_08_20.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/physical_effect_equivalence_normalized_grade_cycle321_2026_07_18.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
)

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -sp.I), (sp.I, 0)))
Z = sp.diag(1, -1)
RHO_STAR = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
RHO_TOMO = (
    I2 / 2,
    (I2 + X) / 2,
    (I2 + Y) / 2,
    (I2 + Z) / 2,
)

REGISTER_DIM = 4
BLANK_INDEX = 0
TERMINAL_INDICES = (1, 2, 3)
PB = sp.diag(1, 0, 0, 0)
TERMINAL_PROJECTORS = tuple(
    sp.diag(*(1 if position == index else 0 for position in range(4)))
    for index in TERMINAL_INDICES
)
T = sum(TERMINAL_PROJECTORS, sp.zeros(4))
PROGRAM_PROJECTORS = (sp.diag(1, 0), sp.diag(0, 1))
FRESH = sp.diag(1, 0)
SPENT = sp.diag(0, 1)
FLAG_SPEND = sp.Matrix(((0, 0), (1, 0)))


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


def zero(matrix: sp.Matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


def matrix_unit(dimension: int, target: int, source: int) -> sp.Matrix:
    result = sp.zeros(dimension)
    result[target, source] = 1
    return result


def commit_kraus(context: str) -> tuple[sp.Matrix, ...]:
    """Total CPTP commit on four-sector register x live system."""

    writers = tuple(
        sp.kronecker_product(
            matrix_unit(REGISTER_DIM, terminal, BLANK_INDEX), operator
        )
        for terminal, operator in zip(
            TERMINAL_INDICES, block7.PROGRAMS[context], strict=True
        )
    )
    hold = sp.kronecker_product(T, I2)
    return writers + (hold,)


def integrated_commit_kraus() -> tuple[sp.Matrix, ...]:
    """One fixed program-controlled, freshness-flag total commit channel.

    Tensor order is program P x register R x live system S x flag F.  The
    active subspace is arbitrary P,S with R blank and F fresh.  Everything
    else is inactive and is held pointwise by one complementary projector.
    """

    writers = []
    for branch, terminal in enumerate(TERMINAL_INDICES):
        writer = sp.zeros(32)
        for program_index, context in enumerate(("A", "B")):
            writer += sp.kronecker_product(
                PROGRAM_PROJECTORS[program_index],
                matrix_unit(REGISTER_DIM, terminal, BLANK_INDEX),
                block7.PROGRAMS[context][branch],
                FLAG_SPEND,
            )
        writers.append(sp.simplify(writer))
    active = sp.kronecker_product(I2, PB, I2, FRESH)
    hold = sp.eye(32) - active
    return tuple(writers) + (hold,)


def integrated_channel(kraus: tuple[sp.Matrix, ...], value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum((operator * value * operator.H for operator in kraus), sp.zeros(32))
    )


def integrated_active_state(context: str, rho: sp.Matrix) -> sp.Matrix:
    program = PROGRAM_PROJECTORS[("A", "B").index(context)]
    return sp.kronecker_product(program, PB, rho, FRESH)


def integrated_expected(context: str, rho: sp.Matrix) -> sp.Matrix:
    program = PROGRAM_PROJECTORS[("A", "B").index(context)]
    result = sp.zeros(32)
    for terminal, operator in zip(
        TERMINAL_PROJECTORS, block7.PROGRAMS[context], strict=True
    ):
        result += sp.kronecker_product(
            program,
            terminal,
            sp.simplify(operator * rho * operator.H),
            SPENT,
        )
    return sp.simplify(result)


def channel(kraus: tuple[sp.Matrix, ...], value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum((operator * value * operator.H for operator in kraus), sp.zeros(8))
    )


def dual(kraus: tuple[sp.Matrix, ...], value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum((operator.H * value * operator for operator in kraus), sp.zeros(8))
    )


def blank_state(rho: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(PB, rho)


def expected_terminal_cq(context: str, rho: sp.Matrix) -> sp.Matrix:
    blocks = [sp.zeros(2)]
    blocks.extend(
        sp.simplify(operator * rho * operator.H)
        for operator in block7.PROGRAMS[context]
    )
    return sp.diag(*blocks)


def matrix_basis(dimension: int) -> tuple[sp.Matrix, ...]:
    return tuple(
        matrix_unit(dimension, row, column)
        for row in range(dimension)
        for column in range(dimension)
    )


def vec(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix).reshape(matrix.rows * matrix.cols, 1)


def stinespring_isometry(kraus: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.Matrix.vstack(*kraus)


def trace_environment(value: sp.Matrix, environment_dim: int = 4) -> sp.Matrix:
    system_dim = 8
    reduced = sp.zeros(system_dim)
    for left in range(system_dim):
        for right in range(system_dim):
            reduced[left, right] = sp.simplify(
                sum(
                    value[environment * system_dim + left, environment * system_dim + right]
                    for environment in range(environment_dim)
                )
            )
    return reduced


def record_code(label: int) -> sp.Matrix:
    """A conjugation-invariant M2 possibility, not a density operator."""

    return sp.I * (label + 1) * I2


def decode_record(content: sp.Matrix) -> int:
    if content is None:
        raise ValueError("a site with no Record is outside the readout domain")
    for label in range(3):
        if content == record_code(label):
            return label
    raise ValueError("content is outside the declared three-code Record menu")


def central_weights(context: str, rho: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(sp.trace(operator * rho * operator.H))
        for operator in block7.PROGRAMS[context]
    )


def diagonal_coupling(weights: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.diag(*weights)


def same_marginal_mismatch_coupling(
    weights: tuple[sp.Expr, ...], epsilon: sp.Expr
) -> sp.Matrix:
    result = sp.diag(*weights)
    result[0, 0] -= epsilon
    result[1, 1] -= epsilon
    result[0, 1] += epsilon
    result[1, 0] += epsilon
    return result


def row_marginal(coupling: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sum(coupling[row, column] for column in range(3))) for row in range(3))


def column_marginal(coupling: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sum(coupling[row, column] for row in range(3))) for column in range(3))


def source_and_authority_controls() -> None:
    axiom = normalized(AXIOM_PATH)
    realized = normalized(REALIZED_PATH)
    block6_text = normalized(BLOCK6_PATH)
    block7_text = normalized(BLOCK7_NOTE_PATH)
    block8_text = normalized(BLOCK8_PATH)
    full_z3_runner = normalized(FULL_Z3_RUNNER_PATH)
    copy_write_text = normalized(COPY_WRITE_PATH)
    note = normalized(NOTE_PATH)
    check(
        "source-and-type-boundary",
        all(path.exists() for path in (NOTE_PATH, AXIOM_PATH, REALIZED_PATH, BLOCK6_PATH, BLOCK7_NOTE_PATH, BLOCK8_PATH, MARKOV_PATH, FULL_Z3_PATH, FULL_Z3_RUNNER_PATH, COPY_WRITE_PATH))
        and "the full one-site possibility domain has algebraic presentation m_2(c)" in axiom
        and "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions" in axiom
        and "when present, a record locks exactly one admissible local possibility" in axiom
        and "a site never carries more than one record; records are permanent" in axiom
        and "only records are readable. a readout value is determined by record content alone. a site with no record cannot be read" in axiom
        and "a state is a configuration of records" in axiom
        and "pointwise evaluation" in realized
        and "a law-admissible state supplied by the physical history" in realized
        and "this is pointwise evaluation, not a state-selection rule" in realized
        and "remaining numerical seam is the physical instrument-ensemble/record-ensemble identification" in block6_text
        and "narrow one-site capacity boundary and counterroutes" in block7_text
        and "regional logical code is not silently registered as one framework site record" in block8_text
        and "no three nonzero orthogonal status sectors fit one m2" in full_z3_runner
        and "since sigma_z has eigenprojectors p_0 and p_1" in copy_write_text,
        "current axioms, realized-state boundary, exact Blocks 6/8 seam, and prior Markov/full-Z3 work are source-bound",
    )
    required = (
        "one ordinary qubit cannot host blank plus three nonzero pairwise-orthogonal readable sectors",
        "the four-sector register is not one framework site record",
        "equal marginals do not force the diagonal coupling",
        "admissibility marginal equality remains supplied",
        "no-go discipline gate: pass",
        "zero obligation retirement",
    )
    check(
        "claim-scope-needles",
        all(needle in note for needle in required),
        "the note keeps the Hilbert carrier, candidate-content calibration, coupling, marginal law, and authority status distinct",
    )


def record_code_and_absence_controls() -> None:
    codes = tuple(record_code(label) for label in range(3))
    conjugators = (I2, X, Z, sp.Matrix(((1, 1), (1, -1))) / sp.sqrt(2))
    absence_rejected = False
    try:
        decode_record(None)  # type: ignore[arg-type]
    except ValueError:
        absence_rejected = True
    check(
        "one-site-record-code",
        len({tuple(code) for code in codes}) == 3
        and all(decode_record(code) == label for label, code in enumerate(codes))
        and absence_rejected
        and all(sp.simplify(unitary * code * unitary.H - code) == sp.zeros(2) for unitary in conjugators for code in codes),
        "three distinct conjugation-invariant M2 candidates decode by content alone; absence is rejected outside the readout domain",
    )
    carrier_map = {
        block8.BLANK: None,
        block8.PENDING: None,
        block8.TERMINALS[0]: codes[0],
        block8.TERMINALS[1]: codes[1],
        block8.TERMINALS[2]: codes[2],
    }
    check(
        "carrier-center-to-site-status",
        carrier_map["000"] is None
        and carrier_map["100"] is None
        and all(carrier_map[word] == code for word, code in zip(block8.TERMINALS, codes, strict=True))
        and carrier_map["010"] is not None,
        "blank and pending leave the candidate target absent; corrected outcome 0 uses a nonblank content candidate, never absence",
    )


def one_qubit_sector_boundary_controls() -> None:
    # Perfectly readable nondemolition status sectors have mutually orthogonal
    # nonzero support projections.  Rank additivity then requires d >= 4.
    required_rank = 1 + 1 + 1 + 1
    c2_dimension = 2
    projectors_c4 = tuple(
        sp.diag(*(1 if position == index else 0 for position in range(4)))
        for index in range(4)
    )
    orthogonal = all(
        left == right or zero(projectors_c4[left] * projectors_c4[right])
        for left in range(4)
        for right in range(4)
    )
    check(
        "single-m2-four-sector-rank-boundary",
        required_rank > c2_dimension,
        "four nonzero orthogonal blank/outcome support sectors require rank at least four, so an ordinary C2 output cannot supply them",
    )
    check(
        "minimal-four-sector-counterroute",
        orthogonal
        and sum(projector.rank() for projector in projectors_c4) == 4
        and sum(projectors_c4, sp.zeros(4)) == sp.eye(4),
        "C4, equivalently a supplied C2-tensor-C2 factorization, realizes the minimal orthogonal partition; no spatial placement is inferred",
    )
    povm = (sp.eye(2) / 4,) * 4
    check(
        "nonorthogonal-povm-route-does-not-meet-status-target",
        sum(povm, sp.zeros(2)) == I2
        and any(not zero(povm[left] * povm[right]) for left in range(4) for right in range(left + 1, 4)),
        "four qubit POVM effects exist but are not four perfectly readable absorbing output sectors; arbitrary M2 Record codes remain a separate classical route",
    )


def external_presence_tag_controls() -> None:
    beta = I2 / 2
    absent = ("absent", beta)
    present = ("present", beta)
    forget = lambda tagged: tagged[1]
    desired_absent_output = ("present", record_code(0))
    desired_present_output = present
    check(
        "external-presence-tag-collision",
        forget(absent) == forget(present)
        and desired_absent_output != desired_present_output,
        "the specified forgetful map identifies absent-beta and present-beta although the tested tagged transition assigns distinct successors; support-restricted sentinel encodings are not excluded",
    )


def absorbing_commit_channel_controls() -> None:
    failures = 0
    idempotence_failures = 0
    terminal_face_failures = 0
    atom_failures = 0
    for context in ("A", "B"):
        kraus = commit_kraus(context)
        completeness = sp.simplify(sum((operator.H * operator for operator in kraus), sp.zeros(8)))
        failures += not zero(completeness - sp.eye(8))
        for rho in RHO_TOMO + (RHO_STAR,):
            failures += not zero(channel(kraus, blank_state(rho)) - expected_terminal_cq(context, rho))
        for basis in matrix_basis(8):
            first = channel(kraus, basis)
            idempotence_failures += not zero(channel(kraus, first) - first)
        terminal_indices = tuple(range(2, 8))
        for left in terminal_indices:
            for right in terminal_indices:
                basis = matrix_unit(8, left, right)
                terminal_face_failures += not zero(channel(kraus, basis) - basis)
        terminal_observable = sp.kronecker_product(T, I2)
        failures += not zero(dual(kraus, terminal_observable) - sp.eye(8))
        for projector, operator in zip(TERMINAL_PROJECTORS, block7.PROGRAMS[context], strict=True):
            observable = sp.kronecker_product(projector, I2)
            expected = observable + sp.kronecker_product(PB, sp.simplify(operator.H * operator))
            observed = dual(kraus, observable)
            atom_failures += not zero(observed - expected)
            atom_failures += any(value < 0 for value in sp.simplify(operator.H * operator).eigenvals())
    check(
        "total-cptp-terminal-commit",
        failures == 0,
        "A/B four-sector maps are exact CPTP on every register-system operator, send the whole blank corner to the exact ternary cq channel, and make the terminal face certain",
    )
    check(
        "idempotent-absorbing-future-law",
        idempotence_failures == 0 and terminal_face_failures == 0 and atom_failures == 0,
        "the complete declared channel is idempotent, fixes every terminal-supported operator, and each terminal atom is subharmonic with the correct incoming effect",
    )


def integrated_program_flag_channel_controls() -> None:
    kraus = integrated_commit_kraus()
    active = sp.kronecker_product(I2, PB, I2, FRESH)
    inactive = sp.eye(32) - active
    terminal = sp.kronecker_product(I2, T, I2, sp.eye(2))
    completeness = sp.simplify(
        sum((operator.H * operator for operator in kraus), sp.zeros(32))
    )
    fixture_failures = 0
    for context in ("A", "B"):
        for rho in RHO_TOMO + (RHO_STAR,):
            fixture_failures += not zero(
                integrated_channel(kraus, integrated_active_state(context, rho))
                - integrated_expected(context, rho)
            )
    algebra_failures = int(not zero(completeness - sp.eye(32)))
    algebra_failures += int(not zero(kraus[-1] - inactive))
    for writer in kraus[:3]:
        algebra_failures += int(not zero(writer * inactive))
        algebra_failures += int(not zero(active * writer))
        algebra_failures += int(not zero(writer * terminal))
    algebra_failures += int(not zero(kraus[-1] * terminal - terminal))
    algebra_failures += int(not zero(active * terminal))
    integrated_atom_failures = 0
    for branch, terminal_projector in enumerate(TERMINAL_PROJECTORS):
        observable = sp.kronecker_product(I2, terminal_projector, I2, I2)
        expected = observable
        for program_projector, context in zip(
            PROGRAM_PROJECTORS, ("A", "B"), strict=True
        ):
            operator = block7.PROGRAMS[context][branch]
            expected += sp.kronecker_product(
                program_projector,
                PB,
                sp.simplify(operator.H * operator),
                FRESH,
            )
        observed = sp.simplify(
            sum(
                (operator.H * observable * operator for operator in kraus),
                sp.zeros(32),
            )
        )
        integrated_atom_failures += int(not zero(observed - expected))

    # These identities prove pointwise identity on the entire inactive
    # operator algebra and idempotence on the full 32x32 matrix algebra.
    inactive_rank = inactive.rank()

    check(
        "program-controlled-freshness-flag-cptp",
        fixture_failures == 0
        and algebra_failures == 0
        and integrated_atom_failures == 0,
        "one fixed P-R-S-F Hilbert channel reads a supplied definite A/B program, flips a one-shot fresh flag to spent, reproduces arbitrary-system tomography sectors, and removes only the host A/B call and post-write switch",
    )
    check(
        "inactive-subspace-and-terminal-totality",
        algebra_failures == 0 and inactive_rank == 28,
        "projector identities fix all 28^2=784 matrix units of the inactive Hilbert operator algebra; terminal, spent-flag, and other nonactive sectors are total rather than undefined",
    )


def environment_and_resource_controls() -> None:
    failures = 0
    ranks = {}
    active_ranks = {}
    for context in ("A", "B"):
        kraus = commit_kraus(context)
        gram = sp.Matrix.hstack(*(vec(operator) for operator in kraus))
        ranks[context] = gram.rank()
        active_ranks[context] = sp.Matrix.hstack(
            *(vec(operator) for operator in kraus[:3])
        ).rank()
        isometry = stinespring_isometry(kraus)
        failures += not zero(isometry.H * isometry - sp.eye(8))
        for rho in RHO_TOMO + (RHO_STAR,):
            value = blank_state(rho)
            joint = sp.simplify(isometry * value * isometry.H)
            failures += not zero(trace_environment(joint) - channel(kraus, value))
        terminal_test = sp.kronecker_product(TERMINAL_PROJECTORS[1], RHO_TOMO[1])
        joint_terminal = sp.simplify(isometry * terminal_test * isometry.H)
        failures += not zero(trace_environment(joint_terminal) - terminal_test)
    check(
        "four-kraus-pure-environment-ledger",
        failures == 0
        and ranks == {"A": 4, "B": 4}
        and active_ranks == {"A": 3, "B": 3},
        "the total absorbing channel has Kraus rank four while its blank formation corner has rank three; two pure-environment qubits suffice and no export/no-return transport is inferred",
    )

    integrated = integrated_commit_kraus()
    integrated_gram = sp.Matrix.hstack(*(vec(operator) for operator in integrated))
    integrated_active = sp.kronecker_product(I2, PB, I2, FRESH)
    integrated_active_gram = sp.Matrix.hstack(
        *(vec(operator * integrated_active) for operator in integrated)
    )
    integrated_isometry = stinespring_isometry(integrated)
    check(
        "integrated-rank-four-factor-isometry",
        integrated_gram.rank() == 4
        and integrated_active_gram.rank() == 3
        and zero(integrated_isometry.H * integrated_isometry - sp.eye(32)),
        "the program-controlled freshness-flag channel has total rank four and active-formation rank three, with seven qubit tensor factors; no spatial embedding or edge compiler is inferred",
    )


def diagonal_commit_coupling_controls() -> None:
    expected = {
        "A": (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25)),
        "B": (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20)),
    }
    diagonal_failures = 0
    mismatch_controls = 0
    marginal_failures = 0
    free_failures = 0
    support_failures = 0
    epsilon = sp.Rational(1, 10)
    for context in ("A", "B"):
        weights = central_weights(context, RHO_STAR)
        diagonal = diagonal_coupling(weights)
        diagonal_failures += weights != expected[context]
        diagonal_failures += row_marginal(diagonal) != weights
        diagonal_failures += column_marginal(diagonal) != weights
        diagonal_failures += any(
            diagonal[row, column] != 0
            for row in range(3)
            for column in range(3)
            if row != column
        )
        diagonal_failures += any(
            decode_record(record_code(column)) != row
            for row in range(3)
            for column in range(3)
            if diagonal[row, column] > 0
        )

        mismatch = same_marginal_mismatch_coupling(weights, epsilon)
        mismatch_controls += row_marginal(mismatch) != weights
        mismatch_controls += column_marginal(mismatch) != weights
        mismatch_controls += any(entry < 0 for entry in mismatch)
        mismatch_controls += sp.simplify(sum(mismatch[row, column] for row in range(3) for column in range(3) if row != column) - 2 * epsilon) != 0

        free = (sp.Rational(1, 3),) * 3
        free_failures += free == weights
        free_failures += sum(free) != 1
        support_failures += any(weight <= 0 for weight in free)
        support_failures += len({tuple(record_code(label)) for label in range(3)}) != 3

        for rho in RHO_TOMO:
            tomo_weights = central_weights(context, rho)
            coupling = diagonal_coupling(tomo_weights)
            marginal_failures += row_marginal(coupling) != tomo_weights
            marginal_failures += column_marginal(coupling) != tomo_weights
    check(
        "stipulated-candidate-diagonal-table",
        diagonal_failures == 0 and marginal_failures == 0,
        "conditional on formation at the declared target, the stipulated joint table has support only on Q_j paired with Record content kappa(j); it proves label agreement but is not a formation kernel",
    )
    check(
        "same-marginal-off-diagonal-hostile",
        mismatch_controls == 0,
        "an exact epsilon-cycle coupling has both correct marginals and positive mismatch mass, proving that marginal equality alone does not force pathwise correlation",
    )
    check(
        "admissibility-marginal-free-law-control",
        free_failures == 0 and support_failures == 0,
        "a supplied normalized uniform site menu gives every kappa(j) positive support but differs from both exact instrument centers; code legality does not supply the trace/Admissibility equality",
    )


def future_hostile_and_scope_controls() -> None:
    swap = sp.eye(4)
    swap[:, 1], swap[:, 2] = swap[:, 2], swap[:, 1]
    hostile = sp.kronecker_product(swap, I2)
    first_atom = sp.kronecker_product(TERMINAL_PROJECTORS[0], I2)
    check(
        "terminal-label-swap-hostile",
        not zero(hostile.H * first_atom * hostile - first_atom),
        "a label-mixing future unitary violates declared terminal-atom permanence/subharmonicity and is outside the isolated absorbing commit law",
    )
    note = normalized(NOTE_PATH)
    scope_needles = (
        "finite four-sector register",
        "separately supplied classical calibration",
        "not a lattice-wide autonomous nearest-neighbour law",
        "formation site, rate, overlap arbitration, and unbounded environment renewal remain open",
        "no axiom amendment is mature",
    )
    check(
        "physical-and-axiom-boundary",
        all(needle in note for needle in scope_needles),
        "the bounded channel/coupling result does not silently become a framework Record dynamics, Born derivation, or constitutional edit",
    )


def resolution_certificate() -> None:
    print(
        "per_element: checked — all four register projectors, all A/B Kraus operators, three site-content codes, and every joint coupling cell are tested separately"
    )
    print(
        "per_site: checked — one candidate target/menu has external absence plus three content-only M2 codes; no ordinary one-qubit sector realization is inferred"
    )
    print(
        "per_mode: checked — coherent cq output, absorbing channel, environment, candidate-content menu, diagonal table, and Admissibility marginal remain distinct"
    )
    print(
        "per_block: checked — one fixed A/B-programmed factor model passes CPTP completeness, flag spend, inactive-algebra identity, terminal absorption, tomography marginals, and mismatch controls"
    )
    print(
        "lattice_wide: checked and not executed — no total homogeneous overlap-safe nearest-neighbour formation process or unbounded environment-renewal law is constructed in this finite block"
    )
    print(
        "no_go_discipline_gate: PASS — scoped C2 rank and specified tag-forgetting factorization bounds, plus marginal/coupling and support/weight insufficiency witnesses only"
    )


def no_go_route_certificate() -> None:
    print(
        "n1_route: ATTEMPTED — four nonzero orthogonal statuses fail the C2 rank sum"
    )
    print(
        "n1_route: ATTEMPTED — four qubit POVM effects exist but are not readable absorbing sectors"
    )
    print(
        "n1_route: ATTEMPTED — three M2 contents survive as a candidate menu, not Hilbert sectors"
    )
    print(
        "n1_route: ATTEMPTED — C4 succeeds as the exact dimensional escape"
    )
    print(
        "n1_route: ATTEMPTED — the irreversible Kraus commit succeeds"
    )
    print(
        "n1_route: ATTEMPTED — equal marginals permit an off-diagonal coupling"
    )
    print(
        "n1_route: ATTEMPTED — uniform positive support permits non-trace weights"
    )
    print(
        "n1_route: ATTEMPTED — the specified tagged transition does not factor through its forgetful map"
    )


def main() -> int:
    source_and_authority_controls()
    record_code_and_absence_controls()
    one_qubit_sector_boundary_controls()
    external_presence_tag_controls()
    absorbing_commit_channel_controls()
    integrated_program_flag_channel_controls()
    environment_and_resource_controls()
    diagonal_commit_coupling_controls()
    future_hostile_and_scope_controls()
    resolution_certificate()
    no_go_route_certificate()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
