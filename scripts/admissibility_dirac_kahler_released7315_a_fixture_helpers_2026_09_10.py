#!/usr/bin/env python3
"""Exact finite fixture shared by corrected Blocks 153--156 and 158--159.

Only constructors used by the six corrected primaries are retained here.  The
historical 23-module import chain is archived, not imported.  The lower-level
cover construction comes from the already corrected current-main fixture
helper, whose sole science import is Block 105.
"""

from __future__ import annotations

from dataclasses import dataclass
import collections
import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10 as fixture


SOURCE_AST_MAP = {
    "block145_extract": {
        "source_sha256": "1599622920371eb1bd804f794a12eb73d8d45201e6e2674f73c632f3c3d7b666",
        "path": "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
        "nodes": {
            "carrier_constants": [406, 442],
            "cover_hodge_general": [449, 473],
            "quotient": [476, 482],
            "moduli_from_field": [485, 493],
            "quotient_action": [500, 512],
            "connection": [520, 522],
            "edge_differentials": [525, 534],
            "witness_field": [711, 717],
            "in_admissible_cone": [731, 735],
        },
    },
    "block147_extract": {
        "source_sha256": "501c8810ea0ac9cf560511cb537bc870109aa55f5f69085ba4ce4db0bbd8ddef",
        "path": "scripts/admissibility_dirac_kahler_annealed_pairing_migration_2026_08_19.py",
        "nodes": {"modulus_point": [555, 564]},
    },
    "block148_extract": {
        "source_sha256": "1b9cfcd0da639e97c72b6f8838e3cfc59eb7cd2718e4f1dc3e832283599dd4e2",
        "path": "scripts/admissibility_dirac_kahler_general_migration_theorem_2026_08_20.py",
        "nodes": {
            "affine_moves": [486, 492],
            "move_permutation": [496, 505],
            "move_matrix": [508, 512],
            "compose_labels": [527, 534],
            "cell_map": [542, 561],
            "push_point": [595, 610],
            "escape_witness_field": [686, 698],
        },
    },
    "block154_extract": {
        "source_sha256": "03ee8d591b5f7ffa88e38d56cc97c86334e077fed8d4847c77ec3578182bea1d",
        "path": "scripts/admissibility_dirac_kahler_unique_completion_price_2026_08_20.py",
        "nodes": {
            "monomial_rows": [558, 580],
            "feasible": [583, 586],
            "support_completion_loop": [1021, 1121],
        },
    },
    "block155_extract": {
        "source_sha256": "b83229b708380d215b1fd51e734f7e1f24e57320416b109682fd8b26e2a6300e",
        "path": "scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py",
        "nodes": {
            "cell_of": [518, 519],
            "link_kind": [522, 536],
            "transfer_witness_profile": [1478, 1486],
        },
    },
    "block159_extract": {
        "source_sha256": "c2bb5378eaee4ffa9ed6d5a7e853feb6f5ef133be4d901e251dce08219413d4e",
        "path": "scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py",
        "nodes": {
            "link_field": [609, 617],
            "dress": [620, 626],
            "holonomy": [629, 642],
            "census": [645, 652],
            "pure_gauge_field": [655, 668],
            "phase_operator": [671, 674],
            "reweight": [786, 795],
        },
    },
}

R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
SIZE = fixture.SIZE
COVER_T = fixture.COVER_TIME_EXTENT
PHYS_T = fixture.PHYSICAL_TIME_EXTENT
LX = fixture.SPACE_EXTENT
PHYS = PHYS_T * LX
HALF = PHYS // 2
ORIGINS = fixture.ORIGINS
INDEX = {origin: position for position, origin in enumerate(ORIGINS)}
CELLS = tuple((t, x) for t in range(PHYS_T) for x in range(LX))
ODD_CELLS = tuple((t, x) for t in (1, 3) for x in range(LX))
EDGE_KEYS = tuple(
    (INDEX[left], INDEX[right]) for left in ORIGINS for right in ORIGINS
)
HEALING_WEIGHTS = fixture.HEALING_WEIGHTS
SHEAR_X, SHEAR_T = sp.symbols("s_x s_t", real=True)
MASS = sp.symbols("m", real=True)

LIFT = sp.Matrix.vstack(-sp.eye(PHYS), sp.eye(PHYS))
SELECT = sp.Matrix.hstack(sp.zeros(PHYS), sp.eye(PHYS))
PLUS = sp.zeros(PHYS, HALF)
MINUS = sp.zeros(PHYS, HALF)
for _slot in range(HALF):
    PLUS[_slot, _slot] = 1
    MINUS[HALF + _slot, _slot] = 1


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(entry) == 0 for entry in sp.Matrix(matrix))


def zero_simplified(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in sp.Matrix(matrix))


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix + matrix.H) / 2)


def anti(matrix: sp.MatrixBase) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix - matrix.H) / 2)


def no_float(value: object) -> bool:
    if isinstance(value, float):
        return False
    if isinstance(value, sp.Basic):
        return not value.has(sp.Float)
    if isinstance(value, dict):
        return all(no_float(k) and no_float(v) for k, v in value.items())
    if isinstance(value, (list, tuple, set, frozenset)):
        return all(no_float(item) for item in value)
    return True


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (positive, zero, negative) inertia by Hermitian congruence."""
    work = sp.Matrix(matrix).as_mutable()
    active = list(range(work.rows))
    positive = negative = null = 0
    while active:
        head = active[0]
        pivot = sp.simplify(work[head, head])
        if pivot != 0:
            if pivot.is_positive:
                positive += 1
            elif pivot.is_negative:
                negative += 1
            else:
                raise ValueError(f"pivot has undecidable sign: {pivot}")
            rest = active[1:]
            for row in rest:
                factor = work[row, head] / pivot
                if factor == 0:
                    continue
                for column in rest:
                    work[row, column] = sp.expand(
                        work[row, column] - factor * work[head, column]
                    )
            active = rest
            continue
        partner = next(
            (k for k in active[1:] if sp.simplify(work[head, k]) != 0), None
        )
        if partner is None:
            null += 1
            active = active[1:]
            continue
        positive += 1
        negative += 1
        block = sp.Matrix(
            [
                [work[head, head], work[head, partner]],
                [work[partner, head], work[partner, partner]],
            ]
        )
        inverse = block.inv()
        rest = [k for k in active if k not in (head, partner)]
        for row in rest:
            coefficients = sp.expand(
                sp.Matrix([[work[row, head], work[row, partner]]]) * inverse
            )
            for column in rest:
                work[row, column] = sp.expand(
                    work[row, column]
                    - coefficients[0, 0] * work[head, column]
                    - coefficients[0, 1] * work[partner, column]
                )
        active = rest
    return positive, null, negative


def site(index: int) -> tuple[int, int]:
    return index // LX, index % LX


def site_index(time_coordinate: int, space_coordinate: int) -> int:
    return (time_coordinate % PHYS_T) * LX + (space_coordinate % LX)


def descend(cover_operator: sp.Matrix) -> sp.Matrix | None:
    candidate = SELECT * cover_operator * LIFT
    if zero(sp.expand(cover_operator * LIFT - LIFT * candidate)):
        return sp.expand(candidate)
    return None


def canonical_theta() -> sp.Matrix:
    matrix = sp.zeros(PHYS)
    for index in range(PHYS):
        t, x = site(index)
        matrix[site_index(3 - t, -x), index] = -1
    return matrix


def staggered_parity() -> sp.Matrix:
    return sp.diag(*[(-1) ** (site(k)[0] + site(k)[1]) for k in range(PHYS)])


THETA = canonical_theta()
X0 = staggered_parity()
DEAD = tuple(k for k in range(HALF) if X0[k, k] == -1)
LIVE = tuple(k for k in range(HALF) if X0[k, k] == 1)

ALL_MOVES = tuple(
    (time_sign, time_shift, space_sign, space_shift)
    for time_sign in (1, -1)
    for time_shift in range(COVER_T)
    for space_sign in (1, -1)
    for space_shift in range(LX)
)
COVARIANT_MOVES = tuple(label for label in ALL_MOVES if label[0] == label[2])
THETA_LABEL = (-1, 7, -1, 0)
THETA_PRIME_LABEL = (-1, 7, -1, 1)


def move_permutation(label: tuple[int, int, int, int]) -> dict[int, int]:
    et, p, ex, q = label
    return {
        fixture.cover_index(t, x): fixture.cover_index(et * t + p, ex * x + q)
        for t in range(COVER_T)
        for x in range(LX)
    }


def move_matrix(label_or_permutation) -> sp.Matrix:
    permutation = (
        move_permutation(label_or_permutation)
        if isinstance(label_or_permutation, tuple)
        else label_or_permutation
    )
    matrix = sp.zeros(SIZE)
    for source, target in permutation.items():
        matrix[target, source] = 1
    return matrix


def compose_labels(left: tuple, right: tuple) -> tuple:
    return (
        left[0] * right[0],
        (left[0] * right[1] + left[1]) % COVER_T,
        left[2] * right[2],
        (left[2] * right[3] + left[3]) % LX,
    )


def kappa(label: tuple) -> int:
    return (label[1] + label[3]) % 2


MOVE_MATRIX = {label: move_matrix(label) for label in COVARIANT_MOVES}
DESCENT = {label: descend(MOVE_MATRIX[label]) for label in COVARIANT_MOVES}
THETA_PRIME = DESCENT[THETA_PRIME_LABEL]
if THETA_PRIME is None:
    raise RuntimeError("theta-prime failed the exact quotient descent test")


def cell_map(label: tuple):
    et, p, _ex, q = label
    if et == 1:
        return lambda cell: ((cell[0] + p) % PHYS_T, (cell[1] + q) % LX)
    return lambda cell: ((p - 1 - cell[0]) % PHYS_T, (q - 1 - cell[1]) % LX)


def push_point(point: dict, label: tuple) -> dict:
    phi = cell_map(label)
    out = {}
    for cell in CELLS:
        image = phi(cell)
        swap = label[0] == -1
        out[NU_MODULUS[image]] = point[
            INV_MODULUS[cell] if swap else NU_MODULUS[cell]
        ]
        out[INV_MODULUS[image]] = point[
            NU_MODULUS[cell] if swap else INV_MODULUS[cell]
        ]
        out[A_MODULUS[image]] = point[A_MODULUS[cell]]
        out[B_MODULUS[image]] = point[B_MODULUS[cell]]
    return out


NU_MODULUS = {cell: sp.Symbol(f"n_{cell[0]}{cell[1]}", real=True) for cell in CELLS}
A_MODULUS = {cell: sp.Symbol(f"a_{cell[0]}{cell[1]}", real=True) for cell in CELLS}
B_MODULUS = {cell: sp.Symbol(f"b_{cell[0]}{cell[1]}", real=True) for cell in CELLS}
INV_MODULUS = {cell: sp.Symbol(f"m_{cell[0]}{cell[1]}", real=True) for cell in CELLS}
FREE_MODULI = (NU_MODULUS, A_MODULUS, B_MODULUS, INV_MODULUS)
COORDS = tuple(
    table[cell]
    for cell in CELLS
    for table in FREE_MODULI
)
SHEAR_COORDS = tuple(B_MODULUS[cell] for cell in CELLS)
ODD_SHEAR_COORDS = tuple(B_MODULUS[cell] for cell in ODD_CELLS)


def cover_hodge_general(nu_value, a_value, b_value, inverse_value) -> sp.Matrix:
    hodge = sp.zeros(SIZE, SIZE)
    for t in range(COVER_T):
        for x in range(LX):
            cell = (t % PHYS_T, x)
            nu, a = nu_value[cell], a_value[cell]
            b, inverse = b_value[cell], inverse_value[cell]
            hodge[fixture.cover_index(t, x), fixture.cover_index(t, x)] += nu / 4
            hodge[fixture.cover_index(t, x + 1), fixture.cover_index(t, x + 1)] += a / 4
            hodge[fixture.cover_index(t + 1, x), fixture.cover_index(t + 1, x)] += a / 4
            hodge[fixture.cover_index(t + 1, x + 1), fixture.cover_index(t + 1, x + 1)] += inverse / 4
            hodge[fixture.cover_index(t, x + 1), fixture.cover_index(t + 1, x)] += b / 4
            hodge[fixture.cover_index(t + 1, x), fixture.cover_index(t, x + 1)] += b / 4
    return sp.expand(hodge)


def quotient(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        PHYS,
        PHYS,
        lambda i, j: sp.expand(matrix[PHYS + i, PHYS + j] - matrix[PHYS + i, j]),
    )


def moduli_from_field(field: dict) -> tuple[dict, dict, dict, dict]:
    nu_value, a_value, b_value, inverse_value = {}, {}, {}, {}
    for cell, (shear, volume) in field.items():
        shear = sp.sympify(shear)
        volume = sp.sympify(volume)
        nu_value[cell] = volume
        a_value[cell] = sp.cancel(volume / (1 - shear**2))
        b_value[cell] = sp.cancel(-volume * shear / (1 - shear**2))
        inverse_value[cell] = sp.cancel(sp.Integer(1) / volume)
    return nu_value, a_value, b_value, inverse_value


def cover_hodge_from_field(field: dict) -> sp.Matrix:
    return cover_hodge_general(*moduli_from_field(field))


def modulus_point(field: dict) -> dict:
    tables = moduli_from_field(field)
    point = {}
    for cell in CELLS:
        for table, values in zip(FREE_MODULI, tables):
            point[table[cell]] = values[cell]
    return point


def quotient_action(differential: sp.Matrix, hodge: sp.Matrix, mass=MASS) -> sp.Matrix:
    return quotient(
        sp.expand(mass * hodge + I * (hodge * differential + differential.H * hodge))
    )


def residue(differential: sp.Matrix, hodge: sp.Matrix | None = None) -> sp.Matrix:
    hodge = COVER_FREE if hodge is None else hodge
    return quotient(sp.expand(I * (hodge * differential + differential.H * hodge)))


def connection(shear_x=SHEAR_X, shear_t=SHEAR_T) -> tuple[dict, sp.Matrix]:
    data = fixture.connection_data(shear_x, shear_t)
    differentials = data["d"]
    return differentials, sp.expand(differentials[(0, 0)] - differentials[(1, 0)])


def edge_differentials(differentials: dict, star: sp.Matrix, weights=HEALING_WEIGHTS) -> dict:
    return {
        (INDEX[left], INDEX[right]): sp.expand(
            differentials[left] + (weights[INDEX[right]] - weights[INDEX[left]]) * star
        )
        for left in ORIGINS
        for right in ORIGINS
    }


def half_block(operator: sp.MatrixBase, matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.expand(PLUS.T * operator * matrix * PLUS)


def full_plus_row(operator: sp.MatrixBase, matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.expand(PLUS.T * operator * matrix)


def sub_block(
    matrix: sp.MatrixBase, rows: tuple[int, ...], columns: tuple[int, ...]
) -> sp.Matrix:
    return sp.Matrix([[sp.expand(matrix[i, j]) for j in columns] for i in rows])


def live_count(matrix: sp.MatrixBase) -> int:
    return sum(sp.expand(entry) != 0 for entry in matrix)


def support_of(matrix: sp.MatrixBase) -> tuple[tuple[int, int], ...]:
    return tuple(
        (row, column)
        for row in range(matrix.rows)
        for column in range(matrix.cols)
        if sp.expand(matrix[row, column]) != 0
    )


def displacement(row: int, column: int) -> tuple[int, int]:
    rt, rx = divmod(row, LX)
    ct, cx = divmod(column, LX)
    dt = (rt - ct) % COVER_T
    dx = (rx - cx) % LX
    dt = dt if dt <= COVER_T // 2 else dt - COVER_T
    dx = dx if dx <= LX // 2 else dx - LX
    return dt, dx


def monomial_rows(expression, parameters, index) -> list[tuple[list, sp.Expr]]:
    """Coefficient rows for an identity in carrier and connection symbols."""
    generators = list(COORDS) + [SHEAR_X, SHEAR_T]
    polynomial = sp.Poly(sp.expand(expression), *generators)
    rows = []
    parameter_set = set(parameters)
    for _monomial, coefficient in polynomial.terms():
        coefficient = sp.expand(sp.sympify(coefficient))
        row = [0] * len(parameters)
        constant = 0
        for term in sp.Add.make_args(coefficient):
            symbols = term.free_symbols & parameter_set
            if not symbols:
                constant += term
            else:
                symbol = symbols.pop()
                row[index[symbol]] += term.coeff(symbol, 1)
        rows.append((row, -constant))
    return rows


def feasible(matrix: sp.Matrix, rhs: sp.Matrix) -> tuple[int, int, bool]:
    rank = matrix.rank()
    augmented = matrix.row_join(rhs).rank()
    return rank, augmented, rank == augmented


def completion_table() -> dict:
    """Solve the Block-154 support-restricted cancellation on all 16 edges.

    The return value records the original support, the uniquely forced active
    deletion, the surviving differential, and the coefficient-map ranks.  Free
    invisible coefficients are set to zero in the displayed representative.
    """
    differentials, star = connection()
    edges = edge_differentials(differentials, star)
    out = {}
    for key, differential in edges.items():
        support = support_of(differential)
        coefficients = sp.symbols(f"c_{key[0]}_{key[1]}_0:{len(support)}", real=True)
        coefficient_index = {
            symbol: position for position, symbol in enumerate(coefficients)
        }
        perturbation = sp.zeros(SIZE)
        for position, (row, column) in enumerate(support):
            perturbation[row, column] = coefficients[position] * differential[row, column]
        delta_half = herm(half_block(THETA_PRIME, residue(perturbation)))
        target_half = herm(half_block(THETA_PRIME, residue(differential)))
        rows, right = [], []
        for row in DEAD:
            for column in LIVE:
                for coefficients_row, value in monomial_rows(
                    delta_half[row, column] + target_half[row, column],
                    coefficients,
                    coefficient_index,
                ):
                    rows.append(coefficients_row)
                    right.append(value)
        matrix, vector = sp.Matrix(rows), sp.Matrix(right)
        rank, augmented, solvable = feasible(matrix, vector)
        if not solvable:
            raise AssertionError(f"support completion is infeasible at edge {key}")
        solution = list(sp.linsolve((matrix, vector), list(coefficients)))[0]
        forced = tuple(
            position
            for position, value in enumerate(solution)
            if not (value.free_symbols & set(coefficients))
        )
        free = tuple(position for position in range(len(solution)) if position not in forced)
        particular = tuple(
            sp.simplify(
                solution[position].xreplace(
                    {coefficients[index]: 0 for index in free}
                )
            )
            for position in range(len(solution))
        )
        completed = sp.Matrix(differential)
        deleted = []
        for position, (row, column) in enumerate(support):
            if particular[position] != 0:
                completed[row, column] = sp.expand(
                    differential[row, column] * (1 + particular[position])
                )
                deleted.append((row, column))
        out[key] = {
            "support": support,
            "forced": forced,
            "free": free,
            "solution": particular,
            "deleted": tuple(deleted),
            "completed": sp.expand(completed),
            "rank": rank,
            "augmented_rank": augmented,
        }
    return out


def formal_compression(matrix: sp.MatrixBase) -> sp.Matrix:
    """The historical SELECT M LIFT map, without a descent interpretation."""
    return sp.expand(SELECT * matrix * LIFT)


def descent_residual(matrix: sp.MatrixBase) -> sp.Matrix:
    q = formal_compression(matrix)
    return sp.expand(matrix * LIFT - LIFT * q)


def link_kind(row: int, column: int) -> str:
    delta_t, delta_x = displacement(row, column)
    if (delta_t, delta_x) == (1, 0):
        return "T+"
    if (delta_t, delta_x) == (-1, 0):
        return "T-"
    if (delta_t, delta_x) == (0, 1):
        return "X+"
    if (delta_t, delta_x) == (0, -1):
        return "X-"
    return "OTHER"


def flat_field() -> dict:
    return {cell: (sp.Integer(0), sp.Integer(1)) for cell in CELLS}


def counterpoint_field() -> dict:
    """The exact zero-connection carrier used in Blocks 156 and 159."""
    field = flat_field()
    for time_coordinate in (1, 3):
        sign = 1 if time_coordinate == 1 else -1
        for space_coordinate in (0, 2):
            field[(time_coordinate, space_coordinate)] = (
                sign * R(1, 3),
                sp.Integer(1),
            )
    return field


def transfer_witness_field() -> dict:
    """The original Block-155 XFER carrier, distinct from the escape carrier."""
    field = flat_field()
    for time_coordinate in (1, 3):
        sign = 1 if time_coordinate == 1 else -1
        for space_coordinate in (0, 2):
            field[(time_coordinate, space_coordinate)] = (
                sign * R(3, 5),
                sp.Integer(1),
            )
    return field


def witness_field() -> dict:
    strong_cells = ((1, 1), (1, 3), (3, 1), (3, 3))
    weak_cells = ((1, 0), (1, 2), (3, 0), (3, 2))
    field = flat_field()
    for cell in strong_cells:
        field[cell] = (R(3, 5), sp.Integer(1))
    for cell in weak_cells:
        field[cell] = (R(15, 32), R(799, 512))
    return field


def escape_witness_field() -> dict:
    profile = {
        1: {0: R(3, 5), 1: R(1, 2), 2: R(3, 5), 3: R(-1, 2)},
        3: {0: R(-3, 5), 1: R(1, 2), 2: R(-3, 5), 3: R(-1, 2)},
    }
    return {
        cell: (
            profile[cell[0]][cell[1]] if cell[0] % 2 else sp.Integer(0),
            sp.Integer(1),
        )
        for cell in CELLS
    }


def in_admissible_cone(field: dict) -> bool:
    return all(volume > 0 and sp.Abs(shear) < 1 for shear, volume in field.values())


TEMPORAL_LINKS = tuple(
    ((t, x), (t + 1, x)) for t in range(COVER_T) for x in range(LX)
)
SPATIAL_LINKS = tuple(
    ((t, x), (t, x + 1)) for t in range(COVER_T) for x in range(LX)
)
ALL_LINKS = TEMPORAL_LINKS + SPATIAL_LINKS
PLAQUETTES = tuple((t, x) for t in range(COVER_T) for x in range(LX))


def link_field(assignment: dict) -> dict:
    """Ordered U(1) links, with the reverse orientation conjugated."""
    field = {}
    for (source, target), value in assignment.items():
        field[(fixture.cover_index(*source), fixture.cover_index(*target))] = sp.expand(value)
        field[(fixture.cover_index(*target), fixture.cover_index(*source))] = sp.expand(
            sp.conjugate(value)
        )
    return field


def dress(matrix: sp.MatrixBase, field: dict) -> sp.Matrix:
    out = sp.Matrix(matrix)
    for (source, target), value in field.items():
        if out[target, source] != 0:
            out[target, source] = sp.expand(out[target, source] * value)
    return out


def holonomy(field: dict, plaquette: tuple[int, int]) -> sp.Expr:
    t, x = plaquette
    loop = (
        ((t, x), (t, x + 1)),
        ((t, x + 1), (t + 1, x + 1)),
        ((t + 1, x + 1), (t + 1, x)),
        ((t + 1, x), (t, x)),
    )
    product = sp.Integer(1)
    for source, target in loop:
        product *= field.get(
            (fixture.cover_index(*source), fixture.cover_index(*target)), 1
        )
    return sp.simplify(sp.expand(product))


def holonomy_census(field: dict) -> tuple[tuple, tuple]:
    values = tuple(holonomy(field, plaquette) for plaquette in PLAQUETTES)
    nontrivial = tuple(
        (PLAQUETTES[index], value)
        for index, value in enumerate(values)
        if sp.simplify(value - 1) != 0
    )
    return values, nontrivial


def pure_gauge_field(phases: dict) -> dict:
    assignment = {}
    for source, target in ALL_LINKS:
        omega_source = phases.get((source[0] % COVER_T, source[1] % LX), 1)
        omega_target = phases.get((target[0] % COVER_T, target[1] % LX), 1)
        assignment[(source, target)] = sp.expand(
            omega_target * sp.conjugate(omega_source)
        )
    return link_field(assignment)


def reweight(matrix: sp.MatrixBase, prefix: str) -> tuple[sp.Matrix, int]:
    out = sp.Matrix(matrix)
    count = 0
    for row in range(out.rows):
        for column in range(out.cols):
            if out[row, column] != 0:
                out[row, column] = sp.Symbol(f"{prefix}_{count}")
                count += 1
    return out, count


def link_occurrence_balance() -> dict:
    """Signed occurrence count of each unoriented link in all plaquettes."""
    ordered = {
        (fixture.cover_index(*source), fixture.cover_index(*target))
        for source, target in ALL_LINKS
    }
    balance = collections.Counter()
    for t, x in PLAQUETTES:
        loop = (
            ((t, x), (t, x + 1)),
            ((t, x + 1), (t + 1, x + 1)),
            ((t + 1, x + 1), (t + 1, x)),
            ((t + 1, x), (t, x)),
        )
        for source, target in loop:
            key = tuple(
                sorted(
                    (
                        (source[0] % COVER_T, source[1] % LX),
                        (target[0] % COVER_T, target[1] % LX),
                    )
                )
            )
            orientation = (
                fixture.cover_index(*source), fixture.cover_index(*target)
            )
            balance[key] += 1 if orientation in ordered else -1
    return dict(balance)


COVER_FREE = cover_hodge_general(*FREE_MODULI)
HQ_FREE = quotient(COVER_FREE)
ODD_SELECTOR = sp.Matrix(
    [[1 if coordinate == moment else 0 for coordinate in COORDS] for moment in ODD_SHEAR_COORDS]
)


def file_sha256(relative_path: str) -> str | None:
    path = ROOT / relative_path
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_input_hashes(expected: dict[str, str]) -> tuple[bool, dict[str, str | None]]:
    actual = {path: file_sha256(path) for path in expected}
    return actual == expected, actual


@dataclass
class Checks:
    results: list[tuple[str, bool, str]]

    def __init__(self) -> None:
        self.results = []

    def add(self, name: str, condition: bool, detail: str) -> None:
        self.results.append((name, bool(condition), detail))

    def emit(self) -> int:
        for name, ok, detail in self.results:
            print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        passed = sum(ok for _, ok, _ in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return 0 if failed == 0 else 1
