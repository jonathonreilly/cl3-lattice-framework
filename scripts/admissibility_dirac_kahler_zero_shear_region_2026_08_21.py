#!/usr/bin/env python3
"""Corrected Block 164 zero-temporal-coupling region certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10 as b


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ZERO_SHEAR_REGION_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    ".claude/science/physics-loops/toe-axiom-closure-block164-zero-shear-region-20260821/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
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
    'docs/ADMISSIBILITY_DIRAC_KAHLER_ZERO_SHEAR_REGION_BOUNDED_THEOREM_NOTE_2026-08-21.md': '72fddce8b7eb60c095a250fd526949f95693f5e559d4e63148594a2cc0346d80',
    '.claude/science/physics-loops/toe-axiom-closure-block164-zero-shear-region-20260821/NO_GO_LEDGER.md': '5ae331bc3e2222a10b483eb728800185fb22b3d21cbbd9c1148b4b7741d206a9',
    'scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py': '97846307bffff108c98466329c65a051e8d896ccb9231fd23d9e0ddec962c2c9',
    'scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py': '0b86243bb0404ec5f0da4d53d8310c9e601372e9f4c823461e579f7b2c90c6ff',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md': 'a595d12fe9a4573c3b8c7f964224e01e6a2fef44f5e504394f9a2d0982da7675',
    'scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py': '2ea65a2613d2822427bfb2a0e3ac4f4ea57a18c732c27f7312bbca585f61776f',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '2601b9fc27fc78df48d22ade9104251fd1da85f174f6c7126cad9e6319ff8068',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}


def unpinned_form(fixture: b.Fixture, label, edge) -> sp.Matrix:
    rows = fixture.slice_rows(fixture.fixed_slice(label), fixture.fixed_slice(label) + 1)
    action = fixture.quotient_action(edge, fixture.H_free, b.MASS)
    return fixture.pairing(fixture.descent(label), action, rows)


def main() -> int:
    checks = b.Checks()
    identity_ok, actual = b.verify_input_hashes(INPUT_SHA256)
    identity_ok = identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS
    checks.add("A-source-input-closure", identity_ok, f"{len(INPUT_SHA256)} literal inputs; actual={actual}")

    fixture = b.Fixture(8, 4, "b164")
    normal = local = rank = hollow = shear_free = 0
    flip_zero = 0
    total = 0
    signature = sp.diag(*([1] * fixture.LX + [-1] * fixture.LX))
    trace = b.hodge_trace(fixture)
    for label in fixture.x_trivial:
        c = fixture.fixed_slice(label)
        local_shears = tuple(fixture.B[cell] for cell in fixture.pinned_cells(c))
        pin = fixture.region_substitution(c)
        target = sp.diag(*(
            [b.MASS * sp.expand(trace[(c, x)].subs(pin)) for x in range(fixture.LX)]
            + [0] * fixture.LX
        ))
        for edge in fixture.edge_d.values():
            form = sp.expand(unpinned_form(fixture, label, edge).subs({b.ST: 0}))
            upper = form[:fixture.LX, :fixture.LX]
            corner = form[fixture.LX:, fixture.LX:]
            cross = form[:fixture.LX, fixture.LX:]
            normal += int(sp.expand(form.subs(pin) - target) == sp.zeros(2 * fixture.LX))
            local += int(cross.free_symbols & fixture.SHEARS <= set(local_shears))
            cross_at_dial = sp.expand(cross.subs({
                b.MASS: sp.Integer(1),
                b.SX: sp.Rational(3, 5),
            }))
            rank += int(
                b.coefficient_rank(cross_at_dial, local_shears)
                == 2 * fixture.LX
            )
            hollow += int(corner == sp.zeros(fixture.LX))
            shear_free += int(not (upper.free_symbols & fixture.SHEARS))
            flipped = sp.expand(form.subs(
                {variable: -variable for variable in fixture.SHEARS},
                simultaneous=True,
            ))
            flip_zero += int(sp.expand(flipped - signature * form * signature) == sp.zeros(2 * fixture.LX))
            total += 1
    checks.add(
        "B-formal-zero-coupling-block-theorem",
        (normal, local, rank, hollow, shear_free, total) == (64, 64, 64, 64, 64, 64)
        and all(sp.expand(trace[(0, x)].subs(fixture.region_substitution(0))).is_positive for x in range(fixture.LX)),
        "on four x-trivial labels and 16 edges: diag(m D) plus zero after pinning; at m=1,s_x=3/5 every unpinned C coefficient map has rank eight",
    )
    checks.add(
        "C-zero-coupling-flip-congruence",
        flip_zero == total,
        "negating all shear moments gives the displayed block-signature congruence at s_t=0",
    )

    c = 1
    label = next(label for label in fixture.x_trivial if fixture.fixed_slice(label) == c)
    raw = unpinned_form(fixture, label, fixture.edge_d[(2, 2)])
    field = b.graded_carrier(fixture, c, sp.Rational(1, 3))
    plus_sub = b.carrier_substitution(fixture, field)
    minus_sub = b.carrier_substitution(
        fixture, {cell: (-shear, volume) for cell, (shear, volume) in field.items()}
    )
    common = {b.SX: sp.Rational(3, 5), b.ST: sp.Rational(1, 5), b.MASS: 1}
    plus = sp.expand(raw.subs(plus_sub).subs(common))
    minus = sp.expand(raw.subs(minus_sub).subs(common))
    checks.add(
        "D-nonzero-coupling-control",
        sp.expand(minus - signature * plus * signature) != sp.zeros(2 * fixture.LX)
        and b.inertia_pzn(plus) == (5, 0, 3),
        "the same flip is not the stated congruence at the named nonzero-coupling point",
    )

    checks.add(
        "E-exact-bounded-scope",
        b.no_float((plus, minus, trace)),
        "formal 8-by-4 x-trivial region and one control only; no off-region or nonzero-coupling classification",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
