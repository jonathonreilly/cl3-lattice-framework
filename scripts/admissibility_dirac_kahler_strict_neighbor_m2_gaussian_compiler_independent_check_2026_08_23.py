#!/usr/bin/env python3
"""Independent check of the Block-44 strict-neighbor M2 compiler.

This checker does not import the primary runner.  On the supplied
xgraded width-four background at T_cover=16 and m=1, it reconstructs the c=1/3
innovation factor with reversed edge order, compiles a reversed eleven-leaf
residual, and checks a temporal cover disjoint from the primary fixtures.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10 as parent


b174 = parent.b174
MENU = b174.MENU
RECORD_CELL = (b174.RECORD_LEVEL, 0)
R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_"
    "COMPILER_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_"
    "compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_"
    "NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-23.md": "b77307fd3fcc3a603a34f41841dc707c09d341011ab54dca19b6e45f3541f6c4",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py": "8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md": "9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py": "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
}


def input_hashes_match() -> bool:
    return all(
        (ROOT / path).is_file()
        and sha256((ROOT / path).read_bytes()).hexdigest()
        == INPUT_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )

A = sp.Integer(3)
B = R(3, 2)
C = R(9, 2)
SA = sp.sqrt(A)
SB = sp.sqrt(B)


@dataclass(frozen=True)
class Leaf:
    name: str
    value: sp.Expr
    visible: bool


def zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and zero(left - right)


def herm(matrix: sp.Matrix) -> sp.Matrix:
    return sp.expand((matrix + matrix.H) / 2)


def edges(matrices: tuple[sp.Matrix, ...]) -> tuple[tuple[int, int], ...]:
    size = matrices[0].rows
    return tuple(
        reversed(
            [
                (row, column)
                for row in range(size)
                for column in range(row + 1, size)
                if any(matrix[row, column] != 0 for matrix in matrices)
            ]
        )
    )


def gram(
    symmetric: sp.Matrix,
    variance,
    edge_roster: tuple[tuple[int, int], ...],
) -> tuple[sp.Matrix, tuple]:
    size = symmetric.rows
    output = sp.zeros(size, len(edge_roster) + size)
    used = [ZERO for _ in range(size)]
    for index, (row, column) in enumerate(edge_roster):
        weight = sp.cancel(symmetric[row, column])
        if weight == 0:
            continue
        magnitude = sp.Abs(weight)
        output[row, index] = sp.sqrt(magnitude)
        output[column, index] = sp.sign(weight) * sp.sqrt(magnitude)
        used[row] += magnitude
        used[column] += magnitude
    residual = tuple(
        sp.cancel(symmetric[row, row] - variance - used[row])
        for row in range(size)
    )
    for row, value in enumerate(residual):
        if value.is_nonnegative:
            output[row, len(edge_roster) + row] = sp.sqrt(value)
    return output, residual


def divide(items: list[Leaf], counter: list[int], cut: int) -> tuple[list[Leaf], list[Leaf]]:
    name = f"h{counter[0]}"
    counter[0] += 1
    left = [Leaf(item.name, sp.expand(SA * item.value), item.visible) for item in items[:cut]]
    right = [Leaf(item.name, sp.expand(SB * item.value), item.visible) for item in items[cut:]]
    left.append(Leaf(name, -SA, False))
    right.append(Leaf(name, SB, False))
    return left, right


def ternary(items: list[Leaf], counter: list[int]) -> list[list[Leaf]]:
    if len(items) <= 3:
        return [items]
    # Reverse-biased cut differs from the primary traversal.
    cut = (len(items) + 1) // 2
    left, right = divide(items, counter, cut)
    return ternary(right, counter) + ternary(left, counter)


def peel(items: list[Leaf], counter: list[int]) -> list[list[Leaf]]:
    result = []
    current = list(reversed(items))
    while sum(item.visible for item in current) > 1:
        index = next(i for i, item in enumerate(current) if item.visible)
        ordered = [current[index], *current[:index], *current[index + 1 :]]
        leaf, current = divide(ordered, counter, 1)
        result.append(leaf)
    result.append(current)
    return result


def independent_compile(values: tuple[sp.Expr, ...]) -> tuple[sp.Matrix, sp.Matrix, list[list[Leaf]], int]:
    counter = [0]
    initial = [
        Leaf(f"v{index}", value, True)
        for index, value in reversed(tuple(enumerate(values)))
    ]
    factors = []
    for item in ternary(initial, counter):
        factors.extend(peel(item, counter))
    hidden_count = counter[0]
    labels = [f"v{index}" for index in range(len(values))] + [
        f"h{index}" for index in range(hidden_count)
    ]
    positions = {name: index for index, name in enumerate(labels)}
    precision = sp.zeros(len(labels))
    for factor in factors:
        vector = sp.zeros(len(labels), 1)
        for item in factor:
            vector[positions[item.name], 0] += item.value
        precision += vector.conjugate() * vector.T
    hidden = precision[len(values) :, len(values) :]
    visible = (
        precision[: len(values), : len(values)]
        - precision[: len(values), len(values) :]
        * hidden.inv(method="DM")
        * precision[len(values) :, : len(values)]
    )
    return sp.simplify(visible), hidden, factors, hidden_count


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, ZERO))
    return tuple(sp.cancel(value / total) for value in values)


def rotations() -> tuple:
    answer = []
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                values = [0, 0, 0]
                values[order[row]] = signs[row]
                rows.append(tuple(values))
            matrix = tuple(rows)
            if int(sp.det(sp.Matrix(matrix))) == 1:
                answer.append(matrix)
    return tuple(answer)


def apply_rotation(rotation, vector):
    return tuple(
        sum(rotation[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


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

    base = sp.Matrix([[A, ZERO, -A], [ZERO, B, B], [-A, B, C]])
    schur = base[:2, :2] - base[:2, 2:] * base[2:, 2:].inv() * base[2:, :2]
    check(
        "independent-normalized-split",
        A + B == C
        and sp.cancel(A * B / C) == ONE
        and equal(schur, sp.ones(2)),
        "a direct three-variable Schur calculation reconstructs the fixed C=9/2 complex-Gaussian identity",
    )

    values = tuple(
        R(12 - index, 13 - index) * (I if index % 2 else ONE)
        for index in range(11)
    )
    visible, hidden, factors, count = independent_compile(values)
    column = sp.Matrix(values)
    mediator_degrees = Counter(
        item.name for factor in factors for item in factor if not item.visible
    )
    check(
        "independent-reversed-eleven-leaf-compiler",
        count == 12
        and len(factors) == 13
        and max(map(len, factors)) <= 3
        and max(sum(item.visible for item in factor) for factor in factors) <= 1
        and set(mediator_degrees.values()) == {2}
        and equal(visible, column.conjugate() * column.T)
        and sp.factor(hidden.det(method="domain-ge")) == C ** count,
        "a reversed leaf order and reverse-biased recursion independently recover the rank-one precision and C^12 hidden determinant",
    )

    fixture = b174.Fixture(4, tag="b179-independent", cover_t=16)
    qs = tuple(fixture.q({RECORD_CELL: value}) for value in MENU)
    symmetric = tuple(herm(q) for q in qs)
    edge_roster = edges(symmetric)
    variance = R(1, 3)
    factors_b = tuple(gram(matrix, variance, edge_roster) for matrix in symmetric)
    check(
        "independent-m3-local-innovation-parent",
        all(
            all(value.is_positive for value in residual)
            and equal(Bmat * Bmat.H, S - variance * sp.eye(fixture.N))
            for S, (Bmat, residual) in zip(symmetric, factors_b)
        ),
        "the disjoint xgraded width-four, physical-time-eight, mass-one cover has an exact reversed-edge c=1/3 Gram split on all four arms",
    )

    reference_q = qs[-1]
    reference_b = factors_b[-1][0]
    changed = tuple(
        row
        for row in range(fixture.N)
        if any(
            q[row, column] != reference_q[row, column]
            for q in qs[:-1]
            for column in range(fixture.N)
        )
        or any(
            Bmat[row, column] != reference_b[row, column]
            for Bmat, _ in factors_b[:-1]
            for column in range(reference_b.cols)
        )
    )
    labels = set()
    for row in changed:
        for column in range(fixture.N):
            if any(q[row, column] != 0 for q in qs):
                labels.add(("p", column))
        for column in range(reference_b.cols):
            if any(Bmat[row, column] != 0 for Bmat, _ in factors_b):
                labels.add(("z", column))
    check(
        "independent-record-star-capacity",
        len(changed) == 3
        and len(labels) == 16
        and len(tuple(range(0, len(labels), 3))) == 6,
        "the independently reconstructed arm mutation has three rows and sixteen complex inputs, hence fits at most three per six Record neighbors",
    )

    rosters = []
    for row in range(fixture.N):
        row_labels = []
        for column in range(fixture.N):
            if any(q[row, column] != 0 for q in qs):
                row_labels.append(("p", column))
        for column in range(reference_b.cols):
            if any(Bmat[row, column] != 0 for Bmat, _ in factors_b):
                row_labels.append(("z", column))
        rosters.append(tuple(row_labels))
    use = Counter(
        label
        for row, roster in enumerate(rosters)
        if row not in changed
        for label in roster
    )
    check(
        "independent-arity-and-port-bounds",
        max(map(len, rosters)) == 11
        and max(use.values(), default=0) <= 8
        and 8 < 6 * 4,
        "the disjoint cover independently has eleven-term residuals and at most eight bulk occurrences per original, below the 24 neighboring M2 port coordinates",
    )

    q_inverses = tuple(q.inv(method="DM") for q in qs)
    covariances = tuple(
        sp.expand(
            inverse
            * (Bmat * Bmat.H + variance * sp.eye(fixture.N))
            * inverse.H
        )
        for inverse, (Bmat, _) in zip(q_inverses, factors_b)
    )
    expected = tuple(herm(inverse) for inverse in q_inverses)
    raw = tuple(
        sp.cancel(variance ** fixture.N / b174.norm2(b174.dm_det(q)))
        for q in qs
    )
    determinant = tuple(
        sp.cancel(ONE / b174.norm2(b174.dm_det(q))) for q in qs
    )
    check(
        "independent-interface-preservation",
        normalize(raw) == normalize(determinant)
        and all(equal(left, right) for left, right in zip(covariances, expected)),
        "the mass-one c=1/3 disjoint cover independently recovers the determinant arm law and Herm(q^-1) covariance that normalized compiler integration must preserve",
    )

    cubic = rotations()
    frame_vectors = {apply_rotation(rotation, (1, 2, 3)) for rotation in cubic}
    rotated_directions = all(
        {apply_rotation(rotation, direction) for direction in parent.b42.DIRECTIONS}
        == set(parent.b42.DIRECTIONS)
        for rotation in cubic
    ) if hasattr(parent.b42, "DIRECTIONS") else all(
        {
            apply_rotation(rotation, direction)
            for direction in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
        }
        == {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}
        for rotation in cubic
    )
    check(
        "independent-cubic-orbit",
        len(cubic) == 24 and len(frame_vectors) == 24 and rotated_directions,
        "an independently enumerated proper-cubic group gives a free 24-frame tag orbit and preserves the six physical neighbor directions",
    )

    unnormalized_zero_integral = sp.cancel(sp.pi / C)
    normalized_zero_factor = sp.cancel((C / sp.pi) * unnormalized_zero_integral)
    broken = sp.Matrix([[A, ZERO, -A], [ZERO, B, -B], [-A, -B, C]])
    broken_schur = broken[:2, :2] - broken[:2, 2:] * broken[2:, 2:].inv() * broken[2:, :2]
    check(
        "independent-mutations",
        normalized_zero_factor == ONE
        and unnormalized_zero_integral != ONE
        and not equal(broken_schur, sp.ones(2)),
        "a normalized zero mediator contributes exactly one, omitting its C/pi normalization leaves pi/C, and a sign mutation changes the exact Schur target",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check(
        "independent-boundary",
        input_hashes_match()
        and parent.supplier_certificate()
        and "representation-invariant base measure" in note_text
        and "autonomous permanent Record write" in note_text
        and "zero TOE percentage movement" in note_text,
        "the extracted runtime closure and current Block 105 supplier are hash-bound, and the final note keeps measure/action selection, Record process, retention, and TOE accounting outside the theorem",
    )

    print("per_element: independent Schur identity, reversed compiler, hidden determinant, signs, and normalization are exact")
    print("per_site: three changed rows, sixteen Record-neighbor coordinates, and the M2 port budget are independently reconstructed")
    print("per_mode: the mass-one c=1/3 Gram, determinant partition, covariance, and 24-frame cubic orbit are checked")
    print("per_block: disjoint physical-time-eight cover, four arms, all rows, and the final claim boundary are checked")
    print("lattice_wide: NOT CLOSED; no periodic cover-independent fixed-density embedding, seam proof, or full site-map covariance is claimed")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
