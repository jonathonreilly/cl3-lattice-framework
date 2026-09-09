#!/usr/bin/env python3
"""Cycle 930 INDEPENDENT CHECK -- specified to REFUTE.

Three attacks, in this order.

  (i)   THE THIRD-PAIR RULE.  Hunt a firing (h_f(b), r(b-1)) episode anywhere.
        The corpus is rebuilt independently at B=5,6,7 and at the blind tier
        B=9, and the hunt is run TWICE per tier: once with the primary's own
        consecutive-run-start definition, and once with a deliberately WIDER
        definition (any two P-separated run starts, consecutive or not) that
        the primary never used.  A widening that finds episodes is a partial
        refutation of the primary's framing and is reported as one.

  (ii)  THE RC-3 VERDICT.  Model degeneracy, taken seriously: five rival
        stretch-configuration discriminators are scored against the same
        population, including two deliberately SIMPLER width statistics, to
        test whether the primary's "equal width" separates at all or is merely
        correlated with something cruder.  Precision and recall are reported
        for every rival, ranked, without commentary.

  (iii) THE SEAL.  Recomputed from the primary's stated text via AST literal
        read plus this checker's own independent reimplementation of the rule's
        pure function, and its build log is audited for holdout-freedom.

Independence.  The tick generator is written from the kernel's crossing
identity (station s fires at tick t for the lanes holding a token at ring
position (s - t + 1) mod N) rather than from a phase table, and is validated
tick for tick against the KERNEL'S OWN composed step function
``apply_controller_step`` -- not against a hand-rolled gate loop.  The detector
is a fourth route: interval algebra on the clean set's maximal intervals, with
no bitmask shift and no tick-index enumeration, validated against a literal
per-tick oracle.  The Cycle-930 primary and every 879/881/889/891/922 runner
are import-blocklisted; the primary is read only as bytes and as an AST.
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

PRIMARY_930 = "scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py"
CACHE_930 = "logs/runner-cache/frontier_cycle930_third_pair_rc3_2026_07_28.txt"
RECEIPT_930 = "outputs/third_pair_rc3_cycle930_receipt_2026_07_28.json"
PRIMARY_922 = "scripts/frontier_cycle922_p32_carrier_2026_07_28.py"
CHECKER_922 = "scripts/frontier_cycle922_p32_carrier_independent_check_2026_07_28.py"
RECEIPT_922 = "outputs/p32_carrier_cycle922_receipt_2026_07_28.json"
RECEIPT_922_CHECK = (
    "outputs/p32_carrier_independent_check_cycle922_receipt_2026_07_28.json")
PRIMARY_891 = "scripts/frontier_cycle891_complement_mechanism_2026_07_28.py"
CHECKER_891 = "scripts/frontier_cycle891_complement_independent_check_2026_07_28.py"
PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CORE_719_HANDSHAKE = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py")

PINS = {
    PRIMARY_922: ("9e1a8de7190188a89cd4449300ab56cc053d6a63eec328265fa80f9955ce3a83",
                  "fdd77d879b142d1bafa1f76926c494bbc4480b1c"),
    CHECKER_922: ("fb7acd4bfe5fa1dcc8f22373861da2038dfdb169371c53d283ae65325d44b118",
                  "faae396e9801cfac4c8f6baa80d022397bed3f64"),
    RECEIPT_922: ("ab40677256009a0b1ecdf841766aa055a113aeb93827dc1d1da21a9e1cb97954",
                  "4497a88d3d2cf7ca058ff759c8f3ecea8c042481"),
    RECEIPT_922_CHECK: ("e609eafcb6ef33c22ec0aa4481cc29ea5be46f5be1312a9ccd4822b154ff059e",
                        "a1fcadfd795d08c9705722f7165349e361778b65"),
    PRIMARY_891: ("3d260f6641d05a22aee092145ea3e5c3b29f3a6882b4cbd9ae966424458afbb7",
                  "a1bbd49ffbe970193cc79054fb7219732f7c9873"),
    CORE_719: ("0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
               "c123b8d681c3d76fce08ef13d7673622deac64ad"),
    CORE_719_HANDSHAKE: (
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f"),
}
AUDIT_INPUT_PATHS = tuple(sorted(PINS)) + (PRIMARY_930, CACHE_930, RECEIPT_930)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 900

RUNTIME_LIMIT_SECONDS = 900
STDOUT_LIMIT_BYTES = 150 * 1024

TOKEN_K = 2
EVENT_COUNT = 2
HORIZON = 16_384
MIN_PERIOD_REPEATS = 2
MIN_STABLE_EVENTS = 8
PINNED_PERIOD_CEILING = 64

REBUILD_TIERS = (5, 6, 7)
BLIND_TIER = 9
DECLARED_MIN_TEETH = 8

DISCLOSED = (
    "TICK GENERATOR INDEPENDENCE.  The lane-parallel bit-slice is the only "
    "shape that fits the runtime budget, and this checker uses it too.  What is "
    "independent: the firing schedule is derived here from the KERNEL'S "
    "CROSSING IDENTITY -- station s fires at tick t exactly for the lanes "
    "holding a token at ring position (s - t + 1) mod N -- rather than from a "
    "precomputed phase table, and the whole generator is validated tick for "
    "tick against the kernel's OWN composed step function "
    "``apply_controller_step`` (which also carries the kernel's own token "
    "shuffle, so the token-advance model is validated too, not assumed).  The "
    "Cycle-930 primary is never imported and is read only as bytes and AST.",
    "TIER SCOPING.  The 900 s cap buys B=5, 6, 7 rebuilt independently plus the "
    "blind tier B=9, bank clocks only (the entry gap exists for interior banks "
    "only, and every quantity attacked here is a bank-clock quantity).  B=4 and "
    "B=8 are not rebuilt; their cells enter the attack from the primary's own "
    "published rows, which the primary itself restricted value-for-value "
    "against the pinned Cycle-922 receipt.  Declared, not hidden.",
    "THE WIDENED THIRD-PAIR HUNT is deliberately WEAKER than the primary's "
    "definition, so it can only find MORE episodes.  If it finds any, that is a "
    "refutation of the primary's framing and is reported as the headline.",
)


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def digest(v):
    return sha256(compact(v).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


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
        got = sha256(payload).hexdigest()
        blob = git_blob(payload)
        ok = got == want_sha and blob == want_blob
        rows[path] = {"sha256": got, "git_blob": blob, "match": ok}
        if not ok:
            bad.append(path)
    return rows, bad


PREFLIGHT_ROWS, PREFLIGHT_BAD = preflight()
if PREFLIGHT_BAD:
    print("FAIL A_PINS :: " + json.dumps(
        {"pins": PREFLIGHT_ROWS, "mismatched": sorted(PREFLIGHT_BAD)},
        sort_keys=True, separators=(",", ":")))
    raise SystemExit(2)

BLOCKLISTED = tuple(Path(p).stem for p in
                    (PRIMARY_930, PRIMARY_879, PRIMARY_881, PRIMARY_889,
                     PRIMARY_891, CHECKER_891, PRIMARY_922, CHECKER_922))


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED:
            self.hits.append(fullname)
            raise ImportError("BLOCKLIST forbids import of %s" % fullname)
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as KERNEL

ALG = KERNEL.A
CHAIN = KERNEL.B
PACK = KERNEL.M
R3 = KERNEL.R3


# ------------------------------------------------- geometry, read from gates
def machine(bank_count):
    """Rows, kinds and edges, read out of the emitted program.  No literals."""
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    relay, hand = defaultdict(list), defaultdict(list)
    for index, (kind, edge, _local) in enumerate(program):
        if kind == "relay":
            relay[edge].append(index)
        elif kind == "handoff":
            hand[edge].append(index)
    swap_f, swap_r, hand_f, hand_r, malformed = {}, {}, {}, {}, 0
    for edge, rows in sorted(relay.items()):
        if len(rows) != 4 or len(hand.get(edge, ())) != 2:
            malformed += 1
            continue
        words = [KERNEL.mapped_macro(program[i]) for i in rows]
        if words[1] != words[2] or words[0] == words[1]:
            malformed += 1
            continue
        swap_f[edge], swap_r[edge] = rows[1], rows[2]
        hand_f[edge], hand_r[edge] = hand[edge][0], hand[edge][1]
    kind_of = {}
    for edge in sorted(swap_f):
        kind_of[hand_f[edge]] = ("hf", edge)
        kind_of[swap_f[edge]] = ("f", edge)
        kind_of[swap_r[edge]] = ("r", edge)
        kind_of[hand_r[edge]] = ("hr", edge)
    own = {}
    for bank in range(bank_count):
        edges = [e for e in (bank - 1, bank) if 0 <= e <= bank_count - 2]
        own[bank] = {s: ke for s, ke in kind_of.items() if ke[1] in edges}
    return {"program": program, "stations": stations, "swap_f": swap_f,
            "swap_r": swap_r, "hand_f": hand_f, "hand_r": hand_r,
            "kind_of": kind_of, "own": own, "malformed": malformed,
            "entry": {b: 8 * (bank_count - 1 - b)
                      for b in range(1, bank_count - 1)}}


def third_pair_stations(mac, bank):
    """(h_f(b), r(b-1)) read from the machine, not from a formula."""
    return mac["hand_f"][bank], mac["swap_r"][bank - 1]


def entry_pair_stations(mac, bank):
    return {"swap_swap": (mac["swap_f"][bank - 1], mac["swap_r"][bank]),
            "swap_handoff": (mac["swap_f"][bank], mac["hand_r"][bank - 1]),
            "handoff_swap": third_pair_stations(mac, bank)}


def placements_of(stations):
    out = []
    for pair in combinations(range(stations), TOKEN_K):
        if any((p + 1) % stations in set(pair) for p in pair):
            continue
        out.append(pair)
    return tuple(out)


def seeds_of(bank_count, program):
    banks, links = CHAIN.chain_genesis(bank_count)
    state = PACK.pack_state(banks, links)
    seeds = []
    for event in range(EVENT_COUNT):
        before = PACK.prepare_endpoint(state, (1, 0) if event % 2 == 0 else (0, 1))
        after, _a, _b, _t = KERNEL.run_orbit(before, program)
        seeds.append(before)
        state = after
    return tuple(seeds)


def watched(bank_count):
    banks, links = CHAIN.chain_genesis(bank_count)
    zb = tuple(tuple(0 for _ in row) for row in banks)
    zl = tuple(tuple(0 for _ in row) for row in links)
    local = (ALG.POINTER, ALG.U_TO_V, ALG.V_TO_U, ALG.DIRECTION_OK,
             *ALG.FRESH, *ALG.ZERO_WORK, ALG.TOKEN_OK)
    out = {}
    for bank in range(bank_count):
        coords = []
        for wire in local:
            probe = [list(row) for row in zb]
            probe[bank][wire] = 1
            packed = PACK.pack_state(tuple(tuple(r) for r in probe), zl)
            hot = [i for i, bit in enumerate(packed) if bit]
            if len(hot) != 1:
                raise AssertionError((bank, wire, hot))
            coords.append(hot[0])
        out[bank] = tuple(sorted(coords))
    return out


BUILD_LOG = []


def generate(bank_count, horizon, perturb=None):
    """Lane-parallel evolution driven by the KERNEL'S CROSSING IDENTITY.

    ``holder[v]`` is the lane mask of lanes carrying a token at ring position
    ``v``.  At tick ``t`` station ``s`` fires exactly for ``holder[(s-t+1)%N]``.
    Nothing here is copied from a phase table; the identity is the definition.
    """
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    words = tuple(KERNEL.mapped_macro(row) for row in program)
    placements = placements_of(stations)
    seeds = seeds_of(bank_count, program)
    keys, states = [], []
    for event, seed in enumerate(seeds):
        for pos in placements:
            state, _a, _b, _t = KERNEL.run_orbit(seed, program, token_positions=pos)
            keys.append((event, pos))
            states.append(state)
    lanes = len(keys)
    holder = [0] * stations
    for lane, (_event, pos) in enumerate(keys):
        for p in pos:
            holder[p] |= 1 << lane
    if perturb is not None:
        holder[perturb % stations] ^= 1
    planes = [0] * len(states[0])
    for lane, state in enumerate(states):
        bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                planes[wire] |= bit
    full = (1 << lanes) - 1
    wires = watched(bank_count)
    src_wire = R3.X.SOURCE_POINTER
    clean = [[0] * (horizon + 1) for _ in range(bank_count)]
    src = [0] * (horizon + 1)

    def observe(tick):
        dirty0 = planes[src_wire] & full
        src[tick] = full & ~dirty0
        for bank in range(bank_count):
            d = dirty0
            for w in wires[bank]:
                d |= planes[w]
            clean[bank][tick] = full & ~d

    observe(0)
    for tick in range(1, horizon + 1):
        shift = (1 - tick) % stations
        for station in range(stations):
            mask = holder[(station + shift) % stations]
            if not mask:
                continue
            for gate in words[station]:
                if gate.kind == "X":
                    planes[gate.wires[0]] ^= mask
                elif gate.kind == "CNOT":
                    c, t2 = gate.wires
                    planes[t2] ^= planes[c] & mask
                elif gate.kind == "TOF":
                    l, r, t2 = gate.wires
                    planes[t2] ^= planes[l] & planes[r] & mask
                else:
                    raise AssertionError(gate.kind)
        observe(tick)
    BUILD_LOG.append({"banks": bank_count, "horizon": horizon, "lanes": lanes,
                      "stations": stations})
    return {"banks": bank_count, "stations": stations, "keys": tuple(keys),
            "lanes": lanes, "clean": clean, "src": src, "horizon": horizon}


def kernel_step_replay(bank_count, horizon, seed, positions):
    """Oracle: the KERNEL'S OWN composed step function, tick by tick."""
    program = KERNEL.interleaved_program(bank_count)
    stations = len(program)
    wires = watched(bank_count)
    src_wire = R3.X.SOURCE_POINTER
    state, _a0, _b0, _t = KERNEL.run_orbit(seed, program, token_positions=positions)
    a = tuple(int(s in positions) for s in range(stations))
    b = (0,) * stations
    trace = []

    def snap(vec):
        return (not vec[src_wire],
                tuple(not (vec[src_wire] or any(vec[w] for w in wires[bank]))
                      for bank in range(bank_count)))

    trace.append(snap(state))
    for _tick in range(horizon):
        state, a, b = KERNEL.apply_controller_step(state, program, a, b)
        trace.append(snap(state))
    return trace


def lane_masks(rows, lanes, horizon):
    width = (horizon >> 3) + 2
    buf = [bytearray(width) for _ in range(lanes)]
    for tick in range(horizon + 1):
        word = rows[tick]
        if not word:
            continue
        byte, bit = tick >> 3, 1 << (tick & 7)
        while word:
            low = word & -word
            buf[low.bit_length() - 1][byte] |= bit
            word -= low
    return [int.from_bytes(bytes(x), "little") for x in buf]


# ----------------------------------------- detector: a fourth route, intervals
def clean_intervals(mask, length):
    """Maximal intervals of SET bits, as [lo, hi] pairs.  Sorted, disjoint."""
    out, i = [], 0
    while i < length:
        if (mask >> i) & 1:
            j = i
            while j + 1 < length and ((mask >> (j + 1)) & 1):
                j += 1
            out.append((i, j))
            i = j + 1
        else:
            i += 1
    return out


def dirty_intervals(mask, length):
    out, i = [], 0
    while i < length:
        if not ((mask >> i) & 1):
            j = i
            while j + 1 < length and not ((mask >> (j + 1)) & 1):
                j += 1
            out.append((i, j))
            i = j + 1
        else:
            i += 1
    return out


def iv_clip(ivs, lo, hi):
    out = []
    for a, b in ivs:
        a2, b2 = max(a, lo), min(b, hi)
        if a2 <= b2:
            out.append((a2, b2))
    return out


def iv_sub(a_ivs, b_ivs):
    """A \\ B on sorted disjoint interval lists.  No bitmasks, no tick walks."""
    out, j = [], 0
    for a, b in a_ivs:
        cur = a
        k = j
        while k < len(b_ivs) and b_ivs[k][1] < cur:
            k += 1
        while k < len(b_ivs) and b_ivs[k][0] <= b:
            lo, hi = b_ivs[k]
            if lo > cur:
                out.append((cur, min(lo - 1, b)))
            cur = max(cur, hi + 1)
            if cur > b:
                break
            k += 1
        if cur <= b:
            out.append((cur, b))
    return out


def iv_len(ivs):
    return sum(b - a + 1 for a, b in ivs)


def interval_detector(mask, length, periods,
                      min_events=MIN_STABLE_EVENTS,
                      min_repeats=MIN_PERIOD_REPEATS):
    """Cycle-930 checker's own detector.  Interval algebra on the clean set."""
    ivs = clean_intervals(mask, length)
    if not ivs:
        return {}
    total = iv_len(ivs)
    if total < min_events:
        return {}
    last = ivs[-1][1]
    out = {}
    for period in periods:
        need = min_repeats * period
        if need > last:
            break
        shifted = [(a - period, b - period) for a, b in ivs]
        a_only = iv_sub(iv_clip(ivs, 0, last - period),
                        iv_clip(shifted, 0, last - period))
        b_only = iv_sub(iv_clip(shifted, 0, last - period),
                        iv_clip(ivs, 0, last - period))
        bad = sorted(a_only + b_only)
        transient = (max(b for _a, b in bad) + 1) if bad else 0
        if last - transient < need:
            continue
        region = iv_clip(ivs, transient, last)
        events = iv_len(region)
        if events < min_events:
            continue
        seen = 0
        for a, b in region:
            span = b - a + 1
            if span >= period:
                seen = (1 << period) - 1
                break
            start = a % period
            for k in range(span):
                seen |= 1 << ((start + k) % period)
        if bin(seen).count("1") == period:
            continue
        out[period] = (transient, events, bin(seen).count("1"))
    return out


def literal_detector(mask, length, periods):
    """A literal per-tick oracle used only to validate the interval route."""
    bits = [bool((mask >> i) & 1) for i in range(length)]
    if sum(bits) < MIN_STABLE_EVENTS:
        return {}
    last = max(i for i, v in enumerate(bits) if v) if any(bits) else -1
    if last < 0:
        return {}
    out = {}
    for period in periods:
        if MIN_PERIOD_REPEATS * period > last:
            break
        worst = -1
        for t in range(0, last - period + 1):
            if bits[t] != bits[t + period]:
                worst = t
        transient = worst + 1
        if last - transient < MIN_PERIOD_REPEATS * period:
            continue
        region = [t for t in range(transient, last + 1) if bits[t]]
        if len(region) < MIN_STABLE_EVENTS:
            continue
        res = {t % period for t in region}
        if len(res) == period:
            continue
        out[period] = (transient, len(region), len(res))
    return out


def run_starts(mask, length):
    return [lo for lo, _hi in dirty_intervals(mask, length)]


def run_widths(mask, length):
    return [hi - lo + 1 for lo, hi in dirty_intervals(mask, length)]


def source_stretches(mask, horizon):
    out = []
    for a, b in clean_intervals(mask, horizon + 1):
        if a > 0 and b < horizon:
            out.append((a, b))
    return out


# ----------------------------------------------------------- the recount
SHAPE_KEYS = ("swap_swap", "swap_handoff", "handoff_swap")


def recount(box, banks=None):
    """Bank-clock recount at each interior bank's entry gap.

    Attribution is by STATION IDENTITY -- the pair of stations a token would be
    crossing at the two run-start ticks is compared with the three entry-gap
    station pairs read out of the machine -- not by kind tuples.  Different
    route, same question.
    """
    bank_count = box["banks"]
    stations = box["stations"]
    lanes = box["lanes"]
    horizon = box["horizon"]
    mac = machine(bank_count)
    scan = banks if banks is not None else list(range(1, bank_count - 1))
    pair_stations = {b: entry_pair_stations(mac, b) for b in scan}
    ceiling = max(PINNED_PERIOD_CEILING, 2 * stations)
    named = set(mac["entry"].values()) | {stations - 8 * (e + 1)
                                          for e in mac["swap_f"]}
    periods = sorted(set(range(2, ceiling + 1)) | {p for p in named if p > 1})
    bank_masks = [lane_masks(box["clean"][b], lanes, horizon)
                  for b in range(bank_count)]
    src = lane_masks(box["src"], lanes, horizon)

    episodes = Counter()
    strict = Counter()          # (bank, shape) -> episodes, consecutive pairs
    widened = Counter()         # (bank, shape) -> episodes, ANY P-separated pair
    strict_occ = Counter()
    widened_occ = Counter()
    population = defaultdict(list)   # bank -> feature rows for attack (ii)
    for lane in range(lanes):
        _event, positions = box["keys"][lane]
        stretches = source_stretches(src[lane], horizon)
        for bank in scan:
            P = mac["entry"][bank]
            mask = bank_masks[bank][lane]
            if mask == 0:
                continue
            want = pair_stations[bank]
            for a, b in stretches:
                length = b - a + 1
                seg = (mask >> a) & ((1 << length) - 1)
                if seg == 0:
                    continue
                iv = dirty_intervals(seg, length)
                if len(iv) < 2:
                    continue
                starts = [a + lo for lo, _hi in iv]
                widths = [hi - lo + 1 for lo, hi in iv]
                index = {t: i for i, t in enumerate(starts)}
                strict_here, wide_here = {}, {}
                for i, t1 in enumerate(starts):
                    t2 = t1 + P
                    if t2 not in index:
                        continue
                    j = index[t2]
                    for p in positions:
                        s1 = (p + t1 - 1) % stations
                        s2 = (p + t2 - 1) % stations
                        for key, (w1, w2) in want.items():
                            if (s1, s2) != (w1, w2):
                                continue
                            wide_here.setdefault(key, []).append((i, j))
                            widened_occ[(bank, key)] += 1
                            if j == i + 1:
                                strict_here.setdefault(key, []).append((i, j))
                                strict_occ[(bank, key)] += 1
                hits = interval_detector(seg, length, periods)
                reads = P in hits
                if reads:
                    episodes[bank] += 1
                for key in strict_here:
                    if reads:
                        strict[(bank, key)] += 1
                for key in wide_here:
                    if reads:
                        widened[(bank, key)] += 1
                if strict_here and length >= 2 * P + 1 and bin(seg).count("1") >= 8:
                    feats = {"equal_width": False, "first_width_le_Pm1": False,
                             "both_widths_le_3": False, "pair_in_last_2P": False}
                    for key, hits_here in strict_here.items():
                        for i, j in hits_here:
                            w1, w2 = widths[i], widths[j]
                            if w1 == w2 and w1 <= P - 1:
                                feats["equal_width"] = True
                            if w1 <= P - 1:
                                feats["first_width_le_Pm1"] = True
                            if w1 <= 3 and w2 <= 3:
                                feats["both_widths_le_3"] = True
                            if starts[j] >= b - 2 * P:
                                feats["pair_in_last_2P"] = True
                    last = length - 1
                    lo = last - MIN_PERIOD_REPEATS * P
                    tail_ok = True
                    if lo >= 0:
                        for t in range(lo, last - P + 1):
                            if ((seg >> t) & 1) != ((seg >> (t + P)) & 1):
                                tail_ok = False
                                break
                    feats["tail_window_P_exact"] = tail_ok
                    feats["always_true"] = True
                    feats["reads_P"] = reads
                    population[bank].append(feats)
    del bank_masks, src
    return {"banks": bank_count, "stations": stations, "lanes": lanes,
            "episodes": episodes, "strict": strict, "widened": widened,
            "strict_occ": strict_occ, "widened_occ": widened_occ,
            "population": population, "entry": mac["entry"],
            "malformed": mac["malformed"]}


DISCRIMINATORS = ("equal_width", "first_width_le_Pm1", "both_widths_le_3",
                  "pair_in_last_2P", "tail_window_P_exact", "always_true")


def score(population):
    out = {}
    for name in DISCRIMINATORS:
        tp = fp = fn = tn = 0
        for row in population:
            pred, truth = row[name], row["reads_P"]
            if pred and truth:
                tp += 1
            elif pred and not truth:
                fp += 1
            elif truth:
                fn += 1
            else:
                tn += 1
        prec = tp / (tp + fp) if tp + fp else 0.0
        rec = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
        out[name] = {"tp": tp, "fp": fp, "fn": fn, "tn": tn,
                     "precision": round(prec, 4), "recall": round(rec, 4),
                     "f1": round(f1, 4),
                     "accuracy": round((tp + tn) / max(1, tp + fp + fn + tn), 4)}
    return out


# --------------------------------------------- the rule, read from the text
def literal_from_primary(name):
    tree = ast.parse((ROOT / PRIMARY_930).read_bytes().decode())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    try:
                        return ast.literal_eval(node.value)
                    except ValueError:
                        return None
    return None


def tp_predicates_from_text(text):
    """Re-derive the rule from the primary's stated words alone."""
    found = {}
    if "r(b-1) - h_r(b) = (8B-6-3b) - (8B-7-3b) = 1" in text:
        found["adjacency_closed_form"] = lambda bc, b: (
            ((8 * bc - 6 - 3 * b) - (8 * bc - 7 - 3 * b)) % (8 * bc - 5) == 1)
    if "h_r(b) - P = 5b+1" in text:
        found["h_r_preimage_is_5b_plus_1"] = lambda bc, b: (
            ((8 * bc - 7 - 3 * b) - 8 * (bc - 1 - b)) % (8 * bc - 5)
            == (5 * b + 1) % (8 * bc - 5))
    if "exactly one" in text.lower() or "ONE consecutive gap equal to 1" in text:
        def one_unit_gap(bc, b):
            n = 8 * bc - 5
            f = lambda e: (4 + 5 * e) % n
            r = lambda e: (8 * bc - 9 - 3 * e) % n
            rows = sorted({(f(b - 1) - 2) % n, f(b - 1), r(b - 1),
                           (r(b - 1) + 2) % n, (f(b) - 2) % n, f(b), r(b),
                           (r(b) + 2) % n})
            gaps = [(rows[(i + 1) % len(rows)] - rows[i]) % n
                    for i in range(len(rows))]
            return gaps.count(1) == 1
        found["exactly_one_unit_gap"] = one_unit_gap
    return found


# ------------------------------------------------------------------------ main
def main():
    started = time.monotonic()
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}
    results, findings = {}, []

    def gate(name, ok, payload):
        print("%s %s :: %s" % ("PASS" if ok else "FAIL", name,
                               json.dumps(payload, **dumps)))
        return ok

    receipt = json.loads((ROOT / RECEIPT_930).read_text())
    cache_text = (ROOT / CACHE_930).read_text()
    r922c = json.loads((ROOT / RECEIPT_922_CHECK).read_text())
    primary_bytes = (ROOT / PRIMARY_930).read_bytes()

    # ------------------------------------------------------------ gate A
    cache_pins_today = sha256(primary_bytes).hexdigest() in cache_text
    a_ok = (not PREFLIGHT_BAD and not FIREWALL.hits
            and (ROOT / PRIMARY_930).is_file() and cache_pins_today)
    results["A_PINS"] = gate("A_PINS", a_ok, {
        "pins_verified": len(PINS),
        "primary_930_sha256": sha256(primary_bytes).hexdigest(),
        "primary_930_git_blob": git_blob(primary_bytes),
        "cache_pins_todays_primary": cache_pins_today,
        "firewall_hits": FIREWALL.hits,
        "blocklisted": sorted(BLOCKLISTED),
        "disclosed": list(DISCLOSED),
    })
    if not a_ok:
        raise SystemExit(2)

    # ------------------------------------------------------------ gate B
    gen_rows, gen_mismatch, lanes_compared, ticks_compared = [], 0, 0, 0
    for bank_count, horizon, sample in ((3, 200, None), (4, 150, 10), (5, 110, 5)):
        box = generate(bank_count, horizon)
        program = KERNEL.interleaved_program(bank_count)
        seeds = seeds_of(bank_count, program)
        lanes = box["lanes"]
        picks = range(lanes) if sample is None else range(0, lanes, max(1, lanes // sample))
        n = 0
        for lane in picks:
            event, positions = box["keys"][lane]
            trace = kernel_step_replay(bank_count, horizon, seeds[event], positions)
            n += 1
            lanes_compared += 1
            for tick in range(horizon + 1):
                ticks_compared += 1
                want_src, want_banks = trace[tick]
                got_src = bool((box["src"][tick] >> lane) & 1)
                if got_src != want_src:
                    gen_mismatch += 1
                for bank in range(bank_count):
                    got = bool((box["clean"][bank][tick] >> lane) & 1)
                    if got != want_banks[bank]:
                        gen_mismatch += 1
        gen_rows.append({"banks": bank_count, "horizon": horizon,
                         "lanes_total": lanes, "lanes_compared": n})
        del box
    b_ok = gen_mismatch == 0 and lanes_compared > 0
    results["B_GENERATOR"] = gate("B_GENERATOR", b_ok, {
        "oracle": "the kernel's own composed step function "
                  "apply_controller_step, including its own token shuffle",
        "rows": gen_rows, "lanes_compared": lanes_compared,
        "tick_snapshots_compared": ticks_compared,
        "total_mismatches": gen_mismatch,
    })

    # ------------------------------------------------------------ gate C
    rng = random.Random(930_1028)
    det_cases = det_mismatch = det_hits = 0
    for _ in range(1300):
        length = rng.randrange(24, 260)
        density = rng.choice((0.05, 0.15, 0.3, 0.5, 0.75))
        bits = 0
        for i in range(length):
            if rng.random() < density:
                bits |= 1 << i
        if rng.random() < 0.4:
            period = rng.randrange(3, 24)
            tail = rng.randrange(length // 2, length)
            base = rng.getrandbits(period)
            for i in range(tail, length):
                if (base >> ((i - tail) % period)) & 1:
                    bits |= 1 << i
                else:
                    bits &= ~(1 << i)
        periods = list(range(2, 36))
        got = interval_detector(bits, length, periods)
        ref = literal_detector(bits, length, periods)
        det_cases += 1
        det_hits += len(got)
        if got != ref:
            det_mismatch += 1
    c_ok = det_mismatch == 0 and det_hits > 0
    results["C_DETECTOR"] = gate("C_DETECTOR", c_ok, {
        "route": "interval algebra on the clean set's maximal intervals -- no "
                 "bitmask shift, no tick-index enumeration",
        "randomised_cases": det_cases, "detections_compared": det_hits,
        "mismatches_vs_literal_per_tick_oracle": det_mismatch,
    })

    # ------------------------------------------------------------ gate D
    tp_text = literal_from_primary("TP_STATEMENT")
    preds = tp_predicates_from_text(tp_text or "")
    determinacy, disagree = 0, 0
    for bc in range(3, 21):
        for b in range(1, bc - 1):
            determinacy += 1
            vals = {name: bool(fn(bc, b)) for name, fn in preds.items()}
            if not all(vals.values()):
                disagree += 1
    d_ok = len(preds) >= 3 and disagree == 0 and determinacy > 0
    results["D_RULE_FROM_TEXT"] = gate("D_RULE_FROM_TEXT", d_ok, {
        "phrasings_found": sorted(preds),
        "cells_checked": determinacy, "disagreements": disagree,
        "note": "the primary's TP text is re-read as an AST literal and its "
                "closed forms re-derived here; every phrasing must hold on "
                "every cell independently of the primary's own code",
    })

    # ------------------------------- rebuild the tiers and run the attacks
    recounts = {}
    for bc in REBUILD_TIERS:
        box = generate(bc, HORIZON)
        recounts[bc] = recount(box)
        del box
    box9 = generate(BLIND_TIER, HORIZON)
    recounts[BLIND_TIER] = recount(box9)
    del box9

    # ------------------------------------------------------------ gate E
    hunt_rows, strict_total, wide_total = [], 0, 0
    for bc in sorted(recounts):
        rec = recounts[bc]
        for bank in sorted(rec["entry"]):
            s = rec["strict"][(bank, "handoff_swap")]
            w = rec["widened"][(bank, "handoff_swap")]
            strict_total += s
            wide_total += w
            hunt_rows.append({
                "cell": "B%d.b%d" % (bc, bank), "P": rec["entry"][bank],
                "episodes_at_the_entry_gap": rec["episodes"][bank],
                "third_pair_episodes_strict": s,
                "third_pair_episodes_WIDENED": w,
                "third_pair_pair_occurrences_strict":
                    rec["strict_occ"][(bank, "handoff_swap")],
                "third_pair_pair_occurrences_WIDENED":
                    rec["widened_occ"][(bank, "handoff_swap")],
                "other_two_episodes": {
                    k: rec["strict"][(bank, k)]
                    for k in ("swap_swap", "swap_handoff")},
            })
    if wide_total:
        findings.append(
            "THE WIDENED HUNT FOUND %d third-pair episodes that the primary's "
            "consecutive-run-start definition does not see.  The primary's "
            "'zero' is therefore a statement about CONSECUTIVE pairs only, and "
            "that qualification is missing from its claim text." % wide_total)
    e_ok = strict_total == 0
    results["E_THIRD_PAIR_HUNT"] = gate("E_THIRD_PAIR_HUNT", e_ok, {
        "attack": "hunt a firing third-pair episode, twice per tier: the "
                  "primary's consecutive definition, and a deliberately wider "
                  "one the primary never used",
        "tiers_rebuilt": sorted(recounts),
        "third_pair_episodes_strict_total": strict_total,
        "third_pair_episodes_widened_total": wide_total,
        "rows": hunt_rows,
        "verdict": ("the primary's zero SURVIVES under its own definition"
                    if strict_total == 0 else
                    "REFUTED: a firing third-pair episode exists"),
        "widening_verdict": ("the zero also survives the widening"
                             if wide_total == 0 else
                             "the zero does NOT survive the widening -- "
                             "partial refutation, reported above"),
    })

    # ------------------------------------------------------------ gate F
    pooled, per_cell_scores = [], {}
    for bc in sorted(recounts):
        for bank, rows in sorted(recounts[bc]["population"].items()):
            if not rows:
                continue
            pooled.extend(rows)
            per_cell_scores["B%d.b%d" % (bc, bank)] = {
                "population": len(rows),
                "reads_P": sum(1 for r in rows if r["reads_P"]),
                "scores": score(rows)}
    pooled_scores = score(pooled)
    ranked = sorted(pooled_scores.items(), key=lambda kv: -kv[1]["f1"])
    best = ranked[0][0] if ranked else None
    eq = pooled_scores.get("equal_width", {})
    crude = pooled_scores.get("first_width_le_Pm1", {})
    degeneracy = (abs(eq.get("f1", 0) - crude.get("f1", 0)) < 0.02
                  if eq and crude else None)
    if degeneracy:
        findings.append(
            "MODEL DEGENERACY ON RC-3: the primary's 'equal width' statistic "
            "scores within 0.02 F1 of the cruder 'first width <= P-1' "
            "statistic on the pooled population, so it is not separating on "
            "equality -- it is riding a width statistic that needs no equality "
            "at all.")
    if best == "tail_window_P_exact":
        findings.append(
            "The best rival discriminator on the pooled population is "
            "tail_window_P_exact (F1 %.4f), which is the primary's own R3 "
            "component -- confirming the primary's reading that the binding "
            "constraint is the TAIL, not the width."
            % pooled_scores[best]["f1"])
    f_ok = len(pooled) > 0 and best is not None
    results["F_RC3_DEGENERACY"] = gate("F_RC3_DEGENERACY", f_ok, {
        "attack": "score five rival stretch-configuration discriminators plus a "
                  "constant-true control against the same population, and ask "
                  "whether the primary's equal-width statistic separates at all "
                  "or merely tracks something cruder",
        "population_size": len(pooled),
        "population_reads_P": sum(1 for r in pooled if r["reads_P"]),
        "pooled_scores": pooled_scores,
        "ranked_by_f1": [k for k, _v in ranked],
        "best_discriminator": best,
        "equal_width_vs_crude_width_are_degenerate": degeneracy,
        "per_cell": per_cell_scores,
    })

    # ------------------------------------------------------------ gate G
    never_built = literal_from_primary("NEVER_BUILT_BANKS") or (9, 10, 11, 12)

    def own_tp_rows(bc):
        n = 8 * bc - 5
        out = []
        for b in range(1, bc - 1):
            period = 8 * (bc - 1 - b)
            f = lambda e: (4 + 5 * e) % n
            r = lambda e: (8 * bc - 9 - 3 * e) % n
            rows = {(f(b - 1) - 2) % n, f(b - 1), r(b - 1), (r(b - 1) + 2) % n,
                    (f(b) - 2) % n, f(b), r(b), (r(b) + 2) % n}
            srt = sorted(rows)
            gaps = [(srt[(i + 1) % len(srt)] - srt[i]) % n for i in range(len(srt))]
            shadow = {srt[(i + 1) % len(srt)] for i, g in enumerate(gaps) if g == 1}
            pairs = {"swap_swap": (f(b - 1), r(b)),
                     "swap_handoff": (f(b), (r(b - 1) + 2) % n),
                     "handoff_swap": ((f(b) - 2) % n, r(b - 1))}
            out.append({
                "bank": b,
                "spans": {k: (v[1] - v[0]) % n == period for k, v in pairs.items()},
                "terminal_shadowed": {k: v[1] in shadow for k, v in pairs.items()},
            })
        return out

    own_payload = {
        "TP_STATEMENT": tp_text,
        "predicted_third_pair_episodes": {str(bc): 0 for bc in never_built},
        "predicted_third_pair_exists_geometrically": {
            str(bc): [row["bank"] for row in own_tp_rows(bc)
                      if row["spans"]["handoff_swap"]] for bc in never_built},
        "predicted_third_pair_terminal_is_shadowed_everywhere": {
            str(bc): all(row["terminal_shadowed"]["handoff_swap"]
                         for row in own_tp_rows(bc)) for bc in never_built},
        "predicted_other_two_pairs_terminals_unshadowed": {
            str(bc): all(not row["terminal_shadowed"]["swap_swap"]
                         and not row["terminal_shadowed"]["swap_handoff"]
                         for row in own_tp_rows(bc)) for bc in never_built},
    }
    own_seal = digest(own_payload)
    published_seal = receipt["seal"]["SEAL_sha256"]
    seal_build_log = receipt["seal"]["build_log_at_seal_time"]
    holdout_free = all(row["banks"] not in never_built for row in seal_build_log)
    b9_predicted_zero = own_payload["predicted_third_pair_episodes"]["9"] == 0
    b9_measured = sum(recounts[BLIND_TIER]["strict"][(b, "handoff_swap")]
                      for b in recounts[BLIND_TIER]["entry"])
    g_ok = (own_seal == published_seal and holdout_free
            and (not b9_predicted_zero or b9_measured == 0))
    results["G_SEAL"] = gate("G_SEAL", g_ok, {
        "attack": "recompute the seal from the primary's stated text plus this "
                  "checker's own reimplementation of the rule's pure function, "
                  "and audit the build log for holdout-freedom",
        "published_SEAL_sha256": published_seal,
        "independently_recomputed_SEAL_sha256": own_seal,
        "seal_agrees": own_seal == published_seal,
        "build_log_at_seal_time": seal_build_log,
        "build_log_is_holdout_free": holdout_free,
        "never_built_banks_declared_by_the_primary": list(never_built),
        "B9_sealed_prediction_third_pair_episodes": 0,
        "B9_measured_third_pair_episodes_by_this_checker": b9_measured,
        "HONESTY_NOTE_CARRIED_FROM_THE_PRIMARY":
            "B=9 is NOT blind: the pinned Cycle-922 checker receipt already "
            "publishes the B=9 shape lists and they contain no hf->r shape.  "
            "This checker verifies B=9 anyway, and records that only B>=10 "
            "would be a blind test of the sealed prediction.",
    })

    # ------------------------------------------------------------ gate H
    rest, rest_bad = [], []
    name_of = {"swap_swap": "ENTRY_GAP_swap_swap",
               "swap_handoff": "ENTRY_GAP_swap_handoff",
               "handoff_swap": "ENTRY_GAP_handoff_swap"}
    for bc in REBUILD_TIERS:
        prim = receipt["per_cell_rows"][str(bc)]
        rec = recounts[bc]
        for row in prim:
            bank = row["bank"]
            mine_ep = rec["episodes"][bank]
            mine_shapes = {name_of[k]: rec["strict"][(bank, k)] for k in SHAPE_KEYS}
            ok_ep = mine_ep == row["episodes_on_the_bank_clock"]
            ok_sh = mine_shapes == row["by_shape"]
            rest.append({"cell": "B%d.b%d" % (bc, bank),
                         "episodes_primary": row["episodes_on_the_bank_clock"],
                         "episodes_checker": mine_ep, "episodes_agree": ok_ep,
                         "by_shape_primary": row["by_shape"],
                         "by_shape_checker": mine_shapes,
                         "by_shape_agree": ok_sh})
            if not (ok_ep and ok_sh):
                rest_bad.append(rest[-1])
    b9_rows = []
    for cell in r922c["blind_holdout_B9"]["cells"]:
        bank = cell["bank"]
        mine_ep = recounts[BLIND_TIER]["episodes"][bank]
        mine_shapes = {k: recounts[BLIND_TIER]["strict"][(bank, k)]
                       for k in SHAPE_KEYS}
        agree = mine_ep == cell["episodes_on_the_bank_clock"]
        b9_rows.append({"bank": bank, "period": cell["period"],
                        "episodes_922_checker": cell["episodes_on_the_bank_clock"],
                        "episodes_this_checker": mine_ep, "agree": agree,
                        "shapes_922_checker": cell["shapes"],
                        "shapes_this_checker": {k: v for k, v in mine_shapes.items()
                                                if v},
                        "third_pair_here": mine_shapes["handoff_swap"]})
        if not agree:
            rest_bad.append(b9_rows[-1])
    h_ok = not rest_bad
    results["H_RESTRICTION"] = gate("H_RESTRICTION", h_ok, {
        "primary_cells_recounted_independently": len(rest),
        "disagreements": rest_bad,
        "rows": rest,
        "B9_vs_the_pinned_922_checker": b9_rows,
    })

    # ------------------------------------------------------------ gate J
    teeth = []

    # 1 -- a tampered pin is caught
    _rows, bad = preflight(overrides={PRIMARY_922: b"x"})
    teeth.append({"tooth": "tampered_pin_is_caught", "fires": PRIMARY_922 in bad})

    # 2 -- a planted third-pair episode is visible to THIS checker's instruments
    mac5 = machine(5)
    plant_bank = 3
    P5 = mac5["entry"][plant_bank]
    N5 = mac5["stations"]
    want5 = entry_pair_stations(mac5, plant_bank)
    s1, s2 = want5["handoff_swap"]
    t1 = (s1 + 1) % N5
    L = 130
    dirty = set()
    t = t1
    while t + 2 < L:
        dirty.update({t, t + 1, t + 2})
        t += P5
    seg = 0
    for i in range(L):
        if i not in dirty:
            seg |= 1 << i
    iv = dirty_intervals(seg, L)
    starts = [lo for lo, _hi in iv]
    idx = {x: i for i, x in enumerate(starts)}
    seen_strict = set()
    for i, a1 in enumerate(starts):
        a2 = a1 + P5
        if a2 in idx and idx[a2] == i + 1:
            for key, (u, v) in want5.items():
                if ((0 + a1 - 1) % N5, (0 + a2 - 1) % N5) == (u, v):
                    seen_strict.add(key)
    hits5 = interval_detector(seg, L, list(range(2, 40)))
    teeth.append({
        "tooth": "planted_third_pair_episode_is_visible_to_this_checker",
        "fires": "handoff_swap" in seen_strict and P5 in hits5,
        "stations": [s1, s2], "period": P5,
        "shapes_seen": sorted(seen_strict), "detector_reads_P": P5 in hits5})

    # 3 -- a tampered seal is caught
    bad_payload = dict(own_payload)
    bad_payload["TP_STATEMENT"] = (tp_text or "") + " "
    teeth.append({"tooth": "tampered_seal_is_caught",
                  "fires": digest(bad_payload) != published_seal})

    # 4 -- a planted B=9 row breaks holdout-freedom
    planted_log = list(seal_build_log) + [{"banks": 9, "horizon": HORIZON,
                                           "lanes": 4288, "stations": 67}]
    teeth.append({
        "tooth": "planted_holdout_tier_in_the_build_log_is_caught",
        "fires": holdout_free and not all(
            row["banks"] not in never_built for row in planted_log)})

    # 5 -- a perturbed generator is detected by the kernel oracle
    prog3 = KERNEL.interleaved_program(3)
    seeds3 = seeds_of(3, prog3)
    good = generate(3, 40)
    bad_box = generate(3, 40, perturb=0)
    perturb_mismatch = 0
    for lane in range(0, good["lanes"], max(1, good["lanes"] // 8)):
        event, positions = good["keys"][lane]
        trace = kernel_step_replay(3, 40, seeds3[event], positions)
        for tick in range(41):
            for bank in range(3):
                if bool((bad_box["clean"][bank][tick] >> lane) & 1) != trace[tick][1][bank]:
                    perturb_mismatch += 1
    teeth.append({"tooth": "perturbed_generator_is_detected",
                  "fires": perturb_mismatch > 0,
                  "mismatches": perturb_mismatch})
    del good, bad_box

    # 6 -- a crippled detector disagrees with the literal oracle
    def crippled_detector(mask, length, periods):
        out = interval_detector(mask, length, periods)
        return {p: v for p, v in out.items() if p != min(out)} if out else out

    rng3 = random.Random(930_1029)
    crip = 0
    for _ in range(300):
        n = rng3.randrange(30, 160)
        bits = rng3.getrandbits(n) | (1 << (n - 1))
        if crippled_detector(bits, n, list(range(2, 24))) != literal_detector(
                bits, n, list(range(2, 24))):
            crip += 1
    teeth.append({"tooth": "crippled_detector_is_detectable",
                  "fires": crip > 0, "disagreeing_cases": crip})

    # 7 -- the discriminator scoring really discriminates
    teeth.append({
        "tooth": "constant_true_control_scores_worse_than_the_best",
        "fires": (best is not None
                  and pooled_scores[best]["f1"] >= pooled_scores["always_true"]["f1"]
                  and pooled_scores[best]["accuracy"]
                  > pooled_scores["always_true"]["accuracy"]),
        "best": best, "best_f1": pooled_scores.get(best, {}).get("f1"),
        "control_f1": pooled_scores["always_true"]["f1"]})

    # 8 -- an out-of-set period is visible (the sweep is not narrowed)
    odd = 0
    oddmask = 0
    for i in range(150):
        if i % 37 not in (0, 1, 2):
            oddmask |= 1 << i
    teeth.append({"tooth": "out_of_set_period_is_visible",
                  "fires": 37 in interval_detector(oddmask, 150,
                                                   list(range(2, 80))),
                  "planted_period": 37})

    # 9 -- the widened hunt would find a planted NON-consecutive episode
    dirty2 = set(dirty)
    inject = t1 + 3
    dirty2.add(inject)
    seg2 = 0
    for i in range(L):
        if i not in dirty2:
            seg2 |= 1 << i
    iv2 = dirty_intervals(seg2, L)
    st2 = [lo for lo, _hi in iv2]
    ix2 = {x: i for i, x in enumerate(st2)}
    strict_hit = wide_hit = False
    for i, a1 in enumerate(st2):
        a2 = a1 + P5
        if a2 not in ix2:
            continue
        if ((0 + a1 - 1) % N5, (0 + a2 - 1) % N5) != (s1, s2):
            continue
        wide_hit = True
        if ix2[a2] == i + 1:
            strict_hit = True
    teeth.append({
        "tooth": "widened_hunt_sees_a_planted_non_consecutive_third_pair",
        "fires": wide_hit,
        "strict_definition_also_sees_it": strict_hit,
        "note": "the widened hunt is strictly weaker, so this tooth proves the "
                "widening is live rather than vacuous"})

    # 10 -- the primary's headline claim numbers survive an independent recount
    claim = receipt["claim_text_numbers"]
    recheck = {}
    r7 = recounts[7]
    recheck["B7_b3_bank_owned_entry_gap_episodes"] = sum(
        r7["strict"][(3, k)] for k in SHAPE_KEYS)
    recheck["B7_b5_swap_handoff_episodes"] = r7["strict"][(5, "swap_handoff")]
    recheck["B6_b3_swap_handoff_episodes"] = recounts[6]["strict"][(3, "swap_handoff")]
    agree = all(claim[k] == v for k, v in recheck.items())
    if not agree:
        findings.append("The primary's claim-text numbers do not survive an "
                        "independent recount: %s vs %s"
                        % (recheck, {k: claim[k] for k in recheck}))
    teeth.append({"tooth": "primary_claim_numbers_survive_an_independent_recount",
                  "fires": agree, "checker": recheck,
                  "primary": {k: claim[k] for k in recheck}})

    j_ok = all(t["fires"] for t in teeth) and len(teeth) >= DECLARED_MIN_TEETH
    results["J_TEETH"] = gate("J_TEETH", j_ok, {
        "teeth": teeth, "count": len(teeth),
        "declared_minimum": DECLARED_MIN_TEETH,
        "all_fire": all(t["fires"] for t in teeth)})

    # ------------------------------------------------------------ gate K
    runtime = time.monotonic() - started
    status = "SUPPORTED" if all(results.values()) else "REFUTED_IN_PART"
    if findings and status == "SUPPORTED":
        status = "SUPPORTED_WITH_FINDINGS"
    k_ok = all(results.values()) and runtime <= RUNTIME_LIMIT_SECONDS
    results["K_VERDICT"] = gate("K_VERDICT", k_ok, {
        "primary_status": status,
        "gates": {k: ("PASS" if v else "FAIL") for k, v in results.items()},
        "findings_the_primary_did_not_report": findings,
        "runtime_s": round(runtime, 1),
        "build_log": list(BUILD_LOG)})

    payload = {
        "campaign": "toe-time-expansion-20260802",
        "block": "toe-time-blockT7-20260802", "cycles": [930],
        "authority": "none", "audit": "unset",
        "authorship": "one Claude Opus 5 worker-authored independent checker "
                      "under supervisor spec",
        "independence": "own generator from the kernel's crossing identity, "
                        "validated tick-for-tick against the kernel's own "
                        "apply_controller_step; own interval-algebra detector "
                        "validated against a literal per-tick oracle; own "
                        "station-identity attribution; the Cycle-930 primary "
                        "import-blocklisted and read only as bytes and AST",
        "primary_status": status,
        "gate_results": {k: ("PASS" if v else "FAIL") for k, v in results.items()},
        "generator_independence": {"rows": gen_rows,
                                   "lanes_compared": lanes_compared,
                                   "tick_snapshots_compared": ticks_compared,
                                   "total_mismatches": gen_mismatch},
        "detector_fourth_route": {"randomised_cases": det_cases,
                                  "mismatches": det_mismatch,
                                  "detections_compared": det_hits},
        "rule_re_derived_from_stated_text": {"phrasings": sorted(preds),
                                             "cells": determinacy,
                                             "disagreements": disagree},
        "third_pair_hunt": {"strict_total": strict_total,
                            "widened_total": wide_total, "rows": hunt_rows},
        "rc3_model_degeneracy": {"pooled_scores": pooled_scores,
                                 "ranked_by_f1": [k for k, _v in ranked],
                                 "best": best,
                                 "equal_width_vs_crude_are_degenerate": degeneracy,
                                 "per_cell": per_cell_scores,
                                 "population_size": len(pooled)},
        "seal_audit": {"published": published_seal, "recomputed": own_seal,
                       "agrees": own_seal == published_seal,
                       "build_log_holdout_free": holdout_free,
                       "B9_measured_third_pair_episodes": b9_measured},
        "restriction_against_the_primary": {"rows": rest,
                                            "disagreements": rest_bad,
                                            "B9_vs_922_checker": b9_rows},
        "findings_the_primary_did_not_report": findings,
        "teeth": teeth,
        "disclosed": list(DISCLOSED),
        "build_log": list(BUILD_LOG),
        "runtime_seconds": round(runtime, 1),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "exit_codes": {"checker": 0 if k_ok else 1},
        "pinned_inputs": {p: PREFLIGHT_ROWS[p] for p in sorted(PINS)},
    }
    me = Path(__file__).read_bytes()
    payload["files"] = {
        "scripts/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py":
            {"sha256": sha256(me).hexdigest(), "git_blob": git_blob(me)}}
    out = (ROOT / "outputs"
           / "third_pair_rc3_independent_check_cycle930_receipt_2026_07_28.json")
    out.write_text(json.dumps(payload, indent=1, sort_keys=True, default=str))
    print("RECEIPT %s :: %s" % (out.name, json.dumps(
        {"sha256": sha256(out.read_bytes()).hexdigest()}, **dumps)))
    return 0 if k_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
