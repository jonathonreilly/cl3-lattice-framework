#!/usr/bin/env python3
"""Cycle 878: the composed-record event space as a sample space (groundwork).

Campaign-5 Born GROUNDWORK.  Strictly structural.  NO probability
postulate is introduced, NO Born rule is claimed, NO candidate weighting
is selected.  Every fraction emitted here is a BOOKKEEPING FRACTION, NOT
A PROBABILITY, and is labelled as such in the emitted certificates.

Substrate: the Cycle-867 composed record-write model (records as genuine
state content -- register writes at bank clean-edges into structurally
dead wires).  Cycle 867 is a SHA/blob-pinned, text/AST-only specification
primary (BLOCKLISTED from import); its construction is rebuilt here from
the landed Cycle-719 core and the landed Cycle-863 replay substrate.

A. EVENT_SPACE: extract the exact set of realized record-write events
   (world, moment, tag, ordinal, content) at the declared horizon; certify
   cardinalities, the per-world event-count distribution, and the
   sigma-algebra-relevant structure -- which declared families are
   partitions, the full refinement/crossing lattice over them (does the
   (bank-tag, ordinal) family refine the global-tag family?), and that the
   atoms are singletons (so the generated sigma-algebra is 2^E).
B. MEASURE_CANDIDATE_INVENTORY (admissibility only, NO selection):
   record-native weightings available WITHOUT new axioms -- counting
   measure on events, per-world uniform, occupation-weighted (from the
   landed Cycle-863 occupation ledger), formation-moment-weighted (two
   declared readings), plus a declared NEGATIVE CONTROL (content
   diversity) that is record-native but NOT additive.  For each: exact
   PASS/FAIL on finite additivity over the certified disjoint families,
   normalizability, and permutation covariance under the landed
   symmetries (the Cycle-856 monitor-phase Z_11 relabelling of worlds and
   the bank-label swap on tags).  Support-faithfulness is reported as a
   disclosed extra diagnostic, not as a demanded axiom.
C. FRACTION_LEDGER: exact rational event-fraction tables per (admissible
   candidate, certified family) -- bookkeeping fractions, not
   probabilities -- plus the exact pairwise DISAGREEMENT matrix with
   witness cells (the discriminating atoms are the future experiment
   surface).
D. BOUNDARY: what the framework does NOT supply, quoted verbatim from the
   sha/blob-pinned in-tree axiom baseline.
E. CONTROLS.

Exact arithmetic: every candidate weighting is carried as an INTEGER
numerator vector over a single common denominator, so all masses, sums
and fractions are exact rationals with no floating point anywhere.

Declared scope and caps (all disclosed in the certificates): B=2, the
Cycle-852 census (748 worlds, 11 stations), horizon 16,384 orbits;
dead-wire derivation window 512 orbits at chunk granularity then orbit
granularity to 4,096; register cap 64 wire-visible ordinals per
(bank-tag, world); one formation slot per world.

Relation to the landed Cycle-867 register: 867 wire-wrote its global tag
ONLY at boundary 0.  This cycle writes a formation tag F at each world's
FIRST global-clean boundary; the F-events at moment 0 are certified to be
exactly the 867 global-tag writes, so the event space strictly extends the
landed register rather than replacing it.

Supervisor-authored primary.  bounded_theorem, authority none, audit
unset.  Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
import json
from math import gcd
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle863_time_from_records_2026_07_28.py",
    "scripts/frontier_cycle867_composed_record_write_2026_07_28.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
COMPUTATIONAL_INPUT_PATHS = AUDIT_INPUT_PATHS[:2]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[2:3]
TEXT_ONLY_PATHS = AUDIT_INPUT_PATHS[3:]
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    AUDIT_INPUT_PATHS[2]:
        "49605f6d0730e224d6c4cd25a182ec49e0c7d2f2316851bc2755632dcbe2c828",
    AUDIT_INPUT_PATHS[3]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    AUDIT_INPUT_PATHS[2]: "5f923e8429373fa5afc71a417cd4e6f787ec71b8",
    AUDIT_INPUT_PATHS[3]: "4a863da1f3f255354839277271a3a69a5c205133",
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
import frontier_cycle863_time_from_records_2026_07_28 as C863

HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
DEAD_ORBIT_ORBITS = 4_096
REGISTER_CAP = 64
DETERMINISM_ORBITS = 192
FULL_TABLE_CELL_CAP = 140
TABLE_BYTE_CAP = 9_000
TOTAL_TABLE_BYTE_BUDGET = 60_000
TOP_CELLS_REPORTED = 5
FRACTION_LABEL = "bookkeeping fraction, not probability"

# The exclusion list of the axiom baseline, quoted VERBATIM from the
# sha/blob-pinned in-tree source docs/MINIMAL_AXIOMS_2026-06-29.md
# ("Open Gates Outside The Axioms").  Presence in the pinned file is
# certified byte-for-byte at run time; nothing here paraphrases it.
EXCLUSION_NEEDLE = (
    "- context selection, measurement basis selection, Born weights,"
    " probability\n  rules, update laws, decoherence mechanisms, and"
    " formation rules (which\n  admissible possibility a new record locks,"
    " at which site, with what weight,\n  or at what rate);"
)
BOUNDARY_STATEMENT = (
    "this block supplies no occurrence rule, no probability, no update"
    " law, and selects no candidate weighting; it certifies a finite"
    " event space, a refinement lattice, and an admissibility inventory"
    " of record-native weightings -- selection remains the named open"
    " gate"
)

CANDIDATE_NAMES = (
    "M1_COUNTING", "M2_PER_WORLD_UNIFORM", "M3_OCCUPATION_WEIGHTED",
    "M4_FORMATION_LIFETIME", "M5_FORMATION_MOMENT",
)
CONTROL_NAME = "M0_CONTENT_DIVERSITY"

FAMILY_ORDER = (
    "F_WORLD", "F_TAG", "F_TAG_ORDINAL", "F_MOMENT", "F_ORBIT",
    "F_CONTENT", "F_WORLD_TAG", "F_ATOM",
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b) if a and b else 0


def source_controls() -> dict:
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in COMPUTATIONAL_INPUT_PATHS + TEXT_AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=Path(__file__).name
    )
    literal = None
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) \
                        and target.id == "AUDIT_INPUT_PATHS":
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
        "text_only_paths_not_imported": TEXT_ONLY_PATHS,
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


# ---------------------------------------------------------------------------
# The composed model (Cycle-867 construction, rebuilt from the landed core)
# ---------------------------------------------------------------------------

def dead_wire_rig(program, sim, columns_proto):
    """Derive boundary-dead wires, then the structurally inert safe slots."""
    fast = C863.compile_fast(C863.masked_h_schedules(program, sim))
    universe_sim = (1 << len(sim)) - 1
    work = list(columns_proto)
    acc = list(work)
    for orbit in range(1, DEAD_ORBIT_ORBITS + 1):
        for chunk in fast:
            chunk(work)
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in range(len(work)):
                    acc[w] |= work[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in range(len(work)):
                acc[w] |= work[w]
    dead_wires = tuple(
        w for w in range(len(acc)) if (acc[w] & universe_sim) == 0
    )
    gate_inputs: set = set()
    gate_targets: set = set()
    for schedule in C863.masked_h_schedules(program, sim):
        for kind, a, b, c3, _mask in schedule:
            if kind == 0:
                gate_targets.add(a)
            elif kind == 1:
                gate_inputs.add(a)
                gate_targets.add(b)
            else:
                gate_inputs.update((a, b))
                gate_targets.add(c3)
    safe_pool = tuple(
        w for w in dead_wires
        if w not in gate_inputs and w not in gate_targets
    )
    slot_tags = [("F", 0)] + [
        (f"B{b}", k) for b in (0, 1) for k in range(REGISTER_CAP)
    ]
    if len(safe_pool) < len(slot_tags):
        raise AssertionError(
            ("insufficient safe slots", len(safe_pool), len(slot_tags))
        )
    return {
        "fast": fast,
        "dead_wires": dead_wires,
        "safe_pool": safe_pool,
        "slot_of": {tag: safe_pool[i] for i, tag in enumerate(slot_tags)},
        "gate_inputs": gate_inputs,
        "gate_targets": gate_targets,
    }


def composed_scan(program, census, states, rig, orbits):
    """The composed model: base dynamics + REAL register writes into the
    inert dead-wire slots.  Returns the realized record-write event list
    plus the occupation ledger accumulated on the same trajectory."""
    slot_of = rig["slot_of"]
    fast = rig["fast"]
    n = len(census)
    dup = n
    columns = C863.pack_lanes(states + (states[0],))
    per_bank, links, source_ptr = C863.dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}
    ))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1
    slot_wires = set(slot_of.values())
    watch_dead = tuple(w for w in rig["dead_wires"] if w not in slot_wires)

    events: list[tuple] = []
    occ_global = [0] * n
    occ_bank = ([0] * n, [0] * n)
    bank_ordinal = [[0, 0] for _ in range(n)]
    beyond_cap = 0
    write_once_violations = 0
    formed: dict[int, int] = {}
    mismatches = 0
    dead_acc = 0

    def wire_write(tag, lane):
        nonlocal write_once_violations
        wire = slot_of[tag]
        bit = 1 << lane
        if columns[wire] & bit:
            write_once_violations += 1
        columns[wire] |= bit

    def content_of(lane):
        return sha256(bytes(C863.lane_state(columns, lane))).hexdigest()[:16]

    g0 = C863.mask_over(columns, global_dirty, uni_sim)
    mismatches += int(bool(g0 & 1) != bool(g0 & (1 << dup)))
    ga0 = g0 & uni_all
    b_mask = [
        C863.mask_over(columns, bank_dirty[b], uni_all) for b in (0, 1)
    ]
    for lane in C863.lanes_of(ga0):
        occ_global[lane] += 1
    for b in (0, 1):
        for lane in C863.lanes_of(b_mask[b]):
            occ_bank[b][lane] += 1
    for lane in C863.lanes_of(ga0):
        formed[lane] = 0
        wire_write(("F", 0), lane)
        events.append((lane, 0, "F", 0, content_of(lane)))
    prev_bank = list(b_mask)

    boundary = 0
    for orbit in range(1, orbits + 1):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = C863.mask_over(columns, global_dirty, uni_sim)
            mismatches += int(bool(g & 1) != bool(g & (1 << dup)))
            ga = g & uni_all
            for lane in C863.lanes_of(ga):
                occ_global[lane] += 1
                if lane not in formed:
                    formed[lane] = boundary
                    wire_write(("F", 0), lane)
                    events.append((lane, boundary, "F", 0, content_of(lane)))
            for b in (0, 1):
                bm = C863.mask_over(columns, bank_dirty[b], uni_all)
                for lane in C863.lanes_of(bm):
                    occ_bank[b][lane] += 1
                for lane in C863.lanes_of(bm & ~prev_bank[b]):
                    ordinal = bank_ordinal[lane][b]
                    if ordinal < REGISTER_CAP:
                        wire_write((f"B{b}", ordinal), lane)
                        events.append(
                            (lane, boundary, f"B{b}", ordinal,
                             content_of(lane))
                        )
                    else:
                        beyond_cap += 1
                    bank_ordinal[lane][b] = ordinal + 1
                prev_bank[b] = bm
            if orbit <= DEAD_CHUNK_ORBITS:
                for w in watch_dead:
                    dead_acc |= columns[w]
        if orbit > DEAD_CHUNK_ORBITS:
            for w in watch_dead:
                dead_acc |= columns[w]
    return {
        "events": events,
        "occ_global": occ_global,
        "occ_bank": occ_bank,
        "formed": formed,
        "beyond_cap": beyond_cap,
        "write_once_violations": write_once_violations,
        "dead_activation_conflicts": bin(dead_acc & uni_sim).count("1"),
        "mismatches": mismatches,
        "columns": columns,
        "global_dirty": global_dirty,
        "bank_dirty": bank_dirty,
        "boundaries": boundary,
        "initial_global_clean_lanes": len(C863.lanes_of(ga0)),
    }


# ---------------------------------------------------------------------------
# Families and the refinement lattice
# ---------------------------------------------------------------------------

def family_keys(events, stations):
    """Cell key of every event under every declared family."""
    keys = {name: [] for name in FAMILY_ORDER}
    for lane, moment, tag, ordinal, content in events:
        keys["F_WORLD"].append(("w", lane))
        keys["F_TAG"].append(("t", tag))
        keys["F_TAG_ORDINAL"].append(("to", tag, ordinal))
        keys["F_MOMENT"].append(("m", moment))
        keys["F_ORBIT"].append(
            ("o", 0 if moment == 0 else ((moment - 1) // stations) + 1)
        )
        keys["F_CONTENT"].append(("c", content))
        keys["F_WORLD_TAG"].append(("wt", lane, tag))
        keys["F_ATOM"].append(("a", lane, tag, ordinal))
    return keys


def cells_of(key_list):
    cells: dict = {}
    for index, key in enumerate(key_list):
        cells.setdefault(key, []).append(index)
    return cells


def refines(keys_a, keys_b):
    """F_a refines F_b iff the a-cell of an event determines its b-cell."""
    seen: dict = {}
    for ka, kb in zip(keys_a, keys_b):
        prior = seen.get(ka)
        if prior is None:
            seen[ka] = kb
        elif prior != kb:
            return False
    return True


# ---------------------------------------------------------------------------
# Landed symmetries
# ---------------------------------------------------------------------------

def monitor_phase_action(census, stations):
    """The Cycle-856 landed symmetry: moving the controller-orbit cut to
    monitor phase m advances the sources by m stations.  On census keys
    (k, event, positions) this is positions -> positions + m (mod
    stations), a Z_stations action on the worlds."""
    index_of = {key: i for i, key in enumerate(census)}
    perms = []
    for m in range(stations):
        image = []
        for k, event, positions in census:
            target = (k, event, tuple(sorted((p + m) % stations
                                             for p in positions)))
            if target not in index_of:
                return (), False
            image.append(index_of[target])
        if sorted(image) != list(range(len(census))):
            return (), False
        perms.append(tuple(image))
    return tuple(perms), True


def group_orbits(perms, size):
    seen = [False] * size
    orbits = []
    for start in range(size):
        if seen[start]:
            continue
        orbit = set()
        frontier = [start]
        seen[start] = True
        while frontier:
            x = frontier.pop()
            orbit.add(x)
            for perm in perms:
                y = perm[x]
                if not seen[y]:
                    seen[y] = True
                    frontier.append(y)
        orbits.append(tuple(sorted(orbit)))
    return tuple(orbits)


# ---------------------------------------------------------------------------
# Measure candidates -- exact integer numerators over a common denominator
# ---------------------------------------------------------------------------

def build_candidates(events, occ_global, formed, boundaries):
    """Record-native weightings available without new axioms.  Each
    additive candidate is an EVENT-LEVEL weight w: E -> Q_{>=0}, carried
    as integer numerators over one common denominator per candidate."""
    per_world = Counter(e[0] for e in events)
    supported = sorted(per_world)
    n_supported = len(supported)
    common = 1
    for count in set(per_world.values()):
        common = lcm(common, count)

    def world_weighted(a_of_world):
        totals = sum(a_of_world(w) for w in supported)
        nums = [
            a_of_world(e[0]) * (common // per_world[e[0]]) for e in events
        ]
        return nums, totals * common

    nums: dict[str, list[int]] = {}
    dens: dict[str, int] = {}
    meta: dict[str, dict] = {}

    nums["M1_COUNTING"] = [1] * len(events)
    dens["M1_COUNTING"] = 1
    meta["M1_COUNTING"] = {
        "definition": "w(e) = 1 for every realized record-write event",
        "record_native_source": "the event space itself",
    }

    nums["M2_PER_WORLD_UNIFORM"], dens["M2_PER_WORLD_UNIFORM"] = \
        world_weighted(lambda w: 1)
    meta["M2_PER_WORLD_UNIFORM"] = {
        "definition": (
            "each world carrying at least one event gets equal mass"
            " 1/|supported worlds|, spread uniformly over its own events"
        ),
        "record_native_source": "the world index of the Cycle-852 census",
        "supported_worlds": n_supported,
    }

    nums["M3_OCCUPATION_WEIGHTED"], dens["M3_OCCUPATION_WEIGHTED"] = \
        world_weighted(lambda w: occ_global[w])
    meta["M3_OCCUPATION_WEIGHTED"] = {
        "definition": (
            "world mass proportional to its clean-dwell occupation count,"
            " uniform within the world"
        ),
        "record_native_source": (
            "the landed Cycle-863 occupation ledger counts['global']"
            " (boundaries at which the world is globally clean)"
        ),
        "occupation_total_over_supported_worlds":
            sum(occ_global[w] for w in supported),
    }

    nums["M4_FORMATION_LIFETIME"], dens["M4_FORMATION_LIFETIME"] = \
        world_weighted(
            lambda w: (boundaries - formed[w] + 1) if w in formed else 0
        )
    meta["M4_FORMATION_LIFETIME"] = {
        "definition": (
            "formation-moment weighting, LIFETIME reading: world mass"
            " proportional to (total boundaries - formation moment + 1),"
            " the number of horizon moments in which the world is already"
            " formed; uniform within the world; never-formed worlds get"
            " zero"
        ),
        "record_native_source":
            "the composed model's first-formation moment per world",
        "lifetime_total": sum(
            (boundaries - formed[w] + 1) for w in supported if w in formed
        ),
    }

    nums["M5_FORMATION_MOMENT"], dens["M5_FORMATION_MOMENT"] = \
        world_weighted(lambda w: formed[w] if w in formed else 0)
    meta["M5_FORMATION_MOMENT"] = {
        "definition": (
            "formation-moment weighting, ELAPSED reading: world mass"
            " proportional to the formation moment itself; uniform within"
            " the world; worlds formed at moment 0 and never-formed worlds"
            " get zero"
        ),
        "record_native_source":
            "the composed model's first-formation moment per world",
        "moment_total": sum(
            formed[w] for w in supported if w in formed
        ),
    }

    meta[CONTROL_NAME] = {
        "definition": (
            "declared NEGATIVE CONTROL: nu(A) = number of DISTINCT record"
            " contents appearing in A -- record-native and monotone, but a"
            " set function with no event-level weight"
        ),
        "record_native_source": "the record content written to the wires",
        "is_negative_control": True,
    }
    return nums, dens, meta, per_world, supported, common


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    controls = source_controls()
    program, event_seeds, census = C863.derive_census()
    stations = len(program)
    n = len(census)
    states, init_fail = C863.build_initial_states(program, event_seeds, census)
    sim = census + (census[0],)
    rig = dead_wire_rig(
        program, sim, C863.pack_lanes(states + (states[0],))
    )
    slot_of = rig["slot_of"]

    scan = composed_scan(program, census, states, rig, HORIZON)
    events = scan["events"]
    boundaries = scan["boundaries"]
    total_events = len(events)

    old_h = C863.TRAJECTORY_HORIZON
    C863.TRAJECTORY_HORIZON = HORIZON
    try:
        rep = C863.replay(program, event_seeds, census)
    finally:
        C863.TRAJECTORY_HORIZON = old_h
    ledger_agrees = list(rep["counts"]["global"]) == list(scan["occ_global"])
    anno_e1 = rep["e1_moment"]
    formed_by_key = {census[lane]: b for lane, b in scan["formed"].items()}
    formation_agrees = formed_by_key == dict(anno_e1)

    # ---- Certificate A: the event space and its lattice --------------------
    keys = family_keys(events, stations)
    cells = {name: cells_of(keys[name]) for name in FAMILY_ORDER}
    partition_ok = {
        name: (
            sum(len(v) for v in cells[name].values()) == total_events
            and len({i for v in cells[name].values() for i in v})
            == total_events
        )
        for name in FAMILY_ORDER
    }
    refine_matrix = {}
    for a in FAMILY_ORDER:
        for b in FAMILY_ORDER:
            if a != b:
                refine_matrix[f"{a}<={b}"] = refines(keys[a], keys[b])
    crossing = tuple(sorted(
        f"{a}~{b}" for i, a in enumerate(FAMILY_ORDER)
        for b in FAMILY_ORDER[i + 1:]
        if not refine_matrix[f"{a}<={b}"] and not refine_matrix[f"{b}<={a}"]
    ))
    atom_sizes = Counter(len(v) for v in cells["F_ATOM"].values())
    atoms_are_singletons = bool(events) and set(atom_sizes) == {1}
    per_world_counts = Counter(e[0] for e in events)
    f_events_at_zero = sum(1 for e in events if e[2] == "F" and e[1] == 0)
    cert_a = {
        "certificate": "A_EVENT_SPACE",
        "declared_horizon_orbits": HORIZON,
        "boundaries_scanned": boundaries,
        "worlds_in_census": n,
        "stations": stations,
        "event_tuple_shape": ("world", "moment", "tag", "ordinal", "content"),
        "event_cardinality": total_events,
        "events_by_tag": dict(sorted(Counter(e[2] for e in events).items())),
        "worlds_with_at_least_one_event": len(per_world_counts),
        "worlds_with_no_event": n - len(per_world_counts),
        "per_world_event_count_histogram_eventcount_to_worlds": dict(sorted(
            Counter(per_world_counts.values()).items()
        )),
        "per_world_event_count_min": min(per_world_counts.values()),
        "per_world_event_count_max": max(per_world_counts.values()),
        "cells_per_family": {
            name: len(cells[name]) for name in FAMILY_ORDER
        },
        "atom_cell_size_histogram": dict(sorted(atom_sizes.items())),
        "atoms_are_singletons": atoms_are_singletons,
        "sigma_algebra": {
            "atoms": "the (world, tag, ordinal) cells",
            "generated": "2^E because the atoms are singletons",
            "log2_cardinality": total_events,
        },
        "families_are_partitions": partition_ok,
        "refinement_matrix_a_refines_b": refine_matrix,
        "banktag_ordinal_refines_global_tag":
            refine_matrix["F_TAG_ORDINAL<=F_TAG"],
        "crossing_pairs_neither_refines_the_other": crossing,
        "declared_caps": {
            "register_cap_per_bank_tag_and_world": REGISTER_CAP,
            "formation_slots_per_world": 1,
            "bank_edge_events_beyond_cap_not_wire_visible":
                scan["beyond_cap"],
            "dead_wire_derivation_window_orbits":
                [DEAD_CHUNK_ORBITS, DEAD_ORBIT_ORBITS],
        },
        "composed_model_integrity": {
            "dead_wires": len(rig["dead_wires"]),
            "safe_slot_pool": len(rig["safe_pool"]),
            "slots_allocated": len(slot_of),
            "slots_in_gate_inputs":
                len(set(slot_of.values()) & rig["gate_inputs"]),
            "slots_in_gate_targets":
                len(set(slot_of.values()) & rig["gate_targets"]),
            "write_once_violations": scan["write_once_violations"],
            "dead_activation_conflicts": scan["dead_activation_conflicts"],
            "duplicate_lane_mismatches": scan["mismatches"],
            "initial_state_failures": init_fail,
        },
        "relation_to_landed_cycle867": {
            "f_events_at_moment_zero": f_events_at_zero,
            "cycle867_global_tag_writes_at_boundary_zero":
                scan["initial_global_clean_lanes"],
            "extends_not_replaces":
                f_events_at_zero == scan["initial_global_clean_lanes"],
            "statement": (
                "Cycle 867 wire-wrote its global tag only at boundary 0;"
                " the F tag here writes at each world's FIRST global-clean"
                " boundary, so the moment-0 F events are exactly the 867"
                " global writes"
            ),
        },
        "landed_ledger_crosscheck": {
            "occupation_ledger_matches_cycle863_replay": ledger_agrees,
            "formation_moments_match_cycle863_e1": formation_agrees,
            "cycle863_e1_stamps_at_horizon": len(anno_e1),
            "cycle863_duplicate_lane_mismatches": rep["mismatches"],
        },
        "finding": (
            "the realized record-write event space at the declared horizon"
            " is finite and exactly enumerated; its atoms are the"
            " (world, tag, ordinal) cells; the declared families and their"
            " refinement/crossing relations are computed, not assumed"
        ),
    }
    # Integrity gate: structural bookkeeping only, never a desired outcome.
    cert_a["pass"] = bool(
        total_events > 0
        and all(partition_ok.values())
        and atoms_are_singletons
        and len(cells["F_ATOM"]) == total_events
        and scan["write_once_violations"] == 0
        and scan["dead_activation_conflicts"] == 0
        and scan["mismatches"] == 0
        and rep["mismatches"] == 0
        and init_fail == 0
        and len(set(slot_of.values()) & rig["gate_inputs"]) == 0
        and len(set(slot_of.values()) & rig["gate_targets"]) == 0
        and ledger_agrees
        and formation_agrees
    )

    # ---- Certificate B: measure-candidate inventory ------------------------
    nums, dens, meta, per_world, supported, common = build_candidates(
        events, scan["occ_global"], scan["formed"], boundaries
    )
    disjoint_families = tuple(
        name for name in FAMILY_ORDER if partition_ok[name]
    )
    totals_num = {
        name: sum(nums[name]) for name in CANDIDATE_NAMES
    }
    contents = [e[4] for e in events]
    whole_diversity = len(set(contents))

    def cell_masses(fam):
        """Exact integer cell masses for every additive candidate."""
        out = {}
        for name in CANDIDATE_NAMES:
            vec = nums[name]
            out[name] = {
                key: sum(vec[i] for i in idx)
                for key, idx in cells[fam].items()
            }
        return out

    masses_by_family = {fam: cell_masses(fam) for fam in disjoint_families}
    diversity_by_family = {
        fam: {
            key: len({contents[i] for i in idx})
            for key, idx in cells[fam].items()
        }
        for fam in disjoint_families
    }

    inventory = {}
    for name in CANDIDATE_NAMES:
        add_rows = {}
        witness = None
        for fam in disjoint_families:
            cell_sum = sum(masses_by_family[fam][name].values())
            add_rows[fam] = (cell_sum == totals_num[name])
            if not add_rows[fam] and witness is None:
                witness = {
                    "family": fam,
                    "sum_over_cells": cell_sum,
                    "value_on_whole_space": totals_num[name],
                }
        for fam in ("F_TAG", "F_TAG_ORDINAL"):
            cell_list = sorted(cells[fam])
            ok = True
            for i in range(len(cell_list) - 1):
                a_idx = cells[fam][cell_list[i]]
                b_idx = cells[fam][cell_list[i + 1]]
                union = sum(nums[name][j] for j in a_idx + b_idx)
                if union != (masses_by_family[fam][name][cell_list[i]]
                             + masses_by_family[fam][name][cell_list[i + 1]]):
                    ok = False
                    break
            add_rows[f"{fam}_pairwise_disjoint_unions"] = ok
        inventory[name] = {
            "definition": meta[name]["definition"],
            "record_native_source": meta[name]["record_native_source"],
            "finite_additivity_over_certified_disjoint_families":
                all(add_rows.values()),
            "additivity_per_family": add_rows,
            "additivity_failure_witness": witness,
            "normalizable": totals_num[name] > 0,
            "total_mass": fr(Fraction(totals_num[name], dens[name])),
            "support_faithful_disclosed_extra_diagnostic":
                all(v > 0 for v in nums[name]),
            "zero_weight_events": sum(1 for v in nums[name] if v == 0),
        }
        inventory[name]["admissible"] = bool(
            inventory[name][
                "finite_additivity_over_certified_disjoint_families"]
            and inventory[name]["normalizable"]
        )

    control_rows = {}
    control_witness = None
    for fam in disjoint_families:
        cell_sum = sum(diversity_by_family[fam].values())
        control_rows[fam] = (cell_sum == whole_diversity)
        if not control_rows[fam] and control_witness is None:
            control_witness = {
                "family": fam,
                "sum_over_cells": cell_sum,
                "value_on_whole_space": whole_diversity,
            }
    inventory[CONTROL_NAME] = {
        "definition": meta[CONTROL_NAME]["definition"],
        "record_native_source": meta[CONTROL_NAME]["record_native_source"],
        "finite_additivity_over_certified_disjoint_families":
            all(control_rows.values()),
        "additivity_per_family": control_rows,
        "additivity_failure_witness": control_witness,
        "normalizable": False,
        "normalizability_reading": (
            "a distinct-content count is not a normalizable measure: it"
            " has no additive total to divide by"
        ),
        "total_mass": whole_diversity,
        "support_faithful_disclosed_extra_diagnostic": all(
            v > 0 for v in diversity_by_family["F_ATOM"].values()
        ),
        "zero_weight_events": 0,
        "admissible": False,
    }

    perms, perm_ok = monitor_phase_action(census, stations)
    world_orbits = group_orbits(perms, n) if perm_ok else ()
    atom_shape: dict[int, list] = {lane: [] for lane in range(n)}
    for lane, _moment, tag, ordinal, _content in events:
        atom_shape[lane].append((tag, ordinal))
    atom_shape = {lane: tuple(sorted(v)) for lane, v in atom_shape.items()}
    action_well_defined_on_atoms = perm_ok and all(
        atom_shape[perm[lane]] == atom_shape[lane]
        for perm in perms for lane in range(n)
    )
    bank_keys = sorted(
        k for k in cells["F_TAG_ORDINAL"] if k[1] == "B0"
    )
    for name in CANDIDATE_NAMES + (CONTROL_NAME,):
        if name == CONTROL_NAME:
            world_cell = diversity_by_family["F_WORLD"]
            tag_cell = diversity_by_family["F_TAG_ORDINAL"]
            zero = 0
        else:
            world_cell = masses_by_family["F_WORLD"][name]
            tag_cell = masses_by_family["F_TAG_ORDINAL"][name]
            zero = 0
        covariant_world = all(
            world_cell.get(("w", orbit[0]), zero)
            == world_cell.get(("w", x), zero)
            for orbit in world_orbits for x in orbit
        ) if perm_ok else None
        bank_swap = all(
            tag_cell.get(key, zero)
            == tag_cell.get(("to", "B1", key[2]), zero)
            for key in bank_keys
        )
        inventory[name]["permutation_covariance"] = {
            "landed_monitor_phase_group_on_worlds": covariant_world,
            "bank_label_swap_on_tag_ordinal_cells": bank_swap,
            "covariant_under_both": bool(covariant_world and bank_swap),
        }

    admissible = tuple(
        name for name in sorted(inventory) if inventory[name]["admissible"]
    )
    cert_b = {
        "certificate": "B_MEASURE_CANDIDATE_INVENTORY",
        "no_selection_statement": (
            "this certificate enumerates record-native weightings and"
            " certifies admissibility ONLY; it does NOT select among them"
            " and asserts no probability interpretation for any of them"
        ),
        "certified_disjoint_families_used": disjoint_families,
        "common_within_world_denominator": common,
        "landed_symmetries": {
            "monitor_phase_group": (
                "Cycle-856 monitor-phase relabelling: positions ->"
                f" positions + m (mod {stations}), a Z_{stations} action"
                " on worlds"
            ),
            "action_is_a_census_bijection": perm_ok,
            "world_orbit_count": len(world_orbits),
            "world_orbit_size_histogram": dict(sorted(
                Counter(len(o) for o in world_orbits).items()
            )),
            "action_well_defined_on_atoms": action_well_defined_on_atoms,
            "bank_label_swap": "B0 <-> B1 on (tag, ordinal) cells",
        },
        "candidates": inventory,
        "admissible_candidates": admissible,
        "inadmissible_candidates": tuple(
            name for name in sorted(inventory)
            if not inventory[name]["admissible"]
        ),
        "additivity_reading": (
            "every event-level weight is finitely additive over ANY"
            " disjoint family by construction; DISJOINTNESS is what is"
            " load-bearing, which is why the declared negative control"
            " (a non-additive record-native set function) is carried in"
            " the inventory and why the independent checker attacks the"
            " certification with overlapping pseudo-families"
        ),
        "finding": (
            "the inventory is the deliverable: exact pass/fail per"
            " candidate per axiom, with selection left as the named open"
            " gate"
        ),
    }
    cert_b["pass"] = bool(
        perm_ok
        and len(inventory) == len(CANDIDATE_NAMES) + 1
        and all(
            set(row) >= {
                "finite_additivity_over_certified_disjoint_families",
                "normalizable", "permutation_covariance", "admissible",
            }
            for row in inventory.values()
        )
        and all(
            inventory[name]["admissible"] == bool(
                inventory[name][
                    "finite_additivity_over_certified_disjoint_families"]
                and inventory[name]["normalizable"]
            )
            for name in inventory
        )
        and inventory[CONTROL_NAME]["additivity_failure_witness"] is not None
    )

    # ---- Certificate C: the fraction ledger --------------------------------
    ledger = {}
    fraction_tables = {}
    sums_ok = True
    table_bytes_spent = 0
    for name in admissible:
        ledger[name] = {}
        for fam in disjoint_families:
            cell_map = masses_by_family[fam][name]
            total = totals_num[name]
            rows = [
                (compact(list(key)), Fraction(value, total))
                for key, value in sorted(cell_map.items())
            ]
            fraction_tables[(name, fam)] = dict(rows)
            ordered = sorted(rows, key=lambda kv: (-kv[1], kv[0]))
            emitted = {
                "label": FRACTION_LABEL,
                "cells": len(rows),
                "sum_of_fractions": fr(sum((v for _k, v in rows),
                                           Fraction(0))),
                "exact_table_digest": digest([[k, fr(v)] for k, v in rows]),
                "distinct_values": len({v for _k, v in rows}),
                "min_fraction": fr(min(v for _k, v in rows)),
                "max_fraction": fr(max(v for _k, v in rows)),
                "zero_mass_cells": sum(1 for _k, v in rows if v == 0),
                "largest_cells": {
                    k: fr(v) for k, v in ordered[:TOP_CELLS_REPORTED]
                },
            }
            if emitted["sum_of_fractions"] != "1/1":
                sums_ok = False
            if len(rows) <= FULL_TABLE_CELL_CAP:
                table = {k: fr(v) for k, v in rows}
                blob = len(compact(table).encode())
                if (blob <= TABLE_BYTE_CAP
                        and table_bytes_spent + blob
                        <= TOTAL_TABLE_BYTE_BUDGET):
                    emitted["table"] = table
                    table_bytes_spent += blob
                else:
                    emitted["full_table_not_inlined"] = {
                        "reason": (
                            "declared stdout byte budget; the exact table"
                            " is pinned by exact_table_digest and is"
                            " recomputed cell-for-cell by the independent"
                            " checker"
                        ),
                        "serialized_bytes": blob,
                        "per_table_cap": TABLE_BYTE_CAP,
                        "total_budget": TOTAL_TABLE_BYTE_BUDGET,
                    }
            ledger[name][fam] = emitted

    all_pairs = [
        (a, b) for i, a in enumerate(admissible) for b in admissible[i + 1:]
    ]
    disagreement = {}
    for a, b in all_pairs:
        witness = None
        for fam in disjoint_families:
            ta, tb = fraction_tables[(a, fam)], fraction_tables[(b, fam)]
            for key in sorted(ta):
                if ta[key] != tb[key]:
                    witness = {"family": fam, "cell": key,
                               a: fr(ta[key]), b: fr(tb[key])}
                    break
            if witness:
                break
        disagreement[f"{a}|{b}"] = {
            "disagree": witness is not None,
            "first_witness_cell": witness,
        }
    atom_disagreement = {}
    for a, b in all_pairs:
        ta, tb = fraction_tables[(a, "F_ATOM")], fraction_tables[(b, "F_ATOM")]
        atom_disagreement[f"{a}|{b}"] = {
            "differing_atoms": sum(1 for key in ta if ta[key] != tb[key]),
            "atoms_total": len(ta),
        }
    cert_c = {
        "certificate": "C_FRACTION_LEDGER",
        "label_on_every_number": FRACTION_LABEL,
        "not_a_probability_statement": (
            "these are exact event-fraction bookkeeping ratios of a"
            " declared weighting over a finite certified event space;"
            " no occurrence rule, no probability, and no update law is"
            " asserted or implied by any number in this table"
        ),
        "admissible_candidates_tabulated": admissible,
        "families_tabulated": disjoint_families,
        "inlined_table_bytes": table_bytes_spent,
        "inlined_table_byte_budget": TOTAL_TABLE_BYTE_BUDGET,
        "tables": ledger,
        "pairwise_disagreement": disagreement,
        "atom_level_disagreement_counts": atom_disagreement,
        "discriminating_pairs": tuple(
            k for k, v in sorted(disagreement.items()) if v["disagree"]
        ),
        "indistinguishable_pairs": tuple(
            k for k, v in sorted(disagreement.items()) if not v["disagree"]
        ),
        "finding": (
            "the atom families on which admissible candidates already"
            " differ are the future experiment surface; pairs that agree"
            " on every certified family are not separated by any"
            " event-fraction bookkeeping over those families"
        ),
    }
    cert_c["pass"] = bool(
        sums_ok
        and len(disagreement) == len(all_pairs)
        and all(
            ledger[name][fam]["sum_of_fractions"] == "1/1"
            for name in admissible for fam in disjoint_families
        )
        and all(
            (v["first_witness_cell"] is not None) == v["disagree"]
            for v in disagreement.values()
        )
    )

    # ---- Certificate D: the boundary --------------------------------------
    axiom_path = AUDIT_INPUT_PATHS[3]
    axiom_bytes = (ROOT / axiom_path).read_bytes()
    needle_present = EXCLUSION_NEEDLE in axiom_bytes.decode("utf-8")
    cert_d = {
        "certificate": "D_BOUNDARY_WHAT_IS_NOT_SUPPLIED",
        "pinned_source": axiom_path,
        "pinned_sha256": sha256(axiom_bytes).hexdigest(),
        "pinned_git_blob": git_blob(axiom_bytes),
        "section": "Open Gates Outside The Axioms",
        "verbatim_exclusion_list": EXCLUSION_NEEDLE,
        "verbatim_present_in_pinned_source": needle_present,
        "block_boundary": BOUNDARY_STATEMENT,
        "explicitly_not_supplied_here": (
            "an occurrence rule (which admissible possibility a new record"
            " locks, at which site, with what weight, or at what rate)",
            "a probability measure, or any probability interpretation of"
            " the emitted fractions",
            "an update law",
            "a selection among the measure candidates",
            "a Born rule, or any amplitude-to-weight bridge",
        ),
        "finding": (
            "the block supplies a finite sample space and an admissibility"
            " inventory; the exclusion list quoted above is untouched by"
            " anything in this cycle"
        ),
    }
    cert_d["pass"] = bool(
        needle_present
        and sha256(axiom_bytes).hexdigest() == EXPECTED_SHA256[axiom_path]
        and git_blob(axiom_bytes) == EXPECTED_GIT_BLOBS[axiom_path]
    )

    # ---- E: controls, including determinism --------------------------------
    short_a = composed_scan(program, census, states, rig, DETERMINISM_ORBITS)
    short_b = composed_scan(program, census, states, rig, DETERMINISM_ORBITS)
    det_a = digest(short_a["events"])
    det_b = digest(short_b["events"])
    prefix = [e for e in events if e[1] <= DETERMINISM_ORBITS * stations]
    prefix_matches = digest(prefix) == det_a
    runtime = round(monotonic() - started, 3)
    cert_e = {
        "certificate": "E_CONTROLS",
        "source_controls": controls,
        "determinism": {
            "short_scan_orbits": DETERMINISM_ORBITS,
            "repeat_digest_equal": det_a == det_b,
            "full_run_prefix_matches_short_scan": prefix_matches,
            "short_scan_events": len(short_a["events"]),
            "full_run_prefix_events": len(prefix),
        },
        "runtime_seconds": runtime,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "event_space_digest": digest(events),
    }
    cert_e["pass"] = bool(
        controls["pass"] and det_a == det_b and prefix_matches
        and runtime < AUDIT_TIMEOUT_SEC
    )

    checks = {
        "A_EVENT_SPACE": cert_a["pass"],
        "B_MEASURE_CANDIDATE_INVENTORY": cert_b["pass"],
        "C_FRACTION_LEDGER": cert_c["pass"],
        "D_BOUNDARY_WHAT_IS_NOT_SUPPLIED": cert_d["pass"],
        "E_CONTROLS": cert_e["pass"],
    }
    lines = [
        "CYCLE878_EVENT_SPACE_GROUNDWORK",
        "BORN_GROUNDWORK_STRUCTURAL_ONLY_NO_PROBABILITY_POSTULATE",
        "EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY",
    ]
    for name, payload in (
        ("A_EVENT_SPACE", cert_a),
        ("B_MEASURE_CANDIDATE_INVENTORY", cert_b),
        ("C_FRACTION_LEDGER", cert_c),
        ("D_BOUNDARY_WHAT_IS_NOT_SUPPLIED", cert_d),
        ("E_CONTROLS", cert_e),
    ):
        lines.append(
            f"CERTIFICATE {name} {'PASS' if payload['pass'] else 'FAIL'} "
            + compact(payload)
        )
    summary = {
        "checks": checks,
        "cycle": 878,
        "event_cardinality": total_events,
        "admissible_candidates": admissible,
        "discriminating_pairs": cert_c["discriminating_pairs"],
        "runtime_seconds": runtime,
        "pass": all(checks.values()),
    }
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append(
        "CYCLE878_EVENT_SPACE_GROUNDWORK_"
        + ("PASS" if summary["pass"] else "HONEST_FAIL")
    )
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
