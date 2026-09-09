#!/usr/bin/env python3
"""Cycle 879: the declared clock-relation family run at B=4.

Cycle 869 ran a DECLARED transformation family (constant time offset, alias
F1; windowed time offset, F1W; tick affine, F2A; index affine, F2B; index lag
plus offset, F3; partial lag overlap, F3P; periodic residue law, F4 -- with
declared caps, an evidence floor of 8, and an identity-like split) over the
B=3 substrate -- 19 stations, 304 census keys -- and reported three bounded
finite-corpus facts:

  * WITHIN A KEY the family is all but exhausted at its declared caps: 13 of
    480 substantive comparisons carry a whole-cadence dictionary, 12 of them
    identity-like, leaving exactly ONE substantive non-identity dictionary
    (index lag plus offset at L=0, d=-1121, which is 59 whole 19-station
    orbits).  This is a family-priced measured result, not a universal
    negative.
  * ACROSS KEYS at a fixed clock index, inside observed equal-gap-word
    classes, every constant-offset edge carries a NONZERO offset; keys
    outside any nontrivial class are counted, never suppressed.
  * Every DETECTOR-SELECTED nondegenerate period in that corpus is a whole
    number of 19-station orbits.  Per the landed Cycle-869 period contract
    these are the declared tail-ladder detector's selections, not least
    periods, and only the divisibility arithmetic is claimed.

The landed second-leg map of the evolution-axis premise (legacy alias:
B-AXIS; Cycle 875) left the ENTIRE B=4 run as its largest open row.  This
runner supplies that row with data by running the SAME family, the SAME caps,
the SAME evidence floor and the SAME identity-like split over a B=4 probe box
DECLARED HERE (27 stations, census 648, events {0,1}, k=2, horizon 8,192),
rebuilt from the tracked Cycle-719 controller core.  (Provenance context,
non-authoritative and non-load-bearing: the same box was named by an earlier
unlanded exploration referred to as Cycle 866; no landed Cycle-866 artifact
exists on the main line, and nothing here executes or inherits it.)

Nothing here tests for a preferred verdict.  Whether each B=3 finite-corpus
fact PERSISTS, STRENGTHENS or BREAKS at B=4 is computed from the measured
corpus and from the sha-pinned landed Cycle-869 cache, and is emitted as
data.  Every gate tests STRUCTURE: well-formedness, definitional identities,
re-verification of witnesses against each member's complete declared
contract, positive and negative controls on the tests themselves, and the
arithmetic consistency of the comparison table.  The terminal PASS marker
certifies measurement and gate integrity only, never a theorem outcome.

ACROSS-KEY SCOPE.  Cycle 875's A4 finding was that the 869 across-key
headline quoted a PAIR-CLOCK sub-corpus while reading as a corpus-wide
figure.  This runner reports the FULL corpus (all ten clock indices: six bank
pairs and four single banks) as its headline from the start, and emits the
pair-only and bank-only figures explicitly labelled as sub-corpora.
"""
from __future__ import annotations

from bisect import bisect_left
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
PRIMARY_869 = "scripts/frontier_cycle869_clock_relation_2026_07_28.py"
CACHE_869 = "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle869_clock_relation_2026_07_28.py",
    "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 1400

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as C719


A = C719.A
B = C719.B
M = C719.M
R3 = C719.R3

# ------------------------------------------------------------- the declared box
# The B=4 probe box DECLARED by this runner (provenance context only: the same
# box was named by the unlanded exploration referred to as Cycle 866, which
# carries no authority here).  Every number is re-derived from the Cycle-719
# geometry below and gated, not assumed.
FIXTURE_BANKS = 4
STATIONS = 27
HORIZON_CHUNKS = 8_192
TOKEN_K = 2
EVENT_COUNT = 2
EXPECTED_PLACEMENTS = 324
EXPECTED_KEYS = EXPECTED_PLACEMENTS * EVENT_COUNT          # 648
BANK_PAIRS = tuple(combinations(range(FIXTURE_BANKS), 2))  # six pairs

# The B=3 box the comparison table is priced against.
B3_FIXTURE_BANKS = 3
B3_STATIONS = 19
B3_KEYS = 304

RUNTIME_LIMIT_SECONDS = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

# ---- Declared storage / search caps.  Identical to Cycle 869 except where the
# ---- DISCLOSED_DEVIATIONS block says otherwise; every cap carries a saturation
# ---- counter so a cap that bites can never be mistaken for an absence of data.
CADENCE_STORE_CAP = HORIZON_CHUNKS + 1        # ticks 0..H inclusive
CYCLE866_DECLARED_STORE_CAP = 1_024           # the probe's nominal store cap
PERIOD_TAIL_WINDOW = 2_048
PERIOD_TAIL_FLOOR = 16
PERIOD_TAIL_RATIO = (3, 4)
PERIOD_MAX_BLOCK_GAPS = 512
MIN_SATURATION_RUN = 8
WINDOWED_OFFSET_ANCHORS = 8
MIN_LAG_OVERLAP = 8
PARTIAL_COVERAGE_FLOOR = Fraction(1, 2)
MIN_PERIOD_REPEATS = 2
ACROSS_KEY_REP_CAP = EXPECTED_KEYS            # 648; see DISCLOSED_DEVIATIONS
WITNESS_PRINT_CAP = 4
SAMPLE_PRINT_CAP = 4
EVIDENCE_FLOOR = 8

DISCLOSED_DEVIATIONS = (
    "STORE CAP.  The unlanded exploration that first named this probe box "
    "(referred to as Cycle 866; provenance only) names a cadence store cap of "
    f"{CYCLE866_DECLARED_STORE_CAP}.  At B=4 the clocks are far longer than at "
    f"B=3, so that cap would TRUNCATE cadences and silently corrupt every "
    f"relation verdict downstream.  This runner therefore stores at the "
    f"horizon ({CADENCE_STORE_CAP} ticks, truncation structurally impossible), "
    "reports the store-saturation counter, and reports exactly how many clocks "
    f"would have been truncated at {CYCLE866_DECLARED_STORE_CAP} so the size of "
    "the deviation is visible.  The deviation strictly ADDS data.",
    "ACROSS-KEY REPRESENTATIVE CAP.  Cycle 869 capped the distinct gap words "
    f"compared per clock index at 600 with {B3_KEYS} keys, so the cap could not "
    f"bite.  At B=4 there are {EXPECTED_KEYS} keys, so 600 could bite.  The cap "
    f"is raised to {ACROSS_KEY_REP_CAP} = the lane count, which is the "
    "structural maximum number of distinct words; the cap is therefore unable "
    "to bite at this census and its saturation counter is gated to zero.",
    "TICK-INDEX LOOKUP.  Cycle 869 carried a {tick: position} dict on every "
    "cadence profile.  At B=4 the corpus is ~4.8M clock events and those dicts "
    "would dominate memory.  The lookup is done by binary search on the "
    "strictly increasing tick tuple instead.  This is the SAME function; gate "
    "C carries a control that the binary-search lookup and the dict agree on "
    "every tick of sampled cadences.",
    "SCOPE.  Per Cycle 875's A4 finding, the across-key headline of this block "
    "is the FULL corpus (all ten clock indices).  Pair-only and bank-only "
    "figures are emitted, labelled as sub-corpora, and are not the headline.",
)

FAMILY = (
    "CONSTANT_TIME_OFFSET (alias F1)    Y = X + c exactly, as sets, over the "
    "whole horizon.  Witness c in [-H,H].",
    "WINDOWED_TIME_OFFSET (alias F1W)   the WHOLE of Y lies inside the window "
    "[max(0,c), min(H,H+c)] in which a shift by c is fully observed, and there "
    "Y = (X + c).  X may carry extra events that the shift pushes outside the "
    "horizon; Y may not.  Candidate c drawn from differences of the first/last "
    f"{WINDOWED_OFFSET_ANCHORS} events of each cadence, plus c=0.",
    "TICK_AFFINE (alias F2A)            |X| = |Y| >= 3 and y_n = a*x_n + b for "
    "all n with a a positive rational, b rational; a != 1 (a = 1 is the "
    "constant time offset, alias F1).  Witness (a,b) solved from the endpoints "
    "and re-verified exactly in Fraction arithmetic on every event.",
    "INDEX_AFFINE (alias F2B)           Y is the arithmetic-index subsequence "
    "y_n = x_{s*n + r} of X, s >= 1, r >= 0, run to exhaustion "
    "(r + s*|Y| >= |X|), so Y is exactly reconstructible from X and (s,r).",
    "INDEX_LAG_PLUS_OFFSET (alias F3)   y_n = x_{n+L} + d for every n in "
    f"[0,|Y|), with |Y| >= {MIN_LAG_OVERLAP}.  This is periodic interleaving "
    "with lag: Y's whole gap word is a contiguous factor of X's at lag L, "
    "replayed at time offset d.  Witness (L,d).",
    "PARTIAL_LAG_OVERLAP (alias F3P)    the same map as the index-lag member "
    "but on a PARTIAL overlap: y_n = x_{n+L} + d holds on a contiguous run of "
    f"at least {MIN_LAG_OVERLAP} events covering at least "
    f"{PARTIAL_COVERAGE_FLOOR.numerator}/{PARTIAL_COVERAGE_FLOOR.denominator} "
    "of the shorter clock, with the rest of BOTH clocks unexplained.  It is "
    "reported as a PARTIAL match, never as a dictionary: it does not carry one "
    "whole cadence onto another.  That clause is ENFORCED, not merely "
    "declared: a run that covers the whole of Y (start 0, overlap |Y|) or the "
    "whole of X (start + L = 0, overlap |X|) is a TOTAL map, is refused by "
    "this member in both the search and the verifier, and must be reported by "
    "the index-lag member (F3) instead.  Witness (L,d,overlap,coverage).",
    "PERIODIC_RESIDUE_LAW (alias F4)    Beyond their transients both cadences "
    "are unions of residue classes modulo one common period P, and the residue "
    "sets differ by a rotation: R_Y = R_X + c (mod P).  Neither clock may be "
    "SATURATED, and both residue sets must be PROPER subsets of Z_P.  The "
    "block is read off the tail window and the transient is then pushed back "
    "as far as the gap word allows, so the least transient is found exactly "
    "rather than picked off a ladder.  Witness (P,c,transients).",
)
SATURATION_NOTE = (
    "A clock is SATURATED when it is clean at every chunk boundary from some "
    "tick through the horizon.  The test is exact and cap-free -- the maximal "
    "run of consecutive ticks ending at the horizon, at least "
    f"{MIN_SATURATION_RUN} long -- so no declared cap can hide or invent one.  "
    "Two saturated clocks agree on their common tail by construction, so that "
    "agreement is classified TRIVIAL_SATURATION and never counted as a relation."
)
EVIDENCE_NOTE = (
    f"A relation is SUBSTANTIVE when the shorter of the two clocks carries at "
    f"least {EVIDENCE_FLOOR} events, and THIN otherwise.  Thin relations are "
    "reported but kept out of the headline coverage figure."
)
FAMILY_CLOSURE = (
    "F is searched in the order constant time offset (F1), windowed time "
    "offset (F1W), tick affine (F2A), index affine (F2B), index lag plus "
    "offset (F3), partial lag overlap (F3P), periodic residue law (F4) and "
    "the first member that holds is reported.  NO_RELATION_IN_F means every "
    "member was searched over its declared parameter range and refused a "
    "witness; it is a negative priced to F and its caps, not a claim about "
    "all conceivable transformations."
)
IDENTITY_NOTE = (
    "IDENTITY-LIKE means the map leaves the tick VALUES alone: one clock is "
    "literally a sub-run of the other at the same absolute times (c = 0, or "
    "d = 0 for the lag members, or s = 1 for the index member).  That is "
    "containment, not a transformation law, whichever member reports it."
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


# ------------------------------------------------------------------- substrate
def separated_placements(stations=STATIONS, size=TOKEN_K):
    """All size-``size`` station subsets with no cyclically adjacent pair."""
    rows = []
    for positions in combinations(range(stations), size):
        occupied = set(positions)
        if any((position + 1) % stations in occupied for position in positions):
            continue
        rows.append(positions)
    return tuple(rows)


def event_seeds(program):
    """Build the alternating-direction endpoint events; certify the allocator."""
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    state = M.pack_state(banks, links)
    seeds = []
    failures = 0
    for event in range(EVENT_COUNT):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        after, a_tokens, b_tokens, _trace = C719.run_orbit(before, program)
        expected = A.apply_semantic(before, M.global_allocator_word(FIXTURE_BANKS))
        failures += after != expected
        failures += a_tokens != (1,) + (0,) * (len(program) - 1)
        failures += any(b_tokens)
        seeds.append(before)
        state = after
    return tuple(seeds), failures


def census_initial_states(program, seeds, placements):
    """Literal (event, positions) census produced by ``run_orbit``."""
    keys = []
    states = []
    token_failures = 0
    for event, seed in enumerate(seeds):
        for positions in placements:
            state, a_tokens, b_tokens, _trace = C719.run_orbit(
                seed, program, token_positions=positions
            )
            keys.append((event, positions))
            states.append(state)
            token_failures += (
                tuple(index for index, bit in enumerate(a_tokens) if bit) != positions
            )
            token_failures += any(b_tokens)
    return tuple(keys), tuple(states), token_failures


def single_bit_location(zero_banks, zero_links, *, bank=None, link=None, wire):
    """Locate one logical coordinate by the required ``pack_state`` probe."""
    banks = [list(row) for row in zero_banks]
    links = [list(row) for row in zero_links]
    if bank is not None:
        banks[bank][wire] = 1
    else:
        links[link][wire] = 1
    packed = M.pack_state(
        tuple(tuple(row) for row in banks), tuple(tuple(row) for row in links)
    )
    locations = tuple(index for index, bit in enumerate(packed) if bit)
    if len(locations) != 1:
        raise AssertionError((bank, link, wire, locations))
    return locations[0]


def watched_layout():
    """Per-bank watched coordinate sets plus the shared SOURCE_POINTER."""
    banks, links = B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in row) for row in banks)
    zero_links = tuple(tuple(0 for _ in row) for row in links)
    local = (
        A.POINTER,
        A.U_TO_V,
        A.V_TO_U,
        A.DIRECTION_OK,
        *A.FRESH,
        *A.ZERO_WORK,
        A.TOKEN_OK,
    )
    per_bank = {}
    for bank in range(FIXTURE_BANKS):
        per_bank[bank] = tuple(sorted(
            single_bit_location(zero_banks, zero_links, bank=bank, wire=wire)
            for wire in local
        ))
    return per_bank, R3.X.SOURCE_POINTER, len(local)


def transpose_states(states, duplicate_source=0):
    """Bit-slice the census into per-coordinate lane planes; add a replay lane."""
    width = len(states[0])
    planes = [0] * width
    for lane, state in enumerate(states):
        lane_bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= lane_bit
    duplicate_bit = 1 << len(states)
    for wire, value in enumerate(states[duplicate_source]):
        if value:
            planes[wire] |= duplicate_bit
    return planes


def station_masks(keys, duplicate_source=0):
    """Per-phase, per-station lane masks for the circulating token sets."""
    masks = [[0] * STATIONS for _ in range(STATIONS)]
    for lane, (_event, positions) in enumerate(keys):
        bit = 1 << lane
        for phase in range(STATIONS):
            for start in positions:
                masks[phase][(start + phase) % STATIONS] |= bit
    duplicate_bit = 1 << len(keys)
    for phase in range(STATIONS):
        for start in keys[duplicate_source][1]:
            masks[phase][(start + phase) % STATIONS] |= duplicate_bit
    return tuple(tuple(row) for row in masks)


def iter_mask(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def short_key(key):
    event, positions = key
    return f"e{event}p{'.'.join(str(position) for position in positions)}"


# --------------------------------------------------------- transformation family
def gaps_of(cadence):
    return tuple(
        cadence[index + 1] - cadence[index] for index in range(len(cadence) - 1)
    )


def gap_word(gaps):
    """Delimiter-bounded encoding so ``str.find`` only matches on gap borders."""
    return "|" + "|".join(str(gap) for gap in gaps) + "|"


def tick_position(ticks, tick):
    """Index of ``tick`` in the strictly increasing ``ticks``, or None.

    Binary search stands in for Cycle 869's {tick: position} dict; at B=4 that
    dict would be ~4.8M entries.  Gate C carries a control that the two agree.
    """
    position = bisect_left(ticks, tick)
    if position < len(ticks) and ticks[position] == tick:
        return position
    return None


def kmp_border(sequence):
    """Longest proper border length of ``sequence`` (KMP failure value)."""
    length = len(sequence)
    if length == 0:
        return 0
    failure = [0] * length
    border = 0
    for index in range(1, length):
        while border and sequence[index] != sequence[border]:
            border = failure[border - 1]
        if sequence[index] == sequence[border]:
            border += 1
        failure[index] = border
    return failure[-1]


def saturation_profile(cadence, horizon=HORIZON_CHUNKS):
    """Exact, cap-free saturation test.

    Decided by the maximal run of consecutive ticks ending at the horizon --
    no period search, no transient cap -- so no declared cap can hide or invent
    a saturated clock.
    """
    if not cadence or cadence[-1] != horizon:
        return None
    start = len(cadence) - 1
    while start and cadence[start - 1] == cadence[start] - 1:
        start -= 1
    run = len(cadence) - start
    if run < MIN_SATURATION_RUN:
        return None
    return {
        "saturated_from_tick": cadence[start],
        "consecutive_run": run,
        "runs_to_horizon": True,
    }


def period_profile(cadence):
    """DETECTOR-SELECTED eventual time period of a cadence, or ``None``.

    The block is read off the TAIL window -- the eventual behaviour is what a
    period claims -- and the transient is then pushed back as far as the gap
    word allows, so the least transient FOR THE SELECTED PERIOD is found
    exactly.  The selected period is the least among the candidates this
    declared tail-ladder detector nominates (one minimal border per rung,
    block cap, repeat floor); it is NOT proven to be the globally least
    period of the cadence, and no complete period census is claimed.
    """
    gaps = gaps_of(cadence)
    if len(gaps) < MIN_PERIOD_REPEATS:
        return None
    best = None
    length = min(len(gaps), PERIOD_TAIL_WINDOW)
    while length >= min(PERIOD_TAIL_FLOOR, len(gaps)):
        tail = gaps[-length:]
        block = len(tail) - kmp_border(tail)
        if block and block <= PERIOD_MAX_BLOCK_GAPS \
                and len(tail) >= MIN_PERIOD_REPEATS * block:
            period = sum(tail[:block])
            if period > 0 and (best is None or period < best[0]):
                best = (period, block)
        if length <= PERIOD_TAIL_FLOOR:
            break
        length = max(
            PERIOD_TAIL_FLOOR,
            length * PERIOD_TAIL_RATIO[0] // PERIOD_TAIL_RATIO[1],
        )
    if best is None:
        return None
    period, block = best
    transient = len(gaps) - block
    while transient and gaps[transient - 1] == gaps[transient - 1 + block]:
        transient -= 1
    if len(gaps) - transient < MIN_PERIOD_REPEATS * block:
        return None
    best = {
        "period_ticks": period,
        "block_gaps": block,
        "transient_events": transient,
        "transient_tick": cadence[transient],
        "repeats": (len(gaps) - transient) // block,
        "tail_window": min(len(gaps), PERIOD_TAIL_WINDOW),
    }
    stable = tuple(tick for tick in cadence if tick >= best["transient_tick"])
    best["residues"] = tuple(sorted({tick % period for tick in stable}))
    best["residue_count"] = len(best["residues"])
    best["saturated"] = len(best["residues"]) == period
    window_hi = max(stable) - period
    lower = {tick for tick in stable if tick <= window_hi}
    upper = {tick for tick in stable if tick >= best["transient_tick"] + period}
    best["shift_exact_on_window"] = {tick + period for tick in lower} == upper
    return best


def cadence_profile(cadence):
    gaps = gaps_of(cadence)
    return {
        "length": len(cadence),
        "gaps": gaps,
        "word": gap_word(gaps),
        "period": period_profile(cadence) if len(cadence) >= MIN_LAG_OVERLAP else None,
        "saturation": saturation_profile(cadence),
        "ticks": cadence,
    }


def f1_constant_offset(x_profile, y_profile):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if not x or len(x) != len(y):
        return None
    offset = y[0] - x[0]
    if any(right - left != offset for left, right in zip(x, y)):
        return None
    return {"member": "F1", "c": offset}


def f1w_windowed_offset(x_profile, y_profile, horizon):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if not x or not y:
        return None
    anchors = WINDOWED_OFFSET_ANCHORS
    candidates = {0}
    for left in x[:anchors] + x[-anchors:]:
        for right in y[:anchors] + y[-anchors:]:
            candidates.add(right - left)
    x_set, y_set = set(x), set(y)
    for offset in sorted(candidates, key=lambda value: (abs(value), value)):
        if abs(offset) > horizon:
            continue
        low = max(0, offset)
        high = min(horizon, horizon + offset)
        if high <= low:
            continue
        if y[0] < low or y[-1] > high:
            continue
        shifted = {tick + offset for tick in x_set if low <= tick + offset <= high}
        if shifted != y_set:
            continue
        return {
            "member": "F1W",
            "c": offset,
            "window": [low, high],
            "events_in_window": len(y_set),
        }
    return None


def f2a_tick_affine(x_profile, y_profile):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if len(x) != len(y) or len(x) < 3 or x[-1] == x[0]:
        return None
    slope = Fraction(y[-1] - y[0], x[-1] - x[0])
    if slope <= 0 or slope == 1:
        return None
    intercept = Fraction(y[0]) - slope * x[0]
    for left, right in zip(x, y):
        if slope * left + intercept != right:
            return None
    return {
        "member": "F2A",
        "a_num": slope.numerator,
        "a_den": slope.denominator,
        "b_num": intercept.numerator,
        "b_den": intercept.denominator,
    }


def f2b_index_affine(x_profile, y_profile):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if len(y) < 2 or len(x) < 2:
        return None
    start = tick_position(x, y[0])
    second = tick_position(x, y[1])
    if start is None or second is None:
        return None
    step = second - start
    if step < 1:
        return None
    if step == 1 and start == 0 and len(x) == len(y):
        return None  # identity re-indexing; F1 already owns this shape
    if start + step * len(y) < len(x):
        return None  # not run to exhaustion: Y would not be reconstructible
    for ordinal, tick in enumerate(y):
        position = start + step * ordinal
        if position >= len(x) or x[position] != tick:
            return None
    return {"member": "F2B", "s": step, "r": start}


def f3_lag_offset(x_profile, y_profile):
    x, y = x_profile["ticks"], y_profile["ticks"]
    if len(y) < MIN_LAG_OVERLAP or len(x) < len(y):
        return None
    position = x_profile["word"].find(y_profile["word"])
    if position < 0:
        return None
    lag = x_profile["word"].count("|", 0, position + 1) - 1
    if lag < 0 or lag + len(y) > len(x):
        return None
    shift = y[0] - x[lag]
    for ordinal, tick in enumerate(y):
        if x[lag + ordinal] + shift != tick:
            return None
    return {"member": "F3", "L": lag, "d": shift, "overlap": len(y)}


def covers_whole_cadence(x_events, y_events, lag, start, overlap):
    """Does the lag run at (lag, start, overlap) carry a WHOLE cadence?

    The run explains y[start : start+overlap] and x[start+lag : start+lag+
    overlap].  It carries a whole cadence when it covers all of Y or all of X;
    either way the map is TOTAL on one clock, which the partial member's
    declared contract excludes.
    """
    whole_target = start == 0 and overlap == y_events
    whole_source = start + lag == 0 and overlap == x_events
    return bool(whole_target or whole_source)


def f3p_partial_lag(x_profile, y_profile):
    """Lag map on a partial overlap, in either index direction.

    Deliberately the most permissive member of F, but a PARTIAL one: the run
    must leave the rest of BOTH clocks unexplained.  A run that covers the
    whole of X, or the whole of Y, carries one whole cadence onto another and
    is therefore a TOTAL map; the declared contract reserves those for the
    index-lag member (F3), so such lags are SKIPPED here and the search
    continues over the rest of the declared lag range.
    """
    x, y = x_profile["ticks"], y_profile["ticks"]
    shorter = min(len(x), len(y))
    if shorter < MIN_LAG_OVERLAP:
        return None
    floor = max(
        MIN_LAG_OVERLAP,
        -(-shorter * PARTIAL_COVERAGE_FLOOR.numerator
          // PARTIAL_COVERAGE_FLOOR.denominator),
    )
    # Only lags whose overlap can reach the coverage floor are worth testing.
    lo = max(-(len(y) - 1), floor - len(y))
    hi = min(len(x) - 1, len(x) - floor)
    for lag in range(lo, hi + 1):
        start = max(0, -lag)
        stop = min(len(y), len(x) - lag)
        if stop - start < floor:
            continue
        # DECLARED PARTIAL CLAUSE.  The run must leave part of BOTH clocks
        # unexplained.  A run covering the whole of Y, or the whole of X, is a
        # total map that the index-lag member (F3) owns; it is never an F3P
        # witness, so skip this lag rather than report a whole cadence here.
        if covers_whole_cadence(len(x), len(y), lag, start, stop - start):
            continue
        shift = y[start] - x[start + lag]
        if x[start + 1 + lag] + shift != y[start + 1]:
            continue
        if all(x[index + lag] + shift == y[index]
               for index in range(start, stop)):
            coverage = Fraction(stop - start, shorter)
            return {
                "member": "F3P",
                "L": lag,
                "d": shift,
                "overlap": stop - start,
                "coverage": f"{coverage.numerator}/{coverage.denominator}",
                "partial": True,
            }
    return None


def f4_periodic_residue(x_profile, y_profile):
    left, right = x_profile["period"], y_profile["period"]
    if left is None or right is None:
        return None
    if not (left["shift_exact_on_window"] and right["shift_exact_on_window"]):
        return None
    if x_profile["saturation"] or y_profile["saturation"]:
        return None  # no cadence to relate; reported as TRIVIAL_SATURATION
    if left["saturated"] or right["saturated"]:
        return None
    period = left["period_ticks"]
    if period != right["period_ticks"]:
        return None
    source, target = set(left["residues"]), set(right["residues"])
    if len(source) != len(target) or not source:
        return None
    for anchor in sorted(source):
        offset = (min(target) - anchor) % period
        if {(value + offset) % period for value in source} == target:
            return {
                "member": "F4",
                "P": period,
                "c": offset,
                "transient_X": left["transient_tick"],
                "transient_Y": right["transient_tick"],
                "residue_count": len(source),
            }
    return None


FULL_MEMBERS = ("F1", "F1W", "F2A", "F2B", "F3", "F4")
PARTIAL_MEMBERS = ("F3P",)


def relate(x_profile, y_profile, horizon=HORIZON_CHUNKS, allow_partial=True):
    """First member of the declared family F carrying X onto Y, else None."""
    if not x_profile["ticks"] or not y_profile["ticks"]:
        return None
    tests = [
        lambda: f1_constant_offset(x_profile, y_profile),
        lambda: f1w_windowed_offset(x_profile, y_profile, horizon),
        lambda: f2a_tick_affine(x_profile, y_profile),
        lambda: f2b_index_affine(x_profile, y_profile),
        lambda: f3_lag_offset(x_profile, y_profile),
    ]
    if allow_partial:
        tests.append(lambda: f3p_partial_lag(x_profile, y_profile))
    tests.append(lambda: f4_periodic_residue(x_profile, y_profile))
    for test in tests:
        found = test()
        if found is not None:
            return found
    return None


def apply_witness(x_profile, witness):
    """Re-derive Y from X and the witness alone; None when not reconstructible."""
    x = x_profile["ticks"]
    member = witness["member"]
    if member == "F1":
        return tuple(tick + witness["c"] for tick in x)
    if member == "F2A":
        slope = Fraction(witness["a_num"], witness["a_den"])
        intercept = Fraction(witness["b_num"], witness["b_den"])
        rebuilt = []
        for tick in x:
            value = slope * tick + intercept
            if value.denominator != 1:
                return None
            rebuilt.append(int(value))
        return tuple(rebuilt)
    if member == "F2B":
        step, start = witness["s"], witness["r"]
        rebuilt = []
        position = start
        while position < len(x):
            rebuilt.append(x[position])
            position += step
        return tuple(rebuilt)
    if member == "F3":
        lag, shift, overlap = witness["L"], witness["d"], witness["overlap"]
        return tuple(x[lag + ordinal] + shift for ordinal in range(overlap))
    return None


def verify_witness(x_profile, y_profile, witness, horizon=HORIZON_CHUNKS):
    """Exact re-verification of a reported witness against the member's
    COMPLETE declared contract, independent of the search.

    Every clause of the member's declaration is re-checked from the immutable
    cadences and the serialized witness alone: bounds, floors, canonical
    windows, whole-clock clauses, slope validity, exhaustion, period equality
    on BOTH sides, direct shift membership, and non-saturation/proper-subset
    conditions.  A witness that reproduces the target but violates any
    declared clause is REFUSED.
    """
    member = witness["member"]
    x, y = x_profile["ticks"], y_profile["ticks"]
    if member == "F1":
        # Y = X + c exactly, as sets, over the whole horizon; |c| <= horizon.
        if abs(witness["c"]) > horizon or len(x) != len(y) or not x:
            return False
        return tuple(tick + witness["c"] for tick in x) == y
    if member == "F1W":
        # Whole-of-Y inside the CANONICAL window for c, and there Y = X + c.
        offset = witness["c"]
        if abs(offset) > horizon:
            return False
        low, high = max(0, offset), min(horizon, horizon + offset)
        if list(witness["window"]) != [low, high] or high <= low:
            return False
        if not y or y[0] < low or y[-1] > high:
            return False  # the WHOLE of Y must lie inside the window
        left = {tick + offset for tick in x if low <= tick + offset <= high}
        right = set(y)
        if witness.get("events_in_window") != len(right):
            return False
        return left == right and bool(right)
    if member == "F2A":
        # Positive rational slope, a != 1, |X| = |Y| >= 3, exact on every event.
        slope = Fraction(witness["a_num"], witness["a_den"])
        intercept = Fraction(witness["b_num"], witness["b_den"])
        if slope <= 0 or slope == 1 or len(x) != len(y) or len(x) < 3:
            return False
        return all(slope * left + intercept == right
                   for left, right in zip(x, y))
    if member == "F2B":
        # s >= 1, r >= 0, run to exhaustion, Y exactly reconstructible.
        step, start = witness["s"], witness["r"]
        if step < 1 or start < 0 or len(y) < 2 or start >= len(x):
            return False
        if start + step * len(y) < len(x):
            return False  # not exhausted: Y would not be reconstructible
        rebuilt = tuple(x[start::step])
        return rebuilt == y
    if member == "F3":
        # Whole-of-Y lag map: y_n = x_{n+L} + d for EVERY n, L >= 0, |Y| >= 8.
        lag, shift, overlap = witness["L"], witness["d"], witness["overlap"]
        if lag < 0 or overlap != len(y) or len(y) < MIN_LAG_OVERLAP:
            return False
        if lag + len(y) > len(x):
            return False
        return all(x[lag + ordinal] + shift == tick
                   for ordinal, tick in enumerate(y))
    if member == "F3P":
        # Partial lag map: contiguous run of >= MIN_LAG_OVERLAP events
        # covering >= the declared floor of the shorter clock, in bounds, and
        # PARTIAL -- it must leave the rest of BOTH clocks unexplained.  A
        # witness that carries a whole cadence onto another is a TOTAL map and
        # is REFUSED here; it must be re-expressed as the index-lag member.
        lag, shift, overlap = witness["L"], witness["d"], witness["overlap"]
        shorter = min(len(x), len(y))
        if overlap < MIN_LAG_OVERLAP or shorter < MIN_LAG_OVERLAP:
            return False
        if Fraction(overlap, shorter) < PARTIAL_COVERAGE_FLOOR:
            return False
        start = max(0, -lag)
        stop = start + overlap
        if start + lag < 0 or stop > len(y) or stop + lag > len(x):
            return False
        if covers_whole_cadence(len(x), len(y), lag, start, overlap):
            return False
        return all(
            x[start + lag + ordinal] + shift == y[start + ordinal]
            for ordinal in range(overlap)
        )
    if member == "F4":
        # Common period on BOTH sides, both windows shift-exact, neither clock
        # saturated, both residue sets PROPER nonempty subsets of Z_P of equal
        # size, rotation exact, transients as witnessed.
        period, offset = witness["P"], witness["c"]
        left = x_profile["period"]
        right = y_profile["period"]
        if left is None or right is None or period <= 0:
            return False
        if left["period_ticks"] != period or right["period_ticks"] != period:
            return False
        if not (left["shift_exact_on_window"] and right["shift_exact_on_window"]):
            return False
        if x_profile["saturation"] or y_profile["saturation"]:
            return False
        if left["saturated"] or right["saturated"]:
            return False
        source, target = set(left["residues"]), set(right["residues"])
        if not source or len(source) != len(target) or len(source) >= period:
            return False
        if witness.get("transient_X") != left["transient_tick"] \
                or witness.get("transient_Y") != right["transient_tick"]:
            return False
        mapped = {(value + offset) % period for value in source}
        return mapped == target
    return False


def identity_like(found):
    """The map leaves the tick VALUES alone -- containment, not a law."""
    return bool(
        found.get("c") == 0
        or (found["member"] in ("F3", "F3P") and found["d"] == 0)
        or (found["member"] == "F2B" and found["s"] == 1)
    )


# --------------------------------------------------------------------- controls
def family_controls(sample_profiles):
    """Positive and negative controls on the tests themselves.

    Positive: synthetic images built by each family member must be accepted
    with the constructed witness.  Negative: a one-tick perturbation of a real
    cadence must be refused by every member.  These gates prove the family can
    say YES when a relation exists and NO when it does not; they say nothing
    about the measured corpus.
    """
    rows = []
    for name, source in sample_profiles:
        base = source["ticks"]
        if len(base) < max(MIN_LAG_OVERLAP + 4, 12):
            continue
        checks = {}
        source_gap_values = set(source["gaps"])

        shifted = cadence_profile(tuple(tick + 7 for tick in base))
        found = relate(source, shifted)
        checks["F1_positive"] = bool(
            found and found["member"] == "F1" and found["c"] == 7
            and verify_witness(source, shifted, found)
        )

        scaled = cadence_profile(tuple(3 * tick + 5 for tick in base))
        found = relate(source, scaled)
        checks["F2A_positive"] = bool(
            found and found["member"] == "F2A"
            and Fraction(found["a_num"], found["a_den"]) == 3
            and Fraction(found["b_num"], found["b_den"]) == 5
            and verify_witness(source, scaled, found)
        )

        thinned = cadence_profile(base[1::3])
        found = relate(source, thinned)
        checks["F2B_positive"] = bool(
            found and found["member"] in ("F2B", "F3")
            and verify_witness(source, thinned, found)
        )

        lagged = cadence_profile(tuple(tick + 11 for tick in base[3:]))
        found = relate(source, lagged)
        checks["F3_positive"] = bool(
            found and verify_witness(source, lagged, found)
        )

        # The binary-search tick index must agree with the dict it replaces on
        # every tick of a real cadence, and must refuse every absent tick.
        lookup = {tick: position for position, tick in enumerate(base)}
        checks["tick_index_binary_search_matches_dict"] = (
            all(tick_position(base, tick) == lookup[tick] for tick in base)
            and all(
                tick_position(base, tick) is None
                for tick in range(base[0], base[-1] + 1)
                if tick not in lookup
            )
        )

        # Negative 1: shift one interior tick by a delta that manufactures two
        # gap values absent from X, so the perturbed gap word provably cannot
        # be a factor of X's and no member of F can hold.
        perturbed = None
        centre = len(base) // 2
        order = sorted(
            range(1, len(base) - 1), key=lambda index: abs(index - centre)
        )
        for middle in order:
            for delta in range(1, 65):
                left_gap = base[middle] - base[middle - 1] + delta
                right_gap = base[middle + 1] - base[middle] - delta
                if right_gap < 1:
                    break
                if left_gap in source_gap_values or right_gap in source_gap_values:
                    continue
                broken = list(base)
                broken[middle] += delta
                perturbed = cadence_profile(tuple(broken))
                break
            if perturbed is not None:
                break
        if perturbed is not None:
            exact = [
                f1_constant_offset(source, perturbed),
                f1w_windowed_offset(source, perturbed, HORIZON_CHUNKS),
                f2a_tick_affine(source, perturbed),
                f2b_index_affine(source, perturbed),
                f3_lag_offset(source, perturbed),
            ]
            residue = f4_periodic_residue(source, perturbed)
            partial = f3p_partial_lag(source, perturbed)
            checks["negative_one_tick_perturbation_refused_by_exact_members"] = (
                perturbed["ticks"] != base and not any(exact)
            )
            checks["negative_perturbation_F4_only_by_moving_its_transient"] = (
                residue is None
                or residue["transient_Y"] > residue["transient_X"]
            )
            checks["negative_one_tick_perturbation_partial_is_identity_only"] = (
                partial is None or partial["d"] == 0
            )

        # Negative 1b: an edit inside the final period leaves no periodic tail
        # for F4 to retreat to, so the tail law must refuse it outright.
        tail_broken = None
        last = len(base) - 2
        for delta in range(1, 65):
            if base[last] + delta >= base[last + 1]:
                break
            left_gap = base[last] - base[last - 1] + delta
            right_gap = base[last + 1] - base[last] - delta
            if left_gap in source_gap_values or right_gap in source_gap_values:
                continue
            broken = list(base)
            broken[last] += delta
            tail_broken = cadence_profile(tuple(broken))
            break
        if tail_broken is not None:
            checks["negative_tail_edit_refused_by_F4"] = (
                f4_periodic_residue(source, tail_broken) is None
            )

        # Negative 2: triangular-index thinning is neither an arithmetic index
        # map nor a contiguous gap-word factor.
        indices = []
        step = 0
        position = 0
        while position < len(base):
            indices.append(position)
            step += 1
            position += step
        if len(indices) >= 4:
            thinned_triangular = cadence_profile(tuple(base[i] for i in indices))
            checks["negative_triangular_thinning_refused"] = (
                relate(source, thinned_triangular) is None
                and relate(thinned_triangular, source) is None
            )

        # Verifier clause-regression probes.  Each probe feeds a witness that
        # reproduces (part of) the target but violates one clause of the
        # member's complete declared contract; the complete-contract verifier
        # must REFUSE every one.  These are decisive controls on the verifier
        # itself, incorporating the landed Cycle-869 review lessons.
        shift_c = 7
        w_low = max(0, shift_c)
        w_high = min(HORIZON_CHUNKS, HORIZON_CHUNKS + shift_c)
        w_profile = cadence_profile(tuple(
            tick + shift_c for tick in base
            if w_low <= tick + shift_c <= w_high
        ))
        good_w = f1w_windowed_offset(source, w_profile, HORIZON_CHUNKS)
        if good_w is not None:
            checks["verifier_refuses_noncanonical_F1W_window"] = (
                verify_witness(source, w_profile, good_w)
                and not verify_witness(source, w_profile, {
                    **good_w,
                    "window": [good_w["window"][0], good_w["window"][1] + 1],
                })
            )
            checks["verifier_refuses_F1W_offset_window_mismatch"] = (
                not verify_witness(
                    source, w_profile, {**good_w, "c": good_w["c"] + 1}
                )
            )
        f1_image = cadence_profile(tuple(tick + 5 for tick in base))
        checks["verifier_refuses_unit_slope_tick_affine"] = not verify_witness(
            source, f1_image,
            {"member": "F2A", "a_num": 1, "a_den": 1, "b_num": 5, "b_den": 1},
        )
        checks["verifier_refuses_nonpositive_slope_tick_affine"] = (
            not verify_witness(
                source, source,
                {"member": "F2A", "a_num": -1, "a_den": 1,
                 "b_num": 0, "b_den": 1},
            )
        )
        even_thinned = cadence_profile(base[0::2])
        checks["verifier_refuses_zero_step_index_affine"] = not verify_witness(
            source, even_thinned, {"member": "F2B", "s": 0, "r": 0}
        )
        checks["verifier_refuses_negative_start_index_affine"] = (
            not verify_witness(
                source, even_thinned, {"member": "F2B", "s": 2, "r": -2}
            )
        )
        checks["verifier_refuses_negative_lag_whole_clock_map"] = (
            not verify_witness(
                source, source,
                {"member": "F3", "L": -1, "d": 0, "overlap": len(base)},
            )
        )
        # A GENUINELY partial image: two unexplained head events on the target
        # and two unexplained tail events on the source, so the run covers
        # neither whole cadence.  (A tail-truncated image, the obvious
        # construction, is a whole-TARGET map and therefore belongs to the
        # index-lag member, not here -- the whole-cadence probes below cover
        # that shape.)
        p_profile = cadence_profile(
            (0, 1) + tuple(tick + 3 for tick in base[:-2])
        )
        good_p = f3p_partial_lag(source, p_profile)
        if good_p is not None:
            checks["verifier_refuses_below_floor_partial_overlap"] = (
                verify_witness(source, p_profile, good_p)
                and not verify_witness(
                    source, p_profile,
                    {**good_p, "overlap": MIN_LAG_OVERLAP - 1},
                )
            )
            checks["verifier_refuses_out_of_bounds_partial_overlap"] = (
                not verify_witness(
                    source, p_profile,
                    {**good_p, "overlap": len(p_profile["ticks"]) + 5},
                )
            )
            if len(p_profile["ticks"]) > 2 * MIN_LAG_OVERLAP:
                checks["verifier_refuses_below_coverage_partial_overlap"] = (
                    not verify_witness(
                        source, p_profile,
                        {**good_p, "overlap": MIN_LAG_OVERLAP},
                    )
                )
            checks["search_partial_overlap_is_never_a_whole_cadence"] = (
                not covers_whole_cadence(
                    len(source["ticks"]), len(p_profile["ticks"]),
                    good_p["L"], max(0, -good_p["L"]), good_p["overlap"],
                )
            )

        # The declared PARTIAL clause, enforced on both whole-cadence shapes.
        # A whole-TARGET run (equal-length clocks under a pure lag) and a
        # whole-SOURCE run (the shorter clock carried entirely into a longer
        # one) are both TOTAL maps: the partial member must refuse each, the
        # index-lag member must accept the same map, and the search must never
        # emit either shape.  The whole-target case is the executed review
        # control from the Cycle-879 confirmation round, carried here verbatim.
        whole_target_image = cadence_profile(tuple(tick + 200 for tick in base))
        whole_target_witness = {
            "member": "F3P", "L": 0, "d": 200, "overlap": len(base),
            "coverage": "1/1", "partial": False,
        }
        checks["verifier_refuses_whole_target_partial_overlap"] = (
            not verify_witness(source, whole_target_image, whole_target_witness)
            and verify_witness(source, whole_target_image, {
                "member": "F3", "L": 0, "d": 200, "overlap": len(base),
            })
        )
        checks["search_never_emits_whole_target_partial_overlap"] = (
            (lambda emitted: emitted is None or not covers_whole_cadence(
                len(base), len(whole_target_image["ticks"]), emitted["L"],
                max(0, -emitted["L"]), emitted["overlap"]))(
                    f3p_partial_lag(source, whole_target_image))
        )
        longer_image = cadence_profile(
            tuple(tick + 200 for tick in base) + (base[-1] + 200 + 4096,)
        )
        whole_source_witness = {
            "member": "F3P", "L": 0, "d": 200, "overlap": len(base),
            "coverage": "1/1", "partial": True,
        }
        checks["verifier_refuses_whole_source_partial_overlap"] = (
            not verify_witness(source, longer_image, whole_source_witness)
            and verify_witness(longer_image, source, {
                "member": "F3", "L": 0, "d": -200, "overlap": len(base),
            })
        )
        checks["search_never_emits_whole_source_partial_overlap"] = (
            (lambda emitted: emitted is None or not covers_whole_cadence(
                len(base), len(longer_image["ticks"]), emitted["L"],
                max(0, -emitted["L"]), emitted["overlap"]))(
                    f3p_partial_lag(source, longer_image))
        )
        x4_profile = cadence_profile((1, 3) + tuple(
            45 * cycle + residue
            for cycle in range(40) for residue in (5, 14, 30)
        ))
        y4_profile = cadence_profile((2,) + tuple(
            45 * cycle + residue
            for cycle in range(40) for residue in (14, 23, 39)
        ))
        z4_profile = cadence_profile(tuple(
            90 * cycle + residue
            for cycle in range(20) for residue in (5, 14, 30, 51)
        ))
        good_4 = f4_periodic_residue(x4_profile, y4_profile)
        if good_4 is not None:
            checks["verifier_refuses_wrong_period_residue_witness"] = (
                verify_witness(x4_profile, y4_profile, good_4)
                and not verify_witness(
                    x4_profile, y4_profile, {**good_4, "P": 90}
                )
            )
            checks["verifier_refuses_right_period_mismatch_residue_witness"] = (
                not verify_witness(x4_profile, z4_profile, good_4)
            )
            checks["verifier_refuses_transient_mismatch_residue_witness"] = (
                not verify_witness(
                    x4_profile, y4_profile,
                    {**good_4, "transient_X": good_4["transient_X"] + 1},
                )
            )

        rows.append({"clock": name, **checks})
        if len(rows) >= 3:
            break
    required = (
        "F1_positive",
        "F2A_positive",
        "F2B_positive",
        "F3_positive",
        "tick_index_binary_search_matches_dict",
        "negative_one_tick_perturbation_refused_by_exact_members",
        "negative_perturbation_F4_only_by_moving_its_transient",
        "negative_one_tick_perturbation_partial_is_identity_only",
        "negative_tail_edit_refused_by_F4",
        "negative_triangular_thinning_refused",
        "verifier_refuses_noncanonical_F1W_window",
        "verifier_refuses_F1W_offset_window_mismatch",
        "verifier_refuses_unit_slope_tick_affine",
        "verifier_refuses_nonpositive_slope_tick_affine",
        "verifier_refuses_zero_step_index_affine",
        "verifier_refuses_negative_start_index_affine",
        "verifier_refuses_negative_lag_whole_clock_map",
        "verifier_refuses_below_floor_partial_overlap",
        "verifier_refuses_out_of_bounds_partial_overlap",
        "verifier_refuses_below_coverage_partial_overlap",
        "verifier_refuses_whole_target_partial_overlap",
        "verifier_refuses_whole_source_partial_overlap",
        "search_partial_overlap_is_never_a_whole_cadence",
        "search_never_emits_whole_target_partial_overlap",
        "search_never_emits_whole_source_partial_overlap",
        "verifier_refuses_wrong_period_residue_witness",
        "verifier_refuses_right_period_mismatch_residue_witness",
        "verifier_refuses_transient_mismatch_residue_witness",
    )
    # The clause-probe INVENTORY is counted here, from the declaration and from
    # the executed rows, and published with the certificate.  Prose elsewhere in
    # this package quotes these numbers; counting them rather than asserting
    # them is what stops the prose and the code drifting apart.  A verifier
    # probe feeds a contract-violating witness to verify_witness and requires
    # refusal; a search-side probe requires that the emitted partial witness is
    # never a whole cadence.
    def _tally(labels):
        return {
            "verifier_clause_probes": sum(
                1 for label in labels if label.startswith("verifier_refuses_")
            ),
            "search_side_whole_cadence_probes": sum(
                1 for label in labels if label.startswith("search_")
            ),
        }

    declared_tally = _tally(required)
    executed_tally = _tally({label for row in rows for label in row})
    inventory = {
        "meaning": (
            "counted from the emitted rows, not asserted: a probe is one "
            "distinct check label that ran on at least one control clock.  "
            "A verifier clause probe feeds a witness violating one clause of "
            "a member's declared contract to verify_witness and requires "
            "REFUSAL; a search-side probe requires that the partial member's "
            "own search never emits a whole-cadence run."
        ),
        **executed_tally,
        "total_clause_probes": sum(executed_tally.values()),
        "executed_inventory_matches_declared": executed_tally == declared_tally,
    }
    passed = (
        bool(rows)
        and all(
            all(value for label, value in row.items() if label != "clock")
            for row in rows
        )
        # Every declared control must be constructible on at least one clock:
        # a control that never ran must not pass by absence.
        and all(any(label in row for row in rows) for label in required)
        # ...and the published probe counts must be the counts that ran.
        and inventory["executed_inventory_matches_declared"]
    )
    return rows, passed, inventory


# ------------------------------------------------- the pinned Cycle-869 numbers
def load_869_reference():
    """Parse the B=3 figures out of the sha-pinned Cycle-869 runner cache.

    Nothing here is a literal: every B=3 number in the comparison table is read
    from the committed cache of the B=3 run, whose header pins it to the
    content sha of the B=3 runner in this worktree.
    """
    text = (ROOT / CACHE_869).read_text()
    header = {}
    for line in text.splitlines():
        if line.startswith("----- stdout -----"):
            break
        if ": " in line:
            label, value = line.split(": ", 1)
            header[label.strip()] = value.strip()
    blocks = {}
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
    runner_sha = sha256((ROOT / PRIMARY_869).read_bytes()).hexdigest()
    verdict = blocks.get("G_RELATION_VERDICT", {})
    clocks = blocks.get("B_CLOCKS", {})
    across = blocks.get("F_ACROSS_KEYS", {})
    parsed = {
        "cache_header_runner": header.get("runner"),
        "cache_header_runner_sha256": header.get("runner_sha256"),
        "cache_exit_code": header.get("exit_code"),
        "cache_status": header.get("status"),
        "worktree_869_runner_sha256": runner_sha,
        "cache_pins_the_worktree_runner": header.get("runner_sha256") == runner_sha,
        "cache_records_a_clean_run": header.get("exit_code") == "0"
        and header.get("status") == "ok",
        "blocks_parsed": sorted(blocks),
    }
    if not (verdict and clocks and across):
        parsed["parse_complete"] = False
        return parsed, None
    scopes = {}
    for scope, key in (("pair", "pair_clocks"), ("bank", "bank_clocks")):
        rows = across.get(key, {})
        scopes[scope] = {
            "labels": sorted(rows),
            "sounding_keys": sum(row["sounding_keys"] for row in rows.values()),
            "silent_keys": sum(row["silent_keys"] for row in rows.values()),
            "distinct_gap_words": sum(
                row["distinct_gap_words"] for row in rows.values()
            ),
            "F1_edges": sum(
                row["F1_edges_to_class_representative"] for row in rows.values()
            ),
            "F1_nonzero_offset_edges": sum(
                row["F1_edges_with_nonzero_offset"] for row in rows.values()
            ),
            "F1_zero_offset_edges": sum(
                row["F1_edges_with_zero_offset_identical_cadences"]
                for row in rows.values()
            ),
            "F3_factor_edges": sum(
                row["F3_factor_edges_between_distinct_words"] for row in rows.values()
            ),
            "keys_outside_any_nontrivial_F1_class": sum(
                row["sounding_keys"] - row["keys_in_nontrivial_F1_class"]
                for row in rows.values()
            ),
        }
    full = {
        field: scopes["pair"][field] + scopes["bank"][field]
        for field in (
            "sounding_keys", "silent_keys", "distinct_gap_words", "F1_edges",
            "F1_nonzero_offset_edges", "F1_zero_offset_edges", "F3_factor_edges",
            "keys_outside_any_nontrivial_F1_class",
        )
    }
    substantive_related, substantive = (
        verdict["headline_substantive_full_dictionary_coverage"].split("/")
    )
    bank_related, bank_substantive = (
        verdict["within_key_bank_clock_substantive_coverage"].split("/")
    )
    reference = {
        "stations": B3_STATIONS,
        "banks": B3_FIXTURE_BANKS,
        "keys": B3_KEYS,
        "pair_clock_count": clocks["pair_clock_count"],
        "bank_clock_count": clocks["bank_clock_count"],
        "silent_pair_clocks": clocks["silent_pair_clocks"],
        "silent_bank_clocks": clocks["silent_bank_clocks"],
        "saturated_pair_clocks": clocks["saturated_pair_clocks"],
        "saturated_bank_clocks": clocks["saturated_bank_clocks"],
        "corpus_sha256": clocks["corpus_sha256"],
        "within_key_pair_clock_verdict": verdict["within_key_pair_clock_verdict"],
        "within_key_substantive_related": int(substantive_related),
        "within_key_substantive": int(substantive),
        "within_key_nonidentity_full_dictionaries": verdict[
            "within_key_substantive_nonidentity_full_dictionaries"
        ],
        "within_key_substantive_partial_matches": verdict[
            "within_key_substantive_partial_matches"
        ],
        "within_key_nonidentity_partial_matches": verdict[
            "within_key_substantive_nonidentity_partial_matches"
        ],
        "within_key_member_histogram": verdict["within_key_member_histogram"],
        "within_key_witness_parameters": verdict["within_key_witness_parameters"],
        "bank_clock_substantive_related": int(bank_related),
        "bank_clock_substantive": int(bank_substantive),
        "across_key_verdict": verdict["across_key_verdict"],
        "headline_F1_edges_as_published": verdict["across_key_F1_edges"],
        "headline_keys_outside_as_published": verdict[
            "across_key_keys_outside_any_nontrivial_F1_class"
        ],
        "pair_clock_information_content": verdict["pair_clock_information_content"],
        "detector_selected_periods": verdict[
            "detector_selected_nondegenerate_periods"
        ],
        "every_detected_period_is_whole_orbits": verdict[
            "every_detected_period_is_whole_orbits"
        ],
        "scopes": {
            "FULL_CORPUS": full,
            "SUB_CORPUS_pair_clocks_only": scopes["pair"],
            "SUB_CORPUS_bank_clocks_only": scopes["bank"],
        },
    }
    parsed["parse_complete"] = True
    # The 875 A4 finding, recomputed here rather than quoted: the published
    # 869 headline is the pair-only sub-corpus, not the full corpus.
    parsed["headline_scope_recomputed"] = (
        "SUB_CORPUS_pair_clocks_only"
        if reference["headline_F1_edges_as_published"] == scopes["pair"]["F1_edges"]
        and reference["headline_F1_edges_as_published"] != full["F1_edges"]
        else "FULL_CORPUS"
        if reference["headline_F1_edges_as_published"] == full["F1_edges"]
        else "UNRECOGNISED"
    )
    return parsed, reference


def compare_row(name, statement, b3, b4, rule, b3_holds, b4_holds,
                b3_magnitude, b4_magnitude, higher_is_stronger=True):
    """One computed row of the B-dependence table.

    The label is DATA: it is derived from the two measured sides by the stated
    rule and is never gated.  A row can read BREAKS without any gate moving.
    """
    if b3_holds and b4_holds:
        if b3_magnitude is None or b4_magnitude is None:
            label = "PERSISTS"
        elif b4_magnitude == b3_magnitude:
            label = "PERSISTS_UNCHANGED"
        elif (b4_magnitude > b3_magnitude) == higher_is_stronger:
            label = "PERSISTS_STRENGTHENED"
        else:
            label = "PERSISTS_WEAKENED"
    elif b3_holds and not b4_holds:
        label = "BREAKS_AT_B4"
    elif b4_holds and not b3_holds:
        label = "APPEARS_ONLY_AT_B4"
    else:
        label = "ABSENT_AT_BOTH"
    return {
        "fact": name,
        "statement": statement,
        "B3": b3,
        "B4": b4,
        "rule": rule,
        "B3_holds": bool(b3_holds),
        "B4_holds": bool(b4_holds),
        "B3_magnitude": None if b3_magnitude is None else str(b3_magnitude),
        "B4_magnitude": None if b4_magnitude is None else str(b4_magnitude),
        "higher_is_stronger": higher_is_stronger,
        "verdict": label,
    }


# ----------------------------------------------------------------------- report
def main():
    started = time.monotonic()
    program = C719.interleaved_program(FIXTURE_BANKS)
    placements = separated_placements()
    seeds, allocator_failures = event_seeds(program)
    keys, states, token_failures = census_initial_states(program, seeds, placements)
    per_bank_watched, source_pointer, local_wire_count = watched_layout()
    schedules = tuple(C719.mapped_macro(row) for row in program)

    setup = {
        "fixture_banks": FIXTURE_BANKS,
        "program_stations": len(program),
        "token_k": TOKEN_K,
        "events": EVENT_COUNT,
        "separated_placements": len(placements),
        "census_keys": len(keys),
        "state_width": len(states[0]) if states else 0,
        "watched_wires_per_bank": local_wire_count,
        "source_pointer_coordinate": source_pointer,
        "horizon_chunks": HORIZON_CHUNKS,
        "bank_pairs": [list(pair) for pair in BANK_PAIRS],
        "allocator_failures": allocator_failures,
        "token_placement_failures": token_failures,
        "declared_probe": "Cycle 866 B=4: 27 stations, census 648, events {0,1}, "
                          "k=2, horizon 8192",
    }
    structural_ok = (
        len(program) == STATIONS
        and len(placements) == EXPECTED_PLACEMENTS
        and len(keys) == EXPECTED_KEYS
        and allocator_failures == 0
        and token_failures == 0
        and all(len(row) == local_wire_count for row in per_bank_watched.values())
        and all(
            not (set(per_bank_watched[left]) & set(per_bank_watched[right]))
            for left, right in BANK_PAIRS
        )
        and all(
            source_pointer not in set(per_bank_watched[bank])
            for bank in range(FIXTURE_BANKS)
        )
    )
    if not structural_ok:
        print("FAIL A_SUBSTRATE :: " + compact(setup))
        return 1

    lane_count = len(keys)
    planes = transpose_states(states)
    masks = station_masks(keys)
    census_mask = (1 << lane_count) - 1
    evolution_mask = (1 << (lane_count + 1)) - 1
    duplicate_lane = lane_count

    bank_clocks = [[[] for _ in range(FIXTURE_BANKS)] for _ in range(lane_count)]
    pair_clocks = [[[] for _ in BANK_PAIRS] for _ in range(lane_count)]
    duplicate_bank_clocks = [[] for _ in range(FIXTURE_BANKS)]
    duplicate_pair_clocks = [[] for _ in BANK_PAIRS]
    duplicate_mismatches = 0
    store_saturations = 0
    bank_clean_totals = [0] * FIXTURE_BANKS
    pair_clean_totals = [0] * len(BANK_PAIRS)
    watched_by_bank = tuple(per_bank_watched[bank] for bank in range(FIXTURE_BANKS))

    def observe(tick):
        nonlocal duplicate_mismatches, store_saturations
        source_dirty = planes[source_pointer]
        clean = []
        for bank in range(FIXTURE_BANKS):
            dirty = source_dirty
            for wire in watched_by_bank[bank]:
                dirty |= planes[wire]
            clean.append(evolution_mask & ~dirty)
        for bank in range(FIXTURE_BANKS):
            duplicate_mismatches += (
                ((clean[bank] >> 0) & 1) != ((clean[bank] >> duplicate_lane) & 1)
            )
            if (clean[bank] >> duplicate_lane) & 1:
                duplicate_bank_clocks[bank].append(tick)
            mask = clean[bank] & census_mask
            bank_clean_totals[bank] += mask.bit_count()
            lane_rows = bank_clocks
            for lane in iter_mask(mask):
                row = lane_rows[lane][bank]
                if len(row) < CADENCE_STORE_CAP:
                    row.append(tick)
                else:
                    store_saturations += 1
        for index, (left, right) in enumerate(BANK_PAIRS):
            if (clean[left] >> duplicate_lane) & (clean[right] >> duplicate_lane) & 1:
                duplicate_pair_clocks[index].append(tick)
            mask = clean[left] & clean[right] & census_mask
            pair_clean_totals[index] += mask.bit_count()
            for lane in iter_mask(mask):
                row = pair_clocks[lane][index]
                if len(row) < CADENCE_STORE_CAP:
                    row.append(tick)
                else:
                    store_saturations += 1

    observe(0)
    for tick in range(1, HORIZON_CHUNKS + 1):
        phase = (tick - 1) % STATIONS
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

    bank_cadences = tuple(
        tuple(tuple(row) for row in lane) for lane in bank_clocks
    )
    pair_cadences = tuple(
        tuple(tuple(row) for row in lane) for lane in pair_clocks
    )
    del bank_clocks, pair_clocks

    # Definitional identity: a pair clock is the intersection of its bank clocks.
    intersection_failures = 0
    monotone_failures = 0
    horizon_failures = 0
    for lane in range(lane_count):
        for bank in range(FIXTURE_BANKS):
            row = bank_cadences[lane][bank]
            monotone_failures += any(
                row[i] >= row[i + 1] for i in range(len(row) - 1)
            )
            horizon_failures += any(not 0 <= tick <= HORIZON_CHUNKS for tick in row)
        for index, (left, right) in enumerate(BANK_PAIRS):
            expected = tuple(sorted(
                set(bank_cadences[lane][left]) & set(bank_cadences[lane][right])
            ))
            intersection_failures += expected != pair_cadences[lane][index]

    # Size of the disclosed store-cap deviation: how many clocks the Cycle-866
    # nominal cap of 1,024 would have truncated had it been used.
    clocks_over_866_cap = sum(
        1 for lane in bank_cadences for row in lane
        if len(row) > CYCLE866_DECLARED_STORE_CAP
    ) + sum(
        1 for lane in pair_cadences for row in lane
        if len(row) > CYCLE866_DECLARED_STORE_CAP
    )
    events_lost_at_866_cap = sum(
        max(0, len(row) - CYCLE866_DECLARED_STORE_CAP)
        for lane in bank_cadences for row in lane
    ) + sum(
        max(0, len(row) - CYCLE866_DECLARED_STORE_CAP)
        for lane in pair_cadences for row in lane
    )

    bank_profiles = tuple(
        tuple(cadence_profile(row) for row in lane) for lane in bank_cadences
    )
    pair_profiles = tuple(
        tuple(cadence_profile(row) for row in lane) for lane in pair_cadences
    )

    corpus_digest = digest({
        "bank": [[list(row) for row in lane] for lane in bank_cadences],
        "pair": [[list(row) for row in lane] for lane in pair_cadences],
    })

    silent_and_saturated = sum(
        1 for lane in pair_profiles for profile in lane
        if not profile["ticks"] and profile["saturation"] is not None
    )
    b_pass = (
        silent_and_saturated == 0
        and intersection_failures == 0
        and monotone_failures == 0
        and horizon_failures == 0
        and store_saturations == 0
        and sum(bank_clean_totals) == sum(
            len(row) for lane in bank_cadences for row in lane
        )
        and sum(pair_clean_totals) == sum(
            len(row) for lane in pair_cadences for row in lane
        )
    )

    empty_bank = sum(1 for lane in bank_cadences for row in lane if not row)
    empty_pair = sum(1 for lane in pair_cadences for row in lane if not row)

    def length_bands(cadences):
        bands = Counter()
        for lane in cadences:
            for row in lane:
                size = len(row)
                if size == 0:
                    bands["0"] += 1
                else:
                    low = 1
                    while low * 2 <= size:
                        low *= 2
                    bands[f"{low}-{low * 2 - 1}"] += 1
        return dict(sorted(bands.items(), key=lambda item: int(item[0].split("-")[0])))

    bank_length_bands = length_bands(bank_cadences)
    pair_length_bands = length_bands(pair_cadences)

    def periodic_census(profiles):
        periodic = saturated = 0
        periods = Counter()
        for lane in profiles:
            for profile in lane:
                if profile["saturation"] is not None:
                    saturated += 1
                period = profile["period"]
                if period is None or not period["shift_exact_on_window"]:
                    continue
                periodic += 1
                if not period["saturated"] and profile["saturation"] is None:
                    periods[period["period_ticks"]] += 1
        return periodic, saturated, dict(sorted(periods.items()))

    periodic_pair_clocks, saturated_pair_clocks, pair_period_hist = periodic_census(
        pair_profiles
    )
    periodic_bank_clocks, saturated_bank_clocks, bank_period_hist = periodic_census(
        bank_profiles
    )

    domination = Counter()
    for lane in range(lane_count):
        for index, (left, right) in enumerate(BANK_PAIRS):
            joint = pair_cadences[lane][index]
            low = bank_cadences[lane][left]
            high = bank_cadences[lane][right]
            if not joint:
                domination["SILENT_PAIR"] += 1
            elif joint == low and joint == high:
                domination["BOTH_BANK_CLOCKS_IDENTICAL"] += 1
            elif joint == low or joint == high:
                domination["ONE_BANK_GATES_THE_PAIR"] += 1
            else:
                domination["STRICTLY_JOINT"] += 1

    sample_rows = []
    for lane in range(lane_count):
        if len(sample_rows) >= SAMPLE_PRINT_CAP:
            break
        if min(len(row) for row in pair_cadences[lane]) < 4:
            continue
        sample_rows.append({
            "key": short_key(keys[lane]),
            "bank_clock_lengths": [len(row) for row in bank_cadences[lane]],
            "pair_clock_lengths": [len(row) for row in pair_cadences[lane]],
            "pair_clock_heads": [list(row[:6]) for row in pair_cadences[lane]],
            "pair_periods": [
                None if profile["period"] is None else profile["period"]["period_ticks"]
                for profile in pair_profiles[lane]
            ],
        })

    control_pool = []
    for lane in range(lane_count):
        for index, profile in enumerate(pair_profiles[lane]):
            if 24 <= len(profile["ticks"]) <= 4096:
                control_pool.append((f"{short_key(keys[lane])}/pair{index}", profile))
        if len(control_pool) >= 6:
            break
    control_rows, controls_pass, control_inventory = family_controls(control_pool)

    # ------------------------------------------------- within-key comparisons
    def is_saturated(profile):
        return profile["saturation"] is not None

    def within_key_block(profiles, labels):
        verdicts = Counter()
        evidence = Counter()
        parameters = Counter()
        witnesses = []
        thin_witnesses = []
        witness_failures = 0
        whole_cadence_partials = 0
        comparable = 0
        substantive = 0
        substantive_related = 0
        code_histogram = Counter()
        disposition_codes = {}
        relation_records = []
        for lane in range(lane_count):
            codes = []
            for left, right in combinations(range(len(labels)), 2):
                x_profile = profiles[lane][left]
                y_profile = profiles[lane][right]
                if not x_profile["ticks"] or not y_profile["ticks"]:
                    verdicts["ONE_SIDE_SILENT"] += 1
                    codes.append("0")
                    continue
                if is_saturated(x_profile) and is_saturated(y_profile):
                    verdicts["TRIVIAL_SATURATION"] += 1
                    codes.append("s")
                    continue
                comparable += 1
                shorter = min(len(x_profile["ticks"]), len(y_profile["ticks"]))
                thin = shorter < EVIDENCE_FLOOR
                if not thin:
                    substantive += 1
                found = relate(x_profile, y_profile)
                direction = "forward"
                if found is None:
                    found = relate(y_profile, x_profile)
                    direction = "reverse"
                if found is None:
                    verdicts["NO_RELATION_IN_F"] += 1
                    evidence[
                        "THIN_NO_RELATION" if thin else "SUBSTANTIVE_NO_RELATION"
                    ] += 1
                    codes.append("x")
                    continue
                source, target = (
                    (x_profile, y_profile) if direction == "forward"
                    else (y_profile, x_profile)
                )
                reverified = verify_witness(source, target, found)
                if not reverified:
                    witness_failures += 1
                # Standing assertion on the declared PARTIAL clause: no
                # emitted partial-overlap witness may carry a whole cadence.
                if found["member"] == "F3P" and covers_whole_cadence(
                    len(source["ticks"]), len(target["ticks"]),
                    found["L"], max(0, -found["L"]), found["overlap"],
                ):
                    whole_cadence_partials += 1
                verdicts[found["member"]] += 1
                full_member = found["member"] in FULL_MEMBERS
                if full_member:
                    evidence["THIN_RELATION" if thin else "SUBSTANTIVE_RELATION"] += 1
                if full_member and not thin:
                    substantive_related += 1
                plain = identity_like(found)
                if found["member"] in PARTIAL_MEMBERS:
                    evidence["PARTIAL" if thin is False else "THIN_PARTIAL"] += 1
                    if not thin and not plain:
                        parameters["#SUBSTANTIVE_NONIDENTITY_PARTIAL"] += 1
                if not thin and not plain and found["member"] in FULL_MEMBERS:
                    parameters["#SUBSTANTIVE_NONIDENTITY"] += 1
                if not thin and plain and found["member"] in FULL_MEMBERS:
                    parameters["#SUBSTANTIVE_IDENTITY_LIKE"] += 1
                if found["member"] in ("F1", "F1W"):
                    parameters[f"{found['member']}:c={found['c']}"] += 1
                elif found["member"] in ("F3", "F3P"):
                    parameters[f"{found['member']}:L={found['L']},d={found['d']}"] += 1
                elif found["member"] == "F4":
                    parameters[f"F4:P={found['P']},c={found['c']}"] += 1
                else:
                    parameters[found["member"]] += 1
                codes.append(
                    "w" if found["member"] == "F1W"
                    else "p" if found["member"] == "F3P"
                    else found["member"][1:2]
                )
                member = found["member"]
                if member in ("F1", "F1W"):
                    params = [found["c"]]
                elif member == "F2A":
                    params = [found["a_num"], found["a_den"],
                              found["b_num"], found["b_den"]]
                elif member == "F2B":
                    params = [found["s"], found["r"]]
                elif member == "F3":
                    params = [found["L"], found["d"]]
                elif member == "F3P":
                    params = [found["L"], found["d"], found["overlap"]]
                else:
                    params = [found["P"], found["c"]]
                relation_records.append([
                    short_key(keys[lane]),
                    labels[left if direction == "forward" else right],
                    labels[right if direction == "forward" else left],
                    member,
                    params,
                    int(plain),
                    int(thin),
                ])
                row = {
                    "key": short_key(keys[lane]),
                    "from": labels[left if direction == "forward" else right],
                    "to": labels[right if direction == "forward" else left],
                    "witness": found,
                    "reverified": reverified,
                    "identity_like": plain,
                    "source_length": len(source["ticks"]),
                    "target_length": len(target["ticks"]),
                }
                bucket = thin_witnesses if thin else witnesses
                if not plain and not thin and len(bucket) < WITNESS_PRINT_CAP:
                    bucket.append(row)
                elif len(bucket) < 2:
                    bucket.append(row)
            code_histogram["".join(codes)] += 1
            disposition_codes[short_key(keys[lane])] = "".join(codes)
        # Witness parameters are capped for stdout, largest classes first.
        printable = sorted(
            ((label, count) for label, count in parameters.items()
             if not label.startswith("#")),
            key=lambda item: (-item[1], item[0]),
        )[:48]
        return {
            "verdicts": dict(sorted(verdicts.items())),
            "evidence_split": dict(sorted(evidence.items())),
            "witness_parameter_histogram": dict(sorted(printable)),
            "witness_parameter_classes": sum(
                1 for label in parameters if not label.startswith("#")
            ),
            "substantive_nonidentity_full_dictionaries": (
                parameters["#SUBSTANTIVE_NONIDENTITY"]
            ),
            "substantive_identity_like_full_dictionaries": (
                parameters["#SUBSTANTIVE_IDENTITY_LIKE"]
            ),
            "substantive_nonidentity_partial_matches": (
                parameters["#SUBSTANTIVE_NONIDENTITY_PARTIAL"]
            ),
            "substantive_partial_matches": evidence["PARTIAL"],
            "comparable_pairs_of_clocks": comparable,
            "substantive_pairs_of_clocks": substantive,
            "substantive_relations": substantive_related,
            "witness_reverification_failures": witness_failures,
            "partial_witnesses_covering_a_whole_cadence": whole_cadence_partials,
            "substantive_witness_examples": witnesses,
            "thin_witness_examples": thin_witnesses,
            "per_key_code_histogram": dict(sorted(
                code_histogram.items(), key=lambda item: (-item[1], item[0])
            )[:24]),
            "distinct_per_key_codes": len(code_histogram),
            # The COMPLETE per-comparison disposition surface, emitted so an
            # independent checker can adjudicate set inclusion per canonical
            # comparison (key, ordered clock-pair position) rather than by
            # aggregate counts.  Codes use the code_legend; positions follow
            # combinations(labels, 2) in order.
            "full_disposition_codes": disposition_codes,
            "relation_record_format": (
                "[key, from, to, member, params, identity_like, thin]; params "
                "per member: F1/F1W [c]; F2A [a_num,a_den,b_num,b_den]; F2B "
                "[s,r]; F3 [L,d]; F3P [L,d,overlap]; F4 [P,c]"
            ),
            "relation_records": relation_records,
            "relation_record_count": len(relation_records),
        }

    pair_labels = tuple(f"{left}{right}" for left, right in BANK_PAIRS)
    bank_labels = tuple(str(bank) for bank in range(FIXTURE_BANKS))
    within_pair = within_key_block(pair_profiles, pair_labels)
    within_bank = within_key_block(bank_profiles, bank_labels)
    d_pass = (
        within_pair["witness_reverification_failures"] == 0
        and within_bank["witness_reverification_failures"] == 0
        and within_pair["partial_witnesses_covering_a_whole_cadence"] == 0
        and within_bank["partial_witnesses_covering_a_whole_cadence"] == 0
        and sum(within_pair["verdicts"].values())
        == lane_count * len(BANK_PAIRS) * (len(BANK_PAIRS) - 1) // 2
        and sum(within_bank["verdicts"].values())
        == lane_count * FIXTURE_BANKS * (FIXTURE_BANKS - 1) // 2
        and all(
            sum(block["evidence_split"].values())
            == block["comparable_pairs_of_clocks"]
            for block in (within_pair, within_bank)
        )
        and all(
            block["substantive_relations"]
            == block["substantive_nonidentity_full_dictionaries"]
            + block["substantive_identity_like_full_dictionaries"]
            for block in (within_pair, within_bank)
        )
    )

    # --------------------------------------------------- across-key comparisons
    def across_key_block(profiles, labels):
        blocks = {}
        cap_hits = 0
        witness_failures = 0
        for index, label in enumerate(labels):
            buckets = defaultdict(list)
            silent = 0
            for lane in range(lane_count):
                profile = profiles[lane][index]
                if not profile["ticks"]:
                    silent += 1
                    continue
                buckets[profile["word"]].append(lane)
            reps = sorted(buckets, key=lambda word: (-len(buckets[word]), word))
            capped = reps[:ACROSS_KEY_REP_CAP]
            cap_hits += len(reps) - len(capped)
            offset_classes = Counter(len(buckets[word]) for word in reps)
            offset_witnesses = []
            offset_values = Counter()
            zero_offset_edges = 0
            nonzero_offset_edges = 0
            for word in reps:
                lanes = buckets[word]
                if len(lanes) < 2:
                    continue
                source = profiles[lanes[0]][index]
                for lane in lanes[1:]:
                    target = profiles[lane][index]
                    found = f1_constant_offset(source, target)
                    if found is None or not verify_witness(source, target, found):
                        witness_failures += 1
                        continue
                    if found["c"]:
                        nonzero_offset_edges += 1
                        offset_values[found["c"]] += 1
                    else:
                        zero_offset_edges += 1
                if len(offset_witnesses) < WITNESS_PRINT_CAP:
                    partner = profiles[lanes[1]][index]
                    found = f1_constant_offset(source, partner)
                    if found is not None:
                        offset_witnesses.append({
                            "from_key": short_key(keys[lanes[0]]),
                            "to_key": short_key(keys[lanes[1]]),
                            "witness": found,
                            "class_size": len(lanes),
                        })
            # F3 across keys: shorter gap word a contiguous factor of a longer one.
            ordered = sorted(capped, key=len)
            factor_edges = 0
            factor_examples = []
            for position, needle in enumerate(ordered):
                needle_len = needle.count("|") - 1
                if needle_len + 1 < MIN_LAG_OVERLAP:
                    continue
                for haystack in ordered[position + 1:]:
                    if len(haystack) < len(needle):
                        continue
                    if haystack.find(needle) < 0:
                        continue
                    source = profiles[buckets[haystack][0]][index]
                    target = profiles[buckets[needle][0]][index]
                    found = f3_lag_offset(source, target)
                    if found is None:
                        continue
                    if not verify_witness(source, target, found):
                        witness_failures += 1
                        continue
                    factor_edges += 1
                    if len(factor_examples) < WITNESS_PRINT_CAP:
                        factor_examples.append({
                            "from_key": short_key(keys[buckets[haystack][0]]),
                            "to_key": short_key(keys[buckets[needle][0]]),
                            "witness": found,
                        })
            periods = Counter(
                profiles[lane][index]["period"]["period_ticks"]
                for lane in range(lane_count)
                if profiles[lane][index]["period"] is not None
                and profiles[lane][index]["period"]["shift_exact_on_window"]
            )
            blocks[label] = {
                "sounding_keys": lane_count - silent,
                "silent_keys": silent,
                "distinct_gap_words": len(reps),
                "largest_F1_class": max(offset_classes) if offset_classes else 0,
                "keys_in_nontrivial_F1_class": sum(
                    size * count for size, count in offset_classes.items() if size > 1
                ),
                "keys_outside_any_nontrivial_F1_class": (
                    lane_count - silent
                    - sum(size * count for size, count in offset_classes.items()
                          if size > 1)
                ),
                "F1_offset_witnesses": offset_witnesses,
                "F1_edges_to_class_representative": zero_offset_edges
                + nonzero_offset_edges,
                "F1_edges_with_nonzero_offset": nonzero_offset_edges,
                "F1_edges_with_zero_offset_identical_cadences": zero_offset_edges,
                "F1_distinct_nonzero_offsets": len(offset_values),
                "F1_offset_extremes": (
                    [min(offset_values), max(offset_values)] if offset_values else []
                ),
                "F3_factor_edges_between_distinct_words": factor_edges,
                "F3_factor_examples": factor_examples,
                "F4_period_histogram": dict(sorted(periods.items())),
            }
        return blocks, cap_hits, witness_failures

    across_pair, pair_cap_hits, pair_witness_failures = across_key_block(
        pair_profiles, pair_labels
    )
    across_bank, bank_cap_hits, bank_witness_failures = across_key_block(
        bank_profiles, bank_labels
    )

    ROLLUP_FIELDS = (
        "sounding_keys", "silent_keys", "distinct_gap_words",
        "keys_in_nontrivial_F1_class", "keys_outside_any_nontrivial_F1_class",
        "F1_edges_to_class_representative", "F1_edges_with_nonzero_offset",
        "F1_edges_with_zero_offset_identical_cadences",
        "F3_factor_edges_between_distinct_words",
    )

    def rollup(*groups):
        total = {field: 0 for field in ROLLUP_FIELDS}
        labels = []
        for group in groups:
            for label, block in group.items():
                labels.append(label)
                for field in ROLLUP_FIELDS:
                    total[field] += block[field]
        total["clock_indices"] = len(labels)
        total["labels"] = sorted(labels)
        return total

    sub_pair = rollup(across_pair)
    sub_bank = rollup(across_bank)
    full_corpus = rollup(across_pair, across_bank)
    across_scopes = {
        "FULL_CORPUS": full_corpus,
        "SUB_CORPUS_pair_clocks_only": sub_pair,
        "SUB_CORPUS_bank_clocks_only": sub_bank,
    }
    e_pass = (
        pair_cap_hits == 0
        and bank_cap_hits == 0
        and pair_witness_failures == 0
        and bank_witness_failures == 0
        and all(
            block["sounding_keys"] + block["silent_keys"] == lane_count
            for block in list(across_pair.values()) + list(across_bank.values())
        )
        and all(
            full_corpus[field] == sub_pair[field] + sub_bank[field]
            for field in ROLLUP_FIELDS
        )
        and full_corpus["clock_indices"] == len(BANK_PAIRS) + FIXTURE_BANKS
        and all(
            block["F1_edges_to_class_representative"]
            == block["F1_edges_with_nonzero_offset"]
            + block["F1_edges_with_zero_offset_identical_cadences"]
            for block in list(across_pair.values()) + list(across_bank.values())
        )
    )

    # -------------------------------------------------------------- the verdict
    period_arithmetic = []
    for period in sorted(set(bank_period_hist) | set(pair_period_hist)):
        row = {
            "period_ticks": period,
            "orbits": str(Fraction(period, STATIONS).limit_denominator()),
            "period_over_stations_squared": str(
                Fraction(period, STATIONS * STATIONS)
            ),
            "exact_multiple_of_stations": period % STATIONS == 0,
            "exact_multiple_of_stations_squared": period % (STATIONS * STATIONS) == 0,
            "bank_clocks_carrying_it": bank_period_hist.get(period, 0),
            "pair_clocks_carrying_it": pair_period_hist.get(period, 0),
        }
        period_arithmetic.append(row)
    every_period_whole_orbits = all(
        row["exact_multiple_of_stations"] for row in period_arithmetic
    )
    non_orbit_rows = [
        row for row in period_arithmetic if not row["exact_multiple_of_stations"]
    ]
    period_break = {
        "distinct_nondegenerate_periods": len(period_arithmetic),
        "periods_that_are_whole_orbits": len(period_arithmetic) - len(non_orbit_rows),
        "periods_that_are_not_whole_orbits": len(non_orbit_rows),
        "non_orbit_periods": [row["period_ticks"] for row in non_orbit_rows],
        "clocks_carrying_a_non_orbit_period": sum(
            row["bank_clocks_carrying_it"] + row["pair_clocks_carrying_it"]
            for row in non_orbit_rows
        ),
        "clocks_carrying_a_whole_orbit_period": sum(
            row["bank_clocks_carrying_it"] + row["pair_clocks_carrying_it"]
            for row in period_arithmetic if row["exact_multiple_of_stations"]
        ),
        "note": (
            "The boolean is ALL-or-nothing over the DETECTOR-SELECTED periods "
            "by construction, so it is reported here with its size: how many "
            "distinct detector-selected periods break it and how many clocks "
            "carry them.  A single surviving non-orbit detector-selected "
            "period falsifies the B=3-corpus divisibility observation for "
            "detector-selected periods, whatever the majority does; no "
            "least-period or complete-census statement is made on either side."
        ),
    }

    pair_totals = within_pair["verdicts"]
    comparable = within_pair["comparable_pairs_of_clocks"]
    related = comparable - pair_totals.get("NO_RELATION_IN_F", 0)
    substantive = within_pair["substantive_pairs_of_clocks"]
    substantive_related = within_pair["substantive_relations"]
    coverage = Fraction(substantive_related, substantive) if substantive else Fraction(0)
    substantive_nonidentity = within_pair["substantive_nonidentity_full_dictionaries"]
    substantive_identity = within_pair["substantive_identity_like_full_dictionaries"]
    substantive_partial = within_pair["substantive_partial_matches"]
    substantive_partial_nonidentity = within_pair[
        "substantive_nonidentity_partial_matches"
    ]
    if substantive and substantive_related == substantive:
        relation_verdict = "DICTIONARY_TOTAL_WITHIN_KEY"
    elif substantive_related == 0:
        relation_verdict = "FAMILY_EXHAUSTED_NO_SUBSTANTIVE_RELATION"
    elif substantive_nonidentity == 0:
        relation_verdict = "COINCIDENCE_ONLY_NO_TRANSFORMATION_LAW_WITHIN_KEY"
    else:
        relation_verdict = "DICTIONARY_SPARSE_WITHIN_KEY"

    # The across-key verdict is priced to the FULL corpus, per Cycle 875's A4.
    cross_key_edges = full_corpus["F1_edges_to_class_representative"]
    cross_key_nonzero = full_corpus["F1_edges_with_nonzero_offset"]
    cross_key_factor = full_corpus["F3_factor_edges_between_distinct_words"]
    unrelated_across = full_corpus["keys_outside_any_nontrivial_F1_class"]
    all_blocks = list(across_pair.values()) + list(across_bank.values())
    if all(block["largest_F1_class"] <= 1 for block in all_blocks) and all(
        block["F3_factor_edges_between_distinct_words"] == 0 for block in all_blocks
    ):
        across_verdict = "NO_CROSS_KEY_DICTIONARY"
    elif cross_key_nonzero == 0:
        across_verdict = "CROSS_KEY_COINCIDENCE_ONLY"
    else:
        across_verdict = "CROSS_KEY_TIME_TRANSLATION_DICTIONARY"

    pricing = {
        "family": list(FAMILY),
        "closure": FAMILY_CLOSURE,
        "declared_caps": {
            "horizon_chunks": HORIZON_CHUNKS,
            "cadence_store_cap": CADENCE_STORE_CAP,
            "cadence_store_saturations": store_saturations,
            "cycle866_nominal_store_cap": CYCLE866_DECLARED_STORE_CAP,
            "clocks_that_866_store_cap_would_truncate": clocks_over_866_cap,
            "events_that_866_store_cap_would_discard": events_lost_at_866_cap,
            "period_tail_window": PERIOD_TAIL_WINDOW,
            "period_tail_floor": PERIOD_TAIL_FLOOR,
            "period_tail_ladder_ratio": list(PERIOD_TAIL_RATIO),
            "period_max_block_gaps": PERIOD_MAX_BLOCK_GAPS,
            "min_saturation_run": MIN_SATURATION_RUN,
            "saturation_detection": (
                "exact and cap-free: maximal consecutive run ending at the "
                "horizon, no period search involved"
            ),
            "windowed_offset_anchors": WINDOWED_OFFSET_ANCHORS,
            "min_lag_overlap": MIN_LAG_OVERLAP,
            "evidence_floor": EVIDENCE_FLOOR,
            "across_key_rep_cap": ACROSS_KEY_REP_CAP,
            "across_key_rep_cap_hits": pair_cap_hits + bank_cap_hits,
        },
        "disclosed_deviations_from_the_869_and_866_declarations": list(
            DISCLOSED_DEVIATIONS
        ),
        "analyst_declared_thresholds": {
            "classification": (
                "every cap, floor and qualitative boundary in this block is "
                "an ANALYST-DECLARED operational boundary condition.  None is "
                "derived from the four axioms, from any approved primitive, "
                "from the Cycle-719 kernel, or from measured data, and none "
                "is fitted.  Every conclusion is conditional on this full "
                "finite box."
            ),
            "qualitative_rarity_boundary": (
                "1/10 -- the comparison-table rule for 'all but exhausted', "
                "'non-identity dictionaries are rare', 'bank clocks carry no "
                "dictionary', and 'saturated clocks are a negligible "
                "minority'"
            ),
            "majority_boundary": (
                "1/2 -- the comparison-table rule for 'classes cover most "
                "keys' and 'most pair clocks are strictly joint'"
            ),
            "evidence_floor": EVIDENCE_FLOOR,
            "partial_coverage_floor": (
                f"{PARTIAL_COVERAGE_FLOOR.numerator}/"
                f"{PARTIAL_COVERAGE_FLOOR.denominator}"
            ),
            "period_detector_walls": (
                f"tail window {PERIOD_TAIL_WINDOW}, tail floor "
                f"{PERIOD_TAIL_FLOOR}, ladder ratio "
                f"{PERIOD_TAIL_RATIO[0]}/{PERIOD_TAIL_RATIO[1]}, block cap "
                f"{PERIOD_MAX_BLOCK_GAPS}, repeat floor {MIN_PERIOD_REPEATS} "
                "-- the detector box that makes every period claim "
                "detector-selected"
            ),
            "windowed_offset_anchors": WINDOWED_OFFSET_ANCHORS,
            "min_lag_overlap": MIN_LAG_OVERLAP,
            "min_saturation_run": MIN_SATURATION_RUN,
        },
        "what_a_negative_costs": (
            "A NO_RELATION_IN_F entry is priced to this family at these caps and "
            "this horizon.  It does not exclude transformations outside F, nor "
            f"relations that only appear beyond tick {HORIZON_CHUNKS}."
        ),
    }

    # ------------------------------------------------- the B-dependence table
    reference_meta, b3 = load_869_reference()
    comparison = []
    table_arithmetic_ok = b3 is not None
    if b3 is not None:
        b3_full = b3["scopes"]["FULL_CORPUS"]
        b3_pair = b3["scopes"]["SUB_CORPUS_pair_clocks_only"]
        b3_cov = Fraction(
            b3["within_key_substantive_related"], b3["within_key_substantive"]
        ) if b3["within_key_substantive"] else Fraction(0)
        comparison.append(compare_row(
            "WITHIN_KEY_FAMILY_ALL_BUT_EXHAUSTED",
            "the declared family supplies a whole-cadence dictionary on fewer "
            "than one in ten substantive pair-clock comparisons",
            f"{b3['within_key_substantive_related']}/"
            f"{b3['within_key_substantive']}",
            f"{substantive_related}/{substantive}",
            "holds when coverage < 1/10; magnitude is the coverage fraction, "
            "lower is stronger exhaustion",
            b3_cov < Fraction(1, 10), coverage < Fraction(1, 10),
            b3_cov, coverage, higher_is_stronger=False,
        ))
        comparison.append(compare_row(
            "WITHIN_KEY_SUBSTANTIVE_NONIDENTITY_DICTIONARIES_ARE_RARE",
            "almost every whole-cadence dictionary found within a key is "
            "identity-like containment, not a transformation law",
            b3["within_key_nonidentity_full_dictionaries"],
            substantive_nonidentity,
            "holds when non-identity dictionaries are at most 1/10 of the "
            "substantive comparisons; magnitude is that rate, lower is stronger",
            Fraction(b3["within_key_nonidentity_full_dictionaries"],
                     b3["within_key_substantive"]) <= Fraction(1, 10)
            if b3["within_key_substantive"] else False,
            Fraction(substantive_nonidentity, substantive) <= Fraction(1, 10)
            if substantive else False,
            Fraction(b3["within_key_nonidentity_full_dictionaries"],
                     b3["within_key_substantive"])
            if b3["within_key_substantive"] else None,
            Fraction(substantive_nonidentity, substantive) if substantive else None,
            higher_is_stronger=False,
        ))
        comparison.append(compare_row(
            "WITHIN_KEY_BANK_CLOCKS_CARRY_NO_DICTIONARY",
            "the single-bank clocks of one key are essentially unrelated to "
            "each other inside the declared family",
            f"{b3['bank_clock_substantive_related']}/"
            f"{b3['bank_clock_substantive']}",
            f"{within_bank['substantive_relations']}/"
            f"{within_bank['substantive_pairs_of_clocks']}",
            "holds when bank-clock coverage < 1/10; lower is stronger",
            Fraction(b3["bank_clock_substantive_related"],
                     b3["bank_clock_substantive"]) < Fraction(1, 10)
            if b3["bank_clock_substantive"] else False,
            Fraction(within_bank["substantive_relations"],
                     within_bank["substantive_pairs_of_clocks"]) < Fraction(1, 10)
            if within_bank["substantive_pairs_of_clocks"] else False,
            Fraction(b3["bank_clock_substantive_related"],
                     b3["bank_clock_substantive"])
            if b3["bank_clock_substantive"] else None,
            Fraction(within_bank["substantive_relations"],
                     within_bank["substantive_pairs_of_clocks"])
            if within_bank["substantive_pairs_of_clocks"] else None,
            higher_is_stronger=False,
        ))
        comparison.append(compare_row(
            "ACROSS_KEY_F1_IS_A_TIME_TRANSLATION_LAW_FULL_CORPUS",
            "over the FULL corpus every constant-offset edge between keys "
            "carries a NONZERO offset",
            f"{b3_full['F1_nonzero_offset_edges']}/{b3_full['F1_edges']}",
            f"{cross_key_nonzero}/{cross_key_edges}",
            "holds when the nonzero fraction is 1; magnitude is that fraction",
            b3_full["F1_edges"] > 0
            and b3_full["F1_nonzero_offset_edges"] == b3_full["F1_edges"],
            cross_key_edges > 0 and cross_key_nonzero == cross_key_edges,
            Fraction(b3_full["F1_nonzero_offset_edges"], b3_full["F1_edges"])
            if b3_full["F1_edges"] else None,
            Fraction(cross_key_nonzero, cross_key_edges)
            if cross_key_edges else None,
        ))
        comparison.append(compare_row(
            "ACROSS_KEY_F1_CLASSES_COVER_MOST_KEYS_FULL_CORPUS",
            "most sounding keys sit inside some nontrivial constant-offset "
            "class, leaving a minority residue",
            f"{b3_full['keys_outside_any_nontrivial_F1_class']} outside of "
            f"{b3_full['sounding_keys']} sounding",
            f"{unrelated_across} outside of {full_corpus['sounding_keys']} sounding",
            "holds when the residue is under half the sounding keys; magnitude "
            "is the covered fraction, higher is stronger",
            b3_full["sounding_keys"] > 0
            and Fraction(b3_full["keys_outside_any_nontrivial_F1_class"],
                         b3_full["sounding_keys"]) < Fraction(1, 2),
            full_corpus["sounding_keys"] > 0
            and Fraction(unrelated_across, full_corpus["sounding_keys"])
            < Fraction(1, 2),
            Fraction(b3_full["sounding_keys"]
                     - b3_full["keys_outside_any_nontrivial_F1_class"],
                     b3_full["sounding_keys"]) if b3_full["sounding_keys"] else None,
            Fraction(full_corpus["sounding_keys"] - unrelated_across,
                     full_corpus["sounding_keys"])
            if full_corpus["sounding_keys"] else None,
        ))
        comparison.append(compare_row(
            "ACROSS_KEY_F3_FACTOR_LAYER_EXISTS_FULL_CORPUS",
            "under the constant-offset classes there is a gap-word factor "
            "layer: shorter cadences are contiguous factors of longer ones",
            b3_full["F3_factor_edges"],
            cross_key_factor,
            "holds when at least one F3 factor edge exists; magnitude is the "
            "edge count, higher is a thicker layer",
            b3_full["F3_factor_edges"] > 0, cross_key_factor > 0,
            b3_full["F3_factor_edges"], cross_key_factor,
        ))
        b3_periods = [
            row["period_ticks"] for row in b3["detector_selected_periods"]
        ]
        comparison.append(compare_row(
            "EVERY_DETECTED_PERIOD_IS_WHOLE_RING_ORBITS",
            "every DETECTOR-SELECTED nondegenerate period in the corpus is an "
            "exact multiple of the station count, i.e. a whole number of ring "
            "orbits.  Both sides are detector selections under the declared "
            "tail-ladder contract, not least periods and not a complete "
            "period census",
            {"periods": b3_periods, "stations": B3_STATIONS,
             "orbits": [period // B3_STATIONS for period in b3_periods]},
            {"periods": [row["period_ticks"] for row in period_arithmetic],
             "stations": STATIONS,
             "orbits": [row["orbits"] for row in period_arithmetic]},
            "holds when every detector-selected period is a whole multiple of "
            "the station count; magnitude is the number of distinct such "
            "periods",
            bool(b3["every_detected_period_is_whole_orbits"]) and bool(b3_periods),
            every_period_whole_orbits and bool(period_arithmetic),
            len(b3_periods), len(period_arithmetic),
        ))
        b3_joint = b3["pair_clock_information_content"].get("STRICTLY_JOINT", 0)
        b3_pair_clocks = b3["pair_clock_count"]
        b4_joint = domination.get("STRICTLY_JOINT", 0)
        b4_pair_clocks = lane_count * len(BANK_PAIRS)
        comparison.append(compare_row(
            "MOST_PAIR_CLOCKS_ARE_STRICTLY_JOINT",
            "a majority of pair clocks carry information neither of their two "
            "bank clocks carries alone",
            f"{b3_joint}/{b3_pair_clocks}", f"{b4_joint}/{b4_pair_clocks}",
            "holds when the strictly-joint share exceeds 1/2; higher is stronger",
            Fraction(b3_joint, b3_pair_clocks) > Fraction(1, 2),
            Fraction(b4_joint, b4_pair_clocks) > Fraction(1, 2),
            Fraction(b3_joint, b3_pair_clocks),
            Fraction(b4_joint, b4_pair_clocks),
        ))
        comparison.append(compare_row(
            "SATURATED_CLOCKS_ARE_A_NEGLIGIBLE_MINORITY",
            "clocks clean at every remaining chunk boundary are rare, so the "
            "TRIVIAL_SATURATION escape hatch is not carrying the result",
            f"{b3['saturated_pair_clocks'] + b3['saturated_bank_clocks']} of "
            f"{b3_pair_clocks + b3['bank_clock_count']}",
            f"{saturated_pair_clocks + saturated_bank_clocks} of "
            f"{b4_pair_clocks + lane_count * FIXTURE_BANKS}",
            "holds when the saturated share is under 1/10; lower is stronger",
            Fraction(b3["saturated_pair_clocks"] + b3["saturated_bank_clocks"],
                     b3_pair_clocks + b3["bank_clock_count"]) < Fraction(1, 10),
            Fraction(saturated_pair_clocks + saturated_bank_clocks,
                     b4_pair_clocks + lane_count * FIXTURE_BANKS) < Fraction(1, 10),
            Fraction(b3["saturated_pair_clocks"] + b3["saturated_bank_clocks"],
                     b3_pair_clocks + b3["bank_clock_count"]),
            Fraction(saturated_pair_clocks + saturated_bank_clocks,
                     b4_pair_clocks + lane_count * FIXTURE_BANKS),
            higher_is_stronger=False,
        ))
        # Arithmetic consistency of the table itself: every B=3 side was parsed
        # from the cache and every rolled-up B=3 scope re-adds to its parts.
        table_arithmetic_ok = (
            reference_meta.get("parse_complete") is True
            and reference_meta.get("cache_pins_the_worktree_runner") is True
            and reference_meta.get("cache_records_a_clean_run") is True
            and all(
                b3_full[field] == b3_pair[field]
                + b3["scopes"]["SUB_CORPUS_bank_clocks_only"][field]
                for field in ("F1_edges", "F1_nonzero_offset_edges",
                              "F3_factor_edges", "sounding_keys",
                              "keys_outside_any_nontrivial_F1_class")
            )
            and b3["headline_F1_edges_as_published"] == b3_pair["F1_edges"]
            and len(comparison) == 9
            and all(row["B3"] is not None and row["B4"] is not None
                    for row in comparison)
        )
    verdict_labels = Counter(row["verdict"] for row in comparison)

    verdict_block = {
        "within_key_pair_clock_verdict": relation_verdict,
        "headline_substantive_full_dictionary_coverage": (
            f"{substantive_related}/{substantive}"
        ),
        "headline_coverage_fraction": f"{coverage.numerator}/{coverage.denominator}",
        "all_comparable_coverage_including_thin": f"{related}/{comparable}",
        "within_key_member_histogram": pair_totals,
        "within_key_evidence_split": within_pair["evidence_split"],
        "within_key_substantive_nonidentity_full_dictionaries": substantive_nonidentity,
        "within_key_substantive_identity_like_full_dictionaries": substantive_identity,
        "within_key_substantive_partial_matches": substantive_partial,
        "within_key_substantive_nonidentity_partial_matches": (
            substantive_partial_nonidentity
        ),
        "identity_note": IDENTITY_NOTE,
        "detector_selected_nondegenerate_periods": period_arithmetic,
        "every_detected_period_is_whole_orbits": every_period_whole_orbits,
        "period_contract": (
            "each listed period is the declared tail-ladder detector's "
            "SELECTION; proper divisors below the detector's reach may also "
            "be membership-supported; only the divisibility arithmetic and "
            "the direct-membership support of the listed values are claimed, "
            "never a least-period or only-period statement"
        ),
        "whole_orbit_divisibility_decomposition": period_break,
        "terminal_marker_semantics": (
            "the terminal PASS marker certifies measurement and gate "
            "integrity only -- structural well-formedness, witness "
            "re-verification, controls, and table arithmetic -- never a "
            "theorem outcome"
        ),
        "within_key_bank_clock_histogram": within_bank["verdicts"],
        "within_key_bank_clock_substantive_coverage": (
            f"{within_bank['substantive_relations']}/"
            f"{within_bank['substantive_pairs_of_clocks']}"
        ),
        "within_key_bank_clock_nonidentity_full_dictionaries": (
            within_bank["substantive_nonidentity_full_dictionaries"]
        ),
        "across_key_verdict": across_verdict,
        "across_key_headline_scope": "FULL_CORPUS_ALL_TEN_CLOCK_INDICES",
        "across_key_scope_disclosure": (
            "Cycle 875's A4 finding was that the 869 across-key headline quoted "
            "a PAIR-CLOCK sub-corpus.  This block's headline figures below are "
            "the FULL corpus: all six bank-pair clock indices AND all four "
            "single-bank clock indices.  The pair-only and bank-only figures "
            "are emitted alongside, explicitly labelled SUB_CORPUS, and are not "
            "the headline."
        ),
        "across_key_F1_edges_FULL_CORPUS": cross_key_edges,
        "across_key_F1_edges_with_nonzero_offset_FULL_CORPUS": cross_key_nonzero,
        "across_key_F3_factor_edges_FULL_CORPUS": cross_key_factor,
        "across_key_keys_outside_any_nontrivial_F1_class_FULL_CORPUS": (
            unrelated_across
        ),
        "across_key_scopes": across_scopes,
        "pair_clock_information_content": dict(sorted(domination.items())),
        "saturation_note": SATURATION_NOTE,
        "evidence_note": EVIDENCE_NOTE,
        "reading": (
            f"At B=4 ({STATIONS} stations, {lane_count} keys, "
            f"{lane_count * len(BANK_PAIRS)} pair clocks and "
            f"{lane_count * FIXTURE_BANKS} bank clocks), on the {substantive} "
            f"substantive pairs-of-pair-clocks the declared family supplies a "
            f"WHOLE-cadence dictionary for {substantive_related}, of which "
            f"{substantive_nonidentity} move the tick values at all and "
            f"{substantive_identity} are identity-like containment; the "
            f"permissive partial member F3P matches a further "
            f"{substantive_partial} on at least half a clock, "
            f"{substantive_partial_nonidentity} of them non-identity.  On the "
            f"single-bank clocks the dictionary count is "
            f"{within_bank['substantive_relations']} of "
            f"{within_bank['substantive_pairs_of_clocks']}.  Of the "
            f"{lane_count * len(BANK_PAIRS)} pair clocks, "
            f"{domination.get('STRICTLY_JOINT', 0)} carry information neither "
            f"bank clock carries alone, "
            f"{domination.get('ONE_BANK_GATES_THE_PAIR', 0)} are one bank clock "
            f"outright, {domination.get('BOTH_BANK_CLOCKS_IDENTICAL', 0)} are "
            f"both, and {domination.get('SILENT_PAIR', 0)} never sound.  Across "
            f"keys over the FULL corpus, {cross_key_nonzero} of "
            f"{cross_key_edges} constant-offset edges carry a nonzero offset, "
            f"{unrelated_across} of {full_corpus['sounding_keys']} sounding "
            f"keys sit outside any nontrivial class, and {cross_key_factor} "
            f"gap-word factor edges form the F3 layer."
        ),
        "pricing": pricing,
    }
    g_pass = (
        comparable + pair_totals.get("ONE_SIDE_SILENT", 0)
        + pair_totals.get("TRIVIAL_SATURATION", 0)
        == lane_count * len(BANK_PAIRS) * (len(BANK_PAIRS) - 1) // 2
        and related + pair_totals.get("NO_RELATION_IN_F", 0) == comparable
        and substantive_related <= related
        and sum(domination.values()) == lane_count * len(BANK_PAIRS)
        and domination.get("SILENT_PAIR", 0) == empty_pair
        and substantive_related == substantive_nonidentity + substantive_identity
        # The period decomposition must re-add and must agree with its own
        # boolean.  This is arithmetic, not an outcome: the gate is blind to
        # WHETHER the whole-orbit divisibility of detector-selected periods
        # holds.
        and period_break["periods_that_are_whole_orbits"]
        + period_break["periods_that_are_not_whole_orbits"]
        == period_break["distinct_nondegenerate_periods"] == len(period_arithmetic)
        and every_period_whole_orbits
        == (period_break["periods_that_are_not_whole_orbits"] == 0)
        and period_break["clocks_carrying_a_non_orbit_period"]
        + period_break["clocks_carrying_a_whole_orbit_period"]
        == sum(bank_period_hist.values()) + sum(pair_period_hist.values())
    )

    # ------------------------------------------------------------------ controls
    input_shas = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    initial_hasher = sha256()
    for state in states:
        initial_hasher.update(bytes(state))
    replay_equal = all(
        ((plane >> 0) & 1) == ((plane >> duplicate_lane) & 1) for plane in planes
    )
    duplicate_clock_equal = (
        all(
            tuple(duplicate_bank_clocks[bank]) == bank_cadences[0][bank]
            for bank in range(FIXTURE_BANKS)
        )
        and all(
            tuple(duplicate_pair_clocks[index]) == pair_cadences[0][index]
            for index in range(len(BANK_PAIRS))
        )
    )
    runner_sha = sha256(Path(__file__).read_bytes()).hexdigest()
    runtime = time.monotonic() - started

    dumps = {"sort_keys": True, "separators": (",", ":")}
    lines = [
        "SETUP_JSON " + json.dumps(setup, **dumps),
        "QUESTION: the landed second-leg map of the evolution-axis premise "
        "(legacy alias: B-AXIS; Cycle 875) left the ENTIRE B=4 run as its "
        "largest open row.  This runner runs the Cycle-869 declared "
        "clock-relation family, unchanged, on a B=4 probe box declared here "
        "(provenance context: the unlanded exploration referred to as Cycle "
        "866; non-authoritative), and reports which B=3 finite-corpus facts "
        "persist, strengthen or break.",
        "FAMILY_DECLARED :: " + json.dumps(list(FAMILY), **dumps),
        "FAMILY_CLOSURE: " + FAMILY_CLOSURE,
        "DISCLOSED_DEVIATIONS :: " + json.dumps(list(DISCLOSED_DEVIATIONS), **dumps),
        "PASS A_SUBSTRATE :: " + json.dumps({
            "structural_checks": True,
            "per_bank_watched_disjoint": True,
            "source_pointer_outside_bank_sets": True,
            "watched_coordinates_per_bank": local_wire_count,
            "stations_from_cycle719_geometry": len(program),
            "placements_from_separation_rule": len(placements),
            "initial_census_sha256": initial_hasher.hexdigest(),
        }, **dumps),
        ("PASS" if b_pass else "FAIL") + " B_CLOCKS :: " + json.dumps({
            "bank_clock_count": lane_count * FIXTURE_BANKS,
            "pair_clock_count": lane_count * len(BANK_PAIRS),
            "bank_clean_occurrences": bank_clean_totals,
            "pair_clean_occurrences": pair_clean_totals,
            "total_clock_events": sum(bank_clean_totals) + sum(pair_clean_totals),
            "silent_bank_clocks": empty_bank,
            "silent_pair_clocks": empty_pair,
            "bank_clock_length_bands": bank_length_bands,
            "pair_clock_length_bands": pair_length_bands,
            "longest_clock_events": max(
                [len(row) for lane in bank_cadences for row in lane]
                + [len(row) for lane in pair_cadences for row in lane]
            ),
            "eventually_periodic_bank_clocks": periodic_bank_clocks,
            "eventually_periodic_pair_clocks": periodic_pair_clocks,
            "saturated_bank_clocks": saturated_bank_clocks,
            "saturated_pair_clocks": saturated_pair_clocks,
            "silent_and_saturated_overlap": silent_and_saturated,
            "nondegenerate_bank_period_histogram": bank_period_hist,
            "nondegenerate_pair_period_histogram": pair_period_hist,
            "saturation_note": SATURATION_NOTE,
            "pair_clock_information_content": dict(sorted(domination.items())),
            "pair_clock_is_bank_clock_intersection_failures": intersection_failures,
            "monotonicity_failures": monotone_failures,
            "out_of_horizon_failures": horizon_failures,
            "store_cap_saturations": store_saturations,
            "clocks_that_866_nominal_store_cap_would_truncate": clocks_over_866_cap,
            "events_that_866_nominal_store_cap_would_discard": events_lost_at_866_cap,
            "corpus_sha256": corpus_digest,
            "verbatim_samples": sample_rows,
        }, **dumps),
        ("PASS" if controls_pass else "FAIL") + " C_FAMILY_CONTROLS :: "
        + json.dumps({
            "meaning": (
                "Positive controls build synthetic images under each family "
                "member and require acceptance with a witness that re-derives "
                "the image exactly.  Negative controls require refusal of a "
                "one-tick perturbation that manufactures two gap values absent "
                "from the source, and refusal of a triangular-index thinning.  "
                "A further control gates the binary-search tick index against "
                "the dict it replaces.  These gate the tests themselves, not "
                "the outcome."
            ),
            "constructible_negative_controls": {
                "one_tick_perturbation": sum(
                    1 for row in control_rows
                    if "negative_one_tick_perturbation_refused_by_exact_members" in row
                ),
                "tail_edit": sum(
                    1 for row in control_rows
                    if "negative_tail_edit_refused_by_F4" in row
                ),
                "triangular_thinning": sum(
                    1 for row in control_rows
                    if "negative_triangular_thinning_refused" in row
                ),
            },
            "clause_probe_inventory": control_inventory,
            "rows": control_rows,
        }, **dumps),
        ("PASS" if d_pass else "FAIL") + " D_WITHIN_KEY_PAIR_OF_PAIRS :: "
        + json.dumps({
            "scope": f"the {len(BANK_PAIRS)} pair clocks of each key, compared "
                     f"pairwise ({len(BANK_PAIRS) * (len(BANK_PAIRS) - 1) // 2} "
                     f"comparisons per key)",
            "code_legend": {
                "1": "F1", "w": "F1W", "2": "F2A/F2B", "3": "F3", "4": "F4",
                "p": "F3P partial", "x": "NO_RELATION_IN_F",
                "0": "one side silent",
                "s": "TRIVIAL_SATURATION (both clocks clean at every tick)",
            },
            "direction_note": (
                "Each unordered pair of clocks is searched forward and, if that "
                "refuses, reversed; the witness records which direction held."
            ),
            "evidence_note": EVIDENCE_NOTE,
            "identity_note": IDENTITY_NOTE,
            **within_pair,
        }, **dumps),
        ("PASS" if d_pass else "FAIL") + " E_WITHIN_KEY_BANK_CLOCKS :: "
        + json.dumps({
            "scope": f"the {FIXTURE_BANKS} single-bank clocks of each key, "
                     f"compared pairwise",
            **within_bank,
        }, **dumps),
        ("PASS" if e_pass else "FAIL") + " F_ACROSS_KEYS :: " + json.dumps({
            "scope": "one clock index at a time, all keys compared; the "
                     "FULL_CORPUS roll-up is the headline scope",
            "scopes": across_scopes,
            "pair_clocks": across_pair,
            "bank_clocks": across_bank,
            "rep_cap_hits": pair_cap_hits + bank_cap_hits,
        }, **dumps),
        ("PASS" if g_pass else "FAIL") + " G_RELATION_VERDICT :: "
        + json.dumps(verdict_block, **dumps),
        ("PASS" if table_arithmetic_ok else "FAIL") + " H_B_DEPENDENCE :: "
        + json.dumps({
            "meaning": (
                "The B=3 side of every row is PARSED from the sha-pinned "
                "Cycle-869 runner cache, not quoted as a literal.  The verdict "
                "column is DATA computed by the stated rule from the two "
                "measured sides; this gate tests only that the table is "
                "complete and arithmetically consistent.  A row reading "
                "BREAKS_AT_B4 does not move this gate."
            ),
            "reference": reference_meta,
            "b3_scope_rollups": None if b3 is None else b3["scopes"],
            "b3_across_key_headline_scope_recomputed": reference_meta.get(
                "headline_scope_recomputed"
            ),
            "verdict_label_histogram": dict(sorted(verdict_labels.items())),
            "rows": comparison,
        }, **dumps),
    ]
    # N5 execution certificate: one substantive line per resolution class for
    # the negative content that ships (the within-key family-priced refusals
    # at declared caps).  These lines are load-bearing for the note's No-Go
    # Discipline record and must state what was tested at each resolution.
    lines.append(
        "N5_RESOLUTION_CERTIFICATE (scope: the within-key family-priced "
        "refusals at declared caps; no wider negative is certified):"
    )
    lines.append(
        f"per_element: all {sum(within_pair['verdicts'].values())} "
        f"pair-of-pair and {sum(within_bank['verdicts'].values())} bank-clock "
        f"within-key comparisons carry an explicit per-comparison disposition "
        f"(full code tables emitted in D/E); every refusal is "
        f"NO_RELATION_IN_F priced to the declared family and caps, never an "
        f"absence claim; {substantive_related} substantive whole-cadence "
        f"dictionaries and {substantive_partial} partial matches are stated "
        f"up front with witnesses"
    )
    lines.append(
        f"per_site: per-clock census: {lane_count * FIXTURE_BANKS} bank "
        f"clocks ({empty_bank} silent, {saturated_bank_clocks} saturated) and "
        f"{lane_count * len(BANK_PAIRS)} pair clocks ({empty_pair} silent, "
        f"{saturated_pair_clocks} saturated); saturation is exact and "
        f"cap-free; per-clock periods are detector-selected only"
    )
    lines.append(
        f"per_mode: per family member (pair clocks): "
        f"{json.dumps(dict(sorted(pair_totals.items())), **dumps)}; bank "
        f"clocks: {json.dumps(dict(sorted(within_bank['verdicts'].items())), **dumps)}; "
        f"every found witness re-verified against the member's complete "
        f"declared contract; members outside F are NOT tested at this "
        f"resolution -- the refusals say nothing about them"
    )
    lines.append(
        f"per_block: per-key disposition codes for all {lane_count} census "
        f"keys emitted in full; across-key structure emitted per clock index "
        f"({len(BANK_PAIRS)} pair + {FIXTURE_BANKS} bank blocks) at "
        f"FULL_CORPUS and both sub-corpus scopes"
    )
    lines.append(
        f"lattice_wide: corpus totals: "
        f"{sum(bank_clean_totals) + sum(pair_clean_totals)} clock events; "
        f"{cross_key_nonzero}/{cross_key_edges} nonzero constant-offset "
        f"edges; {unrelated_across} of {full_corpus['sounding_keys']} "
        f"sounding keys outside any nontrivial class; NO lattice-wide "
        f"negative is claimed -- the within-key refusals remain priced to "
        f"the declared family, caps and horizon {HORIZON_CHUNKS}, and "
        f"transformations outside that box are untested at every resolution"
    )
    i_core = {
        "audit_input_paths_literal": list(AUDIT_INPUT_PATHS),
        "audit_input_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "audit_input_paths_repo_relative": all(
            not Path(path).is_absolute() for path in AUDIT_INPUT_PATHS
        ),
        "input_shas": input_shas,
        "runner_sha256": runner_sha,
        "initial_census_sha256": initial_hasher.hexdigest(),
        "corpus_sha256": corpus_digest,
        "duplicate_lane_clean_mismatches": duplicate_mismatches,
        "duplicate_final_state_equal": replay_equal,
        "duplicate_clock_stable": duplicate_clock_equal,
        "runtime_seconds": round(runtime, 3),
        "runtime_under_1400s": runtime < RUNTIME_LIMIT_SECONDS,
    }
    i_prepass = (
        i_core["audit_input_paths_exist"]
        and i_core["audit_input_paths_repo_relative"]
        and duplicate_mismatches == 0
        and replay_equal
        and duplicate_clock_equal
        and runtime < RUNTIME_LIMIT_SECONDS
    )
    verdicts = (b_pass, controls_pass, d_pass, e_pass, g_pass, table_arithmetic_ok)
    stdout_bytes = 0
    for _ in range(4):
        i_core["stdout_bytes"] = stdout_bytes
        i_core["stdout_under_150KB"] = (
            stdout_bytes < STDOUT_LIMIT_BYTES if stdout_bytes else True
        )
        i_line = (
            ("PASS" if i_prepass and i_core["stdout_under_150KB"] else "FAIL")
            + " I_CONTROLS :: " + json.dumps(i_core, **dumps)
        )
        stdout_bytes = len(
            ("\n".join(lines + [i_line, "CYCLE879_B4_CLOCK_RELATION_PASS"]) + "\n")
            .encode()
        )
    i_core["stdout_bytes"] = stdout_bytes
    i_core["stdout_under_150KB"] = stdout_bytes < STDOUT_LIMIT_BYTES
    i_pass = i_prepass and i_core["stdout_under_150KB"]
    i_line = ("PASS" if i_pass else "FAIL") + " I_CONTROLS :: " + json.dumps(
        i_core, **dumps
    )
    final = (
        "CYCLE879_B4_CLOCK_RELATION_PASS" if all(verdicts) and i_pass
        else "CYCLE879_B4_CLOCK_RELATION_HONEST_FAIL"
    )
    print("\n".join(lines + [i_line, final]))
    return 0 if all(verdicts) and i_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
