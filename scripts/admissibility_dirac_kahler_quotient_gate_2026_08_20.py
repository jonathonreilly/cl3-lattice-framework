#!/usr/bin/env python3
"""Corrected Block 158 finite incidence and restriction certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block158-quotient-gate-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
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
    'docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md': '1e49cb0684f1bd3072b070aeead55e169be1e0817c658193582ed51cf5cedf44',
    '.claude/science/physics-loops/toe-axiom-closure-block158-quotient-gate-20260820/NO_GO_LEDGER.md': '55434a22c8bd88e433682f1a795267d27d97b81a9c3d7228f32e203207fa6de6',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
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


def incidence(edges) -> sp.Matrix:
    columns = []
    for source, target in edges:
        column = sp.zeros(h.HALF, 1)
        column[target] += 1
        column[source] -= 1
        columns.append(column)
    return sp.Matrix.hstack(*columns)


def radical_quotient(form: sp.Matrix) -> tuple[int, sp.Matrix]:
    radical = form.nullspace()
    current = sp.Matrix.hstack(*radical) if radical else sp.zeros(form.rows, 0)
    rank = current.rank()
    complement = []
    for index in range(form.rows):
        vector = sp.eye(form.rows)[:, index]
        trial = sp.Matrix.hstack(current, vector)
        if trial.rank() > rank:
            complement.append(vector)
            current, rank = trial, trial.rank()
    basis = sp.Matrix.hstack(*complement)
    return len(radical), sp.expand(basis.T * form * basis)


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-source-input-closure", identity_ok, f"12 literal inputs; actual={actual}")

    cell_index = {cell: index for index, cell in enumerate(h.ODD_CELLS)}
    x_edges = [
        (cell_index[(t, x)], cell_index[(t, (x + 1) % h.LX)])
        for t in (1, 3) for x in range(h.LX)
    ]
    t_edges = [(cell_index[(1, x)], cell_index[(3, x)]) for x in range(h.LX)]
    operator = incidence(x_edges + t_edges)
    ones = sp.ones(1, h.HALF)
    z_basis = sp.Matrix.hstack(
        *(sp.eye(h.HALF)[:, index] - sp.eye(h.HALF)[:, h.HALF - 1]
          for index in range(h.HALF - 1))
    )
    checks.add(
        "B-incidence-image",
        operator.shape == (8, 12)
        and operator.rank() == 7
        and h.zero(ones * operator)
        and sp.Matrix.hstack(operator, z_basis).rank() == 7,
        "eight spatial plus four time links; rank seven; image equals zero-sum space",
    )

    swaps = []
    for index in range(7):
        swap = sp.eye(8)
        swap[index, index] = swap[index + 1, index + 1] = 0
        swap[index, index + 1] = swap[index + 1, index] = 1
        swaps.append(swap)
    seed = sp.Matrix([1, 2, 4, 8, 16, 32, 64, -127])
    differences = [sp.expand(seed - swap * seed) for swap in swaps]
    checks.add(
        "C-standard-orbit",
        sp.Matrix.hstack(*differences).rank() == 7
        and all(sum(vector) == 0 for vector in differences),
        "seven transposition differences span Z; their permutation orbit does too",
    )

    gram = h.herm(h.half_block(h.THETA_PRIME, h.HQ_FREE))
    b10, b11, b12, b13, b30, b31, b32, b33 = h.ODD_SHEAR_COORDS
    representatives = (
        gram.xreplace({b10: 3, b12: 4, b30: 1, b32: 2,
                       b11: 0, b13: 0, b31: 0, b33: 0}),
        gram.xreplace({b10: 0, b12: 0, b30: 0, b32: 0,
                       b11: 1, b13: 1, b31: 1, b33: 1}),
    )
    restricted = tuple(sp.expand(z_basis.T * matrix * z_basis) for matrix in representatives)
    checks.add(
        "D-forced-floor-and-measured-restriction",
        all(h.congruence_inertia(matrix) == (2, 4, 2) for matrix in representatives)
        and all(h.congruence_inertia(matrix) == (2, 3, 2) for matrix in restricted)
        and 2 - 1 == 1,
        "codimension-one floor is one; exact negative index remains two",
    )

    quotients = tuple(radical_quotient(matrix) for matrix in restricted)
    checks.add(
        "E-radical-quotient",
        all(dimension == 3 for dimension, _ in quotients)
        and all(form.shape == (4, 4) for _, form in quotients)
        and all(h.congruence_inertia(form) == (2, 0, 2) for _, form in quotients),
        "three zero directions removed; two negative directions remain",
    )

    differentials, star = h.connection()
    residues = {
        key: h.residue(value)
        for key, value in h.edge_differentials(differentials, star).items()
    }
    parity = all(h.zero(h.X0 * value * h.X0 + value) for value in residues.values())
    bare_mixed = sp.expand(
        h.PLUS.T * h.THETA_PRIME * residues[(0, 0)] * h.MINUS
    )
    bare_live = h.sub_block(
        h.herm(h.half_block(h.THETA_PRIME, residues[(0, 0)])), h.LIVE, h.LIVE
    )
    checks.add(
        "F-parity-versus-full-row",
        parity and h.zero(bare_live) and not h.zero(bare_mixed),
        "bare grading-diagonal zero coexists with a nonzero mixed-half control",
    )

    checks.add(
        "G-exact-finite-scope",
        h.no_float((operator, representatives, restricted, quotients, bare_mixed)),
        "no exhaustive constraint search or physical quotient interpretation",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
