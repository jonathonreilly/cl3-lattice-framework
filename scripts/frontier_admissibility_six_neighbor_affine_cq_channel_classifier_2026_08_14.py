#!/usr/bin/env python3
"""Block 99: classify affine six-neighbour Record-to-qubit channels.

The calculation starts from the six actual nearest-neighbour slots, rather
than inserting the Block85 axis barycenter.  It classifies linear occupancy
to Bloch intertwiners, tests the cost of a spatial/Pauli soldering, constructs
an independent-symmetry output-only content-average channel on actual M_2(C)
Record inputs, checks its nondemolition boundary, and checks exact CPTP,
ensemble, and joint-law countermodels.  The result is a decision-ready
one-step response/coupling cut conditional on formation, not adoption of a
microscopic law or complete dynamics.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import hashlib

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

AUDIT_INPUT_PATHS = (
    'docs/ADMISSIBILITY_SIX_NEIGHBOR_AFFINE_CQ_CHANNEL_SOLDER_SUPPORT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/audit/data/axiom_premise_nodes.json',
    'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md',
    'docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md',
    'docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    'docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md',
    'docs/ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    'docs/RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    'docs/ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'scripts/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py',
    'docs/ADMISSIBILITY_AXIS_SEPARABLE_BARYCENTER_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'scripts/frontier_admissibility_axis_separable_barycenter_selector_2026_08_14.py',
)

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SIX_NEIGHBOR_AFFINE_CQ_CHANNEL_SOLDER_SUPPORT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
RUNNER_RELATIVE = (
    "scripts/frontier_admissibility_six_neighbor_affine_cq_channel_"
    "classifier_2026_08_14.py"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_AXIS_SEPARABLE_BARYCENTER_SELECTOR_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/frontier_admissibility_axis_separable_barycenter_selector_"
    "2026_08_14.py"
)

HISTORICAL_MAIN = "eee6ab5874e2fc207db5526dc82d9f71ae550c7c"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
PARENT_COMMIT = "5ba5aa1c65bef9142428653e3ccd8ad0186283fb"
HISTORICAL_PARENT_NOTE_BLOB = "0a0df8d3f15bc2a5962273db806ad6d7f15444d6"
HISTORICAL_PARENT_RUNNER_BLOB = "3cd7aa25cba51316a8dbb36cabde0dedd38b48b7"

CURRENT_PARENT_NOTE_SHA256 = "5aa5e8549b928d49025e52ff705a3a2b39a9ec5cf8fd1a4e5ebea7659452218b"
CURRENT_PARENT_RUNNER_SHA256 = "18b3c4ef644b73b22fb5258dc675ed940a444449ccedc4533de8e415da1714bc"

I2 = sp.eye(2)
SIGMA = (
    sp.Matrix(((0, 1), (1, 0))),
    sp.Matrix(((0, -sp.I), (sp.I, 0))),
    sp.Matrix(((1, 0), (0, -1))),
)
SLOTS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
CONDITIONS = tuple(product((0, 1), repeat=6))
DIRECTIONS = tuple(
    direction
    for direction in product((-1, 0, 1), repeat=3)
    if direction != (0, 0, 0)
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 190 else detail[:187] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed





def worktree_blob(relative: str) -> str:
    data = (ROOT / relative).read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(left[row, column] - right[row, column]) == 0
        for row in range(left.rows)
        for column in range(left.cols)
    )


def vector_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return matrix_equal(sp.Matrix(left), sp.Matrix(right))


def proper_cubic_rotations() -> tuple[sp.ImmutableMatrix, ...]:
    rotations: set[sp.ImmutableMatrix] = set()
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for source_axis, target_axis in enumerate(permutation):
                matrix[target_axis, source_axis] = signs[source_axis]
            if matrix.det() == 1:
                rotations.add(sp.ImmutableMatrix(matrix))
    return tuple(sorted(rotations, key=lambda item: tuple(item)))


ROTATIONS = proper_cubic_rotations()


def slot_column(slot: tuple[int, int, int]) -> sp.Matrix:
    return sp.Matrix(slot)


def slot_action(rotation: sp.Matrix) -> sp.Matrix:
    action = sp.zeros(6)
    for source_index, slot in enumerate(SLOTS):
        rotated = rotation * slot_column(slot)
        target_index = next(
            index
            for index, candidate in enumerate(SLOTS)
            if vector_equal(rotated, slot_column(candidate))
        )
        action[target_index, source_index] = 1
    return action


def rotate_condition(
    rotation: sp.Matrix, condition: tuple[int, ...]
) -> tuple[int, ...]:
    transformed = slot_action(rotation) * sp.Matrix(condition)
    return tuple(int(value) for value in transformed)


def difference(condition: tuple[int, ...]) -> sp.Matrix:
    return sp.Matrix(
        (
            condition[0] - condition[1],
            condition[2] - condition[3],
            condition[4] - condition[5],
        )
    )


def bloch_operator(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        sum(
            (sp.simplify(vector[index]) * SIGMA[index] for index in range(3)),
            sp.zeros(2),
        )
    )


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify((I2 + bloch_operator(vector)) / 2)


def diagonal_intertwiner_basis() -> tuple[sp.Matrix, ...]:
    rows: list[list[sp.Expr]] = []
    for rotation in ROTATIONS:
        action = slot_action(rotation)
        for output_axis in range(3):
            for input_slot in range(6):
                row: list[sp.Expr] = [sp.Integer(0)] * 18
                for source_slot in range(6):
                    row[output_axis * 6 + source_slot] += action[
                        source_slot, input_slot
                    ]
                for source_axis in range(3):
                    row[source_axis * 6 + input_slot] -= rotation[
                        output_axis, source_axis
                    ]
                rows.append(row)
    kernel = sp.Matrix(rows).nullspace()
    return tuple(sp.Matrix(3, 6, list(vector)) for vector in kernel)


def fixed_vector_basis() -> tuple[sp.Matrix, ...]:
    constraints = sp.Matrix.vstack(
        *(sp.Matrix(rotation) - sp.eye(3) for rotation in ROTATIONS)
    )
    return tuple(constraints.nullspace())


def internal_commutant_basis() -> tuple[sp.Matrix, ...]:
    rows: list[list[sp.Expr]] = []
    for rotation in ROTATIONS:
        for left_index in range(3):
            for right_index in range(3):
                row: list[sp.Expr] = [sp.Integer(0)] * 9
                for middle in range(3):
                    row[left_index * 3 + middle] += rotation[middle, right_index]
                    row[middle * 3 + right_index] -= rotation[left_index, middle]
                rows.append(row)
    kernel = sp.Matrix(rows).nullspace()
    return tuple(sp.Matrix(3, 3, list(vector)) for vector in kernel)


def slot_invariant_basis() -> tuple[sp.Matrix, ...]:
    rows: list[list[sp.Expr]] = []
    for rotation in ROTATIONS:
        action = slot_action(rotation)
        for output_slot in range(6):
            row = [action[input_slot, output_slot] for input_slot in range(6)]
            row[output_slot] -= 1
            rows.append(row)
    return tuple(sp.Matrix(vector) for vector in sp.Matrix(rows).nullspace())


def independent_occupancy_intertwiner_dimension() -> int:
    constraints = sp.Matrix.vstack(
        *(sp.Matrix(rotation) - sp.eye(3) for rotation in ROTATIONS)
    )
    # Each of the six occupancy columns must be fixed by every independent
    # internal rotation.
    return 6 * len(constraints.nullspace())


def content_average(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.simplify(sum(vectors, sp.zeros(3, 1)) / 6)


def transform_content(
    spatial: sp.Matrix,
    internal: sp.Matrix,
    vectors: tuple[sp.Matrix, ...],
) -> tuple[sp.Matrix, ...]:
    action = slot_action(spatial)
    transformed: list[sp.Matrix | None] = [None] * 6
    for source in range(6):
        target = next(index for index in range(6) if action[index, source] == 1)
        transformed[target] = internal * vectors[source]
    return tuple(sp.Matrix(vector) for vector in transformed if vector is not None)


def partial_trace_two_qubit(matrix: sp.Matrix, keep: int) -> sp.Matrix:
    if matrix.shape != (4, 4) or keep not in (0, 1):
        raise ValueError("two-qubit partial trace expects a 4x4 matrix and keep=0/1")
    result = sp.zeros(2)
    for row_keep in range(2):
        for column_keep in range(2):
            for traced in range(2):
                if keep == 0:
                    row = 2 * row_keep + traced
                    column = 2 * column_keep + traced
                else:
                    row = 2 * traced + row_keep
                    column = 2 * traced + column_keep
                result[row_keep, column_keep] += matrix[row, column]
    return sp.simplify(result)


def nondemolition_access_certificate() -> dict[str, object]:
    ket0 = sp.Matrix((1, 0))
    ket1 = sp.Matrix((0, 1))
    ket_plus = sp.Matrix((1, 1)) / sp.sqrt(2)
    blank = ket0 * ket0.T
    cnot = sp.Matrix(
        (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
        )
    )

    def copied(input_ket: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
        input_density = input_ket * input_ket.conjugate().T
        output = sp.simplify(
            cnot * sp.kronecker_product(input_density, blank) * cnot.T
        )
        return (
            partial_trace_two_qubit(output, 0),
            partial_trace_two_qubit(output, 1),
        )

    zero_marginals = copied(ket0)
    one_marginals = copied(ket1)
    plus_marginals = copied(ket_plus)
    plus_density = ket_plus * ket_plus.T
    omega = sp.Matrix((1, 0, 0, 1))
    identity_choi = omega * omega.T
    return {
        "identity_choi_rank": identity_choi.rank(),
        "classical_copy": matrix_equal(zero_marginals[0], blank)
        and matrix_equal(zero_marginals[1], blank)
        and matrix_equal(one_marginals[0], ket1 * ket1.T)
        and matrix_equal(one_marginals[1], ket1 * ket1.T),
        "coherence_disturbed": not matrix_equal(plus_marginals[0], plus_density),
        "coherence_not_copied": not matrix_equal(plus_marginals[1], plus_density),
    }


def minimum_determinant(alpha: sp.Expr) -> sp.Expr:
    determinants = []
    for condition in CONDITIONS:
        vector = sp.simplify(alpha * difference(condition))
        determinants.append(sp.simplify(density(vector).det()))
    return min(determinants, key=lambda item: float(sp.N(item)))


def cq_channel_certificate(alpha: sp.Expr) -> dict[str, object]:
    traces = []
    determinants = []
    covariance = []
    for condition in CONDITIONS:
        output = density(sp.simplify(alpha * difference(condition)))
        traces.append(sp.simplify(sp.trace(output)))
        determinants.append(sp.simplify(output.det()))
        for rotation in ROTATIONS:
            rotated_condition = rotate_condition(rotation, condition)
            covariance.append(
                vector_equal(
                    alpha * difference(rotated_condition),
                    rotation * (alpha * difference(condition)),
                )
            )
    return {
        "traces": tuple(traces),
        "determinants": tuple(determinants),
        "covariance": tuple(covariance),
        "strict": all(value > 0 for value in determinants),
    }


def vector_key(vector: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(value) for value in vector)


def spectral_measure(
    direction: tuple[int, int, int], alpha: sp.Expr
) -> dict[tuple[sp.Expr, ...], sp.Expr]:
    vector = sp.Matrix(direction)
    radius = sp.sqrt(vector.dot(vector))
    result: dict[tuple[sp.Expr, ...], sp.Expr] = {}
    for sign in (-1, 1):
        atom = sp.simplify(sign * vector / radius)
        weight = sp.simplify((1 + sign * alpha * radius) / 2)
        result[vector_key(atom)] = weight
    return result


def slot_measure(direction: tuple[int, int, int]) -> dict[tuple[sp.Expr, ...], sp.Expr]:
    result: defaultdict[tuple[sp.Expr, ...], sp.Expr] = defaultdict(
        lambda: sp.Integer(0)
    )
    for axis in range(3):
        atom = sp.zeros(3, 1)
        atom[axis] = direction[axis]
        result[vector_key(atom)] += sp.Rational(1, 3)
    return dict(result)


def measure_mass(measure: dict[tuple[sp.Expr, ...], sp.Expr]) -> sp.Expr:
    return sp.simplify(sum(measure.values(), sp.Integer(0)))


def measure_barycenter(
    measure: dict[tuple[sp.Expr, ...], sp.Expr]
) -> sp.Matrix:
    total = sp.zeros(3, 1)
    for atom, weight in measure.items():
        total += weight * sp.Matrix(atom)
    return sp.simplify(total)


def rotate_measure(
    measure: dict[tuple[sp.Expr, ...], sp.Expr], rotation: sp.Matrix
) -> dict[tuple[sp.Expr, ...], sp.Expr]:
    result: defaultdict[tuple[sp.Expr, ...], sp.Expr] = defaultdict(
        lambda: sp.Integer(0)
    )
    for atom, weight in measure.items():
        result[vector_key(rotation * sp.Matrix(atom))] += weight
    return {atom: sp.simplify(weight) for atom, weight in result.items()}


def measures_equal(
    left: dict[tuple[sp.Expr, ...], sp.Expr],
    right: dict[tuple[sp.Expr, ...], sp.Expr],
) -> bool:
    keys = set(left) | set(right)
    return all(sp.simplify(left.get(key, 0) - right.get(key, 0)) == 0 for key in keys)


def authority_certificate(mutation: str) -> dict[str, object]:
    # Current mutable files are declared inputs. No remote ref or old ancestry test.
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_bytes()
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    return {
        "axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": worktree_blob(REGISTRY_PATH),
        "parent_note": hashlib.sha256((ROOT / PARENT_NOTE).read_bytes()).hexdigest(),
        "parent_runner": hashlib.sha256((ROOT / PARENT_RUNNER).read_bytes()).hexdigest(),
    }


def affine_classifier_certificate(mutation: str) -> dict[str, object]:
    basis = diagonal_intertwiner_basis()
    target = sp.Matrix(
        ((1, -1, 0, 0, 0, 0), (0, 0, 1, -1, 0, 0), (0, 0, 0, 0, 1, -1))
    )
    dimension = len(basis) + int(mutation == "break_affine_classifier")
    return {
        "rotations": len(ROTATIONS),
        "conditions": len(CONDITIONS),
        "directions": len({tuple(difference(item)) for item in CONDITIONS}) - 1,
        "dimension": dimension,
        "target_span": len(basis) == 1
        and sp.Matrix.hstack(
            sp.Matrix(18, 1, list(basis[0])), sp.Matrix(18, 1, list(target))
        ).rank()
        == 1,
        "offset_dimension": len(fixed_vector_basis()),
        "covariance": all(
            vector_equal(
                difference(rotate_condition(rotation, condition)),
                rotation * difference(condition),
            )
            for condition in CONDITIONS
            for rotation in ROTATIONS
        ),
    }


def partial_trace_output(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    """Exact output-only channel oracle on a 64-dimensional product input."""
    if len(vectors) != 6:
        raise ValueError("six input qubits required")
    joint = sp.kronecker_product(*(density(v) for v in vectors))
    output = sp.zeros(2)
    for keep in range(6):
        traced = sp.zeros(2)
        for row in range(2):
            for col in range(2):
                for rest in product((0, 1), repeat=5):
                    left = list(rest); right = list(rest)
                    left.insert(keep, row); right.insert(keep, col)
                    i = sum(bit << (5-n) for n, bit in enumerate(left))
                    j = sum(bit << (5-n) for n, bit in enumerate(right))
                    traced[row, col] += joint[i, j]
        output += traced / 6
    return sp.simplify(output)


def actual_content_certificate(mutation: str) -> dict[str, object]:
    commutant = internal_commutant_basis()
    invariants = slot_invariant_basis()
    independent_dimension = independent_occupancy_intertwiner_dimension()
    if mutation == "allow_unsoldered_direction":
        independent_dimension = 1
    vectors = (
        sp.Matrix((1, 0, 0)),
        sp.Matrix((0, sp.Rational(1, 2), 0)),
        sp.Matrix((0, 0, sp.Rational(1, 3))),
        sp.Matrix((-sp.Rational(1, 4), 0, 0)),
        sp.Matrix((0, -sp.Rational(1, 5), 0)),
        sp.Matrix((0, 0, -sp.Rational(1, 6))),
    )
    covariance = all(
        vector_equal(
            content_average(transform_content(spatial, internal, vectors)),
            internal * content_average(vectors),
        )
        for spatial in ROTATIONS
        for internal in ROTATIONS
    )
    # Two occupied slots carry actual equal M_2 contents with Bloch e3; blanks
    # contribute I/2.  This channel differs from the soldered occupancy map.
    actual_vectors = (
        sp.Matrix((0, 0, 1)),
        sp.zeros(3, 1),
        sp.Matrix((0, 0, 1)),
        sp.zeros(3, 1),
        sp.zeros(3, 1),
        sp.zeros(3, 1),
    )
    content_output = content_average(actual_vectors)
    occupancy_output = sp.Rational(1, 3) * sp.Matrix((1, 1, 0))
    distinct = not vector_equal(content_output, occupancy_output)
    content_density = density(content_output)
    oracle_matches = all(matrix_equal(density(content_average(v)), partial_trace_output(v)) for v in (vectors, actual_vectors))
    exact_two_e3 = vector_equal(content_output, sp.Matrix((0, 0, sp.Rational(1, 3))))
    nondemolition = nondemolition_access_certificate()
    if mutation == "break_content_channel":
        distinct = False
    if mutation == "break_nondemolition_boundary":
        nondemolition["identity_choi_rank"] = 2
    return {
        "independent_occupancy_dimension": independent_dimension,
        "commutant_dimension": len(commutant),
        "commutant_identity": len(commutant) == 1
        and sp.Matrix.hstack(
            sp.Matrix(9, 1, list(commutant[0])), sp.Matrix(9, 1, list(sp.eye(3)))
        ).rank()
        == 1,
        "slot_invariant_dimension": len(invariants),
        "slot_uniform": len(invariants) == 1
        and sp.Matrix.hstack(invariants[0], sp.ones(6, 1)).rank() == 1,
        "covariance": covariance,
        "distinct": distinct,
        "content_positive": sp.trace(content_density) == 1
        and content_density.det() >= 0,
        "content_norm": sp.sqrt(content_output.dot(content_output)),
        "partial_trace_oracles": oracle_matches,
        "two_e3_output": exact_two_e3,
        "identity_choi_rank": nondemolition["identity_choi_rank"],
        "classical_copy": nondemolition["classical_copy"],
        "coherence_disturbed": nondemolition["coherence_disturbed"],
        "coherence_not_copied": nondemolition["coherence_not_copied"],
    }


def cp_response_certificate(mutation: str) -> dict[str, object]:
    linear = cq_channel_certificate(sp.Rational(1, 3))
    alternate = cq_channel_certificate(sp.Rational(1, 4))
    boundary = sp.simplify(minimum_determinant(1 / sp.sqrt(3)))
    outside = sp.simplify(minimum_determinant(sp.Rational(2, 3)))
    distinct = not vector_equal(
        sp.Rational(1, 3) * sp.Matrix((1, 0, 0)),
        sp.Rational(1, 4) * sp.Matrix((1, 0, 0)),
    )
    if mutation == "select_alpha":
        distinct = False
    cp_valid = all(value >= 0 for value in linear["determinants"]) and all(
        value >= 0 for value in alternate["determinants"]
    )
    if mutation == "break_cp_channel":
        cp_valid = False
    cubic_residual = sp.Matrix((2, 2, 0)) / 27 - (
        sp.Matrix((1, 0, 0)) / 27 + sp.Matrix((0, 1, 0)) / 27
    )
    cubic_norms_squared = []
    for direction in DIRECTIONS:
        vector = sp.Matrix(direction)
        k = vector.dot(vector)
        cubic_vector = sp.simplify(k * vector / 27)
        cubic_norms_squared.append(sp.simplify(cubic_vector.dot(cubic_vector)))
    cubic_max_norm_squared = max(
        cubic_norms_squared, key=lambda item: float(sp.N(item))
    )
    return {
        "linear_cp": cp_valid,
        "trace": set(linear["traces"]) == {1}
        and set(alternate["traces"]) == {1},
        "strict": linear["strict"] and alternate["strict"],
        "covariance": all(linear["covariance"]) and all(alternate["covariance"]),
        "boundary": boundary,
        "outside": outside,
        "distinct": distinct,
        "cubic_nonaffine": cubic_residual != sp.zeros(3, 1),
        "cubic_positive": cubic_max_norm_squared < 1,
    }


def ensemble_certificate(mutation: str) -> dict[str, object]:
    alpha = sp.Rational(1, 3)
    masses = []
    barycenters = []
    covariance = []
    for direction in DIRECTIONS:
        spectral = spectral_measure(direction, alpha)
        slots = slot_measure(direction)
        target = alpha * sp.Matrix(direction)
        masses.extend((measure_mass(spectral), measure_mass(slots)))
        barycenters.extend(
            (
                vector_equal(measure_barycenter(spectral), target),
                vector_equal(measure_barycenter(slots), target),
            )
        )
        for rotation in ROTATIONS:
            rotated_direction = tuple(int(value) for value in rotation * sp.Matrix(direction))
            covariance.extend(
                (
                    measures_equal(
                        rotate_measure(spectral, rotation),
                        spectral_measure(rotated_direction, alpha),
                    ),
                    measures_equal(
                        rotate_measure(slots, rotation),
                        slot_measure(rotated_direction),
                    ),
                )
            )
    witness = (1, 1, 0)
    spectral_witness = spectral_measure(witness, alpha)
    slot_witness = slot_measure(witness)
    disjoint = set(spectral_witness).isdisjoint(slot_witness)
    if mutation == "select_spectral_support":
        disjoint = False
    return {
        "masses": set(masses),
        "barycenters": all(barycenters),
        "covariance": all(covariance),
        "disjoint": disjoint,
        "spectral_atoms": len(spectral_witness),
        "slot_atoms": len(slot_witness),
    }


def joint_law_certificate(mutation: str) -> dict[str, object]:
    radius = sp.sqrt(2)
    plus = sp.simplify((1 + radius / 3) / 2)
    minus = sp.simplify(1 - plus)
    product_law = {
        (1, 1): sp.simplify(plus**2),
        (1, -1): sp.simplify(plus * minus),
        (-1, 1): sp.simplify(minus * plus),
        (-1, -1): sp.simplify(minus**2),
    }
    shared_law = {
        (1, 1): plus,
        (1, -1): sp.Integer(0),
        (-1, 1): sp.Integer(0),
        (-1, -1): minus,
    }

    def marginal(law: dict[tuple[int, int], sp.Expr], coordinate: int) -> sp.Expr:
        return sp.simplify(
            sum(
                weight
                for outcomes, weight in law.items()
                if outcomes[coordinate] == 1
            )
        )

    distinct = any(
        sp.simplify(product_law[key] - shared_law[key]) != 0 for key in product_law
    )
    if mutation == "select_product_joint":
        distinct = False
    return {
        "product_mass": sp.simplify(sum(product_law.values())),
        "shared_mass": sp.simplify(sum(shared_law.values())),
        "marginals": tuple(
            marginal(law, coordinate)
            for law in (product_law, shared_law)
            for coordinate in (0, 1)
        ),
        "target": plus,
        "distinct": distinct,
        "swap_symmetric": product_law[(1, -1)] == product_law[(-1, 1)]
        and shared_law[(1, -1)] == shared_law[(-1, 1)],
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    result = {
        "beyond_parent": "does not repeat block 85" in note,
        "not_derived": "no microscopic law is derived or adopted" in note,
        "solder_live": "spatial–pauli soldering remains a supplied choice" in note,
        "support_live": "the barycenter does not select its probability measure" in note,
        "joint_live": "fixed one-site marginals do not select the conditional copula" in note,
        "axiom_unchanged": "no axiom amendment is justified or adopted" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "valid": mutation != "weaken_no_go_packet",
    }
    if mutation == "claim_microscopic_derivation":
        result["not_derived"] = False
    if mutation == "claim_axiom_update":
        result["axiom_unchanged"] = False
    return result


def portfolio_certificate(mutation: str) -> dict[str, bool]:
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    result = {
        "hierarchical_cut": "q_r -> j -> alpha -> mu_d -> c_r" in note,
        "no_double_count": "not five pairwise-independent raw objects" in note,
        "composite_wall": "one composite terminal wall" in note,
        "zero_wall_pairs": "zero wall pairs" in note,
        "placement_open": "record/admissibility interface placement remains an owner decision" in note,
        "formation_external": "formation action or hazard, seed/initial law, and physical rate remain external" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "no audit grade or toe score is assigned by this note" in note,
        "stop": "stop if the next channel merely inserts the block 84 target" in note,
    }
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "break_affine_classifier",
            "allow_unsoldered_direction",
            "break_content_channel",
            "break_nondemolition_boundary",
            "break_cp_channel",
            "select_alpha",
            "select_spectral_support",
            "select_product_joint",
            "weaken_no_go_packet",
            "claim_microscopic_derivation",
            "claim_axiom_update",
            "claim_toe_progress",
            "claim_obligation_retirement",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-authority-and-Block85-parent",
        "current axioms, premise registry, and frozen Block85 parent are content-bound",
        authority["axiom"] == authority["expected_axiom"]
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["parent_note"] == CURRENT_PARENT_NOTE_SHA256
        and authority["parent_runner"] == CURRENT_PARENT_RUNNER_SHA256,
        f"current file binding; historical parent={PARENT_COMMIT[:10]} is provenance only",
    )

    affine = affine_classifier_certificate(mutation)
    checks.check(
        "B-six-slot-diagonal-affine-classification",
        "after a soldering is supplied, the unique covariant affine occupancy response is alpha times the opposite-slot difference",
        affine["rotations"] == 24
        and affine["conditions"] == 64
        and affine["directions"] == 26
        and affine["dimension"] == 1
        and affine["target_span"]
        and affine["offset_dimension"] == 0
        and affine["covariance"],
        f"group/conditions/directions={affine['rotations']}/{affine['conditions']}/{affine['directions']}; intertwiner/offset dim={affine['dimension']}/{affine['offset_dimension']}",
    )

    content = actual_content_certificate(mutation)
    checks.check(
        "C-independent-symmetry-and-actual-M2-content-channel",
        "without a soldering occupancy cannot source a Bloch vector; uniform actual-content averaging is output-only, and a CPTP extension preserving the full M2 state space pointwise has constant complementary output",
        content["independent_occupancy_dimension"] == 0
        and content["commutant_dimension"] == 1
        and content["commutant_identity"]
        and content["slot_invariant_dimension"] == 1
        and content["slot_uniform"]
        and content["covariance"]
        and content["distinct"]
        and content["partial_trace_oracles"]
        and content["two_e3_output"]
        and content["content_norm"] == sp.Rational(1, 3)
        and content["content_positive"]
        and content["identity_choi_rank"] == 1
        and content["classical_copy"]
        and content["coherence_disturbed"]
        and content["coherence_not_copied"],
        f"unsoldered occupancy dim={content['independent_occupancy_dimension']}; content commutant/slot dims={content['commutant_dimension']}/{content['slot_invariant_dimension']}; identity-Choi rank={content['identity_choi_rank']}",
    )

    response = cp_response_certificate(mutation)
    checks.check(
        "D-affine-CQ-CPTP-response-family",
        "complete positivity and covariance leave a continuum of alpha values; the cubic twin is positive but non-affine",
        response["linear_cp"]
        and response["trace"]
        and response["strict"]
        and response["covariance"]
        and response["boundary"] == 0
        and response["outside"] < 0
        and response["distinct"]
        and response["cubic_nonaffine"]
        and response["cubic_positive"],
        f"alpha=1/3 and 1/4 both strict CPTP; det boundary/outside={response['boundary']}/{response['outside']}",
    )

    ensemble = ensemble_certificate(mutation)
    checks.check(
        "E-fixed-barycenter-ensemble-nonuniqueness",
        "the Block85 barycenter has both spectral and axis-slot covariant probability measures with disjoint support on d=(1,1,0)",
        ensemble["masses"] == {1}
        and ensemble["barycenters"]
        and ensemble["covariance"]
        and ensemble["disjoint"]
        and ensemble["spectral_atoms"] == 2
        and ensemble["slot_atoms"] == 3,
        f"witness support sizes={ensemble['spectral_atoms']}/{ensemble['slot_atoms']}; total-variation=1",
    )

    joint = joint_law_certificate(mutation)
    checks.check(
        "F-fixed-marginals-do-not-select-conditional-copula",
        "product and shared-latent two-site copulas are normalized, swap-covariant, and have identical fixed local marginals but different histories",
        joint["product_mass"] == 1
        and joint["shared_mass"] == 1
        and set(joint["marginals"]) == {joint["target"]}
        and joint["distinct"]
        and joint["swap_symmetric"],
        f"shared one-site p+={joint['target']}; product/shared mixed atoms differ",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "G-no-go-and-constitutional-scope",
        "N1-N8 pass only for the declared channel nonselection boundary; microscopic derivations and owner decisions remain live",
        all(scope.values()),
    )

    portfolio = portfolio_certificate(mutation)
    checks.check(
        "H-decision-cut-and-TOE-firewall",
        "the exact hierarchical one-step interface/response cut is localized conditional on formation, without adoption, obligation retirement, retained theory, or TOE score movement",
        all(portfolio.values()),
    )

    print(
        f"AXIOM_AUTHORITY: current file axiom={CURRENT_AXIOM_BLOB}; corrected parent={CURRENT_PARENT_NOTE_SHA256}; historical Block85={PARENT_COMMIT}"
    )
    print(
        "per_element: checked 64 occupancy inputs, 26 nonzero differences, two affine CPTP response values, two exact ensembles, and two joint laws"
    )
    print(
        "per_site: checked all six nearest-neighbour slots, actual M2 output channels, and the nondemolition Choi/CNOT boundary; no formation rule or physical site rate is adopted"
    )
    print(
        "per_mode: checked diagonal-soldered, independent-internal, content-sensitive, spectral, axis-slot, product, and shared-latent conditional-copula modes"
    )
    print(
        "per_block: checked exact intertwiner, positivity, covariance, barycenter, support, and correlation boundaries beyond Block85"
    )
    print(
        "lattice_wide: checked and not executed — arbitrary finite-map iteration, scheduler genesis, physical time, source/gravity composition, adoption, and retention remain open"
    )
    print(
        "RESULT: a supplied soldering plus affine covariance derives the d carrier but CP leaves alpha free; full-domain pointwise nondemolition access is constant unless a classical/commuting interface is supplied; conditional ensemble-lift and copula alternatives survive"
    )
    print(
        "DECISION_CUT: conditional on formation, the one-step hierarchy is Q_R -> J -> alpha -> mu_d -> C_R plus eligibility and cadence; formation hazard, initial law, and physical rate remain external; Q_R placement remains an owner decision"
    )
    print(
        "TOE: this source claims zero obligation retirement and no percentage movement; no current audit count or grade assigned"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
