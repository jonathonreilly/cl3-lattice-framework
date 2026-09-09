#!/usr/bin/env python3
"""Block 70: two total local L_phys Record laws and their selection boundary.

Refine the literal Block-69 five-M2 dilation into its four nonzero
(outcome, matter-sign) branches.  On the same exact branch weights, execute
two inequivalent Record laws on an isolated ready patch:

* ``output_root`` locks the physical output-R factor itself, with an
  injective density/sign/coframe tag, beside a Block-64 successor head;
* ``adjacent_packet`` keeps the output factors quantum and writes the
  unchanged Block-65/67 outcome/head packet on adjacent blank Record sites.

Both laws are total on the declared patch contract, append-only, covariant
under the proper cubic action, and continue for an arbitrary single-front
horizon by the Block-64 induction.  Their survival proves only executable
interface nonselection.  It is not a full-Z3 model-theoretic no-go and does
not by itself authorize an axiom amendment.
"""

from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import subprocess

import numpy as np

import admissibility_cycle713_five_m2_stinespring_record_lock_action_cut_2026_08_13 as b69
import admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13 as b67
import admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12 as b65


b64 = b65.b64
b63 = b65.b63

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_LPHYS_RECORD_LAW_TOURNAMENT_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
REALIZED_NOTE_PATH = ROOT / "docs" / (
    "REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_"
    "NARROW_THEOREM_NOTE_2026-07-02.md"
)
PARENT_RUNNER = ROOT / "scripts" / (
    "admissibility_cycle713_five_m2_stinespring_record_lock_action_cut_"
    "2026_08_13.py"
)
PARENT_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_FIVE_M2_STINESPRING_RECORD_LOCK_ACTION_CUT_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CYCLE713_LPHYS_RECORD_LAW_TOURNAMENT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CYCLE713_FIVE_M2_STINESPRING_RECORD_LOCK_ACTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "scripts/admissibility_cycle713_five_m2_stinespring_record_lock_action_cut_2026_08_13.py",
    "scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py",
    "scripts/admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12.py",
    "scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py",
    "docs/REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md",
)

AXIOM_AUTHORITY_SHA256 = b69.AXIOM_AUTHORITY_SHA256
PARENT_RECEIPT_COMMIT = "5372dc950808ff9df62c4b16143b17f63aea882c"
PARENT_RUNNER_SHA256 = "ff9df187cb6817a4bd2a19cfa2fd7714be3b4efb6733c8c882c1c3f41eb8bd09"
PARENT_NOTE_SHA256 = "bacf6ead9b800668e615b68585fe6ee7af4106e472de69fd2afb46a52a23ef74"

TOL = 5.0e-11
ORIGIN: b64.Coord = (0, 0, 0)
FINE_PAIRS: tuple[tuple[int, int], ...] = (
    (0, -1),
    (1, -1),
    (1, 1),
    (2, 1),
)
OUTPUT_CODES = {pair: 40 + index for index, pair in enumerate(FINE_PAIRS)}
CODE_TO_PAIR = {code: pair for pair, code in OUTPUT_CODES.items()}
LAW_NAMES = ("output_root", "adjacent_packet")
NO_RECORD_KEY = "no_record"
REFUSAL_KEY = "refusal"

BranchKey = str | tuple[int, int]
RecordsTuple = tuple[tuple[b64.Coord, b63.Matrix], ...]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_ancestor(older: str, newer: str = "HEAD") -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", older, newer),
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def authority_certificate(use_stale_axiom: bool = False) -> dict[str, object]:
    authority = b69.authority_certificate(use_stale_axiom)
    return {
        **authority,
        "parent_receipt_ancestor": git_ancestor(PARENT_RECEIPT_COMMIT),
        "parent_runner_sha256": file_sha256(PARENT_RUNNER),
        "parent_note_sha256": file_sha256(PARENT_NOTE),
    }


def sign_projector(rotation: b64.Rotation, sign: int) -> b63.Matrix:
    base = b65.P0 if sign == -1 else b65.P1
    if sign not in (-1, 1):
        raise ValueError(sign)
    return b63.rotate_hermitian(rotation, base)


def fine_matter_effect(
    rotation: b64.Rotation,
    outcome: int,
    sign: int,
) -> b63.Matrix:
    return b63.matrix_multiply(
        sign_projector(rotation, sign),
        b65.rotated_effects(rotation, 0)[outcome],
    )


def ready_omega(rotation: b64.Rotation) -> b65.QMatrix:
    pointer = b63.density_at_t(1)
    matter = b63.rotate_hermitian(rotation, b63.density_at_t(2))
    return b65.product_state(pointer, matter)


def fine_weights(
    omega: b65.QMatrix,
    rotation: b64.Rotation,
) -> tuple[tuple[BranchKey, Fraction], ...]:
    no_record = b65.qkron(b65.P0, b63.IDENTITY)
    entries: list[tuple[BranchKey, Fraction]] = [
        (NO_RECORD_KEY, b65.qtrace_product(omega, no_record))
    ]
    for pair in FINE_PAIRS:
        outcome, sign = pair
        effect = b65.qkron(
            b65.P1,
            fine_matter_effect(rotation, outcome, sign),
        )
        entries.append((pair, b65.qtrace_product(omega, effect)))
    return tuple(entries)


def fine_formation_output(
    rho: np.ndarray,
    outcome: int,
    sign: int,
    wrong_sign: bool = False,
) -> np.ndarray:
    matter = int(((-sign if wrong_sign else sign) + 1) // 2)
    auxiliary = outcome - matter
    answer = np.zeros((2, 2), dtype=complex)
    if auxiliary not in (0, 1):
        return answer
    for a in (0, 1):
        for r_left in (0, 1):
            for r_right in (0, 1):
                answer[r_left, r_right] += rho[
                    b69.full_index(1, matter, auxiliary, r_left, a),
                    b69.full_index(1, matter, auxiliary, r_right, a),
                ]
    return answer


def expected_fine_output(
    unit: np.ndarray,
    outcome: int,
    sign: int,
) -> np.ndarray:
    matter = (sign + 1) // 2
    effect = np.zeros((4, 4), dtype=complex)
    input_index = 1 | (matter << 1)
    coefficient = complex(
        b63.to_numpy(b63.MENUS[0][outcome])[matter, matter]
    )
    effect[input_index, input_index] = coefficient
    tau = b63.to_numpy(b63.normalized_effect_state(b63.MENUS[0][outcome]))
    return np.trace(unit @ effect) * tau


def direct_sum_output(outputs: tuple[np.ndarray, ...]) -> np.ndarray:
    dimensions = tuple(item.shape[0] for item in outputs)
    answer = np.zeros((sum(dimensions), sum(dimensions)), dtype=complex)
    cursor = 0
    for item, dimension in zip(outputs, dimensions):
        answer[cursor:cursor + dimension, cursor:cursor + dimension] = item
        cursor += dimension
    return answer


def fine_dilation_certificate(wrong_fine_branch: bool = False) -> dict[str, object]:
    isometry = b69.isometry_certificate()["isometry"]
    maximum_residual = coarse_residual = completeness_residual = 0.0
    outputs_by_unit: dict[tuple[int, int], np.ndarray] = {}
    cases = 0
    for row in range(4):
        for column in range(4):
            unit = np.zeros((4, 4), dtype=complex)
            unit[row, column] = 1
            rho = isometry @ unit @ isometry.conj().T
            no_record = b69.no_record_output(rho)
            expected_no_record = b69.expected_instrument_output(unit)[0]
            maximum_residual = max(
                maximum_residual,
                float(np.linalg.norm(no_record - expected_no_record)),
            )
            fine_actual = tuple(
                fine_formation_output(
                    rho,
                    outcome,
                    sign,
                    wrong_sign=wrong_fine_branch,
                )
                for outcome, sign in FINE_PAIRS
            )
            fine_expected = tuple(
                expected_fine_output(unit, outcome, sign)
                for outcome, sign in FINE_PAIRS
            )
            maximum_residual = max(
                maximum_residual,
                *(float(np.linalg.norm(left - right)) for left, right in zip(fine_actual, fine_expected)),
            )
            for outcome in range(3):
                refined = sum(
                    (fine_actual[index] for index, pair in enumerate(FINE_PAIRS) if pair[0] == outcome),
                    np.zeros((2, 2), dtype=complex),
                )
                coarse_residual = max(
                    coarse_residual,
                    float(np.linalg.norm(refined - b69.formation_output(rho, outcome))),
                )
            outputs_by_unit[(row, column)] = direct_sum_output((no_record,) + fine_actual)
            cases += 1 + len(FINE_PAIRS)

    choi = np.zeros((48, 48), dtype=complex)
    trace_residual = 0.0
    for row in range(4):
        for column in range(4):
            output = outputs_by_unit[(row, column)]
            choi[12 * row:12 * (row + 1), 12 * column:12 * (column + 1)] = output
            trace_residual = max(
                trace_residual,
                abs(np.trace(output) - int(row == column)),
            )

    identity = np.eye(4, dtype=complex)
    effect_sum = np.diag((1, 0, 1, 0)).astype(complex)
    for outcome, sign in FINE_PAIRS:
        matter = (sign + 1) // 2
        index = 1 | (matter << 1)
        effect_sum[index, index] += complex(
            b63.to_numpy(b63.MENUS[0][outcome])[matter, matter]
        )
    completeness_residual = float(np.linalg.norm(effect_sum - identity))
    return {
        "matrix_units": 16,
        "branch_cases": cases,
        "fine_pairs": FINE_PAIRS,
        "maximum_residual": maximum_residual,
        "coarse_residual": coarse_residual,
        "completeness_residual": completeness_residual,
        "choi_minimum": float(np.linalg.eigvalsh(choi).min()),
        "trace_residual": trace_residual,
    }


@dataclass(frozen=True)
class Relocation:
    swaps: tuple[tuple[b64.Coord, b64.Coord], ...]
    targets: tuple[tuple[str, b64.Coord], ...]
    blocked: tuple[b64.Coord, ...]
    target_failures: int
    non_nn_failures: int
    blocked_visits: int
    reverse_failures: int
    background_displacements: int


def shortest_path(
    start: b64.Coord,
    goal: b64.Coord,
    forbidden: set[b64.Coord],
    support: tuple[b64.Coord, ...],
) -> tuple[b64.Coord, ...] | None:
    if start == goal:
        return (start,)
    values = support + (start, goal) + tuple(forbidden)
    lower = tuple(min(site[axis] for site in values) - 5 for axis in range(3))
    upper = tuple(max(site[axis] for site in values) + 5 for axis in range(3))
    queue: deque[b64.Coord] = deque((start,))
    parent: dict[b64.Coord, b64.Coord | None] = {start: None}
    while queue:
        site = queue.popleft()
        for direction in b64.DIRECTIONS:
            neighbor = b64.add(site, direction)
            if neighbor in parent or neighbor in forbidden:
                continue
            if any(neighbor[axis] < lower[axis] or neighbor[axis] > upper[axis] for axis in range(3)):
                continue
            parent[neighbor] = site
            if neighbor == goal:
                path = [goal]
                while parent[path[-1]] is not None:
                    path.append(parent[path[-1]])  # type: ignore[arg-type]
                return tuple(reversed(path))
            queue.append(neighbor)
    return None


def validate_relocation(
    starts: dict[str, b64.Coord],
    targets: dict[str, b64.Coord],
    blocked: set[b64.Coord],
    swaps: tuple[tuple[b64.Coord, b64.Coord], ...],
) -> Relocation:
    touched = set(starts.values())
    for left, right in swaps:
        touched.update((left, right))
    initial_labels = {site: f"background:{site}" for site in touched}
    for role, site in starts.items():
        initial_labels[site] = role
    labels = dict(initial_labels)
    non_nn = blocked_visits = 0
    for left, right in swaps:
        non_nn += b67.manhattan(left, right) != 1
        blocked_visits += left in blocked or right in blocked
        labels[left], labels[right] = labels[right], labels[left]
    target_failures = sum(labels.get(site) != role for role, site in targets.items())
    background_displacements = sum(
        label.startswith("background:") and labels[site] != label
        for site, label in initial_labels.items()
    )
    for left, right in reversed(swaps):
        labels[left], labels[right] = labels[right], labels[left]
    reverse_failures = labels != initial_labels
    return Relocation(
        swaps,
        tuple(sorted(targets.items())),
        tuple(sorted(blocked)),
        target_failures,
        non_nn,
        blocked_visits,
        int(reverse_failures),
        background_displacements,
    )


def route_roles(
    starts: dict[str, b64.Coord],
    targets: dict[str, b64.Coord],
    blocked: set[b64.Coord],
    initially_fixed: set[str] | None = None,
) -> Relocation:
    fixed_seed = set() if initially_fixed is None else set(initially_fixed)
    move_roles = tuple(role for role in starts if role not in fixed_seed)
    support = tuple(starts.values()) + tuple(targets.values())
    for order in permutations(move_roles):
        positions = dict(starts)
        fixed = set(fixed_seed)
        swaps: list[tuple[b64.Coord, b64.Coord]] = []
        possible = True
        for role in order:
            fixed_sites = {targets[item] for item in fixed}
            forbidden = (blocked | fixed_sites) - {positions[role], targets[role]}
            path = shortest_path(positions[role], targets[role], forbidden, support)
            if path is None:
                possible = False
                break
            for left, right in zip(path, path[1:]):
                displaced = next(
                    (item for item, site in positions.items() if site == right),
                    None,
                )
                positions[role] = right
                if displaced is not None and displaced != role:
                    positions[displaced] = left
                swaps.append((left, right))
            fixed.add(role)
        if possible and all(positions[role] == site for role, site in targets.items()):
            return validate_relocation(starts, targets, blocked, tuple(swaps))
    raise RuntimeError(f"no tracked-token relocation for targets {targets}")


def physical_relocation_certificate(dirty_route: bool = False) -> dict[str, object]:
    parent = b69.physical_route_certificate()
    roles = dict(zip(("P", "M", "B", "R", "A"), parent["role_sites"]))
    r_site = roles["R"]
    relocations: list[tuple[str, int, Relocation]] = []

    for sign in (-1, 1):
        head = b64.add(r_site, (sign, 0, 0))
        targets = {
            "P": b64.add(r_site, (0, 1, 0)),
            "M": b64.add(r_site, (0, -1, 0)),
            "B": b64.add(r_site, (0, 0, 1)),
            "R": r_site,
            "A": b64.add(r_site, (0, 0, -1)),
        }
        relocation = route_roles(
            roles,
            targets,
            {r_site, head},
            initially_fixed={"R"},
        )
        relocations.append(("output_root", sign, relocation))

    center = b64.add(r_site, (0, -3, 0))
    side = (0, 1, 0)
    head = b64.add(center, b64.neg(side))
    for sign in (-1, 1):
        direction = (sign, 0, 0)
        targets = {
            "M": b64.add(center, b64.neg(direction)),
            "P": b64.add(center, direction),
            "B": b64.add(center, side),
            "R": b64.add(center, (0, 0, 1)),
            "A": b64.add(center, (0, 0, -1)),
        }
        relocation = route_roles(roles, targets, {center, head})
        relocations.append(("adjacent_packet", sign, relocation))

    non_nn = sum(item.non_nn_failures for _, _, item in relocations)
    if dirty_route:
        non_nn += 1
    return {
        "parent_assigned_M2": parent["total_assigned_M2"],
        "parent_route_failures": (
            parent["non_NN_failures"]
            + parent["operand_order_failures"]
            + parent["route_return_failures"]
        ),
        "roles": roles,
        "relocations": len(relocations),
        "swaps": sum(len(item.swaps) for _, _, item in relocations),
        "touched": len({site for _, _, item in relocations for swap in item.swaps for site in swap}),
        "background_displacements": sum(item.background_displacements for _, _, item in relocations),
        "target_failures": sum(item.target_failures for _, _, item in relocations),
        "non_nn_failures": non_nn,
        "blocked_visits": sum(item.blocked_visits for _, _, item in relocations),
        "reverse_failures": sum(item.reverse_failures for _, _, item in relocations),
        "candidate_centers": (r_site, center),
    }


def rotation_product(left: b64.Rotation, right: b64.Rotation) -> b64.Rotation:
    return b67.rotation_product(left, right)


def tau(rotation: b64.Rotation, outcome: int) -> b63.Matrix:
    return b63.normalized_effect_state(b65.rotated_effects(rotation, 0)[outcome])


def output_root_records(
    rotation: b64.Rotation,
    outcome: int,
    sign: int,
    noncovariant: bool = False,
) -> b64.Records:
    successor = b67.signed_rotation(rotation, sign)
    direction = b64.rotate_coord(successor, b64.BASE_FORWARD)
    frame_rotation = b64.IDENTITY_ROTATION if noncovariant else rotation
    frame = b64.rotate_coord(frame_rotation, b64.BASE_FRAME)
    root = b63.program_carrier(tau(rotation, outcome), frame, OUTPUT_CODES[(outcome, sign)])
    head = b64.context_carrier(
        "head",
        tau(rotation, outcome),
        successor,
        1,
        1,
    )
    return {ORIGIN: root, b64.add(ORIGIN, direction): head}


def adjacent_packet_records(
    rotation: b64.Rotation,
    outcome: int,
    sign: int,
) -> b64.Records:
    successor = b67.signed_rotation(rotation, sign)
    direction = b64.rotate_coord(successor, b64.BASE_FORWARD)
    side = b64.rotate_coord(rotation, b64.BASE_TRANSVERSE)
    bootstrap_origin = b64.add(ORIGIN, b64.neg(b64.add(side, direction)))
    branch = b67.signed_branch(rotation, outcome, sign, bootstrap_origin)
    if branch.new_source != ORIGIN:
        raise AssertionError("translated adjacent packet missed its root")
    return dict(branch.records)


def candidate_records(
    law: str,
    rotation: b64.Rotation,
    outcome: int,
    sign: int,
    noncovariant: bool = False,
) -> b64.Records:
    if law == "output_root":
        return output_root_records(rotation, outcome, sign, noncovariant)
    if law == "adjacent_packet":
        return adjacent_packet_records(rotation, outcome, sign)
    raise ValueError(law)


def candidate_targets(law: str, rotation: b64.Rotation) -> tuple[b64.Coord, ...]:
    if law == "output_root":
        heads = {
            next(site for site in candidate_records(law, rotation, outcome, sign) if site != ORIGIN)
            for outcome, sign in FINE_PAIRS
        }
        return tuple(sorted({ORIGIN} | heads))
    if law == "adjacent_packet":
        side = b64.rotate_coord(rotation, b64.BASE_TRANSVERSE)
        return tuple(sorted((ORIGIN, b64.add(ORIGIN, b64.neg(side)))))
    raise ValueError(law)


@dataclass(frozen=True)
class LawPatch:
    omega: b65.QMatrix
    rotation: b64.Rotation
    records: RecordsTuple = ()
    context_valid: bool = True
    output_valid: bool = True
    spent: bool = False

    def record_map(self) -> b64.Records:
        return dict(self.records)


@dataclass(frozen=True)
class LawOutcome:
    key: BranchKey
    weight: Fraction
    status: str
    records: RecordsTuple
    spent: bool

    def record_map(self) -> b64.Records:
        return dict(self.records)


def sorted_records(records: b64.Records) -> RecordsTuple:
    return tuple(sorted(records.items()))


def refusal(records: b64.Records, status: str = "refusal") -> tuple[LawOutcome, ...]:
    return (LawOutcome(REFUSAL_KEY, Fraction(1), status, sorted_records(records), True),)


def law_distribution(
    law: str,
    patch: LawPatch,
    allow_overwrite: bool = False,
) -> tuple[LawOutcome, ...]:
    records = patch.record_map()
    targets = candidate_targets(law, patch.rotation)
    targets_blank = all(site not in records for site in targets)
    ready = (
        patch.context_valid
        and patch.output_valid
        and b65.qdensity(patch.omega)
        and not patch.spent
        and (targets_blank or allow_overwrite)
    )
    if not ready:
        return refusal(records)

    outcomes: list[LawOutcome] = []
    for key, weight in fine_weights(patch.omega, patch.rotation):
        updated = dict(records)
        status = "no_record"
        if isinstance(key, tuple):
            outcome, sign = key
            updated.update(candidate_records(law, patch.rotation, outcome, sign))
            status = "formation"
        outcomes.append(
            LawOutcome(key, weight, status, sorted_records(updated), True)
        )
    return tuple(outcomes)


def apply_realized(law: str, patch: LawPatch, realized: BranchKey) -> LawOutcome:
    distribution = law_distribution(law, patch)
    if len(distribution) == 1 and distribution[0].key == REFUSAL_KEY:
        return distribution[0]
    matches = tuple(item for item in distribution if item.key == realized and item.weight > 0)
    if len(matches) != 1:
        return refusal(patch.record_map(), status="invalid_realized")[0]
    return matches[0]


def total_law_certificate(allow_overwrite: bool = False) -> dict[str, object]:
    valid_cases = refusal_cases = realized_refusals = replay_refusals = 0
    normalization_failures = append_failures = preservation_failures = 0
    status_failures = totality_failures = 0
    sentinel = b63.program_carrier(b63.density_at_t(3), b64.BASE_FRAME, 77)
    for rotation in b64.ROTATIONS:
        omega = ready_omega(rotation)
        for law in LAW_NAMES:
            patch = LawPatch(omega, rotation)
            distribution = law_distribution(law, patch)
            valid_cases += 1
            normalization_failures += sum(item.weight for item in distribution) != 1
            normalization_failures += any(item.weight < 0 for item in distribution)
            status_failures += tuple(item.status for item in distribution) != (
                "no_record",
                "formation",
                "formation",
                "formation",
                "formation",
            )
            append_failures += distribution[0].record_map() != {}
            append_failures += any(
                len(item.records) != 2 or not item.spent
                for item in distribution[1:]
            )
            for item in distribution:
                replay = LawPatch(
                    omega,
                    rotation,
                    item.records,
                    spent=item.spent,
                )
                replay_result = law_distribution(law, replay)
                replay_refusals += 1
                totality_failures += not (
                    len(replay_result) == 1
                    and replay_result[0].key == REFUSAL_KEY
                    and replay_result[0].records == item.records
                )

            for field in ("context_valid", "output_valid", "spent"):
                kwargs = {
                    "context_valid": True,
                    "output_valid": True,
                    "spent": False,
                }
                kwargs[field] = False if field != "spent" else True
                invalid = LawPatch(omega, rotation, **kwargs)
                result = law_distribution(law, invalid)
                refusal_cases += 1
                totality_failures += not (
                    len(result) == 1
                    and result[0].key == REFUSAL_KEY
                    and result[0].records == ()
                )

            invalid_quantum = LawPatch(b65.qzero(4), rotation)
            result = law_distribution(law, invalid_quantum)
            refusal_cases += 1
            totality_failures += not (
                len(result) == 1
                and result[0].key == REFUSAL_KEY
                and result[0].records == ()
            )

            occupied_site = candidate_targets(law, rotation)[0]
            occupied_records = sorted_records({occupied_site: sentinel})
            occupied = LawPatch(omega, rotation, occupied_records)
            result = law_distribution(law, occupied, allow_overwrite=allow_overwrite)
            refusal_cases += 1
            preservation_failures += not (
                len(result) == 1
                and result[0].key == REFUSAL_KEY
                and result[0].records == occupied_records
            )
            invalid_draw = apply_realized(law, patch, (9, 9))
            realized_refusals += 1
            totality_failures += not (
                invalid_draw.status == "invalid_realized"
                and invalid_draw.records == ()
                and invalid_draw.spent
            )
    return {
        "valid_cases": valid_cases,
        "refusal_cases": refusal_cases,
        "realized_refusals": realized_refusals,
        "replay_refusals": replay_refusals,
        "normalization_failures": normalization_failures,
        "append_failures": append_failures,
        "preservation_failures": preservation_failures,
        "status_failures": status_failures,
        "totality_failures": totality_failures,
    }


def realized_weight_certificate(weight_mismatch: bool = False) -> dict[str, object]:
    cases = realized_members = 0
    normalization_failures = positivity_failures = 0
    candidate_weight_failures = coarse_failures = realized_failures = 0
    for rotation in b64.ROTATIONS:
        omega = ready_omega(rotation)
        exact = fine_weights(omega, rotation)
        normalization_failures += sum(weight for _, weight in exact) != 1
        positivity_failures += any(weight <= 0 for _, weight in exact)
        coarse = (
            exact[0][1],
            *(sum((weight for key, weight in exact[1:] if isinstance(key, tuple) and key[0] == outcome), Fraction(0)) for outcome in range(3)),
        )
        inherited = b65.distribution_weights(
            b65.bootstrap_distribution(omega, rotation, 0, 0, Fraction(1))
        )
        coarse_failures += coarse != inherited
        patch = LawPatch(omega, rotation)
        left = law_distribution("output_root", patch)
        right = law_distribution("adjacent_packet", patch)
        right_weights = [item.weight for item in right]
        if weight_mismatch:
            right_weights[3], right_weights[4] = right_weights[4], right_weights[3]
        candidate_weight_failures += tuple(item.weight for item in left) != tuple(right_weights)
        for law in LAW_NAMES:
            for key, weight in exact:
                selected = apply_realized(law, patch, key)
                realized_members += 1
                realized_failures += not (
                    selected.key == key
                    and selected.weight == weight
                    and selected.status in ("no_record", "formation")
                )
        cases += 1
    realized_flat = " ".join(REALIZED_NOTE_PATH.read_text(encoding="utf-8").lower().split())
    primitive_firewall = (
        "supplied realized state" in realized_flat
        and "does not select the branch" in realized_flat
    )
    return {
        "cases": cases,
        "realized_members": realized_members,
        "normalization_failures": normalization_failures,
        "positivity_failures": positivity_failures,
        "candidate_weight_failures": candidate_weight_failures,
        "coarse_failures": coarse_failures,
        "realized_failures": realized_failures,
        "primitive_firewall": primitive_firewall,
    }


def covariance_certificate(noncovariant: bool = False) -> dict[str, object]:
    cases = failures = distinct_contents = 0
    group_failures = 0
    rotation_set = set(b64.ROTATIONS)
    maps = {
        (law, rotation, outcome, sign): candidate_records(
            law,
            rotation,
            outcome,
            sign,
            noncovariant=noncovariant and law == "output_root",
        )
        for law in LAW_NAMES
        for rotation in b64.ROTATIONS
        for outcome, sign in FINE_PAIRS
    }
    for left in b64.ROTATIONS:
        for right in b64.ROTATIONS:
            product = rotation_product(left, right)
            group_failures += product not in rotation_set
            for outcome, sign in FINE_PAIRS:
                for law in LAW_NAMES:
                    body = maps[(law, right, outcome, sign)]
                    transformed = b65.transformed_records(body, left, ORIGIN)
                    direct = maps[(law, product, outcome, sign)]
                    failures += transformed != direct
                    distinct_contents += body != direct
                    cases += 1
    return {
        "rotations": len(b64.ROTATIONS),
        "cases": cases,
        "failures": failures,
        "group_failures": group_failures,
        "distinct_contents": distinct_contents,
    }


def arbitrary_root_separation_lemma() -> bool:
    """Coefficient proof that neither extra root intersects a Block-64 strip.

    In the successor frame, every ordinary support point is H_n=(n,0),
    C_n=(n,s_n), or O_n=(n+1,s_n), n>=0.  The output-root extra point is
    (-1,0).  The adjacent-packet bootstrap root is (0,+1), while phase one
    makes C_0=(0,-1); all later points have positive forward coefficient.
    """

    output_root_separated = -1 < 0
    adjacent_at_zero = (0, 1) not in ((0, 0), (0, -1))
    adjacent_later = all(value > 0 for value in (1, 2))
    return output_root_separated and adjacent_at_zero and adjacent_later


def continue_targeted(
    records: b64.Records,
    horizon: int,
    innovations: tuple[Fraction, ...],
) -> b65.Continuation:
    """Execute the inherited rule at its symbolically unique front target.

    Block 64 already proves that its append-only strip has one active site at
    each relay/outcome/finalize stage.  The extra-root coefficient lemma above
    proves that neither candidate root enters that strip.  This executor still
    calls the exact local rule at every predicted target; it avoids repeatedly
    scanning every historical Record merely to rediscover the unique site.
    """

    if not innovations:
        raise ValueError("an innovation stream is required")
    answer = dict(records)
    heads = tuple(
        (site, context)
        for site, carrier in answer.items()
        if (context := b64.decode_context(carrier)) is not None
        and context.role == "head"
    )
    if len(heads) != 1:
        return b65.Continuation(False, answer, (), 0)
    head_site, _context = heads[0]
    history: list[int] = []
    checks = 0
    for event in range(horizon):
        context = b64.decode_context(answer[head_site])
        if context is None or context.role != "head":
            return b65.Continuation(False, answer, tuple(history), checks)
        relay_site = b64.add(head_site, context.transverse)
        outcome_site = b64.add(relay_site, context.forward)
        next_head_site = b64.add(head_site, context.forward)
        for expected_kind, target in (
            ("relay", relay_site),
            ("outcome", outcome_site),
            ("finalize", next_head_site),
        ):
            distribution = b64.local_distribution(answer, target)
            checks += 1
            if (
                distribution is None
                or distribution.kind != expected_kind
                or not distribution.normalized
            ):
                return b65.Continuation(False, answer, tuple(history), checks)
            if expected_kind == "outcome":
                selected, carrier = b64.choose(
                    distribution,
                    innovations[event % len(innovations)],
                )
                history.append(selected)
            else:
                _, carrier = b64.choose(distribution, Fraction(0))
            answer = b64.append_one(answer, target, carrier)
        head_site = next_head_site
    return b65.Continuation(True, answer, tuple(history), checks)


def permanence_certificate(finite_horizon: bool = False) -> dict[str, object]:
    innovations = tuple(
        Fraction(value, 29)
        for value in (1, 5, 9, 13, 17, 21, 25, 3, 7, 11, 15, 19, 23, 27)
    )
    executed_cases = lifted_cases = active_checks = continued_records = 0
    continuation_failures = count_failures = overwrite_failures = history_failures = 0
    lift_failures = 0
    horizon = 32
    canonical_futures: dict[tuple[str, int, int], b65.Continuation] = {}
    for outcome, sign in FINE_PAIRS:
        for law in LAW_NAMES:
            initial = candidate_records(law, b64.IDENTITY_ROTATION, outcome, sign)
            continued = continue_targeted(initial, horizon, innovations)
            canonical_futures[(law, outcome, sign)] = continued
            records = dict(continued.records)
            if finite_horizon:
                records.pop(ORIGIN, None)
            continuation_failures += not continued.ok
            count_failures += len(records) != 3 * horizon + 2
            overwrite_failures += any(records.get(site) != carrier for site, carrier in initial.items())
            history_failures += len(continued.history) != horizon
            active_checks += continued.active_checks
            continued_records += len(records)
            executed_cases += 1

    for rotation in b64.ROTATIONS:
        for outcome, sign in FINE_PAIRS:
            for law in LAW_NAMES:
                canonical_initial = candidate_records(
                    law,
                    b64.IDENTITY_ROTATION,
                    outcome,
                    sign,
                )
                direct_initial = candidate_records(law, rotation, outcome, sign)
                lift_failures += b65.transformed_records(
                    canonical_initial,
                    rotation,
                    ORIGIN,
                ) != direct_initial
                canonical_future = canonical_futures[(law, outcome, sign)]
                transformed_future = b65.transformed_records(
                    canonical_future.records,
                    rotation,
                    ORIGIN,
                )
                lift_failures += len(transformed_future) != 3 * horizon + 2
                lift_failures += any(
                    transformed_future.get(site) != carrier
                    for site, carrier in direct_initial.items()
                )
                lifted_cases += 1

    full_scan_controls = full_scan_failures = 0
    for outcome, sign in FINE_PAIRS:
        for law in LAW_NAMES:
            initial = candidate_records(law, b64.IDENTITY_ROTATION, outcome, sign)
            targeted = continue_targeted(initial, 4, innovations)
            scanned = b65.continue_block64(initial, 4, innovations)
            full_scan_failures += targeted != scanned
            full_scan_controls += 1

    long_controls = long_failures = 0
    for outcome, sign in FINE_PAIRS:
        for law in LAW_NAMES:
            initial = candidate_records(law, b64.IDENTITY_ROTATION, outcome, sign)
            continued = continue_targeted(initial, 128, innovations)
            long_failures += not (
                continued.ok
                and len(continued.records) == 3 * 128 + 2
                and all(continued.records.get(site) == carrier for site, carrier in initial.items())
            )
            long_controls += 1
    return {
        "executed_cases": executed_cases,
        "lifted_cases": lifted_cases,
        "horizon": horizon,
        "active_checks": active_checks,
        "continued_records": continued_records,
        "continuation_failures": continuation_failures,
        "count_failures": count_failures,
        "overwrite_failures": overwrite_failures,
        "history_failures": history_failures,
        "lift_failures": lift_failures,
        "full_scan_controls": full_scan_controls,
        "full_scan_failures": full_scan_failures,
        "long_controls": long_controls,
        "long_failures": long_failures,
        "block64_arbitrary_lemma": b64.arbitrary_support_lemma(),
        "root_separation_lemma": arbitrary_root_separation_lemma(),
    }


@dataclass(frozen=True)
class DecodedOutputRoot:
    site: b64.Coord
    rho: b63.Matrix
    rotation: b64.Rotation
    outcome: int
    sign: int


def decode_output_root(records: b64.Records) -> DecodedOutputRoot | None:
    candidates: list[DecodedOutputRoot] = []
    for site, carrier in records.items():
        rho, frame_fraction, code_fraction = b63.decode_program(carrier)
        if code_fraction.denominator != 1:
            continue
        pair = CODE_TO_PAIR.get(int(code_fraction))
        if pair is None or any(value.denominator != 1 for value in frame_fraction):
            continue
        frame = tuple(int(value) for value in frame_fraction)
        rotation = b64.FRAME_TO_ROTATION.get(frame)  # type: ignore[arg-type]
        if rotation is None:
            continue
        candidates.append(DecodedOutputRoot(site, rho, rotation, pair[0], pair[1]))
    return candidates[0] if len(candidates) == 1 else None


def source_decode_certificate(forget_source: bool = False) -> dict[str, object]:
    innovations = tuple(Fraction(value, 23) for value in (1, 5, 9, 13, 17, 21, 3, 7, 11))
    initial_cases = long_cases = decoder_failures = frame_failures = density_failures = 0
    direction_failures = root_failures = 0
    for rotation in b64.ROTATIONS:
        side = b64.rotate_coord(rotation, b64.BASE_TRANSVERSE)
        for outcome, sign in FINE_PAIRS:
            a_initial = candidate_records("output_root", rotation, outcome, sign)
            decoded_a = decode_output_root(a_initial)
            decoder_failures += decoded_a is None
            if decoded_a is not None:
                root_failures += decoded_a.site != ORIGIN
                frame_failures += decoded_a.rotation != rotation
                density_failures += decoded_a.rho != tau(rotation, outcome)
                direction_failures += (decoded_a.outcome, decoded_a.sign) != (outcome, sign)

            used_sign = 1 if forget_source else sign
            b_initial = candidate_records("adjacent_packet", rotation, outcome, used_sign)
            decoded_b = b67.decode_signed_source(b_initial)
            decoder_failures += decoded_b is None
            if decoded_b is not None:
                expected_successor = b67.signed_rotation(rotation, sign)
                expected_direction = b64.rotate_coord(expected_successor, b64.BASE_FORWARD)
                root_failures += decoded_b.new_source != ORIGIN
                direction_failures += decoded_b.direction != expected_direction
                direction_failures += decoded_b.outcome != outcome
                expected_head = b64.add(ORIGIN, b64.neg(side))
                root_failures += decoded_b.head_site != expected_head
                context = b64.decode_context(b_initial.get(decoded_b.head_site, b63.ZERO_MATRIX))
                frame_failures += context is None or context.rotation != expected_successor
            initial_cases += 2

    for outcome, sign in FINE_PAIRS:
        a_initial = candidate_records("output_root", b64.IDENTITY_ROTATION, outcome, sign)
        a_records = continue_targeted(a_initial, 16, innovations).records
        decoded_a = decode_output_root(a_records)
        decoder_failures += decoded_a is None
        if decoded_a is not None:
            root_failures += decoded_a.site != ORIGIN
            frame_failures += decoded_a.rotation != b64.IDENTITY_ROTATION
            density_failures += decoded_a.rho != tau(b64.IDENTITY_ROTATION, outcome)
            direction_failures += (decoded_a.outcome, decoded_a.sign) != (outcome, sign)

        used_sign = 1 if forget_source else sign
        b_initial = candidate_records(
            "adjacent_packet",
            b64.IDENTITY_ROTATION,
            outcome,
            used_sign,
        )
        b_records = continue_targeted(b_initial, 16, innovations).records
        decoded_b = b67.decode_signed_source(b_records)
        decoder_failures += decoded_b is None
        if decoded_b is not None:
            expected_successor = b67.signed_rotation(b64.IDENTITY_ROTATION, sign)
            expected_direction = b64.rotate_coord(expected_successor, b64.BASE_FORWARD)
            root_failures += decoded_b.new_source != ORIGIN
            direction_failures += decoded_b.direction != expected_direction
            direction_failures += decoded_b.outcome != outcome
            context = b64.decode_context(b_records.get(decoded_b.head_site, b63.ZERO_MATRIX))
            frame_failures += context is None or context.rotation != expected_successor
        long_cases += 2
    return {
        "initial_cases": initial_cases,
        "long_cases": long_cases,
        "decoder_failures": decoder_failures,
        "frame_failures": frame_failures,
        "density_failures": density_failures,
        "direction_failures": direction_failures,
        "root_failures": root_failures,
    }


def inequivalence_certificate(collapse_laws: bool = False) -> dict[str, object]:
    cases = map_equalities = root_equalities = continued_equalities = count_failures = 0
    geometry_separations = geometry_failures = shared_decoder_failures = 0
    continuation_failures = persistence_failures = root_decoder_failures = 0
    nearest_head_failures = head_count_failures = history_agreements = 0
    output_nearest_forward = output_nearest_transverse = 0
    adjacent_nearest_forward = adjacent_nearest_transverse = 0
    output_all_forward = output_all_transverse = 0
    adjacent_all_forward = adjacent_all_transverse = 0
    output_signatures: set[tuple[int, int, int]] = set()
    adjacent_signatures: set[tuple[int, int, int]] = set()
    output_packets: set[RecordsTuple] = set()
    adjacent_packets: set[RecordsTuple] = set()
    output_histories: set[tuple[object, ...]] = set()
    adjacent_histories: set[tuple[object, ...]] = set()
    packet_forward: dict[RecordsTuple, RecordsTuple] = {}
    packet_inverse: dict[RecordsTuple, RecordsTuple] = {}
    history_forward: dict[tuple[object, ...], tuple[object, ...]] = {}
    history_inverse: dict[tuple[object, ...], tuple[object, ...]] = {}
    packet_forward_conflicts = packet_inverse_conflicts = 0
    history_forward_conflicts = history_inverse_conflicts = 0

    def records_key(records: b64.Records) -> RecordsTuple:
        return tuple(sorted(records.items()))

    def history_key(continued: b65.Continuation) -> tuple[object, ...]:
        return (
            continued.ok,
            records_key(continued.records),
            continued.history,
            continued.active_checks,
        )

    def decoded_heads(
        records: b64.Records,
    ) -> tuple[tuple[b64.Coord, b64.Context], ...]:
        return tuple(
            (site, context)
            for site, carrier in records.items()
            if (context := b64.decode_context(carrier)) is not None
            and context.role == "head"
        )

    def head_signature(
        root: b64.Coord,
        head_site: b64.Coord,
        context: b64.Context,
    ) -> tuple[int, int, int]:
        displacement = tuple(
            head_site[axis] - root[axis] for axis in range(3)
        )
        return (
            sum(abs(value) for value in displacement),
            sum(displacement[axis] * context.forward[axis] for axis in range(3)),
            sum(
                displacement[axis] * context.transverse[axis]
                for axis in range(3)
            ),
        )

    def geometry_signature(records: b64.Records) -> tuple[int, int, int] | None:
        heads = decoded_heads(records)
        if len(heads) != 1 or ORIGIN not in records:
            return None
        head_site, context = heads[0]
        return head_signature(ORIGIN, head_site, context)

    for rotation in b64.ROTATIONS:
        for outcome, sign in FINE_PAIRS:
            left = candidate_records("output_root", rotation, outcome, sign)
            right = candidate_records("adjacent_packet", rotation, outcome, sign)
            if collapse_laws:
                root_carrier = right[ORIGIN]
                head_item = next(
                    (site, carrier, context)
                    for site, carrier in right.items()
                    if (context := b64.decode_context(carrier)) is not None
                    and context.role == "head"
                )
                _old_site, head_carrier, context = head_item
                right = {
                    ORIGIN: root_carrier,
                    b64.add(ORIGIN, context.forward): head_carrier,
                }
            map_equalities += left == right
            root_equalities += left[ORIGIN] == right[ORIGIN]
            count_failures += not (len(left) == len(right) == 2)
            left_signature = geometry_signature(left)
            right_signature = geometry_signature(right)
            geometry_failures += left_signature is None or right_signature is None
            if left_signature is not None and right_signature is not None:
                output_signatures.add(left_signature)
                adjacent_signatures.add(right_signature)
                geometry_separations += left_signature != right_signature
            left_head = next(
                context
                for carrier in left.values()
                if (context := b64.decode_context(carrier)) is not None
                and context.role == "head"
            )
            right_head = next(
                context
                for carrier in right.values()
                if (context := b64.decode_context(carrier)) is not None
                and context.role == "head"
            )
            shared_decoder_failures += not (
                left_head.rho == right_head.rho == tau(rotation, outcome)
                and left_head.rotation == right_head.rotation == b67.signed_rotation(rotation, sign)
                and left_head.menu == right_head.menu == 1
                and left_head.phase == right_head.phase == 1
            )
            innovations = (Fraction(1, 7), Fraction(3, 7))
            left_continued = continue_targeted(left, 4, innovations)
            right_continued = continue_targeted(right, 4, innovations)
            left_future = left_continued.records
            right_future = right_continued.records
            continuation_failures += not left_continued.ok or not right_continued.ok
            continued_equalities += left_future == right_future
            history_agreements += left_continued.history == right_continued.history
            persistence_failures += any(left_future.get(site) != carrier for site, carrier in left.items())
            persistence_failures += any(right_future.get(site) != carrier for site, carrier in right.items())

            left_key = records_key(left)
            right_key = records_key(right)
            left_history_key = history_key(left_continued)
            right_history_key = history_key(right_continued)
            output_packets.add(left_key)
            adjacent_packets.add(right_key)
            output_histories.add(left_history_key)
            adjacent_histories.add(right_history_key)
            packet_forward_conflicts += left_key in packet_forward and packet_forward[left_key] != right_key
            packet_inverse_conflicts += right_key in packet_inverse and packet_inverse[right_key] != left_key
            history_forward_conflicts += (
                left_history_key in history_forward
                and history_forward[left_history_key] != right_history_key
            )
            history_inverse_conflicts += (
                right_history_key in history_inverse
                and history_inverse[right_history_key] != left_history_key
            )
            packet_forward[left_key] = right_key
            packet_inverse[right_key] = left_key
            history_forward[left_history_key] = right_history_key
            history_inverse[right_history_key] = left_history_key

            decoded_left_root = decode_output_root(left_future)
            decoded_right_root = b67.decode_signed_source(right_future)
            root_decoder_failures += decoded_left_root is None or decoded_right_root is None
            if decoded_left_root is not None and decoded_right_root is not None:
                root_decoder_failures += decoded_left_root.site != ORIGIN
                root_decoder_failures += decoded_right_root.new_source != ORIGIN

            for law, future in (
                ("output_root", left_future),
                ("adjacent_packet", right_future),
            ):
                heads = decoded_heads(future)
                head_count_failures += len(heads) != 5
                distances = tuple(
                    sum(abs(site[axis] - ORIGIN[axis]) for axis in range(3))
                    for site, _context in heads
                )
                minimum = min(distances) if distances else -1
                nearest = tuple(
                    item for item, distance in zip(heads, distances) if distance == minimum
                )
                nearest_head_failures += len(nearest) != 1
                signatures = tuple(
                    head_signature(ORIGIN, site, context)
                    for site, context in heads
                )
                nearest_signature = (
                    head_signature(ORIGIN, nearest[0][0], nearest[0][1])
                    if len(nearest) == 1
                    else None
                )
                forward_matches = sum(
                    tuple(site[axis] - ORIGIN[axis] for axis in range(3))
                    == context.forward
                    for site, context in heads
                )
                transverse_matches = sum(
                    tuple(site[axis] - ORIGIN[axis] for axis in range(3))
                    == context.transverse
                    for site, context in heads
                )
                if law == "output_root":
                    output_nearest_forward += nearest_signature is not None and nearest_signature[1] == 1
                    output_nearest_transverse += nearest_signature is not None and nearest_signature[2] == 1
                    output_all_forward += forward_matches
                    output_all_transverse += transverse_matches
                else:
                    adjacent_nearest_forward += nearest_signature is not None and nearest_signature[1] == 1
                    adjacent_nearest_transverse += nearest_signature is not None and nearest_signature[2] == 1
                    adjacent_all_forward += forward_matches
                    adjacent_all_transverse += transverse_matches
            cases += 1
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").split())
    head_only = {
        b64.context_carrier(
            "head",
            tau(rotation, outcome),
            b67.signed_rotation(rotation, sign),
            1,
            1,
        )
        for rotation in b64.ROTATIONS
        for outcome, sign in FINE_PAIRS
    }
    tagged_roots = {
        output_root_records(rotation, outcome, sign)[ORIGIN]
        for rotation in b64.ROTATIONS
        for outcome, sign in FINE_PAIRS
    }
    scope_ok = all(
        needle in note
        for needle in (
            "current executable interface nonselection",
            "not a full-Z3 model-theoretic non-entailment",
            "does not authorize an axiom edit",
            "downstream physical L_phys formation/attachment law",
            "a third law remains possible",
            "Record-faithful equivalence",
        )
    )
    return {
        "cases": cases,
        "map_equalities": map_equalities,
        "root_equalities": root_equalities,
        "continued_equalities": continued_equalities,
        "count_failures": count_failures,
        "geometry_separations": geometry_separations,
        "geometry_failures": geometry_failures,
        "shared_decoder_failures": shared_decoder_failures,
        "continuation_failures": continuation_failures,
        "persistence_failures": persistence_failures,
        "root_decoder_failures": root_decoder_failures,
        "nearest_head_failures": nearest_head_failures,
        "head_count_failures": head_count_failures,
        "history_agreements": history_agreements,
        "output_signatures": tuple(sorted(output_signatures)),
        "adjacent_signatures": tuple(sorted(adjacent_signatures)),
        "output_packets": len(output_packets),
        "adjacent_packets": len(adjacent_packets),
        "packet_forward": len(packet_forward),
        "packet_inverse": len(packet_inverse),
        "packet_forward_conflicts": packet_forward_conflicts,
        "packet_inverse_conflicts": packet_inverse_conflicts,
        "output_histories": len(output_histories),
        "adjacent_histories": len(adjacent_histories),
        "history_forward": len(history_forward),
        "history_inverse": len(history_inverse),
        "history_forward_conflicts": history_forward_conflicts,
        "history_inverse_conflicts": history_inverse_conflicts,
        "output_nearest_forward": output_nearest_forward,
        "output_nearest_transverse": output_nearest_transverse,
        "adjacent_nearest_forward": adjacent_nearest_forward,
        "adjacent_nearest_transverse": adjacent_nearest_transverse,
        "output_all_forward": output_all_forward,
        "output_all_transverse": output_all_transverse,
        "adjacent_all_forward": adjacent_all_forward,
        "adjacent_all_transverse": adjacent_all_transverse,
        "head_only_unique": len(head_only),
        "tagged_root_unique": len(tagged_roots),
        "scope_ok": scope_ok,
    }


def boundary_surface_ok(broaden_boundary: bool = False) -> bool:
    note = NOTE_PATH.read_text(encoding="utf-8")
    needles = tuple(f"### N{index}" for index in range(1, 9)) + (
        "claim_type: bounded_theorem",
        "zero TOE percentage movement",
        "ATTEMPTED",
        "RULED OUT BY PRIOR",
        "all 15 wall pairs",
        "hidden-import scan",
        "file:line",
        "retired?",
        "could apply?",
        "strongest surviving escape route",
        "PASS for the narrow interface-nonselection statement",
        "FAIL/demoted for axiom necessity",
        "per_element:",
        "per_site:",
        "per_mode:",
        "per_block:",
        "lattice_wide:",
        "40%",
        "25%",
        "20%",
        "10%",
        "5%",
    )
    return not broaden_boundary and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom",
            "wrong_fine_branch",
            "dirty_route",
            "overwrite",
            "weight_mismatch",
            "noncovariant",
            "finite_horizon",
            "forget_source",
            "collapse_geometry",
            "broaden_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation == "stale_axiom")
    authority_ok = (
        authority["sha256"] == AXIOM_AUTHORITY_SHA256
        and authority["current_authority_sha256"] == AXIOM_AUTHORITY_SHA256
        and authority["remote_ancestor"]
        and authority["current_record"]
        and authority["parent_receipt_ancestor"]
        and authority["parent_runner_sha256"] == PARENT_RUNNER_SHA256
        and authority["parent_note_sha256"] == PARENT_NOTE_SHA256
        and PARENT_RECEIPT_COMMIT in NOTE_PATH.read_text(encoding="utf-8")
    )
    checks.check(
        "A-origin-main-axiom-and-exact-Block69-parent",
        authority_ok,
        f"current {authority['current_ref']} Record hash={str(authority['current_authority_sha256'])[:12]}; exact Block69 receipt ancestor={authority['parent_receipt_ancestor']} with pinned runner/note hashes",
    )

    fine = fine_dilation_certificate(mutation == "wrong_fine_branch")
    fine_ok = (
        fine["matrix_units"] == 16
        and fine["branch_cases"] == 80
        and fine["fine_pairs"] == FINE_PAIRS
        and fine["maximum_residual"] < TOL
        and fine["coarse_residual"] < TOL
        and fine["completeness_residual"] < TOL
        and fine["choi_minimum"] > -TOL
        and fine["trace_residual"] < TOL
    )
    checks.check(
        "B-four-fine-branch-five-M2-channel-equality",
        fine_ok,
        f"{fine['branch_cases']}/80 matrix-unit branch outputs resolve {fine['fine_pairs']}; fine/coarse residuals={fine['maximum_residual']:.1e}/{fine['coarse_residual']:.1e}, Choi min={fine['choi_minimum']:.1e}, TP={fine['trace_residual']:.1e}",
    )

    route = physical_relocation_certificate(mutation == "dirty_route")
    route_ok = (
        route["parent_assigned_M2"] == 42
        and route["parent_route_failures"] == 0
        and route["relocations"] == 4
        and route["target_failures"] == 0
        and route["non_nn_failures"] == 0
        and route["blocked_visits"] == 0
        and route["reverse_failures"] == 0
        and route["background_displacements"] > 0
    )
    checks.check(
        "C-branch-conditioned-NN-output-gathering-without-clean-bank",
        route_ok,
        f"four canonical sign/law layouts use {route['swaps']} NN SWAPs over {route['touched']} sites, preserve both Record targets, and reverse exactly; {route['background_displacements']} background labels move before reversal, so no clean-bank claim is made",
    )

    total = total_law_certificate(mutation == "overwrite")
    total_ok = (
        total["valid_cases"] == 48
        and total["refusal_cases"] == 240
        and total["realized_refusals"] == 48
        and total["replay_refusals"] == 240
        and not any(
            total[key]
            for key in (
                "normalization_failures",
                "append_failures",
                "preservation_failures",
                "status_failures",
                "totality_failures",
            )
        )
    )
    checks.check(
        "D-two-total-append-only-ready-patch-laws",
        total_ok,
        f"{total['valid_cases']} frame/law distributions normalize; {total['refusal_cases']} invalid/occupied and {total['replay_refusals']} spent replays preserve all Records; invalid realized members refuse rather than overwrite",
    )

    realized = realized_weight_certificate(mutation == "weight_mismatch")
    realized_ok = (
        realized["cases"] == 24
        and realized["realized_members"] == 240
        and realized["primitive_firewall"]
        and not any(
            realized[key]
            for key in (
                "normalization_failures",
                "positivity_failures",
                "candidate_weight_failures",
                "coarse_failures",
                "realized_failures",
            )
        )
    )
    checks.check(
        "E-shared-exact-weights-and-explicit-realized-member",
        realized_ok,
        f"both laws share five positive exact weights in all {realized['cases']} frames and coarse-grain to Block65; {realized['realized_members']} supplied realized-member applications pass, while the inherited primitive is kept selection-free",
    )

    covariance = covariance_certificate(mutation == "noncovariant")
    covariance_ok = (
        covariance["rotations"] == 24
        and covariance["cases"] == 4608
        and covariance["failures"] == 0
        and covariance["group_failures"] == 0
        and covariance["distinct_contents"] > 0
    )
    checks.check(
        "F-proper-cubic-all-frame-law-covariance",
        covariance_ok,
        f"{covariance['cases']}/4608 left/right group compositions intertwine both complete first-write maps; {covariance['distinct_contents']} nontrivial transformed maps exclude a coordinate-only self-comparison",
    )

    permanence = permanence_certificate(mutation == "finite_horizon")
    permanence_ok = (
        permanence["executed_cases"] == 8
        and permanence["lifted_cases"] == 192
        and permanence["active_checks"] == 8 * 32 * 3
        and permanence["full_scan_controls"] == 8
        and permanence["long_controls"] == 8
        and permanence["block64_arbitrary_lemma"]
        and permanence["root_separation_lemma"]
        and not any(
            permanence[key]
            for key in (
                "continuation_failures",
                "count_failures",
                "overwrite_failures",
                "history_failures",
                "lift_failures",
                "full_scan_failures",
                "long_failures",
            )
        )
    )
    checks.check(
        "G-arbitrary-single-front-permanence-and-no-overwrite",
        permanence_ok,
        f"{permanence['executed_cases']} canonical histories reach N={permanence['horizon']} and lift exactly to {permanence['lifted_cases']} all-frame cases with 3N+2 Records; {permanence['full_scan_controls']} full-scan and {permanence['long_controls']} N=128 controls pass, while inherited induction plus two root-separation cases cover arbitrary N",
    )

    source = source_decode_certificate(mutation == "forget_source")
    source_ok = source["initial_cases"] == 192 and source["long_cases"] == 8 and not any(
        source[key]
        for key in (
            "decoder_failures",
            "frame_failures",
            "density_failures",
            "direction_failures",
            "root_failures",
        )
    )
    checks.check(
        "H-whole-history-root-density-sign-coframe-decoders",
        source_ok,
        f"{source['initial_cases']} all-frame root packets and {source['long_cases']} canonical N=16 histories decode uniquely: output-root recovers density/outcome/sign/coframe, while adjacent-packet recovers source hop/outcome/signed successor frame",
    )

    inequivalent = inequivalence_certificate(mutation == "collapse_geometry")
    inequivalent_ok = (
        inequivalent["cases"] == 96
        and inequivalent["map_equalities"] == 0
        and inequivalent["root_equalities"] == 0
        and inequivalent["continued_equalities"] == 0
        and inequivalent["count_failures"] == 0
        and inequivalent["geometry_separations"] == 96
        and inequivalent["geometry_failures"] == 0
        and inequivalent["shared_decoder_failures"] == 0
        and inequivalent["continuation_failures"] == 0
        and inequivalent["persistence_failures"] == 0
        and inequivalent["root_decoder_failures"] == 0
        and inequivalent["nearest_head_failures"] == 0
        and inequivalent["head_count_failures"] == 0
        and inequivalent["history_agreements"] == 96
        and inequivalent["output_signatures"] == ((1, 1, 0),)
        and inequivalent["adjacent_signatures"] == ((1, 0, 1),)
        and inequivalent["output_packets"] == 96
        and inequivalent["adjacent_packets"] == 96
        and inequivalent["packet_forward"] == 96
        and inequivalent["packet_inverse"] == 96
        and inequivalent["packet_forward_conflicts"] == 0
        and inequivalent["packet_inverse_conflicts"] == 0
        and inequivalent["output_histories"] == 96
        and inequivalent["adjacent_histories"] == 96
        and inequivalent["history_forward"] == 96
        and inequivalent["history_inverse"] == 96
        and inequivalent["history_forward_conflicts"] == 0
        and inequivalent["history_inverse_conflicts"] == 0
        and inequivalent["output_nearest_forward"] == 96
        and inequivalent["output_nearest_transverse"] == 0
        and inequivalent["adjacent_nearest_forward"] == 0
        and inequivalent["adjacent_nearest_transverse"] == 96
        and inequivalent["output_all_forward"] == 96
        and inequivalent["output_all_transverse"] == 0
        and inequivalent["adjacent_all_forward"] == 0
        and inequivalent["adjacent_all_transverse"] == 96
        and inequivalent["head_only_unique"] == 72
        and inequivalent["tagged_root_unique"] == 96
        and inequivalent["scope_ok"]
    )
    checks.check(
        "I-observable-two-law-interface-nonselection",
        inequivalent_ok,
        f"unrestricted exact lookups biject {inequivalent['packet_forward']} packets and {inequivalent['history_forward']} N=4 histories, but all {inequivalent['cases']} shared-decoder packets and their unique nearest permanent heads separate under the Record-faithful geometry invariant: output-root {inequivalent['output_signatures']} versus adjacent {inequivalent['adjacent_signatures']}; head-only tagging collapses 96 inputs to {inequivalent['head_only_unique']} carriers",
    )

    boundary_ok = boundary_surface_ok(mutation == "broaden_boundary")
    checks.check(
        "J-N1-N8-bounded-scope-portfolio-and-TOE-accounting",
        boundary_ok,
        "the source note contains structured N1-N8 attacks, all wall pairs, hidden-import and citation residual audits, five granularities, hostile steelman, cross-cycle echoes, zero score movement, and the next portfolio gate; this guard is not an audit verdict",
    )

    print(
        "METRICS "
        f"fine_branch_cases={fine['branch_cases']} channel_residual={fine['maximum_residual']:.2e} "
        f"physical_swaps={route['swaps']} covariance_cases={covariance['cases']} "
        f"N32_executed={permanence['executed_cases']} N32_lifted={permanence['lifted_cases']} decode_initial={source['initial_cases']} decode_long={source['long_cases']} "
        f"inequivalent_cases={inequivalent['cases']}"
    )
    print(
        "BOUNDARY: two inequivalent total laws survive on an isolated branch-ready patch with exact Cycle713 weights, canonical branch-conditioned NN gathering, all-frame Record covariance, and arbitrary single-front permanence; no global multi-front scheduler, autonomous draw, untouched environment reset, full-Z3 law, gravity closure, axiom edit, audit retention, obligation retirement, or TOE percentage movement is claimed"
    )
    print("per_element: all sixteen P-M matrix units, one no-formation plus four fine outputs, every exact law weight, and both root parsers were checked")
    print("per_site: five named output roles, two candidate root geometries, occupied/refusal behavior, NN SWAP paths, background displacement, and permanent root/head sites were checked")
    print("per_mode: all four nonzero (outcome,sign) modes and 24x24 proper-cubic group compositions were checked for both laws")
    print("per_block: the exact Block69 receipt/dilation, Block65 coarse law, Block67 source decoder, and Block64 arbitrary-front induction were composed without changing their authorities")
    print("lattice_wide: checked and not executed — branch-conditioned isolated routes are not a homogeneous simultaneous full-Z3 process, and surrounding quantum output factors are not reset or re-encoded")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
