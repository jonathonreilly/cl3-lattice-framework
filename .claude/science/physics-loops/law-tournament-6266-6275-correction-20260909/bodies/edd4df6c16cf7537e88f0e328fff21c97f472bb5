#!/usr/bin/env python3
"""Test the current-axiom bridge from M2 Record content to sector grading.

The runner constructs both the proper-cubic adjoint action on the Pauli
subspace and a trivial internal action.  It proves that both can accompany one
exact current-axiom-compatible central admissibility rule, while only the
adjoint action admits a nonzero equivariant linear direction decoder.  It then
embeds the complete Cycle-876 balance model into four typed Pauli-pointer
Records and separates that conditional carrier result from physical selection.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_M2_RECORD_CUBIC_VECTOR_DECODER_SECTOR_GRADING_CARRIER_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
WORLDLINE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_RECORD_WORLDLINE_CONSERVED_STRESS_TWO_TT_LORENTZIAN_"
    "CFL_LOCALITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
CYCLE876_PATH = ROOT / "docs" / (
    "GRADING_AFFINE_CHART_ALGEBRA_CYCLE876_SUPPORT_NOTE_2026-08-09.md"
)
BLOCK55_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SECTOR_GRADING_FULL_PROJECTIVE_STRATIFICATION_POSITIVE_"
    "SELECTOR_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)

AUDIT_TIMEOUT_SEC = 120


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, key, statement, condition, detail=""):
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_group():
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if parity(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = tuple(
                tuple(signs[row] if column == perm[row] else 0 for column in range(3))
                for row in range(3)
            )
            rotations.append(matrix)
    return tuple(sorted(rotations))


ROTATIONS = proper_cubic_group()
DIRECTIONS = tuple(
    tuple(sign if coordinate == axis else 0 for coordinate in range(3))
    for axis in range(3)
    for sign in (1, -1)
)


def mat_vec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def mat_mul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def det3(matrix):
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


# A Gaussian integer is represented as (real, imaginary).
ZERO_GI = (0, 0)
ONE_GI = (1, 0)
I_GI = (0, 1)


def gi_add(left, right):
    return left[0] + right[0], left[1] + right[1]


def gi_mul(left, right):
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gi_scale(value, integer):
    return value[0] * integer, value[1] * integer


def basis(index):
    coefficients = [ZERO_GI] * 4
    coefficients[index] = ONE_GI
    return tuple(coefficients)


def element_add(left, right):
    return tuple(gi_add(a, b) for a, b in zip(left, right))


def element_scale(integer, element):
    return tuple(gi_scale(value, integer) for value in element)


def basis_product(left, right):
    if left == 0:
        return basis(right)
    if right == 0:
        return basis(left)
    if left == right:
        return basis(0)
    unit_left = tuple(int(i == left - 1) for i in range(3))
    unit_right = tuple(int(i == right - 1) for i in range(3))
    vector = cross(unit_left, unit_right)
    output = [ZERO_GI] * 4
    for index, coefficient in enumerate(vector, start=1):
        if coefficient:
            output[index] = gi_scale(I_GI, coefficient)
    return tuple(output)


def element_mul(left, right):
    output = tuple(ZERO_GI for _ in range(4))
    for i, coefficient_left in enumerate(left):
        for j, coefficient_right in enumerate(right):
            coefficient = gi_mul(coefficient_left, coefficient_right)
            if coefficient == ZERO_GI:
                continue
            term = tuple(gi_mul(coefficient, value) for value in basis_product(i, j))
            output = element_add(output, term)
    return output


def adjoint_action(rotation, element):
    output = [element[0], ZERO_GI, ZERO_GI, ZERO_GI]
    for old_axis in range(3):
        for new_axis in range(3):
            output[new_axis + 1] = gi_add(
                output[new_axis + 1],
                gi_scale(element[old_axis + 1], rotation[new_axis][old_axis]),
            )
    return tuple(output)


def rational_rank(rows):
    matrix = [[Fraction(value) for value in row] for row in rows if any(row)]
    if not matrix:
        return 0
    rank = 0
    columns = len(matrix[0])
    for column in range(columns):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [a - factor * b for a, b in zip(matrix[row], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def equivariance_rows(domain_action):
    rows = []
    for rotation in ROTATIONS:
        for output in range(3):
            for source in range(3):
                row = [0] * 9
                # T * domain_action - rotation * T = 0.
                for middle in range(3):
                    row[3 * output + middle] += domain_action(rotation)[middle][source]
                    row[3 * middle + source] -= rotation[output][middle]
                rows.append(row)
    return rows


def identity_action(_rotation):
    return ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def support_matrix(incoming, triple):
    columns = (
        tuple(DIRECTIONS[triple[0]][axis] - DIRECTIONS[incoming][axis] for axis in range(3)),
        DIRECTIONS[triple[1]],
        DIRECTIONS[triple[2]],
    )
    return tuple(tuple(columns[column][row] for column in range(3)) for row in range(3))


def matrix_rank(matrix):
    if det3(matrix):
        return 3
    for rows in ((0, 1), (0, 2), (1, 2)):
        for columns in ((0, 1), (0, 2), (1, 2)):
            minor = (
                matrix[rows[0]][columns[0]] * matrix[rows[1]][columns[1]]
                - matrix[rows[0]][columns[1]] * matrix[rows[1]][columns[0]]
            )
            if minor:
                return 2
    return 1 if any(value for row in matrix for value in row) else 0


def apply_matrix(matrix, weights):
    return tuple(sum(matrix[row][column] * weights[column] for column in range(3)) for row in range(3))


SPECIAL_POINTS = (
    (0, 1, -1), (0, 1, 1), (1, -2, 0), (1, -1, -1), (1, -1, 1),
    (1, 0, -2), (1, 0, 0), (1, 0, 2), (1, 1, -1), (1, 1, 1), (1, 2, 0),
)

ROLE_TAGS = {
    "incoming": -1,
    "matter": 0,
    "field": 1,
    "auxiliary": 2,
}


def tagged_pointer(role, direction_index):
    """Exact Pauli-basis coefficients of tag*I + D[direction].sigma."""
    vector = DIRECTIONS[direction_index]
    return (
        (ROLE_TAGS[role], 0),
        (vector[0], 0),
        (vector[1], 0),
        (vector[2], 0),
    )


def decode_tagged_pointer(content):
    role_by_tag = {tag: role for role, tag in ROLE_TAGS.items()}
    tag = content[0][0]
    vector = tuple(value[0] for value in content[1:])
    return role_by_tag[tag], DIRECTIONS.index(vector)


def classification_and_embedding():
    rank_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    point_counts = {point: 0 for point in SPECIAL_POINTS}
    embedding_mismatches = 0
    supports = 0
    for incoming in range(6):
        for triple in product(range(6), repeat=3):
            records = (
                tagged_pointer("incoming", incoming),
                tagged_pointer("matter", triple[0]),
                tagged_pointer("field", triple[1]),
                tagged_pointer("auxiliary", triple[2]),
            )
            decoded = tuple(decode_tagged_pointer(record) for record in records)
            embedding_mismatches += int(
                decoded
                != (
                    ("incoming", incoming),
                    ("matter", triple[0]),
                    ("field", triple[1]),
                    ("auxiliary", triple[2]),
                )
            )
            matrix = support_matrix(incoming, triple)
            rank_counts[matrix_rank(matrix)] += 1
            supports += 1
            for weights in SPECIAL_POINTS:
                vector_residual = apply_matrix(matrix, weights)
                pauli_residual = tuple(
                    weights[0] * (DIRECTIONS[triple[0]][axis] - DIRECTIONS[incoming][axis])
                    + weights[1] * DIRECTIONS[triple[1]][axis]
                    + weights[2] * DIRECTIONS[triple[2]][axis]
                    for axis in range(3)
                )
                embedding_mismatches += int(vector_residual != pauli_residual)
                point_counts[weights] += int(pauli_residual == (0, 0, 0))
    return supports, rank_counts, point_counts, embedding_mismatches


def main():
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    worldline = WORLDLINE_PATH.read_text(encoding="utf-8")
    cycle876 = CYCLE876_PATH.read_text(encoding="utf-8")
    block55 = BLOCK55_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print("analytic_boundary: exact proper-cubic representation and Pauli-pointer carrier algebra")
    print("physical_boundary: no internal rotation lift, non-scalar decoder, sector roles, grading selector, chirality carrier, or gravity sign is selected")
    print("external_scientific_inputs: none; all group, algebra, rule, and finite-support calculations are reconstructed exactly")

    checks.check(
        "source-interface-boundary",
        "the current sources supply M2 content and scalar readout but keep the vector decoder conditional",
        "M_2(C)" in axiom
        and "proper cubic rotations" in axiom_flat
        and "No possibility is privileged" in axiom_flat
        and "scalar readout `I` is additive" in axiom_flat
        and "incoming-pointer Record" in worldline
        and "not the Record axiom's additive scalar readout" in worldline
        and "supplied sector-indexed vector-readout ansatz" in cycle876.lower()
        and "strict positivity plus lawful-support maximization" in block55,
    )

    rotation_set = set(ROTATIONS)
    orbit = {mat_vec(rotation, DIRECTIONS[0]) for rotation in ROTATIONS}
    closure = all(mat_mul(left, right) in rotation_set for left in ROTATIONS for right in ROTATIONS)
    checks.check(
        "proper-cubic-group-and-orbit",
        "the 24 determinant-one signed permutations form a group transitive on six signed directions",
        len(ROTATIONS) == 24
        and all(det3(rotation) == 1 for rotation in ROTATIONS)
        and closure
        and orbit == set(DIRECTIONS),
        f"group={len(ROTATIONS)}; orbit={len(orbit)}; closure={closure}",
    )

    algebra_failures = 0
    representation_failures = 0
    for rotation in ROTATIONS:
        for left in range(4):
            for right in range(4):
                algebra_failures += int(
                    adjoint_action(rotation, basis_product(left, right))
                    != element_mul(adjoint_action(rotation, basis(left)), adjoint_action(rotation, basis(right)))
                )
    for left in ROTATIONS:
        for right in ROTATIONS:
            composite = mat_mul(left, right)
            for index in range(4):
                representation_failures += int(
                    adjoint_action(left, adjoint_action(right, basis(index)))
                    != adjoint_action(composite, basis(index))
                )
    checks.check(
        "two-current-compatible-internal-actions",
        "both trivial and Pauli-adjoint proper-cubic actions are exact M2 algebra representations",
        algebra_failures == 0 and representation_failures == 0,
        f"adjoint algebra failures={algebra_failures}; representation failures={representation_failures}; trivial action is identity",
    )

    probabilities = {Fraction(1 + sum(bits), 8) for bits in product((0, 1), repeat=6)}
    rule_failures = 0
    for bits in product((0, 1), repeat=6):
        q = Fraction(1 + sum(bits), 8)
        rule_failures += int(not (0 < q < 1 and q + (1 - q) == 1))
        for rotation in ROTATIONS:
            permuted = tuple(bits[DIRECTIONS.index(mat_vec(rotation, direction))] for direction in DIRECTIONS)
            rule_failures += int(Fraction(1 + sum(permuted), 8) != q)
    checks.check(
        "shared-current-axiom-completion",
        "one exact total central rule varies with six-neighbour conditions and is covariant under both internal actions",
        probabilities == {Fraction(i, 8) for i in range(1, 8)} and rule_failures == 0,
        f"probabilities={sorted(probabilities)}; failures={rule_failures}; support={{-I,+I}} fixed by both actions",
    )

    adjoint_rank = rational_rank(equivariance_rows(lambda rotation: rotation))
    trivial_rank = rational_rank(equivariance_rows(identity_action))
    identity_vector = tuple(int(index // 3 == index % 3) for index in range(9))
    identity_satisfies = all(
        sum(row[index] * identity_vector[index] for index in range(9)) == 0
        for row in equivariance_rows(lambda rotation: rotation)
    )
    checks.check(
        "equivariant-decoder-space-fork",
        "the adjoint action has one normalized vector decoder while the trivial action has none",
        adjoint_rank == 8 and trivial_rank == 9 and identity_satisfies,
        f"adjoint rank/nullity={adjoint_rank}/{9-adjoint_rank}; trivial rank/nullity={trivial_rank}/{9-trivial_rank}",
    )

    supports, rank_counts, point_counts, embedding_mismatches = classification_and_embedding()
    checks.check(
        "typed-pauli-record-balance-embedding",
        "four central-tagged Pauli-pointer Records reproduce the complete Cycle-876 balance model exactly",
        supports == 1296
        and rank_counts == {0: 0, 1: 96, 2: 768, 3: 432}
        and embedding_mismatches == 0
        and point_counts[(1, 1, 1)] == 90
        and tuple(point_counts[point] for point in ((0, 1, -1), (0, 1, 1), (1, 0, 0))) == (216, 216, 216)
        and len({tagged_pointer(role, direction) for role in ROLE_TAGS for direction in range(6)}) == 24,
        f"alphabet=24; ranks={rank_counts}; unit={point_counts[(1,1,1)]}; three controls={(point_counts[(0,1,-1)],point_counts[(0,1,1)],point_counts[(1,0,0)])}",
    )

    invariant_covector_rows = []
    for rotation in ROTATIONS:
        for column in range(3):
            invariant_covector_rows.append(tuple(rotation[row][column] - int(row == column) for row in range(3)))
    invariant_covector_rank = rational_rank(invariant_covector_rows)
    pointer_trace_values = {
        tagged_pointer("matter", direction)[0][0] for direction in range(6)
    }
    checks.check(
        "scalar-readout-orbit-blindness",
        "every proper-cubic-invariant scalar is constant on the transitive pointer orbit and every invariant linear scalar vanishes there",
        orbit == set(DIRECTIONS)
        and invariant_covector_rank == 3
        and pointer_trace_values == {0}
        and "a covariant scalar readout cannot recover a signed direction" in note_flat,
        f"orbit size={len(orbit)}; invariant-covector rank={invariant_covector_rank}; trace/2 values={pointer_trace_values}",
    )

    checks.check(
        "axiom-choice-not-physical-identification",
        "the note preserves live joint-law and axiom routes without claiming TOE movement",
        "Promotion Value Gate" in note
        and "No-Go Discipline Gate" in note
        and "Pauli-adjoint action" in note_flat
        and "Bloch-vector decoder" in note_flat
        and "direct unit-grading datum" in note_flat
        and "no toe percentage movement is claimed" in note_flat.lower(),
    )

    print("per_element: checked every Pauli basis product, action image, balance entry, and special-point residual")
    print("per_site: checked the full one-site M2 Pauli pointer orbit and one total six-neighbour local-rule completion")
    print("per_mode: checked all 24 proper-cubic transformations and both exact internal representation choices; no Fourier claim is made")
    print("per_block: checked all 1,296 typed four-Record support configurations and the complete decoder constraint systems")
    print("lattice_wide: checked and not executed — no selected full-Z3 law, sector compiler, chirality lineage, or gravity-sign theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
