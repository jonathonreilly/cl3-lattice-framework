#!/usr/bin/env python3
"""Minimal supplied fixtures for the released Block 213→214 recovery.

The functions below are explicit finite algebraic definitions needed by the
two recovered runners.  Their historical formula provenance is recorded by
blob and SHA-256, but no theorem, authority gate, physical interpretation, or
parent-branch status is inherited from those sources.

Historical definition sources at PR 7981 head
851aff9b3f950e5f08b0bd0878df2e1992bbe15b:

* Block 201 lane construction:
  blob ffbb8fd19247f8938261a868783e86d302ec8aea,
  SHA-256 0a97bedd5e26d6e6d4faca6cc863d3598bfbbbbccc9f1912870553639d02db57.
* Block 211 cell family:
  blob 5ad74997bb99388ab4503598c6f1b977d80ccc6c,
  SHA-256 cb98a75aa02a76ad18507ca9def4b3afecb47fb8e1f2601c8e2cfa3db21e76f2.
* Block 209 exterior-corner machinery:
  blob af2672f13ba633bac9bcaabb393548e2d16a8915,
  SHA-256 fixed in the recovery bundle.
* Historical Block 105 Hodge formula:
  blob 4870f31b5880028ad4f1f3095aad4d0820e4668f,
  SHA-256 1159d796d71fc5b258b0c4123d3adf00d8b03ac1168d20f4cd5b66f5727720d9.

The live Block 105 source is separately imported and bound by Block 213.
"""

from __future__ import annotations

from types import SimpleNamespace

import sympy as sp


def residual_count(matrix: sp.MatrixBase) -> int:
    matrix = sp.Matrix(matrix).applyfunc(sp.expand)
    return sum(
        matrix[row, column] != 0
        for row in range(matrix.rows)
        for column in range(matrix.cols)
    )


def shear_hodge(shear, volume) -> sp.Matrix:
    """Return the explicitly supplied four-corner shear matrix."""
    metric = sp.Matrix([[1, shear], [shear, 1]])
    return sp.diag(volume, volume * metric.inv(), 1 / volume)


# Block 209 subset: lexicographic exterior corners and a Clifford shadow.
CORNERS = tuple(
    (dt, dx, dy) for dt in (0, 1) for dx in (0, 1) for dy in (0, 1)
)
CELL = sp.Matrix(
    8,
    8,
    lambda row, column: sp.Symbol(
        f"D{min(row, column)}{max(row, column)}"
    ),
)
CELL_SYMBOLS = tuple(
    sorted(
        {CELL[row, column] for row in range(8) for column in range(8)},
        key=str,
    )
)
CORNER_DEGREE = tuple(sum(corner) for corner in CORNERS)
DEGREE_INDICES = tuple(
    tuple(index for index in range(8) if CORNER_DEGREE[index] == degree)
    for degree in range(4)
)
PLANE_FRAMES = (
    ((1, 0, 0), (0, 1, 0), (0, 0, 1), "tx"),
    ((1, 0, 0), (0, 0, 1), (0, 1, 0), "ty"),
    ((0, 1, 0), (0, 0, 1), (1, 0, 0), "xy"),
)


def kron(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(sp.kronecker_product(left, right))


SIGMA_X = sp.Matrix([[0, 1], [1, 0]])
SIGMA_Z = sp.Matrix([[1, 0], [0, -1]])
IDENTITY_2 = sp.eye(2)
IDENTITY_4 = sp.eye(4)
CLIFFORD_GENERATORS = (
    kron(SIGMA_X, IDENTITY_2),
    kron(SIGMA_Z, SIGMA_X),
    kron(SIGMA_Z, SIGMA_Z),
)


def omega(site: tuple[int, ...]) -> sp.Matrix:
    result = IDENTITY_4
    for index, coordinate in enumerate(site):
        if coordinate % 2:
            result = result * CLIFFORD_GENERATORS[index]
    return sp.Matrix(sp.expand(result))


b209 = SimpleNamespace(
    CORNERS=CORNERS,
    CELL=CELL,
    CELL_SYMBOLS=CELL_SYMBOLS,
    DEGREE_INDICES=DEGREE_INDICES,
    PLANE_FRAMES=PLANE_FRAMES,
    GENERATORS=CLIFFORD_GENERATORS,
    omega=omega,
)


# Block 201 subset: a direct eta-staggered lane construction and one fork.
UNIT_VOLUME = sp.Integer(1)
FORK_EXTENT = (8, 4)
FORK_SHEAR = sp.Rational(5, 13)
CELL_CORNERS = ((0, 0), (0, 1), (1, 0), (1, 1))
SX = sp.Matrix([[0, 1], [1, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
A_COUPLING = SX
B_COUPLING = -SZ
OFFSET_PERMUTATION = sp.Matrix(
    [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
)


def staggering(time: int, space: int) -> sp.Matrix:
    return (SX ** (time % 2)) * (SZ ** (space % 2))


def covariant_kernel(width: int, extent: int, twist: tuple[int, int]) -> tuple:
    size = width * extent

    def index(time: int, space: int) -> int:
        return (time % width) * extent + space % extent

    kernel = sp.zeros(2 * size, 2 * size)

    def place(first: int, second: int, block: sp.MatrixBase) -> None:
        for row in range(2):
            for column in range(2):
                kernel[2 * first + row, 2 * second + column] += block[row, column]

    for time in range(width):
        for space in range(extent):
            temporal = twist[0] if time == width - 1 else 1
            spatial = twist[1] if space == extent - 1 else 1
            place(
                index(time, space),
                index(time + 1, space),
                temporal * A_COUPLING / 2,
            )
            place(
                index(time + 1, space),
                index(time, space),
                -temporal * A_COUPLING.T / 2,
            )
            place(
                index(time, space),
                index(time, space + 1),
                spatial * B_COUPLING / 2,
            )
            place(
                index(time, space + 1),
                index(time, space),
                -spatial * B_COUPLING.T / 2,
            )

    frame = sp.zeros(2 * size, 2 * size)
    for time in range(width):
        for space in range(extent):
            block = staggering(time, space)
            for row in range(2):
                for column in range(2):
                    frame[2 * index(time, space) + row, 2 * index(time, space) + column] = block[row, column]
    diagonalised = sp.expand(frame.T * kernel * frame)
    nonscalar = 0
    for first in range(size):
        for second in range(size):
            block = diagonalised[2 * first : 2 * first + 2, 2 * second : 2 * second + 2]
            if (
                sp.expand(block[0, 1]) != 0
                or sp.expand(block[1, 0]) != 0
                or sp.expand(block[0, 0] - block[1, 1]) != 0
            ):
                nonscalar += 1
    scalar = sp.Matrix(
        size, size, lambda first, second: diagonalised[2 * first, 2 * second]
    )
    return scalar, nonscalar


def lane_kernel(width: int, extent: int, convention: str) -> sp.Matrix:
    size = width * extent

    def index(time: int, space: int) -> int:
        return (time % width) * extent + space % extent

    kernel = sp.zeros(size, size)
    seam = width // 2 - 1
    for time in range(width):
        for space in range(extent):
            if convention == "wrap":
                sign = -1 if time == width - 1 else 1
            elif convention == "seam":
                sign = -1 if time == seam else 1
            else:
                sign = 1
            kernel[index(time, space), index(time + 1, space)] += sp.Rational(
                sign, 2
            )
            kernel[index(time + 1, space), index(time, space)] -= sp.Rational(
                sign, 2
            )
            stagger = -1 if time % 2 else 1
            kernel[index(time, space), index(time, space + 1)] += sp.Rational(
                stagger, 2
            )
            kernel[index(time, space + 1), index(time, space)] -= sp.Rational(
                stagger, 2
            )
    return kernel


def site_sign_equivalent(
    scalar: sp.Matrix, lane: sp.Matrix, size: int
) -> bool:
    signs = {0: 1}
    frontier = [0]
    links: dict[int, list[int]] = {}
    for first in range(size):
        for second in range(size):
            if scalar[first, second] != 0:
                links.setdefault(first, []).append(second)
    while frontier:
        first = frontier.pop()
        for second in links.get(first, []):
            if lane[first, second] == 0:
                return False
            ratio = sp.Rational(lane[first, second]) / sp.Rational(
                scalar[first, second]
            )
            if ratio not in (1, -1):
                return False
            value = signs[first] * ratio
            if second in signs:
                if signs[second] != value:
                    return False
            else:
                signs[second] = value
                frontier.append(second)
    gauge = sp.diag(*[signs.get(index, 1) for index in range(size)])
    return residual_count(gauge * scalar * gauge - lane) == 0


def fork_index(time: int, space: int) -> int:
    width, extent = FORK_EXTENT
    return (time % width) * extent + space % extent


def grade_projector(grade: int) -> sp.Matrix:
    width, extent = FORK_EXTENT
    return sp.diag(
        *[
            1 if time % 2 + space % 2 == grade else 0
            for time in range(width)
            for space in range(extent)
        ]
    )


def raising_part(kernel: sp.Matrix) -> sp.Matrix:
    p0, p1, p2 = (grade_projector(grade) for grade in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def fork_embedding(time: int, space: int) -> sp.Matrix:
    width, extent = FORK_EXTENT
    matrix = sp.zeros(width * extent, 4)
    for column, (delta_t, delta_x) in enumerate(CELL_CORNERS):
        matrix[fork_index(time + delta_t, space + delta_x), column] = 1
    return matrix


def fork_hodge(shear) -> sp.Matrix:
    width, extent = FORK_EXTENT
    half = width // 2
    block = sp.expand(shear_hodge(shear, UNIT_VOLUME))
    reflected = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    result = sp.zeros(width * extent, width * extent)
    for time in range(width):
        chosen = block if time < half else reflected
        for space in range(extent):
            embedding = fork_embedding(time, space)
            result += embedding * chosen * embedding.T / 4
    return sp.expand(result)


b201 = SimpleNamespace(
    CELL_CORNERS=CELL_CORNERS,
    FORK_SHEAR=FORK_SHEAR,
    OFFSET_PERMUTATION=OFFSET_PERMUTATION,
    covariant_kernel=covariant_kernel,
    fork_hodge=fork_hodge,
    lane_kernel=lane_kernel,
    raising_part=raising_part,
    site_sign_equivalent=site_sign_equivalent,
)


# Block 211 subset: the supplied degree-block family and witness chart.
FACE_KEYS = tuple(
    (name, offset) for _, _, _, name in PLANE_FRAMES for offset in (0, 1)
)
W1_MODULI = (
    sp.Rational(15, 16),
    sp.Rational(1, 4),
    sp.Integer(1),
    sp.Rational(1, 4),
)
W2_MODULI = (
    sp.Rational(7, 16),
    sp.Rational(3, 4),
    sp.Integer(1),
    sp.Rational(3, 4),
)
W3_MODULI = (
    sp.Rational(12, 25),
    sp.Rational(3, 5),
    sp.Rational(3, 4),
    sp.Rational(4, 5),
)


def face_system(face_moduli: dict) -> tuple:
    equations = []
    for first, second, normal, name in PLANE_FRAMES:
        for offset_index in (0, 1):
            offset = tuple(offset_index * component for component in normal)
            volume, shear = face_moduli[(name, offset_index)]
            supplied = shear_hodge(shear, volume)

            def add(left: tuple, right: tuple) -> tuple:
                return tuple(
                    (left[index] + right[index]) % 2 for index in range(3)
                )

            indices = [
                CORNERS.index(offset),
                CORNERS.index(add(offset, second)),
                CORNERS.index(add(offset, first)),
                CORNERS.index(add(offset, add(first, second))),
            ]
            for row in range(4):
                for column in range(4):
                    equations.append(
                        sp.expand(
                            CELL[indices[row], indices[column]]
                            - supplied[row, column]
                        )
                    )
    matrix, right_hand_side = sp.linear_eq_to_matrix(equations, CELL_SYMBOLS)
    return equations, matrix, right_hand_side


def solve_pinned(matrix, right_hand_side, at_zero: bool = True) -> tuple:
    solution = list(sp.linsolve((matrix, right_hand_side), CELL_SYMBOLS))[0]
    free = sorted(
        {
            symbol
            for entry in solution
            for symbol in entry.free_symbols
            if str(symbol).startswith("D")
        },
        key=str,
    )
    zero = {symbol: sp.Integer(0) for symbol in free} if at_zero else {}
    solved = sp.Matrix(
        8,
        8,
        lambda row, column: sp.cancel(
            solution[
                CELL_SYMBOLS.index(CELL[min(row, column), max(row, column)])
            ].subs(zero)
        ),
    )
    return solved, free


def leading_minors(matrix: sp.MatrixBase) -> tuple:
    return tuple(matrix[:size, :size].det() for size in range(1, matrix.rows + 1))


def degree_block(matrix: sp.MatrixBase, degree: int) -> sp.Matrix:
    indices = DEGREE_INDICES[degree]
    return sp.Matrix(
        len(indices),
        len(indices),
        lambda row, column: matrix[indices[row], indices[column]],
    )


def branch_moduli(
    volume0, gamma0, volume1, gamma1, signs: dict
) -> dict:
    moduli = {}
    for name, offset in FACE_KEYS:
        volume = volume0 if offset == 0 else volume1
        gamma = gamma0 if offset == 0 else gamma1
        moduli[(name, offset)] = (volume, signs[(name, offset)] * gamma)
    return moduli


def diagonal_point(gamma) -> tuple:
    return 1 - gamma**2, gamma, sp.Integer(1), gamma


ALL_PLUS = {key: sp.Integer(1) for key in FACE_KEYS}


def flipped(*keys: tuple[str, int]) -> dict:
    signs = dict(ALL_PLUS)
    for key in keys:
        signs[key] = sp.Integer(-1)
    return signs


REPRESENTATIVES = {
    (1, 1): ALL_PLUS,
    (1, -1): flipped(("xy", 1)),
    (-1, 1): flipped(("xy", 0)),
    (-1, -1): flipped(("xy", 0), ("xy", 1)),
}


def signed_triangle(shears) -> sp.Matrix:
    first, second, third = shears
    return sp.Matrix(
        [[1, -first, -second], [-first, 1, -third], [-second, -third, 1]]
    )


CHART_T, CHART_U = sp.symbols("t u")
CHART_SHEAR_ZERO = 2 * CHART_T / (1 + CHART_T**2)
CHART_SHEAR_ONE = 2 * CHART_U / (1 + CHART_U**2)
CHART_VOLUME_ZERO = (
    (1 - CHART_T**2)
    * (1 - CHART_U**2)
    / ((1 + CHART_T**2) * (1 + CHART_U**2))
)
CHART_VOLUME_ONE = (
    (1 + CHART_T**2)
    * (1 - CHART_U**2)
    / ((1 - CHART_T**2) * (1 + CHART_U**2))
)


def chart_moduli(signs: dict) -> dict:
    moduli = {}
    for name, offset in FACE_KEYS:
        volume = CHART_VOLUME_ZERO if offset == 0 else CHART_VOLUME_ONE
        shear = (
            CHART_SHEAR_ZERO if offset == 0 else CHART_SHEAR_ONE
        ) * signs[(name, offset)]
        moduli[(name, offset)] = (volume, shear)
    return moduli


b211 = SimpleNamespace(
    ALL_PLUS=ALL_PLUS,
    CHART_T=CHART_T,
    CHART_U=CHART_U,
    LANDED_SHEAR_HODGE=shear_hodge,
    REPRESENTATIVES=REPRESENTATIVES,
    W1_MODULI=W1_MODULI,
    W2_MODULI=W2_MODULI,
    W3_MODULI=W3_MODULI,
    b209=b209,
    branch_moduli=branch_moduli,
    chart_moduli=chart_moduli,
    degree_block=degree_block,
    diagonal_point=diagonal_point,
    face_system=face_system,
    flipped=flipped,
    leading_minors=leading_minors,
    signed_triangle=signed_triangle,
    solve_pinned=solve_pinned,
)
