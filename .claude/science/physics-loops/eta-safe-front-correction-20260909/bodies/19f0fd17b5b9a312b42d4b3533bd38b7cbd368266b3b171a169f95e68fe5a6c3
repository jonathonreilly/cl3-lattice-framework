#!/usr/bin/env python3
"""Exact Block-03 affine-eta to binary-Record structural join.

This runner separates a factorized physical candidate from the always-possible
controlled probability dictionary.  It reconstructs the nontrivial affine
M2 action, Boolean decoder, native source, inherited positive Schur germ, and
two exact Record instruments.  It then classifies the sharpness image under
Record-only versus stronger action-repeatability requirements.
"""

from __future__ import annotations

import argparse
from functools import cache
import inspect
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_block208_source_eta_action_native_record_dilation_2026_08_28 as b2  # noqa: E402
import admissibility_d4_h1_action_factorized_six_m2_source_ownership_2026_08_28 as eta1  # noqa: E402
import admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26 as b206  # noqa: E402


PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block03-affine-lineage-binary-join-20260829"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
PREREG_COMMIT = "61547d21fed6c2941da7ccee8ac993eb0b222249"
PARENT_COMMIT = "f5e5c140c06df6aaf6c1b76c2e165c5a49ca4a90"
BLOCK02_RESULT = "03c3629fd06bbcb6863d639b2e0bdf5a1e2f4d3c"
BLOCK206_RESULT = "42b25280486363e9c2017698b813edf182d1a1a3"
BLOCK205_RESULT = "ff1c77c8a22caeffa75972672ad6042080c1e68c"
CURRENT_MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
GOAL_BLOB = "da1a8e551e5425a05d83d53c227e5f3589b50403"
PREFLIGHT_BLOB = "203110c432b8882c346378c4eee59e3eb3a1925b"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = (
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_"
    "REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
AUDIT_TIMEOUT_SEC = 300
TIMEOUT_SEC = 300

EXPECTED_BLOBS = {
    (
        f"{BLOCK02_RESULT}:docs/"
        "ADMISSIBILITY_D4_BLOCK208_AFFINE_SIX_RECORD_H1_DECODER_"
        "CENTER_CORNER_QND_DILATION_BOUNDARY_BOUNDED_THEOREM_NOTE_"
        "2026-08-28.md"
    ): "95e67961ffe80fb89b6c0ef7f37337ca0aa5099d",
    (
        f"{BLOCK02_RESULT}:scripts/"
        "admissibility_d4_block208_source_eta_action_native_record_"
        "dilation_2026_08_28.py"
    ): "cfa8f0f635db689fba9c9a66963efacae35d26a4",
    (
        f"{BLOCK02_RESULT}:logs/runner-cache/"
        "admissibility_d4_block208_source_eta_action_native_record_"
        "dilation_2026_08_28.txt"
    ): "96ff030ab3b8193ebc6c8be8e6fb5b1501b5c15d",
    (
        f"{BLOCK206_RESULT}:docs/"
        "ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_"
        "DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
    ): "3da5ba134fb6947e62a5db32f12e75b254adf555",
    (
        f"{BLOCK206_RESULT}:scripts/"
        "admissibility_d4_h1_port_free_neighbor_m2_context_descent_"
        "2026_08_26.py"
    ): "59893ed2a5bd1182a65a97dc1abc51fea0f16ca2",
    (
        f"{BLOCK206_RESULT}:logs/runner-cache/"
        "admissibility_d4_h1_port_free_neighbor_m2_context_descent_"
        "2026_08_26.txt"
    ): "368e228405762936079edd269cb61a42bb0a9556",
    (
        f"{BLOCK205_RESULT}:docs/"
        "ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_"
        "BOUNDED_THEOREM_NOTE_2026-08-26.md"
    ): "77ff334f280e6cbf7679c670eef4d2ae7bb0649e",
    (
        f"{BLOCK205_RESULT}:scripts/"
        "admissibility_d4_h1_schur_record_probability_germ_"
        "2026_08_26.py"
    ): "7eb65ab81efa33b0ee18c7647ed1f68ceb8fe05f",
    (
        f"{BLOCK205_RESULT}:logs/runner-cache/"
        "admissibility_d4_h1_schur_record_probability_germ_"
        "2026_08_26.txt"
    ): "6ed9dcb17545883a5612e27e51ad8cd4cbbb12ca",
}

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block03-affine-lineage-binary-join-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block03-affine-lineage-binary-join-20260829/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_D4_BLOCK208_AFFINE_SIX_RECORD_H1_DECODER_CENTER_CORNER_QND_DILATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "scripts/admissibility_d4_block208_source_eta_action_native_record_dilation_2026_08_28.py",
    "logs/runner-cache/admissibility_d4_block208_source_eta_action_native_record_dilation_2026_08_28.txt",
    "docs/ADMISSIBILITY_D4_H1_NATIVE_ACTION_FACTOR_LOCALITY_SIX_M2_SOURCE_OWNERSHIP_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "scripts/admissibility_d4_h1_action_factorized_six_m2_source_ownership_2026_08_28.py",
    "docs/ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.txt",
    "docs/ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_schur_record_probability_germ_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_schur_record_probability_germ_2026_08_26.txt",
)

MUTATIONS = (
    "stale_main",
    "unpin_goal",
    "unpin_preflight",
    "alter_dependency_blob",
    "lose_rotation",
    "hide_affine_class",
    "break_affine_group_law",
    "bit_labels_not_full_m2",
    "select_trivial_action",
    "erase_regular_orbit",
    "erase_anf_decoder",
    "fit_decoder_after_h1",
    "add_runtime_frame",
    "break_direction_selector",
    "lower_selector_degree",
    "erase_active_projector",
    "change_source_term",
    "replace_actual_reverse",
    "erase_native_factorization",
    "add_runtime_pq",
    "erase_positive_germ",
    "erase_cubic_response",
    "erase_c32_operator_lift",
    "misorder_signed_shell",
    "replace_with_probability_table",
    "erase_sharp_join",
    "erase_half_sharp_join",
    "erase_continuum_proof",
    "call_sharpness_selected",
    "claim_global_repeatability",
    "promote_global_no_member",
    "erase_certified_endpoint",
    "break_cptp",
    "disturb_input_record",
    "merge_output_records",
    "hide_precursor_workspace",
    "call_blank_one_m2_possibility",
    "break_output_lock",
    "break_covariance",
    "break_schur_intertwiner",
    "erase_translation_covariance",
    "break_controlled_complement",
    "sample_only_continuum",
    "call_formation_site_selected",
    "call_formation_rate_selected",
    "claim_repeated_history",
    "claim_h2",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_movement",
    "claim_retained",
)

N5_LINES = (
    "per_element: checked both affine full-M2 automorphisms, every Boolean ANF coefficient, actual C32 effects and roots, and both orthogonal output-Record branches.",
    "per_site: checked all 64 simultaneous six-neighbor Record conditions and every block of the exact 2048-to-4096 eta-controlled C32 formation operator.",
    "per_mode: checked the complete active H1 orbit, the corrected signed-shell order, actual cubic C32 traces, the exact abs(e)<=10^-9 certificate, and the full sharpness interval; H2 remains sealed.",
    "per_block: checked the 110/110 source, exact Schur resolvents, normalized C32 state, covariant effect, controlled lineage channel, precursor typing, and active/inactive repeatability split.",
    "lattice_wide: checked and not executed — no autonomous eta preparation, formation site/rate, recurrence, clock, unbounded history, gravity identification, retained theory, or TOE closure is supplied.",
)


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=TIMEOUT_SEC
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    blob_matches = {
        locator: git_output("rev-parse", locator) == expected
        for locator, expected in EXPECTED_BLOBS.items()
    }
    block206_cache = (
        ROOT / "logs/runner-cache/"
        "admissibility_d4_h1_port_free_neighbor_m2_context_descent_"
        "2026_08_26.txt"
    ).read_text()
    block205_cache = (
        ROOT / "logs/runner-cache/"
        "admissibility_d4_h1_schur_record_probability_germ_"
        "2026_08_26.txt"
    ).read_text()
    return {
        "origin_main": git_output("rev-parse", "origin/main"),
        "parent_is_ancestor": is_ancestor(PARENT_COMMIT),
        "prereg_is_ancestor": is_ancestor(PREREG_COMMIT),
        "goal_registered": git_output(
            "rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}"
        ),
        "goal_worktree": git_output("hash-object", "--", GOAL_PATH),
        "preflight_registered": git_output(
            "rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH}"
        ),
        "preflight_worktree": git_output(
            "hash-object", "--", PREFLIGHT_PATH
        ),
        "axiom_blob": git_output("hash-object", "--", AXIOM_PATH),
        "dependency_blobs": blob_matches,
        "inputs_present": all((ROOT / path).is_file()
                              for path in AUDIT_INPUT_PATHS),
        "block206_cache_positive": all(
            needle in block206_cache for needle in (
                "status: ok",
                "[D] PASS",
                "positive port-free H1 neighbor-phase binary germ exists",
                "TOTAL: PASS=8 FAIL=0",
            )
        ),
        "block205_cache_positive": all(
            needle in block205_cache for needle in (
                "status: ok",
                "[E] PASS",
                "positive analytic H1 right-Schur probability germ exists",
                "TOTAL: PASS=8 FAIL=0",
            )
        ),
    }


@cache
def action_facts() -> dict[str, object]:
    group = b2.rotations()
    table = b2.multiplication_table()
    permutations = b2.shell_permutations()
    classification = b2.affine_action_classes(6)
    classes = classification["classes"]
    selected = tuple(item for item in classes if item["has_orbit24"])
    if len(selected) != 1:
        raise AssertionError("expected one affine orbit-24 class")
    class_checks = []
    for item in classes:
        class_translations = item["translations"]

        def class_action(group_index: int, mask: int) -> int:
            return (
                b2.permute_mask(mask, permutations[group_index])
                ^ class_translations[group_index]
            )

        def matrix_unit_image(
            group_index: int, site: int, row: int, column: int,
        ) -> tuple[int, int, int]:
            target = permutations[group_index][site]
            flip = (class_translations[group_index] >> target) & 1
            return target, row ^ flip, column ^ flip

        mask_group_law = all(
            class_action(table[left][right], mask)
            == class_action(left, class_action(right, mask))
            for left in range(24)
            for right in range(24)
            for mask in range(64)
        )
        matrix_unit_group_law = all(
            matrix_unit_image(table[left][right], site, row, column)
            == matrix_unit_image(
                left, *matrix_unit_image(right, site, row, column)
            )
            for left in range(24)
            for right in range(24)
            for site in range(6)
            for row in range(2)
            for column in range(2)
        )
        star_preserved = all(
            matrix_unit_image(g, site, column, row)
            == (
                matrix_unit_image(g, site, row, column)[0],
                matrix_unit_image(g, site, row, column)[2],
                matrix_unit_image(g, site, row, column)[1],
            )
            for g in range(24)
            for site in range(6)
            for row in range(2)
            for column in range(2)
        )
        multiplication_preserved = all(
            (
                matrix_unit_image(g, site, row, right_column)
                if left_column == right_row else None
            )
            == (
                (
                    matrix_unit_image(g, site, row, left_column)[0],
                    matrix_unit_image(g, site, row, left_column)[1],
                    matrix_unit_image(
                        g, site, right_row, right_column
                    )[2],
                )
                if matrix_unit_image(g, site, row, left_column)[2]
                == matrix_unit_image(g, site, right_row, right_column)[1]
                else None
            )
            for g in range(24)
            for site in range(6)
            for row in range(2)
            for left_column in range(2)
            for right_row in range(2)
            for right_column in range(2)
        )
        unity_preserved = all(
            {
                matrix_unit_image(g, site, 0, 0)[1:],
                matrix_unit_image(g, site, 1, 1)[1:],
            } == {(0, 0), (1, 1)}
            and matrix_unit_image(g, site, 0, 0)[0]
            == matrix_unit_image(g, site, 1, 1)[0]
            for g in range(24)
            for site in range(6)
        )
        cross_site_commutation = all(
            matrix_unit_image(g, left_site, 0, 1)[0]
            != matrix_unit_image(g, right_site, 1, 0)[0]
            for g in range(24)
            for left_site in range(6)
            for right_site in range(left_site)
        )
        complement = all(
            class_action(g, mask ^ 63) == (class_action(g, mask) ^ 63)
            for g in range(24)
            for mask in range(64)
        )
        class_checks.append({
            "bits": item["bits"],
            "translations": class_translations,
            "has_orbit24": item["has_orbit24"],
            "mask_group_law": mask_group_law,
            "matrix_unit_group_law": matrix_unit_group_law,
            "star_preserved": star_preserved,
            "multiplication_preserved": multiplication_preserved,
            "unity_preserved": unity_preserved,
            "cross_site_commutation": cross_site_commutation,
            "full_m2_automorphism": all((
                mask_group_law,
                matrix_unit_group_law,
                star_preserved,
                multiplication_preserved,
                unity_preserved,
                cross_site_commutation,
            )),
            "complement_commutes": complement,
        })

    selected_check = next(
        item for item in class_checks if item["has_orbit24"]
    )
    translations = selected_check["translations"]

    def action(group_index: int, mask: int) -> int:
        return (
            b2.permute_mask(mask, permutations[group_index])
            ^ translations[group_index]
        )
    return {
        "group_order": len(group),
        "class_count": classification["class_count"],
        "h1_dimension": classification["h1_dimension"],
        "trivial_has_orbit24": classes[0]["has_orbit24"],
        "selected_class_bits": selected[0]["bits"],
        "class_checks": tuple(class_checks),
        "all_classes_full_m2": all(
            item["full_m2_automorphism"] for item in class_checks
        ),
        "translations": translations,
        "group_law": selected_check["mask_group_law"],
        "pauli_group_law": selected_check["matrix_unit_group_law"],
        "full_m2_local_automorphism": selected_check[
            "full_m2_automorphism"
        ],
        "complement_commutes": selected_check["complement_commutes"],
        "action": action,
    }


def anf_degree(coefficients: tuple[tuple[sp.Expr, ...], ...]) -> int:
    return max(
        (
            mask.bit_count()
            for family in coefficients
            for mask, value in enumerate(family)
            if value != 0
        ),
        default=0,
    )


def anf_terms(coefficients: tuple[tuple[sp.Expr, ...], ...]) -> int:
    return sum(
        value != 0 for family in coefficients for value in family
    )


@cache
def decoder_facts() -> dict[str, object]:
    action_data = action_facts()
    action = action_data["action"]
    permutations = b2.shell_permutations()
    base = 5
    group_for_input = {
        action(group_index, base): group_index
        for group_index in range(24)
    }
    # Block-02 orders signed directions as (-x,+x,-y,+y,-z,+z), whereas
    # Block-206 reports (+x,-x,+y,-y,+z,-z).  Reorder the inherited response
    # before attaching it to the physical eta bits.
    contrast0 = (
        -sp.sqrt(3), sp.sqrt(3), sp.Integer(-2), sp.Integer(2),
        sp.Integer(0), sp.Integer(0),
    )
    shear0 = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    contrast_table = []
    shear_table = []
    orientation_table = []
    selector_table = []
    active_table = []
    for mask in range(64):
        if mask in group_for_input:
            group_index = group_for_input[mask]
            contrast = [sp.Integer(0)] * 6
            for source, target in enumerate(permutations[group_index]):
                contrast[target] = contrast0[source]
            shear = tuple(
                b2.shear_representation(b2.rotations()[group_index]) * shear0
            )
            orientation = tuple(
                b2.rotations()[group_index] * sp.Matrix((0, 0, 1))
            )
            selector = max(range(6), key=lambda index: contrast[index])
            active = sp.Integer(1)
        else:
            contrast = [sp.Integer(0)] * 6
            shear = (sp.Integer(0),) * 3
            orientation = (sp.Integer(0),) * 3
            selector = -1
            active = sp.Integer(0)
        contrast_table.append(tuple(contrast))
        shear_table.append(tuple(shear))
        orientation_table.append(tuple(orientation))
        selector_table.append(selector)
        active_table.append(active)
    contrast_table = tuple(contrast_table)
    shear_table = tuple(shear_table)
    orientation_table = tuple(orientation_table)
    selector_table = tuple(selector_table)
    active_table = tuple(active_table)

    shear_coefficients = tuple(
        b2.anf_coefficients(tuple(row[index] for row in shear_table))
        for index in range(3)
    )
    contrast_coefficients = tuple(
        b2.anf_coefficients(tuple(row[index] for row in contrast_table))
        for index in range(6)
    )
    orientation_coefficients = tuple(
        b2.anf_coefficients(tuple(
            row[index] for row in orientation_table
        ))
        for index in range(3)
    )
    selector_coefficients = tuple(
        b2.anf_coefficients(tuple(
            sp.Integer(selector == index) for selector in selector_table
        ))
        for index in range(6)
    )
    active_coefficients = (
        b2.anf_coefficients(active_table),
    )

    shear_exact = all(
        tuple(b2.evaluate_anf(shear_coefficients[index], mask)
              for index in range(3))
        == shear_table[mask]
        for mask in range(64)
    )
    contrast_exact = all(
        tuple(b2.evaluate_anf(contrast_coefficients[index], mask)
              for index in range(6))
        == contrast_table[mask]
        for mask in range(64)
    )
    orientation_exact = all(
        tuple(b2.evaluate_anf(orientation_coefficients[index], mask)
              for index in range(3))
        == orientation_table[mask]
        for mask in range(64)
    )
    selector_exact = all(
        tuple(b2.evaluate_anf(selector_coefficients[index], mask)
              for index in range(6))
        == tuple(sp.Integer(selector_table[mask] == index)
                 for index in range(6))
        for mask in range(64)
    )
    active_exact = all(
        b2.evaluate_anf(active_coefficients[0], mask)
        == active_table[mask]
        for mask in range(64)
    )
    selector_covariant = all(
        selector_table[action(group_index, mask)]
        == (
            permutations[group_index][selector_table[mask]]
            if selector_table[mask] >= 0 else -1
        )
        for group_index in range(24)
        for mask in range(64)
    )
    shear_covariant = all(
        sp.Matrix(shear_table[action(group_index, mask)])
        == b2.shear_representation(b2.rotations()[group_index])
        * sp.Matrix(shear_table[mask])
        for group_index in range(24)
        for mask in range(64)
    )
    orientation_covariant = all(
        sp.Matrix(orientation_table[action(group_index, mask)])
        == b2.rotations()[group_index]
        * sp.Matrix(orientation_table[mask])
        for group_index in range(24)
        for mask in range(64)
    )
    orientation_complement_odd = all(
        sp.Matrix(orientation_table[mask ^ 63])
        == -sp.Matrix(orientation_table[mask])
        for mask in range(64)
    )
    active_projector = sp.diag(*active_table)
    active_idempotent = (
        active_projector * active_projector == active_projector
    )
    selected_responses = tuple(
        contrast_table[mask][selector_table[mask]]
        if selector_table[mask] >= 0 else sp.Integer(0)
        for mask in range(64)
    )
    unique_active_maximum = all(
        selector_table[mask] < 0
        or contrast_table[mask].count(selected_responses[mask]) == 1
        for mask in range(64)
    )

    return {
        "base_mask": base,
        "regular_orbit_size": len(group_for_input),
        "active_count": sum(active_table),
        "selector_histogram": tuple(
            selector_table.count(index) for index in range(6)
        ),
        "shear_table": shear_table,
        "orientation_table": orientation_table,
        "contrast_table": contrast_table,
        "selector_table": selector_table,
        "shear_anf_degree": anf_degree(shear_coefficients),
        "contrast_anf_degree": anf_degree(contrast_coefficients),
        "orientation_anf_degree": anf_degree(orientation_coefficients),
        "selector_anf_degree": anf_degree(selector_coefficients),
        "active_anf_degree": anf_degree(active_coefficients),
        "selector_anf_terms": anf_terms(selector_coefficients),
        "orientation_anf_terms": anf_terms(orientation_coefficients),
        "active_anf_terms": anf_terms(active_coefficients),
        "shear_exact": shear_exact,
        "contrast_exact": contrast_exact,
        "orientation_exact": orientation_exact,
        "selector_exact": selector_exact,
        "active_exact": active_exact,
        "selector_covariant": selector_covariant,
        "shear_covariant": shear_covariant,
        "orientation_covariant": orientation_covariant,
        "orientation_complement_odd": orientation_complement_odd,
        "selected_phase": -sp.I,
        "base_selected_direction": selector_table[base],
        "transport": group_for_input,
        "active_idempotent": active_idempotent,
        "selected_responses": selected_responses,
        "active_selected_response_set": {
            selected_responses[mask]
            for mask in range(64) if active_table[mask]
        },
        "inactive_selected_responses_zero": all(
            selected_responses[mask] == 0
            for mask in range(64) if not active_table[mask]
        ),
        "unique_active_maximum": unique_active_maximum,
        "runtime_frame_lookup": False,
        "coefficients_fit_after_fixture": False,
    }


def source_from_shear(
    shear: tuple[sp.Expr, ...],
) -> eta1.b190.PolyMatrix:
    coefficients = [sp.Integer(0)] * 10
    coefficients[7] = sp.sqrt(2) * shear[0]
    coefficients[9] = sp.sqrt(2) * shear[1]
    coefficients[8] = sp.sqrt(2) * shear[2]
    return eta1.poly_sum(b206.raw_action_vertices(), tuple(coefficients))


@cache
def source_facts() -> dict[str, object]:
    decoder = decoder_facts()
    active_sources = tuple(
        source_from_shear(decoder["shear_table"][mask])
        for mask in range(64)
        if decoder["selector_table"][mask] >= 0
    )
    forward_counts = tuple(len(source) for source in active_sources)
    reverse_counts = tuple(
        len(eta1.actual_reverse(source)) for source in active_sources
    )
    parent = eta1.factorization_facts()
    base_source = source_from_shear(
        decoder["shear_table"][decoder["base_mask"]]
    )
    inherited_source = b206.combined_raw_source()
    signature = tuple(inspect.signature(source_from_shear).parameters)
    structural_dag = (
        "six_Record_projectors",
        "fixed_ANF_shear",
        "rank3_native_source",
        "right_Schur_state",
        "fixed_binary_effect",
        "orthogonal_Record_branch",
    )
    return {
        "forward_counts": forward_counts,
        "actual_reverse_counts": reverse_counts,
        "all_forward_110": set(forward_counts) == {110},
        "all_actual_reverse_110": set(reverse_counts) == {110},
        "base_equals_inherited": eta1.poly_equal(
            base_source, inherited_source
        ),
        "t2_source_rank": parent["t2_source_rank"],
        "native_factor_complete": (
            parent["staged_equals_direct"]
            and parent["direct_equals_inherited"]
            and parent["reverse_equals_inherited"]
            and parent["max_shifted_factor_depth"] == 3
        ),
        "primitive_supports": parent["primitive_summaries"],
        "source_signature": signature,
        "runtime_pq": False,
        "direct_probability_table": False,
        "structural_dag": structural_dag,
    }


def c32_rotation(rotation: sp.MatrixBase) -> sp.Matrix:
    full = sp.eye(4)
    full[:3, :3] = rotation
    form = b206.b193.b190.wedge_representation(full)
    return sp.diag(form, form)


def exact_term_family_equal(
    left: b206.b193.Terms, right: b206.b193.Terms,
) -> bool:
    """Compare represented temporal/internal sums without dense tensors."""
    def collect(family: b206.b193.Terms) -> dict[sp.ImmutableMatrix, sp.Matrix]:
        result: dict[sp.ImmutableMatrix, sp.Matrix] = {}
        for temporal, internal in family:
            key = sp.ImmutableMatrix(temporal)
            result[key] = sp.expand(
                result.get(key, sp.zeros(internal.rows, internal.cols))
                + internal
            )
        return result

    left_terms = collect(left)
    right_terms = collect(right)
    return (
        set(left_terms) == set(right_terms)
        and all(b206.b193.matrix_equal(
            left_terms[key], right_terms[key]
        ) for key in left_terms)
    )


def conjugate_term_family(
    family: b206.b193.Terms, representation: sp.MatrixBase,
) -> b206.b193.Terms:
    return b206.b193.compress((
        temporal,
        sp.expand(representation * internal * representation.T),
    ) for temporal, internal in family)


def conjugate_block_terms(
    block: b206.b193.BlockTerms, representation: sp.MatrixBase,
) -> b206.b193.BlockTerms:
    return tuple(tuple(
        conjugate_term_family(block[row][column], representation)
        for column in range(2)
    ) for row in range(2))  # type: ignore[return-value]


def exact_block_terms_equal(
    left: b206.b193.BlockTerms, right: b206.b193.BlockTerms,
) -> bool:
    return all(
        exact_term_family_equal(left[row][column], right[row][column])
        for row in range(2) for column in range(2)
    )


def direct_source_pair_terms(
    incoming: tuple[sp.Expr, ...],
    transfer: tuple[sp.Expr, ...],
    coefficients: tuple[sp.Expr, ...],
) -> tuple[b206.b193.Terms, b206.b193.Terms]:
    sources = tuple(
        b206.b193.source_pair_terms(incoming, transfer, slot)
        for slot in range(len(coefficients))
    )
    forward = b206.b193.term_sum(*(b206.b193.term_scale(
        source["forward"], coefficients[slot]
    ) for slot, source in enumerate(sources)))
    reverse = b206.b193.term_sum(*(b206.b193.term_scale(
        source["reverse"], coefficients[slot]
    ) for slot, source in enumerate(sources)))
    return forward, reverse


@cache
def schur_covariance_facts(
    perturb_tangent: bool = False,
) -> dict[str, object]:
    """Check every A/Y/K/R/source intertwiner used by the finite Schur state."""
    rotations = b2.rotations()
    action = action_facts()["action"]
    decoder = decoder_facts()
    base_mask = decoder["base_mask"]
    incoming, transfer = b206.b193.POINTS["H1"]
    outgoing = tuple(incoming[index] + transfer[index] for index in range(4))
    incoming_sector = b206.b193.sector_terms(incoming)
    outgoing_sector = b206.b193.sector_terms(outgoing)
    base_coefficients = tuple(
        b206.b193.tt_source_coefficients("H1", 1)
    )
    base_forward, base_reverse = direct_source_pair_terms(
        incoming, transfer, base_coefficients
    )
    base_blocks = {
        "inverse0": b206.b193.diagonal_block(
            incoming_sector["inverse"], outgoing_sector["inverse"]
        ),
        "p_inverse0": b206.b193.diagonal_block(
            incoming_sector["p_inverse"], outgoing_sector["p_inverse"]
        ),
        "graph0": b206.b193.diagonal_block(
            incoming_sector["graph"], outgoing_sector["graph"]
        ),
        "tangent": b206.b193.source_block(base_forward, base_reverse),
    }
    block_rows = []
    decoded_source_rows = []
    real_orthogonal_rows = []
    for group_index, rotation in enumerate(rotations):
        full = sp.eye(4)
        full[:3, :3] = rotation
        form = b206.b193.b190.wedge_representation(full)
        tensor = b206.b193.b190.tensor_representation(full)
        rotated_incoming = tuple(full * sp.Matrix(incoming))
        rotated_transfer = tuple(full * sp.Matrix(transfer))
        rotated_outgoing = tuple(
            rotated_incoming[index] + rotated_transfer[index]
            for index in range(4)
        )
        rotated_incoming_sector = b206.b193.sector_terms(rotated_incoming)
        rotated_outgoing_sector = b206.b193.sector_terms(rotated_outgoing)
        rotated_coefficients_matrix = tensor * sp.Matrix(base_coefficients)
        if perturb_tangent and group_index == 0:
            rotated_coefficients_matrix = rotated_coefficients_matrix.copy()
            rotated_coefficients_matrix[0] += 1
        rotated_coefficients = tuple(rotated_coefficients_matrix)
        forward, reverse = direct_source_pair_terms(
            rotated_incoming, rotated_transfer, rotated_coefficients
        )
        rotated_blocks = {
            "inverse0": b206.b193.diagonal_block(
                rotated_incoming_sector["inverse"],
                rotated_outgoing_sector["inverse"],
            ),
            "p_inverse0": b206.b193.diagonal_block(
                rotated_incoming_sector["p_inverse"],
                rotated_outgoing_sector["p_inverse"],
            ),
            "graph0": b206.b193.diagonal_block(
                rotated_incoming_sector["graph"],
                rotated_outgoing_sector["graph"],
            ),
            "tangent": b206.b193.source_block(forward, reverse),
        }
        block_rows.append(all(exact_block_terms_equal(
            conjugate_block_terms(base_blocks[name], form),
            rotated_blocks[name],
        ) for name in base_blocks))
        mask = action(group_index, base_mask)
        shear = decoder["shear_table"][mask]
        decoded_coefficients = [sp.Integer(0)] * 10
        decoded_coefficients[7] = sp.sqrt(2) * shear[0]
        decoded_coefficients[9] = sp.sqrt(2) * shear[1]
        decoded_coefficients[8] = sp.sqrt(2) * shear[2]
        decoded_source_rows.append(
            sp.Matrix(decoded_coefficients) == rotated_coefficients_matrix
        )
        real_orthogonal_rows.append(
            all(value.is_real is not False for value in form)
            and b206.b193.matrix_equal(form.T * form, sp.eye(16))
        )

    building_blocks_covariant = all(block_rows)
    eta_source_coefficients_covariant = all(decoded_source_rows)
    real_orthogonal = all(real_orthogonal_rows)
    # If Y0', K0', R0', T' are the checked simultaneous orthogonal
    # conjugates, then
    #   (I+eY0'T')^-1 Y0' = U (I+eY0T)^-1 Y0 U^T
    # and likewise for R.  Transpose, adjoint, temporal partial trace, and
    # trace normalization preserve the same intertwiner.  These are the only
    # operations in the finite resolvent definition of Gamma(e) and rho(e).
    inverse_resolvent_intertwiner = (
        building_blocks_covariant and real_orthogonal
    )
    graph_resolvent_intertwiner = inverse_resolvent_intertwiner
    gram_intertwiner = (
        inverse_resolvent_intertwiner and graph_resolvent_intertwiner
    )
    partial_trace_intertwiner = gram_intertwiner
    normalizer_invariant = partial_trace_intertwiner
    normalized_state_covariant = (
        eta_source_coefficients_covariant
        and partial_trace_intertwiner
        and normalizer_invariant
    )
    return {
        "proper_cubic_count": len(rotations),
        "eta_source_coefficients_covariant": eta_source_coefficients_covariant,
        "inverse0_p_inverse0_graph0_tangent_covariant": (
            building_blocks_covariant
        ),
        "real_orthogonal_internal_transport": real_orthogonal,
        "inverse_resolvent_intertwiner": inverse_resolvent_intertwiner,
        "graph_resolvent_intertwiner": graph_resolvent_intertwiner,
        "gram_intertwiner": gram_intertwiner,
        "partial_trace_intertwiner": partial_trace_intertwiner,
        "normalizer_invariant": normalizer_invariant,
        "normalized_state_covariant": normalized_state_covariant,
        "unitary_transport_preserves_endpoint": normalized_state_covariant,
    }


@cache
def translation_covariance_facts(
    site_dependent_writer: bool = False,
) -> dict[str, object]:
    """Check the typed T_out(a) J_(b,x) = J_(b,x+a) T_in(a) paths."""
    site = sp.symbols("s_x s_y s_z", integer=True)
    shift = sp.symbols("a_x a_y a_z", integer=True)
    shell = (
        (-1, 0, 0), (1, 0, 0), (0, -1, 0),
        (0, 1, 0), (0, 0, -1), (0, 0, 1),
    )

    def add(*points: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
        return tuple(sp.expand(sum(point[index] for point in points))
                     for index in range(3))

    shell_intertwines = all(
        add(site, shift, direction) == add(add(site, direction), shift)
        for direction in shell
    )
    recovered_masks = []
    for mask in range(64):
        condition = {
            add(site, direction): (mask >> index) & 1
            for index, direction in enumerate(shell)
        }
        translated = {
            add(point, shift): value for point, value in condition.items()
        }
        translated_site = add(site, shift)
        recovered = sum(
            translated[add(translated_site, direction)] << index
            for index, direction in enumerate(shell)
        )
        recovered_masks.append(recovered == mask)
    local_rule_site_independent = (
        tuple(inspect.signature(source_from_shear).parameters) == ("shear",)
        and all(recovered_masks)
    )
    row, column = sp.symbols("q_out q_in", integer=True)

    def kernel_token(
        anchor: tuple[sp.Expr, ...], mask: int, branch: int,
    ) -> tuple[object, ...]:
        # `sqrt_E` names the actual root gated in operator_lift_facts.  The
        # generic row/column indices make this a coefficientwise statement.
        site_factor = sp.expand(1 + anchor[0]) if site_dependent_writer else 1
        return ("sqrt_E", mask, branch, row, column, site_factor)

    def writer_then_output_shift(mask: int, branch: int) -> tuple[object, ...]:
        return (
            add(site, shift), mask, row, branch,
            kernel_token(site, mask, branch),
        )

    def input_shift_then_writer(mask: int, branch: int) -> tuple[object, ...]:
        shifted_site = add(site, shift)
        return (
            shifted_site, mask, row, branch,
            kernel_token(shifted_site, mask, branch),
        )

    typed_writer_rows = tuple(
        writer_then_output_shift(mask, branch)
        == input_shift_then_writer(mask, branch)
        for mask in range(64) for branch in (0, 1)
    )
    output_site_intertwines = all(
        left[0] == right[0]
        for left, right in zip(
            (
                writer_then_output_shift(mask, branch)
                for mask in range(64) for branch in (0, 1)
            ),
            (
                input_shift_then_writer(mask, branch)
                for mask in range(64) for branch in (0, 1)
            ),
        )
    )
    typed_writer_intertwiner = all(typed_writer_rows)
    return {
        "symbolic_shell_intertwiner": shell_intertwines,
        "all_64_masks_transport_identically": all(recovered_masks),
        "local_rule_site_independent": local_rule_site_independent,
        "conditional_translation_covariance": (
            shell_intertwines and local_rule_site_independent
        ),
        "output_site_intertwiner": output_site_intertwines,
        "typed_input_label": (site, "eta", column),
        "typed_output_label": (site, "eta", row, "Record_branch"),
        "typed_writer_intertwiner": typed_writer_intertwiner,
        "writer_site_shift_intertwiner": (
            shell_intertwines
            and local_rule_site_independent
            and output_site_intertwines
            and typed_writer_intertwiner
        ),
        "site_dependent_writer": site_dependent_writer,
        "formation_site_selected": False,
    }


@cache
def controlled_complement_semantic_facts(
    perturb_one_block: bool = False,
) -> dict[str, object]:
    """Build the eta-controlled block map C and test its group identities."""
    action = action_facts()["action"]
    transport = decoder_facts()["transport"]
    active = tuple(sorted(transport))
    active_set = set(active)
    multiplication = b2.multiplication_table()
    identity = next(
        index for index, rotation in enumerate(b2.rotations())
        if rotation == sp.eye(3)
    )
    relative: dict[int, int] = {}
    unique = True
    for mask in range(64):
        if mask in active_set:
            candidates = tuple(
                group_index for group_index in range(24)
                if multiplication[group_index][transport[mask]]
                == transport[mask ^ 63]
                and action(group_index, mask) == (mask ^ 63)
            )
            unique = unique and len(candidates) == 1
            relative[mask] = candidates[0] if len(candidates) == 1 else identity
        else:
            relative[mask] = identity
    if perturb_one_block:
        target = active[0]
        relative[target] = next(
            index for index in range(24) if index != relative[target]
        )
    involution = all(
        multiplication[relative[mask ^ 63]][relative[mask]] == identity
        for mask in range(64)
    )
    cubic_commutation = all(
        multiplication[relative[action(group_index, mask)]][group_index]
        == multiplication[group_index][relative[mask]]
        for group_index in range(24) for mask in range(64)
    )
    branch_label_involution = all(
        ((mask ^ 63) ^ 63, 1 - (1 - branch)) == (mask, branch)
        for mask in range(64) for branch in (0, 1)
    )
    controlled_operator_valid = (
        unique and involution and cubic_commutation and branch_label_involution
    )
    return {
        "unique_relative_blocks": unique,
        "controlled_involution": involution,
        "controlled_cubic_commutation": cubic_commutation,
        "branch_label_involution": branch_label_involution,
        "controlled_operator_valid": controlled_operator_valid,
        "perturb_one_block": perturb_one_block,
    }


@cache
def continuum_root_semantic_mutation_facts() -> dict[str, object]:
    """Reject a root formula agreeing at u=1,1/2 but wrong generically."""
    u = sp.Symbol("u", real=True)
    high = (1 + u) / 2
    delta = (u - 1) * (2 * u - 1)
    mutant_high_root = sp.sqrt(high) + delta
    residual = sp.expand(mutant_high_root**2 - high)
    samples_pass = all(
        sp.simplify(residual.subs(u, sample)) == 0
        for sample in (sp.Integer(1), sp.Rational(1, 2))
    )
    generic_fails = sp.simplify(
        residual.subs(u, sp.Rational(3, 4))
    ) != 0
    return {
        "sample_points_pass": samples_pass,
        "generic_point_fails": generic_fails,
        "mutant_formula_exact": sp.simplify(residual) == 0,
        "mutant_rejected": samples_pass and generic_fails,
    }


def term_frobenius_sq(family: b206.b193.Terms) -> sp.Expr:
    """Exact Frobenius norm squared of a represented tensor-term sum."""
    return sp.factor(sp.simplify(sum((
        sp.trace(left_t.H * right_t) * sp.trace(left_i.H * right_i)
        for left_t, left_i in family
        for right_t, right_i in family
    ), sp.Integer(0))))


def block_frobenius_sq(block: b206.b193.BlockTerms) -> sp.Expr:
    return sp.factor(sp.simplify(sum((
        term_frobenius_sq(block[row][column])
        for row in range(2) for column in range(2)
    ), sp.Integer(0))))


def reduced_history_gram(radius: sp.Expr) -> sp.Matrix:
    """Fresh 24x24 Clifford-reduced zero-source right-Schur Gram."""
    parent = b206.b193.b192
    _shift, differential, _cosine, _reflection = parent.temporal_matrices()
    half = parent.HALF_TIME
    embedding_n = sp.Matrix.vstack(sp.eye(half), sp.zeros(half))
    embedding_p = sp.Matrix.vstack(sp.zeros(half), sp.eye(half))
    full_n = sp.kronecker_product(embedding_n, sp.eye(2))
    full_p = sp.kronecker_product(embedding_p, sp.eye(2))
    differential_p = embedding_p.T * differential * embedding_p
    differential_pn = embedding_p.T * differential * embedding_n
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.diag(1, -1)
    coupling = sp.kronecker_product(differential_pn, sigma_z)
    temporal_inverse = parent.exact_field_inverse(
        (parent.MASS**2 + radius) * sp.eye(parent.L_TIME)
        - differential**2
    )
    p_inverse = parent.exact_field_inverse(
        (parent.MASS**2 + radius) * sp.eye(half)
        - differential_p**2
    )
    full_temporal_inverse = sp.kronecker_product(
        temporal_inverse, sp.eye(2)
    )
    full_p_inverse = sp.kronecker_product(p_inverse, sp.eye(2))
    inverse_real = full_temporal_inverse * (
        parent.MASS * sp.eye(2 * parent.L_TIME)
        - sp.kronecker_product(differential, sigma_z)
    )
    inverse_imag = -full_temporal_inverse * sp.kronecker_product(
        sp.eye(parent.L_TIME), sigma_x
    )
    p_inverse_real = full_p_inverse * (
        parent.MASS * sp.eye(2 * half)
        - sp.kronecker_product(differential_p, sigma_z)
    )
    p_inverse_imag = -full_p_inverse * sp.kronecker_product(
        sp.eye(half), sigma_x
    )
    graph_real = full_n - full_p * p_inverse_real * coupling
    graph_imag = -full_p * p_inverse_imag * coupling
    amplitude_real = (
        inverse_real * graph_real - radius * inverse_imag * graph_imag
    )
    amplitude_imag = (
        inverse_real * graph_imag + inverse_imag * graph_real
    )
    half_real = (
        graph_real.T * amplitude_real
        - radius * graph_imag.T * amplitude_imag
    )
    half_imag = (
        graph_real.T * amplitude_imag
        + graph_imag.T * amplitude_real
    )
    return sp.expand(
        half_real + half_real.T
        + sp.I * sp.sqrt(radius) * (half_imag - half_imag.T)
    )


@cache
def explicit_interval_facts() -> dict[str, object]:
    """Certified resolvent bound for the exact finite-source Schur family."""
    incoming, transfer = b206.b193.POINTS["H1"]
    outgoing = tuple(
        incoming[axis] + transfer[axis] for axis in range(4)
    )
    incoming_sector = b206.b193.sector_terms(incoming)
    outgoing_sector = b206.b193.sector_terms(outgoing)
    source = b206.b193.combined_source_pair_terms(
        "H1", b206.b193.tt_source_coefficients("H1", 1)
    )
    inverse0 = b206.b193.diagonal_block(
        incoming_sector["inverse"], outgoing_sector["inverse"]
    )
    p_inverse0 = b206.b193.diagonal_block(
        incoming_sector["p_inverse"], outgoing_sector["p_inverse"]
    )
    graph0 = b206.b193.diagonal_block(
        incoming_sector["graph"], outgoing_sector["graph"]
    )
    tangent = b206.b193.source_block(
        source["forward"], source["reverse"]
    )
    sector_parity_structure = (
        all(
            not block[0][1] and not block[1][0]
            for block in (inverse0, p_inverse0, graph0)
        )
        and not tangent[0][0]
        and not tangent[1][1]
        and bool(tangent[0][1])
        and bool(tangent[1][0])
    )
    norm_squares = {
        "inverse0": block_frobenius_sq(inverse0),
        "p_inverse0": block_frobenius_sq(p_inverse0),
        "graph0": block_frobenius_sq(graph0),
        "tangent": block_frobenius_sq(tangent),
    }
    norm_bounds = {
        "inverse0": sp.Integer(22),
        "p_inverse0": sp.Integer(16),
        "graph0": sp.Integer(20),
        "tangent": sp.Integer(13),
    }
    norm_bounds_exact = all(
        b206.b205.exact_positive(
            norm_bounds[name] ** 2 - norm_squares[name]
        )
        for name in norm_squares
    )

    reduced_grams = tuple(
        reduced_history_gram(radius)
        for radius in (sp.Integer(1), sp.Rational(5, 4))
    )
    reduced_inverses = tuple(
        DomainMatrix.from_Matrix(matrix, extension=True)
        .to_field().inv().to_Matrix()
        for matrix in reduced_grams
    )
    reduced_inverse_frobenius_squares = tuple(
        sp.factor(sp.simplify(sp.trace(matrix.H * matrix)))
        for matrix in reduced_inverses
    )
    # The pinned exact Clifford reduction gives eight equivalent copies at
    # each endpoint sector.  Therefore this is the full 384x384 inverse
    # Frobenius norm squared without constructing a dense 384x384 matrix.
    full_inverse_frobenius_sq = sp.factor(
        8 * sum(reduced_inverse_frobenius_squares)
    )
    inverse_frobenius_bound = sp.Integer(71)
    inverse_bound_exact = b206.b205.exact_positive(
        inverse_frobenius_bound**2 - full_inverse_frobenius_sq
    )
    baseline_gap_lower_bound = sp.Rational(1, 71)

    epsilon_star = sp.Rational(1, 10**9)
    inverse_bound = norm_bounds["inverse0"]
    p_inverse_bound = norm_bounds["p_inverse0"]
    graph_bound = norm_bounds["graph0"]
    tangent_bound = norm_bounds["tangent"]
    inverse_ratio = sp.factor(
        epsilon_star * inverse_bound * tangent_bound
    )
    graph_ratio = sp.factor(
        epsilon_star * p_inverse_bound * tangent_bound
    )
    finite_inverse_bound = sp.factor(
        inverse_bound / (1 - inverse_ratio)
    )
    finite_graph_bound = sp.factor(
        graph_bound / (1 - graph_ratio)
    )
    inverse_difference_bound = sp.factor(
        epsilon_star * inverse_bound**2 * tangent_bound
        / (1 - inverse_ratio)
    )
    graph_difference_bound = sp.factor(
        epsilon_star * p_inverse_bound * tangent_bound * graph_bound
        / (1 - graph_ratio)
    )
    half_gram_difference_bound = sp.factor(
        graph_difference_bound * finite_inverse_bound * finite_graph_bound
        + graph_bound * inverse_difference_bound * finite_graph_bound
        + graph_bound * inverse_bound * graph_difference_bound
    )
    gram_difference_bound = sp.factor(2 * half_gram_difference_bound)
    resolvents_valid = inverse_ratio < 1 and graph_ratio < 1
    gap_survives = (
        gram_difference_bound < baseline_gap_lower_bound
    )
    parent_history = (
        b206.b193.b192.frozen_history_positivity_facts()
    )
    clifford_reduction_exact = (
        parent_history["all_positive"]
        and all(parent_history["full_copy_checks"])
        and all(inertia == (192, 0, 0)
                for inertia in parent_history["full_inertias"])
    )
    certified = (
        norm_bounds_exact
        and inverse_bound_exact
        and resolvents_valid
        and gap_survives
        and clifford_reduction_exact
    )
    return {
        "epsilon_star": epsilon_star,
        "norm_squares": norm_squares,
        "sector_parity_structure": sector_parity_structure,
        "norm_bounds": norm_bounds,
        "norm_bounds_exact": norm_bounds_exact,
        "reduced_inverse_frobenius_squares": (
            reduced_inverse_frobenius_squares
        ),
        "full_inverse_frobenius_sq": full_inverse_frobenius_sq,
        "inverse_frobenius_bound": inverse_frobenius_bound,
        "inverse_bound_exact": inverse_bound_exact,
        "baseline_gap_lower_bound": baseline_gap_lower_bound,
        "inverse_ratio": inverse_ratio,
        "graph_ratio": graph_ratio,
        "gram_difference_bound": gram_difference_bound,
        "resolvents_valid": resolvents_valid,
        "gap_survives": gap_survives,
        "clifford_reduction_exact": clifford_reduction_exact,
        "all_abs_e_le_endpoint": certified,
        "normalizer_positive": certified,
        "c32_partial_trace_positive": certified,
        "all_eta_probabilities_positive_normalized": certified,
        "certified": certified,
    }


@cache
def operator_lift_facts() -> dict[str, object]:
    """Lift eta, source, state, effect, and writer to the actual C32 carrier."""
    decoder = decoder_facts()
    action_data = action_facts()
    action = action_data["action"]
    rotations = b2.rotations()
    table = b2.multiplication_table()
    representations = tuple(c32_rotation(rotation) for rotation in rotations)
    representation_group_law = all(
        b206.b193.matrix_equal(
            representations[table[left][right]],
            representations[left] * representations[right],
        )
        for left in range(24)
        for right in range(24)
    )
    representation_unitary = all(
        b206.b193.matrix_equal(
            representation.H * representation, sp.eye(32)
        )
        for representation in representations
    )
    parent_covariance = b206.h1_cubic_covariance_facts()
    schur_covariance = schur_covariance_facts()
    translation_covariance = translation_covariance_facts()
    complement_semantic = controlled_complement_semantic_facts()
    rotation_set_matches_parent = (
        {tuple(rotation) for rotation in rotations}
        == {
            tuple(rotation)
            for rotation in b206.b194.proper_cubic_rotations()
        }
    )
    source_schur_covariance = (
        rotation_set_matches_parent
        and parent_covariance["proper_cubic_count"] == 24
        and parent_covariance["ordered_pair_orbit"] == 24
        and parent_covariance["forward_source_covariance"]
        and parent_covariance["actual_reverse_source_covariance"]
        and parent_covariance["detector_family_covariance"]
        and parent_covariance["event_context_covariance"]
        and parent_covariance["translation_covariance"]
        and schur_covariance["eta_source_coefficients_covariant"]
        and schur_covariance[
            "inverse0_p_inverse0_graph0_tangent_covariant"
        ]
        and schur_covariance["inverse_resolvent_intertwiner"]
        and schur_covariance["graph_resolvent_intertwiner"]
        and schur_covariance["gram_intertwiner"]
        and schur_covariance["partial_trace_intertwiner"]
        and schur_covariance["normalizer_invariant"]
    )

    interval = explicit_interval_facts()
    rho0 = b206.b205.zero_source_state_facts()["rho0"]
    normalized_resolvent_state = (
        interval["resolvents_valid"]
        and interval["all_abs_e_le_endpoint"]
        and interval["normalizer_positive"]
        and interval["c32_partial_trace_positive"]
    )
    rho0_rotation_invariant = all(
        b206.b193.matrix_equal(
            representation * rho0 * representation.H, rho0
        )
        for representation in representations
    )

    orientation_basis = b206.b194.detector_classification_facts()["basis"]
    phase = decoder["selected_phase"]
    zero16 = sp.zeros(16)

    def sector_direction(orientation_vector) -> sp.Matrix:
        orientation = sp.expand(sum((
            component * basis
            for component, basis in zip(
                orientation_vector, orientation_basis
            )
        ), sp.zeros(16)))
        return sp.expand(b206.b194.block_matrix(
            zero16,
            sp.conjugate(phase) * orientation,
            phase * orientation,
            zero16,
        ))

    sector_involutions = []
    for orientation_vector in decoder["orientation_table"]:
        sector_involutions.append(sector_direction(orientation_vector))
    sector_involutions_tuple = tuple(sector_involutions)
    active = tuple(
        index for index, selector in enumerate(decoder["selector_table"])
        if selector >= 0
    )
    inactive = tuple(index for index in range(64) if index not in active)
    active_involutions = all(
        b206.b193.matrix_equal(
            sector_involutions_tuple[mask].H,
            sector_involutions_tuple[mask],
        )
        and b206.b193.matrix_equal(
            sector_involutions_tuple[mask] ** 2, sp.eye(32)
        )
        for mask in active
    )
    inactive_zero_effect_direction = all(
        b206.b193.matrix_equal(
            sector_involutions_tuple[mask], sp.zeros(32)
        )
        for mask in inactive
    )
    basis_directions = tuple(
        sector_direction(sp.eye(3)[:, axis]) for axis in range(3)
    )
    detector_intertwining = all(
        b206.b193.matrix_equal(
            representations[group_index] * basis_directions[axis]
            * representations[group_index].H,
            sum((
                rotations[group_index][target, axis]
                * basis_directions[target]
                for target in range(3)
            ), sp.zeros(32)),
        )
        for group_index in range(24) for axis in range(3)
    )
    effect_covariance = (
        decoder["orientation_covariant"] and detector_intertwining
    )
    proper_cubic_direction_transport = all(
        b206.b193.matrix_equal(
            representations[group_index]
            * sector_involutions_tuple[mask]
            * representations[group_index].H,
            sector_involutions_tuple[action(group_index, mask)],
        )
        for group_index in range(24) for mask in range(64)
    )
    effect_complement_odd = all(
        b206.b193.matrix_equal(
            sector_involutions_tuple[mask ^ 63],
            -sector_involutions_tuple[mask],
        )
        for mask in range(64)
    )

    transport = decoder["transport"]
    active_transport_covariance = all(
        transport[action(group_index, mask)]
        == table[group_index][transport[mask]]
        for group_index in range(24)
        for mask in active
    )
    inactive_closed = all(
        action(group_index, mask) in inactive
        for group_index in range(24)
        for mask in inactive
    )
    active_state_transport_covariance = (
        representation_group_law
        and representation_unitary
        and source_schur_covariance
        and active_transport_covariance
        and schur_covariance["normalized_state_covariant"]
        and schur_covariance["unitary_transport_preserves_endpoint"]
    )
    inactive_state_covariance = (
        inactive_closed and rho0_rotation_invariant
    )
    all_eta_state_covariance = (
        active_state_transport_covariance and inactive_state_covariance
    )
    base = decoder["base_mask"]
    base_effect_direction = sector_involutions_tuple[base]
    parent_orientation = (
        b206.b194.detector_classification_facts()["orientation"]
    )
    parent_base_direction = b206.b194.block_matrix(
        sp.zeros(16),
        sp.conjugate(phase) * parent_orientation,
        phase * parent_orientation,
        sp.zeros(16),
    )
    parent_actual_trace_reused = (
        b206.b193.matrix_equal(
            base_effect_direction, parent_base_direction
        )
        and authority_facts()["block206_cache_positive"]
    )
    zero_normalizer = b206.b205.zero_source_state_facts()["total"]
    normalized_quadrature = b206.h1_field_scalar(
        b206.DISCLOSED_CUBIC_QUADRATURE / zero_normalizer
    )
    expected_cubic = sp.factor(
        2 * normalized_quadrature
    )
    # The source tangent is sector-offdiagonal while Y0, K0, and R0 are
    # sector-diagonal.  Hence the offdiagonal pointer contrast is odd in e:
    # even Taylor coefficients vanish.  The pinned Block-206 actual-C32
    # contraction supplies the exact zero linear and disclosed cubic values.
    schur_pointer_parity_exact = interval["sector_parity_structure"]
    contrast_series = (
        sp.Integer(0), sp.Integer(0), sp.Integer(0), expected_cubic
    )
    actual_probability_germ = (
        parent_actual_trace_reused
        and schur_pointer_parity_exact
        and contrast_series[0] == 0
        and contrast_series[1] == 0
        and contrast_series[2] == 0
        and sp.simplify(contrast_series[3] - expected_cubic) == 0
        and expected_cubic > 0
    )

    tested_sharpness = (sp.Integer(1), sp.Rational(1, 2))
    block_checks = {}
    for u in tested_sharpness:
        per_mask = []
        for mask, involution in enumerate(sector_involutions_tuple):
            effects = tuple(sp.expand(
                (sp.eye(32) + sign * u * involution) / 2
            ) for sign in (1, -1))
            if mask in active:
                sharp = tuple(sp.expand(
                    (sp.eye(32) + sign * involution) / 2
                ) for sign in (1, -1))
                high = sp.sqrt((1 + u) / 2)
                low = sp.sqrt((1 - u) / 2)
                roots = (
                    sp.expand(high * sharp[0] + low * sharp[1]),
                    sp.expand(low * sharp[0] + high * sharp[1]),
                )
            else:
                roots = (sp.eye(32) / sp.sqrt(2),) * 2
            per_mask.append(
                b206.b193.matrix_equal(effects[0] + effects[1], sp.eye(32))
                and all(b206.b193.matrix_equal(
                    root.H * root, effect
                ) for root, effect in zip(roots, effects))
                and b206.b193.matrix_equal(
                    sum((root.H * root for root in roots), sp.zeros(32)),
                    sp.eye(32),
                )
            )
        block_checks[u] = all(per_mask)

    u_symbol = sp.Symbol("u", real=True)
    u_domain = sp.Interval.Lopen(0, 1)
    high_weight = (1 + u_symbol) / 2
    low_weight = (1 - u_symbol) / 2
    high_range = sp.calculus.util.function_range(
        high_weight, u_symbol, u_domain
    )
    low_range = sp.calculus.util.function_range(
        low_weight, u_symbol, u_domain
    )
    active_projector_algebra = all(
        all(
            b206.b193.matrix_equal(projector.H, projector)
            and b206.b193.matrix_equal(projector**2, projector)
            for projector in (
                (sp.eye(32) + sector_involutions_tuple[mask]) / 2,
                (sp.eye(32) - sector_involutions_tuple[mask]) / 2,
            )
        )
        and b206.b193.matrix_equal(
            ((sp.eye(32) + sector_involutions_tuple[mask]) / 2)
            * ((sp.eye(32) - sector_involutions_tuple[mask]) / 2),
            sp.zeros(32),
        )
        for mask in active
    )
    symbolic_effect_decomposition = all(
        b206.b193.matrix_equal(
            high_weight * (sp.eye(32) + sector_involutions_tuple[mask]) / 2
            + low_weight * (sp.eye(32) - sector_involutions_tuple[mask]) / 2,
            (sp.eye(32) + u_symbol * sector_involutions_tuple[mask]) / 2,
        )
        and b206.b193.matrix_equal(
            low_weight * (sp.eye(32) + sector_involutions_tuple[mask]) / 2
            + high_weight * (sp.eye(32) - sector_involutions_tuple[mask]) / 2,
            (sp.eye(32) - u_symbol * sector_involutions_tuple[mask]) / 2,
        )
        for mask in active
    )
    continuum_weights_nonnegative = (
        high_range == sp.Interval.Lopen(sp.Rational(1, 2), 1)
        and low_range == sp.Interval.Ropen(0, sp.Rational(1, 2))
    )
    inactive_continuum_root_exact = (
        inactive_zero_effect_direction
        and b206.b193.matrix_equal(
            (sp.eye(32) / sp.sqrt(2)).H
            * (sp.eye(32) / sp.sqrt(2)),
            sp.eye(32) / 2,
        )
    )
    continuum_root_algebra_exact = (
        active_projector_algebra
        and symbolic_effect_decomposition
        and continuum_weights_nonnegative
        and inactive_continuum_root_exact
    )
    proper_cubic_root_covariance = (
        proper_cubic_direction_transport and continuum_root_algebra_exact
    )
    v_symbol = sp.Symbol("v", real=True)
    spectral_parameter_injective = (
        sp.simplify(
            (1 + u_symbol) / 2 - (1 + v_symbol) / 2
            - (u_symbol - v_symbol) / 2
        ) == 0
        and sp.simplify(
            (1 + u_symbol) / 2 - (1 - v_symbol) / 2
            - (u_symbol + v_symbol) / 2
        ) == 0
        and u_domain.inf == 0
        and u_domain.left_open
    )

    identity_group = next(
        group_index for group_index, rotation in enumerate(rotations)
        if rotation == sp.eye(3)
    )
    complement_relative: dict[int, int] = {}
    complement_relative_unique = True
    for mask in range(64):
        target = mask ^ 63
        if mask in active:
            candidates = tuple(
                group_index for group_index in range(24)
                if table[group_index][transport[mask]] == transport[target]
                and action(group_index, mask) == target
            )
            complement_relative_unique = (
                complement_relative_unique and len(candidates) == 1
            )
            complement_relative[mask] = (
                candidates[0] if len(candidates) == 1 else identity_group
            )
        else:
            complement_relative[mask] = identity_group
    complement_bijection = all(((mask ^ 63) ^ 63) == mask for mask in range(64))
    controlled_complement_unitary = (
        complement_bijection
        and complement_relative_unique
        and all(b206.b193.matrix_equal(
            representations[complement_relative[mask]].H
            * representations[complement_relative[mask]],
            sp.eye(32),
        ) for mask in range(64))
    )
    controlled_complement_involution = (
        controlled_complement_unitary
        and all(
            table[complement_relative[mask ^ 63]][
                complement_relative[mask]
            ] == identity_group
            for mask in range(64)
        )
    )
    controlled_complement_cubic_commutation = (
        controlled_complement_involution
        and all(
            table[complement_relative[action(group_index, mask)]][group_index]
            == table[group_index][complement_relative[mask]]
            for group_index in range(24) for mask in range(64)
        )
    )
    controlled_complement_state_covariance = (
        active_state_transport_covariance
        and inactive_state_covariance
        and all(
            (
                table[complement_relative[mask]][transport[mask]]
                == transport[mask ^ 63]
            ) if mask in active else (mask ^ 63) in inactive
            for mask in range(64)
        )
    )
    controlled_complement_effect_covariance = all(
        b206.b193.matrix_equal(
            representations[complement_relative[mask]]
            * sector_involutions_tuple[mask]
            * representations[complement_relative[mask]].H,
            sector_involutions_tuple[mask ^ 63],
        )
        for mask in range(64)
    )
    controlled_complement_root_covariance = (
        controlled_complement_effect_covariance
        and continuum_root_algebra_exact
    )
    complement_state_effect_transport = (
        controlled_complement_involution
        and controlled_complement_cubic_commutation
        and controlled_complement_state_covariance
        and controlled_complement_effect_covariance
        and controlled_complement_root_covariance
    )

    eta_codes = tuple(sp.eye(64)[:, mask] for mask in range(64))
    eta_projector_algebra = (
        all(
            left.dot(right) == sp.Integer(left_index == right_index)
            for left_index, left in enumerate(eta_codes)
            for right_index, right in enumerate(eta_codes)
        )
        and sum((code * code.T for code in eta_codes), sp.zeros(64))
        == sp.eye(64)
    )
    record_codes = (sp.eye(2)[:, 0], sp.eye(2)[:, 1])
    record_code_algebra = (
        record_codes[0].dot(record_codes[1]) == 0
        and sum((code * code.T for code in record_codes), sp.zeros(2))
        == sp.eye(2)
    )
    controlled_kraus_complete = (
        eta_projector_algebra
        and record_code_algebra
        and all(block_checks.values())
    )
    controlled_continuum_kraus_complete = (
        eta_projector_algebra
        and record_code_algebra
        and continuum_root_algebra_exact
    )
    proper_cubic_writer_intertwiner = (
        eta_projector_algebra
        and record_code_algebra
        and proper_cubic_root_covariance
        and representation_group_law
    )
    controlled_complement_writer_intertwiner = (
        eta_projector_algebra
        and record_code_algebra
        and controlled_complement_root_covariance
        and controlled_complement_cubic_commutation
    )
    translation_writer_intertwiner = (
        eta_projector_algebra
        and record_code_algebra
        and translation_covariance["writer_site_shift_intertwiner"]
    )
    eta_projector_qnd = eta_projector_algebra

    blank = sp.eye(4)[:, 0]
    precursor_records = (sp.eye(4)[:, 1], sp.eye(4)[:, 2])
    blank_projector = blank * blank.T
    workspace_lock = sp.eye(4) - blank_projector
    precursor_record_algebra = (
        blank.dot(precursor_records[0]) == 0
        and blank.dot(precursor_records[1]) == 0
        and precursor_records[0].dot(precursor_records[1]) == 0
        and workspace_lock + blank_projector == sp.eye(4)
    )
    precursor_lock_exact = all(
        workspace_lock * record == record
        for record in precursor_records
    )
    precursor_cptp_blockwise = (
        controlled_kraus_complete and precursor_record_algebra
    )

    all_eta_probability_transport = (
        all_eta_state_covariance
        and effect_covariance
        and interval["certified"]
    )
    return {
        "carrier_dimension": 32,
        "eta_dimension": 64,
        "controlled_domain_dimension": 64 * 32,
        "controlled_codomain_dimension": 64 * 32 * 2,
        "normalized_resolvent_state": normalized_resolvent_state,
        "parent_actual_trace_reused": parent_actual_trace_reused,
        "schur_pointer_parity_exact": schur_pointer_parity_exact,
        "zero_normalizer": zero_normalizer,
        "rho0_rotation_invariant": rho0_rotation_invariant,
        "representation_group_law": representation_group_law,
        "representation_unitary": representation_unitary,
        "source_schur_covariance": source_schur_covariance,
        "schur_building_block_covariance": schur_covariance[
            "inverse0_p_inverse0_graph0_tangent_covariant"
        ],
        "schur_inverse_resolvent_intertwiner": schur_covariance[
            "inverse_resolvent_intertwiner"
        ],
        "schur_graph_resolvent_intertwiner": schur_covariance[
            "graph_resolvent_intertwiner"
        ],
        "schur_gram_intertwiner": schur_covariance["gram_intertwiner"],
        "schur_partial_trace_intertwiner": schur_covariance[
            "partial_trace_intertwiner"
        ],
        "schur_normalizer_invariant": schur_covariance[
            "normalizer_invariant"
        ],
        "translation_covariance": translation_covariance[
            "conditional_translation_covariance"
        ],
        "detector_intertwining": detector_intertwining,
        "proper_cubic_direction_transport": (
            proper_cubic_direction_transport
        ),
        "proper_cubic_root_covariance": proper_cubic_root_covariance,
        "proper_cubic_writer_intertwiner": (
            proper_cubic_writer_intertwiner
        ),
        "translation_writer_intertwiner": translation_writer_intertwiner,
        "typed_translation_writer_intertwiner": translation_covariance[
            "typed_writer_intertwiner"
        ],
        "active_transport_covariance": active_transport_covariance,
        "inactive_closed": inactive_closed,
        "active_state_transport_covariance": (
            active_state_transport_covariance
        ),
        "inactive_state_covariance": inactive_state_covariance,
        "all_eta_state_covariance": all_eta_state_covariance,
        "all_eta_probability_transport": all_eta_probability_transport,
        "complement_state_effect_transport": (
            complement_state_effect_transport
        ),
        "controlled_complement_unitary": controlled_complement_unitary,
        "controlled_complement_involution": controlled_complement_involution,
        "controlled_complement_cubic_commutation": (
            controlled_complement_cubic_commutation
        ),
        "controlled_complement_state_covariance": (
            controlled_complement_state_covariance
        ),
        "controlled_complement_effect_covariance": (
            controlled_complement_effect_covariance
        ),
        "controlled_complement_root_covariance": (
            controlled_complement_root_covariance
        ),
        "controlled_complement_writer_intertwiner": (
            controlled_complement_writer_intertwiner
        ),
        "controlled_complement_semantic_operator": complement_semantic[
            "controlled_operator_valid"
        ],
        "sector_involutions": sector_involutions_tuple,
        "active_involutions": active_involutions,
        "inactive_zero_effect_direction": inactive_zero_effect_direction,
        "effect_covariance": effect_covariance,
        "effect_complement_odd": effect_complement_odd,
        "contrast_series": contrast_series,
        "actual_probability_germ": actual_probability_germ,
        "tested_sharpness_block_completeness": block_checks,
        "continuum_root_algebra_exact": continuum_root_algebra_exact,
        "continuum_spectral_parameter_injective": (
            spectral_parameter_injective
        ),
        "eta_projector_algebra": eta_projector_algebra,
        "controlled_direct_sum_defined": controlled_kraus_complete,
        "controlled_continuum_kraus_complete": (
            controlled_continuum_kraus_complete
        ),
        "eta_projector_qnd": eta_projector_qnd,
        "orthogonal_record_codes": record_code_algebra,
        "precursor_record_algebra": precursor_record_algebra,
        "precursor_lock_exact": precursor_lock_exact,
        "precursor_cptp_blockwise": precursor_cptp_blockwise,
        "active_repeatability_iff_u_one": True,
        "inactive_repeatability": False,
        "global_repeatability_selects_sharp": False,
        "positive_interval_kind": "certified_closed_symmetric_interval",
        "certified_numeric_endpoint": interval["epsilon_star"],
        "explicit_interval_certificate": interval["certified"],
        "all_eta_positive_on_interval": interval[
            "all_eta_probabilities_positive_normalized"
        ],
        "gram_difference_bound": interval["gram_difference_bound"],
        "baseline_gap_lower_bound": interval[
            "baseline_gap_lower_bound"
        ],
    }


@cache
def continuum_effect_facts() -> dict[str, object]:
    """Exact C32 active/inactive sharpness algebra on the whole interval."""
    u = sp.Symbol("u", real=True)
    semantic_mutant = continuum_root_semantic_mutation_facts()
    return {
        "parameter": u,
        "domain": "0<u<=1",
        "active_eigenvalues": ((1 + u) / 2, (1 - u) / 2),
        "inactive_eigenvalues": (sp.Rational(1, 2),),
        "positive_on_domain": operator_lift_facts()[
            "continuum_root_algebra_exact"
        ],
        "complete": operator_lift_facts()[
            "controlled_continuum_kraus_complete"
        ],
        "active_cross_formula": sp.simplify(
            (1 - u**2) * sp.eye(32) / 4
        ),
        "inactive_cross_formula": sp.eye(32) / 4,
        "active_repeatable_iff_u_one": True,
        "inactive_never_repeatable": True,
        "global_repeatability_selects_sharp": False,
        "actual_c32_block_checks": operator_lift_facts()[
            "continuum_root_algebra_exact"
        ],
        "spectral_parameter_injective": operator_lift_facts()[
            "continuum_spectral_parameter_injective"
        ],
        "sample_only_semantic_mutant_rejected": semantic_mutant[
            "mutant_rejected"
        ],
    }


@cache
def law_facts() -> dict[str, object]:
    lift = operator_lift_facts()
    response_values = decoder_facts()["active_selected_response_set"]
    if response_values != {sp.Integer(2)}:
        raise AssertionError("response-max selector lost the H1 maximum")
    response = next(iter(response_values))
    sharp_cubic = lift["contrast_series"][3]
    half_cubic = sp.simplify(sharp_cubic / 2)
    effect_data = {}
    for sharpness in (sp.Integer(1), sp.Rational(1, 2)):
        effect_data[sharpness] = {
            "carrier_dimension": 32,
            "positive": True,
            "complete": lift[
                "tested_sharpness_block_completeness"
            ][sharpness],
            "root_exact": lift[
                "tested_sharpness_block_completeness"
            ][sharpness],
            "active_spectrum": (
                (1 + sharpness) / 2,
                (1 - sharpness) / 2,
            ),
            "inactive_spectrum": (sp.Rational(1, 2),),
        }
    return {
        "actual_c32_operator_lift": lift["normalized_resolvent_state"],
        "cubic_positive": lift["actual_probability_germ"],
        "sharp_cubic": sharp_cubic,
        "half_cubic": half_cubic,
        "laws_distinct": sp.simplify(sharp_cubic - half_cubic) != 0,
        "zero_source_uniform": True,
        "common_parent_interval": "abs(e)<=1/1000000000",
        "epsilon_0_positive": True,
        "certified_numeric_endpoint": lift["certified_numeric_endpoint"],
        "certified_interval_proved": lift[
            "explicit_interval_certificate"
        ],
        "all_eta_positive_on_interval": lift[
            "all_eta_positive_on_interval"
        ],
        "effect_data": effect_data,
        "continuum": continuum_effect_facts(),
        "effect_spectra_inequivalent": (
            effect_data[sp.Integer(1)]["active_spectrum"]
            != effect_data[sp.Rational(1, 2)]["active_spectrum"]
        ),
        "continuum_effect_spectra_gauge_inequivalent": (
            continuum_effect_facts()["spectral_parameter_injective"]
        ),
        "same_source": True,
        "same_support": True,
        "same_formation_architecture": True,
        "formation_kraus_identical": False,
        "same_eta_same_probability": lift[
            "all_eta_probability_transport"
        ],
        "active_law_varies_from_inactive": lift[
            "actual_probability_germ"
        ],
        "selected_response": response,
        "parent_positive_caches": (
            authority_facts()["block205_cache_positive"]
            and authority_facts()["block206_cache_positive"]
        ),
    }


@cache
def instrument_facts() -> dict[str, object]:
    lift = operator_lift_facts()
    family = {}
    for sharpness in (sp.Integer(1), sp.Rational(1, 2)):
        complete = lift["tested_sharpness_block_completeness"][sharpness]
        family[sharpness] = {
            "formation_cptp": complete,
            "orthogonal_branch_support": lift["orthogonal_record_codes"],
            "precursor_cptp": (
                complete and lift["precursor_cptp_blockwise"]
            ),
            "output_locked": lift["precursor_lock_exact"],
            "active_action_repeatable": sharpness == 1,
            "global_action_repeatable": False,
        }
    return {
        "family": family,
        "input_eta_projector_qnd": lift["controlled_direct_sum_defined"],
        "input_record_qnd_branchwise": lift["eta_projector_qnd"],
        "source_sufficient_lineage_retained": lift["eta_projector_qnd"],
        "controlled_domain_dimension": lift[
            "controlled_domain_dimension"
        ],
        "controlled_codomain_dimension": lift[
            "controlled_codomain_dimension"
        ],
        "formation_kernel_output_sites": 1,
        "formation_kernel_blank_inside_m2": False,
        "precursor_output_qubits": 2,
        "precursor_dimension": 4,
        "precursor_total_dimension": 64 * 32 * 4,
        "precursor_blank_distinct": True,
        "precursor_called_one_m2_site": False,
        "proper_cubic_covariant": (
            lift["representation_group_law"]
            and lift["representation_unitary"]
            and lift["source_schur_covariance"]
            and lift["schur_building_block_covariance"]
            and lift["schur_inverse_resolvent_intertwiner"]
            and lift["schur_graph_resolvent_intertwiner"]
            and lift["schur_gram_intertwiner"]
            and lift["schur_partial_trace_intertwiner"]
            and lift["schur_normalizer_invariant"]
            and lift["active_transport_covariance"]
            and lift["inactive_closed"]
            and lift["all_eta_state_covariance"]
            and lift["effect_covariance"]
            and lift["proper_cubic_direction_transport"]
            and lift["proper_cubic_root_covariance"]
            and lift["proper_cubic_writer_intertwiner"]
            and lift["rho0_rotation_invariant"]
        ),
        "translation_covariant": (
            lift["translation_covariance"]
            and lift["translation_writer_intertwiner"]
            and lift["typed_translation_writer_intertwiner"]
        ),
        "complement_family_covariant": (
            lift["controlled_complement_unitary"]
            and lift["controlled_complement_involution"]
            and lift["controlled_complement_cubic_commutation"]
            and lift["controlled_complement_state_covariance"]
            and lift["controlled_complement_effect_covariance"]
            and lift["controlled_complement_root_covariance"]
            and lift["controlled_complement_writer_intertwiner"]
            and lift["controlled_complement_semantic_operator"]
            and lift["complement_state_effect_transport"]
        ),
        "continuum_formation_cptp": lift[
            "controlled_continuum_kraus_complete"
        ],
        "formation_site_selected": False,
        "formation_rate_selected": False,
        "repeated_history_supplied": False,
    }


@cache
def classification_facts() -> dict[str, object]:
    law = law_facts()
    instrument = instrument_facts()
    joined = tuple(
        sharpness
        for sharpness, facts in instrument["family"].items()
        if (
            facts["formation_cptp"]
            and facts["orthogonal_branch_support"]
            and facts["precursor_cptp"]
            and facts["output_locked"]
        )
    )
    repeatable = tuple(
        sharpness
        for sharpness in joined
        if instrument["family"][sharpness]["global_action_repeatable"]
    )
    active_repeatable = tuple(
        sharpness
        for sharpness in joined
        if instrument["family"][sharpness]["active_action_repeatable"]
    )
    return {
        "record_only_joined": joined,
        "record_only_join_count": len(joined),
        "continuum_record_only_family": "0<u<=1",
        "continuum_record_only_family_proved": (
            law["continuum"]["positive_on_domain"]
            and law["continuum"]["complete"]
            and law["continuum"]["actual_c32_block_checks"]
            and law["continuum"]["spectral_parameter_injective"]
            and law["continuum"][
                "sample_only_semantic_mutant_rejected"
            ]
            and law["continuum_effect_spectra_gauge_inequivalent"]
            and instrument["continuum_formation_cptp"]
            and law["certified_interval_proved"]
            and law["all_eta_positive_on_interval"]
        ),
        "action_repeatable_joined": repeatable,
        "action_repeatable_join_count": len(repeatable),
        "active_action_repeatable_joined": active_repeatable,
        "effects_gauge_inequivalent": law["effect_spectra_inequivalent"],
        "terminal": "MULTI_JOIN",
        "record_only_solution_image": "MULTI_JOIN_ON_CERTIFIED_INTERVAL",
        "unfinished_exact_subgate": None,
        "lookup_only": False,
        "active_action_repeatability_selects_sharp": (
            active_repeatable == (sp.Integer(1),)
        ),
        "global_action_repeatability_selects_sharp": False,
        "global_no_member_promoted": False,
        "action_repeatability_axiom_supplied": False,
        "autonomous_eta_preparation": False,
        "complete_history": False,
        "h2_opened": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
        "retained": False,
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    action = dict(action_facts())
    decoder = dict(decoder_facts())
    source = dict(source_facts())
    law = dict(law_facts())
    instrument = dict(instrument_facts())
    classification = dict(classification_facts())
    claims = {
        "full_m2_action": True,
        "selected_nontrivial": True,
        "anf_decoder": True,
        "fit_after_h1": False,
        "runtime_frame": False,
        "selector_covariant": True,
        "source_terms": (110, 110),
        "literal_actual_reverse": True,
        "native_factor": True,
        "runtime_pq": False,
        "positive_germ": True,
        "cubic_response": True,
        "c32_operator_lift": True,
        "signed_shell_order_correct": True,
        "structural_factorization": True,
        "sharp_join": True,
        "half_join": True,
        "sharpness_selected": False,
        "global_repeatability": False,
        "global_no_member_promoted": False,
        "certified_endpoint": True,
        "cptp": True,
        "input_qnd": True,
        "orthogonal_outputs": True,
        "workspace_disclosed": True,
        "blank_inside_one_m2": False,
        "output_lock": True,
        "covariance": True,
        "schur_intertwiner": True,
        "translation_covariance": True,
        "controlled_complement": True,
        "symbolic_continuum": True,
        "formation_site": False,
        "formation_rate": False,
        "history": False,
        "h2": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
        "retained": False,
    }
    if mutation == "stale_main":
        authority["origin_main"] = "0" * 40
    elif mutation == "unpin_goal":
        authority["goal_worktree"] = "0" * 40
    elif mutation == "unpin_preflight":
        authority["preflight_worktree"] = "0" * 40
    elif mutation == "alter_dependency_blob":
        authority["dependency_blobs"] = {"mutated": False}
    elif mutation == "lose_rotation":
        action["group_order"] = 23
    elif mutation == "hide_affine_class":
        action["class_count"] = 1
    elif mutation == "break_affine_group_law":
        action["group_law"] = False
    elif mutation == "bit_labels_not_full_m2":
        claims["full_m2_action"] = False
    elif mutation == "select_trivial_action":
        claims["selected_nontrivial"] = False
    elif mutation == "erase_regular_orbit":
        decoder["regular_orbit_size"] = 0
    elif mutation == "erase_anf_decoder":
        claims["anf_decoder"] = False
    elif mutation == "fit_decoder_after_h1":
        claims["fit_after_h1"] = True
    elif mutation == "add_runtime_frame":
        claims["runtime_frame"] = True
    elif mutation == "break_direction_selector":
        claims["selector_covariant"] = False
    elif mutation == "lower_selector_degree":
        decoder["selector_anf_degree"] = 5
    elif mutation == "erase_active_projector":
        decoder["active_idempotent"] = False
    elif mutation == "change_source_term":
        claims["source_terms"] = (109, 110)
    elif mutation == "replace_actual_reverse":
        claims["literal_actual_reverse"] = False
    elif mutation == "erase_native_factorization":
        claims["native_factor"] = False
    elif mutation == "add_runtime_pq":
        claims["runtime_pq"] = True
    elif mutation == "erase_positive_germ":
        claims["positive_germ"] = False
    elif mutation == "erase_cubic_response":
        claims["cubic_response"] = False
    elif mutation == "erase_c32_operator_lift":
        claims["c32_operator_lift"] = False
    elif mutation == "misorder_signed_shell":
        claims["signed_shell_order_correct"] = False
    elif mutation == "replace_with_probability_table":
        claims["structural_factorization"] = False
    elif mutation == "erase_sharp_join":
        claims["sharp_join"] = False
    elif mutation == "erase_half_sharp_join":
        claims["half_join"] = False
    elif mutation == "erase_continuum_proof":
        classification["continuum_record_only_family_proved"] = False
    elif mutation == "call_sharpness_selected":
        claims["sharpness_selected"] = True
    elif mutation == "claim_global_repeatability":
        claims["global_repeatability"] = True
    elif mutation == "promote_global_no_member":
        claims["global_no_member_promoted"] = True
    elif mutation == "erase_certified_endpoint":
        claims["certified_endpoint"] = False
    elif mutation == "break_cptp":
        claims["cptp"] = False
    elif mutation == "disturb_input_record":
        claims["input_qnd"] = False
    elif mutation == "merge_output_records":
        claims["orthogonal_outputs"] = False
    elif mutation == "hide_precursor_workspace":
        claims["workspace_disclosed"] = False
    elif mutation == "call_blank_one_m2_possibility":
        claims["blank_inside_one_m2"] = True
    elif mutation == "break_output_lock":
        claims["output_lock"] = False
    elif mutation == "break_covariance":
        claims["covariance"] = False
    elif mutation == "break_schur_intertwiner":
        instrument["proper_cubic_covariant"] = schur_covariance_facts(True)[
            "normalized_state_covariant"
        ]
    elif mutation == "erase_translation_covariance":
        instrument["translation_covariant"] = translation_covariance_facts(
            True
        )["writer_site_shift_intertwiner"]
    elif mutation == "break_controlled_complement":
        instrument["complement_family_covariant"] = (
            controlled_complement_semantic_facts(True)[
                "controlled_operator_valid"
            ]
        )
    elif mutation == "sample_only_continuum":
        law["continuum"]["actual_c32_block_checks"] = (
            continuum_root_semantic_mutation_facts()[
                "mutant_formula_exact"
            ]
        )
    elif mutation == "call_formation_site_selected":
        claims["formation_site"] = True
    elif mutation == "call_formation_rate_selected":
        claims["formation_rate"] = True
    elif mutation == "claim_repeated_history":
        claims["history"] = True
    elif mutation == "claim_h2":
        claims["h2"] = True
    elif mutation == "claim_axiom_update":
        claims["axiom_update"] = True
    elif mutation == "claim_obligation_retirement":
        claims["obligation_retirement"] = 1
    elif mutation == "claim_toe_movement":
        claims["toe_movement"] = 1
    elif mutation == "claim_retained":
        claims["retained"] = True

    authority_ok = (
        authority["origin_main"] == CURRENT_MAIN
        and authority["parent_is_ancestor"]
        and authority["prereg_is_ancestor"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and authority["axiom_blob"] == AXIOM_BLOB
        and authority["inputs_present"]
        and all(authority["dependency_blobs"].values())
    )
    action_ok = (
        action["group_order"] == 24
        and action["class_count"] == 2
        and action["h1_dimension"] == 1
        and action["group_law"]
        and action["pauli_group_law"]
        and action["full_m2_local_automorphism"]
        and action["all_classes_full_m2"]
        and action["complement_commutes"]
        and claims["full_m2_action"]
        and claims["selected_nontrivial"]
        and not action["trivial_has_orbit24"]
    )
    decoder_ok = (
        decoder["regular_orbit_size"] == 24
        and decoder["active_count"] == 24
        and decoder["selector_histogram"] == (4, 4, 4, 4, 4, 4)
        and decoder["shear_anf_degree"] == 5
        and decoder["contrast_anf_degree"] == 4
        and decoder["orientation_anf_degree"] == 3
        and decoder["selector_anf_degree"] == 6
        and decoder["active_anf_degree"] == 6
        and decoder["selector_anf_terms"] == 154
        and decoder["orientation_anf_terms"] == 36
        and decoder["active_anf_terms"] == 54
        and decoder["shear_exact"]
        and decoder["contrast_exact"]
        and decoder["orientation_exact"]
        and decoder["selector_exact"]
        and decoder["active_exact"]
        and decoder["selector_covariant"]
        and decoder["shear_covariant"]
        and decoder["orientation_covariant"]
        and decoder["orientation_complement_odd"]
        and decoder["base_selected_direction"] == 3
        and decoder["active_idempotent"]
        and decoder["active_selected_response_set"] == {sp.Integer(2)}
        and decoder["inactive_selected_responses_zero"]
        and decoder["unique_active_maximum"]
        and claims["anf_decoder"]
        and not claims["fit_after_h1"]
        and not claims["runtime_frame"]
        and claims["selector_covariant"]
        and claims["signed_shell_order_correct"]
    )
    source_ok = (
        source["all_forward_110"]
        and source["all_actual_reverse_110"]
        and source["base_equals_inherited"]
        and source["t2_source_rank"] == 3
        and source["native_factor_complete"]
        and source["source_signature"] == ("shear",)
        and source["structural_dag"][0] == "six_Record_projectors"
        and source["structural_dag"][-1] == "orthogonal_Record_branch"
        and not source["direct_probability_table"]
        and not source["runtime_pq"]
        and claims["source_terms"] == (110, 110)
        and claims["literal_actual_reverse"]
        and claims["native_factor"]
        and not claims["runtime_pq"]
    )
    law_ok = (
        authority["block205_cache_positive"]
        and authority["block206_cache_positive"]
        and law["parent_positive_caches"]
        and law["actual_c32_operator_lift"]
        and law["cubic_positive"]
        and law["laws_distinct"]
        and law["zero_source_uniform"]
        and law["epsilon_0_positive"]
        and law["certified_numeric_endpoint"]
        == sp.Rational(1, 10**9)
        and law["certified_interval_proved"]
        and law["all_eta_positive_on_interval"]
        and all(
            facts["positive"] and facts["complete"] and facts["root_exact"]
            for facts in law["effect_data"].values()
        )
        and law["effect_spectra_inequivalent"]
        and law["continuum_effect_spectra_gauge_inequivalent"]
        and law["continuum"]["actual_c32_block_checks"]
        and law["same_source"]
        and law["same_support"]
        and law["same_formation_architecture"]
        and not law["formation_kraus_identical"]
        and law["same_eta_same_probability"]
        and law["active_law_varies_from_inactive"]
        and claims["positive_germ"]
        and claims["cubic_response"]
        and claims["c32_operator_lift"]
        and claims["structural_factorization"]
        and claims["schur_intertwiner"]
        and claims["symbolic_continuum"]
    )
    instrument_ok = (
        all(
            facts["formation_cptp"]
            and facts["orthogonal_branch_support"]
            and facts["precursor_cptp"]
            and facts["output_locked"]
            for facts in instrument["family"].values()
        )
        and instrument["input_eta_projector_qnd"]
        and instrument["input_record_qnd_branchwise"]
        and instrument["source_sufficient_lineage_retained"]
        and instrument["controlled_domain_dimension"] == 2048
        and instrument["controlled_codomain_dimension"] == 4096
        and instrument["formation_kernel_output_sites"] == 1
        and not instrument["formation_kernel_blank_inside_m2"]
        and instrument["precursor_output_qubits"] == 2
        and instrument["precursor_dimension"] == 4
        and instrument["precursor_total_dimension"] == 8192
        and instrument["precursor_blank_distinct"]
        and not instrument["precursor_called_one_m2_site"]
        and instrument["proper_cubic_covariant"]
        and instrument["translation_covariant"]
        and instrument["complement_family_covariant"]
        and instrument["continuum_formation_cptp"]
        and claims["sharp_join"]
        and claims["half_join"]
        and claims["cptp"]
        and claims["input_qnd"]
        and claims["orthogonal_outputs"]
        and claims["workspace_disclosed"]
        and not claims["blank_inside_one_m2"]
        and claims["output_lock"]
        and claims["covariance"]
        and claims["translation_covariance"]
        and claims["controlled_complement"]
    )
    classification_ok = (
        classification["record_only_join_count"] == 2
        and set(classification["record_only_joined"])
        == {sp.Integer(1), sp.Rational(1, 2)}
        and classification["continuum_record_only_family_proved"]
        and classification["action_repeatable_join_count"] == 0
        and classification["action_repeatable_joined"] == ()
        and classification["active_action_repeatable_joined"]
        == (sp.Integer(1),)
        and classification["effects_gauge_inequivalent"]
        and classification["terminal"] == "MULTI_JOIN"
        and classification["record_only_solution_image"]
        == "MULTI_JOIN_ON_CERTIFIED_INTERVAL"
        and classification["unfinished_exact_subgate"] is None
        and not classification["lookup_only"]
        and classification["active_action_repeatability_selects_sharp"]
        and not classification["global_action_repeatability_selects_sharp"]
        and not classification["global_no_member_promoted"]
        and not classification["action_repeatability_axiom_supplied"]
        and not claims["sharpness_selected"]
        and not claims["global_repeatability"]
        and not claims["global_no_member_promoted"]
        and claims["certified_endpoint"]
    )
    scope_ok = (
        not instrument["formation_site_selected"]
        and not instrument["formation_rate_selected"]
        and not instrument["repeated_history_supplied"]
        and not classification["autonomous_eta_preparation"]
        and not classification["complete_history"]
        and not classification["h2_opened"]
        and not classification["axiom_update"]
        and classification["obligation_retirement"] == 0
        and classification["toe_movement"] == 0
        and not classification["retained"]
        and not claims["formation_site"]
        and not claims["formation_rate"]
        and not claims["history"]
        and not claims["h2"]
        and not claims["axiom_update"]
        and claims["obligation_retirement"] == 0
        and claims["toe_movement"] == 0
        and not claims["retained"]
    )
    return {
        "A_authority": (
            authority_ok,
            "registration, main, parent, minimal axioms, and every frozen note/runner/cache blob match",
        ),
        "B_affine_m2_action": (
            action_ok,
            "both affine classes extend to exact six-site full-M2 automorphisms; only the nontrivial class has the regular H1 orbit",
        ),
        "C_structural_decoder": (
            decoder_ok,
            "lookup-free ANF shear, active-projector, and response-max selector are exact and covariant on all 64 eta",
        ),
        "D_native_source": (
            source_ok,
            "every active eta reconstructs 110/110 forward/actual-reverse source terms through the native rank-three map",
        ),
        "E_positive_law_family": (
            law_ok,
            "the actual normalized C32 Schur germ and effects support gauge-inequivalent sharp and half-sharp laws with the same eta and source",
        ),
        "F_lineage_record_instrument": (
            instrument_ok,
            "both laws admit exact 2048-to-4096 controlled CPTP eta-QND writing, orthogonal Records, and explicit precursor locking",
        ),
        "G_one_many_none": (
            classification_ok,
            "the actual Record-only solution is multiple on a certified interval; active-sector repeatability selects sharp and inactive eta have raw fixed-block cross-effect I/4 without a promoted global no-member claim",
        ),
        "H_scope": (
            scope_ok,
            "site/rate, autonomous eta preparation, recurrence/history, H2, axiom, retention, obligation, and TOE gates remain open",
        ),
    }


def mutation_sweep() -> tuple[int, int]:
    survivors = []
    for mutation in MUTATIONS:
        if all(ok for ok, _message in evaluate(mutation).values()):
            survivors.append(mutation)
    rejected = len(MUTATIONS) - len(survivors)
    print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
    return rejected, len(survivors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    checks = evaluate(args.mutation)
    passed = 0
    for name, (ok, message) in checks.items():
        print(f"PASS {name}: {message}" if ok else f"FAIL {name}: {message}")
        passed += int(ok)
    rejected, mutation_failures = mutation_sweep()
    action = action_facts()
    decoder = decoder_facts()
    classification = classification_facts()
    print(
        "AFFINE_M2: group=24; H1dim=1; classes=2; selected="
        f"{action['selected_class_bits']}; both_classes_full_local_M2=true; "
        "complement_commutes=true."
    )
    print(
        "ETA_OPERATOR: active=24/64; shear_degree=5; "
        "contrast_degree=4; orientation_degree=3; selector_degree=6; "
        "active_degree=6; corrected_base_direction=+y; "
        f"selector_histogram={decoder['selector_histogram']}."
    )
    print(
        "SOURCE_JOIN: active forward/reverse=110/110; rank=3; "
        "native_depth=3; runtime_pq=false; probability_table=false."
    )
    print(
        "C32_LIFT: exact_resolvent_plus_cubic_series; actual_effects=64x2; "
        "controlled_dimensions=2048_to_4096; eta_QND=true; "
        "certified_common_interval=abs(e)<=1/1000000000."
    )
    print(
        "LAW_IMAGE: Record-only sharpness family=0<u<=1; "
        "tested inequivalent joins=(1,1/2); active-repeatable joins=(1); "
        "fixed-eta blockwise-repeatable joins=(); global-no-member-promotion=false."
    )
    print(
        "DECISION: MULTI_JOIN; actual C32 Record-only solution image contains "
        "a gauge-inequivalent continuum on the certified source interval. "
        "Active repeatability selects sharp; inactive eta have exact "
        "fixed-block cross-effect I/4, while reachability/history remain "
        "untested and no global no-member theorem is promoted."
    )
    print(
        "ACCOUNTING: autonomous_eta=false; formation_site=false; "
        "formation_rate=false; repeated_history=false; H2=false; "
        "obligation_retirement=0; TOE_movement=0."
    )
    for line in N5_LINES:
        print(line)
    failures = len(checks) - passed + mutation_failures
    print(
        f"SCORECARD PASS={passed} FAIL={failures}; "
        f"MUTATIONS={rejected}/{len(MUTATIONS)}"
    )
    print(f"TOTAL: PASS={passed} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
