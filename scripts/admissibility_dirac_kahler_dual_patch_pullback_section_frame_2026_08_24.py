#!/usr/bin/env python3
"""Corrected Block 182 finite pullback and signed-shift certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7359_b_fixture_helpers_2026_09_11 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block182-dual-patch-pullback-section-frame-20260824/NO_GO_LEDGER.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
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
    'docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_THEOREM_NOTE_2026-08-24.md': 'd5e8f667c804c09ac904b33463f9a939de3a8c53318a6dcaac088a5be46b3bf3',
    '.claude/science/physics-loops/toe-axiom-closure-block182-dual-patch-pullback-section-frame-20260824/NO_GO_LEDGER.md': 'f0d8b8fc05f519c19492059986f6743a00841723e655ac027a86f3f68e5bbd2b',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_THEOREM_NOTE_2026-08-24.md': '885a665de6b886afdad9fdafeda4fb357a2f7b6e19dffebfd76e2ab9ebf4e564',
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
    shifts, differentials = data["S"], data["D"]
    d00 = differentials[(0, 0)]
    hodge = data["H"]
    section_hodge = data["Hs"]
    symbolic_mass = sp.Symbol("m", positive=True)

    analysis = sp.Matrix.vstack(*[
        shifts[origin] / 2 for origin in h.ORIGINS
    ])
    patch_differential = sp.diag(*[differentials[origin] for origin in h.ORIGINS])
    patch_hodge = sp.diag(*[hodge for _origin in h.ORIGINS])
    patch_action = h.completion(patch_hodge, patch_differential, symbolic_mass)
    section_action = h.completion(section_hodge, d00, symbolic_mass)
    checks.add(
        "B-patch-pullback-identities",
        analysis.shape == (128, 32)
        and h.zero(analysis.T * analysis - sp.eye(h.COVER_SIZE))
        and h.zero(patch_differential * analysis - analysis * d00)
        and h.zero(analysis.T * patch_hodge * analysis - section_hodge)
        and h.zero(analysis.T * patch_action * analysis - section_action)
        and symbolic_mass in patch_action.free_symbols,
        "the halved four-chart graph section is an isometry and exactly pulls back D, H, and the symbolic-mass completion",
    )

    grade = h.exterior_grade(h.COVER_TIME)
    quotient_grade = h.exterior_grade(data["quotient_time"])
    patch_grade_canonical = sp.diag(*[grade for _origin in h.ORIGINS])
    patch_grade_transported = sp.diag(*[
        sp.expand(shifts[origin] * grade * shifts[origin].T)
        for origin in h.ORIGINS
    ])
    canonical_defect = sp.expand(
        patch_grade_canonical * patch_differential
        - patch_differential * patch_grade_canonical
        - patch_differential
    )
    transported_defect = sp.expand(
        patch_grade_transported * patch_differential
        - patch_differential * patch_grade_transported
        - patch_differential
    )
    checks.add(
        "C-grade-cotransport",
        h.zero(grade * d00 - d00 * grade - d00)
        and h.zero(
            quotient_grade * data["DQ"][(0, 0)]
            - data["DQ"][(0, 0)] * quotient_grade
            - data["DQ"][(0, 0)]
        )
        and canonical_defect.rank() == 48
        and transported_defect.rank() == 0
        and h.zero(patch_grade_transported * analysis - analysis * grade),
        "the exterior grade raises d_00 by one; the repeated canonical patch grade fails with rank 48, while the cotransported grade closes",
    )

    temporal, spatial = data["Ut"], data["Ux"]
    sign = h.sign_field(h.COVER_TIME)
    signed_temporal = sp.expand(sign * temporal)
    flat_action = h.completion(sp.eye(h.COVER_SIZE), d00)
    signed_image = sp.expand(signed_temporal * d00 * signed_temporal.T)
    checks.add(
        "D-signed-shift-controls",
        h.zero(signed_temporal * spatial + spatial * signed_temporal)
        and h.zero(signed_temporal ** 2 - temporal ** 2)
        and not h.zero(temporal ** 2 - sp.eye(h.COVER_SIZE))
        and not h.zero(spatial ** 2 - sp.eye(h.COVER_SIZE))
        and h.zero(temporal ** 2 * flat_action - flat_action * temporal ** 2)
        and h.zero(spatial ** 2 * flat_action - flat_action * spatial ** 2)
        and (temporal * flat_action - flat_action * temporal).rank() == 24
        and h.zero(signed_image ** 2)
        and signed_image.rank() == 16
        and h.zero(signed_image - sign * differentials[(1, 0)] * sign),
        "the displayed signed lifts anticommute and have the stated two-step and rank controls; no complex-gauge or Ward interpretation is made",
    )

    field = h.b128.block105.overlap_field()
    field_hodge = h.hodge_cover(field)
    signed_hodge_image = sp.expand(signed_temporal * field_hodge * signed_temporal.T)
    translated = h.hodge_cover(h.shifted_field(field, 1, 0))
    flipped_translated = h.hodge_cover(h.shifted_field(h.flipped_field(field), 1, 0))
    plain_covariance = (
        h.zero(spatial * field_hodge * spatial.T - h.hodge_cover(h.shifted_field(field, 0, 1)))
        and h.zero(temporal * field_hodge * temporal.T - translated)
    )
    checks.add(
        "E-hodge-shift-and-shear-flip",
        h.zero(field_hodge - hodge)
        and plain_covariance
        and h.zero(signed_hodge_image - flipped_translated)
        and (signed_hodge_image - translated).rank() == 32
        and (temporal * field_hodge * temporal.T - flipped_translated).rank() == 32,
        "the current overlap Hodge is plain-shift covariant; the signed temporal lift implements the displayed shear flip, with both omitted controls rank 32",
    )

    periodic = h.periodic_fine_differential()
    antiperiodic = data["DQ"][(0, 0)]
    difference = sp.expand(antiperiodic - periodic)
    seam = tuple(
        (row, column)
        for row in range(difference.rows)
        for column in range(difference.cols)
        if difference[row, column] != 0
        and (row // h.SPACE_EXTENT, column // h.SPACE_EXTENT)
        in ((data["quotient_time"] - 1, 0), (0, data["quotient_time"] - 1))
    )
    seam_negated = sp.Matrix(periodic)
    for row in range(seam_negated.rows):
        for column in range(seam_negated.cols):
            if (row // h.SPACE_EXTENT, column // h.SPACE_EXTENT) in (
                (data["quotient_time"] - 1, 0),
                (0, data["quotient_time"] - 1),
            ):
                seam_negated[row, column] = -seam_negated[row, column]
    checks.add(
        "F-periodic-antiperiodic-comparison",
        periodic.rank() == 6
        and antiperiodic.rank() == 8
        and h.residual_count(difference) == 32
        and len(seam) == 4
        and not h.zero(antiperiodic - seam_negated),
        "the two supplied dimension-16 operators have ranks 6 and 8 and differ in 32 entries, only four on the temporal seam; this bars similarity but does not isolate a causal twist",
    )

    def section_completion(source: dict) -> sp.Matrix:
        raw = h.hodge_cover(source)
        averaged = sp.expand(sum(
            (shifts[origin].T * raw * shifts[origin] for origin in h.ORIGINS),
            sp.zeros(h.COVER_SIZE, h.COVER_SIZE),
        ) / 4)
        return h.completion(averaged, d00)

    temporal_two, spatial_two = temporal ** 2, spatial ** 2
    section_field_action = section_completion(field)
    two_step = (
        h.zero(temporal_two * section_field_action * temporal_two.T - section_completion(h.shifted_field(field, 2, 0)))
        and h.zero(spatial_two * section_field_action * spatial_two.T - section_completion(h.shifted_field(field, 0, 2)))
    )
    checks.add(
        "G-bounded-finite-scope",
        two_step and h.no_float((data, analysis, patch_action, canonical_defect, field_hodge, periodic, antiperiodic)),
        "exact supplied matrices only; the rank contrast, pullbacks, grades, and shift identities do not establish gravity, a Ward contraction, or an exhaustive boundary classification",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
