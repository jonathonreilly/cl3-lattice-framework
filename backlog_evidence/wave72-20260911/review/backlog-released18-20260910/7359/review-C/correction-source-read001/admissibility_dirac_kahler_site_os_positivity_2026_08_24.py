#!/usr/bin/env python3
"""Corrected Block 188 finite link-seam and site-reflection certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11 as f


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block188-site-os-positivity-20260824/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md': '22457baf8f6b40a7a93c1b62ecc0a81861264f49d00cf335581785401572c3dd',
    '.claude/science/physics-loops/toe-axiom-closure-block188-site-os-positivity-20260824/NO_GO_LEDGER.md': '9594254818453d592b5c55b7e4cc90b6af95d1bf7f411ce7c340048584fd4a6e',
    'scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py': 'd56cb24eeb93ea34268a4a48e5c5cc9c59958b45a6818c192a927bfb42ebd436',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-24.md': '5ffd8259b0cf7360fbbc578a82e029fec96894f4ff66a43119560df2910c5394',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md': 'b3f3eea77444b03f1a03c07eff1216979866117203cb8c2094a6c215d3f49695',
    'scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py': '4299d645f687bec12d945598cca1df5c13a73c871a9e6ad1459e7e6b17c5bab5',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md': 'b3e42b85ff4bd29edd2d3c65bb1685503560af6b512013e062a93601c8661990',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

MASS = sp.Rational(9, 20)
SHEAR = sp.Rational(5, 13)
DIRECT = sp.Rational(-601, 576)
THICKNESS = sp.Rational(65, 1152)
DISCRIMINANT = sp.sqrt(365426) / 576
REAL_SECTORS = (0, 2)
ALL_SECTORS = (0, 1, 2, 3)
SECTOR_ROWS = (0, 1, 2, 3)
SECTOR_COLUMNS = tuple(f.link_theta(time) for time in range(4))
TRIANGLE_INDICES = ((0, 1), (1, 4), (4, 0))


def sector_map(momentum: int) -> sp.Matrix:
    phase = sp.I**momentum
    embedding = sp.zeros(f.COVER_SIZE, f.TIME_EXTENT)
    for time in range(f.TIME_EXTENT):
        for space in range(f.SPACE_EXTENT):
            embedding[f.site_index(time, space), time] = phase**space / 2
    return embedding


def sector_reflection(theta) -> sp.Matrix:
    matrix = sp.zeros(f.TIME_EXTENT)
    for time in range(f.TIME_EXTENT):
        matrix[theta(time), time] = 1
    return matrix


def sign_operator(seam: sp.Matrix) -> sp.Matrix:
    return f.reduce_matrix((2 * seam - DIRECT * sp.eye(seam.rows)) / DISCRIMINANT)


def triangle_sign(gram: sp.Matrix) -> int:
    product = sp.prod(gram[row, column] for row, column in TRIANGLE_INDICES)
    return int(sp.sign(f.reduce_exact(product)))


def factor_key(polynomial: sp.Expr) -> tuple:
    poly = sp.Poly(polynomial, sp.Symbol("lambda"))
    return (poly.degree(),) + tuple(int(coefficient) for coefficient in poly.all_coeffs())


def main() -> int:
    checks = f.Checks()
    identity_ok, actual = f.verify_input_hashes(INPUT_SHA256)
    checks.add(
        "A-source-input-closure",
        identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS,
        f"{len(INPUT_SHA256)} literal current inputs; actual={actual}",
    )

    kernel = f.staggered_kernel()
    raising = f.raising_part(kernel)
    link_reflection = f.reflection_permutation(f.link_theta)
    link_glue = f.link_glue(raising)
    link_hodge = f.link_image_hodge(SHEAR)
    link_action = f.completion(link_hodge, link_glue, MASS)
    link_inverse = link_action.inv()
    positive = f.slice_indices(f.POSITIVE_TIMES)
    partners = f.reflected_indices(f.POSITIVE_TIMES, f.link_theta)
    seam = sp.expand(link_action[list(positive), list(partners)])
    checks.add(
        "B-link-seam-support",
        f.nonzero_entries(link_glue) == 72
        and f.residual_count(link_reflection * link_glue * link_reflection + link_glue) == 0
        and f.residual_count(link_reflection * link_hodge * link_reflection - link_hodge) == 0
        and f.residual_count(link_reflection * link_action * link_reflection - link_action.T) == 0
        and f.band_census(link_action) == {-2: 24, -1: 56, 0: 96, 1: 56, 2: 24}
        and seam.rank() == 16
        and f.inertia(seam) == (8, 8, 0),
        "the finite link route has a full-rank 16x16 theta-paired seam of inertia (8,8,0) and support through offsets ±2",
    )

    sector_objects: dict[int, tuple[sp.Matrix, sp.Matrix]] = {}
    blocks = []
    for momentum in ALL_SECTORS:
        embedding = sector_map(momentum)
        action = sp.expand(embedding.H * link_action * embedding)
        seam_sector = action[list(SECTOR_ROWS), list(SECTOR_COLUMNS)]
        near = sp.Matrix(((seam_sector[0, 0], seam_sector[0, 1]), (seam_sector[1, 0], seam_sector[1, 1])))
        far = sp.Matrix(((seam_sector[3, 3], seam_sector[3, 2]), (seam_sector[2, 3], seam_sector[2, 2])))
        blocks.append((momentum, near, far))
        sector_objects[momentum] = (action, seam_sector)
    phase_formula = all(
        near
        == sp.Matrix(
            ((DIRECT, THICKNESS * (-sp.I) ** momentum), (THICKNESS * sp.I**momentum, 0))
        )
        and far
        == sp.Matrix(
            ((DIRECT, THICKNESS * sp.I**momentum), (THICKNESS * (-sp.I) ** momentum, 0))
        )
        for momentum, near, far in blocks
    )
    determinants = tuple(
        f.reduce_exact(block.det())
        for _momentum, near, far in blocks
        for block in (near, far)
    )
    checks.add(
        "C-sector-phase-and-determinant",
        phase_formula
        and determinants == (-THICKNESS**2,) * 8
        and tuple(f.inertia(sector_objects[momentum][1]) for momentum in REAL_SECTORS)
        == ((2, 2, 0), (2, 2, 0)),
        "near off-diagonals carry (-i)^p and far off-diagonals carry i^p; every displayed 2x2 determinant is -|65/1152|^2",
    )

    sandwich_inertias = []
    insertion_defects = []
    modulus_inertias = []
    polar_inertias: dict[str, list[tuple[int, int, int]]] = {
        "one_sided": [],
        "symmetric": [],
        "sign_preserving": [],
    }
    sector_p = sector_reflection(f.link_theta)
    for momentum in REAL_SECTORS:
        action, seam_sector = sector_objects[momentum]
        sign = sign_operator(seam_sector)
        raw_gram = f.reduce_matrix(action.inv()[list(SECTOR_ROWS), list(SECTOR_COLUMNS)].T)
        sandwich = f.reduce_matrix(sign * raw_gram * sign.T)
        inserted = f.reduce_matrix(sign * raw_gram)
        modulus = f.reduce_matrix(sign * seam_sector)
        sandwich_inertias.append((f.inertia(raw_gram), f.inertia(sandwich)))
        insertion_defects.append(
            (f.residual_count(inserted - inserted.T), f.reduce_matrix(sign * raw_gram - raw_gram * sign).rank())
        )
        modulus_inertias.append(f.inertia(modulus))
        for name in polar_inertias:
            polar_action = sp.Matrix(action)
            for row, source in enumerate(SECTOR_ROWS):
                for column, target in enumerate(SECTOR_COLUMNS):
                    polar_action[source, target] = modulus[row, column]
                    if name == "symmetric":
                        polar_action[target, source] = modulus[row, column]
                    elif name == "sign_preserving":
                        polar_action[target, source] = -modulus[row, column]
            if f.residual_count(sector_p * polar_action * sector_p - polar_action.T) != 0:
                polar_inertias[name].append((-1, -1, -1))
                continue
            polar_gram = f.reduce_matrix(polar_action.inv()[list(SECTOR_ROWS), list(SECTOR_COLUMNS)].T)
            polar_inertias[name].append(f.inertia(polar_gram))
    checks.add(
        "D-congruence-insertion-and-polar-controls",
        tuple(sandwich_inertias)
        == (((2, 2, 0), (2, 2, 0)), ((2, 2, 0), (2, 2, 0)))
        and tuple(insertion_defects) == ((12, 4), (12, 4))
        and tuple(modulus_inertias) == ((4, 0, 0), (4, 0, 0))
        and tuple(polar_inertias["one_sided"]) == ((2, 2, 0), (2, 2, 0))
        and tuple(polar_inertias["symmetric"]) == ((2, 2, 0), (2, 2, 0))
        and tuple(polar_inertias["sign_preserving"]) == ((0, 4, 0), (0, 4, 0)),
        "invertible congruence preserves inertia; S K fails the Hermitian positive-pairing requirement, and three finite action-side polar writings do not yield PSD Grams",
    )

    site_reflection = f.reflection_permutation(f.site_theta)
    site_hodge = f.site_image_hodge(SHEAR)
    flipped_hodge = f.site_image_hodge(SHEAR, flipped=True)
    site_restricted = f.site_restricted_raising(raising)
    site_glue = f.site_glue(raising)
    site_action = f.completion(site_hodge, site_glue, MASS)
    difference = sp.expand(site_glue - raising)
    difference_cells = tuple(
        sorted(
            {
                (row // f.SPACE_EXTENT, column // f.SPACE_EXTENT)
                for row in range(f.COVER_SIZE)
                for column in range(f.COVER_SIZE)
                if difference[row, column] != 0
            }
        )
    )
    checks.add(
        "E-site-construction",
        f.residual_count(site_reflection * site_hodge * site_reflection - site_hodge) == 0
        and f.residual_count(site_reflection * flipped_hodge * site_reflection - flipped_hodge) == 64
        and f.nonzero_entries(site_restricted) == 28
        and f.nonzero_entries(site_glue) == 56
        and f.residual_count(site_reflection * site_glue * site_reflection + site_glue) == 0
        and f.nonzero_entries(difference) == 24
        and difference_cells == ((0, 0), (4, 4), (5, 4), (5, 5), (6, 6), (7, 7))
        and f.residual_count(site_reflection * site_action * site_reflection - site_action.T) == 0
        and f.residual_count(site_action - site_action.T) == 144
        and f.residual_count(site_reflection * link_action * site_reflection - link_action.T) == 240,
        "the unflipped site image and 56-entry site glue satisfy reflected-transpose covariance; the link action does not become this construction under the site permutation",
    )

    strictly_positive = f.slice_indices((1, 2, 3))
    negative = f.slice_indices((5, 6, 7))
    site_partners = f.reflected_indices((1, 2, 3), f.site_theta)
    pieces = (
        sp.expand(MASS * site_hodge),
        sp.expand(site_hodge * site_glue),
        sp.expand(-site_glue.T * site_hodge),
    )
    site_inverse = site_action.inv()
    spans = ((1, 2), (1, 2, 3), (0, 1, 2, 3))
    grams = tuple(f.paired_gram(site_inverse, span, f.site_theta) for span in spans)
    schur_grams = tuple(
        f.paired_gram(site_inverse, order, f.site_theta)
        for order in ((1, 2, 3), (1, 2, 0, 3))
    )
    checks.add(
        "F-empty-cross-and-schur-PSD",
        f.residual_count(site_action[list(strictly_positive), list(site_partners)]) == 0
        and f.residual_count(site_action[list(strictly_positive), list(negative)]) == 0
        and f.residual_count(site_action[list(negative), list(strictly_positive)]) == 0
        and tuple(f.residual_count(piece[list(strictly_positive), list(negative)]) for piece in pieces) == (0, 0, 0)
        and f.minor_signs(f.leading_minors(grams[0])) == (1,) * 8
        and tuple(f.inertia(gram) for gram in grams) == ((8, 0, 0), (8, 0, 4), (8, 0, 8))
        and tuple(f.residual_count(f.schur_complement(gram, 8)) for gram in schur_grams) == (0, 0),
        "the cross is empty term by term; zero 4x4 and 8x8 Schur complements certify PSD rank eight on the two larger displayed spans",
    )

    core_anchors = f.slice_indices((1, 2))
    core_partners = f.reflected_indices((1, 2), f.site_theta)
    shifted = tuple(f.site_index(time + 1, space) for time in (1, 2) for space in range(f.SPACE_EXTENT))
    core_gram = sp.Matrix(8, 8, lambda row, column: site_inverse[core_anchors[column], core_partners[row]])
    shifted_pairing = sp.Matrix(8, 8, lambda row, column: site_inverse[shifted[column], core_partners[row]])
    transfer = sp.expand(core_gram.inv() * shifted_pairing)
    spectral = sp.Symbol("lambda")
    factors = tuple(
        sorted(
            (
                sp.expand(factor)
                for factor, multiplicity in sp.factor_list(transfer.charpoly(spectral).as_expr())[1]
                for _ in range(multiplicity)
            ),
            key=lambda polynomial: (sp.Poly(polynomial, spectral).degree(), str(polynomial)),
        )
    )
    census = (
        sum(sp.count_roots(sp.Poly(poly, spectral), 0, 1) for poly in factors),
        sum(sp.count_roots(sp.Poly(poly, spectral), -sp.oo, 0) for poly in factors),
        8 - sum(sp.count_roots(sp.Poly(poly, spectral)) for poly in factors),
    )
    checks.add(
        "G-naive-transfer-control",
        f.residual_count(shifted_pairing - shifted_pairing.T) == 48
        and f.residual_count(core_gram * transfer - transfer.T * core_gram) == 48
        and tuple(sp.Poly(poly, spectral).degree() for poly in factors) == (2, 2, 4)
        and census == (2, 2, 4),
        "the finite single-readout candidate T=K_c^-1 L is neither K_c-self-adjoint nor spectrally positive; no reconstruction-transfer theorem follows",
    )

    link_core = f.paired_gram(link_inverse, (0, 1), f.link_theta)
    triangle = (triangle_sign(grams[0]), triangle_sign(link_core))
    robustness = []
    for mass, shear in ((sp.Integer(1), SHEAR), (MASS, sp.Rational(3, 5))):
        hodge = f.site_image_hodge(shear)
        action = f.completion(hodge, site_glue, mass)
        inverse = action.inv()
        robustness.append(tuple(f.inertia(f.paired_gram(inverse, span, f.site_theta)) for span in spans))
    checks.add(
        "H-finite-scope-and-diagonal-congruence",
        tuple(robustness)
        == (((8, 0, 0), (8, 0, 4), (8, 0, 8)),) * 2
        and triangle == (-1, 1),
        "three finite site fixtures have the same displayed PSD inertias; the site and link cores are unequal and not diagonally congruent in this indexing, while general congruence and physical equivalence remain open",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
