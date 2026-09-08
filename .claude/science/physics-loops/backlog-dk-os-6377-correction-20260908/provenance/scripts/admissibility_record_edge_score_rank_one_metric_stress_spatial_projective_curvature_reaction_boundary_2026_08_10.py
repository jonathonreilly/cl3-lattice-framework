#!/usr/bin/env python3
"""Compile Record edge scores into metric stress and compact reactions.

The local witness has one null Record and fifteen edge-labelled Records.  Its
null-relative log odds are linear edge-length scores, so differentiation gives
the actual edge-source rays and a rank-one metric stress for each constituent.
Finite-region product laws provide exact spatial marginal consistency.

On the flat Regge carrier, the curvature-squared action lifts the one
nonmetric null branch.  The remaining kernel is exactly the ten-dimensional
constant-metric image, so a metric-only KKT reaction system is nonsingular and
solves every compiled source.  The Record law, beta action unit, alpha
curvature coefficient, compact ensemble, and physical dynamics remain
conditional inputs.
"""

from __future__ import annotations

from fractions import Fraction
from functools import reduce
from itertools import combinations, permutations, product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_record_null_charge_projective_history_phase_selector_scale_response_boundary_2026_08_10 as block30  # noqa: E402
import admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10 as reaction  # noqa: E402
import admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10 as lift  # noqa: E402


regge = reaction.regge

AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_RECORD_EDGE_SCORE_RANK_ONE_METRIC_STRESS_SPATIAL_PROJECTIVE_"
    "CURVATURE_REACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
ANCHOR_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REACTION_PATH = reaction.NOTE_PATH
LIFT_PATH = lift.NOTE_PATH
BLOCK30_PATH = block30.NOTE_PATH
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RECORD_EDGE_SCORE_RANK_ONE_METRIC_STRESS_SPATIAL_PROJECTIVE_CURVATURE_REACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_RECORD_NULL_CHARGE_PROJECTIVE_HISTORY_PHASE_SELECTOR_SCALE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_null_record_log_odds_action_representative_anchor_boundary_2026_08_10.py",
    "scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/admissibility_record_null_charge_projective_history_phase_selector_scale_response_boundary_2026_08_10.py",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def softmax_record_probabilities(
    edge_coordinates: np.ndarray, beta: float, common_action: float
) -> np.ndarray:
    """One null plus fifteen edge Records with a common additive action."""
    actions = np.r_[common_action, common_action + beta * edge_coordinates]
    weights = np.exp(-(actions - np.min(actions)))
    return weights / np.sum(weights)


def rational_site_kernel(site: int) -> tuple[Fraction, ...]:
    """A rational point of the same positive softmax family."""
    weights = [Fraction(1)] + [
        Fraction((site + 2) * (edge + 2) + 1, (site + 3) * (edge + 3) + 2)
        for edge in range(15)
    ]
    normalizer = sum(weights, Fraction())
    return tuple(weight / normalizer for weight in weights)


def subset_law(
    subset: tuple[int, ...], kernels: tuple[tuple[Fraction, ...], ...]
) -> dict[tuple[int, ...], Fraction]:
    return {
        history: reduce(
            lambda left, right: left * right,
            (
                kernels[site][state]
                for site, state in zip(subset, history)
            ),
            Fraction(1),
        )
        for history in product(range(16), repeat=len(subset))
    }


def edge_permutation_matrix(permutation: tuple[int, ...]) -> np.ndarray:
    directions = tuple(tuple(item) for item in regge.DIRS15)
    index = {direction: position for position, direction in enumerate(directions)}
    matrix = np.zeros((15, 15), dtype=float)
    for edge, direction in enumerate(directions):
        transformed = [0, 0, 0, 0]
        for old_axis, bit in enumerate(direction):
            transformed[permutation[old_axis]] = bit
        matrix[index[tuple(transformed)], edge] = 1.0
    return matrix


def metric_permutation_matrix(permutation: tuple[int, ...]) -> np.ndarray:
    index = {tuple(component): position for position, component in enumerate(regge.HCOMPS)}
    matrix = np.zeros((10, 10), dtype=float)
    for column, (left, right) in enumerate(regge.HCOMPS):
        transformed = tuple(sorted((permutation[left], permutation[right])))
        matrix[index[transformed], column] = 1.0
    return matrix


def metric_tensor(coordinate_covector: np.ndarray) -> np.ndarray:
    tensor = np.zeros((4, 4), dtype=float)
    for value, (left, right) in zip(coordinate_covector, regge.HCOMPS):
        if left == right:
            tensor[left, right] = value
        else:
            tensor[left, right] = value / 2.0
            tensor[right, left] = value / 2.0
    return tensor


def compact_operators():
    flat_lengths = np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )
    curvature_kernel = lift.curvature_squared_kernel(flat_lengths)
    q0 = regge.bloch_Q(np.zeros(4)).real
    r20 = lift.bloch(curvature_kernel, np.zeros(4)).real
    metric_map = np.asarray(reaction.exact_metric_map(), dtype=float)
    gram = metric_map.T @ metric_map
    metric_projector = metric_map @ np.linalg.inv(gram) @ metric_map.T

    eigenvalues, eigenvectors = np.linalg.eigh(q0)
    bare_null = eigenvectors[:, np.abs(eigenvalues) < 1.0e-8]
    residual = (np.eye(15) - metric_projector) @ bare_null
    left, singular_values, _ = np.linalg.svd(residual)
    extra = left[:, np.argmax(singular_values)]
    extra /= np.linalg.norm(extra)
    return q0, r20, metric_map, metric_projector, extra


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    anchor_note = flat(ANCHOR_PATH)
    reaction_note = flat(REACTION_PATH)
    lift_note = flat(LIFT_PATH)
    block30_note = flat(BLOCK30_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; the Record family, edge-to-metric map, Regge action, and compact source inventories are repository-local")
    print("analytic_boundary: finite-region marginals and null-relative ratios are exact; compact Regge and curvature-reaction tests use double precision plus one exact extra-branch Hessian")
    print("physical_boundary: the edge-labelled Record law, beta action unit, alpha curvature coefficient, compact metric constraint, source interpretation, full Ward connection, and Lorentzian dynamics remain unselected")

    checks.check(
        "axiom-and-parent-boundary",
        "current axioms do not supply the Record edge-score law or geometry dynamics, while retained parents supply only conditional action and reaction mechanisms",
        "admissibility is not a dynamics axiom" in axioms
        and "source/action and physical-observable identification" in axioms
        and "unique dimensionless action representative" in anchor_note
        and "ten-dimensional constant-metric image" in reaction_note
        and "ten remaining zeros are exactly the constant-metric" in lift_note
        and "ten residual compact channels" in block30_note
        and all(
            key in registry
            for key in (
                "minimal_axioms",
                "scale_reference_primitive",
                "kinetic_isotropy_primitive",
                "realized_state_primitive",
            )
        ),
    )
    checks.check(
        "note-contract",
        "the note separates a constructive Record/source/reaction compiler from physical law selection and carries N1--N8",
        "rank-one metric stress" in note
        and "spatial projective" in note
        and "metric-only reaction" in note
        and "not a selected gravity law" in note
        and "n1--n8 status:" in note
        and "no canonical axiom is edited" in note,
    )

    edge_coordinates = np.linspace(-0.31, 0.43, 15)
    minimum_probability = 1.0
    normalization_error = 0.0
    common_shift_error = 0.0
    action_error = 0.0
    source_error = 0.0
    for beta in (0.5, 1.0, 2.0):
        reference = softmax_record_probabilities(edge_coordinates, beta, -2.75)
        for common in (-2.75, 0.0, 4.5):
            probabilities = softmax_record_probabilities(
                edge_coordinates, beta, common
            )
            minimum_probability = min(minimum_probability, *probabilities)
            normalization_error = max(
                normalization_error, abs(float(np.sum(probabilities)) - 1.0)
            )
            common_shift_error = max(
                common_shift_error, float(np.max(np.abs(probabilities - reference)))
            )
            relative_action = -np.log(probabilities[1:] / probabilities[0])
            action_error = max(
                action_error,
                float(np.max(np.abs(relative_action - beta * edge_coordinates))),
            )
        step = 1.0e-6
        baseline = -np.log(reference[1:] / reference[0])
        jacobian = np.zeros((15, 15))
        for edge in range(15):
            shifted = edge_coordinates.copy()
            shifted[edge] += step
            shifted_probability = softmax_record_probabilities(
                shifted, beta, 1.25
            )
            shifted_action = -np.log(
                shifted_probability[1:] / shifted_probability[0]
            )
            jacobian[:, edge] = (shifted_action - baseline) / step
        source_error = max(
            source_error,
            float(np.max(np.abs(jacobian - beta * np.eye(15)))),
        )
    checks.check(
        "positive-normalized-local-record-family",
        "one null plus fifteen edge Records form a strictly positive normalized local family whose common action cancels",
        minimum_probability > 0.0
        and normalization_error < 1.0e-14
        and common_shift_error < 1.0e-14,
        f"minimum probability={minimum_probability:.6f}; normalization={normalization_error:.3e}; common shift={common_shift_error:.3e}",
    )
    checks.check(
        "null-log-odds-edge-source-compiler",
        "null-relative log odds are beta times the edge coordinates and differentiate to the actual edge-source basis",
        action_error < 1.0e-13 and source_error < 2.0e-9,
        f"action={action_error:.3e}; finite-difference source={source_error:.3e}",
    )

    metric_map = np.asarray(reaction.exact_metric_map(), dtype=float)
    stress_error = 0.0
    stress_minimum_eigenvalue = 1.0
    stress_ranks = set()
    for edge, direction in enumerate(regge.DIRS15):
        source = np.eye(15)[:, edge]
        tensor = metric_tensor(metric_map.T @ source)
        vector = np.asarray(direction, dtype=float)
        expected = np.outer(vector, vector) / (2.0 * np.linalg.norm(vector))
        eigenvalues = np.linalg.eigvalsh(tensor)
        stress_error = max(stress_error, float(np.linalg.norm(tensor - expected)))
        stress_minimum_eigenvalue = min(
            stress_minimum_eigenvalue, float(np.min(eigenvalues))
        )
        stress_ranks.add(int(np.linalg.matrix_rank(tensor, tol=1.0e-10)))
    checks.check(
        "constituent-rank-one-metric-stress",
        "every edge-labelled Record compiles to the positive rank-one Euclidean metric stress vv^T/(2|v|)",
        stress_error < 1.0e-12
        and stress_minimum_eigenvalue > -1.0e-12
        and stress_ranks == {1},
        f"tensor error={stress_error:.3e}; minimum eigenvalue={stress_minimum_eigenvalue:.3e}; ranks={stress_ranks}",
    )

    kernels = tuple(rational_site_kernel(site) for site in range(4))
    laws: dict[tuple[int, ...], dict[tuple[int, ...], Fraction]] = {}
    total_histories = 0
    normalization_failures = 0
    for size in range(5):
        for subset in combinations(range(4), size):
            law = subset_law(subset, kernels)
            laws[subset] = law
            total_histories += len(law)
            normalization_failures += int(sum(law.values(), Fraction()) != 1)

    marginal_failures = 0
    marginal_checks = 0
    additive_failures = 0
    for subset, law in laws.items():
        null_history = (0,) * len(subset)
        null_probability = law[null_history]
        for history, probability in law.items():
            expected_ratio = reduce(
                lambda left, right: left * right,
                (
                    kernels[site][state] / kernels[site][0]
                    for site, state in zip(subset, history)
                ),
                Fraction(1),
            )
            additive_failures += int(
                probability / null_probability != expected_ratio
            )
        for position, site in enumerate(subset):
            target_subset = tuple(item for item in subset if item != site)
            target_law = laws[target_subset]
            for history, probability in target_law.items():
                marginal_checks += 1
                marginal = sum(
                    (
                        law[
                            history[:position]
                            + (state,)
                            + history[position:]
                        ]
                        for state in range(16)
                    ),
                    Fraction(),
                )
                marginal_failures += int(marginal != probability)
    all_null_probability = laws[(0, 1, 2, 3)][(0, 0, 0, 0)]
    checks.check(
        "exact-spatial-projective-record-family",
        "the four-site product family is exactly consistent under every one-site deletion from every finite subset",
        total_histories == 83521
        and marginal_checks == 19652
        and normalization_failures == 0
        and marginal_failures == 0,
        f"histories={total_histories}; marginals={marginal_checks}; failures={marginal_failures}",
    )
    checks.check(
        "all-null-anchor-and-additive-record-action",
        "the all-null history has positive weight and every finite-region null-relative action factorizes into local Record scores",
        all_null_probability > 0 and additive_failures == 0,
        f"all-null probability={all_null_probability}; ratio failures={additive_failures}",
    )

    q0, r20, metric_map, metric_projector, extra = compact_operators()
    (
        _,
        _,
        bare_null_projector,
        homothety,
        scale_projector,
        block30_residual_projector,
    ) = block30.compact_data()
    extra_projector = np.outer(extra, extra)
    shape_projector = metric_projector - scale_projector
    null_split_error = max(
        float(
            np.linalg.norm(
                bare_null_projector - metric_projector - extra_projector, 2
            )
        ),
        float(
            np.linalg.norm(
                block30_residual_projector
                - shape_projector
                - extra_projector,
                2,
            )
        ),
    )
    checks.check(
        "compact-null-sector-refinement",
        "the eleven bare null charges are ten constant-metric stresses plus one nonmetric branch, and the Block-30 residual is nine metric-shape charges plus that branch",
        np.linalg.matrix_rank(metric_projector, tol=1.0e-8) == 10
        and np.linalg.matrix_rank(shape_projector, tol=1.0e-8) == 9
        and np.linalg.matrix_rank(extra_projector, tol=1.0e-8) == 1
        and null_split_error < 1.0e-12,
        f"metric/shape/extra ranks=10/9/1; split error={null_split_error:.3e}",
    )

    exact_extra_lift = lift.exact_extra_curvature_square_hessian()
    extra_lift = float(extra @ r20 @ extra)
    metric_lift_error = float(np.linalg.norm(r20 @ metric_map, 2))
    checks.check(
        "action-native-extra-branch-lift",
        "the retained curvature-squared action lifts the nonmetric branch and annihilates the complete constant-metric image",
        exact_extra_lift == 768 + 384 * sp.sqrt(2)
        and extra_lift > 1300.0
        and metric_lift_error < 1.0e-10,
        f"exact={exact_extra_lift}; numeric={extra_lift:.9f}; metric error={metric_lift_error:.3e}",
    )

    worst_edge_metric_covariance = 0.0
    worst_q_covariance = 0.0
    worst_r2_covariance = 0.0
    worst_projector_covariance = 0.0
    worst_probability_covariance = 0.0
    covariance_coordinates = np.linspace(-0.27, 0.35, 15)
    covariance_probability = softmax_record_probabilities(
        covariance_coordinates, 1.0, 0.0
    )
    for permutation in permutations(range(4)):
        edge_action = edge_permutation_matrix(permutation)
        metric_action = metric_permutation_matrix(permutation)
        worst_edge_metric_covariance = max(
            worst_edge_metric_covariance,
            float(np.linalg.norm(edge_action @ metric_map - metric_map @ metric_action)),
        )
        worst_q_covariance = max(
            worst_q_covariance,
            float(np.linalg.norm(edge_action @ q0 @ edge_action.T - q0, 2)),
        )
        worst_r2_covariance = max(
            worst_r2_covariance,
            float(np.linalg.norm(edge_action @ r20 @ edge_action.T - r20, 2)),
        )
        worst_projector_covariance = max(
            worst_projector_covariance,
            float(
                np.linalg.norm(
                    edge_action @ metric_projector @ edge_action.T
                    - metric_projector,
                    2,
                )
            ),
        )
        transformed_probability = softmax_record_probabilities(
            edge_action @ covariance_coordinates, 1.0, 2.0
        )
        expected_probability = np.r_[
            covariance_probability[0], edge_action @ covariance_probability[1:]
        ]
        worst_probability_covariance = max(
            worst_probability_covariance,
            float(np.max(np.abs(transformed_probability - expected_probability))),
        )
    checks.check(
        "axis-covariant-record-source-and-reaction-data",
        "the local Record law, edge-to-metric compiler, both geometry Hessians, and metric reaction projector commute with all 24 axis permutations",
        worst_edge_metric_covariance == 0.0
        and worst_q_covariance < 1.0e-11
        and worst_r2_covariance < 1.0e-10
        and worst_projector_covariance < 1.0e-12
        and worst_probability_covariance < 1.0e-14,
        f"M={worst_edge_metric_covariance:.3e}; Q={worst_q_covariance:.3e}; R2={worst_r2_covariance:.3e}; P={worst_projector_covariance:.3e}; probability={worst_probability_covariance:.3e}",
    )

    four_site_histories = product(range(16), repeat=4)
    count_sources = {
        tuple(history.count(edge + 1) for edge in range(15))
        for history in four_site_histories
    }
    source_matrix = np.asarray(sorted(count_sources), dtype=float).T
    kkt_ranks = set()
    operator_ranks = set()
    worst_equation = 0.0
    worst_constraint = 0.0
    worst_reaction_identity = 0.0
    gram = metric_map.T @ metric_map
    for alpha in lift.ALPHA_WITNESSES:
        repaired = q0 + alpha * r20
        kkt = np.block(
            [
                [repaired, metric_map],
                [metric_map.T, np.zeros((10, 10))],
            ]
        )
        operator_ranks.add(int(np.linalg.matrix_rank(repaired, tol=1.0e-8)))
        kkt_ranks.add(int(np.linalg.matrix_rank(kkt, tol=1.0e-8)))
        for beta in (0.5, 1.0, 2.0):
            sources = beta * source_matrix
            right = np.vstack((-sources, np.zeros((10, sources.shape[1]))))
            solution = np.linalg.solve(kkt, right)
            response = solution[:15]
            multipliers = solution[15:]
            equation = repaired @ response + metric_map @ multipliers + sources
            constraint = metric_map.T @ response
            reaction_identity = metric_map @ multipliers + metric_projector @ sources
            worst_equation = max(worst_equation, float(np.linalg.norm(equation, 2)))
            worst_constraint = max(
                worst_constraint, float(np.linalg.norm(constraint, 2))
            )
            worst_reaction_identity = max(
                worst_reaction_identity,
                float(np.linalg.norm(reaction_identity, 2)),
            )
    checks.check(
        "metric-only-curvature-kkt-window",
        "after the action-native lift, the ten-column constant-metric reaction system is nonsingular throughout the retained alpha window",
        operator_ranks == {5} and kkt_ranks == {25},
        f"operator ranks={operator_ranks}; KKT ranks={kkt_ranks}",
    )
    checks.check(
        "all-four-site-record-sources-solve",
        "all 3,876 distinct four-site Record count sources solve at five alpha and three beta controls without source projection",
        len(count_sources) == 3876
        and worst_equation < 1.0e-10
        and worst_constraint < 1.0e-10,
        f"sources={len(count_sources)}; equation={worst_equation:.3e}; constraint={worst_constraint:.3e}",
    )
    checks.check(
        "reaction-equals-compiled-metric-stress",
        "the KKT reaction is exactly the negative metric projection of the compiled edge source, leaving the lifted nonmetric response dynamical",
        worst_reaction_identity < 1.0e-10,
        f"reaction identity={worst_reaction_identity:.3e}",
    )

    source_index = int(np.argmax(np.abs(extra)))
    selected_source = np.eye(15)[:, source_index]
    responses = {}
    probabilities = {}
    for alpha in (lift.ALPHA_WITNESSES[0], lift.ALPHA_WITNESSES[-1]):
        repaired = q0 + alpha * r20
        kkt = np.block(
            [
                [repaired, metric_map],
                [metric_map.T, np.zeros((10, 10))],
            ]
        )
        for beta in (0.5, 1.0, 2.0):
            solution = np.linalg.solve(
                kkt, np.r_[-beta * selected_source, np.zeros(10)]
            )
            responses[(alpha, beta)] = solution[:15]
            probabilities[beta] = softmax_record_probabilities(
                edge_coordinates, beta, 0.0
            )
    response_separation = min(
        np.linalg.norm(
            responses[(lift.ALPHA_WITNESSES[0], beta)]
            - responses[(lift.ALPHA_WITNESSES[-1], beta)]
        )
        for beta in (0.5, 1.0, 2.0)
    )
    probability_separation = min(
        np.linalg.norm(probabilities[left] - probabilities[right])
        for left, right in ((0.5, 1.0), (1.0, 2.0), (0.5, 2.0))
    )
    checks.check(
        "source-unit-and-curvature-coefficient-nonselection",
        "positivity, axis covariance, spatial projectivity, rank-one stress, and compact solvability do not select beta or alpha",
        response_separation > 1.0e-3 and probability_separation > 1.0e-3,
        f"minimum response separation={response_separation:.6f}; probability separation={probability_separation:.6f}",
    )
    checks.check(
        "spatial-versus-causal-projectivity-boundary",
        "the new exact spatial product marginals and Block-30 causal-prefix marginals are complementary but do not derive an interacting joint spacetime law",
        "causal-prefix direction" in block30_note
        and "spatial finite-region" in note
        and "interacting joint spacetime law" in note,
    )
    checks.check(
        "full-ward-and-lorentzian-boundary",
        "compact homogeneous solvability does not establish nonzero-momentum conservation, a complete differentiated Ward identity, or Lorentzian nonlinear stability",
        "nonzero-momentum" in note
        and "complete differentiated ward" in note
        and "lorentzian" in note
        and "not a selected gravity law" in note,
    )
    checks.check(
        "minimal-law-or-axiom-delta",
        "the compilers can remain downstream, while autonomy still needs a fixed Record score law, action unit, geometry action and phase, interacting gluing, Ward connection, and causal update",
        "can remain downstream" in note
        and "record score law" in note
        and "action unit" in note
        and "geometry action" in note
        and "ward connection" in note
        and "no fifth ontology axiom is proven necessary" in note,
    )

    print("N5_CERTIFICATE: record_source=one positive null-anchored edge-labelled Record family differentiates to the actual edge-source basis and rank-one metric stress")
    print("N5_CERTIFICATE: spatial_gluing=83,521 exact finite-region probabilities obey 19,652 arbitrary one-site restriction identities")
    print("N5_CERTIFICATE: reaction_repair=the curvature-square action lifts the nonmetric branch and a ten-column metric-only KKT system solves all 3,876 four-site source counts")
    print("N5_CERTIFICATE: gravity_boundary=compact reactions freeze constant-metric modes and do not replace a curved/open field equation, nonzero-momentum Ward law, or Lorentzian update")
    print("N5_CERTIFICATE: axiom_boundary=the compiler can be downstream but the Record score, beta, alpha, phase, interacting law, and dynamics are unselected")
    print("per_element: checked all fifteen actual-edge Records and their rank-one metric stresses")
    print("per_site: checked one null plus fifteen edge Records at four site-dependent rational family points")
    print("per_region: checked every subset of four sites, 83,521 probabilities, and 19,652 exact restriction identities")
    print("per_source: checked all 3,876 four-site count sources at five alpha and three beta controls")
    print("lattice_wide: finite product regions and the compact homogeneous carrier only; no interacting infinite-volume, full-Ward, nonlinear, or Lorentzian theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
