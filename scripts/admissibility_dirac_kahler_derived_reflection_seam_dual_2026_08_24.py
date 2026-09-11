#!/usr/bin/env python3
"""Corrected Block 183 finite reflection, dual, and orbit certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7359_b_fixture_helpers_2026_09_11 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block183-derived-reflection-seam-dual-20260824/NO_GO_LEDGER.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_released7359_b_fixture_helpers_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_THEOREM_NOTE_2026-08-24.md': '2ec458ed791dad84e3b33d936f11b39327fe062b53f6dd44ae8070086195c8d9',
    '.claude/science/physics-loops/toe-axiom-closure-block183-derived-reflection-seam-dual-20260824/NO_GO_LEDGER.md': '7d909fb7b48fbc24d8158e687646001896e37b295b076913827152033faa80a9',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_THEOREM_NOTE_2026-08-24.md': 'd5e8f667c804c09ac904b33463f9a939de3a8c53318a6dcaac088a5be46b3bf3',
    'scripts/admissibility_dirac_kahler_released7359_b_fixture_helpers_2026_09_11.py': 'e3fdea9bda15e830a577419c712197786e5bb4bbc86c4070e50bc3e95301d192',
    'scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py': '594e7032f453fec4c6791067a147d1544636ddce9567a87a3449352b5546d5f5',
    'scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py': '8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2',
    'scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py': '4299d645f687bec12d945598cca1df5c13a73c871a9e6ad1459e7e6b17c5bab5',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md': 'b3e42b85ff4bd29edd2d3c65bb1685503560af6b512013e062a93601c8661990',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_hashes(INPUT_SHA256)
    supplier_ok, supplier_actual = h.supplier_certificate()
    checks.add(
        "A-source-input-closure",
        identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS and supplier_ok,
        f"{len(INPUT_SHA256)} literal inputs; actual={actual}; suppliers={supplier_actual}",
    )

    data = h.section_data()
    temporal, spatial = data["Ut"], data["Ux"]
    d00 = data["D"][(0, 0)]
    d10 = data["D"][(1, 0)]
    field = h.b128.block105.overlap_field()
    reflected = h.reflected_field(field)
    field_hodge = h.hodge_cover(field)
    edge = h.edge_reflection()
    reflection = sp.expand(edge * h.time_parity())
    inverse = reflection.T
    reflected_differential = sp.expand(reflection * d00 * inverse)

    cell_factorization = True
    for time in range(h.COVER_TIME):
        for space in range(h.SPACE_EXTENT):
            image = sp.expand(reflection * h.b128.cover_embedding(time, space))
            target = sp.expand(
                h.b128.cover_embedding((6 - time) % h.COVER_TIME, space)
                * (sp.Integer(-1) ** time * h.CELL_MAP)
            )
            cell_factorization &= h.zero(image - target)
    checks.add(
        "B-convention-conditioned-reflection",
        h.zero(reflection * inverse - sp.eye(h.COVER_SIZE))
        and h.zero(reflection ** 2 + sp.eye(h.COVER_SIZE))
        and not h.zero(reflection ** 2 - sp.eye(h.COVER_SIZE))
        and h.zero(edge ** 2 - sp.eye(h.COVER_SIZE))
        and h.zero(h.CELL_MAP ** 2 + sp.eye(4))
        and h.zero(h.UNDRESSED_CELL_MAP ** 2 - sp.eye(4))
        and cell_factorization,
        "the displayed time-parity-dressed site reflection squares to -I and factorizes through the signed cell map; undressed site/corner swaps square to +I",
    )

    grade = h.exterior_grade(h.COVER_TIME)
    transported_grade = sp.expand(reflection * grade * inverse)
    checks.add(
        "C-reflected-differential-controls",
        h.zero(reflected_differential ** 2)
        and reflected_differential.rank() == 16
        and h.grade_jump_census(d00, grade) == {1: 32}
        and h.grade_jump_census(reflected_differential, grade) == {-1: 16, 1: 16}
        and h.residual_count(grade * reflected_differential - reflected_differential * grade - reflected_differential) == 16
        and h.zero(
            transported_grade * reflected_differential
            - reflected_differential * transported_grade
            - reflected_differential
        )
        and all(h.residual_count(reflected_differential - candidate) != 0 for candidate in (
            d00, -d00, d00.H, -d00.H, d10, -d10, d10.H, -d10.H
        )),
        "the reflected rank-16 nilpotent is graded only by the transported grade and differs from the eight displayed neighbouring differentials",
    )

    q, volume = sp.symbols("q v")
    dual = h.dual_block(q, volume)
    closed_form = sp.Matrix([
        [-volume / (q ** 2 - 1), 0, 0, -q * volume / (q ** 2 - 1)],
        [0, 1 / volume, 0, 0],
        [0, 0, volume, 0],
        [-q * volume / (q ** 2 - 1), 0, 0, -volume / (q ** 2 - 1)],
    ])
    neighbours = (
        h.shear_block(q, volume),
        h.shear_block(-q, volume),
        h.shear_block(q, volume).inv(),
        h.shear_block(-q, volume).inv(),
        h.shear_block(q, 1 / volume),
        h.shear_block(-q, 1 / volume),
    )
    checks.add(
        "D-symbolic-dual-block",
        h.zero(sp.simplify(dual - closed_form))
        and all(h.residual_count(sp.simplify(dual - neighbour)) != 0 for neighbour in neighbours)
        and h.zero(h.dual_block(0, 1) - h.shear_block(0, 1)),
        "M H(q,v) M^T has the displayed rational form for q^2!=1 and v!=0; six rational-function differences are generic, while q=0,v=1 is an equality specialization",
    )

    dual_reflected_hodge = h.hodge_cover(reflected, h.dual_block)
    checks.add(
        "E-hodge-reflection-identity",
        h.zero(field_hodge - h.b128.curved_hodge_cover())
        and h.zero(reflection * field_hodge * inverse - dual_reflected_hodge)
        and h.residual_count(edge * field_hodge * edge.T - dual_reflected_hodge) != 0
        and h.residual_count(reflection * field_hodge * inverse - h.hodge_cover(reflected)) != 0,
        "the convention-defined reflection sends the supplied Hodge matrix to the reflected-field dual; dropping either parity dressing or dualization fails",
    )

    checks.add(
        "F-shift-conjugation-table",
        h.zero(reflection * temporal * inverse + temporal.T)
        and not h.zero(reflection * temporal * inverse - temporal.T)
        and h.zero(reflection * spatial * inverse - spatial),
        "on the displayed carrier R U_t R^-1=-U_t^-1 and R U_x R^-1=U_x",
    )

    closed_sets = h.equal_weight_reflection_sets()
    all_sufficient = True
    for exponents in closed_sets:
        shifts = h.shift_set(exponents)
        averaged = h.orbit_average(field_hodge, shifts)
        averaged_dual = h.orbit_average(dual_reflected_hodge, shifts)
        all_sufficient &= h.zero(reflection * averaged * inverse - averaged_dual)

    asymmetric_weights = {0: h.R(1, 2), 1: h.R(1, 4), 3: h.R(1, 4)}
    asymmetric = h.weighted_temporal_average(field_hodge, asymmetric_weights)
    asymmetric_dual = h.weighted_temporal_average(dual_reflected_hodge, asymmetric_weights)
    duplicate_minimal = h.orbit_average(field_hodge, h.shift_set((0,)))
    duplicate_zero_four = h.orbit_average(field_hodge, h.shift_set((0, 4)))
    full = h.orbit_average(field_hodge, h.shift_set(tuple(range(h.COVER_TIME))))
    checks.add(
        "G-sufficient-average-families",
        len(closed_sets) == 16
        and all_sufficient
        and asymmetric_weights[1] != asymmetric_weights.get(7, 0)
        and h.zero(reflection * asymmetric * inverse - asymmetric_dual)
        and h.zero(duplicate_minimal - duplicate_zero_four)
        and h.residual_count(duplicate_minimal - full) == 96,
        "the 16 reflection-paired equal-weight sets are sufficient, not exhaustive or distinct: an asymmetric mod-8 example closes and {0},{0,4} coincide; the minimal and full averages differ at 96 entries",
    )

    four_shifts = tuple(
        sp.expand(temporal ** origin[0] * spatial ** origin[1])
        for origin in h.ORIGINS
    )
    reflected_four_shifts = tuple(
        sp.expand(temporal.T ** origin[0] * spatial ** origin[1])
        for origin in h.ORIGINS
    )
    section_hodge = h.orbit_average(field_hodge, four_shifts)
    section_dual = h.orbit_average(dual_reflected_hodge, reflected_four_shifts)
    symbolic_mass = sp.Symbol("m", positive=True)
    section_action = h.completion(section_hodge, d00, symbolic_mass)
    checks.add(
        "H-finite-action-corollary-and-scope",
        h.zero(
            reflection * section_action * inverse
            - h.completion(section_dual, reflected_differential, symbolic_mass)
        )
        and h.no_float((data, reflected_differential, dual, field_hodge, asymmetric, full)),
        "the Hodge identity extends through the stipulated completion when the RHS uses reflected temporal exponents {0,-1}; no OS positivity, Gram, uniqueness, or physical reflection claim follows",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
