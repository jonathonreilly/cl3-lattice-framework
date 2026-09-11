#!/usr/bin/env python3
"""Corrected Block 187 finite positivity-chart and Delta_8 certificate."""

from __future__ import annotations

import sys
from dataclasses import dataclass

import sympy as sp

import admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11 as f


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block187-positivity-window-characterization-20260824/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-24.md': '1376e61157e96d3d2aeecde42d4244f36a73655dba560dce1eb27af0cef3e38a',
    '.claude/science/physics-loops/toe-axiom-closure-block187-positivity-window-characterization-20260824/NO_GO_LEDGER.md': '2cee9a946362159c299ada77c47838a263ba12bae2351ff0c2b9036787a3225d',
    'scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py': '98531485267696a626892d55abf52938c49d2a6f9c870175362d01ddd287aa20',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md': 'f2ea677ea996a69b018d1f910e962669fd4938968e67bd03b1854826b4fb5a36',
    'scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py': '4299d645f687bec12d945598cca1df5c13a73c871a9e6ad1459e7e6b17c5bab5',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md': 'b3e42b85ff4bd29edd2d3c65bb1685503560af6b512013e062a93601c8661990',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

MASS = sp.Symbol("m")
SHEAR = sp.Symbol("c")
FIXTURE_MASS = sp.Rational(9, 20)
FIXTURE_SHEAR = sp.Rational(5, 13)
POSITIVE = (1,) * 8
MASS_BRACKET = (sp.Rational(2911, 2048), sp.Rational(91, 64))
SHEAR_BRACKET = (sp.Rational(1713, 2560), sp.Rational(857, 1280))

JACOBI_A = (
    2338702173616900 * MASS**4
    + 5559167172136500 * MASS**2
    - 34342504390877071
)
JACOBI_B_MINUS = (
    584675543404225 * MASS**4
    - 119232179199250 * MASS**3
    - 808327810625400 * MASS**2
    - 7890304777814160 * MASS
    - 12314765055708144
)
JACOBI_B_PLUS = (
    584675543404225 * MASS**4
    + 119232179199250 * MASS**3
    - 808327810625400 * MASS**2
    + 7890304777814160 * MASS
    - 12314765055708144
)
JACOBI_QUOTIENT = sp.Rational(
    1, 7286174197556964924654123391513289072415645283434426863405063938768896
)
DET_F = (
    299684727885699454242816 * MASS**8
    + 1057546650417160380713856 * MASS**6
    + 1122356975550987673041509 * MASS**4
    + 334202761189083845162330 * MASS**2
    + 29915998462435025408400
)
DET_G = (
    1198738911542797816971264 * MASS**8
    + 8357584267546985416158720 * MASS**6
    + 20746825460109491061517732 * MASS**4
    + 21542427261169485079330180 * MASS**2
    + 7964480716014734889397129
)
DET_CONST = sp.Integer(
    22600569498765673425646382617815399421526202244979382923541986986760398250842873973826153086976
)


@dataclass(frozen=True)
class Sample:
    determinant: sp.Expr
    minors: tuple[sp.Expr, ...]
    signs: tuple[int, ...]
    first_failure: int
    hermitian: bool

    @property
    def positive(self) -> bool:
        return self.signs == POSITIVE


def build_sample(mass: object, shear: object, glue: sp.Matrix, volume: object = sp.Integer(1)) -> Sample:
    hodge = f.link_image_hodge(shear, volume)
    action = f.completion(hodge, glue, mass)
    determinant = sp.expand(action.det(method="berkowitz"))
    gram = f.link_gram(action)
    minors = f.leading_minors(gram)
    signs = f.minor_signs(minors)
    return Sample(
        determinant,
        minors,
        signs,
        f.first_failing_minor(signs),
        f.residual_count(gram - gram.H) == 0,
    )


def bisect(low: object, high: object, steps: int, predicate) -> tuple:
    path = []
    brackets = []
    for _ in range(steps):
        midpoint = (low + high) / 2
        verdict = bool(predicate(midpoint))
        path.append((midpoint, verdict))
        if verdict:
            low = midpoint
        else:
            high = midpoint
        brackets.append((low, high))
    return tuple(path), tuple(brackets)


def interpolate(nodes: tuple, values: tuple) -> sp.Poly:
    return sp.Poly(sp.interpolate(tuple(zip(nodes, values)), MASS), MASS)


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
    reflection = f.reflection_permutation(f.link_theta)
    glue = f.link_glue(raising)
    cache: dict[tuple[object, object, object], Sample] = {}

    def sample(mass: object, shear: object, volume: object = sp.Integer(1)) -> Sample:
        key = (mass, shear, volume)
        if key not in cache:
            cache[key] = build_sample(mass, shear, glue, volume)
        return cache[key]

    fixture = sample(FIXTURE_MASS, FIXTURE_SHEAR)
    checks.add(
        "B-fixture-control",
        f.nonzero_entries(glue) == 72
        and f.residual_count(reflection * glue * reflection + glue) == 0
        and fixture.positive
        and fixture.hermitian,
        "the parameter chart rebuilds the corrected Block 185 finite fixture",
    )

    gated_masses = (
        sp.Rational(1, 10),
        sp.Rational(3, 4),
        sp.Rational(5, 4),
        sp.Rational(3, 2),
        sp.Integer(2),
    )
    mass_samples = tuple(sample(value, FIXTURE_SHEAR) for value in gated_masses)
    expected_mass_signs = (
        POSITIVE,
        POSITIVE,
        POSITIVE,
        (1, 1, 1, 1, 1, 1, -1, -1),
        (1, 1, 1, 1, 1, -1, 1, -1),
    )
    checks.add(
        "C-fresh-mass-samples",
        tuple(item.signs for item in mass_samples) == expected_mass_signs
        and all(item.hermitian for item in mass_samples),
        "five primary-reproduced mass points retain their exact sign vectors; four other old checker-cited masses remain historical",
    )

    mass_path_expected = (
        (sp.Rational(11, 8), True),
        (sp.Rational(23, 16), False),
        (sp.Rational(45, 32), True),
        (sp.Rational(91, 64), False),
        (sp.Rational(181, 128), True),
        (sp.Rational(363, 256), True),
        (sp.Rational(727, 512), True),
        (sp.Rational(1455, 1024), True),
        (sp.Rational(2911, 2048), True),
        (sp.Rational(5823, 4096), True),
    )
    mass_path, mass_brackets = bisect(
        sp.Rational(5, 4),
        sp.Rational(3, 2),
        len(mass_path_expected),
        lambda value: sample(value, FIXTURE_SHEAR).positive,
    )
    low_sample = sample(MASS_BRACKET[0], FIXTURE_SHEAR)
    high_sample = sample(MASS_BRACKET[1], FIXTURE_SHEAR)
    checks.add(
        "D-delta8-bracket",
        mass_path == mass_path_expected
        and mass_brackets[8] == MASS_BRACKET
        and low_sample.positive
        and high_sample.signs == (1, 1, 1, 1, 1, 1, 1, -1)
        and low_sample.minors[7] > 0
        and high_sample.minors[7] < 0,
        "exact bisection brackets a Delta_8 sign change; this is not asserted to be the full positive-definite boundary",
    )

    ray_hodge = f.link_image_hodge(FIXTURE_SHEAR)
    span = f.slice_indices((0, 1))
    reflected = f.reflected_indices((0, 1), f.link_theta)
    complement_rows = tuple(index for index in range(f.COVER_SIZE) if index not in reflected)
    complement_columns = tuple(index for index in range(f.COVER_SIZE) if index not in span)
    jacobi_nodes = tuple(sp.Integer(value) for value in range(-12, 13))
    jacobi_values = tuple(
        f.completion(ray_hodge, glue, value)[list(complement_rows), list(complement_columns)].det(method="berkowitz")
        for value in jacobi_nodes
    )
    jacobi_numerator = interpolate(jacobi_nodes, jacobi_values)
    jacobi_target = sp.Poly(
        sp.expand(JACOBI_QUOTIENT * JACOBI_A**2 * JACOBI_B_MINUS * JACOBI_B_PLUS),
        MASS,
    )
    extra_nodes = (sp.Rational(7, 3), sp.Rational(-11, 5), sp.Integer(101), sp.Rational(-3, 7))
    extra_agree = all(
        jacobi_numerator.eval(value)
        == f.completion(ray_hodge, glue, value)[list(complement_rows), list(complement_columns)].det(method="berkowitz")
        for value in extra_nodes
    )
    identity_masses = gated_masses + MASS_BRACKET
    jacobi_identity_points = tuple(
        sample(value, FIXTURE_SHEAR).minors[-1]
        * sample(value, FIXTURE_SHEAR).determinant
        == jacobi_numerator.eval(value)
        for value in identity_masses
    )
    sturm_counts = tuple(
        sp.count_roots(poly, MASS_BRACKET[0], MASS_BRACKET[1])
        for poly in (JACOBI_A, JACOBI_B_MINUS, JACOBI_B_PLUS)
    )
    derivative = sp.diff(JACOBI_B_PLUS, MASS)
    checks.add(
        "E-jacobi-and-simple-root",
        jacobi_numerator == jacobi_target
        and extra_agree
        and all(jacobi_identity_points)
        and sp.gcd(JACOBI_A**2 * JACOBI_B_MINUS * JACOBI_B_PLUS, DET_F**2 * DET_G**2) == 1
        and sturm_counts == (0, 0, 1)
        and sp.gcd(JACOBI_B_PLUS, derivative) == 1
        and sp.count_roots(derivative, MASS_BRACKET[0], MASS_BRACKET[1]) == 0,
        "the complementary 24x24 interpolation and seven direct Jacobi checks give the reduced Delta_8 factorization and one simple B_+ root in the stated bracket",
    )

    shear_path_expected = (
        (sp.Rational(7, 10), False),
        (sp.Rational(13, 20), True),
        (sp.Rational(27, 40), False),
        (sp.Rational(53, 80), True),
        (sp.Rational(107, 160), True),
        (sp.Rational(43, 64), False),
        (sp.Rational(429, 640), False),
        (sp.Rational(857, 1280), False),
        (sp.Rational(1713, 2560), True),
    )
    shear_path, shear_brackets = bisect(
        sp.Rational(3, 5),
        sp.Rational(4, 5),
        len(shear_path_expected),
        lambda value: sample(FIXTURE_MASS, value).positive,
    )
    shear_low = sample(FIXTURE_MASS, SHEAR_BRACKET[0])
    shear_high = sample(FIXTURE_MASS, SHEAR_BRACKET[1])
    first_corner = sample(sp.Integer(1), sp.Rational(3, 5))
    second_corner = sample(sp.Rational(1, 10), sp.Rational(4, 5))
    mass_leg = sample(sp.Integer(1), FIXTURE_SHEAR)
    shear_leg = sample(FIXTURE_MASS, sp.Rational(3, 5))
    checks.add(
        "F-shear-and-nonproduct-samples",
        shear_path == shear_path_expected
        and shear_brackets[-1] == SHEAR_BRACKET
        and shear_low.positive
        and shear_high.first_failure == 7
        and first_corner.first_failure == 6
        and second_corner.first_failure == 7
        and mass_leg.positive
        and shear_leg.positive
        and not first_corner.positive,
        "sampled first-failing indices are 8, 7 and 6 at selected points; they are diagnostics, while the positive legs and failing crosspoint prove only non-product structure",
    )

    det_nodes = tuple(sp.Integer(value) for value in range(-16, 17))
    det_values = tuple(
        f.completion(ray_hodge, glue, value).det(method="berkowitz")
        for value in det_nodes
    )
    det_interpolation = interpolate(det_nodes, det_values)
    det_target = sp.Poly(sp.expand(DET_F**2 * DET_G**2 / DET_CONST), MASS)
    positive_polynomials = all(
        coefficient > 0
        for polynomial in (sp.Poly(DET_F, MASS), sp.Poly(DET_G, MASS))
        for coefficient in polynomial.all_coeffs()
        if coefficient != 0
    )
    checks.add(
        "G-nonsingular-chart-and-local-openness",
        det_interpolation == det_target
        and positive_polynomials
        and sp.count_roots(DET_F) == 0
        and sp.count_roots(DET_G) == 0
        and all(item.determinant != 0 for item in cache.values()),
        "33 exact determinant samples establish the degree-32 identity; strict finite Gram inequalities therefore give local open neighborhoods at each positive sample",
    )
    volume_samples = (
        sample(FIXTURE_MASS, FIXTURE_SHEAR, sp.Rational(4, 5)),
        sample(FIXTURE_MASS, FIXTURE_SHEAR, sp.Rational(5, 4)),
    )
    checks.add(
        "H-bounded-scope-and-volume-controls",
        high_sample.first_failure == 8
        and shear_high.first_failure == 7
        and first_corner.first_failure == 6
        and all(item.positive and item.hermitian and item.determinant != 0 for item in volume_samples),
        "two exact nonzero-volume controls are positive; they do not give a volume interval, lower-minor interval certificate, global boundary curve, connectivity, curvature, or monotone mass/shear theorem",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
