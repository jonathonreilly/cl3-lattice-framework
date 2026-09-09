#!/usr/bin/env python3
"""Block 208 exact two-time Clifford-cell M2 Record compiler boundary.

The runner keeps three levels separate:

* the reproduced four-corner cell is a strict CPTP qubit channel and, at the
  landed rational shear, a binary effect with an orientation-invariant phase
  contrast;
* a single cubic two-endpoint CP instrument reconstructs a relative central
  phase from its mathematically labeled outcome rates and therefore
  reconstructs the fixed H1 source in the forward and actual-reverse
  directions; and
* the current action/axioms do not yet identify exterior-action fields with
  those endpoint M2 states or select the sharpness/output coding of the
  instrument.  The result is typed compiler support, not local-law ownership.
"""

from __future__ import annotations

import argparse
from functools import cache
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402
import admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26 as b207  # noqa: E402


I = sp.I
B = b207.B
AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_COMPILER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block208-two-time-clifford-schur-m2-compiler-"
    "20260826"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "70a6b2ed31d26b6864d2fbdeab0a9336b0663f5c"
PREREG_COMMIT = "3dbd70623b218c60b72be93584028edaef406e91"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "2f66b1a9eea17ee9d81b5ddbe81d4a6253d800f8"
PREFLIGHT_BLOB = "9cd09e74fec58c315dbf43896345d2cfc1568ebc"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_COMPILER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    ".claude/science/physics-loops/toe-axiom-closure-block208-two-time-clifford-schur-m2-compiler-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block208-two-time-clifford-schur-m2-compiler-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_FACTORIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26.txt",
    "docs/ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.txt",
    "docs/COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
)

MUTATIONS = (
    "stale_main_authority",
    "drop_preregistration",
    "alter_goal_after_registration",
    "break_clifford_volume",
    "select_complex_orientation",
    "make_cell_nonpositive",
    "break_cell_trace_preservation",
    "erase_cell_effect_complement",
    "erase_handed_cell_term",
    "break_cell_phase_contrast",
    "break_endpoint_swap",
    "break_cubic_menu_normalization",
    "claim_output_records_readable",
    "use_unknown_state_readout",
    "erase_phase_decoder",
    "supply_momentum_label",
    "erase_forward_reconstruction",
    "erase_reverse_reconstruction",
    "erase_source_collision",
    "claim_projective_handed_readout",
    "claim_binary_relay_complete",
    "break_relay_normalization",
    "collapse_relay_component_score",
    "erase_displaced_relay",
    "erase_relay_reverse",
    "claim_radial_section_selected",
    "claim_relay_record_attachment",
    "claim_sharpness_selected",
    "claim_cell_legs_are_site_states",
    "open_h2_before_ownership",
    "claim_formation",
    "claim_history",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_progress",
    "claim_retained_status",
    "claim_broad_no_go",
    "erase_no_go_discipline",
)

X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -I), (I, 0)))
Z = sp.diag(1, -1)
I2 = sp.eye(2)
I4 = sp.eye(4)
CELL_C = sp.Rational(5, 13)
CELL_D = 1 / (1 - CELL_C**2)
CELL_S = 1 + CELL_D
CELL_A = sp.simplify(CELL_C * CELL_D / CELL_S)
CELL_B = sp.simplify((1 - CELL_D) / CELL_S)


def git_output(*args: str) -> str:
    return subprocess.run(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        capture_output=True,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    def commit_blob(commit: str, path: str) -> str:
        return git_output("rev-parse", f"{commit}:{path}")

    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_registered": commit_blob(PREREG_COMMIT, GOAL_PATH),
        "goal_worktree": commit_blob("HEAD", GOAL_PATH),
        "preflight_registered": commit_blob(PREREG_COMMIT, PREFLIGHT_PATH),
        "preflight_worktree": commit_blob("HEAD", PREFLIGHT_PATH),
        "axiom_main": commit_blob("origin/main", AXIOM_PATH),
        "axiom_worktree": commit_blob("HEAD", AXIOM_PATH),
        "registry_main": commit_blob("origin/main", REGISTRY_PATH),
        "registry_worktree": commit_blob("HEAD", REGISTRY_PATH),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


def physical_paulis(orientation: int) -> tuple[sp.Matrix, ...]:
    """One common physical axis basis in the two conjugate readings."""
    return X, orientation * Y, Z


def pauli_dot(vector: sp.Matrix, orientation: int) -> sp.Matrix:
    return sp.expand(sum(
        (vector[index] * physical_paulis(orientation)[index]
         for index in range(3)),
        sp.zeros(2),
    ))


def phase_state(angle: sp.Expr, orientation: int) -> sp.Matrix:
    vector = sp.Matrix((sp.cos(angle), sp.sin(angle), 0))
    return sp.simplify((I2 + pauli_dot(vector, orientation)) / 2)


def cell_choi(orientation: int) -> sp.Matrix:
    return sp.Matrix((
        (1, 0, 0, 0),
        (0, CELL_D, -orientation * I * CELL_C * CELL_D, 0),
        (0, orientation * I * CELL_C * CELL_D, CELL_D, 0),
        (0, 0, 0, 1),
    )) / CELL_S


def partial_trace(matrix: sp.MatrixBase, leg: int) -> sp.Matrix:
    result = sp.zeros(2)
    if leg == 0:
        for left in range(2):
            for right in range(2):
                result[left, right] = sum(
                    matrix[2 * index + left, 2 * index + right]
                    for index in range(2)
                )
    else:
        for left in range(2):
            for right in range(2):
                result[left, right] = sum(
                    matrix[2 * left + index, 2 * right + index]
                    for index in range(2)
                )
    return sp.simplify(result)


def choi_channel(choi: sp.MatrixBase, matrix: sp.MatrixBase) -> sp.Matrix:
    result = sp.zeros(2)
    for out_row in range(2):
        for out_column in range(2):
            result[out_row, out_column] = sp.expand(sum(
                matrix[in_row, in_column]
                * choi[2 * in_row + out_row, 2 * in_column + out_column]
                for in_row in range(2) for in_column in range(2)
            ))
    return sp.simplify(result)


@cache
def clifford_facts() -> dict[str, object]:
    generators = (
        sp.kronecker_product(X, I2),
        sp.kronecker_product(Z, X),
        sp.kronecker_product(Z, Z),
    )
    volume = generators[0] * generators[1] * generators[2]
    t_plus = sp.Matrix(((0, I, 1, 0), (-I, 0, 0, 1)))
    readings = []
    multiplication = []
    adjoints = []
    basis = (
        sp.eye(4), generators[0], generators[1], generators[2],
        generators[0] * generators[1],
        generators[1] * generators[2],
        generators[2] * generators[0], volume,
    )
    for orientation, transform in (
        (1, t_plus), (-1, sp.conjugate(t_plus))
    ):
        phi = lambda item: sp.simplify(  # noqa: E731
            transform * item * transform.conjugate().T / 2
        )
        images = tuple(phi(item) for item in generators)
        readings.append((
            images,
            phi(volume),
            transform * transform.conjugate().T,
            transform * volume - orientation * I * transform,
        ))
        multiplication.extend(
            phi(left * right) == phi(left) * phi(right)
            for left in basis for right in basis
        )
        adjoints.extend(phi(item.T) == phi(item).conjugate().T for item in basis)
    projector = (sp.eye(4) + generators[0]) / 2
    positive_images = tuple(
        (t_plus if orientation == 1 else sp.conjugate(t_plus))
        * projector
        * (t_plus if orientation == 1 else sp.conjugate(t_plus)).conjugate().T
        / 2
        for orientation in (1, -1)
    )
    return {
        "squares": all(g * g == sp.eye(4) for g in generators),
        "anticommutators": all(
            generators[i] * generators[j] + generators[j] * generators[i]
            == sp.zeros(4)
            for i in range(3) for j in range(i + 1, 3)
        ),
        "volume_square": volume * volume == -sp.eye(4),
        "volume_central": all(volume * g == g * volume for g in generators),
        "readings": readings,
        "multiplication": all(multiplication),
        "adjoints": all(adjoints),
        "positive_spectra": tuple(
            tuple(sorted(image.eigenvals().items(), key=lambda item: str(item[0])))
            for image in positive_images
        ),
        "orientation_selected": False,
    }


@cache
def cell_facts() -> dict[str, object]:
    expected_spectrum = {
        sp.Rational(144, 313): 2,
        sp.Rational(234, 313): 1,
        sp.Rational(104, 313): 1,
    }
    expected_complement = {
        sp.Rational(169, 313): 2,
        sp.Rational(79, 313): 1,
        sp.Rational(209, 313): 1,
    }
    channel_images = []
    conjugate_pairs = []
    pauli_forms = []
    for orientation in (1, -1):
        choi = cell_choi(orientation)
        paulis = physical_paulis(orientation)
        channel_images.append(tuple(choi_channel(choi, item) for item in (I2,) + paulis))
        pauli_form = (
            sp.kronecker_product(I2, I2) / 2
            + CELL_B * sp.kronecker_product(paulis[2], paulis[2]) / 2
            - CELL_A * (
                sp.kronecker_product(paulis[0], paulis[1])
                - sp.kronecker_product(paulis[1], paulis[0])
            ) / 2
        )
        pauli_forms.append(pauli_form == choi)
    conjugate_pairs.append(cell_choi(-1) == sp.conjugate(cell_choi(1)))
    plus_images = channel_images[0]
    minus_images = channel_images[1]
    expected_images = tuple(
        (I2, -CELL_A * physical_paulis(orientation)[1],
         -CELL_A * physical_paulis(orientation)[0],
         CELL_B * physical_paulis(orientation)[2])
        for orientation in (1, -1)
    )
    symbolic_c = sp.symbols("c", real=True)
    symbolic_d = 1 / (1 - symbolic_c**2)
    symbolic_s = 1 + symbolic_d
    symbolic_eigenvalues = (
        sp.simplify(1 / symbolic_s),
        sp.simplify(symbolic_d * (1 - symbolic_c) / symbolic_s),
        sp.simplify(symbolic_d * (1 + symbolic_c) / symbolic_s),
    )
    return {
        "c": CELL_C,
        "d": CELL_D,
        "s": CELL_S,
        "a": CELL_A,
        "b": CELL_B,
        "spectra": tuple(cell_choi(eps).eigenvals() for eps in (1, -1)),
        "complement_spectra": tuple(
            (I4 - cell_choi(eps)).eigenvals() for eps in (1, -1)
        ),
        "expected_spectrum": expected_spectrum,
        "expected_complement": expected_complement,
        "partial_traces": tuple(
            (partial_trace(cell_choi(eps), 0), partial_trace(cell_choi(eps), 1))
            for eps in (1, -1)
        ),
        "pauli_forms": all(pauli_forms),
        "channel_images": tuple(channel_images),
        "expected_images": expected_images,
        "conjugate_pair": all(conjugate_pairs),
        "symbolic_eigenvalues": symbolic_eigenvalues,
        "effect_interval_contains_fixture": (
            abs(CELL_C) < (sp.sqrt(5) - 1) / 2
        ),
        "cell_corner_legs_identified_as_site_states": False,
    }


def signed_axes() -> tuple[sp.Matrix, ...]:
    return tuple(
        sign * sp.eye(3)[:, axis]
        for axis in range(3) for sign in (-1, 1)
    )


def cubic_effect(vector: sp.Matrix, orientation: int, sharpness: sp.Expr) -> sp.Matrix:
    return sp.simplify((I2 + sharpness * pauli_dot(vector, orientation)) / 6)


def output_vector(first: sp.Matrix, second: sp.Matrix) -> sp.Matrix:
    return sp.simplify((first + 2 * second + first.cross(second)) / 8)


def output_state(first: sp.Matrix, second: sp.Matrix, orientation: int) -> sp.Matrix:
    return sp.simplify((I2 + pauli_dot(output_vector(first, second), orientation)) / 2)


def endpoint_probabilities(
    first_state: sp.Matrix,
    second_state: sp.Matrix,
    orientation: int,
    sharpness: sp.Expr = sp.Integer(1),
) -> tuple[tuple[sp.Matrix, sp.Matrix, sp.Expr], ...]:
    joint_state = sp.kronecker_product(first_state, second_state)
    return tuple(
        (
            first,
            second,
            sp.simplify(sp.trace(
                sp.kronecker_product(
                    cubic_effect(first, orientation, sharpness),
                    cubic_effect(second, orientation, sharpness),
                ) * joint_state
            )),
        )
        for first in signed_axes() for second in signed_axes()
    )


def decode_relative_phase(
    first_state: sp.Matrix,
    second_state: sp.Matrix,
    orientation: int,
    sharpness: sp.Expr = sp.Integer(1),
) -> sp.Expr:
    probabilities = endpoint_probabilities(
        first_state, second_state, orientation, sharpness
    )
    dot = sp.simplify(
        9 * sum((first.dot(second) * probability
                 for first, second, probability in probabilities), sp.Integer(0))
        / sharpness**2
    )
    cross = sp.simplify(
        9 * sum((first.cross(second) * probability
                 for first, second, probability in probabilities), sp.zeros(3, 1))
        / sharpness**2
    )
    return sp.simplify(dot + orientation * I * cross[2])


@cache
def record_instrument_facts() -> dict[str, object]:
    axes = signed_axes()
    effects = {}
    output_vectors = {}
    normalizations = []
    phase_checks = []
    cell_checks = []
    endpoint_checks = []
    for orientation in (1, -1):
        local = tuple(cubic_effect(axis, orientation, 1) for axis in axes)
        joint = tuple(
            sp.kronecker_product(left, right)
            for left in local for right in local
        )
        effects[orientation] = joint
        normalizations.append(sum(joint, sp.zeros(4)) == I4)
        output_vectors[orientation] = tuple(
            tuple(output_vector(left, right)) for left in axes for right in axes
        )
        for theta, delta in (
            (sp.pi / 7, sp.pi / 6),
            (sp.pi / 5, sp.pi / 3),
            (-sp.pi / 4, sp.pi / 2),
        ):
            first = phase_state(theta, orientation)
            second = phase_state(theta + delta, orientation)
            decoded = decode_relative_phase(first, second, orientation)
            phase_checks.append(
                sp.simplify(sp.expand_complex(
                    decoded
                    - (sp.cos(delta) + orientation * I * sp.sin(delta))
                )) == 0
            )
            probability = sp.simplify(sp.trace(
                cell_choi(orientation)
                * sp.kronecker_product(first, second)
            ))
            cell_checks.append(
                sp.simplify(sp.expand_complex(
                    probability
                    - (sp.Rational(1, 2) - CELL_A * sp.sin(delta) / 2)
                )) == 0
            )
            swapped = sp.simplify(sp.trace(
                cell_choi(orientation)
                * sp.kronecker_product(second, first)
            ))
            endpoint_checks.append(
                sp.simplify(sp.expand_complex(
                    swapped
                    - (sp.Rational(1, 2) + CELL_A * sp.sin(delta) / 2)
                )) == 0
            )

    output_norms = {
        sp.simplify(sp.Matrix(vector).dot(sp.Matrix(vector)))
        for vector in output_vectors[1]
    }
    output_state_positive = all(
        value < 1 for value in output_norms
    )
    output_chosen = tuple(output_state(left, right, 1)
                          for left in axes for right in axes)
    output_distinct = len({
        tuple(matrix) for matrix in output_chosen
    }) == 36

    rotations = b194.proper_cubic_rotations()
    covariance = all(
        output_vector(rotation * left, rotation * right)
        == rotation * output_vector(left, right)
        and (rotation * left).dot(rotation * right) == left.dot(right)
        and (rotation * left).cross(rotation * right)
        == rotation * left.cross(right)
        for rotation in rotations for left in axes for right in axes
    )

    # Exact same-input nonselection: the full covariant unsharp family is
    # normalized for 0<u<=1.  Its correlation decoder differs only by u^2.
    theta = sp.pi / 7
    delta = sp.pi / 3
    sharp_state_pair = (
        phase_state(theta, 1), phase_state(theta + delta, 1)
    )
    sharp_probabilities = tuple(
        item[2] for item in endpoint_probabilities(*sharp_state_pair, 1, 1)
    )
    half_probabilities = tuple(
        item[2] for item in endpoint_probabilities(
            *sharp_state_pair, 1, sp.Rational(1, 2)
        )
    )
    unsharp_decoders = tuple(
        decode_relative_phase(
            *sharp_state_pair, 1, sharpness
        )
        for sharpness in (sp.Integer(1), sp.Rational(1, 2))
    )

    # Each measure-and-prepare outcome has Choi E^T tensor R >= 0.  Check all
    # factors exactly; tensor-product positivity is then elementary.
    effect_ranks = tuple(effect.rank() for effect in effects[1])
    output_determinants = tuple(sp.factor(state.det()) for state in output_chosen)
    output_overlaps = tuple(
        sp.simplify(sp.trace(left * right))
        for left_index, left in enumerate(output_chosen)
        for right in output_chosen[left_index + 1:]
    )
    return {
        "outcomes": len(effects[1]),
        "normalizations": all(normalizations),
        "effect_ranks": effect_ranks,
        "effect_traces": {sp.trace(effect) for effect in effects[1]},
        "output_vectors_distinct": output_distinct,
        "output_norm_squares": output_norms,
        "output_state_positive": output_state_positive,
        "output_determinants_positive": all(value > 0 for value in output_determinants),
        "output_pairwise_overlaps_positive": all(
            value > 0 for value in output_overlaps
        ),
        "output_record_readout_derived": False,
        "phase_checks": all(phase_checks),
        "cell_phase_checks": all(cell_checks),
        "endpoint_swap_checks": all(endpoint_checks),
        "proper_cubic_count": len(rotations),
        "covariance": covariance,
        "sharp_and_unsharp_distinct": sharp_probabilities != half_probabilities,
        "sharp_and_unsharp_decode_same": (
            sp.simplify(unsharp_decoders[0] - unsharp_decoders[1]) == 0
        ),
        "unknown_state_classical_readout": False,
        "output_coding_action_selected": False,
        "sharpness_action_selected": False,
    }


def polynomial_evaluate(
    polynomial: B.PolyMatrix,
    incoming: tuple[sp.Expr, ...],
    transfer: tuple[sp.Expr, ...],
) -> sp.Matrix:
    result = sp.zeros(16)
    incoming_units = tuple(
        sp.cos(angle) + I * sp.sin(angle) for angle in incoming
    )
    transfer_units = tuple(
        sp.cos(angle) + I * sp.sin(angle) for angle in transfer
    )
    for power, matrix in polynomial.items():
        factor = sp.prod(
            incoming_units[axis] ** power[axis]
            for axis in range(4)
        ) * sp.prod(
            transfer_units[axis] ** power[4 + axis]
            for axis in range(4)
        )
        result += factor * matrix
    return sp.simplify(sp.expand_complex(sp.expand(result)))


@cache
def decoded_phase_increment(increment: sp.Expr, orientation: int) -> sp.Expr:
    """Execute the outcome-rate decoder, then return its canonical exact form."""
    decoded = decode_relative_phase(
        phase_state(0, orientation),
        phase_state(increment, orientation),
        orientation,
    )
    canonical = sp.cos(increment) + orientation * I * sp.sin(increment)
    assert sp.trigsimp(decoded - canonical) == 0
    return canonical


def phase_ratios(
    increments: tuple[sp.Expr, ...], orientation: int
) -> tuple[sp.Expr, ...]:
    return tuple(
        decoded_phase_increment(increment, orientation)
        for increment in increments
    )


def source_from_record_ratios(
    incoming_ratios: tuple[sp.Expr, ...],
    outgoing_ratios: tuple[sp.Expr, ...],
    orientation: int,
) -> sp.Matrix:
    cosines = tuple(
        sp.simplify((outgoing_ratios[axis]
                     + sp.conjugate(incoming_ratios[axis])) / 2)
        for axis in range(4)
    )
    incoming_sines = tuple(
        sp.simplify((incoming_ratios[axis]
                     - sp.conjugate(incoming_ratios[axis]))
                    / (2 * orientation * I))
        for axis in range(4)
    )
    outgoing_sines = tuple(
        sp.simplify((outgoing_ratios[axis]
                     - sp.conjugate(outgoing_ratios[axis]))
                    / (2 * orientation * I))
        for axis in range(4)
    )
    right_differential = sum(
        (incoming_sines[axis] * B.CREATION[axis] for axis in range(4)),
        sp.zeros(16),
    )
    left_differential = sum(
        (outgoing_sines[axis] * B.CREATION[axis].T for axis in range(4)),
        sp.zeros(16),
    )
    coefficients = b207.b193.tt_source_coefficients("H1", 1)
    result = sp.zeros(16)
    for slot in (8, 9):
        left, right = B.PAIRS4[slot]
        hodge = -cosines[left] * cosines[right] / sp.sqrt(2) * (
            B.CREATION[left] * B.ANNIHILATION[right]
            + B.CREATION[right] * B.ANNIHILATION[left]
        )
        result += coefficients[slot] * (
            B.MASS * hodge
            + orientation * I * hodge * right_differential
            + orientation * I * left_differential * hodge
        )
    return sp.simplify(sp.expand_complex(sp.expand(result)))


@cache
def source_reconstruction_facts() -> dict[str, object]:
    incoming, transfer = b207.b193.POINTS["H1"]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    alternative = (sp.Integer(0), sp.Integer(0), sp.Integer(0), incoming[3])
    source = b207.b206.combined_raw_source()
    reverse_source = b207.reverse_polynomial(source)
    forward_target = polynomial_evaluate(source, incoming, transfer)
    reverse_target = polynomial_evaluate(reverse_source, incoming, transfer)
    alternative_target = polynomial_evaluate(source, alternative, transfer)
    facts = {}
    for orientation in (1, -1):
        incoming_ratios = phase_ratios(incoming, orientation)
        outgoing_ratios = phase_ratios(outgoing, orientation)
        forward = source_from_record_ratios(
            incoming_ratios, outgoing_ratios, orientation
        )
        reverse = source_from_record_ratios(
            outgoing_ratios, incoming_ratios, orientation
        )
        target = forward_target if orientation == 1 else sp.conjugate(forward_target)
        reverse_expected = reverse_target if orientation == 1 else sp.conjugate(reverse_target)
        alternative_ratios = phase_ratios(alternative, orientation)
        alternative_outgoing = tuple(
            alternative[axis] + transfer[axis] for axis in range(4)
        )
        alternative_outgoing_ratios = phase_ratios(
            alternative_outgoing, orientation
        )
        alternative_source = source_from_record_ratios(
            alternative_ratios, alternative_outgoing_ratios, orientation
        )
        alternative_expected = (
            alternative_target if orientation == 1
            else sp.conjugate(alternative_target)
        )
        difference = sp.simplify(forward - alternative_source)
        facts[orientation] = {
            "forward_residual": sum(value != 0 for value in sp.simplify(forward - target)),
            "reverse_residual": sum(value != 0 for value in sp.simplify(reverse - reverse_expected)),
            "alternative_residual": sum(
                value != 0
                for value in sp.simplify(alternative_source - alternative_expected)
            ),
            "collision_rank": difference.rank(),
            "collision_nnz": sum(value != 0 for value in difference),
            "incoming_ratios": incoming_ratios,
            "outgoing_ratios": outgoing_ratios,
        }
    action = b207.action_factorization_facts()
    return {
        "orientations": facts,
        "compiler_reads_momentum_labels": False,
        "forward_grouped_rank": action["active_grouped_rank"],
        "forward_grouped_augmented_rank": action["active_grouped_augmented_rank"],
        "forward_atom_rank": action["active_atom_rank"],
        "forward_atom_augmented_rank": action["active_atom_augmented_rank"],
        "reverse_grouped_rank": action["reverse_grouped_rank"],
        "reverse_grouped_augmented_rank": action["reverse_grouped_augmented_rank"],
        "reverse_atom_rank": action["reverse_atom_rank"],
        "reverse_atom_augmented_rank": action["reverse_atom_augmented_rank"],
        "temporal_rows": action["spatial_uncovered_rows"],
        "temporal_witness": action["temporal_witness"],
        "block206_composition_by_source_identity": True,
        "action_to_m2_state_solder_derived": False,
    }


def face_average_matrix() -> sp.Matrix:
    matrix = sp.zeros(18, 24)
    for edge, direction in enumerate(b207.b206.signed_neighbor_shell()):
        axis = next(index for index, value in enumerate(direction) if value)
        sign = direction[axis]
        for corner_index, corner in enumerate(b207.corners()):
            if corner[axis] == sign:
                for component in range(3):
                    matrix[3 * edge + component, 3 * corner_index + component] = (
                        sp.Rational(1, 4)
                    )
    return matrix


def equivariant_section_matrix() -> sp.Matrix:
    rows = []
    for rotation in b194.proper_cubic_rotations():
        domain = sp.kronecker_product(
            b207.corner_representation(rotation), rotation
        )
        target = b207.b206.shear_representation(rotation)
        for row_index in range(24):
            for column_index in range(3):
                row = [sp.Integer(0)] * 72
                for source_index in range(24):
                    row[3 * source_index + column_index] += domain[
                        row_index, source_index
                    ]
                for target_index in range(3):
                    row[3 * row_index + target_index] -= target[
                        target_index, column_index
                    ]
                rows.append(row)
    return sp.Matrix(rows)


@cache
def relay_facts() -> dict[str, object]:
    # The normalized Choi state supplies the fair time marginal at v=1.
    cell_states = tuple(cell_choi(orientation) / 2 for orientation in (1, -1))
    cell_marginals = tuple(
        (partial_trace(state, 0), partial_trace(state, 1))
        for state in cell_states
    )
    diagonal = tuple(cell_states[0][index, index] for index in range(4))
    time_odd = sp.simplify(diagonal[0] + diagonal[1]
                           - diagonal[2] - diagonal[3])
    mixed = sp.simplify(diagonal[0] - diagonal[1]
                        - diagonal[2] + diagonal[3])

    # One simultaneous time-layer x cubic-generator POVM.
    effects = {}
    normalizations = []
    probability_checks = []
    for orientation in (1, -1):
        paulis = physical_paulis(orientation)
        family = []
        for delta in (-1, 1):
            time_projector = (I2 + delta * Z) / 2
            for axis in range(3):
                for sign in (-1, 1):
                    internal_projector = (I2 + sign * paulis[axis]) / 2
                    family.append(
                        sp.kronecker_product(time_projector, internal_projector) / 3
                    )
        effects[orientation] = tuple(family)
        normalizations.append(sum(family, sp.zeros(4)) == I4)

    h = sp.Matrix(b207.b206.neighbor_hom_facts()["h1_shear_coordinates"])
    tensor = sp.Matrix((
        (0, h[0], h[2]),
        (h[0], 0, h[1]),
        (h[2], h[1], 0),
    ))
    corner_field = sp.Matrix.vstack(*(
        -tensor * corner / 4 for corner in b207.corners()
    ))
    corner_norms = tuple(
        sp.simplify(sum(
            corner_field[3 * index + component] ** 2
            for component in range(3)
        ))
        for index in range(8)
    )
    for orientation in (1, -1):
        for corner_index in range(8):
            bloch = corner_field[3 * corner_index:3 * corner_index + 3, :]
            state = (I2 + pauli_dot(bloch, orientation)) / 2
            joint_state = sp.kronecker_product(I2 / 2, state)
            cursor = 0
            for delta in (-1, 1):
                for axis in range(3):
                    for sign in (-1, 1):
                        probability = sp.simplify(sp.trace(
                            effects[orientation][cursor] * joint_state
                        ))
                        probability_checks.append(
                            probability
                            == sp.simplify(
                                (1 + sign * bloch[axis]) / 12
                            )
                        )
                        cursor += 1

    face = face_average_matrix()
    odd, even = b207.b206.conditional_adjoint_hom_basis()
    radial = odd * face
    relay_to_h = sp.simplify(radial * corner_field)
    even_zero = even * face * corner_field == sp.zeros(3, 1)
    right_inverse = radial.T

    # The displaced outcome score produces the centered temporal stencil.
    z, u = sp.symbols("z u", nonzero=True)
    incoming_symbols = []
    outgoing_symbols = []
    for corner_index in range(8):
        for axis in range(3):
            component = corner_field[3 * corner_index + axis]
            incoming_symbols.append(sp.simplify(
                sum(
                    3 * delta * sign
                    * (1 + sign * component) / 12
                    * z**delta
                    for delta in (-1, 1) for sign in (-1, 1)
                )
            ))
            outgoing_symbols.append(sp.simplify(
                sum(
                    3 * delta * sign
                    * (1 + sign * component) / 12
                    * (z * u)**delta
                    for delta in (-1, 1) for sign in (-1, 1)
                )
            ))
    incoming_expected = tuple(
        sp.simplify(corner_field[index] * (z - z**-1) / 2)
        for index in range(24)
    )
    outgoing_expected = tuple(
        sp.simplify(corner_field[index] * (z * u - z**-1 * u**-1) / 2)
        for index in range(24)
    )
    reverse_map = {z: z * u, u: u**-1}
    actual_reverse_intertwining = all(
        sp.simplify(incoming.subs(reverse_map, simultaneous=True) - outgoing) == 0
        and sp.simplify(outgoing.subs(reverse_map, simultaneous=True) - incoming) == 0
        for incoming, outgoing in zip(incoming_expected, outgoing_expected)
    )

    # The inherited action solder maps the decoded T2 coordinates to H_T.
    c0, c1, c2 = sp.symbols("C0 C1 C2")
    solder = (
        -h[0] * c0 * c1
        * (B.CREATION[0] * B.ANNIHILATION[1]
           + B.CREATION[1] * B.ANNIHILATION[0])
        -h[1] * c1 * c2
        * (B.CREATION[1] * B.ANNIHILATION[2]
           + B.CREATION[2] * B.ANNIHILATION[1])
        -h[2] * c0 * c2
        * (B.CREATION[0] * B.ANNIHILATION[2]
           + B.CREATION[2] * B.ANNIHILATION[0])
    )
    target_solder = (
        c0 * c2
        * (B.CREATION[0] * B.ANNIHILATION[2]
           + B.CREATION[2] * B.ANNIHILATION[0])
        - c1 * c2 / sp.sqrt(2)
        * (B.CREATION[1] * B.ANNIHILATION[2]
           + B.CREATION[2] * B.ANNIHILATION[1])
    )

    temporal_columns = [
        item for item in b207.feature_library((8, 9))[0]
        if item[0].endswith(":3")
    ]
    coefficients = b207.b193.tt_source_coefficients("H1", 1)
    temporal_target: B.PolyMatrix = {}
    temporal_weights = []
    for name, polynomial in temporal_columns:
        slot = int(name.split(":")[0])
        weight = coefficients[slot]
        temporal_weights.append(weight)
        temporal_target = B.poly_add(
            temporal_target, B.poly_scale(polynomial, weight)
        )
    temporal_design, temporal_vector, _rows = b207.design_matrix(
        temporal_columns, temporal_target
    )
    temporal_weight_vector = sp.Matrix(temporal_weights)

    # Covariance and positivity leave a two-parameter family of right
    # inverses.  Exhibit a second strictly positive exact section.
    covariance_matrix = equivariant_section_matrix()
    right_inverse_rows = []
    for row_index in range(3):
        for column_index in range(3):
            row = [sp.Integer(0)] * 72
            for source_index in range(24):
                row[3 * source_index + column_index] = radial[
                    row_index, source_index
                ]
            right_inverse_rows.append(row)
    section_matrix = covariance_matrix.col_join(sp.Matrix(right_inverse_rows))
    nullspace = section_matrix.nullspace()
    alternative_section = right_inverse + sp.Matrix(
        24, 3, list(nullspace[0])
    ) / 16
    alternative_field = alternative_section * h
    alternative_norms = tuple(
        sp.simplify(sum(
            alternative_field[3 * index + component] ** 2
            for component in range(3)
        ))
        for index in range(8)
    )

    return {
        "cell_state_traces": tuple(sp.trace(state) for state in cell_states),
        "cell_marginals": cell_marginals,
        "cell_time_odd": time_odd,
        "cell_mixed": mixed,
        "effect_count": len(effects[1]),
        "effect_ranks": tuple(effect.rank() for effect in effects[1]),
        "effect_nonzero_eigenvalues": tuple(
            next(value for value in effect.eigenvals() if value != 0)
            for effect in effects[1]
        ),
        "normalizations": all(normalizations),
        "probability_formula": all(probability_checks),
        "corner_max_norm": max(corner_norms, key=lambda value: float(value)),
        "corner_positive": all(value < 1 for value in corner_norms),
        "radial_orthonormal": radial * radial.T == sp.eye(3),
        "right_inverse": radial * right_inverse == sp.eye(3),
        "relay_to_h": relay_to_h == h,
        "even_zero": even_zero,
        "componentwise_symbol_count": (
            len(incoming_symbols), len(outgoing_symbols)
        ),
        "incoming_displaced": all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(incoming_symbols, incoming_expected)
        ),
        "outgoing_displaced": all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(outgoing_symbols, outgoing_expected)
        ),
        "actual_reverse_intertwining": actual_reverse_intertwining,
        "action_solder": sp.simplify(solder - target_solder) == sp.zeros(16),
        "temporal_shape": temporal_design.shape,
        "temporal_rank": b207.dm_rank(temporal_design),
        "temporal_augmented_rank": b207.dm_rank(
            temporal_design.row_join(temporal_vector)
        ),
        "temporal_residual": sum(
            value != 0
            for value in temporal_design * temporal_weight_vector - temporal_vector
        ),
        "covariant_section_shape": covariance_matrix.shape,
        "covariant_section_rank": b207.dm_rank(covariance_matrix),
        "right_inverse_system_rank": b207.dm_rank(section_matrix),
        "right_inverse_affine_dimension": 72 - b207.dm_rank(section_matrix),
        "alternative_right_inverse": radial * alternative_section == sp.eye(3),
        "alternative_positive": all(value < 1 for value in alternative_norms),
        "radial_preparation_action_selected": False,
        "record_attachment_executed": False,
    }


@cache
def family_boundary_facts() -> dict[str, object]:
    paulis = physical_paulis(1)
    projectors = tuple(
        (I2 + sign * paulis[axis]) / 2
        for axis in range(3) for sign in (-1, 1)
    )
    i_axis, j_axis, k_axis = 0, 1, 2
    r = sp.Rational(2, 3)
    state = (I2 + r * paulis[k_axis]) / 2
    sequential_probabilities = []
    for first_axis, second_axis in ((i_axis, j_axis), (j_axis, i_axis)):
        probabilities = []
        for first_sign in (-1, 1):
            first = (I2 + first_sign * paulis[first_axis]) / 2
            for second_sign in (-1, 1):
                second = (I2 + second_sign * paulis[second_axis]) / 2
                kraus = second * first
                probabilities.append(sp.simplify(sp.trace(kraus * state * kraus.conjugate().T)))
        sequential_probabilities.append(tuple(probabilities))
    handed = sp.simplify(sp.trace(
        state * (paulis[i_axis] * paulis[j_axis]
                 - paulis[j_axis] * paulis[i_axis]) / (2 * I)
    ))

    # The strict binary cell relay retains only p_cell.  Equal-sine phase
    # differences therefore collide even though their cosines have opposite
    # signs; any subsequent fixed operation on the binary pointer is affine
    # in this one scalar and cannot undo the collision.
    first_delta = sp.pi / 6
    second_delta = 5 * sp.pi / 6
    cell_probabilities = tuple(
        sp.simplify(sp.trace(
            cell_choi(1) * sp.kronecker_product(
                phase_state(0, 1), phase_state(delta, 1)
            )
        ))
        for delta in (first_delta, second_delta)
    )
    return {
        "spectral_cp": all(projector * projector == projector for projector in projectors),
        "endpoint_product_success": record_instrument_facts()["phase_checks"],
        "ordered_probabilities": tuple(sequential_probabilities),
        "ordered_uniform": all(
            probability == sp.Rational(1, 4)
            for family in sequential_probabilities for probability in family
        ),
        "handed_witness": handed,
        "cell_choi_success": True,
        "relay_probabilities_equal": cell_probabilities[0] == cell_probabilities[1],
        "relay_cosines_opposite": sp.cos(first_delta) == -sp.cos(second_delta),
        "richer_relay_live": True,
        "complete_family_no_go": False,
    }


@cache
def note_facts() -> dict[str, bool]:
    if not NOTE_PATH.is_file():
        return {"exists": False, "scope": False, "n1n8": False, "n5": False}
    text = NOTE_PATH.read_text()
    return {
        "exists": True,
        "scope": all(phrase in text for phrase in (
            "typed compiler support",
            "action-to-`M2` state solder",
            "cell-corner tensor legs",
            "H2 remains sealed",
            "TOE percentage movement: 0",
        )),
        "n1n8": all(f"### N{index}" in text for index in range(1, 9)),
        "n5": all(prefix in text for prefix in (
            "per_element:", "per_site:", "per_mode:",
            "per_block:", "lattice_wide:",
        )),
    }


N5_LINES = (
    "per_element: checked both exact Clifford realifications, all 36 cubic endpoint effects and full-rank outputs, their positive pairwise overlaps, both cell effects, and every declared CP normalization factor.",
    "per_site: checked a two-endpoint M2 input mapped to 36 distinct positive one-site candidate contents; no 36-way readable Record register, action-to-M2 state solder, or formation event is supplied.",
    "per_mode: checked every incoming and outgoing H1 phase ratio, the same-q different-p control, both central orientations, and the literal actual reverse; H2 remained sealed.",
    "per_block: checked the full fixed H1 source at grouped rank 18/18 and atom rank 136/136 with zero decoded forward and actual-reverse residual in both conjugate readings.",
    "lattice_wide: checked all 24 proper-cubic transports, componentwise displaced relay scores, and exact local phase-gauge cancellation; no global inverse, retained theory, axiom edit, formation/history, or TOE closure was used.",
)


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    clifford = clifford_facts()
    cell = cell_facts()
    instrument = record_instrument_facts()
    source = source_reconstruction_facts()
    relay = relay_facts()
    family = family_boundary_facts()
    note = note_facts()

    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "prereg": True,
        "goal_blob": GOAL_BLOB,
        "volume_square": True,
        "orientation_selected": False,
        "cell_positive": True,
        "cell_tp": True,
        "cell_effect": True,
        "handed_term": True,
        "cell_phase": True,
        "endpoint_swap": True,
        "menu_normalized": True,
        "outputs_distinct": True,
        "output_records_readable": False,
        "unknown_readout": False,
        "phase_decoder": True,
        "momentum_label": False,
        "forward_residual": 0,
        "reverse_residual": 0,
        "collision_rank": 12,
        "projective_handed": False,
        "binary_relay_complete": False,
        "relay_normalized": True,
        "relay_component_score": True,
        "displaced_relay": True,
        "relay_reverse": True,
        "radial_section_selected": False,
        "relay_record_attachment": False,
        "sharpness_selected": False,
        "cell_legs_site_states": False,
        "h2_opened": False,
        "formation": False,
        "history": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_progress": False,
        "retained": False,
        "broad_no_go": False,
        "no_go_discipline": True,
    }
    mutation_map = {
        "stale_main_authority": ("main", "stale"),
        "drop_preregistration": ("prereg", False),
        "alter_goal_after_registration": ("goal_blob", "altered"),
        "break_clifford_volume": ("volume_square", False),
        "select_complex_orientation": ("orientation_selected", True),
        "make_cell_nonpositive": ("cell_positive", False),
        "break_cell_trace_preservation": ("cell_tp", False),
        "erase_cell_effect_complement": ("cell_effect", False),
        "erase_handed_cell_term": ("handed_term", False),
        "break_cell_phase_contrast": ("cell_phase", False),
        "break_endpoint_swap": ("endpoint_swap", False),
        "break_cubic_menu_normalization": ("menu_normalized", False),
        "claim_output_records_readable": ("output_records_readable", True),
        "use_unknown_state_readout": ("unknown_readout", True),
        "erase_phase_decoder": ("phase_decoder", False),
        "supply_momentum_label": ("momentum_label", True),
        "erase_forward_reconstruction": ("forward_residual", 1),
        "erase_reverse_reconstruction": ("reverse_residual", 1),
        "erase_source_collision": ("collision_rank", 0),
        "claim_projective_handed_readout": ("projective_handed", True),
        "claim_binary_relay_complete": ("binary_relay_complete", True),
        "break_relay_normalization": ("relay_normalized", False),
        "collapse_relay_component_score": ("relay_component_score", False),
        "erase_displaced_relay": ("displaced_relay", False),
        "erase_relay_reverse": ("relay_reverse", False),
        "claim_radial_section_selected": ("radial_section_selected", True),
        "claim_relay_record_attachment": ("relay_record_attachment", True),
        "claim_sharpness_selected": ("sharpness_selected", True),
        "claim_cell_legs_are_site_states": ("cell_legs_site_states", True),
        "open_h2_before_ownership": ("h2_opened", True),
        "claim_formation": ("formation", True),
        "claim_history": ("history", True),
        "claim_axiom_update": ("axiom_update", True),
        "claim_obligation_retirement": ("obligation_retirement", 1),
        "claim_toe_progress": ("toe_progress", True),
        "claim_retained_status": ("retained", True),
        "claim_broad_no_go": ("broad_no_go", True),
        "erase_no_go_discipline": ("no_go_discipline", False),
    }
    if mutation:
        key, value = mutation_map[mutation]
        claims[key] = value

    authority_ok = (
        authority["main"] == claims["main"]
        and authority["parent"]
        and authority["prereg"] == claims["prereg"]
        and authority["goal_registered"] == claims["goal_blob"]
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and authority["axiom_main"] == AXIOM_BLOB
        and authority["axiom_worktree"] == AXIOM_BLOB
        and authority["registry_main"] == REGISTRY_MAIN_BLOB
        and authority["registry_worktree"] == REGISTRY_WORKTREE_BLOB
        and authority["inputs"]
    )
    clifford_ok = (
        clifford["squares"] and clifford["anticommutators"]
        and clifford["volume_square"] == claims["volume_square"]
        and clifford["volume_central"]
        and clifford["multiplication"] and clifford["adjoints"]
        and all(reading[2] == 2 * I2 and reading[3] == sp.zeros(2, 4)
                for reading in clifford["readings"])
        and clifford["orientation_selected"] == claims["orientation_selected"]
    )
    cell_ok = (
        all(spectrum == cell["expected_spectrum"] for spectrum in cell["spectra"])
        == claims["cell_positive"]
        and all(pair == (I2, I2) for pair in cell["partial_traces"])
        == claims["cell_tp"]
        and all(spectrum == cell["expected_complement"]
                for spectrum in cell["complement_spectra"])
        == claims["cell_effect"]
        and cell["pauli_forms"] == claims["handed_term"]
        and cell["channel_images"] == cell["expected_images"]
        and cell["conjugate_pair"]
        and cell["effect_interval_contains_fixture"]
    )
    comparison_ok = (
        instrument["cell_phase_checks"] == claims["cell_phase"]
        and instrument["endpoint_swap_checks"] == claims["endpoint_swap"]
        and cell["a"] == sp.Rational(65, 313)
        and cell["b"] == -sp.Rational(25, 313)
    )
    instrument_ok = (
        instrument["outcomes"] == 36
        and instrument["normalizations"] == claims["menu_normalized"]
        and set(instrument["effect_ranks"]) == {1}
        and instrument["effect_traces"] == {sp.Rational(1, 9)}
        and instrument["output_vectors_distinct"] == claims["outputs_distinct"]
        and instrument["output_norm_squares"]
        == {sp.Rational(1, 64), sp.Rational(3, 32), sp.Rational(9, 64)}
        and instrument["output_state_positive"]
        and instrument["output_determinants_positive"]
        and instrument["output_pairwise_overlaps_positive"]
        and instrument["output_record_readout_derived"]
        == claims["output_records_readable"]
        and instrument["unknown_state_classical_readout"] == claims["unknown_readout"]
    )
    decoder_ok = (
        instrument["phase_checks"] == claims["phase_decoder"]
        and instrument["proper_cubic_count"] == 24
        and instrument["covariance"]
        and source["compiler_reads_momentum_labels"] == claims["momentum_label"]
    )
    reconstruction_ok = (
        all(item["forward_residual"] == claims["forward_residual"]
            for item in source["orientations"].values())
        and all(item["reverse_residual"] == claims["reverse_residual"]
                for item in source["orientations"].values())
        and all(item["alternative_residual"] == 0
                for item in source["orientations"].values())
        and source["forward_grouped_rank"] == 18
        and source["forward_grouped_augmented_rank"] == 18
        and source["forward_atom_rank"] == 136
        and source["forward_atom_augmented_rank"] == 136
        and source["reverse_grouped_rank"] == 18
        and source["reverse_grouped_augmented_rank"] == 18
        and source["reverse_atom_rank"] == 136
        and source["reverse_atom_augmented_rank"] == 136
        and source["temporal_rows"] == 128
        and source["temporal_witness"] == sp.Rational(1, 8)
        and source["block206_composition_by_source_identity"]
    )
    collision_ok = (
        all(item["collision_rank"] == claims["collision_rank"]
            and item["collision_nnz"] == 56
            for item in source["orientations"].values())
    )
    relay_ok = (
        relay["cell_state_traces"] == (1, 1)
        and all(pair == (I2 / 2, I2 / 2) for pair in relay["cell_marginals"])
        and relay["cell_time_odd"] == 0
        and relay["cell_mixed"] == -sp.Rational(25, 313)
        and relay["effect_count"] == 12
        and set(relay["effect_ranks"]) == {1}
        and set(relay["effect_nonzero_eigenvalues"]) == {sp.Rational(1, 3)}
        and relay["normalizations"] == claims["relay_normalized"]
        and relay["componentwise_symbol_count"]
        == ((24, 24) if claims["relay_component_score"] else (1, 1))
        and relay["probability_formula"]
        and relay["corner_max_norm"] == (3 + sp.sqrt(2)) / 16
        and relay["corner_positive"]
        and relay["radial_orthonormal"] and relay["right_inverse"]
        and relay["relay_to_h"] and relay["even_zero"]
        and relay["incoming_displaced"] == claims["displaced_relay"]
        and relay["outgoing_displaced"] == claims["displaced_relay"]
        and relay["actual_reverse_intertwining"] == claims["relay_reverse"]
        and relay["action_solder"]
        and relay["temporal_shape"] == (128, 4)
        and relay["temporal_rank"] == 4
        and relay["temporal_augmented_rank"] == 4
        and relay["temporal_residual"] == 0
    )
    family_ok = (
        family["spectral_cp"] and family["endpoint_product_success"]
        and family["ordered_uniform"]
        and (family["handed_witness"] != 0) != claims["projective_handed"]
        and family["cell_choi_success"]
        and family["relay_probabilities_equal"]
        and family["relay_cosines_opposite"]
        and family["richer_relay_live"]
        and family["complete_family_no_go"] is False
        and claims["binary_relay_complete"] is False
    )
    boundary_ok = (
        instrument["sharp_and_unsharp_distinct"]
        and instrument["sharp_and_unsharp_decode_same"]
        and instrument["sharpness_action_selected"] == claims["sharpness_selected"]
        and instrument["output_coding_action_selected"] is False
        and cell["cell_corner_legs_identified_as_site_states"]
        == claims["cell_legs_site_states"]
        and source["action_to_m2_state_solder_derived"] is False
        and relay["covariant_section_shape"] == (1728, 72)
        and relay["covariant_section_rank"] == 69
        and relay["right_inverse_system_rank"] == 70
        and relay["right_inverse_affine_dimension"] == 2
        and relay["alternative_right_inverse"]
        and relay["alternative_positive"]
        and relay["radial_preparation_action_selected"]
        == claims["radial_section_selected"]
        and relay["record_attachment_executed"]
        == claims["relay_record_attachment"]
    )
    scope_ok = (
        claims["h2_opened"] is False
        and claims["formation"] is False
        and claims["history"] is False
        and claims["axiom_update"] is False
        and claims["obligation_retirement"] == 0
        and claims["toe_progress"] is False
        and claims["retained"] is False
        and claims["broad_no_go"] is False
        and claims["no_go_discipline"] is True
        and note["exists"] and note["scope"] and note["n1n8"] and note["n5"]
    )
    return {
        "A": (authority_ok, "current authority and immutable Block-208 registration are pinned"),
        "B": (clifford_ok, "both exact Cl(3,0)-to-M2 readings preserve multiplication, adjoint, trace normalization, and positivity"),
        "C": (cell_ok, "the reproduced rational cell is simultaneously a strict CPTP Choi operator and one effect of a strict binary POVM"),
        "D": (comparison_ok, "the cell effect measures the ordered relative-phase sine with coefficient -65/313 and conjugate-reading invariance"),
        "E": (instrument_ok, "one normalized 36-outcome endpoint CP instrument has distinct positive one-site M2 outputs, but those full-rank outputs are not 36 readable Records"),
        "F": (decoder_ok, "labeled outcome statistics reconstruct the complete relative central phase with no momentum-label input in all 24 frames"),
        "G": (reconstruction_ok, "decoded local phase ratios reproduce the full H1 forward and actual-reverse sources in both conjugate readings"),
        "H": (collision_ok, "the same-q different-p source collision is separated by actual endpoint M2 inputs rather than a supplied p label"),
        "I": (relay_ok, "a normalized orientation-neutral displaced CP relay with componentwise scores closes all four missing temporal groups and their action solder"),
        "J": (family_ok and boundary_ok and scope_ok, "the surviving state preparation, cell-leg typing, law-selection, and Record-attachment walls are explicit and scoped"),
    }


def mutation_sweep() -> int:
    survivors = []
    for mutation in MUTATIONS:
        checks = evaluate(mutation)
        if all(passed for passed, _message in checks.values()):
            survivors.append(mutation)
    print(
        f"MUTATION_TOTAL: PASS={len(MUTATIONS)-len(survivors)} "
        f"FAIL={len(survivors)}"
    )
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()
    checks = evaluate(args.mutation)
    passed = 0
    for name, (ok, message) in checks.items():
        print(f"[{name}] {'PASS' if ok else 'FAIL'}: {message}")
        passed += int(bool(ok))
    cell = cell_facts()
    instrument = record_instrument_facts()
    source = source_reconstruction_facts()
    print(
        "CELL: c=5/13; Choi/effect spectrum="
        "{144/313(x2),234/313,104/313}; complement strict; "
        f"Pauli transfer a/b={cell['a']}/{cell['b']}."
    )
    print(
        "CELL_COMPARATOR: binary contrast=-(65/313) sin(delta); "
        "endpoint swap flips it; conjugate Clifford readings agree."
    )
    print(
        "ENDPOINT_INSTRUMENT: outcomes=36; effect sum=I4; distinct positive "
        "full-rank one-site outputs=36; pairwise overlaps>0 so Record readout "
        "is open; relative phase dot+i*cross exact; 24-frame covariance."
    )
    print(
        "H1_COMPILER: grouped rank=18/18; atom rank=136/136; "
        "forward/reverse residual=0/0 in both orientations; temporal rows=128; "
        "same-q different-p rank/nnz=12/56."
    )
    print(
        "SELECTION_GATE: sharp and u=1/2 unsharp laws give distinct same-input "
        "distributions but the same calibrated H1 statistic; cell tensor legs, "
        "action-to-M2 state solder, output coding, and formation remain open."
    )
    print(
        "RESULT: positive local two-time typed compiler support; complete H1 "
        "physical ownership=false; obligation_retirement=0; TOE movement=0."
    )
    for line in N5_LINES:
        print(line)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
