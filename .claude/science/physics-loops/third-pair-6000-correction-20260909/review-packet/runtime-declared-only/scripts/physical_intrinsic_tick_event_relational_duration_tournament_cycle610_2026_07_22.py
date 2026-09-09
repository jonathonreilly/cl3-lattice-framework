#!/usr/bin/env python3
"""Cycle 610: intrinsic tick / event relational-duration tournament.

Decisive question: can the byte-pinned Cycle-230/578/583 contact-dimer matter
law, an explicitly supplied two-channel detector word, and the finite
event/counter/admission definitions implemented below jointly produce an
operational, additive, reproducible relational duration Delta-tau(A,B) between
locally admitted candidate events, with a no-refit motion- and
uniform-phase-conditioned clock-rate ratio?

Route A generates oriented tick events from the declared two-channel detector
word over the literal fixed-K fiber dynamics.  Route B turns tick certificates
into a predecessor-linked candidate-event chain with rollover receipts and
decodes additive relational intervals from the stored chain state only.
Route C freezes spectral (Birman-Schwinger) and field (N*Q) predictions for the
tick-rate ratios before the dynamics are inspected and reports agreement or
falsification without refit.

Firewalls: update count is not time; a tick ordinal is not proper time; wrapped
phase is not energy; a generator element is not a rate; a tick certificate is a
candidate opportunity, not an occurrence; an admitted chain cell is a
conditional candidate Record (actuality/admissibility/law-domain supplied), not
a framework Record; proper-cubic covariance is not Lorentz covariance.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import json
import math
import sys
import time
from dataclasses import dataclass, field
from hashlib import sha256
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22 as c583

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_"
    "CYCLE610_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_intrinsic_tick_event_relational_duration_tournament_"
    "cycle610_receipt_2026_07_22.json"
)

AUTHORITY = "none"
AUDIT = "unset"

BETA_TRAIN = -0.3
BETA_HELD = -0.35
CONTACT = 0.37
L_TRAIN = 9
L_HELD = 13
Q_TRAIN = 4096
Q_HELD = 2048
Q_SKIP = 64
V_FLOOR = 1e-8
EXACT = 1e-12
WEYL_DIM = 16
FIELD_ROWS = tuple((q, s) for q in (1, 2, 3, 8) for s in (+1, -1))
K_TRAIN_0 = np.zeros(3)
K_TRAIN_1 = np.asarray((2 * np.pi * 3 / 128, 0.0, 0.0))
K_HELD = np.asarray((2 * np.pi * 6 / 128, 0.0, 0.0))
BANK_SIZE = 24
BANK_REFILL = 8
WALL_CAP_SECONDS = 360.0

FROZEN_CONTRACT_SHA256 = (
    "52666bb481107d722f976a4ebb72943d802211acac84e6108dca8f5daa233406"
)

DEPENDENCY_SHA256 = {
    "common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py":
        "4ef60441d31d62b1fc61c9b5e09ff3bc8f7f32d1b68bc3c548834431d24302f6",
    "physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py":
        "ef6805e691a1ddd303a96f7cabd7000517e0cf33d5b1c577b20c2cbbf29aca23",
}

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def dependency_controls() -> None:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCY_SHA256}
    check(
        "every consumed shore runner is byte exact",
        observed == DEPENDENCY_SHA256,
        {name: value[:12] for name, value in observed.items()},
    )


# ----------------------------------------------------------------------------
# Fiber machinery: literal fixed-K antisymmetric two-CAR free-plus-contact law.
# ----------------------------------------------------------------------------

J2 = c583.J2
A2_FULL = c583.A2_FULL
ONSITE_PROJ = J2 @ J2.conj().T


def momentum_grid(length: int) -> np.ndarray:
    axis = 2 * np.pi * np.arange(length) / length
    grid = np.stack(np.meshgrid(axis, axis, axis, indexing="ij"), axis=-1)
    return grid.reshape(-1, 3)


def coin2(beta: float) -> np.ndarray:
    coin = c219.common_species(beta).coin
    return np.kron(coin, coin)


def free_stack(length: int, total_momentum: np.ndarray, beta: float) -> np.ndarray:
    grid = momentum_grid(length)
    relative = c210.DIRECTIONS[:, None, :] - c210.DIRECTIONS[None, :, :]
    center = c210.DIRECTIONS[:, None, :] + c210.DIRECTIONS[None, :, :]
    phase = np.exp(
        -1j * (
            np.einsum("pk,ijk->pij", grid, relative)
            + 0.5 * np.einsum("k,ijk->ij", total_momentum, center)[None, :, :]
        )
    ).reshape(len(grid), 36)
    return phase[:, :, None] * coin2(beta)[None, :, :]


def swap_index() -> np.ndarray:
    order = np.empty(36, int)
    for d1 in range(6):
        for d2 in range(6):
            order[d1 * 6 + d2] = d2 * 6 + d1
    return order


SWAP36 = swap_index()


def negate_grid_index(length: int) -> np.ndarray:
    """Flat index map sending grid momentum p to -p (mod 2*pi)."""
    single = (length - np.arange(length)) % length
    idx = np.arange(length**3).reshape(length, length, length)
    return idx[np.ix_(single, single, single)].reshape(-1)


def antisym_defect(state: np.ndarray, length: int) -> float:
    mirrored = state[negate_grid_index(length)][:, SWAP36]
    return float(np.linalg.norm(state + mirrored))


def a2_source(length: int) -> np.ndarray:
    state = np.tile(A2_FULL.astype(complex), (length**3, 1))
    return state / np.linalg.norm(state)


def apply_update(state: np.ndarray, stack: np.ndarray, alpha: float = 0.0) -> np.ndarray:
    """One literal fiber update: free stream, onsite contact, uniform-field phase."""
    state = np.einsum("pij,pj->pi", stack, state)
    uniform = state.mean(axis=0)
    correction = (np.exp(1j * CONTACT) - 1) * (ONSITE_PROJ @ uniform)
    state = state + correction[None, :]
    if alpha:
        state = state * np.exp(1j * alpha)
    return state


def apply_inverse(state: np.ndarray, stack: np.ndarray, alpha: float = 0.0) -> np.ndarray:
    if alpha:
        state = state * np.exp(-1j * alpha)
    uniform = state.mean(axis=0)
    correction = (np.exp(-1j * CONTACT) - 1) * (ONSITE_PROJ @ uniform)
    state = state + correction[None, :]
    return np.einsum("pji,pj->pi", stack.conj(), state)


def evolve_word(
    stack: np.ndarray,
    source: np.ndarray,
    steps: int,
    alpha: float = 0.0,
    length: int | None = None,
    contact_on: bool = True,
) -> dict[str, object]:
    """Iterate the law and record the onsite word c00_q = <a|G^q|a>.

    The declared two-channel aggregate follows exactly from unitarity:
    <d|G^q|a> = (c00_q + c00_{q-1})/sqrt(2), with c00_{-1} = conj(c00_1).
    """
    state = source.copy()
    c00 = np.empty(steps + 1, complex)
    norm_defect = 0.0
    anti_defect = 0.0
    stride = max(1, steps // 64)
    for q in range(steps + 1):
        c00[q] = np.vdot(source, state)
        if q == steps:
            break
        if contact_on:
            state = apply_update(state, stack, alpha)
        else:
            state = np.einsum("pij,pj->pi", stack, state)
            if alpha:
                state = state * np.exp(1j * alpha)
        if q % stride == 0:
            norm_defect = max(norm_defect, abs(np.linalg.norm(state) - 1.0))
            if length is not None:
                anti_defect = max(anti_defect, antisym_defect(state, length))
    aggregate = np.empty(steps + 1, complex)
    aggregate[0] = (c00[0] + np.conj(c00[1])) / math.sqrt(2)
    aggregate[1:] = (c00[1:] + c00[:-1]) / math.sqrt(2)
    return {
        "c00": c00,
        "aggregate": aggregate,
        "norm_defect": norm_defect,
        "antisym_defect": anti_defect,
        "final_state": state,
    }


# ----------------------------------------------------------------------------
# Birman-Schwinger spectral predictor (independent of the dynamics loop).
# ----------------------------------------------------------------------------

def bs_matrix(stack: np.ndarray, phase: float) -> np.ndarray:
    z = np.exp(1j * phase)
    blocks = stack - z * np.eye(36)[None, :, :]
    solved = np.linalg.solve(blocks, np.broadcast_to(J2, (len(stack), 36, 15)))
    accumulator = np.einsum("ki,pkj->ij", J2.conj(), solved)
    return np.eye(15) - z * (np.exp(-1j * CONTACT) - 1) * accumulator / len(stack)


def a2_branch_value(stack: np.ndarray, phase: float) -> tuple[float, np.ndarray]:
    """|eigenvalue| of the B(z) branch whose eigenvector maximizes A2 overlap.

    At K = 0 the A2 contact channel is exactly one-dimensional, so this branch
    is the Cycle-583 scalar; at K != 0 it is the continuously deformed branch
    (amendment 1 of the frozen contract).
    """
    matrix = bs_matrix(stack, phase)
    values, vectors = np.linalg.eig(matrix)
    overlaps = np.abs(c583.A2_AXIS.conj() @ vectors)
    branch = int(np.argmax(overlaps))
    return float(abs(values[branch])), vectors[:, branch]


def bs_root(
    length: int,
    total_momentum: np.ndarray,
    beta: float,
    window: tuple[float, float] = (-3.12, -2.80),
    coarse: int = 33,
) -> dict[str, object]:
    stack = free_stack(length, total_momentum, beta)
    phases = np.linspace(window[0], window[1], coarse)
    values = [a2_branch_value(stack, p)[0] for p in phases]
    center = int(np.argmin(values))
    lo = phases[max(0, center - 1)]
    hi = phases[min(coarse - 1, center + 1)]
    for _ in range(64):
        third = (hi - lo) / 3
        a, b = lo + third, hi - third
        if a2_branch_value(stack, a)[0] < a2_branch_value(stack, b)[0]:
            hi = b
        else:
            lo = a
        if hi - lo < 1e-11:
            break
    root = 0.5 * (lo + hi)
    branch_value, null_vector = a2_branch_value(stack, root)
    overlap = abs(np.vdot(c583.A2_AXIS, null_vector))
    return {
        "theta": float(root),
        "branch_abs_value": float(branch_value),
        "null_A2_overlap": float(overlap),
        "eta": null_vector,
    }


def bound_state(
    length: int, total_momentum: np.ndarray, beta: float, root: dict[str, object]
) -> tuple[np.ndarray, float]:
    """Fiber bound eigenvector from the BS null vector, with eigen residual."""
    stack = free_stack(length, total_momentum, beta)
    z = np.exp(1j * float(root["theta"]))
    eta = np.asarray(root["eta"], complex)
    blocks = stack - z * np.eye(36)[None, :, :]
    onsite = (J2 @ eta).reshape(1, 36, 1)
    psi = np.linalg.solve(blocks, np.broadcast_to(onsite, (len(stack), 36, 1)))[:, :, 0]
    psi = psi / np.linalg.norm(psi)
    evolved = apply_update(psi.copy(), stack)
    residual = float(np.linalg.norm(evolved - z * psi))
    return psi, residual


# ----------------------------------------------------------------------------
# Tick machinery: lift, oriented crossings, convention control.
# ----------------------------------------------------------------------------

def wrap_angle(value: float) -> float:
    wrapped = math.fmod(value + math.pi, 2 * math.pi)
    if wrapped <= 0:
        wrapped += 2 * math.pi
    return wrapped - math.pi


def lift_sequence(word: np.ndarray) -> dict[str, object]:
    lifts = np.zeros(len(word))
    defined = np.zeros(len(word), bool)
    phases = np.angle(word)
    for q in range(1, len(word)):
        if abs(word[q]) >= V_FLOOR and abs(word[q - 1]) >= V_FLOOR:
            lifts[q] = wrap_angle(float(phases[q] - phases[q - 1]))
            defined[q] = True
    cumulative = np.cumsum(lifts)
    return {"lifts": lifts, "defined": defined, "cumulative": cumulative}


def tick_events(
    cumulative: np.ndarray, defined: np.ndarray, law: str, skip: int
) -> list[tuple[int, int]]:
    """Oriented crossing events of the cumulative lift.

    T1 crosses multiples of 2*pi; T2 crosses odd multiples of pi.  Events stop
    at the first undefined lift (undefined is never coerced to a tick).
    """
    events: list[tuple[int, int]] = []
    if law == "T1":
        def marker(value: float) -> int:
            return math.floor(value / (2 * math.pi))
    else:
        def marker(value: float) -> int:
            return math.floor((value - math.pi) / (2 * math.pi))
    previous = marker(float(cumulative[skip]))
    for q in range(skip + 1, len(cumulative)):
        if not defined[q]:
            break
        current = marker(float(cumulative[q]))
        if current != previous:
            events.append((q, +1 if current > previous else -1))
        previous = current
    return events


def tick_rate(events: list[tuple[int, int]], skip: int, total: int) -> float:
    signed = sum(orientation for _, orientation in events)
    return signed / (total - skip)


def clock_row(word: np.ndarray, skip: int, law: str = "T1") -> dict[str, object]:
    """Rate plus the amendment-1 lock certificate (lawful-domain condition).

    A word is inside the tick law's lawful domain only when every lift in the
    window is defined and the two half-window rates agree within twice the
    half-window discretization bound.  Unlocked words are undefined for
    rate-law tests and are reported, never coerced.
    """
    total = len(word) - 1
    lifted = lift_sequence(word)
    events = tick_events(lifted["cumulative"], lifted["defined"], law, skip)
    rate = tick_rate(events, skip, total)
    middle = skip + (total - skip) // 2
    first = [e for e in events if e[0] <= middle]
    second = [e for e in events if e[0] > middle]
    rate_1 = tick_rate(first, skip, middle)
    rate_2 = tick_rate(second, middle, total)
    half_bound = 2 * (2 / (total - skip))
    locked = (
        bool(lifted["defined"][skip + 1 :].all())
        and abs(rate_1 - rate_2) <= half_bound
    )
    fine_rate = (
        float(lifted["cumulative"][-1] - lifted["cumulative"][skip])
        / ((total - skip) * 2 * math.pi)
        if bool(lifted["defined"][skip + 1 :].all())
        else None
    )
    return {
        "rate": rate, "count": len(events), "events": events,
        "locked": locked, "rate_half1": rate_1, "rate_half2": rate_2,
        "fine_rate": fine_rate, "lifted": lifted,
    }


# ----------------------------------------------------------------------------
# Route B: candidate-event chain with rollover receipts and interval decoding.
# ----------------------------------------------------------------------------

@dataclass
class EventCell:
    identity: int
    rotor: int
    carry: int
    predecessor: int | None
    binder: int
    valid: int
    orientation: int


@dataclass
class EventChain:
    bank: int
    cells: list[EventCell] = field(default_factory=list)
    admitted_ticks: set[int] = field(default_factory=set)
    exhausted: bool = False

    def admit(
        self,
        tick_id: int,
        orientation: int,
        certificate: int,
        binder: int,
        actuality: int,
        admissibility: int,
        law_domain: int,
    ) -> str:
        opportunity = certificate & binder
        if not opportunity:
            return "no_opportunity"
        fresh = int(tick_id not in self.admitted_ticks)
        if not fresh:
            return "refused_fresh"
        if not (actuality & admissibility & law_domain):
            return "refused_supplied"
        if len(self.cells) >= self.bank:
            self.exhausted = True
            return "exhausted"
        previous = self.cells[-1] if self.cells else None
        rotor_prev = previous.rotor if previous else 14
        rotor = (rotor_prev + 1) % 16
        self.cells.append(
            EventCell(
                identity=tick_id,
                rotor=rotor,
                carry=int(rotor == 0),
                predecessor=previous.identity if previous else None,
                binder=binder,
                valid=1,
                orientation=orientation,
            )
        )
        self.admitted_ticks.add(tick_id)
        return "admitted"

    def refill(self, extra: int) -> None:
        self.bank += extra
        self.exhausted = False

    def interval(self, start_identity: int, end_identity: int) -> int | None:
        """Decode Delta-tau from the stored chain state only."""
        ids = [cell.identity for cell in self.cells]
        if start_identity not in ids or end_identity not in ids:
            return None
        start = ids.index(start_identity)
        end = ids.index(end_identity)
        if start > end:
            reverse = self.interval(end_identity, start_identity)
            return None if reverse is None else -reverse
        span = self.cells[start + 1 : end + 1]
        expected = self.cells[start].identity
        for cell in span:
            if cell.predecessor != expected or not cell.valid or not cell.binder:
                return None
            expected = cell.identity
        carries = sum(cell.carry for cell in span)
        rotor_delta = self.cells[end].rotor - self.cells[start].rotor
        return 16 * carries + rotor_delta


# ----------------------------------------------------------------------------
# Frame covariance helper.
# ----------------------------------------------------------------------------

def frame_word(
    length: int, total_momentum: np.ndarray, beta: float, frame: np.ndarray, steps: int
) -> np.ndarray:
    stack = free_stack(length, frame @ total_momentum, beta)
    return evolve_word(stack, a2_source(length), steps)["aggregate"]


# ----------------------------------------------------------------------------
# Main tournament.
# ----------------------------------------------------------------------------

def sanitize_root(root: dict[str, object]) -> dict[str, float]:
    return {key: float(value) for key, value in root.items() if key != "eta"}


def main() -> int:
    start = time.time()
    receipt: dict[str, object] = {
        "cycle": 610,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "frozen_contract_sha256": FROZEN_CONTRACT_SHA256,
        "parameters": {
            "beta_train": BETA_TRAIN, "beta_held": BETA_HELD, "contact": CONTACT,
            "L_train": L_TRAIN, "L_held": L_HELD, "Q_train": Q_TRAIN,
            "Q_held": Q_HELD, "Q_skip": Q_SKIP, "v_floor": V_FLOOR,
            "weyl_dim": WEYL_DIM, "field_rows": [list(row) for row in FIELD_ROWS],
            "K_rows": [list(K_TRAIN_0), list(K_TRAIN_1), list(K_HELD)],
            "bank": BANK_SIZE, "refill": BANK_REFILL,
        },
    }
    dependency_controls()

    # ---- Spectral predictions (computed before dynamics are inspected).
    spectral = {
        "train_K0": bs_root(L_TRAIN, K_TRAIN_0, BETA_TRAIN),
        "train_K1": bs_root(L_TRAIN, K_TRAIN_1, BETA_TRAIN),
        "held_K2": bs_root(L_HELD, K_HELD, BETA_TRAIN),
        "held_K0": bs_root(L_HELD, K_TRAIN_0, BETA_TRAIN),
        "beta_held": bs_root(L_TRAIN, K_TRAIN_0, BETA_HELD),
    }
    receipt["spectral_roots"] = {k: sanitize_root(v) for k, v in spectral.items()}
    theta0 = float(spectral["train_K0"]["theta"])
    check(
        "A2 bound-branch root exists near the landed Cycle-583 phase with an "
        "A2-dominant null vector",
        abs(theta0 + 2.9756) < 0.03
        and float(spectral["train_K0"]["null_A2_overlap"]) > 0.99,
        sanitize_root(spectral["train_K0"]),
    )
    psi_b, eig_residual = bound_state(L_TRAIN, K_TRAIN_0, BETA_TRAIN, spectral["train_K0"])
    check(
        "the BS null vector reconstructs a genuine fiber bound eigenvector",
        eig_residual < 1e-6 and antisym_defect(psi_b, L_TRAIN) < 1e-9,
        {"eigen_residual": eig_residual,
         "antisym": antisym_defect(psi_b, L_TRAIN),
         "source_overlap": float(abs(np.vdot(psi_b, a2_source(L_TRAIN))) ** 2)},
    )

    predicted0 = wrap_angle(theta0) / (2 * math.pi)
    bound_rate = 2 / (Q_TRAIN - Q_SKIP)
    bound_held = 2 / (Q_HELD - Q_SKIP)

    # ---- Route A: base train runs (raw source, purified confirmation).
    stack0 = free_stack(L_TRAIN, K_TRAIN_0, BETA_TRAIN)
    source = a2_source(L_TRAIN)
    base = evolve_word(stack0, source, Q_TRAIN, length=L_TRAIN)
    check(
        "norm and antisymmetry are preserved by the literal law",
        base["norm_defect"] < 1e-10 and base["antisym_defect"] < 1e-10,
        {"norm": base["norm_defect"], "antisym": base["antisym_defect"]},
    )
    c00 = base["c00"]
    check(
        "P4: the onsite single-channel word has exact q=1 darkness at fiber "
        "level while q=3 is bright",
        abs(c00[1]) < EXACT and abs(c00[3]) > 1e-3,
        {"abs_c00_1": float(abs(c00[1])), "abs_c00_3": float(abs(c00[3])),
         "abs_c00_2": float(abs(c00[2]))},
    )
    aggregate = base["aggregate"]
    visibility = np.abs(aggregate[1:13])
    check(
        "the declared two-channel aggregate is bright at every early q",
        bool(np.all(visibility > 1e-6)),
        {"min_visibility_q1_12": float(visibility.min())},
    )

    raw_row = clock_row(aggregate, Q_SKIP, "T1")
    raw_row_t2 = clock_row(aggregate, Q_SKIP, "T2")
    pure_run = evolve_word(stack0, psi_b, Q_TRAIN)
    pure_row = clock_row(pure_run["aggregate"], Q_SKIP, "T1")
    check(
        "P1 purified: the bound-branch clock locks and its tick rate equals "
        "the Birman-Schwinger prediction without refit",
        pure_row["locked"] and abs(pure_row["rate"] - predicted0) < bound_rate + 1e-9,
        {"rate": pure_row["rate"], "predicted": predicted0,
         "locked": pure_row["locked"]},
    )
    check(
        "P1 fine: the stored lift-sum rate (same word data, finer than "
        "the integer tick count) matches the spectral root to 1e-6",
        pure_row["fine_rate"] is not None
        and abs(pure_row["fine_rate"] - predicted0) < 1e-6,
        {"fine_rate": pure_row["fine_rate"], "predicted": predicted0},
    )
    check(
        "P1 raw source: if the raw onsite-A2 clock locks it must match the "
        "prediction; an unlocked raw clock is a domain-boundary measurement "
        "(reported, never coerced)",
        (not raw_row["locked"]) or abs(raw_row["rate"] - predicted0) < bound_rate + 1e-9,
        {"rate": raw_row["rate"], "locked": raw_row["locked"],
         "halves": (raw_row["rate_half1"], raw_row["rate_half2"]),
         "predicted": predicted0},
    )
    check(
        "tick-unit convention shifts counts but not rates (T1 versus T2)",
        abs(raw_row["rate"] - raw_row_t2["rate"]) < 2 * bound_rate
        and abs(raw_row["count"] - raw_row_t2["count"])
        <= max(4, 0.01 * max(raw_row["count"], 1)),
        {"rate_T1": raw_row["rate"], "rate_T2": raw_row_t2["rate"],
         "count_T1": raw_row["count"], "count_T2": raw_row_t2["count"]},
    )
    receipt["route_a_train"] = {
        "raw": {k: raw_row[k] for k in
                ("rate", "count", "locked", "rate_half1", "rate_half2", "fine_rate")},
        "raw_T2": {k: raw_row_t2[k] for k in ("rate", "count", "locked")},
        "purified": {k: pure_row[k] for k in ("rate", "count", "locked", "fine_rate")},
        "predicted_rate": predicted0,
        "bound_eigen_residual": eig_residual,
        "odd_darkness": {"q1": float(abs(c00[1])), "q3": float(abs(c00[3]))},
    }

    # Orientation: the reversed history flips the signed tick rate.
    rev_row = clock_row(np.conj(pure_run["aggregate"]), Q_SKIP, "T1")
    check(
        "orientation: the reversed history has the opposite signed tick rate",
        abs(rev_row["rate"] + pure_row["rate"]) < 2 * bound_rate,
        {"rate_forward": pure_row["rate"], "rate_reversed": rev_row["rate"]},
    )

    # Unwrap certificate on the purified word.
    lifted_pure = pure_row["lifted"]
    budget = float(lifted_pure["cumulative"][-1] - lifted_pure["cumulative"][Q_SKIP])
    endpoint = wrap_angle(
        float(np.angle(pure_run["aggregate"][-1]) - np.angle(pure_run["aggregate"][Q_SKIP]))
    )
    residual = abs(wrap_angle(budget - endpoint))
    check(
        "unwrap certificate: the stored lift chain reconciles with the "
        "endpoint principal phase modulo 2*pi",
        residual < 1e-6,
        {"residual": residual},
    )

    # Missed-crossing control: stride-2 sampling aliases exactly as predicted.
    stride2 = pure_run["aggregate"][::2]
    s2_row = clock_row(stride2, Q_SKIP // 2, "T1")
    rate_s2 = s2_row["rate"] / 2
    stride_pred = wrap_angle(2 * wrap_angle(theta0)) / (2 * math.pi) / 2
    check(
        "missed-crossing control: stride-2 subsampling aliases to the frozen "
        "fold prediction, demonstrating why the per-update lift is load-bearing",
        abs(rate_s2 - stride_pred) < 2 * bound_rate
        and abs(stride_pred - predicted0) > 0.1,
        {"stride2_rate_per_update": rate_s2, "aliased_prediction": stride_pred,
         "true_rate": predicted0},
    )

    # Preparation independence (independent calibration).
    prep_rows = {}
    prep_specs = {
        "raw_a2": None,
        "raw_a3": None,
        "pure_mix1": None,
        "pure_mix2": None,
    }
    prep2_raw = source + 0.3 * apply_update(source.copy(), stack0)
    prep_specs["raw_a2"] = prep2_raw / np.linalg.norm(prep2_raw)
    prep3_raw = source - 0.25 * apply_update(apply_update(source.copy(), stack0), stack0)
    prep_specs["raw_a3"] = prep3_raw / np.linalg.norm(prep3_raw)
    mix1 = psi_b + 0.15 * source
    prep_specs["pure_mix1"] = mix1 / np.linalg.norm(mix1)
    mix2 = psi_b - 0.10 * apply_update(source.copy(), stack0)
    prep_specs["pure_mix2"] = mix2 / np.linalg.norm(mix2)
    for label, prep in prep_specs.items():
        run = evolve_word(stack0, prep, Q_HELD)
        row = clock_row(run["aggregate"], Q_SKIP, "T1")
        prep_rows[label] = {
            "rate": row["rate"], "locked": row["locked"],
            "matched": bool(abs(row["rate"] - predicted0) < 2 * bound_held),
        }
    check(
        "independent calibration: every locked separately-prepared clock of "
        "the same species ticks at the same asymptotic rate (locked rows must "
        "match; unlocked rows are domain-boundary reports)",
        all((not row["locked"]) or row["matched"] for row in prep_rows.values())
        and any(row["locked"] and row["matched"] for row in prep_rows.values()),
        prep_rows,
    )
    receipt["preparation_rates"] = prep_rows

    # Contact deletion: the intrinsic clock line vanishes with the contact law.
    free_run = evolve_word(stack0, psi_b, Q_HELD, contact_on=False)
    free_row = clock_row(free_run["aggregate"], Q_SKIP, "T1")
    late_free = np.abs(free_run["aggregate"][Q_SKIP:])
    check(
        "contact deletion: without the contact law the bound-branch clock "
        "decays toward the visibility floor, unlocks, or leaves the "
        "bound-branch prediction",
        (float(np.median(late_free)) < 0.05)
        or (not free_row["locked"])
        or abs(free_row["rate"] - predicted0) > 5 * bound_held,
        {"median_late_visibility": float(np.median(late_free)),
         "locked": free_row["locked"], "rate": free_row["rate"]},
    )

    # Detector deletion: the single-channel word has an undefined q=1 lift.
    lifted_single = lift_sequence(c00[:64])
    check(
        "detector deletion: removing the transported channel restores the "
        "q=1 undefined boundary (lift chain breaks)",
        not bool(lifted_single["defined"][1]),
        {"q1_defined": bool(lifted_single["defined"][1]),
         "q3_defined": bool(lifted_single["defined"][3])},
    )

    # Exact inverse: reverse the full word and restore the prepared source.
    state = base["final_state"].copy()
    for _ in range(Q_TRAIN):
        state = apply_inverse(state, stack0)
    inverse_residual = float(np.linalg.norm(state - source))
    check(
        "exact inverse: the reversed word restores the prepared source",
        inverse_residual < 1e-9 * math.sqrt(Q_TRAIN),
        {"inverse_residual": inverse_residual},
    )

    # All-24 frame covariance, including a K != 0 row.
    frames = c210.proper_cubic_frames()
    reference_k0 = frame_word(L_TRAIN, K_TRAIN_0, BETA_TRAIN, np.eye(3), 8)
    reference_k1 = frame_word(L_TRAIN, K_TRAIN_1, BETA_TRAIN, np.eye(3), 8)
    max_defect = 0.0
    for frame in frames:
        for reference, momentum in ((reference_k0, K_TRAIN_0), (reference_k1, K_TRAIN_1)):
            rotated = frame_word(L_TRAIN, momentum, BETA_TRAIN, frame, 8)
            max_defect = max(max_defect, float(np.max(np.abs(rotated - reference))))
    check(
        "all 24 proper-cubic frames leave the detector word invariant (the A2 "
        "sign cancels; the fiber family transforms covariantly)",
        max_defect < 1e-10,
        {"max_frame_defect": max_defect},
    )

    # ---- Route C: motion rows (raw primary, purified confirmation).
    stack1 = free_stack(L_TRAIN, K_TRAIN_1, BETA_TRAIN)
    theta1 = float(spectral["train_K1"]["theta"])
    ratio_pred = wrap_angle(theta1) / wrap_angle(theta0)
    ratio_bound = 3 * bound_rate / abs(predicted0)
    psi_b1, eig_res1 = bound_state(L_TRAIN, K_TRAIN_1, BETA_TRAIN, spectral["train_K1"])
    moving_raw = clock_row(evolve_word(stack1, source, Q_TRAIN)["aggregate"], Q_SKIP)
    moving_pure = clock_row(evolve_word(stack1, psi_b1, Q_TRAIN)["aggregate"], Q_SKIP)
    ratio_meas_pure = moving_pure["rate"] / pure_row["rate"]
    check(
        "P3 train purified: the moving-clock tick-rate ratio matches the "
        "no-refit spectral prediction",
        moving_pure["locked"] and eig_res1 < 1e-6
        and abs(ratio_meas_pure - ratio_pred) < ratio_bound,
        {"ratio_meas": ratio_meas_pure, "ratio_pred": ratio_pred,
         "bound": ratio_bound, "eig_residual_K1": eig_res1},
    )
    fine_ratio = (
        moving_pure["fine_rate"] / pure_row["fine_rate"]
        if moving_pure["fine_rate"] and pure_row["fine_rate"] else None
    )
    check(
        "P3 fine: the lift-sum rate ratio resolves the dispersion shift below "
        "the integer-tick bound and matches the spectral prediction to 1e-5",
        fine_ratio is not None and abs(fine_ratio - ratio_pred) < 1e-5,
        {"fine_ratio": fine_ratio, "ratio_pred": ratio_pred,
         "dispersion_effect": ratio_pred - 1.0},
    )
    raw_ratio = (
        moving_raw["rate"] / raw_row["rate"]
        if raw_row["locked"] and moving_raw["locked"] and raw_row["rate"] != 0
        else None
    )
    check(
        "P3 train raw: locked raw clocks must reproduce the same ratio; "
        "unlocked raw rows are domain-boundary reports",
        raw_ratio is None or abs(raw_ratio - ratio_pred) < ratio_bound,
        {"raw_ratio": raw_ratio, "raw_locked": raw_row["locked"],
         "moving_raw_locked": moving_raw["locked"]},
    )
    receipt["motion_rows"] = {
        "train": {"ratio_pred": ratio_pred, "ratio_meas_pure": ratio_meas_pure,
                  "ratio_meas_raw": raw_ratio, "fine_ratio": fine_ratio,
                  "raw_locked": bool(raw_row["locked"] and moving_raw["locked"])},
    }

    # Held-size motion row.
    theta_h0 = float(spectral["held_K0"]["theta"])
    theta_h2 = float(spectral["held_K2"]["theta"])
    held_ratio_pred = wrap_angle(theta_h2) / wrap_angle(theta_h0)
    psi_h0, eig_h0 = bound_state(L_HELD, K_TRAIN_0, BETA_TRAIN, spectral["held_K0"])
    psi_h2, eig_h2 = bound_state(L_HELD, K_HELD, BETA_TRAIN, spectral["held_K2"])
    held0 = evolve_word(free_stack(L_HELD, K_TRAIN_0, BETA_TRAIN), psi_h0, Q_HELD,
                        length=L_HELD)
    held2 = evolve_word(free_stack(L_HELD, K_HELD, BETA_TRAIN), psi_h2, Q_HELD)
    held0_row = clock_row(held0["aggregate"], Q_SKIP)
    held2_row = clock_row(held2["aggregate"], Q_SKIP)
    held_ratio_meas = held2_row["rate"] / held0_row["rate"]
    held_bound = 3 * bound_held / abs(wrap_angle(theta_h0) / (2 * math.pi))
    check(
        "P3 held: the held-size moving-clock ratio matches without refit and "
        "the held run preserves norm and antisymmetry",
        held0_row["locked"] and held2_row["locked"]
        and abs(held_ratio_meas - held_ratio_pred) < held_bound
        and held0["norm_defect"] < 1e-10 and held0["antisym_defect"] < 1e-10
        and max(eig_h0, eig_h2) < 1e-6,
        {"ratio_meas": held_ratio_meas, "ratio_pred": held_ratio_pred,
         "bound": held_bound, "norm": held0["norm_defect"],
         "antisym": held0["antisym_defect"]},
    )
    held_fine_ratio = (
        held2_row["fine_rate"] / held0_row["fine_rate"]
        if held2_row["fine_rate"] and held0_row["fine_rate"] else None
    )
    receipt["motion_rows"]["held"] = {
        "ratio_meas": held_ratio_meas, "ratio_pred": held_ratio_pred,
        "fine_ratio": held_fine_ratio,
    }
    check(
        "P3 held fine: the held-size lift-sum ratio matches the spectral "
        "prediction to 1e-5",
        held_fine_ratio is not None and abs(held_fine_ratio - held_ratio_pred) < 1e-5,
        {"fine_ratio": held_fine_ratio, "ratio_pred": held_ratio_pred,
         "dispersion_effect": held_ratio_pred - 1.0},
    )

    # Species row (held beta): the rate follows the species' own spectral root.
    psi_bh, eig_bh = bound_state(L_TRAIN, K_TRAIN_0, BETA_HELD, spectral["beta_held"])
    species = evolve_word(free_stack(L_TRAIN, K_TRAIN_0, BETA_HELD), psi_bh, Q_HELD)
    species_row = clock_row(species["aggregate"], Q_SKIP)
    species_pred = wrap_angle(float(spectral["beta_held"]["theta"])) / (2 * math.pi)
    check(
        "species variation: the held-beta clock rate follows its own spectral "
        "root (mass-parameter dependence, not a fitted constant)",
        species_row["locked"] and eig_bh < 1e-6
        and abs(species_row["rate"] - species_pred) < 2 * bound_held,
        {"rate": species_row["rate"], "predicted": species_pred},
    )
    receipt["species_row"] = {
        "rate": species_row["rate"], "predicted": species_pred,
        "theta_beta_held": float(spectral["beta_held"]["theta"]),
    }

    # ---- Route C: field rows (one literal dynamical row, then exact identity).
    alpha_literal = 2 * math.pi * (+1) * 2 * 1 / WEYL_DIM
    literal = evolve_word(stack0, source, 512, alpha=alpha_literal)
    modulated = c00[:513] * np.exp(1j * alpha_literal * np.arange(513))
    identity_defect = float(np.max(np.abs(literal["c00"] - modulated)))
    check(
        "P2 identity: the literal uniform-field dynamics equals the exact N*Q "
        "phase modulation of the field-off word (one dynamical row executed)",
        identity_defect < 1e-10,
        {"identity_defect": identity_defect},
    )
    field_rows = []
    all_match = True
    pure_aggregate = pure_run["aggregate"]
    for weyl_q, sign in FIELD_ROWS:
        alpha = 2 * math.pi * sign * 2 * weyl_q / WEYL_DIM
        modulation = np.exp(1j * alpha * np.arange(len(pure_aggregate)))
        row_pure = clock_row(pure_aggregate * modulation, Q_SKIP)
        row_raw = clock_row(aggregate * modulation[: len(aggregate)], Q_SKIP)
        pred_f = wrap_angle(theta0 + alpha) / (2 * math.pi)
        matched = row_pure["locked"] and abs(row_pure["rate"] - pred_f) < 2 * bound_rate
        all_match = all_match and matched
        field_rows.append({
            "weyl_Q": weyl_q, "sign": sign, "alpha": alpha,
            "rate_pure": row_pure["rate"], "rate_pred": pred_f,
            "ratio_pure": row_pure["rate"] / pure_row["rate"],
            "ratio_pred": wrap_angle(theta0 + alpha) / wrap_angle(theta0),
            "rate_raw": row_raw["rate"], "raw_locked": row_raw["locked"],
            "orientation_flip": bool(np.sign(row_pure["rate"]) != np.sign(pure_row["rate"])),
            "matched": bool(matched),
        })
    check(
        "P2: every frozen field row matches its no-refit wrapped prediction, "
        "including fold rows with orientation flips (stroboscopic discreteness "
        "signature of the candidate tick law)",
        all_match,
        {"rows": len(field_rows),
         "flips": sum(row["orientation_flip"] for row in field_rows)},
    )
    null_rows = [row for row in field_rows if row["weyl_Q"] == 8]
    check(
        "P2 null: the Q=8 rows are exact nulls (alpha wraps to 2*pi exactly)",
        all(abs(row["ratio_pure"] - 1.0) < 3 * bound_rate / abs(predicted0)
            for row in null_rows),
        {"null_ratios": [row["ratio_pure"] for row in null_rows]},
    )
    receipt["field_rows"] = field_rows

    # Comparator protocol versus the 3:4 / 5:4 shore (frozen; no identification).
    comparator = []
    for row in field_rows:
        for target, name in ((0.75, "3:4"), (1.25, "5:4")):
            if abs(row["ratio_pred"] - target) < 0.02:
                comparator.append({
                    "row": [row["weyl_Q"], row["sign"]],
                    "target": name,
                    "ratio_pred": row["ratio_pred"],
                })
    receipt["comparator_map"] = {
        "near_hits": comparator,
        "statement": (
            "algebraic reachability only; any cross-apparatus event "
            "association and empirical calibration are underived, so no "
            "physical identification with the 3:4/5:4 comparators is claimed"
        ),
    }
    check(
        "comparator map contains only the frozen Q=1, s=+1 near-hit in the "
        "3:4 class; cross-apparatus identification remains outside this runner",
        len(comparator) == 1
        and comparator[0]["row"] == [1, 1]
        and comparator[0]["target"] == "3:4",
        {"near_hits": len(comparator)},
    )

    # ---- Route B: event chain, admission, additive interval decoding.
    tick_stream = pure_row["events"]
    chain = EventChain(bank=BANK_SIZE)
    statuses = [
        chain.admit(tick_id=index, orientation=orientation, certificate=1,
                    binder=1, actuality=1, admissibility=1, law_domain=1)
        for index, (_, orientation) in enumerate(tick_stream[:40])
    ]
    admitted = [status for status in statuses if status == "admitted"]
    check(
        "route B: ticks are admitted through the declared opportunity and "
        "admission predicates until the finite bank exhausts",
        len(admitted) == BANK_SIZE and "exhausted" in statuses,
        {"admitted": len(admitted),
         "post_bank_statuses": statuses[BANK_SIZE:BANK_SIZE + 3]},
    )
    chain.refill(BANK_REFILL)
    post_refill = chain.admit(
        tick_id=100, orientation=-1, certificate=1, binder=1,
        actuality=1, admissibility=1, law_domain=1,
    )
    check(
        "route B renewal: one declared finite-bank refill extends the domain",
        post_refill == "admitted",
        {"post_refill": post_refill},
    )
    ids = [cell.identity for cell in chain.cells]
    a_id, b_id, c_id = ids[2], ids[11], ids[23]
    d_ab = chain.interval(a_id, b_id)
    d_bc = chain.interval(b_id, c_id)
    d_ac = chain.interval(a_id, c_id)
    check(
        "additivity: Delta(A,C) = Delta(A,B) + Delta(B,C) decoded from "
        "stored chain state across rollover receipts",
        d_ab is not None and d_bc is not None and d_ac == d_ab + d_bc
        and sum(cell.carry for cell in chain.cells) >= 1,
        {"d_ab": d_ab, "d_bc": d_bc, "d_ac": d_ac,
         "carries": sum(cell.carry for cell in chain.cells)},
    )
    check(
        "reversal: the decoded interval is orientation-antisymmetric",
        chain.interval(b_id, a_id) == -d_ab,
        {"forward": d_ab, "reverse": chain.interval(b_id, a_id)},
    )
    duplicate = chain.admit(
        tick_id=a_id, orientation=+1, certificate=1, binder=1,
        actuality=1, admissibility=1, law_domain=1,
    )
    check(
        "duplicate admission is refused by the derived freshness predicate",
        duplicate == "refused_fresh",
        {"status": duplicate},
    )
    no_binder = chain.admit(
        tick_id=555, orientation=+1, certificate=1, binder=0,
        actuality=1, admissibility=1, law_domain=1,
    )
    no_actuality = chain.admit(
        tick_id=556, orientation=+1, certificate=1, binder=1,
        actuality=0, admissibility=1, law_domain=1,
    )
    check(
        "binder deletion blocks the opportunity; deleting the supplied "
        "actuality token blocks admission (the supplied middle is explicit)",
        no_binder == "no_opportunity" and no_actuality == "refused_supplied",
        {"no_binder": no_binder, "no_actuality": no_actuality},
    )
    broken = EventChain(bank=BANK_SIZE)
    for index in range(6):
        broken.admit(tick_id=index, orientation=+1, certificate=1, binder=1,
                     actuality=1, admissibility=1, law_domain=1)
    removed = broken.cells.pop(3)
    check(
        "missing event: a lineage gap makes the interval undefined, never zero",
        broken.interval(broken.cells[0].identity, broken.cells[-1].identity) is None,
        {"removed_identity": removed.identity},
    )
    observer_a = EventChain(bank=BANK_SIZE)
    observer_b = EventChain(bank=BANK_SIZE)
    for index, (_, orientation) in enumerate(tick_stream[:12]):
        for observer in (observer_a, observer_b):
            observer.admit(tick_id=index, orientation=orientation, certificate=1,
                           binder=1, actuality=1, admissibility=1, law_domain=1)
    interval_a = observer_a.interval(
        observer_a.cells[1].identity, observer_a.cells[9].identity
    )
    interval_b = observer_b.interval(
        observer_b.cells[1].identity, observer_b.cells[9].identity
    )
    check(
        "independent observers: two chains fed by the same tick stream decode "
        "identical intervals",
        interval_a is not None and interval_a == interval_b,
        {"observer_a": interval_a, "observer_b": interval_b},
    )
    receipt["route_b"] = {
        "admitted_total": len(chain.cells),
        "sample_intervals": {"d_ab": d_ab, "d_bc": d_bc, "d_ac": d_ac},
        "carries": sum(cell.carry for cell in chain.cells),
    }

    # ---- Discipline and firewall summaries (full text lives in the note).
    receipt["n1_families"] = [
        "two-channel transported-detector tick clock (attempted, positive)",
        "onsite single-channel Ramsey clock (boundary reproduced here)",
        "controlled first-return comparator (unexecuted alternative)",
        "spectral-instrument pointer clock (unexecuted alternative)",
        "finite event/Record-candidate interval chain with supplied opportunity",
        "A2/T2 vernier beat clock (open)",
        "two-dimer encounter clock (open, N4 outside code)",
    ]
    receipt["interpretation_firewall"] = [
        "update count is not time; the tick ordinal is not proper time",
        "wrapped phase is not energy; a generator element is not a rate",
        "a tick certificate is a candidate opportunity, not an occurrence",
        "an admitted cell is a conditional candidate Record; actuality, "
        "admissibility, and law-domain tokens are supplied",
        "tick-rate ratios are dimensionless relational candidates, not lapse, "
        "redshift, or proper time",
        "proper-cubic covariance is not Lorentz covariance",
        "the uniform-field row is a supplied lawful field configuration; "
        "non-uniform field gradients across the packet remain open",
        "the purified source is a supplied preparation (disclosed); the raw "
        "onsite-A2 rows measure the lawful-domain boundary",
    ]

    elapsed = time.time() - start
    receipt["elapsed_seconds"] = elapsed
    receipt["pass_count"] = PASS
    receipt["fail_count"] = FAIL
    receipt["pass"] = FAIL == 0
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=1, default=float) + "\n", encoding="utf-8"
    )
    print("RESULT", PASS, FAIL, "elapsed", round(elapsed, 2), "s")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
