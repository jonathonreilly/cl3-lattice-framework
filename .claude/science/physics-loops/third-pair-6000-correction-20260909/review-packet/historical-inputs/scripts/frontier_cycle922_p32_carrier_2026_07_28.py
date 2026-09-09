#!/usr/bin/env python3
"""Cycle 922: the P=32 carrier anatomy and the entry-gap REALIZATION CONDITION.

Cycle 891 derived the complement mechanism: ring-complement-valued separations
between incident transport stations take exactly three shapes -- the same-edge
pair (r(e), f(e)) with value N - DELTA(B,e) = 8(e+1), the ENTRY GAP
(f(b-1), r(b)) with value 8(B-1-b) owned by bank b = B-2-e, and (r(b-1), r(b))
with value 8(B-1) = N-3.  891 sealed a rule at B=4/5 and held it out at B=6/7.
The value-level holdout was exact.  The CARRIER-level holdout was 3/4: at B=7
the value P=32 was predicted to fire through the entry-gap class on bank b=2 and
instead fired ONLY through the edge-complement class.  Two 2-episode residuals
(P=40 and P=48 at B=7) were anatomised and left ruleless.

This runner answers all three of the questions that left open.

  Q1  THE P=32 CARRIER ANATOMY.  Every P=32 episode at B=7 is anatomised at
      register level with a CLOCK-LOCAL attribution: each dirty-run start of the
      reading clock is charged to the token and to the transport row OF THAT
      CLOCK'S OWN incident edges that caused it, via the pinned bookkeeping
      identity  s2 - s1 == Delta_t + (p2 - p1)  (mod N).  That is the sharpening
      891's census lacked: 891's ``classify_separation`` is VALUE-based for the
      DELTA/COMPLEMENT classes (it scans every swap station in the machine, not
      the reading clock's own rows) and gives RELAY_ENTRY_GAP top priority, so a
      value that is simultaneously a bank's entry gap and that bank's own edge
      complement is labelled ENTRY_GAP whatever produced it.

  Q2  THE REALIZATION CONDITION, sealed and held out.  RC-1 is derived station
      arithmetic; RC-2 is a closed form fitted to the clock-local incidence at
      B=4..7, frozen behind a digest printed BEFORE any B=8 corpus exists, and
      verified at B=8.  The runner NEVER builds a B=9 corpus, so its B=9
      prediction is holdout-free by construction; the independent checker builds
      B=9 and verifies it.

  Q3  THE 40/48 RESIDUALS.  Both are re-binned by the clock-local taxonomy and a
      verdict is issued -- fourth shape, or not.

Nothing is quoted from Cycles 879/881/889/891 except through sha-pinned
text/AST/JSON reads; their runners are import-blocklisted.  The only executable
dependency is the Cycle-719 controller core, the substrate under test.
"""
from __future__ import annotations

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
CHECKER_891 = "scripts/frontier_cycle891_complement_independent_check_2026_07_28.py"
RECEIPT_891 = "outputs/complement_mechanism_cycle891_receipt_2026_07_28.json"
RECEIPT_891_CHECK = (
    "outputs/complement_independent_check_cycle891_receipt_2026_07_28.json")
SHIP_891 = "outputs/complement_block_cycle891_ship_receipt_2026_07_28.json"
CACHE_891 = "logs/runner-cache/frontier_cycle891_complement_mechanism_2026_07_28.txt"
CACHE_891_CHECK = (
    "logs/runner-cache/frontier_cycle891_complement_independent_check_2026_07_28.txt")
NOTE_891 = (
    "docs/COMPLEMENT_MECHANISM_KRUN_LAW_CYCLE891_BOUNDED_THEOREM_NOTE_2026-07-28.md")
PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
CHECKER_889 = "scripts/frontier_cycle889_delta_spectrum_independent_check_2026_07_28.py"
RECEIPT_889 = "outputs/delta_spectrum_cycle889_receipt_2026_07_28.json"
CACHE_889 = "logs/runner-cache/frontier_cycle889_delta_spectrum_2026_07_28.txt"
PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CORE_719_HANDSHAKE = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py")

# Every pin is read as bytes; its sha256 AND its git blob id are compared with
# the value recorded here.  Any mismatch is exit 2 before anything else runs.
# The 889/881/879 and Cycle-719 rows are inherited from the pinned Cycle-891
# receipt byte for byte; the 891 rows are this cycle's own.
PINS = {
    PRIMARY_891: ("3d260f6641d05a22aee092145ea3e5c3b29f3a6882b4cbd9ae966424458afbb7",
                  "a1bbd49ffbe970193cc79054fb7219732f7c9873"),
    CHECKER_891: ("f2e9ca32b7d3f863822126c05fbf6a3b637164e8969e5ec7c6c04f15cd89e568",
                  "53f5cf560f6dfad20dc6b4b91b0c003c848c6bea"),
    RECEIPT_891: ("f8e30d50a50e39a13f8f968b2ae21991885b6c858c6c96439ed733fc8514bacd",
                  "f537715a927b00b817f8de2569953d78929c86db"),
    RECEIPT_891_CHECK: ("cb2f6badda7315725f5f33c5aad89e7e37cf9201472362e0af3a16c4225fae8f",
                        "478f19642c1d66a6e1575798f9974b645c9f9a18"),
    SHIP_891: ("9d1ac3b6b8189dcac29c7dc78e786967ead4474fc2d8f24b0853ffb27bee8137",
               "4d1366da9325d69bb5bfc9d9604e9e02cf894d9d"),
    CACHE_891: ("47b07a1f1428e50bab41890dff77345130cfa9456b887bafbb00df360027409c",
                "7099e5ece90f4b59acec9bf27af29468c4e6b746"),
    CACHE_891_CHECK: ("2372d2d55c386ff05af6cee8126469ca5baad6d49fc3a60bbf93b6c064df1061",
                      "7f2f15677a906c638d526389318568dec33360f8"),
    NOTE_891: ("5b20f90a643e890492d65907050e31772b85f1b00e1ee5581f5132f45f6a700c",
               "235965affc47ce7745327ef194e7c0ae31e6a6c8"),
    PRIMARY_889: ("c18ed0c49281fd2d54ad013ba12264b181d1720349ee002b144c028b521dd826",
                  "f1bdf1f789a85213a0a854ab0bed45e6bf250fed"),
    CHECKER_889: ("19b38fb116bb8cb79cbb925df91456c5d08d899d4b56de301a9a673ec7dc3ec3",
                  "0f946f44c431c997410a08ec3e03ae2d26d89b8a"),
    RECEIPT_889: ("10840d84d3110fa192c28667334152da815f535f131d59e763dc64bf0aef3a72",
                  "2191d809ff5b4b9f082d9f703969e05638e6e33e"),
    CACHE_889: ("48c0bc663d2a5254947087003ece0b34dd730a291ccef2f1b007a5043ec2a5be",
                "a1ac91d1ce89275f7034756fbb3b527a564e9738"),
    PRIMARY_881: ("7cc1c8984869d824f33d83ccf6599c6ef9e166766015979d204309c3e820ed35",
                  "4b7297890a822184914bace90f60b47dc09f8305"),
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

# Detector constants: inherited verbatim from the pinned Cycle-889 primary and
# re-checked against its AST in gate A.
TOKEN_K = 2
EVENT_COUNT = 2
HORIZON = 16_384
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8
PINNED_PERIOD_CEILING = 64

DERIVATION_BANKS = (4, 5, 6, 7)     # RC-2 is fitted here
HOLDOUT_BANKS = (8,)                # and held out here
NEVER_BUILT_BANKS = (9, 10, 11, 12)  # predicted only; no corpus is ever built

DISCLOSED_DEVIATIONS = (
    "PERIOD CEILING.  Inherited verbatim from Cycles 889/891: every P in "
    "[2, max(64, 2N(B))] is tried, which strictly contains every DELTA(B,e) and "
    "every ring complement.  The sweep is never narrowed to a predicted set, so "
    "an out-of-set falsifier cannot be invisible (gate J proves it on a plant).",
    "HORIZON.  H = 16384 ticks per substrate for every tier, identical to "
    "Cycles 889 and 891, so the B=4..7 census here is directly comparable with "
    "the pinned 891 receipt and the B=8 tier is on the same footing.",
    "NO SAMPLING IN THE CENSUS.  Every clock of every corpus is swept at every "
    "bank count in 4,5,6,7,8 -- all bank clocks and all pair clocks, every "
    "closed quiescent stretch.  The clock count is gated against "
    "lanes * (B + C(B,2)).",
    "B=9 IS NEVER BUILT BY THIS RUNNER.  The B=9..12 rows are pure-function "
    "predictions of the sealed rule.  This is deliberate: it makes the B=9 "
    "prediction holdout-free by construction (there is no B=9 corpus in this "
    "process to leak) and it hands the B=9 verification to the independent "
    "checker, which builds that corpus itself.",
    "WORKER DISCLOSURE ON THE B=8 SEAL.  During scoping the worker RAN the "
    "Cycle-891 census code at B=8 and SAW its 891-label output (class_counts, "
    "carrier_counts, spectrum) before RC-2 was written.  RC-2 was fitted only to "
    "the CLOCK-LOCAL incidence at B=4..7, which the worker had; the clock-local "
    "B=8 incidence was NOT computed until after RC-2 and its B=8/B=9 predictions "
    "were written down and hashed.  RC-2 CONTRADICTS the 891-label B=8 row on "
    "two of six cells (it says the value 32 does NOT fire entry-gap at B=8 where "
    "the 891 label says it does, and that the value 8 DOES where the label says "
    "it does not), so the prediction demonstrably was not copied from what was "
    "seen.  The honest status is: B=8 is a partially-informed holdout at the "
    "891-label level and a blind holdout at the clock-local level; B=9 is blind "
    "on every level and is the checker's to verify.",
    "ANATOMY SUBSET.  Clock-local run attribution is extracted for every episode "
    "whose period is a DELTA or a ring complement -- that is the whole "
    "population the questions are about -- and the count is reported in full and "
    "never sampled.  Other periods contribute to the spectrum and to the "
    "completeness ledger only.",
)

# ----------------------------------------------------------------- the claims
SHAPE_INVENTORY_STATEMENT = (
    "THE CLOCK-LOCAL SHAPE INVENTORY (derived, exhaustive).  A clock's dirty-run "
    "starts are crossings of ITS OWN incident transport rows.  Bank b owns "
    "exactly eight of them -- for each incident edge e in {b-1, b} the four "
    "ordered rows h_f(e) = f(e)-2, f(e), r(e), h_r(e) = r(e)+2, with "
    "f(e) = 4+5e and r(e) = 8B-9-3e on N = 8B-5 stations.  Among the ordered "
    "SAME-TOKEN pairs of those eight rows the ring-complement-valued "
    "separations are exactly these and no others: "
    "(1) SAME-EDGE COMPLEMENT (r(e), f(e)) = 8(e+1) for each incident e; "
    "(2) the ENTRY GAP value 8(B-1-b), realised by THREE ordered pairs -- "
    "(f(b-1), r(b)), (f(b), h_r(b-1)) and (h_f(b), r(b-1)) -- all three present "
    "iff 1 <= b <= B-2; "
    "(3) the value 8(B-1) = N-3, realised by (r(b-1), r(b)) and by "
    "(h_r(b-1), h_r(b)). "
    "Cycle 891 reported ONE pair for the entry gap because its census was "
    "restricted to the two RELAY_SWAP rows per edge; the handoff rows carry the "
    "same value and, measured, carry MOST of the entry-gap episodes at every B "
    "where the entry gap fires at all."
)

RC_STATEMENT = (
    "THE ENTRY-GAP REALIZATION CONDITION (RC).  Fix a bank count B, N = 8B-5, "
    "and a bank b; let P = 8(B-1-b) be b's entry-gap value.  "
    "RC-1 EXISTENCE (derived station arithmetic, exhaustively verified): P is a "
    "bank-owned same-token separation of bank b, realised by exactly the three "
    "ordered row pairs (f(b-1), r(b)), (f(b), h_r(b-1)), (h_f(b), r(b-1)), and "
    "all three exist iff 1 <= b <= B-2. "
    "RC-2 SHORT-ARC NECESSITY (closed form, fitted at B=4..7 and sealed): a "
    "bank-owned entry-gap reading occurs ONLY IF 2P < N, equivalently "
    "b >= floor(B/2), equivalently -- in the edge labelling P = 8(e+1) with "
    "carrier b = B-2-e -- only if e + 1 < (8B-5)/16.  The entry gap must be the "
    "SHORT arc of the bank's own two dwell residues; when 2P >= N a P-shift-exact "
    "stable region of the required length 2P+1 would have to close on a third "
    "dwell residue u + 2P = u + (2P - N) that the bank does not own, and the "
    "reading dies. "
    "RC-3 NOT SUFFICIENT (declared boundary, measured): RC-2 is necessary but "
    "not sufficient.  What remains is stretch-local in exactly Cycle 891's "
    "declared sense -- the reading also needs some closed quiescent stretch to "
    "present the two P-separated runs with EQUAL width w <= P-1 and at least "
    "MIN_STABLE_EVENTS clean ticks in the stable region -- and that is a "
    "dynamical fact about which word a stretch carries, not a function of (B,b). "
    "THE CARRIER CORRECTION.  891's carrier prediction 'the value 8(e+1) fires "
    "through the entry gap on bank B-2-e' is therefore true only on the "
    "short-arc half of the family.  At B=7 that cuts the family at e <= 2, i.e. "
    "P in {8,16,24}: P=32 (e=3, carrier b=2) is excluded, which is exactly 891's "
    "carrier miss, now derived rather than observed."
)

BOOKKEEPING_STATEMENT = (
    "THE CLOCK-LOCAL BOOKKEEPING IDENTITY.  A dirty-run start of clock C at tick "
    "t is the crossing of station (p + t - 1) mod N by some token p, and that "
    "station must be one of C's OWN incident transport rows.  Two run starts "
    "separated by Delta_t are therefore rows s1, s2 of C with "
    "s2 - s1 == Delta_t + (p2 - p1) (mod N).  Restricting s1, s2 to the reading "
    "clock's own rows is the sharpening: 891's classifier scanned every swap "
    "station in the machine and gave RELAY_ENTRY_GAP top priority, so a value "
    "that is simultaneously a bank's entry gap and that bank's own edge "
    "complement was labelled ENTRY_GAP whatever produced it."
)

DETECTOR_STATEMENT = (
    "THE DETECTOR.  Reimplemented from the sha-pinned Cycle-889/891 declared "
    "semantics: a clock's clean ticks inside one closed quiescent stretch become "
    "a bitmask S; for a period P the bits of (S ^ (S >> P)) below last - P + 1 "
    "are exactly the ticks where t in S <=> t+P in S fails, so the highest such "
    "bit + 1 is the LEAST transient -- no window, no ladder, no block cap.  A "
    "reading is kept only if last - transient >= 2P, the stable stretch carries "
    ">= 8 clean ticks, and the stable clean residues modulo P are not all of "
    "them.  The detector is given no knowledge of DELTA, of the complement set "
    "or of RC: it sweeps a contiguous period range and the predicted sets are "
    "compared against its output afterwards."
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
        rows[path] = {"present": True, "sha256": got_sha, "git_blob": got_blob,
                      "sha256_pinned": want_sha, "git_blob_pinned": want_blob,
                      "match": ok}
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


BLOCKLISTED_MODULES = tuple(Path(p).stem for p in
                            (PRIMARY_879, PRIMARY_881, PRIMARY_889, CHECKER_889,
                             PRIMARY_891, CHECKER_891))


class _Firewall(importlib.abc.MetaPathFinder):
    """Any import of a blocklisted Cycle-879/881/889/891 runner is a hard failure."""

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
    return per_bank, labels, R3.X.SOURCE_POINTER, len(local)


def relay_rows_by_edge(program):
    rows = defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "relay":
            rows[edge].append(index)
    return dict(sorted(rows.items()))


def relay_swap_rows(program):
    """The forward/reverse RELAY_SWAP station indices per edge, read from gates."""
    swaps, malformed = {}, 0
    for edge, indices in relay_rows_by_edge(program).items():
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


BUILD_LOG = []


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
    per_bank, labels, source_pointer, wire_count = watched_layout(bank_count)
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
    BUILD_LOG.append({"banks": bank_count, "horizon": horizon,
                      "lanes": lane_count, "stations": stations})
    return {
        "banks": bank_count, "stations": stations, "program": program,
        "keys": tuple(keys), "lane_count": lane_count,
        "placements": len(placements), "clean_planes": clean_planes,
        "source_clean": source_clean, "swaps": swaps, "malformed": malformed,
        "source_pointer": source_pointer, "wire_count": wire_count,
        "seed_failures": seed_failures, "token_failures": token_failures,
        "horizon": horizon, "seeds": seeds, "schedules": schedules,
        "per_bank": per_bank, "labels": labels,
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
    out = {}
    if mask == 0:
        return out
    if bin(mask).count("1") < min_events:
        return out
    last = mask.bit_length() - 1
    for period in periods:
        need = min_repeats * period
        if need > last:
            break
        low = last - need
        window = (mask >> low) & ((1 << (need + 1)) - 1)
        if (window ^ (window >> period)) & ((1 << (period + 1)) - 1):
            continue
        span = last - period
        broken = (mask ^ (mask >> period)) & ((1 << (span + 1)) - 1)
        transient = broken.bit_length()
        if last - transient < min_repeats * period:
            continue
        reach = last - transient
        stable = (mask >> transient) & ((1 << (reach + 1)) - 1)
        events = bin(stable).count("1")
        if events < min_events:
            continue
        folded, step = stable, period
        while step <= reach:
            folded |= folded >> step
            step <<= 1
        residue_count = bin(folded & ((1 << period) - 1)).count("1")
        if residue_count == period:
            continue
        out[period] = (transient, events, residue_count)
    return out


def reference_tail_periods(mask, periods):
    """The same semantics with a literal bit-walk residue count.  No folding."""
    out = {}
    if mask == 0 or bin(mask).count("1") < MIN_STABLE_EVENTS:
        return out
    last = mask.bit_length() - 1
    for period in periods:
        if MIN_PERIOD_REPEATS * period > last:
            break
        span = last - period
        broken = (mask ^ (mask >> period)) & ((1 << (span + 1)) - 1)
        transient = broken.bit_length()
        if last - transient < MIN_PERIOD_REPEATS * period:
            continue
        stable = (mask >> transient) & ((1 << (last - transient + 1)) - 1)
        events = bin(stable).count("1")
        if events < MIN_STABLE_EVENTS:
            continue
        residues, walk = set(), stable
        while walk:
            low = walk & -walk
            residues.add((transient + low.bit_length() - 1) % period)
            walk -= low
        if len(residues) == period:
            continue
        out[period] = (transient, events, len(residues))
    return out


def maximal_runs(mask, horizon):
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


def zero_runs(segment, length):
    """Maximal runs of CLEAR bits (= dirty ticks) inside a segment."""
    runs, index = [], 0
    while index < length:
        if not ((segment >> index) & 1):
            stop = index
            while stop + 1 < length and not ((segment >> (stop + 1)) & 1):
                stop += 1
            runs.append((index, stop))
            index = stop + 1
        else:
            index += 1
    return runs


def max_exact_run(mask, period, length):
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


def krun_imax(stations, dirty_phases, period):
    """891's k-run law, ring form.  None means UNBOUNDED (Fbad empty)."""
    word = set(x % stations for x in dirty_phases)
    shifted = set((x - period) % stations for x in word)
    bad = sorted(word ^ shifted)
    if not bad:
        return None
    if len(bad) == 1:
        return stations - 1
    return max(((bad[(i + 1) % len(bad)] - bad[i]) % stations) - 1
               for i in range(len(bad)))


# ----------------------------------------------- station / shape bookkeeping
def station_table(bank_count):
    """Every transport row of the machine, with its kind and edge."""
    program = K.interleaved_program(bank_count)
    stations = len(program)
    swaps, malformed = relay_swap_rows(program)
    forward = {e: pair[0] for e, pair in swaps.items()}
    reverse = {e: pair[1] for e, pair in swaps.items()}
    handoff = defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "handoff":
            handoff[edge].append(index)
    handoff_forward = {e: rows[0] for e, rows in handoff.items() if len(rows) == 2}
    handoff_return = {e: rows[1] for e, rows in handoff.items() if len(rows) == 2}
    station_edge = {}
    for edge in sorted(swaps):
        station_edge[handoff_forward[edge]] = ("handoff_forward", edge)
        station_edge[forward[edge]] = ("forward", edge)
        station_edge[reverse[edge]] = ("reverse", edge)
        station_edge[handoff_return[edge]] = ("handoff_return", edge)
    entry_gap = {b: (reverse[b] - forward[b - 1]) % stations
                 for b in range(1, bank_count - 1)}
    rows_of_bank = {}
    for bank in range(bank_count):
        incident = [e for e in (bank - 1, bank) if 0 <= e <= bank_count - 2]
        rows_of_bank[bank] = {s: (k, e) for s, (k, e) in station_edge.items()
                              if e in incident}
    return {"program": program, "stations": stations, "swaps": swaps,
            "forward": forward, "reverse": reverse,
            "handoff_forward": handoff_forward, "handoff_return": handoff_return,
            "station_edge": station_edge, "rows_of_bank": rows_of_bank,
            "entry_gap": entry_gap, "malformed": malformed,
            "delta": {e: (r - f) % stations for e, (f, r) in swaps.items()}}


def bank_owned_shape_inventory(bank_count, bank, table):
    """Every ordered same-token pair of bank ``bank``'s own rows, classified.

    Returns {separation -> [(s1, kind1, edge1, s2, kind2, edge2, shape), ...]}.
    Pure station arithmetic; no corpus is read.
    """
    stations = table["stations"]
    rows = table["rows_of_bank"][bank]
    incident = sorted({e for _k, e in rows.values()})
    complements = {stations - d for d in table["delta"].values()}
    entry = 8 * (bank_count - 1 - bank)
    out = defaultdict(list)
    for s1, (k1, e1) in sorted(rows.items()):
        for s2, (k2, e2) in sorted(rows.items()):
            if s1 == s2:
                continue
            sep = (s2 - s1) % stations
            shape = "OTHER"
            if k1 == "reverse" and k2 == "forward" and e1 == e2:
                shape = "SAME_EDGE_COMPLEMENT"
            elif k1 == "forward" and k2 == "reverse" and e1 == e2:
                shape = "SAME_EDGE_DELTA"
            elif (k1, k2) == ("forward", "reverse") and e2 == e1 + 1:
                shape = "ENTRY_GAP_swap_swap"
            elif (k1, k2) == ("forward", "handoff_return") and e1 == e2 + 1:
                shape = "ENTRY_GAP_swap_handoff"
            elif (k1, k2) == ("handoff_forward", "reverse") and e1 == e2 + 1:
                shape = "ENTRY_GAP_handoff_swap"
            elif (k1, k2) == ("reverse", "reverse") and e2 == e1 + 1:
                shape = "REVERSE_PAIR"
            elif (k1, k2) == ("handoff_return", "handoff_return") and e2 == e1 + 1:
                shape = "HANDOFF_RETURN_PAIR"
            out[sep].append((s1, k1, e1, s2, k2, e2, shape))
    return {"separations": dict(sorted(out.items())), "incident_edges": incident,
            "entry_gap_value": entry, "complement_values": sorted(complements)}


ENTRY_GAP_SHAPES = ("ENTRY_GAP_swap_swap", "ENTRY_GAP_swap_handoff",
                    "ENTRY_GAP_handoff_swap")


def attribute_runs(starts, positions, rows, stations):
    """Charge each dirty-run start to (token, own row).  May be ambiguous."""
    out = []
    for tick in starts:
        cand = []
        for p in positions:
            s = (p + tick - 1) % stations
            if s in rows:
                cand.append((p, s, rows[s][0], rows[s][1]))
        out.append(cand)
    return out


def local_pairs_for_period(starts, attribution, period):
    """Every consecutive run-start pair separated by ``period``, clock-locally.

    Returns a set of (same_token, kind1, edge1, kind2, edge2) tuples.
    """
    found = set()
    for i in range(len(starts) - 1):
        if starts[i + 1] - starts[i] != period:
            continue
        for p1, _s1, k1, e1 in attribution[i]:
            for p2, _s2, k2, e2 in attribution[i + 1]:
                found.add((p1 == p2, k1, e1, k2, e2))
    return found


def shape_of_local_pair(pair, bank, bank_count):
    """Name the clock-local shape of one attributed consecutive-run-start pair."""
    same_token, k1, e1, k2, e2 = pair
    if not same_token:
        return "CROSS_TOKEN"
    if k1 == "reverse" and k2 == "forward" and e1 == e2:
        return "SAME_EDGE_COMPLEMENT"
    if k1 == "forward" and k2 == "reverse" and e1 == e2:
        return "SAME_EDGE_DELTA"
    if (k1, k2) == ("forward", "reverse") and e2 == e1 + 1 and e2 == bank:
        return "ENTRY_GAP_swap_swap"
    if (k1, k2) == ("forward", "handoff_return") and e1 == e2 + 1 and e1 == bank:
        return "ENTRY_GAP_swap_handoff"
    if (k1, k2) == ("handoff_forward", "reverse") and e1 == e2 + 1 and e1 == bank:
        return "ENTRY_GAP_handoff_swap"
    if (k1, k2) == ("reverse", "reverse"):
        return "REVERSE_PAIR"
    return "OTHER_SAME_TOKEN"


# --------------------------------------- 891's own classifier, reimplemented
CLASS_PRIORITY = ("RELAY_ENTRY_GAP", "RELAY_EDGE_COMPLEMENT", "RELAY_EDGE_DELTA",
                  "TOKEN_SEPARATION", "MIXED")


def classify_separation_891(table, banks_of_clock, positions, separation):
    """Cycle 891's ``classify_separation``, reimplemented from its pinned text.

    Reproduced verbatim in SEMANTICS so that gate D can compare value for value
    with the pinned 891 receipt.  It is VALUE-based for the DELTA/COMPLEMENT
    classes -- it scans every swap station of the machine, not the reading
    clock's own rows -- and gives RELAY_ENTRY_GAP top priority.  That is the
    property this cycle sharpens; it is reproduced here only as a restriction
    gate, never used as this cycle's taxonomy.
    """
    stations = table["stations"]
    swap_set = table["station_edge"]
    labels = set()
    for p1 in positions:
        for p2 in positions:
            for s1 in swap_set:
                s2 = (s1 + separation + (p2 - p1)) % stations
                if s2 not in swap_set:
                    continue
                kind1, edge1 = swap_set[s1]
                kind2, edge2 = swap_set[s2]
                label = "MIXED"
                if p1 == p2:
                    if s1 == s2:
                        label = "MIXED"
                    elif kind1 == "forward" and kind2 == "reverse" and edge1 == edge2:
                        label = "RELAY_EDGE_DELTA"
                    elif kind1 == "reverse" and kind2 == "forward" and edge1 == edge2:
                        label = "RELAY_EDGE_COMPLEMENT"
                    elif (kind1 == "forward" and kind2 == "reverse"
                          and edge2 == edge1 + 1
                          and (edge1 + 1) in banks_of_clock):
                        label = "RELAY_ENTRY_GAP"
                elif s1 == s2:
                    label = "TOKEN_SEPARATION"
                labels.add(label)
    if not labels:
        return "UNATTRIBUTED"
    return next(name for name in CLASS_PRIORITY if name in labels)


# ---------------------------------------------------------------- the census
def census(box, anatomy_cap=8):
    """One exhaustive episode census carrying BOTH taxonomies in one pass."""
    bank_count = box["banks"]
    stations = box["stations"]
    lanes = box["lane_count"]
    horizon = box["horizon"]
    table = station_table(bank_count)
    deltas = table["delta"]
    delta_set = sorted(set(deltas.values()))
    complement_set = sorted({stations - d for d in deltas.values()})
    named = set(delta_set) | set(complement_set)
    ceiling = max(PINNED_PERIOD_CEILING, 2 * stations)
    periods = sorted(set(range(2, ceiling + 1)) | named)
    pairs = tuple(combinations(range(bank_count), 2))
    bank_masks = [transpose_planes(box["clean_planes"][b], lanes, horizon)
                  for b in range(bank_count)]
    source_masks = transpose_planes(box["source_clean"], lanes, horizon)

    spectrum = Counter()
    class_counts_891 = Counter()
    carrier_counts_891 = defaultdict(Counter)
    local_shape_counts = Counter()       # (bank, period, shape) -> episodes
    bank_period = Counter()              # (bank, period) -> episodes, bank clocks
    bank_period_sigma = defaultdict(Counter)
    unattributed = Counter()
    ledger = Counter()
    cooccurrence = 0
    stretch_total = 0
    longest_stretch = 0
    clocks_total = 0
    anatomy = defaultdict(list)
    cache_891 = {}

    for lane in range(lanes):
        event, positions = box["keys"][lane]
        _leader, _follower, sigma = leader_and_sigma(positions, stations)
        stretches = [(a, b) for (a, b) in maximal_runs(source_masks[lane], horizon)
                     if a > 0 and b < horizon]
        stretch_total += len(stretches)
        for a, b in stretches:
            if b - a + 1 > longest_stretch:
                longest_stretch = b - a + 1
        cleaned = [bank_masks[bank][lane] for bank in range(bank_count)]
        items = [("bank%d" % b, cleaned[b], (b,)) for b in range(bank_count)]
        items += [("pair%d%d" % (l, r), cleaned[l] & cleaned[r], (l, r))
                  for l, r in pairs]
        for name, mask, member_banks in items:
            clocks_total += 1
            if mask == 0:
                ledger["no_reading"] += 1
                continue
            found = set()
            for a, b in stretches:
                length = b - a + 1
                segment = (mask >> a) & ((1 << length) - 1)
                if segment == 0:
                    continue
                hits = tail_periods(segment, periods)
                if not hits:
                    continue
                interesting = [p for p in hits if p % stations and p in named]
                for period in hits:
                    if period % stations:
                        spectrum[period] += 1
                        found.add(period)
                if not interesting:
                    continue
                runs = zero_runs(segment, length)
                starts = [a + lo for lo, _hi in runs]
                widths = [hi - lo + 1 for lo, hi in runs]
                for period in interesting:
                    key = (frozenset(member_banks), positions, period)
                    if key not in cache_891:
                        cache_891[key] = classify_separation_891(
                            table, set(member_banks), positions, period)
                    label = cache_891[key]
                    class_counts_891[(period, label)] += 1
                    for bank in member_banks:
                        carrier_counts_891[(period, label)][bank] += 1
                    if len(member_banks) != 1:
                        continue
                    bank = member_banks[0]
                    bank_period[(bank, period)] += 1
                    bank_period_sigma[(bank, period)][sigma] += 1
                    attribution = attribute_runs(
                        starts, positions, table["rows_of_bank"][bank], stations)
                    local = local_pairs_for_period(starts, attribution, period)
                    if not local:
                        unattributed[(bank, period)] += 1
                    shapes = {shape_of_local_pair(p, bank, bank_count)
                              for p in local}
                    for shape in sorted(shapes):
                        local_shape_counts[(bank, period, shape)] += 1
                    if len(anatomy[(bank, period)]) < anatomy_cap:
                        anatomy[(bank, period)].append({
                            "banks": bank_count, "lane": lane, "event": event,
                            "clock": name, "token_positions": list(positions),
                            "sigma": sigma, "stretch": [a, b],
                            "stretch_len": length, "period": period,
                            "detector_transient_events_residues": list(hits[period]),
                            "dirty_runs": len(runs),
                            "run_start_ticks": starts[:14],
                            "run_widths": widths[:14],
                            "consecutive_gaps": [starts[i + 1] - starts[i]
                                                 for i in range(min(13, len(starts) - 1))],
                            "attribution": [
                                ["p%d@s%d:%s%d" % (p, s, k, e) for p, s, k, e in c]
                                for c in attribution[:14]],
                            "local_pairs": sorted(
                                "%s|%s%d->%s%d" % ("SAME_TOKEN" if st else "CROSS_TOKEN",
                                                   k1, e1, k2, e2)
                                for st, k1, e1, k2, e2 in local),
                            "local_shapes": sorted(shapes),
                        })
            if found:
                has_delta = any(p in delta_set for p in found)
                has_comp = any(p in complement_set for p in found)
                if has_delta and has_comp:
                    ledger["both_delta_and_complement"] += 1
                    cooccurrence += 1
                elif has_delta:
                    ledger["delta_only"] += 1
                elif has_comp:
                    ledger["complement_only"] += 1
                else:
                    ledger["other_periods_only"] += 1
            else:
                ledger["no_reading"] += 1
    del bank_masks, source_masks
    return {
        "banks": bank_count, "stations": stations, "lanes": lanes,
        "clocks_swept": clocks_total,
        "clocks_expected": lanes * (bank_count + len(pairs)),
        "closed_quiescent_stretches": stretch_total,
        "longest_closed_stretch": longest_stretch,
        "period_ceiling": ceiling,
        "delta_set": delta_set, "complement_set": complement_set,
        "entry_gap_table": {str(k): v for k, v in table["entry_gap"].items()},
        "spectrum": dict(sorted(spectrum.items())),
        "complements_observed": sorted(p for p in spectrum if p in complement_set),
        "class_counts_891": class_counts_891,
        "carrier_counts_891": carrier_counts_891,
        "local_shape_counts": local_shape_counts,
        "bank_period": bank_period,
        "bank_period_sigma": bank_period_sigma,
        "unattributed": unattributed,
        "completeness_ledger": dict(ledger),
        "cooccurrence_clocks": cooccurrence,
        "anatomy": anatomy,
        "table": table,
    }


def entry_gap_incidence(cen):
    """Which (B, b) cells fire a BANK-OWNED entry-gap reading, clock-locally."""
    bank_count = cen["banks"]
    rows = {}
    for bank in range(1, bank_count - 1):
        period = 8 * (bank_count - 1 - bank)
        shapes = {shape: cen["local_shape_counts"].get((bank, period, shape), 0)
                  for shape in ENTRY_GAP_SHAPES}
        total = sum(shapes.values())
        rows[bank] = {
            "bank": bank, "entry_gap_period": period,
            "episodes_on_the_bank_clock": cen["bank_period"].get((bank, period), 0),
            "bank_owned_entry_gap_episodes": total,
            "by_shape": shapes,
            "fires": total > 0,
        }
    return rows


# ------------------------------------------------------------------ THE RULE
def rc_rows(bank_count):
    """RC as a pure function of the bank count.  Reads no corpus, ever."""
    stations = 8 * bank_count - 5
    rows = []
    for bank in range(1, bank_count - 1):
        period = 8 * (bank_count - 1 - bank)
        edge = bank_count - 2 - bank
        forward_prev = 4 + 5 * (bank - 1)
        reverse_here = 8 * bank_count - 9 - 3 * bank
        handoff_return_prev = (8 * bank_count - 9 - 3 * (bank - 1)) + 2
        forward_here = 4 + 5 * bank
        handoff_forward_here = forward_here - 2
        reverse_prev = 8 * bank_count - 9 - 3 * (bank - 1)
        rows.append({
            "bank": bank, "edge_of_the_value": edge, "period": period,
            "pair_swap_swap": [forward_prev, reverse_here],
            "pair_swap_handoff": [forward_here, handoff_return_prev],
            "pair_handoff_swap": [handoff_forward_here, reverse_prev],
            "all_three_pairs_span_the_value": (
                (reverse_here - forward_prev) % stations == period
                and (handoff_return_prev - forward_here) % stations == period
                and (reverse_prev - handoff_forward_here) % stations == period),
            "two_P": 2 * period, "stations": stations,
            "short_arc": 2 * period < stations,
            "RC_predicts_fire": bool(2 * period < stations),
        })
    return rows


def rc_firing_banks(bank_count):
    return sorted(row["bank"] for row in rc_rows(bank_count)
                  if row["RC_predicts_fire"])


def rc_firing_values(bank_count):
    return sorted(row["period"] for row in rc_rows(bank_count)
                  if row["RC_predicts_fire"])


# ------------------------------------------------------------------------ main
def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    def emit(line):
        lines.append(line)
        sys.stdout.write(line + "\n")
        sys.stdout.flush()

    header_891, blocks_891 = parse_cache(CACHE_891)
    header_891_check, blocks_891_check = parse_cache(CACHE_891_CHECK)
    receipt_891 = json.loads((ROOT / RECEIPT_891).read_text())
    receipt_891_check = json.loads((ROOT / RECEIPT_891_CHECK).read_text())
    receipt_889 = json.loads((ROOT / RECEIPT_889).read_text())
    tree_889 = ast.parse((ROOT / PRIMARY_889).read_bytes().decode())
    tree_891 = ast.parse((ROOT / PRIMARY_891).read_bytes().decode())

    def literals(tree):
        out = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        try:
                            out[target.id] = ast.literal_eval(node.value)
                        except (ValueError, TypeError):
                            pass
        return out

    literals_889 = literals(tree_889)
    literals_891 = literals(tree_891)

    # ------------------------------------------------------------ A  PINS
    pin_block = {
        "pins": PREFLIGHT_ROWS, "pin_count": len(PINS),
        "preflight": "PASS (hard-fail exit 2 on any mismatch)",
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "read_mode_for_879_881_889_891": "TEXT_AST_JSON_ONLY_BLOCKLISTED",
        "kernel_imported": CORE_719,
        "kernel_import_rationale": (
            "The Cycle-719 controller core is the SUBSTRATE under test, not a "
            "source of claims; Cycles 881, 889 and 891 import it on the same "
            "grounds.  Its own dependency is pinned too, so the whole executed "
            "surface is digest-fixed."),
        "cache_891_pins_the_worktree_runner":
            header_891.get("runner_sha256") == PREFLIGHT_ROWS[PRIMARY_891]["sha256"],
        "cache_891_check_pins_the_worktree_checker":
            header_891_check.get("runner_sha256")
            == PREFLIGHT_ROWS[CHECKER_891]["sha256"],
        "cache_891_clean_run": header_891.get("exit_code") == "0"
                               and header_891.get("status") == "ok",
        "cache_891_check_clean_run": header_891_check.get("exit_code") == "0"
                                     and header_891_check.get("status") == "ok",
        "receipt_891_files_agree_with_pins": all(
            receipt_891["files"][path]["sha256"] == PREFLIGHT_ROWS[path]["sha256"]
            and receipt_891["files"][path]["git_blob"]
            == PREFLIGHT_ROWS[path]["git_blob"]
            for path in (PRIMARY_891, CACHE_891)),
        "receipt_891_pins_889_as_this_runner_does": all(
            receipt_891["pinned_inputs"][path]["sha256"]
            == PREFLIGHT_ROWS[path]["sha256"]
            for path in (PRIMARY_889, CHECKER_889, RECEIPT_889, CACHE_889,
                         PRIMARY_881, PRIMARY_879, CORE_719, CORE_719_HANDSHAKE)),
        "891_checker_verdict_on_891": receipt_891_check.get(
            "checker_verdict_block", {}),
        "891_blocks_parsed": sorted(blocks_891),
        "891_checker_blocks_parsed": sorted(blocks_891_check),
        "detector_constants_match_pinned_889_and_891": (
            literals_889.get("MIN_PERIOD_REPEATS") == MIN_PERIOD_REPEATS
            and literals_889.get("MIN_STABLE_EVENTS") == MIN_STABLE_EVENTS
            and literals_889.get("PINNED_PERIOD_CEILING") == PINNED_PERIOD_CEILING
            and literals_889.get("HORIZON") == HORIZON
            and literals_891.get("MIN_PERIOD_REPEATS") == MIN_PERIOD_REPEATS
            and literals_891.get("MIN_STABLE_EVENTS") == MIN_STABLE_EVENTS
            and literals_891.get("PINNED_PERIOD_CEILING") == PINNED_PERIOD_CEILING
            and literals_891.get("HORIZON") == HORIZON
            and literals_891.get("TOKEN_K") == TOKEN_K
            and literals_891.get("EVENT_COUNT") == EVENT_COUNT),
        "891_class_priority_from_ast": literals_891.get("CLASS_PRIORITY"),
        "891_class_priority_matches_this_reimplementation":
            tuple(literals_891.get("CLASS_PRIORITY") or ()) == CLASS_PRIORITY,
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(
            not Path(p).is_absolute() for p in AUDIT_INPUT_PATHS),
        "disclosed_deviations": list(DISCLOSED_DEVIATIONS),
        "shape_inventory_statement": SHAPE_INVENTORY_STATEMENT,
        "realization_condition_statement": RC_STATEMENT,
        "bookkeeping_statement": BOOKKEEPING_STATEMENT,
        "detector_statement": DETECTOR_STATEMENT,
    }
    a_pass = (
        not pin_block["blocklisted_modules_loaded"]
        and not pin_block["firewall_hits"]
        and pin_block["cache_891_pins_the_worktree_runner"]
        and pin_block["cache_891_check_pins_the_worktree_checker"]
        and pin_block["cache_891_clean_run"]
        and pin_block["cache_891_check_clean_run"]
        and pin_block["receipt_891_files_agree_with_pins"]
        and pin_block["receipt_891_pins_889_as_this_runner_does"]
        and pin_block["detector_constants_match_pinned_889_and_891"]
        and pin_block["891_class_priority_matches_this_reimplementation"]
        and pin_block["audit_input_paths_repo_relative"]
        and {"G_HOLDOUT_B67", "H_NONTWORUN_B7", "F_DERIVATION_B45"} <= set(blocks_891))
    emit(("PASS" if a_pass else "FAIL") + " A_PINS :: "
                 + json.dumps(pin_block, **dumps))
    if not a_pass:
        return 1

    # -------------------------------------------- B  GEOMETRY + SHAPE INVENTORY
    geometry_rows, shape_bad, geom_bad = [], 0, 0
    for bank_count in range(3, 13):
        table = station_table(bank_count)
        stations = table["stations"]
        ok = (stations == 8 * bank_count - 5
              and all(v == 4 + 5 * e for e, v in table["forward"].items())
              and all(v == 8 * bank_count - 9 - 3 * e
                      for e, v in table["reverse"].items())
              and all(table["handoff_forward"][e] == table["forward"][e] - 2
                      for e in table["forward"])
              and all(table["handoff_return"][e] == table["reverse"][e] + 2
                      for e in table["reverse"])
              and all(g == 8 * (bank_count - 1 - b)
                      for b, g in table["entry_gap"].items())
              and table["malformed"] == 0)
        geom_bad += not ok
        per_bank = {}
        for bank in range(bank_count):
            inv = bank_owned_shape_inventory(bank_count, bank, table)
            entry = inv["entry_gap_value"]
            comps = set(inv["complement_values"])
            realising = {sep: sorted({row[6] for row in rows})
                         for sep, rows in inv["separations"].items()
                         if sep in comps}
            entry_pairs = sorted(
                "%s%d->%s%d" % (row[1], row[2], row[4], row[5])
                for sep, rows in inv["separations"].items() if sep == entry
                for row in rows if row[6] in ENTRY_GAP_SHAPES)
            interior = 1 <= bank <= bank_count - 2
            expect = 3 if interior else 0
            if len(entry_pairs) != expect:
                shape_bad += 1
            # the only complement-valued same-token shapes are the named ones
            for sep, shapes in realising.items():
                for shape in shapes:
                    if shape not in ("SAME_EDGE_COMPLEMENT", "REVERSE_PAIR",
                                     "HANDOFF_RETURN_PAIR", "OTHER",
                                     *ENTRY_GAP_SHAPES):
                        shape_bad += 1
            per_bank[bank] = {
                "entry_gap_value": entry,
                "entry_gap_pairs": entry_pairs,
                "entry_gap_pair_count": len(entry_pairs),
                "n_minus_three_shapes": sorted(
                    {row[6] for sep, rows in inv["separations"].items()
                     if sep == stations - 3 for row in rows
                     if row[6] in ("REVERSE_PAIR", "HANDOFF_RETURN_PAIR")}),
                "same_edge_complements": sorted(
                    sep for sep, rows in inv["separations"].items()
                    if any(row[6] == "SAME_EDGE_COMPLEMENT" for row in rows)),
            }
        geometry_rows.append({
            "banks": bank_count, "stations": stations,
            "geometry_ok": ok,
            "entry_gap_measured": {str(b): g for b, g in table["entry_gap"].items()},
            "per_bank": {str(b): v for b, v in per_bank.items()},
        })
    # determinism of the program build and of a tiny corpus
    twice = [digest([[list(K.interleaved_program(bc)[i][:2])
                      for i in range(len(K.interleaved_program(bc)))]
                     for bc in range(3, 9)]) for _ in range(2)]
    corpus_twice = []
    for _ in range(2):
        probe = build_corpus(3, 64)
        corpus_twice.append(digest({
            "keys": [list(k[1]) for k in probe["keys"]],
            "clean": [[probe["clean_planes"][b][t] for t in range(0, 65, 8)]
                      for b in range(3)],
            "source": [probe["source_clean"][t] for t in range(0, 65, 8)]}))
    del probe
    geometry_block = {
        "rows": geometry_rows,
        "bank_counts_checked": list(range(3, 13)),
        "geometry_disagreements": geom_bad,
        "shape_inventory_disagreements": shape_bad,
        "derivation": (
            "f(b-1) -> r(b) : (8B-9-3b) - (4+5(b-1)) = 8(B-1-b).  "
            "f(b) -> h_r(b-1) : (8B-9-3(b-1)+2) - (4+5b) = 8(B-1-b).  "
            "h_f(b) -> r(b-1) : (8B-9-3(b-1)) - (4+5b-2) = 8(B-1-b).  "
            "r(b-1) -> r(b) and h_r(b-1) -> h_r(b) both span -3 = N-3 = 8(B-1).  "
            "r(e) -> f(e) spans N - DELTA(B,e) = 8(e+1) on each incident edge.  "
            "Everything else among a bank's own eight rows is not a multiple of 8 "
            "and so is not a ring complement."),
        "program_double_build_digest": twice[0],
        "program_double_build_deterministic": twice[0] == twice[1],
        "corpus_double_build_digest": corpus_twice[0],
        "corpus_double_build_deterministic": corpus_twice[0] == corpus_twice[1],
        "statement": SHAPE_INVENTORY_STATEMENT,
    }
    b_pass = (geom_bad == 0 and shape_bad == 0
              and geometry_block["program_double_build_deterministic"]
              and geometry_block["corpus_double_build_deterministic"])
    emit(("PASS" if b_pass else "FAIL") + " B_GEOMETRY_AND_SHAPES :: "
                 + json.dumps(geometry_block, **dumps))

    # --------------------------------------------------- C  DETECTOR SEMANTICS
    def synthetic(pattern, repeats):
        word, length = 0, 0
        for _ in range(repeats):
            for bit in pattern:
                if bit:
                    word |= 1 << length
                length += 1
        return word, length

    known_rows = []
    for period, clean in ((7, 4), (11, 6), (13, 5), (19, 11), (24, 17), (31, 20)):
        pattern = [1] * clean + [0] * (period - clean)
        word, _length = synthetic(pattern, 8)
        found = tail_periods(word, range(2, 96))
        known_rows.append({"period": period, "detected": period in found})
    rng = random.Random(922922)
    fold_bad = 0
    for _ in range(4000):
        bits = rng.randrange(40, 400)
        word = rng.getrandbits(bits) | (1 << (bits - 1))
        ps = range(2, 40)
        if tail_periods(word, ps) != reference_tail_periods(word, ps):
            fold_bad += 1
    impostors = []
    for period, clean, damage in ((11, 6, 40), (13, 5, 33), (19, 11, 60)):
        pattern = [1] * clean + [0] * (period - clean)
        word, _length = synthetic(pattern, 8)
        broken = word ^ (1 << damage)
        got = tail_periods(broken, [period])
        impostors.append({"period": period, "damaged_tick": damage,
                          "refused_before_the_damage":
                              period not in got or got[period][0] > damage})
    detector_block = {
        "known_period_rows": known_rows,
        "all_known_periods_detected": all(r["detected"] for r in known_rows),
        "residue_fold_equivalence_cases": 4000,
        "residue_fold_equivalence_failures": fold_bad,
        "impostors": impostors,
        "all_impostors_refused": all(r["refused_before_the_damage"]
                                     for r in impostors),
        "statement": DETECTOR_STATEMENT,
    }
    c_pass = (detector_block["all_known_periods_detected"] and fold_bad == 0
              and detector_block["all_impostors_refused"])
    emit(("PASS" if c_pass else "FAIL") + " C_DETECTOR :: "
                 + json.dumps(detector_block, **dumps))

    # -------------------------------- D  RESTRICTION: reproduce Cycle 891 exactly
    censuses = {}
    for bank_count in DERIVATION_BANKS:
        box = build_corpus(bank_count, HORIZON)
        censuses[bank_count] = census(box)
        del box

    holdout_891 = {int(row["banks"]): row for row in blocks_891["G_HOLDOUT_B67"]["rows"]}
    derivation_891 = receipt_891["derivation_tiers"]
    restriction_rows, restriction_bad = [], 0
    for bank_count in DERIVATION_BANKS:
        cen = censuses[bank_count]
        cc = {"%d|%s" % k: v for k, v in cen["class_counts_891"].items()}
        carriers = {"%d|%s" % k: dict(sorted(v.items()))
                    for k, v in cen["carrier_counts_891"].items()}
        row = {"banks": bank_count, "stations": cen["stations"],
               "lanes": cen["lanes"], "clocks_swept": cen["clocks_swept"],
               "every_clock_classified":
                   cen["clocks_swept"] == cen["clocks_expected"],
               "closed_quiescent_stretches": cen["closed_quiescent_stretches"],
               "longest_closed_stretch": cen["longest_closed_stretch"],
               "complements_observed": cen["complements_observed"],
               "class_counts_891": dict(sorted(cc.items())),
               "cooccurrence_clocks": cen["cooccurrence_clocks"],
               "completeness_ledger": cen["completeness_ledger"],
               "entry_gap_table": cen["entry_gap_table"]}
        checks = {}
        if str(bank_count) in derivation_891:
            pinned = derivation_891[str(bank_count)]
            checks["complement_source_classes"] = (
                {k: v for k, v in cc.items()
                 if int(k.split("|")[0]) in cen["complement_set"]}
                == pinned["complement_source_classes"])
            checks["completeness_ledger"] = (
                cen["completeness_ledger"] == pinned["completeness_ledger"])
            checks["cooccurrence_clocks"] = (
                cen["cooccurrence_clocks"] == pinned["cooccurrence_clocks"])
            checks["closed_quiescent_stretches"] = (
                cen["closed_quiescent_stretches"]
                == pinned["closed_quiescent_stretches"])
            checks["clocks_swept"] = cen["clocks_swept"] == pinned["clocks_swept"]
            measured_eg = defaultdict(dict)
            for key, banks in cen["carrier_counts_891"].items():
                period, label = key
                if label == "RELAY_ENTRY_GAP":
                    measured_eg[str(period)] = dict(sorted(
                        (str(b), n) for b, n in banks.items()))
            checks["entry_gap_carrier_banks_measured"] = (
                dict(measured_eg) == pinned["entry_gap_carrier_banks_measured"])
            checks["entry_gap_table"] = (
                cen["entry_gap_table"] == pinned["entry_gap_table"])
        if bank_count in holdout_891:
            pinned = holdout_891[bank_count]
            observed = {str(p): cen["spectrum"].get(p, 0)
                        for p in cen["complement_set"]}
            checks["observed_episode_counts"] = (
                observed == pinned["observed_episode_counts"])
            checks["closed_quiescent_stretches_holdout"] = (
                cen["closed_quiescent_stretches"]
                == pinned["closed_quiescent_stretches"])
            checks["clocks_swept_holdout"] = (
                cen["clocks_swept"] == pinned["clocks_swept"])
            checks["cooccurrence_clocks_holdout"] = (
                cen["cooccurrence_clocks"] == pinned["cooccurrence_clocks"])
            checks["completeness_ledger_holdout"] = (
                cen["completeness_ledger"] == pinned["completeness_ledger"])
            checks["longest_closed_stretch"] = (
                cen["longest_closed_stretch"] == pinned["longest_closed_stretch"])
            verify = {}
            for period_s, block in pinned["carrier_verification"].items():
                period = int(period_s)
                got = dict(sorted(
                    (str(b), n) for b, n in
                    cen["carrier_counts_891"].get(
                        (period, "RELAY_ENTRY_GAP"), Counter()).items()))
                verify[period_s] = got == block["measured_entry_gap_banks"]
            checks["carrier_verification_entry_gap_banks"] = all(verify.values())
            checks["carrier_verification_rows"] = verify
            checks["P32_has_no_entry_gap_episode"] = (
                cen["class_counts_891"].get((32, "RELAY_ENTRY_GAP"), 0) == 0
                if 32 in cen["complement_set"] else None)
            checks["P32_edge_complement_episodes"] = (
                cen["class_counts_891"].get((32, "RELAY_EDGE_COMPLEMENT"), 0))
        row["restriction_checks"] = checks
        bad = [k for k, v in checks.items()
               if isinstance(v, bool) and not v]
        row["failed_checks"] = bad
        restriction_bad += len(bad)
        restriction_rows.append(row)
    b7 = censuses[7]
    restriction_block = {
        "rows": restriction_rows,
        "total_failed_checks": restriction_bad,
        "pinned_891_B7_residuals": holdout_891[7]["residual_episode_counts"],
        "reproduced_B7_residuals": {
            "40": b7["spectrum"].get(40, 0), "48": b7["spectrum"].get(48, 0)},
        "pinned_891_B7_32_is_edge_complement_only": (
            holdout_891[7]["carrier_verification"]["32"]["measured_entry_gap_banks"]
            == {}),
        "reproduced_B7_32_is_edge_complement_only": (
            b7["class_counts_891"].get((32, "RELAY_ENTRY_GAP"), 0) == 0
            and b7["class_counts_891"].get((32, "RELAY_EDGE_COMPLEMENT"), 0) > 0),
        "note": (
            "This gate is a hard restriction: every published Cycle-891 number "
            "that this cycle builds on is recomputed from a fresh corpus and "
            "compared value for value before any new number is produced."),
    }
    d_pass = (restriction_bad == 0
              and restriction_block["reproduced_B7_32_is_edge_complement_only"]
              and restriction_block["reproduced_B7_residuals"]
                  == {k: v for k, v in
                      ((k, int(v)) for k, v in
                       holdout_891[7]["residual_episode_counts"].items())})
    emit(("PASS" if d_pass else "FAIL") + " D_RESTRICTION_891 :: "
                 + json.dumps(restriction_block, **dumps))

    # ------------------------------------------------- E  THE P=32 ANATOMY (Q1)
    stations7 = b7["stations"]
    table7 = b7["table"]
    p32_bank_rows = {}
    for bank in range(7):
        n = b7["bank_period"].get((bank, 32), 0)
        if not n:
            continue
        shapes = {s: c for (bk, p, s), c in b7["local_shape_counts"].items()
                  if bk == bank and p == 32}
        p32_bank_rows[str(bank)] = {
            "episodes_on_the_bank_clock": n,
            "sigmas": dict(sorted(b7["bank_period_sigma"][(bank, 32)].items())),
            "local_shapes": dict(sorted(shapes.items())),
            "unattributed": b7["unattributed"].get((bank, 32), 0),
        }
    carriers32 = dict(sorted(
        b7["carrier_counts_891"][(32, "RELAY_EDGE_COMPLEMENT")].items()))
    # the bookkeeping identity, checked on every attributed pair of every
    # anatomy row this cycle publishes
    identity_checked, identity_bad = 0, 0
    for (bank, period), rows_ in b7["anatomy"].items():
        for row in rows_:
            positions = row["token_positions"]
            starts = row["run_start_ticks"]
            attribution = attribute_runs(
                starts, tuple(positions), table7["rows_of_bank"][bank], stations7)
            for i in range(len(starts) - 1):
                delta_t = starts[i + 1] - starts[i]
                for p1, s1, _k1, _e1 in attribution[i]:
                    for p2, s2, _k2, _e2 in attribution[i + 1]:
                        identity_checked += 1
                        if (s2 - s1) % stations7 != (delta_t + (p2 - p1)) % stations7:
                            identity_bad += 1
    entry_gap_pairs_32 = sorted(
        "%s%d->%s%d" % (row[1], row[2], row[4], row[5])
        for row in bank_owned_shape_inventory(7, 2, table7)["separations"].get(32, [])
        if row[6] in ENTRY_GAP_SHAPES)
    anatomy_block = {
        "question": "why is the entry-gap route absent for P=32 at B=7?",
        "P32_episodes_total_891_label": dict(sorted(
            {"%s" % lab: c for (p, lab), c in b7["class_counts_891"].items()
             if p == 32}.items())),
        "P32_bank_clock_rows": p32_bank_rows,
        "banks_that_read_P32": sorted(int(k) for k in p32_bank_rows),
        "bank2_reads_P32": "2" in p32_bank_rows,
        "any_clock_containing_bank2_reads_P32": any(
            2 in banks for (p, _lab), banks in b7["carrier_counts_891"].items()
            if p == 32),
        "member_banks_of_every_clock_that_reads_P32": sorted(
            {b for (p, _lab), banks in b7["carrier_counts_891"].items()
             if p == 32 for b in banks}),
        "P32_891_edge_complement_carrier_banks": carriers32,
        "P32_carrier_bank_required_by_the_entry_gap": 7 - 2 - 3,
        "bank2_entry_gap_value_at_B7": table7["entry_gap"][2],
        "bank2_owns_the_value_32_through": entry_gap_pairs_32,
        "the_answer": (
            "The entry-gap route for P=32 at B=7 is absent for the plainest "
            "possible reason and NOT because the separation is alignment-"
            "forbidden the way 8(B-1) is.  Bank 2 owns the value 32 through all "
            "three entry-gap row pairs -- the geometry is intact -- but NO CLOCK "
            "CONTAINING BANK 2 READS THE PERIOD 32 AT ALL, in any stretch, in any "
            "lane, at any sigma.  Since 891's classifier gives RELAY_ENTRY_GAP "
            "top priority and the label attaches to any clock containing the "
            "carrier bank, zero bank-2 readings is exactly zero entry-gap labels. "
            "The 276 episodes that do fire are read on banks 0 and 4 (and the "
            "pair clocks containing them): on bank 4 the clock-local attribution "
            "is the SAME-EDGE COMPLEMENT r(3) -> f(3) of edge 3, which bank 4 is "
            "incident to, and on bank 0 it is the cross-token separation "
            "N - sigma = 51 - 19 = 32.  The reason bank 2 cannot read 32 is "
            "RC-2: 2*32 = 64 > 51 = N, so bank 2's entry gap is the LONG arc of "
            "its own two dwell residues and no P-shift-exact stable region of "
            "the required length 2P+1 = 65 can close."),
        "bookkeeping_identity_pairs_checked": identity_checked,
        "bookkeeping_identity_violations": identity_bad,
        "bookkeeping_statement": BOOKKEEPING_STATEMENT,
        "sample_anatomies": {
            "bank4_P32": b7["anatomy"].get((4, 32), [])[:3],
            "bank0_P32": b7["anatomy"].get((0, 32), [])[:2],
        },
    }
    e_pass = (not anatomy_block["bank2_reads_P32"]
              and not anatomy_block["any_clock_containing_bank2_reads_P32"]
              and identity_bad == 0 and identity_checked > 0
              and len(entry_gap_pairs_32) == 3
              and len(anatomy_block["banks_that_read_P32"]) > 0)
    emit(("PASS" if e_pass else "FAIL") + " E_P32_ANATOMY :: "
                 + json.dumps(anatomy_block, **dumps))

    # -------------------------------------- F  THE RC, DERIVED AND THEN SEALED
    incidence = {bc: entry_gap_incidence(censuses[bc]) for bc in DERIVATION_BANKS}
    fit_rows, fit_bad = [], 0
    for bc in DERIVATION_BANKS:
        for bank, row in sorted(incidence[bc].items()):
            predicted = 2 * row["entry_gap_period"] < 8 * bc - 5
            agree = predicted == row["fires"]
            fit_bad += not agree
            fit_rows.append({"banks": bc, **row, "RC_predicts_fire": predicted,
                             "agrees": agree})
    seal_payload = {
        "rule_text": RC_STATEMENT,
        "shape_text": SHAPE_INVENTORY_STATEMENT,
        "predicted_firing_banks": {str(bc): rc_firing_banks(bc)
                                   for bc in (8, 9, 10, 11, 12)},
        "predicted_firing_values": {str(bc): rc_firing_values(bc)
                                    for bc in (8, 9, 10, 11, 12)},
        "predicted_rows": {str(bc): rc_rows(bc) for bc in (8, 9, 10, 11, 12)},
    }
    SEAL = digest(seal_payload)
    seal_build_log = [dict(row) for row in BUILD_LOG]
    rc_block = {
        "statement": RC_STATEMENT,
        "fit_rows": fit_rows,
        "fit_cells": len(fit_rows),
        "fit_disagreements": fit_bad,
        "fitted_on": list(DERIVATION_BANKS),
        "necessity_holds_on_every_fitted_cell": all(
            (not r["fires"]) or r["RC_predicts_fire"] for r in fit_rows),
        "derivation_status": {
            "RC_1": "derived -- pure station arithmetic, exhaustive over B=3..12 "
                    "in gate B, zero disagreeing rows",
            "RC_2": "closed form FITTED to the clock-local incidence at B=4..7 "
                    "(14 cells), then sealed and held out at B=8; the mechanism "
                    "sketch (the entry gap must be the short arc of the bank's "
                    "own two dwell residues) is a derivation for the "
                    "single-token orbit word only -- with two tokens a bank can "
                    "carry more than two dwell residues, which is exactly why "
                    "the SAME-EDGE COMPLEMENT shape is readable at 2P > N and "
                    "the entry-gap shape is not.  Status: fitted-then-sealed, "
                    "not derived.",
            "RC_3": "declared boundary, measured -- the residual sufficiency "
                    "failure is stretch-local in Cycle 891's own declared sense",
        },
        "SEAL_sha256": SEAL,
        "build_log_at_seal_time": seal_build_log,
        "build_log_at_seal_time_is_holdout_free": all(
            row["banks"] not in HOLDOUT_BANKS and row["banks"] not in NEVER_BUILT_BANKS
            for row in seal_build_log),
        "seal_predicts": seal_payload["predicted_firing_banks"],
        "seal_discipline": (
            "The seal is a digest of the rule TEXT plus the rule's pure-function "
            "output at B = 8, 9, 10, 11, 12.  It is computed and printed here, "
            "before any B=8 corpus exists in this process; BUILD_LOG at seal time "
            "is published above and contains only the B=3 determinism probe and "
            "the B=4..7 derivation tiers.  Re-digesting after the holdout "
            "reproduces it byte for byte (gate G)."),
    }
    f_pass = (fit_bad == 0 and rc_block["build_log_at_seal_time_is_holdout_free"]
              and rc_block["necessity_holds_on_every_fitted_cell"])
    emit(("PASS" if f_pass else "FAIL") + " F_RC_DERIVED_AND_SEALED :: "
                 + json.dumps(rc_block, **dumps))

    # ------------------------------------------------------ G  HOLDOUT AT B=8
    holdout_rows = {}
    for bank_count in HOLDOUT_BANKS:
        box = build_corpus(bank_count, HORIZON)
        cen = census(box)
        del box
        inc = entry_gap_incidence(cen)
        rows = []
        for bank, row in sorted(inc.items()):
            predicted = 2 * row["entry_gap_period"] < 8 * bank_count - 5
            rows.append({**row, "RC_predicts_fire": predicted,
                         "agrees": predicted == row["fires"]})
        cc = {"%d|%s" % k: v for k, v in cen["class_counts_891"].items()}
        holdout_rows[str(bank_count)] = {
            "banks": bank_count, "stations": cen["stations"],
            "lanes": cen["lanes"], "clocks_swept": cen["clocks_swept"],
            "every_clock_classified": cen["clocks_swept"] == cen["clocks_expected"],
            "closed_quiescent_stretches": cen["closed_quiescent_stretches"],
            "entry_gap_table": cen["entry_gap_table"],
            "complements_observed": cen["complements_observed"],
            "spectrum_at_the_complement_values": {
                str(p): cen["spectrum"].get(p, 0) for p in cen["complement_set"]},
            "class_counts_891": dict(sorted(cc.items())),
            "carrier_counts_891_entry_gap": {
                str(p): dict(sorted(v.items()))
                for (p, lab), v in cen["carrier_counts_891"].items()
                if lab == "RELAY_ENTRY_GAP"},
            "RC_rows": rows,
            "RC_agreements": sum(r["agrees"] for r in rows),
            "RC_cells": len(rows),
            "RC_false_negatives": [r["bank"] for r in rows
                                   if r["fires"] and not r["RC_predicts_fire"]],
            "RC_false_positives": [r["bank"] for r in rows
                                   if r["RC_predicts_fire"] and not r["fires"]],
            "the_891_label_would_have_said": {
                str(p): dict(sorted(v.items()))
                for (p, lab), v in cen["carrier_counts_891"].items()
                if lab == "RELAY_ENTRY_GAP"},
            "local_shape_counts_at_the_complement_values": {
                "b%d|P%d|%s" % k: v
                for k, v in sorted(cen["local_shape_counts"].items())
                if k[1] in cen["complement_set"]},
        }
        censuses[bank_count] = cen
    reseal = digest(seal_payload)
    holdout_block = {
        "rows": holdout_rows,
        "SEAL_sha256": SEAL,
        "SEAL_recomputed_after_the_holdout": reseal,
        "seal_unchanged": reseal == SEAL,
        "build_log_at_seal_time": seal_build_log,
        "build_log_final": [dict(row) for row in BUILD_LOG],
        "seal_predates_the_holdout_corpus": all(
            row["banks"] not in HOLDOUT_BANKS for row in seal_build_log),
        "B9_and_up_never_built_by_this_runner": all(
            row["banks"] not in NEVER_BUILT_BANKS for row in BUILD_LOG),
        "B9_prediction_for_the_checker": {
            "stations": 8 * 9 - 5,
            "firing_banks": rc_firing_banks(9),
            "firing_entry_gap_values": rc_firing_values(9),
            "non_firing_banks": [row["bank"] for row in rc_rows(9)
                                 if not row["RC_predicts_fire"]],
            "marginal_cell_flagged_in_advance": {
                "bank": 9 - 2, "period": 8,
                "why": ("the b = B-2 cell is the one RC-3 puts at risk: it fired "
                        "at B=4,5,6,7 with 492, 1368, 506 and 8 episodes and did "
                        "NOT fire at B=8, a monotone decline this rule does not "
                        "model")},
        },
        "worker_disclosure": DISCLOSED_DEVIATIONS[4],
    }
    g_pass = (holdout_block["seal_unchanged"]
              and holdout_block["seal_predates_the_holdout_corpus"]
              and holdout_block["B9_and_up_never_built_by_this_runner"]
              and all(r["every_clock_classified"] for r in holdout_rows.values()))
    emit(("PASS" if g_pass else "FAIL") + " G_HOLDOUT_B8 :: "
                 + json.dumps(holdout_block, **dumps))

    # ------------------------------------------------- H  THE 40/48 RESIDUALS
    residual_rows = {}
    for period in (40, 48):
        banks = {}
        for bank in range(7):
            n = b7["bank_period"].get((bank, period), 0)
            if not n:
                continue
            shapes = {s: c for (bk, p, s), c in b7["local_shape_counts"].items()
                      if bk == bank and p == period}
            inv = bank_owned_shape_inventory(7, bank, table7)
            banks[str(bank)] = {
                "episodes": n,
                "sigmas": dict(sorted(b7["bank_period_sigma"][(bank, period)].items())),
                "local_shapes": dict(sorted(shapes.items())),
                "bank_owns_the_value_through": sorted(
                    "%s%d->%s%d|%s" % (row[1], row[2], row[4], row[5], row[6])
                    for row in inv["separations"].get(period, [])),
                "anatomy": b7["anatomy"].get((bank, period), [])[:2],
                "ring_form_I_max": krun_imax(
                    stations7,
                    [t % stations7 for t in
                     (b7["anatomy"].get((bank, period), [{}])[0] or {}).get(
                         "run_start_ticks", [])],
                    period),
            }
        residual_rows[str(period)] = {
            "period": period,
            "891_label": dict(sorted(
                {lab: c for (p, lab), c in b7["class_counts_891"].items()
                 if p == period}.items())),
            "bank_clock_rows": banks,
            "two_P_vs_N": [2 * period, stations7],
            "RC2_short_arc": 2 * period < stations7,
        }
    residual_block = {
        "rows": residual_rows,
        "verdict": (
            "NOT A FOURTH SHAPE.  Clock-locally both residual families are the "
            "SAME-EDGE COMPLEMENT r(e) -> f(e), same token, read on a bank "
            "incident to that edge: P=40 = N - DELTA(7,4) on bank 4 through "
            "r(4) -> f(4), and P=48 = N - DELTA(7,5) on bank 6 through "
            "r(5) -> f(5).  They are 'residuals' only relative to Cycle 891's "
            "RULE, which predicts the ENTRY-GAP route and treats every other "
            "route as residue; the three-shape census did not mis-bin them (891 "
            "labelled both RELAY_EDGE_COMPLEMENT, which is right), it simply had "
            "no rule for that route.  Their rarity is the same short-arc fact "
            "that RC-2 names: 2*40 = 80 and 2*48 = 96 both exceed N = 51, so no "
            "ring-periodic reading of either value can close, and only "
            "stretch-local (finite-form) readings survive -- which is exactly "
            "891's own finding that the ring form refuses both witnesses while "
            "the finite form is exact on them.  A derived rule now covers all "
            "four episodes: a complement value with 2P >= N is readable ONLY "
            "stretch-locally and therefore only in ones and twos."),
        "coverage": "4 of 4 residual episodes at B=7 (2 at P=40, 2 at P=48)",
        "still_open": (
            "WHY a particular stretch carries the truncated word that admits "
            "the finite-form reading remains dynamical -- 891's declared "
            "boundary, untouched here."),
    }
    h_pass = all(
        any(row["local_shapes"].get("SAME_EDGE_COMPLEMENT", 0) > 0
            for row in residual_rows[str(period)]["bank_clock_rows"].values())
        for period in (40, 48))
    emit(("PASS" if h_pass else "FAIL") + " H_RESIDUALS_40_48 :: "
                 + json.dumps(residual_block, **dumps))

    # -------------------------------------------------------------- J  TEETH
    teeth = []

    # T1 tampered pin
    payload = (ROOT / RECEIPT_891).read_bytes()
    tampered = payload[:-1] + bytes([payload[-1] ^ 0x01])
    teeth.append({"tooth": "tampered_pin_is_caught",
                  "fires": sha256(tampered).hexdigest() != PINS[RECEIPT_891][0]
                           and git_blob(tampered) != PINS[RECEIPT_891][1]})

    # T2 planted entry-gap P=32 episode at B=7 must flip the anatomy verdict
    planted_starts = [1000, 1000 + 32]
    planted_positions = (0, 20)
    planted_attr = attribute_runs(planted_starts, planted_positions,
                                  table7["rows_of_bank"][2], stations7)
    # choose the token phase that puts the first start on f(1) and the second on r(2)
    plant_found = False
    for base in range(stations7):
        starts = [base, base + 32]
        attr = attribute_runs(starts, planted_positions,
                              table7["rows_of_bank"][2], stations7)
        local = local_pairs_for_period(starts, attr, 32)
        shapes = {shape_of_local_pair(p, 2, 7) for p in local}
        if shapes & set(ENTRY_GAP_SHAPES):
            plant_found = True
            break
    teeth.append({"tooth": "planted_bank2_entry_gap_P32_flips_the_verdict",
                  "fires": plant_found and not anatomy_block["bank2_reads_P32"],
                  "detail": ("a synthetic bank-2 run-start pair separated by 32 is "
                             "classified ENTRY_GAP by the same code path that "
                             "returns nothing on the real corpus, so the absence "
                             "measured in gate E is a fact about the substrate, "
                             "not about the classifier"),
                  "planted_attribution": [
                      ["p%d@s%d:%s%d" % (p, s, k, e) for p, s, k, e in c]
                      for c in planted_attr]})

    # T3 tampered seal
    tampered_seal = digest({**seal_payload, "rule_text": RC_STATEMENT + " "})
    teeth.append({"tooth": "tampered_seal_is_caught",
                  "fires": tampered_seal != SEAL})

    # T4/T5 perturbed RC must break on controls
    def perturbed_fire(bank_count, bank, slack):
        return 2 * (8 * (bank_count - 1 - bank)) < 8 * bank_count - 5 + slack

    controls = []
    for slack in (8, -8):
        bad = 0
        for bc in list(DERIVATION_BANKS) + list(HOLDOUT_BANKS):
            for bank, row in sorted(entry_gap_incidence(censuses[bc]).items()):
                if perturbed_fire(bc, bank, slack) != row["fires"]:
                    bad += 1
        controls.append({"slack": slack, "cells_broken": bad})
    teeth.append({"tooth": "perturbed_RC2_breaks_on_controls",
                  "fires": all(c["cells_broken"] > 0 for c in controls),
                  "controls": controls})

    # T6 dropping the pair clocks must break the 891 restriction
    bank_only = Counter()
    for (period, label), n in b7["class_counts_891"].items():
        bank_only[(period, label)] = n
    dropped_ok = True
    for (period, label), banks in b7["carrier_counts_891"].items():
        if label != "RELAY_ENTRY_GAP":
            continue
        pinned = holdout_891[7]["carrier_verification"].get(str(period))
        if pinned is None:
            continue
        only_single = {str(b): n for b, n in banks.items()
                       if b == 7 - 2 - (period // 8 - 1)}
        if only_single == pinned["measured_entry_gap_banks"]:
            dropped_ok = False
    teeth.append({"tooth": "dropped_pair_clock_family_breaks_the_restriction",
                  "fires": dropped_ok})

    # T7 hardcoded shape row: a two-pair entry-gap inventory must fail gate B
    two_pair_bad = 0
    for bc in range(4, 13):
        tbl = station_table(bc)
        for bank in range(1, bc - 1):
            inv = bank_owned_shape_inventory(bc, bank, tbl)
            pairs_ = [row for row in inv["separations"][8 * (bc - 1 - bank)]
                      if row[6] in ENTRY_GAP_SHAPES]
            if len(pairs_) != 3:
                two_pair_bad += 1
    teeth.append({"tooth": "hardcoded_two_pair_inventory_would_fail",
                  "fires": two_pair_bad == 0,
                  "detail": "every interior bank at B=4..12 carries exactly three "
                            "entry-gap row pairs, so a two-pair claim is refuted"})

    # T8 falsifier visibility: an out-of-set period must be detectable
    pattern = [1] * 12 + [0] * 11
    word, _ = synthetic(pattern, 9)
    seen = tail_periods(word, range(2, 96))
    teeth.append({"tooth": "out_of_set_period_is_visible",
                  "fires": 23 in seen and 23 not in b7["delta_set"]
                           and 23 not in b7["complement_set"],
                  "planted_period": 23})

    # T9 bookkeeping identity perturbation must fail everywhere
    perturb_bad = 0
    perturb_total = 0
    for (bank, period), rows_ in b7["anatomy"].items():
        for row in rows_[:2]:
            positions = row["token_positions"]
            starts = row["run_start_ticks"]
            attribution = attribute_runs(starts, tuple(positions),
                                         table7["rows_of_bank"][bank], stations7)
            for i in range(len(starts) - 1):
                delta_t = starts[i + 1] - starts[i]
                for p1, s1, _k, _e in attribution[i]:
                    for p2, s2, _k2, _e2 in attribution[i + 1]:
                        perturb_total += 1
                        if (s2 - s1) % stations7 == (delta_t + (p2 - p1) + 1) % stations7:
                            perturb_bad += 1
    teeth.append({"tooth": "perturbed_bookkeeping_identity_fails",
                  "fires": perturb_total > 0 and perturb_bad < perturb_total,
                  "pairs": perturb_total, "still_satisfied": perturb_bad})

    # T10 fake anatomy: claiming P=40 is an entry-gap pair must be refutable
    inv40 = bank_owned_shape_inventory(7, 4, table7)["separations"].get(40, [])
    teeth.append({"tooth": "fake_entry_gap_claim_for_P40_is_refuted",
                  "fires": not any(row[6] in ENTRY_GAP_SHAPES for row in inv40)
                           and any(row[6] == "SAME_EDGE_COMPLEMENT" for row in inv40),
                  "shapes_bank4_owns_at_40": sorted({row[6] for row in inv40})})

    teeth_block = {"teeth": teeth, "count": len(teeth),
                   "all_fire": all(t["fires"] for t in teeth)}
    j_pass = teeth_block["all_fire"]
    emit(("PASS" if j_pass else "FAIL") + " J_TEETH :: "
                 + json.dumps(teeth_block, **dumps))

    # ------------------------------------------------------------ K  VERDICT
    elapsed = time.monotonic() - started
    gate_flags = {"A_PINS": a_pass, "B_GEOMETRY_AND_SHAPES": b_pass,
                  "C_DETECTOR": c_pass, "D_RESTRICTION_891": d_pass,
                  "E_P32_ANATOMY": e_pass, "F_RC_DERIVED_AND_SEALED": f_pass,
                  "G_HOLDOUT_B8": g_pass, "H_RESIDUALS_40_48": h_pass,
                  "J_TEETH": j_pass}
    all_rc = [{"banks": bc, **row,
               "RC_predicts_fire": 2 * row["entry_gap_period"] < 8 * bc - 5}
              for bc in list(DERIVATION_BANKS) + list(HOLDOUT_BANKS)
              for _bank, row in sorted(entry_gap_incidence(censuses[bc]).items())]
    fires = [r for r in all_rc if r["fires"]]
    verdict = {
        "gates": gate_flags, "gates_passed": sum(gate_flags.values()),
        "gates_total": len(gate_flags),
        "headline": (
            "THE P=32 CARRIER MISS IS DERIVED, and it is not an alignment "
            "forbiddance of the entry-gap separation.  Bank 2 owns the value 32 "
            "at B=7 through all three entry-gap row pairs; what fails is that no "
            "clock containing bank 2 reads the period 32 at all.  RC-2 -- a "
            "bank-owned entry-gap reading occurs only if 2P < N, i.e. the entry "
            "gap is the SHORT arc -- cuts the family at e <= 2 at B=7 and so "
            "excludes P=32 exactly.  RC-2 was fitted to the clock-local "
            "incidence at B=4..7 (14 cells, 0 disagreements), sealed, and held "
            "out at B=8: NECESSITY held on 6 of 6 cells (no cell with 2P >= N "
            "fires) and SUFFICIENCY failed on 1 of 6 (bank 6, P=8, predicted to "
            "fire and does not).  The sharpened taxonomy also re-bins 891's own "
            "labels: at B=6 the value 24 and at B=8 the value 32 are labelled "
            "ENTRY_GAP by 891 and are, clock-locally, SAME-EDGE COMPLEMENTS of "
            "the reading bank's own edge -- the ENTRY_GAP label is stolen by "
            "priority whenever a bank's entry gap coincides with its own edge "
            "complement.  The B=7 residuals P=40 and P=48 are not a fourth "
            "shape: both are same-edge complements read on an incident bank, "
            "rare because 2P > N leaves only stretch-local readings."),
        "rc_cells_total": len(all_rc),
        "rc_cells_firing": len(fires),
        "rc_necessity_violations": [
            {"banks": r["banks"], "bank": r["bank"], "period": r["entry_gap_period"]}
            for r in fires if not r["RC_predicts_fire"]],
        "rc_sufficiency_failures": [
            {"banks": r["banks"], "bank": r["bank"], "period": r["entry_gap_period"]}
            for r in all_rc if r["RC_predicts_fire"] and not r["fires"]],
        "SEAL_sha256": SEAL,
        "B9_prediction": holdout_block["B9_prediction_for_the_checker"],
        "runtime_seconds": round(elapsed, 3),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "within_runtime_limit": elapsed < RUNTIME_LIMIT_SECONDS,
        "open": [
            "RC-2's sufficiency: the (B=8, b=6) cell satisfies 2P < N and does "
            "not fire; the discriminating measurement is the equal-width "
            "requirement of RC-3, which is stretch-local",
            "RC-2 is fitted-then-sealed, not derived; the single-token "
            "derivation sketch does not cover the two-token word",
            "which word a stretch carries -- 891's declared boundary",
        ],
        "disclosed_deviations": list(DISCLOSED_DEVIATIONS),
    }
    emit(("PASS" if all(gate_flags.values()) else "FAIL")
                 + " K_VERDICT :: " + json.dumps(verdict, **dumps))

    emitted = sum(len(line.encode()) + 1 for line in lines)
    if emitted > STDOUT_LIMIT_BYTES:
        sys.stdout.write("<STDOUT_OVER_DECLARED_LIMIT:%d>\n" % emitted)
    return 0 if all(gate_flags.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
