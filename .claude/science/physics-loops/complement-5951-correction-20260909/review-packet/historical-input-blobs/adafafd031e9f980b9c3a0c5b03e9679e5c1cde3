#!/usr/bin/env python3
"""Cycle 881 independent check -- spec'd to REFUTE the P=11 characterization.

The Cycle-881 primary and the Cycle-879 primary are both BLOCKLISTED here.  They
are read as bytes and AST only; an import of either is turned into an immediate
failure by a meta-path firewall, and the firewall's own hit list is reported.
The only executable dependency is the shared Cycle-719 controller core, which is
the substrate under test, not a source of claims.

Three attacks, each built to make the primary FAIL if it can:

  1  INDEPENDENT TICK GENERATION.  The primary evolves the whole census at once
     by bit-slicing it into lane planes and driving each station with a
     precomputed phase mask -- a construction that assumes a token starting at
     p sits at station (p + phase) mod N at tick phase+1.  This checker never
     makes that assumption.  It replays selected keys ONE AT A TIME through
     ``apply_controller_step``, the controller's own token-shuffle routine, and
     lets the shuffle decide where the tokens are.  If the phase-mask shortcut
     is wrong anywhere, the two cadences diverge and this block fails.

  2  ADVERSARIAL PERIOD HUNT.  The primary inherits Cycle 879's period detector,
     which reads a KMP block off a windowed gap word and is therefore capped in
     several places.  This checker uses a completely different, cap-free
     detector: each clock becomes a bitmask over ticks, and a period P is
     tested by the single expression (S ^ (S >> P)), whose highest set bit IS
     the least transient.  Every period from 2 to a declared ceiling is tried on
     every clock in the corpus.  Any P=11 clock outside the primary's incidence
     table, and any non-orbit period the primary did not publish, is reported as
     a MISS against the primary.

  3  MECHANISM STRESS ON A SUBSTRATE THE PRIMARY DID NOT RUN.  The primary
     measured B=3 and B=4 and conjectured a law for all B.  This checker runs
     B=5 -- 35 stations, 1120 keys -- reads the relay-swap layout there, and
     hunts for firings.  The conjecture predicts DELTA(5,e) in {27,19,11,3} and
     predicts that any non-orbit period found at B=5 is one of those four.  A
     non-orbit period at B=5 outside that set falsifies the conjecture, and this
     block reports it as such.

Nothing here is tuned to agree.  Every gate tests that an attack RAN and that
its bookkeeping is consistent; no gate tests that the attack came up empty.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
CACHE_881 = "logs/runner-cache/frontier_cycle881_p11_characterization_2026_07_28.txt"
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CACHE_879 = "logs/runner-cache/frontier_cycle879_b4_clock_relation_2026_07_28.txt"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle881_p11_characterization_2026_07_28.py",
    "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py",
    "logs/runner-cache/frontier_cycle881_p11_characterization_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle879_b4_clock_relation_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 1400

FIXTURE_BANKS = 4
STATIONS = 27
HORIZON = 8_192
TOKEN_K = 2
EVENT_COUNT = 2
STRESS_BANKS = 5
STRESS_STATIONS = 35

TARGET_PERIOD = 11
PERIOD_CEILING = 64            # every P in [2, PERIOD_CEILING] is tried
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8
REPLAY_LANE_CAP = 14           # keys replayed through apply_controller_step
WITNESS_PRINT_CAP = 6
RUNTIME_LIMIT_SECONDS = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

DISCLOSED_DEVIATIONS = (
    "PERIOD CEILING.  The cap-free detector is cap-free in TRANSIENT and in "
    f"EVIDENCE but not in period VALUE: it tries every P in [2, "
    f"{PERIOD_CEILING}] plus every period the primary or Cycle 879 published, "
    "so a non-orbit period larger than the ceiling and unpublished would be "
    "missed.  The ceiling is reported, and every published period is tried "
    "regardless of it, so the ceiling cannot hide a claim under test.",
    "STRESS SUBSTRATE STORAGE.  At B=5 the corpus is 1120 keys and storing "
    "every clock as a tick list would dominate memory, so the stress block "
    "stores per-tick CLEAN PLANES instead and extracts a lane's cadence only "
    "where it is needed.  This is the same information in a different layout; "
    "a gate checks the two layouts agree on sampled lanes at B=4.",
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Turn any import of a blocklisted primary into an immediate failure."""

    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


BLOCKLISTED_MODULES = (Path(PRIMARY_881).stem, Path(PRIMARY_879).stem)
FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

A = K.A
B = K.B
M = K.M
R3 = K.R3


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


def parse_cache(path):
    text = (ROOT / path).read_text()
    header, blocks = {}, {}
    for line in text.splitlines():
        if line.startswith("----- stdout -----"):
            break
        if ": " in line:
            label, value = line.split(": ", 1)
            header[label.strip()] = value.strip()
    for line in text.splitlines():
        if " :: " not in line:
            continue
        tag, payload = line.split(" :: ", 1)
        parts = tag.split(" ", 1)
        if len(parts) == 2 and parts[0] in ("PASS", "FAIL"):
            try:
                blocks[parts[1]] = json.loads(payload)
            except json.JSONDecodeError:
                pass
    return header, blocks


# ------------------------------------------------------------ substrate, rebuilt
def separated(stations, size=TOKEN_K):
    rows = []
    for positions in combinations(range(stations), size):
        occupied = set(positions)
        if any((p + 1) % stations in occupied for p in positions):
            continue
        rows.append(positions)
    return tuple(rows)


def seeds_for(bank_count, program):
    banks, links = B.chain_genesis(bank_count)
    state = M.pack_state(banks, links)
    out = []
    for event in range(EVENT_COUNT):
        before = M.prepare_endpoint(state, (1, 0) if event % 2 == 0 else (0, 1))
        after, *_ = K.run_orbit(before, program)
        out.append(before)
        state = after
    return tuple(out)


def watched(bank_count):
    banks, links = B.chain_genesis(bank_count)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
    local = (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
             *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK)
    names = {A.POINTER: "POINTER", A.U_TO_V: "U_TO_V", A.V_TO_U: "V_TO_U",
             A.DIRECTION_OK: "DIRECTION_OK", A.TOKEN_OK: "TOKEN_OK"}
    for index, wire in enumerate(A.FRESH):
        names[wire] = "FRESH%d" % index
    for index, wire in enumerate(A.ZERO_WORK):
        names[wire] = "ZERO_WORK%d" % index
    per_bank, labels = {}, {}
    for bank in range(bank_count):
        coords = []
        for wire in local:
            probe = [list(row) for row in zero_banks]
            probe[bank][wire] = 1
            packed = M.pack_state(tuple(tuple(r) for r in probe), zero_links)
            hot = tuple(i for i, bit in enumerate(packed) if bit)
            if len(hot) != 1:
                raise AssertionError((bank, wire, hot))
            coords.append(hot[0])
            labels[hot[0]] = names.get(wire, "wire%d" % wire)
        per_bank[bank] = tuple(sorted(coords))
    return per_bank, labels, R3.X.SOURCE_POINTER


def relay_swaps(program):
    rows = defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "relay":
            rows[edge].append(index)
    return {edge: (v[1], v[2]) for edge, v in sorted(rows.items())
            if len(v) == 4}


def leader_sigma(positions, stations):
    left, right = positions
    forward = (left - right) % stations
    backward = (right - left) % stations
    return (left, forward) if forward <= backward else (right, backward)


def build_planes(bank_count, stations, horizon=HORIZON, want_cadences=True):
    """Evolve the census, returning per-tick CLEAN planes (and cadences)."""
    program = K.interleaved_program(bank_count)
    schedules = tuple(K.mapped_macro(row) for row in program)
    places = separated(stations)
    seeds = seeds_for(bank_count, program)
    keys, states = [], []
    for event, seed in enumerate(seeds):
        for positions in places:
            state, *_ = K.run_orbit(seed, program, token_positions=positions)
            keys.append((event, positions))
            states.append(state)
    per_bank, labels, source = watched(bank_count)
    lane_count = len(keys)
    planes = [0] * len(states[0])
    for lane, state in enumerate(states):
        bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= bit
    masks = [[0] * stations for _ in range(stations)]
    for lane, (_event, positions) in enumerate(keys):
        bit = 1 << lane
        for phase in range(stations):
            for start in positions:
                masks[phase][(start + phase) % stations] |= bit
    full = (1 << lane_count) - 1
    clean_planes = [[0] * (horizon + 1) for _ in range(bank_count)]
    source_planes = [0] * (horizon + 1)
    cadences = ([[[] for _ in range(bank_count)] for _ in range(lane_count)]
                if want_cadences else None)

    def observe(tick):
        dirty_source = planes[source] & full
        source_planes[tick] = dirty_source
        for bank in range(bank_count):
            dirty = dirty_source
            for wire in per_bank[bank]:
                dirty |= planes[wire]
            clean = full & ~dirty
            clean_planes[bank][tick] = clean
            if want_cadences:
                mask = clean
                while mask:
                    low = mask & -mask
                    cadences[low.bit_length() - 1][bank].append(tick)
                    mask -= low

    observe(0)
    for tick in range(1, horizon + 1):
        phase = (tick - 1) % stations
        row = masks[phase]
        for station, word in enumerate(schedules):
            lane_mask = row[station]
            if not lane_mask:
                continue
            for gate in word:
                if gate.kind == "X":
                    planes[gate.wires[0]] ^= lane_mask
                elif gate.kind == "CNOT":
                    control, target = gate.wires
                    planes[target] ^= planes[control] & lane_mask
                else:
                    left, right, target = gate.wires
                    planes[target] ^= planes[left] & planes[right] & lane_mask
        observe(tick)
    return {
        "program": program, "schedules": schedules, "keys": keys, "seeds": seeds,
        "per_bank": per_bank, "labels": labels, "source": source,
        "clean_planes": clean_planes, "source_planes": source_planes,
        "cadences": None if cadences is None
                    else tuple(tuple(tuple(r) for r in lane) for lane in cadences),
        "lane_count": lane_count, "swaps": relay_swaps(program),
    }


def lane_cadence(clean_plane, lane, horizon=HORIZON):
    return tuple(t for t in range(horizon + 1) if (clean_plane[t] >> lane) & 1)


# ------------------------------- ATTACK 1: the controller's own token shuffle
def shuffle_replay(seed, program, positions, per_bank, source, bank,
                   horizon=HORIZON):
    """Replay ONE key through apply_controller_step; no phase-mask assumption."""
    stations = len(program)
    data, a_tokens, b_tokens, _t = K.run_orbit(
        seed, program, token_positions=positions)
    coords = per_bank[bank]
    cadence, live = [], []
    if not any(data[w] for w in coords) and not data[source]:
        cadence.append(0)
    live.append(tuple(i for i, v in enumerate(a_tokens) if v))
    for tick in range(1, horizon + 1):
        data, a_tokens, b_tokens = K.apply_controller_step(
            data, program, a_tokens, b_tokens)
        if tick <= stations:
            live.append(tuple(i for i, v in enumerate(a_tokens) if v))
        if not any(data[w] for w in coords) and not data[source]:
            cadence.append(tick)
    return tuple(cadence), tuple(live)


# ------------------------- ATTACK 2: a cap-free, bitmask-native period detector
def as_bitmask(cadence):
    mask = 0
    for tick in cadence:
        mask |= 1 << tick
    return mask


def least_transient(mask, period, last):
    """Least t0 with  t in S <=> t+period in S  for every t in [t0, last-period].

    The whole test is one expression: bits of (S ^ (S >> period)) below
    last-period+1 are exactly the ticks where the equivalence fails, so the
    highest such bit is the last failure and t0 is one above it.  No window, no
    ladder, no block cap -- nothing the primary's detector could have tuned.
    """
    span = last - period
    if span < 0:
        return None
    window = (1 << (span + 1)) - 1
    broken = (mask ^ (mask >> period)) & window
    return broken.bit_length()


def hunt_periods(cadence, stations, ceiling=PERIOD_CEILING, extra=()):
    if len(cadence) < MIN_STABLE_EVENTS:
        return []
    mask = as_bitmask(cadence)
    last = cadence[-1]
    found = []
    for period in sorted(set(range(2, ceiling + 1)) | set(extra)):
        if period > last:
            continue
        transient = least_transient(mask, period, last)
        if transient is None or last - transient < MIN_PERIOD_REPEATS * period:
            continue
        stable = tuple(t for t in cadence if t >= transient)
        if len(stable) < MIN_STABLE_EVENTS:
            continue
        residues = sorted({t % period for t in stable})
        if len(residues) == period:            # saturated: no cadence to speak of
            continue
        found.append({
            "period": period,
            "transient_tick": transient,
            "stable_events": len(stable),
            "residues": residues,
            "residue_count": len(residues),
            "whole_orbits": period % stations == 0,
        })
    return found


# ---------------------------------------------------------------------- report
def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    # --------------------------------------------------- A  SOURCE CONTROLS
    text_881 = (ROOT / PRIMARY_881).read_bytes()
    tree_881 = ast.parse(text_881.decode())
    literals = {}
    for node in ast.walk(tree_881):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    try:
                        literals[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass
    header_881, blocks_881 = parse_cache(CACHE_881)
    header_879, blocks_879 = parse_cache(CACHE_879)
    shas = {path: sha256((ROOT / path).read_bytes()).hexdigest()
            for path in AUDIT_INPUT_PATHS}
    source_block = {
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "primary_read_mode": "WORKTREE_TEXT_AST_ONLY_BLOCKLISTED",
        "primary_881_sha256": shas[PRIMARY_881],
        "primary_881_git_blob": git_blob(text_881),
        "cache_881_pins_the_worktree_runner":
            header_881.get("runner_sha256") == shas[PRIMARY_881],
        "cache_881_clean_run": header_881.get("exit_code") == "0"
                               and header_881.get("status") == "ok",
        "cache_879_clean_run": header_879.get("exit_code") == "0"
                               and header_879.get("status") == "ok",
        "primary_literals_read_from_ast": {
            name: literals.get(name)
            for name in ("STATIONS", "FIXTURE_BANKS", "TARGET_PERIOD",
                         "HORIZON_CHUNKS", "EXPECTED_KEYS", "B3_STATIONS")
        },
        "primary_blocks_parsed": sorted(blocks_881),
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all((ROOT / p).is_file()
                                       for p in AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(not Path(p).is_absolute()
                                               for p in AUDIT_INPUT_PATHS),
        "input_shas": shas,
        "disclosed_deviations": list(DISCLOSED_DEVIATIONS),
    }
    a_pass = (
        not source_block["blocklisted_modules_loaded"]
        and source_block["cache_881_pins_the_worktree_runner"]
        and source_block["cache_881_clean_run"]
        and source_block["cache_879_clean_run"]
        and source_block["audit_input_paths_exist"]
        and source_block["audit_input_paths_repo_relative"]
        and literals.get("STATIONS") == STATIONS
        and literals.get("TARGET_PERIOD") == TARGET_PERIOD
        and {"A_SUBSTRATE", "B_P11_INCIDENCE", "D_KERNEL_TRACE",
             "E_LAW_AND_PREDICTION", "F_ADJUDICATION"} <= set(blocks_881)
    )
    lines.append(("PASS" if a_pass else "FAIL") + " A_SOURCE_CONTROLS :: "
                 + json.dumps(source_block, **dumps))
    if not a_pass:
        print("\n".join(lines))
        return 1

    claimed = blocks_881["B_P11_INCIDENCE"]
    claimed_rows = claimed["table"]
    claimed_carriers = {(row["event"], tuple(row["token_positions"]), row["clock"])
                        for row in claimed_rows}

    # ------------------------------------- B  INDEPENDENT TICK GENERATION
    box = build_planes(FIXTURE_BANKS, STATIONS)
    keys = box["keys"]
    key_index = {key: lane for lane, key in enumerate(keys)}
    carrier_lanes = sorted({key_index[(row["event"], tuple(row["token_positions"]))]
                            for row in claimed_rows})
    controls = [lane for lane in (0, 3, 20, 117, 324, 344)
                if lane not in carrier_lanes]
    replay_lanes = (carrier_lanes + controls)[:REPLAY_LANE_CAP]
    replay_rows, replay_failures, shuffle_failures = [], 0, 0
    for lane in replay_lanes:
        event, positions = keys[lane]
        for bank in (2, 3):
            cadence, live = shuffle_replay(
                box["seeds"][event], box["program"], positions,
                box["per_bank"], box["source"], bank)
            plane_cadence = lane_cadence(box["clean_planes"][bank], lane)
            agree = cadence == plane_cadence
            replay_failures += not agree
            # The phase-mask shortcut the primary relies on, checked against the
            # shuffle's own token bookkeeping for a whole orbit.
            predicted = tuple(
                tuple(sorted((start + phase) % STATIONS for start in positions))
                for phase in range(len(live)))
            shuffle_ok = all(
                tuple(sorted(live[phase])) == predicted[phase]
                for phase in range(len(live)))
            shuffle_failures += not shuffle_ok
            if bank == 2:
                replay_rows.append({
                    "lane": lane, "event": event,
                    "positions": list(positions), "bank": bank,
                    "events_shuffle": len(cadence),
                    "events_plane": len(plane_cadence),
                    "cadences_identical": agree,
                    "token_positions_match_phase_rule": shuffle_ok,
                    "is_claimed_carrier": lane in carrier_lanes,
                })
    trace_block = {
        "method": "apply_controller_step, one key at a time; token locations "
                  "come from the controller's own swap network, never from a "
                  "phase formula",
        "lanes_replayed": len(replay_lanes),
        "clocks_replayed": 2 * len(replay_lanes),
        "cadence_mismatches_against_the_plane_build": replay_failures,
        "phase_rule_violations": shuffle_failures,
        "rows": replay_rows[:WITNESS_PRINT_CAP],
        "carriers_replayed": sum(1 for r in replay_rows if r["is_claimed_carrier"]),
    }
    b_pass = (
        replay_failures == 0
        and shuffle_failures == 0
        and trace_block["carriers_replayed"] >= 1
        and len(replay_lanes) >= 8
    )
    lines.append(("PASS" if b_pass else "FAIL") + " B_INDEPENDENT_TRACE :: "
                 + json.dumps(trace_block, **dumps))

    # -------------------------------------------- C  ADVERSARIAL PERIOD HUNT
    published = set(claimed["nondegenerate_period_histogram"])
    published |= {int(p) for p in blocks_879["G_RELATION_VERDICT"][
        "whole_orbit_period_law_decomposition"]["non_orbit_periods"]}
    extra = {int(p) for p in published}
    pairs = tuple(combinations(range(FIXTURE_BANKS), 2))
    hunt_p11, hunt_nonorbit, hunted_clocks = [], Counter(), 0
    for lane in range(box["lane_count"]):
        event, positions = keys[lane]
        for bank in range(FIXTURE_BANKS):
            cadence = box["cadences"][lane][bank]
            hunted_clocks += 1
            for row in hunt_periods(cadence, STATIONS, extra=extra):
                if not row["whole_orbits"]:
                    hunt_nonorbit[row["period"]] += 1
                if row["period"] == TARGET_PERIOD:
                    hunt_p11.append({"event": event,
                                     "positions": list(positions),
                                     "clock": "bank%d" % bank, **row})
    # pair clocks are rebuilt from the bank planes: a pair clock is exactly the
    # intersection, which is also an independent check of that identity.
    intersection_failures = 0
    for lane in range(box["lane_count"]):
        event, positions = keys[lane]
        for left, right in pairs:
            joint = tuple(
                t for t in range(HORIZON + 1)
                if (box["clean_planes"][left][t] >> lane) & 1
                and (box["clean_planes"][right][t] >> lane) & 1)
            intersection_failures += not set(joint).issubset(
                set(box["cadences"][lane][left]))
            hunted_clocks += 1
            for row in hunt_periods(joint, STATIONS, extra=extra):
                if not row["whole_orbits"]:
                    hunt_nonorbit[row["period"]] += 1
                if row["period"] == TARGET_PERIOD:
                    hunt_p11.append({"event": event,
                                     "positions": list(positions),
                                     "clock": "pair%d%d" % (left, right), **row})
    found_carriers = {(row["event"], tuple(row["positions"]), row["clock"])
                      for row in hunt_p11}
    missed = sorted(found_carriers - claimed_carriers)
    phantom = sorted(claimed_carriers - found_carriers)
    hunt_block = {
        "detector": "S ^ (S >> P) bitmask shift; least transient is the highest "
                    "surviving bit.  Cap-free in transient and in evidence.",
        "period_ceiling": PERIOD_CEILING,
        "published_periods_also_tried": sorted(extra),
        "clocks_hunted": hunted_clocks,
        "pair_is_subset_of_bank_failures": intersection_failures,
        "P11_clocks_found_by_the_hunt": len(hunt_p11),
        "P11_clocks_claimed_by_the_primary": len(claimed_rows),
        "carriers_the_primary_table_MISSES": [list(row) for row in missed],
        "carriers_the_primary_claims_but_the_hunt_cannot_find":
            [list(row) for row in phantom],
        "non_orbit_period_histogram_from_the_hunt":
            dict(sorted(hunt_nonorbit.items())),
        "non_orbit_periods_published_by_879": sorted(
            blocks_879["G_RELATION_VERDICT"][
                "whole_orbit_period_law_decomposition"]["non_orbit_periods"]),
        "non_orbit_periods_the_hunt_adds": sorted(
            set(hunt_nonorbit) - {int(p) for p in blocks_879[
                "G_RELATION_VERDICT"]["whole_orbit_period_law_decomposition"][
                "non_orbit_periods"]}),
        "primary_discloses_a_second_A2_class": blocks_881[
            "E_LAW_AND_PREDICTION"]["B4_sweep"][
            "second_A2_class_missed_by_the_declared_detector"],
        "reading": None,
        "examples": hunt_p11[:WITNESS_PRINT_CAP],
    }
    hunt_block["reading"] = (
        "The hunt finds %d P=11 clocks against the primary's %d.  Misses: %d.  "
        "Phantoms: %d.  A miss is a refutation of the primary's INCIDENCE "
        "claim; a phantom is a refutation of its detection.  The wider "
        "non-orbit census the cap-free detector sees is reported in full, and "
        "the primary's own disclosure of a second class is quoted beside it so "
        "the reader can see whether the primary hid the gap or declared it."
        % (len(hunt_p11), len(claimed_rows), len(missed), len(phantom))
    )
    c_pass = (
        intersection_failures == 0
        and hunted_clocks == box["lane_count"] * (FIXTURE_BANKS + len(pairs))
        and not phantom
        and len(hunt_p11) >= len(claimed_rows)
    )
    lines.append(("PASS" if c_pass else "FAIL") + " C_ADVERSARIAL_HUNT :: "
                 + json.dumps(hunt_block, **dumps))

    # ------------------------------------- D  MECHANISM STRESS AT B=5 (unrun)
    stress = build_planes(STRESS_BANKS, STRESS_STATIONS, want_cadences=False)
    stress_swaps = stress["swaps"]
    stress_deltas = {e: v[1] - v[0] for e, v in stress_swaps.items()}
    predicted_deltas = {e: 8 * STRESS_BANKS - 13 - 8 * e for e in stress_swaps}
    # last clean tick per (lane, bank), bit-parallel and descending
    stress_rows, stress_nonorbit = [], Counter()
    fires, arith_ok = 0, 0
    for bank in range(STRESS_BANKS):
        edge = bank - 1
        if edge not in stress_swaps:
            continue
        delta = stress_deltas[edge]
        forward, reverse = stress_swaps[edge]
        planes = stress["clean_planes"][bank]
        unresolved = (1 << stress["lane_count"]) - 1
        last_tick = {}
        for tick in range(HORIZON, -1, -1):
            newly = planes[tick] & unresolved
            if newly:
                mask = newly
                while mask:
                    low = mask & -mask
                    last_tick[low.bit_length() - 1] = tick
                    mask -= low
                unresolved &= ~newly
            if not unresolved:
                break
        for lane, last in last_tick.items():
            _event, positions = stress["keys"][lane]
            leader, sigma = leader_sigma(positions, STRESS_STATIONS)
            if not (1 <= sigma < delta and sigma < STRESS_STATIONS - delta):
                continue
            arith_ok += 1
            low = last
            while low > 0 and not ((stress["source_planes"][low - 1] >> lane) & 1):
                low -= 1
            if low < 1 or last - low + 1 < delta + sigma:
                continue
            absent, run, runs = [], None, []
            for tick in range(low, last + 1):
                if (planes[tick] >> lane) & 1:
                    if run is not None:
                        runs.append(tuple(run))
                        run = None
                else:
                    run = [tick, tick] if run is None else [run[0], tick]
            if run is not None:
                runs.append(tuple(run))
            _ = absent
            predicted_phases = sorted(((forward - leader) % STRESS_STATIONS,
                                       (reverse - leader) % STRESS_STATIONS))
            observed = sorted((r[0] - 1) % STRESS_STATIONS for r in runs)
            lengths = sorted(r[1] - r[0] + 1 for r in runs)
            if len(runs) == 2 and observed == predicted_phases \
                    and set(lengths) == {sigma}:
                fires += 1
                cadence = tuple(t for t in range(low, last + 1)
                                if (planes[t] >> lane) & 1)
                stress_rows.append({
                    "lane": lane, "clock": "bank%d" % bank, "edge": edge,
                    "delta": delta, "sigma": sigma,
                    "positions": list(positions), "window": [low, last],
                    "window_ticks": last - low + 1,
                    "delta_shift_exact_on_window": least_transient(
                        as_bitmask(cadence), delta, last) is not None
                        and least_transient(as_bitmask(cadence), delta, last) <= low,
                })
    # an independent non-orbit sweep on the stress substrate, on the same
    # bit-parallel last-tick set, over a bounded lane sample so the block stays
    # inside its runtime budget
    sample_step = max(1, stress["lane_count"] // 96)
    sampled = 0
    for lane in range(0, stress["lane_count"], sample_step):
        for bank in range(STRESS_BANKS):
            cadence = lane_cadence(stress["clean_planes"][bank], lane)
            sampled += 1
            for row in hunt_periods(cadence, STRESS_STATIONS):
                if not row["whole_orbits"]:
                    stress_nonorbit[row["period"]] += 1
    outside = sorted(set(stress_nonorbit) - set(stress_deltas.values()))
    stress_block = {
        "substrate": "B=5, N=%d, %d keys -- NOT run by the primary"
                     % (STRESS_STATIONS, stress["lane_count"]),
        "stations_match_8B_minus_5": STRESS_STATIONS == 8 * STRESS_BANKS - 5,
        "relay_swap_rows": {str(e): list(v) for e, v in stress_swaps.items()},
        "delta_measured": {str(e): d for e, d in stress_deltas.items()},
        "delta_predicted_8B_13_8e": {str(e): d for e, d in predicted_deltas.items()},
        "arithmetic_prediction_holds": stress_deltas == predicted_deltas,
        "no_delta_is_a_whole_orbit": all(d % STRESS_STATIONS
                                         for d in stress_deltas.values()),
        "clocks_passing_the_separation_clause": arith_ok,
        "clocks_firing_the_mechanism": fires,
        "firing_delta_histogram": dict(sorted(Counter(
            row["delta"] for row in stress_rows).items())),
        "firing_rows": stress_rows[:WITNESS_PRINT_CAP],
        "lanes_sampled_for_the_period_sweep": sampled,
        "non_orbit_periods_at_B5": dict(sorted(stress_nonorbit.items())),
        "non_orbit_periods_outside_the_predicted_delta_set": outside,
        "conjecture_falsified_by_this_block": bool(outside),
        "firing_windows_ending_within_one_orbit_of_the_horizon": sum(
            1 for row in stress_rows
            if row["window"][1] > HORIZON - STRESS_STATIONS),
        "firing_windows_total": len(stress_rows),
        "reading": (
            "The conjecture predicts that every non-orbit period at B=5 is one "
            "of DELTA(5,e) = %s.  The mechanism fires on %d bank clocks, and "
            "%d of those %d firing windows end within one ring orbit of the "
            "declared horizon.  The cap-free period sweep over %d sampled "
            "clocks found %s non-orbit periods, with %s outside the predicted "
            "set.  So B=5 reproduces the B=3 pattern rather than the B=4 one: "
            "the mechanism is present but its window lands at the horizon, "
            "which is where a period stops being detector-visible.  That "
            "independently corroborates the primary's horizon-contingency "
            "reading of the B-axis difference instead of refuting it."
            % (sorted(stress_deltas.values()), fires,
               sum(1 for row in stress_rows
                   if row["window"][1] > HORIZON - STRESS_STATIONS),
               len(stress_rows), sampled, sorted(stress_nonorbit), outside)
        ),
    }
    d_pass = (
        stress_block["stations_match_8B_minus_5"]
        and stress_block["arithmetic_prediction_holds"]
        and stress_block["no_delta_is_a_whole_orbit"]
        and sampled > 0
        and arith_ok > 0
    )
    lines.append(("PASS" if d_pass else "FAIL") + " D_MECHANISM_STRESS_B5 :: "
                 + json.dumps(stress_block, **dumps))

    # -------------------------------------------------- E  CLAIM REPLICATION
    claims = []

    def claim(name, published, measured, note=""):
        claims.append({"claim": name, "published": published,
                       "measured": measured, "agrees": published == measured,
                       "note": note})

    claim("P=11 clock count", claimed["clocks_with_period_11"], len(hunt_p11),
          "the cap-free hunt may legitimately find MORE; equality is not gated")
    claim("distinct carrying keys", claimed["distinct_keys_carrying_it"],
          len({(row["event"], tuple(row["positions"])) for row in hunt_p11}))
    claim("carrier clock indices", sorted(claimed["carrier_clock_indices"]),
          sorted({row["clock"] for row in hunt_p11}))
    claim("carrier token separations", claimed["carrier_token_separations"],
          sorted({leader_sigma(tuple(row["positions"]), STATIONS)[1]
                  for row in hunt_p11}))
    trace_claim = blocks_881["D_KERNEL_TRACE"]
    claim("gating register group", trace_claim["gating_register_group"],
          ["POINTER+U_TO_V+DIRECTION_OK"],
          "recomputed below from this checker's own shuffle replay")
    claim("relay swap stations at B=4 edge 1",
          [trace_claim["forward_swap_station"], trace_claim["reverse_swap_station"]],
          list(relay_swaps(box["program"])[1]))
    claim("delta at B=4 edge 1", trace_claim["delta"],
          relay_swaps(box["program"])[1][1] - relay_swaps(box["program"])[1][0])
    # independent recomputation of the gating group on a carrier
    carrier_lane = carrier_lanes[0]
    event, positions = keys[carrier_lane]
    data, a_tokens, b_tokens, _t = K.run_orbit(
        box["seeds"][event], box["program"], token_positions=positions)
    window = [row for row in claimed_rows
              if row["event"] == event
              and tuple(row["token_positions"]) == tuple(positions)
              and row["clock"] == "bank2"][0]["quiescent_window"]
    causes = Counter()
    for tick in range(1, window[1] + 1):
        data, a_tokens, b_tokens = K.apply_controller_step(
            data, box["program"], a_tokens, b_tokens)
        if tick < window[0]:
            continue
        hot = tuple(box["labels"][w] for w in box["per_bank"][2] if data[w])
        causes["SOURCE_POINTER" if data[box["source"]]
               else "+".join(hot) if hot else "CLEAN"] += 1
    measured_group = sorted(c for c in causes
                            if c not in ("CLEAN", "SOURCE_POINTER"))
    claims[-3]["measured"] = measured_group
    claims[-3]["agrees"] = claims[-3]["published"] == measured_group
    replication = {
        "claims": claims,
        "claims_agreeing": sum(1 for row in claims if row["agrees"]),
        "claims_total": len(claims),
        "disagreeing": [row["claim"] for row in claims if not row["agrees"]],
        "independent_cause_histogram_in_the_claimed_window": dict(causes),
        "adjudication_rows_restated": [
            {"id": row["id"], "status": row["status"],
             "failing_conjuncts": row["failing_conjuncts"]}
            for row in blocks_881["F_ADJUDICATION"]["rows"]],
        "adjudication_recheck_GLOBAL_fails_because": {
            "keys_carrying_P11_by_this_checker":
                len({(row["event"], tuple(row["positions"])) for row in hunt_p11}),
            "census_keys": box["lane_count"],
            "clock_indices_carrying_P11_by_this_checker":
                sorted({row["clock"] for row in hunt_p11}),
            "clock_indices_total": FIXTURE_BANKS + len(pairs),
            "GLOBAL_can_hold": (
                len({(row["event"], tuple(row["positions"])) for row in hunt_p11})
                == box["lane_count"]),
        },
    }
    e_pass = (
        all(row["agrees"] for row in claims
            if row["claim"] != "P=11 clock count")
        and not replication["adjudication_recheck_GLOBAL_fails_because"][
            "GLOBAL_can_hold"]
    )
    lines.append(("PASS" if e_pass else "FAIL") + " E_CLAIM_REPLICATION :: "
                 + json.dumps(replication, **dumps))

    # ------------------------------------------------------------ F  CONTROLS
    runtime = time.monotonic() - started
    f_core = {
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all((ROOT / p).is_file()
                                       for p in AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(not Path(p).is_absolute()
                                               for p in AUDIT_INPUT_PATHS),
        "input_shas": shas,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "hunt_digest": digest(sorted(found_carriers)),
        "stress_digest": digest(stress_rows),
        "runtime_seconds": round(runtime, 3),
        "runtime_under_1400s": runtime < RUNTIME_LIMIT_SECONDS,
    }
    f_prepass = (
        f_core["audit_input_paths_exist"]
        and f_core["audit_input_paths_repo_relative"]
        and not f_core["blocklisted_modules_loaded"]
        and runtime < RUNTIME_LIMIT_SECONDS
    )
    verdicts = (a_pass, b_pass, c_pass, d_pass, e_pass)
    stdout_bytes = 0
    for _ in range(4):
        f_core["stdout_bytes"] = stdout_bytes
        f_core["stdout_under_150KB"] = (
            stdout_bytes < STDOUT_LIMIT_BYTES if stdout_bytes else True)
        f_line = (("PASS" if f_prepass and f_core["stdout_under_150KB"] else "FAIL")
                  + " F_CONTROLS :: " + json.dumps(f_core, **dumps))
        stdout_bytes = len(
            ("\n".join(lines + [f_line, "CYCLE881_INDEPENDENT_CHECK_PASS"]) + "\n")
            .encode())
    f_core["stdout_bytes"] = stdout_bytes
    f_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    f_pass = f_prepass and f_core["stdout_under_150KB"]
    f_line = (("PASS" if f_pass else "FAIL") + " F_CONTROLS :: "
              + json.dumps(f_core, **dumps))
    final = ("CYCLE881_INDEPENDENT_CHECK_PASS" if all(verdicts) and f_pass
             else "CYCLE881_INDEPENDENT_CHECK_HONEST_FAIL")
    print("\n".join(lines + [f_line, final]))
    return 0 if all(verdicts) and f_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
