#!/usr/bin/env python3
"""Exact checks for a homogeneous-payload NN Record writer/readout Law."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, integrate, oo, pi, simplify, sqrt, symbols


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_HOMOGENEOUS_PAYLOAD_SELF_HOSTING_WRITER_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_HOMOGENEOUS_PAYLOAD_SELF_HOSTING_WRITER_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md"
)

I2 = Matrix.eye(2)
ZERO2 = Matrix.zeros(2)
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])

DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)

APPEND_ORDER = (
    (1, 1, 0),
    (1, 0, 0),
    (0, 1, 0),
    (-1, 1, 0),
    (-1, 0, 0),
    (1, 0, 1),
    (0, 0, 1),
    (1, 0, -1),
    (0, 0, -1),
    (1, -1, 0),
    (0, -1, 0),
)


@dataclass(frozen=True)
class PayloadData:
    preparation: Matrix
    projector: Matrix
    complement: Matrix


@dataclass(frozen=True)
class GaussianLaw:
    name: str = "unit-frobenius-gaussian"


def matrix_equal(left: Matrix, right: Matrix) -> bool:
    return left.shape == right.shape and all(
        simplify(left[row, column] - right[row, column]) == 0
        for row in range(left.rows)
        for column in range(left.cols)
    )


def hermitian_part(value: Matrix) -> Matrix:
    return simplify((value + value.conjugate().T) / 2)


def antihermitian_coefficient(value: Matrix) -> Matrix:
    return simplify((value - value.conjugate().T) / (2 * I))


def positive_truth(value) -> bool:
    return bool(simplify(value).is_positive)


def nonnegative_truth(value) -> bool:
    return bool(simplify(value).is_nonnegative)


def is_density(value: Matrix) -> bool:
    return (
        matrix_equal(value, value.conjugate().T)
        and simplify(value.trace()) == 1
        and nonnegative_truth(value[0, 0])
        and nonnegative_truth(value[1, 1])
        and nonnegative_truth(value.det())
    )


def is_rank_one_projector(value: Matrix) -> bool:
    return (
        matrix_equal(value, value.conjugate().T)
        and matrix_equal(simplify(value * value), value)
        and simplify(value.trace()) == 1
    )


def decode_payload(value: Matrix) -> PayloadData | None:
    h_value = hermitian_part(value)
    k_value = antihermitian_coefficient(value)
    k_zero = simplify(k_value - k_value.trace() * I2 / 2)
    density_denominator = simplify((h_value * h_value).trace())
    radius_squared = simplify((k_zero * k_zero).trace() / 2)
    if not positive_truth(density_denominator) or not positive_truth(radius_squared):
        return None
    radius = sqrt(radius_squared)
    preparation = simplify(h_value * h_value / density_denominator)
    projector = simplify((I2 + k_zero / radius) / 2)
    complement = simplify(I2 - projector)
    if not (
        is_density(preparation)
        and is_rank_one_projector(projector)
        and is_rank_one_projector(complement)
    ):
        return None
    return PayloadData(preparation, projector, complement)


def homogeneous(neighbors: tuple[Matrix, ...]) -> bool:
    return bool(neighbors) and all(matrix_equal(value, neighbors[0]) for value in neighbors)


def distinct_generic_payloads(neighbors: tuple[Matrix, ...]) -> tuple[Matrix, ...]:
    payloads = []
    for value in neighbors:
        if decode_payload(value) is None:
            continue
        if not any(matrix_equal(value, prior) for prior in payloads):
            payloads.append(value)
    return tuple(payloads)


def trace_weight(preparation: Matrix, projector: Matrix):
    return simplify((preparation * projector).trace())


def local_law(neighbors: tuple[Matrix, ...]):
    """One total kernel on the recorded portion of a six-neighbor shell."""
    if not neighbors:
        return GaussianLaw()
    if len(neighbors) == 6 and homogeneous(neighbors):
        payload = decode_payload(neighbors[0])
        if payload is not None:
            return (
                (payload.projector, trace_weight(payload.preparation, payload.projector)),
                (payload.complement, trace_weight(payload.preparation, payload.complement)),
            )
    payloads = distinct_generic_payloads(neighbors)
    if payloads:
        mass = Q(1, len(payloads))
        return tuple((payload, mass) for payload in payloads)
    return GaussianLaw()


def finite_law_equal(left, right) -> bool:
    if isinstance(left, GaussianLaw) or isinstance(right, GaussianLaw):
        return isinstance(left, GaussianLaw) and isinstance(right, GaussianLaw)
    if len(left) != len(right):
        return False
    unmatched = list(right)
    for left_content, left_mass in left:
        for index, (right_content, right_mass) in enumerate(unmatched):
            if matrix_equal(left_content, right_content) and simplify(left_mass - right_mass) == 0:
                unmatched.pop(index)
                break
        else:
            return False
    return not unmatched


def content_mass(law, content: Matrix):
    if isinstance(law, GaussianLaw):
        return None
    return simplify(
        sum(
            (mass for candidate, mass in law if matrix_equal(candidate, content)),
            Q(0),
        )
    )


def add(left: tuple[int, int, int], right: tuple[int, int, int]):
    return tuple(left[index] + right[index] for index in range(3))


def recorded_neighbor_contents(records, site):
    return tuple(records[add(site, direction)] for direction in DIRECTIONS if add(site, direction) in records)


def append_record(records, site, content: Matrix) -> bool:
    if site in records:
        return False
    records[site] = content
    return True


def permutation_sign(perm: tuple[int, int, int]) -> int:
    inversions = sum(
        1 for left in range(3) for right in range(left + 1, 3) if perm[left] > perm[right]
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[Matrix, ...]:
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            rotation = Matrix.zeros(3)
            for row, column in enumerate(perm):
                rotation[row, column] = signs[row]
            rotations.append(rotation)
    return tuple(rotations)


def rotate_site(rotation: Matrix, site: tuple[int, int, int]):
    result = rotation * Matrix(site)
    return tuple(int(result[index]) for index in range(3))


def conjugate_law(law, unitary: Matrix):
    if isinstance(law, GaussianLaw):
        return law
    return tuple(
        (simplify(unitary * content * unitary.conjugate().T), mass)
        for content, mass in law
    )


def gaussian_density_at(value: Matrix):
    norm_squared = simplify((value.conjugate().T * value).trace())
    return exp(-norm_squared) / pi**4


def independent_equality_constraint_rank() -> int:
    """Rank of A_2=A_1,...,A_6=A_1 in 6 copies of R^8."""
    constraint = Matrix.zeros(5 * 8, 6 * 8)
    for block in range(5):
        for coordinate in range(8):
            constraint[block * 8 + coordinate, coordinate] = -1
            constraint[block * 8 + coordinate, (block + 1) * 8 + coordinate] = 1
    return constraint.rank()


def main() -> int:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    x = symbols("x", real=True)
    gaussian_line = integrate(exp(-(x**2)) / sqrt(pi), (x, -oo, oo))
    check(
        "gaussian-normalization",
        gaussian_line == 1 and gaussian_line**8 == 1,
        "the eight-real-dimensional unit Frobenius Gaussian normalizes exactly",
    )

    h_real = Matrix([[1, 1], [1, 2]])
    seed_real = simplify(h_real + I * SX)
    decoded_real = decode_payload(seed_real)
    expected_real = simplify(h_real * h_real / (h_real * h_real).trace())
    expected_px = simplify((I2 + SX) / 2)
    check(
        "generic-payload-decoder",
        decoded_real is not None
        and matrix_equal(decoded_real.preparation, expected_real)
        and matrix_equal(decoded_real.projector, expected_px),
        "one generic M2 Record uniquely decodes a density and binary projector frame",
    )
    coordinates = symbols("g0:8", real=True)
    arbitrary_matrix = Matrix(
        [
            [coordinates[0] + I * coordinates[1], coordinates[2] + I * coordinates[3]],
            [coordinates[4] + I * coordinates[5], coordinates[6] + I * coordinates[7]],
        ]
    )
    check(
        "gaussian-full-support",
        positive_truth(gaussian_density_at(arbitrary_matrix))
        and positive_truth(gaussian_density_at(seed_real)),
        "the Gaussian density is symbolically positive at every finite M2 point; each exact singleton still has mass zero",
    )

    canonical_seed = simplify(h_real / sqrt((h_real * h_real).trace()) + I * expected_px)
    canonical_decoded = decode_payload(canonical_seed)
    check(
        "canonical-representative",
        canonical_decoded is not None
        and matrix_equal(canonical_decoded.preparation, expected_real)
        and matrix_equal(canonical_decoded.projector, expected_px),
        "sqrt(C)+iP reaches the intended quotient fiber on this exact mixed fixture; the note gives the general proof",
    )

    h_complex = Matrix([[2, I], [-I, 1]])
    seed_complex = simplify(h_complex + I * SY)
    decoded_complex = decode_payload(seed_complex)
    complex_weight = (
        trace_weight(decoded_complex.preparation, decoded_complex.projector)
        if decoded_complex is not None
        else None
    )
    check(
        "complex-payload",
        decoded_complex is not None
        and matrix_equal(decoded_complex.projector, simplify((I2 + SY) / 2))
        and complex_weight == Q(1, 14),
        "a genuinely complex Y payload decodes and gives exact nontrivial mass 1/14",
    )

    pz = simplify((I2 + SZ) / 2)
    seed_endpoint = simplify(pz + I * SZ)
    endpoint_data = decode_payload(seed_endpoint)
    endpoint_law = local_law((seed_endpoint,) * 6)
    check(
        "pure-endpoint",
        endpoint_data is not None
        and matrix_equal(endpoint_data.preparation, pz)
        and content_mass(endpoint_law, pz) == 1
        and content_mass(endpoint_law, I2 - pz) == 0,
        "a pure aligned payload has literal one/zero Record masses without fabricating the zero branch",
    )

    copy_law = local_law((seed_real,))
    read_law = local_law((seed_real,) * 6)
    conflicting_law = local_law((seed_real, seed_complex))
    malformed_law = local_law((I * I2, I * I2))
    check(
        "total-kernel-branches",
        isinstance(local_law(tuple()), GaussianLaw)
        and content_mass(copy_law, seed_real) == 1
        and not isinstance(read_law, GaussianLaw)
        and content_mass(conflicting_law, seed_real) == Q(1, 2)
        and content_mass(conflicting_law, seed_complex) == Q(1, 2)
        and isinstance(malformed_law, GaussianLaw),
        "empty, copy, conflicting-payload, complete-read, and malformed conditions all receive one answer",
    )

    read_mass_p = content_mass(read_law, decoded_real.projector)
    read_mass_q = content_mass(read_law, decoded_real.complement)
    check(
        "trace-readout",
        read_mass_p == Q(13, 14) and read_mass_q == Q(1, 14) and read_mass_p + read_mass_q == 1,
        "six identical payload Records produce normalized literal projectors with masses 13/14 and 1/14",
    )

    sigma_prefix = Matrix([[2, 1], [1, 2]])
    prefix_center = simplify(sigma_prefix / sigma_prefix.trace())
    prefix_projector = expected_px
    # Use an exact positive H whose square normalizes to sigma_prefix.
    prefix_h = Matrix([[1 + sqrt(3), sqrt(3) - 1], [sqrt(3) - 1, 1 + sqrt(3)]])
    prefix_seed = simplify(prefix_h + I * prefix_projector)
    prefix_data = decode_payload(prefix_seed)
    parent_mass = simplify(
        (prefix_projector * sigma_prefix * prefix_projector).trace() / sigma_prefix.trace()
    )
    check(
        "parent-prefix-composition",
        prefix_data is not None
        and matrix_equal(prefix_data.preparation, prefix_center)
        and trace_weight(prefix_data.preparation, prefix_projector) == parent_mass == Q(3, 4),
        "the payload trace mass equals the selected parent trace-Lueders one-site prefix mass",
    )

    second_seed = simplify(h_real + I * SZ)
    second_data = decode_payload(second_seed)
    check(
        "preparation-quotient",
        second_data is not None
        and matrix_equal(second_data.preparation, decoded_real.preparation)
        and not matrix_equal(second_data.projector, decoded_real.projector),
        "changing only the anti-Hermitian seed data changes the program while keeping preparation fixed",
    )

    records = {}
    formation_ok = True
    predecessor_counts = []
    for index, site in enumerate(APPEND_ORDER):
        condition = recorded_neighbor_contents(records, site)
        predecessor_counts.append(len(condition))
        if index == 0:
            formation_ok = formation_ok and isinstance(local_law(condition), GaussianLaw)
            formation_ok = formation_ok and positive_truth(gaussian_density_at(seed_real))
        else:
            formation_ok = formation_ok and content_mass(local_law(condition), seed_real) == 1
        formation_ok = formation_ok and append_record(records, site, seed_real)
    check(
        "append-scaffold",
        formation_ok and predecessor_counts == [0] + [1] * 10,
        "one Gaussian seed plus ten deterministic fresh-site copies builds the exact 11-Record scaffold",
    )

    target = (0, 0, 0)
    target_condition = recorded_neighbor_contents(records, target)
    check(
        "fresh-target-shell",
        target not in records
        and len(target_condition) == 6
        and homogeneous(target_condition)
        and finite_law_equal(local_law(target_condition), read_law),
        "the origin stays fresh until all six nearest neighbors carry the common payload",
    )

    before = dict(records)
    chosen_output = decoded_real.projector
    permanent_append = append_record(records, target, chosen_output)
    rewrite_rejected = not append_record(records, target, decoded_real.complement)
    check(
        "record-permanence",
        permanent_append
        and rewrite_rejected
        and all(matrix_equal(records[site], content) for site, content in before.items())
        and matrix_equal(records[target], chosen_output),
        "the history only appends one target Record and never changes any prior content",
    )

    check(
        "same-law-output-closure",
        positive_truth(gaussian_density_at(seed_real))
        and content_mass(copy_law, seed_real) == 1
        and predecessor_counts == [0] + [1] * 10
        and matrix_equal(target_condition[0], seed_real)
        and all(matrix_equal(value, seed_real) for value in target_condition),
        "the root is in full Gaussian support and all ten later carrier copies are mass-one outputs of the same kernel",
    )

    rotations = proper_cubic_rotations()
    rotation_ok = len(rotations) == 24
    for rotation in rotations:
        rotated_order = tuple(rotate_site(rotation, site) for site in APPEND_ORDER)
        rotated_records = {}
        counts = []
        for site in rotated_order:
            condition = recorded_neighbor_contents(rotated_records, site)
            counts.append(len(condition))
            rotated_records[site] = seed_real
        rotated_target = recorded_neighbor_contents(rotated_records, target)
        rotation_ok = rotation_ok and counts == [0] + [1] * 10
        rotation_ok = rotation_ok and finite_law_equal(local_law(rotated_target), read_law)
    check(
        "proper-cubic-history",
        rotation_ok,
        "all 24 proper cubic rotations preserve the seed/copy order and final trace branch",
    )

    shift = (7, -5, 3)
    translated_records = {add(site, shift): content for site, content in before.items()}
    translated_target = add(target, shift)
    check(
        "translation-covariance",
        finite_law_equal(local_law(recorded_neighbor_contents(translated_records, translated_target)), read_law),
        "translating the complete scaffold leaves the local answer unchanged",
    )

    hadamard = Matrix([[1, 1], [1, -1]]) / sqrt(2)
    conjugated_seed = simplify(hadamard * seed_real * hadamard.conjugate().T)
    conjugated_law = local_law((conjugated_seed,) * 6)
    check(
        "internal-basis-covariance",
        finite_law_equal(conjugated_law, conjugate_law(read_law, hadamard)),
        "simultaneous unitary re-presentation transports contents and preserves trace masses",
    )

    check(
        "atomless-independent-deletion",
        independent_equality_constraint_rank() == 40,
        "six independent atomless M2 draws meet the exact homogeneous carrier only on a codimension-40 null set",
    )

    premature_records = {
        APPEND_ORDER[0]: seed_real,
        APPEND_ORDER[1]: seed_real,
    }
    premature_law = local_law(recorded_neighbor_contents(premature_records, target))
    premature_copy = content_mass(premature_law, seed_real) == 1
    premature_write = append_record(premature_records, target, seed_real)
    later_rejected = not append_record(premature_records, target, chosen_output)
    check(
        "formation-order-deletion",
        premature_copy and premature_write and later_rejected,
        "forming the target after one neighbor locks a payload permanently, so the fresh-buffer order is load-bearing",
    )

    degenerate_seed = I * I2
    check(
        "degenerate-totality",
        decode_payload(degenerate_seed) is None
        and isinstance(local_law((degenerate_seed,) * 6), GaussianLaw),
        "zero-H or scalar-K payloads are rejected into the declared fallback rather than left undefined",
    )

    note_text = NOTE.read_text() if NOTE.exists() else ""
    check(
        "source-contract",
        all(
            token in note_text
            for token in (
                "No-Go Discipline Gate",
                "Formation-site boundary",
                "zero singleton mass",
                "alternative binary-projective carrier",
                "no TOE-percentage movement",
                "PR #7317",
            )
        ),
        "the source binds support language, the formation wall, carrier replacement, pincer, and score boundary",
    )

    print(
        "per_element: exact payload quotient, Gaussian support density, copy atom, projector contents, and trace masses are checked"
    )
    print(
        "per_site: empty, partial homogeneous, complete homogeneous, malformed, premature, and permanent site branches are executed"
    )
    print(
        "per_mode: no momentum, spectral, continuum, gravity, or PR determinant-matrix fixture is executed; the ancillary finite inverse-determinant identity is separate"
    )
    print(
        "per_block: the 11-Record scaffold and all 24 proper-cubic copies are checked, with the target fresh until completion"
    )
    print(
        "lattice_wide: checked and not executed — one finite append order is witnessed; no autonomous global formation process is claimed"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
