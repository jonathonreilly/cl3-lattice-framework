#!/usr/bin/env python3
"""Block 194: detector-conditioned orientation and M2 pointer discriminator.

The detector family, classifier, phase-zero contact, discovery points, and
hard stop were committed before this response was evaluated.  The runner
derives the unique nondemolition ray, constructs its complete coherent PVM and
explicit binary pointer dilation, and contracts the literal Block-193 source
tangent.  It does not scan another connector or open held-outs after the
discovery rank gate fails.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import permutations, product
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402


b191 = b193.b191
b190 = b193.b190
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "cef8b0407aea496c9c1dadd65cfde0c9afc6f73a"
PREREG_COMMIT = "eeec3dee69bfb2ae77b7f89f83728709909f0622"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
AUDIT_TIMEOUT_SEC = 240

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.txt",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.txt",
    "docs/ADMISSIBILITY_D4_GRADE3_SOURCE_INSTRUMENT_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.py",
    "logs/runner-cache/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.txt",
    "docs/ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
    "logs/runner-cache/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.txt",
)

MUTATIONS = (
    "stale_main_authority",
    "replace_literal_source_by_local_lift",
    "claim_empty_detector_ray",
    "claim_multiple_detector_rays",
    "break_reflection_label_covariance",
    "break_proper_cubic_covariance",
    "break_effect_orthogonality",
    "break_pointer_dilation",
    "claim_pointer_alone_stores_eight_labels",
    "claim_d1_rank_two",
    "claim_h1_rank_two",
    "open_heldouts_after_discovery_failure",
    "claim_permanent_record",
    "claim_broad_detector_no_go",
    "claim_axiom_update",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "stale_main_authority": "A",
    "replace_literal_source_by_local_lift": "A",
    "claim_empty_detector_ray": "B",
    "claim_multiple_detector_rays": "B",
    "break_reflection_label_covariance": "C",
    "break_proper_cubic_covariance": "C",
    "break_effect_orthogonality": "D",
    "break_pointer_dilation": "D",
    "claim_pointer_alone_stores_eight_labels": "F",
    "claim_d1_rank_two": "E",
    "claim_h1_rank_two": "E",
    "open_heldouts_after_discovery_failure": "F",
    "claim_permanent_record": "F",
    "claim_broad_detector_no_go": "G",
    "claim_axiom_update": "G",
    "claim_toe_progress": "G",
}


I = sp.I
R = sp.Rational
IDENTITY16 = sp.eye(16)
ZERO16 = sp.zeros(16)
GTIME = b193.GTIME
GSPACE = b193.GSPACE
SIGMA_X = sp.Matrix(((0, 1), (1, 0)))
SIGMA_Z = sp.diag(1, -1)
POINTER_I = sp.eye(2)
KET_ZERO = sp.Matrix((1, 0))
KET_ONE = sp.Matrix((0, 1))
Q_PLUS = (POINTER_I + SIGMA_Z) / 2
Q_MINUS = (POINTER_I - SIGMA_Z) / 2


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "worktree_axiom": git_output("hash-object", "--", AXIOM_PATH),
        "registry": git_output("rev-parse", f"origin/main:{REGISTRY_PATH}"),
        "worktree_registry": git_output("hash-object", "--", REGISTRY_PATH),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


def block_matrix(
    upper_left: sp.MatrixBase,
    upper_right: sp.MatrixBase,
    lower_left: sp.MatrixBase,
    lower_right: sp.MatrixBase,
) -> sp.Matrix:
    return sp.Matrix.vstack(
        sp.Matrix.hstack(upper_left, upper_right),
        sp.Matrix.hstack(lower_left, lower_right),
    )


def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        permutation_matrix = sp.zeros(3)
        for row, column in enumerate(permutation):
            permutation_matrix[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            candidate = sp.diag(*signs) * permutation_matrix
            if candidate.det() == 1:
                rotations.append(candidate)
    return tuple(rotations)


@cache
def detector_classification_facts() -> dict[str, object]:
    detector_basis = tuple(
        sp.expand(I * GTIME * spatial_gamma)
        for spatial_gamma in GSPACE
    )
    columns = []
    for generator in detector_basis:
        commutator_1 = sp.expand(generator * b191.O1 - b191.O1 * generator)
        commutator_2 = sp.expand(generator * b191.O2 - b191.O2 * generator)
        columns.append(sp.Matrix.vstack(
            commutator_1.reshape(256, 1),
            commutator_2.reshape(256, 1),
        ))
    constraint = sp.Matrix.hstack(*columns)
    constraint_rank = DomainMatrix.from_Matrix(
        constraint, extension=True
    ).rank()
    nullspace = constraint.nullspace()
    if len(nullspace) == 1:
        raw_ray = nullspace[0]
        first_nonzero = next(value for value in raw_ray if value != 0)
        ray = sp.Matrix(tuple(
            sp.simplify(value / first_nonzero) for value in raw_ray
        ))
        norm_squared = sp.simplify((ray.T * ray)[0])
        unit_ray = sp.simplify(ray / sp.sqrt(norm_squared))
        orientation = sp.expand(sum((
            unit_ray[axis] * detector_basis[axis] for axis in range(3)
        ), ZERO16))
    else:
        ray = sp.zeros(3, 1)
        unit_ray = ray
        orientation = ZERO16

    rotations = proper_cubic_rotations()
    family_covariance = True
    context_covariance = True
    for spatial in rotations:
        full = sp.eye(4)
        full[:3, :3] = spatial
        form_rotation = b190.wedge_representation(full)
        rotated_events = tuple(sp.expand(
            form_rotation * effect * form_rotation.T
        ) for effect in b191.EFFECTS)
        transformed_o1 = sp.expand(
            form_rotation * b191.O1 * form_rotation.T
        )
        transformed_o2 = sp.expand(
            form_rotation * b191.O2 * form_rotation.T
        )
        context_covariance = context_covariance and all(
            b193.matrix_equal(
                rotated_events[index],
                (IDENTITY16 + b191.OUTCOME_LABELS[index][0] * transformed_o1)
                * (IDENTITY16 + b191.OUTCOME_LABELS[index][1] * transformed_o2)
                / 4,
            ) for index in range(4)
        )
        for old_axis, generator in enumerate(detector_basis):
            expected = sp.expand(sum((
                spatial[new_axis, old_axis] * detector_basis[new_axis]
                for new_axis in range(3)
            ), ZERO16))
            family_covariance = family_covariance and b193.matrix_equal(
                form_rotation * generator * form_rotation.T, expected
            )

    reflection_event_map = all(b193.matrix_equal(
        GTIME * b191.EFFECTS[index] * GTIME,
        b191.EFFECTS[3 - index],
    ) for index in range(4))
    coordinate_time_transform = sp.diag(1, 1, 1, -1)
    coordinate_time_reflection = b190.wedge_representation(
        coordinate_time_transform
    )
    coordinate_reflection_odd = b193.matrix_equal(
        coordinate_time_reflection * orientation
        * coordinate_time_reflection.T,
        -orientation,
    )
    coordinate_reflection_context_fixed = all(b193.matrix_equal(
        coordinate_time_reflection * effect
        * coordinate_time_reflection.T,
        effect,
    ) for effect in b191.EFFECTS)
    return {
        "basis": detector_basis,
        "constraint_shape": constraint.shape,
        "constraint_rank": constraint_rank,
        "solution_dimension": len(nullspace),
        "ray": tuple(ray),
        "unit_ray": tuple(unit_ray),
        "orientation": orientation,
        "hermitian": b193.matrix_equal(orientation.H, orientation),
        "involution": b193.matrix_equal(
            orientation * orientation, IDENTITY16
        ),
        "event_compatible": all(b193.matrix_equal(
            orientation * effect, effect * orientation
        ) for effect in b191.EFFECTS),
        "fiber_reflection_odd": b193.matrix_equal(
            GTIME * orientation * GTIME, -orientation
        ),
        "fiber_reflection_event_map": reflection_event_map,
        "coordinate_reflection_odd": coordinate_reflection_odd,
        "coordinate_reflection_context_fixed": (
            coordinate_reflection_context_fixed
        ),
        "proper_cubic_count": len(rotations),
        "family_covariance": family_covariance,
        "context_covariance": context_covariance,
    }


@cache
def instrument_pointer_facts() -> dict[str, object]:
    classification = detector_classification_facts()
    orientation = classification["orientation"]
    connectors = tuple(sp.expand(effect * orientation)
                       for effect in b191.EFFECTS)
    effects = tuple(
        sp.expand(block_matrix(
            effect, sign * connector,
            sign * connector.H, effect,
        ) / 2)
        for effect, connector in zip(b191.EFFECTS, connectors)
        for sign in (1, -1)
    )
    diagonal_events = tuple(block_matrix(
        effect, ZERO16, ZERO16, effect
    ) for effect in b191.EFFECTS)
    sector_orientation = block_matrix(
        ZERO16, orientation, orientation, ZERO16
    )
    p_plus = sp.expand((sp.eye(32) + sector_orientation) / 2)
    p_minus = sp.expand((sp.eye(32) - sector_orientation) / 2)
    writer = sp.expand(
        sp.kronecker_product(p_plus, POINTER_I)
        + sp.kronecker_product(p_minus, SIGMA_X)
    )
    input_isometry = sp.kronecker_product(sp.eye(32), KET_ZERO)
    pointer_codes = (Q_PLUS, Q_MINUS)
    induced_effects = []
    for diagonal_event in diagonal_events:
        for pointer_code in pointer_codes:
            joint_readout = sp.kronecker_product(
                diagonal_event, pointer_code
            )
            induced_effects.append(sp.expand(
                input_isometry.H * writer.H * joint_readout
                * writer * input_isometry
            ))

    sector_reflection = block_matrix(
        GTIME, ZERO16, ZERO16, GTIME
    )
    reflection_effect_map = all(b193.matrix_equal(
        sector_reflection * effects[2 * index + sign_index]
        * sector_reflection,
        effects[2 * (3 - index) + (1 - sign_index)],
    ) for index in range(4) for sign_index in range(2))
    minus_input = sp.kronecker_product(p_minus, KET_ZERO)
    minus_output = sp.kronecker_product(p_minus, KET_ONE)
    return {
        "connectors": connectors,
        "effects": effects,
        "orientation_partial_unitaries": all(
            b193.matrix_equal(connector.H * connector, effect)
            and b193.matrix_equal(connector * connector.H, effect)
            for connector, effect in zip(connectors, b191.EFFECTS)
        ),
        "projectors": all(
            b193.matrix_equal(effect.H, effect)
            and b193.matrix_equal(effect * effect, effect)
            for effect in effects
        ),
        "pairwise_orthogonal": all(b193.matrix_equal(
            effects[left] * effects[right], sp.zeros(32)
        ) for left in range(8) for right in range(left + 1, 8)),
        "complete": b193.matrix_equal(
            sum(effects, sp.zeros(32)), sp.eye(32)
        ),
        "coarsenings": all(b193.matrix_equal(
            effects[2 * index] + effects[2 * index + 1],
            diagonal_events[index],
        ) for index in range(4)),
        "effect_ranks": tuple(effect.rank() for effect in effects),
        "baseline_weights": tuple(sp.trace(effect) / 32 for effect in effects),
        "sector_involution": b193.matrix_equal(
            sector_orientation.H, sector_orientation
        ) and b193.matrix_equal(
            sector_orientation * sector_orientation, sp.eye(32)
        ),
        "pointer_projectors": all(
            b193.matrix_equal(code.H, code)
            and b193.matrix_equal(code * code, code)
            for code in pointer_codes
        ),
        "pointer_orthogonal": b193.matrix_equal(
            Q_PLUS * Q_MINUS, sp.zeros(2)
        ),
        "pointer_complete": b193.matrix_equal(Q_PLUS + Q_MINUS, POINTER_I),
        "pointer_label_flip": b193.matrix_equal(
            SIGMA_X * Q_PLUS * SIGMA_X, Q_MINUS
        ),
        "writer_unitary": b193.matrix_equal(
            writer.H * writer, sp.eye(64)
        ) and b193.matrix_equal(writer * writer.H, sp.eye(64)),
        "writer_nonidentity": not b193.matrix_equal(writer, sp.eye(64)),
        "minus_branch_flip": b193.matrix_equal(
            writer * minus_input, minus_output
        ),
        "faithful_joint_readout": all(b193.matrix_equal(
            induced_effects[index], effects[index]
        ) for index in range(8)),
        "reflection_effect_map": reflection_effect_map,
    }


@cache
def response_facts(point_name: str) -> dict[str, object]:
    instrument = instrument_pointer_facts()
    connectors = instrument["connectors"]
    tangent = b193.tt_tangent_columns(point_name)
    overlaps = sp.Matrix(4, 2, lambda row, column: b193.term_trace(
        tangent["columns"][column], connectors[row].H
    ))
    real_overlaps = overlaps.applyfunc(lambda value: sp.factor(sp.simplify(
        (value + sp.conjugate(value)) / 2
    )))
    slopes = sp.expand(8 * real_overlaps / tangent["normalizer"])
    return {
        "overlaps": overlaps,
        "slopes": slopes,
        "complex_rank": DomainMatrix.from_Matrix(
            overlaps, extension=True
        ).rank(),
        "real_rank": DomainMatrix.from_Matrix(
            slopes, extension=True
        ).rank(),
        "first_column_zero": all(
            sp.simplify(overlaps[row, 0]) == 0 for row in range(4)
        ),
        "second_column_zero": all(
            sp.simplify(overlaps[row, 1]) == 0 for row in range(4)
        ),
        "second_column_signed_pair": (
            sp.simplify(overlaps[0, 1]) != 0
            and sp.simplify(overlaps[1, 1] - overlaps[0, 1]) == 0
            and sp.simplify(overlaps[2, 1] + overlaps[0, 1]) == 0
            and sp.simplify(overlaps[3, 1] + overlaps[0, 1]) == 0
        ),
        "source_second_column_nonzero": (
            tangent["second_column_operator_nonzero"]
        ),
    }


N5_LINES = (
    "per_element: checked all three degree-two detector generators, the exact nondemolition commutator map, the unique ray, four event connectors, and two pointer codes.",
    "per_site: checked one fixed phase-zero source-event contact and its nonidentity M2 write; no spatial formation or permanence dynamics were supplied.",
    "per_mode: checked exact D1/H1 TT response for the classified ray and kept D2/D3/H2/X1 sealed after the discovery gate failed.",
    "per_block: checked classifier, eight coherent effects, and controlled pointer dilation as distinct blocks and stopped before the Record tail.",
    "lattice_wide: checked and not executed -- no extended-support detector, full lattice apparatus, autonomous formation, physical time, Born derivation, nonlinear gravity, or retained TOE theory is claimed.",
)


@cache
def note_facts() -> dict[str, bool]:
    if not NOTE_PATH.is_file():
        return {"exists": False, "n5": False, "scope": False}
    text = NOTE_PATH.read_text(encoding="utf-8")
    scope_tokens = (
        "detector_solution_dimension: one",
        "detector_ray: spatial_plus_axis_3",
        "m2_pointer_dilation: exact",
        "d1_real_tt_rank: zero",
        "h1_real_tt_rank: one",
        "heldouts: sealed",
        "permanent_record: not_claimed",
        "broad_detector_no_go: not_claimed",
        "no_go_discipline_gate: FAIL",
        "negative_disposition: partial-attempt-with-named-untested-routes",
        "minimal_axiom_update: none",
        "toe_percentage_movement: 0",
    )
    return {
        "exists": True,
        "n5": all(line in text for line in N5_LINES),
        "scope": all(token in text for token in scope_tokens),
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    literal_source = b193.literal_source_facts()
    classification = detector_classification_facts()
    instrument = instrument_pointer_facts()
    d1 = response_facts("D1")
    h1 = response_facts("H1")
    note = note_facts()

    claims = {
        "main": CURRENT_MAIN,
        "literal_source": True,
        "solution_dimension": 1,
        "reflection_covariance": True,
        "proper_cubic_covariance": True,
        "effect_orthogonality": True,
        "pointer_dilation": True,
        "pointer_alone_eight_labels": False,
        "d1_rank_two": False,
        "h1_rank_two": False,
        "heldouts_open": False,
        "permanent_record": False,
        "broad_detector_no_go": False,
        "axiom_update": False,
        "toe_progress": False,
    }
    if mutation == "stale_main_authority":
        claims["main"] = "stale"
    elif mutation == "replace_literal_source_by_local_lift":
        claims["literal_source"] = False
    elif mutation == "claim_empty_detector_ray":
        claims["solution_dimension"] = 0
    elif mutation == "claim_multiple_detector_rays":
        claims["solution_dimension"] = 2
    elif mutation == "break_reflection_label_covariance":
        claims["reflection_covariance"] = False
    elif mutation == "break_proper_cubic_covariance":
        claims["proper_cubic_covariance"] = False
    elif mutation == "break_effect_orthogonality":
        claims["effect_orthogonality"] = False
    elif mutation == "break_pointer_dilation":
        claims["pointer_dilation"] = False
    elif mutation == "claim_pointer_alone_stores_eight_labels":
        claims["pointer_alone_eight_labels"] = True
    elif mutation == "claim_d1_rank_two":
        claims["d1_rank_two"] = True
    elif mutation == "claim_h1_rank_two":
        claims["h1_rank_two"] = True
    elif mutation == "open_heldouts_after_discovery_failure":
        claims["heldouts_open"] = True
    elif mutation == "claim_permanent_record":
        claims["permanent_record"] = True
    elif mutation == "claim_broad_detector_no_go":
        claims["broad_detector_no_go"] = True
    elif mutation == "claim_axiom_update":
        claims["axiom_update"] = True
    elif mutation == "claim_toe_progress":
        claims["toe_progress"] = True

    reflection_covariance = (
        classification["fiber_reflection_odd"]
        and classification["fiber_reflection_event_map"]
        and classification["coordinate_reflection_odd"]
        and classification["coordinate_reflection_context_fixed"]
        and instrument["reflection_effect_map"]
        and instrument["pointer_label_flip"]
    )
    proper_cubic_covariance = (
        classification["proper_cubic_count"] == 24
        and classification["family_covariance"]
        and classification["context_covariance"]
    )
    effect_instrument = (
        instrument["orientation_partial_unitaries"]
        and instrument["projectors"]
        and instrument["pairwise_orthogonal"]
        and instrument["complete"]
        and instrument["coarsenings"]
        and instrument["effect_ranks"] == (4,) * 8
        and instrument["baseline_weights"] == (R(1, 8),) * 8
        and instrument["sector_involution"]
    )
    pointer_dilation = (
        instrument["pointer_projectors"]
        and instrument["pointer_orthogonal"]
        and instrument["pointer_complete"]
        and instrument["writer_unitary"]
        and instrument["writer_nonidentity"]
        and instrument["minus_branch_flip"]
        and instrument["faithful_joint_readout"]
    )
    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["parent"] and authority["prereg"]
            and authority["axiom"] == CURRENT_AXIOM_BLOB
            and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
            and authority["inputs"]
            and literal_source["literal"] == claims["literal_source"]
            and literal_source["actual_reverse_distinct"]
            and literal_source["block_placement"],
            "authority and preregistration are pinned and the literal source occupies its frozen blocks",
        ),
        "B": (
            classification["constraint_shape"] == (512, 3)
            and classification["constraint_rank"] == 2
            and classification["solution_dimension"]
            == claims["solution_dimension"]
            and classification["ray"] == (0, 0, 1)
            and classification["hermitian"]
            and classification["involution"]
            and classification["event_compatible"],
            "the frozen degree-two nondemolition classifier selects exactly the spatial-plus axis-3 ray",
        ),
        "C": (
            reflection_covariance == claims["reflection_covariance"]
            and proper_cubic_covariance == claims["proper_cubic_covariance"],
            "the detector family is proper-cubic covariant and reflection swaps event and pointer labels",
        ),
        "D": (
            effect_instrument == claims["effect_orthogonality"]
            and pointer_dilation == claims["pointer_dilation"],
            "the classified ray gives eight orthogonal effects and an exact nonidentity M2 dilation",
        ),
        "E": (
            d1["complex_rank"] == 0 and d1["real_rank"] == 0
            and d1["first_column_zero"] and d1["second_column_zero"]
            and d1["source_second_column_nonzero"]
            and h1["complex_rank"] == 1 and h1["real_rank"] == 1
            and h1["first_column_zero"]
            and h1["second_column_signed_pair"]
            and h1["source_second_column_nonzero"]
            and claims["d1_rank_two"] is False
            and claims["h1_rank_two"] is False,
            "the physical detector is blind at D1 and sees only one TT direction at H1, so the hard gate fails",
        ),
        "F": (
            claims["pointer_alone_eight_labels"] is False
            and claims["heldouts_open"] is False
            and claims["permanent_record"] is False,
            "the four event ports plus one pointer bit form eight labels, while held-outs and Record stay sealed",
        ),
        "G": (
            note["exists"] and note["n5"] and note["scope"]
            and claims["broad_detector_no_go"] is False
            and claims["axiom_update"] is False
            and claims["toe_progress"] is False,
            "the no-go gate fails closed against a broad negative and states zero axiom, retained-theory, or TOE movement",
        ),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 96 else statement[:93] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0
    checks = Checks()
    for key, (condition, statement) in evaluate(args.mutation).items():
        checks.check(key, statement, condition)
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
