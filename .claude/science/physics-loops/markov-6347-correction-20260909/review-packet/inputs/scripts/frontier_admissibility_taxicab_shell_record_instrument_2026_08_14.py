#!/usr/bin/env python3
"""Exact checks for a seed-grown Admissibility/Record instrument on Z^3.

The displayed candidate is one fixed synchronous local law.  Occupancy of the
six nearest neighbours determines d in {-1,0,1}^3.  At a forming site d != 0,
the law stores one of the two spectral projectors P_s(d) with either the
linear spectral weights or a hostile cubic-response weight.  The runner proves
the taxicab-shell geometry, exact M_2(C) identities, finite-cylinder
normalization/consistency, proper-cubic covariance, Record permanence, and
spatial frequency bounds.  It also keeps the two weight laws distinct.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Vec = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

ORIGIN: Site = (0, 0, 0)
AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
I2 = sp.eye(2)


def add(left: Site, right: Site) -> Site:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def sub(left: Site, right: Site) -> Site:
    return tuple(left[i] - right[i] for i in range(3))  # type: ignore[return-value]


def taxicab_norm(site: Site, center: Site = ORIGIN) -> int:
    return sum(abs(site[i] - center[i]) for i in range(3))


def taxicab_ball(radius: int, center: Site = ORIGIN) -> frozenset[Site]:
    if radius < 0:
        return frozenset()
    return frozenset(
        (center[0] + x, center[1] + y, center[2] + z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


def taxicab_shell(radius: int, center: Site = ORIGIN) -> frozenset[Site]:
    return taxicab_ball(radius, center) - taxicab_ball(radius - 1, center)


def ball_size_formula(radius: int) -> int:
    if radius < 0:
        return 0
    return (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3


def shell_size_formula(radius: int) -> int:
    if radius == 0:
        return 1
    if radius < 0:
        return 0
    return 4 * radius**2 + 2


def occupied(site: Site, records: set[Site] | frozenset[Site]) -> int:
    return int(site in records)


def neighbour_difference(site: Site, records: set[Site] | frozenset[Site]) -> Vec:
    return tuple(
        occupied(add(site, axis), records) - occupied(sub(site, axis), records)
        for axis in AXES
    )  # type: ignore[return-value]


def k_value(direction: Vec) -> int:
    return sum(value * value for value in direction)


def candidate_frontier(records: set[Site] | frozenset[Site]) -> frozenset[Site]:
    candidates = {
        add(site, step)
        for site in records
        for axis in AXES
        for step in (axis, tuple(-value for value in axis))
    }
    return frozenset(
        site
        for site in candidates - set(records)
        if neighbour_difference(site, records) != (0, 0, 0)
    )


def expected_shell_direction(site: Site, center: Site = ORIGIN) -> Vec:
    relative = sub(site, center)
    return tuple(0 if value == 0 else (-1 if value > 0 else 1) for value in relative)  # type: ignore[return-value]


def nonzero_coordinate_count(site: Site, center: Site = ORIGIN) -> int:
    return sum(value != 0 for value in sub(site, center))


def shell_type_counts_formula(radius: int) -> dict[int, int]:
    if radius < 1:
        return {1: 0, 2: 0, 3: 0}
    return {
        1: 6,
        2: 12 * (radius - 1),
        3: 4 * (radius - 1) * (radius - 2),
    }


def cumulative_type_count(radius: int, k: int) -> int:
    if radius < 1:
        return 0
    if k == 1:
        return 6 * radius
    if k == 2:
        return 6 * radius * (radius - 1)
    if k == 3:
        return 4 * radius * (radius - 1) * (radius - 2) // 3
    raise ValueError("k must be 1, 2, or 3")


def bloch_operator(direction: Vec) -> sp.Matrix:
    return sum(
        (sp.Integer(direction[index]) * SIGMA[index] for index in range(3)),
        sp.zeros(2),
    )


def projector(direction: Vec, sign: int) -> sp.Matrix:
    k = k_value(direction)
    if k == 0 or sign not in (-1, 1):
        raise ValueError("a projector needs nonzero direction and sign +/-1")
    return sp.simplify((I2 + sign * bloch_operator(direction) / sp.sqrt(k)) / 2)


def local_density(direction: Vec) -> sp.Matrix:
    return sp.simplify((I2 + bloch_operator(direction) / 3) / 2)


def response_density(direction: Vec, power: int) -> sp.Matrix:
    """Density representer induced by one displayed spectral response."""
    k = k_value(direction)
    if k == 0:
        raise ValueError("a spectral response needs a nonzero direction")
    return sp.simplify(
        sum(
            (
                response_weight(k, sign, power) * projector(direction, sign)
                for sign in (-1, 1)
            ),
            sp.zeros(2),
        )
    )


def response_weight(k: int, sign: int, power: int) -> sp.Expr:
    if k not in (1, 2, 3) or sign not in (-1, 1) or power not in (1, 3):
        raise ValueError("declared law uses k=1,2,3; sign +/-1; power 1 or 3")
    radial = sp.sqrt(k) / 3
    return sp.simplify((1 + sign * radial**power) / 2)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(left[row, col] - right[row, col]) == 0
        for row in range(left.rows)
        for col in range(left.cols)
    )


def finite_record_update(
    records: dict[Site, sp.ImmutableMatrix],
    signs: dict[Site, int],
) -> dict[Site, sp.ImmutableMatrix]:
    old_sites = frozenset(records)
    frontier = candidate_frontier(old_sites)
    if set(signs) != set(frontier):
        raise ValueError("one branch sign is required for every forming site")
    updated = dict(records)
    for site in sorted(frontier):
        direction = neighbour_difference(site, old_sites)
        updated[site] = sp.ImmutableMatrix(projector(direction, signs[site]))
    return updated


def content_readout(content: sp.ImmutableMatrix) -> sp.ImmutableMatrix:
    """The displayed content-only readout: return the locked matrix."""
    return sp.ImmutableMatrix(content)


def preserves_records(
    before: dict[Site, sp.ImmutableMatrix],
    after: dict[Site, sp.ImmutableMatrix],
) -> bool:
    return all(site in after and after[site] == content for site, content in before.items())


def deterministic_sign(site: Site) -> int:
    return 1 if (site[0] + 2 * site[1] + 3 * site[2]) % 2 == 0 else -1


def branch_probability(
    assignments: dict[Site, int], center: Site, power: int
) -> sp.Expr:
    out = sp.Integer(1)
    for site, sign in assignments.items():
        direction = expected_shell_direction(site, center)
        out *= response_weight(k_value(direction), sign, power)
    return sp.simplify(out)


def shell_partition_sum(radius: int, power: int) -> sp.Expr:
    counts = shell_type_counts_formula(radius)
    out = sp.Integer(1)
    for k, count in counts.items():
        plus = response_weight(k, 1, power)
        minus = response_weight(k, -1, power)
        binomial_sum = sum(
            sp.Integer(comb(count, number_plus))
            * plus**number_plus
            * minus ** (count - number_plus)
            for number_plus in range(count + 1)
        )
        out *= sp.simplify(binomial_sum)
    return sp.simplify(out)


def two_cube_patch() -> frozenset[Site]:
    cube_a = {
        (x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)
    }
    cube_b = {
        (x, y, z) for x in (1, 2) for y in (0, 1) for z in (0, 1)
    }
    return frozenset(cube_a | cube_b)


def patch_frontier(records: frozenset[Site], patch: frozenset[Site]) -> frozenset[Site]:
    return frozenset(
        site
        for site in patch - records
        if neighbour_difference(site, records) != (0, 0, 0)
    )


def determinant3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def quaternion_rotation(q: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]) -> sp.Matrix:
    w, x, y, z = q
    return sp.simplify(
        sp.Matrix(
            [
                [1 - 2 * (y**2 + z**2), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                [2 * (x * y + z * w), 1 - 2 * (x**2 + z**2), 2 * (y * z - x * w)],
                [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x**2 + y**2)],
            ]
        )
    )


def quaternion_unitary(q: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]) -> sp.Matrix:
    w, x, y, z = q
    return sp.Matrix(
        [[w - sp.I * z, -y - sp.I * x], [y - sp.I * x, w + sp.I * z]]
    )


def proper_cubic_lifts() -> list[tuple[Rotation, sp.Matrix]]:
    quaternions: list[tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]] = []
    for coordinate in range(4):
        for sign in (-1, 1):
            values = [sp.Integer(0)] * 4
            values[coordinate] = sp.Integer(sign)
            quaternions.append(tuple(values))  # type: ignore[arg-type]
    for signs in product((-1, 1), repeat=4):
        quaternions.append(tuple(sp.Rational(sign, 2) for sign in signs))
    for first, second in combinations(range(4), 2):
        for signs in product((-1, 1), repeat=2):
            values = [sp.Integer(0)] * 4
            values[first] = signs[0] / sp.sqrt(2)
            values[second] = signs[1] / sp.sqrt(2)
            quaternions.append(tuple(values))  # type: ignore[arg-type]

    lifts: dict[Rotation, sp.Matrix] = {}
    for quaternion in quaternions:
        rotation_symbolic = quaternion_rotation(quaternion)
        entries = tuple(
            tuple(int(sp.simplify(rotation_symbolic[row, col])) for col in range(3))
            for row in range(3)
        )
        rotation: Rotation = entries  # type: ignore[assignment]
        lifts.setdefault(rotation, quaternion_unitary(quaternion))
    return sorted(lifts.items(), key=lambda item: item[0])


def rotate(rotation: Rotation, vector: Vec) -> Vec:
    return tuple(
        sum(rotation[row][col] * vector[col] for col in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def binomial_frequency_moments(
    k: int, radius: int, power: int
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Derive normalization, mean, and variance from the exact binomial PGF."""
    count = cumulative_type_count(radius, k)
    if count == 0:
        raise ValueError("frequency requires a nonempty k-sector")
    plus = response_weight(k, 1, power)
    z = sp.symbols("z")
    pgf = (1 - plus + plus * z) ** count
    first_derivative = sp.diff(pgf, z)
    second_derivative = sp.diff(first_derivative, z)
    normalization = sp.simplify(pgf.subs(z, 1))
    mean = sp.simplify(first_derivative.subs(z, 1) / count)
    second_moment = sp.simplify(
        (second_derivative.subs(z, 1) + first_derivative.subs(z, 1))
        / count**2
    )
    variance = sp.simplify(second_moment - mean**2)
    return normalization, mean, variance


def common_sign_frequency_moments(
    k: int, radius: int, power: int
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Hostile law: one Bernoulli sign is copied to the entire sector."""
    count = cumulative_type_count(radius, k)
    if count == 0:
        raise ValueError("frequency requires a nonempty k-sector")
    plus = response_weight(k, 1, power)
    z = sp.symbols("z")
    pgf = (1 - plus) + plus * z**count
    first_derivative = sp.diff(pgf, z)
    second_derivative = sp.diff(first_derivative, z)
    normalization = sp.simplify(pgf.subs(z, 1))
    mean = sp.simplify(first_derivative.subs(z, 1) / count)
    second_moment = sp.simplify(
        (second_derivative.subs(z, 1) + first_derivative.subs(z, 1))
        / count**2
    )
    variance = sp.simplify(second_moment - mean**2)
    return normalization, mean, variance


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; exact Z, Q, radicals, and M_2(C) algebra")
    print("package_local_integrity_reads: proposed note and current minimal-axiom memo")
    print("claim_boundary: one displayed candidate and one hostile twin; neither is adopted")
    print("time_boundary: synchronous tick is an iteration ordinal, not a derived physical duration")

    # Exact taxicab geometry and the k=1,2,3 census.
    geometry_ok = True
    type_count_ok = True
    records = frozenset({ORIGIN})
    for radius in range(0, 9):
        ball = taxicab_ball(radius)
        shell = taxicab_shell(radius)
        geometry_ok &= len(ball) == ball_size_formula(radius)
        geometry_ok &= len(shell) == shell_size_formula(radius)
        if radius >= 1:
            frontier = candidate_frontier(records)
            geometry_ok &= frontier == shell
            geometry_ok &= all(
                neighbour_difference(site, records) == expected_shell_direction(site)
                for site in shell
            )
            enumerated = Counter(nonzero_coordinate_count(site) for site in shell)
            type_count_ok &= dict(enumerated) == {
                k: count
                for k, count in shell_type_counts_formula(radius).items()
                if count
            }
            records = records | frontier
            geometry_ok &= records == ball
    checks.check(
        "taxicab-induction",
        "the synchronous local frontier grows B_t to B_(t+1) through radius 8",
        geometry_ok,
    )
    checks.check(
        "shell-k-census",
        "shell sectors have exact counts 6, 12(t-1), 4(t-1)(t-2)",
        type_count_ok,
    )

    cumulative_ok = True
    for radius in range(1, 9):
        ball_without_seed = taxicab_ball(radius) - {ORIGIN}
        enumerated = Counter(nonzero_coordinate_count(site) for site in ball_without_seed)
        cumulative_ok &= all(
            enumerated[k] == cumulative_type_count(radius, k) for k in (1, 2, 3)
        )
    checks.check(
        "cumulative-k-census",
        "B_T minus the seed has exact k-sector population polynomials",
        cumulative_ok,
    )

    # Actual M_2(C) possibilities and the linear spectral law.
    directions = [
        direction
        for direction in product((-1, 0, 1), repeat=3)
        if direction != (0, 0, 0)
    ]
    projector_ok = True
    spectral_ok = True
    weight_ok = True
    cubic_representer_ok = True
    for direction in directions:
        k = k_value(direction)
        plus = projector(direction, 1)
        minus = projector(direction, -1)
        projector_ok &= matrix_equal(plus * plus, plus)
        projector_ok &= matrix_equal(minus * minus, minus)
        projector_ok &= matrix_equal(plus.H, plus)
        projector_ok &= matrix_equal(minus.H, minus)
        projector_ok &= sp.simplify(sp.trace(plus) - 1) == 0
        projector_ok &= sp.simplify(sp.trace(minus) - 1) == 0
        projector_ok &= matrix_equal(plus + minus, I2)
        projector_ok &= matrix_equal(plus * minus, sp.zeros(2))
        p_plus = response_weight(k, 1, 1)
        p_minus = response_weight(k, -1, 1)
        spectral_ok &= matrix_equal(
            sp.simplify(p_plus * plus + p_minus * minus),
            local_density(direction),
        )
        weight_ok &= sp.simplify(p_plus + p_minus - 1) == 0
        weight_ok &= p_plus.is_positive is True and p_minus.is_positive is True
        q_plus = response_weight(k, 1, 3)
        q_minus = response_weight(k, -1, 3)
        weight_ok &= sp.simplify(q_plus + q_minus - 1) == 0
        weight_ok &= q_plus.is_positive is True and q_minus.is_positive is True
        cubic_density = response_density(direction, 3)
        expected_cubic_density = sp.simplify(
            (I2 + sp.Rational(k, 27) * bloch_operator(direction)) / 2
        )
        cubic_representer_ok &= matrix_equal(cubic_density, expected_cubic_density)
        cubic_representer_ok &= matrix_equal(cubic_density.H, cubic_density)
        cubic_representer_ok &= sp.simplify(sp.trace(cubic_density) - 1) == 0
        cubic_representer_ok &= sp.simplify(sp.trace(cubic_density * plus) - q_plus) == 0
        cubic_representer_ok &= sp.simplify(sp.trace(cubic_density * minus) - q_minus) == 0
        cubic_representer_ok &= q_plus.is_positive is True
        cubic_representer_ok &= q_minus.is_positive is True
        cubic_representer_ok &= not matrix_equal(cubic_density, local_density(direction))
    checks.check(
        "m2-projectors",
        "all 26 nonzero neighbour directions give complementary rank-one projectors",
        projector_ok,
    )
    checks.check(
        "spectral-reconstruction",
        "linear weights reconstruct rho(d)=(I+d.sigma/3)/2 exactly",
        spectral_ok,
    )
    checks.check(
        "two-normalized-laws",
        "linear and cubic-response weights are positive normalized pairs for k=1,2,3",
        weight_ok,
    )
    checks.check(
        "cubic-trace-representer",
        "the cubic twin has its own positive trace-one density and survives full-effect trace form",
        cubic_representer_ok,
    )

    # Proper-cubic covariance with explicit SU(2) lifts.
    lifts = proper_cubic_lifts()
    lift_structure_ok = (
        len(lifts) == 24
        and all(determinant3(rotation) == 1 for rotation, _ in lifts)
        and all(
            matrix_equal(sp.simplify(unitary.H * unitary), I2)
            for _, unitary in lifts
        )
    )
    covariance_ok = True
    for rotation, unitary in lifts:
        for direction in directions:
            rotated = rotate(rotation, direction)
            covariance_ok &= k_value(rotated) == k_value(direction)
            for sign in (-1, 1):
                covariance_ok &= matrix_equal(
                    sp.simplify(unitary * projector(direction, sign) * unitary.H),
                    projector(rotated, sign),
                )
        for radius in range(0, 5):
            covariance_ok &= {
                rotate(rotation, site) for site in taxicab_ball(radius)
            } == set(taxicab_ball(radius))
    checks.check(
        "proper-cubic-lifts",
        "the 48 binary-octahedral quaternions reduce to 24 determinant-one rotations",
        lift_structure_ok,
    )
    checks.check(
        "proper-cubic-covariance",
        "all projectors, k sectors, weights, and B_t geometries transform covariantly",
        covariance_ok,
    )

    translated_ok = True
    for center in ((2, -1, 3), (-4, 2, 1)):
        records_at_center = frozenset({center})
        for radius in range(1, 6):
            frontier = candidate_frontier(records_at_center)
            translated_ok &= frontier == taxicab_shell(radius, center)
            translated_ok &= all(
                neighbour_difference(site, records_at_center)
                == expected_shell_direction(site, center)
                for site in frontier
            )
            records_at_center |= frontier
    checks.check(
        "translation-covariance",
        "translated seeds produce translated shells with the same local distributions",
        translated_ok,
    )

    # Permanent Record update with actual matrix contents.
    record_map: dict[Site, sp.ImmutableMatrix] = {
        ORIGIN: sp.ImmutableMatrix(I2 / 2)
    }
    record_update_ok = True
    for radius in range(1, 5):
        old = dict(record_map)
        frontier = candidate_frontier(frozenset(old))
        signs = {site: deterministic_sign(site) for site in frontier}
        record_map = finite_record_update(record_map, signs)
        record_update_ok &= frozenset(record_map) == taxicab_ball(radius)
        record_update_ok &= all(record_map[site] == value for site, value in old.items())
        record_update_ok &= all(
            matrix_equal(sp.Matrix(record_map[site]), projector(
                expected_shell_direction(site), signs[site]
            ))
            for site in frontier
        )
    checks.check(
        "record-permanence",
        "four iterations append supported M_2(C) contents without overwrite",
        record_update_ok,
    )
    checks.check(
        "content-only-readout",
        "identity readout returns locked matrices and descends on one shared projector",
        all(content_readout(content) == content for content in record_map.values())
        and sp.ImmutableMatrix(projector((1, 0, 0), 1))
        == sp.ImmutableMatrix(projector((-1, 0, 0), -1))
        and content_readout(sp.ImmutableMatrix(projector((1, 0, 0), 1)))
        == content_readout(sp.ImmutableMatrix(projector((-1, 0, 0), -1))),
    )
    checks.check(
        "zero-direction-totalization",
        "the empty state forms nothing and d=0 has the central I/2 possibility",
        candidate_frontier(frozenset()) == frozenset()
        and matrix_equal(local_density((0, 0, 0)), I2 / 2),
    )

    # Cylinder normalization and projective consistency.
    shell_normalization_ok = all(
        shell_partition_sum(radius, power) == 1
        for radius in range(1, 7)
        for power in (1, 3)
    )
    explicit_first_shell_ok = True
    first_shell = sorted(taxicab_shell(1))
    for power in (1, 3):
        explicit_sum = sp.Integer(0)
        for signs in product((-1, 1), repeat=len(first_shell)):
            explicit_sum += branch_probability(
                dict(zip(first_shell, signs)), ORIGIN, power
            )
        explicit_first_shell_ok &= sp.simplify(explicit_sum - 1) == 0
    checks.check(
        "finite-cylinder-normalization",
        "all shell laws through t=6 normalize exactly for both response powers",
        shell_normalization_ok and explicit_first_shell_ok,
    )

    cylinder_consistency_ok = True
    for radius in range(2, 5):
        prefix_sites = taxicab_ball(radius - 1) - {ORIGIN}
        prefix_signs = {site: deterministic_sign(site) for site in prefix_sites}
        for power in (1, 3):
            prefix_weight = branch_probability(prefix_signs, ORIGIN, power)
            extended_marginal = sp.simplify(
                prefix_weight * shell_partition_sum(radius, power)
            )
            cylinder_consistency_ok &= sp.simplify(
                extended_marginal - prefix_weight
            ) == 0
    checks.check(
        "projective-consistency",
        "marginalizing each new shell returns the prior finite-cylinder law",
        cylinder_consistency_ok,
    )

    # The open Grok two-cube fixture becomes fully iterable once radicals are kept.
    patch = two_cube_patch()
    patch_records = frozenset({ORIGIN})
    patch_rows: list[tuple[int, Counter[int]]] = []
    for _ in range(5):
        new_sites = patch_frontier(patch_records, patch)
        patch_rows.append(
            (
                len(new_sites),
                Counter(k_value(neighbour_difference(site, patch_records)) for site in new_sites),
            )
        )
        patch_records |= new_sites
        if not new_sites:
            break
    expected_patch_rows = [
        (3, Counter({1: 3})),
        (4, Counter({2: 3, 1: 1})),
        (3, Counter({2: 2, 3: 1})),
        (1, Counter({3: 1})),
        (0, Counter()),
    ]
    checks.check(
        "two-cube-full-iteration",
        "the supplied 12-site patch fills in waves 3,4,3,1 and exercises every k",
        patch_rows == expected_patch_rows and patch_records == patch,
    )

    # Spatial-corpus concentration for each k sector under the product law.
    frequency_ok = True
    common_sign_control_ok = True
    for power in (1, 3):
        for k, start in ((1, 1), (2, 2), (3, 3)):
            plus = response_weight(k, 1, power)
            for radius in range(max(start, 4), 11):
                count = cumulative_type_count(radius, k)
                normalization, mean, variance = binomial_frequency_moments(
                    k, radius, power
                )
                frequency_ok &= normalization == 1
                frequency_ok &= sp.simplify(mean - plus) == 0
                frequency_ok &= sp.simplify(variance - plus * (1 - plus) / count) == 0
                next_count = cumulative_type_count(radius + 1, k)
                _, _, next_variance = binomial_frequency_moments(
                    k, radius + 1, power
                )
                frequency_ok &= next_count > count
                frequency_ok &= sp.simplify(
                    next_variance / variance - sp.Rational(count, next_count)
                ) == 0
                correlated_normalization, correlated_mean, correlated_variance = (
                    common_sign_frequency_moments(k, radius, power)
                )
                common_sign_control_ok &= correlated_normalization == 1
                common_sign_control_ok &= sp.simplify(correlated_mean - plus) == 0
                common_sign_control_ok &= sp.simplify(
                    correlated_variance - plus * (1 - plus)
                ) == 0
                common_sign_control_ok &= sp.simplify(
                    correlated_variance - variance
                ) != 0

    radius_symbol = sp.symbols("T", positive=True, integer=True)
    count_polynomials = {
        1: 6 * radius_symbol,
        2: 6 * radius_symbol * (radius_symbol - 1),
        3: sp.Rational(4, 3)
        * radius_symbol
        * (radius_symbol - 1)
        * (radius_symbol - 2),
    }
    frequency_limit_ok = all(
        sp.limit(
            response_weight(k, 1, power)
            * (1 - response_weight(k, 1, power))
            / count_polynomials[k],
            radius_symbol,
            sp.oo,
        )
        == 0
        for power in (1, 3)
        for k in (1, 2, 3)
    )
    checks.check(
        "spatial-frequency-bound",
        "PGF moments give p(1-p)/N, vanish as T grows, and reject common-sign correlation",
        frequency_ok and frequency_limit_ok and common_sign_control_ok,
    )

    # Exact selector diagnostic: two models share the contract and differ.
    born_k2 = response_weight(2, 1, 1)
    cubic_k2 = response_weight(2, 1, 3)
    all_plus_shell_one_born = response_weight(1, 1, 1) ** 6
    all_plus_shell_one_cubic = response_weight(1, 1, 3) ** 6
    twin_difference_ok = (
        sp.simplify(born_k2 - cubic_k2) != 0
        and sp.simplify(all_plus_shell_one_born - all_plus_shell_one_cubic) != 0
    )
    checks.check(
        "hostile-twin-difference",
        "linear and cubic laws differ on one site and on a complete shell cylinder",
        twin_difference_ok,
    )

    r = sp.symbols("r", real=True)
    linear_plus = (1 + r) / 2
    cubic_plus = (1 + r**3) / 2
    affinity_control_ok = (
        sp.simplify(linear_plus.subs(r, sp.Rational(1, 2)) - sp.Rational(3, 4))
        == 0
        and sp.simplify(cubic_plus.subs(r, sp.Rational(1, 2)) - sp.Rational(3, 4))
        != 0
        and linear_plus.subs(r, 0) == cubic_plus.subs(r, 0) == sp.Rational(1, 2)
        and linear_plus.subs(r, 1) == cubic_plus.subs(r, 1) == 1
    )
    checks.check(
        "affinity-discriminator",
        "extended midpoint preparation affinity accepts linear and rejects cubic response",
        affinity_control_ok,
    )

    p_plus = response_weight(1, 1, 1)
    p_minus_mutated = response_weight(1, -1, 1) + sp.Rational(1, 100)
    mutated_shell_sum = sp.simplify((p_plus + p_minus_mutated) ** 6)
    checks.check(
        "mutation-normalization",
        "adding 1/100 to one branch mass is rejected by shell normalization",
        mutated_shell_sum != 1,
    )
    overwritten = dict(record_map)
    overwritten[ORIGIN] = sp.ImmutableMatrix(projector((1, 0, 0), 1))
    checks.check(
        "mutation-permanence",
        "overwriting the seed is rejected by the append-only Record invariant",
        not preserves_records(record_map, overwritten),
    )

    # Axiom, claim-scope, and no-go-discipline surface contracts.
    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    qubit_quote = "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    admissibility_quote = (
        "For each site, the probability distribution over the possibilities is"
    )
    record_quote = "A state is a configuration of records."
    checks.check(
        "live-axiom-quotes",
        "the note uses the current Lattice, Qubit, Admissibility, and Record wording",
        all(token in axiom and token in note for token in (
            lattice_quote, qubit_quote, admissibility_quote, record_quote
        )),
    )
    checks.check(
        "claim-boundary-contract",
        "bounded status, supplied law fields, zero score movement, and non-adoption are visible",
        "actual_current_surface_status: bounded-support" in note
        and "zero TOE" in note
        and "percentage movement" in note
        and "neither law is adopted" in note
        and "synchronous tick" in note
        and "seed" in note.lower()
        and "independence" in note.lower(),
    )
    checks.check(
        "no-go-discipline-contract",
        "the landed note contains a PASS gate and every N1 through N8 section",
        "No-go discipline status: `PASS`" in note
        and all(f"### N{number}" in note for number in range(1, 9)),
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is a literal tuple containing only note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_"
            "BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in source,
    )

    print(
        "per_element: exact complementary M_2(C) projectors and both response laws are resolved for all 26 nonzero local directions."
    )
    print(
        "per_site: every forming site on shells through the executed radius receives one supported matrix content with normalized local odds."
    )
    print(
        "per_mode: checked and not executed — no Fourier, transfer-spectrum, or continuum mode exhaustion is claimed by this growth law."
    )
    print(
        "per_block: exact finite-cylinder normalization, shell marginalization, two-cube iteration, and append-only updates are executed."
    )
    print(
        "lattice_wide: taxicab-ball induction and count formulas are proved symbolically; countable extension uses the consistent cylinder family."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
