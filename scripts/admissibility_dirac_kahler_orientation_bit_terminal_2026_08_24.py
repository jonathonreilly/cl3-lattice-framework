#!/usr/bin/env python3
"""Corrected Block 180 finite orientation-sector certificate."""

from __future__ import annotations

import sys

import sympy as sp

import admissibility_dirac_kahler_released7359_b_fixture_helpers_2026_09_11 as h


AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ORIENTATION_BIT_TERMINAL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    ".claude/science/physics-loops/toe-axiom-closure-block180-orientation-bit-terminal-20260824/NO_GO_LEDGER.md",
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
    'docs/ADMISSIBILITY_DIRAC_KAHLER_ORIENTATION_BIT_TERMINAL_BOUNDED_THEOREM_NOTE_2026-08-24.md': '8e82d52ab09f48e14c158a485c1d11faf5681e4a0639025895224394347ca0d8',
    '.claude/science/physics-loops/toe-axiom-closure-block180-orientation-bit-terminal-20260824/NO_GO_LEDGER.md': '247a9b747de91f0e1d52af758cf21186862899a2f6db1d77b2ba2c62be4bef79',
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


def wigner_controls(action: sp.Matrix, action_minus: sp.Matrix, grading: sp.Matrix, reflection: sp.Matrix):
    dimension = action.rows
    zero = sp.zeros(dimension, dimension)
    doubled = sp.diag(action, action_minus)
    generators = {
        "r": reflection,
        "rX0": sp.expand(reflection * grading),
        "X0r": sp.expand(grading * reflection),
    }
    defects = []
    for placement_kind in ("diag", "swap"):
        for generator in generators.values():
            placement = (
                sp.diag(generator, generator)
                if placement_kind == "diag"
                else sp.Matrix(sp.BlockMatrix([[zero, generator], [generator, zero]]))
            )
            defects.append(h.residual_count(
                placement.T * doubled * placement.conjugate() - doubled.T
            ))
    swap = sp.Matrix(sp.BlockMatrix([[zero, grading], [grading, zero]]))
    return tuple(defects), h.zero(swap.H * doubled * swap - doubled), h.zero(swap.H * swap - sp.eye(2 * dimension))


def main() -> int:
    checks = h.Checks()
    identity_ok, actual = h.verify_hashes(INPUT_SHA256)
    supplier_ok, supplier_actual = h.supplier_certificate()
    checks.add(
        "A-source-input-closure",
        identity_ok and tuple(INPUT_SHA256) == AUDIT_INPUT_PATHS and supplier_ok,
        f"{len(INPUT_SHA256)} literal inputs; actual={actual}; suppliers={supplier_actual}",
    )

    fixtures = {}
    expected_counts = {"12x6": (0, 84, 84, 144), "8x4": (0, 32, 32, 56)}
    expected_traces = {
        "12x6": (h.R(47794293, 896000), h.R(82268811, 1792000)),
        "8x4": (h.R(378637341, 17920000), h.R(335627241, 17920000)),
    }
    frame_ok = True
    channel_ok = True
    for tag, cover_t, space_extent in (("12x6", 12, 6), ("8x4", 8, 4)):
        bench, qpp = h.orientation_action(tag, cover_t, space_extent, h.FRAME_SX, h.FRAME_ST)
        _, qmm = h.orientation_action(tag, cover_t, space_extent, -h.FRAME_SX, -h.FRAME_ST)
        _, qmp = h.orientation_action(tag, cover_t, space_extent, -h.FRAME_SX, h.FRAME_ST)
        _, qpm = h.orientation_action(tag, cover_t, space_extent, h.FRAME_SX, -h.FRAME_ST)
        grading = h.staggered_grading(bench.T, bench.lx)
        conjugated = sp.expand(grading * qpp * grading)
        counts = (
            h.residual_count(conjugated - qmm),
            h.residual_count(conjugated - qmp),
            h.residual_count(conjugated - qpm),
            h.residual_count(conjugated - qpp),
        )
        traces = (
            sp.expand((qpp * qpp).trace()),
            sp.expand((qpm * qpm).trace()),
        )
        frame_ok &= counts == expected_counts[tag]
        channel_ok &= bool(
            h.zero(grading ** 2 - sp.eye(bench.N))
            and h.zero(grading * bench.r - bench.r * grading)
            and qpp.charpoly().all_coeffs() == qmm.charpoly().all_coeffs()
            and sp.expand(qpp.det() - qmm.det()) == 0
            and h.zero(grading * qpp.inv(method="LU") * grading - qmm.inv(method="LU"))
            and traces == expected_traces[tag]
            and traces[0] != traces[1]
        )
        fixtures[tag] = (bench, qpp, qmm, grading)
    checks.add(
        "B-two-fixture-joint-flip",
        frame_ok,
        "joint flip closes on both even fixtures; the two single flips and self-map have the displayed finite defects",
    )
    checks.add(
        "C-specified-conjugate-channels",
        channel_ok,
        "similarity, determinant, characteristic polynomial, inverse covariance, and trace-square controls only",
    )

    bench, action = h.orientation_action("12x6", 12, 6, h.MEASURE_SX, h.MEASURE_ST)
    _, action_minus = h.orientation_action("12x6", 12, 6, -h.MEASURE_SX, h.MEASURE_ST)
    grading = h.staggered_grading(bench.T, bench.lx)
    sector = h.orientation_sector(bench, action)
    lines = sector["lines"]
    lam_plus, lam_minus = sector["lambdas"]
    sector_ok = bool(
        h.zero(sector["B1"].H * sector["B1"] - sp.eye(2))
        and h.zero(sector["B2"].H * sector["B2"] - sp.eye(2))
        and h.zero(sector["B1"].H * action * sector["B1"] - (h.SECTOR_A * sp.eye(2) + h.SECTOR_D * h.J2))
        and h.zero(sector["B2"].H * action * sector["B2"] - (h.SECTOR_A * sp.eye(2) + h.SECTOR_D * h.J2))
        and all(h.zero(action * lines[name] - eigenvalue * lines[name]) for name, eigenvalue in (
            ("g+", lam_plus), ("g-", lam_minus), ("h+", lam_plus), ("h-", lam_minus)
        ))
        and h.zero(sector["theta"](lines["g+"]) - lines["h-"])
        and h.zero(sector["theta"](lines["g-"]) - lines["h+"])
        and sector["disconnected"]
        and h.zero(action * sector["covariance"] - sp.eye(action.rows))
    )
    plain, reflected = h.witt_forms(sector)
    reflected_target = h.WITT_ENTRY * sp.Matrix([
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0],
    ])
    cells_ok = bool(
        plain == h.WITT_ENTRY * sp.eye(4)
        and reflected == reflected_target
        and reflected.extract((0, 3), (0, 3)).det() == -h.WITT_ENTRY ** 2
        and sp.simplify((lines["g+"] + lines["h-"]).H * sector["weight"] * (lines["g+"] + lines["h-"]))[0] == 2 * h.WITT_ENTRY
    )
    checks.add(
        "D-complex-bilinear-witt-cells",
        sector_ok and cells_ok,
        "four exact eigenlines; reflected anti-diagonal entry 875/1462, isotropic lines, and cell determinant -(875/1462)^2",
    )

    defects, unitary_control, unitary = wigner_controls(action, action_minus, grading, bench.r)
    checks.add(
        "E-six-antiunitary-candidates",
        defects == (360, 336, 336, 336, 360, 360) and unitary_control and unitary,
        f"six named placement defects={defects}; the displayed unitary class-swap control closes",
    )

    basis = sp.Matrix.hstack(lines["g+"], lines["g-"], lines["h+"], lines["h-"])
    sector_block = sp.expand(basis.H * action * basis)
    unit = sp.expand(h.SECTOR_A ** 2 + h.SECTOR_D ** 2)
    slots = sp.Integer(2)
    supplied_r = slots / 2
    supplied_q = (1 + 2 * supplied_r) / 3
    checks.add(
        "F-determinant-and-conditional-slot-arithmetic",
        h.zero(sector_block - sp.diag(lam_plus, lam_minus, lam_plus, lam_minus))
        and unit == h.R(62866, 30625)
        and sp.expand(sector_block.det()) == unit ** 2
        and (supplied_r, supplied_q) == (1, 1),
        "multiplicity-two determinant factor plus the separately supplied r=n/2, Q=(1+2r)/3 arithmetic; no slot or physical interpretation",
    )

    def sigma(vector: sp.MatrixBase) -> sp.Matrix:
        return sp.expand(-bench.r * grading * sp.Matrix(vector).conjugate())

    fixed_x = sp.expand(lines["g+"] + lines["h+"])
    fixed_y = sp.expand(h.I * (lines["g+"] - lines["h+"]))
    restricted = sp.expand(sp.Matrix.hstack(fixed_x, fixed_y).H * action * sp.Matrix.hstack(fixed_x, fixed_y))
    checks.add(
        "G-sigma-fixed-slice-and-complex-gaussian",
        h.zero(sigma(fixed_x) - fixed_x)
        and h.zero(sigma(fixed_y) - fixed_y)
        and sp.Matrix.hstack(fixed_x, fixed_y).rank() == 2
        and restricted == 2 * lam_plus * sp.eye(2)
        and sp.im(lam_plus) != 0
        and not h.zero(sigma(action * fixed_x) - action * fixed_x)
        and sp.simplify(sp.pi / (2 * lam_plus) * 2 - sp.pi / lam_plus) == 0,
        "Fix(sigma) is real two-dimensional; Q restricts to 2(a+id)I, giving coordinate pi/[2(a+id)] and induced-area pi/(a+id), while the slice is not Q-invariant",
    )

    checks.add(
        "H-exact-bounded-scope",
        h.no_float((fixtures, action, action_minus, sector_block, plain, reflected, restricted)),
        "supplied finite matrices and named controls only; no observable-algebra, corepresentation, physical-slot, or reality classification",
    )
    return checks.emit()


if __name__ == "__main__":
    sys.exit(main())
