#!/usr/bin/env python3
"""Exact finite constructors for corrected released-7359 Blocks 180--183.

Only two reviewed suppliers are imported.  The released-7332/7334 fixture
reconstructs the sparse constant-carrier actions used by Block 180.  Current
Block 128 supplies the 8-by-4 cover, chart differentials, curved Hodge matrix,
and antiperiodic quotient used by Blocks 181--183.  Historical theorem text,
status, exercise conclusions, and the original 55-module runtime chain are not
imported or accepted here.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10 as finite
import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128


ROOT = Path(__file__).resolve().parents[1]
R = sp.Rational
I = sp.I
ZERO = sp.Integer(0)
ONE = sp.Integer(1)

SUPPLIER_SHA256 = {
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py":
        "594e7032f453fec4c6791067a147d1544636ddce9567a87a3449352b5546d5f5",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py":
        "8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py":
        "4299d645f687bec12d945598cca1df5c13a73c871a9e6ad1459e7e6b17c5bab5",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py":
        "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
}


def file_sha256(relative_path: str) -> str | None:
    path = ROOT / relative_path
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_hashes(expected: dict[str, str]) -> tuple[bool, dict[str, str | None]]:
    actual = {path: file_sha256(path) for path in expected}
    return actual == expected, actual


def supplier_certificate() -> tuple[bool, dict[str, str | None]]:
    hashes_ok, actual = verify_hashes(SUPPLIER_SHA256)
    return bool(hashes_ok and finite.supplier_certificate()), actual


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(sp.expand(entry)) == 0 for entry in sp.Matrix(matrix))


def residual_count(matrix: sp.MatrixBase) -> int:
    return sum(sp.simplify(sp.expand(entry)) != 0 for entry in sp.Matrix(matrix))


def no_float(value: object) -> bool:
    if isinstance(value, dict):
        return all(no_float(key) and no_float(item) for key, item in value.items())
    if isinstance(value, (tuple, list, set, frozenset)):
        return all(no_float(item) for item in value)
    try:
        return not bool(sp.sympify(value).atoms(sp.Float))
    except (TypeError, AttributeError, sp.SympifyError):
        return True


@dataclass
class Checks:
    results: list[tuple[str, bool, str]]

    def __init__(self) -> None:
        self.results = []

    def add(self, name: str, condition: object, detail: str) -> None:
        self.results.append((name, bool(condition), detail))

    def emit(self) -> int:
        for name, ok, detail in self.results:
            print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        passed = sum(ok for _, ok, _ in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return 0 if failed == 0 else 1


# ---------------------------------------------------------------------------
# Block 180: constant-carrier orientation fixtures and record slice.
# ---------------------------------------------------------------------------
FRAME_SX = R(3, 5)
FRAME_ST = R(1, 4)
MEASURE_SX = R(3, 5)
MEASURE_ST = ZERO
CONST_VOLUME = R(7, 5)
CARRIER_SIGMA = R(3, 5)
SECTOR_A = R(43, 35)
SECTOR_D = R(129, 175)
WITT_ENTRY = R(875, 1462)
J2 = sp.Matrix([[0, 1], [-1, 0]])
OMEGA = (-ONE + sp.sqrt(3) * I) / 2


def orientation_action(tag: str, cover_t: int, lx: int, sx, st):
    """Rebuild one historical constant-carrier quotient action exactly."""
    bench = finite.Bench(tag, cover_t, lx)
    pinned = {(bench.c - 1) % bench.T, bench.c % bench.T}
    field = {
        (time, space): (
            ZERO if time in pinned else CARRIER_SIGMA,
            CONST_VOLUME,
        )
        for time, space in bench.fx.CELLS
    }
    substitution = finite.finite.carrier_substitution(bench.fx, field)
    substitution[finite.SX] = sp.sympify(sx)
    substitution[finite.ST] = sp.sympify(st)
    substitution[finite.MASS] = ONE
    return bench, sp.expand(bench.Q.subs(substitution))


def staggered_grading(time_extent: int, space_extent: int) -> sp.Matrix:
    return sp.diag(*[
        sp.Integer(-1) ** (time + space)
        for time in range(time_extent)
        for space in range(space_extent)
    ])


def orientation_sector(bench, action: sp.MatrixBase) -> dict[str, object]:
    """The four supplied Fourier lines and their exact covariance restriction."""
    action = sp.Matrix(action)
    dimension = bench.N
    space_extent = bench.lx
    time_extent = bench.T

    def site(time: int, space: int) -> int:
        return space_extent * (time % time_extent) + (space % space_extent)

    def character(momentum: int, time: int, parity: int) -> sp.Matrix:
        vector = sp.zeros(dimension, 1)
        for index in range(3):
            vector[site(time, parity + 2 * index), 0] = (
                OMEGA ** ((-momentum * index) % 3) / sp.sqrt(3)
            )
        return vector

    b1 = character(1, 1, 0).row_join(character(1, 1, 1))
    b2 = character(2, 1, 0).row_join(character(2, 1, 1))
    up = sp.Matrix([1, I]) / sp.sqrt(2)
    down = sp.Matrix([1, -I]) / sp.sqrt(2)
    lines = {
        "g+": b1 * up,
        "g-": b1 * down,
        "h+": b2 * up,
        "h-": b2 * down,
    }
    lam_plus = SECTOR_A + I * SECTOR_D
    lam_minus = SECTOR_A - I * SECTOR_D

    def theta(vector: sp.MatrixBase) -> sp.Matrix:
        return sp.expand(bench.r * sp.Matrix(vector).conjugate())

    slice_rows = [site(1, x) for x in range(space_extent)]
    complement = [index for index in range(dimension) if index not in slice_rows]
    slice_block = action.extract(slice_rows, slice_rows)
    rest_block = action.extract(complement, complement)
    slice_inverse = slice_block.inv(method="LU")
    rest_inverse = rest_block.inv(method="LU")
    covariance = sp.zeros(dimension, dimension)
    for local_row, row in enumerate(slice_rows):
        for local_col, column in enumerate(slice_rows):
            covariance[row, column] = slice_inverse[local_row, local_col]
    for local_row, row in enumerate(complement):
        for local_col, column in enumerate(complement):
            covariance[row, column] = rest_inverse[local_row, local_col]
    weight = sp.expand((covariance + covariance.T) / 2)
    return {
        "site": site,
        "character": character,
        "B1": b1,
        "B2": b2,
        "lines": lines,
        "order": ("g+", "g-", "h+", "h-"),
        "lambdas": (lam_plus, lam_minus),
        "theta": theta,
        "reflection": bench.r,
        "slice_rows": slice_rows,
        "complement": complement,
        "slice_block": slice_block,
        "rest_block": rest_block,
        "disconnected": all(
            action[row, column] == 0 and action[column, row] == 0
            for row in slice_rows for column in complement
        ),
        "covariance": sp.expand(covariance),
        "weight": weight,
    }


def witt_forms(sector: dict[str, object]) -> tuple[sp.Matrix, sp.Matrix]:
    order = sector["order"]
    lines = [sector["lines"][name] for name in order]
    weight = sector["weight"]
    theta = sector["theta"]
    plain = sp.Matrix(4, 4, lambda row, column: sp.simplify(
        (lines[row].H * weight * lines[column])[0]
    ))
    reflected = sp.Matrix(4, 4, lambda row, column: sp.simplify(
        (theta(lines[row]).H * weight * lines[column])[0]
    ))
    return plain, reflected


# ---------------------------------------------------------------------------
# Blocks 181--183: current Block-128 finite carrier.
# ---------------------------------------------------------------------------
ORIGINS = ((0, 0), (0, 1), (1, 0), (1, 1))
SPACE_EXTENT = b128.SPACE_EXTENT
PHYSICAL_TIME = b128.PHYSICAL_TIME_EXTENT
COVER_TIME = b128.COVER_TIME_EXTENT
COVER_SIZE = COVER_TIME * SPACE_EXTENT
MASS = b128.MASS


def cover_shift(dt: int, dx: int) -> sp.Matrix:
    shift = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(COVER_TIME):
        for space in range(SPACE_EXTENT):
            shift[
                b128.cover_index(time + dt, space + dx),
                b128.cover_index(time, space),
            ] = ONE
    return shift


def quotient_shift(
    dimension: int,
    time_extent: int,
    dt: int,
    dx: int,
    temporal_wrap: int,
    spatial_wrap: int = 1,
) -> sp.Matrix:
    shift = sp.zeros(dimension, dimension)
    for time in range(time_extent):
        for space in range(SPACE_EXTENT):
            next_time = time + dt
            next_space = space + dx
            sign = temporal_wrap if not 0 <= next_time < time_extent else 1
            sign *= spatial_wrap if not 0 <= next_space < SPACE_EXTENT else 1
            shift[
                (next_time % time_extent) * SPACE_EXTENT + next_space % SPACE_EXTENT,
                time * SPACE_EXTENT + space,
            ] = sign
    return shift


def completion(hodge: sp.MatrixBase, differential: sp.MatrixBase, mass=MASS) -> sp.Matrix:
    hodge = sp.Matrix(hodge)
    differential = sp.Matrix(differential)
    return sp.expand(mass * hodge + I * (hodge * differential + differential.H * hodge))


def flat_hodge_cover() -> sp.Matrix:
    flat = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(COVER_TIME):
        for space in range(SPACE_EXTENT):
            embedding = b128.cover_embedding(time, space)
            flat += (
                embedding
                * b128.block105.shear_hodge(ZERO, ONE)
                * embedding.T
                / 4
            )
    return sp.expand(flat)


def section_data() -> dict[str, object]:
    temporal = cover_shift(1, 0)
    spatial = cover_shift(0, 1)
    shifts = {
        (0, 0): sp.eye(COVER_SIZE),
        (0, 1): spatial,
        (1, 0): temporal,
        (1, 1): sp.expand(temporal * spatial),
    }
    differentials = {
        origin: sp.Matrix(b128.chart_differential_cover(origin))
        for origin in ORIGINS
    }
    hodge = sp.Matrix(b128.curved_hodge_cover())
    section_hodge = sp.expand(sum(
        (shifts[origin].T * hodge * shifts[origin] for origin in ORIGINS),
        sp.zeros(COVER_SIZE, COVER_SIZE),
    ) / 4)
    quotient_differentials = {
        origin: sp.Matrix(b128.antiperiodic_quotient(differentials[origin]))
        for origin in ORIGINS
    }
    quotient_dimension = quotient_differentials[(0, 0)].rows
    quotient_time = quotient_dimension // SPACE_EXTENT
    quotient_shifts = {
        (0, 1): quotient_shift(quotient_dimension, quotient_time, 0, 1, 1),
        (1, 0): quotient_shift(quotient_dimension, quotient_time, 1, 0, -1),
    }
    quotient_shifts[(1, 1)] = sp.expand(
        quotient_shifts[(1, 0)] * quotient_shifts[(0, 1)]
    )
    return {
        "Ut": temporal,
        "Ux": spatial,
        "S": shifts,
        "D": differentials,
        "H": hodge,
        "Hs": section_hodge,
        "DQ": quotient_differentials,
        "SQ": quotient_shifts,
        "quotient_dimension": quotient_dimension,
        "quotient_time": quotient_time,
    }


def exterior_grade(time_extent: int) -> sp.Matrix:
    return sp.diag(*[
        sp.Integer((time % 2) + (space % 2))
        for time in range(time_extent)
        for space in range(SPACE_EXTENT)
    ])


def sign_field(time_extent: int) -> sp.Matrix:
    return sp.diag(*[
        sp.Integer(-1) ** space
        for _time in range(time_extent)
        for space in range(SPACE_EXTENT)
    ])


def hodge_cover(field: dict, block=None) -> sp.Matrix:
    block = b128.block105.shear_hodge if block is None else block
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(COVER_TIME):
        for space in range(SPACE_EXTENT):
            shear, volume = field[(time % PHYSICAL_TIME, space)]
            embedding = b128.cover_embedding(time, space)
            result += embedding * block(shear, volume) * embedding.T / 4
    return sp.expand(result)


def shifted_field(field: dict, dt: int, dx: int) -> dict:
    return {
        (time, space): field[
            ((time - dt) % PHYSICAL_TIME, (space - dx) % SPACE_EXTENT)
        ]
        for time in range(PHYSICAL_TIME)
        for space in range(SPACE_EXTENT)
    }


def flipped_field(field: dict) -> dict:
    return {site: (-shear, volume) for site, (shear, volume) in field.items()}


def periodic_fine_differential() -> sp.Matrix:
    """The historical 4-by-4 periodic exterior derivative, reconstructed."""
    time_extent = PHYSICAL_TIME
    dimension = time_extent * SPACE_EXTENT
    temporal = quotient_shift(dimension, time_extent, 1, 0, 1)
    spatial = quotient_shift(dimension, time_extent, 0, 1, 1)
    eta_x = sp.diag(*[
        sp.Integer(-1) ** time
        for time in range(time_extent)
        for _space in range(SPACE_EXTENT)
    ])
    kernel = (temporal.T - temporal) / 2 + eta_x * (spatial.T - spatial) / 2
    grade = exterior_grade(time_extent)
    projectors = tuple(sp.diag(*[
        sp.Integer(grade[index, index] == degree)
        for index in range(dimension)
    ]) for degree in range(3))
    raising = projectors[1] * kernel * projectors[0] + projectors[2] * kernel * projectors[1]
    return sp.expand(-I * raising)


# ---------------------------------------------------------------------------
# Block 183: convention-conditioned reflection, duality, and averages.
# ---------------------------------------------------------------------------
CELL_MAP = sp.Matrix([
    [0, 0, -1, 0],
    [0, 0, 0, -1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
])
UNDRESSED_CELL_MAP = sp.Matrix([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
])


def edge_reflection() -> sp.Matrix:
    matrix = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(COVER_TIME):
        for space in range(SPACE_EXTENT):
            matrix[
                b128.cover_index(COVER_TIME - 1 - time, space),
                b128.cover_index(time, space),
            ] = ONE
    return matrix


def time_parity() -> sp.Matrix:
    return sp.diag(*[
        sp.Integer(-1) ** (time % 2)
        for time in range(COVER_TIME)
        for _space in range(SPACE_EXTENT)
    ])


def space_parity() -> sp.Matrix:
    return sp.diag(*[
        sp.Integer(-1) ** space
        for _time in range(COVER_TIME)
        for space in range(SPACE_EXTENT)
    ])


def grade_jump_census(operator: sp.MatrixBase, grade: sp.MatrixBase) -> dict[int, int]:
    operator = sp.Matrix(operator)
    grade = sp.Matrix(grade)
    census: dict[int, int] = {}
    for row in range(operator.rows):
        for column in range(operator.cols):
            if operator[row, column] != 0:
                jump = int(grade[row, row] - grade[column, column])
                census[jump] = census.get(jump, 0) + 1
    return census


def shear_block(shear, volume) -> sp.Matrix:
    return sp.Matrix(b128.block105.shear_hodge(shear, volume))


def dual_block(shear, volume) -> sp.Matrix:
    return sp.expand(CELL_MAP * shear_block(shear, volume) * CELL_MAP.T)


def reflected_field(field: dict) -> dict:
    return {
        (time, space): field[((2 - time) % PHYSICAL_TIME, space)]
        for time in range(PHYSICAL_TIME)
        for space in range(SPACE_EXTENT)
    }


def orbit_average(matrix: sp.MatrixBase, shifts: tuple[sp.Matrix, ...]) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    return sp.expand(sum(
        (shift.T * matrix * shift for shift in shifts),
        sp.zeros(matrix.rows, matrix.cols),
    ) / len(shifts))


def reflection_orbits() -> tuple[tuple[int, ...], ...]:
    orbits: list[tuple[int, ...]] = []
    seen: set[int] = set()
    for step in range(COVER_TIME):
        if step not in seen:
            orbit = tuple(sorted({step, (-step) % COVER_TIME}))
            orbits.append(orbit)
            seen.update(orbit)
    return tuple(orbits)


def equal_weight_reflection_sets() -> tuple[tuple[int, ...], ...]:
    orbits = reflection_orbits()
    others = tuple(orbit for orbit in orbits if 0 not in orbit)
    result = []
    for size in range(len(others) + 1):
        for choice in combinations(others, size):
            result.append(tuple(sorted({0} | {
                step for orbit in choice for step in orbit
            })))
    return tuple(result)


def shift_set(exponents: tuple[int, ...]) -> tuple[sp.Matrix, ...]:
    temporal = cover_shift(1, 0)
    spatial = cover_shift(0, 1)
    return tuple(
        sp.expand(temporal ** step * spatial ** offset)
        for step in exponents
        for offset in range(2)
    )


def weighted_temporal_average(matrix: sp.MatrixBase, weights: dict[int, object]) -> sp.Matrix:
    """Average over supplied temporal weights and the two spatial offsets."""
    matrix = sp.Matrix(matrix)
    temporal = cover_shift(1, 0)
    spatial = cover_shift(0, 1)
    total = sp.zeros(matrix.rows, matrix.cols)
    for step, raw_weight in weights.items():
        weight = sp.sympify(raw_weight)
        for offset in range(2):
            shift = sp.expand(temporal ** step * spatial ** offset)
            total += weight * shift.T * matrix * shift / 2
    return sp.expand(total)
