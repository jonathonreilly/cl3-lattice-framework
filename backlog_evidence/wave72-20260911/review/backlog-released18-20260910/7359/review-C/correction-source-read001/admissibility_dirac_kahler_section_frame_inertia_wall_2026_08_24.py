#!/usr/bin/env python3
"""Corrected Block 186 finite section-frame inertia certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11 as f


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SECTION_FRAME_INERTIA_WALL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block186-section-frame-inertia-wall-20260824/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SECTION_FRAME_INERTIA_WALL_BOUNDED_THEOREM_NOTE_2026-08-24.md': 'd194cec4026b6885f5da6af311f92059a67e10cdecf701e2b0ce09fe4476692c',
    '.claude/science/physics-loops/toe-axiom-closure-block186-section-frame-inertia-wall-20260824/NO_GO_LEDGER.md': '1df18679f45cc677ae463b23917636e53cb2a9ee7585270180a63f832c0bc981',
    'scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py': 'd56cb24eeb93ea34268a4a48e5c5cc9c59958b45a6818c192a927bfb42ebd436',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md': '6fe011fe12de417f4dcbe85fcf9df6b4d3477738caedb04fcc8d43997fd842c1',
    'scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py': '4299d645f687bec12d945598cca1df5c13a73c871a9e6ad1459e7e6b17c5bab5',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md': 'b3e42b85ff4bd29edd2d3c65bb1685503560af6b512013e062a93601c8661990',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

MASS = sp.Rational(9, 20)
SEAM_PARAMETER = sp.Rational(1, 5)
MASS_SWEEP = (
    sp.Rational(1, 3),
    MASS,
    sp.Integer(1),
    sp.Integer(2),
    sp.Integer(10),
)
LAMBDA = sp.Symbol("lambda")


def charpoly_coefficients(matrix: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(reversed(sp.Poly(matrix.charpoly(LAMBDA).as_expr(), LAMBDA).all_coeffs()))


def main() -> int:
    checks = f.Checks()
    identity_ok, actual = f.verify_input_hashes(INPUT_SHA256)
    checks.add(
        "A-source-input-closure",
        identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS,
        f"{len(INPUT_SHA256)} literal current inputs; actual={actual}",
    )

    differential = sp.Matrix(f.b128.chart_differential_cover((0, 0)))
    field = f.b128.block105.overlap_field()
    reflection = sp.expand(
        f.reflection_permutation(f.link_theta) * f.section_space_parity()
    )
    spatial_shift = f.cover_shift(0, 1)
    cells = f.section_cells()

    def intra_cell(row: int, column: int) -> bool:
        return any(row in cell and column in cell for cell in cells)

    differential_positions = tuple(
        (row, column)
        for row in range(f.COVER_SIZE)
        for column in range(f.COVER_SIZE)
        if differential[row, column] != 0
    )
    curved_hodge = f.section_hodge_from_blocks(
        lambda time, space: f.shear_block(
            *field[(time % f.PHYSICAL_TIME_EXTENT, space)]
        )
    )
    curved_action = f.section_completion(curved_hodge, differential)
    curved_inter = tuple(
        (row, column)
        for row in range(f.COVER_SIZE)
        for column in range(f.COVER_SIZE)
        if not intra_cell(row, column) and curved_action[row, column] != 0
    )
    hodge_inter = tuple(
        (row, column)
        for row in range(f.COVER_SIZE)
        for column in range(f.COVER_SIZE)
        if not intra_cell(row, column) and curved_hodge[row, column] != 0
    )
    checks.add(
        "B-cell-locality-and-support",
        len(cells) == 8
        and len(differential_positions) == 32
        and all(intra_cell(*position) for position in differential_positions)
        and len(curved_inter) == 144
        and len({frozenset(position) for position in curved_inter}) == 72
        and len(hodge_inter) == 48
        and len({frozenset(position) for position in hodge_inter}) == 24
        and sum(curved_hodge[position] == 0 for position in curved_inter) == 96,
        "the cover has eight disjoint 2x2 cells; the curved completion has 144 ordered inter-cell entries, 48 already in H and 96 transport-created",
    )

    flat_seam_hodge = f.section_glued_hodge(sp.eye(4), field, spatial_shift)
    restricted = f.section_restricted_differential(differential)
    glue = sp.expand(restricted - reflection * restricted * reflection)
    flat_action = f.section_completion(flat_seam_hodge, glue)
    flat_gram = f.section_dressed_gram(flat_action, reflection)
    dressing = sp.expand(f.OFFSET_PERMUTATION * f.SECTION_XI)
    dimension = f.section_self_dual_dimension(dressing)
    shear, volume = sp.symbols("q v", real=True)
    residual = sp.simplify(
        f.shear_block(shear, volume)
        - f.OFFSET_PERMUTATION
        * f.shear_block(shear, volume)
        * f.OFFSET_PERMUTATION.T
    )
    numerators = [
        sp.numer(sp.together(value))
        for value in residual
        if sp.simplify(value) != 0
    ]
    solutions = sp.solve(numerators, (shear, volume), dict=True)
    nonzero_volume_solutions = tuple(
        sorted(
            (
                (solution.get(shear), solution.get(volume))
                for solution in solutions
                if solution.get(volume, 0) != 0
                and sp.simplify(solution.get(shear, 0) ** 2 - 1) != 0
            ),
            key=str,
        )
    )
    checks.add(
        "C-flat-seam-and-modulus",
        f.support_components(flat_action) == (16, 16)
        and f.cross_half_entries(flat_action) == 0
        and f.nonzero_entries(flat_gram) == 0
        and f.inertia(flat_gram) == (0, 0, 16)
        and dimension == (6, 4)
        and set(nonzero_volume_solutions) == {(0, 1), (0, -1)},
        "the flat-seam Gram is the zero PSD matrix; the six-dimensional self-dual modulus meets the shear family at (q,v)=(0,±1), uniquely flat only after v>0 is imposed",
    )

    seams = f.section_seam_family(SEAM_PARAMETER)
    reference_hodge = f.section_glued_hodge(seams[0][1], field, spatial_shift)
    reference_action = f.section_completion(reference_hodge, glue)
    reference_gram = f.section_dressed_gram(reference_action, reflection)
    undressed = f.section_undressed_gram(reference_action)
    checks.add(
        "D-reference-construction",
        f.nonzero_entries(restricted) == 16
        and f.nonzero_entries(glue) == 32
        and f.residual_count(reflection * glue * reflection + glue) == 0
        and f.residual_count(reflection * reference_hodge * reflection - reference_hodge) == 0
        and f.residual_count(reflection * reference_action * reflection - reference_action.T) == 0
        and f.cross_half_entries(reference_action) == 48
        and f.support_components(reference_action) == (32,)
        and f.residual_count(reference_gram - reference_gram.H) == 0
        and f.residual_count(undressed - undressed.H) == 80,
        "the displayed E02 section frame is real, reflection-covariant and connected; its dressed Gram is Hermitian while the undressed neighbor is not",
    )

    seam_inertias = []
    seam_ranks = []
    seam_self_dual = []
    for _name, block in seams:
        seam_self_dual.append(f.residual_count(dressing * block * dressing.T - block) == 0)
        action = f.section_completion(
            f.section_glued_hodge(block, field, spatial_shift), glue
        )
        gram = f.section_dressed_gram(action, reflection)
        seam_inertias.append(f.inertia(gram))
        seam_ranks.append(gram.rank())
    expected_inertias = (
        (6, 6, 4),
        (6, 6, 4),
        (3, 3, 10),
        (0, 0, 16),
        (6, 6, 4),
        (6, 6, 4),
    )
    checks.add(
        "E-six-finite-seam-directions",
        tuple(seam_inertias) == expected_inertias
        and tuple(seam_ranks) == (12, 12, 6, 0, 12, 12)
        and all(seam_self_dual),
        f"six explicitly listed directions have inertias {tuple(seam_inertias)}; b8 is zero PSD and the other five are indefinite",
    )

    mass_inertias = []
    mass_traces = []
    for mass in MASS_SWEEP:
        gram = f.section_dressed_gram(
            f.section_completion(reference_hodge, glue, mass), reflection
        )
        mass_inertias.append(f.inertia(gram))
        mass_traces.append(sp.expand(gram.trace()))
    geometry_gram = f.section_pairing_from_resolvent(
        sp.expand(reference_hodge.inv() * reflection)
    )
    checks.add(
        "F-finite-mass-and-geometry-probes",
        tuple(mass_inertias) == ((6, 6, 4),) * 5
        and f.inertia(geometry_gram) == (4, 4, 8)
        and all(trace > 0 for trace in mass_traces),
        "five finite masses and the pure-geometry limit are not positive definite; positive traces exclude exact opposite eigenvalue pairing but do not explain balanced inertia",
    )

    coefficients = charpoly_coefficients(reference_gram)
    kernel_dimension = next(index for index, value in enumerate(coefficients) if value != 0)
    characteristic = sp.Poly(list(reversed(coefficients)), LAMBDA)
    reflected_characteristic = sp.Poly(
        characteristic.as_expr().subs(LAMBDA, -LAMBDA), LAMBDA
    )
    spectral_gcd = sp.Poly(sp.gcd(characteristic, reflected_characteristic), LAMBDA).monic()
    odd_powers = tuple(
        power for power, coefficient in enumerate(coefficients) if power % 2 and coefficient != 0
    )
    checks.add(
        "G-spectral-gcd",
        f.residual_count(reference_gram - reference_gram.T) == 0
        and kernel_dimension == 4
        and odd_powers == (5, 7, 9, 11, 13, 15)
        and sp.expand(spectral_gcd.as_expr() - LAMBDA**4) == 0
        and kernel_dimension**2 == 16,
        "gcd(p(lambda),p(-lambda))=lambda^4 and dim ker=4, so the anti-commutant is the 16-dimensional kernel-to-kernel block and contains no invertible map",
    )
    checks.add(
        "H-bounded-obstruction",
        all(inertia[0] < 16 for inertia in tuple(seam_inertias) + tuple(mass_inertias) + (f.inertia(geometry_gram),))
        and expected_inertias[3] == (0, 0, 16),
        "no tested Gram is positive definite; zero PSD cases are distinguished from indefinite cases, and no all-frame or all-pairing no-go is claimed",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
