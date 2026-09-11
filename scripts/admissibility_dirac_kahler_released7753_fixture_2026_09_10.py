#!/usr/bin/env python3
"""Reviewed finite fixture used only by the repaired Block 212 calculation.

This module extracts the small part of the historical Block 171 -> 170 ->
165/166 construction that Block 212 actually evaluated.  It builds one fixed
12 x 4 antiperiodic cover, its selected self-edge differential, the pinned
Hodge quotient, the x-graded record substitution, and the W2/W9 diagonal
profiles.  It does not import or adopt the historical closure, its parent
theorems, its action interpretation, or a physical conditional law.

The staggered matrices and shift lifts come from the current reviewed Block
105 source.  The historical healing weights are absent because the selected
self edge has equal chart labels: their difference is identically zero.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

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
I = sp.I
SX = sp.Symbol("s_x", real=True)
ST = sp.Symbol("s_t", real=True)
MASS = sp.Symbol("m", real=True)

COVER_T = 12
LX = 4
PHYS_T = 6
PHYS = 24
SLICE_C = 1
CARRIER_SIGMA = R(3, 5)
BENCH_SX = R(3, 5)
BENCH_MASS = sp.Integer(1)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def supplier_certificate() -> bool:
    """Bind the current Block 105 bytes and the three imported constructions."""
    rt, rx = block105.shift_lifts()
    return bool(
        sha256_path(ROOT / BLOCK105_PATH) == BLOCK105_SHA256
        and block105.EX == sp.Matrix(
            [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
        )
        and block105.ET == sp.Matrix(
            [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, -1, 0, 0]]
        )
        and rt.shape == (4, 4)
        and rx.shape == (4, 4)
        and sp.expand(rt.H * rt) == sp.eye(4)
        and sp.expand(rx.H * rx) == sp.eye(4)
    )


def smul(left: dict, right: dict) -> dict:
    rows: dict = {}
    for (k, j), value in right.items():
        rows.setdefault(k, []).append((j, value))
    out: dict = {}
    for (i, k), value in left.items():
        for j, other in rows.get(k, ()):
            out[(i, j)] = out.get((i, j), 0) + value * other
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
        (j, i): sp.expand(sp.conjugate(value))
        for (i, j), value in matrix.items()
    }


def sclean(matrix: dict) -> dict:
    return {
        key: sp.expand(value)
        for key, value in matrix.items()
        if sp.expand(value) != 0
    }


def dense(matrix: dict, rows: int, cols: int) -> sp.Matrix:
    out = sp.zeros(rows, cols)
    for (i, j), value in matrix.items():
        out[i, j] = value
    return out


def ssubs(matrix: dict, mapping: dict) -> dict:
    return sclean(
        {
            key: sp.expand(value.subs(mapping))
            if hasattr(value, "subs")
            else value
            for key, value in matrix.items()
        }
    )


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.expand((matrix + matrix.H) / 2)


def exact_inv(matrix: sp.MatrixBase) -> sp.Matrix:
    """Invert exactly in the fraction field selected by SymPy."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).to_field().inv().to_Matrix()


class Fixture:
    """The fixed 12 x 4 cover and only the self edge used by Block 212."""

    def __init__(self) -> None:
        self.COVER_T = COVER_T
        self.LX = LX
        self.PHYS_T = PHYS_T
        self.SIZE = COVER_T * LX
        self.PHYS = PHYS
        self.CELLS = tuple(
            (t, x) for t in range(self.PHYS_T) for x in range(self.LX)
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

    def cover_index(self, t: int, x: int) -> int:
        return (t % self.COVER_T) * self.LX + (x % self.LX)

    def cell_sites(self, t: int, x: int) -> tuple:
        return tuple(
            self.cover_index(t + dt, x + dx)
            for dt, dx in ((0, 0), (0, 1), (1, 0), (1, 1))
        )

    def chart_cells(self) -> tuple:
        return tuple(
            (2 * ct, 2 * cx)
            for ct in range(self.COVER_T // 2)
            for cx in range(self.LX // 2)
        )

    def _selected_self_edge(self) -> dict:
        # Calling shift_lifts preserves the actual Block 105 supplier boundary.
        # At chart origin (0, 0), both powers are zero and the gauge is I_4.
        rt, rx = block105.shift_lifts()
        gauge = (rt ** 0) * (rx ** 0)
        local = sp.expand(
            gauge.H * (I * (SX * block105.EX + ST * block105.ET)) * gauge
        )
        out: dict = {}
        for anchor in self.chart_cells():
            sites = self.cell_sites(*anchor)
            for p in range(4):
                for q in range(4):
                    if local[p, q] != 0:
                        key = (sites[p], sites[q])
                        out[key] = out.get(key, 0) + local[p, q]
        return sclean(out)

    def cover_hodge(self, nu, a, b, mu) -> dict:
        out: dict = {}

        def bump(i, j, value):
            out[(i, j)] = out.get((i, j), 0) + value

        for t in range(self.COVER_T):
            for x in range(self.LX):
                cell = (t % self.PHYS_T, x)
                s00, s01, s10, s11 = self.cell_sites(t, x)
                bump(s00, s00, nu[cell] / 4)
                bump(s01, s01, a[cell] / 4)
                bump(s10, s10, a[cell] / 4)
                bump(s11, s11, mu[cell] / 4)
                bump(s01, s10, b[cell] / 4)
                bump(s10, s01, b[cell] / 4)
        return sclean(out)

    def moduli_from_field(self, carrier: dict) -> tuple:
        nu, a, b, mu = {}, {}, {}, {}
        for cell, (shear, volume_value) in carrier.items():
            shear = sp.sympify(shear)
            volume_value = sp.sympify(volume_value)
            nu[cell] = volume_value
            a[cell] = volume_value / (1 - shear ** 2)
            b[cell] = -volume_value * shear / (1 - shear ** 2)
            mu[cell] = 1 / volume_value
        return nu, a, b, mu

    def quotient(self, matrix: dict) -> dict:
        """Historical antiperiodic half-cover fold used by this fixture."""
        out: dict = {}
        for (i, j), value in matrix.items():
            if i < self.PHYS:
                continue
            if j >= self.PHYS:
                key = (i - self.PHYS, j - self.PHYS)
                out[key] = out.get(key, 0) + value
            else:
                key = (i - self.PHYS, j)
                out[key] = out.get(key, 0) - value
        return sclean(out)

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


def region_pin(fixture: Fixture, links) -> dict:
    pin: dict = {}
    for slot in links:
        slot %= fixture.PHYS_T
        for x in range(fixture.LX):
            pin[fixture.B[(slot, x)]] = sp.Integer(0)
            pin[fixture.A[(slot, x)]] = fixture.NU[(slot, x)]
    return pin


def volume(mode: str, t: int, x: int):
    if mode == "xgraded":
        return R(1 + (3 * t + 2 * x) % 5, 3) + R(1, 2)
    raise ValueError(mode)


def carrier_field(
    fixture: Fixture,
    core: int,
    sigma=CARRIER_SIGMA,
    mode: str = "xgraded",
    records: dict | None = None,
) -> dict:
    records = records or {}
    pinned = {(core - 1) % fixture.PHYS_T, core % fixture.PHYS_T}
    out = {}
    for t, x in fixture.CELLS:
        shear = sp.Integer(0) if t in pinned else sp.sympify(
            records.get((t, x), sigma)
        )
        out[(t, x)] = (shear, volume(mode, t, x))
    return out


def carrier_substitution(fixture: Fixture, carrier: dict) -> dict:
    nu, a, b, mu = fixture.moduli_from_field(carrier)
    out: dict = {}
    for cell in fixture.CELLS:
        out[fixture.NU[cell]] = nu[cell]
        out[fixture.A[cell]] = a[cell]
        out[fixture.B[cell]] = b[cell]
        out[fixture.MU[cell]] = mu[cell]
    return out


class Bench:
    """The symbolic pinned quotient action for the sole repaired bench."""

    def __init__(self) -> None:
        self.fx = Fixture()
        self.c = SLICE_C
        self.lx = LX
        self.T = PHYS_T
        self.N = PHYS
        pin = region_pin(self.fx, [self.c - 1, self.c])
        hodge = ssubs(self.fx.H_free, pin)
        self.Hq = dense(self.fx.quotient(hodge), self.N, self.N)
        self.Kq = dense(
            self.fx.quotient_connection(self.fx.edge_d[(0, 0)], hodge),
            self.N,
            self.N,
        )
        self.Q = sp.expand(MASS * self.Hq + self.Kq)


class Site:
    """Compatibility surface consumed by the repaired Block 212 runner."""

    def __init__(self, tag: str, cover_t: int, lx: int) -> None:
        if (tag, cover_t, lx) != ("12x4", COVER_T, LX):
            raise ValueError("released7753 fixture is fixed to ('12x4', 12, 4)")
        self.bench = Bench()
        self.tag = tag
        self.lx = lx
        self.c = self.bench.c
        self.T = self.bench.T
        self.N = self.bench.N
        self.fx = self.bench.fx
        self.free_levels = tuple(
            t
            for t in range(self.T)
            if t not in {(self.c - 1) % self.T, self.c}
        )
        self.tstar = self.free_levels[-1]

    def sub(
        self,
        sigma=CARRIER_SIGMA,
        sx=BENCH_SX,
        st=sp.Integer(0),
        m=BENCH_MASS,
        mode="xgraded",
        records=None,
    ) -> dict:
        mapping = carrier_substitution(
            self.fx,
            carrier_field(self.fx, self.c, sigma, mode, records),
        )
        mapping[SX] = sp.sympify(sx)
        mapping[ST] = sp.sympify(st)
        mapping[MASS] = sp.sympify(m)
        return mapping

    def rows(self, level: int) -> list:
        return [self.lx * (level % self.T) + x for x in range(self.lx)]


class Env:
    """One exact action and only the W2/W9 profiles used by Block 212."""

    def __init__(self, site: Site, action: sp.MatrixBase, label: str) -> None:
        self.site = site
        self.label = label
        self.Q = sp.expand(action)
        self.S = herm(self.Q)
        self._inverse: dict[str, sp.Matrix] = {}

    def inv(self, which: str) -> sp.Matrix:
        if which not in {"Q", "S"}:
            raise ValueError(which)
        if which not in self._inverse:
            target = self.Q if which == "Q" else self.S
            self._inverse[which] = exact_inv(target)
        return self._inverse[which]

    def block(self, name: str, level: int) -> sp.Matrix:
        if name not in {"W2", "W9"}:
            raise ValueError(name)
        rows = self.site.rows(level)
        inverse = self.inv("Q" if name == "W9" else "S")
        return sp.Matrix(
            self.site.lx,
            self.site.lx,
            lambda i, j: sp.expand(
                (inverse[rows[i], rows[j]] + sp.conjugate(inverse[rows[j], rows[i]]))
                / 2
            ),
        )

    def profile(self, name: str, level: int):
        block = self.block(name, level)
        total = sp.expand(sum(block[i, i] for i in range(self.site.lx)))
        if total == 0:
            return None
        return tuple(
            sp.cancel(block[i, i] / total) for i in range(self.site.lx)
        )
