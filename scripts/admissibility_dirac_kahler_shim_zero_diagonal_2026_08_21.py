#!/usr/bin/env python3
"""Corrected Block 168 finite Schur and displacement-two certificate.

The closed shim identity is checked only at 12x4.  The 8x6 wrap control is
kept separate, and profile statements distinguish pointwise feasibility from
uniform feasibility near ``s_t = 0``.
"""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10 as h


R = sp.Rational
G2 = sp.Symbol("g_2", real=True)
SLICE_C = 1

AUDIT_INPUT_PATHS = ('scripts/admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10.py',
 'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIM_ZERO_DIAGONAL_BOUNDED_THEOREM_NOTE_2026-08-21.md',
 '.claude/science/physics-loops/toe-axiom-closure-block168-shim-zero-diagonal-20260821/NO_GO_LEDGER.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/audit/data/axiom_premise_nodes.json',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md')

INPUT_SHA256 = {'scripts/admissibility_dirac_kahler_released7315_c_fixture_helpers_2026_09_10.py': '90d9e48440a8a74eabd73553ab61322cf0b75a11de9be1cd65eaee6b5bc6c0db',
 'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIM_ZERO_DIAGONAL_BOUNDED_THEOREM_NOTE_2026-08-21.md': 'f6d15e00fd7ee448d2a8263f3ee656bddd5005d574b00f4b7ff6437dfb86beb8',
 '.claude/science/physics-loops/toe-axiom-closure-block168-shim-zero-diagonal-20260821/NO_GO_LEDGER.md': '2dfbfd874eb3846791608675e4f67a07184ae49f8d067e5bc314511dc5b46836',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
 'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
 'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
 'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33'}

SOURCE_AST_MAP = {
    "original_block168": {
        "path": "scripts/admissibility_dirac_kahler_shim_zero_diagonal_2026_08_21.py",
        "source_sha256": "5d87942f24be65c811a6b49b9c99a105a4a0dbb3a0e5458f7a729b578d8b961c",
        "nodes": {
            "cover_disp2": [553, 567],
            "cancellation_probe": [741, 912],
            "shim_probe": [918, 1117],
            "zero_diagonal_probe": [1123, 1209],
            "wrap_probe": [1274, 1328],
        },
    }
}


def carrier_without_st(bench: h.Bench) -> dict:
    substitution = bench.carrier()
    substitution.pop(h.ST)
    return substitution


def shim_increment(bench: h.Bench, power: int, corner: sp.MatrixBase | None = None) -> sp.Matrix:
    block = sp.eye(bench.lx) if corner is None else sp.Matrix(corner)
    displacement = h.cover_displacement_two(
        bench.fixture, block, G2 * h.ST ** power
    )
    return sp.expand(bench.pair_action(h.sadd(bench.action, displacement)) - bench.form)


def mass_only_injectivity(fixture: h.Fixture, c: int) -> dict:
    """Only the connection-off mass map; no statement about cancellation with d."""
    label = h.site_label(fixture, c)
    rows = fixture.slice_rows(c, c + 1)
    mass_action = fixture.quotient_action({}, fixture.H_free, h.MASS)
    form = fixture.pairing(fixture.descent(label), mass_action, rows)
    cross = sp.expand(form[:fixture.LX, fixture.LX:])
    incident = tuple(
        fixture.B[(time % fixture.PHYS_T, space)]
        for time in (c - 1, c)
        for space in range(fixture.LX)
    )
    rank_nonzero_mass = h.coefficient_rank(cross.subs({h.MASS: 1}), incident)
    zero_at_zero_mass = h.zero(cross.subs({h.MASS: 0}))

    slice_shears = {
        time: sp.Symbol(f"z_{time}", real=True)
        for time in range(fixture.PHYS_T)
    }
    homogeneous = {
        fixture.B[(time, space)]: slice_shears[time]
        for time, space in fixture.CELLS
    }
    for cell in fixture.CELLS:
        homogeneous.update({
            fixture.NU[cell]: 1,
            fixture.A[cell]: 1,
            fixture.MU[cell]: 1,
        })
    selected = (slice_shears[(c - 1) % fixture.PHYS_T], slice_shears[c])
    homogeneous_cross = sp.expand(cross.subs(homogeneous).subs({h.MASS: 1}))
    return {
        "incident_variables": len(incident),
        "rank_at_m_one": rank_nonzero_mass,
        "zero_at_m_zero": zero_at_zero_mass,
        "x_homogeneous_variables": tuple(map(str, selected)),
        "x_homogeneous_rank": h.coefficient_rank(homogeneous_cross, selected),
    }


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-input-identity", identity_ok, f"nine exact inputs; actual={actual}")

    fx12 = h.Fixture(12, 4, "12x4")
    bench12 = h.Bench(fx12, SLICE_C)
    env12 = carrier_without_st(bench12)
    base12 = sp.expand(bench12.form.subs(env12))
    B = sp.expand(base12[:4, :4])
    C1 = sp.expand(base12[:4, 4:].diff(h.ST))
    kappa_matrix = sp.expand(C1.H * B.inv() * C1)
    kappa = R(57, 160)
    increment2 = sp.expand(shim_increment(bench12, 2).subs(env12))
    wanted2 = sp.diag(sp.zeros(4, 4), G2 * h.ST ** 2 * sp.eye(4))
    closed_identity = h.zero(increment2 - wanted2)
    checks.add(
        "B-12x4-closed-identity",
        closed_identity
        and h.zero(base12[:4, 4:] - h.ST * C1)
        and h.zero(base12[4:, 4:])
        and h.zero(kappa_matrix - kappa * sp.eye(4)),
        "at 12x4 only: [[B,s_t C1],[s_t C1^H,g2 s_t^2 I]], with C1^H B^-1 C1=(57/160)I at m=1",
    )

    threshold_form = sp.expand(
        (base12 + increment2).subs({h.ST: R(1, 2), G2: kappa})
    )
    below_form = sp.expand(
        (base12 + increment2).subs({h.ST: R(1, 2), G2: R(1, 4)})
    )
    boundary_a = sp.expand((base12 + increment2).subs({h.ST: 0, G2: -100}))
    boundary_b = sp.expand((base12 + increment2).subs({h.ST: 0, G2: 100}))
    checks.add(
        "C-domain-and-boundary",
        h.is_psd(threshold_form)
        and not h.is_psd(below_form)
        and h.zero(boundary_a - boundary_b)
        and sp.expand(base12[:4, 4:].subs({h.ST: 0})).rank() == 0
        and sp.expand(base12[:4, 4:].subs({h.ST: R(1, 2)})).rank() == 4,
        "the identity-corner threshold applies for B>0 and s_t!=0; s_t=0 is g2-independent and has rank C=0",
    )

    positive_corner = sp.diag(2, 3, 4, 5)
    general_increment = sp.diag(
        sp.zeros(4, 4), G2 * h.ST ** 2 * positive_corner
    )
    general_at = sp.expand(
        (base12 + general_increment).subs({h.ST: R(1, 2), G2: kappa / 2})
    )
    general_below = sp.expand(
        (base12 + general_increment).subs({h.ST: R(1, 2), G2: kappa / 3})
    )
    checks.add(
        "D-general-positive-corner",
        h.is_psd(general_at) and not h.is_psd(general_below),
        "for P=diag(2,3,4,5), the generalized threshold is kappa/2; it depends on P",
    )

    profile_rows = []
    for power in (2, 4, 6):
        increment = sp.expand(shim_increment(bench12, power).subs(env12))
        for st in (R(1, 2), sp.Integer(2)):
            required = sp.cancel(kappa * st ** (2 - power))
            form = sp.expand((base12 + increment).subs({h.ST: st, G2: required}))
            profile_rows.append((power, st, required, h.inertia_pzn(form)))
    uniform_limits = {
        power: sp.limit(kappa * h.ST ** (2 - power), h.ST, 0, dir="+")
        for power in (2, 4, 6)
    }
    checks.add(
        "E-pointwise-versus-uniform",
        all(inertia[2] == 0 for _, _, _, inertia in profile_rows)
        and uniform_limits == {2: kappa, 4: sp.oo, 6: sp.oo},
        f"k=2,4,6 work at the listed nonzero points; only k=2 has finite uniform threshold near zero; rows={profile_rows}",
    )

    fx86 = h.Fixture(8, 6, "8x6")
    bench86 = h.Bench(fx86, SLICE_C)
    env86 = carrier_without_st(bench86)
    increment86 = sp.expand(shim_increment(bench86, 2).subs(env86))
    base86 = sp.expand(bench86.form.subs(env86))
    checks.add(
        "F-8x6-wrap-control",
        h.zero(increment86)
        and not h.zero(base86[6:, 6:]),
        "the homogeneous displacement-two shim has rank zero at 8x6, where the pre-existing T_phys=4 wrap corner is live",
    )

    injection = mass_only_injectivity(fx12, SLICE_C)
    checks.add(
        "G-mass-only-selected-map",
        injection == {
            "incident_variables": 8,
            "rank_at_m_one": 8,
            "zero_at_m_zero": True,
            "x_homogeneous_variables": ("z_0", "z_1"),
            "x_homogeneous_rank": 2,
        },
        f"finite connection-off result, requiring nonzero mass; it does not decide cancellation against a connection; {injection}",
    )

    checks.add(
        "H-exact-bounded-scope",
        h.no_float((base12, increment2, profile_rows, base86, injection))
        and len(SOURCE_AST_MAP) == 1,
        "12x4 closed formula, 8x6 wrap control, and selected maps only; no all-cone or physical closure",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
