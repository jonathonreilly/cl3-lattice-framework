#!/usr/bin/env python3
"""Corrected Block 156 finite Gram and transversality certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block156-residue-transversality-gate-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_unique_completion_price_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md': '1709d206ccfcbfda1fbbc4f8473dbf7bbaf4f5b388145b17453a80a4a6234b09',
    '.claude/science/physics-loops/toe-axiom-closure-block156-residue-transversality-gate-20260820/NO_GO_LEDGER.md': 'b2f224ac4bac2b8f7bf7146adfadfba036554f63393f3715be108320d8975cba',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_discriminator_verdict_2026_08_20.py': '08017edef3f69070b00707bb54a1eb9312222d60c9b299822c81964f14ab5926',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_DISCRIMINATOR_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '227c121b6ba02f5414af664b2d14a6602338694df18f46c38f7bfa012650df3d',
    'scripts/admissibility_dirac_kahler_unique_completion_price_2026_08_20.py': '806e4dc362c468703303f943beb6ccde039c8a6f262c50a80c3153ef828c80ff',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_UNIQUE_COMPLETION_PRICE_BOUNDED_THEOREM_NOTE_2026-08-20.md': 'b2e5d57e255dae4f010988c0dc823607260179006860cc5b45619898535f19d4',
    'scripts/admissibility_dirac_kahler_bare_character_2026_08_20.py': 'af15e1cdd0bded4bfc37edfd49ebbb572b2ced3233e137ddec2532dc0ac32c51',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md': '830435f2f820728c213a24665958ee82abb1c1622b7b5a56018de10251a55dcd',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

PAIRS_R = ((0, 3), (1, 2), (4, 7), (5, 6))


def equation_rows(sign: int) -> sp.Matrix:
    return sp.Matrix(
        [[(1 if k == i else 0) + sign * (1 if k == j else 0)
          for k in range(8)] for i, j in PAIRS_R]
    )


def hermiticity_map(operator: sp.Matrix) -> sp.Matrix:
    raw = h.half_block(operator, h.HQ_FREE)
    conditions = [
        sp.expand(raw[i, j] - sp.conjugate(raw[j, i]))
        for i in range(h.HALF) for j in range(i + 1, h.HALF)
    ]
    conditions = [value for value in conditions if value != 0]
    return sp.Matrix(
        [[value.coeff(variable) for variable in h.ODD_SHEAR_COORDS]
         for value in conditions]
    )


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-source-input-closure", identity_ok, f"14 literal inputs; actual={actual}")

    gram = h.herm(h.half_block(h.THETA_PRIME, h.HQ_FREE))
    b10, b11, b12, b13, b30, b31, b32, b33 = h.ODD_SHEAR_COORDS
    closed = sp.zeros(h.HALF)
    closed[0, 0], closed[2, 2] = b30 / 4, b32 / 4
    closed[5, 5], closed[7, 7] = -b10 / 4, -b12 / 4
    closed[1, 3] = closed[3, 1] = (b31 + b33) / 8
    closed[4, 6] = closed[6, 4] = -(b11 + b13) / 8
    theta_map = hermiticity_map(h.THETA)
    prime_map = hermiticity_map(h.THETA_PRIME)
    checks.add(
        "B-exact-gram-and-loci",
        h.zero(gram - closed)
        and (prime_map.rank(), 8 - prime_map.rank()) == (2, 6)
        and (theta_map.rank(), 8 - theta_map.rank()) == (4, 4),
        "closed Gram reproduced; theta-prime locus 2/6 and theta locus 4/4",
    )

    type_a = gram.xreplace({
        b10: 3, b12: 4, b30: 1, b32: 2,
        b11: 0, b13: 0, b31: 0, b33: 0,
    })
    type_b = gram.xreplace({
        b10: 0, b12: 0, b30: 0, b32: 0,
        b11: 1, b13: 1, b31: 1, b33: 1,
    })
    counterpoint = gram.xreplace(h.modulus_point(h.counterpoint_field()))
    checks.add(
        "C-finite-inertia-controls",
        h.congruence_inertia(type_a) == (2, 4, 2)
        and h.congruence_inertia(type_b) == (2, 4, 2)
        and h.congruence_inertia(counterpoint) == (4, 4, 0),
        "two signed branches (2,4,2); zero-connection counterpoint (4,4,0)",
    )

    l145 = equation_rows(-1)
    l147 = equation_rows(1)
    l154 = sp.Matrix(
        [[0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1]]
    )
    checks.add(
        "D-linear-transversality",
        (8 - l145.rank(), 8 - l147.rank(), 8 - l154.rank()) == (4, 4, 6)
        and sp.Matrix.vstack(l145, l147).rank() == 8
        and sp.Matrix.vstack(l145, l154).rank() == 6
        and sp.Matrix.vstack(l147, l154).rank() == 6,
        "L145/L147 complementary; both intersections with L154 have dimension two",
    )

    p, q = sp.symbols("p q", real=True)
    expected = (
        (q / 4, -q / 4, -p / 4, p / 4),
        (-q / 4, q / 4, p / 4, -p / 4),
    )
    diagonals = []
    for locus in (l145, l147):
        basis = sp.Matrix.hstack(*sp.Matrix.vstack(locus, l154).nullspace())
        vector = basis * sp.Matrix([p, q])
        restricted = gram.xreplace(
            {h.ODD_SHEAR_COORDS[index]: vector[index] for index in range(8)}
        )
        diagonals.append(tuple(sp.expand(restricted[k, k]) for k in h.LIVE))
    nonzero_probes = (
        gram.xreplace({
            h.ODD_SHEAR_COORDS[index]:
                (sp.Matrix.hstack(*sp.Matrix.vstack(l145, l154).nullspace()) * sp.Matrix([1, 0]))[index]
            for index in range(8)
        }),
        gram.xreplace({
            h.ODD_SHEAR_COORDS[index]:
                (sp.Matrix.hstack(*sp.Matrix.vstack(l147, l154).nullspace()) * sp.Matrix([0, 1]))[index]
            for index in range(8)
        }),
    )
    checks.add(
        "E-psd-intersection-scope",
        tuple(diagonals) == expected
        and all(h.congruence_inertia(matrix)[2] > 0 for matrix in nonzero_probes)
        and h.zero(sp.zeros(8)),
        "nonzero intersection points are indefinite at nonzero mass; mass zero yields the zero form without killing p,q",
    )

    differentials, star = h.connection()
    residues = h.edge_differentials(differentials, star)
    residues = {key: h.residue(value) for key, value in residues.items()}
    live_live_zero = all(
        h.zero(h.sub_block(h.anti(h.half_block(h.THETA_PRIME, value)), h.LIVE, h.LIVE))
        and h.zero(h.sub_block(h.herm(h.half_block(h.X0, value)), h.LIVE, h.LIVE))
        for value in residues.values()
    )
    dead_live_nonzero = all(
        not h.zero(h.sub_block(h.herm(h.half_block(h.THETA_PRIME, value)), h.DEAD, h.LIVE))
        for value in residues.values()
    )
    checks.add(
        "F-bare-residue-channels",
        live_live_zero and dead_live_nonzero,
        "two bare live-live channels zero on 16 edges; dead-live controls nonzero",
    )

    checks.add(
        "G-exact-scope",
        h.no_float((gram, type_a, type_b, counterpoint, diagonals)),
        "finite forms and explicit linear loci only",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
