#!/usr/bin/env python3
"""Exact finite record-profile fixture for corrected Blocks 171--173.

This module contains only the sparse cell construction and record-profile
operations used by the three corrected primaries.  It replaces the historical
43-module import chain and the absent ``b171_profile_table_v2.py`` executable.
The current reviewed Block 105 matrices enter through the existing minimal
reflection fixture; no theorem from the historical Blocks 165--170 is imported.

``SOURCE_AST_MAP`` records definition provenance.  It is not a premise or an
acceptance of the cited historical conclusions.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10 as base


SOURCE_AST_MAP = {
    "current_block153_inertia_extract": {
        "revision": "d4e3025ca131b2ec8e349c13641b83e86c4c8c08",
        "sha256": "37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383",
        "path": "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
        "nodes": {"congruence_inertia": [148, 195]},
        "disposition": "copied_exact_linear_algebra_utility_only",
    },
    "block165_sparse_extract": {
        "revision": "3c4d52bdb9d3d2e1211799db7232b91b561bf0e1",
        "sha256": "ed55383a5f15a0ff18c528f2ed33afa2e9f90c5d5d92125249a845fa3c17db18",
        "path": "scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py",
        "nodes": {
            "smul": [419, 428],
            "sadd": [431, 437],
            "sscale": [440, 445],
            "sdagger": [448, 452],
            "sclean": [455, 456],
            "dense": [459, 463],
            "Fixture": [481, 725],
        },
        "disposition": "copied_required_definition_subset_only",
    },
    "block166_carrier_extract": {
        "revision": "3c4d52bdb9d3d2e1211799db7232b91b561bf0e1",
        "sha256": "13e2bcd055ebe986d72bd05bf568d68a31021afbd7a8b1f0edd3cb5f92ed42ae",
        "path": "scripts/admissibility_dirac_kahler_interpretation_discriminators_2026_08_21.py",
        "nodes": {
            "ssubs": [468, 472],
            "region_pin": [475, 483],
            "carrier_substitution": [516, 524],
        },
        "disposition": "copied_required_definition_subset_only",
    },
    "block171_profile_extract": {
        "revision": "97912d510826c729da6f3a2a6c40ad1b0e698c96",
        "sha256": "520b84507149d7cac89c4c6c4100dfd8060469220e619a75e2d67c0386a98ed5",
        "path": "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
        "nodes": {
            "exact_inv": [467, 480],
            "volume": [486, 493],
            "field": [496, 507],
            "Site": [554, 590],
            "Env": [593, 690],
            "frequency_profile": [1198, 1200],
            "census_probe": [1203, 1253],
        },
        "disposition": "reimplemented_bounded_w9_subset",
    },
    "block173_stationary_extract": {
        "revision": "e7078f7ada6a45008b397ba8ebfb3f3243174093",
        "sha256": "2d83dc110d6f41c2168767aed79dc2bd27d5273450dbe50d1b6e891d43ff79d1",
        "path": "scripts/admissibility_dirac_kahler_stationary_kernel_characterization_2026_08_21.py",
        "nodes": {
            "Cfg": [553, 575],
            "kernel_by_cofactor": [588, 599],
            "Fix": [602, 786],
        },
        "disposition": "reimplemented_with_normalizable_kernel_criterion",
    },
}


R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
ORIGINS = base.ORIGINS
CHART_INDEX = {origin: position for position, origin in enumerate(ORIGINS)}
HEALING_WEIGHTS = base.HEALING_WEIGHTS
EX = base.block105.EX
ET = base.block105.ET
SX, ST = sp.symbols("s_x s_t", real=True)
MASS = sp.Symbol("m", real=True)
SLICE_C = 1
CARRIER_SIGMA = R(3, 5)
BENCH_SX = R(3, 5)
BENCH_ST = sp.Integer(0)
BENCH_MASS = sp.Integer(1)
PRIMARY = (("12x4", 12, 4), ("8x4", 8, 4))


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(entry) == 0 for entry in sp.Matrix(matrix))


def no_float(value: object) -> bool:
    if isinstance(value, float):
        return False
    if isinstance(value, sp.Basic):
        return not value.has(sp.Float)
    if isinstance(value, dict):
        return all(no_float(key) and no_float(item) for key, item in value.items())
    if isinstance(value, (list, tuple, set, frozenset)):
        return all(no_float(item) for item in value)
    return True


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact ``(positive, zero, negative)`` inertia by Hermitian congruence."""
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
            (index for index in active[1:] if sp.simplify(work[head, index]) != 0),
            None,
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
        rest = [index for index in active if index not in (head, partner)]
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
    """The supplied antiperiodic 2-by-2 cell construction at one finite size."""

    def __init__(self, cover_t: int, lx: int, tag: str) -> None:
        if cover_t % 4 or lx % 2:
            raise ValueError(
                "the supplied 2-by-2 construction needs cover_t divisible by 4 "
                "and lx even"
            )
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
        self.edge_d = self.connection_for(I * SX, I * ST)
        self.H_free = self.cover_hodge(self.NU, self.A, self.B, self.MU)

    def cover_index(self, time: int, space: int) -> int:
        return (time % self.COVER_T) * self.LX + (space % self.LX)

    def cell_sites(self, time: int, space: int) -> tuple[int, ...]:
        return tuple(
            self.cover_index(time + delta_t, space + delta_x)
            for delta_t, delta_x in ((0, 0), (0, 1), (1, 0), (1, 1))
        )

    def chart_cells(self, origin: tuple[int, int]) -> tuple[tuple[int, int], ...]:
        return tuple(
            (2 * cell_t + origin[0], 2 * cell_x + origin[1])
            for cell_t in range(self.COVER_T // 2)
            for cell_x in range(self.LX // 2)
        )

    def connection_for(self, gx, gt) -> dict:
        local = sp.expand(gx * EX + gt * ET)
        shift_t, shift_x = base.block105.shift_lifts()
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
            for left in ORIGINS
            for right in ORIGINS
        }

    def cover_hodge(self, nu, a, b, inverse) -> dict:
        out: dict = {}

        def bump(row: int, column: int, value) -> None:
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

    def moduli_from_field(self, field: dict) -> tuple[dict, dict, dict, dict]:
        nu: dict = {}
        a: dict = {}
        b: dict = {}
        inverse: dict = {}
        for cell, (shear, volume_value) in field.items():
            shear = sp.sympify(shear)
            volume_value = sp.sympify(volume_value)
            nu[cell] = volume_value
            a[cell] = sp.cancel(volume_value / (1 - shear ** 2))
            b[cell] = sp.cancel(-volume_value * shear / (1 - shear ** 2))
            inverse[cell] = sp.cancel(sp.Integer(1) / volume_value)
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
            sscale(
                sadd(
                    smul(hodge, differential),
                    smul(sdagger(differential), hodge),
                ),
                I,
            )
        )


def region_pin(fixture: Fixture, links) -> dict:
    substitution: dict = {}
    for link in links:
        time = link % fixture.PHYS_T
        for space in range(fixture.LX):
            substitution[fixture.B[(time, space)]] = sp.Integer(0)
            substitution[fixture.A[(time, space)]] = fixture.NU[(time, space)]
    return substitution


def carrier_substitution(fixture: Fixture, field: dict) -> dict:
    nu, a, b, inverse = fixture.moduli_from_field(field)
    substitution: dict = {}
    for cell in fixture.CELLS:
        substitution[fixture.NU[cell]] = nu[cell]
        substitution[fixture.A[cell]] = a[cell]
        substitution[fixture.B[cell]] = b[cell]
        substitution[fixture.MU[cell]] = inverse[cell]
    return substitution


def carrier_volume(mode: str, time: int, space: int):
    if mode == "flat":
        return sp.Integer(1)
    if mode == "xgraded":
        return R(1 + (3 * time + 2 * space) % 5, 3) + R(1, 2)
    raise ValueError(mode)


def carrier_field(
    fixture: Fixture,
    records: dict | None = None,
    sigma=CARRIER_SIGMA,
    mode: str = "xgraded",
    c: int = SLICE_C,
) -> dict:
    records = {} if records is None else records
    pinned = {(c - 1) % fixture.PHYS_T, c % fixture.PHYS_T}
    return {
        cell: (
            sp.Integer(0)
            if cell[0] in pinned
            else sp.sympify(records.get(cell, sigma)),
            carrier_volume(mode, *cell),
        )
        for cell in fixture.CELLS
    }


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).to_field().inv().to_Matrix()


@dataclass(frozen=True)
class KernelResult:
    exists: bool
    unique: bool
    rank: int
    nullity: int
    representative: tuple | None


def normalizable_kernel(matrix: sp.MatrixBase) -> KernelResult:
    matrix = sp.Matrix(matrix)
    basis = matrix.nullspace()
    normalizable = tuple(vector for vector in basis if sp.expand(sum(vector)) != 0)
    representative = None
    if normalizable:
        total = sp.expand(sum(normalizable[0]))
        representative = tuple(sp.cancel(value / total) for value in normalizable[0])
    return KernelResult(
        exists=bool(normalizable),
        unique=len(basis) == 1 and bool(normalizable),
        rank=int(matrix.rank()),
        nullity=len(basis),
        representative=representative,
    )


def reciprocal_bracket(value) -> tuple[int, sp.Rational, sp.Rational]:
    magnitude = sp.Abs(sp.cancel(value))
    if not (magnitude > 0 and magnitude <= 1):
        raise ValueError("reciprocal bracket requires 0 < |value| <= 1")
    integer = int(sp.floor(1 / magnitude))
    return integer, R(1, integer + 1), R(1, integer)


def frequency_profile(trail: tuple[int, ...], alphabet_size: int = 4) -> tuple:
    return tuple(
        R(sum(letter == target for letter in trail), len(trail))
        for target in range(alphabet_size)
    )


class RecordProfileFixture:
    """The corrected finite W9 record-profile construction at one extent."""

    def __init__(self, tag: str, cover_t: int, lx: int = 4) -> None:
        self.tag = tag
        self.fixture = Fixture(cover_t, lx, tag)
        self.lx = lx
        self.T = self.fixture.PHYS_T
        self.c = SLICE_C
        self.free_levels = tuple(
            time
            for time in range(self.T)
            if time not in {(self.c - 1) % self.T, self.c}
        )
        self.tstar = self.free_levels[-1]
        self.slots = self.free_levels[:-1]
        pin = region_pin(self.fixture, (self.c - 1, self.c))
        self.hodge = ssubs(self.fixture.H_free, pin)
        hq = dense(
            self.fixture.quotient(self.hodge),
            self.fixture.PHYS,
            self.fixture.PHYS,
        )
        kq = dense(
            self.fixture.quotient_connection(
                self.fixture.edge_d[(0, 0)], self.hodge
            ),
            self.fixture.PHYS,
            self.fixture.PHYS,
        )
        self.q_symbolic = sp.expand(MASS * hq + kq)
        self._inverse_cache: dict = {}

    def rows(self, level: int) -> tuple[int, ...]:
        return tuple(
            self.lx * (level % self.T) + space for space in range(self.lx)
        )

    def substitution(
        self,
        records: dict | None = None,
        *,
        sigma=CARRIER_SIGMA,
        sx=BENCH_SX,
        st=BENCH_ST,
        mass=BENCH_MASS,
        mode: str = "xgraded",
    ) -> dict:
        substitution = carrier_substitution(
            self.fixture,
            carrier_field(self.fixture, records, sigma, mode, self.c),
        )
        substitution[SX] = sp.sympify(sx)
        substitution[ST] = sp.sympify(st)
        substitution[MASS] = sp.sympify(mass)
        return substitution

    @staticmethod
    def _record_key(records: dict | None) -> tuple:
        return tuple(
            sorted((cell, str(value)) for cell, value in (records or {}).items())
        )

    def q_matrix(self, records: dict | None = None, **parameters) -> sp.Matrix:
        return sp.Matrix(self.q_symbolic.xreplace(self.substitution(records, **parameters)))

    def inverse(self, records: dict | None = None, **parameters) -> sp.Matrix:
        key = (
            self._record_key(records),
            tuple(sorted((name, str(value)) for name, value in parameters.items())),
        )
        if key not in self._inverse_cache:
            self._inverse_cache[key] = exact_inverse(self.q_matrix(records, **parameters))
        return self._inverse_cache[key]

    def raw_diagonal(
        self,
        records: dict | None = None,
        *,
        level: int | None = None,
        **parameters,
    ) -> tuple:
        inverse = self.inverse(records, **parameters)
        use_level = self.tstar if level is None else level
        return tuple(
            sp.expand(sp.re(inverse[index, index])) for index in self.rows(use_level)
        )

    def weight(self, records: dict | None = None, **parameters):
        return sp.expand(sum(self.raw_diagonal(records, **parameters)))

    def profile(
        self,
        records: dict | None = None,
        *,
        level: int | None = None,
        **parameters,
    ) -> tuple:
        diagonal = self.raw_diagonal(records, level=level, **parameters)
        total = sp.expand(sum(diagonal))
        if total == 0:
            raise ZeroDivisionError("the supplied W9 block has zero trace")
        return tuple(sp.cancel(value / total) for value in diagonal)

    def w9_block(
        self,
        records: dict | None = None,
        *,
        level: int | None = None,
        **parameters,
    ) -> sp.Matrix:
        inverse = self.inverse(records, **parameters)
        rows = self.rows(self.tstar if level is None else level)
        return sp.Matrix(
            self.lx,
            self.lx,
            lambda row, column: sp.expand(
                (
                    inverse[rows[row], rows[column]]
                    + sp.conjugate(inverse[rows[column], rows[row]])
                )
                / 2
            ),
        )

    def profile_table(self) -> tuple[dict, ...]:
        first, second = self.free_levels[:2]
        rows = []
        for left in range(self.lx):
            for right in range(self.lx):
                records = {
                    (first, left): sp.Integer(0),
                    (second, right): sp.Integer(0),
                }
                rows.append(
                    {
                        "trail": (left, right),
                        "records": records,
                        "weight": self.weight(records),
                        "profile": self.profile(records),
                        "frequency": frequency_profile((left, right), self.lx),
                    }
                )
        return tuple(rows)

    def system(self, base_records: dict, slot: int, **parameters):
        p0 = self.profile(base_records, **parameters)
        extensions = []
        for letter in range(self.lx):
            records = dict(base_records)
            records[(slot, letter)] = sp.Integer(0)
            extensions.append(self.profile(records, **parameters))
        transition = sp.Matrix(
            self.lx,
            self.lx,
            lambda row, column: extensions[column][row],
        )
        influence = transition - sp.Matrix(p0) * sp.ones(1, self.lx)
        return p0, tuple(extensions), transition, influence


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

    def add(self, name: str, condition: object, detail: str) -> None:
        self.results.append((name, bool(condition), detail))

    def emit(self) -> int:
        for name, ok, detail in self.results:
            print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        passed = sum(ok for _, ok, _ in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return 0 if failed == 0 else 1
