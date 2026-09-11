#!/usr/bin/env python3
"""Bounded finite fixture for the released PR7333 compiler calculation.

This module extracts only the construction definitions used by the three
recovered strict-neighbor compiler runners.  It builds the disclosed
antiperiodic covers, the selected self-edge differential, the pinned Hodge
quotient, the supplied carrier substitutions, the finite positive completion,
and the local Gram factor.  The formulas are traced to the historical
Block 43 -> 41 -> 175 -> 174 -> 171 -> 170 -> 166 -> 165 runtime chain.

The staggered matrices and shift lifts come from the current reviewed
Block 105 source and are content-bound below.  No historical theorem,
physical interpretation, probability law, action-selection rule, or audit
status is imported by this extraction.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from types import SimpleNamespace

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14 as block105


BLOCK105_PATH = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)
BLOCK105_SHA256 = (
    "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445"
)

R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
I = sp.I

SX = sp.Symbol("s_x", real=True)
ST = sp.Symbol("s_t", real=True)
MASS = sp.Symbol("m", real=True)

SLICE_C = 1
CARRIER_SIGMA = R(3, 5)
BENCH_SX = R(3, 5)
BENCH_MASS = ONE

MENU = (ZERO, R(1, 5), R(2, 5), R(3, 5))
RECORD_LEVEL = 2
RECORD_CELL = (RECORD_LEVEL, 0)
LX = 4
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def supplier_certificate() -> bool:
    """Bind the current Block 105 bytes and used finite constructions."""
    rt, rx = block105.shift_lifts()
    return bool(
        sha256_path(ROOT / BLOCK105_PATH) == BLOCK105_SHA256
        and block105.EX
        == sp.Matrix(
            [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
        )
        and block105.ET
        == sp.Matrix(
            [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, -1, 0, 0]]
        )
        and rt.shape == (4, 4)
        and rx.shape == (4, 4)
        and sp.expand(rt.H * rt) == sp.eye(4)
        and sp.expand(rx.H * rx) == sp.eye(4)
    )


def smul(left: dict, right: dict) -> dict:
    rows: dict = {}
    for (middle, column), value in right.items():
        rows.setdefault(middle, []).append((column, value))
    output: dict = {}
    for (row, middle), value in left.items():
        for column, other in rows.get(middle, ()):
            output[(row, column)] = (
                output.get((row, column), ZERO) + value * other
            )
    return {
        key: sp.expand(value)
        for key, value in output.items()
        if sp.expand(value) != 0
    }


def sadd(*terms: dict) -> dict:
    output: dict = {}
    for term in terms:
        for key, value in term.items():
            output[key] = output.get(key, ZERO) + value
    return {
        key: sp.expand(value)
        for key, value in output.items()
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
            key: (
                sp.expand(value.subs(mapping))
                if hasattr(value, "subs")
                else value
            )
            for key, value in matrix.items()
        }
    )


def dense(matrix: dict, rows: int, columns: int) -> sp.Matrix:
    output = sp.zeros(rows, columns)
    for (row, column), value in matrix.items():
        output[row, column] = value
    return output


def exact_inv(matrix: sp.MatrixBase) -> sp.Matrix:
    """Invert exactly in the fraction field selected by SymPy."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).to_field().inv().to_Matrix()


def dm_det(matrix: sp.MatrixBase):
    """Compute an exact determinant through DomainMatrix."""
    domain_matrix = DomainMatrix.from_Matrix(sp.Matrix(matrix))
    return sp.expand(
        domain_matrix.domain.to_sympy(domain_matrix.det())
    )


def norm2(value):
    """Return |value|^2 for the exact Gaussian-rational inputs used here."""
    return sp.cancel(sp.re(value) ** 2 + sp.im(value) ** 2)


class _Cover:
    """Sparse selected-self-edge cover used by the recovered finite fixtures."""

    def __init__(self, cover_t: int, lx: int) -> None:
        if cover_t <= 0 or cover_t % 2 or lx <= 0 or lx % 2:
            raise ValueError("cover_t and lx must be positive even integers")
        self.COVER_T = cover_t
        self.LX = lx
        self.PHYS_T = cover_t // 2
        self.SIZE = cover_t * lx
        self.PHYS = self.PHYS_T * lx
        self.CELLS = tuple(
            (time, space)
            for time in range(self.PHYS_T)
            for space in range(lx)
        )
        self.NU = {
            cell: sp.Symbol(f"n_{cell[0]}_{cell[1]}", real=True)
            for cell in self.CELLS
        }
        self.A = {
            cell: sp.Symbol(f"a_{cell[0]}_{cell[1]}", real=True)
            for cell in self.CELLS
        }
        self.B = {
            cell: sp.Symbol(f"b_{cell[0]}_{cell[1]}", real=True)
            for cell in self.CELLS
        }
        self.MU = {
            cell: sp.Symbol(f"u_{cell[0]}_{cell[1]}", real=True)
            for cell in self.CELLS
        }
        self.edge_d = {(0, 0): self._selected_self_edge()}
        self.H_free = self.cover_hodge(self.NU, self.A, self.B, self.MU)

    def cover_index(self, time: int, space: int) -> int:
        return (time % self.COVER_T) * self.LX + (space % self.LX)

    def cell_sites(self, time: int, space: int) -> tuple[int, ...]:
        return tuple(
            self.cover_index(time + dt, space + dx)
            for dt, dx in ((0, 0), (0, 1), (1, 0), (1, 1))
        )

    def chart_cells(self) -> tuple[tuple[int, int], ...]:
        return tuple(
            (2 * chart_time, 2 * chart_space)
            for chart_time in range(self.COVER_T // 2)
            for chart_space in range(self.LX // 2)
        )

    def _selected_self_edge(self) -> dict:
        # The historical selected edge has identical chart labels, so the
        # historical healing-weight difference is exactly zero.  Its live
        # content is the current Block 105 origin-(0,0) connection.
        rt, rx = block105.shift_lifts()
        gauge = (rt ** 0) * (rx ** 0)
        local = sp.expand(
            gauge.H
            * (I * (SX * block105.EX + ST * block105.ET))
            * gauge
        )
        output: dict = {}
        for anchor in self.chart_cells():
            sites = self.cell_sites(*anchor)
            for row in range(4):
                for column in range(4):
                    if local[row, column] != 0:
                        key = (sites[row], sites[column])
                        output[key] = (
                            output.get(key, ZERO) + local[row, column]
                        )
        return sclean(output)

    def cover_hodge(self, nu, a, b, mu) -> dict:
        output: dict = {}

        def bump(row: int, column: int, value) -> None:
            output[(row, column)] = (
                output.get((row, column), ZERO) + value
            )

        for time in range(self.COVER_T):
            for space in range(self.LX):
                cell = (time % self.PHYS_T, space)
                s00, s01, s10, s11 = self.cell_sites(time, space)
                bump(s00, s00, nu[cell] / 4)
                bump(s01, s01, a[cell] / 4)
                bump(s10, s10, a[cell] / 4)
                bump(s11, s11, mu[cell] / 4)
                bump(s01, s10, b[cell] / 4)
                bump(s10, s01, b[cell] / 4)
        return sclean(output)

    def moduli_from_field(self, field: dict) -> tuple:
        nu, a, b, mu = {}, {}, {}, {}
        for cell, (shear, volume_value) in field.items():
            shear = sp.sympify(shear)
            volume_value = sp.sympify(volume_value)
            nu[cell] = volume_value
            a[cell] = volume_value / (1 - shear ** 2)
            b[cell] = -volume_value * shear / (1 - shear ** 2)
            mu[cell] = 1 / volume_value
        return nu, a, b, mu

    def quotient(self, matrix: dict) -> dict:
        """Apply the historical antiperiodic half-cover fold."""
        output: dict = {}
        for (row, column), value in matrix.items():
            if row < self.PHYS:
                continue
            if column >= self.PHYS:
                key = (row - self.PHYS, column - self.PHYS)
                output[key] = output.get(key, ZERO) + value
            else:
                key = (row - self.PHYS, column)
                output[key] = output.get(key, ZERO) - value
        return sclean(output)

    def quotient_connection(self, differential: dict, hodge: dict) -> dict:
        return self.quotient(
            sscale(
                sadd(
                    smul(hodge, differential),
                    smul(sdagger(differential), hodge),
                ),
                I,
            )
        )


def region_pin(fixture: _Cover, links) -> dict:
    output: dict = {}
    for slot in links:
        slot %= fixture.PHYS_T
        for space in range(fixture.LX):
            output[fixture.B[(slot, space)]] = ZERO
            output[fixture.A[(slot, space)]] = fixture.NU[(slot, space)]
    return output


def carrier_substitution(fixture: _Cover, field: dict) -> dict:
    nu, a, b, mu = fixture.moduli_from_field(field)
    output: dict = {}
    for cell in fixture.CELLS:
        output[fixture.NU[cell]] = nu[cell]
        output[fixture.A[cell]] = a[cell]
        output[fixture.B[cell]] = b[cell]
        output[fixture.MU[cell]] = mu[cell]
    return output


class _Bench:
    """Symbolic pinned quotient action at one disclosed cover."""

    def __init__(self, cover_t: int, lx: int) -> None:
        self.fx = _Cover(cover_t, lx)
        self.c = SLICE_C
        self.lx = lx
        self.T = self.fx.PHYS_T
        self.N = self.fx.PHYS
        pin = region_pin(self.fx, (self.c - 1, self.c))
        hodge = ssubs(self.fx.H_free, pin)
        self.Hq = dense(self.fx.quotient(hodge), self.N, self.N)
        self.Kq = dense(
            self.fx.quotient_connection(self.fx.edge_d[(0, 0)], hodge),
            self.N,
            self.N,
        )
        self.Q = sp.expand(MASS * self.Hq + self.Kq)


def xgraded_volume(time: int, space: int):
    return R(1 + (3 * time + 2 * space) % 5, 3) + R(1, 2)


class Fixture:
    """Q-only finite fixture used by the recovered PR7333 runners."""

    def __init__(
        self,
        lx: int,
        pattern=None,
        tag: str = "released7333",
        cover_t: int = 12,
    ) -> None:
        self.tag = tag
        self.lx = lx
        self.cover_t = cover_t
        self.pattern = (
            None
            if pattern is None
            else tuple(sp.sympify(value) for value in pattern)
        )
        if self.pattern is not None and len(self.pattern) != lx:
            raise ValueError("pattern length must equal lx")
        self.bench = _Bench(cover_t, lx)
        self.fx = self.bench.fx
        self.c = self.bench.c
        self.T = self.bench.T
        self.N = self.bench.N
        self.free_levels = tuple(
            time
            for time in range(self.T)
            if time not in {(self.c - 1) % self.T, self.c}
        )
        self.tstar = self.free_levels[-1]

    def volume(self, time: int, space: int):
        if self.pattern is None:
            return xgraded_volume(time, space)
        return self.pattern[space % self.lx]

    def field(self, sigma, records: dict) -> dict:
        pinned = {(self.c - 1) % self.T, self.c}
        return {
            (time, space): (
                ZERO
                if time in pinned
                else sp.sympify(records.get((time, space), sigma)),
                self.volume(time, space),
            )
            for time, space in self.fx.CELLS
        }

    def substitution(self, sigma, records, sx, st, mass) -> dict:
        output = carrier_substitution(
            self.fx,
            self.field(sigma, records),
        )
        output[SX] = sp.sympify(sx)
        output[ST] = sp.sympify(st)
        output[MASS] = sp.sympify(mass)
        return output

    def q(
        self,
        records: dict | None = None,
        sigma=CARRIER_SIGMA,
        sx=BENCH_SX,
        st=ZERO,
        mass=BENCH_MASS,
        action: str = "bench",
        **_unused,
    ) -> sp.Matrix:
        if action != "bench":
            raise ValueError(
                "released7333 fixture extracts only the used bench action"
            )
        substitution = self.substitution(
            sigma,
            records or {},
            sx,
            st,
            mass,
        )
        return sp.expand(self.bench.Q.subs(substitution))


def constant_pattern(lx: int) -> tuple:
    return (ONE,) * lx


def positive_completion(q: sp.MatrixBase) -> dict:
    """Finite positive completion reconstructed directly from q."""
    q_matrix = sp.Matrix(q)
    q_inverse = exact_inv(q_matrix)
    symmetric = sp.expand((q_matrix + q_matrix.H) / 2)
    symmetric_inverse = exact_inv(symmetric)
    covariance = sp.expand((q_inverse + q_inverse.H) / 2)
    precision = sp.expand(q_matrix.H * symmetric_inverse * q_matrix)
    return {
        "q_inv": q_inverse,
        "symmetric": symmetric,
        "covariance": covariance,
        "precision": precision,
    }


def slice_rows(fixture: object, level: int) -> tuple[int, ...]:
    return tuple(
        fixture.lx * (level % fixture.T) + space
        for space in range(fixture.lx)
    )


def edge_union(
    matrices: tuple[sp.MatrixBase, ...],
) -> tuple[tuple[int, int], ...]:
    size = matrices[0].rows
    return tuple(
        (row, column)
        for row in range(size)
        for column in range(row + 1, size)
        if any(matrix[row, column] != 0 for matrix in matrices)
    )


def signed_edge_factor(
    symmetric: sp.MatrixBase,
    innovation_variance,
    edges: tuple[tuple[int, int], ...],
) -> tuple[sp.Matrix, tuple]:
    """Return the finite local Gram factor of symmetric-cI."""
    size = symmetric.rows
    factor = sp.zeros(size, len(edges) + size)
    incident = [ZERO for _ in range(size)]
    for index, (row, column) in enumerate(edges):
        weight = sp.cancel(symmetric[row, column])
        if weight == 0:
            continue
        magnitude = sp.Abs(weight)
        root = sp.sqrt(magnitude)
        factor[row, index] = root
        factor[column, index] = sp.sign(weight) * root
        incident[row] += magnitude
        incident[column] += magnitude
    residuals = tuple(
        sp.cancel(
            symmetric[row, row] - innovation_variance - incident[row]
        )
        for row in range(size)
    )
    for row, residual in enumerate(residuals):
        if residual.is_nonnegative:
            factor[row, len(edges) + row] = sp.sqrt(residual)
    return factor, residuals


def arm_bundle(
    fixture: object,
    value,
    edges: tuple[tuple[int, int], ...],
    mass=ONE,
    fraction=R(1, 2),
) -> dict:
    """Construct one supplied finite Gaussian arm without importing a theorem."""
    q = fixture.q({RECORD_CELL: value}, mass=mass)
    completion = positive_completion(q)
    symmetric = completion["symmetric"]
    variance = sp.cancel(sp.sympify(mass) * sp.sympify(fraction))
    factor, residuals = signed_edge_factor(
        symmetric,
        variance,
        edges,
    )
    inverse = completion["q_inv"]
    covariance = sp.expand(
        inverse
        * (factor * factor.H + variance * sp.eye(fixture.N))
        * inverse.H
    )
    determinant = dm_det(q)
    return {
        "value": value,
        "q": q,
        "q_inv": inverse,
        "S": symmetric,
        "B": factor,
        "residuals": residuals,
        "variance": variance,
        "W": completion["covariance"],
        "covariance": covariance,
        "det_q": determinant,
        "raw_mass": sp.cancel(variance ** fixture.N / norm2(determinant)),
    }


b174 = SimpleNamespace(
    Fixture=Fixture,
    MENU=MENU,
    RECORD_LEVEL=RECORD_LEVEL,
    constant_pattern=constant_pattern,
    dm_det=dm_det,
    norm2=norm2,
)
b175 = SimpleNamespace(
    MENU=MENU,
    RECORD_CELL=RECORD_CELL,
    LX=LX,
    b174=b174,
)
b41 = SimpleNamespace(
    b174=b174,
    b175=b175,
    positive_completion=positive_completion,
    slice_rows=slice_rows,
)
b42 = SimpleNamespace(
    DIRECTIONS=DIRECTIONS,
    b174=b174,
    b175=b175,
    b41=b41,
)
