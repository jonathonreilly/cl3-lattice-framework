#!/usr/bin/env python3
"""Corrected Block 185 five-point seam-glued Gram certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11 as f


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block185-curved-os-seam-glued-gram-20260824/NO_GO_LEDGER.md",
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
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md': 'f2ea677ea996a69b018d1f910e962669fd4938968e67bd03b1854826b4fb5a36',
    '.claude/science/physics-loops/toe-axiom-closure-block185-curved-os-seam-glued-gram-20260824/NO_GO_LEDGER.md': 'eb3acc2666213a58dfc6088f7a7eb6159cf7dd953a85da57e371a2b30450fea7',
    'scripts/admissibility_dirac_kahler_released7359_c_fixtures_2026_09_11.py': '98531485267696a626892d55abf52938c49d2a6f9c870175362d01ddd287aa20',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md': '660ae4597d0f7eb0ea24347bc189020f772c330afa4fb11fcc921e1b6ea62776',
    'scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py': '4299d645f687bec12d945598cca1df5c13a73c871a9e6ad1459e7e6b17c5bab5',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md': 'b3e42b85ff4bd29edd2d3c65bb1685503560af6b512013e062a93601c8661990',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}

BASE_MASS = sp.Rational(9, 20)
BASE_SHEAR = sp.Rational(5, 13)
POSITIVE = (1,) * 8


def variant(
    mass: object,
    hodge: sp.Matrix,
    glue: sp.Matrix,
    reflection: sp.Matrix,
) -> dict[str, object]:
    action = f.completion(hodge, glue, mass)
    covariance = f.residual_count(reflection * action * reflection - action.T)
    invertible = action.det(method="berkowitz") != 0
    if not invertible:
        return {"covariance": covariance, "invertible": False, "delta": None, "signs": ()}
    gram = f.link_gram(action)
    minors = f.leading_minors(gram)
    return {
        "covariance": covariance,
        "invertible": True,
        "delta": f.max_norm(gram - gram.H),
        "signs": f.minor_signs(minors),
        "first_minor": minors[0],
    }


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
    checks.add(
        "B-finite-carrier",
        f.residual_count(kernel - (raising - raising.T)) == 0
        and f.residual_count(raising * raising) == 0
        and f.residual_count(reflection * reflection - sp.eye(f.COVER_SIZE)) == 0
        and f.nonzero_entries(glue) == 72
        and f.residual_count(reflection * glue * reflection + glue) == 0,
        "the 32-dimensional supplied carrier has the exact grading split and a 72-entry reflection-odd glue",
    )

    flat_action = BASE_MASS * sp.eye(f.COVER_SIZE) + kernel
    flat_gram = f.link_gram(flat_action)
    flat_signs = f.minor_signs(f.leading_minors(flat_gram))
    checks.add(
        "C-flat-calibration",
        f.residual_count(reflection * flat_action * reflection - flat_action.T) == 0
        and f.residual_count(flat_gram - flat_gram.H) == 0
        and flat_signs == POSITIVE,
        f"the flat finite calibration is Hermitian and has signs {flat_signs}",
    )

    base_hodge = f.link_image_hodge(BASE_SHEAR)
    base = variant(BASE_MASS, base_hodge, glue, reflection)
    action = f.completion(base_hodge, glue, BASE_MASS)
    inverse = action.inv()
    checks.add(
        "D-covariance-and-reality",
        f.residual_count(reflection * base_hodge * reflection - base_hodge) == 0
        and base["covariance"] == 0
        and f.residual_count(reflection * inverse * reflection - inverse.T) == 0
        and all(sp.im(value) == 0 for value in action)
        and base["delta"] == 0,
        "real transpose covariance implies Hermiticity for this invertible supplied action",
    )
    tiny_action = sp.Matrix(((sp.I,),))
    tiny_gram = sp.Matrix(((sp.conjugate(tiny_action.inv()[0, 0]),),))
    checks.add(
        "E-reality-is-load-bearing",
        tiny_action == tiny_action.T and f.residual_count(tiny_gram - tiny_gram.H) == 1,
        "the one-dimensional complex control satisfies transpose covariance but has a non-Hermitian paired inverse",
    )

    seam_results = []
    for seams in ((), (f.NEAR_SEAM,), (f.FAR_SEAM,), f.BOTH_SEAMS):
        seam_glue = f.link_glue(raising, seams)
        seam_results.append(variant(BASE_MASS, base_hodge, seam_glue, reflection))
    seam_signs = tuple(result["signs"] for result in seam_results)
    checks.add(
        "F-enumerated-seam-controls",
        seam_signs
        == (
            (0,) * 8,
            (1, 1, 1, 1, -1, 1, -1, 1),
            (1, 1, 1, 1, 0, 0, 0, 0),
            POSITIVE,
        )
        and all(result["delta"] == 0 for result in seam_results),
        f"zero, near, far, and both-seam sign vectors are {seam_signs}",
    )

    points = (
        ("base", BASE_MASS, BASE_SHEAR, f.link_image_hodge(BASE_SHEAR)),
        ("mass_1_3", sp.Rational(1, 3), BASE_SHEAR, f.link_image_hodge(BASE_SHEAR)),
        ("mass_2", sp.Integer(2), BASE_SHEAR, f.link_image_hodge(BASE_SHEAR)),
        ("constant_c_3_5", BASE_MASS, sp.Rational(3, 5), f.link_image_hodge(sp.Rational(3, 5))),
        ("x_alternating_c_3_5", BASE_MASS, sp.Rational(3, 5), f.x_alternating_link_image_hodge(sp.Rational(3, 5))),
    )
    measured = tuple((name, variant(mass, hodge, glue, reflection)) for name, mass, _shear, hodge in points)
    signs = tuple(result["signs"] for _, result in measured)
    checks.add(
        "G-five-point-window",
        signs
        == (
            POSITIVE,
            POSITIVE,
            (1, 1, 1, 1, 1, -1, 1, -1),
            POSITIVE,
            (1, 1, 1, 1, 1, 1, -1, -1),
        )
        and sum(sign == POSITIVE for sign in signs) == 3
        and all(result["covariance"] == 0 and result["delta"] == 0 for _, result in measured),
        f"five explicitly constructed points give three positive Grams; signs={dict(zip((name for name, _ in measured), signs))}",
    )
    checks.add(
        "H-bounded-scope",
        base["signs"] == POSITIVE and all(f.exact_real(value) for value in (BASE_MASS, BASE_SHEAR)),
        "the result concerns only the five listed points and seam variants; the unrun (1/3,3/5) crosspoint remains open",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
