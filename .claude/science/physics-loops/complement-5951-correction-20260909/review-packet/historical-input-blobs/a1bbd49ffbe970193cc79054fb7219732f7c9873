#!/usr/bin/env python3
"""Cycle 891: the complement mechanism and the k-run alignment law.

Cycle 881 derived the relay-swap gap  DELTA(B,e) = 8B - 13 - 8e  on N(B) = 8B - 5
stations and read it off a two-run quiescent word.  Cycle 889 falsified 881's
spectrum conjecture and replaced it with the ALIGNMENT LAW for a two-run word,

    I_max(D, sigma) = max(G - sigma, N - G - sigma),   G = (2D) mod N,

leaving two named mechanism rows open:

  (a) THE COMPLEMENT MECHANISM.  889's census OBSERVED the even ring-complement
      periods N - DELTA(B,e) = 8(e+1) at 8, 16, 24, 32, 40, 48.  The law says
      they are admissible; a law-level admissibility is not a mechanism.  What
      physical event structure realises a period of N - DELTA rather than DELTA?

  (b) THE NON-TWO-RUN DIRT.  At B=7 the episode census fired P = 35 and P = 43
      from quiescent stretches whose dirt is NOT the pure two-run pattern, i.e.
      outside the law's scope entirely.

This runner closes both by computation.

  Q1  THE COMPLEMENT MECHANISM.  An instrumented tick-for-tick kernel trace with
      PER-STATION attribution (rebuilt from the pinned Cycle-881 primary's
      instrumentation approach: replay one key on a single state vector, but
      applying the active stations ONE AT A TIME so every watched-wire
      transition is charged to the station that caused it) establishes the
      generating fact:

        RELAY_SWAP(e) is an INVOLUTIVE EXCHANGE of the local register between
        bank e and bank e+1.  It is the ONLY station kind that changes a bank's
        dirt, and each crossing raises exactly one of the pair and lowers the
        other.

      Everything follows.  A dirty run on bank b begins when a token crosses one
      of bank b's four incident swap stations E_b = {f(b-1), r(b-1), f(b), r(b)},
      and each is crossed twice per orbit -- once by the leader, once by the
      follower sigma ticks later.  So a run-start separation Delta_t inside a
      quiescent stretch obeys the EXACT bookkeeping identity

        s2 - s1  ==  Delta_t + (p2 - p1)   (mod N),  s1, s2 swap stations,
                                                    p1, p2 token positions,

      which classifies every observed period into exactly four sources:

        EDGE_DELTA        s1 = f(e), s2 = r(e), same token  -> P = DELTA(B,e)
        EDGE_COMPLEMENT   s1 = r(e), s2 = f(e), same token  -> P = N - DELTA(B,e)
        ENTRY_GAP         s1 = f(b-1), s2 = r(b), same token
                          -> P = r(b) - f(b-1) = 8(B-1-b) = N - DELTA(B, B-2-b)
        TOKEN_SEPARATION  s1 = s2, different tokens         -> P = sigma or N - sigma
        (anything else is reported as MIXED and counted, never dropped.)

      The ENTRY_GAP source is the answer to (a): the complement value 8(e+1) has
      a SIGMA-INDEPENDENT geometric source -- the distance from the station that
      hands the pointer UP into bank b on the ascending pass to the station that
      hands it BACK DOWN into bank b on the descending pass -- and that distance
      is 8(B-1-b), exactly a ring complement, on the carrier bank b = B-2-e.
      DELTA lives on ONE edge; its complement lives on ONE BANK.

  Q2  THE NON-TWO-RUN DIRT and the k-RUN LAW.  The two-run law is generalised
      exactly.  For a dirty phase set W on Z_N (any number of runs, any widths)
      and a candidate P,

        Fbad(P) = W  SYMDIFF  (W - P)    (mod N)
        I_max(P) = N - 1                if |Fbad| = 1
                 = UNBOUNDED             if Fbad is empty
                 = max cyclic gap between consecutive members of Fbad, minus 1

      and a 2-repeat reading still needs I_max >= P + 1.  The finite form, which
      is what a bounded quiescent stretch actually exercises, replaces the ring
      by the segment: Fbad = (D SYMDIFF (D - P)) INTERSECT [0, L-P-1] for the
      segment's dirty tick set D.  889's two-run law is the special case
      |W| = 2 runs of width sigma at separation D, and is recovered on all 580
      of its own cells.

Nothing is quoted from Cycles 879/881/889 except through sha-pinned text/AST/JSON
reads; their runners are import-blocklisted.  The only executable dependency is
the Cycle-719 controller core, the substrate under test.  Every gate tests that a
measurement RAN and that its bookkeeping is consistent; the DERIVATION/HOLDOUT
split is enforced by a seal that is computed -- and printed -- before any
holdout-tier corpus exists.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
import inspect
from itertools import combinations
import json
from pathlib import Path
import random
import sys
import time


ROOT = Path(__file__).resolve().parents[1]

PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
CHECKER_881 = "scripts/frontier_cycle881_p11_independent_check_2026_07_28.py"
RECEIPT_881 = "outputs/p11_characterization_cycle881_receipt_2026_07_28.json"
CACHE_881 = "logs/runner-cache/frontier_cycle881_p11_characterization_2026_07_28.txt"
CACHE_881_CHECK = (
    "logs/runner-cache/frontier_cycle881_p11_independent_check_2026_07_28.txt")
PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
CHECKER_889 = "scripts/frontier_cycle889_delta_spectrum_independent_check_2026_07_28.py"
RECEIPT_889 = "outputs/delta_spectrum_cycle889_receipt_2026_07_28.json"
RECEIPT_889_CHECK = (
    "outputs/delta_spectrum_independent_check_cycle889_receipt_2026_07_28.json")
CACHE_889 = "logs/runner-cache/frontier_cycle889_delta_spectrum_2026_07_28.txt"
CACHE_889_CHECK = (
    "logs/runner-cache/frontier_cycle889_delta_spectrum_independent_check_2026_07_28.txt")
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CORE_719_HANDSHAKE = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py")

# Preflight pins.  Every one is read as bytes and its sha256 AND its git blob id
# are compared with the value recorded here; any mismatch is exit 2.  The
# Cycle-719 kernel pair is pinned exactly as Cycle 889 pinned it.
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
    PRIMARY_889: ("c18ed0c49281fd2d54ad013ba12264b181d1720349ee002b144c028b521dd826",
                  "f1bdf1f789a85213a0a854ab0bed45e6bf250fed"),
    CHECKER_889: ("19b38fb116bb8cb79cbb925df91456c5d08d899d4b56de301a9a673ec7dc3ec3",
                  "0f946f44c431c997410a08ec3e03ae2d26d89b8a"),
    RECEIPT_889: ("10840d84d3110fa192c28667334152da815f535f131d59e763dc64bf0aef3a72",
                  "2191d809ff5b4b9f082d9f703969e05638e6e33e"),
    RECEIPT_889_CHECK: ("1ef593d7fab537900eeef3a31bd97370791b9ba3715bf2fbb7646646a08a0ded",
                        "ca6f8b2a18fab2b327f08fb1548de17943c8efbb"),
    CACHE_889: ("48c0bc663d2a5254947087003ece0b34dd730a291ccef2f1b007a5043ec2a5be",
                "a1ac91d1ce89275f7034756fbb3b527a564e9738"),
    CACHE_889_CHECK: ("f28a427b70791f25f31dada9c46b6d535fefa6f31b37a096e4e1521ced91596e",
                      "d46f2982b9a80688271e50caf321bb705242badd"),
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
HORIZON = 16_384
DERIVATION_BANKS = (4, 5)
HOLDOUT_BANKS = (6, 7)
REPRODUCTION_BANKS = (3,)
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8
PINNED_PERIOD_CEILING = 64

DISCLOSED_DEVIATIONS = (
    "PERIOD CEILING.  Inherited verbatim from Cycle 889: every P in "
    "[2, max(64, 2N(B))] is tried, which strictly contains the pinned Cycle-881 "
    "checker's [2, 64] and every DELTA(B,e) and every ring complement.  A "
    "non-orbit period above 2N(B) would be missed; the ceiling is disclosed per "
    "B and is never narrowed to the predicted set.",
    "HORIZON.  H = 16384 ticks per substrate, identical to Cycle 889's top "
    "horizon, so the episode census here is directly comparable with the pinned "
    "889 receipt.  No horizon ladder is re-run: 889 already published it and the "
    "episode instrument is horizon-robust by construction (a longer horizon adds "
    "closed stretches, it does not move the answer on stretches already closed).",
    "NO SAMPLING IN THE CENSUS.  Every clock of every corpus is swept at every "
    "bank count in 3,4,5,6,7 -- all bank clocks and all pair clocks, every closed "
    "quiescent stretch.  The clock count is gated against lanes * (B + C(B,2)).",
    "ANATOMY SUBSET.  Run-level anatomy and station attribution are extracted "
    "ONLY for episodes in which a DELTA or a ring-complement period actually "
    "fires (that is the population the questions are about).  The count of such "
    "episodes is reported in full and is never sampled; the remaining episodes "
    "contribute to the spectrum and to the completeness ledger only.",
    "REGISTER-LEVEL TRACES.  The per-station attributed trace is a single-lane "
    "replay and is run on the witness lanes named in the output plus the "
    "involution audit lanes; the audit lane set is declared, exhaustive over the "
    "B=4 placement classes it names, and its size is reported.",
)

MECHANISM_STATEMENT = (
    "THE COMPLEMENT MECHANISM.  (1) TRANSPORT.  Inside a closed quiescent "
    "stretch the ONLY stations that move a bank's dirt are the four ordered rows "
    "of an edge incident to it -- HANDOFF_FORWARD h_f(e) = f(e) - 2, RELAY_SWAP "
    "forward f(e) = 4 + 5e, RELAY_SWAP reverse r(e) = 8B - 9 - 3e, and "
    "HANDOFF_RETURN h_r(e) = r(e) + 2 -- and a pointer-carrying crossing is an "
    "EXCHANGE across that edge: one of the two banks is raised and the other "
    "lowered.  Machine-verified per station, per tick, on the attributed kernel "
    "trace inside closed quiescent stretches (transitions charged to a "
    "non-transport station = 0), with the contrast measured OUTSIDE quiescence, "
    "where source/finalizer stations inject and retire packets and of course do "
    "move bank dirt.  (2) BOOKKEEPING.  Each transport station is crossed twice "
    "per orbit -- by the leader and, sigma ticks later, by the follower -- so two "
    "dirty-run starts separated by Delta_t satisfy the exact identity "
    "s2 - s1 = Delta_t + (p2 - p1) mod N for transport stations s1, s2 and token "
    "positions p1, p2.  That classifies every readable period into "
    "RELAY_EDGE_DELTA (f(e) -> r(e), same token, P = DELTA(B,e)), "
    "RELAY_EDGE_COMPLEMENT (r(e) -> f(e), same token, P = N - DELTA(B,e)), "
    "RELAY_ENTRY_GAP (f(b-1) -> r(b), same token, P = 8(B-1-b)), "
    "TOKEN_SEPARATION (same station, different tokens, P = sigma or N - sigma), "
    "or MIXED -- and nothing is dropped.  (3) THE ANSWER.  Among ordered pairs "
    "of RELAY_SWAP stations on the edges incident to bank b, the separations "
    "that equal a ring complement are exactly three shapes, verified exhaustively "
    "for B = 3..8 and every bank: the same-edge (r(e), f(e)) pair with value "
    "N - DELTA(B,e); the ENTRY-GAP pair (f(b-1), r(b)) with value 8(B-1-b); and "
    "the (r(b-1), r(b)) pair with value 8(B-1) = N - 3, which the alignment "
    "condition forbids at every B.  The ENTRY GAP is the only one of the three "
    "that belongs to a BANK rather than to an edge -- it is the distance from "
    "the station that hands the pointer UP into bank b on the ascending pass to "
    "the station that hands it BACK DOWN into bank b on the descending pass -- "
    "and it is the sigma-independent source of the complement family.  DELTA is "
    "a property of ONE EDGE; the complement the census actually carries is a "
    "property of ONE BANK, the bank b = B - 2 - e."
)

KRUN_LAW_STATEMENT = (
    "THE k-RUN ALIGNMENT LAW.  Let W be the dirty phase set on Z_N of a clock in "
    "the quiescent regime (any number k of runs, any widths).  For a candidate "
    "period P put Fbad(P) = W SYMDIFF (W - P) mod N.  Then the maximal run of "
    "consecutive shift-exact indices is EXACTLY  I_max(P) = (max cyclic gap "
    "between consecutive members of Fbad) - 1, with I_max = N - 1 when |Fbad| = 1 "
    "and I_max UNBOUNDED when Fbad is empty (P is then a true period of the "
    "phase word).  A 2-repeat reading needs I_max >= P + 1 and an enclosing "
    "closed quiescent stretch of length >= 2P + 1.  FINITE FORM: a bounded "
    "stretch does not see the whole ring word, so on a segment of length L with "
    "dirty tick set D the exact failure set is (D SYMDIFF (D - P)) INTERSECT "
    "[0, L-P-1] and I_max is the longest gap in its complement; the ring form is "
    "the special case in which the segment carries the full orbit-periodic run "
    "pattern.  Cycle 889's law is the sub-case k = 2 with equal widths sigma at "
    "separation D: Fbad is then two zones of width sigma separated by "
    "G = (2D) mod N and I_max = max(G - sigma, N - G - sigma)."
)

COMPLEMENT_RULE_TEXT = (
    "THE GENERIC COMPLEMENT RULE (derived at B = 4 and B = 5; B = 6 and B = 7 are "
    "the declared holdout).  At bank count B, with N = 8B - 5, f(e) = 4 + 5e and "
    "r(e) = 8B - 9 - 3e, the ring-complement period P = 8(e+1) = N - DELTA(B,e) "
    "is GENERICALLY readable if and only if BOTH: "
    "(a) ENTRY-GAP EXISTENCE -- P is the entry gap of some bank, i.e. "
    "P = r(b) - f(b-1) = 8(B-1-b) for a bank b with 1 <= b <= B-2 (equivalently "
    "0 <= e <= B-3, with carrier bank b = B-2-e); and "
    "(b) RING ALIGNMENT -- with G = (2P) mod N the two forbidden zones of width "
    "w >= 1 leave an arc long enough for two repeats, i.e. "
    "max(G, N-G) - w >= P + 1 for some w >= 1, equivalently max(G, N-G) >= P + 2. "
    "The CARRIER PREDICTION is that the ENTRY_GAP source of P is realised on bank "
    "b = B-2-e and on no other bank clock (pair clocks inherit it from the bank "
    "they contain).  DEGENERATE STRETCHES -- closed quiescent stretches in which "
    "the generic orbit-periodic run pattern is incomplete, so that fewer runs are "
    "present than the ring word carries -- are OUTSIDE this rule by construction "
    "and are reported as residuals with their episode counts, never absorbed."
)

DETECTOR_STATEMENT = (
    "THE DETECTOR.  Reimplemented from the sha-pinned Cycle-889 checker's own "
    "declared semantics (which are the pinned Cycle-881 checker's): a clock's "
    "clean ticks become a bitmask S; for a period P the bits of (S ^ (S >> P)) "
    "below last - P + 1 are exactly the ticks where t in S <=> t+P in S fails, so "
    "the highest such bit + 1 is the LEAST transient -- no window, no ladder, no "
    "block cap.  A reading is kept only if last - transient >= 2P, the stable "
    "stretch carries >= 8 clean ticks, and the stable residues modulo P are not "
    "all of them (non-saturation).  The detector is given no knowledge of DELTA "
    "or of the complement set: it sweeps a contiguous period range and the "
    "predicted sets are compared against its output afterwards."
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
                       Path(PRIMARY_889).stem, Path(CHECKER_889).stem,
                       Path(PRIMARY_879).stem)


class _Firewall(importlib.abc.MetaPathFinder):
    """Any import of a blocklisted Cycle-879/881/889 runner is an immediate failure."""

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


WATCHED_WIRE_NAMES = None


def watched_layout(bank_count):
    """Locate each bank's local handshake wires by a single-bit probe."""
    global WATCHED_WIRE_NAMES
    banks, links = B.chain_genesis(bank_count)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
    local = (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
             *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK)
    names = (["POINTER", "U_TO_V", "V_TO_U", "DIRECTION_OK"]
             + ["FRESH%d" % i for i in range(len(A.FRESH))]
             + ["ZERO_WORK%d" % i for i in range(len(A.ZERO_WORK))]
             + ["TOKEN_OK"])
    WATCHED_WIRE_NAMES = tuple(names)
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
    """The forward/reverse RELAY_SWAP station indices per edge, read from gates.

    ``interleaved_program`` emits per edge the forward pair (RELAY_LATCH then
    RELAY_SWAP) and later the reverse pair (RELAY_SWAP then RELAY_UNLATCH), so
    the swaps are rows 1 and 2 of the edge's four relay rows.  Both are located
    by reading the emitted gate words; no index literal is used anywhere.
    """
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
    """Cycle-889/881 checker semantics: least transient by S ^ (S >> P), no caps."""
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
        # Residue count, exactly as a bit-walk would give it but folded: the
        # residue of stable bit i is (transient + i) mod P, so OR-ing the word
        # with itself shifted by successive multiples of P collapses every
        # residue class into the low P bits.  Doubling the shift makes it
        # O(log(reach/P)) bignum steps instead of one step per clean tick.
        folded, step = stable, period
        while step <= reach:
            folded |= folded >> step
            step <<= 1
        residue_count = bin(folded & ((1 << period) - 1)).count("1")
        if residue_count == period:
            continue
        out[period] = (transient, events, residue_count)
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


def zero_runs(segment, length):
    """Maximal runs of CLEAR bits (= dirty ticks) inside a segment of ``length``."""
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
    """Longest run of consecutive shift-exact indices, measured directly."""
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


# --------------------------------------------------------------- the k-run law
def krun_imax(stations, dirty_phases, period):
    """I_max for a k-run ring word.  None means UNBOUNDED (Fbad empty)."""
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


def finite_imax(segment, length, period):
    """Finite form: longest shift-exact run inside a bounded segment."""
    return max_exact_run(segment, period, length)


# -------------------------------------------------- station / period bookkeeping
def swap_station_table(bank_count):
    program = K.interleaved_program(bank_count)
    stations = len(program)
    swaps, malformed = relay_swap_rows(program)
    forward = {edge: pair[0] for edge, pair in swaps.items()}
    reverse = {edge: pair[1] for edge, pair in swaps.items()}
    handoff = defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "handoff":
            handoff[edge].append(index)
    handoff_forward = {e: rows[0] for e, rows in handoff.items() if len(rows) == 2}
    handoff_return = {e: rows[1] for e, rows in handoff.items() if len(rows) == 2}
    # Every station that can move a bank's dirt: the edge's four ordered rows.
    station_edge = {}
    for edge in sorted(swaps):
        station_edge[handoff_forward[edge]] = ("handoff_forward", edge)
        station_edge[forward[edge]] = ("forward", edge)
        station_edge[reverse[edge]] = ("reverse", edge)
        station_edge[handoff_return[edge]] = ("handoff_return", edge)
    entry_gap = {b: (reverse[b] - forward[b - 1]) % stations
                 for b in range(1, bank_count - 1)}
    return {
        "program": program, "stations": stations, "swaps": swaps,
        "forward": forward, "reverse": reverse, "station_edge": station_edge,
        "handoff_forward": handoff_forward, "handoff_return": handoff_return,
        "entry_gap": entry_gap, "malformed": malformed,
        "delta": {e: (r - f) % stations for e, (f, r) in swaps.items()},
    }


def incident_pair_separations(table, bank, bank_count, relay_only=False):
    """Every ordered pair of transport stations on the edges incident to a bank.

    Returns {separation -> [(s1, kind1, edge1, s2, kind2, edge2), ...]}.  With
    ``relay_only`` the handoff rows are excluded, which is the sub-table the
    complement structure lives in.
    """
    stations = table["stations"]
    incident = [e for e in (bank - 1, bank) if 0 <= e <= bank_count - 2]
    rows = [(s, kind, edge) for s, (kind, edge) in table["station_edge"].items()
            if edge in incident
            and (not relay_only or kind in ("forward", "reverse"))]
    out = defaultdict(list)
    for s1, k1, e1 in rows:
        for s2, k2, e2 in rows:
            if s1 == s2:
                continue
            out[(s2 - s1) % stations].append((s1, k1, e1, s2, k2, e2))
    return out


def expected_complement_pairs(bank_count, bank):
    """The complement VALUES a bank's incident RELAY_SWAP pairs can realise.

    Derived, not measured: on incident edge e the reverse->forward pair spans
    N - DELTA(B,e); the ascending-entry-to-descending-entry pair f(b-1) -> r(b)
    spans 8(B-1-b); and the two reverse swaps r(b-1) -> r(b) span N - 3 =
    8(B-1) because r(e) descends in steps of 3.
    """
    stations = 8 * bank_count - 5
    values = set()
    detail = {}
    for edge in (bank - 1, bank):
        if 0 <= edge <= bank_count - 2:
            value = stations - (8 * bank_count - 13 - 8 * edge)
            values.add(value)
            detail.setdefault("reverse_to_forward_same_edge", []).append(
                {"edge": edge, "value": value})
    if 1 <= bank <= bank_count - 2:
        values.add(8 * (bank_count - 1 - bank))
        detail["entry_gap_f_bminus1_to_r_b"] = 8 * (bank_count - 1 - bank)
        values.add(8 * (bank_count - 1))
        detail["reverse_to_reverse_r_bminus1_to_r_b"] = 8 * (bank_count - 1)
    return values, detail


CLASS_PRIORITY = ("RELAY_ENTRY_GAP", "RELAY_EDGE_COMPLEMENT", "RELAY_EDGE_DELTA",
                  "TOKEN_SEPARATION", "MIXED")


def classify_separation(table, banks_of_clock, positions, separation):
    """Every (station, token) pair that can realise ``separation``, classified.

    A run start at tick t caused by the token at position p is the crossing of
    station (p + t - 1) mod N.  So two run starts separated by Delta_t are the
    crossings of stations s1, s2 with s2 - s1 == Delta_t + (p2 - p1) (mod N).
    The taxonomy below is exhaustive over swap-station pairs; anything that is a
    swap-station pair but none of the named shapes is MIXED and is counted.
    """
    stations = table["stations"]
    labels = set()
    witnesses = []
    swap_set = table["station_edge"]
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
                if len(witnesses) < 8:
                    witnesses.append({"s1": s1, "s2": s2, "p1": p1, "p2": p2,
                                      "kind1": kind1, "edge1": edge1,
                                      "kind2": kind2, "edge2": edge2,
                                      "label": label})
    if not labels:
        return "UNATTRIBUTED", [], witnesses
    primary = next(name for name in CLASS_PRIORITY if name in labels)
    return primary, sorted(labels), witnesses


# ------------------------------------------------------- the instrumented trace
def attributed_trace(box, event, positions, lo, hi):
    """Replay ONE key on a single state vector, ONE STATION AT A TIME.

    Rebuilt from the pinned Cycle-881 primary's ``instrumented_trace`` approach
    (single-lane replay through the kernel, recording every dirtying wire) with
    the one refinement this cycle needs: the active stations of a tick are
    applied separately so that every watched-wire transition is charged to the
    station that caused it.
    """
    program = box["program"]
    stations = box["stations"]
    schedules = box["schedules"]
    per_bank = box["per_bank"]
    labels = box["labels"]
    source_pointer = box["source_pointer"]
    bank_count = box["banks"]
    state = list(K.run_orbit(box["seeds"][event], program,
                             token_positions=positions)[0])
    events = []

    def dirty(bank):
        return any(state[wire] for wire in per_bank[bank])

    # Fast-forward to the window with the plain replay; attribution is only
    # needed inside [lo, hi] and costs a per-station snapshot of every bank.
    for tick in range(1, lo):
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

    for tick in range(max(1, lo), hi + 1):
        phase = (tick - 1) % stations
        active = sorted((p + phase) % stations for p in positions)
        for station in active:
            before = [dirty(bank) for bank in range(bank_count)]
            before_source = bool(state[source_pointer])
            for gate in schedules[station]:
                if gate.kind == "X":
                    state[gate.wires[0]] ^= 1
                elif gate.kind == "CNOT":
                    control, target = gate.wires
                    state[target] ^= state[control]
                else:
                    left, right, target = gate.wires
                    state[target] ^= state[left] & state[right]
            after = [dirty(bank) for bank in range(bank_count)]
            after_source = bool(state[source_pointer])
            changed = [bank for bank in range(bank_count)
                       if before[bank] != after[bank]]
            if changed or before_source != after_source:
                events.append({
                    "tick": tick, "phase": phase, "station": station,
                    "station_kind": program[station][0] + str(program[station][1]),
                    "token": next((p for p in positions
                                   if (p + phase) % stations == station), None),
                    "banks_raised": [b for b in changed if after[b]],
                    "banks_lowered": [b for b in changed if not after[b]],
                    "source_changed": before_source != after_source,
                    "wires_now_set": [labels[w] for b in changed
                                      for w in per_bank[b] if state[w]][:8],
                })
    return events


def involution_audit(box, lane_indices, source_masks, stretches_per_lane=3):
    """Every bank-dirt transition inside a CLOSED quiescent stretch, charged to
    the station that caused it, and the exchange shape tested.

    The audit is deliberately confined to closed SOURCE_POINTER-quiescent
    stretches: that is the regime the whole question lives in.  Outside them the
    source/finalizer/handoff stations inject and retire packets and of course
    move bank dirt; those transitions are counted separately and published, they
    are not suppressed.
    """
    table = swap_station_table(box["banks"])
    horizon = box["horizon"]
    rows = []
    unattributed = 0
    non_exchange = 0
    exchange = 0
    local_flag = Counter()
    non_swap_causes = Counter()
    transitions = 0
    outside_transitions = 0
    outside_causes = Counter()
    audited = []
    for lane in lane_indices:
        event, positions = box["keys"][lane]
        stretches = [(a, b) for (a, b) in maximal_runs(source_masks[lane], horizon)
                     if a > 0 and b < horizon][:stretches_per_lane]
        for low, high in stretches:
            audited.append({"lane": lane, "event": event,
                            "token_positions": list(positions),
                            "stretch": [low, high]})
            events = attributed_trace(box, event, positions, low + 1, high)
            for row in events:
                if not row["banks_raised"] and not row["banks_lowered"]:
                    continue
                station = row["station"]
                moved = len(row["banks_raised"]) + len(row["banks_lowered"])
                transitions += moved
                if station not in table["station_edge"]:
                    unattributed += moved
                    non_swap_causes[row["station_kind"]] += moved
                    continue
                _direction, edge = table["station_edge"][station]
                raised = set(row["banks_raised"])
                lowered = set(row["banks_lowered"])
                pair = {edge, edge + 1}
                if not (raised | lowered) <= pair:
                    non_exchange += 1
                elif (len(raised) == 1 and len(lowered) == 1
                      and raised | lowered == pair):
                    exchange += 1
                else:
                    local_flag[row["station_kind"]] += 1
                if len(rows) < 200:
                    rows.append({"tick": row["tick"], "station": station,
                                 "station_kind": row["station_kind"],
                                 "edge": edge, "raised": sorted(raised),
                                 "lowered": sorted(lowered),
                                 "token": row["token"],
                                 "wires_now_set": row["wires_now_set"][:4]})
    # the same audit run WITHOUT the quiescence restriction, published as contrast
    for lane in lane_indices[:2]:
        event, positions = box["keys"][lane]
        for row in attributed_trace(box, event, positions, 1, 400):
            if not row["banks_raised"] and not row["banks_lowered"]:
                continue
            if row["station"] not in table["station_edge"]:
                outside_transitions += 1
                outside_causes[row["station_kind"]] += 1
    return {
        "lanes_audited": audited,
        "stretches_audited": len(audited),
        "bank_dirt_transitions_inside_closed_quiescent_stretches": transitions,
        "transitions_not_caused_by_a_transport_station": unattributed,
        "non_transport_cause_histogram": dict(non_swap_causes),
        "crossings_that_are_a_clean_edge_exchange": exchange,
        "crossings_that_set_a_local_flag_only": dict(local_flag),
        "crossings_that_touched_a_bank_off_the_edge": non_exchange,
        "transport_is_confined_to_incident_edge_stations": unattributed == 0,
        "every_pointer_crossing_is_an_edge_exchange": non_exchange == 0,
        "contrast_outside_quiescence_non_transport_transitions": outside_transitions,
        "contrast_outside_quiescence_causes": dict(outside_causes),
        "sample_rows": rows[:24],
    }


# ---------------------------------------------------------------- the census
def census_tier(box, want_anatomy, anatomy_cap=40):
    """One exhaustive episode census + run anatomy on DELTA/complement episodes.

    ``anatomy_cap`` is PER PERIOD, not global, so a rare period can never be
    crowded out of the anatomy store by a common one.
    """
    bank_count = box["banks"]
    stations = box["stations"]
    lanes = box["lane_count"]
    horizon = box["horizon"]
    table = swap_station_table(bank_count)
    deltas = table["delta"]
    delta_set = sorted(set(deltas.values()))
    complement_set = sorted({stations - d for d in deltas.values()})
    ceiling = max(PINNED_PERIOD_CEILING, 2 * stations)
    periods = sorted(set(range(2, ceiling + 1)) | set(delta_set)
                     | set(complement_set))
    pairs = tuple(combinations(range(bank_count), 2))
    bank_masks = [transpose_planes(box["clean_planes"][b], lanes, horizon)
                  for b in range(bank_count)]
    source_masks = transpose_planes(box["source_clean"], lanes, horizon)

    spectrum = Counter()
    clock_periods = {}
    stretch_total = 0
    longest_stretch = 0
    anatomy_by_period = defaultdict(list)
    class_counts = Counter()
    carrier_counts = defaultdict(Counter)
    clocks_total = 0
    for lane in range(lanes):
        event, positions = box["keys"][lane]
        leader, follower, sigma = leader_and_sigma(positions, stations)
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
                continue
            found = set()
            for a, b in stretches:
                length = b - a + 1
                segment = (mask >> a) & ((1 << length) - 1)
                if segment == 0:
                    continue
                hits = tail_periods(segment, periods)
                interesting = [p for p in hits
                               if p % stations
                               and (p in delta_set or p in complement_set)]
                for period in hits:
                    if period % stations:
                        spectrum[period] += 1
                        found.add(period)
                if not interesting or not want_anatomy:
                    continue
                runs = zero_runs(segment, length)
                starts = [a + lo for lo, _hi in runs]
                widths = [hi - lo + 1 for lo, hi in runs]
                gaps = [starts[i + 1] - starts[i] for i in range(len(starts) - 1)]
                for period in interesting:
                    matching = [i for i, gap in enumerate(gaps) if gap == period]
                    label, labels_all, witnesses = classify_separation(
                        table, set(member_banks), positions, period)
                    class_counts[(period, label)] += 1
                    for bank in member_banks:
                        carrier_counts[(period, label)][bank] += 1
                    if len(anatomy_by_period[period]) < anatomy_cap:
                        anatomy_by_period[period].append({
                            "banks": bank_count, "lane": lane, "event": event,
                            "token_positions": list(positions), "sigma": sigma,
                            "leader": leader, "follower": follower,
                            "clock": name, "member_banks": list(member_banks),
                            "stretch": [a, b], "stretch_len": length,
                            "period": period,
                            "period_kind": ("DELTA" if period in delta_set
                                            else "RING_COMPLEMENT"),
                            "dirty_runs": len(runs),
                            "run_start_stations": [
                                ["p%d@s%d:%s" % (
                                    p, (p + tick - 1) % stations,
                                    table["station_edge"].get(
                                        (p + tick - 1) % stations,
                                        ("non_transport", -1))[0])
                                 for p in positions]
                                for tick in starts[:6]],
                            "run_start_ticks": starts[:12],
                            "run_widths": widths[:12],
                            "consecutive_gaps": gaps[:12],
                            "gaps_equal_to_the_period": len(matching),
                            "two_run_pattern": (len(runs) == 2
                                                and len(set(widths)) == 1),
                            "source_class": label,
                            "source_classes_available": labels_all,
                            "station_witness": witnesses[:3],
                            "detector": list(hits[period]),
                        })
            if found:
                clock_periods[(lane, name)] = (found, sigma, member_banks, event)
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
        "delta_members_observed": sorted(p for p in spectrum if p in delta_set),
        "complements_observed": sorted(p for p in spectrum
                                       if p in complement_set),
        "clock_periods": clock_periods, "keys": box["keys"],
        "anatomy_by_period": {p: rows for p, rows in anatomy_by_period.items()},
        "anatomy": [row for p in sorted(anatomy_by_period)
                    for row in anatomy_by_period[p]],
        "class_counts": class_counts,
        "carrier_counts": carrier_counts,
    }


# ------------------------------------------------------------------ THE RULE
def predicted_complement_rows(bank_count):
    """THE GENERIC COMPLEMENT RULE, as a pure function of the bank count.

    No census, corpus, receipt or measured quantity is read here -- only the
    program-geometry constants N = 8B-5, f(e) = 4+5e, r(e) = 8B-9-3e.
    """
    stations = 8 * bank_count - 5
    rows = []
    for edge in range(bank_count - 2):          # entry gap exists <=> e <= B-3
        period = 8 * (edge + 1)
        carrier = bank_count - 2 - edge
        forward_prev = 4 + 5 * (carrier - 1)
        reverse_here = 8 * bank_count - 9 - 3 * carrier
        gap = (reverse_here - forward_prev) % stations
        pivot = (2 * period) % stations
        aligned = max(pivot, stations - pivot) >= period + 2
        rows.append({"period": period, "edge": edge, "carrier_bank": carrier,
                     "entry_gap_check": gap == period,
                     "G_two_P_mod_N": pivot,
                     "ring_alignment_admits": aligned,
                     "predicted": bool(gap == period and aligned)})
    return rows


def predicted_complement_set(bank_count):
    return sorted(row["period"] for row in predicted_complement_rows(bank_count)
                  if row["predicted"])


def predicted_carriers(bank_count):
    return {row["period"]: row["carrier_bank"]
            for row in predicted_complement_rows(bank_count) if row["predicted"]}


# ------------------------------------------------------------------------ main
def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    header_881, blocks_881 = parse_cache(CACHE_881)
    header_889, blocks_889 = parse_cache(CACHE_889)
    header_889_check, blocks_889_check = parse_cache(CACHE_889_CHECK)
    receipt_881 = json.loads((ROOT / RECEIPT_881).read_text())
    receipt_889 = json.loads((ROOT / RECEIPT_889).read_text())
    receipt_889_check = json.loads((ROOT / RECEIPT_889_CHECK).read_text())
    tree_881 = ast.parse((ROOT / PRIMARY_881).read_bytes().decode())
    tree_889 = ast.parse((ROOT / PRIMARY_889).read_bytes().decode())

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

    literals_881 = literals(tree_881)
    literals_889 = literals(tree_889)

    # ------------------------------------------------------------ A  PINS
    pin_block = {
        "pins": PREFLIGHT_ROWS,
        "pin_count": len(PINS),
        "preflight": "PASS (hard-fail exit 2 on any mismatch)",
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklisted_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                       if m in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "read_mode_for_881_and_889": "TEXT_AST_JSON_ONLY_BLOCKLISTED",
        "kernel_imported": CORE_719,
        "kernel_import_rationale": (
            "The Cycle-719 controller core is the SUBSTRATE under test, not a "
            "source of claims; the pinned Cycle-881 and Cycle-889 runners import "
            "it on the same grounds.  Its own import dependency "
            "frontier_cycle719_local_handshake_controller_core_2026_07_26.py is "
            "pinned here too, so the whole executed surface is digest-fixed."),
        "cache_881_pins_the_worktree_runner":
            header_881.get("runner_sha256") == PREFLIGHT_ROWS[PRIMARY_881]["sha256"],
        "cache_889_pins_the_worktree_runner":
            header_889.get("runner_sha256") == PREFLIGHT_ROWS[PRIMARY_889]["sha256"],
        "cache_889_check_pins_the_worktree_checker":
            header_889_check.get("runner_sha256")
            == PREFLIGHT_ROWS[CHECKER_889]["sha256"],
        "cache_889_clean_run": header_889.get("exit_code") == "0"
                               and header_889.get("status") == "ok",
        "cache_889_check_clean_run": header_889_check.get("exit_code") == "0"
                                     and header_889_check.get("status") == "ok",
        "receipt_889_files_agree_with_pins": all(
            receipt_889["files"][path]["sha256"] == PREFLIGHT_ROWS[path]["sha256"]
            and receipt_889["files"][path]["git_blob"]
            == PREFLIGHT_ROWS[path]["git_blob"]
            for path in (PRIMARY_889, CHECKER_889, CACHE_889, CACHE_889_CHECK)),
        "receipt_881_files_agree_with_pins": all(
            receipt_881["files"][path]["sha256"] == PREFLIGHT_ROWS[path]["sha256"]
            for path in (PRIMARY_881, CACHE_881)),
        "receipt_889_check_confirms_falsification":
            receipt_889_check["checker_verdict_block"]["primary_status"],
        "primary_881_literals_from_ast": {
            name: literals_881.get(name)
            for name in ("STATIONS", "FIXTURE_BANKS", "TARGET_PERIOD", "B3_STATIONS")},
        "primary_889_literals_from_ast": {
            name: literals_889.get(name)
            for name in ("HORIZON", "CENSUS_BANKS", "MIN_PERIOD_REPEATS",
                         "MIN_STABLE_EVENTS", "PINNED_PERIOD_CEILING")},
        "detector_constants_match_pinned_889": (
            literals_889.get("MIN_PERIOD_REPEATS") == MIN_PERIOD_REPEATS
            and literals_889.get("MIN_STABLE_EVENTS") == MIN_STABLE_EVENTS
            and literals_889.get("PINNED_PERIOD_CEILING") == PINNED_PERIOD_CEILING
            and literals_889.get("HORIZON") == HORIZON),
        "primary_889_blocks_parsed": sorted(blocks_889),
        "checker_889_blocks_parsed": sorted(blocks_889_check),
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_repo_relative": all(
            not Path(p).is_absolute() for p in AUDIT_INPUT_PATHS),
        "disclosed_deviations": list(DISCLOSED_DEVIATIONS),
        "mechanism_statement": MECHANISM_STATEMENT,
        "krun_law_statement": KRUN_LAW_STATEMENT,
        "complement_rule_statement": COMPLEMENT_RULE_TEXT,
        "detector_statement": DETECTOR_STATEMENT,
    }
    a_pass = (
        not pin_block["blocklisted_modules_loaded"]
        and not pin_block["firewall_hits"]
        and pin_block["cache_881_pins_the_worktree_runner"]
        and pin_block["cache_889_pins_the_worktree_runner"]
        and pin_block["cache_889_check_pins_the_worktree_checker"]
        and pin_block["cache_889_clean_run"]
        and pin_block["cache_889_check_clean_run"]
        and pin_block["receipt_889_files_agree_with_pins"]
        and pin_block["receipt_881_files_agree_with_pins"]
        and pin_block["detector_constants_match_pinned_889"]
        and pin_block["audit_input_paths_repo_relative"]
        and literals_881.get("TARGET_PERIOD") == 11
        and {"D_ALIGNMENT_LAW", "F_CENSUS"} <= set(blocks_889)
    )
    lines.append(("PASS" if a_pass else "FAIL") + " A_PINS :: "
                 + json.dumps(pin_block, **dumps))
    if not a_pass:
        print("\n".join(lines))
        return 1

    # ----------------------------------------- B  PROGRAM REBUILD + GEOMETRY
    pinned_layout = {int(row["banks"]): row
                     for row in blocks_889["B_PROGRAM_REBUILD"]["rows"]}
    geometry_rows, rebuild_bad = [], 0
    for bank_count in sorted(pinned_layout):
        table = swap_station_table(bank_count)
        stations = table["stations"]
        pinned = pinned_layout[bank_count]
        agrees = (
            stations == pinned["stations"]
            and {str(e): list(v) for e, v in table["swaps"].items()}
                == pinned["relay_swap_rows"]
            and {str(e): d for e, d in table["delta"].items()}
                == pinned["delta_measured"]
            and table["malformed"] == pinned["malformed_edges"])
        rebuild_bad += not agrees
        entry = table["entry_gap"]
        geometry_rows.append({
            "banks": bank_count, "stations": stations,
            "forward_swaps_f_e": {str(e): v for e, v in table["forward"].items()},
            "reverse_swaps_r_e": {str(e): v for e, v in table["reverse"].items()},
            "f_formula_4_plus_5e": all(v == 4 + 5 * e
                                       for e, v in table["forward"].items()),
            "r_formula_8B_minus_9_minus_3e": all(
                v == 8 * bank_count - 9 - 3 * e
                for e, v in table["reverse"].items()),
            "delta_measured": {str(e): d for e, d in table["delta"].items()},
            "entry_gap_measured": {str(b): g for b, g in entry.items()},
            "entry_gap_formula_8_B_minus_1_minus_b": all(
                g == 8 * (bank_count - 1 - b) for b, g in entry.items()),
            "entry_gap_is_a_ring_complement": all(
                g == stations - (8 * bank_count - 13 - 8 * (bank_count - 2 - b))
                for b, g in entry.items()),
            "ring_complements": {str(e): stations - d
                                 for e, d in table["delta"].items()},
            "malformed_edges": table["malformed"],
            "agrees_with_pinned_889_rebuild": agrees,
        })
    twice = []
    for _ in range(2):
        twice.append(digest([
            [list(K.interleaved_program(bc)[i][:2])
             for i in range(len(K.interleaved_program(bc)))]
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
    del probe
    geometry_block = {
        "rows": geometry_rows,
        "bank_counts_checked": sorted(pinned_layout),
        "disagreements_with_pinned_889_rebuild": rebuild_bad,
        "entry_gap_derivation": (
            "r(b) - f(b-1) = (8B - 9 - 3b) - (4 + 5(b-1)) = 8(B - 1 - b), and "
            "N - DELTA(B,e) = 8(e+1), so the entry gap of bank b is exactly the "
            "ring complement of edge e = B - 2 - b.  It exists only for "
            "1 <= b <= B-2, i.e. 0 <= e <= B-3."),
        "program_double_build_digest": twice[0],
        "program_double_build_deterministic": twice[0] == twice[1],
        "corpus_double_build_digest": corpus_twice[0],
        "corpus_double_build_deterministic": corpus_twice[0] == corpus_twice[1],
    }
    b_pass = (
        rebuild_bad == 0
        and all(row["f_formula_4_plus_5e"] for row in geometry_rows)
        and all(row["r_formula_8B_minus_9_minus_3e"] for row in geometry_rows)
        and all(row["entry_gap_formula_8_B_minus_1_minus_b"] for row in geometry_rows)
        and all(row["entry_gap_is_a_ring_complement"] for row in geometry_rows)
        and all(row["malformed_edges"] == 0 for row in geometry_rows)
        and geometry_block["program_double_build_deterministic"]
        and geometry_block["corpus_double_build_deterministic"]
        and sorted(pinned_layout) == list(range(3, 9))
    )
    lines.append(("PASS" if b_pass else "FAIL") + " B_PROGRAM_AND_GEOMETRY :: "
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
        known_rows.append({"period": period, "detected": period in found,
                           "transient": found.get(period, (None,))[0]})
    thue_morse = 0
    for index in range(2048):
        if bin(index).count("1") % 2 == 0:
            thue_morse |= 1 << index
    tm_found = sorted(tail_periods(thue_morse, range(2, 96)))
    all_clean = (1 << 2048) - 1
    impostors = []
    for period, clean, damage in ((11, 6, 40), (13, 5, 33), (19, 11, 60)):
        pattern = [1] * clean + [0] * (period - clean)
        word, _length = synthetic(pattern, 8)
        broken = word ^ (1 << damage)
        broken_found = tail_periods(broken, [period])
        impostors.append({
            "period": period, "damaged_tick": damage,
            "refused_before_the_damage": (period not in broken_found
                                          or broken_found[period][0] > damage)})
    # the residue fold is an optimisation; it is proved equivalent to the pinned
    # semantics' literal bit-walk on a declared randomised corpus, not asserted.
    def reference_tail_periods(mask, periods):
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

    fold_rng = random.Random(891891)
    fold_cases, fold_bad = 0, []
    for _trial in range(4000):
        length = fold_rng.randint(10, 400)
        word = 0
        if fold_rng.random() < 0.4:
            period = fold_rng.randint(2, 40)
            width = fold_rng.randint(1, max(1, period - 1))
            for index in range(length):
                if (index % period) >= width:
                    word |= 1 << index
        else:
            density = fold_rng.choice([0.3, 0.6, 0.9])
            for index in range(length):
                if fold_rng.random() < density:
                    word |= 1 << index
        sweep = list(range(2, 80))
        fold_cases += 1
        if tail_periods(word, sweep) != reference_tail_periods(word, sweep):
            fold_bad.append(length)

    planted_period, planted_clean = 23, 9
    planted, length = synthetic([1] * planted_clean
                                + [0] * (planted_period - planted_clean), 12)
    b4_delta_set = sorted({8 * 4 - 13 - 8 * e for e in range(3)})
    b4_complements = sorted({27 - d for d in b4_delta_set})
    planted_found = tail_periods(planted, sorted(set(range(2, 96))))
    detector_block = {
        "statement": DETECTOR_STATEMENT,
        "known_period_recovery": known_rows,
        "all_known_recovered": all(row["detected"] for row in known_rows),
        "thue_morse_periods_found": tm_found,
        "thue_morse_is_period_free": tm_found == [],
        "all_clean_refused_as_saturated": tail_periods(all_clean, range(2, 96)) == {},
        "all_dirty_refused": tail_periods(0, range(2, 96)) == {},
        "seeded_wrong_period_impostors": impostors,
        "all_impostors_refused": all(row["refused_before_the_damage"]
                                     for row in impostors),
        "residue_fold_equivalence_cases": fold_cases,
        "residue_fold_equivalence_failures": len(fold_bad),
        "residue_fold_note": (
            "The only departure from the pinned semantics' literal code is that "
            "the residue count is obtained by OR-folding the stable word in "
            "steps of P (doubling) instead of walking one clean tick at a time.  "
            "Both are run head to head on %d randomised words (seed 891891, "
            "periodic and Bernoulli families, periods 2..79); they agree on "
            "every one." % fold_cases),
        "falsifier_visibility_control": {
            "planted_period": planted_period,
            "B4_delta_set": b4_delta_set,
            "B4_complement_set": b4_complements,
            "planted_period_in_either_named_set":
                planted_period in b4_delta_set or planted_period in b4_complements,
            "planted_period_detected": planted_period in planted_found,
            "detector_output": sorted(planted_found),
            "note": "A period outside BOTH named sets is detected by the same "
                    "code path, so an out-of-set falsifier cannot be invisible.",
        },
        "leak_control": {
            "detector_signature_is_period_range_only": True,
            "note": "tail_periods takes (mask, periods) only; neither the DELTA "
                    "set nor the complement set is ever passed to it.",
        },
    }
    c_pass = (
        detector_block["all_known_recovered"]
        and detector_block["thue_morse_is_period_free"]
        and detector_block["all_clean_refused_as_saturated"]
        and detector_block["all_dirty_refused"]
        and detector_block["all_impostors_refused"]
        and not fold_bad and fold_cases >= 4000
        and detector_block["falsifier_visibility_control"]["planted_period_detected"]
        and not detector_block["falsifier_visibility_control"][
            "planted_period_in_either_named_set"]
    )
    lines.append(("PASS" if c_pass else "FAIL") + " C_DETECTOR :: "
                 + json.dumps(detector_block, **dumps))

    # ------------------------------------------------------ D  SWAP INVOLUTION
    box4 = build_corpus(4, HORIZON)
    source_masks4 = transpose_planes(box4["source_clean"], box4["lane_count"],
                                     HORIZON)
    audit_key_set = ((0, 2), (0, 5), (0, 8), (0, 11), (0, 13), (3, 9))
    audit_lane_indices = [box4["keys"].index((0, positions))
                          for positions in audit_key_set]
    audit = involution_audit(box4, audit_lane_indices, source_masks4)
    audit["declared_audit_keys"] = [list(p) for p in audit_key_set]
    del source_masks4
    table4 = swap_station_table(4)
    exemplar_events = attributed_trace(box4, 0, (0, 8), 860, 900)
    # WHICH station pairs can carry a ring-complement value at all?
    pair_shapes = []
    complement_pair_bad = 0
    for bank_count in range(3, 9):
        table = swap_station_table(bank_count)
        stations = table["stations"]
        complements = {stations - d for d in table["delta"].values()}
        for bank in range(bank_count):
            separations = incident_pair_separations(table, bank, bank_count,
                                                    relay_only=True)
            measured = {value for value in complements if separations.get(value)}
            derived, detail = expected_complement_pairs(bank_count, bank)
            agrees = measured == derived
            complement_pair_bad += not agrees
            entry_value = (8 * (bank_count - 1 - bank)
                           if 1 <= bank <= bank_count - 2 else None)
            entry_shapes = separations.get(entry_value, []) if entry_value else []
            pair_shapes.append({
                "banks": bank_count, "bank": bank,
                "complement_values_measured": sorted(measured),
                "complement_values_derived": sorted(derived),
                "agrees": agrees,
                "derivation": detail,
                "entry_gap_value": entry_value,
                "entry_gap_pair_is_forward_to_reverse": bool(
                    entry_shapes and any(s[1] == "forward" and s[4] == "reverse"
                                         and s[5] == bank for s in entry_shapes)),
            })
    involution_block = {
        "statement": MECHANISM_STATEMENT,
        "audit": audit,
        "transport_station_table_B4": {
            "handoff_forward": {str(e): v
                                for e, v in table4["handoff_forward"].items()},
            "forward": {str(e): v for e, v in table4["forward"].items()},
            "reverse": {str(e): v for e, v in table4["reverse"].items()},
            "handoff_return": {str(e): v
                               for e, v in table4["handoff_return"].items()},
            "entry_gap": {str(b): g for b, g in table4["entry_gap"].items()},
            "delta": {str(e): d for e, d in table4["delta"].items()},
            "h_f_equals_f_minus_2": all(
                table4["handoff_forward"][e] == table4["forward"][e] - 2
                for e in table4["forward"]),
            "h_r_equals_r_plus_2": all(
                table4["handoff_return"][e] == table4["reverse"][e] + 2
                for e in table4["reverse"]),
        },
        "complement_valued_incident_pairs": {
            "rows": pair_shapes,
            "row_count": len(pair_shapes),
            "rows_where_measured_disagrees_with_the_derivation":
                complement_pair_bad,
            "reading": ("Exhaustive over B = 3..8 and every bank: the ring "
                        "complement VALUES realisable as a separation between "
                        "two RELAY_SWAP stations of the incident edges are "
                        "exactly the derived ones -- N - DELTA(B,e) on an "
                        "incident edge (the same-edge reverse->forward pair), "
                        "the ENTRY GAP 8(B-1-b) = f(b-1) -> r(b), and the "
                        "always-alignment-forbidden 8(B-1) = r(b-1) -> r(b).  "
                        "The entry gap is the only one of the three that belongs "
                        "to the BANK rather than to an edge, and it is the one "
                        "the census actually carries."),
        },
        "exemplar_key": {"event": 0, "token_positions": [0, 8],
                         "leader_sigma": list(leader_and_sigma((0, 8), 27))},
        "exemplar_register_events": exemplar_events[:18],
        "reading": (
            "Inside a closed quiescent stretch every bank-dirt transition is "
            "caused by a RELAY_SWAP station of an edge incident to the bank, and "
            "the crossing moves the dirt across that edge's bank pair.  No other "
            "station kind ever moves a bank's dirt while the source is quiet -- "
            "the contrast row shows the source/finalizer/handoff stations doing "
            "exactly that OUTSIDE quiescence, which is packet injection and "
            "retirement, not the clock mechanism.  This is the generating fact "
            "the whole complement derivation rests on."),
    }
    d_pass = (
        audit["transport_is_confined_to_incident_edge_stations"]
        and audit["every_pointer_crossing_is_an_edge_exchange"]
        and audit["bank_dirt_transitions_inside_closed_quiescent_stretches"] > 0
        and audit["crossings_that_are_a_clean_edge_exchange"] > 0
        and audit["contrast_outside_quiescence_non_transport_transitions"] > 0
        and complement_pair_bad == 0
        and len(pair_shapes) == sum(range(3, 9))
        and all(row["entry_gap_pair_is_forward_to_reverse"] for row in pair_shapes
                if row["entry_gap_value"] is not None)
        and involution_block["transport_station_table_B4"]["h_f_equals_f_minus_2"]
        and involution_block["transport_station_table_B4"]["h_r_equals_r_plus_2"]
    )
    lines.append(("PASS" if d_pass else "FAIL") + " D_SWAP_INVOLUTION :: "
                 + json.dumps(involution_block, **dumps))

    # -------------------------------------------------------- E  THE k-RUN LAW
    rng = random.Random(89189189)
    grid_cells, grid_bad, unbounded_cells = 0, [], 0
    for _trial in range(3000):
        stations = rng.randint(9, 60)
        runs = rng.randint(1, 5)
        phases = set()
        for _ in range(runs):
            start = rng.randrange(stations)
            width = rng.randint(1, max(1, stations // 3))
            for offset in range(width):
                phases.add((start + offset) % stations)
        if not phases or len(phases) == stations:
            continue
        period = rng.randint(2, 3 * stations)
        length = stations * 24
        word = ring_word(stations, phases, length)
        predicted = krun_imax(stations, phases, period)
        measured = max_exact_run(word, period, length)
        grid_cells += 1
        if predicted is None:
            unbounded_cells += 1
            if measured != length - period:
                grid_bad.append({"stations": stations, "phases": sorted(phases),
                                 "period": period, "predicted": "UNBOUNDED",
                                 "measured": measured})
        elif predicted != measured:
            grid_bad.append({"stations": stations, "phases": sorted(phases),
                             "period": period, "predicted": predicted,
                             "measured": measured})
    special_cells, special_bad = 0, []
    for bank_count in range(3, 9):
        stations = 8 * bank_count - 5
        for edge in range(bank_count - 1):
            delta = 8 * bank_count - 13 - 8 * edge
            for sigma in range(1, min(delta, stations - delta)):
                phases = set()
                for offset in range(sigma):
                    phases.add(offset)
                    phases.add((delta + offset) % stations)
                law889 = max(((2 * delta) % stations) - sigma,
                             stations - ((2 * delta) % stations) - sigma)
                for period in (delta, stations - delta):
                    got = krun_imax(stations, phases, period)
                    special_cells += 1
                    if got != law889:
                        special_bad.append({"banks": bank_count, "edge": edge,
                                            "sigma": sigma, "period": period,
                                            "krun": got, "law889": law889})
    # finite form on a declared grid of truncated segments
    finite_cells, finite_bad = 0, []
    for _trial in range(600):
        stations = rng.randint(11, 55)
        runs = rng.randint(2, 4)
        phases = set()
        for _ in range(runs):
            start = rng.randrange(stations)
            for offset in range(rng.randint(1, 5)):
                phases.add((start + offset) % stations)
        if not phases or len(phases) == stations:
            continue
        length = rng.randint(stations, 4 * stations)
        period = rng.randint(2, max(3, length // 2))
        word = ring_word(stations, phases, length)
        dirty = set(t for t in range(length) if not ((word >> t) & 1))
        bad_set = sorted({t for t in range(max(0, length - period))
                          if (t in dirty) != ((t + period) in dirty)})
        best, cursor = 0, 0
        limit = max(0, length - period)
        for boundary in bad_set + [limit]:
            if boundary - cursor > best:
                best = boundary - cursor
            cursor = boundary + 1
        finite_cells += 1
        if best != finite_imax(word, length, period):
            finite_bad.append({"stations": stations, "length": length,
                               "period": period, "law": best,
                               "measured": finite_imax(word, length, period)})
    # impostor controls for the run classifier
    two_run_word = set()
    for offset in range(3):
        two_run_word.add(offset)
        two_run_word.add((11 + offset) % 27)
    three_run_word = set(two_run_word) | {19, 20, 21}
    def run_count(phases, stations):
        live = sorted(set(x % stations for x in phases))
        if not live:
            return 0
        count = 0
        for value in live:
            if (value - 1) % stations not in live:
                count += 1
        return count
    law_block = {
        "statement": KRUN_LAW_STATEMENT,
        "randomised_ring_grid_cells": grid_cells,
        "randomised_ring_grid_unbounded_cells": unbounded_cells,
        "randomised_ring_grid_mismatches": len(grid_bad),
        "randomised_ring_grid_mismatch_sample": grid_bad[:WITNESS_PRINT_CAP],
        "grid_declaration": ("stations 9..60, 1..5 runs of width 1..N//3 at "
                             "uniform starts, period 2..3N, word length 24N; "
                             "seed 89189189; predicted vs measured on EVERY cell"),
        "cycle889_special_case_cells": special_cells,
        "cycle889_special_case_mismatches": len(special_bad),
        "cycle889_special_case_sample": special_bad[:WITNESS_PRINT_CAP],
        "recovers_the_pinned_889_law": not special_bad and special_cells == 580,
        "finite_form_cells": finite_cells,
        "finite_form_mismatches": len(finite_bad),
        "finite_form_sample": finite_bad[:WITNESS_PRINT_CAP],
        "impostor_two_run_word_run_count": run_count(two_run_word, 27),
        "impostor_three_run_word_run_count": run_count(three_run_word, 27),
        "impostor_three_run_is_not_two_run": run_count(three_run_word, 27) != 2,
        "impostor_two_run_is_not_k_run": run_count(two_run_word, 27) == 2,
    }
    e_pass = (
        not grid_bad and grid_cells > 2500
        and not special_bad and special_cells == 580
        and not finite_bad and finite_cells > 400
        and law_block["impostor_three_run_is_not_two_run"]
        and law_block["impostor_two_run_is_not_k_run"]
    )
    lines.append(("PASS" if e_pass else "FAIL") + " E_KRUN_LAW :: "
                 + json.dumps(law_block, **dumps))

    # ------------------------------------------- F  DERIVATION TIER  (B=4, B=5)
    pinned_episode = {int(k): v for k, v
                      in receipt_889["census_episode_instrument"].items()}
    tiers = {}
    tiers[4] = census_tier(box4, want_anatomy=True)
    del box4
    for bank_count in (3,) + tuple(b for b in DERIVATION_BANKS if b != 4):
        box = build_corpus(bank_count, HORIZON)
        tiers[bank_count] = census_tier(box, want_anatomy=bank_count in DERIVATION_BANKS)
        del box

    def incidence_report(tier):
        table = swap_station_table(tier["banks"])
        rows = Counter()
        ledger = Counter()
        cooccurrence = Counter()
        cooccurrence_witnesses = []
        label_cache = {}
        for (lane, name), (found, sigma, member_banks, event) in tier[
                "clock_periods"].items():
            deltas_here = sorted(p for p in found if p in tier["delta_set"])
            comps_here = sorted(p for p in found if p in tier["complement_set"])
            if comps_here and deltas_here:
                ledger["both_delta_and_complement"] += 1
                cooccurrence[(tuple(deltas_here), tuple(comps_here))] += 1
                if len(cooccurrence_witnesses) < 8:
                    cooccurrence_witnesses.append({
                        "banks": tier["banks"], "lane": lane, "clock": name,
                        "event": event, "sigma": sigma,
                        "delta_periods": deltas_here,
                        "complement_periods": comps_here})
            elif comps_here:
                ledger["complement_only"] += 1
            elif deltas_here:
                ledger["delta_only"] += 1
            else:
                ledger["other_periods_only"] += 1
            positions = tier["keys"][lane][1]
            for period in comps_here:
                cache_key = (period, tuple(sorted(member_banks)), positions)
                if cache_key not in label_cache:
                    label_cache[cache_key] = classify_separation(
                        table, set(member_banks), positions, period)[0]
                rows[(period, name, sigma, label_cache[cache_key])] += 1
        ledger["no_reading"] = tier["clocks_swept"] - sum(ledger.values())
        return rows, ledger, cooccurrence, cooccurrence_witnesses

    derivation_rows = []
    for bank_count in DERIVATION_BANKS:
        tier = tiers[bank_count]
        rows, ledger, cooccurrence, witnesses = incidence_report(tier)
        classes = Counter()
        for (period, label), count in tier["class_counts"].items():
            if period in tier["complement_set"]:
                classes[(period, label)] += count
        carriers = {}
        for (period, label), counter in tier["carrier_counts"].items():
            if period in tier["complement_set"] and label == "RELAY_ENTRY_GAP":
                carriers[period] = dict(sorted(counter.items()))
        pinned = pinned_episode.get(bank_count, {})
        derivation_rows.append({
            "banks": bank_count, "stations": tier["stations"],
            "clocks_swept": tier["clocks_swept"],
            "clocks_expected": tier["clocks_expected"],
            "census_complete": tier["clocks_swept"] == tier["clocks_expected"],
            "closed_quiescent_stretches": tier["closed_quiescent_stretches"],
            "longest_closed_stretch": tier["longest_closed_stretch"],
            "delta_set": tier["delta_set"],
            "complement_set": tier["complement_set"],
            "entry_gap_table": tier["entry_gap_table"],
            "spectrum": tier["spectrum"],
            "complements_observed": tier["complements_observed"],
            "delta_members_observed": tier["delta_members_observed"],
            "pinned_889_episode_spectrum": {int(k): v for k, v
                                            in pinned.get("non_orbit_spectrum",
                                                          {}).items()},
            "reproduces_pinned_889_episode_spectrum": (
                {int(k): v for k, v in pinned.get("non_orbit_spectrum", {}).items()}
                == tier["spectrum"]),
            "pinned_889_stretch_count": pinned.get(
                "closed_quiescent_stretches_swept"),
            "stretch_count_agrees": (pinned.get("closed_quiescent_stretches_swept")
                                     == tier["closed_quiescent_stretches"]),
            "pinned_889_complements_observed": pinned.get(
                "ring_complements_observed"),
            "complements_agree_with_pinned_889": (
                pinned.get("ring_complements_observed")
                == tier["complements_observed"]),
            "incidence_table_complement_carrying_clocks": [
                {"period": p, "clock": c, "sigma": s, "source_class": k,
                 "clocks": n}
                for (p, c, s, k), n in sorted(rows.items())],
            "incidence_table_row_count": len(rows),
            "completeness_ledger": dict(sorted(ledger.items())),
            "completeness_ledger_total": sum(ledger.values()),
            "every_clock_classified": sum(ledger.values()) == tier["clocks_swept"],
            "complement_source_classes": {
                "%d|%s" % (p, label): n for (p, label), n in sorted(classes.items())},
            "entry_gap_carrier_banks_measured": {
                str(p): v for p, v in sorted(carriers.items())},
            "cooccurrence_delta_and_complement_on_one_clock": {
                "clocks": ledger.get("both_delta_and_complement", 0),
                "patterns": {"%s|%s" % (d, c): n
                             for (d, c), n in sorted(cooccurrence.items())},
                "witnesses": witnesses},
            "anatomy_sample": tier["anatomy"][:WITNESS_PRINT_CAP],
        })

    # THE SEAL.  Computed here, before any holdout corpus exists.
    rule_source = inspect.getsource(predicted_complement_rows)
    rule_source_digest = sha256(rule_source.encode()).hexdigest()
    rule_body = ast.parse(rule_source.strip()).body[0]
    if (rule_body.body and isinstance(rule_body.body[0], ast.Expr)
            and isinstance(rule_body.body[0].value, ast.Constant)):
        rule_body.body = rule_body.body[1:]      # drop the docstring, keep the code
    rule_code_only = ast.dump(rule_body)
    seal_payload = {
        "rule_text": COMPLEMENT_RULE_TEXT,
        "rule_source": rule_source,
        "rule_source_sha256": rule_source_digest,
        "predictions": {str(bc): {"set": predicted_complement_set(bc),
                                  "carriers": {str(k): v for k, v
                                               in predicted_carriers(bc).items()}}
                        for bc in range(3, 9)},
        "build_log_at_seal_time": list(BUILD_LOG),
        "derivation_banks": list(DERIVATION_BANKS),
        "holdout_banks": list(HOLDOUT_BANKS),
    }
    SEAL = digest(seal_payload)
    seal_touched_holdout = any(row["banks"] in HOLDOUT_BANKS for row in BUILD_LOG)
    rule_reads_measurements = any(
        token in rule_code_only
        for token in ("tier", "census", "spectrum", "observed", "receipt",
                      "BUILD_LOG", "clock_periods", "anatomy", "box",
                      "PREFLIGHT", "blocks_889", "receipt_889"))

    f_pass = (
        all(row["census_complete"] for row in derivation_rows)
        and all(row["every_clock_classified"] for row in derivation_rows)
        and all(row["reproduces_pinned_889_episode_spectrum"]
                for row in derivation_rows)
        and all(row["stretch_count_agrees"] for row in derivation_rows)
        and all(row["incidence_table_row_count"] > 0 for row in derivation_rows)
        and not seal_touched_holdout
        and not rule_reads_measurements
    )
    lines.append(("PASS" if f_pass else "FAIL") + " F_DERIVATION_B45 :: "
                 + json.dumps({
                     "mechanism": MECHANISM_STATEMENT,
                     "rows": derivation_rows,
                     "rule_text": COMPLEMENT_RULE_TEXT,
                     "rule_source_sha256": rule_source_digest,
                     "rule_source": rule_source,
                     "rule_reads_no_measurement": not rule_reads_measurements,
                     "rule_free_variables": sorted(
                         {node.id for node in ast.walk(rule_body)
                          if isinstance(node, ast.Name)}),
                     "SEAL_sha256": SEAL,
                     "build_log_at_seal_time": list(BUILD_LOG),
                     "seal_predates_every_holdout_corpus": not seal_touched_holdout,
                     "declared_split": {"derivation": list(DERIVATION_BANKS),
                                        "holdout": list(HOLDOUT_BANKS)},
                 }, **dumps))

    # ---------------------------------------------------- G  HOLDOUT (B=6, B=7)
    holdout_rows = []
    b7_tier = None
    box7 = None
    for bank_count in HOLDOUT_BANKS:
        predicted = predicted_complement_set(bank_count)
        carriers = predicted_carriers(bank_count)
        box = build_corpus(bank_count, HORIZON)
        tier = census_tier(box, want_anatomy=True)
        if bank_count == 7:
            b7_tier = tier
            box7 = box
        else:
            del box
        rows, ledger, cooccurrence, witnesses = incidence_report(tier)
        observed = tier["complements_observed"]
        measured_carriers = {}
        for (period, label), counter in tier["carrier_counts"].items():
            if period in tier["complement_set"] and label == "RELAY_ENTRY_GAP":
                measured_carriers[period] = dict(sorted(counter.items()))
        episode_counts = {p: tier["spectrum"].get(p, 0)
                          for p in tier["complement_set"]}
        residuals = sorted(p for p in observed if p not in predicted)
        missed = sorted(p for p in predicted if p not in observed)
        carrier_hits = {}
        for period, want in sorted(carriers.items()):
            got = measured_carriers.get(period, {})
            bank_clocks = {b: n for b, n in got.items()}
            carrier_hits[str(period)] = {
                "predicted_carrier_bank": want,
                "measured_entry_gap_banks": bank_clocks,
                "predicted_carrier_present": want in bank_clocks,
                "predicted_carrier_is_the_top_entry_gap_bank": (
                    bool(bank_clocks)
                    and max(bank_clocks, key=lambda b: (bank_clocks[b], -b)) == want),
            }
        pinned = pinned_episode.get(bank_count, {})
        holdout_rows.append({
            "banks": bank_count, "stations": tier["stations"],
            "clocks_swept": tier["clocks_swept"],
            "census_complete": tier["clocks_swept"] == tier["clocks_expected"],
            "closed_quiescent_stretches": tier["closed_quiescent_stretches"],
            "longest_closed_stretch": tier["longest_closed_stretch"],
            "complement_set": tier["complement_set"],
            "PREDICTED_from_the_sealed_rule": predicted,
            "PREDICTED_carriers": {str(k): v for k, v in carriers.items()},
            "OBSERVED": observed,
            "observed_episode_counts": {str(k): v
                                        for k, v in episode_counts.items()},
            "predicted_all_present": not missed,
            "predicted_missing": missed,
            "residuals_observed_but_not_predicted": residuals,
            "residual_episode_counts": {str(p): tier["spectrum"].get(p, 0)
                                        for p in residuals},
            "carrier_verification": carrier_hits,
            "reproduces_pinned_889_episode_spectrum": (
                {int(k): v for k, v in pinned.get("non_orbit_spectrum", {}).items()}
                == tier["spectrum"]),
            "complements_agree_with_pinned_889": (
                pinned.get("ring_complements_observed")
                == tier["complements_observed"]),
            "stretch_count_agrees": (pinned.get("closed_quiescent_stretches_swept")
                                     == tier["closed_quiescent_stretches"]),
            "incidence_table_complement_carrying_clocks": [
                {"period": p, "clock": c, "sigma": s, "source_class": k,
                 "clocks": n}
                for (p, c, s, k), n in sorted(rows.items())][:80],
            "completeness_ledger": dict(sorted(ledger.items())),
            "every_clock_classified": sum(ledger.values()) == tier["clocks_swept"],
            "cooccurrence_clocks": ledger.get("both_delta_and_complement", 0),
        })
    post_seal = digest({
        "rule_text": COMPLEMENT_RULE_TEXT,
        "rule_source": inspect.getsource(predicted_complement_rows),
        "rule_source_sha256": sha256(
            inspect.getsource(predicted_complement_rows).encode()).hexdigest(),
        "predictions": {str(bc): {"set": predicted_complement_set(bc),
                                  "carriers": {str(k): v for k, v
                                               in predicted_carriers(bc).items()}}
                        for bc in range(3, 9)},
        "build_log_at_seal_time": seal_payload["build_log_at_seal_time"],
        "derivation_banks": list(DERIVATION_BANKS),
        "holdout_banks": list(HOLDOUT_BANKS),
    })
    holdout_block = {
        "discipline": (
            "The rule was frozen and its SEAL printed in F_DERIVATION_B45 before "
            "any B=6 or B=7 corpus existed; BUILD_LOG at seal time is published "
            "and contains only the derivation and control tiers.  The rule is a "
            "pure function of the bank count -- it reads no census, corpus, "
            "receipt or measured quantity -- and re-digesting it after the "
            "holdout reproduces the seal byte for byte."),
        "SEAL_sha256": SEAL,
        "SEAL_recomputed_after_holdout": post_seal,
        "seal_unchanged": SEAL == post_seal,
        "build_log_at_seal_time": seal_payload["build_log_at_seal_time"],
        "build_log_final": list(BUILD_LOG),
        "seal_predates_every_holdout_corpus": not seal_touched_holdout,
        "rows": holdout_rows,
    }
    g_pass = (
        holdout_block["seal_unchanged"]
        and holdout_block["seal_predates_every_holdout_corpus"]
        and all(row["census_complete"] for row in holdout_rows)
        and all(row["every_clock_classified"] for row in holdout_rows)
        and all(row["reproduces_pinned_889_episode_spectrum"] for row in holdout_rows)
        and all(row["stretch_count_agrees"] for row in holdout_rows)
    )
    lines.append(("PASS" if g_pass else "FAIL") + " G_HOLDOUT_B67 :: "
                 + json.dumps(holdout_block, **dumps))

    # ------------------------------------------------- H  THE NON-TWO-RUN DIRT
    stations7 = b7_tier["stations"]
    named_open = sorted({35, 43} | {p for p in b7_tier["complements_observed"]
                                    if p not in predicted_complement_set(7)})
    anatomies = {period: sorted(b7_tier["anatomy_by_period"].get(period, []),
                                key=lambda row: row["stretch"][0])
                 for period in named_open}
    anatomies = {p: rows for p, rows in anatomies.items() if rows}
    witness_rows = []
    for period in sorted(anatomies):
        sample = anatomies[period][0]
        witness_rows.append({
            "period": period,
            "period_kind": sample["period_kind"],
            "episodes_with_anatomy_captured": len(anatomies[period]),
            "episodes_in_census": b7_tier["spectrum"].get(period, 0),
            "clock": sample["clock"], "lane": sample["lane"],
            "event": sample["event"],
            "token_positions": sample["token_positions"],
            "sigma": sample["sigma"], "leader": sample["leader"],
            "stretch": sample["stretch"], "stretch_len": sample["stretch_len"],
            "dirty_runs_in_the_stretch": sample["dirty_runs"],
            "run_start_ticks": sample["run_start_ticks"],
            "run_widths": sample["run_widths"],
            "consecutive_gaps": sample["consecutive_gaps"],
            "is_the_pure_two_run_pattern": sample["two_run_pattern"],
            "source_class": sample["source_class"],
            "source_classes_available": sample["source_classes_available"],
            "station_witness": sample["station_witness"],
            "detector": sample["detector"],
        })
    run_histogram = Counter()
    class_histogram = Counter()
    for period in sorted(anatomies):
        for row in anatomies[period]:
            run_histogram[(period, row["dirty_runs"])] += 1
            class_histogram[(period, row["source_class"])] += 1
    # register-level anatomy for one witness of each named-open period
    register_traces = []
    for row in witness_rows[:4]:
        low, high = row["stretch"]
        events = attributed_trace(box7, row["event"], tuple(row["token_positions"]),
                                  max(1, low - 2), min(high + 2, HORIZON))
        register_traces.append({
            "period": row["period"], "clock": row["clock"],
            "token_positions": row["token_positions"],
            "stretch": row["stretch"],
            "register_events": events[:26],
            "event_count": len(events),
        })
    # k-run law applied to the witnesses, finite form (the stretch is what fires)
    lanes7 = box7["lane_count"]
    bank_masks7 = [transpose_planes(box7["clean_planes"][b], lanes7, HORIZON)
                   for b in range(7)]
    law_checks = []
    for row in witness_rows:
        low, high = row["stretch"]
        name = row["clock"]
        lane = row["lane"]
        if name.startswith("bank"):
            mask = bank_masks7[int(name[4:])][lane]
        else:
            left, right = int(name[4]), int(name[5])
            mask = bank_masks7[left][lane] & bank_masks7[right][lane]
        length = high - low + 1
        segment = (mask >> low) & ((1 << length) - 1)
        period = row["period"]
        dirty = set(t for t in range(length) if not ((segment >> t) & 1))
        limit = max(0, length - period)
        bad_set = sorted({t for t in range(limit)
                          if (t in dirty) != ((t + period) in dirty)})
        best, cursor = 0, 0
        for boundary in bad_set + [limit]:
            best = max(best, boundary - cursor)
            cursor = boundary + 1
        phases = set(t % stations7 for t in dirty)
        ring_prediction = krun_imax(stations7, phases, period)
        law_checks.append({
            "period": period, "clock": name, "lane": lane,
            "finite_I_max_law": best,
            "finite_I_max_measured": finite_imax(segment, length, period),
            "finite_form_exact": best == finite_imax(segment, length, period),
            "two_repeats_need": period + 1,
            "finite_form_admits": best >= period + 1,
            "ring_form_I_max": ring_prediction,
            "ring_form_admits": (ring_prediction is None
                                 or ring_prediction >= period + 1),
            "ring_form_would_have_refused": (ring_prediction is not None
                                             and ring_prediction < period + 1),
        })
    del bank_masks7, box7
    nontworun_block = {
        "named_open_periods_at_B7": named_open,
        "witnesses": witness_rows,
        "runs_per_episode_histogram": {"%d|%d" % k: v
                                       for k, v in sorted(run_histogram.items())},
        "source_class_histogram": {"%d|%s" % k: v
                                   for k, v in sorted(class_histogram.items())},
        "register_level_traces": register_traces,
        "krun_law_on_the_witnesses": law_checks,
        "finite_form_exact_on_every_witness": all(row["finite_form_exact"]
                                                  for row in law_checks),
        "every_witness_admitted_by_the_finite_form": all(
            row["finite_form_admits"] for row in law_checks),
        "witnesses_the_ring_form_would_have_refused": [
            row["period"] for row in law_checks if row["ring_form_would_have_refused"]],
        "reading": (
            "The B=7 out-of-law periods do not need a new alignment law: they "
            "need the FINITE form of the one stated here.  A closed quiescent "
            "stretch does not carry the full orbit-periodic run pattern; where "
            "the pattern is incomplete the segment's dirty set has fewer runs "
            "than the ring word, the ring-form forbidden zones that would have "
            "killed the period are simply not present inside the segment, and "
            "the reading is exact on the segment.  The k-run law is verified "
            "exactly in BOTH forms; the ring form is the sub-case in which the "
            "stretch carries the whole pattern."),
    }
    h_pass = (
        len(witness_rows) > 0
        and nontworun_block["finite_form_exact_on_every_witness"]
        and len(register_traces) > 0
        and all(row["event_count"] > 0 for row in register_traces)
    )
    lines.append(("PASS" if h_pass else "FAIL") + " H_NONTWORUN_B7 :: "
                 + json.dumps(nontworun_block, **dumps))

    # ---------------------------------------------------------------- I VERDICT
    predicted_67 = {bc: predicted_complement_set(bc) for bc in HOLDOUT_BANKS}
    observed_67 = {row["banks"]: row["OBSERVED"] for row in holdout_rows}
    verdict = {
        "Q1_mechanism": MECHANISM_STATEMENT,
        "Q1_rule": COMPLEMENT_RULE_TEXT,
        "Q1_holdout": {
            "predicted": {str(k): v for k, v in predicted_67.items()},
            "observed": {str(k): v for k, v in observed_67.items()},
            "exact_match": {str(k): predicted_67[k] == observed_67[k]
                            for k in predicted_67},
            "predicted_all_present": {
                str(row["banks"]): row["predicted_all_present"]
                for row in holdout_rows},
            "residuals": {str(row["banks"]):
                          row["residuals_observed_but_not_predicted"]
                          for row in holdout_rows},
            "residual_episode_counts": {str(row["banks"]):
                                        row["residual_episode_counts"]
                                        for row in holdout_rows},
            "carrier_verification": {str(row["banks"]): row["carrier_verification"]
                                     for row in holdout_rows},
        },
        "Q1_cooccurrence": {
            "question": "can a complement and a DELTA period be read on ONE "
                        "clock at different stretches?",
            "clocks_carrying_both_by_bank_count": {
                str(row["banks"]): row["cooccurrence_delta_and_complement_on_one_clock"][
                    "clocks"] for row in derivation_rows},
            "holdout_tiers": {str(row["banks"]): row["cooccurrence_clocks"]
                              for row in holdout_rows},
            "witnesses": [w for row in derivation_rows
                          for w in row["cooccurrence_delta_and_complement_on_one_clock"][
                              "witnesses"]][:8],
        },
        "Q2_status": {
            "k_run_law": "DERIVED AND VERIFIED (ring form and finite form)",
            "ring_cells": grid_cells, "ring_mismatches": len(grid_bad),
            "finite_cells": finite_cells, "finite_mismatches": len(finite_bad),
            "recovers_889_law_cells": special_cells,
            "B7_named_open_periods": named_open,
            "B7_finite_form_exact_on_every_witness":
                nontworun_block["finite_form_exact_on_every_witness"],
            "boundary": (
                "The general law is exact for ANY dirty-run structure, but it is "
                "a law about a WORD.  What it does not derive is which word a "
                "given quiescent stretch carries: the incompleteness of the "
                "orbit-periodic run pattern inside a short stretch is a "
                "dynamical fact, measured here per witness, not derived."),
        },
        "runtime_note": "see J_CONTROLS",
    }
    lines.append("PASS I_VERDICT :: " + json.dumps(verdict, **dumps))

    # --------------------------------------------------------------- J CONTROLS
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
        "bank_counts_swept": sorted(set(row["banks"] for row in BUILD_LOG)),
        "build_log": list(BUILD_LOG),
        "horizon": HORIZON,
        "seal_sha256": SEAL,
        "disclosed_deviations": list(DISCLOSED_DEVIATIONS),
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
            ("\n".join(lines + [j_line, "CYCLE891_COMPLEMENT_MECHANISM_PASS"]) + "\n")
            .encode())
    j_core["stdout_bytes"] = stdout_bytes
    j_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    j_pass = j_prepass and j_core["stdout_under_150KB"]
    j_line = (("PASS" if j_pass else "FAIL") + " J_CONTROLS :: "
              + json.dumps(j_core, **dumps))
    final = ("CYCLE891_COMPLEMENT_MECHANISM_PASS" if all(verdicts) and j_pass
             else "CYCLE891_COMPLEMENT_MECHANISM_HONEST_FAIL")
    print("\n".join(lines + [j_line, final]))
    return 0 if all(verdicts) and j_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
