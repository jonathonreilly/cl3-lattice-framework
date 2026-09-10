#!/usr/bin/env python3
"""Minimal exact fixture closure for the carrier-reflection certificates.

This module replaces a 17-file historical import chain with the definitions
actually used by the Block 142 and Block 143 primaries.  Block 105 is imported
whole from the independently reviewed candidate; the Block 134/137/141 pieces
below are narrow extractions from their frozen original blobs.  The historical
modules remain byte-for-byte recoverable under
``.claude/science/physics-loops/released-reflection-recovery-20260910/`` and
are not promoted as canonical helpers.

``SOURCE_AST_MAP`` is provenance, not a scientific premise.  For copied
functions it names the original top-level AST node and source-line interval.
References formerly qualified through ``b134`` or ``b105`` are rebound only to
the same definitions in this module or to the intact reviewed Block 105 module.
"""

from __future__ import annotations

import sympy as sp

import admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14 as block105


SOURCE_AST_MAP = {
    "block105_reviewed_import": {
        "commit": "41f814ac102f9225a1c1553efd849e199168bb17",
        "blob": "f07498986b05885b5335777b46c96bd926f260ef",
        "path": "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
        "nodes": {
            "EX": [65, 67],
            "ET": [68, 70],
            "LENGTH": [77, 77],
            "OVERLAP_SHEARS": [87, 96],
            "phase_unitary": [123, 129],
            "shift_lifts": [132, 133],
            "shear_hodge": [329, 331],
            "overlap_field": [344, 349],
        },
        "disposition": "imported_intact_from_provisional_reviewed_candidate",
    },
    "block134_extract": {
        "commit": "275f1bd78201b0d9f440099536d3f602106caf29",
        "blob": "f092e5560590d6a4e485a57721878caaa874b4dd",
        "path": "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
        "nodes": {
            "matrix_zero": [238, 239],
            "SPACE_EXTENT": [255, 255],
            "PHYSICAL_TIME_EXTENT": [256, 256],
            "COVER_TIME_EXTENT": [257, 257],
            "SIZE": [258, 258],
            "NCELLS": [259, 259],
            "ORIGINS": [260, 260],
            "DISPLAYED": [261, 261],
            "S_X": [262, 262],
            "S_T": [263, 263],
            "MASS": [264, 264],
            "cover_index": [267, 271],
            "cover_embedding": [274, 283],
            "cover_chart_matrix": [286, 296],
            "lifted": [327, 328],
            "local_differential": [331, 332],
            "chart_gauge": [346, 348],
            "curved_hodge_cover": [356, 371],
            "antiperiodic_quotient": [374, 378],
        },
        "disposition": "copied_required_ast_nodes_only",
    },
    "block137_extract": {
        "commit": "275f1bd78201b0d9f440099536d3f602106caf29",
        "blob": "f2268cebddd7b7a9ee4fdf455a832a2ee5fe9a9a",
        "path": "scripts/admissibility_dirac_kahler_twisted_scouting_record_2026_08_19.py",
        "nodes": {
            "connection_data": [276, 320],
            "quotient_action": [363, 369],
            "quotient_correction": [372, 374],
        },
        "disposition": "copied_required_ast_nodes_only",
    },
    "block141_extract": {
        "commit": "275f1bd78201b0d9f440099536d3f602106caf29",
        "blob": "bd3288da45b01b3f8f60d76538a0b78b7154d719",
        "path": "scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py",
        "nodes": {"HEALING_WEIGHTS": [355, 355]},
        "disposition": "copied_required_ast_node_only",
    },
}


R = sp.Rational
I = sp.I


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


SPACE_EXTENT = block105.LENGTH
PHYSICAL_TIME_EXTENT = block105.LENGTH
COVER_TIME_EXTENT = 2 * PHYSICAL_TIME_EXTENT
SIZE = COVER_TIME_EXTENT * SPACE_EXTENT
NCELLS = SIZE // 4
ORIGINS = ((0, 0), (0, 1), (1, 0), (1, 1))
DISPLAYED = ((1, 0), (1, 1))
S_X = R(3, 5)
S_T = R(4, 5)
MASS = R(2, 7)
HEALING_WEIGHTS = (sp.Integer(0), sp.Integer(0), R(1, 2), R(-1, 3))


def cover_index(time_coordinate: int, space_coordinate: int) -> int:
    return (
        (time_coordinate % COVER_TIME_EXTENT) * SPACE_EXTENT
        + space_coordinate % SPACE_EXTENT
    )


def cover_embedding(time_coordinate: int, space_coordinate: int) -> sp.Matrix:
    matrix = sp.zeros(SIZE, 4)
    for column, (delta_t, delta_x) in enumerate(
        ((0, 0), (0, 1), (1, 0), (1, 1))
    ):
        matrix[
            cover_index(time_coordinate + delta_t, space_coordinate + delta_x),
            column,
        ] = 1
    return matrix


def cover_chart_matrix(origin: tuple[int, int]) -> sp.Matrix:
    matrix = sp.zeros(SIZE)
    row = 0
    for coarse_t in range(COVER_TIME_EXTENT // 2):
        for coarse_x in range(SPACE_EXTENT // 2):
            embedding = cover_embedding(
                2 * coarse_t + origin[0], 2 * coarse_x + origin[1]
            )
            matrix[row : row + 4, :] = embedding.T
            row += 4
    return matrix


def lifted(matrix: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(sp.eye(NCELLS), matrix)


def local_differential(sx: sp.Expr, st: sp.Expr) -> sp.Matrix:
    return I * (sx * block105.EX + st * block105.ET)


def chart_gauge(origin: tuple[int, int]) -> sp.Matrix:
    rt, rx = block105.shift_lifts()
    return (rt ** origin[0]) * (rx ** origin[1])


def curved_hodge_cover() -> sp.Matrix:
    field = block105.overlap_field()
    result = sp.zeros(SIZE)
    for time_coordinate in range(COVER_TIME_EXTENT):
        for space_coordinate in range(SPACE_EXTENT):
            shear, volume = field[
                (time_coordinate % PHYSICAL_TIME_EXTENT, space_coordinate)
            ]
            embedding = cover_embedding(time_coordinate, space_coordinate)
            result += (
                embedding
                * block105.shear_hodge(shear, volume)
                * embedding.T
                / 4
            )
    return sp.simplify(result)


def antiperiodic_quotient(matrix: sp.Matrix) -> sp.Matrix:
    identity = sp.eye(PHYSICAL_TIME_EXTENT * SPACE_EXTENT)
    injection = sp.Matrix.vstack(-identity, identity)
    selection = sp.Matrix.hstack(sp.zeros(identity.rows), identity)
    return sp.simplify(selection * matrix * injection)


def connection_data(sx: sp.Expr, st: sp.Expr) -> dict[str, object]:
    """Return the exact chart, frame, transition, and differential data."""
    local = local_differential(sx, st)
    phase = lifted(block105.phase_unitary().H)
    charts = {origin: cover_chart_matrix(origin) for origin in ORIGINS}
    frames = {origin: phase * charts[origin] for origin in ORIGINS}
    gauges = {origin: chart_gauge(origin) for origin in ORIGINS}
    local_charts = {
        origin: lifted(sp.simplify(gauges[origin].H * local * gauges[origin]))
        for origin in ORIGINS
    }
    differentials = {
        origin: sp.simplify(charts[origin].H * local_charts[origin] * charts[origin])
        for origin in ORIGINS
    }
    frame_differentials = {
        origin: sp.simplify(frames[origin] * differentials[origin] * frames[origin].H)
        for origin in ORIGINS
    }
    transitions = {
        (first, second): sp.simplify(frames[second] * frames[first].H)
        for first in ORIGINS
        for second in ORIGINS
    }
    defects = {
        (first, second): sp.simplify(
            frame_differentials[second] * transitions[(first, second)]
            - transitions[(first, second)] * frame_differentials[first]
        )
        for first in ORIGINS
        for second in ORIGINS
    }
    return {
        "local": local,
        "phase": phase,
        "charts": charts,
        "frames": frames,
        "gauges": gauges,
        "local_charts": local_charts,
        "d": differentials,
        "dhat": frame_differentials,
        "g": transitions,
        "theta": defects,
    }


def quotient_action(
    differential: sp.Matrix, hodge: sp.Matrix, mass: sp.Expr
) -> sp.Matrix:
    cover = sp.simplify(
        mass * hodge + I * (hodge * differential + differential.H * hodge)
    )
    return antiperiodic_quotient(cover)


def quotient_correction(operator: sp.Matrix, hodge: sp.Matrix) -> sp.Matrix:
    cover = sp.simplify(I * (hodge * operator + operator.H * hodge))
    return antiperiodic_quotient(cover)
