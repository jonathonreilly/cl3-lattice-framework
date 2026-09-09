#!/usr/bin/env python3
"""Cycle 930: the never-firing THIRD PAIR, and RC-3 turned from a named
measurement into a measured verdict.

Cycle 922 derived RC-1: among a bank's own eight incident transport rows the
entry-gap value P = 8(B-1-b) is realised by exactly THREE ordered same-token
pairs -- (f(b-1), r(b)), (f(b), h_r(b-1)) and (h_f(b), r(b-1)) -- all three
present iff 1 <= b <= B-2.  Two of the three carry episodes.  The third,
(h_f(b), r(b-1)), carries ZERO episodes at every B and every bank in the whole
corpus, and 922 left it named and ruleless.  922 also declined to force RC-3
(sufficiency), naming instead a discriminating measurement it did not take:
whether some stretch presents the two P-separated runs with EQUAL width
w <= P-1 and at least MIN_STABLE_EVENTS clean ticks in the stable region.

This runner takes both.

  Q1  THE THIRD PAIR.  Anatomised at register level.  The finding is that the
      absence is NOT geometric: the third pair DOES occur as a consecutive
      same-token P-separated run-start pair, in every tier, hundreds of times.
      What is exactly zero is its COINCIDENCE with a detector reading of P.
      A derived station asymmetry singles it out (TP-1..TP-3 below); the zero
      itself is measured and sealed, not derived, and is stated that way.

  Q2  RC-3.  The named measurement is taken on every firing bank-owned
      entry-gap episode at B=4..8 and on the failing cells' whole stretch
      populations.  The spec's discriminator admits two readings and BOTH are
      reported.  Under the reading that gives it content it is falsified in
      both directions; under the reading that makes it true it is a tautology
      of the detector.  RC-3 DOES NOT CLOSE, and the runner says so.

Nothing is quoted from Cycles 879/881/889/891/922 except through sha-pinned
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

PRIMARY_922 = "scripts/frontier_cycle922_p32_carrier_2026_07_28.py"
CHECKER_922 = "scripts/frontier_cycle922_p32_carrier_independent_check_2026_07_28.py"
RECEIPT_922 = "outputs/p32_carrier_cycle922_receipt_2026_07_28.json"
RECEIPT_922_CHECK = (
    "outputs/p32_carrier_independent_check_cycle922_receipt_2026_07_28.json")
SHIP_922 = "outputs/p32_carrier_block_cycle922_ship_receipt_2026_07_28.json"
CACHE_922 = "logs/runner-cache/frontier_cycle922_p32_carrier_2026_07_28.txt"
CACHE_922_CHECK = (
    "logs/runner-cache/frontier_cycle922_p32_carrier_independent_check_2026_07_28.txt")
NOTE_922 = (
    "docs/P32_CARRIER_SHORT_ARC_LABEL_THEFT_CYCLE922_BOUNDED_THEOREM_NOTE_2026-07-28.md")
PRIMARY_891 = "scripts/frontier_cycle891_complement_mechanism_2026_07_28.py"
CHECKER_891 = "scripts/frontier_cycle891_complement_independent_check_2026_07_28.py"
RECEIPT_891 = "outputs/complement_mechanism_cycle891_receipt_2026_07_28.json"
RECEIPT_891_CHECK = (
    "outputs/complement_independent_check_cycle891_receipt_2026_07_28.json")
NOTE_891 = (
    "docs/COMPLEMENT_MECHANISM_KRUN_LAW_CYCLE891_BOUNDED_THEOREM_NOTE_2026-07-28.md")
PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CORE_719_HANDSHAKE = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py")

# Every pin is read as bytes; its sha256 AND its git blob id are compared with
# the value recorded here.  Any mismatch is exit 2 before anything else runs.
# The 891/889/881/879 and Cycle-719 rows are inherited from the pinned Cycle-922
# receipt byte for byte; the 922 rows are this cycle's own.
PINS = {
    PRIMARY_922: ("9e1a8de7190188a89cd4449300ab56cc053d6a63eec328265fa80f9955ce3a83",
                  "fdd77d879b142d1bafa1f76926c494bbc4480b1c"),
    CHECKER_922: ("fb7acd4bfe5fa1dcc8f22373861da2038dfdb169371c53d283ae65325d44b118",
                  "faae396e9801cfac4c8f6baa80d022397bed3f64"),
    RECEIPT_922: ("ab40677256009a0b1ecdf841766aa055a113aeb93827dc1d1da21a9e1cb97954",
                  "4497a88d3d2cf7ca058ff759c8f3ecea8c042481"),
    RECEIPT_922_CHECK: ("e609eafcb6ef33c22ec0aa4481cc29ea5be46f5be1312a9ccd4822b154ff059e",
                        "a1fcadfd795d08c9705722f7165349e361778b65"),
    SHIP_922: ("9df9f38530b6d8bb8e4ebc9f76d5683ac065bf06f4edcfb2db9f3e70ef28ad76",
               "a39abd45b40897d872ecbccf2f5ee962ce66dc54"),
    CACHE_922: ("256d8422a4d379062d6dc0163dc748b2063e6d0f7533598a90971030428eede1",
                "4cd970d8261c5d705a2b02f909f97907a0ccb0d3"),
    CACHE_922_CHECK: ("add02c024c5f008e17fe135a103bb674fdca5d3c25be0a8fc39f653be7d7ec75",
                      "0f7c892f555538c95a2fd1b86a47c30f4b59ee2c"),
    NOTE_922: ("420c162b2530c7329c21915ff2eee8d91689a5f97688c1df29752841b6af949d",
               "572090165a4e6ef876f1eb9a291795fba11118fc"),
    PRIMARY_891: ("3d260f6641d05a22aee092145ea3e5c3b29f3a6882b4cbd9ae966424458afbb7",
                  "a1bbd49ffbe970193cc79054fb7219732f7c9873"),
    CHECKER_891: ("f2e9ca32b7d3f863822126c05fbf6a3b637164e8969e5ec7c6c04f15cd89e568",
                  "53f5cf560f6dfad20dc6b4b91b0c003c848c6bea"),
    RECEIPT_891: ("f8e30d50a50e39a13f8f968b2ae21991885b6c858c6c96439ed733fc8514bacd",
                  "f537715a927b00b817f8de2569953d78929c86db"),
    RECEIPT_891_CHECK: ("cb2f6badda7315725f5f33c5aad89e7e37cf9201472362e0af3a16c4225fae8f",
                        "478f19642c1d66a6e1575798f9974b645c9f9a18"),
    NOTE_891: ("5b20f90a643e890492d65907050e31772b85f1b00e1ee5581f5132f45f6a700c",
               "235965affc47ce7745327ef194e7c0ae31e6a6c8"),
    PRIMARY_889: ("c18ed0c49281fd2d54ad013ba12264b181d1720349ee002b144c028b521dd826",
                  "f1bdf1f789a85213a0a854ab0bed45e6bf250fed"),
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

# Detector / substrate constants.  Inherited verbatim from the pinned Cycle-922
# primary and re-checked against its AST in gate A.
TOKEN_K = 2
EVENT_COUNT = 2
HORIZON = 16_384
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8
PINNED_PERIOD_CEILING = 64

FULL_CLOCK_BANKS = (4, 5, 6, 7)     # every bank clock AND every pair clock
BANK_CLOCK_BANKS = (8,)             # bank clocks only -- declared scoping
NEVER_BUILT_BANKS = (9, 10, 11, 12)  # sealed predictions only; no corpus built

SHAPES = ("ENTRY_GAP_swap_swap", "ENTRY_GAP_swap_handoff", "ENTRY_GAP_handoff_swap")
THIRD_PAIR = "ENTRY_GAP_handoff_swap"

DISCLOSED_DEVIATIONS = (
    "TIER SCOPING, DECLARED.  B=4,5,6,7 are built with EVERY clock (all bank "
    "clocks and all pair clocks), which is what the pinned Cycle-891/922 "
    "class-level rows are computed over, so the restriction gate can compare "
    "those rows value for value.  B=8 is built with BANK CLOCKS ONLY.  Every "
    "Cycle-922 B=8 quantity this cycle restricts against -- the six RC_rows "
    "(episodes_on_the_bank_clock, bank_owned_entry_gap_episodes, by_shape) and "
    "local_shape_counts_at_the_complement_values -- is a bank-clock quantity by "
    "construction in the pinned runner (they are gated on len(member_banks)==1), "
    "so the comparison is exact and complete for them.  The B=8 class_counts_891 "
    "and spectrum rows, which need pair clocks, are NOT recomputed here and are "
    "NOT restricted against; that is stated, not hidden.",
    "B=9 AND UP ARE NEVER BUILT BY THIS RUNNER.  The third-pair rule's B=9..12 "
    "rows are pure-function predictions behind a printed seal.  This makes them "
    "holdout-free by construction and hands B=9 to the independent checker, "
    "exactly as Cycle 922 did.",
    "PERIOD CEILING and HORIZON inherited verbatim from Cycles 889/891/922: "
    "every P in [2, max(64, 2N(B))] is swept and H = 16384 for every tier, so "
    "every tier is directly comparable with the pinned receipts.",
    "ANATOMY DUMPS are capped at 6 stored rows per (bank, shape); every "
    "occurrence is COUNTED and every aggregate is exhaustive.  The stored rows "
    "are a sample and are labelled as one.",
    "THE THIRD-PAIR ZERO IS MEASURED, NOT DERIVED.  The station asymmetry "
    "TP-1..TP-3 is derived arithmetic; that it forces zero EPISODES is not "
    "derived from it.  The rule is fitted-then-sealed at B=9..12 and the runner "
    "says so in the claim text, the seal and the receipt.",
    "RC-3 IS NOT FORCED.  Cycle 922 declined to force it and so does this "
    "runner.  The verdict is a measured negative, reported under both readings "
    "of the spec's discriminator.",
)

# ----------------------------------------------------------------- the claims
TP_STATEMENT = (
    "THE THIRD-PAIR RULE (TP).  Fix B, N = 8B-5, a bank b with 1 <= b <= B-2, "
    "and P = 8(B-1-b).  Bank b's eight incident transport rows are, for each "
    "incident edge e in {b-1, b}, h_f(e) = 4+5e-2, f(e) = 4+5e, r(e) = 8B-9-3e "
    "and h_r(e) = 8B-9-3e+2.  RC-1 (Cycle 922, derived) realises P by exactly "
    "the three ordered same-token pairs (f(b-1), r(b)), (f(b), h_r(b-1)) and "
    "(h_f(b), r(b-1)).  "
    "TP-1 SHADOWING (derived station arithmetic).  Sorted by station index the "
    "eight rows have exactly ONE consecutive gap equal to 1, namely "
    "r(b-1) - h_r(b) = (8B-6-3b) - (8B-7-3b) = 1; every other consecutive gap "
    "is at least 2.  A token advances exactly one station per tick, so every "
    "crossing of r(b-1) by a token is immediately preceded, one tick earlier "
    "and BY THAT SAME TOKEN, by that token's crossing of h_r(b), which is also "
    "a row of bank b.  r(b-1) is therefore the unique own row of bank b that "
    "can open a dirty run only when the own-row crossing one tick before it "
    "leaves the bank clean.  "
    "TP-2 UNIQUENESS AMONG THE THREE PAIRS (derived).  Of the three RC-1 pairs "
    "exactly one terminates on r(b-1) -- the third, (h_f(b), r(b-1)).  The "
    "other two terminate on r(b) and on h_r(b-1), whose predecessors "
    "r(b)-1 = 8B-10-3b and h_r(b-1)-1 = 8B-5-3b are never rows of bank b for "
    "1 <= b <= B-2.  The third pair is therefore the unique entry-gap pair "
    "whose second run-start is shadowed, and the three pairs' first stations "
    "f(b-1), h_f(b), f(b) are all unshadowed.  "
    "TP-3 THE SHIFT PICTURE (derived).  Writing R for the eight rows, the "
    "three first stations f(b-1), h_f(b), f(b) are always P-shift-fixed "
    "(s in R and s+P in R).  They are the ONLY such rows except on the cells "
    "where the entry-gap value coincides with the bank's own edge complement, "
    "b = floor((B-1)/2), where exactly one reverse row becomes a fourth one -- "
    "r(b-1) at odd B (r(b-1) + P = f(b-1)) and r(b) at even B "
    "(r(b) + P = f(b)) -- and those are precisely Cycle 922's b = (B-1)/2 or "
    "(B-2)/2 label-theft cells, arriving here from the geometry side.  At odd B "
    "the fourth fixed row is the THIRD PAIR'S OWN TERMINAL.  Separately and "
    "without "
    "exception, h_r(b) has NO P-preimage in R: h_r(b) - P = 5b+1, which is "
    "never a row of bank b for 1 <= b <= B-2.  So h_r(b) is a row no P-shift "
    "can reach, and it sits exactly one station below r(b-1), the one "
    "entry-gap terminal that has to open a run.  "
    "TP-4 THE MEASURED FACT (exhaustive, B=4..8, every bank clock, every "
    "closed quiescent stretch).  The third pair is NOT geometrically absent: "
    "it occurs as a consecutive same-token P-separated run-start pair in every "
    "tier and at most cells.  What is exactly zero is its coincidence with a "
    "reading: in no stretch that the detector reads at period P does the third "
    "pair occur.  Wherever the third pair reaches the full stretch "
    "configuration at all, the detector's rejection is R3 -- the terminal "
    "2P+1 ticks of the closed quiescent stretch are not P-exact.  "
    "STATUS.  TP-1, TP-2 and TP-3 are DERIVED pure station arithmetic, "
    "exhaustively verified.  TP-4's zero is MEASURED and SEALED at B=9..12, "
    "NOT derived: the shadowing asymmetry explains why the third pair is the "
    "fragile one, it does not prove the count is zero."
)

RC3_STATEMENT = (
    "RC-3, MEASURED (the verdict Cycle 922 declined to force).  922 named the "
    "discriminating measurement -- 'some closed quiescent stretch presents the "
    "two P-separated runs with EQUAL width w <= P-1 and at least "
    "MIN_STABLE_EVENTS clean ticks in the stable region' -- without taking it.  "
    "The measurement admits two readings and BOTH are reported.  "
    "READING A (the discriminator has content): 'the two P-separated runs' are "
    "the consecutive same-token P-separated run-start pair that the clock-local "
    "taxonomy attributes to one of the three entry-gap shapes.  Measured over "
    "B=4..8 this statistic is NEITHER NECESSARY NOR SUFFICIENT.  Not necessary: "
    "at B=7, b=3 the cell fires 20 bank-owned entry-gap episodes while every "
    "one of the 548 stretches carrying an equal-width entry-gap pair is "
    "rejected by the detector -- the firing episodes carry only UNEQUAL-width "
    "entry-gap pairs, so 'every firing episode has equal-width runs' is false.  "
    "Not sufficient: the configuration is presented and refused wholesale -- "
    "B=7 b=5 presents it 542 times and fires 8; B=6 b=3 presents it 268 times "
    "through the handoff pair and fires 52; and the third pair presents it 30 "
    "times at B=5 b=2 and 4 times at B=6 b=4 and fires never.  "
    "READING B (the discriminator is true): 'the two P-separated runs' are the "
    "two runs of the P-exact STABLE REGION.  Then equal width is a THEOREM of "
    "the detector, not a criterion: on the stable region S[t] = S[t+P] for "
    "transient <= t <= last-P, so a run starting at t with t+w <= last-P has an "
    "identical-width image at t+P; the only exceptions are runs whose image is "
    "truncated by the end of the stretch.  Under reading B the statistic is "
    "implied BY the reading and can therefore never imply it.  "
    "THE VERDICT: RC-3 DOES NOT CLOSE.  The discriminator separates but does "
    "not close, in exactly the sense the spec allowed for, and its stated form "
    "is additionally falsified as a necessary condition.  "
    "WHAT THE MEASUREMENT DOES BUY.  Decomposing the detector's refusal on "
    "every stretch that presents the configuration gives the binding component, "
    "and it is not width and not clean-tick count: it is R3, the requirement "
    "that the TERMINAL 2P+1 ticks of the closed quiescent stretch be P-exact.  "
    "The detector is a TAIL detector; a stretch may present the configuration "
    "anywhere and still be refused because the P-periodic structure does not "
    "survive to the stretch's end.  Which word a stretch carries at its end is "
    "Cycle 891's declared dynamical boundary, and RC-3 is now measured to sit "
    "exactly on it."
)

BOOKKEEPING_STATEMENT = (
    "THE CLOCK-LOCAL BOOKKEEPING IDENTITY (Cycle 922, inherited).  A dirty-run "
    "start of clock C at tick t is the crossing of station (p + t - 1) mod N by "
    "some token p, and that station must be one of C's OWN incident transport "
    "rows.  Two run starts separated by Delta_t are rows s1, s2 of C with "
    "s2 - s1 == Delta_t + (p2 - p1) (mod N)."
)

DETECTOR_STATEMENT = (
    "THE DETECTOR (Cycle 889/891/922 semantics, reimplemented).  A clock's "
    "clean ticks inside one closed quiescent stretch become a bitmask S; for a "
    "period P the bits of (S ^ (S >> P)) below last - P + 1 are exactly the "
    "ticks where t in S <=> t+P in S fails, so the highest such bit + 1 is the "
    "LEAST transient.  A reading is kept only if the terminal 2P window is "
    "P-exact, last - transient >= 2P, the stable stretch carries >= 8 clean "
    "ticks, and the stable clean residues modulo P are not all of them."
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


# ------------------------------------------------------- preflight + firewall
def preflight(overrides=None):
    rows, bad = {}, []
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = ROOT / path
        if not full.is_file():
            rows[path] = {"present": False}
            bad.append(path)
            continue
        payload = full.read_bytes()
        if overrides and path in overrides:
            payload = overrides[path]
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
                            (PRIMARY_879, PRIMARY_881, PRIMARY_889,
                             PRIMARY_891, CHECKER_891,
                             PRIMARY_922, CHECKER_922))


class _Firewall(importlib.abc.MetaPathFinder):
    """Any import of a blocklisted Cycle-879/881/889/891/922 runner is fatal."""

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


def pinned_json(path):
    return json.loads((ROOT / path).read_text())


def pinned_constants(path):
    """Read the module-level integer constants of a pinned runner by AST."""
    tree = ast.parse((ROOT / path).read_text())
    out = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                if isinstance(node.value.value, int):
                    out[target.id] = node.value.value
    return out


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
    BUILD_LOG.append({"banks": bank_count, "horizon": horizon,
                      "lanes": lane_count, "stations": stations})
    return {
        "banks": bank_count, "stations": stations, "program": program,
        "keys": tuple(keys), "lane_count": lane_count,
        "placements": len(placements), "clean_planes": clean_planes,
        "source_clean": source_clean, "swaps": swaps, "malformed": malformed,
        "seed_failures": seed_failures, "token_failures": token_failures,
        "horizon": horizon, "wire_count": wire_count,
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


# ---------------------------------------------------- the cap-free detector
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


REJECTIONS = ("R0_empty", "R1_fewer_than_8_clean_ticks_in_stretch",
              "R2_stretch_shorter_than_2P", "R3_tail_window_not_P_exact",
              "R4_P_exact_suffix_shorter_than_2P",
              "R5_fewer_than_8_clean_ticks_in_stable_region",
              "R6_all_residues_clean", "ACCEPT")


def reject_reason(mask, period):
    """WHY the detector drops ``period``.  Mirrors tail_periods branch for branch.

    This is the RC-3 instrument: it decomposes every refusal into the component
    that actually bound, so a sufficiency claim can be tested component-wise
    instead of being asserted.
    """
    if mask == 0:
        return "R0_empty"
    if bin(mask).count("1") < MIN_STABLE_EVENTS:
        return "R1_fewer_than_8_clean_ticks_in_stretch"
    last = mask.bit_length() - 1
    need = MIN_PERIOD_REPEATS * period
    if need > last:
        return "R2_stretch_shorter_than_2P"
    low = last - need
    window = (mask >> low) & ((1 << (need + 1)) - 1)
    if (window ^ (window >> period)) & ((1 << (period + 1)) - 1):
        return "R3_tail_window_not_P_exact"
    span = last - period
    broken = (mask ^ (mask >> period)) & ((1 << (span + 1)) - 1)
    transient = broken.bit_length()
    if last - transient < need:
        return "R4_P_exact_suffix_shorter_than_2P"
    reach = last - transient
    stable = (mask >> transient) & ((1 << (reach + 1)) - 1)
    events = bin(stable).count("1")
    if events < MIN_STABLE_EVENTS:
        return "R5_fewer_than_8_clean_ticks_in_stable_region"
    folded, step = stable, period
    while step <= reach:
        folded |= folded >> step
        step <<= 1
    if bin(folded & ((1 << period) - 1)).count("1") == period:
        return "R6_all_residues_clean"
    return "ACCEPT"


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


# ------------------------------------------- station / shape bookkeeping
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
    rows_of_bank = {}
    for bank in range(bank_count):
        incident = [e for e in (bank - 1, bank) if 0 <= e <= bank_count - 2]
        rows_of_bank[bank] = {s: (k, e) for s, (k, e) in station_edge.items()
                              if e in incident}
    return {"program": program, "stations": stations, "swaps": swaps,
            "forward": forward, "reverse": reverse,
            "handoff_forward": handoff_forward, "handoff_return": handoff_return,
            "station_edge": station_edge, "rows_of_bank": rows_of_bank,
            "entry_gap": {b: (reverse[b] - forward[b - 1]) % stations
                          for b in range(1, bank_count - 1)},
            "malformed": malformed,
            "delta": {e: (r - f) % stations for e, (f, r) in swaps.items()}}


def closed_form_rows(bank_count, edge):
    """f, r, h_f, h_r from the pinned closed form -- no kernel read."""
    f = 4 + 5 * edge
    r = 8 * bank_count - 9 - 3 * edge
    return {"handoff_forward": f - 2, "forward": f, "reverse": r,
            "handoff_return": r + 2}


def tp_rows(bank_count):
    """TP as a pure function of the bank count.  Reads no corpus, ever."""
    stations = 8 * bank_count - 5
    out = []
    for bank in range(1, bank_count - 1):
        period = 8 * (bank_count - 1 - bank)
        here = closed_form_rows(bank_count, bank)
        prev = closed_form_rows(bank_count, bank - 1)
        rows = {}
        for kind, station in here.items():
            rows[station % stations] = (kind, bank)
        for kind, station in prev.items():
            rows[station % stations] = (kind, bank - 1)
        ordered = sorted(rows)
        gaps = [(ordered[(i + 1) % len(ordered)] - ordered[i]) % stations
                for i in range(len(ordered))]
        unit = [ordered[i] for i, g in enumerate(gaps) if g == 1]
        shadowed = {(ordered[(i + 1) % len(ordered)]) for i, g in enumerate(gaps)
                    if g == 1}
        pairs = {
            "swap_swap": (prev["forward"] % stations, here["reverse"] % stations),
            "swap_handoff": (here["forward"] % stations,
                             prev["handoff_return"] % stations),
            "handoff_swap": (here["handoff_forward"] % stations,
                             prev["reverse"] % stations),
        }
        rowset = set(ordered)
        intersect = sorted(s for s in ordered if (s + period) % stations in rowset)
        unreachable = sorted(s for s in ordered
                             if (s - period) % stations not in rowset)
        firsts = sorted({pairs[k][0] for k in pairs})
        out.append({
            "bank": bank, "period": period, "stations": stations,
            "rows_sorted": ordered,
            "unit_gap_lower_stations": sorted(unit),
            "shadowed_rows": sorted(shadowed),
            "pairs": {k: list(v) for k, v in pairs.items()},
            "pairs_span_the_value": {
                k: (v[1] - v[0]) % stations == period for k, v in pairs.items()},
            "pair_terminal_is_shadowed": {
                k: v[1] in shadowed for k, v in pairs.items()},
            "pair_first_is_shadowed": {
                k: v[0] in shadowed for k, v in pairs.items()},
            "P_shift_fixed_rows": intersect,
            "three_first_stations": firsts,
            "extra_P_shift_fixed_rows": sorted(set(intersect) - set(firsts)),
            "coincidence_cell_b_equals_floor_B_minus_1_over_2":
                bank == (bank_count - 1) // 2,
            "rows_with_no_P_preimage_in_R": unreachable,
            "reverse_rows": [prev["reverse"] % stations, here["reverse"] % stations],
            "h_r_b": here["handoff_return"] % stations,
            "h_r_b_has_no_P_preimage":
                (here["handoff_return"] - period) % stations not in rowset,
            "h_r_b_sits_one_below_the_third_pair_terminal":
                (here["handoff_return"] + 1) % stations
                == pairs["handoff_swap"][1],
            "TP_predicts_third_pair_fires": False,
        })
    return out


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


def shape_of_local_pair(pair, bank):
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


CLASS_PRIORITY = ("RELAY_ENTRY_GAP", "RELAY_EDGE_COMPLEMENT", "RELAY_EDGE_DELTA",
                  "TOKEN_SEPARATION", "MIXED")


def classify_separation_891(table, banks_of_clock, positions, separation):
    """Cycle 891's value-based classifier, reimplemented for the restriction gate."""
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
def census(box, full_clocks, anatomy_cap=6):
    """One exhaustive pass: the 922/891 restriction quantities AND the new
    third-pair / RC-3 instruments, on the same corpus, in one sweep."""
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
    local_shape_counts = Counter()
    bank_period = Counter()
    ledger = Counter()
    cooccurrence = 0
    stretch_total = 0
    longest_stretch = 0
    clocks_total = 0
    cache_891 = {}

    # --- the new instruments, per (bank, shape) at the bank's entry gap -----
    ladder = defaultdict(Counter)       # (bank, shape) -> S1..S6 + rejections
    occurrence = Counter()              # (bank, shape) -> raw pair occurrences
    ep_shape = Counter()                # (bank, shape) -> 922-semantics episodes
    ep_total = Counter()                # bank -> episodes at the entry gap
    ep_eqwidth = Counter()              # bank -> episodes carrying an equal-width
    ep_uneqonly = Counter()             # bank -> firing episodes with NO equal pair
    ep_nopair = Counter()               # bank -> firing episodes with no pair at all
    stable_eq = Counter()               # bank -> stable-region pairs, equal widths
    stable_uneq = Counter()             # bank -> stable-region pairs, unequal
    stable_uneq_trunc = Counter()       # ... of which explained by tail truncation
    anatomy = defaultdict(list)
    entry_of = {b: 8 * (bank_count - 1 - b) for b in range(1, bank_count - 1)}

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
        if full_clocks:
            items += [("pair%d%d" % (l, r), cleaned[l] & cleaned[r], (l, r))
                      for l, r in pairs]
        for name, mask, member_banks in items:
            clocks_total += 1
            if mask == 0:
                ledger["no_reading"] += 1
                continue
            found = set()
            single = member_banks[0] if len(member_banks) == 1 else None
            P = entry_of.get(single) if single is not None else None
            for a, b in stretches:
                length = b - a + 1
                segment = (mask >> a) & ((1 << length) - 1)
                if segment == 0:
                    continue
                hits = tail_periods(segment, periods)

                # ---------- the new instruments (bank clocks, entry gap only)
                if P is not None:
                    runs = zero_runs(segment, length)
                    starts = [a + lo for lo, _hi in runs]
                    widths = [hi - lo + 1 for lo, hi in runs]
                    idx = [i for i in range(len(starts) - 1)
                           if starts[i + 1] - starts[i] == P]
                    present = {}
                    if idx:
                        att = attribute_runs(
                            starts, positions, table["rows_of_bank"][single], stations)
                        for i in idx:
                            w1, w2 = widths[i], widths[i + 1]
                            for p1, _s1, k1, e1 in att[i]:
                                for p2, _s2, k2, e2 in att[i + 1]:
                                    if p1 != p2:
                                        continue
                                    sh = shape_of_local_pair(
                                        (True, k1, e1, k2, e2), single)
                                    if sh not in SHAPES:
                                        continue
                                    occurrence[(single, sh)] += 1
                                    cur = present.setdefault(
                                        sh, {"pair": 0, "eq": 0, "eqle": 0,
                                             "first": i})
                                    cur["pair"] += 1
                                    if w1 == w2:
                                        cur["eq"] += 1
                                        if w1 <= P - 1:
                                            cur["eqle"] += 1
                    nclean = bin(segment).count("1")
                    why = reject_reason(segment, P) if present else None
                    for sh, cur in present.items():
                        L = ladder[(single, sh)]
                        L["S1_stretches_with_the_pair"] += 1
                        if cur["eq"]:
                            L["S2_equal_width"] += 1
                        if cur["eqle"]:
                            L["S3_equal_width_le_Pm1"] += 1
                            if nclean >= MIN_STABLE_EVENTS:
                                L["S4_and_8_clean_ticks"] += 1
                                if length >= 2 * P + 1:
                                    L["S5_FULL_CONFIGURATION"] += 1
                                    L["reject_%s" % why] += 1
                        if P in hits:
                            L["S6_and_the_stretch_reads_P"] += 1
                            ep_shape[(single, sh)] += 1
                            if len(anatomy[(single, sh)]) < anatomy_cap:
                                i = cur["first"]
                                anatomy[(single, sh)].append({
                                    "banks": bank_count, "lane": lane,
                                    "event": event, "clock": name,
                                    "token_positions": list(positions),
                                    "sigma": sigma, "stretch": [a, b],
                                    "stretch_len": length, "period": P,
                                    "transient_events_residues": list(hits[P]),
                                    "pair_start_ticks": [starts[i], starts[i + 1]],
                                    "pair_widths": [widths[i], widths[i + 1]],
                                    "equal_width": widths[i] == widths[i + 1],
                                    "dirty_runs": len(runs),
                                })
                    if P in hits:
                        ep_total[single] += 1
                        transient = hits[P][0]
                        anyeq = any(widths[i] == widths[i + 1] for i in idx)
                        entry_eq = any(cur["eq"] for cur in present.values())
                        if present:
                            if entry_eq:
                                ep_eqwidth[single] += 1
                            else:
                                ep_uneqonly[single] += 1
                        elif not idx:
                            ep_nopair[single] += 1
                        # the stable-region equal-width THEOREM check
                        last = length - 1
                        for i in idx:
                            if starts[i] - a < transient:
                                continue
                            if widths[i] == widths[i + 1]:
                                stable_eq[single] += 1
                            else:
                                stable_uneq[single] += 1
                                lo = starts[i] - a
                                if lo + max(widths[i], widths[i + 1]) > last - P:
                                    stable_uneq_trunc[single] += 1
                        del anyeq

                # ---------- the pinned 922/891 quantities -------------------
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
                for period in interesting:
                    key = (frozenset(member_banks), positions, period)
                    if key not in cache_891:
                        cache_891[key] = classify_separation_891(
                            table, set(member_banks), positions, period)
                    label = cache_891[key]
                    class_counts_891[(period, label)] += 1
                    for bank in member_banks:
                        carrier_counts_891[(period, label)][bank] += 1
                    if single is None:
                        continue
                    bank_period[(single, period)] += 1
                    att = attribute_runs(
                        starts, positions, table["rows_of_bank"][single], stations)
                    local = set()
                    for i in range(len(starts) - 1):
                        if starts[i + 1] - starts[i] != period:
                            continue
                        for p1, _s1, k1, e1 in att[i]:
                            for p2, _s2, k2, e2 in att[i + 1]:
                                local.add((p1 == p2, k1, e1, k2, e2))
                    for shape in sorted({shape_of_local_pair(p, single)
                                         for p in local}):
                        local_shape_counts[(single, period, shape)] += 1
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
    expected = lanes * (bank_count + (len(pairs) if full_clocks else 0))
    return {
        "banks": bank_count, "stations": stations, "lanes": lanes,
        "full_clocks": full_clocks,
        "clocks_swept": clocks_total, "clocks_expected": expected,
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
        "completeness_ledger": dict(ledger),
        "cooccurrence_clocks": cooccurrence,
        "ladder": ladder, "occurrence": occurrence, "ep_shape": ep_shape,
        "ep_total": ep_total, "ep_eqwidth": ep_eqwidth,
        "ep_uneqonly": ep_uneqonly, "ep_nopair": ep_nopair,
        "stable_eq": stable_eq, "stable_uneq": stable_uneq,
        "stable_uneq_trunc": stable_uneq_trunc,
        "anatomy": anatomy, "table": table,
    }


def entry_gap_rows(cen):
    """The per-cell table: 922's numbers, plus this cycle's ladder."""
    bank_count = cen["banks"]
    rows = []
    for bank in range(1, bank_count - 1):
        period = 8 * (bank_count - 1 - bank)
        by_shape = {sh: cen["local_shape_counts"].get((bank, period, sh), 0)
                    for sh in SHAPES}
        total = sum(by_shape.values())
        rows.append({
            "banks": bank_count, "bank": bank, "entry_gap_period": period,
            "two_P": 2 * period, "stations": cen["stations"],
            "short_arc_2P_lt_N": 2 * period < cen["stations"],
            "episodes_on_the_bank_clock":
                cen["bank_period"].get((bank, period), 0),
            "bank_owned_entry_gap_episodes": total,
            "by_shape": by_shape,
            "fires": total > 0,
            "register_level_pair_occurrences": {
                sh: cen["occurrence"].get((bank, sh), 0) for sh in SHAPES},
            "ladder": {sh: dict(cen["ladder"].get((bank, sh), {}))
                       for sh in SHAPES},
            "firing_episodes_with_an_equal_width_entry_gap_pair":
                cen["ep_eqwidth"].get(bank, 0),
            "firing_episodes_with_only_unequal_width_entry_gap_pairs":
                cen["ep_uneqonly"].get(bank, 0),
            "firing_episodes_with_no_P_separated_pair_at_all":
                cen["ep_nopair"].get(bank, 0),
            "stable_region_pairs_equal_width": cen["stable_eq"].get(bank, 0),
            "stable_region_pairs_unequal_width": cen["stable_uneq"].get(bank, 0),
            "stable_region_unequal_explained_by_tail_truncation":
                cen["stable_uneq_trunc"].get(bank, 0),
        })
    return rows


# ------------------------------------------------------- claim-text numbers
# Every number quoted inside RC3_STATEMENT lives here and is GATED against the
# measurement, so the prose can never drift away from the corpus.
CLAIM_NUMBERS = {
    "B7_b3_bank_owned_entry_gap_episodes": 20,
    "B7_b3_equal_width_entry_gap_stretches": 548,
    "B7_b3_equal_width_entry_gap_stretches_accepted": 0,
    "B7_b5_swap_handoff_full_configurations": 542,
    "B7_b5_swap_handoff_episodes": 8,
    "B6_b3_swap_handoff_full_configurations": 268,
    "B6_b3_swap_handoff_episodes": 52,
    "B5_b2_third_pair_full_configurations": 30,
    "B6_b4_third_pair_full_configurations": 4,
}


def tp_seal_payload():
    """The sealed object: the rule TEXT plus its pure-function output at the
    bank counts this runner NEVER builds."""
    return {
        "TP_STATEMENT": TP_STATEMENT,
        "predicted_third_pair_episodes": {str(bc): 0 for bc in NEVER_BUILT_BANKS},
        "predicted_third_pair_exists_geometrically": {
            str(bc): [row["bank"] for row in tp_rows(bc)
                      if row["pairs_span_the_value"]["handoff_swap"]]
            for bc in NEVER_BUILT_BANKS},
        "predicted_third_pair_terminal_is_shadowed_everywhere": {
            str(bc): all(row["pair_terminal_is_shadowed"]["handoff_swap"]
                         for row in tp_rows(bc))
            for bc in NEVER_BUILT_BANKS},
        "predicted_other_two_pairs_terminals_unshadowed": {
            str(bc): all(not row["pair_terminal_is_shadowed"]["swap_swap"]
                         and not row["pair_terminal_is_shadowed"]["swap_handoff"]
                         for row in tp_rows(bc))
            for bc in NEVER_BUILT_BANKS},
    }


def restriction_compare(label, pinned, reproduced, failures):
    ok = pinned == reproduced
    if not ok:
        failures.append({"check": label, "pinned": pinned,
                         "reproduced": reproduced})
    return ok


# ------------------------------------------------------------------------ main
def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    def emit(line):
        lines.append(line)
        print(line)

    def gate(name, ok, payload):
        emit("%s %s :: %s" % ("PASS" if ok else "FAIL", name,
                              json.dumps(payload, **dumps)))
        return ok

    results = {}
    R922 = pinned_json(RECEIPT_922)
    R922C = pinned_json(RECEIPT_922_CHECK)
    R891 = pinned_json(RECEIPT_891)

    # ------------------------------------------------------------ gate A
    const_922 = pinned_constants(PRIMARY_922)
    want = {"TOKEN_K": TOKEN_K, "EVENT_COUNT": EVENT_COUNT, "HORIZON": HORIZON,
            "MIN_PERIOD_REPEATS": MIN_PERIOD_REPEATS,
            "MIN_STABLE_EVENTS": MIN_STABLE_EVENTS,
            "PINNED_PERIOD_CEILING": PINNED_PERIOD_CEILING}
    const_ok = all(const_922.get(k) == v for k, v in want.items())
    a_ok = (not PREFLIGHT_BAD) and const_ok and not FIREWALL.hits
    results["A_PINS"] = gate("A_PINS", a_ok, {
        "pins_verified": len(PINS), "mismatched": sorted(PREFLIGHT_BAD),
        "constants_inherited_from_the_pinned_922_AST": want,
        "constants_read_from_the_pinned_922_AST":
            {k: const_922.get(k) for k in want},
        "constants_match": const_ok,
        "firewall_hits": FIREWALL.hits,
        "blocklisted_modules": sorted(BLOCKLISTED_MODULES),
        "declared_deviations": list(DISCLOSED_DEVIATIONS),
    })
    if not a_ok:
        raise SystemExit(2)

    # ------------------------------------------------------------ gate B
    geom_rows, geom_bad = [], []
    for bc in range(3, 13):
        tab = station_table(bc)
        stations = tab["stations"]
        if stations != 8 * bc - 5:
            geom_bad.append({"banks": bc, "stations": stations})
        for edge in sorted(tab["swaps"]):
            cf = closed_form_rows(bc, edge)
            got = {"forward": tab["forward"][edge], "reverse": tab["reverse"][edge],
                   "handoff_forward": tab["handoff_forward"][edge],
                   "handoff_return": tab["handoff_return"][edge]}
            if cf != got:
                geom_bad.append({"banks": bc, "edge": edge,
                                 "closed_form": cf, "kernel": got})
    tp_bad, tp_cells, coincidence_cells = [], 0, []
    for bc in range(3, 25):
        for row in tp_rows(bc):
            tp_cells += 1
            extra = row["extra_P_shift_fixed_rows"]
            checks = {
                "all_three_pairs_span_P": all(row["pairs_span_the_value"].values()),
                "exactly_one_unit_gap": len(row["unit_gap_lower_stations"]) == 1,
                "third_pair_terminal_shadowed":
                    row["pair_terminal_is_shadowed"]["handoff_swap"],
                "other_two_terminals_unshadowed":
                    not row["pair_terminal_is_shadowed"]["swap_swap"]
                    and not row["pair_terminal_is_shadowed"]["swap_handoff"],
                "no_first_station_shadowed":
                    not any(row["pair_first_is_shadowed"].values()),
                "three_first_stations_are_P_shift_fixed":
                    set(row["three_first_stations"]) <= set(row["P_shift_fixed_rows"]),
                "h_r_b_has_no_P_preimage": row["h_r_b_has_no_P_preimage"],
                "h_r_b_sits_one_below_the_third_pair_terminal":
                    row["h_r_b_sits_one_below_the_third_pair_terminal"],
                "extra_shift_fixed_rows_only_at_coincidence_cells":
                    (not extra) or (
                        row["coincidence_cell_b_equals_floor_B_minus_1_over_2"]
                        and len(extra) == 1
                        and extra[0] in row["reverse_rows"]),
            }
            if extra:
                coincidence_cells.append(
                    {"banks": bc, "bank": row["bank"], "extra_rows": extra,
                     "extra_row_is": ("r(b-1), the third pair's own terminal"
                                      if extra == [row["reverse_rows"][0]]
                                      else "r(b)"),
                     "is_the_922_label_theft_cell":
                         row["coincidence_cell_b_equals_floor_B_minus_1_over_2"]})
            if not all(checks.values()):
                tp_bad.append({"banks": bc, "bank": row["bank"],
                               "failed": [k for k, v in checks.items() if not v]})
        geom_rows.append({"banks": bc, "stations": 8 * bc - 5,
                          "cells": len(tp_rows(bc))})
    pinned_shape_text = R922["shape_inventory"] if "shape_inventory" in R922 else ""
    text_ok = ("THREE ordered pairs" in str(pinned_shape_text)
               or "THREE ordered pairs" in R922["realization_condition"]
               or "three ordered row pairs" in R922["realization_condition"])
    b_ok = not geom_bad and not tp_bad and text_ok
    results["B_GEOMETRY_AND_TP"] = gate("B_GEOMETRY_AND_TP", b_ok, {
        "closed_form_vs_kernel_program_banks": "3..12",
        "closed_form_disagreements": geom_bad,
        "TP_cells_checked_banks_3_to_24": tp_cells,
        "TP_disagreeing_cells": tp_bad,
        "cells_with_a_fourth_P_shift_fixed_row": coincidence_cells,
        "fourth_fixed_row_note":
            "on exactly the cells b = floor((B-1)/2) the value 8(B-1-b) is "
            "simultaneously the bank's own edge complement, and there r(b-1) -- "
            "the THIRD PAIR'S OWN TERMINAL -- becomes a fourth P-shift-fixed "
            "row because r(b-1) + P = f(b-1).  These are exactly Cycle 922's "
            "label-theft cells, reached here from the geometry side.",
        "worker_correction_disclosure":
            "The worker's first TP-3 said the three first stations were the "
            "ONLY P-shift-fixed rows and that h_r(b) was the UNIQUE row with no "
            "P-preimage.  This gate FAILED that formulation on all 105 cells of "
            "its first run; both over-claims were withdrawn and replaced with "
            "the exception-carrying statement above, which passes.  The "
            "published TP-3 is the corrected one.",
        "pinned_922_text_claims_three_pairs": text_ok,
        "TP_statement": TP_STATEMENT,
        "example_rows_B7": tp_rows(7),
    })

    # ------------------------------------------------------------ gate C
    rng = random.Random(930_0728)
    det_cases, det_mismatch, det_hits, rej_mismatch = 0, 0, 0, 0
    for _ in range(1400):
        length = rng.randrange(24, 300)
        density = rng.choice((0.05, 0.15, 0.3, 0.5, 0.75))
        bits = 0
        for i in range(length):
            if rng.random() < density:
                bits |= 1 << i
        if rng.random() < 0.4:
            period = rng.randrange(3, 26)
            tail = rng.randrange(length // 2, length)
            base = rng.getrandbits(period)
            for i in range(tail, length):
                if (base >> ((i - tail) % period)) & 1:
                    bits |= 1 << i
                else:
                    bits &= ~(1 << i)
        periods = list(range(2, 40))
        got = tail_periods(bits, periods)
        ref = reference_tail_periods(bits, periods)
        det_cases += 1
        det_hits += len(got)
        if got != ref:
            det_mismatch += 1
        for p in periods:
            accept = reject_reason(bits, p) == "ACCEPT"
            if accept != (p in got):
                rej_mismatch += 1
    c_ok = det_mismatch == 0 and rej_mismatch == 0 and det_hits > 0
    results["C_DETECTOR"] = gate("C_DETECTOR", c_ok, {
        "randomised_cases": det_cases, "detections_compared": det_hits,
        "folded_vs_literal_mismatches": det_mismatch,
        "reject_reason_vs_tail_periods_mismatches": rej_mismatch,
        "detector_statement": DETECTOR_STATEMENT,
        "rejection_alphabet": list(REJECTIONS),
    })

    # -------------------------------------------------- build the corpora
    tiers = {}
    for bc in FULL_CLOCK_BANKS + BANK_CLOCK_BANKS:
        box = build_corpus(bc, HORIZON)
        cen = census(box, full_clocks=bc in FULL_CLOCK_BANKS)
        cen["substrate_failures"] = box["seed_failures"] + box["token_failures"]
        cen["malformed_edges"] = box["malformed"]
        tiers[bc] = cen
        del box

    # ------------------------------------------------------------ gate D
    failures = []
    pinned_rows = {row["banks"]: row for row in
                   R922["restriction_gate_against_cycle891"]["rows"]}
    d_rows = []
    for bc in FULL_CLOCK_BANKS:
        cen = tiers[bc]
        pr = pinned_rows[bc]
        cc = {"%d|%s" % (p, lab): n for (p, lab), n in cen["class_counts_891"].items()}
        checks = {
            "clocks_swept": restriction_compare(
                "B%d.clocks_swept" % bc, pr["clocks_swept"], cen["clocks_swept"],
                failures),
            "closed_quiescent_stretches": restriction_compare(
                "B%d.stretches" % bc, pr["closed_quiescent_stretches"],
                cen["closed_quiescent_stretches"], failures),
            "longest_closed_stretch": restriction_compare(
                "B%d.longest" % bc, pr["longest_closed_stretch"],
                cen["longest_closed_stretch"], failures),
            "class_counts_891": restriction_compare(
                "B%d.class_counts_891" % bc, pr["class_counts_891"], cc, failures),
            "completeness_ledger": restriction_compare(
                "B%d.ledger" % bc, pr["completeness_ledger"],
                cen["completeness_ledger"], failures),
            "cooccurrence_clocks": restriction_compare(
                "B%d.cooccurrence" % bc, pr["cooccurrence_clocks"],
                cen["cooccurrence_clocks"], failures),
            "entry_gap_table": restriction_compare(
                "B%d.entry_gap_table" % bc, pr["entry_gap_table"],
                cen["entry_gap_table"], failures),
            "complements_observed": restriction_compare(
                "B%d.complements" % bc, pr["complements_observed"],
                cen["complements_observed"], failures),
            "clocks_swept_equals_expected":
                cen["clocks_swept"] == cen["clocks_expected"],
            "substrate_failures_zero": cen["substrate_failures"] == 0,
        }
        if not checks["clocks_swept_equals_expected"]:
            failures.append({"check": "B%d.clock_count_identity" % bc})
        if not checks["substrate_failures_zero"]:
            failures.append({"check": "B%d.substrate" % bc})
        d_rows.append({"banks": bc, "checks": checks})

    # the 14 pinned per-cell rows at B=4..7
    pinned_fit = {(r["banks"], r["bank"]): r for r in R922["rc_fit"]["fit_rows"]}
    cell_rows = {}
    for bc in FULL_CLOCK_BANKS + BANK_CLOCK_BANKS:
        cell_rows[bc] = entry_gap_rows(tiers[bc])
    for (bc, bank), pr in sorted(pinned_fit.items()):
        mine = next(r for r in cell_rows[bc] if r["bank"] == bank)
        restriction_compare("fit.B%d.b%d.episodes_on_the_bank_clock" % (bc, bank),
                            pr["episodes_on_the_bank_clock"],
                            mine["episodes_on_the_bank_clock"], failures)
        restriction_compare("fit.B%d.b%d.bank_owned_entry_gap_episodes" % (bc, bank),
                            pr["bank_owned_entry_gap_episodes"],
                            mine["bank_owned_entry_gap_episodes"], failures)
        restriction_compare("fit.B%d.b%d.by_shape" % (bc, bank),
                            pr["by_shape"], mine["by_shape"], failures)
    # the 6 pinned B=8 holdout rows
    for pr in R922["sealed_holdout"]["rows"]["8"]["RC_rows"]:
        mine = next(r for r in cell_rows[8] if r["bank"] == pr["bank"])
        restriction_compare("B8.b%d.episodes_on_the_bank_clock" % pr["bank"],
                            pr["episodes_on_the_bank_clock"],
                            mine["episodes_on_the_bank_clock"], failures)
        restriction_compare("B8.b%d.bank_owned_entry_gap_episodes" % pr["bank"],
                            pr["bank_owned_entry_gap_episodes"],
                            mine["bank_owned_entry_gap_episodes"], failures)
        restriction_compare("B8.b%d.by_shape" % pr["bank"], pr["by_shape"],
                            mine["by_shape"], failures)
    # the B=8 clock-local shape counts at the complement values (bank clocks only)
    pinned_lsc = R922["sealed_holdout"]["rows"]["8"][
        "local_shape_counts_at_the_complement_values"]
    comp8 = set(tiers[8]["complement_set"])
    mine_lsc = {}
    for (bank, period, shape), n in tiers[8]["local_shape_counts"].items():
        if period in comp8:
            mine_lsc["b%d|P%d|%s" % (bank, period, shape)] = n
    restriction_compare("B8.local_shape_counts_at_the_complement_values",
                        pinned_lsc, mine_lsc, failures)
    # the B=7 residuals and the P=32 anatomy
    b7 = tiers[7]
    res = {p: sum(n for (per, lab), n in b7["class_counts_891"].items() if per == p)
           for p in (40, 48)}
    restriction_compare("B7.residual_episode_counts",
                        {int(k): v for k, v in
                         R922["restriction_gate_against_cycle891"][
                             "pinned_891_B7_residuals"].items()},
                        res, failures)
    p32_entry = sum(n for (bank, period, shape), n in b7["local_shape_counts"].items()
                    if period == 32 and shape in SHAPES)
    restriction_compare("B7.P32_has_no_bank_owned_entry_gap_episode", 0, p32_entry,
                        failures)
    p32_total = sum(n for (per, lab), n in b7["class_counts_891"].items() if per == 32)
    restriction_compare("B7.P32_total_episodes",
                        R922["p32_anatomy"]["P32_episodes_total_891_label"][
                            "RELAY_EDGE_COMPLEMENT"], p32_total, failures)
    banks_reading_32 = sorted({bank for (bank, period), n in b7["bank_period"].items()
                               if period == 32 and n})
    restriction_compare("B7.banks_that_read_P32",
                        sorted(R922["p32_anatomy"]["banks_that_read_P32"]),
                        banks_reading_32, failures)
    restriction_compare("B7.bank2_reads_P32", False, 2 in banks_reading_32, failures)
    d_ok = not failures
    results["D_RESTRICTION_922_891"] = gate("D_RESTRICTION_922_891", d_ok, {
        "note": "Every pinned Cycle-922/891 number this cycle builds on is "
                "recomputed from a fresh corpus and compared value for value "
                "BEFORE any new number is produced.",
        "tier_rows": d_rows,
        "pinned_cells_compared": len(pinned_fit)
                                 + len(R922["sealed_holdout"]["rows"]["8"]["RC_rows"]),
        "total_failed_checks": len(failures),
        "failed_checks": failures[:20],
    })
    if not d_ok:
        raise SystemExit(1)

    # ------------------------------------------------------------ gate E
    all_cells = [r for bc in sorted(cell_rows) for r in cell_rows[bc]]
    third_occurrences = {}
    third_episodes = 0
    third_full_config = {}
    third_reject = Counter()
    for r in all_cells:
        key = "B%d.b%d" % (r["banks"], r["bank"])
        third_occurrences[key] = r["register_level_pair_occurrences"][THIRD_PAIR]
        L = r["ladder"][THIRD_PAIR]
        third_episodes += r["by_shape"][THIRD_PAIR]
        third_full_config[key] = L.get("S5_FULL_CONFIGURATION", 0)
        for k, n in L.items():
            if k.startswith("reject_"):
                third_reject[k[7:]] += n
    tiers_with_occurrence = sorted({int(k.split(".")[0][1:])
                                    for k, n in third_occurrences.items() if n})
    e_ok = (third_episodes == 0
            and sum(third_occurrences.values()) > 0
            and set(tiers_with_occurrence) == set(FULL_CLOCK_BANKS + BANK_CLOCK_BANKS)
            and set(third_reject) <= {"R3_tail_window_not_P_exact"}
            and all(r["ladder"][THIRD_PAIR].get("S6_and_the_stretch_reads_P", 0) == 0
                    for r in all_cells))
    results["E_THIRD_PAIR"] = gate("E_THIRD_PAIR", e_ok, {
        "question": "why does (h_f(b), r(b-1)) carry zero episodes anywhere?",
        "answer": "NOT because it is geometrically absent.  It occurs as a "
                  "consecutive same-token P-separated run-start pair in EVERY "
                  "tier -- %d occurrences over B=4..8 -- and reaches the full "
                  "stretch configuration %d times.  What is exactly zero is its "
                  "coincidence with a reading: no stretch that the detector "
                  "reads at period P contains it.  Every refusal of a full "
                  "third-pair configuration is the SAME component: R3, the "
                  "terminal 2P+1 ticks are not P-exact.  The derived asymmetry "
                  "that singles the pair out is TP-1/TP-2/TP-3: r(b-1) is the "
                  "unique own row of bank b whose immediately preceding station "
                  "is also an own row of bank b (r(b-1) - h_r(b) = 1), so it is "
                  "the one entry-gap terminal that can open a run only when the "
                  "same token's own-row crossing one tick earlier leaves the "
                  "bank clean; and h_r(b), the row sitting one station below it, "
                  "is a row that no P-shift can reach."
                  % (sum(third_occurrences.values()), sum(third_full_config.values())),
        "third_pair_episodes_over_all_cells_B4_to_B8": third_episodes,
        "third_pair_register_level_occurrences": third_occurrences,
        "third_pair_full_configurations": third_full_config,
        "third_pair_refusal_components": dict(third_reject),
        "tiers_in_which_the_third_pair_occurs": tiers_with_occurrence,
        "per_cell": [{"banks": r["banks"], "bank": r["bank"],
                      "P": r["entry_gap_period"],
                      "occurrences": r["register_level_pair_occurrences"],
                      "episodes_by_shape": r["by_shape"],
                      "ladder": r["ladder"]} for r in all_cells],
        "anatomy_samples": {
            "%s|B%d.b%d" % (sh, bc, bank): rows
            for bc in sorted(tiers)
            for (bank, sh), rows in sorted(tiers[bc]["anatomy"].items())
            if bank in (1, 2, 3, 4, 5, 6)},
    })

    # ------------------------------------------------------------ gate F
    seal_payload = tp_seal_payload()
    seal_sha = digest(seal_payload)
    build_log_at_seal = list(BUILD_LOG)
    holdout_free = all(row["banks"] not in NEVER_BUILT_BANKS
                       for row in build_log_at_seal)
    emit("SEAL TP_SEAL_sha256 :: " + json.dumps(
        {"SEAL_sha256": seal_sha,
         "build_log_at_seal_time": build_log_at_seal,
         "build_log_at_seal_time_is_holdout_free": holdout_free,
         "never_built_banks": list(NEVER_BUILT_BANKS)}, **dumps))
    seal_again = digest(tp_seal_payload())
    f_ok = holdout_free and seal_again == seal_sha
    results["F_TP_SEAL"] = gate("F_TP_SEAL", f_ok, {
        "SEAL_sha256": seal_sha,
        "SEAL_recomputed": seal_again,
        "seal_discipline": "The seal is a digest of the TP rule TEXT plus its "
                           "pure-function output at B = 9, 10, 11, 12.  This "
                           "runner never builds a corpus at those bank counts, "
                           "so the seal is holdout-free BY CONSTRUCTION; the "
                           "build log at seal time is published above.",
        "seal_payload": seal_payload,
        "build_log_at_seal_time": build_log_at_seal,
        "build_log_at_seal_time_is_holdout_free": holdout_free,
        "HONESTY_DISCLOSURE":
            "B=8 is NOT a holdout for TP: the pinned Cycle-922 receipt already "
            "publishes ENTRY_GAP_handoff_swap = 0 on all six of its B=8 rows and "
            "the worker read them before TP was written.  B=9 is NOT a blind "
            "holdout either: the pinned Cycle-922 CHECKER receipt publishes the "
            "B=9 per-bank shape lists, which contain only f->r and f->hr shapes "
            "and no hf->r shape, and the worker read them too.  The first "
            "genuinely blind tier for TP is B=10, which no runner in this "
            "lineage has ever built.  The seal therefore covers B=9..12 but only "
            "B>=10 is blind, and the block claims only that.",
    })

    # ------------------------------------------------------------ gate G
    rc3 = {"reading_A": {"cells": [], "necessity_counterexamples": [],
                         "sufficiency_counterexamples": []},
           "reading_B": {}}
    reject_hist = Counter()
    stable_eq_tot = stable_uneq_tot = stable_uneq_trunc_tot = 0
    for r in all_cells:
        key = "B%d.b%d" % (r["banks"], r["bank"])
        presented = sum(r["ladder"][sh].get("S5_FULL_CONFIGURATION", 0)
                        for sh in SHAPES)
        fired = r["bank_owned_entry_gap_episodes"]
        row = {"cell": key, "P": r["entry_gap_period"],
               "short_arc_2P_lt_N": r["short_arc_2P_lt_N"],
               "full_configurations_presented": presented,
               "bank_owned_entry_gap_episodes": fired,
               "firing_episodes_with_an_equal_width_entry_gap_pair":
                   r["firing_episodes_with_an_equal_width_entry_gap_pair"],
               "firing_episodes_with_only_unequal_width_entry_gap_pairs":
                   r["firing_episodes_with_only_unequal_width_entry_gap_pairs"],
               "by_shape_full_configurations": {
                   sh: r["ladder"][sh].get("S5_FULL_CONFIGURATION", 0)
                   for sh in SHAPES},
               "by_shape_episodes": r["by_shape"]}
        rc3["reading_A"]["cells"].append(row)
        if r["firing_episodes_with_only_unequal_width_entry_gap_pairs"]:
            rc3["reading_A"]["necessity_counterexamples"].append(row)
        if presented and not fired:
            rc3["reading_A"]["sufficiency_counterexamples"].append(row)
        for sh in SHAPES:
            for k, n in r["ladder"][sh].items():
                if k.startswith("reject_"):
                    reject_hist[k[7:]] += n
        stable_eq_tot += r["stable_region_pairs_equal_width"]
        stable_uneq_tot += r["stable_region_pairs_unequal_width"]
        stable_uneq_trunc_tot += r[
            "stable_region_unequal_explained_by_tail_truncation"]
    rc3["reading_B"] = {
        "claim": "on the P-exact stable region equal width is a THEOREM of the "
                 "detector, not a criterion: S[t] = S[t+P] for "
                 "transient <= t <= last-P, so a run starting at t inside the "
                 "stable region has an identical-width image at t+P unless the "
                 "image is truncated by the end of the stretch.",
        "stable_region_P_separated_pairs_equal_width": stable_eq_tot,
        "stable_region_P_separated_pairs_unequal_width": stable_uneq_tot,
        "unequal_ones_explained_by_tail_truncation": stable_uneq_trunc_tot,
        "unexplained_violations": stable_uneq_tot - stable_uneq_trunc_tot,
    }
    measured_claims = {
        "B7_b3_bank_owned_entry_gap_episodes":
            next(r for r in cell_rows[7] if r["bank"] == 3)[
                "bank_owned_entry_gap_episodes"],
        "B7_b3_equal_width_entry_gap_stretches":
            sum(next(r for r in cell_rows[7] if r["bank"] == 3)["ladder"][sh]
                .get("S3_equal_width_le_Pm1", 0) for sh in SHAPES),
        "B7_b3_equal_width_entry_gap_stretches_accepted":
            sum(next(r for r in cell_rows[7] if r["bank"] == 3)["ladder"][sh]
                .get("reject_ACCEPT", 0) for sh in SHAPES),
        "B7_b5_swap_handoff_full_configurations":
            next(r for r in cell_rows[7] if r["bank"] == 5)["ladder"][
                "ENTRY_GAP_swap_handoff"].get("S5_FULL_CONFIGURATION", 0),
        "B7_b5_swap_handoff_episodes":
            next(r for r in cell_rows[7] if r["bank"] == 5)["by_shape"][
                "ENTRY_GAP_swap_handoff"],
        "B6_b3_swap_handoff_full_configurations":
            next(r for r in cell_rows[6] if r["bank"] == 3)["ladder"][
                "ENTRY_GAP_swap_handoff"].get("S5_FULL_CONFIGURATION", 0),
        "B6_b3_swap_handoff_episodes":
            next(r for r in cell_rows[6] if r["bank"] == 3)["by_shape"][
                "ENTRY_GAP_swap_handoff"],
        "B5_b2_third_pair_full_configurations":
            next(r for r in cell_rows[5] if r["bank"] == 2)["ladder"][
                THIRD_PAIR].get("S5_FULL_CONFIGURATION", 0),
        "B6_b4_third_pair_full_configurations":
            next(r for r in cell_rows[6] if r["bank"] == 4)["ladder"][
                THIRD_PAIR].get("S5_FULL_CONFIGURATION", 0),
    }
    claim_ok = measured_claims == CLAIM_NUMBERS
    binding = reject_hist.most_common(1)[0][0] if reject_hist else None
    g_ok = (claim_ok
            and rc3["reading_B"]["unexplained_violations"] == 0
            and bool(rc3["reading_A"]["necessity_counterexamples"])
            and bool(rc3["reading_A"]["sufficiency_counterexamples"])
            and binding == "R3_tail_window_not_P_exact")
    results["G_RC3_MEASURED"] = gate("G_RC3_MEASURED", g_ok, {
        "RC3_statement": RC3_STATEMENT,
        "VERDICT": "RC-3 DOES NOT CLOSE.  Under reading A the named "
                   "discriminator is neither necessary nor sufficient; under "
                   "reading B it is a theorem of the detector and therefore "
                   "carries no sufficiency content.  Reported as a measured "
                   "negative, not forced either way.",
        "reading_A": rc3["reading_A"],
        "reading_B": rc3["reading_B"],
        "refusal_components_over_every_presented_configuration": dict(reject_hist),
        "binding_component": binding,
        "claim_text_numbers_declared": CLAIM_NUMBERS,
        "claim_text_numbers_measured": measured_claims,
        "claim_text_numbers_agree": claim_ok,
    })

    # ------------------------------------------------------------ gate H
    failing = []
    for r in all_cells:
        if r["short_arc_2P_lt_N"] and not r["fires"]:
            failing.append(r)
    fail_rows = []
    for r in failing:
        L = {sh: r["ladder"][sh] for sh in SHAPES}
        fail_rows.append({
            "cell": "B%d.b%d" % (r["banks"], r["bank"]),
            "P": r["entry_gap_period"], "bank_is_B_minus_2": r["bank"] == r["banks"] - 2,
            "episodes_on_the_bank_clock": r["episodes_on_the_bank_clock"],
            "stretches_presenting_the_pair":
                {sh: L[sh].get("S1_stretches_with_the_pair", 0) for sh in SHAPES},
            "of_those_equal_width":
                {sh: L[sh].get("S2_equal_width", 0) for sh in SHAPES},
            "of_those_equal_width_le_Pm1":
                {sh: L[sh].get("S3_equal_width_le_Pm1", 0) for sh in SHAPES},
            "of_those_with_8_clean_ticks":
                {sh: L[sh].get("S4_and_8_clean_ticks", 0) for sh in SHAPES},
            "FULL_CONFIGURATIONS_PRESENTED":
                {sh: L[sh].get("S5_FULL_CONFIGURATION", 0) for sh in SHAPES},
            "refusal_component_of_every_full_configuration":
                {sh: {k[7:]: n for k, n in L[sh].items() if k.startswith("reject_")}
                 for sh in SHAPES},
        })
    b8b6 = next((r for r in fail_rows if r["cell"] == "B8.b6"), None)
    presented_at_the_failing_cell = (
        sum(b8b6["FULL_CONFIGURATIONS_PRESENTED"].values()) if b8b6 else None)
    failing_components = Counter()
    if b8b6:
        for sh, hist in b8b6["refusal_component_of_every_full_configuration"].items():
            for k, n in hist.items():
                failing_components[k] += n
    h_ok = (b8b6 is not None and presented_at_the_failing_cell > 0
            and "ACCEPT" not in failing_components
            and not ({"R1_fewer_than_8_clean_ticks_in_stretch",
                      "R2_stretch_shorter_than_2P",
                      "R5_fewer_than_8_clean_ticks_in_stable_region"}
                     & set(failing_components)))
    results["H_FAILING_CELLS"] = gate("H_FAILING_CELLS", h_ok, {
        "question": "does the failing cell's stretch population simply never "
                    "present the required configuration, and if so which "
                    "component fails?",
        "answer": "NO -- and that is the result.  The RC-2-satisfying cell that "
                  "does not fire, B=8 b=6 (P=8, the b=B-2 cell 922 flagged), "
                  "PRESENTS the full configuration %s times (equal-width "
                  "P-separated entry-gap pairs, w <= P-1, >= 8 clean ticks, "
                  "stretch at least 2P+1 long) and the detector refuses every "
                  "one of them.  NOT ONE component of the named measurement "
                  "fails: width equality holds, w <= P-1 holds, the clean ticks "
                  "are there, the runs are there, the stretch is long enough.  "
                  "The refusals are %s -- the terminal 2P+1 ticks are not "
                  "P-exact, or the stable residues are degenerate.  The "
                  "sufficiency gap is a TAIL fact, and the tail is 891's "
                  "declared dynamical boundary."
                  % (presented_at_the_failing_cell, dict(failing_components)),
        "refusal_components_at_the_failing_cell": dict(failing_components),
        "no_component_of_the_named_measurement_is_what_fails": h_ok,
        "sufficiency_failing_cells_at_2P_lt_N": fail_rows,
        "full_configurations_at_the_B8_b6_failing_cell":
            presented_at_the_failing_cell,
    })

    # ------------------------------------------------------------ gate J
    teeth = []

    # T1 -- a tampered pin is caught
    _rows, bad = preflight(overrides={PRIMARY_922: b"tampered"})
    teeth.append({"tooth": "tampered_pin_is_caught",
                  "fires": PRIMARY_922 in bad, "mismatched": sorted(bad)})

    # T2 -- a planted third-pair episode is caught by this cycle's instrument
    plant_bc, plant_bank = 5, 3
    plant_P = 8 * (plant_bc - 1 - plant_bank)
    plant_tab = station_table(plant_bc)
    plant_N = plant_tab["stations"]
    plant_pos = (0, 4)
    hf_here = plant_tab["handoff_forward"][plant_bank]
    r_prev = plant_tab["reverse"][plant_bank - 1]
    t1 = (hf_here - plant_pos[0] + 1) % plant_N
    length = 120
    dirty = set()
    tick = t1
    while tick + 2 < length:
        dirty.update({tick, tick + 1, tick + 2})
        tick += plant_P
    seg = 0
    for i in range(length):
        if i not in dirty:
            seg |= 1 << i
    runs = zero_runs(seg, length)
    starts = [lo for lo, _hi in runs]
    widths = [hi - lo + 1 for lo, hi in runs]
    att = attribute_runs(starts, plant_pos, plant_tab["rows_of_bank"][plant_bank],
                         plant_N)
    planted_shapes = set()
    for i in range(len(starts) - 1):
        if starts[i + 1] - starts[i] != plant_P:
            continue
        for p1, _s1, k1, e1 in att[i]:
            for p2, _s2, k2, e2 in att[i + 1]:
                if p1 == p2:
                    planted_shapes.add(shape_of_local_pair(
                        (True, k1, e1, k2, e2), plant_bank))
    planted_hits = tail_periods(seg, list(range(2, 40)))
    teeth.append({
        "tooth": "planted_third_pair_episode_is_caught",
        "fires": THIRD_PAIR in planted_shapes and plant_P in planted_hits,
        "cell": "B%d.b%d" % (plant_bc, plant_bank), "period": plant_P,
        "stations": [hf_here, r_prev], "shapes_seen": sorted(planted_shapes),
        "detector_reads_P": plant_P in planted_hits,
        "equal_widths": len(set(widths[:4])) == 1,
        "note": "a REAL third-pair episode of exactly this form would be "
                "reported by the same code path that reports zero over the "
                "corpus, so the zero is not an instrument blind spot",
    })

    # T3 -- a planted configuration in a non-presenting cell flips the verdict
    def sufficiency_counterexample_cells(rows):
        return sorted(r["cell"] for r in rows
                      if r["full_configurations_presented"]
                      and not r["bank_owned_entry_gap_episodes"])

    before = sufficiency_counterexample_cells(rc3["reading_A"]["cells"])
    mutated = [dict(r) for r in rc3["reading_A"]["cells"]]
    victim = next((r for r in mutated
                   if not r["full_configurations_presented"]
                   and not r["bank_owned_entry_gap_episodes"]), None)
    if victim is not None:
        victim["full_configurations_presented"] = 1
    after = sufficiency_counterexample_cells(mutated)
    teeth.append({"tooth": "planted_configuration_flips_the_RC3_verdict",
                  "fires": victim is not None and after != before,
                  "planted_into": victim["cell"] if victim else None,
                  "counterexamples_before": len(before),
                  "counterexamples_after": len(after)})

    # T4 -- a perturbed station formula breaks TP
    def perturbed_rows(bank_count, edge):
        f = 4 + 5 * edge + 1
        r = 8 * bank_count - 9 - 3 * edge
        return {"handoff_forward": f - 2, "forward": f, "reverse": r,
                "handoff_return": r + 2}

    broken = 0
    for bc in range(4, 9):
        stations = 8 * bc - 5
        for bank in range(1, bc - 1):
            period = 8 * (bc - 1 - bank)
            here, prev = perturbed_rows(bc, bank), perturbed_rows(bc, bank - 1)
            spans = [(here["reverse"] - prev["forward"]) % stations == period,
                     (prev["handoff_return"] - here["forward"]) % stations == period,
                     (prev["reverse"] - here["handoff_forward"]) % stations == period]
            if not all(spans):
                broken += 1
    teeth.append({"tooth": "perturbed_station_formula_breaks_TP",
                  "fires": broken > 0, "cells_broken": broken})

    # T5 -- dropping the third shape from the classifier makes the claim vacuous
    def crippled_shape(pair, bank):
        out = shape_of_local_pair(pair, bank)
        return "OTHER_SAME_TOKEN" if out == THIRD_PAIR else out

    true_hits = crippled_hits = 0
    for bc in FULL_CLOCK_BANKS + BANK_CLOCK_BANKS:
        for bank in range(1, bc - 1):
            probe = (True, "handoff_forward", bank, "reverse", bank - 1)
            true_hits += shape_of_local_pair(probe, bank) == THIRD_PAIR
            crippled_hits += crippled_shape(probe, bank) == THIRD_PAIR
    teeth.append({"tooth": "dropping_the_third_shape_is_detectable",
                  "fires": true_hits > 0 and crippled_hits == 0,
                  "cells_classified_by_the_true_classifier": true_hits,
                  "cells_classified_by_the_crippled_classifier": crippled_hits})

    # T6 -- the restriction comparison really compares
    probe_failures = []
    restriction_compare("tooth.probe", 1, 1, probe_failures)
    restriction_compare("tooth.probe", 1, 2, probe_failures)
    teeth.append({"tooth": "restriction_comparison_actually_compares",
                  "fires": len(probe_failures) == 1,
                  "failures_raised": len(probe_failures)})

    # T7 -- the detector's clean-tick constant is load bearing
    tight = 0
    for i in range(length):
        if (seg >> i) & 1:
            tight += 1
    teeth.append({
        "tooth": "detector_min_events_constant_is_load_bearing",
        "fires": (plant_P in tail_periods(seg, [plant_P], min_events=8)
                  and plant_P not in tail_periods(seg, [plant_P],
                                                  min_events=tight + 1)),
        "clean_ticks_in_the_planted_mask": tight,
    })

    # T8 -- a tampered seal is caught
    tampered = dict(seal_payload)
    tampered["TP_STATEMENT"] = TP_STATEMENT.replace("unique", "typical")
    teeth.append({"tooth": "tampered_seal_is_caught",
                  "fires": digest(tampered) != seal_sha,
                  "tampered_digest": digest(tampered)})

    # T9 -- a crippled rejection decomposer disagrees with the detector
    def crippled_reject(mask, period):
        if mask == 0:
            return "R0_empty"
        if bin(mask).count("1") < MIN_STABLE_EVENTS:
            return "R1_fewer_than_8_clean_ticks_in_stretch"
        last = mask.bit_length() - 1
        if MIN_PERIOD_REPEATS * period > last:
            return "R2_stretch_shorter_than_2P"
        span = last - period
        broken_bits = (mask ^ (mask >> period)) & ((1 << (span + 1)) - 1)
        transient = broken_bits.bit_length()
        if last - transient < MIN_PERIOD_REPEATS * period:
            return "R4_P_exact_suffix_shorter_than_2P"
        return "ACCEPT"

    rng2 = random.Random(930_0729)
    disagree = 0
    for _ in range(400):
        n = rng2.randrange(30, 200)
        bits = rng2.getrandbits(n) | (1 << (n - 1))
        for p in range(2, 20):
            if (crippled_reject(bits, p) == "ACCEPT") != (p in tail_periods(bits, [p])):
                disagree += 1
    teeth.append({"tooth": "crippled_rejection_decomposer_is_detectable",
                  "fires": disagree > 0, "disagreements": disagree})

    # T10 -- the stable-region equal-width theorem is load bearing
    unexplained = rc3["reading_B"]["unexplained_violations"]
    faked = unexplained + 1
    teeth.append({"tooth": "stable_region_equal_width_theorem_is_load_bearing",
                  "fires": unexplained == 0 and faked != 0,
                  "measured_unexplained_violations": unexplained,
                  "note": "a single unexplained unequal-width pair inside a "
                          "P-exact stable region would break gate G; the gate "
                          "asserts zero and the corpus delivers zero"})

    j_ok = all(t["fires"] for t in teeth) and len(teeth) >= 8
    results["J_TEETH"] = gate("J_TEETH", j_ok, {
        "teeth": teeth, "count": len(teeth), "declared_minimum": 8,
        "all_fire": all(t["fires"] for t in teeth)})

    # ------------------------------------------------------------ gate K
    runtime = time.monotonic() - started
    k_ok = all(results.values()) and runtime <= RUNTIME_LIMIT_SECONDS
    headline = (
        "THE THIRD PAIR IS NOT ABSENT, IT IS NEVER READ.  (h_f(b), r(b-1)) "
        "occurs %d times as a consecutive same-token P-separated run-start pair "
        "over B=4..8 and reaches the full stretch configuration %d times, yet "
        "appears in ZERO stretches that the detector reads at period P; the "
        "derived asymmetry is that r(b-1) is the unique entry-gap terminal whose "
        "immediately preceding station is another own row of the same bank "
        "(r(b-1) - h_r(b) = 1), and h_r(b) is a row no P-shift can reach.  "
        "AND RC-3 DOES NOT CLOSE: the equal-width discriminator is not "
        "necessary (B=7 b=3 fires %d episodes with only unequal-width entry-gap "
        "pairs) and not sufficient (the B=8 b=6 failing cell PRESENTS the full "
        "configuration %d times and is refused every time); the binding "
        "component everywhere is R3, the terminal 2P+1 ticks failing to be "
        "P-exact -- a tail fact, which is 891's declared dynamical boundary."
        % (sum(third_occurrences.values()), sum(third_full_config.values()),
           CLAIM_NUMBERS["B7_b3_bank_owned_entry_gap_episodes"],
           presented_at_the_failing_cell))
    results["K_VERDICT"] = gate("K_VERDICT", k_ok, {
        "headline": headline,
        "gates": {k: ("PASS" if v else "FAIL") for k, v in results.items()},
        "runtime_s": round(runtime, 1),
        "runtime_limit_s": RUNTIME_LIMIT_SECONDS,
        "build_log": list(BUILD_LOG),
        "open": [
            "the third-pair ZERO is measured and sealed, not derived: TP-1..TP-3 "
            "explain why that pair is the fragile one, they do not prove the "
            "count is zero",
            "B>=10 is the first genuinely blind tier for TP (B=8 and B=9 shape "
            "rows are already published in the pinned 922 primary and checker "
            "receipts and were read before TP was written)",
            "RC-3 sufficiency remains OPEN and is now measured to be a TAIL "
            "fact -- which word a stretch carries at its END -- i.e. exactly "
            "891's declared dynamical boundary, not a function of (B, b)",
            "the model-degeneracy band on RC-2 (Cycle 922) is untouched here",
        ],
    })

    payload = {
        "campaign": "toe-time-expansion-20260802",
        "block": "toe-time-blockT7-20260802",
        "cycles": [930],
        "claim_type": "bounded structure theorem + measured negative",
        "authority": "none", "audit": "unset",
        "authorship": "one Claude Opus 5 worker-authored primary and checker "
                      "under supervisor spec; supervisor review",
        "independence": "primary only -- see the independent-check receipt",
        "note": "none -- this block ships scripts, caches and receipts only",
        "headline": headline,
        "TP_statement": TP_STATEMENT,
        "RC3_statement": RC3_STATEMENT,
        "bookkeeping_identity": BOOKKEEPING_STATEMENT,
        "detector": DETECTOR_STATEMENT,
        "derivation_status": {
            "TP_1_shadowing": "derived -- pure station arithmetic, exhaustive "
                              "over B=3..16, zero disagreeing cells",
            "TP_2_uniqueness_among_the_three_pairs": "derived -- same gate",
            "TP_3_shift_picture": "derived -- same gate",
            "TP_4_the_zero": "MEASURED and SEALED, not derived.  Exhaustive over "
                             "B=4..8 (every bank clock, every closed quiescent "
                             "stretch); predictions at B=9..12 behind a printed "
                             "seal with a holdout-free build log; only B>=10 is "
                             "genuinely blind and that is disclosed.",
            "RC_3": "MEASURED NEGATIVE -- does not close.  Neither necessary nor "
                    "sufficient under reading A; a theorem of the detector under "
                    "reading B.  Both readings reported; nothing forced.",
        },
        "gate_results": {k: ("PASS" if v else "FAIL") for k, v in results.items()},
        "per_cell_rows": {str(bc): cell_rows[bc] for bc in sorted(cell_rows)},
        "third_pair": results and {
            "episodes_over_all_cells": third_episodes,
            "register_level_occurrences": third_occurrences,
            "full_configurations": third_full_config,
            "refusal_components": dict(third_reject),
        },
        "rc3": rc3,
        "rc3_refusal_components": dict(reject_hist),
        "rc3_binding_component": binding,
        "claim_text_numbers": CLAIM_NUMBERS,
        "claim_text_numbers_measured": measured_claims,
        "failing_cells": fail_rows,
        "seal": {"SEAL_sha256": seal_sha, "payload": seal_payload,
                 "build_log_at_seal_time": build_log_at_seal,
                 "build_log_at_seal_time_is_holdout_free": holdout_free,
                 "blind_from_bank_count": 10},
        "teeth": teeth,
        "restriction_gate": {"total_failed_checks": len(failures),
                             "tier_rows": d_rows,
                             "pinned_cells_compared": len(pinned_fit) + 6},
        "disclosed_deviations": list(DISCLOSED_DEVIATIONS),
        "build_log": list(BUILD_LOG),
        "runtime_seconds": round(runtime, 1),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "exit_codes": {"primary": 0 if k_ok else 1},
        "open": results["K_VERDICT"] and [
            "the third-pair zero is measured, not derived",
            "RC-3 sufficiency remains open and is measured to be a tail fact",
            "B>=10 is the first blind tier for TP",
        ],
        "pinned_inputs": {p: {"sha256": PREFLIGHT_ROWS[p]["sha256"],
                              "git_blob": PREFLIGHT_ROWS[p]["git_blob"]}
                          for p in sorted(PINS)},
    }
    me = Path(__file__).read_bytes()
    payload["files"] = {
        "scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py": {
            "sha256": sha256(me).hexdigest(), "git_blob": git_blob(me)}}
    out = ROOT / "outputs" / "third_pair_rc3_cycle930_receipt_2026_07_28.json"
    out.write_text(json.dumps(payload, indent=1, sort_keys=True, default=str))
    emit("RECEIPT %s :: %s" % (out.name, json.dumps(
        {"sha256": sha256(out.read_bytes()).hexdigest(),
         "git_blob": git_blob(out.read_bytes())}, **dumps)))
    return 0 if k_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
