#!/usr/bin/env python3
"""Corrected Block 166 finite interpretation-discriminator certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10 as b


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_INTERPRETATION_DISCRIMINATORS_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    ".claude/science/physics-loops/toe-axiom-closure-block166-interpretation-discriminators-20260821/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCALING_PROBE_BOUNDED_THEOREM_NOTE_2026-08-21.md",
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
    'docs/ADMISSIBILITY_DIRAC_KAHLER_INTERPRETATION_DISCRIMINATORS_BOUNDED_THEOREM_NOTE_2026-08-21.md': 'f907c1ba52cc083b65aadda2b9c231971c421897135d6505202c5b4c69f87c32',
    '.claude/science/physics-loops/toe-axiom-closure-block166-interpretation-discriminators-20260821/NO_GO_LEDGER.md': 'c7a49b43550ada5b5c5fb63614fe7b157a0e64bcb13de4dc1a9d1b5a3016f35f',
    'scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py': '97846307bffff108c98466329c65a051e8d896ccb9231fd23d9e0ddec962c2c9',
    'scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py': '5cd7b4071bed36c6b63d4556a4fe13c2ade02d2020f3c0c848f5ff811dd37c21',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SCALING_PROBE_BOUNDED_THEOREM_NOTE_2026-08-21.md': 'e5f5e98f1182c57a9f075e82c423547a622c9cde8682d3af2cfbbc6123b64322',
    'scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py': '2ea65a2613d2822427bfb2a0e3ac4f4ea57a18c732c27f7312bbca585f61776f',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '2601b9fc27fc78df48d22ade9104251fd1da85f174f6c7126cad9e6319ff8068',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}


def region_numeric(fixture: b.Fixture, c: int) -> tuple[sp.Matrix, dict]:
    form, pin = b.region_pairing(fixture, c, fixture.edge_d[(2, 2)])
    field = b.graded_carrier(fixture, c, sp.Rational(1, 3))
    numeric = sp.expand(form.subs(b.carrier_substitution(fixture, field)).subs({
        b.SX: sp.Rational(3, 5),
        b.MASS: sp.Integer(1),
    }))
    return numeric, pin


def symbols_of_sparse(matrix: dict) -> set[sp.Symbol]:
    return set().union(*(value.free_symbols for value in matrix.values())) if matrix else set()


def main() -> int:
    checks = b.Checks()
    identity_ok, actual = b.verify_input_hashes(INPUT_SHA256)
    identity_ok = identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS
    checks.add("A-source-input-closure", identity_ok, f"{len(INPUT_SHA256)} literal inputs; actual={actual}")

    fixture = b.Fixture(12, 4, "b166")
    c = 1
    edge = fixture.edge_d[(2, 2)]
    form, pin = b.region_pairing(fixture, c, edge)
    flat_pairing = sp.expand(form.subs({b.ST: 0}))
    free = {fixture.B[cell] for cell in fixture.free_cells(c)}
    hodge = b.ssubs(fixture.H_free, pin)
    action = b.ssubs(fixture.quotient_action(edge, hodge, b.MASS), {b.ST: 0})
    metric = fixture.quotient(hodge)

    three_link_pin = b.region_pin(fixture, (c - 1, c, c + 1))
    three_link_action = b.ssubs(
        fixture.quotient_action(edge, b.ssubs(fixture.H_free, three_link_pin), b.MASS),
        {b.ST: 0},
    )
    action_block = b.dense(
        three_link_action, fixture.PHYS, fixture.PHYS
    ).extract(fixture.slice_rows(c + 1), fixture.slice_rows(c))

    one_link_pin = b.region_pin(fixture, (c - 1,))
    control_field = {
        cell: (
            0 if cell[0] == (c - 1) % fixture.PHYS_T else sp.Rational(2, 5),
            sp.Rational(1 + (3 * cell[0] + 5 * cell[1]) % 5, 3) + sp.Rational(1, 2),
        )
        for cell in fixture.CELLS
    }
    metric_control = b.dense(
        fixture.quotient(fixture.H_free), fixture.PHYS, fixture.PHYS
    ).subs(one_link_pin).subs(
        b.carrier_substitution(fixture, control_field)
    ).extract(fixture.slice_rows(c + 1), fixture.slice_rows(c))
    checks.add(
        "B-pairing-action-and-metric-scope",
        not (flat_pairing.free_symbols & free)
        and len(symbols_of_sparse(action) & free) == len(free)
        and len(symbols_of_sparse(metric) & free) == len(free)
        and action_block == sp.zeros(fixture.LX)
        and metric_control.rank() == fixture.LX,
        "free shears are invisible to this s_t=0 pairing but live in the full action and metric; the zero action block uses the stated three-link pin, while the off-region control is metric",
    )

    numeric, _ = region_numeric(fixture, c)
    n = fixture.LX
    block_b = sp.expand(numeric[:n, :n].subs({b.ST: 0}))
    c1 = sp.expand(numeric[:n, n:].diff(b.ST))
    e1 = sp.expand(numeric[n:, n:].diff(b.ST))
    displayed_pencil = sp.Matrix.vstack(
        sp.Matrix.hstack(block_b, b.ST * c1),
        sp.Matrix.hstack(b.ST * c1.H, sp.zeros(n)),
    )
    schur = sp.expand(c1.H * block_b.inv() * c1)
    norm0 = sp.sqrt(sp.trace(block_b.H * block_b))
    checks.add(
        "C-hollow-corner-and-margin",
        block_b == sp.Rational(57, 40) * sp.eye(n)
        and c1 == sp.diag(sp.Rational(57, 80), -sp.Rational(57, 80),
                          sp.Rational(57, 80), -sp.Rational(57, 80))
        and e1 == sp.zeros(n)
        and numeric == displayed_pencil
        and sp.expand(schur - sp.Rational(57, 160) * sp.eye(n)) == sp.zeros(n)
        and norm0 == sp.Rational(57, 20)
        and sp.simplify(sp.Rational(57, 160) / norm0) == sp.Rational(1, 8)
        and b.inertia_pzn(numeric.subs({b.ST: sp.Rational(1, 5)})) == (4, 0, 4),
        "the full displayed 12-by-4 pencil has blocks B, s_t C1, s_t C1*, 0; its raw Schur coefficient is 57/160 and normalized coefficient is 1/8",
    )

    gre, gim = sp.symbols("g_re g_im", real=True)
    coupling = gre + sp.I * gim
    coupled = sp.Matrix.vstack(
        sp.Matrix.hstack(block_b, coupling * c1),
        sp.Matrix.hstack(sp.conjugate(coupling) * c1.H, sp.zeros(n)),
    )
    coupled_schur = sp.expand(
        -sp.conjugate(coupling) * coupling * c1.H * block_b.inv() * c1
    )
    checks.add(
        "D-stipulated-Hermitian-block-pencil",
        sp.expand(
            coupled_schur
            + (gre ** 2 + gim ** 2) * sp.Rational(57, 160) * sp.eye(n)
        ) == sp.zeros(n)
        and c1.rank() == n
        and coupled.subs({gre: b.ST, gim: 0}) == displayed_pencil
        and b.inertia_pzn(coupled.subs({gre: sp.Rational(1, 5), gim: 0})) == (4, 0, 4),
        "the stipulated Hermitian block pencil matches the displayed fixture on its real-g slice and has a negative-definite Schur complement for every nonzero scalar; it is not identified with a general complex connection",
    )

    small = b.Fixture(8, 4, "b166_wrap")
    small_form, _ = b.region_pairing(small, 1, small.edge_d[(2, 2)])
    small_numeric = sp.expand(small_form.subs(
        b.carrier_substitution(small, b.graded_carrier(small, 1, sp.Rational(1, 3)))
    ).subs({b.SX: sp.Rational(3, 5), b.MASS: 1}))
    small_e1 = sp.expand(small_numeric[4:, 4:].diff(b.ST))
    sigma, nu = sp.symbols("sigma nu", real=True)
    hodge_b = -nu * sigma / (1 - sigma ** 2)
    checks.add(
        "E-wrap-linear-branch-and-chart-order",
        small_e1.eigenvals() == {
            -sp.Rational(7, 64): 1,
            sp.Rational(7, 64): 1,
            sp.Integer(0): 2,
        }
        and b.inertia_pzn(small_e1) == (1, 2, 1)
        and sp.diff(hodge_b, sigma).subs({sigma: 0}) == -nu
        and sp.expand(hodge_b + nu * sigma) != 0,
        "the displayed 8-by-4 E-live corner has a linear first-order split; b is exact in sigma only through -nu sigma/(1-sigma^2)",
    )

    field = b.graded_carrier(fixture, c, sp.Rational(1, 3))
    plus_sub = b.carrier_substitution(fixture, field)
    minus_sub = b.carrier_substitution(
        fixture, {cell: (-shear, volume) for cell, (shear, volume) in field.items()}
    )
    common = {b.SX: sp.Rational(3, 5), b.MASS: 1}
    plus_zero = sp.expand(form.subs(plus_sub).subs(common).subs({b.ST: 0}))
    minus_zero = sp.expand(form.subs(minus_sub).subs(common).subs({b.ST: 0}))
    plus_live = sp.expand(form.subs(plus_sub).subs(common).subs({b.ST: sp.Rational(1, 5)}))
    minus_live = sp.expand(form.subs(minus_sub).subs(common).subs({b.ST: sp.Rational(1, 5)}))
    signature = sp.diag(*([1] * n + [-1] * n))
    checks.add(
        "F-flip-scope",
        minus_zero == signature * plus_zero * signature
        and minus_live != signature * plus_live * signature,
        "the block-signature flip congruence holds at s_t=0 and fails at the named nonzero-coupling point",
    )

    checks.add(
        "G-exact-bounded-disposition",
        b.no_float((
            flat_pairing, action_block, metric_control, numeric, schur,
            coupled, small_e1, plus_zero, plus_live,
        )),
        "finite supplied carriers only; no two-cone, Page-Wootters, or global off-region conclusion",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
