#!/usr/bin/env python3
"""Independent exact reconstruction of the homogeneous-payload writer claim."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

from sympy import I, Matrix, Rational as Q, simplify, sqrt


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
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])

NEIGHBORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)

ORDER = (
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


def equal(left: Matrix, right: Matrix) -> bool:
    return all(
        simplify(left[row, column] - right[row, column]) == 0
        for row in range(left.rows)
        for column in range(left.cols)
    )


def payload(value: Matrix):
    hermitian = simplify((value + value.conjugate().T) / 2)
    anti = simplify((value - value.conjugate().T) / (2 * I))
    centered = simplify(anti - anti.trace() * I2 / 2)
    d_value = simplify((hermitian * hermitian).trace())
    r2_value = simplify((centered * centered).trace() / 2)
    if not bool(d_value.is_positive) or not bool(r2_value.is_positive):
        return None
    center = simplify(hermitian * hermitian / d_value)
    projector = simplify((I2 + centered / sqrt(r2_value)) / 2)
    return center, projector, simplify(I2 - projector)


def adjacent(left, right) -> bool:
    return sum(abs(left[index] - right[index]) for index in range(3)) == 1


def determinant_sign(perm):
    inversions = sum(
        1 for left in range(3) for right in range(left + 1, 3) if perm[left] > perm[right]
    )
    return -1 if inversions % 2 else 1


def rotations():
    result = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if determinant_sign(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = Matrix.zeros(3)
            for row, column in enumerate(perm):
                matrix[row, column] = signs[row]
            result.append(matrix)
    return tuple(result)


def rotate(matrix, site):
    result = matrix * Matrix(site)
    return tuple(int(result[index]) for index in range(3))


def equality_rank() -> int:
    rows = []
    for copy_index in range(1, 6):
        for coordinate in range(8):
            row = [0] * 48
            row[coordinate] = -1
            row[copy_index * 8 + coordinate] = 1
            rows.append(row)
    return Matrix(rows).rank()


def main() -> int:
    passed = 0
    failed = 0

    def check(name, condition, detail):
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    h_value = Matrix([[1, 1], [1, 2]])
    seed = simplify(h_value + I * SX)
    decoded = payload(seed)
    center_expected = Matrix([[Q(2, 7), Q(3, 7)], [Q(3, 7), Q(5, 7)]])
    px = simplify((I2 + SX) / 2)
    check(
        "decoder-reconstruction",
        decoded is not None and equal(decoded[0], center_expected) and equal(decoded[1], px),
        "an independent implementation recovers C and P from the generic payload",
    )

    center, projector, complement = decoded
    mass = simplify((center * projector).trace())
    other_mass = simplify((center * complement).trace())
    check(
        "binary-trace-law",
        mass == Q(13, 14) and other_mass == Q(1, 14) and mass + other_mass == 1,
        "independently reconstructed literal branches have exact normalized masses 13/14 and 1/14",
    )

    canonical = simplify(h_value / sqrt(7) + I * px)
    canonical_data = payload(canonical)
    check(
        "supported-surjection-fixture",
        canonical_data is not None
        and equal(canonical_data[0], center_expected)
        and equal(canonical_data[1], px),
        "the canonical sqrt(C)+iP representative reaches the same quotient fiber exactly",
    )

    complex_h = Matrix([[2, I], [-I, 1]])
    complex_data = payload(simplify(complex_h + I * SY))
    check(
        "complex-control",
        complex_data is not None
        and equal(complex_data[1], simplify((I2 + SY) / 2))
        and simplify((complex_data[0] * complex_data[1]).trace()) == Q(1, 14),
        "a separate complex-H/Y-program reconstruction gives mass 1/14",
    )

    pz = simplify((I2 + SZ) / 2)
    endpoint = payload(simplify(pz + I * pz))
    check(
        "endpoint-control",
        endpoint is not None
        and equal(endpoint[0], pz)
        and equal(endpoint[1], pz)
        and simplify((endpoint[0] * endpoint[2]).trace()) == 0,
        "a canonical pure payload independently reproduces the exact absent branch",
    )

    prior = []
    predecessor_counts = []
    for site in ORDER:
        predecessor_counts.append(sum(adjacent(site, old) for old in prior))
        prior.append(site)
    target_neighbors = {site for site in ORDER if adjacent(site, (0, 0, 0))}
    check(
        "append-geometry",
        predecessor_counts == [0] + [1] * 10 and target_neighbors == set(NEIGHBORS),
        "the independent graph check finds one seed, ten single-parent copies, and the complete target shell",
    )

    rotation_ok = True
    proper = rotations()
    for rotation in proper:
        rotated = tuple(rotate(rotation, site) for site in ORDER)
        counts = [
            sum(adjacent(site, old) for old in rotated[:index])
            for index, site in enumerate(rotated)
        ]
        shell = {site for site in rotated if adjacent(site, (0, 0, 0))}
        rotation_ok = rotation_ok and counts == [0] + [1] * 10
        rotation_ok = rotation_ok and shell == {rotate(rotation, d) for d in NEIGHBORS}
    check(
        "cubic-orbit",
        len(proper) == 24 and rotation_ok,
        "an independent signed-permutation enumeration preserves all 24 append certificates",
    )

    unitary = Matrix([[1, 1], [I, -I]]) / sqrt(2)
    transported = payload(simplify(unitary * seed * unitary.conjugate().T))
    check(
        "quotient-equivariance",
        transported is not None
        and equal(transported[0], simplify(unitary * center * unitary.conjugate().T))
        and equal(transported[1], simplify(unitary * projector * unitary.conjugate().T)),
        "a different exact unitary independently transports both decoded objects",
    )

    check(
        "independent-null-codimension",
        equality_rank() == 40,
        "the exact six-payload diagonal has codimension 40 under independent continuous draws",
    )

    determinant_values = (1 + I, 2 - I, -1 + 2 * I, 3)
    z_values = tuple(simplify(Q(1) / value) for value in determinant_values)
    norm2 = simplify(sum((value.conjugate() * value for value in z_values), Q(0)))
    psi = Matrix(z_values) / sqrt(norm2)
    rho = simplify(psi * psi.conjugate().T)
    projectors = tuple(
        simplify(Matrix.eye(4)[:, index] * Matrix.eye(4)[:, index].conjugate().T)
        for index in range(4)
    )
    born = tuple(simplify((projector * rho * projector).trace()) for projector in projectors)
    inverse_determinant = tuple(
        simplify(Q(1) / (value.conjugate() * value)) for value in determinant_values
    )
    inverse_norm = simplify(sum(inverse_determinant, Q(0)))
    inverse_squared = tuple(simplify(value / inverse_norm) for value in inverse_determinant)
    check(
        "four-arm-pincer-algebra",
        simplify(rho.trace()) == 1
        and sum(born, Q(0)) == 1
        and born == inverse_squared,
        "explicit rank-one product-basis traces select normalized inverse determinant modulus squared for four nonzero arms",
    )

    check(
        "premature-target-geometry",
        adjacent((1, 0, 0), (0, 0, 0)) and len(target_neighbors) == 6,
        "the origin is already copy-eligible after the first carrier, so formation order is a real boundary",
    )

    text = NOTE.read_text() if NOTE.exists() else ""
    check(
        "independent-source-fence",
        all(
            phrase in text
            for phrase in (
                "generic Gaussian seed",
                "canonical representative of a quotient fiber",
                "Formation-site boundary",
                "two-qubit",
                "No Minimal Axioms edit",
            )
        ),
        "the note preserves the generic/canonical, formation, pincer, and axiom fences",
    )

    print(
        "per_element: independent quotient, complex control, endpoint, trace weights, and canonical representative are checked"
    )
    print(
        "per_site: independent append adjacency, premature target eligibility, and exact six-neighbor completion are checked"
    )
    print(
        "per_mode: checked and not executed — the four-arm test is finite amplitude algebra, not a determinant or continuum mode"
    )
    print(
        "per_block: all 24 rotated 11-Record scaffolds and one conditional two-qubit four-arm readout are checked"
    )
    print(
        "lattice_wide: checked and not executed — no global site-selection, rate, recurrence, or infinite-volume process is claimed"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
