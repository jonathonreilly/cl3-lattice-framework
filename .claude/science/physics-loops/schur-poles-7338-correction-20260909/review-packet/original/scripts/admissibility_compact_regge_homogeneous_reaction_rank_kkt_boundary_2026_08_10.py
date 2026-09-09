#!/usr/bin/env python3
"""Check compact Regge reaction ranks and constructive KKT completion.

The paired note studies only the zero-momentum equation of the supplied flat
periodic 15-edge Regge Hessian.  It computes the null-projection rank of the
Block-15/16 positive source families, proves that a pure homothety reaction is
not aligned with those sources, and constructs source-family and full-kernel
KKT reactions without silently projecting the source in the field equation.
"""

from __future__ import annotations

from itertools import product
from math import sqrt
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NETWORK_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_"
    "REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
TWO_STREAM_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
HISTORY_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
SCALE_PATH = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "scripts/admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py",
    "scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10 as helix  # noqa: E402
import admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10 as network  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def exact_metric_map() -> sp.Matrix:
    """Return the exact k=0 line-averaged edge-to-metric map."""
    matrix = sp.zeros(15, 10)
    for row, direction in enumerate(regge.DIRS15):
        length = sp.sqrt(sum(direction))
        for column, (left, right) in enumerate(regge.HCOMPS):
            if left == right:
                matrix[row, column] = sp.Rational(direction[left], 2) / length
            else:
                matrix[row, column] = (
                    sp.Rational(direction[left] * direction[right], 1) / length
                )
    return matrix


def exact_source_rows() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return the per-step bouquet/two-stream row and the two bundle rows."""
    index = {direction: position for position, direction in enumerate(regge.DIRS15)}
    two_stream = sp.zeros(15, 1)
    two_stream[index[(0, 0, 0, 1)]] = 2
    two_stream[index[(1, 0, 0, 1)]] = 2
    bundle_a = sp.zeros(15, 1)
    bundle_b = sp.zeros(15, 1)
    for position, direction in enumerate(regge.DIRS15):
        if direction[3] != 1:
            continue
        spatial_weight = sum(direction[:3])
        if spatial_weight == 1:
            bundle_a[position] = 2 * sp.sqrt(2)
        elif spatial_weight == 0:
            bundle_b[position] = 3
        elif spatial_weight == 2:
            bundle_b[position] = sp.sqrt(3)
    return two_stream, bundle_a, bundle_b


def matrix_float(matrix: sp.Matrix) -> np.ndarray:
    return np.asarray(matrix.evalf(), dtype=float)


def kkt_residuals(
    hessian: np.ndarray, reactions: np.ndarray, sources: np.ndarray
) -> tuple[float, float]:
    """Use source-aligned reaction columns and return equation/constraint errors."""
    pinv = np.linalg.pinv(hessian, rcond=1.0e-10)
    worst_equation = 0.0
    worst_constraint = 0.0
    for column in range(sources.shape[1]):
        multiplier = np.zeros(reactions.shape[1])
        multiplier[column] = -1.0
        reacted_source = sources[:, column] + reactions @ multiplier
        response = -pinv @ reacted_source
        worst_equation = max(
            worst_equation,
            float(
                np.linalg.norm(
                    hessian @ response
                    + sources[:, column]
                    + reactions @ multiplier
                )
            ),
        )
        worst_constraint = max(
            worst_constraint, float(np.linalg.norm(reactions.T @ response))
        )
    return worst_equation, worst_constraint


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    network_note = NETWORK_NOTE_PATH.read_text(encoding="utf-8")
    two_stream_note = TWO_STREAM_NOTE_PATH.read_text(encoding="utf-8")
    history_note = HISTORY_NOTE_PATH.read_text(encoding="utf-8")
    regge_note = REGGE_NOTE_PATH.read_text(encoding="utf-8")
    scale_note = SCALE_PATH.read_text(encoding="utf-8")
    kinetic_note = KINETIC_PATH.read_text(encoding="utf-8")
    realized_note = REALIZED_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print("external_scientific_inputs: none; the reaction-rank lemma is finite-dimensional linear algebra on the supplied actual Regge carrier")
    print("package_local_integrity_reads: current axioms, approved primitives, Blocks 12/15/16, and the actual zero-momentum Hessian are source-bound")
    print("analytic_boundary: ranks and radical identities are exact; KKT residuals use the unprojected actual 15-edge Hessian")
    print("physical_boundary: reaction gradients, targets, source family, action, coupling, nonlinear geometry, and realized history remain unselected")

    checks.check(
        "source-current-axiom-boundary",
        "Admissibility is not a dynamics axiom" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat
        and "update laws" in axiom_flat,
    )
    checks.check(
        "source-approved-primitive-boundary",
        "units conversion" in scale_note
        and "no dimensionless dynamical content" in kinetic_note
        and "pointwise evaluation, not a state-selection rule" in realized_note,
    )
    checks.check(
        "source-prior-compact-boundary",
        "compact scale mechanism" in network_note
        and "fixed-global, open, sign-indefinite combined-geometry" in two_stream_note
        and "globally constrained zero-mode" in history_note,
    )
    checks.check(
        "source-regge-zero-inventory",
        "Constant metric perturbations are exact zero modes at `k=0`" in regge_note
        and "one exactly flat branch" in regge_note,
    )

    q0 = regge.bloch_Q(np.zeros(4)).real
    eigenvalues, eigenvectors = np.linalg.eigh(q0)
    null_basis = eigenvectors[:, np.abs(eigenvalues) < 1.0e-8]
    null_projector = null_basis @ null_basis.T
    exact_m0 = exact_metric_map()
    numeric_m0 = matrix_float(exact_m0)
    body_edge = sp.zeros(15, 1)
    body_edge[14] = 1
    exact_null_spanning = exact_m0.row_join(body_edge)
    checks.check(
        "actual-zero-mode-inventory",
        np.linalg.matrix_rank(q0, tol=1.0e-8) == 4
        and null_basis.shape[1] == 11
        and exact_m0.rank() == 10
        and exact_null_spanning.rank() == 11
        and np.linalg.norm(q0 @ matrix_float(exact_null_spanning)) < 3.0e-13,
        "rank(Q0)=4; nullity=11; constant-metric rank=10; extra branch=1",
    )

    two_stream, bundle_a, bundle_b = exact_source_rows()
    combined = two_stream.row_join(bundle_a).row_join(bundle_b)
    overlap_two_stream = exact_null_spanning.T * two_stream
    overlap_bundles = exact_null_spanning.T * bundle_a.row_join(bundle_b)
    overlap_combined = exact_null_spanning.T * combined
    checks.check(
        "exact-declared-reaction-ranks",
        overlap_two_stream.rank() == 1
        and overlap_bundles.rank() == 2
        and overlap_combined.rank() == 3,
        "bouquet/two-stream=1; 504-history family=2; combined family=3",
    )
    rank_three_minor = sp.simplify(
        overlap_combined.extract([0, 1, 4], [0, 1, 2]).det()
    )
    checks.check(
        "exact-rank-three-certificate",
        rank_three_minor == sp.sqrt(2) / 2,
        f"selected null-pairing minor={rank_three_minor}",
    )

    temporal_sources = sp.Matrix.hstack(
        *[
            2 * sp.eye(15)[:, index]
            for index, direction in enumerate(regge.DIRS15)
            if direction[3] == 1
        ]
    )
    all_edge_sources = 2 * sp.eye(15)
    checks.check(
        "source-family-rank-ladder",
        (exact_null_spanning.T * temporal_sources).rank() == 8
        and (exact_null_spanning.T * all_edge_sources).rank() == 11,
        "all future-temporal rays=8; all actual-edge rays=11",
    )

    exact_projector = sp.simplify(
        exact_null_spanning
        * (exact_null_spanning.T * exact_null_spanning).inv()
        * exact_null_spanning.T
    )
    projected_combined = sp.simplify(exact_projector * combined)
    homothety = exact_m0 * sp.Matrix([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
    scale_residual = sp.simplify(
        projected_combined
        - homothety
        * (homothety.T * projected_combined)
        / (homothety.dot(homothety))
    )
    scale_norms_squared = [
        sp.simplify(scale_residual[:, column].dot(scale_residual[:, column]))
        for column in range(3)
    ]
    checks.check(
        "pure-homothety-reaction-fails-declared-generators",
        scale_residual.rank() == 3
        and projected_combined.row_join(homothety).rank() == 4
        and scale_norms_squared
        == [
            sp.Rational(133, 24) + 3 * sp.sqrt(2) / 4,
            sp.Rational(15, 2),
            sp.Rational(27, 4),
        ],
        "best scale-only residual norm^2="
        + ",".join(str(value) for value in scale_norms_squared),
    )

    extra_branch = sp.Matrix(
        [
            -sp.sqrt(2), -sp.sqrt(2), 0, -sp.sqrt(2), 0,
            0, sp.sqrt(6), -sp.sqrt(2), 0, 0,
            sp.sqrt(6), 0, sp.sqrt(6), sp.sqrt(6), -4 * sp.sqrt(2),
        ]
    ) / 8
    extra_overlaps = [
        sp.simplify((extra_branch.T * combined)[column]) for column in range(3)
    ]
    checks.check(
        "exact-extra-branch-vector",
        sp.simplify(extra_branch.dot(extra_branch)) == 1
        and exact_m0.T * extra_branch == sp.zeros(10, 1)
        and np.linalg.norm(q0 @ matrix_float(extra_branch).reshape(15)) < 3.0e-13,
    )
    checks.check(
        "metric-only-reaction-extra-branch-boundary",
        extra_overlaps
        == [-sp.sqrt(2) / 4, 0, 3 * sp.sqrt(2) / 4],
        "extra overlaps [two-stream,A,B]="
        + ",".join(str(value) for value in extra_overlaps),
    )

    numeric_sources = matrix_float(combined)
    source_reactions = null_projector @ numeric_sources
    source_kkt_equation, source_kkt_constraint = kkt_residuals(
        q0, source_reactions, numeric_sources
    )
    checks.check(
        "minimal-three-channel-kkt-construction",
        np.linalg.matrix_rank(source_reactions, tol=1.0e-9) == 3
        and np.linalg.norm(q0 @ source_reactions) < 3.0e-13
        and source_kkt_equation < 2.0e-13
        and source_kkt_constraint < 2.0e-13,
        f"equation={source_kkt_equation:.3e}; constraint={source_kkt_constraint:.3e}",
    )

    metric_left, metric_singular, _ = np.linalg.svd(numeric_m0, full_matrices=False)
    metric_basis = metric_left[:, metric_singular > 1.0e-10]
    metric_projector = metric_basis @ metric_basis.T
    numeric_extra = matrix_float(extra_branch).reshape(15, 1)
    separated_reactions = np.column_stack(
        (metric_projector @ source_reactions, numeric_extra)
    )
    separated_worst_equation = 0.0
    separated_worst_constraint = 0.0
    q0_pinv = np.linalg.pinv(q0, rcond=1.0e-10)
    for column in range(3):
        multiplier = np.zeros(4)
        multiplier[column] = -1.0
        multiplier[3] = -float(
            (numeric_extra.T @ numeric_sources[:, column]).item()
        )
        reacted = numeric_sources[:, column] + separated_reactions @ multiplier
        response = -q0_pinv @ reacted
        separated_worst_equation = max(
            separated_worst_equation,
            float(
                np.linalg.norm(
                    q0 @ response
                    + numeric_sources[:, column]
                    + separated_reactions @ multiplier
                )
            ),
        )
        separated_worst_constraint = max(
            separated_worst_constraint,
            float(np.linalg.norm(separated_reactions.T @ response)),
        )
    checks.check(
        "four-channel-sector-separated-kkt-construction",
        np.linalg.matrix_rank(separated_reactions, tol=1.0e-9) == 4
        and separated_worst_equation < 2.0e-13
        and separated_worst_constraint < 2.0e-13,
        f"equation={separated_worst_equation:.3e}; constraint={separated_worst_constraint:.3e}",
    )

    full_kkt = np.block(
        [
            [q0, null_basis],
            [null_basis.T, np.zeros((11, 11))],
        ]
    )
    full_worst = 0.0
    for column in range(3):
        rhs = np.concatenate((-numeric_sources[:, column], np.zeros(11)))
        solution = np.linalg.solve(full_kkt, rhs)
        full_worst = max(full_worst, float(np.linalg.norm(full_kkt @ solution - rhs)))
    checks.check(
        "full-eleven-channel-unique-kkt-construction",
        np.linalg.matrix_rank(full_kkt, tol=1.0e-9) == 26
        and full_worst < 2.0e-13,
        f"KKT rank=26; max residual={full_worst:.3e}",
    )

    single_reaction = source_reactions[:, :1]
    single_equation, single_constraint = kkt_residuals(
        q0, single_reaction, numeric_sources[:, :1]
    )
    checks.check(
        "one-source-aligned-channel-control",
        single_equation < 2.0e-13 and single_constraint < 2.0e-13,
        "one scalar channel suffices for one fixed source only when aligned to its full null projection",
    )
    reduced_reactions = source_reactions[:, :2]
    best_reduced_multiplier = -np.linalg.lstsq(
        reduced_reactions, null_projector @ numeric_sources[:, 2], rcond=None
    )[0]
    reduced_residual = np.linalg.norm(
        null_projector
        @ (numeric_sources[:, 2] + reduced_reactions @ best_reduced_multiplier)
    )
    checks.check(
        "rank-two-reaction-negative-control",
        reduced_residual > 1.0,
        f"omitting the third combined-family reaction leaves null residual={reduced_residual:.6f}",
    )

    bundle_reactions = null_projector @ numeric_sources[:, 1:3]
    history_count = 0
    history_worst = 0.0
    for length in range(3, 9):
        for bits in product((0, 1), repeat=length):
            history_count += 1
            fraction = sum(bits) / length
            mean_source = (
                fraction * numeric_sources[:, 1]
                + (1.0 - fraction) * numeric_sources[:, 2]
            )
            coefficients = np.linalg.lstsq(
                bundle_reactions, null_projector @ mean_source, rcond=None
            )[0]
            history_worst = max(
                history_worst,
                float(
                    np.linalg.norm(
                        null_projector @ mean_source
                        - bundle_reactions @ coefficients
                    )
                ),
            )
    checks.check(
        "all-binary-history-reaction-span",
        history_count == 504 and history_worst < 2.0e-14,
        f"histories={history_count}; worst span residual={history_worst:.3e}",
    )

    checks.check(
        "theorem-source-surface",
        all(
            phrase in note_flat
            for phrase in (
                "ranks one, two, and three",
                "133/24+3sqrt(2)/4",
                "eight and eleven",
                "three mixed reactions",
                "four sector-separated reactions",
                "eleven-reaction map",
                "candidate amendment",
            )
        ),
    )
    checks.check(
        "no-go-discipline-source-surface",
        all(f"N{index}" in note for index in range(1, 9))
        and "No universal compact-gravity no-go" in note_flat
        and "pure homothety reaction" in note_flat,
    )
    checks.check(
        "canonical-axiom-nonmutation",
        all(
            phrase not in axiom_flat
            for phrase in (
                "homogeneous reaction map",
                "null-projection coverage",
                "extra Regge branch lift",
            )
        ),
    )
    checks.check(
        "fixed-rubric-boundary",
        "fixed TOE percentages remain unchanged" in note_flat,
    )

    print("per_element: checked all fifteen actual-edge rays, all eight future-temporal rays, and the exact extra-branch covector")
    print("per_site: checked all 504 binary bundle histories through their compact mean sources and common two-reaction span")
    print("per_mode: checked the actual compact k=0 Hessian with eleven null directions and no source projection in the KKT equation")
    print("per_block: checked the general reaction-rank lower bound, exact rank ladder, constructive three/four/eleven-channel completions, and axiom boundary")
    print("lattice_wide: checked the complete declared compact source families; open, curved, nonlinear, alternate-carrier, and background routes remain outside scope")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
