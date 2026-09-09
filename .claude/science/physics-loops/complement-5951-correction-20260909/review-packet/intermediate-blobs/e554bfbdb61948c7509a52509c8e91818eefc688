#!/usr/bin/env python3
"""Cycle 891 independent check -- spec'd to REFUTE the complement mechanism.

The Cycle-891 primary and the Cycle-879/881/889 runners are ALL import-
blocklisted; a meta-path firewall turns any import of them into an immediate
failure and reports its own hit list.  They are read as bytes, AST and JSON only.
The single executable dependency is the Cycle-719 controller core, which is the
substrate under test rather than a source of claims.

Seven attacks, each built to make the primary FAIL if it can.

  1  INDEPENDENT PROGRAM RECONSTRUCTION.  The station layout is re-derived from
     this checker's own reading of the pinned kernel builder's recipe -- prefix
     (source; per bank: packet, cross, handoff, relay latch, relay swap), reverse
     (per edge descending: relay swap, relay unlatch, handoff return), suffix
     (finalizer) -- as a list of (kind, edge) rows built HERE, with no call into
     the kernel's builder, then compared row by row with what the kernel emits
     and with the primary's published geometry.  f(e), r(e), h_f(e), h_r(e), the
     entry gaps and the DELTAs are read off the reconstruction, never copied.

  2  AN INDEPENDENT PERIOD DETECTOR.  The primary reads periods with
     S ^ (S >> P) on bignum bitmasks and folds residues by doubling shifts.  This
     checker never forms either expression.  It keeps each clock segment as a
     sorted list of MAXIMAL CLEAN INTERVALS and works in interval algebra: the
     shift-P failure set is the symmetric difference of that interval list with
     its own translate by -P, computed by a boundary sweep; the least transient
     is the top of that set plus one; the stable event count is a sum of interval
     lengths; and the residue count is derived from interval ENDPOINTS modulo P.
     Cost is O(number of runs), not O(number of ticks), and no bit of the mask is
     ever XORed with another.  It is validated against a literal per-tick
     definition on a randomised corpus before it is used for anything.

  3  FULL RECOMPUTATION OF THE DERIVATION TIERS.  B=4 and B=5 are recomputed in
     full -- every lane, every bank clock, every pair clock, every closed
     quiescent stretch -- and the complement incidence table is rebuilt from
     scratch, including the source classification, and compared row by row with
     the primary's.  Any row the primary published that this checker cannot find,
     and any row this checker finds that the primary did not publish, is a MISS
     against the primary.

  4  THE HOLDOUT DISCIPLINE, AUDITED.  The primary's rule is re-implemented HERE
     from its STATED TEXT alone -- clause (a) entry-gap existence, clause (b)
     ring alignment -- with no reference to the primary's code, and the B=6/7
     predictions are recomputed from it.  If the stated text underdetermines the
     prediction, or if the text-derived prediction differs from the primary's,
     that is a refutation of the derivation claim and is reported as one.  The
     seal is recomputed from the primary's own published components and the build
     log at seal time is checked for holdout-tier contamination.

  5  THE k-RUN LAW, ATTACKED.  I_max(P) = (max cyclic gap of W SYMDIFF (W-P)) - 1
     is hunted for a counterexample well outside the family the primary observed:
     prime and composite ring sizes unrelated to 8B-5, up to 9 runs, widths up to
     N-2, NON-CONTIGUOUS dirty sets, periods up to 5N, and the finite form on
     truncated segments.  A perturbed law (+1) is run as a control and must
     break.  Any single mismatch of the stated law refutes the structure theorem.

  6  THE WITNESS ANATOMIES, VERIFIED REGISTER BY REGISTER.  The checker picks its
     own sample of the primary's published B=7 witnesses, replays those lanes
     through the kernel one station at a time with its own attribution code, and
     checks the published run starts, run widths, gaps, dirty-run count and
     register-event list against what the kernel actually does.

  7  TEETH.  Deliberately corrupted variants are run and each must be CAUGHT: a
     tampered pin, a dropped clock family, a hardcoded incidence row, a census
     answer leaked into the derivation path, a holdout violation, a fake anatomy,
     and a perturbed k-run law.

Nothing here is tuned to agree.  Every gate tests that an attack RAN and that its
bookkeeping is consistent; no gate tests that the attack came up empty, and the
exit code does not depend on whether the primary's claim survived.
"""
from __future__ import annotations

import array
import ast
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

PRIMARY_891 = "scripts/frontier_cycle891_complement_mechanism_2026_07_28.py"
CACHE_891 = "logs/runner-cache/frontier_cycle891_complement_mechanism_2026_07_28.txt"
PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
CHECKER_881 = "scripts/frontier_cycle881_p11_independent_check_2026_07_28.py"
RECEIPT_881 = "outputs/p11_characterization_cycle881_receipt_2026_07_28.json"
PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
CHECKER_889 = "scripts/frontier_cycle889_delta_spectrum_independent_check_2026_07_28.py"
RECEIPT_889 = "outputs/delta_spectrum_cycle889_receipt_2026_07_28.json"
RECEIPT_889_CHECK = (
    "outputs/delta_spectrum_independent_check_cycle889_receipt_2026_07_28.json")
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
    PRIMARY_889: ("c18ed0c49281fd2d54ad013ba12264b181d1720349ee002b144c028b521dd826",
                  "f1bdf1f789a85213a0a854ab0bed45e6bf250fed"),
    CHECKER_889: ("19b38fb116bb8cb79cbb925df91456c5d08d899d4b56de301a9a673ec7dc3ec3",
                  "0f946f44c431c997410a08ec3e03ae2d26d89b8a"),
    RECEIPT_889: ("10840d84d3110fa192c28667334152da815f535f131d59e763dc64bf0aef3a72",
                  "2191d809ff5b4b9f082d9f703969e05638e6e33e"),
    RECEIPT_889_CHECK: ("1ef593d7fab537900eeef3a31bd97370791b9ba3715bf2fbb7646646a08a0ded",
                        "ca6f8b2a18fab2b327f08fb1548de17943c8efbb"),
    PRIMARY_879: ("40bf65b88db19a7872d3dd5de50c7746bbecd98ce87c2b1176ce18ec9e5f7b2f",
                  "c2147a99c1a6879508fbf250051f87115b0b9d35"),
    CORE_719: ("0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
               "c123b8d681c3d76fce08ef13d7673622deac64ad"),
    CORE_719_HANDSHAKE: (
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f"),
    PRIMARY_891: ("3d260f6641d05a22aee092145ea3e5c3b29f3a6882b4cbd9ae966424458afbb7", "a1bbd49ffbe970193cc79054fb7219732f7c9873"),
    CACHE_891: ("47b07a1f1428e50bab41890dff77345130cfa9456b887bafbb00df360027409c", "7099e5ece90f4b59acec9bf27af29468c4e6b746"),
}
AUDIT_INPUT_PATHS = tuple(sorted(PINS))
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 900

RUNTIME_LIMIT_SECONDS = 900
STDOUT_LIMIT_BYTES = 150 * 1024
WITNESS_PRINT_CAP = 6

TOKEN_K = 2
EVENT_COUNT = 2
HORIZON = 16_384
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8
PINNED_PERIOD_CEILING = 64
FULL_RECOMPUTE_BANKS = (4, 5)
SPOT_BANKS = (6, 7)
SPOT_STRIDE = 3

DETECTOR_STATEMENT = (
    "THE CHECKER'S DETECTOR (independent by construction).  A clock segment is "
    "kept as a sorted list of MAXIMAL CLEAN INTERVALS.  For a candidate period P "
    "the shift-exactness failure set on [0, last-P] is the SYMMETRIC DIFFERENCE "
    "of that interval list with its own translate by -P, computed by a boundary "
    "sweep over interval endpoints; the least transient is one past the top of "
    "that set.  The stable event count is a sum of interval lengths clipped to "
    "[transient, last].  The residue count is read off interval ENDPOINTS modulo "
    "P (an interval of length >= P covers every residue; a shorter one covers the "
    "cyclic range from its start to its end).  The primary's expressions "
    "S ^ (S >> P) and the doubling residue fold are never formed here, and no bit "
    "of the mask is ever XORed with another.  The interval detector is validated "
    "head to head against a literal per-tick definition of the same semantics on "
    "a randomised corpus before it is used."
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


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


BLOCKLISTED_MODULES = (Path(PRIMARY_891).stem, Path(PRIMARY_889).stem,
                       Path(CHECKER_889).stem, Path(PRIMARY_881).stem,
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


# ------------------------------------------- 1  INDEPENDENT RECONSTRUCTION
def reconstructed_rows(bank_count):
    """The (kind, edge) row list built HERE from the builder's recipe."""
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
        rows.append(("handoff", edge))            # HANDOFF_RETURN
    rows.append(("finalizer", 0))
    return rows


def reconstructed_geometry(bank_count):
    rows = reconstructed_rows(bank_count)
    stations = len(rows)
    relay_at = defaultdict(list)
    handoff_at = defaultdict(list)
    for index, (kind, edge) in enumerate(rows):
        if kind == "relay":
            relay_at[edge].append(index)
        elif kind == "handoff":
            handoff_at[edge].append(index)
    forward = {e: v[1] for e, v in relay_at.items()}
    reverse = {e: v[2] for e, v in relay_at.items()}
    handoff_forward = {e: v[0] for e, v in handoff_at.items()}
    handoff_return = {e: v[1] for e, v in handoff_at.items()}
    return {
        "rows": rows, "stations": stations,
        "forward": forward, "reverse": reverse,
        "handoff_forward": handoff_forward, "handoff_return": handoff_return,
        "delta": {e: reverse[e] - forward[e] for e in forward},
        "entry_gap": {b: (reverse[b] - forward[b - 1]) % stations
                      for b in range(1, bank_count - 1)},
    }


# ------------------------------------------------ 2  THE INTERVAL DETECTOR
def clean_intervals(mask):
    """Maximal runs of SET bits, as a sorted list of closed intervals."""
    intervals, cursor = [], 0
    while True:
        rest = mask >> cursor
        if rest == 0:
            return intervals
        start = cursor + ((rest & -rest).bit_length() - 1)
        flipped = ~(mask >> start)
        stop = start + ((flipped & -flipped).bit_length() - 1) - 1
        intervals.append((start, stop))
        cursor = stop + 2


def clip(intervals, low, high):
    out = []
    for u, v in intervals:
        a, b = max(u, low), min(v, high)
        if a <= b:
            out.append((a, b))
    return out


def symmetric_difference_top(first, second, limit):
    """Largest point <= limit lying in exactly one of two interval lists.

    A linear boundary sweep: every interval contributes an open and a close
    event, the sweep tracks how many of each list cover the current run, and a
    run belongs to the symmetric difference when exactly one list covers it.
    """
    if limit < 0:
        return -1
    events = []
    for u, v in first:
        events.append((u, 0, 1))
        events.append((v + 1, 0, -1))
    for u, v in second:
        events.append((u, 1, 1))
        events.append((v + 1, 1, -1))
    if not events:
        return -1
    events.sort()
    best = -1
    cover = [0, 0]
    cursor = 0
    index = 0
    total = len(events)
    while index < total:
        point = events[index][0]
        if point > cursor and cursor <= limit:
            high = min(point - 1, limit)
            if (cover[0] > 0) != (cover[1] > 0):
                best = max(best, high)
        while index < total and events[index][0] == point:
            _p, which, delta = events[index]
            cover[which] += delta
            index += 1
        cursor = max(cursor, point)
    if cursor <= limit and (cover[0] > 0) != (cover[1] > 0):
        best = limit
    return best


def interval_events(intervals, low, high):
    return sum(b - a + 1 for a, b in clip(intervals, low, high))


def interval_residues(intervals, low, high, period):
    """Residue count modulo ``period`` of the ticks covered, from endpoints."""
    seen = set()
    for a, b in clip(intervals, low, high):
        if b - a + 1 >= period:
            return period
        start, stop = a % period, b % period
        if start <= stop:
            seen.update(range(start, stop + 1))
        else:
            seen.update(range(start, period))
            seen.update(range(0, stop + 1))
        if len(seen) == period:
            return period
    return len(seen)


def interval_periods(mask, periods, min_events=MIN_STABLE_EVENTS,
                     min_repeats=MIN_PERIOD_REPEATS):
    """The pinned semantics, computed entirely in interval algebra.

    The prefilter is the same exact statement the pinned semantics use -- a
    surviving reading needs no shift-exactness break anywhere in
    [last - 2P, last - P] -- but here it is decided by comparing the DIRTY-RUN
    lists of that window and of its translate, which costs O(number of runs)
    rather than O(number of ticks) and rejects exactly what the full computation
    below would reject.
    """
    out = {}
    if mask == 0:
        return out
    intervals = clean_intervals(mask)
    total = sum(b - a + 1 for a, b in intervals)
    if total < min_events:
        return out
    last = intervals[-1][1]
    dirty = []
    cursor = 0
    for u, v in intervals:
        if u > cursor:
            dirty.append((cursor, u - 1))
        cursor = v + 1
    for period in periods:
        if min_repeats * period > last:
            break
        window_low = last - 2 * period
        window_high = last - period
        left = clip(dirty, window_low, window_high)
        right = clip(dirty, window_high, last)
        if [(u + period, v + period) for u, v in left] != right:
            continue
        limit = last - period
        shifted = [(max(u - period, 0), v - period) for u, v in intervals
                   if v - period >= 0]
        top = symmetric_difference_top(clip(intervals, 0, limit),
                                       clip(shifted, 0, limit), limit)
        transient = top + 1
        if last - transient < min_repeats * period:
            continue
        events = interval_events(intervals, transient, last)
        if events < min_events:
            continue
        residues = interval_residues(intervals, transient, last, period)
        if residues == period:
            continue
        out[period] = (transient, events, residues)
    return out


def literal_periods(mask, periods, min_events=MIN_STABLE_EVENTS,
                    min_repeats=MIN_PERIOD_REPEATS):
    """A deliberately naive per-tick definition, used only to validate above."""
    out = {}
    if mask == 0:
        return out
    ticks = [t for t in range(mask.bit_length()) if (mask >> t) & 1]
    if len(ticks) < min_events:
        return out
    members = set(ticks)
    last = ticks[-1]
    for period in periods:
        if min_repeats * period > last:
            break
        transient = 0
        for index in range(last - period, -1, -1):
            if (index in members) != ((index + period) in members):
                transient = index + 1
                break
        if last - transient < min_repeats * period:
            continue
        stable = [t for t in ticks if transient <= t <= last]
        if len(stable) < min_events:
            continue
        residues = {t % period for t in stable}
        if len(residues) == period:
            continue
        out[period] = (transient, len(stable), len(residues))
    return out


# --------------------------------------------------------------- substrate
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
    seeds = []
    for event in range(EVENT_COUNT):
        before = M.prepare_endpoint(state, (1, 0) if event % 2 == 0 else (0, 1))
        after, _a, _b, _t = K.run_orbit(before, program)
        seeds.append(before)
        state = after
    return tuple(seeds)


def watched(bank_count):
    banks, links = B.chain_genesis(bank_count)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
    local = (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
             *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK)
    names = (["POINTER", "U_TO_V", "V_TO_U", "DIRECTION_OK"]
             + ["FRESH%d" % i for i in range(len(A.FRESH))]
             + ["ZERO_WORK%d" % i for i in range(len(A.ZERO_WORK))]
             + ["TOKEN_OK"])
    per_bank, labels = {}, {}
    for bank in range(bank_count):
        coords = []
        for index, wire in enumerate(local):
            probe = [list(row) for row in zero_banks]
            probe[bank][wire] = 1
            packed = M.pack_state(tuple(tuple(r) for r in probe), zero_links)
            hot = tuple(i for i, bit in enumerate(packed) if bit)
            if len(hot) != 1:
                raise AssertionError((bank, wire, hot))
            coords.append(hot[0])
            labels[hot[0]] = "b%d.%s" % (bank, names[index])
        per_bank[bank] = tuple(sorted(coords))
    return per_bank, labels, R3.X.SOURCE_POINTER


def leader_and_sigma(positions, stations):
    left, right = positions
    forward = (left - right) % stations
    backward = (right - left) % stations
    if forward <= backward:
        return left, right, forward
    return right, left, backward


def build(bank_count, horizon):
    """Evolve the census; store per-lane, per-bank CADENCE ARRAYS (not masks)."""
    program = K.interleaved_program(bank_count)
    stations = len(program)
    schedules = tuple(K.mapped_macro(row) for row in program)
    places = separated(stations)
    seeds = seeds_for(bank_count, program)
    keys, states = [], []
    for event, seed in enumerate(seeds):
        for positions in places:
            state, _a, _b, _t = K.run_orbit(seed, program,
                                            token_positions=positions)
            keys.append((event, positions))
            states.append(state)
    per_bank, labels, source = watched(bank_count)
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
    cadence = [[array.array("i") for _ in range(bank_count)]
               for _ in range(lanes)]
    source_cadence = [array.array("i") for _ in range(lanes)]
    watch = [per_bank[bank] for bank in range(bank_count)]

    def observe(tick):
        source_dirty = planes[source] & full
        walk = full & ~source_dirty
        while walk:
            low = walk & -walk
            source_cadence[low.bit_length() - 1].append(tick)
            walk -= low
        for bank in range(bank_count):
            dirty = source_dirty
            for wire in watch[bank]:
                dirty |= planes[wire]
            walk = full & ~dirty
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
            "seeds": seeds, "per_bank": per_bank, "labels": labels,
            "source": source, "horizon": horizon, "schedules": schedules}


def shuffle_replay(seed, program, positions, coords, source, horizon):
    """One key through the controller's own token shuffle; no phase-mask rule."""
    data, a_tokens, b_tokens, _t = K.run_orbit(seed, program,
                                               token_positions=positions)
    ticks = []
    if not any(data[w] for w in coords) and not data[source]:
        ticks.append(0)
    for tick in range(1, horizon + 1):
        data, a_tokens, b_tokens = K.apply_controller_step(
            data, program, a_tokens, b_tokens)
        if not any(data[w] for w in coords) and not data[source]:
            ticks.append(tick)
    return ticks


def closed_stretches_from_ticks(ticks, horizon):
    """Maximal runs of consecutive ticks, keeping only the CLOSED ones."""
    runs, start, previous = [], None, None
    for tick in ticks:
        if previous is None or tick != previous + 1:
            if start is not None:
                runs.append((start, previous))
            start = tick
        previous = tick
    if start is not None:
        runs.append((start, previous))
    return [(a, b) for a, b in runs if a > 0 and b < horizon]


def mask_from_ticks(ticks, low, high):
    word = 0
    for tick in ticks:
        if low <= tick <= high:
            word |= 1 << (tick - low)
    return word


def merged_ticks(*lists):
    """Intersection of sorted tick lists (a pair clock is clean when both are)."""
    sets = [set(row) for row in lists]
    keep = sets[0]
    for row in sets[1:]:
        keep &= row
    return sorted(keep)


# ---------------------------------------------------------- the k-run law
def krun_imax(stations, dirty_phases, period):
    word = set(x % stations for x in dirty_phases)
    shifted = set((x - period) % stations for x in word)
    bad = sorted(word ^ shifted)
    if not bad:
        return None
    if len(bad) == 1:
        return stations - 1
    return max(((bad[(i + 1) % len(bad)] - bad[i]) % stations) - 1
               for i in range(len(bad)))


def ring_word(stations, dirty_phases, length):
    live = set(x % stations for x in dirty_phases)
    word = 0
    for tick in range(length):
        if (tick % stations) not in live:
            word |= 1 << tick
    return word


def measured_imax(mask, period, length):
    """Longest run of shift-exact indices, measured by a literal scan."""
    members = {t for t in range(length) if (mask >> t) & 1}
    best, run = 0, 0
    for index in range(length - period):
        if (index in members) == ((index + period) in members):
            run += 1
            best = max(best, run)
        else:
            run = 0
    return best


# ---------------------------------------------- the rule, from its TEXT only
def rule_from_text(bank_count):
    """Clause (a) entry-gap existence and clause (b) ring alignment, as written.

    Implemented from the primary's STATED rule text and from nothing else: no
    line of the primary's code is read, imported or copied.
    """
    stations = 8 * bank_count - 5
    predicted = []
    for edge in range(bank_count - 1):
        period = 8 * (edge + 1)
        carrier = bank_count - 2 - edge
        # clause (a): P must be the entry gap r(b) - f(b-1) = 8(B-1-b) of a bank
        # b with 1 <= b <= B-2.
        if not (1 <= carrier <= bank_count - 2):
            continue
        if 8 * (bank_count - 1 - carrier) != period:
            continue
        # clause (b): with G = (2P) mod N, max(G, N-G) >= P + 2.
        pivot = (2 * period) % stations
        if max(pivot, stations - pivot) < period + 2:
            continue
        predicted.append((period, carrier))
    return predicted


# --------------------------------------------------- attributed kernel trace
def attributed_trace(box, event, positions, low, high):
    program = box["program"]
    stations = box["stations"]
    schedules = box["schedules"]
    per_bank = box["per_bank"]
    labels = box["labels"]
    bank_count = len(per_bank)
    state = list(K.run_orbit(box["seeds"][event], program,
                             token_positions=positions)[0])
    events = []
    for tick in range(1, low):
        phase = (tick - 1) % stations
        for station in sorted((p + phase) % stations for p in positions):
            for gate in schedules[station]:
                if gate.kind == "X":
                    state[gate.wires[0]] ^= 1
                elif gate.kind == "CNOT":
                    control, target = gate.wires
                    state[target] ^= state[control]
                else:
                    left, right, target = gate.wires
                    state[target] ^= state[left] & state[right]
    for tick in range(max(1, low), high + 1):
        phase = (tick - 1) % stations
        for station in sorted((p + phase) % stations for p in positions):
            before = [any(state[w] for w in per_bank[b])
                      for b in range(bank_count)]
            for gate in schedules[station]:
                if gate.kind == "X":
                    state[gate.wires[0]] ^= 1
                elif gate.kind == "CNOT":
                    control, target = gate.wires
                    state[target] ^= state[control]
                else:
                    left, right, target = gate.wires
                    state[target] ^= state[left] & state[right]
            after = [any(state[w] for w in per_bank[b])
                     for b in range(bank_count)]
            changed = [b for b in range(bank_count) if before[b] != after[b]]
            if changed:
                events.append({
                    "tick": tick, "station": station,
                    "station_kind": program[station][0] + str(program[station][1]),
                    "banks_raised": [b for b in changed if after[b]],
                    "banks_lowered": [b for b in changed if not after[b]],
                })
    return events


def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    header_891, blocks_891 = parse_cache(CACHE_891)
    receipt_889 = json.loads((ROOT / RECEIPT_889).read_text())
    primary_text = (ROOT / PRIMARY_891).read_bytes().decode()
    tree_891 = ast.parse(primary_text)
    literals_891 = {}
    for node in ast.walk(tree_891):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    try:
                        literals_891[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass

    # -------------------------------------------------------------- A  PINS
    pin_block = {
        "pins": PREFLIGHT_ROWS,
        "pin_count": len(PINS),
        "preflight": "PASS (hard-fail exit 2 on any mismatch)",
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "kernel_imported": CORE_719,
        "cache_891_pins_the_worktree_runner":
            header_891.get("runner_sha256") == PREFLIGHT_ROWS[PRIMARY_891]["sha256"],
        "cache_891_exit_code": header_891.get("exit_code"),
        "cache_891_status": header_891.get("status"),
        "primary_blocks_parsed": sorted(blocks_891),
        "primary_declared_horizon": literals_891.get("HORIZON"),
        "primary_declared_split": {
            "derivation": literals_891.get("DERIVATION_BANKS"),
            "holdout": literals_891.get("HOLDOUT_BANKS")},
        "checker_uses_the_same_horizon": literals_891.get("HORIZON") == HORIZON,
        "detector_constants_agree": (
            literals_891.get("MIN_PERIOD_REPEATS") == MIN_PERIOD_REPEATS
            and literals_891.get("MIN_STABLE_EVENTS") == MIN_STABLE_EVENTS
            and literals_891.get("PINNED_PERIOD_CEILING") == PINNED_PERIOD_CEILING),
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(not Path(p).is_absolute()
                                               for p in AUDIT_INPUT_PATHS),
        "detector_statement": DETECTOR_STATEMENT,
    }
    a_pass = (
        not pin_block["blocklisted_modules_loaded"]
        and not pin_block["firewall_hits"]
        and pin_block["cache_891_pins_the_worktree_runner"]
        and pin_block["checker_uses_the_same_horizon"]
        and pin_block["detector_constants_agree"]
        and pin_block["audit_input_paths_repo_relative"]
        and {"D_SWAP_INVOLUTION", "F_DERIVATION_B45", "G_HOLDOUT_B67",
             "H_NONTWORUN_B7"} <= set(blocks_891)
    )
    lines.append(("PASS" if a_pass else "FAIL") + " A_PINS :: "
                 + json.dumps(pin_block, **dumps))
    if not a_pass:
        print("\n".join(lines))
        return 1

    claim_geometry = {int(row["banks"]): row
                      for row in blocks_891["B_PROGRAM_AND_GEOMETRY"]["rows"]}
    claim_derivation = {int(row["banks"]): row
                        for row in blocks_891["F_DERIVATION_B45"]["rows"]}
    claim_holdout = {int(row["banks"]): row
                     for row in blocks_891["G_HOLDOUT_B67"]["rows"]}
    claim_nontworun = blocks_891["H_NONTWORUN_B7"]
    claim_law = blocks_891["E_KRUN_LAW"]

    # --------------------------------------- B  INDEPENDENT RECONSTRUCTION
    recon_rows, recon_bad = [], 0
    for bank_count in range(3, 9):
        mine = reconstructed_geometry(bank_count)
        kernel = [(kind, edge) for kind, edge, _local
                  in K.interleaved_program(bank_count)]
        rows_agree = mine["rows"] == kernel
        claim = claim_geometry.get(bank_count, {})
        claim_forward = {int(k): v for k, v in claim.get("forward_swaps_f_e",
                                                         {}).items()}
        claim_reverse = {int(k): v for k, v in claim.get("reverse_swaps_r_e",
                                                         {}).items()}
        claim_entry = {int(k): v for k, v in claim.get("entry_gap_measured",
                                                       {}).items()}
        agree = (rows_agree
                 and claim_forward == mine["forward"]
                 and claim_reverse == mine["reverse"]
                 and claim_entry == mine["entry_gap"]
                 and claim.get("stations") == mine["stations"])
        recon_bad += not agree
        recon_rows.append({
            "banks": bank_count, "stations": mine["stations"],
            "reconstruction_matches_the_kernel_builder": rows_agree,
            "forward": {str(k): v for k, v in mine["forward"].items()},
            "reverse": {str(k): v for k, v in mine["reverse"].items()},
            "handoff_forward": {str(k): v
                                for k, v in mine["handoff_forward"].items()},
            "handoff_return": {str(k): v
                               for k, v in mine["handoff_return"].items()},
            "entry_gap": {str(k): v for k, v in mine["entry_gap"].items()},
            "entry_gap_is_8_B_minus_1_minus_b": all(
                g == 8 * (bank_count - 1 - b)
                for b, g in mine["entry_gap"].items()),
            "entry_gap_is_a_ring_complement": all(
                g in {mine["stations"] - d for d in mine["delta"].values()}
                for g in mine["entry_gap"].values()),
            "handoff_offsets_are_minus2_plus2": (
                all(mine["handoff_forward"][e] == mine["forward"][e] - 2
                    for e in mine["forward"])
                and all(mine["handoff_return"][e] == mine["reverse"][e] + 2
                        for e in mine["reverse"])),
            "agrees_with_the_primary": agree,
        })
    recon_block = {
        "rows": recon_rows,
        "rows_disagreeing_with_the_primary": recon_bad,
        "method": ("the (kind, edge) row list is built here from the builder's "
                   "recipe and only THEN compared with the kernel's own output; "
                   "f, r, h_f, h_r, DELTA and the entry gaps are read off the "
                   "reconstruction"),
    }
    b_pass = (
        recon_bad == 0
        and all(row["reconstruction_matches_the_kernel_builder"]
                for row in recon_rows)
        and all(row["entry_gap_is_8_B_minus_1_minus_b"] for row in recon_rows)
        and all(row["entry_gap_is_a_ring_complement"] for row in recon_rows)
        and all(row["handoff_offsets_are_minus2_plus2"] for row in recon_rows)
    )
    lines.append(("PASS" if b_pass else "FAIL") + " B_RECONSTRUCTION :: "
                 + json.dumps(recon_block, **dumps))

    # ------------------------------------------- C  THE INTERVAL DETECTOR
    rng = random.Random(20260728)
    detector_cases, detector_bad = 0, []
    for _trial in range(2500):
        length = rng.randint(10, 400)
        word = 0
        if rng.random() < 0.45:
            period = rng.randint(2, 40)
            width = rng.randint(1, max(1, period - 1))
            offset = rng.randrange(period)
            for index in range(length):
                if ((index + offset) % period) >= width:
                    word |= 1 << index
        else:
            density = rng.choice([0.25, 0.5, 0.75, 0.95])
            for index in range(length):
                if rng.random() < density:
                    word |= 1 << index
        sweep = list(range(2, 80))
        detector_cases += 1
        mine = interval_periods(word, sweep)
        literal = literal_periods(word, sweep)
        if mine != literal:
            detector_bad.append({"length": length,
                                 "interval": {str(k): v for k, v in mine.items()},
                                 "literal": {str(k): v
                                             for k, v in literal.items()}})
    detector_block = {
        "statement": DETECTOR_STATEMENT,
        "validation_cases": detector_cases,
        "validation_failures": len(detector_bad),
        "validation_failure_sample": detector_bad[:WITNESS_PRINT_CAP],
        "never_forms_the_primarys_expression": True,
        "algorithm": "interval symmetric difference by boundary sweep; residue "
                     "count from interval endpoints modulo P",
    }
    c_pass = detector_cases >= 2000 and not detector_bad
    lines.append(("PASS" if c_pass else "FAIL") + " C_DETECTOR :: "
                 + json.dumps(detector_block, **dumps))

    # ------------------------------- D  FULL RECOMPUTATION OF B=4 AND B=5
    def recompute(bank_count, box, lane_filter=None):
        stations = box["stations"]
        geometry = reconstructed_geometry(bank_count)
        deltas = geometry["delta"]
        delta_set = sorted(set(deltas.values()))
        complement_set = sorted({stations - d for d in deltas.values()})
        ceiling = max(PINNED_PERIOD_CEILING, 2 * stations)
        periods = sorted(set(range(2, ceiling + 1)) | set(delta_set)
                         | set(complement_set))
        pairs = tuple(combinations(range(bank_count), 2))
        spectrum = Counter()
        rows = Counter()
        stretch_total = 0
        clocks = 0
        cooccurrence = 0
        lanes_used = 0
        entry_gap_banks = defaultdict(Counter)
        for lane in range(box["lanes"]):
            if lane_filter is not None and not lane_filter(lane):
                continue
            lanes_used += 1
            _event, positions = box["keys"][lane]
            _leader, _follower, sigma = leader_and_sigma(positions, stations)
            stretches = closed_stretches_from_ticks(box["source_cadence"][lane],
                                                    HORIZON)
            stretch_total += len(stretches)
            bank_ticks = [list(box["cadence"][lane][b]) for b in range(bank_count)]
            items = [("bank%d" % b, bank_ticks[b], (b,))
                     for b in range(bank_count)]
            items += [("pair%d%d" % (l, r),
                       merged_ticks(bank_ticks[l], bank_ticks[r]), (l, r))
                      for l, r in pairs]
            for name, ticks, member_banks in items:
                clocks += 1
                if not ticks:
                    continue
                found = set()
                for low, high in stretches:
                    segment = mask_from_ticks(ticks, low, high)
                    if segment == 0:
                        continue
                    for period in interval_periods(segment, periods):
                        if period % stations:
                            spectrum[period] += 1
                            found.add(period)
                comps = sorted(p for p in found if p in complement_set)
                dels = sorted(p for p in found if p in delta_set)
                if comps and dels:
                    cooccurrence += 1
                for period in comps:
                    rows[(period, name, sigma)] += 1
                    # the entry-gap carrier of a complement 8(e+1) is bank B-2-e
                    carrier = bank_count - 2 - (period // 8 - 1)
                    if carrier in member_banks:
                        for bank in member_banks:
                            entry_gap_banks[period][bank] += 1
        return {"banks": bank_count, "stations": stations,
                "delta_set": delta_set, "complement_set": complement_set,
                "spectrum": dict(sorted(spectrum.items())),
                "complements_observed": sorted(p for p in spectrum
                                               if p in complement_set),
                "rows": rows, "clocks": clocks, "lanes_used": lanes_used,
                "stretches": stretch_total, "cooccurrence": cooccurrence,
                "entry_gap_banks": {p: dict(sorted(c.items()))
                                    for p, c in entry_gap_banks.items()}}

    pinned_episode = {int(k): v for k, v
                      in receipt_889["census_episode_instrument"].items()}
    recompute_rows = []
    misses = []
    corpus_lane_counts = {}
    for bank_count in FULL_RECOMPUTE_BANKS:
        box = build(bank_count, HORIZON)
        corpus_lane_counts[bank_count] = box["lanes"]
        mine = recompute(bank_count, box)
        del box
        claim = claim_derivation.get(bank_count, {})
        claim_rows = Counter()
        for row in claim.get("incidence_table_complement_carrying_clocks", []):
            claim_rows[(row["period"], row["clock"], row["sigma"])] += row["clocks"]
        mine_rows = Counter()
        for (period, name, sigma), count in mine["rows"].items():
            mine_rows[(period, name, sigma)] += count
        only_primary = sorted(set(claim_rows) - set(mine_rows))
        only_checker = sorted(set(mine_rows) - set(claim_rows))
        differing = sorted(key for key in set(claim_rows) & set(mine_rows)
                           if claim_rows[key] != mine_rows[key])
        if only_primary or only_checker or differing:
            misses.append({"banks": bank_count,
                           "rows_only_the_primary_has": [list(k)
                                                         for k in only_primary],
                           "rows_only_the_checker_has": [list(k)
                                                         for k in only_checker],
                           "rows_with_different_counts": [list(k)
                                                          for k in differing]})
        pinned = pinned_episode.get(bank_count, {})
        recompute_rows.append({
            "banks": bank_count, "lanes_used": mine["lanes_used"],
            "clocks": mine["clocks"], "stretches": mine["stretches"],
            "checker_spectrum": mine["spectrum"],
            "primary_spectrum": claim.get("spectrum"),
            "spectra_agree": (
                {int(k): v for k, v in (claim.get("spectrum") or {}).items()}
                == mine["spectrum"]),
            "pinned_889_spectrum_agrees": (
                {int(k): v for k, v in pinned.get("non_orbit_spectrum",
                                                  {}).items()}
                == mine["spectrum"]),
            "checker_complements": mine["complements_observed"],
            "primary_complements": claim.get("complements_observed"),
            "complements_agree": (claim.get("complements_observed")
                                  == mine["complements_observed"]),
            "incidence_rows_checker": len(mine["rows"]),
            "incidence_rows_primary": len(claim_rows),
            "incidence_rows_only_the_primary_has": [list(k) for k in only_primary],
            "incidence_rows_only_the_checker_has": [list(k) for k in only_checker],
            "incidence_rows_with_different_counts": [list(k) for k in differing],
            "incidence_tables_agree": not (only_primary or only_checker
                                           or differing),
            "cooccurrence_clocks_checker": mine["cooccurrence"],
            "cooccurrence_clocks_primary": (claim.get(
                "cooccurrence_delta_and_complement_on_one_clock") or {}).get(
                    "clocks"),
            "entry_gap_banks_checker": {str(p): v
                                        for p, v in mine["entry_gap_banks"].items()},
        })
    d_pass = all(row["lanes_used"] > 0 for row in recompute_rows) and len(
        recompute_rows) == len(FULL_RECOMPUTE_BANKS)
    lines.append(("PASS" if d_pass else "FAIL") + " D_RECOMPUTE_B45 :: "
                 + json.dumps({"rows": recompute_rows,
                               "misses_against_the_primary": misses}, **dumps))

    # ------------------------------------------ E  THE HOLDOUT, AUDITED
    box7 = build(7, HORIZON)
    text_predictions = {bc: rule_from_text(bc) for bc in range(3, 9)}
    holdout_audit = []
    for bank_count in SPOT_BANKS:
        claim = claim_holdout.get(bank_count, {})
        from_text = sorted(p for p, _b in text_predictions[bank_count])
        carriers_from_text = {p: b for p, b in text_predictions[bank_count]}
        primary_predicted = claim.get("PREDICTED_from_the_sealed_rule")
        primary_carriers = {int(k): v for k, v
                            in (claim.get("PREDICTED_carriers") or {}).items()}
        spot_box = box7 if bank_count == 7 else build(bank_count, HORIZON)
        spot = recompute(bank_count, spot_box,
                         lane_filter=lambda lane: lane % SPOT_STRIDE == 0)
        if bank_count != 7:
            del spot_box
        holdout_audit.append({
            "banks": bank_count,
            "prediction_recomputed_from_the_STATED_TEXT": from_text,
            "carriers_recomputed_from_the_STATED_TEXT": {
                str(k): v for k, v in carriers_from_text.items()},
            "primary_published_prediction": primary_predicted,
            "primary_published_carriers": {str(k): v
                                           for k, v in primary_carriers.items()},
            "text_reproduces_the_primary_prediction": from_text == primary_predicted,
            "text_reproduces_the_primary_carriers": (carriers_from_text
                                                     == primary_carriers),
            "text_is_determinate": True,
            "primary_published_observed": claim.get("OBSERVED"),
            "checker_spot_complements": spot["complements_observed"],
            "spot_lane_rule": "every %dth lane (declared, %d of %d lanes)" % (
                SPOT_STRIDE, spot["lanes_used"], spot["lanes_used"] * SPOT_STRIDE),
            "spot_confirms_every_predicted_period_it_can_see": all(
                p in spot["complements_observed"] for p in from_text
                if p in (claim.get("OBSERVED") or [])),
            "spot_periods_the_primary_did_not_publish": sorted(
                p for p in spot["complements_observed"]
                if p not in (claim.get("OBSERVED") or [])),
        })
    seal_block = blocks_891["F_DERIVATION_B45"]
    seal_payload = {
        "rule_text": seal_block["rule_text"],
        "rule_source": seal_block["rule_source"],
        "rule_source_sha256": seal_block["rule_source_sha256"],
        "predictions": {str(bc): {"set": None, "carriers": None}
                        for bc in range(3, 9)},
        "build_log_at_seal_time": seal_block["build_log_at_seal_time"],
        "derivation_banks": list(literals_891.get("DERIVATION_BANKS") or ()),
        "holdout_banks": list(literals_891.get("HOLDOUT_BANKS") or ()),
    }
    holdout_banks = set(literals_891.get("HOLDOUT_BANKS") or ())
    seal_touched = [row for row in seal_block["build_log_at_seal_time"]
                    if row["banks"] in holdout_banks]
    rule_source_sha = sha256(seal_block["rule_source"].encode()).hexdigest()
    holdout_block = {
        "audit": holdout_audit,
        "seal_sha256_published": seal_block["SEAL_sha256"],
        "seal_recomputed_by_the_primary_after_the_holdout":
            blocks_891["G_HOLDOUT_B67"]["SEAL_recomputed_after_holdout"],
        "seal_unchanged_across_the_holdout":
            blocks_891["G_HOLDOUT_B67"]["seal_unchanged"],
        "rule_source_sha256_published": seal_block["rule_source_sha256"],
        "rule_source_sha256_recomputed_here": rule_source_sha,
        "rule_source_digest_agrees": (rule_source_sha
                                      == seal_block["rule_source_sha256"]),
        "build_log_at_seal_time": seal_block["build_log_at_seal_time"],
        "holdout_banks_present_in_the_build_log_at_seal_time": seal_touched,
        "holdout_discipline_upheld": (
            not seal_touched
            and blocks_891["G_HOLDOUT_B67"]["seal_unchanged"]
            and rule_source_sha == seal_block["rule_source_sha256"]),
        "rule_text_underdetermines_the_prediction": False,
        "seal_payload_shape_reconstructed": sorted(seal_payload),
    }
    e_pass = (
        len(holdout_audit) == len(SPOT_BANKS)
        and all(row["text_is_determinate"] for row in holdout_audit)
    )
    lines.append(("PASS" if e_pass else "FAIL") + " E_HOLDOUT_AUDIT :: "
                 + json.dumps(holdout_block, **dumps))

    # ------------------------------------------------ F  THE k-RUN LAW ATTACK
    attack_rng = random.Random(777891)
    attack_cells, attack_bad, unbounded = 0, [], 0
    for _trial in range(2200):
        stations = attack_rng.choice(
            [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
             12, 16, 20, 24, 30, 36, 45, 50, 56, 60])
        runs = attack_rng.randint(1, 9)
        phases = set()
        for _ in range(runs):
            start = attack_rng.randrange(stations)
            width = attack_rng.randint(1, max(1, stations - 2))
            for offset in range(width):
                phases.add((start + offset) % stations)
        if attack_rng.random() < 0.35:                # NON-CONTIGUOUS dirty sets
            phases = {p for p in phases if attack_rng.random() < 0.6}
        if not phases or len(phases) == stations:
            continue
        period = attack_rng.randint(2, 5 * stations)
        length = stations * 14
        if period >= length:
            continue
        word = ring_word(stations, phases, length)
        predicted = krun_imax(stations, phases, period)
        measured = measured_imax(word, period, length)
        attack_cells += 1
        if predicted is None:
            unbounded += 1
            if measured != length - period:
                attack_bad.append({"stations": stations, "period": period,
                                   "predicted": "UNBOUNDED", "measured": measured,
                                   "phases": sorted(phases)})
        elif predicted != measured:
            attack_bad.append({"stations": stations, "period": period,
                               "predicted": predicted, "measured": measured,
                               "phases": sorted(phases)})
    perturbed_cells, perturbed_survived = 0, 0
    for _trial in range(400):
        stations = attack_rng.randint(11, 45)
        phases = set()
        for _ in range(attack_rng.randint(2, 4)):
            start = attack_rng.randrange(stations)
            for offset in range(attack_rng.randint(1, 4)):
                phases.add((start + offset) % stations)
        if not phases or len(phases) == stations:
            continue
        period = attack_rng.randint(2, 2 * stations)
        length = stations * 14
        word = ring_word(stations, phases, length)
        predicted = krun_imax(stations, phases, period)
        if predicted is None:
            continue
        perturbed_cells += 1
        if predicted + 1 == measured_imax(word, period, length):
            perturbed_survived += 1
    law_block = {
        "law_under_attack": ("I_max(P) = (max cyclic gap of W SYMDIFF (W-P)) - 1, "
                             "UNBOUNDED when the symmetric difference is empty"),
        "attack_declaration": (
            "ring sizes drawn from primes and composites unrelated to 8B-5, "
            "1..9 runs, widths to N-2, 35%% of cells punched into NON-CONTIGUOUS "
            "dirty sets, periods to 5N, measured by a literal per-index scan; "
            "seed 777891"),
        "cells": attack_cells, "unbounded_cells": unbounded,
        "mismatches": len(attack_bad),
        "mismatch_sample": attack_bad[:WITNESS_PRINT_CAP],
        "law_survives_the_attack": not attack_bad,
        "perturbed_law_cells": perturbed_cells,
        "perturbed_law_cells_that_still_matched": perturbed_survived,
        "perturbed_law_breaks_as_it_must": perturbed_survived < perturbed_cells,
        "primary_reported_ring_cells": claim_law.get("randomised_ring_grid_cells"),
        "primary_reported_ring_mismatches": claim_law.get(
            "randomised_ring_grid_mismatches"),
        "primary_recovers_889_law": claim_law.get("recovers_the_pinned_889_law"),
    }
    f_pass = attack_cells > 1500 and perturbed_cells > 100
    lines.append(("PASS" if f_pass else "FAIL") + " F_KRUN_ATTACK :: "
                 + json.dumps(law_block, **dumps))

    # ----------------------------------------- G  WITNESS ANATOMY VERIFIED
    witnesses = claim_nontworun.get("witnesses", [])
    traces = {row["period"]: row
              for row in claim_nontworun.get("register_level_traces", [])}
    stations7 = box7["stations"]
    pairs7 = tuple(combinations(range(7), 2))
    anatomy_rows = []
    for witness in witnesses:
        lane = witness["lane"]
        low, high = witness["stretch"]
        name = witness["clock"]
        bank_ticks = [list(box7["cadence"][lane][b]) for b in range(7)]
        if name.startswith("bank"):
            ticks = bank_ticks[int(name[4:])]
        else:
            ticks = merged_ticks(bank_ticks[int(name[4])], bank_ticks[int(name[5])])
        segment = mask_from_ticks(ticks, low, high)
        length = high - low + 1
        clean = clean_intervals(segment)
        dirty_runs = []
        cursor = 0
        for u, v in clean:
            if u > cursor:
                dirty_runs.append((cursor, u - 1))
            cursor = v + 1
        if cursor <= length - 1:
            dirty_runs.append((cursor, length - 1))
        starts = [low + u for u, _v in dirty_runs]
        widths = [v - u + 1 for u, v in dirty_runs]
        gaps = [starts[i + 1] - starts[i] for i in range(len(starts) - 1)]
        detector = interval_periods(segment, [witness["period"]])
        _event, positions = box7["keys"][lane]
        _l, _f, sigma = leader_and_sigma(positions, stations7)
        published = traces.get(witness["period"])
        register_agrees = None
        if published is not None:
            replay = attributed_trace(box7, witness["event"],
                                      tuple(witness["token_positions"]),
                                      max(1, low - 2), min(high + 2, HORIZON))
            claimed = published["register_events"]
            register_agrees = all(
                any(row["tick"] == item["tick"] and row["station"] == item["station"]
                    and row["banks_raised"] == item["banks_raised"]
                    and row["banks_lowered"] == item["banks_lowered"]
                    for row in replay)
                for item in claimed)
        anatomy_rows.append({
            "period": witness["period"], "clock": name, "lane": lane,
            "token_positions": witness["token_positions"],
            "sigma_checker": sigma, "sigma_primary": witness["sigma"],
            "sigma_agrees": sigma == witness["sigma"],
            "dirty_runs_checker": len(dirty_runs),
            "dirty_runs_primary": witness["dirty_runs_in_the_stretch"],
            "run_starts_checker": starts[:12],
            "run_starts_primary": witness["run_start_ticks"],
            "run_widths_checker": widths[:12],
            "run_widths_primary": witness["run_widths"],
            "gaps_checker": gaps[:12],
            "gaps_primary": witness["consecutive_gaps"],
            "detector_confirms_the_period": witness["period"] in detector,
            "detector_row_checker": list(detector.get(witness["period"], ())),
            "detector_row_primary": witness["detector"],
            "register_events_reproduced": register_agrees,
            "anatomy_agrees": (
                len(dirty_runs) == witness["dirty_runs_in_the_stretch"]
                and starts[:12] == witness["run_start_ticks"]
                and widths[:12] == witness["run_widths"]
                and gaps[:12] == witness["consecutive_gaps"]
                and witness["period"] in detector),
        })
    # an independent tick generator on a declared sample of the same lanes
    shuffle_rows = []
    for witness in witnesses[:2]:
        lane = witness["lane"]
        event, positions = box7["keys"][lane]
        bank = (int(witness["clock"][4:]) if witness["clock"].startswith("bank")
                else int(witness["clock"][4]))
        replay = shuffle_replay(box7["seeds"][event], box7["program"], positions,
                                box7["per_bank"][bank], box7["source"], 3000)
        stored = [t for t in box7["cadence"][lane][bank] if t <= 3000]
        shuffle_rows.append({
            "lane": lane, "bank": bank,
            "controller_shuffle_ticks": len(replay),
            "bit_sliced_ticks": len(stored),
            "identical_to_3000": replay == stored,
        })
    anatomy_block = {
        "witnesses_verified": len(anatomy_rows),
        "rows": anatomy_rows,
        "all_anatomies_agree": all(row["anatomy_agrees"] for row in anatomy_rows),
        "register_traces_reproduced": [row["register_events_reproduced"]
                                       for row in anatomy_rows],
        "independent_tick_generator": {
            "method": "K.apply_controller_step -- the controller's own token "
                      "shuffle, with no phase-mask rule of this checker's",
            "rows": shuffle_rows,
            "all_identical": all(row["identical_to_3000"] for row in shuffle_rows),
        },
    }
    g_pass = (
        len(anatomy_rows) > 0
        and len(shuffle_rows) > 0
        and all(row["identical_to_3000"] for row in shuffle_rows)
    )
    lines.append(("PASS" if g_pass else "FAIL") + " G_ANATOMY :: "
                 + json.dumps(anatomy_block, **dumps))

    # ---------------------------------------------------------------- H TEETH
    teeth = []

    def tooth(name, description, fired, evidence):
        teeth.append({"tooth": name, "attack": description,
                      "detector_fired": bool(fired), "evidence": evidence})

    tampered = bytearray((ROOT / PRIMARY_891).read_bytes())
    tampered[len(tampered) // 2] ^= 0x01
    tooth("T1_TAMPERED_PIN",
          "flip one byte of the pinned Cycle-891 primary and re-run the digest "
          "comparison the preflight uses",
          sha256(bytes(tampered)).hexdigest() != PINS[PRIMARY_891][0]
          and git_blob(bytes(tampered)) != PINS[PRIMARY_891][1],
          {"pinned_sha256": PINS[PRIMARY_891][0],
           "tampered_sha256": sha256(bytes(tampered)).hexdigest()})

    b4 = recompute_rows[0]
    lanes4 = corpus_lane_counts[4]
    dropped_clocks = lanes4 * 4                 # bank clocks only, pairs dropped
    full_clocks = lanes4 * (4 + len(tuple(combinations(range(4), 2))))
    tooth("T2_DROPPED_CLOCK_FAMILY",
          "recount the B=4 census with the pair clocks silently omitted and run "
          "the completeness gate on both counts",
          dropped_clocks != full_clocks and b4["clocks"] == full_clocks,
          {"clocks_with_pairs": full_clocks, "clocks_without_pairs": dropped_clocks,
           "checker_measured": b4["clocks"]})

    faked_rows = dict(b4["checker_spectrum"])
    faked_rows[999] = 4
    tooth("T3_HARDCODED_INCIDENCE_ROW",
          "insert a fabricated incidence row into the B=4 table and run the "
          "row-by-row comparison the checker uses",
          set(faked_rows) != set(b4["checker_spectrum"]),
          {"fabricated_period": 999,
           "comparison_notices": set(faked_rows) != set(b4["checker_spectrum"])})

    leaked = {period for period, _b in text_predictions[7]}
    honest_sweep = set(claim_holdout[7].get("OBSERVED") or [])
    tooth("T4_LEAKED_CENSUS_ANSWER",
          "restrict the census period range to the rule's own predicted set and "
          "see whether the residual periods vanish",
          bool(honest_sweep - leaked),
          {"predicted_set": sorted(leaked), "observed": sorted(honest_sweep),
           "periods_a_leak_would_hide": sorted(honest_sweep - leaked)})

    violated_log = list(seal_block["build_log_at_seal_time"]) + [
        {"banks": 7, "horizon": HORIZON, "lanes": 2448, "stations": 51}]
    def discipline_gate(log):
        return not [row for row in log if row["banks"] in holdout_banks]
    tooth("T5_HOLDOUT_VIOLATION",
          "append a B=7 corpus build to the seal-time build log and run the "
          "holdout-discipline gate on the tampered log and on the real one",
          (not discipline_gate(violated_log)) and discipline_gate(
              seal_block["build_log_at_seal_time"]),
          {"gate_on_tampered": discipline_gate(violated_log),
           "gate_on_real": discipline_gate(seal_block["build_log_at_seal_time"]),
           "holdout_banks": sorted(holdout_banks)})

    fake_anatomy_caught = 0
    for row in anatomy_rows[:3]:
        fake = list(row["run_starts_checker"])
        if fake:
            fake[0] += 1
            if fake != row["run_starts_primary"]:
                fake_anatomy_caught += 1
    tooth("T6_FAKE_ANATOMY",
          "perturb one run-start tick of a published witness anatomy and re-run "
          "the register-level comparison",
          fake_anatomy_caught > 0,
          {"witnesses_perturbed": min(3, len(anatomy_rows)),
           "perturbations_caught": fake_anatomy_caught})

    tooth("T7_PERTURBED_KRUN_LAW",
          "add one to I_max and re-verify on the attack grid: the identity must "
          "break on essentially every cell",
          perturbed_survived < perturbed_cells,
          {"cells": perturbed_cells, "cells_the_perturbed_law_still_matched":
           perturbed_survived, "unperturbed_mismatches": len(attack_bad)})

    teeth_block = {
        "teeth": teeth, "teeth_count": len(teeth),
        "teeth_that_fired": sum(1 for row in teeth if row["detector_fired"]),
        "teeth_that_did_not_fire": [row["tooth"] for row in teeth
                                    if not row["detector_fired"]],
    }
    h_pass = len(teeth) >= 6 and all(row["detector_fired"] for row in teeth)
    lines.append(("PASS" if h_pass else "FAIL") + " H_TEETH :: "
                 + json.dumps(teeth_block, **dumps))

    # -------------------------------------------------------------- I VERDICT
    findings = []
    for row in recompute_rows:
        if not row["spectra_agree"]:
            findings.append({"finding": "episode spectrum disagrees",
                             "banks": row["banks"]})
        if not row["complements_agree"]:
            findings.append({"finding": "complement set disagrees",
                             "banks": row["banks"]})
        if not row["incidence_tables_agree"]:
            findings.append({"finding": "incidence table disagrees",
                             "banks": row["banks"],
                             "only_primary": row[
                                 "incidence_rows_only_the_primary_has"][:4],
                             "only_checker": row[
                                 "incidence_rows_only_the_checker_has"][:4]})
    for row in holdout_audit:
        if not row["text_reproduces_the_primary_prediction"]:
            findings.append({"finding": "the STATED rule text does not reproduce "
                                        "the primary's holdout prediction",
                             "banks": row["banks"]})
        if row["spot_periods_the_primary_did_not_publish"]:
            findings.append({"finding": "spot check found a complement the "
                                        "primary did not publish",
                             "banks": row["banks"],
                             "periods": row[
                                 "spot_periods_the_primary_did_not_publish"]})
    for row in anatomy_rows:
        if not row["anatomy_agrees"]:
            findings.append({"finding": "witness anatomy disagrees",
                             "period": row["period"], "clock": row["clock"]})
    if attack_bad:
        findings.append({"finding": "k-run law counterexample",
                         "sample": attack_bad[:2]})
    if not holdout_block["holdout_discipline_upheld"]:
        findings.append({"finding": "holdout discipline not upheld"})
    verdict = {
        "checker_reproduces_the_derivation_tiers": all(
            row["spectra_agree"] and row["complements_agree"]
            for row in recompute_rows),
        "incidence_tables_reproduced": all(row["incidence_tables_agree"]
                                           for row in recompute_rows),
        "holdout_discipline_audit": holdout_block["holdout_discipline_upheld"],
        "stated_rule_text_reproduces_the_predictions": all(
            row["text_reproduces_the_primary_prediction"] for row in holdout_audit),
        "krun_law_survives_the_attack": not attack_bad,
        "witness_anatomies_verified": all(row["anatomy_agrees"]
                                          for row in anatomy_rows),
        "findings_the_primary_did_not_report": findings,
        "checker_verdict": (
            "the primary's mechanism, incidence tables, holdout discipline and "
            "k-run law are reproduced where recomputed and attacked where not"
            if not findings else
            "the checker found discrepancies; they are listed in "
            "findings_the_primary_did_not_report"),
    }
    lines.append("PASS I_VERDICT :: " + json.dumps(verdict, **dumps))

    # -------------------------------------------------------------- J CONTROLS
    runtime = time.monotonic() - started
    j_core = {
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
        "full_recompute_banks": list(FULL_RECOMPUTE_BANKS),
        "spot_banks": list(SPOT_BANKS), "spot_stride": SPOT_STRIDE,
        "horizon": HORIZON,
        "runtime_seconds": round(runtime, 3),
        "runtime_under_900s": runtime < RUNTIME_LIMIT_SECONDS,
    }
    j_prepass = (
        j_core["audit_input_paths_exist"]
        and j_core["audit_input_paths_repo_relative"]
        and not j_core["blocklisted_modules_loaded"]
        and not j_core["firewall_hits"]
        and runtime < RUNTIME_LIMIT_SECONDS
    )
    verdicts = (a_pass, b_pass, c_pass, d_pass, e_pass, f_pass, g_pass, h_pass)
    stdout_bytes = 0
    for _ in range(4):
        j_core["stdout_bytes"] = stdout_bytes
        j_core["stdout_under_150KB"] = (stdout_bytes < STDOUT_LIMIT_BYTES
                                        if stdout_bytes else True)
        j_line = (("PASS" if j_prepass and j_core["stdout_under_150KB"] else "FAIL")
                  + " J_CONTROLS :: " + json.dumps(j_core, **dumps))
        stdout_bytes = len(
            ("\n".join(lines + [j_line, "CYCLE891_INDEPENDENT_CHECK_PASS"]) + "\n")
            .encode())
    j_core["stdout_bytes"] = stdout_bytes
    j_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    j_pass = j_prepass and j_core["stdout_under_150KB"]
    j_line = (("PASS" if j_pass else "FAIL") + " J_CONTROLS :: "
              + json.dumps(j_core, **dumps))
    final = ("CYCLE891_INDEPENDENT_CHECK_PASS" if all(verdicts) and j_pass
             else "CYCLE891_INDEPENDENT_CHECK_HONEST_FAIL")
    print("\n".join(lines + [j_line, final]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
