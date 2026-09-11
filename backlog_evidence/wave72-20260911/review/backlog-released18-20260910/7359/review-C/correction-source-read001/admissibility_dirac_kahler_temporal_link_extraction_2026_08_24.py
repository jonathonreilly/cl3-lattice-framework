#!/usr/bin/env python3
"""Corrected Block 184 finite temporal-link certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11 as f


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block184-temporal-link-extraction-20260824/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md': '6fe011fe12de417f4dcbe85fcf9df6b4d3477738caedb04fcc8d43997fd842c1',
    '.claude/science/physics-loops/toe-axiom-closure-block184-temporal-link-extraction-20260824/NO_GO_LEDGER.md': '19d381337a5e98049557d2f752d99871db6f15196ab427d32fbfc4089f30c540',
    'scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py': 'd56cb24eeb93ea34268a4a48e5c5cc9c59958b45a6818c192a927bfb42ebd436',
    'scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py': '4299d645f687bec12d945598cca1df5c13a73c871a9e6ad1459e7e6b17c5bab5',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md': 'b3e42b85ff4bd29edd2d3c65bb1685503560af6b512013e062a93601c8661990',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

T = f.TIME_EXTENT
X = f.SPACE_EXTENT
N = f.COVER_SIZE
PHYSICAL_T = f.PHYSICAL_TIME_EXTENT
SYMBOLIC_MASS = sp.Symbol("m", real=True)
SLICE_SHEARS = sp.symbols("q0 q1 q2 q3")
SLICE_VOLUMES = sp.symbols("v0 v1 v2 v3", positive=True)
CELL_MAP = f.SIGNED_CELL_MAP


def cover_shift(dt: int, dx: int) -> sp.Matrix:
    shift = sp.zeros(N)
    for time in range(T):
        for space in range(X):
            shift[f.b128.cover_index(time + dt, space + dx), f.b128.cover_index(time, space)] = 1
    return shift


def edge_reflection() -> sp.Matrix:
    matrix = sp.zeros(N)
    for time in range(T):
        for space in range(X):
            matrix[f.b128.cover_index(T - 1 - time, space), f.b128.cover_index(time, space)] = 1
    return matrix


def time_parity() -> sp.Matrix:
    return sp.diag(*[(-1) ** (time % 2) for time in range(T) for _ in range(X)])


def completion(hodge: sp.Matrix, differential: sp.Matrix) -> sp.Matrix:
    return sp.expand(
        SYMBOLIC_MASS * hodge
        + sp.I * (hodge * differential + differential.H * hodge)
    )


def dual_block(shear: object, volume: object) -> sp.Matrix:
    block = f.shear_block(shear, volume)
    return sp.expand(CELL_MAP * block * CELL_MAP.T)


def hodge_cover(field: dict, block=f.shear_block) -> sp.Matrix:
    result = sp.zeros(N)
    for time in range(T):
        for space in range(X):
            shear, volume = field[(time % PHYSICAL_T, space)]
            embedding = f.b128.cover_embedding(time, space)
            result += embedding * block(shear, volume) * embedding.T / 4
    return sp.expand(result)


def reflected_field(field: dict) -> dict:
    return {
        (time, space): field[((2 - time) % PHYSICAL_T, space)]
        for time in range(PHYSICAL_T)
        for space in range(X)
    }


def two_shift_average(matrix: sp.Matrix, spatial_shift: sp.Matrix) -> sp.Matrix:
    return sp.expand((matrix + spatial_shift.T * matrix * spatial_shift) / 2)


def slice_block(matrix: sp.Matrix, row_slice: int, column_slice: int) -> sp.Matrix:
    return sp.expand(
        matrix[
            X * row_slice : X * (row_slice + 1),
            X * column_slice : X * (column_slice + 1),
        ]
    )


def band(matrix: sp.Matrix, separation: int, period: int = T) -> sp.Matrix:
    result = sp.zeros(matrix.rows, matrix.cols)
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if (row // X - column // X) % period == separation % period:
                result[row, column] = matrix[row, column]
    return result


def band_census(matrix: sp.Matrix, period: int = T) -> dict[int, int]:
    census: dict[int, int] = {}
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if matrix[row, column] != 0:
                separation = (row // X - column // X) % period
                census[separation] = census.get(separation, 0) + 1
    return dict(sorted(census.items()))


def odd_even_split(matrix: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
    flipped = sp.expand(
        matrix.subs(
            {shear: -shear for shear in SLICE_SHEARS}, simultaneous=True
        )
    )
    return sp.expand((matrix - flipped) / 2), sp.expand((matrix + flipped) / 2)


def main() -> int:
    checks = f.Checks()
    identity_ok, actual = f.verify_input_hashes(INPUT_SHA256)
    checks.add(
        "A-source-input-closure",
        identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS,
        f"{len(INPUT_SHA256)} literal current inputs; actual={actual}",
    )

    ux = cover_shift(0, 1)
    ut = cover_shift(1, 0)
    d00 = sp.Matrix(f.b128.chart_differential_cover((0, 0)))
    field = f.b128.block105.overlap_field()
    reflection = sp.expand(edge_reflection() * time_parity())
    reflected_differential = sp.expand(reflection * d00 * reflection.T)

    hodge = hodge_cover(field)
    displayed_frame = two_shift_average(hodge, ux)
    dual_frame = two_shift_average(hodge_cover(reflected_field(field), dual_block), ux)
    action = completion(displayed_frame, d00)
    dual_action = completion(dual_frame, reflected_differential)
    checks.add(
        "B-displayed-frame",
        f.residual_count(hodge - f.b128.curved_hodge_cover()) == 0
        and f.residual_count(reflection * reflection.T - sp.eye(N)) == 0
        and f.residual_count(reflection * displayed_frame * reflection.T - dual_frame) == 0
        and all(
            displayed_frame[:size, :size].det(method="berkowitz") > 0
            for size in range(1, N + 1)
        ),
        "the explicit two-shift average is positive definite and closes under the displayed reflection; no completeness or minimality is asserted",
    )

    census = band_census(action)
    forward = band(action, 1)
    backward = band(action, -1)
    link_blocks = tuple(slice_block(action, (time + 1) % T, time) for time in range(T))
    checks.add(
        "C-band-and-link-census",
        census == {0: 80, 1: 72, 2: 16, 6: 16, 7: 72}
        and tuple(block.rank() for block in link_blocks) == (4,) * 8
        and tuple(f.nonzero_entries(block) for block in link_blocks) == (10, 8) * 4
        and all(not block.nullspace() for block in link_blocks)
        and (
            f.residual_count(backward - forward.H),
            f.residual_count(backward + forward.H),
            f.residual_count(backward - forward.T),
        )
        == (40, 32, 40),
        f"finite cover census={census}; eight bond ranks are computed directly",
    )

    reflected_forward = sp.expand(reflection * forward * reflection.T)
    wrong_dual = completion(dual_frame, d00)
    checks.add(
        "D-reflection-parity",
        f.residual_count(reflected_forward - band(dual_action, -1)) == 0
        and f.residual_count(reflected_forward - band(wrong_dual, -1)) == 16
        and f.residual_count(reflected_forward - band(dual_action, 1)) == 144,
        "the forward band maps to the dual backward band only with the reflected differential",
    )

    symbolic_field = {
        (time, space): (SLICE_SHEARS[time], SLICE_VOLUMES[time])
        for time in range(PHYSICAL_T)
        for space in range(X)
    }
    symbolic_action = completion(two_shift_average(hodge_cover(symbolic_field), ux), d00)
    odd_bond = slice_block(symbolic_action, 2, 1)
    even_bond = slice_block(symbolic_action, 1, 0)
    odd_part, even_part = odd_even_split(even_bond)
    even_magnitude = (
        1 / SLICE_VOLUMES[0]
        + SLICE_VOLUMES[1]
        - SLICE_VOLUMES[0] / (SLICE_SHEARS[0] ** 2 - 1)
        - SLICE_VOLUMES[1] / (SLICE_SHEARS[1] ** 2 - 1)
    ) / 5
    even_positions = tuple(
        (row, column)
        for row in range(X)
        for column in range(X)
        if even_part[row, column] != 0
    )
    checks.add(
        "E-symbolic-bond-split",
        f.nonzero_entries(odd_bond) == 8
        and f.residual_count(odd_bond.subs(SLICE_SHEARS[1], 0)) == 0
        and f.nonzero_entries(odd_part) == 8
        and f.nonzero_entries(even_part) == 4
        and SYMBOLIC_MASS in odd_part.free_symbols
        and SYMBOLIC_MASS not in even_part.free_symbols
        and even_positions == ((0, 0), (1, 1), (2, 2), (3, 3))
        and tuple(
            sp.simplify(even_part[position] / even_magnitude)
            for position in even_positions
        )
        == (-1, 1, -1, 1),
        "odd bonds vanish at zero shear; the even bond has an 8-entry odd part and a 4-entry shear-dependent even part",
    )

    slice_dets = tuple(
        sp.expand(slice_block(action, time, time).det(method="berkowitz"))
        for time in range(T)
    )
    polys = tuple(sp.Poly(value, SYMBOLIC_MASS) for value in slice_dets[:PHYSICAL_T])
    checks.add(
        "F-original-slice-blocks",
        all(sp.expand(slice_dets[time] - slice_dets[time + PHYSICAL_T]) == 0 for time in range(PHYSICAL_T))
        and len({sp.srepr(value) for value in slice_dets}) == 4
        and all(poly.degree() == 4 for poly in polys)
        and all(monomial[0] % 2 == 0 for poly in polys for monomial, _ in poly.terms())
        and all(coefficient > 0 for poly in polys for coefficient in poly.all_coeffs() if coefficient != 0),
        "each displayed original diagonal slice block has a positive even-quartic determinant for every real mass; no Schur-pivot claim is made",
    )

    quotient = sp.Matrix(f.b128.antiperiodic_quotient(action))
    quotient_bonds = tuple(
        quotient[
            X * ((time + 1) % PHYSICAL_T) : X * ((time + 1) % PHYSICAL_T + 1),
            X * time : X * (time + 1),
        ]
        for time in range(PHYSICAL_T)
    )
    quotient_seam = quotient[:X, -X:]
    cover_seam = slice_block(action, PHYSICAL_T, PHYSICAL_T - 1)
    checks.add(
        "G-antiperiodic-quotient",
        band_census(quotient, PHYSICAL_T) == {0: 40, 1: 36, 2: 16, 3: 36}
        and tuple(block.rank() for block in quotient_bonds) == (4,) * 4
        and tuple(f.nonzero_entries(block) for block in quotient_bonds) == (10, 8, 10, 8)
        and f.residual_count(quotient_seam + cover_seam) == 0
        and f.residual_count(quotient_seam - cover_seam) > 0,
        "the 16-dimensional quotient has four full-rank bonds and the measured antiperiodic seam sign",
    )

    equal_frames = tuple(
        sp.expand((ut**time) * (ux**space))
        for time in range(PHYSICAL_T)
        for space in range(X)
    )
    equal_weight = sp.expand(
        sum((shift.T * hodge * shift for shift in equal_frames), sp.zeros(N))
        / len(equal_frames)
    )
    checks.add(
        "H-finite-scope",
        band_census(completion(equal_weight, d00)) == census
        and f.residual_count(equal_weight - displayed_frame) == 96,
        "the equal-weight orbit average shares the measured band census but differs from the displayed two-shift average; no finite-family completeness claim follows",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
