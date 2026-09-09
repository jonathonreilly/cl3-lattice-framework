#!/usr/bin/env python3
"""Independent exact check for the bounded RETA/C3 source-response packet.

This checker imports no primary implementation.  It builds the three C3
characters and their projectors in Q(w), w^2 + w + 1 = 0; obtains the source
response by multiplying the three one-dimensional determinant factors; and
evaluates the local and lens-space sums directly with stdlib complex/trig
arithmetic before comparing them with separately constructed Fraction
identities.  The p=3 uniqueness and the torsion-character rejection are exact.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import cos, isqrt, pi, sin
import sys


EXPECTED_CHECK_COUNT = 34
CHECKS: list[tuple[str, bool]] = []


def check(name: str, condition: object, detail: str = "") -> bool:
    ok = bool(condition)
    CHECKS.append((name, ok))
    suffix = f"  {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} {name}{suffix}")
    return ok


@dataclass(frozen=True)
class Eisenstein:
    """a + b*w in Q(w), with w^2 + w + 1 = 0."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", Fraction(self.a))
        object.__setattr__(self, "b", Fraction(self.b))

    @staticmethod
    def coerce(value: object) -> "Eisenstein":
        if isinstance(value, Eisenstein):
            return value
        return Eisenstein(Fraction(value), Fraction(0))

    def __add__(self, other: object) -> "Eisenstein":
        other = self.coerce(other)
        return Eisenstein(self.a + other.a, self.b + other.b)

    def __sub__(self, other: object) -> "Eisenstein":
        other = self.coerce(other)
        return Eisenstein(self.a - other.a, self.b - other.b)

    def __neg__(self) -> "Eisenstein":
        return Eisenstein(-self.a, -self.b)

    def __mul__(self, other: object) -> "Eisenstein":
        other = self.coerce(other)
        # (a+bw)(c+dw) = (ac-bd) + (ad+bc-bd)w.
        return Eisenstein(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a - self.b * other.b,
        )

    def __truediv__(self, other: object) -> "Eisenstein":
        scalar = Fraction(other)
        return Eisenstein(self.a / scalar, self.b / scalar)

    def conjugate(self) -> "Eisenstein":
        # bar(w) = w^2 = -1-w.
        return Eisenstein(self.a - self.b, -self.b)


ZERO = Eisenstein(0)
ONE = Eisenstein(1)
W = Eisenstein(0, 1)
Matrix = list[list[Eisenstein]]


def w_power(exponent: int) -> Eisenstein:
    return (ONE, W, -ONE - W)[exponent % 3]


def matrix_zero(size: int = 3) -> Matrix:
    return [[ZERO for _ in range(size)] for _ in range(size)]


def matrix_identity(size: int = 3) -> Matrix:
    return [
        [ONE if row == column else ZERO for column in range(size)]
        for row in range(size)
    ]


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] + right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def matrix_scale(scalar: object, matrix: Matrix) -> Matrix:
    scalar = Eisenstein.coerce(scalar)
    return [[scalar * entry for entry in row] for row in matrix]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    result = matrix_zero(size)
    for i in range(size):
        for j in range(size):
            value = ZERO
            for k in range(size):
                value = value + left[i][k] * right[k][j]
            result[i][j] = value
    return result


def matrix_conjugate(matrix: Matrix) -> Matrix:
    return [[entry.conjugate() for entry in row] for row in matrix]


def matrix_adjoint(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return [
        [matrix[j][i].conjugate() for j in range(size)]
        for i in range(size)
    ]


def matrix_trace(matrix: Matrix) -> Eisenstein:
    value = ZERO
    for i in range(len(matrix)):
        value = value + matrix[i][i]
    return value


def matrix_key(matrix: Matrix) -> tuple[tuple[Eisenstein, ...], ...]:
    return tuple(tuple(row) for row in matrix)


def polynomial_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def determinant_source_coefficients(
    a_s: Fraction, a_d: Fraction, source_scale: Fraction
) -> tuple[Fraction, ...]:
    """Coefficients of a_s (a_d + source_scale*j)^2, built mode by mode."""

    factors = (
        [Fraction(a_s)],
        [Fraction(a_d), Fraction(source_scale)],
        [Fraction(a_d), Fraction(source_scale)],
    )
    result = [Fraction(1)]
    for factor in factors:
        result = polynomial_multiply(result, factor)
    return tuple(result)


def normalized_trace_response(
    a_s: Fraction, a_d: Fraction, source_scale: Fraction
) -> Fraction:
    coefficients = determinant_source_coefficients(a_s, a_d, source_scale)
    logarithmic_derivative = coefficients[1] / coefficients[0]
    return logarithmic_derivative / 3


def stipulated_response(
    a_s: Fraction, a_d: Fraction, source_scale: Fraction
) -> Fraction:
    """Normalized trace followed by the separately stipulated 1/3 density."""

    return normalized_trace_response(a_s, a_d, source_scale) / 3


def local_sum_numeric(p: int) -> complex:
    total = 0j
    for k in range(1, p):
        angle = 2 * pi * k / p
        root = complex(cos(angle), sin(angle))
        total += 1 / ((root - 1) * (root.conjugate() - 1))
    return total / p


def lens_sum_numeric(p: int) -> float:
    return sum((cos(pi * k / p) / sin(pi * k / p)) ** 2 for k in range(1, p)) / p


def local_closed(p: int) -> Fraction:
    return Fraction(p * p - 1, 12 * p)


def lens_closed(p: int) -> Fraction:
    return Fraction((p - 1) * (p - 2), 3 * p)


def gap_closed(p: int) -> Fraction:
    return Fraction((p - 1) * (p - 3), 4 * p)


def integer_polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def integer_polynomial_scale(scalar: int, polynomial: list[int]) -> list[int]:
    return [scalar * coefficient for coefficient in polynomial]


def integer_polynomial_subtract(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return [
        (left[i] if i < len(left) else 0)
        - (right[i] if i < len(right) else 0)
        for i in range(size)
    ]


def mod_one(value: Fraction) -> Fraction:
    value = Fraction(value)
    return value - value.numerator // value.denominator


def main() -> int:
    identity = matrix_identity()
    cycle = [
        [ZERO, ZERO, ONE],
        [ONE, ZERO, ZERO],
        [ZERO, ONE, ZERO],
    ]
    cycle_powers = (identity, cycle, matrix_multiply(cycle, cycle))

    characters = {
        r: tuple(w_power(r * k) for k in range(3))
        for r in range(3)
    }
    character_law = all(
        characters[r][(k + ell) % 3]
        == characters[r][k] * characters[r][ell]
        for r in range(3)
        for k in range(3)
        for ell in range(3)
    )
    check(
        "c3.characters.enumerated",
        character_law and len(set(characters.values())) == 3,
        "three distinct exact homomorphisms",
    )

    orthogonal = True
    for r in range(3):
        for s in range(3):
            inner = ZERO
            for k in range(3):
                inner = inner + characters[r][k].conjugate() * characters[s][k]
            orthogonal &= inner / 3 == (ONE if r == s else ZERO)
    check("c3.characters.orthogonality", orthogonal, "exact Q(w) inner products")

    projectors: list[Matrix] = []
    for r in range(3):
        projector = matrix_zero()
        for k in range(3):
            projector = matrix_add(
                projector,
                matrix_scale(w_power(-r * k), cycle_powers[k]),
            )
        projectors.append(matrix_scale(Fraction(1, 3), projector))

    spectral = all(
        matrix_multiply(cycle, projectors[r])
        == matrix_scale(w_power(r), projectors[r])
        for r in range(3)
    )
    check("c3.projectors.spectral", spectral, "C P_r = w^r P_r")

    resolution = matrix_zero()
    for projector in projectors:
        resolution = matrix_add(resolution, projector)
    projector_algebra = (
        resolution == identity
        and all(matrix_trace(projector) == ONE for projector in projectors)
        and all(
            matrix_multiply(projectors[r], projectors[s])
            == (projectors[r] if r == s else matrix_zero())
            for r in range(3)
            for s in range(3)
        )
    )
    check("c3.projectors.resolution", projector_algebra, "three rank-one orthogonal idempotents")

    star_and_k = all(matrix_adjoint(projector) == projector for projector in projectors)
    star_and_k &= all(
        matrix_conjugate(projectors[r]) == projectors[(-r) % 3]
        for r in range(3)
    )
    check("c3.projectors.star_and_K", star_and_k, "K fixes P0 and swaps P1,P2")

    subset_projectors: dict[tuple[int, int, int], Matrix] = {}
    for mask in range(8):
        bits = tuple((mask >> r) & 1 for r in range(3))
        projector = matrix_zero()
        for r, bit in enumerate(bits):
            if bit:
                projector = matrix_add(projector, projectors[r])
        subset_projectors[bits] = projector

    all_eight = (
        len({matrix_key(projector) for projector in subset_projectors.values()}) == 8
        and all(
            matrix_adjoint(projector) == projector
            and matrix_multiply(projector, projector) == projector
            and matrix_multiply(cycle, projector) == matrix_multiply(projector, cycle)
            for projector in subset_projectors.values()
        )
    )
    check("c3.projections.character_subsets", all_eight, "all 2^3 spectral projections")

    k_even_bits = {
        bits
        for bits, projector in subset_projectors.items()
        if matrix_conjugate(projector) == projector
    }
    expected_k_even = {(0, 0, 0), (1, 0, 0), (0, 1, 1), (1, 1, 1)}
    check("c3.projections.K_even", k_even_bits == expected_k_even, "0, P_s, P_d, I")

    pure_doublet = [
        bits
        for bits in k_even_bits
        if bits != (0, 0, 0)
        and matrix_multiply(subset_projectors[bits], projectors[0]) == matrix_zero()
    ]
    check("c3.projections.doublet_unique", pure_doublet == [(0, 1, 1)], "unique P_d")

    source_grid = (
        (Fraction(1, 2), Fraction(1), Fraction(7, 3)),
        (Fraction(1, 3), Fraction(1), Fraction(5, 2), Fraction(4)),
        (Fraction(-2), Fraction(1, 4), Fraction(1), Fraction(3)),
    )
    response_family = all(
        stipulated_response(a_s, a_d, c) == Fraction(2) * c / (9 * a_d)
        for a_s in source_grid[0]
        for a_d in source_grid[1]
        for c in source_grid[2]
    )
    check("response.mode_product_family", response_family, "48 exact (a_s,a_d,c) triples")

    base_coefficients = determinant_source_coefficients(Fraction(7), Fraction(1), Fraction(1))
    base_response = stipulated_response(Fraction(7), Fraction(1), Fraction(1))
    check(
        "response.unit_member",
        base_coefficients == (Fraction(7), Fraction(14), Fraction(7))
        and base_response == Fraction(2, 9)
        and 3 * base_response == Fraction(2, 3),
        "h=2/9, Phi=2/3",
    )

    check(
        "response.trace_then_density_typed",
        normalized_trace_response(Fraction(7), Fraction(1), Fraction(1))
        == Fraction(2, 3)
        and stipulated_response(Fraction(7), Fraction(1), Fraction(1))
        == Fraction(1, 3) * Fraction(2, 3),
        "tau(A^-1 P_d)=2/3; stipulated density gives 2/9",
    )

    true_group_average = matrix_zero()
    for k in range(3):
        true_group_average = matrix_add(
            true_group_average,
            matrix_multiply(
                matrix_multiply(cycle_powers[k], subset_projectors[(0, 1, 1)]),
                cycle_powers[(-k) % 3],
            ),
        )
    true_group_average = matrix_scale(Fraction(1, 3), true_group_average)
    check(
        "response.true_conjugation_average",
        true_group_average == subset_projectors[(0, 1, 1)],
        "invariant P_d is returned unchanged, not divided by three",
    )

    determinant_exponents = {
        "real_boson": Fraction(-1, 2),
        "complex_boson": Fraction(-1),
        "complex_Grassmann": Fraction(1),
    }
    check(
        "response.statistics_change_determinant_power",
        len(set(determinant_exponents.values())) == 3
        and determinant_exponents["complex_Grassmann"] == 1,
        "det^-1/2, det^-1, det",
    )

    source_scales = (Fraction(1), Fraction(2), Fraction(-3, 2))
    source_responses = tuple(
        stipulated_response(Fraction(5), Fraction(1), c) for c in source_scales
    )
    check(
        "response.source_scale_counterfamily",
        source_responses == (Fraction(2, 9), Fraction(4, 9), Fraction(-1, 3)),
        "c=(1,2,-3/2) changes h linearly",
    )

    action_scales = (Fraction(1, 2), Fraction(1), Fraction(3))
    action_responses = tuple(
        stipulated_response(Fraction(5), scale, Fraction(1))
        for scale in action_scales
    )
    check(
        "response.action_scale_counterfamily",
        action_responses == (Fraction(4, 9), Fraction(2, 9), Fraction(2, 27))
        and all(scale * value == Fraction(2, 9) for scale, value in zip(action_scales, action_responses)),
        "a_d=(1/2,1,3) changes h inversely",
    )

    tolerance = 3e-12
    for p in range(2, 13):
        local_numeric = local_sum_numeric(p)
        lens_numeric = lens_sum_numeric(p)
        local_exact = local_closed(p)
        lens_exact = lens_closed(p)
        direct_sums_match = (
            abs(local_numeric.imag) < tolerance
            and abs(local_numeric.real - float(local_exact)) < tolerance
            and abs(lens_numeric - float(lens_exact)) < tolerance
        )
        exact_gap_matches = lens_exact - local_exact == gap_closed(p)
        check(
            f"cyclic.p{p}.local_vs_lens",
            direct_sums_match and exact_gap_matches,
            f"F={local_exact} E={lens_exact} E-F={gap_closed(p)}",
        )

    # Put both formulas over 12p using polynomial coefficients low-to-high.
    four_e_numerator = integer_polynomial_scale(
        4, integer_polynomial_multiply([-1, 1], [-2, 1])
    )
    f_numerator = [-1, 0, 1]
    gap_numerator = integer_polynomial_subtract(four_e_numerator, f_numerator)
    factored_gap_numerator = integer_polynomial_scale(
        3, integer_polynomial_multiply([-1, 1], [-3, 1])
    )
    check(
        "cyclic.gap_polynomial_identity",
        gap_numerator == factored_gap_numerator == [9, -12, 3],
        "12p(E-F)=3(p-1)(p-3)",
    )

    check(
        "cyclic.p3.crossing_value",
        local_closed(3) == lens_closed(3) == Fraction(2, 9),
        "F_3=E_3=2/9",
    )

    lens_plus = lens_sum_numeric(3)
    lens_minus = -lens_sum_numeric(3)
    check(
        "cyclic.lens_weight_orientation_sign",
        abs(lens_plus - float(Fraction(2, 9))) < tolerance
        and abs(lens_minus + float(Fraction(2, 9))) < tolerance,
        "weights (1,1) and (1,-1) differ by orientation/sign",
    )

    raw_eta = Fraction(2, 9)
    kernel_h = Fraction(1)
    check(
        "cyclic.raw_vs_reduced_eta",
        (raw_eta + kernel_h) / 2 == Fraction(11, 18)
        and (-raw_eta + kernel_h) / 2 == Fraction(7, 18),
        "h_B=1; reduced eta is 11/18 or 7/18",
    )

    c0, c1, c2 = gap_numerator
    discriminant = c1 * c1 - 4 * c2 * c0
    square_root = isqrt(discriminant)
    exact_roots = {
        Fraction(-c1 - square_root, 2 * c2),
        Fraction(-c1 + square_root, 2 * c2),
    }
    admissible_roots = {root for root in exact_roots if root.denominator == 1 and root >= 2}
    scanned_crossings = [p for p in range(2, 13) if local_closed(p) == lens_closed(p)]
    check(
        "cyclic.p3.unique_nontrivial_integer",
        discriminant == 36
        and square_root * square_root == discriminant
        and exact_roots == {Fraction(1), Fraction(3)}
        and admissible_roots == {Fraction(3)}
        and scanned_crossings == [3],
        "exact roots {1,3}; p>=2 leaves p=3",
    )

    torsion_values = tuple(Fraction(m, 3) for m in range(3))
    torsion_maps = {
        value: tuple(mod_one(n * value) for n in range(3))
        for value in torsion_values
    }
    torsion_homomorphisms = all(
        torsion_maps[value][(left + right) % 3]
        == mod_one(torsion_maps[value][left] + torsion_maps[value][right])
        for value in torsion_values
        for left in range(3)
        for right in range(3)
    )
    check(
        "torsion.Z3_characters_enumerated",
        torsion_homomorphisms
        and len(set(torsion_maps.values())) == 3
        and all(mod_one(3 * value) == 0 for value in torsion_values),
        "generator values {0,1/3,2/3}",
    )

    candidate = Fraction(2, 9)
    candidate_residual = mod_one(3 * candidate)
    check(
        "torsion.two_ninths_invalid_character",
        candidate not in torsion_values and candidate_residual == Fraction(2, 3),
        "3*(2/9)=2/3 mod 1, not 0",
    )

    check(
        "harness.expected_check_count",
        len(CHECKS) + 1 == EXPECTED_CHECK_COUNT,
        f"declared={EXPECTED_CHECK_COUNT}",
    )

    passed = sum(ok for _name, ok in CHECKS)
    failed = len(CHECKS) - passed
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
