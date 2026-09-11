#!/usr/bin/env python3
"""Corrected Block 181 finite common-section certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7359_b_fixture_helpers_2026_09_11 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block181-common-differential-section-20260824/NO_GO_LEDGER.md",
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
    'docs/ADMISSIBILITY_DIRAC_KAHLER_COMMON_DIFFERENTIAL_SECTION_BOUNDED_THEOREM_NOTE_2026-08-24.md': '885a665de6b886afdad9fdafeda4fb357a2f7b6e19dffebfd76e2ab9ebf4e564',
    '.claude/science/physics-loops/toe-axiom-closure-block181-common-differential-section-20260824/NO_GO_LEDGER.md': '9a2801dc710febe054e4ce73219ae4aecb9a7e81ff9f700ddbbc9cc1a2e515bc',
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
    naive = sp.expand(sum(differentials.values(), sp.zeros(h.COVER_SIZE, h.COVER_SIZE)) / 4)
    orbit_ok = all(
        h.zero(shifts[origin] * d00 * shifts[origin].T - differentials[origin])
        for origin in h.ORIGINS
    )
    chart_ok = all(
        h.zero(differential ** 2) and differential.rank() == 16
        for differential in differentials.values()
    )
    checks.add(
        "B-chart-orbit-and-naive-average",
        chart_ok and orbit_ok
        and h.zero(data["Ut"] * data["Ux"] - data["Ux"] * data["Ut"])
        and (naive ** 2).rank() == 32,
        "four rank-16 nilpotent chart differentials are plain-shift conjugates; their naive average has full-rank square",
    )

    intertwining = all(
        h.zero(differentials[origin] * shifts[origin] - shifts[origin] * d00)
        for origin in h.ORIGINS
    )
    selected_commutant = sp.eye(h.COVER_SIZE) + d00
    selected_family = all(
        h.zero(
            differentials[origin] * shifts[origin] * selected_commutant
            - shifts[origin] * selected_commutant * d00
        )
        for origin in h.ORIGINS
    )
    checks.add(
        "C-graph-section-intertwiners",
        intertwining and h.zero(selected_commutant * d00 - d00 * selected_commutant) and selected_family,
        "S_o intertwines d_00 with d_o; S_o C_o also intertwines for the displayed nontrivial commuting C_o",
    )

    quotient = data["DQ"]
    dq00 = quotient[(0, 0)]
    anti = data["SQ"][(1, 0)]
    periodic = h.quotient_shift(data["quotient_dimension"], data["quotient_time"], 1, 0, 1)
    spatial = data["SQ"][(0, 1)]
    quotient_ok = all(h.zero(value ** 2) and value.rank() == 8 for value in quotient.values())
    checks.add(
        "D-antiperiodic-acyclic-complex",
        quotient_ok
        and dq00.rows == 16
        and len(dq00.nullspace()) == 8
        and h.zero(anti * dq00 * anti.inv() - quotient[(1, 0)])
        and h.residual_count(periodic * dq00 * periodic.inv() - quotient[(1, 0)]) == 4
        and h.zero(spatial * dq00 * spatial.inv() - quotient[(0, 1)]),
        "rank=8 and d^2=0 on dimension 16 imply im(d)=ker(d), with an eight-dimensional nonempty kernel; only the displayed temporal descent needs antiperiodic wrap",
    )

    hodge = data["H"]
    section_hodge = data["Hs"]
    flat = h.flat_hodge_cover()
    leading_minors_positive = all(
        section_hodge[:size, :size].det() > 0
        for size in range(1, h.COVER_SIZE + 1)
    )
    checks.add(
        "E-section-hodge-controls",
        h.zero(section_hodge - section_hodge.T)
        and leading_minors_positive
        and h.residual_count(section_hodge - hodge) == 96
        and h.zero(flat - sp.eye(h.COVER_SIZE))
        and h.residual_count(section_hodge - flat) == 96
        and sp.expand(section_hodge.trace()) == h.R(927831123589, 27222868400),
        "the supplied equal-weight section Hodge is symmetric positive definite and differs from the raw and flat matrices at 96 entries; its trace is the stated finite control",
    )

    q_section = h.completion(section_hodge, d00)
    covariance = all(
        h.zero(
            shifts[origin] * q_section * shifts[origin].T
            - h.completion(
                shifts[origin] * section_hodge * shifts[origin].T,
                differentials[origin],
            )
        )
        for origin in h.ORIGINS
    )
    landed = h.b128.build_completions()
    z14 = {
        completion.origin: sp.expand(sp.Matrix(completion.physical_action).charpoly().all_coeffs()[2])
        for completion in landed
    }
    expected_z14 = {
        (1, 0): h.R(1195620534151694060907411, 62608868331486568000000),
        (1, 1): h.R(8650195819888697214240517, 435757723587146513280000),
    }
    checks.add(
        "F-covariance-and-landed-contrast",
        covariance and z14 == expected_z14 and len(set(z14.values())) == 2,
        "the section completion is chart-covariant; the two supplied Block-128 physical completions have different exact z^14 characteristic coefficients",
    )

    q_physical = sp.Matrix(h.b128.antiperiodic_quotient(q_section))
    generator = h.b128.block105.translation_matrix((0, 1))
    doubled_generator = sp.diag(generator, generator)
    section_form = sp.Matrix(h.b128.grassmann_form(q_physical))
    flat_physical = sp.Matrix(h.b128.antiperiodic_quotient(h.completion(flat, d00)))
    flat_form = sp.Matrix(h.b128.grassmann_form(flat_physical))
    checks.add(
        "G-translation-noninvariance-controls",
        (section_form * doubled_generator - doubled_generator * section_form).rank() == 32
        and (flat_form * doubled_generator - doubled_generator * flat_form).rank() == 32,
        "both the section completion and flat-Hodge control have rank-32 spatial translation commutators; this measures noninvariance, not curvature",
    )

    dimension = dq00.rows
    commutator_map = sp.Matrix(
        sp.kronecker_product(sp.eye(dimension), dq00)
        - sp.kronecker_product(dq00.T, sp.eye(dimension))
    )
    centralizer_dimension = dimension * dimension - commutator_map.rank()
    checks.add(
        "H-centralizer-and-bounded-scope",
        centralizer_dimension == 128
        and h.no_float((data, naive, section_hodge, q_section, z14)),
        "the complex commutant of the displayed quotient differential has dimension 128; it is not a Hodge or section-moduli dimension, and equal weights are supplied rather than unique",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
