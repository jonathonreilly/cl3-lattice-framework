#!/usr/bin/env python3
"""Corrected Block 159 finite support and link-curvature certificate."""

from __future__ import annotations

import collections
import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block159-link-curvature-scout-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_quotient_gate_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_residue_transversality_gate_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '2601b9fc27fc78df48d22ade9104251fd1da85f174f6c7126cad9e6319ff8068',
    '.claude/science/physics-loops/toe-axiom-closure-block159-link-curvature-scout-20260820/NO_GO_LEDGER.md': '2bd6445238146c6b7f0a968bf22d3806c594ff96062ec3c790d51dc529d791a5',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_quotient_gate_2026_08_20.py': 'ee3631b982733607987698e4d06e5e25052fda843a02c295e048bb77e89a8267',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md': '1e49cb0684f1bd3072b070aeead55e169be1e0817c658193582ed51cf5cedf44',
    'scripts/admissibility_dirac_kahler_residue_transversality_gate_2026_08_20.py': '73ddfb24d417b4a7a517c9561bdb2486a076c2dbe613ad5cb578b40f4742615c',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md': '1709d206ccfcbfda1fbbc4f8473dbf7bbaf4f5b388145b17453a80a4a6234b09',
    'scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py': '08017edef3f69070b00707bb54a1eb9312222d60c9b299822c81964f14ab5926',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '227c121b6ba02f5414af664b2d14a6602338694df18f46c38f7bfa012650df3d',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

ATLAS = {h.SHEAR_X: h.R(3, 5), h.SHEAR_T: h.R(4, 5)}
PROBE_EDGE = (0, 2)


def live_block(differential: sp.Matrix, cover_hodge: sp.Matrix) -> sp.Matrix:
    gram = h.herm(h.half_block(h.THETA_PRIME, h.residue(differential, cover_hodge)))
    return h.sub_block(gram, h.LIVE, h.LIVE)


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-source-input-closure", identity_ok, f"14 literal inputs; actual={actual}")

    differentials, star = h.connection()
    edges = h.edge_differentials(differentials, star)
    probe = sp.expand(edges[PROBE_EDGE].xreplace(ATLAS))
    generic_probe, count = h.reweight(probe, "w")
    generic_residue = h.residue(generic_probe)
    displacement_counts = collections.Counter(
        h.displacement(row, column) for row, column in h.support_of(probe)
    )
    checks.add(
        "B-support-preserving-parity",
        count == 48
        and displacement_counts == {(0, 1): 16, (1, 0): 16, (-1, 0): 16}
        and h.zero(h.X0 * generic_residue * h.X0 + generic_residue)
        and h.zero(h.sub_block(
            h.herm(h.half_block(h.THETA_PRIME, generic_residue)), h.LIVE, h.LIVE
        )),
        "48 independent coefficients remain grading-odd; live-live block zero",
    )

    cover = h.cover_hodge_from_field(h.counterpoint_field())
    far_corner = sp.Matrix(probe)
    two_time = sp.Matrix(probe)
    for t in range(h.COVER_T):
        for x in range(h.LX):
            far_corner[h.fixture.cover_index(t + 1, x + 1), h.fixture.cover_index(t, x)] += sp.Symbol(f"f_{t}_{x}")
            two_time[h.fixture.cover_index(t + 2, x), h.fixture.cover_index(t, x)] += sp.Symbol(f"e_{t}_{x}")
    checks.add(
        "C-even-hop-controls",
        h.live_count(live_block(far_corner, cover)) == 8
        and h.live_count(live_block(two_time, cover)) == 4,
        "far-corner extension opens eight slots; two-time-step extension opens four",
    )

    unit = h.R(3, 5) + sp.I * h.R(4, 5)
    chosen_link = h.TEMPORAL_LINKS[0]
    field = h.link_field({chosen_link: unit})
    dressed = h.dress(probe, field)
    modulus_difference = sp.Matrix(
        h.SIZE,
        h.SIZE,
        lambda i, j: sp.simplify(
            dressed[i, j] * sp.conjugate(dressed[i, j])
            - probe[i, j] * sp.conjugate(probe[i, j])
        ),
    )
    checks.add(
        "D-operator-closure-only",
        h.zero_simplified(modulus_difference)
        and sp.simplify(sp.trace(dressed.H * dressed) - sp.trace(probe.H * probe)) == 0
        and not h.zero(probe),
        "entry moduli and Frobenius norm preserved; conclusion is only about the differential operator",
    )

    balance = h.link_occurrence_balance()
    dipole_counts = {
        len(h.holonomy_census(h.link_field({link: unit}))[1])
        for link in h.ALL_LINKS
    }
    checks.add(
        "E-closed-cover-plaquettes",
        len(balance) == 64
        and set(balance.values()) == {0}
        and dipole_counts == {2},
        "all 64 links cancel in the 32-plaquette product; every single-link field makes a dipole",
    )

    chart_break_counts = set()
    for link in h.ALL_LINKS:
        link_value = h.link_field({link: unit})
        broken = sum(
            not h.zero_simplified(h.dress(matrix.xreplace(ATLAS), link_value) ** 2)
            for matrix in differentials.values()
        )
        chart_break_counts.add(broken)
    phases = {
        (t, x): unit ** ((t + 2 * x) % 4)
        for t in range(h.COVER_T) for x in range(h.LX)
    }
    pure = h.pure_gauge_field(phases)
    pure_nilpotent = all(
        h.zero_simplified(h.dress(matrix.xreplace(ATLAS), pure) ** 2)
        for matrix in differentials.values()
    )
    checks.add(
        "F-chartwise-nilpotency",
        chart_break_counts == {2}
        and pure_nilpotent
        and len(h.holonomy_census(pure)[1]) == 0,
        "single-link curvature breaks two charts and leaves two nilpotent; pure gauge is flat on all four",
    )

    checks.add(
        "G-exact-finite-scope",
        h.no_float((probe, generic_probe, far_corner, two_time, unit, balance)),
        "no image-closure, physical interaction, or exhaustive curvature claim",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
