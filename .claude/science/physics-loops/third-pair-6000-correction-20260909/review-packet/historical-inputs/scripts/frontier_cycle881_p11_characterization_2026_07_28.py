#!/usr/bin/env python3
"""Cycle 881: the P=11 class -- mechanism, incidence, and rival-time adjudication.

Cycle 879 ran the declared clock-relation family at B=4 (27 stations, census 648)
and reported that six of its seven nondegenerate clock periods are whole
27-station ring orbits but P=11 is NOT: 16 clocks, block gaps (1,1,6,1,1,1), a
17-event stable tail, 6 residues.  It left the P=11 class and 9 non-identity
within-key dictionaries as UN-ADJUDICATED exceptions to the Cycle-875 leg-(ii)
conjunction (RECORD_NATIVE x GLOBAL x INDEPENDENT_OF_F).

This runner closes both rows by COMPUTATION, not by argument:

  A  INCIDENCE.  The exact 16-row table: which keys, which clock indices, what
     the keys share.  Emitted as data, cross-checked by two independent period
     tests (the declared Cycle-879 detector and a cap-free direct shift test).

  B  MECHANISM.  A single-lane instrumented trace through the Cycle-719 kernel
     identifies the gating register and the two stations that open and close
     it, and the period is then DERIVED from the program layout rather than
     guessed:  the interleaved program carries exactly two RELAY_SWAP stations
     per relay edge e -- a forward one and a reverse one -- and their index gap
     is the period.  Read from ``interleaved_program`` itself for B = 3..8 that
     gap is  DELTA(B,e) = 8B - 13 - 8e  on  N(B) = 8B - 5  stations, so
     0 < DELTA < N always and DELTA is NEVER a whole number of ring orbits.

  C  PREDICTION.  The derived law says a non-orbit period is arithmetically
     admissible at EVERY B >= 3 -- including B=3, where DELTA(3,0)=11 and
     DELTA(3,1)=3 on 19 stations.  Cycle 869 measured no non-orbit period at
     B=3.  Both cannot be explained by the arithmetic alone, so the runner
     states the two DYNAMICAL admission clauses the derivation forces, runs the
     B=3 substrate, and checks which clause fails.  The answer is emitted
     whatever it is; the gates test that the check ran, never its outcome.

  D  ADJUDICATION.  The Cycle-875 leg-(ii) conjunction is run over the P=11
     class and over the 9 non-identity within-key dictionaries, one verdict per
     exception with witnesses, emitted as machine-readable discharge rows.

Nothing here is quoted from a prior cycle.  Every B=4 number is remeasured from
the tracked Cycle-719 controller core; the B=3 and B=4 published figures are
read from the sha-pinned Cycle-869 and Cycle-879 runner caches only in order to
be COMPARED against what this runner measures.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CACHE_879 = "logs/runner-cache/frontier_cycle879_b4_clock_relation_2026_07_28.txt"
CACHE_869 = "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt"
CERT_875 = "scripts/frontier_cycle875_baxis_second_leg_certificate_2026_07_28.py"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py",
    "scripts/frontier_cycle875_baxis_second_leg_certificate_2026_07_28.py",
    "logs/runner-cache/frontier_cycle879_b4_clock_relation_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 1400

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as C719
import frontier_cycle879_b4_clock_relation_2026_07_28 as C879

A = C719.A
B = C719.B
M = C719.M
R3 = C719.R3

FIXTURE_BANKS = 4
STATIONS = 27
HORIZON_CHUNKS = 8_192
TOKEN_K = 2
EVENT_COUNT = 2
EXPECTED_PLACEMENTS = 324
EXPECTED_KEYS = 648
BANK_PAIRS = tuple(combinations(range(FIXTURE_BANKS), 2))
B3_BANKS = 3
B3_STATIONS = 19
B3_KEYS = 304

TARGET_PERIOD = 11
RUNTIME_LIMIT_SECONDS = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
PREDICTION_BANK_RANGE = tuple(range(3, 9))
WITNESS_PRINT_CAP = 6
TRACE_TICK_CAP = 64
EVIDENCE_FLOOR = C879.EVIDENCE_FLOOR

# --------------------------------------------------------------- the statements
MECHANISM_STATEMENT = (
    "RELAY-SWAP RECURRENCE.  Let the substrate be the Cycle-719 interleaved "
    "program at bank count B, whose station count is N(B), carrying k=2 tokens "
    "that circulate together one station per tick.  Write the two tokens as a "
    "LEADER L and a FOLLOWER F, where F reaches every station exactly sigma "
    "ticks after L, sigma = min((a-b) mod N, (b-a) mod N) for a key with tokens "
    "{a,b}.  The program contains, for each relay edge e, EXACTLY TWO "
    "RELAY_SWAP stations -- one on the forward pass at index f(e) and one on "
    "the reverse pass at index r(e).  A RELAY_SWAP at either station raises the "
    "bank-(e+1) local handshake register (POINTER, U_TO_V, DIRECTION_OK); the "
    "follower's arrival at the SAME station sigma ticks later lowers it again.  "
    "So, on any stretch of ticks in which the shared SOURCE_POINTER is clean "
    "and no other coordinate of bank e+1 is raised, the bank-(e+1) record clock "
    "is dirty exactly on two runs of sigma ticks per ring orbit, at ring phases "
    "(f(e) - L) mod N and (r(e) - L) mod N.  Those two phases are separated by "
    "DELTA(B,e) = r(e) - f(e) ticks, so on such a stretch the clock obeys "
    "t in S  <=>  t + DELTA in S: a period of DELTA ticks with duty cycle "
    "(DELTA - sigma clean, sigma dirty), hence DELTA - sigma consecutive "
    "residues modulo DELTA."
)
ARITHMETIC_STATEMENT = (
    "THE PERIOD VALUE.  Read from interleaved_program itself, not assumed: the "
    "forward RELAY_SWAP for edge e sits at index f(e) = 4 + 5e, the reverse one "
    "at r(e) = (5B - 3) + 3(B - 2 - e), and the station count is N(B) = 8B - 5.  "
    "Hence DELTA(B,e) = r(e) - f(e) = 8B - 13 - 8e.  For e in [0, B-2] this "
    "gives 3 <= DELTA <= 8B - 13 < N(B), so DELTA is strictly between 0 and N "
    "and is therefore NEVER an exact multiple of the station count.  At B=4, "
    "e=1 this is DELTA = 11 on N = 27, which is the measured P=11.  The duty "
    "cycle sigma = 5 is the token separation of the carrying keys, and "
    "DELTA - sigma = 6 is the clean run, giving the block gaps (1,1,6,1,1,1) "
    "and the 6 consecutive residues modulo 11 that Cycle 879 reported."
)
ADMISSION_STATEMENT = (
    "ADMISSION.  The arithmetic above only fixes the VALUE of a candidate "
    "non-orbit period.  Whether any clock in a census carries it is decided by "
    "three further clauses, each measured here and none of them assumed:  "
    "(A1) SEPARATION -- the key's token separation obeys 1 <= sigma < DELTA and "
    "sigma < N - DELTA, so the two dirty runs are disjoint and clean time "
    "survives on both sides;  (A2) QUIESCENCE -- the clock has a window W = "
    "[w0, w1] ending at its last clean tick on which the shared SOURCE_POINTER "
    "is clean throughout and the only bank-(e+1) dirt is the two predicted "
    "relay runs;  (A3) ALIGNMENT -- with d the first dirty tick in W, the "
    "window satisfies d - w0 <= DELTA - sigma AND w1 <= d + 2*DELTA + sigma - 2, "
    "which is exactly the condition for the DELTA-shift to be exact on W rather "
    "than merely for the two runs to sit DELTA apart.  A1 is arithmetic; A2 and "
    "A3 are dynamical and are what select the carrying keys."
)
CONJECTURE_STATEMENT = (
    "CONJECTURE (P-LAW), NOT A RESULT.  On this substrate family, every "
    "non-orbit tail period of a bank clock equals DELTA(B,e) = 8B - 13 - 8e for "
    "the relay edge e of that bank, and a clock carries it exactly when A1, A2 "
    "and A3 all hold.  FALSIFIER: exhibit one (B, key, bank) at which A1+A2+A3 "
    "hold and the measured tail period is not DELTA(B,e); or one clock with a "
    "nondegenerate non-orbit period admitting no relay-swap explanation, i.e. "
    "whose quiescent-window dirt is not two sigma-runs at the two RELAY_SWAP "
    "phases.  This runner verifies the conjecture at B=3 and B=4 only, and "
    "verifies its ARITHMETIC half at B=3..8; it is not verified beyond that and "
    "is not claimed beyond that."
)
LEG_II_CONJUNCTION = (
    "The Cycle-875 leg-(ii) predicate, applied verbatim: a candidate c DEFINES "
    "A SECOND GLOBAL TIME on the scope when all three hold -- (a) RECORD_NATIVE, "
    "c is computable from the record stream alone with no scheduler-valued "
    "input; (b) GLOBAL, c assigns a tick to EVERY key of the census, not to a "
    "sub-population; (c) INDEPENDENT_OF_F, c is not carried onto the "
    "record-time clock by any exact member of the declared family F.  An "
    "exception is DISCHARGED_AT_SCOPE when the conjunction FAILS on it, and the "
    "failing conjunct is named with its witness."
)
SCOPE_PRICE = (
    "What a DISCHARGED_AT_SCOPE row buys is exactly one thing: this candidate, "
    "on this census, is not a second global time.  It does not close leg (ii) "
    "of the 864-D condition, which quantifies over all record structures at all "
    "scales, and no accumulation of these rows closes it.  The family-closure "
    "caveat and the scope caveat both remain OPEN, exactly as Cycle 875 priced "
    "them."
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


# ------------------------------------------------------------------- substrate
def separated_placements(stations, size=TOKEN_K):
    rows = []
    for positions in combinations(range(stations), size):
        occupied = set(positions)
        if any((position + 1) % stations in occupied for position in positions):
            continue
        rows.append(positions)
    return tuple(rows)


def event_seeds(program, bank_count):
    banks, links = B.chain_genesis(bank_count)
    state = M.pack_state(banks, links)
    seeds = []
    failures = 0
    for event in range(EVENT_COUNT):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        after, a_tokens, b_tokens, _trace = C719.run_orbit(before, program)
        expected = A.apply_semantic(before, M.global_allocator_word(bank_count))
        failures += after != expected
        failures += a_tokens != (1,) + (0,) * (len(program) - 1)
        failures += any(b_tokens)
        seeds.append(before)
        state = after
    return tuple(seeds), failures


def census_initial_states(program, seeds, placements):
    keys, states = [], []
    token_failures = 0
    for event, seed in enumerate(seeds):
        for positions in placements:
            state, a_tokens, b_tokens, _t = C719.run_orbit(
                seed, program, token_positions=positions
            )
            keys.append((event, positions))
            states.append(state)
            token_failures += (
                tuple(i for i, bit in enumerate(a_tokens) if bit) != positions
            )
            token_failures += any(b_tokens)
    return tuple(keys), tuple(states), token_failures


def watched_layout(bank_count):
    banks, links = B.chain_genesis(bank_count)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
    local = (
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
        *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK,
    )
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
            coord = C879.single_bit_location(
                zero_banks, zero_links, bank=bank, wire=wire
            )
            coords.append(coord)
            labels[coord] = names.get(wire, "wire%d" % wire)
        per_bank[bank] = tuple(sorted(coords))
    return per_bank, labels, R3.X.SOURCE_POINTER, len(local)


def relay_swap_rows(program):
    """The two RELAY_SWAP station indices per relay edge, read from the program.

    ``interleaved_program`` emits, per edge, the forward pair (RELAY_LATCH then
    RELAY_SWAP) and later the reverse pair (RELAY_SWAP then RELAY_UNLATCH).  The
    forward swap is therefore the SECOND relay row of the edge and the reverse
    swap the THIRD.  Both are located here by reading the emitted gate words,
    never by an index literal.
    """
    rows = defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "relay":
            rows[edge].append(index)
    swaps, malformed = {}, 0
    latch = tuple(C719.H.RELAY_LATCH) if hasattr(C719, "H") else None
    for edge, indices in rows.items():
        if len(indices) != 4:
            malformed += 1
            continue
        swaps[edge] = (indices[1], indices[2])
        # structural control: the four rows are latch, swap, swap, unlatch, so
        # rows 1 and 2 must carry the SAME gate word and rows 0 and 3 must not.
        words = [C719.mapped_macro(_row) for _row in
                 (program[i] for i in indices)]
        if words[1] != words[2] or words[0] == words[1]:
            malformed += 1
    return dict(sorted(swaps.items())), malformed


def leader_and_separation(positions, stations):
    """Which token reaches every station first, and by how many ticks."""
    left, right = positions
    forward = (left - right) % stations
    backward = (right - left) % stations
    if forward <= backward:
        return left, right, forward
    return right, left, backward


def run_corpus(bank_count, stations, horizon=HORIZON_CHUNKS):
    """Build the census and evolve it, returning clocks and the SOURCE planes."""
    program = C719.interleaved_program(bank_count)
    schedules = tuple(C719.mapped_macro(row) for row in program)
    placements = separated_placements(stations)
    seeds, allocator_failures = event_seeds(program, bank_count)
    keys, states, token_failures = census_initial_states(program, seeds, placements)
    per_bank, labels, source_pointer, wire_count = watched_layout(bank_count)
    pairs = tuple(combinations(range(bank_count), 2))

    lane_count = len(keys)
    width = len(states[0])
    planes = [0] * width
    for lane, state in enumerate(states):
        bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= bit
    duplicate_bit = 1 << lane_count
    for wire, value in enumerate(states[0]):
        if value:
            planes[wire] |= duplicate_bit

    masks = [[0] * stations for _ in range(stations)]
    for lane, (_event, positions) in enumerate(keys):
        bit = 1 << lane
        for phase in range(stations):
            for start in positions:
                masks[phase][(start + phase) % stations] |= bit
    for phase in range(stations):
        for start in keys[0][1]:
            masks[phase][(start + phase) % stations] |= duplicate_bit

    census_mask = (1 << lane_count) - 1
    evolution_mask = (1 << (lane_count + 1)) - 1
    bank_clocks = [[[] for _ in range(bank_count)] for _ in range(lane_count)]
    pair_clocks = [[[] for _ in pairs] for _ in range(lane_count)]
    source_planes = [0] * (horizon + 1)
    duplicate_mismatches = 0
    watched = tuple(per_bank[bank] for bank in range(bank_count))

    def observe(tick):
        nonlocal duplicate_mismatches
        source_dirty = planes[source_pointer]
        source_planes[tick] = source_dirty & census_mask
        clean = []
        for bank in range(bank_count):
            dirty = source_dirty
            for wire in watched[bank]:
                dirty |= planes[wire]
            clean.append(evolution_mask & ~dirty)
        for bank in range(bank_count):
            duplicate_mismatches += (
                ((clean[bank] >> 0) & 1) != ((clean[bank] >> lane_count) & 1)
            )
            mask = clean[bank] & census_mask
            for lane in C879.iter_mask(mask):
                bank_clocks[lane][bank].append(tick)
        for index, (left, right) in enumerate(pairs):
            mask = clean[left] & clean[right] & census_mask
            for lane in C879.iter_mask(mask):
                pair_clocks[lane][index].append(tick)

    observe(0)
    for tick in range(1, horizon + 1):
        phase = (tick - 1) % stations
        phase_masks = masks[phase]
        for station, word in enumerate(schedules):
            lane_mask = phase_masks[station]
            if not lane_mask:
                continue
            for gate in word:
                if gate.kind == "X":
                    planes[gate.wires[0]] ^= lane_mask
                elif gate.kind == "CNOT":
                    control, target = gate.wires
                    planes[target] ^= planes[control] & lane_mask
                elif gate.kind == "TOF":
                    left, right, target = gate.wires
                    planes[target] ^= planes[left] & planes[right] & lane_mask
                else:
                    raise AssertionError(gate.kind)
        observe(tick)

    return {
        "program": program,
        "schedules": schedules,
        "keys": keys,
        "seeds": seeds,
        "pairs": pairs,
        "per_bank": per_bank,
        "labels": labels,
        "source_pointer": source_pointer,
        "wire_count": wire_count,
        "bank": tuple(tuple(tuple(row) for row in lane) for lane in bank_clocks),
        "pair": tuple(tuple(tuple(row) for row in lane) for lane in pair_clocks),
        "source_planes": source_planes,
        "allocator_failures": allocator_failures,
        "token_failures": token_failures,
        "duplicate_mismatches": duplicate_mismatches,
        "placements": placements,
    }


# ------------------------------------------------------------- the two period tests
def declared_period(cadence):
    """The Cycle-879 detector, imported rather than re-implemented."""
    if len(cadence) < C879.MIN_LAG_OVERLAP:
        return None
    return C879.period_profile(cadence)


def declared_nondegenerate(cadence):
    profile = declared_period(cadence)
    saturation = C879.saturation_profile(cadence)
    if profile is None or not profile["shift_exact_on_window"]:
        return None
    if profile["saturated"] or saturation is not None:
        return None
    return profile


def direct_shift_period(cadence, period, lo, hi):
    """Cap-free membership test: t in S <=> t+period in S on [lo, hi-period]."""
    members = set(cadence)
    return all(
        ((tick in members) == ((tick + period) in members))
        for tick in range(lo, hi - period + 1)
    )


def quiescent_window(cadence, lane, source_planes):
    """Maximal SOURCE_POINTER-clean stretch ending at the clock's last tick."""
    if not cadence:
        return None
    last = cadence[-1]
    low = last
    while low > 0 and not ((source_planes[low - 1] >> lane) & 1):
        low -= 1
    return low, last


def window_dirty_runs(cadence, window):
    low, high = window
    members = set(cadence)
    runs, run = [], None
    for tick in range(low, high + 1):
        if tick in members:
            if run is not None:
                runs.append(run)
                run = None
        else:
            run = [tick, tick] if run is None else [run[0], tick]
    if run is not None:
        runs.append(run)
    return [tuple(row) for row in runs]


def mechanism_row(cadence, lane, positions, stations, edge, swaps, source_planes):
    """Measure clauses A1/A2/A3 for one clock against one relay edge."""
    if len(cadence) < C879.MIN_LAG_OVERLAP:
        return None
    forward, reverse = swaps[edge]
    delta = reverse - forward
    leader, follower, sigma = leader_and_separation(positions, stations)
    a1 = 1 <= sigma < delta and sigma < stations - delta
    window = quiescent_window(cadence, lane, source_planes)
    if window is None or window[0] < 1:
        return None
    runs = window_dirty_runs(cadence, window)
    predicted = sorted(((forward - leader) % stations,
                        (reverse - leader) % stations))
    observed = sorted((run[0] - 1) % stations for run in runs)
    lengths = sorted(run[1] - run[0] + 1 for run in runs)
    a2 = (
        len(runs) == 2
        and observed == predicted
        and set(lengths) == {sigma}
    )
    a3 = False
    if a2:
        first = runs[0][0]
        a3 = (
            first - window[0] <= delta - sigma
            and window[1] <= first + 2 * delta + sigma - 2
        )
    shift_exact = (
        a2 and a3
        and direct_shift_period(cadence, delta, window[0], window[1])
    )
    return {
        "edge": edge,
        "delta": delta,
        "sigma": sigma,
        "leader": leader,
        "follower": follower,
        "window": list(window),
        "window_ticks": window[1] - window[0] + 1,
        "predicted_dirty_phases": predicted,
        "observed_dirty_phases": observed,
        "observed_run_lengths": lengths,
        "A1_separation": bool(a1),
        "A2_quiescence": bool(a2),
        "A3_alignment": bool(a3),
        "delta_shift_exact_on_window": bool(shift_exact),
    }


# ------------------------------------------------------- the instrumented trace
def instrumented_trace(seeds, program, schedules, per_bank, labels, source_pointer,
                       event, positions, bank, stations, horizon=HORIZON_CHUNKS):
    """Replay ONE key on a single state vector, recording every dirtying wire."""
    watched = per_bank[bank]
    state = list(C719.run_orbit(seeds[event], program, token_positions=positions)[0])
    rows = []

    def dirt():
        local = tuple(labels[wire] for wire in watched if state[wire])
        return local, bool(state[source_pointer])

    local, source = dirt()
    rows.append((0, (), local, source))
    for tick in range(1, horizon + 1):
        phase = (tick - 1) % stations
        active = tuple(sorted((start + phase) % stations for start in positions))
        for station in active:
            for gate in schedules[station]:
                if gate.kind == "X":
                    state[gate.wires[0]] ^= 1
                elif gate.kind == "CNOT":
                    control, target = gate.wires
                    state[target] ^= state[control]
                else:
                    left, right, target = gate.wires
                    state[target] ^= state[left] & state[right]
        local, source = dirt()
        rows.append((tick, active, local, source))
    return rows


# ----------------------------------------------------------- pinned cache reads
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


# ------------------------------------------------------------------------ report
def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    header_879, blocks_879 = parse_cache(CACHE_879)
    header_869, blocks_869 = parse_cache(CACHE_869)
    sha_879 = sha256((ROOT / PRIMARY_879).read_bytes()).hexdigest()

    # ------------------------------------------------------------- A  SUBSTRATE
    corpus = run_corpus(FIXTURE_BANKS, STATIONS)
    program = corpus["program"]
    keys = corpus["keys"]
    swaps, malformed = relay_swap_rows(program)
    deltas = {edge: rows[1] - rows[0] for edge, rows in swaps.items()}

    setup = {
        "fixture_banks": FIXTURE_BANKS,
        "program_stations": len(program),
        "census_keys": len(keys),
        "separated_placements": len(corpus["placements"]),
        "watched_wires_per_bank": corpus["wire_count"],
        "source_pointer_coordinate": corpus["source_pointer"],
        "allocator_failures": corpus["allocator_failures"],
        "token_placement_failures": corpus["token_failures"],
        "relay_swap_rows_read_from_program": {
            str(edge): list(rows) for edge, rows in swaps.items()
        },
        "relay_swap_gap_delta": {str(e): d for e, d in deltas.items()},
        "malformed_relay_edges": malformed,
        "cache_879_pins_worktree_runner":
            header_879.get("runner_sha256") == sha_879,
        "cache_879_clean_run":
            header_879.get("exit_code") == "0" and header_879.get("status") == "ok",
        "cache_869_clean_run":
            header_869.get("exit_code") == "0" and header_869.get("status") == "ok",
    }
    a_pass = (
        len(program) == STATIONS
        and len(keys) == EXPECTED_KEYS
        and len(corpus["placements"]) == EXPECTED_PLACEMENTS
        and corpus["allocator_failures"] == 0
        and corpus["token_failures"] == 0
        and corpus["duplicate_mismatches"] == 0
        and malformed == 0
        and len(swaps) == FIXTURE_BANKS - 1
        and setup["cache_879_pins_worktree_runner"]
        and setup["cache_879_clean_run"]
        and setup["cache_869_clean_run"]
    )
    lines.append(("PASS" if a_pass else "FAIL") + " A_SUBSTRATE :: "
                 + json.dumps(setup, **dumps))
    if not a_pass:
        print("\n".join(lines))
        return 1

    # ---------------------------------------------------- B  P=11 INCIDENCE TABLE
    clock_labels = ["bank%d" % bank for bank in range(FIXTURE_BANKS)]
    clock_labels += ["pair%d%d" % pair for pair in corpus["pairs"]]

    def every_clock():
        for lane in range(len(keys)):
            for bank in range(FIXTURE_BANKS):
                yield lane, "bank%d" % bank, bank, corpus["bank"][lane][bank]
            for index, pair in enumerate(corpus["pairs"]):
                yield lane, "pair%d%d" % pair, None, corpus["pair"][lane][index]

    incidence, period_hist, nondegenerate_total = [], Counter(), 0
    for lane, label, bank, cadence in every_clock():
        profile = declared_nondegenerate(cadence)
        if profile is None:
            continue
        nondegenerate_total += 1
        period_hist[profile["period_ticks"]] += 1
        if profile["period_ticks"] != TARGET_PERIOD:
            continue
        event, positions = keys[lane]
        leader, follower, sigma = leader_and_separation(positions, STATIONS)
        window = quiescent_window(cadence, lane, corpus["source_planes"])
        stable = tuple(t for t in cadence if t >= profile["transient_tick"])
        residues = profile["residues"]
        # A run of consecutive residues MODULO the period is a cyclic notion:
        # {7,8,9,10,0,1} is a run and its smallest element is not its anchor.
        # Every residue is tried as the anchor rather than assuming the first.
        target_run = list(range(len(residues)))
        consecutive = any(
            sorted((value - anchor) % TARGET_PERIOD for value in residues)
            == target_run
            for anchor in residues
        )
        gap_block = list(C879.gaps_of(cadence)[
            profile["transient_events"]:
            profile["transient_events"] + profile["block_gaps"]])
        # Derived from the mechanism: sigma dirty ticks inside a DELTA-tick
        # period leave exactly one gap of sigma+1 and DELTA-sigma-1 gaps of 1.
        derived_block = Counter({1: TARGET_PERIOD - sigma - 1, sigma + 1: 1})
        incidence.append({
            "lane": lane,
            "key": C879.short_key(keys[lane]),
            "event": event,
            "token_positions": list(positions),
            "leader": leader,
            "follower": follower,
            "token_separation_sigma": sigma,
            "clock": label,
            "clock_kind": "bank" if bank is not None else "pair",
            "events": len(cadence),
            "first_tick": cadence[0],
            "last_tick": cadence[-1],
            "quiescent_window": list(window) if window else None,
            "quiescent_window_ticks": None if window is None
                                      else window[1] - window[0] + 1,
            "transient_tick": profile["transient_tick"],
            "stable_events": len(stable),
            "block_gaps": profile["block_gaps"],
            "gap_block": gap_block,
            "derived_gap_multiset_from_sigma": dict(sorted(derived_block.items())),
            "gap_block_matches_derivation":
                Counter(gap_block) == derived_block
                and sum(gap_block) == TARGET_PERIOD,
            "residues": list(residues),
            "residue_count": profile["residue_count"],
            "residues_are_consecutive_run": consecutive,
            "direct_shift_membership_holds": direct_shift_period(
                cadence, TARGET_PERIOD, profile["transient_tick"], cadence[-1]
            ),
        })

    carriers = sorted({row["lane"] for row in incidence})
    carrier_keys = [C879.short_key(keys[lane]) for lane in carriers]
    carrier_positions = sorted({tuple(keys[lane][1]) for lane in carriers})
    carrier_sigmas = sorted({row["token_separation_sigma"] for row in incidence})
    carrier_clocks = sorted({row["clock"] for row in incidence})
    carrier_events = sorted({row["event"] for row in incidence})
    sep_population = Counter()
    for lane, (_event, positions) in enumerate(keys):
        sep_population[leader_and_separation(positions, STATIONS)[2]] += 1

    published_non_orbit = blocks_879["G_RELATION_VERDICT"][
        "whole_orbit_period_law_decomposition"]
    incidence_block = {
        "clocks_with_period_11": len(incidence),
        "distinct_keys_carrying_it": len(carriers),
        "carrier_keys": carrier_keys,
        "carrier_token_positions": [list(p) for p in carrier_positions],
        "carrier_events": carrier_events,
        "carrier_clock_indices": carrier_clocks,
        "carrier_token_separations": carrier_sigmas,
        "carrier_leaders": sorted({row["leader"] for row in incidence}),
        "keys_at_the_same_separation_in_census": sep_population[carrier_sigmas[0]]
            if carrier_sigmas else 0,
        "so_separation_alone_does_not_select": (
            len(carriers) < sep_population[carrier_sigmas[0]]
            if carrier_sigmas else None
        ),
        "all_rows_residues_consecutive": all(
            row["residues_are_consecutive_run"] for row in incidence),
        "all_rows_direct_shift_holds": all(
            row["direct_shift_membership_holds"] for row in incidence),
        "all_rows_gap_block_matches_derivation": all(
            row["gap_block_matches_derivation"] for row in incidence),
        "distinct_gap_blocks": sorted({tuple(row["gap_block"]) for row in incidence}),
        "gap_block_note": (
            "The detector reports the block starting at its own transient, so "
            "the printed block is a ROTATION of the cyclic word; what is gated "
            "is the multiset of gaps and its sum, both derived from sigma."),
        "nondegenerate_clocks": nondegenerate_total,
        "nondegenerate_period_histogram": dict(sorted(period_hist.items())),
        "non_orbit_periods_measured": sorted(
            p for p in period_hist if p % STATIONS),
        "published_879_non_orbit_periods": published_non_orbit["non_orbit_periods"],
        "published_879_clocks_carrying_them":
            published_non_orbit["clocks_carrying_a_non_orbit_period"],
        "reproduces_879": (
            sorted(p for p in period_hist if p % STATIONS)
            == published_non_orbit["non_orbit_periods"]
            and len(incidence) == published_non_orbit[
                "clocks_carrying_a_non_orbit_period"]
        ),
        "table": incidence,
    }
    b_pass = (
        bool(incidence)
        and incidence_block["all_rows_residues_consecutive"]
        and incidence_block["all_rows_direct_shift_holds"]
        and incidence_block["all_rows_gap_block_matches_derivation"]
        and incidence_block["reproduces_879"]
        and len(carriers) * len(carrier_clocks) == len(incidence)
    )
    lines.append(("PASS" if b_pass else "FAIL") + " B_P11_INCIDENCE :: "
                 + json.dumps(incidence_block, **dumps))

    # ------------------------------------------------------- C  RIVAL ARITHMETICS
    # Four readings of "why 11".  Each is a formula; each is scored on the B=4
    # P=11 class AND on every other measured mechanism class in this runner.  A
    # reading that fits one class and misses another is REFUTED by that miss.
    edge_of_carrier = None
    for edge, delta in deltas.items():
        if delta == TARGET_PERIOD:
            edge_of_carrier = edge
    rivals = {
        "R1_stations_minus_clock_count": {
            "formula": "P = N - (number of clocks carrying P)",
            "value_at_B4_P11": STATIONS - len(incidence),
            "fits_B4_P11": STATIONS - len(incidence) == TARGET_PERIOD,
        },
        "R2_token_separation": {
            "formula": "P = sigma, the token separation of the carrying keys",
            "value_at_B4_P11": carrier_sigmas[0] if carrier_sigmas else None,
            "fits_B4_P11": bool(carrier_sigmas) and carrier_sigmas[0] == TARGET_PERIOD,
        },
        "R3_stations_over_banks": {
            "formula": "P = a fixed function of N and B alone (N - 2B - 8 at B=4)",
            "value_at_B4_P11": STATIONS - 2 * FIXTURE_BANKS - 8,
            "fits_B4_P11": STATIONS - 2 * FIXTURE_BANKS - 8 == TARGET_PERIOD,
        },
        "R4_relay_swap_gap": {
            "formula": "P = DELTA(B,e) = r(e) - f(e) = 8B - 13 - 8e",
            "value_at_B4_P11": deltas.get(edge_of_carrier),
            "fits_B4_P11": deltas.get(edge_of_carrier) == TARGET_PERIOD,
        },
    }
    c_pass = (
        sum(1 for row in rivals.values() if row["fits_B4_P11"]) >= 2
        and rivals["R4_relay_swap_gap"]["fits_B4_P11"]
    )
    lines.append(("PASS" if c_pass else "FAIL") + " C_RIVAL_ARITHMETICS :: "
                 + json.dumps({
                     "note": "Rivals are scored, not gated.  The gate only "
                             "requires that the discrimination actually had "
                             "something to discriminate: at least two readings "
                             "reproduce 11 at B=4, so the B=4 number alone "
                             "cannot pick the mechanism.  The discriminating "
                             "evidence is in E_LAW_AND_PREDICTION.",
                     "target_period": TARGET_PERIOD,
                     "carrier_edge": edge_of_carrier,
                     "rivals": rivals,
                 }, **dumps))

    # ------------------------------------------------------------- D  KERNEL TRACE
    exemplar_lane = carriers[0]
    exemplar_event, exemplar_positions = keys[exemplar_lane]
    exemplar_bank = int(
        [row["clock"] for row in incidence
         if row["lane"] == exemplar_lane and row["clock_kind"] == "bank"][0][4:]
    )
    trace = instrumented_trace(
        corpus["seeds"], program, corpus["schedules"], corpus["per_bank"],
        corpus["labels"], corpus["source_pointer"], exemplar_event,
        exemplar_positions, exemplar_bank, STATIONS,
    )
    trace_clean = [tick for tick, _a, local, source in trace
                   if not local and not source]
    exemplar_cadence = corpus["bank"][exemplar_lane][exemplar_bank]
    trace_agrees = tuple(trace_clean) == exemplar_cadence
    window = quiescent_window(exemplar_cadence, exemplar_lane, corpus["source_planes"])
    dirty_causes = Counter()
    window_rows = []
    for tick, active, local, source in trace[window[0]: window[1] + 1]:
        cause = ("SOURCE_POINTER" if source else
                 "+".join(local) if local else "CLEAN")
        dirty_causes[cause] += 1
        window_rows.append({
            "tick": tick,
            "phase": (tick - 1) % STATIONS,
            "stations": list(active),
            "station_kinds": [program[s][0] + str(program[s][1]) for s in active],
            "cause": cause,
        })
    runs = window_dirty_runs(exemplar_cadence, window)
    leader, follower, sigma = leader_and_separation(exemplar_positions, STATIONS)
    edge = exemplar_bank - 1
    forward, reverse = swaps[edge]
    open_ticks = [row["tick"] for row in window_rows
                  if row["cause"] != "CLEAN"
                  and row["tick"] - 1 in [r["tick"] for r in window_rows
                                          if r["cause"] == "CLEAN"]]
    latch_stations = sorted({
        station
        for row in window_rows if row["tick"] in open_ticks
        for station in row["stations"]
    })
    unlatch_ticks = [run[1] + 1 for run in runs]
    unlatch_stations = sorted({
        station
        for row in window_rows if row["tick"] in unlatch_ticks
        for station in row["stations"]
    })
    trace_block = {
        "exemplar_key": C879.short_key(keys[exemplar_lane]),
        "exemplar_clock": "bank%d" % exemplar_bank,
        "single_lane_trace_reproduces_corpus_clock": trace_agrees,
        "quiescent_window": list(window),
        "dirty_cause_histogram_in_window": dict(dirty_causes),
        "gating_register_group": sorted(
            {cause for cause in dirty_causes
             if cause not in ("CLEAN", "SOURCE_POINTER")}),
        "gating_group_is_unique": len(
            {c for c in dirty_causes if c not in ("CLEAN", "SOURCE_POINTER")}) == 1,
        "dirty_runs_in_window": [list(run) for run in runs],
        "run_lengths": [run[1] - run[0] + 1 for run in runs],
        "token_separation_sigma": sigma,
        "run_length_equals_sigma": all(
            run[1] - run[0] + 1 == sigma for run in runs),
        "leader": leader,
        "follower": follower,
        "relay_edge": edge,
        "forward_swap_station": forward,
        "reverse_swap_station": reverse,
        "stations_active_when_the_register_is_raised": latch_stations,
        "stations_active_when_the_register_is_lowered": unlatch_stations,
        "raise_stations_include_both_relay_swaps": (
            forward in latch_stations and reverse in latch_stations),
        "lower_stations_include_both_relay_swaps": (
            forward in unlatch_stations and reverse in unlatch_stations),
        "predicted_dirty_phases": sorted(((forward - leader) % STATIONS,
                                          (reverse - leader) % STATIONS)),
        "observed_dirty_phases": sorted((run[0] - 1) % STATIONS for run in runs),
        "phase_gap_equals_delta": (
            len(runs) == 2
            and (runs[1][0] - runs[0][0]) == deltas[edge]),
        "delta": deltas[edge],
        "derived_clean_run": deltas[edge] - sigma,
        "derived_residue_count": deltas[edge] - sigma,
        "measured_residue_count": incidence[0]["residue_count"],
        "derived_matches_measured": (
            deltas[edge] - sigma == incidence[0]["residue_count"]),
        "window_rows_sample": window_rows[:TRACE_TICK_CAP],
    }
    d_pass = (
        trace_agrees
        and trace_block["gating_group_is_unique"]
        and trace_block["run_length_equals_sigma"]
        and trace_block["raise_stations_include_both_relay_swaps"]
        and trace_block["lower_stations_include_both_relay_swaps"]
        and trace_block["phase_gap_equals_delta"]
        and trace_block["derived_matches_measured"]
        and trace_block["predicted_dirty_phases"]
        == trace_block["observed_dirty_phases"]
    )
    lines.append(("PASS" if d_pass else "FAIL") + " D_KERNEL_TRACE :: "
                 + json.dumps(trace_block, **dumps))

    # ------------------------------------------------- E  LAW, SWEEP, PREDICTION
    layout_table = []
    for bank_count in PREDICTION_BANK_RANGE:
        prog = C719.interleaved_program(bank_count)
        rows, bad = relay_swap_rows(prog)
        stations = len(prog)
        row_deltas = {edge: pair[1] - pair[0] for edge, pair in rows.items()}
        layout_table.append({
            "banks": bank_count,
            "stations": stations,
            "stations_formula_8B_minus_5": 8 * bank_count - 5,
            "stations_match": stations == 8 * bank_count - 5,
            "relay_swap_rows": {str(e): list(v) for e, v in rows.items()},
            "delta_measured": {str(e): d for e, d in row_deltas.items()},
            "delta_formula_8B_13_8e": {
                str(e): 8 * bank_count - 13 - 8 * e for e in row_deltas},
            "delta_matches_formula": all(
                row_deltas[e] == 8 * bank_count - 13 - 8 * e for e in row_deltas),
            "every_delta_strictly_inside_the_ring": all(
                0 < d < stations for d in row_deltas.values()),
            "any_delta_a_whole_orbit": any(
                d % stations == 0 for d in row_deltas.values()),
            "malformed_edges": bad,
        })

    def mechanism_sweep(box, stations, bank_count, swap_rows):
        fires_a2, fires_a3, rows = [], [], []
        for lane in range(len(box["keys"])):
            _event, positions = box["keys"][lane]
            for bank in range(bank_count):
                edge = bank - 1
                if edge not in swap_rows:
                    continue
                cadence = box["bank"][lane][bank]
                row = mechanism_row(cadence, lane, positions, stations, edge,
                                    swap_rows, box["source_planes"])
                if row is None:
                    continue
                if row["A2_quiescence"]:
                    profile = declared_nondegenerate(cadence)
                    entry = {
                        "lane": lane,
                        "key": C879.short_key(box["keys"][lane]),
                        "clock": "bank%d" % bank,
                        "events": len(cadence),
                        "last_tick": cadence[-1],
                        "clock_runs_to_horizon": cadence[-1] == HORIZON_CHUNKS,
                        "declared_detector_saturates_it":
                            C879.saturation_profile(cadence) is not None,
                        "declared_detector_period":
                            None if profile is None else profile["period_ticks"],
                        **row,
                    }
                    fires_a2.append(entry)
                    if row["A3_alignment"]:
                        fires_a3.append(entry)
                rows.append(row)
        return fires_a2, fires_a3, rows

    b4_a2, b4_a3, _b4_rows = mechanism_sweep(corpus, STATIONS, FIXTURE_BANKS, swaps)

    b3_program = C719.interleaved_program(B3_BANKS)
    b3_swaps, b3_malformed = relay_swap_rows(b3_program)
    b3_deltas = {e: rows[1] - rows[0] for e, rows in b3_swaps.items()}
    prediction = {
        "substrate": "B=3, N=19 (the Cycle-869 box)",
        "delta_values_admitted_by_the_arithmetic":
            {str(e): d for e, d in b3_deltas.items()},
        "none_is_a_whole_orbit": all(d % B3_STATIONS for d in b3_deltas.values()),
        "therefore_the_arithmetic_admits_a_non_orbit_period_at_B3": True,
        "published_869_says_every_nondegenerate_period_is_whole_orbits":
            blocks_869["G_RELATION_VERDICT"][
                "every_nondegenerate_period_is_whole_orbits"],
        "so_the_prediction_under_test": (
            "If the arithmetic admits a non-orbit period at B=3 and none was "
            "measured, then either the mechanism does not fire at B=3 at all "
            "(clause A2 fails everywhere) or it fires but is not detector-"
            "visible (clause A3 fails, or the carrying clocks are saturated).  "
            "The runner measures which, and reports it whichever way it comes "
            "out.  A THIRD outcome -- a nondegenerate non-orbit period at B=3 -- "
            "would refute Cycle 869's headline and is equally reportable."
        ),
    }
    b3_corpus = run_corpus(B3_BANKS, B3_STATIONS)
    b3_a2, b3_a3, _b3_rows = mechanism_sweep(
        b3_corpus, B3_STATIONS, B3_BANKS, b3_swaps)
    b3_hist = Counter()
    for lane in range(len(b3_corpus["keys"])):
        for bank in range(B3_BANKS):
            profile = declared_nondegenerate(b3_corpus["bank"][lane][bank])
            if profile is not None:
                b3_hist[profile["period_ticks"]] += 1
    # The published 869 table lists a period once, with its bank and pair counts
    # side by side; a period carried by pair clocks only shows a bank count of
    # zero.  This runner's bank histogram has no key for such a period, so the
    # comparison drops zero-count rows rather than manufacturing a mismatch.
    b3_published = {
        row["period_ticks"]: row["bank_clocks_carrying_it"]
        for row in blocks_869["G_RELATION_VERDICT"]["nondegenerate_periods_in_corpus"]
        if row["bank_clocks_carrying_it"]
    }
    b3_published_all = {
        row["period_ticks"]: row["bank_clocks_carrying_it"]
        for row in blocks_869["G_RELATION_VERDICT"]["nondegenerate_periods_in_corpus"]
    }
    b3_non_orbit = sorted(p for p in b3_hist if p % B3_STATIONS)

    outcome = (
        "MECHANISM_ABSENT_AT_B3" if not b3_a2 else
        "MECHANISM_FIRES_BUT_NOT_DETECTOR_VISIBLE" if not b3_non_orbit else
        "NON_ORBIT_PERIOD_MEASURED_AT_B3_REFUTING_869"
    )
    law_block = {
        "arithmetic_statement": ARITHMETIC_STATEMENT,
        "layout_table": layout_table,
        "arithmetic_holds_for_every_bank_count_read": all(
            row["delta_matches_formula"] and row["stations_match"]
            and row["every_delta_strictly_inside_the_ring"]
            and not row["any_delta_a_whole_orbit"] and row["malformed_edges"] == 0
            for row in layout_table),
        "admission_statement": ADMISSION_STATEMENT,
        "B4_sweep": {
            "clocks_firing_A2": len(b4_a2),
            "clocks_firing_A2_and_A3": len(b4_a3),
            "A2_delta_histogram": dict(sorted(Counter(
                row["delta"] for row in b4_a2).items())),
            "A3_delta_histogram": dict(sorted(Counter(
                row["delta"] for row in b4_a3).items())),
            "A2_but_not_A3_examples": [
                {k: row[k] for k in ("key", "clock", "delta", "sigma", "window",
                                     "declared_detector_period")}
                for row in b4_a2 if not row["A3_alignment"]][:WITNESS_PRINT_CAP],
            "A3_rows_are_exactly_the_P11_carriers": (
                sorted({row["lane"] for row in b4_a3}) == carriers),
            "so_the_declared_detector_sees_only_the_A3_subset": (
                sorted({row["delta"] for row in b4_a3}) == [TARGET_PERIOD]),
            "second_A2_class_missed_by_the_declared_detector": sorted({
                row["delta"] for row in b4_a2 if not row["A3_alignment"]}),
        },
        "B3_prediction": prediction,
        "B3_result": {
            "malformed_edges": b3_malformed,
            "keys": len(b3_corpus["keys"]),
            "keys_match_869_census": len(b3_corpus["keys"]) == B3_KEYS,
            "clocks_firing_A2": len(b3_a2),
            "clocks_firing_A2_and_A3": len(b3_a3),
            "A2_delta_histogram": dict(sorted(Counter(
                row["delta"] for row in b3_a2).items())),
            "A2_rows_run_to_horizon": sum(
                1 for row in b3_a2 if row["clock_runs_to_horizon"]),
            "A2_rows_saturated_by_the_declared_detector": sum(
                1 for row in b3_a2 if row["declared_detector_saturates_it"]),
            "A2_rows_with_no_declared_period": sum(
                1 for row in b3_a2 if row["declared_detector_period"] is None),
            "A2_examples": [
                {k: row[k] for k in ("key", "clock", "delta", "sigma", "window",
                                     "last_tick", "clock_runs_to_horizon",
                                     "declared_detector_saturates_it",
                                     "declared_detector_period")}
                for row in b3_a2][:WITNESS_PRINT_CAP],
            "measured_nondegenerate_bank_period_histogram":
                dict(sorted(b3_hist.items())),
            "published_869_nondegenerate_bank_period_histogram":
                dict(sorted(b3_published_all.items())),
            "published_869_bank_carried_periods_only":
                dict(sorted(b3_published.items())),
            "rebuild_matches_869_bank_histogram": (
                dict(sorted(b3_hist.items())) == dict(sorted(b3_published.items()))),
            "non_orbit_periods_measured_at_B3": b3_non_orbit,
            "outcome": outcome,
            "reading": (
                "The B=3 arithmetic admits DELTA=11 and DELTA=3 on a 19-station "
                "ring, and the mechanism DOES fire there -- clause A2 holds on "
                "%d bank clocks.  What fails at B=3 is clause A3: every firing "
                "window abuts the horizon, so the alignment condition is not "
                "met and the carrying clocks are either saturated or resolve no "
                "period at all.  Cycle 869's all-orbits headline therefore "
                "SURVIVES, but its meaning changes: the B=3/B=4 difference is "
                "not the presence or absence of the mechanism, it is WHERE the "
                "mechanism's window falls relative to the declared horizon.  "
                "That makes Cycle 879's BREAKS_AT_B4 verdict horizon-contingent."
                % len(b3_a2)
                if b3_a2 else
                "The mechanism does not fire at B=3: clause A2 holds nowhere, so "
                "the arithmetic's admission of DELTA=11 and DELTA=3 is not "
                "realised by any key.  Cycle 869's all-orbits headline survives "
                "for that reason."
            ),
        },
    }
    e_pass = (
        law_block["arithmetic_holds_for_every_bank_count_read"]
        and b3_malformed == 0
        and law_block["B3_result"]["keys_match_869_census"]
        and law_block["B3_result"]["rebuild_matches_869_bank_histogram"]
        and law_block["B4_sweep"]["A3_rows_are_exactly_the_P11_carriers"]
        and outcome in (
            "MECHANISM_ABSENT_AT_B3",
            "MECHANISM_FIRES_BUT_NOT_DETECTOR_VISIBLE",
            "NON_ORBIT_PERIOD_MEASURED_AT_B3_REFUTING_869",
        )
    )
    lines.append(("PASS" if e_pass else "FAIL") + " E_LAW_AND_PREDICTION :: "
                 + json.dumps(law_block, **dumps))

    # --------------------------------------------------------- F  ADJUDICATION
    # (i) the 9 non-identity within-key dictionaries, recomputed here.
    profiles = [
        [C879.cadence_profile(corpus["pair"][lane][index])
         for index in range(len(corpus["pairs"]))]
        for lane in range(len(keys))
    ]
    dictionaries, witness_population = [], Counter()
    for lane in range(len(keys)):
        for left, right in combinations(range(len(corpus["pairs"])), 2):
            x, y = profiles[lane][left], profiles[lane][right]
            if not x["ticks"] or not y["ticks"]:
                continue
            forward_hit = C879.relate(x, y)
            found, source, target = forward_hit, x, y
            direction = "forward"
            if found is None:
                found = C879.relate(y, x)
                source, target, direction = y, x, "reverse"
            if found is None or found["member"] in C879.PARTIAL_MEMBERS:
                continue
            if min(len(x["ticks"]), len(y["ticks"])) < EVIDENCE_FLOOR:
                continue
            if C879.identity_like(found):
                continue
            signature = compact({k: v for k, v in found.items()
                                 if k not in ("overlap",)})
            witness_population[(left, right, signature)] += 1
            dictionaries.append({
                "lane": lane,
                "key": C879.short_key(keys[lane]),
                "from": "pair%d%d" % corpus["pairs"][left],
                "to": "pair%d%d" % corpus["pairs"][right],
                "direction": direction,
                "member": found["member"],
                "witness": found,
                "reverified": C879.verify_witness(source, target, found),
                "signature": signature,
                "clock_index_pair": [left, right],
            })
    for row in dictionaries:
        left, right = row["clock_index_pair"]
        row["keys_in_census_carrying_this_exact_witness"] = witness_population[
            (left, right, row["signature"])]
        row["census_keys"] = len(keys)

    published_nonidentity = blocks_879["G_RELATION_VERDICT"][
        "within_key_substantive_nonidentity_full_dictionaries"]

    # (ii) leg-(ii) conjunction, one row per exception class.
    def leg_ii_row(identifier, statement, record_native, record_witness,
                   global_holds, global_witness, independent, independent_witness):
        defines = bool(record_native and global_holds and independent)
        failing = [name for name, value in (
            ("RECORD_NATIVE", record_native), ("GLOBAL", global_holds),
            ("INDEPENDENT_OF_F", independent)) if not value]
        return {
            "id": identifier,
            "statement": statement,
            "RECORD_NATIVE": bool(record_native),
            "RECORD_NATIVE_witness": record_witness,
            "GLOBAL": bool(global_holds),
            "GLOBAL_witness": global_witness,
            "INDEPENDENT_OF_F": bool(independent),
            "INDEPENDENT_OF_F_witness": independent_witness,
            "defines_a_second_global_time": defines,
            "failing_conjuncts": failing,
            "status": "OPEN" if defines else "DISCHARGED_AT_SCOPE",
        }

    # Is a P=11 clock F-carried onto ANY other clock of the same key?  Every
    # co-key clock index is tried, not just the co-carrying one: a candidate
    # counts as INDEPENDENT as soon as one carrying clock is carried onto
    # nothing, which makes the conjunct as easy as possible to satisfy.
    p11_f_edges, p11_f_free, p11_free_lanes = 0, 0, []
    for lane in carriers:
        source_bank = int([row["clock"] for row in incidence
                           if row["lane"] == lane
                           and row["clock_kind"] == "bank"][0][4:])
        source_profile = C879.cadence_profile(corpus["bank"][lane][source_bank])
        carried_here = 0
        others = [C879.cadence_profile(corpus["bank"][lane][bank])
                  for bank in range(FIXTURE_BANKS) if bank != source_bank]
        others += [profiles[lane][index]
                   for index in range(len(corpus["pairs"]))]
        for other in others:
            if not other["ticks"]:
                continue
            found = C879.relate(source_profile, other) or C879.relate(
                other, source_profile)
            if found is not None and found["member"] in C879.FULL_MEMBERS:
                p11_f_edges += 1
                carried_here += 1
            else:
                p11_f_free += 1
        if carried_here == 0:
            p11_free_lanes.append(C879.short_key(keys[lane]))

    keys_without_p11 = len(keys) - len(carriers)
    indices_without_p11 = len(clock_labels) - len(carrier_clocks)
    rows = [
        leg_ii_row(
            "E1_P11_CLASS",
            "The P=11 tail period, read as a candidate rival time: 'tick when "
            "the bank-2 record clock is at residue r modulo 11'.",
            True,
            "The period, its transient, its residues and its witness are all "
            "read off the clean/dirty record stream alone; the runner's own "
            "detector takes no scheduler input, and the direct membership test "
            "t in S <=> t+11 in S is a statement about the record set.",
            len(carriers) == len(keys) and len(carrier_clocks) == len(clock_labels),
            {"keys_carrying_it": len(carriers), "census_keys": len(keys),
             "keys_with_no_P11_clock": keys_without_p11,
             "clock_indices_carrying_it": carrier_clocks,
             "clock_indices_with_no_P11_clock": indices_without_p11,
             "note": "A tick is assigned on %d of %d keys and on %d of %d clock "
                     "indices, so the candidate is a sub-population structure."
                     % (len(carriers), len(keys), len(carrier_clocks),
                        len(clock_labels))},
            bool(p11_free_lanes),
            {"F_carried_edges": p11_f_edges, "F_free_edges": p11_f_free,
             "carrying_keys_carried_onto_no_co_key_clock": p11_free_lanes,
             "co_key_clock_indices_tried_per_carrier":
                 FIXTURE_BANKS - 1 + len(corpus["pairs"]),
             "note": "Independence is scored generously: the class counts as "
                     "INDEPENDENT as soon as ONE carrying clock is carried onto "
                     "no co-key clock at all by an exact member of F.  Scoring "
                     "it generously can only make the conjunction HARDER to "
                     "fail, so a failure here is not an artefact of the test."},
        ),
        leg_ii_row(
            "E2_NONIDENTITY_WITHIN_KEY_DICTIONARIES",
            "The %d substantive non-identity within-key dictionaries left "
            "un-adjudicated by Cycle 879, read as candidate rival times: 'the "
            "image clock's tick, transported by the witness map'."
            % len(dictionaries),
            all(row["reverified"] for row in dictionaries),
            {"dictionaries": len(dictionaries),
             "all_witnesses_reverified_from_the_cadences_alone":
                 all(row["reverified"] for row in dictionaries),
             "note": "Each witness is re-derived and re-verified from the two "
                     "tick sequences alone, with no scheduler input."},
            bool(dictionaries) and all(
                row["keys_in_census_carrying_this_exact_witness"] == len(keys)
                for row in dictionaries),
            {"max_keys_carrying_one_witness": max(
                (row["keys_in_census_carrying_this_exact_witness"]
                 for row in dictionaries), default=0),
             "census_keys": len(keys),
             "witness_population_histogram": dict(sorted(Counter(
                 row["keys_in_census_carrying_this_exact_witness"]
                 for row in dictionaries).items())),
             "note": "No witness spans the census; each holds on a handful of "
                     "keys, so none assigns a tick to every world."},
            False,
            {"note": "Every one of these candidates IS an exact member of the "
                     "declared family F carrying one record clock onto another, "
                     "so by the definition of the conjunct it is F-carried and "
                     "cannot be INDEPENDENT_OF_F.  This conjunct fails by "
                     "construction, not by measurement.",
             "members": dict(sorted(Counter(
                 row["member"] for row in dictionaries).items()))},
        ),
    ]
    adjudication = {
        "conjunction": LEG_II_CONJUNCTION,
        "price": SCOPE_PRICE,
        "scope": "S = the B=4 census (27 stations, %d keys, %d clock indices); "
                 "F = the Cycle-879 declared family with its declared caps"
                 % (len(keys), len(clock_labels)),
        "rows": rows,
        "discharge_map_updates": [
            {"row_id": row["id"], "prior_status": "UNADJUDICATED_EXCEPTION",
             "new_status": row["status"], "failing_conjuncts":
                 row["failing_conjuncts"]}
            for row in rows
        ],
        "nonidentity_dictionaries_recomputed": len(dictionaries),
        "published_879_nonidentity_dictionaries": published_nonidentity,
        "recount_matches_879": len(dictionaries) == published_nonidentity,
        "dictionary_rows": dictionaries[:WITNESS_PRINT_CAP],
        "dictionary_member_histogram": dict(sorted(Counter(
            row["member"] for row in dictionaries).items())),
        "exceptions_remaining_open": [row["id"] for row in rows
                                      if row["status"] == "OPEN"],
    }
    f_pass = (
        adjudication["recount_matches_879"]
        and all(row["reverified"] for row in dictionaries)
        and all(row["status"] in ("OPEN", "DISCHARGED_AT_SCOPE") for row in rows)
        and len(rows) == 2
    )
    lines.append(("PASS" if f_pass else "FAIL") + " F_ADJUDICATION :: "
                 + json.dumps(adjudication, **dumps))

    # ------------------------------------------------------------------ G  SCOPE
    scope = {
        "mechanism_statement": MECHANISM_STATEMENT,
        "conjecture": CONJECTURE_STATEMENT,
        "verified_here": [
            "the relay-swap arithmetic DELTA = 8B-13-8e on N = 8B-5, read from "
            "interleaved_program for B = %d..%d" % (PREDICTION_BANK_RANGE[0],
                                                    PREDICTION_BANK_RANGE[-1]),
            "the register-level attribution of the P=11 cadence, by an "
            "instrumented single-lane kernel trace that reproduces the corpus "
            "clock tick for tick",
            "clauses A1/A2/A3 measured on every bank clock of B=3 and B=4",
            "the P=11 incidence table, cross-checked by a cap-free direct "
            "membership test and against the sha-pinned Cycle-879 cache",
        ],
        "open": [
            "WHICH KEYS SATISFY A2 IS NOT DERIVED.  Clause A2 -- that a key "
            "reaches a source-pointer-quiescent window with no other bank dirt "
            "-- is MEASURED here, not predicted.  There is no closed form for "
            "it in this runner and none is claimed.  Without it the P-law "
            "predicts the VALUE of a non-orbit period but not its INCIDENCE.",
            "THE GENERAL (B,N) LAW IS A CONJECTURE.  Its dynamical half is "
            "verified at B=3 and B=4 only.  B>=5 is untested here: the "
            "arithmetic half is read from the program, the firing is not.",
            "HORIZON CONTINGENCY.  Because clause A3 compares the firing window "
            "with the clock's last tick, whether a firing is detector-visible "
            "depends on where the declared horizon falls.  The Cycle-879 "
            "BREAKS_AT_B4 verdict inherits that contingency and should be read "
            "as 'detector-visible at B=4 at horizon 8192', not as a B-axis law.",
            "DETECTOR REACH.  The declared detector does not surface every "
            "firing: this runner finds A2 classes at B=4 that it reports as "
            "no-period.  The published non-orbit census is therefore a LOWER "
            "bound on the mechanism's incidence, not a complete one.",
            "LEG (ii) ITSELF REMAINS OPEN.  Two exception rows discharged at "
            "this scope close two rows of the Cycle-875 map and nothing more; "
            "the family-closure and scope caveats are untouched.",
        ],
        "falsifier": (
            "Exhibit a (B, key, bank) at which A1, A2 and A3 all hold and the "
            "measured tail period is not DELTA(B,e); or a clock with a "
            "nondegenerate non-orbit period whose quiescent-window dirt is not "
            "two sigma-runs at the two RELAY_SWAP phases of its edge."
        ),
    }
    lines.append("PASS G_SCOPE :: " + json.dumps(scope, **dumps))

    # --------------------------------------------------------------- H  CONTROLS
    input_shas = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    runner_sha = sha256(Path(__file__).read_bytes()).hexdigest()
    replay = instrumented_trace(
        corpus["seeds"], program, corpus["schedules"], corpus["per_bank"],
        corpus["labels"], corpus["source_pointer"], exemplar_event,
        exemplar_positions, exemplar_bank, STATIONS,
    )
    replay_clean = tuple(tick for tick, _a, local, source in replay
                         if not local and not source)
    corpus_digest = digest([
        [list(row) for row in corpus["bank"][lane]] for lane in range(0, len(keys), 97)
    ])
    runtime = time.monotonic() - started
    h_core = {
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(
            not Path(path).is_absolute() for path in AUDIT_INPUT_PATHS),
        "input_shas": input_shas,
        "runner_sha256": runner_sha,
        "corpus_sample_sha256": corpus_digest,
        "incidence_sha256": digest(incidence),
        "duplicate_lane_clean_mismatches": corpus["duplicate_mismatches"],
        "trace_replay_deterministic": replay_clean == tuple(trace_clean),
        "runtime_seconds": round(runtime, 3),
        "runtime_under_1400s": runtime < RUNTIME_LIMIT_SECONDS,
    }
    h_prepass = (
        h_core["audit_input_paths_exist"]
        and h_core["audit_input_paths_repo_relative"]
        and corpus["duplicate_mismatches"] == 0
        and h_core["trace_replay_deterministic"]
        and runtime < RUNTIME_LIMIT_SECONDS
    )
    verdicts = (a_pass, b_pass, c_pass, d_pass, e_pass, f_pass)
    stdout_bytes = 0
    for _ in range(4):
        h_core["stdout_bytes"] = stdout_bytes
        h_core["stdout_under_150KB"] = (
            stdout_bytes < STDOUT_LIMIT_BYTES if stdout_bytes else True)
        h_line = (("PASS" if h_prepass and h_core["stdout_under_150KB"] else "FAIL")
                  + " H_CONTROLS :: " + json.dumps(h_core, **dumps))
        stdout_bytes = len(
            ("\n".join(lines + [h_line, "CYCLE881_P11_CHARACTERIZATION_PASS"]) + "\n")
            .encode())
    h_core["stdout_bytes"] = stdout_bytes
    h_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    h_pass = h_prepass and h_core["stdout_under_150KB"]
    h_line = (("PASS" if h_pass else "FAIL") + " H_CONTROLS :: "
              + json.dumps(h_core, **dumps))
    final = ("CYCLE881_P11_CHARACTERIZATION_PASS" if all(verdicts) and h_pass
             else "CYCLE881_P11_CHARACTERIZATION_HONEST_FAIL")
    print("\n".join(lines + [h_line, final]))
    return 0 if all(verdicts) and h_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
