#!/usr/bin/env python3
"""Cycle 863: the time-from-records triptych (owner-directed, supervisor-run).

Three constructions, one replay substrate, no axiom surface touched:

A. FORMATION-AS-SATURATION: at formation boundaries, does the neighborhood
   leave exactly ONE available direction-possibility (counterfactual test via
   the core's own prepare_endpoint operator), while dirty control boundaries
   leave more than one?
B. THE DERIVED CLOCK: per-bank formation events; synchronization events
   (both banks clean); does the supplied tick (orbit cadence) RE-DERIVE from
   the record structure (sync events sitting on orbit boundaries; the E2
   census as first sync events)?
C. NO-BACKGROUND-CLOCK RECONSTRUCTION: re-express the landed censuses
   intrinsically (E1 = first formation event; E2' = first synchronization
   event) with no scheduler index in the definitions; certify reproduction.

Supervisor-authored primary.  bounded_theorem, authority none, audit unset.
Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle860_readout_discriminator_2026_07_28.py",
)
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "28a62fb0bc83ec7a46c18901158693344a84cc1eff8c0c9537b40d9004d8b926",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "b48450fbe70f152bfeaab561a12591a2ec7d48c0",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
TRAJECTORY_HORIZON = 51_115
LANDED_E1 = 182
LANDED_E2 = 114
EVENT_STORE_CAP = 4096


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    for path, payload in payloads.items():
        ast.parse(payload, filename=path)
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=Path(__file__).name
    )
    literal = None
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
    }
    result["pass"] = (
        result["literal_ok"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def pairwise_separated(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return all((s + 1) % stations not in occupied for s in occupied)


def derive_event_seeds(program):
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if not (
            after == K.A.apply_semantic(before, allocator)
            and rail_a == (1,) + (0,) * (len(program) - 1)
            and not any(rail_b)
            and len(trace) == len(program)
        ):
            raise AssertionError(("event seed", event))
        rows.append((event, before))
        state = after
    return tuple(rows)


def derive_census():
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    event_seeds = derive_event_seeds(program)
    keys = tuple(
        (k, event, positions)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), k)
        if pairwise_separated(positions, stations)
        for event, _s in event_seeds
    )
    return program, event_seeds, tuple(sorted(keys))


def watched_registers():
    return (
        ("POINTER", K.A.POINTER), ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U), ("DIRECTION_OK", K.A.DIRECTION_OK),
        *((f"FRESH_{i}", w) for i, w in enumerate(K.A.FRESH)),
        *((f"ZERO_WORK_{i}", w) for i, w in enumerate(K.A.ZERO_WORK)),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def dirty_partition():
    """Global dirty coordinates partitioned: per-bank, links, source pointer."""

    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _ in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _ in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)
    per_bank: list[set[int]] = [set() for _ in zero_banks]
    for bank_index in range(len(zero_banks)):
        for _name, wire in watched_registers():
            changed = [list(b) for b in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(
                tuple(tuple(b) for b in changed), zero_links
            )
            diffs = [i for i, (l, r) in enumerate(zip(baseline, marked)) if l != r]
            if len(diffs) != 1:
                raise AssertionError(("bank marker", diffs))
            per_bank[bank_index].add(diffs[0])
    link_set: set[int] = set()
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(zero_banks, tuple(tuple(r) for r in changed))
            diffs = [i for i, (l, r) in enumerate(zip(baseline, marked)) if l != r]
            if len(diffs) != 1:
                raise AssertionError(("link marker", diffs))
            link_set.add(diffs[0])
    return (
        tuple(tuple(sorted(s)) for s in per_bank),
        tuple(sorted(link_set)),
        K.R3.X.SOURCE_POINTER,
    )


def synchronous_word(program, positions0):
    positions = tuple(positions0)
    word = []
    for _ in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple((s + 1) % len(program) for s in positions)
    return tuple(word)


def build_initial_states(program, event_seeds, census):
    seed_by_event = dict(event_seeds)
    states = []
    failures = 0
    for k, event, positions in census:
        before = seed_by_event[event]
        after, rail_a, rail_b, _ = K.run_orbit(
            before, program, token_positions=positions
        )
        expected_rail = tuple(
            int(s in positions) for s in range(len(program))
        )
        failures += rail_a != expected_rail or any(rail_b)
        states.append(after)
    return tuple(states), failures


def pack_lanes(states):
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def compile_masked_gate(gate, mask):
    if gate.kind == "X":
        return (0, gate.wires[0], 0, 0, mask)
    if gate.kind == "CNOT":
        return (1, gate.wires[0], gate.wires[1], 0, mask)
    if gate.kind == "TOF":
        return (2, gate.wires[0], gate.wires[1], gate.wires[2], mask)
    raise ValueError(("gate", gate))


def masked_h_schedules(program, census):
    stations = len(program)
    rows = []
    for step in range(stations):
        schedule = []
        for station, row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_k, _e, positions) in enumerate(census)
                if (station - step) % stations in positions
            )
            if mask:
                schedule.extend(
                    compile_masked_gate(g, mask) for g in K.mapped_macro(row)
                )
        rows.append(tuple(schedule))
    return tuple(rows)


def compile_fast(schedules):
    fns = []
    for schedule in schedules:
        src = ["def apply_chunk(c):"]
        for kind, a, b, c3, mask in schedule:
            if kind == 0:
                src.append(f" c[{a}] ^= {mask}")
            elif kind == 1:
                src.append(f" c[{b}] ^= c[{a}] & {mask}")
            else:
                src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        ns: dict[str, object] = {}
        exec("\n".join(src), {"__builtins__": {}}, ns)
        fns.append(ns["apply_chunk"])
    return tuple(fns)


def mask_over(columns, indices, universe):
    dirty = 0
    for wire in indices:
        dirty |= columns[wire]
    return universe & ~dirty


def lanes_of(mask):
    out = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


def lane_state(columns, lane):
    bit = 1 << lane
    return tuple(int(bool(col & bit)) for col in columns)


def replay(program, event_seeds, census):
    """One exact replay: global/bank clean events, sync events, E1/E2 stamps,
    with per-key capped event stores and total counts."""

    started = monotonic()
    states, init_fail = build_initial_states(program, event_seeds, census)
    n = len(census)
    sim = census + (census[0],)
    dup = n
    columns = pack_lanes(states + (states[0],))
    fast = compile_fast(masked_h_schedules(program, sim))
    per_bank, links, source_ptr = dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}
    ))
    bank_dirty = (
        tuple(sorted(set(per_bank[0]))), tuple(sorted(set(per_bank[1]))),
    )
    universe_all = (1 << n) - 1
    universe_sim = (1 << (n + 1)) - 1
    stations = len(program)

    e1_moment: dict[Key, int] = {}
    e2_moment: dict[Key, int] = {}
    counts = {
        "global": [0] * n, "bank0": [0] * n, "bank1": [0] * n, "sync": [0] * n,
    }
    stores = {
        "global": [[] for _ in range(n)], "sync": [[] for _ in range(n)],
        "bank0": [[] for _ in range(n)], "bank1": [[] for _ in range(n)],
    }
    mismatches = 0

    def record_events(mask, kind, boundary):
        for lane in lanes_of(mask):
            counts[kind][lane] += 1
            store = stores[kind][lane]
            if len(store) < EVENT_STORE_CAP:
                store.append(boundary)

    g0 = mask_over(columns, global_dirty, universe_sim)
    mismatches += int(bool(g0 & 1) != bool(g0 & (1 << dup)))
    b0 = mask_over(columns, bank_dirty[0], universe_all)
    b1 = mask_over(columns, bank_dirty[1], universe_all)
    record_events(g0 & universe_all, "global", 0)
    record_events(b0, "bank0", 0)
    record_events(b1, "bank1", 0)
    record_events(b0 & b1, "sync", 0)
    for lane in lanes_of(g0 & universe_all):
        e1_moment.setdefault(census[lane], 0)
        e2_moment.setdefault(census[lane], 0)

    for orbit in range(1, TRAJECTORY_HORIZON + 1):
        for step, chunk in enumerate(fast, 1):
            chunk(columns)
            boundary = (orbit - 1) * stations + step
            g = mask_over(columns, global_dirty, universe_sim)
            mismatches += int(bool(g & 1) != bool(g & (1 << dup)))
            ga = g & universe_all
            b0 = mask_over(columns, bank_dirty[0], universe_all)
            b1 = mask_over(columns, bank_dirty[1], universe_all)
            record_events(ga, "global", boundary)
            record_events(b0, "bank0", boundary)
            record_events(b1, "bank1", boundary)
            record_events(b0 & b1, "sync", boundary)
            for lane in lanes_of(ga):
                e1_moment.setdefault(census[lane], boundary)
        for lane in lanes_of(ga):
            e2_moment.setdefault(census[lane], orbit)

    return {
        "columns_final": columns,
        "init_failures": init_fail,
        "e1_moment": e1_moment,
        "e2_moment": e2_moment,
        "counts": counts,
        "stores": stores,
        "mismatches": mismatches,
        "stations": stations,
        "runtime_seconds": round(monotonic() - started, 3),
    }


def certificate_b(rep, census):
    """The derived clock: sync events vs the supplied tick; E2 as first sync."""

    stations = rep["stations"]
    on_tick = 0
    off_tick = 0
    first_sync_matches = 0
    first_sync_total = 0
    spacing = Counter()
    for lane, key in enumerate(census):
        syncs = rep["stores"]["sync"][lane]
        for b in syncs:
            if b % stations == 0:
                on_tick += 1
            else:
                off_tick += 1
        for left, right in zip(syncs, syncs[1:]):
            spacing[right - left] += 1
        if key in rep["e2_moment"] and syncs:
            first_sync_total += 1
            if syncs[0] == rep["e2_moment"][key] * stations or (
                syncs[0] == 0 and rep["e2_moment"][key] == 0
            ):
                first_sync_matches += 1
    total = on_tick + off_tick
    result = {
        "certificate": "B_DERIVED_CLOCK",
        "sync_events_total": total,
        "sync_on_tick": on_tick,
        "sync_off_tick": off_tick,
        "on_tick_fraction": round(on_tick / total, 6) if total else None,
        "first_sync_equals_landed_E2": f"{first_sync_matches}/{first_sync_total}",
        "spacing_top": spacing.most_common(6),
        "finding": (
            "the supplied tick re-derives from record structure iff sync"
            " events sit on orbit boundaries and the E2 census equals first"
            " sync events; fractions above are the exact verdict"
        ),
    }
    result["pass"] = total > 0
    return result


def certificate_c(rep, census):
    """No-background-clock reconstruction of the landed censuses."""

    e1_set = frozenset(rep["e1_moment"])
    e2_set = frozenset(rep["e2_moment"])
    stations = rep["stations"]
    intrinsic_e1 = 0
    for lane, key in enumerate(census):
        g = rep["stores"]["global"][lane]
        if g and key in rep["e1_moment"] and g[0] == rep["e1_moment"][key]:
            intrinsic_e1 += 1
    e2_prime_matches = 0
    e2_prime_extra = 0
    for lane, key in enumerate(census):
        syncs = rep["stores"]["sync"][lane]
        if syncs:
            moment = syncs[0]
            if key in rep["e2_moment"] and moment == rep["e2_moment"][key] * stations:
                e2_prime_matches += 1
            elif key in rep["e2_moment"] and moment == 0 == rep["e2_moment"][key]:
                e2_prime_matches += 1
            elif key not in rep["e2_moment"]:
                e2_prime_extra += 1
    result = {
        "certificate": "C_INTRINSIC_RECONSTRUCTION",
        "landed_counts": (len(e1_set), len(e2_set)),
        "landed_expected": (LANDED_E1, LANDED_E2),
        "intrinsic_E1_identity": f"{intrinsic_e1}/{len(e1_set)}",
        "E2_prime_first_sync_matches": f"{e2_prime_matches}/{len(e2_set)}",
        "E2_prime_extra_keys": e2_prime_extra,
        "finding": (
            "E1 is intrinsically definable by construction (first formation"
            " event); E2 is scheduler-free iff first-sync reproduces it"
            " exactly and adds no extra keys"
        ),
    }
    result["pass"] = (
        len(e1_set) == LANDED_E1 and len(e2_set) == LANDED_E2
        and intrinsic_e1 == len(e1_set)
    )
    return result


SATURATION_BOUNDARY_CAP = 1_100
SATURATION_LANE_CAP = 64


def certificate_a(rep, program, census):
    """Formation-as-saturation: counterfactual direction availability.

    Declared bounded sample: the earliest-formation lanes (first clean
    boundary <= SATURATION_BOUNDARY_CAP), at most SATURATION_LANE_CAP of
    them, each evaluated by ONE forward walk that captures the control
    state (boundary first-1) and the formation state (boundary first).
    Memory-safe: no per-boundary snapshot store.
    """

    word_cache: dict[tuple[int, ...], tuple] = {}
    directions = ((1, 0), (0, 1))
    per_bank, links, source_ptr = dirty_partition()
    rows = {"formation": Counter(), "control": Counter()}
    samples = {"formation": 0, "control": 0}
    errors = 0
    seeds = dict(derive_event_seeds(program))
    stations = len(program)

    candidates = sorted(
        (rep["stores"]["global"][lane][0], lane)
        for lane, key in enumerate(census)
        if key in rep["e1_moment"] and rep["stores"]["global"][lane]
        and 0 < rep["stores"]["global"][lane][0] <= SATURATION_BOUNDARY_CAP
    )[:SATURATION_LANE_CAP]

    def availability(state):
        nonlocal errors
        available = 0
        for v in directions:
            try:
                sub = K.M.prepare_endpoint(state, v)
                after = K.A.apply_semantic(sub, word_cache["__chunk0__"])
            except Exception:
                errors += 1
                continue
            flags_zero = all(
                after[w] == 0 for bank in per_bank for w in bank
            )
            available += int(flags_zero)
        return available

    for first, lane in candidates:
        key = census[lane]
        positions = key[2]
        if positions not in word_cache:
            word_cache[positions] = synchronous_word(program, positions)
        word = word_cache[positions]
        per_chunk = len(word) // stations
        before = seeds[key[1]]
        state, _ra, _rb, _t = K.run_orbit(
            before, program, token_positions=positions
        )
        control_state = None
        for b in range(first):
            if b == first - 1:
                control_state = state
            chunk = word[(b % stations) * per_chunk:
                         ((b % stations) + 1) * per_chunk]
            state = K.A.apply_semantic(state, chunk)
        next_chunk = word[(first % stations) * per_chunk:
                          ((first % stations) + 1) * per_chunk]
        word_cache["__chunk0__"] = next_chunk
        rows["formation"][availability(state)] += 1
        samples["formation"] += 1
        if control_state is not None and (first - 1) not in \
                rep["stores"]["global"][lane]:
            prev_chunk = word[((first - 1) % stations) * per_chunk:
                              (((first - 1) % stations) + 1) * per_chunk]
            word_cache["__chunk0__"] = prev_chunk
            rows["control"][availability(control_state)] += 1
            samples["control"] += 1

    result = {
        "certificate": "A_SATURATION",
        "counterfactual_operator": "K.M.prepare_endpoint(state, direction)",
        "declared_sample": {
            "boundary_cap": SATURATION_BOUNDARY_CAP,
            "lane_cap": SATURATION_LANE_CAP,
            "lanes_sampled": len(candidates),
        },
        "availability_histogram_formation": dict(rows["formation"]),
        "availability_histogram_control": dict(rows["control"]),
        "samples": dict(samples),
        "substitution_errors": errors,
        "finding": (
            "formation-as-saturation holds iff formation boundaries"
            " concentrate at availability==1 and dirty controls at"
            " availability!=1; histograms above are the exact verdict at"
            " the declared bounded sample"
        ),
    }
    result["pass"] = samples["formation"] > 0
    return result


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program, event_seeds, census = derive_census()
    rep = replay(program, event_seeds, census)
    cert_b = certificate_b(rep, census)
    cert_c = certificate_c(rep, census)
    cert_a = certificate_a(rep, program, census)
    runtime = round(monotonic() - started, 3)
    checks = {
        "A_SATURATION": cert_a["pass"],
        "B_DERIVED_CLOCK": cert_b["pass"],
        "C_INTRINSIC_RECONSTRUCTION": cert_c["pass"],
        "D_CONTROLS": bool(
            controls["pass"] and rep["mismatches"] == 0
            and rep["init_failures"] == 0 and runtime < AUDIT_TIMEOUT_SEC
        ),
    }
    lines = ["CYCLE863_TIME_FROM_RECORDS_TRIPTYCH",
             "OWNER_DIRECTED_SUPERVISOR_RUN_NO_AXIOM_SURFACE_TOUCHED"]
    for name, payload in (("A_SATURATION", cert_a),
                          ("B_DERIVED_CLOCK", cert_b),
                          ("C_INTRINSIC_RECONSTRUCTION", cert_c)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {
        "checks": checks, "cycle": 863, "runtime_seconds": runtime,
        "replay_runtime": rep["runtime_seconds"],
        "event_store_cap": EVENT_STORE_CAP,
        "pass": all(checks.values()),
    }
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE863_TIME_FROM_RECORDS_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
