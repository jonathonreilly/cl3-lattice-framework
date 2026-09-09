#!/usr/bin/env python3
"""Cycle 611: autonomous bound-branch preparation tournament.

Decisive question: can a lawful, bounded, autonomous dynamics take the raw
onsite-A2 source (bound weight 0.2627, falsified as a clock by Cycle 610) to a
state that passes the UNCHANGED Cycle-610 clock certificates, with no spectral
data consulted by the preparation at runtime?

Routes: P-A echo-interference minus-port filter (602/605 controlled-contact
structure); P-B radius-1 window-conditioning cascade (590 Route-C pointer
style); P-C adiabatic contact ramp from the extremal contact phase.  The
bound-weight diagnostic is computed offline against the Birman-Schwinger
eigenvector and never enters preparation control flow.  Certification consumes
the byte-pinned Cycle-610 runner unchanged.

Firewalls: update count is not time; a preparation schedule is not time; the
conditioning pointer is not a Record; success probability is not Born
probability; the purifier certificates are operational, not actuality.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
import time
from hashlib import sha256
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

C610_NAME = (
    "physical_intrinsic_tick_event_relational_duration_tournament_"
    "cycle610_2026_07_22"
)
C610_SHA256 = "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac"
FROZEN_CONTRACT_SHA256 = (
    "1dab9ebb17ac1d351651da745ca698a15a3bc94648dd38c6222022df6df77bde"
)

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_"
    "CYCLE611_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_autonomous_bound_branch_preparation_tournament_"
    "cycle611_receipt_2026_07_22.json"
)

BETA = -0.3
CONTACT = 0.37
L_TRAIN = 9
L_HELD = 13
Q_CERT = 2048
Q_SKIP = 64
G_START = math.pi
RAMP_STEPS = (256, 1024, 4096)
FILTER_M = (8, 16)
FILTER_K = 12
CERT_K_GRID = (4, 8, 12)
WINDOW_RADIUS = 1
WALL_CAP_SECONDS = 600.0

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


def load_c610():
    path = ROOT / "scripts" / (C610_NAME + ".py")
    digest = sha256(path.read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location(C610_NAME, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[C610_NAME] = module
    spec.loader.exec_module(module)
    return module, digest


C610, C610_OBSERVED_SHA = load_c610()


# ----------------------------------------------------------------------------
# Position-representation engine (relative coordinate r on the odd torus).
# ----------------------------------------------------------------------------

def direction_deltas() -> np.ndarray:
    import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
    deltas = np.empty((36, 3), int)
    for d1 in range(6):
        for d2 in range(6):
            deltas[d1 * 6 + d2] = (
                c210.DIRECTIONS[d1] - c210.DIRECTIONS[d2]
            ).astype(int)
    return deltas


DELTAS = direction_deltas()


class PositionEngine:
    def __init__(self, length: int, beta: float):
        self.length = length
        self.coin2 = C610.coin2(beta)
        self.shape = (length, length, length, 36)

    def source(self) -> np.ndarray:
        state = np.zeros(self.shape, complex)
        state[0, 0, 0, :] = C610.A2_FULL
        return state / np.linalg.norm(state)

    def free(self, state: np.ndarray) -> np.ndarray:
        state = state @ self.coin2.T
        rolled = np.empty_like(state)
        for column in range(36):
            rolled[..., column] = np.roll(
                state[..., column],
                shift=tuple(DELTAS[column]),
                axis=(0, 1, 2),
            )
        return rolled

    def step(self, state: np.ndarray, contact: float) -> np.ndarray:
        state = self.free(state)
        if contact:
            onsite = state[0, 0, 0, :].copy()
            projected = C610.ONSITE_PROJ @ onsite
            state[0, 0, 0, :] = onsite + (np.exp(1j * contact) - 1) * projected
        return state

    def evolve(self, state: np.ndarray, steps: int, contact: float) -> np.ndarray:
        for _ in range(steps):
            state = self.step(state, contact)
        return state

    def word(self, state: np.ndarray, steps: int, contact: float) -> np.ndarray:
        bra = self.source()
        u = np.empty(steps + 1, complex)
        current = state.copy()
        for q in range(steps + 1):
            u[q] = np.vdot(bra, current)
            if q < steps:
                current = self.step(current, contact)
        aggregate = np.empty(steps + 1, complex)
        aggregate[0] = (u[0] + np.conj(u[1])) / math.sqrt(2)
        aggregate[1:] = (u[1:] + u[:-1]) / math.sqrt(2)
        return aggregate

    def antisym_defect(self, state: np.ndarray) -> float:
        mirrored = np.roll(state[::-1, ::-1, ::-1], (1, 1, 1), axis=(0, 1, 2))
        mirrored = mirrored[..., C610.SWAP36]
        return float(np.linalg.norm(state + mirrored))

    def window_mask(self, radius: int) -> np.ndarray:
        axis = np.minimum(np.arange(self.length), self.length - np.arange(self.length))
        chebyshev = np.maximum.reduce(np.meshgrid(axis, axis, axis, indexing="ij"))
        return (chebyshev <= radius)[..., None]


def momentum_to_position(state_mom: np.ndarray, length: int) -> np.ndarray:
    grid = state_mom.reshape(length, length, length, 36)
    return np.fft.ifftn(grid, axes=(0, 1, 2), norm="ortho")


# ----------------------------------------------------------------------------
# Certification: the unchanged Cycle-610 certificates on the prepared state.
# ----------------------------------------------------------------------------

def certify(engine: PositionEngine, state: np.ndarray, theta0: float) -> dict[str, object]:
    aggregate = engine.word(state, Q_CERT, CONTACT)
    row_t1 = C610.clock_row(aggregate, Q_SKIP, "T1")
    row_t2 = C610.clock_row(aggregate, Q_SKIP, "T2")
    predicted = C610.wrap_angle(theta0) / (2 * math.pi)
    bound = 2 / (Q_CERT - Q_SKIP)
    convention_ok = (
        abs(row_t1["rate"] - row_t2["rate"]) < 2 * bound
        and abs(row_t1["count"] - row_t2["count"])
        <= max(4, 0.01 * max(row_t1["count"], 1))
    )
    rate_ok = abs(row_t1["rate"] - predicted) < bound + 1e-9
    fine_ok = (
        row_t1["fine_rate"] is not None
        and abs(row_t1["fine_rate"] - predicted) < 1e-6
    )
    return {
        "rate_T1": row_t1["rate"], "rate_T2": row_t2["rate"],
        "count_T1": row_t1["count"], "count_T2": row_t2["count"],
        "locked": bool(row_t1["locked"]),
        "convention_independent": bool(convention_ok),
        "rate_matches": bool(rate_ok),
        "fine_matches": bool(fine_ok),
        "fine_rate": row_t1["fine_rate"],
        "certified": bool(row_t1["locked"] and convention_ok and rate_ok),
        "predicted": predicted,
    }


# ----------------------------------------------------------------------------
# Routes.
# ----------------------------------------------------------------------------

def route_pa(engine: PositionEngine, m: int, rounds: int, minus_port: bool = True):
    state = engine.source()
    probabilities = []
    for _ in range(rounds):
        full = engine.evolve(state.copy(), m, CONTACT)
        free = engine.evolve(state.copy(), m, 0.0)
        port = (full - free) / 2 if minus_port else (full + free) / 2
        p = float(np.linalg.norm(port) ** 2)
        probabilities.append(p)
        if p < 1e-12:
            return None, probabilities
        state = port / math.sqrt(p)
    return state, probabilities


def route_pb(engine: PositionEngine, m: int, rounds: int, condition: bool = True):
    mask = engine.window_mask(WINDOW_RADIUS)
    state = engine.source()
    probabilities = []
    for _ in range(rounds):
        if condition:
            kept = state * mask
            p = float(np.linalg.norm(kept) ** 2)
            probabilities.append(p)
            if p < 1e-12:
                return None, probabilities
            state = kept / math.sqrt(p)
        state = engine.evolve(state, m, CONTACT)
    return state, probabilities


def route_pc(engine: PositionEngine, total_steps: int):
    state = engine.source()
    for t in range(total_steps):
        g_t = G_START + (CONTACT - G_START) * (t + 1) / total_steps
        state = engine.step(state, g_t)
    return state


# ----------------------------------------------------------------------------
# Main tournament.
# ----------------------------------------------------------------------------

def main() -> int:
    start = time.time()
    receipt: dict[str, object] = {
        "cycle": 611,
        "authority": "none",
        "audit": "unset",
        "frozen_contract_sha256": FROZEN_CONTRACT_SHA256,
        "consumed_cycle610_sha256": C610_OBSERVED_SHA,
        "parameters": {
            "beta": BETA, "contact": CONTACT, "L_train": L_TRAIN,
            "L_held": L_HELD, "Q_cert": Q_CERT, "Q_skip": Q_SKIP,
            "g_start": G_START, "ramp_steps": list(RAMP_STEPS),
            "filter_m": list(FILTER_M), "filter_k": FILTER_K,
            "cert_k_grid": list(CERT_K_GRID), "window_radius": WINDOW_RADIUS,
        },
    }
    check(
        "the Cycle-610 runner is consumed byte-pinned and unchanged",
        C610_OBSERVED_SHA == C610_SHA256,
        C610_OBSERVED_SHA[:16],
    )

    engine = PositionEngine(L_TRAIN, BETA)
    root = C610.bs_root(L_TRAIN, C610.K_TRAIN_0, BETA)
    theta0 = float(root["theta"])
    psi_b_mom, eig_res = C610.bound_state(L_TRAIN, C610.K_TRAIN_0, BETA, root)
    psi_b_pos = momentum_to_position(psi_b_mom, L_TRAIN)

    def bound_weight(state: np.ndarray) -> float:
        return float(abs(np.vdot(psi_b_pos, state)) ** 2)

    # Engine/representation cross-check against the Cycle-610 momentum engine.
    mom = C610.evolve_word(
        C610.free_stack(L_TRAIN, C610.K_TRAIN_0, BETA), C610.a2_source(L_TRAIN), 16
    )
    pos_aggregate = engine.word(engine.source(), 16, CONTACT)
    rep_defect = float(np.max(np.abs(pos_aggregate - mom["aggregate"])))
    raw_weight = bound_weight(engine.source())
    check(
        "the position-representation engine reproduces the Cycle-610 word and "
        "the raw source bound weight",
        rep_defect < 1e-12 and abs(raw_weight - 0.2627) < 5e-4 and eig_res < 1e-6,
        {"rep_defect": rep_defect, "raw_bound_weight": raw_weight,
         "eig_residual": eig_res},
    )

    # No-op control: raw source straight to certification (610 falsification).
    noop = certify(engine, engine.source(), theta0)
    check(
        "no-op control reproduces the Cycle-610 falsification: locked but "
        "convention-dependent and uncertified",
        noop["locked"] and not noop["convention_independent"]
        and not noop["certified"],
        {k: noop[k] for k in ("rate_T1", "rate_T2", "locked",
                              "convention_independent", "certified")},
    )
    receipt["noop_control"] = noop

    # Lawful-domain detection: a non-antisymmetric input is outside the domain.
    bad = engine.source()
    bad[1, 0, 0, 0] += 0.1
    defect = engine.antisym_defect(bad)
    check(
        "lawful-domain: a non-antisymmetric input is detected outside the "
        "declared domain",
        defect > 1e-9,
        {"antisym_defect": defect},
    )

    # Window symmetry: the radius-1 window commutes with all 24 frames.
    mask = engine.window_mask(WINDOW_RADIUS)[..., 0]
    max_mask_defect = 0
    import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
    axis = np.arange(L_TRAIN)
    coords = np.stack(np.meshgrid(axis, axis, axis, indexing="ij"), axis=-1)
    signed = np.where(coords > L_TRAIN // 2, coords - L_TRAIN, coords)
    for frame in c210.proper_cubic_frames():
        rotated = np.einsum("ij,abcj->abci", frame, signed).astype(int) % L_TRAIN
        permuted = mask[rotated[..., 0], rotated[..., 1], rotated[..., 2]]
        max_mask_defect = max(max_mask_defect, int(np.sum(permuted != mask)))
    check(
        "the radius-1 conditioning window is proper-cubic invariant "
        "(all 24 frames)",
        max_mask_defect == 0,
        {"max_mask_defect": max_mask_defect},
    )

    # ---- Route P-B: window-conditioning cascade.
    pb_results = []
    pb_first_certified = None
    for m in FILTER_M:
        for k in CERT_K_GRID:
            state, probs = route_pb(engine, m, k)
            if state is None:
                pb_results.append({"m": m, "k": k, "collapsed": True})
                continue
            weight = bound_weight(state)
            cert = certify(engine, state, theta0)
            row = {
                "m": m, "k": k, "bound_weight": weight,
                "cumulative_success": float(np.prod(probs)),
                "round_success_last": probs[-1],
                **{key: cert[key] for key in
                   ("certified", "locked", "convention_independent",
                    "rate_matches", "rate_T1", "fine_rate")},
            }
            pb_results.append(row)
            if cert["certified"] and pb_first_certified is None:
                pb_first_certified = row
    receipt["route_pb"] = pb_results
    check(
        "P-B prior: the window-conditioning cascade certifies within k <= 12 "
        "at m = 16 (raw source in, certified clock out)",
        any(r.get("certified") for r in pb_results if r.get("m") == 16),
        {"first_certified": pb_first_certified},
    )

    # Conditioning deletion: without conditioning nothing changes.
    unconditioned, _ = route_pb(engine, 16, 12, condition=False)
    check(
        "conditioning deletion: pure evolution leaves the bound weight at the "
        "raw value and uncertified",
        abs(bound_weight(unconditioned) - raw_weight) < 1e-9
        and not certify(engine, unconditioned, theta0)["certified"],
        {"weight": bound_weight(unconditioned)},
    )

    # ---- Route P-A: echo-interference minus-port filter.
    pa_results = []
    for m in FILTER_M:
        weights = []
        state = None
        probs_all = []
        for k in CERT_K_GRID:
            state, probs = route_pa(engine, m, k)
            if state is None:
                pa_results.append({"m": m, "k": k, "collapsed": True})
                break
            weights.append(bound_weight(state))
            cert = certify(engine, state, theta0)
            pa_results.append({
                "m": m, "k": k, "bound_weight": weights[-1],
                "cumulative_success": float(np.prod(probs)),
                **{key: cert[key] for key in
                   ("certified", "locked", "convention_independent",
                    "rate_matches", "rate_T1")},
            })
            probs_all = probs
        receipt.setdefault("route_pa_success_tail", {})[str(m)] = probs_all[-3:]
    receipt["route_pa"] = pa_results
    pa_weights_by_m = {
        m: [r["bound_weight"] for r in pa_results
            if r.get("m") == m and "bound_weight" in r]
        for m in FILTER_M
    }
    check(
        "P-A prior: the minus-port filter raises the bound-weight diagnostic "
        "monotonically over the certification grid",
        all(
            len(w) < 2 or all(b >= a - 1e-9 for a, b in zip(w, w[1:]))
            for w in pa_weights_by_m.values()
        ) and any(w and w[-1] > raw_weight + 0.05 for w in pa_weights_by_m.values()),
        {str(m): [round(x, 4) for x in w] for m, w in pa_weights_by_m.items()},
    )

    # Port-swap control: the plus port anti-filters.
    plus_state, _ = route_pa(engine, 16, 4, minus_port=False)
    plus_weight = bound_weight(plus_state) if plus_state is not None else 0.0
    check(
        "port-swap control: the plus port does not purify (the minus port is "
        "load-bearing)",
        plus_weight < raw_weight + 0.05,
        {"plus_port_weight": plus_weight, "raw": raw_weight},
    )

    # ---- Route P-C: adiabatic contact ramp.
    pc_results = []
    for total in RAMP_STEPS:
        state = route_pc(engine, total)
        weight = bound_weight(state)
        cert = certify(engine, state, theta0)
        pc_results.append({
            "T": total, "bound_weight": weight,
            **{key: cert[key] for key in
               ("certified", "locked", "convention_independent", "rate_matches",
                "rate_T1")},
        })
    receipt["route_pc"] = pc_results
    pc_weights = [r["bound_weight"] for r in pc_results]
    check(
        "P-C frozen prior: bound weight improves monotonically with ramp "
        "length (certification outcome separately reported)",
        all(b >= a - 1e-9 for a, b in zip(pc_weights, pc_weights[1:])),
        {"weights": [round(w, 4) for w in pc_weights],
         "certified": [r["certified"] for r in pc_results]},
    )

    # ---- Winner: held-size transfer and the 610 field-row identity.
    winner = pb_first_certified
    if winner is not None:
        engine_h = PositionEngine(L_HELD, BETA)
        root_h = C610.bs_root(L_HELD, C610.K_TRAIN_0, BETA)
        state_h, _ = route_pb(engine_h, winner["m"], winner["k"])
        cert_h = certify(engine_h, state_h, float(root_h["theta"]))
        receipt["held_transfer"] = {
            "m": winner["m"], "k": winner["k"], **{
                key: cert_h[key] for key in
                ("certified", "locked", "convention_independent",
                 "rate_matches", "rate_T1", "predicted")},
        }
        check(
            "held transfer: the first-certified P-B configuration certifies at "
            "L13 with no re-tuning",
            cert_h["certified"],
            receipt["held_transfer"],
        )

        state_w, _ = route_pb(engine, winner["m"], winner["k"])
        word_w = engine.word(state_w, Q_CERT, CONTACT)
        alpha = 2 * math.pi * (+1) * 2 * 1 / 16
        modulated = word_w * np.exp(1j * alpha * np.arange(len(word_w)))
        row_base = C610.clock_row(word_w, Q_SKIP, "T1")
        row_field = C610.clock_row(modulated, Q_SKIP, "T1")
        ratio = row_field["rate"] / row_base["rate"]
        ratio_pred = C610.wrap_angle(theta0 + alpha) / C610.wrap_angle(theta0)
        check(
            "the Cycle-610 field ratio law survives on a prepared-by-dynamics "
            "clock (Q=1, s=+1 row)",
            abs(ratio - ratio_pred) < 3 * (2 / (Q_CERT - Q_SKIP)) / abs(
                C610.wrap_angle(theta0) / (2 * math.pi)
            ),
            {"ratio": ratio, "ratio_pred": ratio_pred},
        )
    else:
        check("held transfer: no certified P-B configuration to transfer", False,
              "P-B never certified")

    receipt["interpretation_firewall"] = [
        "a preparation schedule is not time; update count is not time",
        "the conditioning pointer/selector is not a Record",
        "success probability is a norm account, not Born probability",
        "certification uses spectral data; preparation does not",
        "conditioned routes are resource-accounted postselection, not "
        "deterministic autonomy; the tested deterministic P-C candidate is "
        "falsified",
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
