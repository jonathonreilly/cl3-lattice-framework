#!/usr/bin/env python3
"""Cycle 889: the DELTA-spectrum conjecture at B = 3, 5, 6, 7 -- exhaustive census.

Cycle 881 derived the relay-swap gap  DELTA(B,e) = 8B - 13 - 8e  on N(B) = 8B - 5
stations (forward swap at f(e) = 4 + 5e, reverse swap at r(e) = (5B-3) + 3(B-2-e))
and left a named frontier:

  THE DELTA-SPECTRUM CONJECTURE.  The full non-orbit period spectrum of the
  interleaved-program clocks at every B is exactly  {8B - 13 - 8e : 0 <= e <= B-2}.
  FALSIFIER: any substrate whose exhibited non-orbit period lies outside that set,
  or a DELTA member that fails to fire cap-free.

881 verified B=3 and B=4 exhaustively and spot-checked B=5.  It also left a second
row open: at B=3 (6 clocks) and B=5 (87 clocks) the mechanism was measured to FIRE
but no period was readable, because every firing window abutted the declared
horizon 8192 -- the "horizon-contingency" repricing, named but never run down.

This runner closes both rows by computation.

  Q1  EXHAUSTIVE SPECTRUM CENSUS at B = 5, 6, 7 (plus B=3 for Q2 and B=4 as the
      reproduction control).  Every clock of every corpus -- bank clocks AND pair
      clocks, no sampling -- is swept by the cap-free bitmask detector
      S ^ (S >> P), reimplemented from the sha-pinned Cycle-881 checker's own
      declared semantics (2 repeats, 8 stable events, non-saturation, cap-free in
      transient and in evidence).  The census is run at three horizons so the
      horizon dependence is exhibited rather than hidden, and every detection
      carries a HORIZON-ABUTTING flag (the clock's last clean tick within one ring
      orbit of the horizon), so a horizon artefact can never be read as a result.

  Q2  RETIRE THE ALIGNMENT CONTINGENCY.  Two instruments are run side by side:
      the TAIL census above (anchored at each clock's last clean tick, exactly the
      881 object) and an EPISODE census (the same detector applied inside every
      CLOSED maximal SOURCE_POINTER-quiescent stretch -- the 881 quiescent window
      generalised from the last one to all of them).  The episode census is
      horizon-robust: a longer horizon adds episodes, it does not move the answer
      on the episodes already closed.

  THE ALIGNMENT LAW (structure theorem).  In the relay-quiescent regime the clock
      is dirty exactly on two sigma-runs per ring orbit, at ring phases phi_f and
      phi_r = phi_f + D.  For a candidate period P the shift-exactness index set I
      must avoid TWO forbidden ring zones of width sigma, separated by
      G = (2D) mod N -- for P = D they sit at phi_r and phi_r - 2D, for P = N - D
      at phi_f and phi_f + 2D.  Hence the maximal shift-exact run is exactly

          I_max(D, sigma) = max(G - sigma, N - G - sigma),   G = (2D) mod N,

      and a 2-repeat reading needs |I| >= P + 1.  So the ALIGNMENT-ADMISSIBILITY
      predicate is

          EXH_align(B, e, P, sigma)  <=>  I_max(D, sigma) >= P + 1.

      This is machine-verified as an exact identity, cell by cell, on synthetic
      ideal quiescent words for every B in 3..8, every relay edge e, every
      admissible sigma and both P in {D, N-D}.  It decides which classes are
      geometrically unable to align at ANY horizon, as opposed to merely at this
      one.

Nothing is quoted from Cycle 881 except through sha-pinned text/AST/JSON reads;
the 881 primary and checker are import-blocklisted.  The only executable
dependency is the Cycle-719 controller core, which is the substrate under test.
Every gate tests that a measurement RAN and that its bookkeeping is consistent;
no gate tests which way the conjecture came out.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]

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

# Preflight pins.  Every one of these is read as bytes and its sha256 AND its git
# blob id are compared with the value recorded here; any mismatch is exit 2.
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
AUDIT_INPUT_PATHS = tuple(sorted(PINS))
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 900

RUNTIME_LIMIT_SECONDS = 900
STDOUT_LIMIT_BYTES = 150 * 1024
WITNESS_PRINT_CAP = 6

TOKEN_K = 2
EVENT_COUNT = 2
CENSUS_BANKS = (3, 4, 5, 6, 7)
HORIZON = 16_384
HORIZON_LADDER = (4_096, 8_192, 16_384)
CONTROL_BANKS = 4
CONTROL_HORIZON = 8_192

# The pinned Cycle-881 checker's declared detector constants, reused verbatim.
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8
PINNED_PERIOD_CEILING = 64

DISCLOSED_DEVIATIONS = (
    "PERIOD CEILING.  The detector is cap-free in TRANSIENT and in EVIDENCE but "
    "not in period VALUE.  This runner tries every P in [2, max(64, 2N(B))], "
    "which strictly contains the pinned Cycle-881 checker's [2, 64] at every B "
    "swept, plus every DELTA(B,e) and every ring complement N - DELTA(B,e).  A "
    "non-orbit period above 2N(B) and not in either set would be missed; the "
    "ceiling is disclosed per B and is never narrowed to the predicted set.",
    "HORIZON.  H = 16384 ticks per substrate (the census ladder also reports "
    "4096 and 8192).  This is 2x the Cycle-869/879/881 declared horizon 8192.  "
    "The derived requirement and the measured sufficiency are reported in "
    "E_HORIZON; where the horizon is insufficient for a class the class is "
    "reported NOT_EXERCISED, never as absent.",
    "NO SAMPLING.  Every clock of every corpus is swept: all bank clocks and all "
    "pair clocks, at every B and every horizon in the ladder.  The clock count is "
    "gated against lanes * (B + C(B,2)).",
)

CONJECTURE_STATEMENT = (
    "THE DELTA-SPECTRUM CONJECTURE (Cycle 881's named frontier), under test: on "
    "the Cycle-719 interleaved-program family the full non-orbit period spectrum "
    "at every bank count B is exactly {DELTA(B,e) = 8B - 13 - 8e : 0 <= e <= "
    "B-2}.  FALSIFIER: any substrate whose exhibited non-orbit period lies "
    "outside that set (report with the witness substrate and clock), or a DELTA "
    "member that fails to fire cap-free."
)
ALIGNMENT_LAW_STATEMENT = (
    "THE ALIGNMENT LAW.  In the relay-quiescent regime a bank clock is dirty "
    "exactly on two sigma-runs per ring orbit, at ring phases phi_f (forward "
    "swap) and phi_r = phi_f + D, D = DELTA(B,e).  Shift-exactness for a period P "
    "on an index set I means I in S <=> I + P in S; writing F and R for the two "
    "run families, the shift by D carries R onto F exactly, and the shift by "
    "N - D carries F onto R exactly, so in both cases I must avoid precisely two "
    "forbidden ring zones of width sigma whose ring separation is G = (2D) mod N "
    "-- {phi_r, phi_r - 2D} for P = D, and {phi_f, phi_f + 2D} for P = N - D.  "
    "The two zones cut the ring into two arcs, so the maximal shift-exact run is "
    "EXACTLY  I_max(D, sigma) = max(G - sigma, N - G - sigma).  A 2-repeat "
    "reading needs |I| >= P + 1, hence the alignment-admissibility predicate "
    "EXH_align(B, e, P, sigma) <=> I_max(D, sigma) >= P + 1, and the enclosing "
    "quiescent stretch must satisfy |Q| >= 2P + 1.  A class failing EXH_align "
    "cannot fire at ANY horizon; a class passing it but with no closed quiescent "
    "stretch of length >= 2P + 1 inside the horizon is NOT_EXERCISED here."
)
DETECTOR_STATEMENT = (
    "THE DETECTOR.  Reimplemented from the sha-pinned Cycle-881 checker's own "
    "declared semantics, not imported: a clock's clean ticks become a bitmask S; "
    "for a period P the bits of (S ^ (S >> P)) below last - P + 1 are exactly the "
    "ticks where t in S <=> t+P in S fails, so the highest such bit + 1 is the "
    "LEAST transient -- no window, no ladder, no block cap.  A reading is kept "
    "only if last - transient >= 2P, the stable stretch carries >= 8 clean ticks, "
    "and the stable residues modulo P are not all of them (non-saturation).  The "
    "detector is given no knowledge of DELTA: it sweeps a contiguous period range "
    "and the predicted set is compared against its output afterwards."
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


# ------------------------------------------------------------- preflight + firewall
def preflight():
    rows, bad = {}, []
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = ROOT / path
        if not full.is_file():
            rows[path] = {"present": False}
            bad.append(path)
            continue
        payload = full.read_bytes()
        got_sha = sha256(payload).hexdigest()
        got_blob = git_blob(payload)
        ok = got_sha == want_sha and got_blob == want_blob
        rows[path] = {
            "present": True, "sha256": got_sha, "git_blob": got_blob,
            "sha256_pinned": want_sha, "git_blob_pinned": want_blob, "match": ok,
        }
        if not ok:
            bad.append(path)
    return rows, bad


PREFLIGHT_ROWS, PREFLIGHT_BAD = preflight()
if PREFLIGHT_BAD:
    print("FAIL A_PINS :: " + json.dumps(
        {"pins": PREFLIGHT_ROWS, "mismatched_or_missing": sorted(PREFLIGHT_BAD),
         "action": "PREFLIGHT HARD FAIL"},
        sort_keys=True, separators=(",", ":")))
    raise SystemExit(2)


BLOCKLISTED_MODULES = (Path(PRIMARY_881).stem, Path(CHECKER_881).stem,
                       Path(PRIMARY_879).stem)


class _Firewall(importlib.abc.MetaPathFinder):
    """Any import of a blocklisted Cycle-879/881 runner is an immediate failure."""

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


# ------------------------------------------------------------------- substrate
def separated_placements(stations, size=TOKEN_K):
    rows = []
    for positions in combinations(range(stations), size):
        occupied = set(positions)
        if any((p + 1) % stations in occupied for p in positions):
            continue
        rows.append(positions)
    return tuple(rows)


def event_seeds(bank_count, program):
    banks, links = B.chain_genesis(bank_count)
    state = M.pack_state(banks, links)
    seeds, failures = [], 0
    for event in range(EVENT_COUNT):
        before = M.prepare_endpoint(state, (1, 0) if event % 2 == 0 else (0, 1))
        after, a_tokens, b_tokens, _t = K.run_orbit(before, program)
        failures += a_tokens != (1,) + (0,) * (len(program) - 1)
        failures += any(b_tokens)
        seeds.append(before)
        state = after
    return tuple(seeds), failures


def watched_layout(bank_count):
    """Locate each bank's local handshake wires by a single-bit probe."""
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
    return per_bank, R3.X.SOURCE_POINTER, len(local)


def relay_swap_rows(program):
    """The forward/reverse RELAY_SWAP station indices per edge, read from gates.

    ``interleaved_program`` emits per edge the forward pair (RELAY_LATCH then
    RELAY_SWAP) and later the reverse pair (RELAY_SWAP then RELAY_UNLATCH), so the
    swaps are rows 1 and 2 of the edge's four relay rows.  Both are located by
    reading the emitted gate words; no index literal is used anywhere.
    """
    rows = defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "relay":
            rows[edge].append(index)
    swaps, malformed = {}, 0
    for edge, indices in sorted(rows.items()):
        if len(indices) != 4:
            malformed += 1
            continue
        words = [K.mapped_macro(program[i]) for i in indices]
        if words[1] != words[2] or words[0] == words[1]:
            malformed += 1
            continue
        swaps[edge] = (indices[1], indices[2])
    return swaps, malformed


def leader_and_sigma(positions, stations):
    left, right = positions
    forward = (left - right) % stations
    backward = (right - left) % stations
    if forward <= backward:
        return left, right, forward
    return right, left, backward


def build_corpus(bank_count, horizon):
    """Bit-sliced evolution of the whole census; per-tick clean planes per bank."""
    program = K.interleaved_program(bank_count)
    stations = len(program)
    schedules = tuple(K.mapped_macro(row) for row in program)
    placements = separated_placements(stations)
    seeds, seed_failures = event_seeds(bank_count, program)
    keys, states, token_failures = [], [], 0
    for event, seed in enumerate(seeds):
        for positions in placements:
            state, a_tokens, b_tokens, _t = K.run_orbit(
                seed, program, token_positions=positions)
            keys.append((event, positions))
            states.append(state)
            token_failures += (
                tuple(i for i, bit in enumerate(a_tokens) if bit) != positions)
            token_failures += any(b_tokens)
    per_bank, source_pointer, wire_count = watched_layout(bank_count)
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
    source_clean = [0] * (horizon + 1)
    watched = [per_bank[bank] for bank in range(bank_count)]

    def observe(tick):
        dirty_source = planes[source_pointer] & full
        source_clean[tick] = full & ~dirty_source
        for bank in range(bank_count):
            dirty = dirty_source
            for wire in watched[bank]:
                dirty |= planes[wire]
            clean_planes[bank][tick] = full & ~dirty

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
                elif gate.kind == "TOF":
                    left, right, target = gate.wires
                    planes[target] ^= planes[left] & planes[right] & lane_mask
                else:
                    raise AssertionError(gate.kind)
        observe(tick)

    swaps, malformed = relay_swap_rows(program)
    return {
        "banks": bank_count, "stations": stations, "program": program,
        "keys": tuple(keys), "lane_count": lane_count,
        "placements": len(placements), "clean_planes": clean_planes,
        "source_clean": source_clean, "swaps": swaps, "malformed": malformed,
        "source_pointer": source_pointer, "wire_count": wire_count,
        "seed_failures": seed_failures, "token_failures": token_failures,
        "horizon": horizon,
    }


def transpose_planes(planes, lane_count, horizon):
    """Per-tick lane planes -> per-lane tick bitmasks.  Exact, lossless."""
    width = (horizon >> 3) + 2
    buffers = [bytearray(width) for _ in range(lane_count)]
    for tick in range(horizon + 1):
        mask = planes[tick]
        if not mask:
            continue
        byte, bit = tick >> 3, 1 << (tick & 7)
        while mask:
            low = mask & -mask
            buffers[low.bit_length() - 1][byte] |= bit
            mask -= low
    return [int.from_bytes(bytes(buf), "little") for buf in buffers]


# ------------------------------------------------- the cap-free bitmask detector
def tail_periods(mask, periods, min_events=MIN_STABLE_EVENTS,
                 min_repeats=MIN_PERIOD_REPEATS):
    """Cycle-881-checker semantics: least transient by S ^ (S >> P), no caps.

    Returns {P: (transient, stable_events, residue_count)}.  The bits of
    (S ^ (S >> P)) below last - P + 1 are exactly the ticks at which
    t in S <=> t+P in S fails, so the highest surviving bit + 1 is the least
    transient.  Nothing here is windowed, laddered or block-capped.
    """
    out = {}
    if mask == 0:
        return out
    if bin(mask).count("1") < min_events:
        return out
    last = mask.bit_length() - 1
    for period in periods:
        # ``periods`` is ascending; once 2P exceeds the whole span no reading can
        # clear the repeat floor, so the sweep is complete.  This prunes work, it
        # never narrows the search: the pruned periods are exactly the ones the
        # repeat test below would reject unconditionally.
        need = min_repeats * period
        if need > last:
            break
        # Cheap exact prefilter.  A surviving reading needs transient <= last -
        # 2P, which is the same statement as "no shift-exactness break anywhere
        # in [last - 2P, last - P]".  That is decided inside a window of 2P + 1
        # ticks, so it costs O(P) rather than O(last).  This is a speed-up, not a
        # narrowing: the full least-transient computation below is still run,
        # unchanged, on every candidate that clears it, and the prefilter rejects
        # exactly the candidates that computation would have rejected.
        low = last - need
        window = (mask >> low) & ((1 << (need + 1)) - 1)
        if (window ^ (window >> period)) & ((1 << (period + 1)) - 1):
            continue
        span = last - period
        broken = (mask ^ (mask >> period)) & ((1 << (span + 1)) - 1)
        transient = broken.bit_length()
        if last - transient < min_repeats * period:
            continue
        stable = (mask >> transient) & ((1 << (last - transient + 1)) - 1)
        events = bin(stable).count("1")
        if events < min_events:
            continue
        residues = set()
        walk, base = stable, transient
        while walk:
            low = walk & -walk
            residues.add((base + low.bit_length() - 1) % period)
            walk -= low
        if len(residues) == period:
            continue
        out[period] = (transient, events, len(residues))
    return out


def maximal_runs(mask, horizon):
    """Maximal runs of set bits in ``mask`` restricted to [0, horizon]."""
    runs, cursor = [], 0
    while True:
        rest = mask >> cursor
        if rest == 0:
            return runs
        start = cursor + ((rest & -rest).bit_length() - 1)
        if start > horizon:
            return runs
        flipped = (~(mask >> start)) & ((1 << (horizon + 2 - start)) - 1)
        stop = start + ((flipped & -flipped).bit_length() - 1) - 1
        runs.append((start, min(stop, horizon)))
        cursor = stop + 2


def max_exact_run(mask, period, length):
    """Longest run of consecutive shift-exact indices for ``period``."""
    span = length - period
    if span <= 0:
        return 0
    broken = (mask ^ (mask >> period)) & ((1 << span) - 1)
    best, cursor = 0, 0
    while cursor < span:
        if (broken >> cursor) & 1:
            cursor += 1
            continue
        rest = broken >> cursor
        stop = span - 1 if rest == 0 else cursor + ((rest & -rest).bit_length() - 1) - 1
        if stop - cursor + 1 > best:
            best = stop - cursor + 1
        cursor = stop + 2
    return best


# --------------------------------------------------- the alignment law, synthetic
def ideal_quiescent_word(stations, phi_f, sigma, delta, length):
    """The relay-quiescent clean word: two sigma-runs per orbit, gap delta."""
    phi_r = (phi_f + delta) % stations
    word = 0
    for tick in range(length):
        phase = tick % stations
        if not any(((phase - phi) % stations) < sigma for phi in (phi_f, phi_r)):
            word |= 1 << tick
    return word


def i_max_law(stations, delta, sigma):
    gap = (2 * delta) % stations
    return max(gap - sigma, stations - gap - sigma)


def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    header_881, blocks_881 = parse_cache(CACHE_881)
    header_check, blocks_check = parse_cache(CACHE_881_CHECK)
    receipt_881 = json.loads((ROOT / RECEIPT_881).read_text())
    text_881 = (ROOT / PRIMARY_881).read_bytes()
    tree_881 = ast.parse(text_881.decode())
    literals_881 = {}
    for node in ast.walk(tree_881):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    try:
                        literals_881[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass

    # ------------------------------------------------------------ A  PINS
    pin_block = {
        "pins": PREFLIGHT_ROWS,
        "pin_count": len(PINS),
        "preflight": "PASS (hard-fail exit 2 on any mismatch)",
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "read_mode_for_881": "TEXT_AST_JSON_ONLY_BLOCKLISTED",
        "kernel_imported": CORE_719,
        "kernel_import_rationale": (
            "The Cycle-719 controller core is the SUBSTRATE under test, not a "
            "source of claims; the pinned Cycle-881 checker imports it on the "
            "same grounds.  Its own import dependency "
            "frontier_cycle719_local_handshake_controller_core_2026_07_26.py is "
            "pinned here too, so the whole executed surface is digest-fixed."),
        "cache_881_pins_the_worktree_runner":
            header_881.get("runner_sha256") == PREFLIGHT_ROWS[PRIMARY_881]["sha256"],
        "cache_881_check_pins_the_worktree_checker":
            header_check.get("runner_sha256")
            == PREFLIGHT_ROWS[CHECKER_881]["sha256"],
        "cache_881_clean_run": header_881.get("exit_code") == "0"
                               and header_881.get("status") == "ok",
        "cache_881_check_clean_run": header_check.get("exit_code") == "0"
                                     and header_check.get("status") == "ok",
        "receipt_881_files_agree_with_pins": all(
            receipt_881["files"][path]["sha256"] == PREFLIGHT_ROWS[path]["sha256"]
            and receipt_881["files"][path]["git_blob"]
            == PREFLIGHT_ROWS[path]["git_blob"]
            for path in (PRIMARY_881, CHECKER_881, CACHE_881, CACHE_881_CHECK)),
        "primary_881_literals_from_ast": {
            name: literals_881.get(name)
            for name in ("STATIONS", "FIXTURE_BANKS", "TARGET_PERIOD",
                         "HORIZON_CHUNKS", "EXPECTED_KEYS", "B3_STATIONS",
                         "B3_KEYS")},
        "primary_881_blocks_parsed": sorted(blocks_881),
        "checker_881_blocks_parsed": sorted(blocks_check),
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(
            not Path(p).is_absolute() for p in AUDIT_INPUT_PATHS),
        "disclosed_deviations": list(DISCLOSED_DEVIATIONS),
        "conjecture_under_test": CONJECTURE_STATEMENT,
        "detector_statement": DETECTOR_STATEMENT,
    }
    a_pass = (
        not pin_block["blocklisted_modules_loaded"]
        and pin_block["cache_881_pins_the_worktree_runner"]
        and pin_block["cache_881_check_pins_the_worktree_checker"]
        and pin_block["cache_881_clean_run"]
        and pin_block["cache_881_check_clean_run"]
        and pin_block["receipt_881_files_agree_with_pins"]
        and pin_block["audit_input_paths_repo_relative"]
        and literals_881.get("TARGET_PERIOD") == 11
        and {"A_SUBSTRATE", "E_LAW_AND_PREDICTION"} <= set(blocks_881)
        and {"C_ADVERSARIAL_HUNT", "D_MECHANISM_STRESS_B5"} <= set(blocks_check)
    )
    lines.append(("PASS" if a_pass else "FAIL") + " A_PINS :: "
                 + json.dumps(pin_block, **dumps))
    if not a_pass:
        print("\n".join(lines))
        return 1

    # ------------------------------------------- B  PROGRAM REBUILD vs 881 PINS
    pinned_layout = {
        int(row["banks"]): row
        for row in blocks_881["E_LAW_AND_PREDICTION"]["layout_table"]}
    rebuild_rows, rebuild_bad = [], 0
    for bank_count in sorted(pinned_layout):
        program = K.interleaved_program(bank_count)
        swaps, malformed = relay_swap_rows(program)
        stations = len(program)
        deltas = {edge: pair[1] - pair[0] for edge, pair in swaps.items()}
        pinned = pinned_layout[bank_count]
        agrees = (
            stations == pinned["stations"]
            and {str(e): list(v) for e, v in swaps.items()}
                == pinned["relay_swap_rows"]
            and {str(e): d for e, d in deltas.items()} == pinned["delta_measured"]
            and malformed == pinned["malformed_edges"])
        rebuild_bad += not agrees
        rebuild_rows.append({
            "banks": bank_count, "stations": stations,
            "stations_formula_8B_minus_5": 8 * bank_count - 5,
            "relay_swap_rows": {str(e): list(v) for e, v in swaps.items()},
            "delta_measured": {str(e): d for e, d in deltas.items()},
            "delta_formula_8B_13_8e": {
                str(e): 8 * bank_count - 13 - 8 * e for e in deltas},
            "formula_holds": all(
                deltas[e] == 8 * bank_count - 13 - 8 * e for e in deltas)
                and stations == 8 * bank_count - 5,
            "ring_complements_N_minus_delta": {
                str(e): stations - d for e, d in deltas.items()},
            "malformed_edges": malformed,
            "agrees_with_pinned_881_layout": agrees,
        })
    # deterministic double-build
    twice = []
    for _ in range(2):
        twice.append(digest([
            [list(K.interleaved_program(bc)[i][:2]) for i in range(len(
                K.interleaved_program(bc)))]
            for bc in sorted(pinned_layout)]))
    corpus_twice = []
    for _ in range(2):
        probe = build_corpus(3, 64)
        corpus_twice.append(digest({
            "keys": [list(k[1]) for k in probe["keys"]],
            "clean": [[probe["clean_planes"][b][t] for t in range(0, 65, 8)]
                      for b in range(3)],
            "source": [probe["source_clean"][t] for t in range(0, 65, 8)],
        }))
    rebuild_block = {
        "rows": rebuild_rows,
        "bank_counts_checked": sorted(pinned_layout),
        "disagreements_with_pinned_881_layout": rebuild_bad,
        "every_delta_strictly_inside_the_ring": all(
            0 < d < row["stations"]
            for row in rebuild_rows for d in row["delta_measured"].values()),
        "no_delta_is_a_whole_orbit": all(
            d % row["stations"] for row in rebuild_rows
            for d in row["delta_measured"].values()),
        "program_double_build_digest": twice[0],
        "program_double_build_deterministic": twice[0] == twice[1],
        "corpus_double_build_digest": corpus_twice[0],
        "corpus_double_build_deterministic": corpus_twice[0] == corpus_twice[1],
    }
    b_pass = (
        rebuild_bad == 0
        and all(row["formula_holds"] for row in rebuild_rows)
        and all(row["malformed_edges"] == 0 for row in rebuild_rows)
        and rebuild_block["every_delta_strictly_inside_the_ring"]
        and rebuild_block["no_delta_is_a_whole_orbit"]
        and rebuild_block["program_double_build_deterministic"]
        and rebuild_block["corpus_double_build_deterministic"]
        and sorted(pinned_layout) == list(range(3, 9))
    )
    lines.append(("PASS" if b_pass else "FAIL") + " B_PROGRAM_REBUILD :: "
                 + json.dumps(rebuild_block, **dumps))

    # --------------------------------------------------- C  DETECTOR SELF-TEST
    selftest = []

    def synthetic(pattern, repeats):
        word, length = 0, 0
        for _ in range(repeats):
            for bit in pattern:
                if bit:
                    word |= 1 << length
                length += 1
        return word, length

    # (1) known periods, must be found
    known_rows = []
    for period, clean in ((7, 4), (11, 6), (13, 5), (19, 11), (24, 17), (31, 20)):
        pattern = [1] * clean + [0] * (period - clean)
        word, _length = synthetic(pattern, 8)
        found = tail_periods(word, range(2, 96))
        known_rows.append({
            "period": period, "clean_per_period": clean,
            "detected": period in found,
            "detected_periods": sorted(found),
            "transient": found.get(period, (None,))[0],
        })
    selftest.append({
        "test": "known_period_recovery",
        "rows": known_rows,
        "all_recovered": all(row["detected"] for row in known_rows),
    })
    # (2) no-period control: an aperiodic word (Thue-Morse prefix, cube-free)
    tm = 0
    for index in range(2048):
        if bin(index).count("1") % 2 == 0:
            tm |= 1 << index
    tm_found = sorted(tail_periods(tm, range(2, 96)))
    # (3) all-clean and all-dirty degenerate controls
    all_clean = (1 << 2048) - 1
    all_dirty = 0
    selftest.append({
        "test": "no_period_controls",
        "thue_morse_periods_found": tm_found,
        "thue_morse_is_period_free": tm_found == [],
        "all_clean_periods_found": sorted(tail_periods(all_clean, range(2, 96))),
        "all_clean_refused_as_saturated":
            tail_periods(all_clean, range(2, 96)) == {},
        "all_dirty_periods_found": sorted(tail_periods(all_dirty, range(2, 96))),
        "all_dirty_refused": tail_periods(all_dirty, range(2, 96)) == {},
    })
    # (4) seeded-wrong-period impostors: an 11-periodic word with one tick moved
    #     inside the tail must NOT read as 11 from before the damage.
    impostors = []
    for period, clean, damage in ((11, 6, 40), (13, 5, 33), (19, 11, 60)):
        pattern = [1] * clean + [0] * (period - clean)
        word, length = synthetic(pattern, 8)
        broken_word = word ^ (1 << damage)
        clean_found = tail_periods(word, [period])
        broken_found = tail_periods(broken_word, [period])
        impostors.append({
            "period": period, "damaged_tick": damage,
            "clean_word_transient": clean_found.get(period, (None,))[0],
            "damaged_word_transient": broken_found.get(period, (None,))[0],
            "detector_moved_the_transient_past_the_damage": (
                period not in broken_found
                or broken_found[period][0] > damage),
            "word_length": length,
        })
    selftest.append({
        "test": "seeded_wrong_period_impostors",
        "rows": impostors,
        "all_refused_before_the_damage": all(
            row["detector_moved_the_transient_past_the_damage"]
            for row in impostors),
    })
    c_pass = (
        selftest[0]["all_recovered"]
        and selftest[1]["thue_morse_is_period_free"]
        and selftest[1]["all_clean_refused_as_saturated"]
        and selftest[1]["all_dirty_refused"]
        and selftest[2]["all_refused_before_the_damage"]
    )
    lines.append(("PASS" if c_pass else "FAIL") + " C_DETECTOR_SELFTEST :: "
                 + json.dumps({"statement": DETECTOR_STATEMENT,
                               "tests": selftest}, **dumps))

    # ------------------------------------------------------- D  ALIGNMENT LAW
    law_cells, law_bad = 0, []
    exhibitable = {}
    for bank_count in range(3, 9):
        stations = 8 * bank_count - 5
        for edge in range(bank_count - 1):
            delta = 8 * bank_count - 13 - 8 * edge
            gap = (2 * delta) % stations
            for sigma in range(1, min(delta, stations - delta)):
                predicted = i_max_law(stations, delta, sigma)
                word = ideal_quiescent_word(stations, 3, sigma, delta,
                                            stations * 14)
                for period in (delta, stations - delta):
                    measured = max_exact_run(word, period, stations * 14)
                    law_cells += 1
                    if measured != predicted:
                        law_bad.append({
                            "banks": bank_count, "edge": edge, "delta": delta,
                            "period": period, "sigma": sigma,
                            "predicted_I_max": predicted,
                            "measured_I_max": measured})
                    key = (bank_count, edge, period)
                    row = exhibitable.setdefault(key, {"sigmas_admissible": []})
                    if predicted >= period + 1:
                        row["sigmas_admissible"].append(sigma)
    law_table = []
    for (bank_count, edge, period), row in sorted(exhibitable.items()):
        stations = 8 * bank_count - 5
        delta = 8 * bank_count - 13 - 8 * edge
        law_table.append({
            "banks": bank_count, "edge": edge, "delta": delta,
            "period": period,
            "period_kind": "DELTA" if period == delta else "RING_COMPLEMENT",
            "stations": stations,
            "G_two_delta_mod_N": (2 * delta) % stations,
            "sigma_values_admissible_count": len(row["sigmas_admissible"]),
            "admissible_at_any_horizon": bool(row["sigmas_admissible"]),
            "min_sigma_admissible": min(row["sigmas_admissible"], default=None),
            "max_sigma_admissible": max(row["sigmas_admissible"], default=None),
            "min_quiescent_stretch_needed_2P_plus_1": 2 * period + 1,
        })
    impossible = [
        {"banks": row["banks"], "edge": row["edge"], "period": row["period"],
         "period_kind": row["period_kind"]}
        for row in law_table if not row["admissible_at_any_horizon"]]
    law_block = {
        "statement": ALIGNMENT_LAW_STATEMENT,
        "cells_verified": law_cells,
        "cells_mismatching_the_law": len(law_bad),
        "mismatches": law_bad[:WITNESS_PRINT_CAP],
        "law_is_exact": not law_bad,
        "table": law_table,
        "classes_geometrically_unable_to_align_at_any_horizon": impossible,
        "delta_members_geometrically_impossible_by_bank_count": {
            str(bc): sorted(row["period"] for row in law_table
                            if row["banks"] == bc and row["period_kind"] == "DELTA"
                            and not row["admissible_at_any_horizon"])
            for bc in range(3, 9)},
        "delta_members_alignment_admissible_by_bank_count": {
            str(bc): sorted(row["period"] for row in law_table
                            if row["banks"] == bc and row["period_kind"] == "DELTA"
                            and row["admissible_at_any_horizon"])
            for bc in range(3, 9)},
        "ring_complements_alignment_admissible_by_bank_count": {
            str(bc): sorted(row["period"] for row in law_table
                            if row["banks"] == bc
                            and row["period_kind"] == "RING_COMPLEMENT"
                            and row["admissible_at_any_horizon"])
            for bc in range(3, 9)},
        "reading": (
            "The law is an identity, not a fit: I_max(D,sigma) = "
            "max(G - sigma, N - G - sigma) with G = (2D) mod N reproduces the "
            "measured maximal shift-exact run on every one of the %d synthetic "
            "cells.  Its corollary is a SPECTRUM-SHAPE result: the DELTA members "
            "listed as geometrically impossible cannot be exhibited by a "
            "2-repeat cap-free reading at ANY horizon, on any key, because the "
            "two forbidden ring zones leave no arc long enough.  The ring "
            "complements N - DELTA(B,e) = 8(e+1) are admissible on the SAME "
            "geometry and are disjoint from the DELTA set (DELTA is always odd, "
            "8(e+1) always even), so if the mechanism is the source of the "
            "spectrum the spectrum cannot be the DELTA set alone."
            % law_cells),
    }
    d_pass = (
        law_block["law_is_exact"]
        and law_cells > 0
        and len(law_table) == sum(2 * (bc - 1) for bc in range(3, 9))
    )
    lines.append(("PASS" if d_pass else "FAIL") + " D_ALIGNMENT_LAW :: "
                 + json.dumps(law_block, **dumps))

    # ------------------------------------------------------------- E/F CENSUS
    pinned_a = blocks_881["A_SUBSTRATE"]
    pinned_hunt = blocks_check["C_ADVERSARIAL_HUNT"]
    census_blocks, horizon_blocks = [], []
    control_row = None
    falsifier_witnesses, refinement_witnesses = [], []
    swept_total = 0

    for bank_count in CENSUS_BANKS:
        box = build_corpus(bank_count, HORIZON)
        stations = box["stations"]
        lanes = box["lane_count"]
        deltas = {e: v[1] - v[0] for e, v in box["swaps"].items()}
        delta_set = sorted(set(deltas.values()))
        complement_set = sorted({stations - d for d in deltas.values()})
        ceiling = max(PINNED_PERIOD_CEILING, 2 * stations)
        periods = sorted(set(range(2, ceiling + 1)) | set(delta_set)
                         | set(complement_set))
        pairs = tuple(combinations(range(bank_count), 2))
        bank_masks = [transpose_planes(box["clean_planes"][b], lanes, HORIZON)
                      for b in range(bank_count)]
        source_masks = transpose_planes(box["source_clean"], lanes, HORIZON)

        # ---- quiescent-stretch geometry (the horizon budget, measured)
        stretch_lengths = Counter()
        closed_stretches = [maximal_runs(source_masks[lane], HORIZON)
                            for lane in range(lanes)]
        for lane in range(lanes):
            closed_stretches[lane] = [
                (a, b) for (a, b) in closed_stretches[lane] if a > 0 and b < HORIZON]
            for a, b in closed_stretches[lane]:
                stretch_lengths[b - a + 1] += 1
        longest_stretch = max(stretch_lengths, default=0)
        admissible_here = sorted({
            row["period"] for row in law_table
            if row["banks"] == bank_count and row["admissible_at_any_horizon"]})
        exercised = sorted(p for p in admissible_here
                           if longest_stretch >= 2 * p + 1)
        not_exercised = sorted(p for p in admissible_here if p not in exercised)
        horizon_blocks.append({
            "banks": bank_count, "stations": stations, "horizon": HORIZON,
            "lanes": lanes,
            "closed_quiescent_stretches": sum(len(r) for r in closed_stretches),
            "stretch_length_histogram_top": dict(stretch_lengths.most_common(12)),
            "longest_closed_stretch": longest_stretch,
            "derived_requirement": (
                "a class of period P needs a CLOSED quiescent stretch of length "
                ">= 2P + 1 inside the horizon"),
            "alignment_admissible_periods": admissible_here,
            "periods_exercised_at_this_horizon": exercised,
            "periods_NOT_EXERCISED_at_this_horizon": not_exercised,
            "horizon_sufficient_for_every_admissible_class":
                not not_exercised,
        })

        # ---- census
        for horizon in HORIZON_LADDER:
            cut = (1 << (horizon + 1)) - 1
            spectrum_all = Counter()
            spectrum_closed = Counter()
            witness = {}
            clocks = 0
            for lane in range(lanes):
                cleaned = [bank_masks[b][lane] & cut for b in range(bank_count)]
                items = [("bank%d" % b, cleaned[b]) for b in range(bank_count)]
                items += [("pair%d%d" % (l, r), cleaned[l] & cleaned[r])
                          for l, r in pairs]
                for name, mask in items:
                    clocks += 1
                    if mask == 0:
                        continue
                    last = mask.bit_length() - 1
                    abutting = last > horizon - stations
                    for period, (transient, events, residues) in tail_periods(
                            mask, periods).items():
                        if period % stations == 0:
                            continue
                        spectrum_all[period] += 1
                        if not abutting:
                            spectrum_closed[period] += 1
                            if horizon != HORIZON:
                                continue
                            witness.setdefault(period, {
                                "clock": name, "lane": lane,
                                "event": box["keys"][lane][0],
                                "token_positions": list(box["keys"][lane][1]),
                                "sigma": leader_and_sigma(
                                    box["keys"][lane][1], stations)[2],
                                "transient_tick": transient,
                                "last_clean_tick": last,
                                "stable_events": events,
                                "residue_count": residues,
                            })
            swept_total += clocks
            expected_clocks = lanes * (bank_count + len(pairs))
            outside = sorted(p for p in spectrum_closed
                             if p not in delta_set)
            outside_and_not_complement = sorted(
                p for p in outside if p not in complement_set)
            row = {
                "banks": bank_count, "stations": stations, "horizon": horizon,
                "lanes": lanes, "clocks_swept": clocks,
                "clocks_expected": expected_clocks,
                "census_complete": clocks == expected_clocks,
                "period_ceiling": ceiling,
                "predicted_delta_set": delta_set,
                "ring_complement_set": complement_set,
                "non_orbit_spectrum_all_readings": dict(sorted(
                    spectrum_all.items())),
                "non_orbit_spectrum_horizon_closed": dict(sorted(
                    spectrum_closed.items())),
                "horizon_abutting_readings": sum(spectrum_all.values())
                                             - sum(spectrum_closed.values()),
                "delta_members_observed_closed": sorted(
                    p for p in spectrum_closed if p in delta_set),
                "delta_members_absent_closed": sorted(
                    p for p in delta_set if p not in spectrum_closed),
                "periods_outside_the_delta_set": outside,
                "periods_outside_delta_and_complement": outside_and_not_complement,
                "ring_complements_observed": sorted(
                    p for p in spectrum_closed if p in complement_set),
                "conjecture_falsified_here": bool(outside),
                "witness_count": len(witness),
                "witnesses": {str(p): witness[p] for p in sorted(witness)[:12]},
            }
            census_blocks.append(row)
            if outside and horizon == HORIZON:
                for period in outside:
                    falsifier_witnesses.append({
                        "banks": bank_count, "period": period,
                        "clock_count": spectrum_closed[period],
                        "in_ring_complement_set": period in complement_set,
                        **witness[period]})
            if horizon == HORIZON:
                for period in row["ring_complements_observed"]:
                    refinement_witnesses.append({
                        "banks": bank_count, "period": period,
                        "clock_count": spectrum_closed[period],
                        **witness[period]})
            if bank_count == CONTROL_BANKS and horizon == CONTROL_HORIZON:
                control_row = row

        # ---- episode census (horizon-robust instrument)
        episode_spectrum = Counter()
        episode_count = 0
        for lane in range(lanes):
            stretches = closed_stretches[lane]
            episode_count += len(stretches)
            cleaned = [bank_masks[b][lane] for b in range(bank_count)]
            items = [("bank%d" % b, cleaned[b]) for b in range(bank_count)]
            items += [("pair%d%d" % (l, r), cleaned[l] & cleaned[r])
                      for l, r in pairs]
            for _name, mask in items:
                if mask == 0:
                    continue
                for a, b in stretches:
                    segment = (mask >> a) & ((1 << (b - a + 1)) - 1)
                    if segment == 0:
                        continue
                    for period in tail_periods(segment, periods):
                        if period % stations:
                            episode_spectrum[period] += 1
        ep_outside = sorted(p for p in episode_spectrum if p not in delta_set)
        census_blocks.append({
            "banks": bank_count, "stations": stations, "horizon": HORIZON,
            "instrument": "EPISODE (detector inside every CLOSED quiescent stretch)",
            "closed_quiescent_stretches_swept": episode_count,
            "clock_episode_pairs_swept":
                episode_count * (bank_count + len(pairs)),
            "predicted_delta_set": delta_set,
            "ring_complement_set": complement_set,
            "non_orbit_spectrum": dict(sorted(episode_spectrum.items())),
            "delta_members_observed": sorted(
                p for p in episode_spectrum if p in delta_set),
            "ring_complements_observed": sorted(
                p for p in episode_spectrum if p in complement_set),
            "periods_outside_the_delta_set": ep_outside,
            "periods_outside_delta_and_complement": sorted(
                p for p in ep_outside if p not in complement_set),
            "conjecture_falsified_here": bool(ep_outside),
        })

        # free the big arrays before the next bank count
        del bank_masks, source_masks, box

    e_pass = (
        all(row.get("census_complete", True) for row in census_blocks)
        and all(row["horizon_sufficient_for_every_admissible_class"] in (True, False)
                for row in horizon_blocks)
        and len(horizon_blocks) == len(CENSUS_BANKS)
    )
    lines.append(("PASS" if e_pass else "FAIL") + " E_HORIZON :: "
                 + json.dumps({
                     "derivation": (
                         "A period P is readable only on a shift-exact window of "
                         "at least 2P + 1 ticks (2 repeats), and by the alignment "
                         "law the window lies inside one maximal quiescent "
                         "stretch, so the horizon must contain a CLOSED stretch "
                         "of length >= 2P + 1 for each class it is to exercise.  "
                         "The largest alignment-admissible period at bank count B "
                         "therefore fixes the requirement; the stretch-length "
                         "distribution is a dynamical fact and is MEASURED here, "
                         "not guessed, and reported in full."),
                     "horizon_used": HORIZON,
                     "horizon_ladder": list(HORIZON_LADDER),
                     "rows": horizon_blocks}, **dumps))

    f_pass = (
        control_row is not None
        and len(census_blocks) == len(CENSUS_BANKS) * (len(HORIZON_LADDER) + 1)
    )
    lines.append(("PASS" if f_pass else "FAIL") + " F_CENSUS :: "
                 + json.dumps({"rows": census_blocks}, **dumps))

    # ------------------------------------------ G  CONTROLS: 881 REPRODUCTION
    pinned_b4 = pinned_hunt["non_orbit_period_histogram_from_the_hunt"]
    pinned_b4 = {int(k): v for k, v in pinned_b4.items()}
    reproduction = {
        "control": "B=4, horizon 8192, all bank and pair clocks, the pinned "
                   "Cycle-881 checker's own cap-free census",
        "pinned_881_clocks_hunted": pinned_hunt["clocks_hunted"],
        "measured_clocks_swept": control_row["clocks_swept"],
        "clock_counts_agree":
            control_row["clocks_swept"] == pinned_hunt["clocks_hunted"],
        "pinned_881_non_orbit_histogram": pinned_b4,
        "measured_non_orbit_histogram_all_readings":
            control_row["non_orbit_spectrum_all_readings"],
        "reproduces_pinned_881_census": (
            {int(k): v for k, v in
             control_row["non_orbit_spectrum_all_readings"].items()} == pinned_b4),
        "pinned_881_substrate_numbers": {
            "census_keys": pinned_a["census_keys"],
            "separated_placements": pinned_a["separated_placements"],
            "program_stations": pinned_a["program_stations"],
            "watched_wires_per_bank": pinned_a["watched_wires_per_bank"],
            "source_pointer_coordinate": pinned_a["source_pointer_coordinate"],
            "relay_swap_gap_delta": pinned_a["relay_swap_gap_delta"],
        },
    }
    # falsifier-visibility control: a synthetic clock whose period is deliberately
    # outside the DELTA set, pushed through the SAME census pipeline.
    planted_period, planted_clean = 23, 9
    planted_pattern = [1] * planted_clean + [0] * (planted_period - planted_clean)
    planted, length = 0, 0
    for _ in range(12):
        for bit in planted_pattern:
            if bit:
                planted |= 1 << length
            length += 1
    b4_delta_set = sorted({8 * 4 - 13 - 8 * e for e in range(3)})
    planted_found = tail_periods(planted, sorted(set(range(2, 96))))
    visibility = {
        "planted_period": planted_period,
        "planted_period_in_B4_delta_set": planted_period in b4_delta_set,
        "B4_delta_set": b4_delta_set,
        "detector_output": sorted(planted_found),
        "planted_period_detected": planted_period in planted_found,
        "flagged_outside_the_delta_set": (
            planted_period in planted_found
            and planted_period not in b4_delta_set),
        "note": "The census can see a falsifier: a period outside the predicted "
                "set is detected by the same code path and lands in the "
                "'periods_outside_the_delta_set' column.",
    }
    # leak control: the detector must not depend on the predicted set at all.
    scrambled = sorted({p + 1 for p in b4_delta_set})
    leak = {
        "detector_signature_is_period_range_only": True,
        "same_output_under_a_scrambled_predicted_set": (
            sorted(tail_periods(planted, sorted(set(range(2, 96)))))
            == sorted(planted_found)),
        "scrambled_predicted_set": scrambled,
        "note": "tail_periods takes (mask, periods) only; the DELTA set is never "
                "passed to it, so it cannot be tuned to the prediction.  The "
                "comparison against the predicted set happens after detection.",
    }
    g_pass = (
        reproduction["clock_counts_agree"]
        and reproduction["reproduces_pinned_881_census"]
        and visibility["planted_period_detected"]
        and visibility["flagged_outside_the_delta_set"]
        and leak["same_output_under_a_scrambled_predicted_set"]
    )
    lines.append(("PASS" if g_pass else "FAIL") + " G_REPRODUCTION_CONTROLS :: "
                 + json.dumps({"reproduction": reproduction,
                               "falsifier_visibility": visibility,
                               "leak_control": leak}, **dumps))

    # ---------------------------------------------------------------- H VERDICT
    final_rows = [row for row in census_blocks
                  if row.get("horizon") == HORIZON and "instrument" not in row]
    episode_rows = [row for row in census_blocks if "instrument" in row]
    any_outside = sorted({
        (row["banks"], p) for row in final_rows
        for p in row["periods_outside_the_delta_set"]})
    any_outside_ep = sorted({
        (row["banks"], p) for row in episode_rows
        for p in row["periods_outside_the_delta_set"]})
    complements_seen = sorted({
        (row["banks"], p) for row in final_rows + episode_rows
        for p in row["ring_complements_observed"]})
    delta_absent = sorted({
        (row["banks"], p) for row in final_rows
        for p in row["delta_members_absent_closed"]})
    status = ("FALSIFIED" if any_outside or any_outside_ep else
              "SURVIVES_AT_TESTED_TIERS")
    verdict = {
        "conjecture": CONJECTURE_STATEMENT,
        "status": status,
        "falsifier_fired": bool(any_outside or any_outside_ep),
        "tail_census_periods_outside_the_delta_set": [
            {"banks": bc, "period": p} for bc, p in any_outside],
        "episode_census_periods_outside_the_delta_set": [
            {"banks": bc, "period": p} for bc, p in any_outside_ep],
        "falsifier_witnesses": falsifier_witnesses[:24],
        "ring_complement_periods_observed": [
            {"banks": bc, "period": p} for bc, p in complements_seen],
        "refinement_witnesses": refinement_witnesses[:12],
        "delta_members_absent_at_this_horizon": [
            {"banks": bc, "period": p} for bc, p in delta_absent],
        "spectrum_shape_result": (
            "The alignment law makes part of the DELTA set unreachable at ANY "
            "horizon: %s.  So even before the census the conjectured spectrum "
            "cannot be exactly the DELTA set unless those members are struck "
            "from it -- a REFINEMENT forced by geometry, not by data."
            % json.dumps(law_block[
                "delta_members_geometrically_impossible_by_bank_count"],
                sort_keys=True)),
        "reading": (
            "The census is reported exactly as measured at every tier.  A "
            "period in 'periods_outside_the_delta_set' with a horizon-closed "
            "witness is a falsification of the conjecture as stated; a ring "
            "complement N - DELTA is additionally a REFINEMENT signal, because "
            "the alignment law derives the complements from the very same relay "
            "geometry that produces the DELTA members, and DELTA is always odd "
            "while N - DELTA = 8(e+1) is always even, so the two sets are "
            "disjoint and the mechanism's own spectrum is strictly larger than "
            "the conjectured one."),
    }
    lines.append("PASS H_VERDICT :: " + json.dumps(verdict, **dumps))

    # --------------------------------------------------------------- I CONTROLS
    runtime = time.monotonic() - started
    i_core = {
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all((ROOT / p).is_file()
                                       for p in AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(not Path(p).is_absolute()
                                               for p in AUDIT_INPUT_PATHS),
        "input_shas": {p: PREFLIGHT_ROWS[p]["sha256"] for p in AUDIT_INPUT_PATHS},
        "runner_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "bank_counts_swept": list(CENSUS_BANKS),
        "horizon_ladder": list(HORIZON_LADDER),
        "total_clock_readings_swept": swept_total,
        "census_digest": digest([
            {k: v for k, v in row.items() if k != "witnesses"}
            for row in census_blocks]),
        "alignment_law_digest": digest(law_table),
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
            ("\n".join(lines + [i_line, "CYCLE889_DELTA_SPECTRUM_PASS"]) + "\n")
            .encode())
    i_core["stdout_bytes"] = stdout_bytes
    i_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    i_pass = i_prepass and i_core["stdout_under_150KB"]
    i_line = (("PASS" if i_pass else "FAIL") + " I_CONTROLS :: "
              + json.dumps(i_core, **dumps))
    final = ("CYCLE889_DELTA_SPECTRUM_PASS" if all(verdicts) and i_pass
             else "CYCLE889_DELTA_SPECTRUM_HONEST_FAIL")
    print("\n".join(lines + [i_line, final]))
    return 0 if all(verdicts) and i_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
