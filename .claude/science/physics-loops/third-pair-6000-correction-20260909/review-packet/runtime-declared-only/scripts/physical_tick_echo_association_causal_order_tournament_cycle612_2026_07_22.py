#!/usr/bin/env python3
"""Cycle 612: tick/echo association, pi-ceiling discriminator, matched-ray
certification, and causal-order bridge tournament.

Evaluates a frozen A-count comparison convention on the Cycle-610 rows; proves
the exhaustive pi-ceiling corollary (the 5:4 magnitude is unreachable by any
declared uniform-field rate shift); tests the detector-ray re-contamination
prediction by matched-ray certification of the Cycle-611 P-A prepared state;
and executes the finite causal-order acyclicity/refusal semantics for
co-registered two-device event chains.

Firewalls: a count word is not time; the A-count comparison is not an
identification of events across apparatuses; the pi ceiling is a property of
the candidate tick law, not a no-go on other response mechanisms; an admitted
cell is a conditional candidate Record.

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

FROZEN_CONTRACT_SHA256 = (
    "8c8c0082d56c79fec970af54213961db2feb4415c674796d0cefea88a75cbc2c"
)
C610_SHA256 = "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac"
C611_SHA256 = "15db2200b08bc4a5d7669975806fe51e9b8a55049f0660969d427332602bf9e8"
C610_RECEIPT_SHA256 = (
    "be7e6f6c29e5b914a427a5dccff3bb143eafbc9e0a5150b5c532001b3eb1b0d2"
)

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_"
    "CYCLE612_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_tick_echo_association_causal_order_tournament_"
    "cycle612_receipt_2026_07_22.json"
)
C610_RECEIPT = ROOT / (
    "outputs/physical_intrinsic_tick_event_relational_duration_tournament_"
    "cycle610_receipt_2026_07_22.json"
)

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


def load_module(name: str):
    path = ROOT / "scripts" / (name + ".py")
    digest = sha256(path.read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module, digest


C610, C610_SHA = load_module(
    "physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22"
)
C611, C611_SHA = load_module(
    "physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22"
)


def a_count(ratio: float) -> int | None:
    magnitude = 4 * abs(ratio) + 0.5
    if abs(magnitude - round(magnitude)) < 1e-9:
        return None
    return int(math.copysign(math.floor(magnitude), ratio))


# ----------------------------------------------------------------------------
# Causal-order semantics: two devices, shared co-registrations.
# ----------------------------------------------------------------------------

class JointOrder:
    """Per-device chains plus shared co-registration events.

    A shared event is admitted only if its per-device position is after every
    previously shared event's position in BOTH devices (a locally checkable
    cross-order consistency rule).  The joint relation is the union of the
    per-device predecessor edges and the shared-event identifications.
    """

    def __init__(self):
        self.chains = {"A": [], "B": []}
        self.shared: list[tuple[int, int]] = []

    def admit_local(self, device: str, identity: int) -> None:
        self.chains[device].append(identity)

    def admit_shared(self, identity: int) -> str:
        pos_a = len(self.chains["A"])
        pos_b = len(self.chains["B"])
        for prev_a, prev_b in self.shared:
            if not (prev_a < pos_a and prev_b < pos_b):
                return "refused_inverted"
        self.chains["A"].append(identity)
        self.chains["B"].append(identity)
        self.shared.append((pos_a, pos_b))
        return "admitted"

    def force_shared(self, identity: int, pos_a: int, pos_b: int) -> None:
        """Adversary: inject a shared identification without the consistency
        rule (models a malformed registration)."""
        self.shared.append((pos_a, pos_b))

    def acyclic(self) -> bool:
        edges = set()
        counter = 0
        alias: dict[tuple[str, int], int] = {}
        for dev in ("A", "B"):
            for i in range(len(self.chains[dev])):
                alias[(dev, i)] = counter
                counter += 1
        for pos_a, pos_b in self.shared:
            if pos_a < len(self.chains["A"]) and pos_b < len(self.chains["B"]):
                alias[("B", pos_b)] = alias[("A", pos_a)]
        for dev in ("A", "B"):
            for i in range(1, len(self.chains[dev])):
                edges.add((alias[(dev, i - 1)], alias[(dev, i)]))
        nodes = set(alias.values())
        indegree = {n: 0 for n in nodes}
        for a, b in edges:
            indegree[b] += 1
        queue = [n for n in nodes if indegree[n] == 0]
        seen = 0
        while queue:
            n = queue.pop()
            seen += 1
            for a, b in list(edges):
                if a == n:
                    edges.discard((a, b))
                    indegree[b] -= 1
                    if indegree[b] == 0:
                        queue.append(b)
        return seen == len(nodes)


# ----------------------------------------------------------------------------
# Main.
# ----------------------------------------------------------------------------

def main() -> int:
    start = time.time()
    receipt: dict[str, object] = {
        "cycle": 612,
        "authority": "none",
        "audit": "unset",
        "frozen_contract_sha256": FROZEN_CONTRACT_SHA256,
        "consumed": {"cycle610_runner": C610_SHA, "cycle611_runner": C611_SHA},
        "comparison_scope": (
            "A-count is a declared finite comparison convention; no "
            "campaign-only response mechanism is imported as authority"
        ),
    }
    c610_receipt = json.loads(C610_RECEIPT.read_text())
    c610_receipt_sha = sha256(C610_RECEIPT.read_bytes()).hexdigest()
    check(
        "the Cycle-610 and Cycle-611 runners and the consumed Cycle-610 "
        "receipt are byte-pinned and unchanged",
        C610_SHA == C610_SHA256
        and C611_SHA == C611_SHA256
        and c610_receipt_sha == C610_RECEIPT_SHA256,
        {
            "cycle610_runner": C610_SHA[:16],
            "cycle611_runner": C611_SHA[:16],
            "cycle610_receipt": c610_receipt_sha[:16],
        },
    )
    receipt["consumed"]["cycle610_receipt_sha256"] = c610_receipt_sha

    theta0 = float(c610_receipt["spectral_roots"]["train_K0"]["theta"])

    # ---- A-count comparison table (declared convention, no mechanism import).
    rows = []
    expected = {(1, 1): 3, (2, 1): 2, (3, 1): 1, (8, 1): 4, (8, -1): 4,
                (1, -1): -3, (2, -1): -2, (3, -1): -1}
    table_ok = True
    hit_34 = []
    for row in c610_receipt["field_rows"]:
        ratio = float(row["ratio_pred"])
        count = a_count(ratio)
        key = (int(row["weyl_Q"]), int(row["sign"]))
        ok = count == expected[key]
        table_ok = table_ok and ok
        word = f"{abs(count)}:4" if count is not None and count > 0 else (
            "reversed" if count is not None and count < 0 else "undefined")
        if count == 3:
            hit_34.append(key)
        rows.append({"Q": key[0], "s": key[1], "ratio": ratio,
                     "count": count, "word": word, "matches_frozen": ok})
    motion = float(c610_receipt["motion_rows"]["train"]["ratio_pred"])
    held = float(c610_receipt["motion_rows"]["held"]["ratio_pred"])
    species_ratio = C610.wrap_angle(
        float(c610_receipt["spectral_roots"]["beta_held"]["theta"])
    ) / C610.wrap_angle(theta0)
    for label, ratio in (("motion_train", motion), ("motion_held", held),
                         ("species", species_ratio)):
        count = a_count(ratio)
        table_ok = table_ok and count == 4
        rows.append({"row": label, "ratio": ratio, "count": count,
                     "word": "4:4", "matches_frozen": count == 4})
    receipt["a_count_table"] = rows
    check(
        "A-count reproduces the frozen expected table: exactly one 3:4 hit at "
        "(Q=1, s=+1), 4:4 at nulls/motion/species, reversed-class rows for "
        "s=-1, and no 5:4 anywhere",
        table_ok and hit_34 == [(1, 1)],
        {"hit_3_4": hit_34},
    )

    # ---- Pi-ceiling corollary (exhaustive over W=16 and W=64 alpha lattices).
    ceiling = math.pi / abs(C610.wrap_angle(theta0))
    max_ratio = 0.0
    for weyl in (16, 64):
        for q in range(weyl):
            for sign in (+1, -1):
                alpha = 2 * math.pi * sign * 2 * q / weyl
                ratio = abs(C610.wrap_angle(theta0 + alpha) / C610.wrap_angle(theta0))
                max_ratio = max(max_ratio, ratio)
    check(
        "pi-ceiling corollary: |R| <= pi/|theta0| = 1.0556 for every uniform-"
        "field modulation on the full W=16 and W=64 lattices; the 5:4 advance "
        "word (|R| = 1.25) is unreachable by any uniform-field rate shift, "
        "while the declared A-count convention has a 3:4-class row",
        max_ratio <= ceiling + 1e-12 and max_ratio < 1.125,
        {"ceiling": ceiling, "max_ratio_found": max_ratio},
    )
    receipt["pi_ceiling"] = {"ceiling": ceiling, "max_ratio": max_ratio}

    # ---- Matched-ray certification of the Cycle-611 P-A (m=16, k=4) state.
    engine = C611.PositionEngine(C611.L_TRAIN, C611.BETA)
    root = C610.bs_root(C611.L_TRAIN, C610.K_TRAIN_0, C611.BETA)
    state, probs = C611.route_pa(engine, 16, 4)
    cumulative = float(np.prod(probs))
    v = np.empty(C611.Q_CERT + 1, complex)
    current = state.copy()
    for q in range(C611.Q_CERT + 1):
        v[q] = np.vdot(state, current)
        if q < C611.Q_CERT:
            current = engine.step(current, C611.CONTACT)
    matched = np.empty(C611.Q_CERT + 1, complex)
    matched[0] = (v[0] + np.conj(v[1])) / math.sqrt(2)
    matched[1:] = (v[1:] + v[:-1]) / math.sqrt(2)
    row_t1 = C610.clock_row(matched, C611.Q_SKIP, "T1")
    row_t2 = C610.clock_row(matched, C611.Q_SKIP, "T2")
    predicted = C610.wrap_angle(float(root["theta"])) / (2 * math.pi)
    bound = 2 / (C611.Q_CERT - C611.Q_SKIP)
    convention_ok = (
        abs(row_t1["rate"] - row_t2["rate"]) < 2 * bound
        and abs(row_t1["count"] - row_t2["count"])
        <= max(4, 0.01 * max(row_t1["count"], 1))
    )
    matched_certified = bool(
        row_t1["locked"] and convention_ok
        and abs(row_t1["rate"] - predicted) < bound + 1e-9
    )
    raw_control = C611.certify(engine, state, float(root["theta"]))
    psi_b_mom, _ = C610.bound_state(
        C611.L_TRAIN, C610.K_TRAIN_0, C611.BETA, root
    )
    psi_b_pos = C611.momentum_to_position(psi_b_mom, C611.L_TRAIN)
    bound_weight_input = float(abs(np.vdot(psi_b_pos, state)) ** 2)
    check(
        "matched-ray certification: the Cycle-611 P-A (m=16, k=4) prepared "
        "state certifies through its own rays (frozen prediction), while the "
        "raw-ray control on the same state stays uncertified — certification "
        "is a property of the (ray, state) pair",
        matched_certified and not raw_control["certified"],
        {"matched": {"rate": row_t1["rate"], "predicted": predicted,
                     "locked": row_t1["locked"],
                     "convention_independent": convention_ok},
         "raw_control_certified": raw_control["certified"],
         "cumulative_success": cumulative},
    )
    receipt["matched_ray"] = {
        "rate": row_t1["rate"], "rate_T2": row_t2["rate"],
        "predicted": predicted, "certified": matched_certified,
        "fine_rate": row_t1["fine_rate"],
        "raw_control_certified": bool(raw_control["certified"]),
        "cumulative_success": cumulative,
        "bound_weight_input": bound_weight_input,
    }

    # ---- Causal-order bridge: acyclicity and inverted-registration refusal.
    joint = JointOrder()
    for i in range(3):
        joint.admit_local("A", 100 + i)
    for i in range(2):
        joint.admit_local("B", 200 + i)
    s1 = joint.admit_shared(900)
    joint.admit_local("A", 103)
    joint.admit_local("B", 202)
    s2 = joint.admit_shared(901)
    consistent_acyclic = joint.acyclic()
    check(
        "causal-order bridge: consistent sequential co-registrations are "
        "admitted and the joint predecessor relation is acyclic",
        s1 == "admitted" and s2 == "admitted" and consistent_acyclic,
        {"s1": s1, "s2": s2, "acyclic": consistent_acyclic},
    )
    adversary = JointOrder()
    for i in range(4):
        adversary.admit_local("A", 300 + i)
    for i in range(4):
        adversary.admit_local("B", 400 + i)
    first = adversary.admit_shared(910)
    adversary.force_shared(911, 1, 6)
    refusal = adversary.admit_shared(912)
    check(
        "inverted registration: the locally checkable cross-order rule "
        "refuses a shared event that would precede an earlier shared event in "
        "one device (no silent cycle admission)",
        first == "admitted" and refusal == "refused_inverted",
        {"first": first, "attempt_after_forced_inversion": refusal},
    )
    forced = JointOrder()
    for i in range(3):
        forced.admit_local("A", 500 + i)
        forced.admit_local("B", 600 + i)
    forced.force_shared(920, 0, 2)
    forced.force_shared(921, 2, 0)
    check(
        "adversary witness: forcing inverted identifications past the rule "
        "creates a cyclic joint relation, which the acyclicity decoder "
        "detects (undefined, never a lawful order)",
        not forced.acyclic(),
        {"acyclic": forced.acyclic()},
    )
    receipt["causal_order"] = {
        "consistent_admitted": [s1, s2],
        "inverted_refused": refusal,
        "forced_cycle_detected": not forced.acyclic(),
    }

    receipt["interpretation_firewall"] = [
        "a count word is not time; A-count consistency is not identification",
        "the pi ceiling is a property of the declared candidate tick law, not "
        "a no-go on other response mechanisms",
        "matched-ray certification uses spectral data on the certification "
        "side only; the preparation and rays consume no spectral data",
        "shared co-registrations are candidate events; the acyclicity result "
        "is a finite declared-code statement, not a lattice-wide light-cone "
        "theorem",
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
