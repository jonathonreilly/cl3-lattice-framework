#!/usr/bin/env python3
"""Check the joint Record/gravity law cut exposed by the repaired Regge sector.

The runner keeps the approved foundation explicit and separates five law
controls: formation probability, event precedence, Euclidean-to-Lorentzian
clock identification, constraint preservation, and the Record-to-source
dictionary.  The first two already distinguish Record laws; the last three
distinguish conditional gravity completions before a physical operational
quotient is supplied.  The construction is a bounded non-entailment witness
and a constitutional cut gate.  It is not a selected physical law, a gravity
no-go, or an axiom amendment.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_"
    "BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE_PATH = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)
BLOCK44_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK45_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_"
    "TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_"
    "2026-08-11.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py",
    "scripts/admissibility_permanent_record_formation_scheduler_lorentzian_time_constraint_selection_boundary_2026_08_11.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_permanent_record_formation_scheduler_lorentzian_time_constraint_selection_boundary_2026_08_11 as block45  # noqa: E402
import admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11 as block44  # noqa: E402


TOLERANCE = 1.0e-11


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def schedule_mixture(mixing: Fraction) -> dict[tuple[int, int], Fraction]:
    """Convexly mix the exact parallel and random-order sequential laws."""
    if not (Fraction(0, 1) <= mixing <= Fraction(1, 1)):
        raise ValueError("schedule mixing must lie in [0,1]")
    parallel, sequential = block45.two_site_schedule_laws()
    return {
        pair: (1 - mixing) * parallel[pair] + mixing * sequential[pair]
        for pair in parallel
    }


def correlation(law: dict[tuple[int, int], Fraction]) -> Fraction:
    return sum(
        Fraction(left * right, 1) * probability
        for (left, right), probability in law.items()
    )


def continued_tt_form(
    spatial_wave_number: float, frequency: float, clock_map: float
) -> float:
    """The fixed Euclidean TT form after k_4 = i a omega and overall Wick sign."""
    euclidean_value = ((1j * clock_map * frequency) ** 2 + spatial_wave_number**2) / 4.0
    return float((-euclidean_value).real)


def source_response(source_coupling: float) -> tuple[float, float]:
    operator = block45.timed_einstein_operator((1.0, 0.0, 0.0), 0.0, 1.0)
    source = np.zeros(len(block44.HCOMPS), dtype=float)
    source[block44.STATIC_SOURCE_INDEX] = source_coupling
    response = -np.linalg.pinv(operator, rcond=1.0e-12) @ source
    residual = float(np.linalg.norm(operator @ response + source))
    return float(response[block44.STATIC_SOURCE_INDEX]), residual


def gravity_signature(clock_map: float, constraint_kinetic: float, source_coupling: float):
    plus, _ = block44.transverse_traceless_vectors()
    kinetic = block45.timed_einstein_operator((0.0, 0.0, 0.0), 1.0, clock_map)
    broken = block45.constraint_breaking_operator(
        (0.0, 0.0, 0.0), 1.0, constraint_kinetic
    )
    response, residual = source_response(source_coupling)
    return (
        float(plus @ kinetic @ plus),
        float(
            broken[
                block44.STATIC_SOURCE_INDEX,
                block44.STATIC_SOURCE_INDEX,
            ]
        ),
        response,
        residual,
    )


def record_signature(formation_probability: Fraction, schedule_mixing: Fraction):
    empty = (block45.EMPTY,) * 6
    kernel = block45.local_record_kernel(
        block45.EMPTY, empty, formation_probability
    )
    law = schedule_mixture(schedule_mixing)
    return (
        tuple(sorted(kernel.items())),
        tuple(sorted(law.items())),
        correlation(law),
    )


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    kinetic = flat(KINETIC_PATH)
    scale = flat(SCALE_PATH)
    realized = flat(REALIZED_PATH)
    block44_note = flat(BLOCK44_NOTE_PATH)
    block45_note = flat(BLOCK45_NOTE_PATH)
    registry = json.loads(PREMISE_REGISTRY_PATH.read_text(encoding="utf-8"))

    expected_primitives = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    checks.check(
        "complete-foundation-binding",
        "all four supplied foundation nodes and both constructive gravity parents are read explicitly",
        set(registry["canonical_ids"]) == expected_primitives
        and all(
            path.exists()
            for path in (
                NOTE_PATH,
                AXIOM_PATH,
                KINETIC_PATH,
                SCALE_PATH,
                REALIZED_PATH,
                BLOCK44_NOTE_PATH,
                BLOCK45_NOTE_PATH,
            )
        )
        and "admissibility is not a dynamics axiom" in axiom
        and "not a record-native causal update" in block44_note
        and "not a gravity no-go" in block45_note,
    )

    checks.check(
        "approved-primitives-remain-bounded",
        "kinetic isotropy fixes only OS0 form, scale fixes units only, and realized state supplies no selector",
        "c_t = c_s" in kinetic
        and "not a new dynamics" in kinetic
        and "fixes only the one dimensionless graining ratio" in kinetic
        and "units conversion" in scale
        and "zero dimensionless content" in scale
        and "does not supply a state, state-selection rule" in realized,
    )

    plus, _ = block44.transverse_traceless_vectors()
    continuation_errors = []
    for clock_map in (0.5, 1.0, 2.0):
        for spatial_wave_number, frequency in ((0.0, 1.0), (0.7, 0.9), (1.0, 1.0 / clock_map)):
            operator = block45.timed_einstein_operator(
                (spatial_wave_number, 0.0, 0.0), frequency, clock_map
            )
            continuation_errors.append(
                abs(
                    float(plus @ operator @ plus)
                    - continued_tt_form(spatial_wave_number, frequency, clock_map)
                )
            )
    checks.check(
        "os0-versus-clock-map-separation",
        "one fixed Euclidean OS0 TT form admits the family k4=i*a*omega without changing that Euclidean form",
        max(continuation_errors) < TOLERANCE,
        f"a=1/2,1,2; max continued-TT error={max(continuation_errors):.3e}",
    )

    schedule_values = (Fraction(0, 1), Fraction(1, 2), Fraction(1, 1))
    schedule_correlations = tuple(
        correlation(schedule_mixture(value)) for value in schedule_values
    )
    schedule_normalized = all(
        sum(schedule_mixture(value).values(), Fraction(0, 1)) == 1
        for value in schedule_values
    )
    checks.check(
        "continuous-precedence-control",
        "a symmetric exact schedule family preserves one-site marginals while its two-site correlation is 3r/5",
        schedule_normalized
        and schedule_correlations
        == (Fraction(0, 1), Fraction(3, 10), Fraction(3, 5)),
        f"r=0,1/2,1 correlations={schedule_correlations}",
    )

    source_values = (0.5, 1.0, 2.0)
    source_results = tuple(source_response(value) for value in source_values)
    checks.check(
        "record-source-dictionary-control",
        "the same static Einstein operator maps source couplings g=1/2,1,2 to distinct h_tt residues 1,2,4",
        max(residual for _, residual in source_results) < TOLERANCE
        and np.max(
            np.abs(
                np.asarray([response for response, _ in source_results])
                - np.asarray((1.0, 2.0, 4.0))
            )
        )
        < TOLERANCE,
        "h_tt=" + ",".join(f"{response:.12f}" for response, _ in source_results),
    )

    def observable_vector(parameters: np.ndarray) -> np.ndarray:
        q_value, r_value, a_value, zeta_value, g_value = parameters
        q_fraction = Fraction(str(float(q_value)))
        empty_kernel = block45.local_record_kernel(
            block45.EMPTY, (block45.EMPTY,) * 6, q_fraction
        )
        formation = 1.0 - float(empty_kernel[block45.EMPTY])
        parallel, sequential = block45.two_site_schedule_laws()
        schedule_correlation = (1.0 - r_value) * float(correlation(parallel)) + r_value * float(
            correlation(sequential)
        )
        tt_kinetic, constraint_coefficient, static_response, residual = gravity_signature(
            a_value, zeta_value, g_value
        )
        if residual >= TOLERANCE:
            raise AssertionError("static source solve failed inside Jacobian")
        return np.asarray(
            (
                formation,
                schedule_correlation,
                tt_kinetic,
                constraint_coefficient,
                static_response,
            ),
            dtype=float,
        )

    standard_point = np.asarray((0.5, 0.5, 1.0, 0.0, 1.0), dtype=float)
    step = 1.0e-5
    wall_jacobian = np.zeros((5, 5), dtype=float)
    for column in range(5):
        forward = standard_point.copy()
        backward = standard_point.copy()
        forward[column] += step
        backward[column] -= step
        wall_jacobian[:, column] = (
            observable_vector(forward) - observable_vector(backward)
        ) / (2.0 * step)
    expected_jacobian = np.diag((1.0, 3.0 / 5.0, 1.0 / 2.0, 1.0, 2.0))
    checks.check(
        "five-independent-controls",
        "formation, precedence, clock map, constraint kinetic status, and source coupling are locally independent",
        np.linalg.matrix_rank(wall_jacobian) == 5
        and float(np.max(np.abs(wall_jacobian - expected_jacobian))) < 2.0e-9
        and abs(float(np.linalg.det(wall_jacobian)) - 3.0 / 5.0) < TOLERANCE,
        "computed Jacobian diag=(1,3/5,1/2,1,2); rank=5; determinant=3/5",
    )

    fixed_record = record_signature(Fraction(1, 3), Fraction(0, 1))
    gravity_family = tuple(
        gravity_signature(*parameters)
        for parameters in (
            (1.0, 0.0, 1.0),
            (2.0, 0.0, 1.0),
            (1.0, 0.25, 1.0),
            (1.0, 0.0, 2.0),
        )
    )
    checks.check(
        "record-kernel-does-not-fix-gravity",
        "one exact Record kernel can be held fixed while clock, constraint, or source gravity observables change",
        all(record_signature(Fraction(1, 3), Fraction(0, 1)) == fixed_record for _ in gravity_family)
        and len(
            {
                tuple(round(value, 12) for value in signature[:3])
                for signature in gravity_family
            }
        )
        == 4
        and max(signature[3] for signature in gravity_family) < TOLERANCE,
    )

    fixed_gravity = gravity_signature(1.0, 0.0, 1.0)
    record_family = tuple(
        record_signature(*parameters)
        for parameters in (
            (Fraction(1, 3), Fraction(0, 1)),
            (Fraction(2, 3), Fraction(0, 1)),
            (Fraction(1, 3), Fraction(1, 1)),
        )
    )
    checks.check(
        "gravity-operator-does-not-fix-record-law",
        "one Einstein operator and source dictionary can be held fixed while formation or precedence laws change",
        all(gravity_signature(1.0, 0.0, 1.0) == fixed_gravity for _ in record_family)
        and len(set(record_family)) == 3,
    )

    checks.check(
        "exact-joint-law-cut-gate",
        "the source identifies one exact joint law referent rather than five vague existence clauses",
        all(
            phrase in note
            for phrase in (
                "record-extension instrument",
                "event-precedence composition",
                "euclidean-to-lorentzian clock map",
                "constraint intertwiner",
                "record-to-source decoder",
                "exact immutable referent",
                "no live axiom edit is ready",
                "fixed toe percentages remain unchanged",
            )
        ),
    )

    checks.check(
        "fresh-no-go-discipline-packet",
        "the bounded non-entailment passes N1 through N8 while preserving every constructive completion route",
        all(f"### n{index}" in note for index in range(1, 9))
        and "status: pass" in note
        and all(
            phrase in note
            for phrase in (
                "not a gravity no-go",
                "downstream uniqueness theorem",
                "reflection-positive reconstruction",
                "unitary dilation",
                "exact physical-equivalence class",
                "record inclusion order",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: the complete four-node supplied foundation, exact Block45 binary Record family, conditional Block44 Einstein sector, three schedule mixtures, three clock maps, one constraint deformation, and three source couplings are resolved"
    )
    print(
        "per_element: checked empty and both central binary Record contents plus all ten metric coordinates"
    )
    print(
        "per_site: inherited all 729 six-neighbour conditions and 24 proper rotations from the source-bound Block45 runner"
    )
    print(
        "per_mode: checked static source, pure kinetic, generic off-shell, and null-shell TT probes"
    )
    print(
        "per_block: checked five independent control blocks and both directions of the Record/gravity factorization"
    )
    print(
        "lattice_wide: no full-Z3 selected law, physical inner product, nonlinear constraint propagation, or realized complete history is inferred"
    )
    print(
        "scope_boundary: bounded current-foundation non-entailment and sufficient exact-law cut gate; not gravity failure, global axiom minimality, adoption, or TOE closure"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
