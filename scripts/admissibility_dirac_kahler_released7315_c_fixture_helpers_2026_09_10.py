#!/usr/bin/env python3
"""Exact finite constructors for corrected released-7315 Blocks 167--170.

This module extracts only the size-parametric sparse fixture and small matrix
utilities needed by the four corrected producers.  It imports the accepted
released-7315-A helper for the local cell matrices and healing data.  It does
not import the historical 40-script theorem chain or the concurrent B repair.

All inertia triples in this module and its consumers use the order
``(n_positive, n_zero, n_negative)``.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10 as a


SOURCE_AST_MAP = {
    "block165_sparse_extract": {
        "path": "scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py",
        "source_sha256": "ed55383a5f15a0ff18c528f2ed33afa2e9f90c5d5d92125249a845fa3c17db18",
        "nodes": {
            "smul": [419, 428],
            "sadd": [431, 437],
            "sscale": [440, 445],
            "sdagger": [448, 452],
            "sclean": [455, 456],
            "dense": [459, 463],
            "Fixture": [481, 725],
        },
    },
    "block166_region_extract": {
        "path": "scripts/admissibility_dirac_kahler_interpretation_discriminators_2026_08_21.py",
        "source_sha256": "13e2bcd055ebe986d72bd05bf568d68a31021afbd7a8b1f0edd3cb5f92ed42ae",
        "nodes": {
            "ssubs": [468, 472],
            "region_pin": [475, 483],
            "hodge_trace_D": [486, 495],
            "graded_carrier": [504, 513],
            "carrier_substitution": [516, 524],
            "region_pairing": [527, 533],
        },
    },
}

R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]

ORIGINS = a.ORIGINS
CHART_INDEX = {origin: position for position, origin in enumerate(ORIGINS)}
HEALING_WEIGHTS = a.HEALING_WEIGHTS
EX = a.fixture.block105.EX
ET = a.fixture.block105.ET
SHIFT_T, SHIFT_X = a.fixture.block105.shift_lifts()
SX, ST = sp.symbols("s_x s_t", real=True)
MASS = sp.Symbol("m", real=True)


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(entry) == 0 for entry in sp.Matrix(matrix))


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix + matrix.H) / 2)


def no_float(value: object) -> bool:
    return a.no_float(value)


def inertia_pzn(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact Hermitian inertia in (positive, zero, negative) order."""
    return a.congruence_inertia(sp.Matrix(matrix))


def is_psd(matrix: sp.MatrixBase) -> bool:
    return inertia_pzn(matrix)[2] == 0


def free_symbols_of(matrix: sp.MatrixBase) -> set[sp.Symbol]:
    out: set[sp.Symbol] = set()
    for entry in sp.Matrix(matrix):
        out |= sp.expand(entry).free_symbols
    return out


def file_sha256(relative_path: str) -> str | None:
    path = ROOT / relative_path
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def verify_input_hashes(expected: dict[str, str]) -> tuple[bool, dict[str, str | None]]:
    actual = {path: file_sha256(path) for path in expected}
    return actual == expected, actual


Checks = a.Checks


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
    return sclean({
        key: sp.expand(value.subs(mapping)) if hasattr(value, "subs") else value
        for key, value in matrix.items()
    })


def dense(matrix: dict, rows: int, columns: int) -> sp.Matrix:
    out = sp.zeros(rows, columns)
    for (row, column), value in matrix.items():
        out[row, column] = value
    return out


def coefficient_rank(matrix: sp.MatrixBase, variables) -> int:
    variables = tuple(variables)
    rows = []
    for entry in sp.Matrix(matrix):
        real, imag = sp.expand(entry).as_real_imag()
        rows.append([sp.diff(real, variable) for variable in variables])
        rows.append([sp.diff(imag, variable) for variable in variables])
    return sp.Matrix(rows).rank() if rows else 0


class Fixture:
    """The supplied antiperiodic cell construction at one even finite size."""

    def __init__(self, cover_t: int, lx: int, tag: str) -> None:
        if cover_t % 2 or lx % 2:
            raise ValueError("the supplied 2-by-2 construction requires even extents")
        self.tag = tag
        self.COVER_T = cover_t
        self.LX = lx
        self.PHYS_T = cover_t // 2
        self.SIZE = cover_t * lx
        self.PHYS = self.PHYS_T * lx
        self.CELLS = tuple(
            (time, space)
            for time in range(self.PHYS_T)
            for space in range(self.LX)
        )
        self.NU = {
            cell: sp.Symbol(f"n_{tag}_{cell[0]}_{cell[1]}", real=True)
            for cell in self.CELLS
        }
        self.A = {
            cell: sp.Symbol(f"a_{tag}_{cell[0]}_{cell[1]}", real=True)
            for cell in self.CELLS
        }
        self.B = {
            cell: sp.Symbol(f"b_{tag}_{cell[0]}_{cell[1]}", real=True)
            for cell in self.CELLS
        }
        self.MU = {
            cell: sp.Symbol(f"u_{tag}_{cell[0]}_{cell[1]}", real=True)
            for cell in self.CELLS
        }
        self.SHEARS = frozenset(self.B.values())
        self.EDGE_KEYS = tuple(
            (CHART_INDEX[left], CHART_INDEX[right])
            for left in ORIGINS
            for right in ORIGINS
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

    def connection_for(self, gx, gt, generator_t: sp.MatrixBase = ET) -> dict:
        local = sp.expand(gx * EX + gt * sp.Matrix(generator_t))
        chart_d: dict = {}
        for origin in ORIGINS:
            gauge = (SHIFT_T ** origin[0]) * (SHIFT_X ** origin[1])
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
            for left in ORIGINS
            for right in ORIGINS
        }

    def cover_hodge(self, nu, aa, bb, inverse) -> dict:
        out: dict = {}

        def bump(row: int, column: int, value) -> None:
            out[(row, column)] = out.get((row, column), 0) + value

        for time in range(self.COVER_T):
            for space in range(self.LX):
                cell = (time % self.PHYS_T, space)
                s00, s01, s10, s11 = self.cell_sites(time, space)
                bump(s00, s00, nu[cell] / 4)
                bump(s01, s01, aa[cell] / 4)
                bump(s10, s10, aa[cell] / 4)
                bump(s11, s11, inverse[cell] / 4)
                bump(s01, s10, bb[cell] / 4)
                bump(s10, s01, bb[cell] / 4)
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
        nu, aa, bb, inverse = {}, {}, {}, {}
        for cell, (shear, volume) in field.items():
            shear = sp.sympify(shear)
            volume = sp.sympify(volume)
            nu[cell] = volume
            aa[cell] = sp.cancel(volume / (1 - shear ** 2))
            bb[cell] = sp.cancel(-volume * shear / (1 - shear ** 2))
            inverse[cell] = sp.cancel(sp.Integer(1) / volume)
        return nu, aa, bb, inverse

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
        return self.quotient(sscale(sadd(
            smul(hodge, differential),
            smul(sdagger(differential), hodge),
        ), I))

    def quotient_action(self, differential: dict, hodge: dict, mass=MASS) -> dict:
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
            label for label in self.site_labels
            if self._is_involutive(self.descent(label))
        )
        self.x_trivial = tuple(
            label for label in self.involutive
            if (label[2], label[3]) == (1, 0)
        )
        self.non_x_trivial = tuple(
            label for label in self.involutive if label not in set(self.x_trivial)
        )

    def fixed_slice(self, label: tuple[int, int, int, int]) -> int:
        return (label[1] // 2) % self.PHYS_T

    def slice_rows(self, *slices: int) -> tuple[int, ...]:
        return tuple(
            self.LX * (time % self.PHYS_T) + space
            for time in slices
            for space in range(self.LX)
        )

    def pairing(self, reflection: dict, action: dict, rows: tuple[int, ...]) -> sp.Matrix:
        index = {row: position for position, row in enumerate(rows)}
        product = smul(reflection, action)
        out = sp.zeros(len(rows), len(rows))
        for (row, column), value in product.items():
            if row in index and column in index:
                out[index[row], index[column]] = value
        return herm(out)


def region_pin(fixture: Fixture, links) -> dict:
    substitution: dict = {}
    for link in links:
        time = link % fixture.PHYS_T
        for space in range(fixture.LX):
            substitution[fixture.B[(time, space)]] = sp.Integer(0)
            substitution[fixture.A[(time, space)]] = fixture.NU[(time, space)]
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
    nu, aa, bb, inverse = fixture.moduli_from_field(field)
    substitution: dict = {}
    for cell in fixture.CELLS:
        substitution[fixture.NU[cell]] = nu[cell]
        substitution[fixture.A[cell]] = aa[cell]
        substitution[fixture.B[cell]] = bb[cell]
        substitution[fixture.MU[cell]] = inverse[cell]
    return substitution


def site_label(fixture: Fixture, c: int) -> tuple[int, int, int, int]:
    return next(label for label in fixture.x_trivial if fixture.fixed_slice(label) == c)


def link_labels_x_trivial(fixture: Fixture) -> tuple[tuple[int, int, int, int], ...]:
    return tuple(
        label for label in fixture.link_labels
        if (label[2], label[3]) == (1, 0)
    )


def block_operator(fixture: Fixture, blocks: dict[tuple[int, int], sp.MatrixBase]) -> dict:
    out: dict = {}
    for (target_t, source_t), block in blocks.items():
        block = sp.Matrix(block)
        for target_x in range(fixture.LX):
            for source_x in range(fixture.LX):
                value = block[target_x, source_x]
                if value != 0:
                    out[(
                        fixture.LX * (target_t % fixture.PHYS_T) + target_x,
                        fixture.LX * (source_t % fixture.PHYS_T) + source_x,
                    )] = value
    return sclean(out)


def cover_displacement_two(fixture: Fixture, block: sp.MatrixBase, coefficient) -> dict:
    block = sp.Matrix(block)
    out: dict = {}
    for time in range(fixture.COVER_T):
        target = (time + 2) % fixture.COVER_T
        for target_x in range(fixture.LX):
            for source_x in range(fixture.LX):
                value = block[target_x, source_x]
                if value != 0:
                    forward = (fixture.LX * target + target_x, fixture.LX * time + source_x)
                    reverse = (fixture.LX * time + source_x, fixture.LX * target + target_x)
                    out[forward] = out.get(forward, 0) + coefficient * value
                    out[reverse] = out.get(reverse, 0) + coefficient * sp.conjugate(value)
    return fixture.quotient(sclean(out))


def displacement_two_shift(fixture: Fixture, coefficient, backward: bool = False) -> dict:
    out: dict = {}
    step = -2 if backward else 2
    for time in range(fixture.COVER_T):
        target = (time + step) % fixture.COVER_T
        for space in range(fixture.LX):
            out[(fixture.LX * target + space, fixture.LX * time + space)] = coefficient
    return sclean(out)


def first_order(fixture: Fixture, hodge: dict, differential: dict) -> dict:
    return fixture.quotient(sscale(sadd(
        smul(hodge, differential),
        smul(sdagger(differential), hodge),
    ), I))


def second_order(fixture: Fixture, hodge: dict, left: dict, right: dict) -> dict:
    return fixture.quotient(sadd(
        smul(sdagger(left), smul(hodge, right)),
        smul(sdagger(right), smul(hodge, left)),
    ))


@dataclass
class Bench:
    fixture: Fixture
    c: int = 1

    def __post_init__(self) -> None:
        self.label = site_label(self.fixture, self.c)
        self.reflection = self.fixture.descent(self.label)
        self.rows = self.fixture.slice_rows(self.c, self.c + 1)
        self.pin = region_pin(self.fixture, (self.c - 1, self.c))
        self.hodge = ssubs(self.fixture.H_free, self.pin)
        self.action = self.fixture.quotient_action(
            self.fixture.edge_d[(0, 0)], self.hodge, MASS
        )
        self.form = self.fixture.pairing(self.reflection, self.action, self.rows)

    @property
    def lx(self) -> int:
        return self.fixture.LX

    def carrier(self, shear=R(3, 5), sx=R(3, 5), st=R(1, 2), mass=sp.Integer(1)) -> dict:
        substitution = carrier_substitution(
            self.fixture, graded_carrier(self.fixture, self.c, shear)
        )
        substitution.update({SX: sx, ST: st, MASS: mass})
        return substitution

    def pair_action(self, action: dict) -> sp.Matrix:
        return self.fixture.pairing(self.reflection, action, self.rows)


def fixed_support_components(matrix: sp.MatrixBase) -> int:
    matrix = sp.Matrix(matrix)
    parent = list(range(matrix.rows))

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if row != column and sp.expand(matrix[row, column]) != 0:
                left, right = find(row), find(column)
                if left != right:
                    parent[left] = right
    return len({find(node) for node in range(matrix.rows)})
