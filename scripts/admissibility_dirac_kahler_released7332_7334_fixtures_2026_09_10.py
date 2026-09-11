#!/usr/bin/env python3
"""Finite construction supplier for the released PR7332--PR7334 pair.

This module adds only the surfaces used by the recovered rank-two transport and
source-functional runners to the reviewed released7333 finite cover supplier:
the Block170-style two-slice reflection bench, its exact graded carrier, one
finite rank-two effect example, exact Hermitian inertia, and the historical
Block107 row/column convention used for a dated comparison.

The formulas are extracted from the original PR pair's historical runtime at
its recorded heads.  Historical theorem text, status, routing advice, and the
rest of the 51-script import chain are not imported or accepted here.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10 as finite


ROOT = Path(__file__).resolve().parents[1]
FINITE_SUPPLIER_PATH = (
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_"
    "compiler_released7333_fixture_2026_09_10.py"
)
FINITE_SUPPLIER_SHA256 = (
    "8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2"
)
HISTORICAL_FORMULA_PROVENANCE = {
    "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py":
        "5d2360f0cb81718a480d77e6eecc303f82cc433299f827148317205c0bf75ea9",
    "scripts/admissibility_dirac_kahler_interpretation_discriminators_2026_08_21.py":
        "13e2bcd055ebe986d72bd05bf568d68a31021afbd7a8b1f0edd3cb5f92ed42ae",
    "scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py":
        "ed55383a5f15a0ff18c528f2ed33afa2e9f90c5d5d92125249a845fa3c17db18",
    "scripts/admissibility_dirac_kahler_pincer_identity_cross_lane_2026_08_22.py":
        "37fa40baae20ef5b1ab3bcd938f8be145d80f0048968c055cf1378903208bb3c",
    "scripts/admissibility_dirac_kahler_adm_seam_two_history_gram_2026_08_15.py":
        "b64e3ff954e7e4767835b11eb72794c39bde7bcef6b00fdc216dafae3b551915",
}

R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
ST = finite.ST
SX = finite.SX
MASS = finite.MASS

SLICE_C = 1
CARRIER_SIGMA = R(3, 5)
BENCH_SX = R(3, 5)
BENCH_MASS = ONE
PRIMARY = (("8x4", 8, 4), ("12x4", 12, 4))
MENU = (ZERO, R(1, 5), R(2, 5), R(3, 5))
DENSITY_DENOMINATOR = sp.Integer(
    894555786619317339421650665156104028453509785664333673843970497575127328208
)
DENSITY_NUMERATORS = tuple(
    map(
        sp.Integer,
        (
            268251574285153956297813548296329792195197468843616541008641132195640585440,
            221001943568477496197298503927672181662102219068198431958029827878618664480,
            218355469342291864735240151179441946892053542743480442321946476045569116869,
            186946799423394022191298461752660107704156555009038258555353061455298961419,
        ),
    )
)
LAMBDA = sp.Symbol("lambda")


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def supplier_certificate() -> bool:
    """Bind the reviewed finite base and exact extracted constants."""
    return bool(
        sha256_path(ROOT / FINITE_SUPPLIER_PATH) == FINITE_SUPPLIER_SHA256
        and finite.supplier_certificate()
        and sum(DENSITY_NUMERATORS) == DENSITY_DENOMINATOR
        and PRIMARY == (("8x4", 8, 4), ("12x4", 12, 4))
    )


def graded_carrier(fixture: finite._Cover, c: int, sigma) -> dict:
    """The exact finite carrier used by the original Block170 bench."""
    pinned = {(c - 1) % fixture.PHYS_T, c % fixture.PHYS_T}
    return {
        (time, space): (
            ZERO if time in pinned else sp.sympify(sigma),
            R(1 + (3 * time + 5 * space) % 5, 3) + R(1, 2),
        )
        for time, space in fixture.CELLS
    }


def lift_sign(fixture: finite._Cover, time: int) -> int:
    return -1 if (time // fixture.PHYS_T) % 2 == 0 else 1


def temporal_reflection(fixture: finite._Cover, c: int) -> sp.Matrix:
    """Descend the historical x-trivial site reflection fixing slice c."""
    point_time = 2 * c
    reflection = sp.zeros(fixture.PHYS, fixture.PHYS)
    for time in range(fixture.PHYS_T):
        reflected_time = (point_time - time) % fixture.PHYS_T
        sign = lift_sign(fixture, time) * lift_sign(
            fixture, point_time - time
        )
        for space in range(fixture.LX):
            reflection[
                fixture.LX * time + space,
                fixture.LX * reflected_time + space,
            ] = sign
    return reflection


def slice_rows(fixture: finite._Cover, *slices: int) -> tuple[int, ...]:
    return tuple(
        fixture.LX * (time % fixture.PHYS_T) + space
        for time in slices
        for space in range(fixture.LX)
    )


class Bench:
    """One exact finite two-slice reflection bench, with no parent status."""

    def __init__(
        self,
        tag: str,
        cover_t: int,
        lx: int,
        c: int = SLICE_C,
    ) -> None:
        self.tag = tag
        base = finite._Bench(cover_t, lx)
        self.fx = base.fx
        self.c = c
        self.lx = lx
        self.T = base.T
        self.N = base.N
        self.r = temporal_reflection(self.fx, c)
        self.rows = slice_rows(self.fx, c, c + 1)
        self.Hq = base.Hq
        self.Kq = base.Kq
        self.Q = base.Q
        self.form = self.pair(self.Q)

    def pair(
        self,
        action: sp.MatrixBase,
        reflection: sp.MatrixBase | None = None,
        rows: tuple[int, ...] | None = None,
    ) -> sp.Matrix:
        """Hermitian part of the selected [r Q] block."""
        r_matrix = self.r if reflection is None else reflection
        selected = self.rows if rows is None else rows
        product = sp.expand(r_matrix * action)
        block = sp.Matrix(
            len(selected),
            len(selected),
            lambda row, column: product[selected[row], selected[column]],
        )
        return sp.expand((block + block.H) / 2)

    def carrier(
        self,
        sigma=CARRIER_SIGMA,
        sx=BENCH_SX,
        mass=BENCH_MASS,
        st=None,
    ) -> dict:
        substitution = finite.carrier_substitution(
            self.fx,
            graded_carrier(self.fx, self.c, sigma),
        )
        substitution[SX] = sp.sympify(sx)
        substitution[MASS] = sp.sympify(mass)
        if st is not None:
            substitution[ST] = sp.sympify(st)
        return substitution


def witness_isometry() -> sp.Matrix:
    """X=[(4e0+3e4)/5,(4e2+3e6)/5] on the selected eight rows."""
    identity = sp.eye(8)
    return sp.Matrix.hstack(
        (4 * identity.col(0) + 3 * identity.col(4)) / 5,
        (4 * identity.col(2) + 3 * identity.col(6)) / 5,
    )


def projector(index: int) -> sp.Matrix:
    effect = sp.zeros(4, 4)
    effect[index, index] = ONE
    return effect


def effect_for(cell) -> sp.Matrix:
    return sum(
        (projector(MENU.index(value)) for value in cell),
        sp.zeros(4, 4),
    )


def trace_reading(density: sp.MatrixBase, effect: sp.MatrixBase):
    return sp.cancel(sp.trace(density * effect))


def historical107_history_gram(
    propagator: sp.MatrixBase,
    site_index,
    spatial_extent: int = 1,
) -> sp.Matrix:
    """Exact original107 code convention, retained as dated comparison only."""
    positive = [
        site_index(time, space)
        for time in (0, 1)
        for space in range(spatial_extent)
    ]
    reflected = [
        site_index(-1 - time, space)
        for time in (0, 1)
        for space in range(spatial_extent)
    ]
    return sp.Matrix(
        len(positive),
        len(positive),
        lambda row, column: sp.conjugate(
            propagator[positive[row], reflected[column]]
        ),
    )


def historical107_displayed_gram(
    propagator: sp.MatrixBase,
    site_index,
    spatial_extent: int = 1,
) -> sp.Matrix:
    """Original107 displayed K_ab=conj(G(b,theta a)) convention."""
    positive = [
        site_index(time, space)
        for time in (0, 1)
        for space in range(spatial_extent)
    ]
    reflected = [
        site_index(-1 - time, space)
        for time in (0, 1)
        for space in range(spatial_extent)
    ]
    return sp.Matrix(
        len(positive),
        len(positive),
        lambda row, column: sp.conjugate(
            propagator[positive[column], reflected[row]]
        ),
    )


def real_symmetric_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (positive, negative, zero) inertia for a Hermitian matrix."""
    if matrix != matrix.H:
        raise ValueError("inertia requires an exactly Hermitian matrix")
    polynomial = sp.Poly(matrix.charpoly(LAMBDA).as_expr(), LAMBDA)
    coefficients = list(polynomial.all_coeffs())

    def changes(sequence) -> int:
        nonzero = [value for value in sequence if value != 0]
        return sum(
            1
            for left, right in zip(nonzero, nonzero[1:])
            if left * right < 0
        )

    positive = changes(coefficients)
    alternating = [
        value * (-1) ** index
        for index, value in enumerate(reversed(coefficients))
    ]
    negative = changes(list(reversed(alternating)))
    return positive, negative, matrix.rows - positive - negative


def local_hodge_positive(field: dict) -> bool:
    """Check the constructive positive-cell conditions on one exact carrier."""
    for shear, volume in field.values():
        shear = sp.sympify(shear)
        volume = sp.sympify(volume)
        eigenvalues = (
            volume,
            1 / volume,
            volume / (1 - shear),
            volume / (1 + shear),
        )
        if not all(sp.simplify(value).is_positive is True for value in eigenvalues):
            return False
    return True


def antiperiodic_injection(fixture: finite._Cover) -> sp.Matrix:
    """J=(-I,I)^T for the historical half-cover antiperiodic fold."""
    identity = sp.eye(fixture.PHYS)
    return sp.Matrix.vstack(-identity, identity)


def hodge_restriction_certificate(bench: Bench, field: dict) -> bool:
    """Verify the exact positive-restriction premises for one carrier.

    Each disclosed local Hodge block is positive when ``local_hodge_positive``
    holds.  Their cover sum is therefore positive, and every cover site occurs
    in those blocks.  The full-column-rank antiperiodic injection then makes
    ``J^dag H J/2`` positive.  This function checks the carrier inequalities,
    the injection rank, and the exact equality of that restriction with the
    quotient Hodge matrix used by the live runners.
    """
    substitutions = finite.carrier_substitution(bench.fx, field)
    cover_hodge = finite.dense(
        finite.ssubs(bench.fx.H_free, substitutions),
        bench.fx.SIZE,
        bench.fx.SIZE,
    )
    injection = antiperiodic_injection(bench.fx)
    quotient_hodge = sp.expand(bench.Hq.subs(substitutions))
    restricted = sp.expand(injection.H * cover_hodge * injection / 2)
    return bool(
        local_hodge_positive(field)
        and injection.rank() == bench.fx.PHYS
        and restricted == quotient_hodge
        and quotient_hodge == quotient_hodge.H
    )
