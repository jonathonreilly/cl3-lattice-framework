#!/usr/bin/env python3
"""Corrected Block 153 certificate on the supplied finite matrices."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block153-bare-character-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md': '830435f2f820728c213a24665958ee82abb1c1622b7b5a56018de10251a55dcd',
    '.claude/science/physics-loops/toe-axiom-closure-block153-bare-character-20260820/NO_GO_LEDGER.md': 'ab432d7c306649e36133f44929ded2495fc13401e10c1fec6f86c8becc3e7a8f',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

CHART01_EDGES = ((0, 0), (0, 1), (1, 0), (1, 1))
IMPORTED_MASS = h.R(2, 7)


def diagonal_live(matrix: sp.MatrixBase) -> int:
    return sum(sp.expand(matrix[k, k]) != 0 for k in range(h.HALF))


def forcing_system(name: str, pairing: sp.Matrix, gram: sp.Matrix) -> tuple:
    diagonal_source = gram if name == "theta-prime" else pairing
    slots = [
        k for k in range(h.HALF) if sp.expand(diagonal_source[k, k]) == 0
    ]
    rows = []
    for k in slots:
        for j in range(h.HALF):
            for part in (sp.re(pairing[k, j]), sp.im(pairing[k, j])):
                part = sp.expand(part)
                if part != 0:
                    rows.append(
                        [part.coeff(value, 1) for value in h.ODD_SHEAR_COORDS]
                    )
    matrix = sp.Matrix(rows)
    return matrix.rank(), sp.factor((matrix.T * matrix).det())


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_input_hashes(INPUT_SHA256)
    checks.add("A-source-input-closure", identity_ok, f"8 literal inputs; actual={actual}")

    moves = h.COVARIANT_MOVES
    bare = tuple(label for label in moves if h.kappa(label) == 0)
    homomorphism = all(
        h.kappa(h.compose_labels(left, right))
        == (h.kappa(left) + h.kappa(right)) % 2
        for left in moves
        for right in moves
    )
    checks.add(
        "B-character",
        len(moves) == 64
        and len(bare) == 32
        and sum(label[0] == 1 for label in bare) == 16
        and sum(label[0] == -1 for label in bare) == 16
        and homomorphism,
        "64 moves; kernel 32 = 16 translations + 16 reflections; all 4096 composites",
    )

    commutation = all(
        h.zero(
            h.DESCENT[label] * h.X0
            - (-1) ** h.kappa(label) * h.X0 * h.DESCENT[label]
        )
        for label in moves
    )
    checks.add(
        "C-grading-character",
        commutation
        and h.kappa(h.THETA_LABEL) == 1
        and h.kappa(h.THETA_PRIME_LABEL) == 0,
        "same character controls X0 commutation; no liveness converse is asserted",
    )

    differentials, star = h.connection()
    edges = h.edge_differentials(differentials, star)
    residues = {key: h.residue(value) for key, value in edges.items()}
    parity = h.zero(h.X0 * h.HQ_FREE * h.X0 - h.HQ_FREE) and all(
        h.zero(h.X0 * value * h.X0 + value) for value in residues.values()
    )
    mass_grams = {
        "theta": h.herm(h.half_block(h.THETA, h.HQ_FREE)),
        "theta-prime": h.herm(h.half_block(h.THETA_PRIME, h.HQ_FREE)),
    }
    connection_diagonals = {
        name: {
            diagonal_live(h.herm(h.half_block(operator, residues[key])))
            for key in h.EDGE_KEYS
        }
        for name, operator in (("theta", h.THETA), ("theta-prime", h.THETA_PRIME))
    }
    checks.add(
        "D-parity-and-displayed-liveness",
        parity
        and diagonal_live(mass_grams["theta"]) == 0
        and diagonal_live(mass_grams["theta-prime"]) == 4
        and connection_diagonals["theta"] == {4}
        and connection_diagonals["theta-prime"] == {0}
        and h.zero(sp.zeros(h.PHYS)),
        "forbidden blocks vanish; theta/theta-prime liveness is evaluated separately",
    )

    pairings = {}
    for name, operator in (("theta", h.THETA), ("theta-prime", h.THETA_PRIME)):
        for key in CHART01_EDGES:
            action = sp.expand(h.MASS * h.HQ_FREE + residues[key])
            pairings[(name, key)] = h.herm(h.half_block(operator, action))
    prime_results = {
        forcing_system(
            "theta-prime",
            pairings[("theta-prime", key)],
            mass_grams["theta-prime"],
        )
        for key in CHART01_EDGES
    }
    theta_results = {
        forcing_system("theta", pairings[("theta", key)], mass_grams["theta"])
        for key in CHART01_EDGES
    }
    expected_prime = (
        (h.SHEAR_T**2 + h.SHEAR_X**2) ** 6
        * (4 * h.MASS**2 + h.SHEAR_T**2 + h.SHEAR_X**2) ** 2
        / 2**48
    )
    prime_rank, prime_det = next(iter(prime_results))
    theta_rank_st0 = forcing_system(
        "theta",
        pairings[("theta", (0, 0))].subs({h.SHEAR_T: 0, h.SHEAR_X: h.R(3, 5)}),
        mass_grams["theta"],
    )[0]
    prime_rank_st0 = forcing_system(
        "theta-prime",
        pairings[("theta-prime", (0, 0))].subs({h.SHEAR_T: 0, h.SHEAR_X: h.R(3, 5)}),
        mass_grams["theta-prime"],
    )[0]
    checks.add(
        "E-forcing-determinant",
        len(prime_results) == 1
        and len(theta_results) == 1
        and prime_rank == 8
        and sp.simplify(prime_det - expected_prime) == 0
        and prime_det.subs({h.SHEAR_X: 0, h.SHEAR_T: 0}) == 0
        and (theta_rank_st0, prime_rank_st0) == (4, 8),
        "determinant is zero at the origin; ranks at (3/5,0) are theta 4 and theta-prime 8",
    )

    carriers = (
        h.flat_field(),
        h.fixture.block105.overlap_field(),
        h.witness_field(),
        h.escape_witness_field(),
        {
            cell: (
                h.R(3, 5) if cell[0] % 2 else h.R(-1, 3),
                h.R(7, 4) if cell[1] % 2 else h.R(2, 5),
            )
            for cell in h.CELLS
        },
    )
    scan_count = sum(
        1
        for field in carriers
        for _key in h.EDGE_KEYS
        for _operator in (h.THETA, h.THETA_PRIME)
    )
    checks.add(
        "F-scan-domain",
        len(carriers) == 5 and scan_count == 160 and IMPORTED_MASS == h.R(2, 7),
        "domain cardinality only: five carriers x sixteen edges x two operators at one imported mass",
    )

    checks.add(
        "G-exact-scope",
        h.no_float((moves, prime_det, IMPORTED_MASS)),
        "finite supplied-matrix theorem; no generic physical or continuum inference",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
