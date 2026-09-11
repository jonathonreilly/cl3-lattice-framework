#!/usr/bin/env python3
"""Exact finite constructors shared by corrected Blocks 184--188.

The carrier primitives are imported from the corrected current Block 128
module, which re-exports the corrected Block 105 module.  The remaining
functions are narrow extractions of the constructions actually exercised by
the five original primaries.  They are fixture definitions, not premises or
general physical laws.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128


ROOT = Path(__file__).resolve().parents[1]
R = sp.Rational
I = sp.I

TIME_EXTENT = b128.COVER_TIME_EXTENT
PHYSICAL_TIME_EXTENT = b128.PHYSICAL_TIME_EXTENT
SPACE_EXTENT = b128.SPACE_EXTENT
COVER_SIZE = TIME_EXTENT * SPACE_EXTENT

OFFSET_PERMUTATION = sp.Matrix(
    ((0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0))
)
SIGNED_CELL_MAP = sp.Matrix(
    ((0, 0, -1, 0), (0, 0, 0, -1), (1, 0, 0, 0), (0, 1, 0, 0))
)
FAR_SEAM = frozenset((3, 4))
NEAR_SEAM = frozenset((7, 0))
BOTH_SEAMS = (FAR_SEAM, NEAR_SEAM)
POSITIVE_TIMES = (0, 1, 2, 3)
FIXED_SLICES = (0, 4)
CLOSED_HALF = (0, 1, 2, 3, 4)


SOURCE_PROVENANCE = {
    "block128": {
        "path": "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
        "used": (
            "COVER_TIME_EXTENT",
            "PHYSICAL_TIME_EXTENT",
            "SPACE_EXTENT",
            "cover_index",
            "cover_embedding",
            "curved_hodge_cover",
            "chart_differential_cover",
            "antiperiodic_quotient",
        ),
        "disposition": "imported from corrected current source",
    },
    "block105": {
        "path": "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
        "used": ("shear_hodge", "overlap_field"),
        "disposition": "used through corrected current Block 128",
    },
    "blocks184_188": {
        "commits": (
            "1702e73876839f0ba01f5ff28bfe26ed5d370987",
            "4d411820f1c19b4130db8ab064a79ba8e86f0fc8",
            "f5bcab65286f03001c8d3b88ad0904afa92588a8",
            "22bc4f5406d1aff3b16d120d1e0a1951faf8b2b2",
            "094200a75208b6c8d153c1b91df32a3913729ed0",
        ),
        "disposition": "finite constructors extracted; historical claims are not imported",
    },
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, bool, str]] = []

    def add(self, key: str, condition: object, detail: str) -> None:
        self.results.append((key, bool(condition), detail))

    def emit(self) -> int:
        for key, condition, detail in self.results:
            print(f"[{'PASS' if condition else 'FAIL'}] {key}: {detail}")
        passed = sum(condition for _, condition, _ in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


def file_sha256(path: str) -> str | None:
    candidate = ROOT / path
    return hashlib.sha256(candidate.read_bytes()).hexdigest() if candidate.is_file() else None


def verify_input_hashes(expected: dict[str, str]) -> tuple[bool, dict[str, str | None]]:
    actual = {path: file_sha256(path) for path in expected}
    valid_literals = all(
        isinstance(value, str)
        and len(value) == 64
        and set(value) <= set("0123456789abcdef")
        for value in expected.values()
    )
    return valid_literals and actual == expected, actual


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(matrix[row, column] != 0 for row in range(matrix.rows) for column in range(matrix.cols))


def residual_count(matrix: sp.MatrixBase) -> int:
    return nonzero_entries(sp.expand(matrix))


def max_norm(matrix: sp.MatrixBase) -> sp.Expr:
    expanded = sp.expand(matrix)
    return max(sp.Abs(value) for value in expanded)


def leading_minors(matrix: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.expand(matrix[:size, :size].det(method="berkowitz"))
        for size in range(1, matrix.rows + 1)
    )


def minor_signs(minors: tuple[sp.Expr, ...]) -> tuple[int, ...]:
    return tuple(int(sp.sign(value)) for value in minors)


def first_failing_minor(signs: tuple[int, ...]) -> int:
    return next((index for index, value in enumerate(signs, 1) if value <= 0), 0)


def exact_real(value: object) -> bool:
    expression = sp.sympify(value)
    return not expression.atoms(sp.Float) and expression.is_real is True


def reduce_exact(expression: object) -> sp.Expr:
    return sp.radsimp(sp.expand(expression))


def reduce_matrix(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(matrix).applyfunc(reduce_exact)


def inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact inertia by symmetric congruence elimination."""
    active = reduce_matrix(matrix)
    positive = negative = null = 0
    while active.rows:
        size = active.rows
        pivot = next((i for i in range(size) if active[i, i] != 0), None)
        if pivot is None:
            pair = next(
                (
                    (i, j)
                    for i in range(size)
                    for j in range(i + 1, size)
                    if active[i, j] != 0
                ),
                None,
            )
            if pair is None:
                null += size
                break
            first, second = pair
            transform = sp.eye(size)
            transform[second, first] = 1
            active = reduce_matrix(transform.T * active * transform)
            pivot = first
        value = active[pivot, pivot]
        positive += int(value > 0)
        negative += int(value < 0)
        rest = [index for index in range(size) if index != pivot]
        active = sp.Matrix(
            len(rest),
            len(rest),
            lambda i, j: reduce_exact(
                active[rest[i], rest[j]]
                - active[rest[i], pivot] * active[pivot, rest[j]] / value
            ),
        )
    return positive, negative, null


def site_index(time_coordinate: int, space_coordinate: int) -> int:
    return (time_coordinate % TIME_EXTENT) * SPACE_EXTENT + space_coordinate % SPACE_EXTENT


def staggered_kernel(antiperiodic: bool = True) -> sp.Matrix:
    kernel = sp.zeros(COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            temporal_sign = -1 if antiperiodic and time == 3 else 1
            here = site_index(time, space)
            ahead = site_index(time + 1, space)
            kernel[here, ahead] += R(temporal_sign, 2)
            kernel[ahead, here] -= R(temporal_sign, 2)
            right = site_index(time, space + 1)
            spatial_sign = (-1) ** time
            kernel[here, right] += R(spatial_sign, 2)
            kernel[right, here] -= R(spatial_sign, 2)
    return kernel


def site_degree(time_coordinate: int, space_coordinate: int) -> int:
    return time_coordinate % 2 + space_coordinate % 2


def grade_projector(grade: int) -> sp.Matrix:
    return sp.diag(
        *[
            int(site_degree(time, space) == grade)
            for time in range(TIME_EXTENT)
            for space in range(SPACE_EXTENT)
        ]
    )


def raising_part(kernel: sp.Matrix) -> sp.Matrix:
    p0, p1, p2 = (grade_projector(grade) for grade in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def reflection_permutation(theta) -> sp.Matrix:
    matrix = sp.zeros(COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            matrix[site_index(theta(time), space), site_index(time, space)] = 1
    return matrix


def link_theta(time: int) -> int:
    return (-1 - time) % TIME_EXTENT


def site_theta(time: int) -> int:
    return (-time) % TIME_EXTENT


def link_anchor_theta(time: int) -> int:
    return (-2 - time) % TIME_EXTENT


def site_anchor_theta(time: int) -> int:
    return (-1 - time) % TIME_EXTENT


def shear_block(shear: object, volume: object = sp.Integer(1)) -> sp.Matrix:
    return sp.Matrix(b128.block105.shear_hodge(shear, volume))


def step_history(shear: object) -> tuple[sp.Expr, ...]:
    return (shear, shear, shear, sp.Integer(0), -shear, -shear, -shear, sp.Integer(0))


def completion(hodge: sp.Matrix, differential: sp.Matrix, mass: object) -> sp.Matrix:
    return sp.expand(mass * hodge + hodge * differential - differential.T * hodge)


def hodge_from_cells(cell_block) -> sp.Matrix:
    result = sp.zeros(COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            embedding = b128.cover_embedding(time, space)
            result += embedding * cell_block(time, space) * embedding.T / 4
    return sp.expand(result)


def link_image_hodge(shear: object, volume: object = sp.Integer(1)) -> sp.Matrix:
    history = step_history(shear)

    def block(time: int, _space: int) -> sp.Matrix:
        if time in POSITIVE_TIMES:
            local = history[time]
            return sp.eye(SPACE_EXTENT) if local == 0 else shear_block(local, volume)
        reflected = link_anchor_theta(time)
        local = history[reflected]
        source = sp.eye(SPACE_EXTENT) if local == 0 else shear_block(local, volume)
        return sp.expand(OFFSET_PERMUTATION * source * OFFSET_PERMUTATION.T)

    return hodge_from_cells(block)


def x_alternating_link_image_hodge(shear: object) -> sp.Matrix:
    history = step_history(shear)

    def local_block(local: object) -> sp.Matrix:
        return sp.eye(SPACE_EXTENT) if local == 0 else shear_block(local)

    def block(time: int, space: int) -> sp.Matrix:
        if time in POSITIVE_TIMES:
            return local_block(history[time] * (-1) ** space)
        reflected = link_anchor_theta(time)
        source = local_block(history[reflected] * (-1) ** space)
        return sp.expand(OFFSET_PERMUTATION * source * OFFSET_PERMUTATION.T)

    return hodge_from_cells(block)


def site_image_hodge(shear: object, flipped: bool = False) -> sp.Matrix:
    physical = shear_block(shear)
    image_source = shear_block(-shear) if flipped else physical

    def block(time: int, _space: int) -> sp.Matrix:
        if time in POSITIVE_TIMES:
            return physical
        if site_anchor_theta(time) not in POSITIVE_TIMES:
            raise AssertionError("site image anchor left the supplied half")
        return sp.expand(OFFSET_PERMUTATION * image_source * OFFSET_PERMUTATION.T)

    return hodge_from_cells(block)


def restricted_raising(raising: sp.Matrix, seams: tuple[frozenset[int], ...]) -> sp.Matrix:
    result = sp.zeros(COVER_SIZE)
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            keep = row_time in POSITIVE_TIMES and column_time in POSITIVE_TIMES
            if frozenset((row_time, column_time)) in seams:
                keep = True
            if keep:
                result[row, column] = raising[row, column]
    return result


def link_glue(raising: sp.Matrix, seams: tuple[frozenset[int], ...] = BOTH_SEAMS) -> sp.Matrix:
    reflection = reflection_permutation(link_theta)
    restricted = restricted_raising(raising, seams)
    return sp.expand(restricted - reflection * restricted * reflection)


def site_restricted_raising(raising: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(COVER_SIZE)
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            if row_time not in CLOSED_HALF or column_time not in CLOSED_HALF:
                continue
            if row_time == column_time and row_time in FIXED_SLICES:
                continue
            result[row, column] = raising[row, column]
    return result


def site_glue(raising: sp.Matrix) -> sp.Matrix:
    reflection = reflection_permutation(site_theta)
    restricted = site_restricted_raising(raising)
    return sp.expand(restricted - reflection * restricted * reflection)


def slice_indices(slices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(site_index(time, space) for time in slices for space in range(SPACE_EXTENT))


def reflected_indices(slices: tuple[int, ...], theta) -> tuple[int, ...]:
    return tuple(site_index(theta(time), space) for time in slices for space in range(SPACE_EXTENT))


def paired_gram(inverse: sp.Matrix, slices: tuple[int, ...], theta) -> sp.Matrix:
    anchors = slice_indices(slices)
    partners = reflected_indices(slices, theta)
    return sp.Matrix(
        len(anchors),
        len(anchors),
        lambda row, column: sp.conjugate(inverse[anchors[column], partners[row]]),
    ).applyfunc(sp.expand)


def link_gram(action: sp.Matrix, slices: tuple[int, ...] = (0, 1)) -> sp.Matrix:
    return paired_gram(action.inv(), slices, link_theta)


def band_census(action: sp.Matrix) -> dict[int, int]:
    census: dict[int, int] = {}
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if action[row, column] == 0:
                continue
            offset = (row // SPACE_EXTENT - column // SPACE_EXTENT) % TIME_EXTENT
            if offset > TIME_EXTENT // 2:
                offset -= TIME_EXTENT
            census[offset] = census.get(offset, 0) + 1
    return dict(sorted(census.items()))


def schur_complement(gram: sp.Matrix, core_size: int) -> sp.Matrix:
    core = gram[:core_size, :core_size]
    corner = gram[:core_size, core_size:]
    tail = gram[core_size:, core_size:]
    return sp.expand(tail - corner.T * core.inv() * corner)


# Block 186's separately supplied section-frame fixture.
SECTION_PLAIN_TIMES = (0, 1, 2)
SECTION_SEAM_TIMES = (3, 7)
SECTION_XI = sp.diag(1, -1, 1, -1)
SECTION_SPAN = tuple(
    (time, space) for time in POSITIVE_TIMES for space in range(SPACE_EXTENT)
)


def cover_shift(delta_t: int, delta_x: int) -> sp.Matrix:
    shift = sp.zeros(COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            shift[site_index(time + delta_t, space + delta_x), site_index(time, space)] = 1
    return shift


def section_space_parity(times: tuple[int, ...] = tuple(range(TIME_EXTENT))) -> sp.Matrix:
    return sp.diag(*[(-1) ** space for _time in times for space in range(SPACE_EXTENT)])


def section_cells() -> tuple[frozenset[int], ...]:
    """The eight disjoint even-anchored 2x2 cells of the 8x4 cover."""
    return tuple(
        frozenset(
            site_index(2 * coarse_t + dt, 2 * coarse_x + dx)
            for dt in (0, 1)
            for dx in (0, 1)
        )
        for coarse_t in range(TIME_EXTENT // 2)
        for coarse_x in range(SPACE_EXTENT // 2)
    )


def section_hodge_from_blocks(block) -> sp.Matrix:
    return hodge_from_cells(block)


def section_completion(
    hodge: sp.Matrix,
    differential: sp.Matrix,
    mass: object = R(9, 20),
) -> sp.Matrix:
    return sp.expand(
        mass * hodge + I * (hodge * differential + differential.H * hodge)
    )


def section_glued_hodge(
    seam_block: sp.Matrix,
    field: dict,
    spatial_shift: sp.Matrix,
) -> sp.Matrix:
    def block(time: int, space: int) -> sp.Matrix:
        if time in SECTION_SEAM_TIMES:
            return seam_block
        if time in SECTION_PLAIN_TIMES:
            return shear_block(*field[(time % PHYSICAL_TIME_EXTENT, space)])
        reflected = (-2 - time) % TIME_EXTENT
        shear, volume = field[(reflected % PHYSICAL_TIME_EXTENT, space)]
        return sp.expand(
            OFFSET_PERMUTATION
            * shear_block(-shear, volume)
            * OFFSET_PERMUTATION.T
        )

    raw = section_hodge_from_blocks(block)
    return sp.expand((raw + spatial_shift.T * raw * spatial_shift) / 2)


def section_restricted_differential(differential: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(COVER_SIZE)
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if (
                differential[row, column] != 0
                and row // SPACE_EXTENT in POSITIVE_TIMES
                and column // SPACE_EXTENT in POSITIVE_TIMES
            ):
                result[row, column] = differential[row, column]
    return result


def section_pairing_from_resolvent(resolvent: sp.Matrix) -> sp.Matrix:
    size = len(SECTION_SPAN)
    return sp.Matrix(
        size,
        size,
        lambda row, column: sp.conjugate(
            resolvent[
                site_index(*SECTION_SPAN[column]),
                site_index(*SECTION_SPAN[row]),
            ]
        ),
    ).applyfunc(sp.expand)


def section_dressed_gram(action: sp.Matrix, reflection: sp.Matrix) -> sp.Matrix:
    return section_pairing_from_resolvent(sp.expand(action.inv() * reflection))


def section_undressed_gram(action: sp.Matrix) -> sp.Matrix:
    inverse = action.inv()
    size = len(SECTION_SPAN)
    return sp.Matrix(
        size,
        size,
        lambda row, column: sp.conjugate(
            inverse[
                site_index(*SECTION_SPAN[column]),
                site_index((-1 - SECTION_SPAN[row][0]) % TIME_EXTENT, SECTION_SPAN[row][1]),
            ]
        ),
    ).applyfunc(sp.expand)


def support_components(matrix: sp.Matrix) -> tuple[int, ...]:
    parent = list(range(matrix.rows))

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if matrix[row, column] != 0:
                left, right = find(row), find(column)
                if left != right:
                    parent[left] = right
    sizes: dict[int, int] = {}
    for node in range(matrix.rows):
        root = find(node)
        sizes[root] = sizes.get(root, 0) + 1
    return tuple(sorted(sizes.values()))


def cross_half_entries(matrix: sp.Matrix) -> int:
    return sum(
        matrix[row, column] != 0
        and (row // SPACE_EXTENT in POSITIVE_TIMES)
        != (column // SPACE_EXTENT in POSITIVE_TIMES)
        for row in range(matrix.rows)
        for column in range(matrix.cols)
    )


def symmetric_pair(row: int, column: int) -> sp.Matrix:
    matrix = sp.zeros(4)
    matrix[row, column] = matrix[column, row] = 1
    return matrix


def section_seam_family(parameter: object) -> tuple[tuple[str, sp.Matrix], ...]:
    f02 = symmetric_pair(0, 2)
    f13 = symmetric_pair(1, 3)
    b5 = symmetric_pair(1, 2) - symmetric_pair(0, 3)
    b8 = symmetric_pair(2, 3) - symmetric_pair(0, 1)
    return (
        ("E02", sp.eye(4) + parameter * f02),
        ("E13", sp.eye(4) + parameter * f13),
        ("b5_type_mixed_sign", sp.eye(4) + parameter * b5),
        ("b8_type", sp.eye(4) + parameter * b8),
        ("Bgen1", sp.eye(4) + parameter * (f02 + f13 + b5 + b8)),
        ("Bgen2", sp.eye(4) + parameter * (f02 + 2 * f13 + 3 * b5 + 4 * b8)),
    )


def section_self_dual_dimension(dressing: sp.Matrix) -> tuple[int, int]:
    symbols: dict[tuple[int, int], sp.Symbol] = {}
    block = sp.zeros(4)
    for row in range(4):
        for column in range(row, 4):
            symbol = sp.Symbol(f"b_{row}{column}")
            symbols[(row, column)] = symbol
            block[row, column] = block[column, row] = symbol
    residual = sp.expand(dressing * block * dressing.T - block)
    order = list(symbols.values())
    solution = list(
        sp.linsolve(
            [residual[row, column] for row in range(4) for column in range(4)],
            order,
        )
    )[0]
    free = set().union(*(entry.free_symbols for entry in solution))
    off_diagonal = set().union(
        *(
            solution[order.index(symbol)].free_symbols
            for (row, column), symbol in symbols.items()
            if row != column
        )
    )
    return len(free), len(off_diagonal)
