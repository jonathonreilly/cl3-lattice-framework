#!/usr/bin/env python3
"""Corrected Block 162 finite mass-survival and stratum certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10 as b


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    ".claude/science/physics-loops/toe-axiom-closure-block162-mass-survival-stratum-20260820/NO_GO_LEDGER.md",
    "scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_validation_battery_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_MASS_SURVIVAL_STRATUM_BOUNDED_THEOREM_NOTE_2026-08-20.md': '4b07b9409731e1b1263ec722f294847c7ac264573176f716e389c3aedaa6882b',
    '.claude/science/physics-loops/toe-axiom-closure-block162-mass-survival-stratum-20260820/NO_GO_LEDGER.md': 'b0fceb7cd01cdd81f99de49a78d95e6ab5371f320d7958836ec9dc27501440f2',
    'scripts/admissibility_dirac_kahler_released7315_b_fixture_helpers_2026_09_10.py': '97846307bffff108c98466329c65a051e8d896ccb9231fd23d9e0ddec962c2c9',
    'scripts/admissibility_dirac_kahler_validation_battery_2026_08_20.py': '1fa7366927e9b04094232033720478e815bcf87252f429a3df2f40a8b28dd10e',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_VALIDATION_BATTERY_BOUNDED_THEOREM_NOTE_2026-08-20.md': 'd3efa6d5231babb9b3da9146285a6563004865775e71ae9a20a79c3d0167262a',
    'scripts/admissibility_dirac_kahler_link_curvature_scout_2026_08_20.py': '2ea65a2613d2822427bfb2a0e3ac4f4ea57a18c732c27f7312bbca585f61776f',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md': '2601b9fc27fc78df48d22ade9104251fd1da85f174f6c7126cad9e6319ff8068',
    'scripts/admissibility_dirac_kahler_released7315_a_fixture_helpers_2026_09_10.py': '37e2520596484df264bc169a6c7ced21575c2e7784bc78d668338ec30dcc4383',
    'scripts/admissibility_dirac_kahler_reflection_fixture_helpers_2026_09_10.py': '0974a71bab3c753e66692740e303ea8062bfa7b6bd88fdc4a2c665d61ac95f87',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}


def form_for(edge: sp.MatrixBase) -> sp.Matrix:
    return b.dense_pairing(
        b.THETA,
        b.h.quotient_action(edge, b.h.COVER_FREE, b.MASS),
    )


def main() -> int:
    checks = b.Checks()
    identity_ok, actual = b.verify_input_hashes(INPUT_SHA256)
    identity_ok = identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS
    checks.add("A-source-input-closure", identity_ok, f"{len(INPUT_SHA256)} literal inputs; actual={actual}")

    symbolic_edges = b.dense_edges()
    edge = b.restrict_dense(
        sp.expand(symbolic_edges[(2, 2)].xreplace(b.ATLAS)), b.EVEN_SUPPORT
    )
    form = form_for(edge)
    bmod = b.h.B_MODULUS
    expected_massless = {
        (0, 7): bmod[(2, 0)] / 10,
        (1, 4): bmod[(0, 0)] / 10,
        (2, 5): bmod[(2, 2)] / 10,
        (3, 6): bmod[(0, 2)] / 10,
    }
    expected_mass = {
        (0, 3): (bmod[(3, 0)] + bmod[(3, 3)]) / 8,
        (1, 2): (bmod[(3, 1)] + bmod[(3, 2)]) / 8,
        (4, 5): -(bmod[(1, 0)] + bmod[(1, 3)]) / 8,
        (6, 7): -(bmod[(1, 1)] + bmod[(1, 2)]) / 8,
    }
    actual_massless = {
        key: sp.expand(form[key].xreplace({b.MASS: 0}))
        for key in expected_massless
    }
    actual_mass = {key: sp.expand(sp.diff(form[key], b.MASS)) for key in expected_mass}
    checks.add(
        "B-eight-cross-parity-coefficients",
        actual_massless == expected_massless
        and actual_mass == expected_mass
        and all(sp.expand(form[j, j]) == 0 for j in b.ODD_SLOTS),
        "four even-shear massless coefficients and four odd-row-sum mass coefficients; odd-slot diagonal zero",
    )

    cells = b.CELLS
    rows = []
    for cell in b.EVEN_CELLS:
        rows.append([sp.Integer(other == cell) for other in cells])
    l147_pairs = (
        ((1, 0), (1, 3)), ((1, 1), (1, 2)),
        ((3, 0), (3, 3)), ((3, 1), (3, 2)),
    )
    for left, right in l147_pairs:
        rows.append([
            sp.Integer(other == left) + sp.Integer(other == right)
            for other in cells
        ])
    l154_pairs = (((1, 1), (1, 3)), ((3, 1), (3, 3)))
    l154_rows = [
        [sp.Integer(other == left) + sp.Integer(other == right) for other in cells]
        for left, right in l154_pairs
    ]
    survival_rank = sp.Matrix(rows).rank()
    stratum_rank = sp.Matrix(rows + l154_rows).rank()
    checks.add(
        "C-layered-linear-loci",
        (survival_rank, stratum_rank, 32 - survival_rank, 32 - stratum_rank)
        == (8, 10, 24, 22),
        "the displayed independent equations give a 24-coordinate survival locus and a 22-coordinate L154 slice",
    )

    p1, q1, p3, q3 = sp.symbols("p1 q1 p3 q3", real=True)
    survival_b = {
        (0, 0): 0, (0, 2): 0, (2, 0): 0, (2, 2): 0,
        (1, 0): p1, (1, 1): q1, (1, 2): -q1, (1, 3): -p1,
        (3, 0): p3, (3, 1): q3, (3, 2): -q3, (3, 3): -p3,
    }
    survival = {bmod[cell]: value for cell, value in survival_b.items()}
    survival_form = sp.expand(form.xreplace(survival))
    checks.add(
        "D-disjoint-coordinate-survival",
        survival_form.is_diagonal()
        and not (survival_form.free_symbols & {p1, q1, p3, q3, b.MASS})
        and all(sp.expand(survival_form[j, j]) == 0 for j in b.ODD_SLOTS),
        "on the displayed symbolic cone form, the eight equations remove every cross term at every mass",
    )

    u, v = sp.symbols("u v", real=True)
    stratum_b = dict(survival_b)
    stratum_b.update({
        (1, 0): u, (1, 1): u, (1, 2): -u, (1, 3): -u,
        (3, 0): v, (3, 1): v, (3, 2): -v, (3, 3): -v,
    })
    stratum = {bmod[cell]: value for cell, value in stratum_b.items()}
    reference_form = sp.expand(form.xreplace(stratum))
    projection = sp.zeros(4, b.HALF)
    for row, slot in enumerate(b.EVEN_SLOTS):
        projection[row, slot] = 1
    common = sp.diag(*[reference_form[slot, slot] for slot in b.EVEN_SLOTS])
    pullback = projection.T * common * projection

    weights = sp.symbols("lambda0:4", real=True)
    weight_edges = b.dense_edges(weights=weights)
    base = (0, 0, b.ST, -b.ST)
    reference = (
        b.h.A_MODULUS[(2, 0)] + b.h.A_MODULUS[(3, 3)]
        + b.h.INV_MODULUS[(2, 3)] + b.h.NU_MODULUS[(3, 0)]
    )
    factorization = []
    coefficient_law = []
    for i, j in b.EDGE_KEYS:
        candidate = form_for(b.restrict_dense(weight_edges[(i, j)], b.EVEN_SUPPORT))
        candidate = sp.expand(candidate.xreplace(stratum))
        coefficient = sp.cancel(candidate[0, 0] * 5 / reference)
        predicted = sp.Rational(5, 4) * (base[i] - b.ST * (weights[j] - weights[i]))
        coefficient_law.append(sp.simplify(coefficient - predicted) == 0)
        scalar = sp.cancel(candidate[0, 0] / reference_form[0, 0])
        factorization.append(sp.expand(candidate - scalar * pullback) == sp.zeros(b.HALF))
    checks.add(
        "E-shared-pullback-and-corrected-law",
        reference_form == pullback
        and all(factorization)
        and all(coefficient_law),
        "all 16 displayed edge forms share the pullback; 4c = 5(base - s_t Delta-lambda)",
    )

    rperm = sp.Matrix(4, 4, lambda i, j: sp.Integer(j == (3 - i) % 4))
    sperm = sp.Matrix(4, 4, lambda i, j: sp.Integer(j == (i + 2) % 4))
    joint = sp.Matrix.vstack(rperm + sp.eye(4), sperm + sp.eye(4))
    checks.add(
        "F-finite-Klein-character",
        rperm ** 2 == sp.eye(4)
        and sperm ** 2 == sp.eye(4)
        and rperm * sperm == sperm * rperm
        and 4 - joint.rank() == 1,
        "the displayed involutions generate a regular Klein action with one joint (-1,-1) character",
    )

    checks.add(
        "G-exact-bounded-scope",
        b.no_float((form, survival_form, reference_form, pullback, rows, l154_rows)),
        "supplied finite symbolic matrices and specified loci only; no global physical-sector or off-locus classification",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
