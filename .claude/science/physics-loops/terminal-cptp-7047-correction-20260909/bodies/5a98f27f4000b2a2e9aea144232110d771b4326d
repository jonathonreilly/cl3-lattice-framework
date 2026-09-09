#!/usr/bin/env python3
"""Cycle 321: physical effect-equivalence and normalized-grade tournament.

Two pairs of bounded Cycle-317/Cycle-311 apparatus programs are compared:

* axis-identity programs have identical compressed effects but different
  post-outcome and pointer-erased system CP maps;
* ray-split/refinement programs have identical coarse CP instruments and
  system-only futures, while their fine pointer transcripts remain distinct.

All equivalence tests use operators, Choi matrices, and channel composition.
No numerical outcome grade is used to define physical equivalence.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import sqrt
from pathlib import Path
import re
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EFFECT_EQUIVALENCE_NORMALIZED_GRADE_CYCLE321_NOTE_2026-07-18.md"
)
TOL = 6.0e-11
FRESH_MAIN = "17cb0c5c32e753ef1297b185fbd1e8c6d41920c2"
PASS = 0
FAIL = 0

I2 = c317.I2
X = c317.X
Y = c317.Y
Z = c317.Z

N1_ROUTES = (
    "effect-only quotient on the axis pair",
    "coarse-CP quotient on the ray refinement",
    "system-only future-process quotient",
    "fine pointer-transcript quotient",
    "exhaustive-pointer normalized-grade route",
    "autonomous physical program/equivalence law",
    "occurrence and lawful Record route",
    "process-functional/global-history route",
)
WALLS = ("W_program", "W_quotient", "W_grade", "W_occ_record", "W_global")
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natur", "ally"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-321 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "physical effect-equivalence tournament",
        "same two-ray m64 apparatus",
        "axis-identity pair",
        "ray-split/refinement pair",
        "equality for every input state",
        "post-outcome cp maps",
        "system-only future-process equivalence",
        "pointer-visible transcript",
        "locally certified quotient",
        "physical exhaustive-pointer law",
        "finite normalized non-trace grade",
        "actual cycle-230 contact",
        "all 24 proper-cubic frames",
        "held l=6",
        "pointer erasure is not occurrence",
        "pointer labels are not records",
        "frequency remains open",
        "supplied program/quotient inventory",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "broad gate status: fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the operator/process tournament, semantic firewalls, inventory, and N1-N8 gate",
        not missing,
        missing,
    )


def projector(direction) -> np.ndarray:
    vector = np.asarray(direction, dtype=float)
    vector /= np.linalg.norm(vector)
    return c317.projector_bloch(vector)


@dataclass(frozen=True)
class Program:
    name: str
    kraus: tuple[np.ndarray, ...]
    coarse_groups: tuple[tuple[int, ...], ...]

    def __post_init__(self) -> None:
        if not 1 <= len(self.kraus) <= 8:
            raise ValueError("one bounded program has one to eight fine labels")
        if any(operator.shape != (2, 2) for operator in self.kraus):
            raise ValueError("every Kraus block acts on the seam qubit")
        flattened = tuple(index for group in self.coarse_groups for index in group)
        if sorted(flattened) != list(range(len(self.kraus))):
            raise ValueError("coarse groups must partition the fine pointer labels")

    @property
    def fine_effects(self) -> tuple[np.ndarray, ...]:
        return tuple(operator.conj().T @ operator for operator in self.kraus)

    @property
    def coarse_effects(self) -> tuple[np.ndarray, ...]:
        return tuple(
            sum(
                (self.fine_effects[index] for index in group),
                start=np.zeros((2, 2), dtype=complex),
            )
            for group in self.coarse_groups
        )

    @property
    def completeness(self) -> np.ndarray:
        return sum(self.fine_effects, start=np.zeros((2, 2), dtype=complex))


def choi(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    return sum(
        (
            np.outer(
                operator.reshape(-1, order="F"),
                operator.reshape(-1, order="F").conj(),
            )
            for operator in kraus
        ),
        start=np.zeros((4, 4), dtype=complex),
    )


def grouped_kraus(program: Program, group: int) -> tuple[np.ndarray, ...]:
    return tuple(program.kraus[index] for index in program.coarse_groups[group])


def grouped_chois(program: Program) -> tuple[np.ndarray, ...]:
    return tuple(
        choi(grouped_kraus(program, group))
        for group in range(len(program.coarse_groups))
    )


def apply_cp(kraus: tuple[np.ndarray, ...], rho: np.ndarray) -> np.ndarray:
    return sum(
        (operator @ rho @ operator.conj().T for operator in kraus),
        start=np.zeros((2, 2), dtype=complex),
    )


def transcript_choi(
    effects: tuple[np.ndarray, ...], dimension: int = 8
) -> np.ndarray:
    if len(effects) > dimension:
        raise ValueError("transcript capacity exceeded")
    result = np.zeros((2 * dimension, 2 * dimension), dtype=complex)
    for index, effect in enumerate(effects):
        result[2 * index : 2 * (index + 1), 2 * index : 2 * (index + 1)] = effect.T
    return result


def held_states() -> tuple[np.ndarray, ...]:
    vectors = [
        np.asarray((1, 0), dtype=complex),
        np.asarray((0, 1), dtype=complex),
        np.asarray((1, 1), dtype=complex) / sqrt(2),
        np.asarray((1, 1j), dtype=complex) / sqrt(2),
    ]
    rng = np.random.default_rng(321)
    for _ in range(8):
        vector = rng.normal(size=2) + 1j * rng.normal(size=2)
        vectors.append(vector / np.linalg.norm(vector))
    return tuple(np.outer(vector, vector.conj()) for vector in vectors)


def every_input_effect_residual(left: np.ndarray, right: np.ndarray) -> float:
    delta = left - right
    return max(
        abs(np.trace(delta @ rho))
        for rho in held_states()
    )


def future_process_witness(
    left: tuple[np.ndarray, ...], right: tuple[np.ndarray, ...]
) -> float:
    effects = tuple(
        projector(direction)
        for direction in (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        )
    )
    return max(
        abs(
            np.trace(
                effect @ (apply_cp(left, rho) - apply_cp(right, rho))
            )
        )
        for rho in held_states()
        for effect in effects
    )


def axis_programs(contact: np.ndarray) -> tuple[Program, Program, dict[str, object]]:
    direction = np.asarray((1, 2, 3), dtype=float)
    direction /= np.linalg.norm(direction)
    c0 = 2 / (1 + np.sum(np.abs(direction)))
    left_components = [(c0 / 2, projector(direction))]
    for axis in range(3):
        unit = np.zeros(3)
        unit[axis] = -np.sign(direction[axis])
        left_components.append(
            (c0 * abs(direction[axis]) / 2, projector(unit))
        )
    right_direction = np.asarray((1, -1, 2), dtype=float)
    right_direction /= np.linalg.norm(right_direction)
    right_components = (
        (0.5, projector(right_direction)),
        (0.5, projector(-right_direction)),
    )

    def build(name: str, components) -> Program:
        kraus = tuple(
            operator
            for weight, p in components
            for operator in (
                sqrt(weight) * p @ contact,
                sqrt(weight) * (I2 - p) @ contact,
            )
        )
        return Program(
            name,
            kraus,
            (
                tuple(range(0, len(kraus), 2)),
                tuple(range(1, len(kraus), 2)),
            ),
        )

    return (
        build("four-component axis", left_components),
        build("two-component antipodal", right_components),
        {
            "direction": tuple(float(value) for value in direction),
            "left_weights": tuple(float(weight) for weight, _ in left_components),
            "right_weights": (0.5, 0.5),
        },
    )


def ray_programs(contact: np.ndarray) -> tuple[Program, Program, dict[str, float]]:
    p = projector((3, -4, 0))
    weight = 0.61
    split = 0.37
    unsplit = Program(
        "unsplit ray",
        (
            sqrt(weight) * p @ contact,
            sqrt(weight) * (I2 - p) @ contact,
            sqrt(1 - weight) * contact,
        ),
        ((0,), (1,), (2,)),
    )
    refined = Program(
        "two-piece ray refinement",
        (
            sqrt(split * weight) * p @ contact,
            sqrt((1 - split) * weight) * p @ contact,
            sqrt(weight) * (I2 - p) @ contact,
            sqrt(1 - weight) * contact,
        ),
        ((0, 1), (2,), (3,)),
    )
    return unsplit, refined, {"weight": weight, "split": split}


def auxiliary_programs(contact: np.ndarray) -> tuple[Program, Program]:
    trine = tuple(
        sqrt(2 / 3)
        * projector(
            (
                np.cos(2 * np.pi * index / 3),
                np.sin(2 * np.pi * index / 3),
                0,
            )
        )
        @ contact
        for index in range(3)
    )
    coin = (I2 @ contact / 2, I2 @ contact / 2, I2 @ contact / sqrt(2))
    return (
        Program("contact trine", trine, ((0,), (1,), (2,))),
        Program("quarter coin", coin, ((0,), (1,), (2,))),
    )


def physical_fixture_controls() -> dict[int, c317.PhysicalFixture]:
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    rows = []
    for length, fixture in fixtures.items():
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "gram": float(
                    np.linalg.norm(
                        fixture.two_ray_encoding.conj().T
                        @ fixture.two_ray_encoding
                        - I2
                    )
                ),
                "contact": float(
                    np.linalg.norm(
                        fixture.physical_contact @ fixture.two_ray_encoding
                        - fixture.two_ray_encoding @ fixture.contact
                    )
                ),
                "constraint": float(
                    np.linalg.norm(
                        fixture.constraint @ fixture.two_ray_encoding
                        - fixture.two_ray_encoding
                    )
                ),
            }
        )
    species = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c317.c311.c219.rest_mass(species) / species.analytic_mass - 1
    )
    check(
        "the Cycle-321 tournament stays on the accepted same-number Cycle-311/Cycle-317 contact seam through held L=6",
        all(max(row["gram"], row["contact"], row["constraint"]) < TOL for row in rows)
        and mass_residual < 3e-12,
        {"rows": rows, "one_particle_mass_relative_residual": mass_residual},
    )
    return fixtures


def axis_equivalence_controls(
    left: Program, right: Program
) -> dict[str, float]:
    left_effects = left.coarse_effects
    right_effects = right.coarse_effects
    effect_residual = max(
        float(np.linalg.norm(a - b))
        for a, b in zip(left_effects, right_effects)
    )
    input_residual = max(
        every_input_effect_residual(a, b)
        for a, b in zip(left_effects, right_effects)
    )
    selected_cp_residual = float(
        np.linalg.norm(grouped_chois(left)[0] - grouped_chois(right)[0])
    )
    nonselective_residual = float(
        np.linalg.norm(choi(left.kraus) - choi(right.kraus))
    )
    future_selected = future_process_witness(
        grouped_kraus(left, 0), grouped_kraus(right, 0)
    )
    future_erased = future_process_witness(left.kraus, right.kraus)
    coarse_transcript = float(
        np.linalg.norm(
            transcript_choi(left.coarse_effects)
            - transcript_choi(right.coarse_effects)
        )
    )
    fine_transcript = float(
        np.linalg.norm(
            transcript_choi(left.fine_effects)
            - transcript_choi(right.fine_effects)
        )
    )
    detail = {
        "coarse_effect_residual": effect_residual,
        "held_every_input_matrix_element_residual": input_residual,
        "selected_outcome_Choi_residual": selected_cp_residual,
        "pointer_erased_system_Choi_residual": nonselective_residual,
        "held_future_selected_witness": future_selected,
        "held_future_erased_witness": future_erased,
        "coarse_transcript_Choi_residual": coarse_transcript,
        "fine_transcript_Choi_residual": fine_transcript,
    }
    check(
        "the two axis-identity programs have the same compressed effects for every input but distinguishable post-outcome and pointer-erased future processes",
        effect_residual < TOL
        and input_residual < TOL
        and coarse_transcript < TOL
        and selected_cp_residual > 0.4
        and nonselective_residual > 0.8
        and future_selected > 0.1
        and future_erased > 0.2
        and fine_transcript > 0.4,
        detail,
    )
    return detail


def ray_equivalence_controls(
    unsplit: Program, refined: Program
) -> dict[str, float]:
    effect_residual = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(unsplit.coarse_effects, refined.coarse_effects)
    )
    cp_residual = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(grouped_chois(unsplit), grouped_chois(refined))
    )
    total_residual = float(
        np.linalg.norm(choi(unsplit.kraus) - choi(refined.kraus))
    )
    coarse_transcript = float(
        np.linalg.norm(
            transcript_choi(unsplit.coarse_effects)
            - transcript_choi(refined.coarse_effects)
        )
    )
    fine_transcript = float(
        np.linalg.norm(
            transcript_choi(unsplit.fine_effects)
            - transcript_choi(refined.fine_effects)
        )
    )
    future_residual = future_process_witness(unsplit.kraus, refined.kraus)
    detail = {
        "coarse_effect_residual": effect_residual,
        "coarse_instrument_Choi_residual": cp_residual,
        "pointer_erased_system_Choi_residual": total_residual,
        "coarse_transcript_Choi_residual": coarse_transcript,
        "held_future_witness": future_residual,
        "fine_transcript_Choi_residual": fine_transcript,
    }
    check(
        "the ray split/refinement is exactly equivalent as a coarse CP instrument and under every system-only future, while fine pointer transcripts remain distinct",
        effect_residual < TOL
        and cp_residual < TOL
        and total_residual < TOL
        and coarse_transcript < TOL
        and future_residual < TOL
        and fine_transcript > 0.3,
        detail,
    )
    return detail


def quotient_controls(
    axis_left: Program,
    axis_right: Program,
    ray_unsplit: Program,
    ray_refined: Program,
) -> dict[str, bool]:
    def effect_equivalent(left: Program, right: Program) -> bool:
        return len(left.coarse_effects) == len(right.coarse_effects) and all(
            np.linalg.norm(a - b) < TOL
            for a, b in zip(left.coarse_effects, right.coarse_effects)
        )

    def cp_equivalent(left: Program, right: Program) -> bool:
        return len(left.coarse_groups) == len(right.coarse_groups) and all(
            np.linalg.norm(a - b) < TOL
            for a, b in zip(grouped_chois(left), grouped_chois(right))
        )

    result = {
        "axis_effect_quotient": effect_equivalent(axis_left, axis_right),
        "axis_CP_quotient": cp_equivalent(axis_left, axis_right),
        "ray_effect_quotient": effect_equivalent(ray_unsplit, ray_refined),
        "ray_CP_quotient": cp_equivalent(ray_unsplit, ray_refined),
        "ray_future_stability": np.linalg.norm(
            choi(ray_unsplit.kraus) - choi(ray_refined.kraus)
        )
        < TOL,
    }
    check(
        "the locally certified coarse-CP quotient retires exact refinement dependence but does not identify every same-effect program",
        result
        == {
            "axis_effect_quotient": True,
            "axis_CP_quotient": False,
            "ray_effect_quotient": True,
            "ray_CP_quotient": True,
            "ray_future_stability": True,
        },
        result,
    )
    return result


def unique_effects_and_menus(
    programs: tuple[Program, ...]
) -> tuple[tuple[np.ndarray, ...], tuple[tuple[int, ...], ...]]:
    menus = [program.fine_effects for program in programs]
    menus.extend(program.coarse_effects for program in programs[:4])
    unique: list[np.ndarray] = []
    indices = []
    for menu in menus:
        row = []
        for effect in menu:
            found = next(
                (
                    index
                    for index, existing in enumerate(unique)
                    if np.linalg.norm(effect - existing) < 1e-10
                ),
                None,
            )
            if found is None:
                found = len(unique)
                unique.append(effect)
            row.append(found)
        indices.append(tuple(row))
    return tuple(unique), tuple(indices)


def finite_grade_controls(programs: tuple[Program, ...]) -> dict[str, object]:
    unique, menus = unique_effects_and_menus(programs)
    matrix = np.zeros((len(menus), len(unique)))
    for row, menu in enumerate(menus):
        for index in menu:
            matrix[row, index] += 1
    target = np.ones(len(menus))
    trace_grade = np.asarray([np.trace(effect).real / 2 for effect in unique])
    singular = np.linalg.svd(matrix, full_matrices=True)
    rank = int(np.sum(singular[1] > 1e-10))
    null_basis = singular[2][rank:].T
    bloch = np.asarray(
        [
            [0.5 * np.trace(pauli @ effect).real for pauli in (X, Y, Z)]
            for effect in unique
        ]
    )
    q, _ = np.linalg.qr(bloch)
    candidates = tuple(
        vector - q @ (q.T @ vector)
        for vector in null_basis.T
    )
    chosen = max(candidates, key=np.linalg.norm)
    chosen /= np.linalg.norm(chosen)
    margin = min(
        np.min(trace_grade[trace_grade > 1e-10]),
        np.min(1 - trace_grade[trace_grade < 1 - 1e-10]),
    )
    epsilon = 0.3 * margin / np.max(np.abs(chosen))
    finite_grade = trace_grade + epsilon * chosen
    trace_coefficients, *_ = np.linalg.lstsq(
        bloch, finite_grade - trace_grade, rcond=None
    )
    trace_fit = trace_grade + bloch @ trace_coefficients
    trace_fit_residual = float(np.linalg.norm(finite_grade - trace_fit))
    non_born_sums = tuple(
        sum(c317.nonlinear_binary_weight(effect) for effect in program.fine_effects)
        for program in programs
    )
    detail = {
        "compiled_program_menus": len(menus),
        "unique_effects": len(unique),
        "normalization_rank": rank,
        "normalization_nullity": len(unique) - rank,
        "trace_grade_normalization_residual": float(
            np.linalg.norm(matrix @ trace_grade - target)
        ),
        "finite_nontrace_grade_normalization_residual": float(
            np.linalg.norm(matrix @ finite_grade - target)
        ),
        "finite_grade_minimum": float(np.min(finite_grade)),
        "finite_grade_maximum": float(np.max(finite_grade)),
        "best_trace_form_residual": trace_fit_residual,
        "nonlinear_binary_grade_menu_sums": non_born_sums,
    }
    check(
        "physical pointer exhaustiveness gives operator completeness for every program but does not uniquely normalize or select a numerical grade",
        all(np.linalg.norm(program.completeness - I2) < TOL for program in programs)
        and len(menus) == 10
        and len(unique) == 20
        and rank == 7
        and len(unique) - rank == 13
        and detail["trace_grade_normalization_residual"] < TOL
        and detail["finite_nontrace_grade_normalization_residual"] < TOL
        and 0 < detail["finite_grade_minimum"]
        and detail["finite_grade_maximum"] < 1
        and trace_fit_residual > 0.02
        and max(abs(value - 1) for value in non_born_sums) > 0.3,
        detail,
    )
    return detail


def physical_support_covariance_and_contact_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    programs: tuple[Program, ...],
) -> dict[str, object]:
    locality_rows = []
    for length, fixture in fixtures.items():
        representatives = tuple(
            c317.c311.branch_representative(
                fixture.code, fixture.encoder.body, branch, r_value
            )
            for r_value in (0, 1)
            for branch in fixture.basis_rows
        )
        pairs = set()
        for program in programs:
            for operator in program.kraus:
                raw = (
                    fixture.two_ray_encoding
                    @ operator
                    @ fixture.two_ray_encoding.conj().T
                )
                pairs.update(
                    (int(row), int(column))
                    for row, column in np.argwhere(abs(raw) > 1e-12)
                )
        support_union = 0
        maximum = 0
        port_failures = sector_failures = 0
        for row, column in pairs:
            transition = representatives[row] @ c317.c311.local.pauli_dagger(
                representatives[column]
            )
            support = transition.x | transition.z
            support_union |= support
            maximum = max(maximum, support.bit_count())
            port_failures += sum(
                not transition.commutes(
                    c317.c311.c305.constraint_pauli(fixture.code, vertex)
                )
                for vertex in range(len(fixture.code.graph.vertices))
            )
            sector_failures += sum(
                not transition.commutes(check_row)
                for check_row in fixture.code.local_checks + fixture.code.wilsons
            )
        locality_rows.append(
            {
                "L": length,
                "held": length == 6,
                "matrix_unit_pairs": len(pairs),
                "transition_union_M2": support_union.bit_count(),
                "maximum_transition_M2": maximum,
                "maximum_with_pointer_M2": maximum + 3,
                "conservative_patch_M2": 59,
                "installed_overhead_M2_per_cell": 26,
                "port_constraint_failures": port_failures,
                "local_check_or_Wilson_failures": sector_failures,
            }
        )
    check(
        "all equivalence programs retain bounded physical support and zero inherited leakage through held L=6",
        all(
            row["matrix_unit_pairs"] == 16
            and row["transition_union_M2"] == 20
            and row["maximum_transition_M2"] <= 20
            and row["maximum_with_pointer_M2"] <= 23
            and row["conservative_patch_M2"] == 59
            and row["installed_overhead_M2_per_cell"] == 26
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in locality_rows
        ),
        locality_rows,
    )

    base = fixtures[3]
    reducer = c317.c311.c305.StabilizerReducer(base.code)
    frame_rows = []
    selected = np.zeros((127, 2), dtype=complex)
    selected[
        [
            c317.c311.SEAM_INDEX[(2, (0, 1), stream_slice)]
            for stream_slice in (0, 1)
        ],
        [0, 1],
    ] = 1
    for frame in c317.c311.c235.proper_cubic_frames():
        logical_r = c317.c311.logical_frame_representation(frame)
        old_r, failures = c317.c311.flagged_frame_representation(
            base.encoder,
            base.basis_rows,
            base.occurrence,
            frame,
            reducer,
        )
        mapping, phases, mapping_failures = c317.c311.signed_mapping(old_r)
        new_mapping = np.concatenate((mapping, mapping + 255))
        new_phases = np.concatenate((phases, phases))
        carried_f = base.full_encoding @ logical_r @ selected
        residual = 0.0
        for program in programs:
            base_v = c317.physical_isometry(base.two_ray_encoding, program.kraus)
            carried_v = c317.physical_isometry(carried_f, program.kraus)
            blocks = []
            for pointer in range(8):
                block = base_v[510 * pointer : 510 * (pointer + 1), :]
                blocks.append(
                    c317.c311.apply_signed_mapping(
                        new_mapping, new_phases, block
                    )
                )
            residual = max(residual, float(np.linalg.norm(np.vstack(blocks) - carried_v)))
        frame_rows.append((failures + mapping_failures, residual))
    check(
        "every program has carried covariance under all 24 proper-cubic frames",
        len(frame_rows) == 24
        and all(failures == 0 and residual < TOL for failures, residual in frame_rows),
        {
            "frames": len(frame_rows),
            "branch_failures": sum(row[0] for row in frame_rows),
            "maximum_apparatus_residual": max(row[1] for row in frame_rows),
        },
    )

    ray = programs[2]
    p = projector((3, -4, 0))
    deleted_contact_effect = 0.61 * p
    contact_residual = float(
        np.linalg.norm(ray.coarse_effects[0] - deleted_contact_effect)
    )
    axis_fine_residual = max(
        np.linalg.norm(
            effect
            - deleted_operator.conj().T @ deleted_operator
        )
        for effect, deleted_operator in zip(
            programs[0].fine_effects,
            tuple(
                operator @ base.contact.conj().T
                for operator in programs[0].kraus
            ),
        )
    )
    check(
        "the equivalence tournament remains actually contact dependent on the ray fixture",
        contact_residual > 0.15,
        {
            "contact_deletion_selected_ray_effect_residual": contact_residual,
            "axis_coarse_half_I_contact_residual": float(
                np.linalg.norm(programs[0].coarse_effects[0] - I2 / 2)
            ),
            "axis_fine_contact_boundary": axis_fine_residual,
        },
    )
    return {"locality": locality_rows, "contact_deletion": contact_residual}


def deletion_and_domain_controls(programs: tuple[Program, ...]) -> None:
    refined = programs[3]
    deleted = refined.kraus[:1] + (
        np.zeros((2, 2), dtype=complex),
    ) + refined.kraus[2:]
    deletion_residual = float(
        np.linalg.norm(
            sum(
                (operator.conj().T @ operator for operator in deleted),
                start=np.zeros((2, 2), dtype=complex),
            )
            - I2,
            2,
        )
    )
    axis = programs[0]
    axis_deleted = axis.kraus[:2] + tuple(
        np.zeros((2, 2), dtype=complex) if index in (2, 3) else operator
        for index, operator in enumerate(axis.kraus[2:], start=2)
    )
    axis_effect_deleted = sum(
        (
            axis_deleted[index].conj().T @ axis_deleted[index]
            for index in range(0, len(axis_deleted), 2)
        ),
        start=np.zeros((2, 2), dtype=complex),
    )
    axis_deletion_residual = float(np.linalg.norm(axis_effect_deleted - I2 / 2))
    check(
        "deleting a nonzero refinement branch or one axis component breaks its declared exhaustive/equal-effect contract",
        deletion_residual > 0.1 and axis_deletion_residual > 0.1,
        {
            "ray_refinement_branch_completeness_residual": deletion_residual,
            "axis_component_equal_effect_residual": axis_deletion_residual,
        },
    )

    rejected = 0
    invalid = (
        lambda: Program("nine", tuple(I2 for _ in range(9)), (tuple(range(9)),)),
        lambda: Program("bad group", (I2,), ((1,),)),
        lambda: Program("duplicate group", (I2, I2), ((0,), (0,))),
        lambda: transcript_choi(tuple(I2 for _ in range(9))),
    )
    for call in invalid:
        try:
            call()
        except ValueError:
            rejected += 1
    check(
        "the lawful domain rejects excess capacity and malformed fine/coarse pointer declarations",
        rejected == len(invalid),
        rejected,
    )


def semantic_firewall_controls() -> None:
    text = normalized(NOTE)
    check(
        "the semantic firewall keeps pointer erasure, effect quotient, numerical grade, occurrence, Record, and frequency distinct",
        "pointer erasure is not occurrence" in text
        and "pointer labels are not records" in text
        and "finite normalized assignment is not a frequency law" in text
        and "actual member remains open" in text
        and "record formation and permanence remain open" in text
        and "frequency remains open" in text,
        {
            "physical_effects": "derived",
            "coarse_CP_quotient": "certified for exact refinements",
            "general_effect_functionality": "open",
            "numerical_grade_selection": None,
            "occurrence": None,
            "actual_member": None,
            "Record": None,
            "frequency": None,
        },
    )


def markdown_section(body: str, start: str, end: str | None) -> str:
    left = body.index(start)
    right = len(body) if end is None else body.index(end, left)
    return body[left:right]


def strict_no_go_controls() -> None:
    print("\nSTRICT N1-N8 RELEASE DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FRESH_MAIN, "origin/main"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    check(
        "the recorded no-go methodology commit remains an ancestor of origin/main",
        completed.returncode == 0,
        {"recorded": FRESH_MAIN, "current_ref": "origin/main"},
    )

    n1 = markdown_section(note, "### N1", "### N2")
    allowed = {"ATTEMPTED", "RULED OUT BY PRIOR RESULT", "OPEN / UNTESTED"}
    markers = {}
    malformed = []
    for route in N1_ROUTES:
        match = re.search(
            rf"^\|\s*{re.escape(route)}\s*\|[^|]*\|\s*(\*\*[^*]+\*\*)\s*\|",
            n1,
            re.MULTILINE,
        )
        raw = match.group(1) if match else ""
        marker = raw.replace("*", "")
        markers[route] = marker
        if raw != f"**{marker}**" or marker not in allowed:
            malformed.append((route, raw))
    bold = tuple(re.findall(r"\*\*([^*]+)\*\*", n1))
    check(
        "N1 uses only exact bold honesty markers on eight distinct routes",
        not malformed and len(bold) == 8 and set(bold) <= allowed,
        {"markers": markers, "malformed": malformed, "all_bold": bold},
    )

    n2 = markdown_section(note, "### N2", "### N3")
    pair_rows = []
    for left, right in combinations(WALLS, 2):
        match = re.search(
            rf"^\|\s*`{left}/{right}`\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|",
            n2,
            re.MULTILINE | re.IGNORECASE,
        )
        pair_rows.append(
            (left, right, tuple(value.lower() for value in match.groups()) if match else None)
        )
    check(
        "N2 validates both closure directions for all ten collapsed wall pairs",
        len(pair_rows) == 10 and all(row[2] == ("no", "no", "yes") for row in pair_rows),
        pair_rows,
    )

    trigger_rows = []
    for path in (Path(__file__).resolve(), NOTE):
        lines = path.read_text(encoding="utf-8").lower().splitlines()
        hits = []
        for parts in TRIGGER_PARTS:
            trigger = "".join(parts)
            hits.extend(
                (trigger, line_number)
                for line_number, line in enumerate(lines, 1)
                if trigger in line
            )
        trigger_rows.append((str(path.relative_to(ROOT)), tuple(hits)))
    check(
        "N3 literal hidden-condition procedure scan has zero hits on both release paths",
        all(not row[1] for row in trigger_rows),
        trigger_rows,
    )

    fragment_parts = (
        (
            "the two axis-identity programs have the same compressed effects ",
            "for every input but distinguishable post-outcome and pointer-erased future processes",
        ),
        (
            "the ray split/refinement is exactly equivalent as a coarse CP instrument ",
            "and under every system-only future, while fine pointer transcripts remain distinct",
        ),
        (
            "the locally certified coarse-CP quotient retires exact refinement dependence ",
            "but does not identify every same-effect program",
        ),
        (
            "physical pointer exhaustiveness gives operator completeness for every program ",
            "but does not uniquely normalize or select a numerical grade",
        ),
        (
            "all equivalence programs retain bounded physical support ",
            "and zero inherited leakage through held L=6",
        ),
        (
            "every program has carried covariance ",
            "under all 24 proper-cubic frames",
        ),
    )
    fragments = tuple(left + right for left, right in fragment_parts)
    runner_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    relative = str(Path(__file__).resolve().relative_to(ROOT))
    rows = []
    for fragment in fragments:
        hits = tuple(
            line_number
            for line_number, line in enumerate(runner_lines, 1)
            if fragment in line
        )
        reference = f"{relative}:{hits[0]}" if len(hits) == 1 else None
        rows.append((fragment, hits, reference, bool(reference and reference in note)))
    check(
        "N4 pins every decisive current residual to one exact executable line",
        all(len(row[1]) == 1 and row[3] for row in rows),
        rows,
    )

    flat = " ".join(note.split())
    requirements = (
        (
            "N5 separates effect, CP map, block, pointer, and global resolutions",
            (
                "per-effect",
                "per-coarse CP outcome",
                "per complete block",
                "pointer-visible",
                "lattice/global",
            ),
        ),
        (
            "N6 retains six explicit constructive import-retirement paths",
            (
                "fixed physical program carrier",
                "coarse-CP quotient",
                "effect-only quotient",
                "exhaustive pointer",
                "occurrence/Record",
                "process-functional/global-history",
            ),
        ),
        (
            "N7 contains the strongest quotient-selection steelman",
            (
                "hostile constructive reviewer",
                "physically privileged effect quotient",
                "could still select",
            ),
        ),
        (
            "N8 records six cross-cycle retirement mechanisms",
            (
                "Cycle 278 binary pointer",
                "Cycle 285 contact phase",
                "Cycle 287 typed Record DAG",
                "Cycle 311 M64 seam",
                "Cycle 317 forcing basis",
                "PR-5451 instrument nonselection",
            ),
        ),
    )
    for label, required in requirements:
        missing = tuple(item for item in required if item not in flat)
        check(label, not missing, missing)
    broad = (
        "Broad gate status: FAIL / DO NOT SHIP",
        "No shared obstruction and no axiom pressure follow.",
        "occurrence/process-functional routes remain open",
    )
    missing = tuple(item for item in broad if item not in flat)
    check(
        "the broad effect-functionality/Born/Record no-go and axiom-pressure release is blocked",
        not missing,
        missing,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    fixtures = physical_fixture_controls()
    contact = fixtures[3].contact
    axis_left, axis_right, axis_data = axis_programs(contact)
    ray_unsplit, ray_refined, ray_data = ray_programs(contact)
    trine, coin = auxiliary_programs(contact)
    programs = (axis_left, axis_right, ray_unsplit, ray_refined, trine, coin)
    check(
        "all six finite apparatus programs are exact physical exhaustive-pointer isometries",
        all(
            np.linalg.norm(program.completeness - I2) < TOL
            and np.linalg.norm(c317.stack_isometry(program.kraus).conj().T @ c317.stack_isometry(program.kraus) - I2) < TOL
            for program in programs
        ),
        {program.name: float(np.linalg.norm(program.completeness - I2)) for program in programs},
    )
    axis_result = axis_equivalence_controls(axis_left, axis_right)
    ray_result = ray_equivalence_controls(ray_unsplit, ray_refined)
    quotient_result = quotient_controls(
        axis_left, axis_right, ray_unsplit, ray_refined
    )
    grade_result = finite_grade_controls(programs)
    physical_result = physical_support_covariance_and_contact_controls(
        fixtures, programs
    )
    deletion_and_domain_controls(programs)
    semantic_firewall_controls()
    strict_no_go_controls()
    check(
        "Cycle 321 closes exact CP-preserving refinement equivalence but neither general effect functionality nor normalized-grade selection",
        quotient_result["ray_CP_quotient"]
        and not quotient_result["axis_CP_quotient"]
        and grade_result["best_trace_form_residual"] > 0.02
        and physical_result["contact_deletion"] > 0.15
        and "broad gate status: fail / do not ship" in normalized(NOTE),
        {
            "axis": axis_result,
            "ray": ray_result,
            "axis_program": axis_data,
            "ray_program": ray_data,
        },
    )
    print("DATA axis", axis_result)
    print("DATA ray", ray_result)
    print("DATA grade", grade_result)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE321_PHYSICAL_EFFECT_EQUIVALENCE_GRADE_GREEN"
        if FAIL == 0
        else "CYCLE321_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
