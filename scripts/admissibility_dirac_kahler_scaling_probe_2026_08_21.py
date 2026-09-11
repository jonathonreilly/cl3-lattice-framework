#!/usr/bin/env python3
"""Corrected Block 165 four-size finite scaling certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10 as b


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCALING_PROBE_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    ".claude/science/physics-loops/toe-axiom-closure-block165-scaling-probe-20260821/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_zero_shear_region_2026_08_21.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ZERO_SHEAR_REGION_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SCALING_PROBE_BOUNDED_THEOREM_NOTE_2026-08-21.md': 'e5f5e98f1182c57a9f075e82c423547a622c9cde8682d3af2cfbbc6123b64322',
    '.claude/science/physics-loops/toe-axiom-closure-block165-scaling-probe-20260821/NO_GO_LEDGER.md': 'ccf2bd37a7ece87262e735fbcd5ccba6e82c55d3df09c65d2cefb9f9e420b733',
    'scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py': '97846307bffff108c98466329c65a051e8d896ccb9231fd23d9e0ddec962c2c9',
    'scripts/admissibility_dirac_kahler_zero_shear_region_2026_08_21.py': '028485e8e606f9c66771373e34facbaa6f2294dd8d341a3ca7a9411795420be3',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_ZERO_SHEAR_REGION_BOUNDED_THEOREM_NOTE_2026-08-21.md': '72fddce8b7eb60c095a250fd526949f95693f5e559d4e63148594a2cc0346d80',
    'scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py': '2ea65a2613d2822427bfb2a0e3ac4f4ea57a18c732c27f7312bbca585f61776f',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '2601b9fc27fc78df48d22ade9104251fd1da85f174f6c7126cad9e6319ff8068',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

SIZES = ((8, 4), (12, 4), (8, 6), (16, 4))
EXPECTED_DIMENSIONS = (24, 40, 36, 56)
EXPECTED_INVOLUTIONS = (24, 36, 32, 48)
EXPECTED_E_LIVE = ((2, 4), (0, 6), (2, 4), (0, 8))


def unpinned_form(fixture: b.Fixture, c: int) -> sp.Matrix:
    label = next(label for label in fixture.x_trivial if fixture.fixed_slice(label) == c)
    rows = fixture.slice_rows(c, c + 1)
    action = fixture.quotient_action(fixture.edge_d[(2, 2)], fixture.H_free, b.MASS)
    return fixture.pairing(fixture.descent(label), action, rows)


def main() -> int:
    checks = b.Checks()
    identity_ok, actual = b.verify_input_hashes(INPUT_SHA256)
    identity_ok = identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS
    checks.add("A-source-input-closure", identity_ok, f"{len(INPUT_SHA256)} literal inputs; actual={actual}")

    dimensions = []
    involutions = []
    symbolic_ranks = []
    numeric_ranks = []
    affine = []
    zero_inertias = []
    e_live = []
    exact_pool = []
    for cover_t, lx in SIZES:
        fixture = b.Fixture(cover_t, lx, f"b165_{cover_t}_{lx}")
        dimensions.append(2 * len(fixture.CELLS) - len(fixture.pinned_cells(0)))
        involutions.append(len(fixture.involutive))
        live = 0
        cells = 0
        for c in range(fixture.PHYS_T):
            raw = unpinned_form(fixture, c)
            zero = sp.expand(raw.subs({b.ST: 0}))
            local = tuple(fixture.B[cell] for cell in fixture.pinned_cells(c))
            symbolic_ranks.append((cover_t, lx, c, b.coefficient_rank(
                sp.expand(zero[:lx, lx:].subs({
                    b.MASS: sp.Integer(1),
                    b.SX: sp.Rational(3, 5),
                })),
                local,
            )))

            region, _pin = b.region_pairing(fixture, c, fixture.edge_d[(2, 2)])
            affine.append(all(
                sp.expand(sp.diff(entry, b.ST, 2)) == 0 for entry in region
            ))
            field = b.graded_carrier(fixture, c, sp.Rational(1, 3))
            numeric = sp.expand(region.subs(b.carrier_substitution(fixture, field)).subs({
                b.SX: sp.Rational(3, 5),
                b.MASS: sp.Integer(1),
            }))
            c1 = sp.expand(numeric[:lx, lx:].diff(b.ST))
            e1 = sp.expand(numeric[lx:, lx:].diff(b.ST))
            numeric_ranks.append((cover_t, lx, c, c1.rank()))
            zero_inertias.append((cover_t, lx, c, b.inertia_pzn(
                sp.expand(numeric.subs({b.ST: 0}))
            )))
            live += int(e1 != sp.zeros(lx))
            cells += 1
            exact_pool.extend((region, c1, e1))
        e_live.append((live, cells))

    checks.add(
        "B-four-size-enumeration",
        tuple(dimensions) == EXPECTED_DIMENSIONS
        and tuple(involutions) == EXPECTED_INVOLUTIONS,
        "region dimensions 24,40,36,56 and involution counts 24,36,32,48 are enumerated from each fixture",
    )
    checks.add(
        "C-independent-entry-ranks",
        all(rank == 2 * lx for _ct, lx, _c, rank in symbolic_ranks)
        and all(rank == lx for _ct, lx, _c, rank in numeric_ranks),
        "for edge (2,2) at m=1,s_x=3/5, every tested fixed slice has full 2Lx local-coordinate rank and full Lx numeric C1 rank",
    )
    checks.add(
        "D-region-and-affine-censuses",
        all(affine)
        and all(inertia == (lx, lx, 0) for _ct, lx, _c, inertia in zero_inertias)
        and tuple(e_live) == EXPECTED_E_LIVE,
        "all 22 forms are affine in s_t and PSD at zero; E1 is live only on two of four slices at the two Tphys=4 sizes",
    )
    checks.add(
        "E-exact-bounded-scope",
        b.no_float((dimensions, involutions, symbolic_ranks, numeric_ranks, zero_inertias, exact_pool)),
        "four finite fixtures, one edge and every x-trivial fixed slice; no size-universal or off-region theorem",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
