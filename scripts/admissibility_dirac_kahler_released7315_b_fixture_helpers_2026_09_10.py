#!/usr/bin/env python3
"""Exact finite helpers for corrected released-7315 Blocks 160--166.

The committed 8-by-4 constructors come from corrected Block 159 and its
released-7315-A helper.  The sparse ``Fixture`` below is the bounded
size-parametric reconstruction used by the historical Blocks 165--166, with
the same local 2-by-2 cell matrices and antiperiodic quotient.  Historical
authority and deep-scan machinery is deliberately not imported.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_link_curvature_scout_2026_08_20 as b159


h = b159.h
R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]

ORIGINS = h.ORIGINS
CHART_INDEX = {origin: position for position, origin in enumerate(ORIGINS)}
HEALING_WEIGHTS = h.HEALING_WEIGHTS
EX = h.fixture.block105.EX
ET = h.fixture.block105.ET
SX, ST = sp.symbols("s_x s_t", real=True)
MASS = sp.Symbol("m", real=True)


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(entry) == 0 for entry in sp.Matrix(matrix))


def no_float(value: object) -> bool:
    return h.no_float(value)


def inertia_pzn(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact inertia in the explicit (positive, zero, negative) order."""
    return h.congruence_inertia(sp.Matrix(matrix))


def is_psd_pzn(matrix: sp.MatrixBase) -> bool:
    return inertia_pzn(matrix)[2] == 0


def free_symbols_of(matrix: sp.MatrixBase) -> set[sp.Symbol]:
    symbols: set[sp.Symbol] = set()
    for entry in sp.Matrix(matrix):
        symbols |= sp.expand(entry).free_symbols
    return symbols


def file_sha256(relative_path: str) -> str | None:
    path = ROOT / relative_path
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_input_hashes(expected: dict[str, str]) -> tuple[bool, dict[str, str | None]]:
    actual = {path: file_sha256(path) for path in expected}
    return actual == expected, actual


Checks = h.Checks


# ---------------------------------------------------------------------------
# Dense 8-by-4 layer inherited from the corrected Block-159 supplier.
# ---------------------------------------------------------------------------
SIZE = h.SIZE
COVER_T = h.COVER_T
PHYS_T = h.PHYS_T
LX = h.LX
PHYS = h.PHYS
HALF = h.HALF
CELLS = h.CELLS
EDGE_KEYS = h.EDGE_KEYS
THETA = h.THETA
THETA_PRIME = h.THETA_PRIME
COMMITTED_ROWS = tuple(range(HALF))
EVEN_SLOTS = tuple(slot for slot in range(HALF) if slot % LX in (0, 2))
ODD_SLOTS = tuple(slot for slot in range(HALF) if slot not in EVEN_SLOTS)
EVEN_CELLS = ((0, 0), (0, 2), (2, 0), (2, 2))
ATLAS = {SX: R(3, 5), ST: R(4, 5)}


def dense_edges(sx=SX, st=ST, weights=HEALING_WEIGHTS) -> dict:
    differentials, star = h.connection(sx, st)
    return h.edge_differentials(differentials, star, weights)


def crossing_support(columns: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Antiperiodic temporal hops crossing the committed half boundary."""
    support: list[tuple[int, int]] = []
    for x in columns:
        for target_t, source_t in ((1, 2), (3, 4)):
            p = h.fixture.cover_index(target_t, x)
            q = h.fixture.cover_index(source_t, x)
            support.append((p, q))
            support.append(((p + PHYS) % SIZE, (q + PHYS) % SIZE))
    return tuple(support)


EVEN_SUPPORT = crossing_support((0, 2))
ODD_SUPPORT = crossing_support((1, 3))


def restrict_dense(matrix: sp.MatrixBase, support) -> sp.Matrix:
    out = sp.zeros(matrix.rows, matrix.cols)
    for row, column in support:
        out[row, column] = sp.expand(matrix[row, column])
    return out


def selector(rows: tuple[int, ...], dimension=PHYS) -> sp.Matrix:
    out = sp.zeros(dimension, len(rows))
    for column, row in enumerate(rows):
        out[row, column] = 1
    return out


def dense_pairing(
    reflection: sp.MatrixBase,
    action: sp.MatrixBase,
    rows: tuple[int, ...] = COMMITTED_ROWS,
) -> sp.Matrix:
    select = selector(rows, action.rows)
    raw = sp.expand(select.T * reflection * action * select)
    return sp.expand((raw + raw.H) / 2)


def dense_action_pairing(
    differential: sp.MatrixBase,
    field: dict,
    mass=sp.Integer(0),
    reflection: sp.MatrixBase = THETA,
    rows: tuple[int, ...] = COMMITTED_ROWS,
) -> sp.Matrix:
    hodge = h.cover_hodge_from_field(field)
    return dense_pairing(reflection, h.quotient_action(differential, hodge, mass), rows)


def field_of(shears: dict | None = None, volumes: dict | None = None) -> dict:
    shears = {} if shears is None else shears
    volumes = {} if volumes is None else volumes
    return {
        cell: (sp.sympify(shears.get(cell, 0)), sp.sympify(volumes.get(cell, 1)))
        for cell in CELLS
    }


def balanced_field() -> dict:
    """The curved Block-161 all-mass witness, in physical (sigma, nu) data."""
    return field_of(
        {
            (1, 0): R(1, 3), (1, 3): R(-1, 3),
            (1, 1): R(1, 3), (1, 2): R(-1, 3),
            (3, 0): R(1, 3), (3, 3): R(-1, 3),
            (3, 1): R(1, 3), (3, 2): R(-1, 3),
        }
    )


def odd_time_field(shear, volume) -> dict:
    return field_of(
        {cell: sp.sympify(shear) for cell in CELLS if cell[0] % 2},
        {cell: sp.sympify(volume) for cell in CELLS},
    )


def all_time_reflections() -> tuple[tuple[int, int, int, int], ...]:
    return tuple(
        (-1, pt, ex, px)
        for pt in range(COVER_T)
        for ex in (1, -1)
        for px in range(LX)
    )


def dense_descent(label: tuple[int, int, int, int]) -> sp.Matrix:
    matrix = h.descend(h.move_matrix(label))
    if matrix is None:
        raise ValueError(f"label does not descend: {label}")
    return matrix


def dense_involutive_site_labels() -> tuple[tuple[int, int, int, int], ...]:
    labels = tuple(label for label in all_time_reflections() if label[1] % 2 == 0)
    return tuple(label for label in labels if zero(dense_descent(label) ** 2 - sp.eye(PHYS)))


def fixed_slice(label: tuple[int, int, int, int]) -> int:
    return (label[1] // 2) % PHYS_T


def dense_slice_rows(*slices: int) -> tuple[int, ...]:
    return tuple(LX * (time % PHYS_T) + x for time in slices for x in range(LX))


# ---------------------------------------------------------------------------
# Sparse exact layer used to rebuild the same local construction at four sizes.
# ---------------------------------------------------------------------------
def smul(left: dict, right: dict) -> dict:
    rows: dict[int, list[tuple[int, sp.Expr]]] = {}
    for (middle, column), value in right.items():
        rows.setdefault(middle, []).append((column, value))
    out: dict = {}
    for (row, middle), value in left.items():
        for column, other in rows.get(middle, ()):
            out[(row, column)] = out.get((row, column), 0) + value * other
    return {
        key: sp.expand(value)
        for key, value in out.items()
        if sp.expand(value) != 0
    }


def sadd(*terms: dict) -> dict:
    out: dict = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, 0) + value
    return {
        key: sp.expand(value)
        for key, value in out.items()
        if sp.expand(value) != 0
    }


def sscale(matrix: dict, factor) -> dict:
    return {
        key: sp.expand(factor * value)
        for key, value in matrix.items()
        if sp.expand(factor * value) != 0
    }


def sdagger(matrix: dict) -> dict:
    return {
        (column, row): sp.expand(sp.conjugate(value))
        for (row, column), value in matrix.items()
    }


def sclean(matrix: dict) -> dict:
    return {
        key: sp.expand(value)
        for key, value in matrix.items()
        if sp.expand(value) != 0
    }


def ssubs(matrix: dict, mapping: dict) -> dict:
    return sclean(
        {
            key: sp.expand(value.subs(mapping)) if hasattr(value, "subs") else value
            for key, value in matrix.items()
        }
    )


def dense(matrix: dict, rows: int, columns: int) -> sp.Matrix:
    out = sp.zeros(rows, columns)
    for (row, column), value in matrix.items():
        out[row, column] = value
    return out


class Fixture:
    """The supplied antiperiodic cell construction at an even finite size."""

    def __init__(self, cover_t: int, lx: int, tag: str) -> None:
        if cover_t % 4 or lx % 2:
            raise ValueError("the supplied 2-by-2 construction needs cover_t divisible by 4 and lx even")
        self.tag = tag
        self.COVER_T = cover_t
        self.LX = lx
        self.PHYS_T = cover_t // 2
        self.SIZE = cover_t * lx
        self.PHYS = self.PHYS_T * lx
        self.CELLS = tuple(
            (t, x) for t in range(self.PHYS_T) for x in range(self.LX)
        )
        self.NU = {cell: sp.Symbol(f"n_{tag}_{cell[0]}_{cell[1]}", positive=True) for cell in self.CELLS}
        self.A = {cell: sp.Symbol(f"a_{tag}_{cell[0]}_{cell[1]}", positive=True) for cell in self.CELLS}
        self.B = {cell: sp.Symbol(f"b_{tag}_{cell[0]}_{cell[1]}", real=True) for cell in self.CELLS}
        self.MU = {cell: sp.Symbol(f"u_{tag}_{cell[0]}_{cell[1]}", positive=True) for cell in self.CELLS}
        self.SHEARS = frozenset(self.B.values())
        self.EDGE_KEYS = tuple(
            (CHART_INDEX[left], CHART_INDEX[right])
            for left in ORIGINS for right in ORIGINS
        )
        self.edge_d = self.connection_for(I * SX, I * ST)
        self.H_free = self.cover_hodge(self.NU, self.A, self.B, self.MU)
        self._build_reflections()

    def cover_index(self, time: int, space: int) -> int:
        return (time % self.COVER_T) * self.LX + (space % self.LX)

    def cell_sites(self, time: int, space: int) -> tuple[int, ...]:
        return tuple(
            self.cover_index(time + dt, space + dx)
            for dt, dx in ((0, 0), (0, 1), (1, 0), (1, 1))
        )

    def chart_cells(self, origin: tuple[int, int]) -> tuple[tuple[int, int], ...]:
        return tuple(
            (2 * cell_t + origin[0], 2 * cell_x + origin[1])
            for cell_t in range(self.COVER_T // 2)
            for cell_x in range(self.LX // 2)
        )

    def connection_for(self, gx, gt) -> dict:
        local = sp.expand(gx * EX + gt * ET)
        shift_t, shift_x = h.fixture.block105.shift_lifts()
        chart_d: dict = {}
        for origin in ORIGINS:
            gauge = (shift_t ** origin[0]) * (shift_x ** origin[1])
            block = sp.expand(gauge.H * local * gauge)
            out: dict = {}
            for anchor in self.chart_cells(origin):
                sites = self.cell_sites(*anchor)
                for row in range(4):
                    for column in range(4):
                        if block[row, column] != 0:
                            key = (sites[row], sites[column])
                            out[key] = out.get(key, 0) + block[row, column]
            chart_d[origin] = sclean(out)
        star = sadd(chart_d[(0, 0)], sscale(chart_d[(1, 0)], -1))
        return {
            (CHART_INDEX[left], CHART_INDEX[right]): sadd(
                chart_d[left],
                sscale(
                    star,
                    HEALING_WEIGHTS[CHART_INDEX[right]]
                    - HEALING_WEIGHTS[CHART_INDEX[left]],
                ),
            )
            for left in ORIGINS for right in ORIGINS
        }

    def cover_hodge(self, nu, a, b, inverse) -> dict:
        out: dict = {}

        def bump(row, column, value) -> None:
            out[(row, column)] = out.get((row, column), 0) + value

        for time in range(self.COVER_T):
            for space in range(self.LX):
                cell = (time % self.PHYS_T, space)
                s00, s01, s10, s11 = self.cell_sites(time, space)
                bump(s00, s00, nu[cell] / 4)
                bump(s01, s01, a[cell] / 4)
                bump(s10, s10, a[cell] / 4)
                bump(s11, s11, inverse[cell] / 4)
                bump(s01, s10, b[cell] / 4)
                bump(s10, s01, b[cell] / 4)
        return sclean(out)

    def flat_moduli(self) -> tuple[dict, dict, dict, dict]:
        one = sp.Integer(1)
        return (
            {cell: one for cell in self.CELLS},
            {cell: one for cell in self.CELLS},
            {cell: sp.Integer(0) for cell in self.CELLS},
            {cell: one for cell in self.CELLS},
        )

    def moduli_from_field(self, field: dict) -> tuple[dict, dict, dict, dict]:
        nu, a, b, inverse = {}, {}, {}, {}
        for cell, (shear, volume) in field.items():
            shear = sp.sympify(shear)
            volume = sp.sympify(volume)
            nu[cell] = volume
            a[cell] = sp.cancel(volume / (1 - shear ** 2))
            b[cell] = sp.cancel(-volume * shear / (1 - shear ** 2))
            inverse[cell] = sp.cancel(sp.Integer(1) / volume)
        return nu, a, b, inverse

    def quotient(self, matrix: dict) -> dict:
        out: dict = {}
        for (row, column), value in matrix.items():
            if row < self.PHYS:
                continue
            key = (
                row - self.PHYS,
                column - self.PHYS if column >= self.PHYS else column,
            )
            signed = value if column >= self.PHYS else -value
            out[key] = out.get(key, 0) + signed
        return sclean(out)

    def quotient_connection(self, differential: dict, hodge: dict) -> dict:
        return self.quotient(
            sscale(sadd(smul(hodge, differential), smul(sdagger(differential), hodge)), I)
        )

    def quotient_action(self, differential: dict, hodge: dict, mass) -> dict:
        return sadd(
            sscale(self.quotient(hodge), mass),
            self.quotient_connection(differential, hodge),
        )

    def parity(self) -> dict:
        return {
            (index, index): sp.Integer((-1) ** (index // self.LX + index % self.LX))
            for index in range(self.PHYS)
        }

    def lift_sign(self, time: int) -> int:
        return -1 if (time // self.PHYS_T) % 2 == 0 else 1

    def descent(self, label: tuple[int, int, int, int]) -> dict:
        _time_sign, shift_t, sign_x, shift_x = label
        out: dict = {}
        for time in range(self.PHYS_T):
            image_t = (shift_t - time) % self.PHYS_T
            sign = self.lift_sign(time) * self.lift_sign(shift_t - time)
            for space in range(self.LX):
                image_x = (sign_x * (space - shift_x)) % self.LX
                out[(self.LX * time + space, self.LX * image_t + image_x)] = sp.Integer(sign)
        return out

    def _is_involutive(self, reflection: dict) -> bool:
        identity = {(index, index): sp.Integer(1) for index in range(self.PHYS)}
        return sadd(smul(reflection, reflection), sscale(identity, -1)) == {}

    def _build_reflections(self) -> None:
        self.site_labels = tuple(
            (-1, shift_t, sign_x, shift_x)
            for shift_t in range(0, self.COVER_T, 2)
            for sign_x in (1, -1)
            for shift_x in range(self.LX)
        )
        self.link_labels = tuple(
            (-1, shift_t, sign_x, shift_x)
            for shift_t in range(1, self.COVER_T, 2)
            for sign_x in (1, -1)
            for shift_x in range(self.LX)
        )
        self.involutive = tuple(
            label for label in self.site_labels if self._is_involutive(self.descent(label))
        )
        self.x_trivial = tuple(
            label for label in self.involutive if (label[2], label[3]) == (1, 0)
        )
        self.non_x_trivial = tuple(
            label for label in self.involutive if label not in set(self.x_trivial)
        )

    def fixed_slice(self, label: tuple[int, int, int, int]) -> int:
        return (label[1] // 2) % self.PHYS_T

    def slice_rows(self, *slices: int) -> tuple[int, ...]:
        return tuple(
            self.LX * (time % self.PHYS_T) + space
            for time in slices for space in range(self.LX)
        )

    def pairing(self, reflection: dict, action: dict, rows: tuple[int, ...]) -> sp.Matrix:
        index = {row: position for position, row in enumerate(rows)}
        product = smul(reflection, action)
        out = sp.zeros(len(rows), len(rows))
        for (row, column), value in product.items():
            if row in index and column in index:
                out[index[row], index[column]] = value
        return sp.expand((out + out.H) / 2)

    def pinned_cells(self, c: int) -> frozenset[tuple[int, int]]:
        return frozenset(
            {((c - 1) % self.PHYS_T, x) for x in range(self.LX)}
            | {(c % self.PHYS_T, x) for x in range(self.LX)}
        )

    def free_cells(self, c: int) -> frozenset[tuple[int, int]]:
        return frozenset(set(self.CELLS) - self.pinned_cells(c))

    def region_substitution(self, c: int) -> dict:
        substitution: dict = {}
        for cell in self.pinned_cells(c):
            substitution[self.B[cell]] = sp.Integer(0)
            substitution[self.A[cell]] = self.NU[cell]
        return substitution


def region_pin(fixture: Fixture, links) -> dict:
    substitution: dict = {}
    for link in links:
        time = link % fixture.PHYS_T
        for x in range(fixture.LX):
            substitution[fixture.B[(time, x)]] = sp.Integer(0)
            substitution[fixture.A[(time, x)]] = fixture.NU[(time, x)]
    return substitution


def hodge_trace(fixture: Fixture) -> dict:
    return {
        (time, space): (
            fixture.NU[(time, space)]
            + fixture.A[((time - 1) % fixture.PHYS_T, space)]
            + fixture.A[(time, (space - 1) % fixture.LX)]
            + fixture.MU[((time - 1) % fixture.PHYS_T, (space - 1) % fixture.LX)]
        ) / 4
        for time, space in fixture.CELLS
    }


def graded_carrier(fixture: Fixture, c: int, shear) -> dict:
    pinned_times = {(c - 1) % fixture.PHYS_T, c % fixture.PHYS_T}
    return {
        (time, space): (
            sp.Integer(0) if time in pinned_times else sp.sympify(shear),
            R(1 + (3 * time + 5 * space) % 5, 3) + R(1, 2),
        )
        for time, space in fixture.CELLS
    }


def carrier_substitution(fixture: Fixture, field: dict) -> dict:
    nu, a, b, inverse = fixture.moduli_from_field(field)
    substitution: dict = {}
    for cell in fixture.CELLS:
        substitution[fixture.NU[cell]] = nu[cell]
        substitution[fixture.A[cell]] = a[cell]
        substitution[fixture.B[cell]] = b[cell]
        substitution[fixture.MU[cell]] = inverse[cell]
    return substitution


def region_pairing(
    fixture: Fixture,
    c: int,
    edge: dict,
    pinned_links=None,
    mass=MASS,
) -> tuple[sp.Matrix, dict]:
    if pinned_links is None:
        pinned_links = (c - 1, c)
    label = next(label for label in fixture.x_trivial if fixture.fixed_slice(label) == c)
    pin = region_pin(fixture, pinned_links)
    hodge = ssubs(fixture.H_free, pin)
    action = fixture.quotient_action(edge, hodge, mass)
    rows = fixture.slice_rows(c, c + 1)
    return fixture.pairing(fixture.descent(label), action, rows), pin


def coefficient_rank(matrix: sp.MatrixBase, variables) -> int:
    variables = tuple(variables)
    rows = [
        [sp.expand(entry).coeff(variable, 1) for variable in variables]
        for entry in sp.Matrix(matrix)
    ]
    return sp.Matrix(rows).rank()
