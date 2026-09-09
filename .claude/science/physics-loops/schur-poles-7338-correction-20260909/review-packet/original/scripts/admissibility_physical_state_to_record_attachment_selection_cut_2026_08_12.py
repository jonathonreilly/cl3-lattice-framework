#!/usr/bin/env python3
"""Block 65: physical-state to Record attachment selection cut.

Construct a branch-first completely-positive pointer/matter instrument whose
classical formation branches write the first pure outcome Record and the
known post-outcome Block-64 head.  Compare exact menu and formation-hazard
forks, and isolate the owner datum not selected by the current axioms.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np

import admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12 as b64


b63 = b64.b63
AUDIT_TIMEOUT_SEC = 180
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK64_NOTE = ROOT / "docs" / "ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md"
CYCLE713_NOTE = ROOT / "docs" / "PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md"
CYCLE883_NOTE = ROOT / "docs" / "RECURRENT_ENCODE_UPDATE_DECODE_SANDWICH_CYCLE883_BOUNDED_THEOREM_NOTE_2026-08-03.md"
SELECTION_NOTE = ROOT / "docs" / "ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_ENCODE_UPDATE_DECODE_SANDWICH_CYCLE883_BOUNDED_THEOREM_NOTE_2026-08-03.md",
    "docs/ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
)

Exact = b63.ExactComplex
Matrix = b63.Matrix
QMatrix = tuple[tuple[Exact, ...], ...]
Coord = b64.Coord
Rotation = b64.Rotation
Records = b64.Records

P0: Matrix = b63.matrix(1, 0, 0, 0)
P1: Matrix = b63.matrix(0, 0, 0, 1)
PPLUS: Matrix = b63.matrix(Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))


def qzero(size: int) -> QMatrix:
    return tuple(tuple(b63.ZERO for _ in range(size)) for _ in range(size))


def qidentity(size: int) -> QMatrix:
    return tuple(
        tuple(b63.ONE if row == column else b63.ZERO for column in range(size))
        for row in range(size)
    )


def qadd(left: QMatrix, right: QMatrix) -> QMatrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(len(left)))
        for row in range(len(left))
    )


def qscale(value: Fraction, operand: QMatrix) -> QMatrix:
    scalar = Exact(value)
    return tuple(
        tuple(scalar * entry for entry in row)
        for row in operand
    )


def qkron(left: QMatrix, right: QMatrix) -> QMatrix:
    left_rows, right_rows = len(left), len(right)
    return tuple(
        tuple(
            left[row // right_rows][column // right_rows]
            * right[row % right_rows][column % right_rows]
            for column in range(left_rows * right_rows)
        )
        for row in range(left_rows * right_rows)
    )


def qtrace_product(left: QMatrix, right: QMatrix) -> Fraction:
    value = b63.ZERO
    for row in range(len(left)):
        for column in range(len(left)):
            value += left[row][column] * right[column][row]
    if value.imag != 0:
        raise ValueError("trace product is not real")
    return value.real


def qnumpy(operand: QMatrix) -> np.ndarray:
    return np.asarray(
        [[complex(float(entry.real), float(entry.imag)) for entry in row] for row in operand],
        dtype=complex,
    )


def qdensity(operand: QMatrix) -> bool:
    numeric = qnumpy(operand)
    return (
        np.allclose(numeric, numeric.conj().T, atol=2e-12)
        and abs(np.trace(numeric) - 1) < 2e-12
        and float(np.linalg.eigvalsh(numeric).min()) > -2e-12
    )


def product_state(pointer: Matrix, matter: Matrix) -> QMatrix:
    return qkron(pointer, matter)


def bell_state() -> QMatrix:
    answer = [list(row) for row in qzero(4)]
    for row, column in ((0, 0), (0, 3), (3, 0), (3, 3)):
        answer[row][column] = Exact(Fraction(1, 2))
    return tuple(tuple(row) for row in answer)


def rotated_effects(rotation: Rotation, menu: int) -> tuple[Matrix, ...]:
    return b64.rotated_menus(rotation)[menu]


def instrument_effects(
    rotation: Rotation,
    menu: int,
    formation_hazard: Fraction,
) -> tuple[QMatrix, tuple[QMatrix, ...]]:
    if not 0 <= formation_hazard <= 1:
        raise ValueError("formation hazard must lie in [0,1]")
    pointer_zero = qkron(P0, b63.IDENTITY)
    pointer_one = qkron(P1, b63.IDENTITY)
    no_record = qadd(pointer_zero, qscale(1 - formation_hazard, pointer_one))
    formation = tuple(
        qscale(formation_hazard, qkron(P1, effect))
        for effect in rotated_effects(rotation, menu)
    )
    return no_record, formation


def branch_choi_minimum(
    rotation: Rotation,
    menu: int,
    formation_hazard: Fraction,
) -> float:
    no_record, formation = instrument_effects(rotation, menu, formation_hazard)
    minima: list[float] = []
    for effect4, effect2 in zip(formation, rotated_effects(rotation, menu)):
        tau = b63.normalized_effect_state(effect2)
        choi = np.kron(qnumpy(effect4).T, b63.to_numpy(tau))
        minima.append(float(np.linalg.eigvalsh(choi).min()))

    # A one-Kraus no-formation branch has K=P0 x I + sqrt(1-f) P1 x I.
    # The two hazards used by this packet have exact rational square roots.
    roots = {Fraction(1): Fraction(0), Fraction(3, 4): Fraction(1, 2)}
    root = roots[formation_hazard]
    kraus = qadd(qkron(P0, b63.IDENTITY), qscale(root, qkron(P1, b63.IDENTITY)))
    vector = qnumpy(kraus).reshape(-1, order="F")
    no_record_choi = np.outer(vector, vector.conj())
    minima.append(float(np.linalg.eigvalsh(no_record_choi).min()))
    expected_effect = qnumpy(no_record)
    actual_effect = qnumpy(kraus).conj().T @ qnumpy(kraus)
    if not np.allclose(expected_effect, actual_effect, atol=2e-12):
        raise AssertionError("no-formation Kraus effect mismatch")
    return min(minima)


@dataclass(frozen=True)
class Branch:
    kind: str
    weight: Fraction
    records: tuple[tuple[Coord, Matrix], ...]

    def record_map(self) -> Records:
        return dict(self.records)


@dataclass
class Patch:
    omega: QMatrix
    rotation: Rotation
    menu: int
    phase: int
    formation_hazard: Fraction
    origin: Coord = b64.ORIGIN
    context_valid: bool = True
    quantum_valid: bool = True
    spent: bool = False
    records: Records | None = None

    def __post_init__(self) -> None:
        if self.records is None:
            self.records = {}


@dataclass(frozen=True)
class BootstrapDistribution:
    kind: str
    outcomes: tuple[tuple[Fraction, Matrix | None], ...]

    @property
    def normalized(self) -> bool:
        return (
            sum((weight for weight, _ in self.outcomes), Fraction(0)) == 1
            and all(weight >= 0 for weight, _ in self.outcomes)
        )


def signed_side(rotation: Rotation, phase: int) -> Coord:
    side = b64.rotate_coord(rotation, b64.BASE_TRANSVERSE)
    return b64.scale(1 if phase == 0 else -1, side)


def branch_sites(
    rotation: Rotation,
    phase: int,
    origin: Coord = b64.ORIGIN,
) -> tuple[Coord, Coord, Coord, Coord]:
    forward = b64.rotate_coord(rotation, b64.BASE_FORWARD)
    side = signed_side(rotation, phase)
    live_context = origin
    live_quantum = b64.add(origin, side)
    outcome = b64.add(live_quantum, forward)
    next_head = b64.add(origin, forward)
    return live_context, live_quantum, outcome, next_head


def bootstrap_distribution(
    omega: QMatrix,
    rotation: Rotation,
    menu: int,
    phase: int,
    formation_hazard: Fraction,
    origin: Coord = b64.ORIGIN,
) -> tuple[Branch, ...]:
    if not qdensity(omega):
        raise ValueError("joint pointer/matter input must be a density operator")
    no_record, formation = instrument_effects(rotation, menu, formation_hazard)
    _, _, outcome_site, head_site = branch_sites(rotation, phase, origin)
    effects = rotated_effects(rotation, menu)
    branches = [Branch("no_record", qtrace_product(omega, no_record), ())]
    for outcome, (effect4, effect2) in enumerate(zip(formation, effects)):
        outcome_record = b63.outcome_carrier(effect2, outcome + 1)
        next_head = b64.context_carrier(
            "head",
            b63.normalized_effect_state(effect2),
            rotation,
            1 - menu,
            1 - phase,
        )
        records = tuple(sorted(((outcome_site, outcome_record), (head_site, next_head))))
        branches.append(
            Branch("formation", qtrace_product(omega, effect4), records)
        )
    return tuple(branches)


def bootstrap_local_distribution(
    patch: Patch,
    target: Coord,
) -> BootstrapDistribution | None:
    """Fixed radius-one rule on the two bootstrap targets.

    The stochastic target sees the live quantum site.  The successor-head
    target sees the live context and realized outcome.  Their common edge
    makes the branch order locally forced rather than host scheduled.
    """

    records = patch.records if patch.records is not None else {}
    if target in records or not (patch.context_valid and patch.quantum_valid):
        return None
    context_site, quantum_site, outcome_site, head_site = branch_sites(
        patch.rotation, patch.phase, patch.origin
    )

    if target == outcome_site and not patch.spent and head_site not in records:
        if sum(abs(a - b) for a, b in zip(target, quantum_site)) != 1:
            return None
        no_record, formation = instrument_effects(
            patch.rotation, patch.menu, patch.formation_hazard
        )
        effects = rotated_effects(patch.rotation, patch.menu)
        outcomes: list[tuple[Fraction, Matrix | None]] = [
            (qtrace_product(patch.omega, no_record), None)
        ]
        outcomes.extend(
            (
                qtrace_product(patch.omega, branch_effect),
                b63.outcome_carrier(effect, outcome + 1),
            )
            for outcome, (branch_effect, effect) in enumerate(zip(formation, effects))
        )
        return BootstrapDistribution("outcome", tuple(outcomes))

    if target == head_site and outcome_site in records:
        if (
            sum(abs(a - b) for a, b in zip(target, context_site)) != 1
            or sum(abs(a - b) for a, b in zip(target, outcome_site)) != 1
        ):
            return None
        decoded = b64.outcome_decode(records[outcome_site])
        if decoded is None:
            return None
        effect, outcome = decoded
        effects = rotated_effects(patch.rotation, patch.menu)
        if effect != effects[outcome]:
            return None
        next_head = b64.context_carrier(
            "head",
            b63.normalized_effect_state(effect),
            patch.rotation,
            1 - patch.menu,
            1 - patch.phase,
        )
        return BootstrapDistribution("finalize", ((Fraction(1), next_head),))
    return None


def bootstrap_active_sites(patch: Patch) -> dict[Coord, BootstrapDistribution]:
    _, _, outcome_site, head_site = branch_sites(
        patch.rotation, patch.phase, patch.origin
    )
    return {
        site: distribution
        for site in (outcome_site, head_site)
        if (distribution := bootstrap_local_distribution(patch, site)) is not None
    }


def realized_bootstrap_patch(patch: Patch, outcome: int) -> Patch:
    """Execute one named formation branch and its forced finalization."""

    if outcome not in (0, 1, 2):
        raise ValueError("outcome index must be 0, 1, or 2")
    active = bootstrap_active_sites(patch)
    if len(active) != 1:
        raise ValueError("bootstrap must have exactly one stochastic target")
    outcome_site, distribution = next(iter(active.items()))
    if distribution.kind != "outcome" or not distribution.normalized:
        raise ValueError("bootstrap stochastic distribution is invalid")
    weight, carrier = distribution.outcomes[outcome + 1]
    if weight <= 0 or carrier is None:
        raise ValueError("requested formation branch has zero weight")
    records = dict(patch.records or {})
    records[outcome_site] = carrier
    after_outcome = Patch(
        patch.omega,
        patch.rotation,
        patch.menu,
        patch.phase,
        patch.formation_hazard,
        patch.origin,
        patch.context_valid,
        patch.quantum_valid,
        True,
        records,
    )
    active = bootstrap_active_sites(after_outcome)
    if len(active) != 1:
        raise ValueError("realized outcome must force exactly one successor head")
    head_site, finalization = next(iter(active.items()))
    if finalization.kind != "finalize" or finalization.outcomes[0][0] != 1:
        raise ValueError("bootstrap finalization is invalid")
    records[head_site] = finalization.outcomes[0][1]  # type: ignore[assignment]
    return Patch(
        patch.omega,
        patch.rotation,
        patch.menu,
        patch.phase,
        patch.formation_hazard,
        patch.origin,
        patch.context_valid,
        patch.quantum_valid,
        True,
        records,
    )


def distribution_weights(branches: tuple[Branch, ...]) -> tuple[Fraction, ...]:
    return tuple(branch.weight for branch in branches)


def valid_patch(context_valid: bool, targets_blank: bool, spent: bool) -> bool:
    return context_valid and targets_blank and not spent


def attachment_stage(
    live_context: bool,
    live_quantum: bool,
    outcome_present: bool,
    head_present: bool,
) -> tuple[str, ...]:
    if not (live_context and live_quantum) or head_present:
        return ()
    if not outcome_present:
        return ("outcome",)
    return ("finalize",)


@dataclass(frozen=True)
class Continuation:
    ok: bool
    records: Records
    history: tuple[int, ...]
    active_checks: int


def continue_block64(
    records: Records,
    horizon: int,
    innovations: tuple[Fraction, ...],
) -> Continuation:
    answer = dict(records)
    history: list[int] = []
    checks = 0
    for event in range(horizon):
        for expected_kind in ("relay", "outcome", "finalize"):
            active = b64.active_sites(answer)
            checks += 1
            if len(active) != 1:
                return Continuation(False, answer, tuple(history), checks)
            target, distribution = next(iter(active.items()))
            if distribution.kind != expected_kind or not distribution.normalized:
                return Continuation(False, answer, tuple(history), checks)
            if expected_kind == "outcome":
                outcome, carrier = b64.choose(
                    distribution, innovations[event % len(innovations)]
                )
                history.append(outcome)
            else:
                _, carrier = b64.choose(distribution, Fraction(0))
            answer = b64.append_one(answer, target, carrier)
    return Continuation(True, answer, tuple(history), checks)


def future_cylinder_weight(state: b63.State, word: tuple[int, ...]) -> Fraction:
    weight = Fraction(1)
    current = state
    for outcome in word:
        probability, current = b63.transition(current, outcome)
        weight *= probability
    return weight


def transformed_records(
    records: Records,
    rotation: Rotation,
    shift: Coord,
) -> Records:
    return {
        b64.add(b64.rotate_coord(rotation, site), shift): b64.rotate_carrier(rotation, carrier)
        for site, carrier in records.items()
    }


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "state_independent",
            "ontic_density_copy",
            "clean_bank",
            "nonlocal_bootstrap",
            "host_schedule",
            "finite_stock",
            "contextual_shared",
            "rate_selected",
            "note_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    block64 = BLOCK64_NOTE.read_text(encoding="utf-8")
    cycle713 = CYCLE713_NOTE.read_text(encoding="utf-8")
    cycle883 = CYCLE883_NOTE.read_text(encoding="utf-8")
    selection = SELECTION_NOTE.read_text(encoding="utf-8")
    source_surface = " ".join(
        " ".join(item.split())
        for item in (note, axiom, block64, cycle713, cycle883, selection)
    )
    source_ok = all(
        phrase in source_surface
        for phrase in (
            "it does not supply the formation site, probability, or rate",
            "autonomous preparation of the first head by a matter engine",
            "It is not an occurrence selector",
            "first clean genesis, dirty-input admission/fault repair, and physical occurrence/start trigger",
            "normalized kernel on monotone Record extensions",
            "Cycle 883 already closes conditional renewal",
        )
    )
    checks.check(
        "A-current-source-and-route-correction",
        source_ok,
        "current axioms, Block 64, Cycle 713, Cycle 883, and the prior selection cut are literal; reset/renewal is not reopened",
    )

    rho_a = b63.matrix(1, 0, 0, 0)
    rho_b = b63.pure_real(Fraction(3, 5), Fraction(4, 5))
    rho_mix = b63.matrix_scale(Fraction(1, 2), b63.IDENTITY)
    omega_a = product_state(P1, rho_a)
    omega_b = product_state(P1, rho_b)
    omega_pointer_plus = product_state(PPLUS, rho_b)
    instrument_normalized = True
    cp_minimum = 1.0
    effect_cases = 0
    for rotation in b64.ROTATIONS:
        for menu in (0, 1):
            for hazard in (Fraction(1), Fraction(3, 4)):
                no_record, formation = instrument_effects(rotation, menu, hazard)
                instrument_normalized &= qadd(no_record, sum_qmatrices(formation)) == qidentity(4)
                cp_minimum = min(cp_minimum, branch_choi_minimum(rotation, menu, hazard))
                effect_cases += 1
    state_dependent = (
        distribution_weights(bootstrap_distribution(omega_a, b64.IDENTITY_ROTATION, 0, 0, Fraction(1)))
        != distribution_weights(bootstrap_distribution(omega_b, b64.IDENTITY_ROTATION, 0, 0, Fraction(1)))
    )
    if mutation == "state_independent":
        state_dependent = False
    pointer_weights = distribution_weights(
        bootstrap_distribution(omega_pointer_plus, b64.IDENTITY_ROTATION, 0, 0, Fraction(3, 4))
    )
    instrument_ok = (
        instrument_normalized
        and cp_minimum > -2e-12
        and state_dependent
        and sum(pointer_weights) == 1
        and sum(pointer_weights[1:]) == Fraction(3, 8)
    )
    checks.check(
        "B-coherent-pointer-state-dependent-CP-instrument",
        instrument_ok,
        f"{effect_cases} frame/menu/hazard effect resolutions normalize; CP Choi min={cp_minimum:.3e}; coherent pointer formation weight=3/8",
    )

    head_a = b64.context_carrier("head", rho_a, b64.IDENTITY_ROTATION, 0, 0)
    head_b = b64.context_carrier("head", b63.matrix(0, 0, 0, 1), b64.IDENTITY_ROTATION, 0, 0)
    head_mix = b64.context_carrier("head", rho_mix, b64.IDENTITY_ROTATION, 0, 0)
    deterministic_mix = {head_mix: Fraction(1)}
    mixture_of_labels = {head_a: Fraction(1, 2), head_b: Fraction(1, 2)}
    no_copy = deterministic_mix != mixture_of_labels
    omega_left = product_state(P1, rho_a)
    omega_right = product_state(P1, b63.matrix(0, 0, 0, 1))
    omega_half = qscale(Fraction(1, 2), qadd(omega_left, omega_right))
    weights_left = distribution_weights(bootstrap_distribution(omega_left, b64.IDENTITY_ROTATION, 0, 0, Fraction(1)))
    weights_right = distribution_weights(bootstrap_distribution(omega_right, b64.IDENTITY_ROTATION, 0, 0, Fraction(1)))
    weights_half = distribution_weights(bootstrap_distribution(omega_half, b64.IDENTITY_ROTATION, 0, 0, Fraction(1)))
    affine_repair = weights_half == tuple(
        (left + right) / 2 for left, right in zip(weights_left, weights_right)
    )
    repair_heads_known = all(
        b64.decode_context(branch.record_map()[branch_sites(b64.IDENTITY_ROTATION, 0)[3]]).rho
        == b63.normalized_effect_state(effect)
        for branch, effect in zip(
            bootstrap_distribution(omega_half, b64.IDENTITY_ROTATION, 0, 0, Fraction(1))[1:],
            b63.MENUS[0],
        )
    )
    if mutation == "ontic_density_copy":
        no_copy = False
    checks.check(
        "C-no-unknown-density-copy-branch-first-repair",
        no_copy and affine_repair and repair_heads_known,
        "deterministic exact-density Record labeling fails mixture affinity; branch weights are affine and every successor head carries the fixed effect-normalized state",
    )

    dirty_inputs = (
        product_state(P0, rho_a),
        product_state(P1, rho_b),
        product_state(PPLUS, rho_mix),
        bell_state(),
        qscale(Fraction(1, 4), qidentity(4)),
    )
    dirty_ok = all(
        qdensity(omega)
        and sum(distribution_weights(bootstrap_distribution(omega, b64.IDENTITY_ROTATION, 0, 0, Fraction(3, 4)))) == 1
        for omega in dirty_inputs
    )
    disposition_ok = (
        valid_patch(True, True, False)
        and not valid_patch(False, True, False)
        and not valid_patch(True, False, False)
        and not valid_patch(True, True, True)
    )
    if mutation == "clean_bank":
        dirty_ok = False
    checks.check(
        "D-total-pointer-density-and-dirty-disposition",
        dirty_ok and disposition_ok,
        "five arbitrary/coherent/entangled joint densities normalize; invalid, occupied, and spent patches refuse without a clean-bank premise",
    )

    local_cases = 0
    local_ok = True
    for rotation in b64.ROTATIONS:
        for phase in (0, 1):
            context_site, quantum_site, outcome_site, head_site = branch_sites(rotation, phase)
            if mutation == "nonlocal_bootstrap":
                quantum_site = b64.add(context_site, b64.scale(2, signed_side(rotation, phase)))
            distances = (
                sum(abs(a - b) for a, b in zip(quantum_site, outcome_site)),
                sum(abs(a - b) for a, b in zip(context_site, head_site)),
                sum(abs(a - b) for a, b in zip(outcome_site, head_site)),
            )
            branches = bootstrap_distribution(product_state(P1, rho_b), rotation, 0, phase, Fraction(1))
            formed = branches[1:]
            patch = Patch(product_state(P1, rho_b), rotation, 0, phase, Fraction(1))
            initial_active = bootstrap_active_sites(patch)
            sequential = tuple(realized_bootstrap_patch(patch, outcome) for outcome in range(3))
            local_ok &= (
                distances == (1, 1, 1)
                and attachment_stage(True, True, False, False) == ("outcome",)
                and attachment_stage(True, True, True, False) == ("finalize",)
                and attachment_stage(True, True, True, True) == ()
                and len(initial_active) == 1
                and next(iter(initial_active.values())).kind == "outcome"
                and next(iter(initial_active.values())).normalized
                and all(
                    set(branch.record_map()) == set(done.records or {}) == {outcome_site, head_site}
                    and branch.record_map() == (done.records or {})
                    and bootstrap_active_sites(done) == {}
                    and len(b64.active_sites(done.records or {})) == 1
                    and next(iter(b64.active_sites(done.records or {}).values())).kind == "relay"
                    for branch, done in zip(formed, sequential)
                )
            )
            local_cases += 1
    if mutation == "host_schedule":
        local_ok = False
    checks.check(
        "E-strict-NN-outcome-gated-bootstrap",
        local_ok and local_cases == 48,
        f"{local_cases}/48 frame/phase patches use three unit edges; local absence/presence forces outcome then head then the Block-64 relay",
    )

    stream = tuple(Fraction(value, 19) for value in (1, 5, 9, 13, 17, 3, 7, 11, 15))
    initial_branches = bootstrap_distribution(
        product_state(P1, b63.density_at_t(1)),
        b64.IDENTITY_ROTATION,
        0,
        0,
        Fraction(1),
    )[1:]
    continuation_ok = True
    continuation_records = 0
    continuation_checks = 0
    for first_outcome, branch in enumerate(initial_branches):
        run = continue_block64(branch.record_map(), 63, stream)
        full_support = b64.support_formula(64, b64.IDENTITY_ROTATION, 0)
        context_site, quantum_site, _, _ = branch_sites(b64.IDENTITY_ROTATION, 0)
        word = (first_outcome,) + run.history
        first_probability = branch.weight
        future_probability = future_cylinder_weight(
            (b63.normalized_effect_state(b63.MENUS[0][first_outcome]), 1),
            run.history,
        )
        continuation_ok &= (
            run.ok
            and len(run.history) == 63
            and run.active_checks == 189
            and len(run.records) == 191
            and set(run.records) == full_support - {context_site, quantum_site}
            and first_probability * future_probability
            == b63.cylinder_weight((b63.density_at_t(1), 0), word)
        )
        continuation_records = len(run.records)
        continuation_checks += run.active_checks
    if mutation == "finite_stock":
        continuation_ok = False
    checks.check(
        "F-exact-Block64-history-continuation",
        continuation_ok,
        f"all three first branches continue 63 events with {continuation_checks} unique microsteps; 64 outcomes occupy {continuation_records}=3*64-1 permanent Records",
    )

    base_rho = b63.pure_real(Fraction(3, 5), Fraction(4, 5))
    base_omega = product_state(P1, base_rho)
    covariance_ok = True
    covariance_cases = 0
    translations = (b64.ORIGIN, (7, -5, 3), (-11, 4, 9))
    for phase in (0, 1):
        base = bootstrap_distribution(base_omega, b64.IDENTITY_ROTATION, 0, phase, Fraction(3, 4))
        for rotation in b64.ROTATIONS:
            rotated_rho = b63.rotate_hermitian(rotation, base_rho)
            for shift in translations:
                transformed = bootstrap_distribution(
                    product_state(P1, rotated_rho), rotation, 0, phase, Fraction(3, 4), shift
                )
                covariance_ok &= all(
                    actual.kind == expected.kind
                    and actual.weight == expected.weight
                    and actual.record_map() == transformed_records(expected.record_map(), rotation, shift)
                    for actual, expected in zip(transformed, base)
                )
                covariance_cases += 1
    checks.check(
        "G-active-proper-cubic-translation-covariance",
        covariance_ok and covariance_cases == 144,
        f"{covariance_cases}/144 joint pointer/instrument/Record extension controls intertwine exactly",
    )

    fork_input = product_state(P1, rho_b)
    candidate_a = bootstrap_distribution(fork_input, b64.IDENTITY_ROTATION, 0, 0, Fraction(1))
    menu_fork = bootstrap_distribution(fork_input, b64.IDENTITY_ROTATION, 1, 0, Fraction(1))
    rate_fork = bootstrap_distribution(fork_input, b64.IDENTITY_ROTATION, 0, 0, Fraction(3, 4))
    shared_literal = candidate_a[1].record_map()[branch_sites(b64.IDENTITY_ROTATION, 0)[2]] == menu_fork[1].record_map()[branch_sites(b64.IDENTITY_ROTATION, 0)[2]]
    menu_distinct = distribution_weights(candidate_a) != distribution_weights(menu_fork)
    rate_distinct = (
        sum(branch.weight for branch in candidate_a[1:]) == 1
        and sum(branch.weight for branch in rate_fork[1:]) == Fraction(3, 4)
        and tuple(branch.weight / Fraction(3, 4) for branch in rate_fork[1:])
        == tuple(branch.weight for branch in candidate_a[1:])
    )
    if mutation == "contextual_shared":
        shared_literal = False
    if mutation == "rate_selected":
        rate_distinct = False
    checks.check(
        "H-extensional-menu-and-occurrence-forks",
        shared_literal and menu_distinct and rate_distinct,
        "menu 0/1 give distinct exact laws while preserving literal shared E0; hazards 1 and 3/4 change occurrence but not conditional content",
    )

    clause_needles = (
        "physical_state_domain",
        "pointer_projector",
        "admission_and_dirty_disposition",
        "formation_hazard",
        "causal_precedence",
        "effect_menu",
        "record_carrier",
        "next_head_decoder",
        "coframe_rule",
        "collision_domain",
        "clock_normalization",
        "claim_type: bounded_theorem",
        "No canonical axiom is edited",
        "zero TOE percentage movement",
        "### N1",
        "### N8",
    )
    boundary_ok = all(needle in note for needle in clause_needles) and mutation != "note_boundary"
    checks.check(
        "I-owner-clause-completeness-and-boundary",
        boundary_ok,
        "all eleven attachment fields are explicit; the packet is an unadopted bounded selection cut with no audit or TOE promotion",
    )

    print(
        f"METRICS effects={effect_cases} cp_min={cp_minimum:.3e} dirty_inputs={len(dirty_inputs)} "
        f"local_cases={local_cases}/48 continuation_microsteps={continuation_checks} records_N64={continuation_records} "
        f"covariance={covariance_cases}/144 menu_fork={distribution_weights(candidate_a)}!={distribution_weights(menu_fork)}"
    )
    print(
        "BOUNDARY: a branch-first coherent-pointer instrument can seed the unchanged Block-64 front without copying an unknown density, but physical-state ontology, menu/frame/decoder, occurrence hazard, global conflicts, clock, and law adoption are extensional owner choices"
    )
    return checks.finish()


def sum_qmatrices(items: tuple[QMatrix, ...]) -> QMatrix:
    if not items:
        raise ValueError("matrix family must be nonempty")
    answer = qzero(len(items[0]))
    for item in items:
        answer = qadd(answer, item)
    return answer


if __name__ == "__main__":
    raise SystemExit(main())
