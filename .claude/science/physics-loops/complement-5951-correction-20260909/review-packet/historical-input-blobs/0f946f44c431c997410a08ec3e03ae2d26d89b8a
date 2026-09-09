#!/usr/bin/env python3
"""Cycle 889 independent check -- spec'd to REFUTE the DELTA-spectrum census.

The Cycle-889 primary and the Cycle-879/881 runners are ALL import-blocklisted; a
meta-path firewall turns any import of them into an immediate failure and reports
its own hit list.  They are read as bytes, AST and JSON only.  The single
executable dependency is the Cycle-719 controller core, which is the substrate
under test rather than a source of claims.

Six attacks, each built to make the primary FAIL if it can.

  1  INDEPENDENT PROGRAM RECONSTRUCTION.  The station layout is re-derived from
     this checker's own reading of the pinned kernel's ``interleaved_program``
     source -- prefix (source, per bank: packet, cross, handoff, latch, swap),
     reverse (per edge in reverse: swap, unlatch, handoff-return), suffix
     (finalizer) -- built here as a list of (kind, edge) rows with no call into
     the kernel builder, then compared row by row with what the kernel emits and
     with the primary's published table.  A layout disagreement refutes the
     f(e)/r(e)/N(B) arithmetic the whole census rests on.

  2  AN INDEPENDENT PERIOD DETECTOR.  The primary reads periods with
     S ^ (S >> P) on bignum bitmasks.  This checker never forms that expression.
     It keeps each clock as a SET of clean ticks and finds the least transient by
     a backward membership scan -- walk i down from last - P and stop at the first
     i with (i in S) != (i+P in S) -- and then confirms the surviving stretch with
     a KMP FAILURE FUNCTION computed on the stable stretch as a 0/1 list, whose
     period set {m - k : k in the failure chain} must contain P.  Two different
     algorithms, neither of them the primary's.

  3  CENSUS RECOMPUTATION.  B=5 is recomputed in FULL -- every lane, every bank
     clock and every pair clock, same horizon ladder.  B=6 and B=7 are
     SPOT-VERIFIED on a declared lane subset (every 4th lane, plus every lane the
     primary named as a witness), disclosed with its selection rule and its exact
     coverage fraction.  Any period the primary published that this checker cannot
     find, and any period this checker finds that the primary did not publish, is
     reported as a MISS against the primary.

  4  THE HORIZON DERIVATION, ATTACKED.  The primary derives that a class of period
     P needs a closed quiescent stretch of length >= 2P + 1.  This checker builds
     the WORST-CASE alignment by hand -- the ideal relay-quiescent word cut to a
     stretch of exactly 2P, 2P+1 and 2P+2 ticks at every ring offset -- and checks
     that 2P really is insufficient and 2P+1 really is attainable.  If the bound
     is off by one in either direction the attack says so.

  5  THE ALIGNMENT LAW, ATTACKED.  I_max(D,sigma) = max(G - sigma, N - G - sigma)
     is searched for a counterexample well beyond the primary's cells: every
     bank count to 12, every edge, every admissible sigma, both periods, AND a
     free sweep over (N, D, sigma) triples unrelated to the 8B-5 family.  Any
     single mismatch refutes the structure theorem.

  6  TEETH.  Seven deliberately corrupted variants of the primary's own pipeline
     are run and each must be CAUGHT: a tampered pin, a dropped clock class, a
     hardcoded spectrum, a detector leaked the predicted set, an undisclosed
     shortened horizon, a skipped bank count, and a perturbed alignment law.

Nothing here is tuned to agree.  Every gate tests that an attack RAN and that its
bookkeeping is consistent; no gate tests that the attack came up empty, and the
exit code does not depend on whether the primary's claim survived.
"""
from __future__ import annotations

import array
import ast
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import random
import sys
import time


ROOT = Path(__file__).resolve().parents[1]

PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
CACHE_889 = "logs/runner-cache/frontier_cycle889_delta_spectrum_2026_07_28.txt"
PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
CHECKER_881 = "scripts/frontier_cycle881_p11_independent_check_2026_07_28.py"
RECEIPT_881 = "outputs/p11_characterization_cycle881_receipt_2026_07_28.json"
CACHE_881 = "logs/runner-cache/frontier_cycle881_p11_characterization_2026_07_28.txt"
CACHE_881_CHECK = (
    "logs/runner-cache/frontier_cycle881_p11_independent_check_2026_07_28.txt")
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CORE_719_HANDSHAKE = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py")

PINS = {
    PRIMARY_881: ("7cc1c8984869d824f33d83ccf6599c6ef9e166766015979d204309c3e820ed35",
                  "4b7297890a822184914bace90f60b47dc09f8305"),
    CHECKER_881: ("d95698707eb2c86d14789fc5a48d37219605bd214ef9bf432425950d86e27310",
                  "adafafd031e9f980b9c3a0c5b03e9679e5c1cde3"),
    RECEIPT_881: ("eeb3b18c7677fb9e0e4901d0d3118111f76d1214c290e47d3febc91387d1d390",
                  "868ea09dda4c5712908461b9472350dc89a259ca"),
    CACHE_881: ("2cc8891de863d3554c4b8fae3f8aebe920fb6cd7675da67b0cf229b9725f0973",
                "a3bb9edc20236928ea27b02d75663478d087063a"),
    CACHE_881_CHECK: ("05677189ed2799accae3681b7d38aba45c74aceb5887f645b329c0bb2af8794c",
                      "3a4e816703e40bfe5958a02d4db0e32098a6de70"),
    PRIMARY_879: ("40bf65b88db19a7872d3dd5de50c7746bbecd98ce87c2b1176ce18ec9e5f7b2f",
                  "c2147a99c1a6879508fbf250051f87115b0b9d35"),
    CORE_719: ("0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
               "c123b8d681c3d76fce08ef13d7673622deac64ad"),
    CORE_719_HANDSHAKE: (
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f"),
}
AUDIT_INPUT_PATHS = tuple(sorted(set(PINS) | {PRIMARY_889, CACHE_889}))
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 900

RUNTIME_LIMIT_SECONDS = 900
STDOUT_LIMIT_BYTES = 150 * 1024
WITNESS_PRINT_CAP = 6

TOKEN_K = 2
EVENT_COUNT = 2
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8

FULL_RECOMPUTE_BANKS = 5
SPOT_BANKS = (6, 7)
SPOT_LANE_STRIDE = 4
REPLAY_LANE_CAP = 10

DISCLOSED_SCOPE = (
    "RECOMPUTED IN FULL: B=5 at every horizon of the primary's ladder, every "
    "lane, every bank clock and every pair clock, with this checker's own "
    "corpus build and its own period detector.",
    "SPOT-VERIFIED: B=6 and B=7 at the primary's top horizon on a DECLARED lane "
    "subset -- lane index congruent to 0 modulo 4, UNION every lane the primary "
    "named as a census witness.  All bank and pair clocks of those lanes are "
    "swept; no clock of a swept lane is skipped.  The coverage fraction is "
    "reported.  A period the primary published at B=6/7 that this subset cannot "
    "reach is reported as UNREACHED_BY_SUBSET, never as refuted.",
    "NOT RECOMPUTED: B=3 and B=4 censuses (the primary's own B=4 reproduction "
    "control against the sha-pinned Cycle-881 checker census is re-verified here "
    "from the pinned cache instead of re-run).",
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


BLOCKLISTED_MODULES = (Path(PRIMARY_889).stem, Path(PRIMARY_881).stem,
                       Path(CHECKER_881).stem, Path(PRIMARY_879).stem)


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError("BLOCKLIST forbids import of %s" % fullname)
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

A = K.A
B = K.B
M = K.M
R3 = K.R3


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


# ---------------------------------------- ATTACK 1: independent program layout
def reconstructed_layout(bank_count):
    """The station layout, rebuilt here from the pinned builder's own recipe."""
    rows = [("source", 0)]
    for bank in range(bank_count):
        rows.append(("bank", bank))
        if bank:
            rows.append(("cross", bank - 1))
        if bank < bank_count - 1:
            rows.append(("handoff", bank))
            rows.append(("relay", bank))          # RELAY_LATCH
            rows.append(("relay", bank))          # RELAY_SWAP  (forward)
    for edge in reversed(range(bank_count - 1)):
        rows.append(("relay", edge))              # RELAY_SWAP  (reverse)
        rows.append(("relay", edge))              # RELAY_UNLATCH
        rows.append(("handoff", edge))
    rows.append(("finalizer", 0))
    return tuple(rows)


def reconstructed_swaps(bank_count):
    """Forward/reverse RELAY_SWAP indices from the reconstructed layout alone."""
    per_edge = defaultdict(list)
    for index, (kind, edge) in enumerate(reconstructed_layout(bank_count)):
        if kind == "relay":
            per_edge[edge].append(index)
    return {edge: (rows[1], rows[2]) for edge, rows in sorted(per_edge.items())
            if len(rows) == 4}


# ------------------------------------------- ATTACK 2: the independent detector
def failure_function(word):
    """Classic KMP failure function of a 0/1 list."""
    fail = [0] * (len(word) + 1)
    k = 0
    for index in range(1, len(word)):
        while k and word[index] != word[k]:
            k = fail[k]
        if word[index] == word[k]:
            k += 1
        fail[index + 1] = k
    return fail


def kmp_period_set(word):
    """All periods of ``word``: {len - k : k in the failure chain}."""
    fail = failure_function(word)
    periods, k = set(), fail[len(word)]
    while k:
        periods.add(len(word) - k)
        k = fail[k]
    periods.add(len(word))
    return periods


def scan_periods(members, ticks, last, periods, min_events=MIN_STABLE_EVENTS,
                 min_repeats=MIN_PERIOD_REPEATS):
    """Least transient by BACKWARD MEMBERSHIP SCAN; no bitmask anywhere.

    ``members`` is the set of clean ticks, ``ticks`` the same ticks in ascending
    order and ``last`` their maximum.  For a period P the transient is one past
    the highest i <= last - P at which membership of i and of i+P disagree; the
    scan walks down from last - P and stops at the first disagreement, so it
    costs one step on a clock that is not P-periodic.  Every surviving reading is
    then re-confirmed by the KMP FAILURE FUNCTION of a bounded suffix of the
    stable stretch (length max(4P, 64), disclosed), whose period set must contain
    P -- a second test with no shared machinery.
    """
    out = {}
    if len(members) < min_events:
        return out
    for period in periods:
        if min_repeats * period > last:
            break
        index = last - period
        while index >= 0 and ((index in members) == ((index + period) in members)):
            index -= 1
        transient = index + 1
        if last - transient < min_repeats * period:
            continue
        low = bisect_left(ticks, transient)
        events = len(ticks) - low
        if events < min_events:
            continue
        residues = {ticks[position] % period for position in range(low, len(ticks))}
        if len(residues) == period:
            continue
        window = max(4 * period, 64)
        start = max(transient, last - window + 1)
        word = [1 if tick in members else 0 for tick in range(start, last + 1)]
        if period not in kmp_period_set(word):
            continue                      # the two algorithms disagree: refuse
        out[period] = (transient, events, len(residues))
    return out


# --------------------------------------------------------- substrate, rebuilt
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
    per_bank = {}
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
        per_bank[bank] = tuple(sorted(coords))
    return per_bank, R3.X.SOURCE_POINTER


def build(bank_count, horizon, record_lanes=None):
    """Evolve the census; returns per-lane, per-bank CADENCE ARRAYS (not masks).

    ``record_lanes`` restricts which lanes are STORED, never which lanes are
    evolved: every lane of the census is evolved in the same bit-sliced pass, so
    the recorded lanes are bit-for-bit what a full recording would hold.  The
    restriction exists only to keep the tick lists inside memory at B=7 and is
    disclosed with its selection rule wherever it is used.
    """
    program = K.interleaved_program(bank_count)
    stations = len(program)
    schedules = tuple(K.mapped_macro(row) for row in program)
    places = separated(stations)
    seeds = seeds_for(bank_count, program)
    keys, states = [], []
    for event, seed in enumerate(seeds):
        for positions in places:
            state, *_ = K.run_orbit(seed, program, token_positions=positions)
            keys.append((event, positions))
            states.append(state)
    per_bank, source = watched(bank_count)
    lanes = len(keys)
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
    full = (1 << lanes) - 1
    if record_lanes is None:
        keep = full
        recorded = list(range(lanes))
    else:
        recorded = sorted(record_lanes)
        keep = 0
        for lane in recorded:
            keep |= 1 << lane
    cadence = [[array.array("i") for _ in range(bank_count)]
               for _ in range(lanes)]
    source_cadence = [array.array("i") for _ in range(lanes)]
    watch = [per_bank[bank] for bank in range(bank_count)]

    def observe(tick):
        source_dirty = planes[source] & full
        walk = keep & ~source_dirty
        while walk:
            low = walk & -walk
            source_cadence[low.bit_length() - 1].append(tick)
            walk -= low
        for bank in range(bank_count):
            dirty = source_dirty
            for wire in watch[bank]:
                dirty |= planes[wire]
            walk = keep & ~dirty
            while walk:
                low = walk & -walk
                cadence[low.bit_length() - 1][bank].append(tick)
                walk -= low

    observe(0)
    for tick in range(1, horizon + 1):
        row = masks[(tick - 1) % stations]
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
    return {"program": program, "stations": stations, "keys": tuple(keys),
            "lanes": lanes, "cadence": cadence, "source_cadence": source_cadence,
            "seeds": seeds, "per_bank": per_bank, "source": source,
            "horizon": horizon, "schedules": schedules,
            "recorded_lanes": recorded}


def shuffle_replay(seed, program, positions, coords, source, horizon):
    """One key through the controller's own token shuffle; no phase-mask rule."""
    data, a_tokens, b_tokens, _t = K.run_orbit(
        seed, program, token_positions=positions)
    cadence = []
    if not any(data[w] for w in coords) and not data[source]:
        cadence.append(0)
    for tick in range(1, horizon + 1):
        data, a_tokens, b_tokens = K.apply_controller_step(
            data, program, a_tokens, b_tokens)
        if not any(data[w] for w in coords) and not data[source]:
            cadence.append(tick)
    return cadence


def ideal_word(stations, phi_f, sigma, delta, length):
    phi_r = (phi_f + delta) % stations
    return [0 if any(((tick % stations - phi) % stations) < sigma
                     for phi in (phi_f, phi_r)) else 1
            for tick in range(length)]


def i_max_law(stations, delta, sigma):
    gap = (2 * delta) % stations
    return max(gap - sigma, stations - gap - sigma)


def max_exact_run_list(word, period):
    """Longest run of consecutive shift-exact indices, computed on a LIST."""
    span = len(word) - period
    if span <= 0:
        return 0
    best, run = 0, 0
    for index in range(span):
        if word[index] == word[index + period]:
            run += 1
            if run > best:
                best = run
        else:
            run = 0
    return best


def maximal_runs_from_ticks(ticks, horizon):
    """Maximal contiguous runs in a sorted tick list, closed inside [1, H-1]."""
    runs, start, previous = [], None, None
    for tick in ticks:
        if start is None:
            start, previous = tick, tick
        elif tick == previous + 1:
            previous = tick
        else:
            runs.append((start, previous))
            start, previous = tick, tick
    if start is not None:
        runs.append((start, previous))
    return [(a, b) for a, b in runs if a > 0 and b < horizon]


def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    # ------------------------------------------------------ A  SOURCE CONTROLS
    shas, blobs, pin_bad = {}, {}, []
    for path in AUDIT_INPUT_PATHS:
        full = ROOT / path
        if not full.is_file():
            pin_bad.append(path)
            continue
        payload = full.read_bytes()
        shas[path] = sha256(payload).hexdigest()
        blobs[path] = git_blob(payload)
        if path in PINS and (shas[path], blobs[path]) != PINS[path]:
            pin_bad.append(path)
    header_889, blocks_889 = parse_cache(CACHE_889)
    header_881c, blocks_881c = parse_cache(CACHE_881_CHECK)
    text_889 = (ROOT / PRIMARY_889).read_bytes()
    tree_889 = ast.parse(text_889.decode())
    literals_889 = {}
    for node in ast.walk(tree_889):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    try:
                        literals_889[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass
    source_block = {
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "read_mode": "WORKTREE_TEXT_AST_JSON_ONLY_BLOCKLISTED",
        "pins_rechecked": len(PINS),
        "pin_mismatches_or_missing": sorted(pin_bad),
        "primary_889_sha256": shas.get(PRIMARY_889),
        "primary_889_git_blob": blobs.get(PRIMARY_889),
        "cache_889_pins_the_worktree_runner":
            header_889.get("runner_sha256") == shas.get(PRIMARY_889),
        "cache_889_exit_code": header_889.get("exit_code"),
        "cache_889_elapsed_sec": header_889.get("elapsed_sec"),
        "primary_889_blocks_parsed": sorted(blocks_889),
        "primary_889_literals_from_ast": {
            name: literals_889.get(name)
            for name in ("HORIZON", "HORIZON_LADDER", "CENSUS_BANKS",
                         "MIN_PERIOD_REPEATS", "MIN_STABLE_EVENTS",
                         "PINNED_PERIOD_CEILING", "CONTROL_BANKS",
                         "CONTROL_HORIZON")},
        "input_shas": shas,
        "disclosed_scope": list(DISCLOSED_SCOPE),
    }
    a_pass = (
        not source_block["blocklisted_modules_loaded"]
        and not pin_bad
        and source_block["cache_889_pins_the_worktree_runner"]
        and {"A_PINS", "B_PROGRAM_REBUILD", "C_DETECTOR_SELFTEST",
             "D_ALIGNMENT_LAW", "E_HORIZON", "F_CENSUS",
             "G_REPRODUCTION_CONTROLS", "H_VERDICT"} <= set(blocks_889)
    )
    lines.append(("PASS" if a_pass else "FAIL") + " A_SOURCE_CONTROLS :: "
                 + json.dumps(source_block, **dumps))
    if not a_pass:
        print("\n".join(lines))
        return 1

    HORIZON = literals_889["HORIZON"]
    LADDER = list(literals_889["HORIZON_LADDER"])
    claim_rebuild = blocks_889["B_PROGRAM_REBUILD"]
    claim_law = blocks_889["D_ALIGNMENT_LAW"]
    claim_horizon = blocks_889["E_HORIZON"]
    claim_census = blocks_889["F_CENSUS"]["rows"]
    claim_controls = blocks_889["G_REPRODUCTION_CONTROLS"]
    claim_verdict = blocks_889["H_VERDICT"]

    # ------------------------------------- B  INDEPENDENT PROGRAM RECONSTRUCTION
    layout_rows, layout_bad = [], 0
    for bank_count in range(3, 13):
        mine = reconstructed_layout(bank_count)
        kernel = tuple((row[0], row[1]) for row in K.interleaved_program(bank_count))
        my_swaps = reconstructed_swaps(bank_count)
        stations = len(mine)
        deltas = {edge: pair[1] - pair[0] for edge, pair in my_swaps.items()}
        agrees_kernel = mine == kernel
        forward_formula = all(pair[0] == 4 + 5 * edge
                              for edge, pair in my_swaps.items())
        reverse_formula = all(
            pair[1] == (5 * bank_count - 3) + 3 * (bank_count - 2 - edge)
            for edge, pair in my_swaps.items())
        delta_formula = all(
            deltas[edge] == 8 * bank_count - 13 - 8 * edge for edge in deltas)
        stations_formula = stations == 8 * bank_count - 5
        published = None
        for row in claim_rebuild["rows"]:
            if row["banks"] == bank_count:
                published = row
        matches_primary = published is None or (
            published["stations"] == stations
            and published["relay_swap_rows"]
                == {str(e): list(v) for e, v in my_swaps.items()}
            and published["delta_measured"] == {str(e): d for e, d in deltas.items()})
        ok = (agrees_kernel and forward_formula and reverse_formula
              and delta_formula and stations_formula and matches_primary)
        layout_bad += not ok
        layout_rows.append({
            "banks": bank_count, "stations": stations,
            "reconstruction_matches_kernel_emission": agrees_kernel,
            "forward_swap_is_4_plus_5e": forward_formula,
            "reverse_swap_is_5B_minus_3_plus_3_B_minus_2_minus_e": reverse_formula,
            "delta_is_8B_minus_13_minus_8e": delta_formula,
            "stations_is_8B_minus_5": stations_formula,
            "matches_primary_published_row": matches_primary,
            "primary_published_this_bank_count": published is not None,
            "delta": {str(e): d for e, d in deltas.items()},
            "ring_complement": {str(e): stations - d for e, d in deltas.items()},
        })
    layout_block = {
        "method": "layout rebuilt here from the pinned builder's recipe as "
                  "(kind, edge) rows; the kernel builder is called only to be "
                  "COMPARED against, never to supply the answer",
        "bank_counts": list(range(3, 13)),
        "rows_disagreeing": layout_bad,
        "rows": layout_rows,
        "primary_disagreements_reported_by_primary":
            claim_rebuild["disagreements_with_pinned_881_layout"],
        "delta_and_complement_are_disjoint_parities": all(
            all(int(d) % 2 == 1 for d in row["delta"].values())
            and all(int(c) % 2 == 0 for c in row["ring_complement"].values())
            for row in layout_rows),
    }
    b_pass = (
        layout_bad == 0
        and layout_block["delta_and_complement_are_disjoint_parities"]
    )
    lines.append(("PASS" if b_pass else "FAIL") + " B_INDEPENDENT_LAYOUT :: "
                 + json.dumps(layout_block, **dumps))

    # ------------------------------------------- C  FULL RECOMPUTE AT B = 5
    box5 = build(FULL_RECOMPUTE_BANKS, HORIZON)
    stations5 = box5["stations"]
    swaps5 = reconstructed_swaps(FULL_RECOMPUTE_BANKS)
    deltas5 = sorted({pair[1] - pair[0] for pair in swaps5.values()})
    complements5 = sorted({stations5 - d for d in deltas5})
    ceiling5 = max(literals_889["PINNED_PERIOD_CEILING"], 2 * stations5)
    periods5 = sorted(set(range(2, ceiling5 + 1)) | set(deltas5) | set(complements5))
    pairs5 = tuple(combinations(range(FULL_RECOMPUTE_BANKS), 2))

    # independent tick generation on a declared lane sample
    replay_rows, replay_bad = [], 0
    replay_lanes = list(range(0, box5["lanes"], max(1, box5["lanes"] // REPLAY_LANE_CAP)))
    for lane in replay_lanes[:REPLAY_LANE_CAP]:
        event, positions = box5["keys"][lane]
        bank = 2
        got = shuffle_replay(box5["seeds"][event], box5["program"], positions,
                             box5["per_bank"][bank], box5["source"], 512)
        want = [t for t in box5["cadence"][lane][bank] if t <= 512]
        agree = got == want
        replay_bad += not agree
        replay_rows.append({"lane": lane, "bank": bank, "ticks": 512,
                            "shuffle_events": len(got), "plane_events": len(want),
                            "identical": agree})

    def census_at(cadences, lanes, bank_count, stations, periods, horizon,
                  lane_filter=None, drop_pairs=False):
        """Sweep every clock of every selected lane with the independent detector.

        The candidate period list is restricted to NON-multiples of the station
        count.  That is disclosed and it cannot hide a falsifier: a whole-orbit
        period is excluded from the non-orbit census by definition on both sides,
        and detection of a non-orbit period does not depend on whether orbit
        periods were also tried.  It exists only to keep the backward scan away
        from the very long orbit-periodic tails.
        """
        candidates = [p for p in periods if p % stations]
        pairs = tuple(combinations(range(bank_count), 2))
        spectrum_all, spectrum_closed = Counter(), Counter()
        witness, clocks = {}, 0
        for lane in range(lanes):
            if lane_filter is not None and lane not in lane_filter:
                continue
            lists = []
            for bank in range(bank_count):
                full_row = cadences[lane][bank]
                cut = bisect_right(full_row, horizon)
                lists.append(full_row[:cut])
            sets = [set(row) for row in lists]
            items = [("bank%d" % b, sets[b], lists[b]) for b in range(bank_count)]
            if not drop_pairs:
                for left, right in pairs:
                    joint = sets[left] & sets[right]
                    items.append(("pair%d%d" % (left, right), joint,
                                  sorted(joint)))
            for name, members, ordered in items:
                clocks += 1
                if not members:
                    continue
                last = ordered[-1]
                abutting = last > horizon - stations
                for period, row in scan_periods(
                        members, ordered, last, candidates).items():
                    spectrum_all[period] += 1
                    if not abutting:
                        spectrum_closed[period] += 1
                        witness.setdefault(period, {
                            "clock": name, "lane": lane,
                            "transient_tick": row[0], "last_clean_tick": last,
                            "stable_events": row[1], "residue_count": row[2]})
        return spectrum_all, spectrum_closed, witness, clocks

    b5_rows, b5_disagreements = [], []
    for horizon in LADDER:
        spectrum_all, spectrum_closed, witness, clocks = census_at(
            box5["cadence"], box5["lanes"], FULL_RECOMPUTE_BANKS, stations5,
            periods5, horizon)
        published = None
        for row in claim_census:
            if (row.get("banks") == FULL_RECOMPUTE_BANKS
                    and row.get("horizon") == horizon
                    and "instrument" not in row):
                published = row
        mine_all = {str(k): v for k, v in sorted(spectrum_all.items())}
        mine_closed = {str(k): v for k, v in sorted(spectrum_closed.items())}
        agree_all = published is not None and (
            published["non_orbit_spectrum_all_readings"] == mine_all)
        agree_closed = published is not None and (
            published["non_orbit_spectrum_horizon_closed"] == mine_closed)
        if not (agree_all and agree_closed):
            b5_disagreements.append({
                "horizon": horizon,
                "primary_all": None if published is None
                               else published["non_orbit_spectrum_all_readings"],
                "checker_all": mine_all,
                "primary_closed": None if published is None
                                  else published["non_orbit_spectrum_horizon_closed"],
                "checker_closed": mine_closed})
        b5_rows.append({
            "horizon": horizon, "clocks_swept": clocks,
            "clocks_expected": box5["lanes"] * (FULL_RECOMPUTE_BANKS + len(pairs5)),
            "checker_non_orbit_all": mine_all,
            "checker_non_orbit_closed": mine_closed,
            "primary_clocks_swept": None if published is None
                                    else published["clocks_swept"],
            "agrees_with_primary_all_readings": agree_all,
            "agrees_with_primary_closed_readings": agree_closed,
            "periods_outside_the_delta_set": sorted(
                p for p in spectrum_closed if p not in deltas5),
            "witnesses": {str(p): witness[p] for p in sorted(witness)[:8]},
        })
    # --- the EPISODE instrument, recomputed on the B=5 bank clocks
    episode_spectrum = Counter()
    episode_total, episode_clock_readings = 0, 0
    candidates5 = [p for p in periods5 if p % stations5]
    for lane in range(box5["lanes"]):
        stretches = maximal_runs_from_ticks(box5["source_cadence"][lane], HORIZON)
        episode_total += len(stretches)
        for bank in range(FULL_RECOMPUTE_BANKS):
            ordered_all = box5["cadence"][lane][bank]
            if not ordered_all:
                continue
            for start, stop in stretches:
                left = bisect_left(ordered_all, start)
                right = bisect_right(ordered_all, stop)
                if right - left < MIN_STABLE_EVENTS:
                    continue
                # rebase to the stretch's own origin, exactly as the primary's
                # (mask >> a) does: tick 0 of the episode is absolute tick start
                ordered = [tick - start for tick in ordered_all[left:right]]
                members = set(ordered)
                episode_clock_readings += 1
                for period in scan_periods(members, ordered, ordered[-1],
                                           candidates5):
                    episode_spectrum[period] += 1
    published_episode = None
    for row in claim_census:
        if row.get("banks") == FULL_RECOMPUTE_BANKS and "instrument" in row:
            published_episode = row
    episode_block = {
        "scope": "B=5 BANK clocks only (the primary's episode instrument also "
                 "sweeps pair clocks); disclosed as a partial recomputation, so "
                 "a period the primary reports only on pair clocks is expected "
                 "to be missing here and is not counted as a disagreement",
        "closed_quiescent_stretches": episode_total,
        "clock_episode_readings": episode_clock_readings,
        "checker_non_orbit_spectrum_bank_clocks_only": {
            str(k): v for k, v in sorted(episode_spectrum.items())},
        "primary_non_orbit_spectrum_all_clocks": (
            {} if published_episode is None
            else published_episode["non_orbit_spectrum"]),
        "primary_closed_stretch_count": (
            None if published_episode is None
            else published_episode["closed_quiescent_stretches_swept"]),
        "stretch_counts_agree": (
            published_episode is not None
            and episode_total
            == published_episode["closed_quiescent_stretches_swept"]),
        "periods_this_checker_finds_that_the_primary_did_not_publish": sorted(
            p for p in episode_spectrum
            if published_episode is not None
            and str(p) not in published_episode["non_orbit_spectrum"]),
        "periods_outside_the_delta_set": sorted(
            p for p in episode_spectrum if p not in deltas5),
    }

    b5_block = {
        "substrate": "B=5, N=%d, %d lanes, %d clocks -- FULL recompute"
                     % (stations5, box5["lanes"],
                        box5["lanes"] * (FULL_RECOMPUTE_BANKS + len(pairs5))),
        "episode_instrument_recomputed": episode_block,
        "detector": "backward membership scan + KMP failure-function "
                    "confirmation; the primary's S ^ (S >> P) expression is never "
                    "formed in this file",
        "delta_set": deltas5, "ring_complement_set": complements5,
        "period_ceiling": ceiling5,
        "independent_tick_generation": {
            "method": "apply_controller_step, one key at a time, 512 ticks",
            "lanes_replayed": len(replay_rows),
            "cadence_mismatches": replay_bad,
            "rows": replay_rows[:WITNESS_PRINT_CAP]},
        "rows": b5_rows,
        "disagreements_with_primary": b5_disagreements,
        "verdict": ("AGREES" if not b5_disagreements
                    else "DISAGREES -- the primary's B=5 census is not reproduced"),
    }
    c_pass = (
        replay_bad == 0
        and all(row["clocks_swept"] == row["clocks_expected"] for row in b5_rows)
        and episode_total > 0
        and episode_clock_readings > 0)
    lines.append(("PASS" if c_pass else "FAIL") + " C_FULL_RECOMPUTE_B5 :: "
                 + json.dumps(b5_block, **dumps))

    # --------------------------------------------- D  SPOT VERIFY AT B = 6, 7
    spot_rows, spot_disagreements = [], []
    for bank_count in SPOT_BANKS:
        stations = 8 * bank_count - 5
        lanes_expected = 2 * len(separated(stations))
        swaps = reconstructed_swaps(bank_count)
        deltas = sorted({pair[1] - pair[0] for pair in swaps.values()})
        complements = sorted({stations - d for d in deltas})
        ceiling = max(literals_889["PINNED_PERIOD_CEILING"], 2 * stations)
        periods = sorted(set(range(2, ceiling + 1)) | set(deltas) | set(complements))
        published = None
        for row in claim_census:
            if (row.get("banks") == bank_count and row.get("horizon") == HORIZON
                    and "instrument" not in row):
                published = row
        named = set()
        if published:
            for entry in published.get("witnesses", {}).values():
                named.add(entry["lane"])
        lane_filter = set(range(0, lanes_expected, SPOT_LANE_STRIDE)) | named
        box = build(bank_count, HORIZON, record_lanes=lane_filter)
        if box["lanes"] != lanes_expected:
            raise AssertionError((bank_count, box["lanes"], lanes_expected))
        spectrum_all, spectrum_closed, witness, clocks = census_at(
            box["cadence"], box["lanes"], bank_count, stations, periods, HORIZON,
            lane_filter=lane_filter)
        mine_closed = {str(k): v for k, v in sorted(spectrum_closed.items())}
        primary_closed = ({} if published is None
                          else published["non_orbit_spectrum_horizon_closed"])
        missing = sorted(int(p) for p in primary_closed
                         if int(p) not in spectrum_closed)
        extra = sorted(p for p in spectrum_closed if str(p) not in primary_closed)
        over_count = sorted(
            p for p in spectrum_closed
            if str(p) in primary_closed and spectrum_closed[p] > primary_closed[str(p)])
        if extra or over_count:
            spot_disagreements.append({
                "banks": bank_count, "periods_the_primary_missed": extra,
                "periods_this_subset_counts_higher_than_the_primary": over_count})
        spot_rows.append({
            "banks": bank_count, "stations": stations,
            "lane_selection_rule": "lane %% %d == 0 UNION primary witness lanes"
                                   % SPOT_LANE_STRIDE,
            "lanes_selected": len(lane_filter), "lanes_total": box["lanes"],
            "coverage_fraction": round(len(lane_filter) / box["lanes"], 4),
            "clocks_swept": clocks,
            "delta_set": deltas, "ring_complement_set": complements,
            "checker_non_orbit_closed_on_subset": mine_closed,
            "primary_non_orbit_closed_full": primary_closed,
            "periods_the_primary_published_but_the_subset_did_not_reach": missing,
            "periods_the_primary_MISSED": extra,
            "periods_counted_higher_than_the_primary": over_count,
            "periods_outside_the_delta_set_confirmed_by_this_checker": sorted(
                p for p in spectrum_closed if p not in deltas),
            "witnesses": {str(p): witness[p] for p in sorted(witness)[:8]},
        })
        del box
    spot_block = {
        "scope": DISCLOSED_SCOPE[1],
        "rows": spot_rows,
        "disagreements": spot_disagreements,
        "note": "A period in 'the primary published but the subset did not "
                "reach' is NOT a refutation: the subset is a quarter of the "
                "lanes and a rare class can live entirely outside it.  A period "
                "in 'the primary MISSED' or a count above the primary's FULL "
                "count IS a refutation, because the subset is contained in the "
                "primary's sweep.",
    }
    d_pass = all(row["clocks_swept"] > 0 for row in spot_rows) and len(spot_rows) == 2
    lines.append(("PASS" if d_pass else "FAIL") + " D_SPOT_VERIFY_B6_B7 :: "
                 + json.dumps(spot_block, **dumps))

    # ------------------------------- E  THE HORIZON DERIVATION AND THE LAW, ATTACKED
    horizon_attack = []
    for bank_count in (3, 4, 5, 6, 7):
        stations = 8 * bank_count - 5
        for edge in range(bank_count - 1):
            delta = 8 * bank_count - 13 - 8 * edge
            for period in (delta, stations - delta):
                sigma_ok = [s for s in range(1, min(delta, stations - delta))
                            if i_max_law(stations, delta, s) >= period + 1]
                if not sigma_ok:
                    continue
                sigma = sigma_ok[0]
                attain, deny = False, True
                for length, target in ((2 * period, False), (2 * period + 1, True)):
                    hit = False
                    for phi in range(stations):
                        word = ideal_word(stations, phi, sigma, delta,
                                          length + stations)[:length]
                        ordered = [i for i, bit in enumerate(word) if bit]
                        members = set(ordered)
                        if not members:
                            continue
                        last = ordered[-1]
                        found = scan_periods(members, ordered, last, [period],
                                             min_events=1)
                        if period in found:
                            hit = True
                            break
                    if target:
                        attain = hit
                    else:
                        deny = not hit
                horizon_attack.append({
                    "banks": bank_count, "edge": edge, "delta": delta,
                    "period": period, "sigma": sigma,
                    "stretch_2P_is_insufficient": deny,
                    "stretch_2P_plus_1_is_attainable_at_some_ring_offset": attain,
                    "bound_holds": deny})
    law_bad, law_cells = [], 0
    for bank_count in range(3, 13):
        stations = 8 * bank_count - 5
        for edge in range(bank_count - 1):
            delta = 8 * bank_count - 13 - 8 * edge
            for sigma in range(1, min(delta, stations - delta)):
                word = ideal_word(stations, 3, sigma, delta, stations * 12)
                predicted = i_max_law(stations, delta, sigma)
                for period in (delta, stations - delta):
                    law_cells += 1
                    measured = max_exact_run_list(word, period)
                    if measured != predicted:
                        law_bad.append({"banks": bank_count, "edge": edge,
                                        "delta": delta, "period": period,
                                        "sigma": sigma, "predicted": predicted,
                                        "measured": measured})
    rng = random.Random(889)
    free_bad, free_cells = [], 0
    for _ in range(600):
        stations = rng.randrange(9, 80) | 1
        delta = rng.randrange(2, stations - 1)
        top = min(delta, stations - delta)
        if top < 2:
            continue
        sigma = rng.randrange(1, top)
        word = ideal_word(stations, rng.randrange(stations), sigma, delta,
                          stations * 12)
        predicted = i_max_law(stations, delta, sigma)
        for period in (delta, stations - delta):
            free_cells += 1
            measured = max_exact_run_list(word, period)
            if measured != predicted:
                free_bad.append({"stations": stations, "delta": delta,
                                 "sigma": sigma, "period": period,
                                 "predicted": predicted, "measured": measured})
    # attack the primary's impossibility claim head on
    impossible_claim = claim_law["delta_members_geometrically_impossible_by_bank_count"]
    impossibility_attack = []
    for banks_text, members in sorted(impossible_claim.items()):
        bank_count = int(banks_text)
        stations = 8 * bank_count - 5
        for period in members:
            broke = None
            for sigma in range(1, stations):
                if not 1 <= sigma < min(period, stations - period):
                    continue
                word = ideal_word(stations, 3, sigma, period, stations * 12)
                if max_exact_run_list(word, period) >= period + 1:
                    broke = sigma
                    break
            impossibility_attack.append({
                "banks": bank_count, "period": period,
                "counterexample_sigma": broke,
                "claim_survives": broke is None})
    attack_block = {
        "horizon_bound_cells": len(horizon_attack),
        "horizon_bound_failures": [row for row in horizon_attack
                                   if not row["bound_holds"]][:WITNESS_PRINT_CAP],
        "horizon_bound_holds_everywhere": all(row["bound_holds"]
                                              for row in horizon_attack),
        "cells_where_2P_plus_1_is_also_sufficient": sum(
            1 for row in horizon_attack
            if row["stretch_2P_plus_1_is_attainable_at_some_ring_offset"]),
        "alignment_law_cells_in_family": law_cells,
        "alignment_law_family_mismatches": law_bad[:WITNESS_PRINT_CAP],
        "alignment_law_family_exact": not law_bad,
        "alignment_law_free_cells": free_cells,
        "alignment_law_free_mismatches": free_bad[:WITNESS_PRINT_CAP],
        "alignment_law_free_exact": not free_bad,
        "primary_claimed_cells": claim_law["cells_verified"],
        "checker_extends_to_bank_count": 12,
        "impossibility_attack": impossibility_attack,
        "impossibility_claim_survives": all(row["claim_survives"]
                                            for row in impossibility_attack),
        "note": "The alignment law is re-derived here on plain 0/1 lists with a "
                "linear scan; the primary computes it with bignum shifts.  The "
                "free sweep leaves the 8B-5 family entirely, so an accidental fit "
                "to that family would show up as a mismatch.",
    }
    e_pass = (
        law_cells > claim_law["cells_verified"] // 2
        and free_cells > 0
        and len(horizon_attack) > 0
        and len(impossibility_attack) > 0
    )
    lines.append(("PASS" if e_pass else "FAIL") + " E_LAW_AND_HORIZON_ATTACK :: "
                 + json.dumps(attack_block, **dumps))

    # --------------------------------------------------------------- F  TEETH
    teeth = []

    def tooth(name, description, fired, evidence):
        teeth.append({"tooth": name, "attack": description,
                      "detector_fired": bool(fired), "evidence": evidence})

    # T1 tampered pin
    tampered = bytearray((ROOT / PRIMARY_881).read_bytes())
    tampered[len(tampered) // 2] ^= 0x01
    tooth("T1_TAMPERED_PIN",
          "flip one byte of the pinned Cycle-881 primary and re-run the digest "
          "comparison the preflight uses",
          sha256(bytes(tampered)).hexdigest() != PINS[PRIMARY_881][0]
          and git_blob(bytes(tampered)) != PINS[PRIMARY_881][1],
          {"pinned_sha256": PINS[PRIMARY_881][0],
           "tampered_sha256": sha256(bytes(tampered)).hexdigest()})

    # T2 dropped clock class
    drop_all, drop_closed, _w, drop_clocks = census_at(
        box5["cadence"], box5["lanes"], FULL_RECOMPUTE_BANKS, stations5,
        periods5, HORIZON, drop_pairs=True)
    full_clocks = box5["lanes"] * (FULL_RECOMPUTE_BANKS + len(pairs5))
    tooth("T2_DROPPED_CLOCK_CLASS",
          "recompute the B=5 census with the pair clocks silently omitted",
          drop_clocks != full_clocks,
          {"clocks_with_pairs": full_clocks, "clocks_without_pairs": drop_clocks,
           "spectrum_with_pairs": {str(k): v for k, v in sorted(
               b5_rows[-1]["checker_non_orbit_closed"].items())},
           "spectrum_without_pairs": {str(k): v for k, v in sorted(
               drop_closed.items())},
           "completeness_gate_catches_it": drop_clocks != full_clocks})

    # T3 hardcoded spectrum
    def hardcoded_detector(_members, _last, _periods, **_kw):
        return {p: (0, 99, 1) for p in deltas5}
    hard_hits = 0
    hard_rows = 0
    for lane in range(0, box5["lanes"], 40):
        ordered = list(box5["cadence"][lane][2])
        members = set(ordered)
        if not members:
            continue
        hard_rows += 1
        honest = scan_periods(members, ordered, ordered[-1],
                              [p for p in periods5 if p % stations5])
        faked = hardcoded_detector(members, ordered[-1], periods5)
        if set(faked) != set(honest):
            hard_hits += 1
    tooth("T3_HARDCODED_SPECTRUM",
          "swap the detector for one that returns the DELTA set on every clock "
          "and compare with the honest detector clock by clock",
          hard_hits > 0,
          {"clocks_compared": hard_rows, "clocks_where_the_fake_disagrees": hard_hits,
           "faked_output": deltas5})

    # T4 predicted set leaked into the detector
    leaked_periods = sorted(set(deltas5))
    leaked_all, leaked_closed, _w, _c = census_at(
        box5["cadence"], box5["lanes"], FULL_RECOMPUTE_BANKS, stations5,
        leaked_periods, HORIZON)
    honest_closed = {int(k): v for k, v in
                     b5_rows[-1]["checker_non_orbit_closed"].items()}
    tooth("T4_LEAKED_PREDICTED_SET",
          "restrict the detector's period range to the DELTA set alone and see "
          "whether the falsifying periods vanish",
          set(leaked_closed) != set(honest_closed),
          {"honest_spectrum": {str(k): v for k, v in sorted(honest_closed.items())},
           "leaked_spectrum": {str(k): v for k, v in sorted(leaked_closed.items())},
           "periods_hidden_by_the_leak": sorted(
               set(honest_closed) - set(leaked_closed))})

    # T5 undisclosed shortened horizon
    short = HORIZON // 2
    short_all, short_closed, _w, _c = census_at(
        box5["cadence"], box5["lanes"], FULL_RECOMPUTE_BANKS, stations5,
        periods5, short)
    tooth("T5_SHORTENED_HORIZON_UNDISCLOSED",
          "run the census at half the declared horizon while claiming the full "
          "one, and compare the spectra",
          {str(k): v for k, v in sorted(short_closed.items())}
          != b5_rows[-1]["checker_non_orbit_closed"],
          {"declared_horizon": HORIZON, "secretly_used": short,
           "spectrum_at_declared": b5_rows[-1]["checker_non_orbit_closed"],
           "spectrum_at_shortened": {str(k): v for k, v in sorted(
               short_closed.items())}})

    # T6 skipped bank count
    declared_banks = sorted(literals_889["CENSUS_BANKS"])
    census_banks_seen = sorted({row["banks"] for row in claim_census})
    skipped_variant = [b for b in census_banks_seen if b != 6]

    def coverage_gate(banks_seen):
        return sorted(set(banks_seen)) == declared_banks

    tooth("T6_SKIPPED_BANK_COUNT",
          "drop B=6 from the census rows and run the coverage gate on the "
          "tampered list and on the real one",
          (not coverage_gate(skipped_variant)) and coverage_gate(census_banks_seen),
          {"declared_banks": declared_banks,
           "banks_present_in_the_primary_census": census_banks_seen,
           "tampered_banks": skipped_variant,
           "gate_on_tampered": coverage_gate(skipped_variant),
           "gate_on_real": coverage_gate(census_banks_seen)})

    # T7 perturbed alignment law
    perturbed_bad = 0
    perturbed_cells = 0
    for bank_count in range(3, 9):
        stations = 8 * bank_count - 5
        for edge in range(bank_count - 1):
            delta = 8 * bank_count - 13 - 8 * edge
            for sigma in range(1, min(delta, stations - delta)):
                word = ideal_word(stations, 3, sigma, delta, stations * 12)
                wrong = i_max_law(stations, delta, sigma) + 1
                for period in (delta, stations - delta):
                    perturbed_cells += 1
                    if max_exact_run_list(word, period) != wrong:
                        perturbed_bad += 1
    tooth("T7_PERTURBED_ALIGNMENT_LAW",
          "add one to I_max and re-verify: the identity must break on essentially "
          "every cell",
          perturbed_bad > 0,
          {"cells": perturbed_cells, "cells_the_perturbed_law_fails": perturbed_bad,
           "unperturbed_failures": len(law_bad)})

    teeth_block = {
        "teeth": teeth,
        "teeth_count": len(teeth),
        "teeth_that_fired": sum(1 for row in teeth if row["detector_fired"]),
        "teeth_that_did_not_fire": [row["tooth"] for row in teeth
                                    if not row["detector_fired"]],
    }
    f_pass = len(teeth) >= 6 and all(row["detector_fired"] for row in teeth)
    lines.append(("PASS" if f_pass else "FAIL") + " F_TEETH :: "
                 + json.dumps(teeth_block, **dumps))

    # --------------------------------- G  CONTROLS AND FALSIFIER VISIBILITY
    pinned_hunt = blocks_881c["C_ADVERSARIAL_HUNT"]
    planted_period, planted_clean = 23, 9
    word, length = [], 0
    for _ in range(12):
        word.extend([1] * planted_clean + [0] * (planted_period - planted_clean))
    ordered = [i for i, bit in enumerate(word) if bit]
    members = set(ordered)
    planted_found = scan_periods(members, ordered, ordered[-1],
                                 list(range(2, 96)))
    b4_delta = sorted({8 * 4 - 13 - 8 * e for e in range(3)})
    # and plant it into a REAL clock's tail, then run the census detector on it
    graft_lane = 0
    graft = set(box5["cadence"][graft_lane][2])
    offset = (max(graft) + 200) if graft else 200
    for index, bit in enumerate(word):
        if bit:
            graft.add(offset + index)
    graft_ordered = sorted(graft)
    graft_found = scan_periods(graft, graft_ordered, graft_ordered[-1],
                               [p for p in periods5 if p % stations5])
    controls = {
        "falsifier_visibility_synthetic": {
            "planted_period": planted_period,
            "in_B4_delta_set": planted_period in b4_delta,
            "detected_by_this_checker": planted_period in planted_found,
            "detector_output": sorted(planted_found)},
        "falsifier_visibility_grafted_onto_a_real_clock": {
            "lane": graft_lane, "bank": 2, "graft_offset": offset,
            "detected": planted_period in graft_found,
            "detector_output": sorted(graft_found),
            "outside_the_B5_delta_set": planted_period not in deltas5},
        "primary_falsifier_visibility_claim":
            claim_controls["falsifier_visibility"],
        "primary_visibility_claim_reproduced": (
            claim_controls["falsifier_visibility"]["planted_period_detected"]
            == (planted_period in planted_found)),
        "primary_B4_reproduction_claim": claim_controls["reproduction"][
            "reproduces_pinned_881_census"],
        "pinned_881_B4_histogram":
            pinned_hunt["non_orbit_period_histogram_from_the_hunt"],
        "primary_B4_histogram": claim_controls["reproduction"][
            "measured_non_orbit_histogram_all_readings"],
        "B4_reproduction_confirmed_from_the_pinned_cache": (
            {int(k): v for k, v in claim_controls["reproduction"][
                "measured_non_orbit_histogram_all_readings"].items()}
            == {int(k): v for k, v in
                pinned_hunt["non_orbit_period_histogram_from_the_hunt"].items()}
            and claim_controls["reproduction"]["measured_clocks_swept"]
            == pinned_hunt["clocks_hunted"]),
        "detector_takes_no_predicted_set": (
            "scan_periods(members, last, periods) -- the DELTA set is never an "
            "argument; the comparison happens after detection"),
    }
    g_pass = (
        controls["falsifier_visibility_synthetic"]["detected_by_this_checker"]
        and controls["falsifier_visibility_grafted_onto_a_real_clock"]["detected"]
        and controls["B4_reproduction_confirmed_from_the_pinned_cache"]
    )
    lines.append(("PASS" if g_pass else "FAIL") + " G_CONTROLS :: "
                 + json.dumps(controls, **dumps))

    # ------------------------------------------------------------- H  VERDICT
    outside_confirmed = sorted({
        (row["banks"], p) for row in spot_rows
        for p in row["periods_outside_the_delta_set_confirmed_by_this_checker"]})
    outside_confirmed += sorted({
        (FULL_RECOMPUTE_BANKS, p) for row in b5_rows
        for p in row["periods_outside_the_delta_set"]})
    verdict = {
        "primary_status": claim_verdict["status"],
        "checker_reproduces_the_B5_census": not b5_disagreements,
        "checker_finds_nothing_the_primary_missed": not spot_disagreements,
        "periods_outside_the_delta_set_confirmed_independently": [
            {"banks": bc, "period": p} for bc, p in sorted(set(outside_confirmed))],
        "episode_instrument_stretch_counts_agree":
            episode_block["stretch_counts_agree"],
        "episode_periods_the_primary_did_not_publish": episode_block[
            "periods_this_checker_finds_that_the_primary_did_not_publish"],
        "alignment_law_survives_an_independent_derivation":
            attack_block["alignment_law_family_exact"]
            and attack_block["alignment_law_free_exact"],
        "impossibility_claim_survives": attack_block["impossibility_claim_survives"],
        "horizon_bound_survives": attack_block["horizon_bound_holds_everywhere"],
        "checker_verdict": (
            "The primary's census is reproduced where it is recomputed and "
            "nothing it missed was found where it is spot-checked."
            if not b5_disagreements and not spot_disagreements else
            "REFUTED IN PART -- see disagreements_with_primary and "
            "spot_disagreements."),
        "findings_the_primary_did_not_report": [],
    }
    if b5_disagreements:
        verdict["findings_the_primary_did_not_report"].append(
            "B=5 census disagreement under an independent detector")
    if spot_disagreements:
        verdict["findings_the_primary_did_not_report"].append(
            "B=6/B=7 periods the primary's sweep missed")
    if not attack_block["alignment_law_free_exact"]:
        verdict["findings_the_primary_did_not_report"].append(
            "the alignment law fails outside the 8B-5 family")
    if episode_block["periods_this_checker_finds_that_the_primary_did_not_publish"]:
        verdict["findings_the_primary_did_not_report"].append(
            "B=5 episode periods absent from the primary's episode spectrum")
    if not episode_block["stretch_counts_agree"]:
        verdict["findings_the_primary_did_not_report"].append(
            "the closed quiescent stretch count at B=5 does not match")
    lines.append("PASS H_CHECKER_VERDICT :: " + json.dumps(verdict, **dumps))

    # ------------------------------------------------------------ I  CONTROLS
    runtime = time.monotonic() - started
    i_core = {
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all((ROOT / p).is_file()
                                       for p in AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(not Path(p).is_absolute()
                                               for p in AUDIT_INPUT_PATHS),
        "input_shas": shas,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "b5_digest": digest(b5_rows),
        "spot_digest": digest(spot_rows),
        "law_digest": digest([attack_block["alignment_law_family_exact"],
                              attack_block["alignment_law_free_exact"],
                              law_cells, free_cells]),
        "runtime_seconds": round(runtime, 3),
        "runtime_under_900s": runtime < RUNTIME_LIMIT_SECONDS,
    }
    i_prepass = (
        i_core["audit_input_paths_exist"]
        and i_core["audit_input_paths_repo_relative"]
        and not i_core["blocklisted_modules_loaded"]
        and runtime < RUNTIME_LIMIT_SECONDS
    )
    verdicts = (a_pass, b_pass, c_pass, d_pass, e_pass, f_pass, g_pass)
    stdout_bytes = 0
    for _ in range(4):
        i_core["stdout_bytes"] = stdout_bytes
        i_core["stdout_under_150KB"] = (
            stdout_bytes < STDOUT_LIMIT_BYTES if stdout_bytes else True)
        i_line = (("PASS" if i_prepass and i_core["stdout_under_150KB"] else "FAIL")
                  + " I_CONTROLS :: " + json.dumps(i_core, **dumps))
        stdout_bytes = len(
            ("\n".join(lines + [i_line, "CYCLE889_INDEPENDENT_CHECK_PASS"]) + "\n")
            .encode())
    i_core["stdout_bytes"] = stdout_bytes
    i_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    i_pass = i_prepass and i_core["stdout_under_150KB"]
    i_line = (("PASS" if i_pass else "FAIL") + " I_CONTROLS :: "
              + json.dumps(i_core, **dumps))
    final = ("CYCLE889_INDEPENDENT_CHECK_PASS" if all(verdicts) and i_pass
             else "CYCLE889_INDEPENDENT_CHECK_HONEST_FAIL")
    print("\n".join(lines + [i_line, final]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
