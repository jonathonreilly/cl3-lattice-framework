#!/usr/bin/env python3
"""Corrected Block 163 finite site-reflection certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10 as b


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    ".claude/science/physics-loops/toe-axiom-closure-block163-site-reflection-channel-20260821/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_mass_survival_stratum_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
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
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md': 'a595d12fe9a4573c3b8c7f964224e01e6a2fef44f5e504394f9a2d0982da7675',
    '.claude/science/physics-loops/toe-axiom-closure-block163-site-reflection-channel-20260821/NO_GO_LEDGER.md': 'b047d0471c968d232b7bc4d3f3d6c6c2464c0959d5778c9b660a8db0374a8e99',
    'scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py': '97846307bffff108c98466329c65a051e8d896ccb9231fd23d9e0ddec962c2c9',
    'scripts/admissibility_dirac_kahler_mass_survival_stratum_2026_08_20.py': 'e7e53a44a65549f68b5d51c1c9ff328f84f657a0a6dcf51562034d07fb87594a',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md': '4b07b9409731e1b1263ec722f294847c7ac264573176f716e389c3aedaa6882b',
    'scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py': '2ea65a2613d2822427bfb2a0e3ac4f4ea57a18c732c27f7312bbca585f61776f',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '2601b9fc27fc78df48d22ade9104251fd1da85f174f6c7126cad9e6319ff8068',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}


def main() -> int:
    checks = b.Checks()
    identity_ok, actual = b.verify_input_hashes(INPUT_SHA256)
    identity_ok = identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS
    checks.add("A-source-input-closure", identity_ok, f"{len(INPUT_SHA256)} literal inputs; actual={actual}")

    fixture = b.Fixture(8, 4, "b163")
    site = fixture.site_labels
    link = fixture.link_labels
    dense_agreement = all(
        b.dense(fixture.descent(label), fixture.PHYS, fixture.PHYS)
        == b.dense_descent(label)
        for label in site + link
    )
    checks.add(
        "B-antiperiodic-descent",
        (len(site), len(link), len(fixture.involutive), len(fixture.x_trivial))
        == (32, 32, 24, 4)
        and dense_agreement,
        "the analytic signed-permutation descent matches the supplied 8-by-4 quotient on all 64 labels",
    )

    grading = b.dense(fixture.parity(), fixture.PHYS, fixture.PHYS)
    grading_law = True
    for label in site + link:
        reflection = b.dense(fixture.descent(label), fixture.PHYS, fixture.PHYS)
        expected_commute = (label[1] + label[3]) % 2 == 0
        commute = b.zero(reflection * grading - grading * reflection)
        anticommute = b.zero(reflection * grading + grading * reflection)
        grading_law = grading_law and commute == expected_commute and anticommute != expected_commute
    checks.add(
        "C-grading-selection-law",
        grading_law,
        "the descended reflection commutes with parity when p_t+p_x is even and anticommutes when it is odd",
    )

    c = 1
    region_form, _pin = b.region_pairing(fixture, c, fixture.edge_d[(2, 2)])
    field = b.graded_carrier(fixture, c, sp.Rational(1, 3))
    numeric = sp.expand(region_form.subs(b.carrier_substitution(fixture, field)).subs({
        b.SX: sp.Rational(3, 5),
        b.MASS: sp.Integer(1),
    }))
    zero_form = sp.expand(numeric.subs({b.ST: 0}))
    live_form = sp.expand(numeric.subs({b.ST: sp.Rational(1, 5)}))
    checks.add(
        "D-named-site-reflection-samples",
        b.inertia_pzn(zero_form) == (4, 4, 0)
        and b.inertia_pzn(live_form) == (5, 0, 3)
        and zero_form.rank() == 4
        and live_form.rank() == 8,
        "one exact pinned carrier is semidefinite at s_t=0 and indefinite at s_t=1/5",
    )

    checks.add(
        "E-exact-bounded-scope",
        b.no_float((
            tuple(tuple(fixture.descent(label).values()) for label in site + link),
            zero_form,
            live_form,
        )),
        "finite sign, grading and named-carrier results only; off-region and nonzero-coupling carriers remain open",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
