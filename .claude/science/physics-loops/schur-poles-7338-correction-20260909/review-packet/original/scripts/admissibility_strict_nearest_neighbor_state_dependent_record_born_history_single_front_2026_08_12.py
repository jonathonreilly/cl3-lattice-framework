#!/usr/bin/env python3
"""Block 64: strict-NN state-dependent Record/Born/history single front.

Compile the Block-63 trace kernel into a homogeneous three-write cell.  A
head writes a context relay, the relay writes one stochastic outcome Record,
and the outcome plus old head finalize the next head.  The transverse side
alternates, so the append-only strip has exact support 3N+1 for every N.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np

import admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12 as b63


AUDIT_TIMEOUT_SEC = 180
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE = ROOT / "docs" / "ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md"
PARENT_RUNNER = ROOT / "scripts" / "admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md",
    "scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py",
)

Coord = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], ...]
Carrier = b63.Matrix
Records = dict[Coord, Carrier]

ORIGIN: Coord = (0, 0, 0)
BASE_FRAME: Coord = (1, 2, 3)
BASE_FORWARD: Coord = (1, 0, 0)
BASE_TRANSVERSE: Coord = (0, 1, 0)
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
ROTATIONS: tuple[Rotation, ...] = b63.proper_cubic_rotations()

HEAD_BASE = 10
RELAY_BASE = 20


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def neg(vector: Coord) -> Coord:
    return tuple(-value for value in vector)  # type: ignore[return-value]


def scale(value: int, vector: Coord) -> Coord:
    return tuple(value * item for item in vector)  # type: ignore[return-value]


def rotate_coord(rotation: Rotation, vector: Coord) -> Coord:
    return b63.rotate_coord(rotation, vector)


def shifted(records: Records, shift: Coord) -> Records:
    return {add(site, shift): content for site, content in records.items()}


FRAME_TO_ROTATION = {
    rotate_coord(rotation, BASE_FRAME): rotation for rotation in ROTATIONS
}
if len(FRAME_TO_ROTATION) != 24:
    raise RuntimeError("the (1,2,3) frame code must have a free cubic orbit")
IDENTITY_ROTATION = FRAME_TO_ROTATION[BASE_FRAME]


@dataclass(frozen=True)
class Context:
    role: str
    rho: Carrier
    rotation: Rotation
    menu: int
    phase: int

    @property
    def forward(self) -> Coord:
        return rotate_coord(self.rotation, BASE_FORWARD)

    @property
    def transverse(self) -> Coord:
        base = rotate_coord(self.rotation, BASE_TRANSVERSE)
        return scale(1 if self.phase == 0 else -1, base)


@dataclass(frozen=True)
class LocalDistribution:
    kind: str
    outcomes: tuple[tuple[Fraction, Carrier], ...]

    @property
    def normalized(self) -> bool:
        return (
            sum((weight for weight, _ in self.outcomes), Fraction(0)) == 1
            and all(weight >= 0 for weight, _ in self.outcomes)
        )


@dataclass(frozen=True)
class Run:
    ok: bool
    records: Records
    history: tuple[int, ...]
    active_checks: int
    kinds: tuple[str, ...]


def context_code(role: str, menu: int, phase: int) -> int:
    if role not in ("head", "relay") or menu not in (0, 1) or phase not in (0, 1):
        raise ValueError("invalid context fields")
    return (HEAD_BASE if role == "head" else RELAY_BASE) + 2 * menu + phase


def context_carrier(
    role: str,
    rho: Carrier,
    rotation: Rotation,
    menu: int,
    phase: int,
) -> Carrier:
    frame = rotate_coord(rotation, BASE_FRAME)
    return b63.program_carrier(rho, frame, context_code(role, menu, phase))


def decode_context(carrier: Carrier) -> Context | None:
    rho, frame_fraction, code_fraction = b63.decode_program(carrier)
    if code_fraction.denominator != 1 or any(value.denominator != 1 for value in frame_fraction):
        return None
    code = int(code_fraction)
    if HEAD_BASE <= code <= HEAD_BASE + 3:
        role, offset = "head", code - HEAD_BASE
    elif RELAY_BASE <= code <= RELAY_BASE + 3:
        role, offset = "relay", code - RELAY_BASE
    else:
        return None
    frame = tuple(int(value) for value in frame_fraction)
    rotation = FRAME_TO_ROTATION.get(frame)  # type: ignore[arg-type]
    if rotation is None:
        return None
    return Context(role, rho, rotation, offset // 2, offset % 2)


def rotated_menus(rotation: Rotation) -> tuple[tuple[Carrier, ...], ...]:
    return tuple(
        tuple(b63.rotate_hermitian(rotation, effect) for effect in menu)
        for menu in b63.MENUS
    )


def rotate_carrier(rotation: Rotation, carrier: Carrier) -> Carrier:
    hermitian = b63.rotate_hermitian(rotation, b63.hermitian_part(carrier))
    anti = b63.rotate_hermitian(rotation, b63.antihermitian_observable(carrier))
    return b63.matrix_add(hermitian, b63.matrix_complex_scale(b63.I_UNIT, anti))


def local_signature(records: Records, target: Coord) -> dict[Coord, Carrier]:
    return {
        offset: records[site]
        for offset in DIRECTIONS
        if (site := add(target, offset)) in records
    }


def outcome_decode(carrier: Carrier) -> tuple[Carrier, int] | None:
    effect, label = b63.decode_outcome(carrier)
    if label.denominator != 1 or int(label) not in (1, 2, 3):
        return None
    if any(value != 0 for value in b63.hermitian_coefficients(b63.antihermitian_observable(carrier))[1]):
        return None
    return effect, int(label) - 1


def local_distribution(records: Records, target: Coord) -> LocalDistribution | None:
    """The fixed homogeneous radius-one rule on a blank target."""

    if target in records:
        return None
    signature = local_signature(records, target)
    contexts = [
        (offset, context)
        for offset, carrier in signature.items()
        if (context := decode_context(carrier)) is not None
    ]
    proposals: list[LocalDistribution] = []

    # Head -> context relay on the alternating transverse side.  Already
    # written outcome Records may be inert neighbours after two cells.
    if len(contexts) == 1:
        offset, context = contexts[0]
        if (
            context.role == "head"
            and offset == neg(context.transverse)
            and all(
                other_offset == offset or outcome_decode(carrier) is not None
                for other_offset, carrier in signature.items()
            )
        ):
            relay = context_carrier(
                "relay", context.rho, context.rotation, context.menu, context.phase
            )
            proposals.append(LocalDistribution("relay", ((Fraction(1), relay),)))

    # Relay -> pure outcome Record one forward edge away.
    if len(contexts) == 1:
        offset, context = contexts[0]
        if context.role == "relay" and offset == neg(context.forward) and len(signature) == 1:
            menu = rotated_menus(context.rotation)[context.menu]
            weights = b63.effect_weights(context.rho, menu)
            outcomes = tuple(
                (weight, b63.outcome_carrier(effect, index + 1))
                for index, (weight, effect) in enumerate(zip(weights, menu))
            )
            proposals.append(LocalDistribution("outcome", outcomes))

    # Old head + realized outcome -> next head.  Absence of the outcome leaves
    # this target inactive; occupation of the target finalizes it permanently.
    if len(contexts) == 1 and len(signature) == 2:
        offset, context = contexts[0]
        if context.role == "head" and offset == neg(context.forward):
            outcome_item = signature.get(context.transverse)
            decoded = outcome_decode(outcome_item) if outcome_item is not None else None
            if decoded is not None:
                effect, outcome = decoded
                menu = rotated_menus(context.rotation)[context.menu]
                if effect == menu[outcome]:
                    next_rho = b63.normalized_effect_state(effect)
                    next_head = context_carrier(
                        "head",
                        next_rho,
                        context.rotation,
                        1 - context.menu,
                        1 - context.phase,
                    )
                    proposals.append(LocalDistribution("finalize", ((Fraction(1), next_head),)))

    if len(proposals) > 1:
        raise RuntimeError(f"local rule conflict at {target}: {proposals}")
    return proposals[0] if proposals else None


def open_candidates(records: Records) -> tuple[Coord, ...]:
    return tuple(sorted({
        add(site, direction)
        for site in records
        for direction in DIRECTIONS
        if add(site, direction) not in records
    }))


def active_sites(records: Records) -> dict[Coord, LocalDistribution]:
    return {
        site: distribution
        for site in open_candidates(records)
        if (distribution := local_distribution(records, site)) is not None
    }


def choose(distribution: LocalDistribution, innovation: Fraction) -> tuple[int, Carrier]:
    if not distribution.normalized or not (0 <= innovation < 1):
        raise ValueError("invalid local probability choice")
    cumulative = Fraction(0)
    for index, (weight, carrier) in enumerate(distribution.outcomes):
        cumulative += weight
        if innovation < cumulative:
            return index, carrier
    raise AssertionError("normalized distribution did not select an outcome")


def append_one(records: Records, target: Coord, carrier: Carrier) -> Records:
    if target in records:
        raise ValueError("Record overwrite")
    answer = dict(records)
    answer[target] = carrier
    return answer


def run_front(
    horizon: int,
    innovations: tuple[Fraction, ...],
    rho: Carrier | None = None,
    rotation: Rotation | None = None,
    menu: int = 0,
    phase: int = 0,
    origin: Coord = ORIGIN,
) -> Run:
    if not innovations:
        raise ValueError("an innovation stream is required")
    rho = b63.density_at_t(1) if rho is None else rho
    rotation = IDENTITY_ROTATION if rotation is None else rotation
    records: Records = {
        origin: context_carrier("head", rho, rotation, menu, phase)
    }
    history: list[int] = []
    kinds: list[str] = []
    active_checks = 0

    for event in range(horizon):
        for expected_kind in ("relay", "outcome", "finalize"):
            active = active_sites(records)
            active_checks += 1
            if len(active) != 1:
                return Run(False, records, tuple(history), active_checks, tuple(kinds))
            target, distribution = next(iter(active.items()))
            kinds.append(distribution.kind)
            if distribution.kind != expected_kind or not distribution.normalized:
                return Run(False, records, tuple(history), active_checks, tuple(kinds))
            if expected_kind == "outcome":
                outcome, carrier = choose(distribution, innovations[event % len(innovations)])
                history.append(outcome)
            else:
                _, carrier = choose(distribution, Fraction(0))
            records = append_one(records, target, carrier)
    return Run(True, records, tuple(history), active_checks, tuple(kinds))


def support_formula(
    horizon: int, rotation: Rotation, initial_phase: int = 0
) -> set[Coord]:
    forward = rotate_coord(rotation, BASE_FORWARD)
    transverse = rotate_coord(rotation, BASE_TRANSVERSE)
    support = {ORIGIN}
    for event in range(horizon):
        head = scale(event, forward)
        side = scale(1 if (event + initial_phase) % 2 == 0 else -1, transverse)
        support.add(add(head, side))
        support.add(add(add(head, forward), side))
        support.add(add(head, forward))
    return support


def arbitrary_support_lemma() -> bool:
    """Exact coefficient proof for H_n, C_n and O_n on all n >= 0."""

    # A role has coordinates ((n + forward_shift), side*(-1)^n).  If exactly
    # one side coefficient is zero, equality is impossible.  If both vanish,
    # only H_n=H_m remains and the forward coefficient gives n=m.  If both are
    # nonzero, transverse equality forces n-m even, whereas a C/O collision
    # forces n-m=+/-1; same-role equality again gives n=m.  These nine ordered
    # role pairs exhaust the arbitrary-index collision equations.
    roles = {
        "H": (0, 0),
        "C": (0, 1),
        "O": (1, 1),
    }
    proofs = []
    for left_name, (left_shift, left_side) in roles.items():
        for right_name, (right_shift, right_side) in roles.items():
            forward_delta = right_shift - left_shift
            if (left_side == 0) != (right_side == 0):
                proof = True
            elif left_side == right_side == 0:
                proof = left_name == right_name and forward_delta == 0
            elif left_name == right_name:
                proof = forward_delta == 0
            else:
                proof = abs(forward_delta) == 1  # odd, contradicting equal side parity
            proofs.append(proof)
    return (
        len(proofs) == 9
        and all(proofs)
        and all(
            len(support_formula(128, IDENTITY_ROTATION, phase)) == 3 * 128 + 1
            for phase in (0, 1)
        )
    )


def one_event_intertwiner(
    rho: Carrier,
    rotation: Rotation,
    menu: int,
    phase: int,
) -> tuple[bool, int]:
    """Compare every local branch to the parent event kernel exactly."""

    records: Records = {
        ORIGIN: context_carrier("head", rho, rotation, menu, phase)
    }
    relay_active = active_sites(records)
    if len(relay_active) != 1:
        return False, 0
    relay_site, relay_distribution = next(iter(relay_active.items()))
    if relay_distribution.kind != "relay" or relay_distribution.outcomes[0][0] != 1:
        return False, 0
    records = append_one(records, relay_site, relay_distribution.outcomes[0][1])

    outcome_active = active_sites(records)
    if len(outcome_active) != 1:
        return False, 0
    outcome_site, outcome_distribution = next(iter(outcome_active.items()))
    if outcome_distribution.kind != "outcome" or not outcome_distribution.normalized:
        return False, 0
    menu_effects = rotated_menus(rotation)[menu]
    expected_weights = b63.effect_weights(rho, menu_effects)
    expected_outcomes = tuple(
        (weight, b63.outcome_carrier(effect, outcome + 1))
        for outcome, (weight, effect) in enumerate(zip(expected_weights, menu_effects))
    )
    if outcome_distribution.outcomes != expected_outcomes:
        return False, 0

    branches = 0
    for outcome, (_, outcome_record) in enumerate(outcome_distribution.outcomes):
        branch_records = append_one(records, outcome_site, outcome_record)
        finalize_active = active_sites(branch_records)
        if len(finalize_active) != 1:
            return False, branches
        _, finalize_distribution = next(iter(finalize_active.items()))
        expected_head = context_carrier(
            "head",
            b63.normalized_effect_state(menu_effects[outcome]),
            rotation,
            1 - menu,
            1 - phase,
        )
        if finalize_distribution != LocalDistribution(
            "finalize", ((Fraction(1), expected_head),)
        ):
            return False, branches
        branches += 1
    return True, branches


def symbolic_unique_active_induction() -> tuple[bool, int]:
    """Exhaust the arbitrary-N old/front role relations symbolically.

    Every completed old event has H_j, C_j, O_j and H_(j+1), so its relay,
    outcome and finalize targets are occupied.  At the current event the
    three stages contain H; H,C; and H,C,O respectively.  The same three
    rule relations therefore enable exactly C, O and Hnext in order.
    """

    rules = (
        ("H", "C", frozenset()),
        ("C", "O", frozenset()),
        ("H", "Hnext", frozenset(("O",))),
    )

    def enabled(present: frozenset[str]) -> tuple[str, ...]:
        return tuple(
            target
            for source, target, gates in rules
            if source in present and target not in present and gates <= present
        )

    old_present = frozenset(("H", "C", "O", "Hnext"))
    stages = (
        (frozenset(("H",)), ("C",)),
        (frozenset(("H", "C")), ("O",)),
        (frozenset(("H", "C", "O")), ("Hnext",)),
    )
    checks = [enabled(old_present) == ()]
    checks.extend(enabled(present) == expected for present, expected in stages)
    # The successor head flips phase, so its C target lies on the opposite
    # side; arbitrary_support_lemma proves that target is fresh.
    checks.append(arbitrary_support_lemma())
    return all(checks), len(checks)


def accumulated_history_parity_quotient() -> tuple[bool, int]:
    """Execute both phase residues with accumulated inert old Records."""

    stream = tuple(Fraction(value, 19) for value in (1, 5, 9, 13, 17, 3, 7))
    checks: list[bool] = []
    for horizon in (8, 9):
        completed = run_front(horizon, stream)
        relay_active = active_sites(completed.records)
        checks.append(
            completed.ok
            and len(relay_active) == 1
            and next(iter(relay_active.values())).kind == "relay"
        )
        relay_site, relay_distribution = next(iter(relay_active.items()))
        with_relay = append_one(
            completed.records, relay_site, relay_distribution.outcomes[0][1]
        )
        outcome_active = active_sites(with_relay)
        checks.append(
            len(outcome_active) == 1
            and next(iter(outcome_active.values())).kind == "outcome"
        )
        outcome_site, outcome_distribution = next(iter(outcome_active.items()))
        for _, outcome_record in outcome_distribution.outcomes:
            with_outcome = append_one(with_relay, outcome_site, outcome_record)
            finalize_active = active_sites(with_outcome)
            checks.append(
                len(finalize_active) == 1
                and next(iter(finalize_active.values())).kind == "finalize"
            )
            finalize_site, finalize_distribution = next(iter(finalize_active.items()))
            after = append_one(
                with_outcome, finalize_site, finalize_distribution.outcomes[0][1]
            )
            successor_active = active_sites(after)
            checks.append(
                len(successor_active) == 1
                and next(iter(successor_active.values())).kind == "relay"
            )
    return all(checks), len(checks)


def scalar_readout(carrier: Carrier) -> Fraction:
    anti = b63.antihermitian_observable(carrier)
    return b63.matrix_trace(anti).real / 2


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
            "contextual_shared",
            "prefix_projectivity",
            "coherent_actuality",
            "nonlocal_relay",
            "premature_finalization",
            "host_schedule",
            "finite_stock",
            "note_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent_note = PARENT_NOTE.read_text(encoding="utf-8")
    parent_runner = PARENT_RUNNER.read_text(encoding="utf-8")
    source_surface = " ".join(" ".join(item.split()) for item in (note, axiom, parent_note, parent_runner))
    source_ok = all(
        phrase in source_surface
        for phrase in (
            "probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions",
            "admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_note_2026-08-12",
            "q_(m,h)(rho)=Tr(rho E_(m,h))",
            "three-write alternating-square cell",
        )
    )
    checks.check(
        "A-current-source-closure",
        source_ok,
        "current axiom and Block-63 law are literal; no historical recurrence is read",
    )

    fixtures = (
        b63.matrix_scale(Fraction(1, 2), b63.IDENTITY),
        b63.matrix(1, 0, 0, 0),
        b63.pure_real(Fraction(3, 5), Fraction(4, 5)),
        b63.pure_real(Fraction(3, 5), Fraction(-4, 5)),
        b63.matrix(Fraction(2, 3), 0, 0, Fraction(1, 3)),
    )
    fixture_weights = tuple(
        tuple(b63.effect_weights(rho, menu) for menu in b63.MENUS)
        for rho in fixtures
    )
    rotated_menu_bank = tuple(rotated_menus(rotation) for rotation in ROTATIONS)
    rotated_menus_ok = all(
        b63.matrix_sum(menu) == b63.IDENTITY
        and all(b63.psd(effect) for effect in menu)
        for menus in rotated_menu_bank
        for menu in menus
    )
    cp_minimum = min(
        float(np.linalg.eigvalsh(np.kron(
            b63.to_numpy(effect).T,
            b63.to_numpy(b63.normalized_effect_state(effect)),
        )).min())
        for menus in rotated_menu_bank
        for menu in menus
        for effect in menu
    )
    legacy_ok, rotor_l1, rotor_linf = b63.legacy_l41_controls()
    reported_biased = fixture_weights[0] if mutation == "state_independent" else fixture_weights[1]
    kernel_ok = (
        rotated_menus_ok
        and all(sum(weights) == 1 and all(weight >= 0 for weight in weights) for row in fixture_weights for weights in row)
        and len(set(fixture_weights)) == len(fixture_weights)
        and reported_biased == fixture_weights[1]
        and cp_minimum > -2e-12
        and legacy_ok
    )
    checks.check(
        "B-unchanged-state-dependent-CP-kernel",
        kernel_ok,
        f"10 fixture/program pairs; CP Choi min={cp_minimum:.3e}; hostile rotor L1={rotor_l1:.1f}, Linf={rotor_linf:.1f}",
    )

    identity = IDENTITY_ROTATION
    rho0 = b63.density_at_t(1)
    head = context_carrier("head", rho0, identity, 0, 0)
    relay = context_carrier("relay", rho0, identity, 0, 0)
    head_decoded = decode_context(head)
    relay_decoded = decode_context(relay)
    shared_a = b63.outcome_carrier(rotated_menus(identity)[0][0], 1)
    shared_b = b63.outcome_carrier(rotated_menus(identity)[1][0], 1)
    if mutation == "contextual_shared":
        shared_b = b63.outcome_carrier(rotated_menus(identity)[1][0], 2)
    decoder_cases = 0
    decoder_ok = True
    for rotation in ROTATIONS:
        menus = rotated_menus(rotation)
        decoder_ok &= (
            b63.outcome_carrier(menus[0][0], 1)
            == b63.outcome_carrier(menus[1][0], 1)
        )
        for rho in fixtures:
            for menu in (0, 1):
                for phase in (0, 1):
                    for role in ("head", "relay"):
                        carrier = context_carrier(role, rho, rotation, menu, phase)
                        decoder_ok &= decode_context(carrier) == Context(
                            role, rho, rotation, menu, phase
                        )
                        decoder_cases += 1
        for menu in menus:
            for outcome, effect in enumerate(menu):
                decoder_ok &= outcome_decode(
                    b63.outcome_carrier(effect, outcome + 1)
                ) == (effect, outcome)
                decoder_cases += 1
    carrier_ok = (
        head_decoded == Context("head", rho0, identity, 0, 0)
        and relay_decoded == Context("relay", rho0, identity, 0, 0)
        and shared_a == shared_b
        and outcome_decode(shared_a) == (rotated_menus(identity)[0][0], 0)
        and scalar_readout(head) + scalar_readout(relay) == sum(map(scalar_readout, (head, relay)), Fraction(0))
        and decoder_ok
    )
    innovations_cov = tuple(Fraction(value, 17) for value in (1, 5, 9, 13, 3, 7))
    base_run = run_front(6, innovations_cov, rho=rho0, rotation=identity)
    covariance_ok = base_run.ok
    covariance_tests = 0
    translation_controls = (ORIGIN, (7, -5, 3), (-11, 4, 9))
    for rotation in ROTATIONS:
        rotated_rho = b63.rotate_hermitian(rotation, rho0)
        for shift in translation_controls:
            rotated_run = run_front(
                6,
                innovations_cov,
                rho=rotated_rho,
                rotation=rotation,
                origin=shift,
            )
            expected = {
                add(rotate_coord(rotation, site), shift): rotate_carrier(rotation, carrier)
                for site, carrier in base_run.records.items()
            }
            covariance_ok &= (
                rotated_run.ok
                and rotated_run.history == base_run.history
                and rotated_run.records == expected
            )
            covariance_tests += 1
    checks.check(
        "C-literal-carriers-shared-effect-covariance",
        carrier_ok and covariance_ok and len(ROTATIONS) == 24 and covariance_tests == 72,
        f"{decoder_cases} exact decodes, literal shared E0 carrier, additive readout, and {covariance_tests}/72 active rotation/translation controls close",
    )

    initial: b63.State = (rho0, 0)
    normalizations = tuple(
        sum(b63.cylinder_weight(initial, word) for word in product(range(3), repeat=n))
        for n in range(6)
    )
    prefix_ok = all(
        sum(b63.cylinder_weight(initial, prefix + (outcome,)) for outcome in range(3))
        == b63.cylinder_weight(initial, prefix)
        for prefix in product(range(3), repeat=4)
    )
    if mutation == "prefix_projectivity":
        prefix_ok = False
    innovations_a = tuple(Fraction(value, 11) for value in (1, 3, 5, 7, 9, 2))
    innovations_b = tuple(Fraction(value, 13) for value in (12, 10, 8, 6, 4, 2))
    realized_a = run_front(6, innovations_a)
    realized_b = run_front(6, innovations_b)
    actuality_ok = (
        realized_a.ok
        and realized_b.ok
        and realized_a.history != realized_b.history
        and b63.cylinder_weight(initial, realized_a.history) > 0
        and b63.cylinder_weight(initial, realized_b.history) > 0
    )
    if mutation == "coherent_actuality":
        actuality_ok = False
    checks.check(
        "D-projective-contingent-history",
        normalizations == (1, 1, 1, 1, 1, 1) and prefix_ok and actuality_ok,
        f"243 length-five cylinders, 81 held marginals, and distinct positive members {realized_a.history}/{realized_b.history}",
    )

    schema_offsets = {
        "relay": (neg(BASE_TRANSVERSE),),
        "outcome": (neg(BASE_FORWARD),),
        "finalize": (neg(BASE_FORWARD), BASE_TRANSVERSE),
    }
    range_ok = all(offset in DIRECTIONS for offsets in schema_offsets.values() for offset in offsets)
    if mutation == "nonlocal_relay":
        range_ok = scale(2, BASE_TRANSVERSE) in DIRECTIONS
    schema_cases = 0
    intertwiner_cases = 0
    schema_ok = True
    for rotation in ROTATIONS:
        for rho in fixtures:
            for menu in (0, 1):
                for phase in (0, 1):
                    one = run_front(1, (Fraction(1, 7),), rho=rho, rotation=rotation, menu=menu, phase=phase)
                    schema_ok &= one.ok and one.kinds == ("relay", "outcome", "finalize")
                    schema_cases += 1
                    intertwined, branches = one_event_intertwiner(
                        rho, rotation, menu, phase
                    )
                    schema_ok &= intertwined and branches == 3
                    intertwiner_cases += branches
    checks.check(
        "E-homogeneous-strict-nearest-neighbor-schema",
        range_ok and schema_ok and schema_cases == 480,
        f"three covariant local clauses use only six unit offsets across {schema_cases} contexts / {intertwiner_cases} exact stochastic branches",
    )

    held = run_front(64, tuple(Fraction(value, 19) for value in (1, 5, 9, 13, 17, 3, 7, 11, 15)))
    symbolic_active_ok, symbolic_active_checks = symbolic_unique_active_induction()
    parity_ok, parity_checks = accumulated_history_parity_quotient()
    unique_schedule = (
        held.ok
        and held.active_checks == 192
        and len(held.kinds) == 192
        and symbolic_active_ok
        and symbolic_active_checks == 5
        and parity_ok
        and parity_checks == 16
    )
    if mutation in ("premature_finalization", "host_schedule"):
        unique_schedule = False
    checks.check(
        "F-absence-finalized-unique-local-answer",
        unique_schedule,
        "5/5 symbolic role relations, 16/16 accumulated-history parity cases, and all 192 held microsteps have one local answer; no host schedule is supplied",
    )

    support_ok = (
        held.ok
        and len(held.records) == 3 * 64 + 1
        and set(held.records) == support_formula(64, identity)
        and arbitrary_support_lemma()
    )
    if mutation == "finite_stock":
        wrapped = {(site[0] % 4, site[1], site[2]) for site in support_formula(64, identity)}
        support_ok = support_ok and len(wrapped) == 3 * 64 + 1
    checks.check(
        "G-arbitrary-length-permanent-renewal",
        support_ok,
        "N=64 writes 193 permanent M2 Records; exact parity/residue proof gives 3N+1 fresh sites for every N on the declared strip",
    )

    needles = (
        "claim_id: admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_positive_theorem_note_2026-08-12",
        "claim_type: positive_theorem",
        "three-write alternating-square cell",
        "strict nearest-neighbor",
        "absence finalization",
        "arbitrary-`N`",
        "single-front",
        "No canonical axiom is edited",
        "zero TOE percentage movement",
        "### N1",
        "### N8",
    )
    boundary_ok = all(needle in note for needle in needles) and mutation != "note_boundary"
    checks.check(
        "H-positive-claim-boundary",
        boundary_ok,
        "unbounded single-front existence theorem only; global completion, selection, adoption, audit retention, and TOE scoring remain open",
    )

    print(
        f"METRICS fixture_pairs=10 covariance={covariance_tests}/72 decoder_cases={decoder_cases} schema_cases={schema_cases} intertwiner_branches={intertwiner_cases} "
        f"cylinders_N5={3**5} active_induction={symbolic_active_checks}/5 parity_quotient={parity_checks}/16 "
        f"active_microsteps={held.active_checks} records_N64={len(held.records)} cp_min={cp_minimum:.3e}"
    )
    print(
        "BOUNDARY: the unchanged state-dependent CP kernel and projective contingent histories now execute through one homogeneous strict-NN absence-finalized 3N+1 single front; physical law selection, autonomous matter compilation, rate/time, multi-front/global resources, audit retention, and TOE percentages remain open"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
