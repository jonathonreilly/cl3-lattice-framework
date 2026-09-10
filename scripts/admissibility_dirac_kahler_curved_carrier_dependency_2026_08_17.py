#!/usr/bin/env python3
"""Block 128: finite matrix boundary on one curved-carrier fixture.

The runner constructs two exact chartwise action matrices from the reviewed
Block 105 overlap Hodge. It checks their finite support, one spatial-shift
commutator, raw distance-two blocks, and complete adjacent grouped maps.
It does not perform a Schur elimination or establish transition inequivalence,
a global-action no-go, a universal evolution no-go, or a construction order.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import time

import sympy as sp

import admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14 as block105


R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
LEDGER_PATH = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block128-curved-carrier-dependency-20260817/"
    "NO_GO_LEDGER.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK105_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_"
    "NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK105_RUNNER = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)
BLOCK105_LEDGER = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block105-shifted-origin-frame-gauge-20260814/"
    "NO_GO_LEDGER.md"
)
RECOVERY_ROOT = (
    ".claude/science/physics-loops/released6844-recovery-20260910"
)
BLOCK127_CONTEXT = RECOVERY_ROOT + "/BLOCK127_ROADMAP_CONTEXT.json"
CITATION_SCOPE = RECOVERY_ROOT + "/CITATION_SCOPE.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    ".claude/science/physics-loops/toe-axiom-closure-block128-curved-carrier-dependency-20260817/NO_GO_LEDGER.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    ".claude/science/physics-loops/toe-axiom-closure-block105-shifted-origin-frame-gauge-20260814/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/released6844-recovery-20260910/BLOCK127_ROADMAP_CONTEXT.json",
    ".claude/science/physics-loops/released6844-recovery-20260910/CITATION_SCOPE.json",
)

# Frozen after the corrected source/input/citation preflight. No moving Git ref
# or ancestry condition participates in the scientific result.
INPUT_SHA256 = {
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md": "b3e42b85ff4bd29edd2d3c65bb1685503560af6b512013e062a93601c8661990",
    ".claude/science/physics-loops/toe-axiom-closure-block128-curved-carrier-dependency-20260817/NO_GO_LEDGER.md": "49687a033f2f388bf35ef8de90f9ae73310e2ce9436ae40ad027d40ce7bae8f6",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md": "9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py": "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    ".claude/science/physics-loops/toe-axiom-closure-block105-shifted-origin-frame-gauge-20260814/NO_GO_LEDGER.md": "e92c85ac05cd969ce0f35cf4d0892f5a144f59a98b975586002aefe2e57747c7",
    ".claude/science/physics-loops/released6844-recovery-20260910/BLOCK127_ROADMAP_CONTEXT.json": "18035ecd1d1a0e976350cbc73a6fdff8972c3ac719b2e033654b68fb889c2d86",
    ".claude/science/physics-loops/released6844-recovery-20260910/CITATION_SCOPE.json": "cc236bef1535e04ce457b5034782687e5daebb79de435e741a73e8898bcbc0fb",
}

AUDIT_TIMEOUT_SEC = 60
MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_inequivalence",
    "claim_global_action",
    "break_commutator_rank",
    "break_schur_rank",
    "break_kernel_witness",
    "break_underdetermination",
    "break_regrouping_survival",
    "break_census",
    "claim_differential_impossible",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_axiom_amendment",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        key: str,
        statement: str,
        condition: object,
        detail: str = "",
    ) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def file_sha256(path: str) -> str | None:
    candidate = ROOT / path
    if not candidate.is_file():
        return None
    return hashlib.sha256(candidate.read_bytes()).hexdigest()


def input_certificate(mutation: str) -> dict[str, object]:
    expected = dict(INPUT_SHA256)
    if mutation == "stale_axiom_authority":
        expected[AXIOM_PATH] = "0" * 64
    if mutation == "stale_parent_authority":
        expected[BLOCK105_NOTE] = "0" * 64
    actual = {path: file_sha256(path) for path in AUDIT_INPUT_PATHS}
    loaded_module = Path(block105.__file__).resolve()
    return {
        "matches": tuple(expected) == AUDIT_INPUT_PATHS and actual == expected,
        "actual": actual,
        "expected": expected,
        "loaded_block105": str(loaded_module),
        "loaded_expected_file": loaded_module == (ROOT / BLOCK105_RUNNER).resolve(),
    }


def normalized_note() -> str:
    try:
        return " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    except (FileNotFoundError, OSError, UnicodeError):
        return ""


SPACE_EXTENT = block105.LENGTH
PHYSICAL_TIME_EXTENT = block105.LENGTH
COVER_TIME_EXTENT = 2 * PHYSICAL_TIME_EXTENT
COVER_SIZE = COVER_TIME_EXTENT * SPACE_EXTENT
DISPLAYED_ORIGINS = ((1, 0), (1, 1))
DISPLAYED_STEPS = (1, 3)
FORWARD_DIRECTIONS = (2, -2)
KERNEL_WITNESS = sp.Matrix((0, 1, 0, 0))
S_X = R(3, 5)
S_T = R(4, 5)
MASS = R(2, 7)


def cover_index(time_coordinate: int, space_coordinate: int) -> int:
    return (
        (time_coordinate % COVER_TIME_EXTENT) * SPACE_EXTENT
        + space_coordinate % SPACE_EXTENT
    )


def cover_embedding(time_coordinate: int, space_coordinate: int) -> sp.Matrix:
    matrix = sp.zeros(COVER_SIZE, 4)
    for column, (delta_t, delta_x) in enumerate(
        ((0, 0), (0, 1), (1, 0), (1, 1))
    ):
        matrix[
            cover_index(
                time_coordinate + delta_t,
                space_coordinate + delta_x,
            ),
            column,
        ] = 1
    return matrix


def curved_hodge_cover() -> sp.Matrix:
    """Lift the exact Block 105 overlap Hodge to an unaliased time cover."""
    field = block105.overlap_field()
    result = sp.zeros(COVER_SIZE)
    for time_coordinate in range(COVER_TIME_EXTENT):
        for space_coordinate in range(SPACE_EXTENT):
            shear, volume = field[
                (
                    time_coordinate % PHYSICAL_TIME_EXTENT,
                    space_coordinate,
                )
            ]
            embedding = cover_embedding(time_coordinate, space_coordinate)
            result += (
                embedding
                * block105.shear_hodge(shear, volume)
                * embedding.T
                / 4
            )
    return sp.simplify(result)


def chart_differential_cover(origin: tuple[int, int]) -> sp.Matrix:
    """One displayed chartwise nilpotent choice, not a common differential."""
    local_differential = I * (S_X * block105.EX + S_T * block105.ET)
    result = sp.zeros(COVER_SIZE)
    for coarse_t in range(COVER_TIME_EXTENT // 2):
        for coarse_x in range(SPACE_EXTENT // 2):
            embedding = cover_embedding(
                2 * coarse_t + origin[0],
                2 * coarse_x + origin[1],
            )
            result += embedding * local_differential * embedding.T
    return result


def antiperiodic_quotient(matrix: sp.Matrix) -> sp.Matrix:
    """Fold the two-period cover with psi(t+4)=-psi(t)."""
    identity = sp.eye(PHYSICAL_TIME_EXTENT * SPACE_EXTENT)
    injection = sp.Matrix.vstack(-identity, identity)
    selection = sp.Matrix.hstack(sp.zeros(identity.rows), identity)
    return sp.simplify(selection * matrix * injection)


def grassmann_form(action: sp.Matrix) -> sp.Matrix:
    """Alternating form for one complex Grassmann mode and its conjugate."""
    zero = sp.zeros(action.rows)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(zero, action),
        sp.Matrix.hstack(-action.T, zero),
    )


def time_bands(matrix: sp.Matrix) -> tuple[int, ...]:
    bands: set[int] = set()
    for row in range(matrix.rows):
        row_time = row // SPACE_EXTENT
        for column in range(matrix.cols):
            if matrix[row, column] == 0:
                continue
            raw = (column // SPACE_EXTENT - row_time) % COVER_TIME_EXTENT
            signed = (
                raw
                if raw <= COVER_TIME_EXTENT // 2
                else raw - COVER_TIME_EXTENT
            )
            bands.add(signed)
    return tuple(sorted(bands))


@dataclass(frozen=True)
class CurvedCompletion:
    origin: tuple[int, int]
    differential: sp.Matrix
    cover_action: sp.Matrix
    physical_action: sp.Matrix
    alternating_action: sp.Matrix
    bands: tuple[int, ...]
    commutator_rank: int


def build_completions() -> tuple[CurvedCompletion, CurvedCompletion]:
    hodge = curved_hodge_cover()
    spatial_shift = block105.translation_matrix((0, 1))
    doubled_shift = sp.diag(spatial_shift, spatial_shift)
    completions: list[CurvedCompletion] = []
    for origin in DISPLAYED_ORIGINS:
        differential = chart_differential_cover(origin)
        cover_action = sp.simplify(
            MASS * hodge
            + I * (hodge * differential + differential.H * hodge)
        )
        physical_action = antiperiodic_quotient(cover_action)
        alternating_action = grassmann_form(physical_action)
        completions.append(
            CurvedCompletion(
                origin=origin,
                differential=differential,
                cover_action=cover_action,
                physical_action=physical_action,
                alternating_action=alternating_action,
                bands=time_bands(cover_action),
                commutator_rank=(
                    alternating_action * doubled_shift
                    - doubled_shift * alternating_action
                ).rank(),
            )
        )
    return tuple(completions)  # type: ignore[return-value]


def supplier_fixture_certificate(
    completions: tuple[CurvedCompletion, ...],
) -> bool:
    required = (
        "EX",
        "ET",
        "LENGTH",
        "overlap_field",
        "shear_hodge",
        "translation_matrix",
    )
    field = block105.overlap_field()
    return (
        all(hasattr(block105, name) for name in required)
        and SPACE_EXTENT == 4
        and COVER_TIME_EXTENT == 8
        and len(field) == 16
        and all(
            completion.differential**2 == sp.zeros(COVER_SIZE)
            for completion in completions
        )
    )


def completion_certificate(
    completions: tuple[CurvedCompletion, ...],
) -> dict[str, object]:
    first_difference = sp.simplify(
        completions[1].physical_action[10, 11]
        - completions[0].physical_action[10, 11]
    )
    pairwise_unequal = completions[0].physical_action != completions[1].physical_action
    exact = all(
        all(value.is_Rational is True for value in completion.physical_action)
        for completion in completions
    )
    return {
        "origins": tuple(completion.origin for completion in completions),
        "pairwise_unequal": pairwise_unequal,
        "first_difference": first_difference,
        "pentadiagonal": all(
            completion.bands == (-2, -1, 0, 1, 2)
            for completion in completions
        ),
        "exact": exact,
        "alternating": all(
            completion.alternating_action.T == -completion.alternating_action
            for completion in completions
        ),
    }


def spatial_slice_shift(displacement: int) -> sp.Matrix:
    matrix = sp.zeros(SPACE_EXTENT)
    for source in range(SPACE_EXTENT):
        matrix[(source + displacement) % SPACE_EXTENT, source] = 1
    return matrix


def directional_slice_frame(time_coordinate: int, direction: int) -> sp.Matrix:
    """Frame in which the displayed raw-block witness is e2."""
    if direction == 2:
        displacement = time_coordinate - 2
    elif direction == -2:
        displacement = -time_coordinate - 1
    else:
        raise ValueError("direction must be +2 or -2")
    return spatial_slice_shift(displacement)


def slice_block(
    completion: CurvedCompletion,
    row_time: int,
    column_time: int,
    direction: int,
) -> sp.Matrix:
    row_time %= COVER_TIME_EXTENT
    column_time %= COVER_TIME_EXTENT
    raw = completion.cover_action[
        SPACE_EXTENT * row_time : SPACE_EXTENT * (row_time + 1),
        SPACE_EXTENT * column_time : SPACE_EXTENT * (column_time + 1),
    ]
    return sp.simplify(
        directional_slice_frame(row_time, direction).T
        * raw
        * directional_slice_frame(column_time, direction)
    )


def raw_distance_two_block(
    completion: CurvedCompletion,
    step: int,
    direction: int,
) -> sp.Matrix:
    """A framed raw Q[j,j+direction] block; no elimination is performed."""
    return slice_block(completion, step, step + direction, direction)


def raw_records(
    completions: tuple[CurvedCompletion, ...],
) -> tuple[tuple[tuple[int, int], int, int, sp.Matrix], ...]:
    return tuple(
        (
            completion.origin,
            direction,
            step,
            raw_distance_two_block(completion, step, direction),
        )
        for completion in completions
        for direction in FORWARD_DIRECTIONS
        for step in DISPLAYED_STEPS
    )


def exact_raw_kernel(matrix: sp.Matrix) -> bool:
    return (
        matrix.rank() == 3
        and matrix * KERNEL_WITNESS == sp.zeros(4, 1)
        and matrix.nullspace() == [KERNEL_WITNESS]
    )


def bracketed_forward_blocks(
    completion: CurvedCompletion,
    start: int,
    direction: int,
) -> tuple[tuple[sp.Matrix, sp.Matrix], tuple[sp.Matrix, sp.Matrix]]:
    source_times = (start, start + 1)
    target_times = (
        (start + 2, start + 3)
        if direction == 2
        else (start - 2, start - 1)
    )
    return tuple(
        tuple(
            slice_block(completion, source, target, direction)
            for target in target_times
        )
        for source in source_times
    )  # type: ignore[return-value]


def complete_grouped_map(
    completion: CurvedCompletion,
    start: int,
    direction: int,
) -> sp.Matrix:
    blocks = bracketed_forward_blocks(completion, start, direction)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(*blocks[0]),
        sp.Matrix.hstack(*blocks[1]),
    )


@dataclass(frozen=True)
class GroupedRecord:
    origin: tuple[int, int]
    direction: int
    step: int
    start: int
    matrix: sp.Matrix
    embedded_witness: sp.Matrix
    residual: sp.Matrix


def grouped_records(
    completions: tuple[CurvedCompletion, ...],
) -> tuple[GroupedRecord, ...]:
    result: list[GroupedRecord] = []
    zero = sp.zeros(4, 1)
    for completion in completions:
        for direction in FORWARD_DIRECTIONS:
            for step in DISPLAYED_STEPS:
                for start in (step - 1, step):
                    matrix = complete_grouped_map(completion, start, direction)
                    witness = (
                        sp.Matrix.vstack(KERNEL_WITNESS, zero)
                        if start == step
                        else sp.Matrix.vstack(zero, KERNEL_WITNESS)
                    )
                    result.append(
                        GroupedRecord(
                            origin=completion.origin,
                            direction=direction,
                            step=step,
                            start=start,
                            matrix=matrix,
                            embedded_witness=witness,
                            residual=matrix * witness,
                        )
                    )
    return tuple(result)


N5_LINES = (
    "N5: per_element: checked — two displayed 16x16 physical matrices differ at entry (10,11) by exact -89/140; no transition equivalence is tested",
    "per_site: checked — the doubled alternating form represents one complex Grassmann mode and its conjugate at each of 16 physical sites, not two site modes",
    "per_mode: checked — rank[Q_alt,Sx⊕Sx]=32 for each displayed matrix, so this spatial-shift eigenspace reduction is not invariant; other spectral descriptions are open",
    "per_block: checked — eight raw framed distance-two 4x4 blocks have rank3 and kernel e2; sixteen full adjacent 8x8 maps have ranks3/4, and the embedded e2 witness fails in six",
    "lattice_wide: checked and not executed — no common differential, transition law, true Schur elimination, descriptor evolution, direct Gram OS proof, ADM/history transporter, joint gravity, Records, or TOE closure is constructed",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    forbidden = (
        "no global curved action exists",
        "the dependency is exact",
        "the proven bottleneck",
        "pairwise inequivalent",
        "survives every displayed regrouping",
        "everything downstream undefined",
        "reject curved-os attempts",
        "audited_conditional expected",
    )
    result = {
        "raw_not_schur": (
            "raw distance-two" in note and "not a schur complement" in note
        ),
        "matrix_boundary": (
            "matrix inequality alone is silent" in note
            and "absence of a global curved action" in note
        ),
        "full_grouped_control": (
            "sixteen complete adjacent" in note
            and "9/80" in note
            and "10 zero, 6 nonzero" in note
        ),
        "no_order_theorem": "no universal dependency-order theorem" in note,
        "alternatives_open": all(
            phrase in note
            for phrase in (
                "descriptor",
                "enlarged-state",
                "direct-gram",
                "other curved fixtures",
            )
        ),
        "no_forbidden_live_claim": not any(phrase in note for phrase in forbidden),
        "audit_deferred": "formal audit remains deferred" in note,
        "no_axiom": "no action, axiom, premise, or primitive is adopted" in note,
        "toe_unchanged": (
            "zero obligation retirement" in note
            and "no toe percentage moves" in note
        ),
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "original_no_go_fails": (
            "original w1 no-go" in note
            and "partial narrowing" in note
            and "no no-go packet pass is claimed" in note
        ),
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
    }
    if mutation == "claim_global_action":
        result["matrix_boundary"] = False
    if mutation == "claim_differential_impossible":
        result["no_order_theorem"] = False
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
        result["original_no_go_fails"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_toe_progress":
        result["toe_unchanged"] = False
    if mutation == "claim_axiom_amendment":
        result["no_axiom"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    inputs = input_certificate(mutation)
    checks.check(
        "A-source-inputs",
        "literal filesystem inputs and the loaded Block105 module match frozen SHA-256 bindings",
        inputs["matches"] and inputs["loaded_expected_file"],
        f"paths={len(AUDIT_INPUT_PATHS)}; moving refs=0; ancestry gates=0",
    )

    completions = build_completions()
    completion = completion_certificate(completions)
    displayed_raw = (
        supplier_fixture_certificate(completions)
        and completion["origins"] == DISPLAYED_ORIGINS
        and completion["pairwise_unequal"]
        and completion["first_difference"] == -R(89, 140)
        and completion["pentadiagonal"]
        and completion["exact"]
        and completion["alternating"]
    )
    displayed_gate = displayed_raw
    if mutation == "break_inequivalence":
        displayed_gate = False
    checks.check(
        "B-displayed-matrix-facts",
        "two exact displayed matrices are unequal by -89/140 and retain five time bands",
        displayed_gate,
        "matrix inequality is not a transition-equivalence or global-action test",
    )

    commutator_ranks = tuple(item.commutator_rank for item in completions)
    translation_raw = commutator_ranks == (32, 32)
    translation_gate = (
        False if mutation == "break_commutator_rank" else translation_raw
    )
    checks.check(
        "C-spatial-shift-sector-control",
        "both displayed alternating matrices have doubled-shift commutator rank 32",
        translation_gate,
        "only this spatial-shift eigenspace reduction is excluded",
    )

    raw = raw_records(completions)
    raw_rank = len(raw) == 8 and all(
        matrix.rank() == 3 for _, _, _, matrix in raw
    )
    raw_kernel = all(exact_raw_kernel(matrix) for _, _, _, matrix in raw)
    raw_gate = raw_rank and raw_kernel
    if mutation in ("break_schur_rank", "break_kernel_witness"):
        raw_gate = False
    checks.check(
        "D-raw-distance-two-blocks",
        "eight framed raw 4x4 Q[j,j±2] blocks have rank 3 and coordinate kernel e2",
        raw_gate,
        "no Schur elimination or complete next-state equation is computed",
    )

    grouped = grouped_records(completions)
    rank_counts = Counter(record.matrix.rank() for record in grouped)
    zero = sp.zeros(8, 1)
    zero_count = sum(record.residual == zero for record in grouped)
    counterexample = next(
        record
        for record in grouped
        if record.origin == (1, 0)
        and record.direction == 2
        and record.step == 1
        and record.start == 1
    )
    expected_counterexample = sp.Matrix(
        (0, 0, 0, 0, R(9, 80), 0, 0, 0)
    )
    grouped_raw = (
        len(grouped) == 16
        and rank_counts == Counter({4: 12, 3: 4})
        and zero_count == 10
        and counterexample.residual == expected_counterexample
    )
    grouped_gate = (
        False if mutation == "break_regrouping_survival" else grouped_raw
    )
    checks.check(
        "E-full-grouped-control",
        "sixteen complete 8x8 maps have ranks 3/4 and disprove universal embedded-e2 survival",
        grouped_gate,
        "embedded witness: zero=10, nonzero=6; exact counterexample component=9/80",
    )

    finite_census_raw = (
        displayed_raw
        and translation_raw
        and raw_rank
        and raw_kernel
        and grouped_raw
    )
    finite_census_gate = finite_census_raw
    if mutation in ("break_underdetermination", "break_census"):
        finite_census_gate = False
    checks.check(
        "F-bounded-census",
        "finite support, shift, raw-block, and full-group results are kept without a pipeline theorem",
        finite_census_gate,
        "legacy underdetermination mutation is guard-only; no next-state family is claimed",
    )

    note = normalized_note()
    scope = scope_certificate(note, mutation)
    boundary_keys = (
        "raw_not_schur",
        "matrix_boundary",
        "full_grouped_control",
        "no_order_theorem",
        "alternatives_open",
        "no_forbidden_live_claim",
    )
    checks.check(
        "G-open-construction-boundary",
        "transition, common descent, descriptors, direct Gram OS, and other fixtures remain open",
        all(scope[key] for key in boundary_keys),
        "Block127 is roadmap history; no independent wall count is claimed",
    )

    packet_keys = (
        "audit_deferred",
        "no_axiom",
        "toe_unchanged",
        "n1_n8",
        "original_no_go_fails",
        "n5_resolution",
    )
    checks.check(
        "H-scope-and-no-go-discipline",
        "the original W1 no-go fails; the live result is a finite partial narrowing",
        all(scope[key] for key in packet_keys)
        and time.monotonic() - started <= 50,
        "no audit status, premise adoption, obligation retirement, or TOE movement",
    )

    print("INPUT_BINDINGS: " + json.dumps(inputs["actual"], sort_keys=True))
    print(
        "FIXTURE: cover=(time8,space4); quotient=time4 antiperiodic; "
        "origins=((1,0),(1,1)); mass=2/7; weights=(3/5,4/5); "
        "directions=(+2,-2); steps=(1,3)"
    )
    print(
        "DISPLAYED_MATRICES: unequal entry difference=-89/140; "
        "time_bands=(-2,-1,0,1,2); transition_equivalence=NOT_TESTED"
    )
    print(
        "TRANSLATION: rank[Q_alt,Sx⊕Sx]=(32,32); "
        "only this shift-sector reduction is excluded"
    )
    print(
        "RAW_DISTANCE_TWO: count=8; shape=4x4; ranks=3; "
        "framed_kernel=e2; Schur_elimination=NOT_PERFORMED"
    )
    print(
        "GROUPED_FULL: count=16; shape=8x8; rank3=4; rank4=12; "
        "embedded_e2_zero=10; embedded_e2_nonzero=6"
    )
    print(
        "COUNTEREXAMPLE: origin=(1,0); direction=+2; step=1; start=1; "
        "G*(e2,0)=(0,0,0,0,9/80,0,0,0)"
    )
    for line in N5_LINES:
        print(line)
    print(
        "RESULT: exact finite matrix boundary only; no transition "
        "inequivalence, global-action no-go, evolution no-go, or universal "
        "dependency order"
    )
    print(
        "OPEN: common descent; transition law; true Schur or descriptor "
        "formulation; constraints; enlarged state; direct Gram OS; other "
        "groupings; other curved fixtures"
    )
    print(
        "AUDIT: none; formal audit deferred; zero obligation retirement; "
        "no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
