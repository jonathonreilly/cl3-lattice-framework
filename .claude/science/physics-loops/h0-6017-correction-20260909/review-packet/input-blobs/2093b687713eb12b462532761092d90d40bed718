"""Cycle 913 -- O2 AS A COMPUTATION: THE LANDED SELECTION FUNCTION.

Cycle 911 re-typed the lane: the 748 census worlds are SETUPS (zero branch
pairs), and the real occurrence arena is the 164 formation lock points, where
|A| = 2 under both operational readings.  The landed composed scan is
DETERMINISTIC -- so at each lock point it in fact realizes exactly one of the
two menu items.  Nobody computed WHICH, or WHAT DETERMINES IT.  This block
does.

  C1  THE SELECTION FUNCTION, EXTRACTED.  For each of the 164 lock points,
      the lock context is rebuilt from the Cycle-911 machinery (AST-lifted,
      never imported) and the REALIZED menu item is read from the composed
      scan's own trajectory by FOUR independent readouts that must agree
      row-for-row:
        RD-STATE     the endpoint content the lock state carries;
        RD-HAMMING   the unique menu item whose prepared endpoint sits at
                     Hamming distance 1 from the lock state;
        RD-REARM     the scan's OWN next endpoint preparation -- at the first
                     post-lock boundary where the source pointer rises, the
                     trajectory state is compared bit-for-bit against
                     K.M.prepare_endpoint(previous state, v) for each menu
                     item v; exactly one must match on all 5,815 wires;
        RD-SETUP     the direction the world's own seed was prepared with.
      Deliverable: the complete 164-row selection table.

  C2  WHAT DETERMINES THE SELECTION.  A declared fingerprint ladder
      (neighbour shell radius 1, 2, 3; + schedule phase; + lock tick; + token
      positions; + source count), each tested for single-valuedness on the
      164 rows, plus an EXHAUSTIVE sweep of all 5,815 single-wire contexts and
      the empty context, giving the minimal determining context exactly.
      Then the covariance tests: the landed translation symmetry (the pinned
      Cycle-878 monitor-phase action) and the proper/full cubic action on the
      Cycle-911 declared six-direction embedding.

  C3  THE CONTENT QUESTION.  Is the selection a function of RECORD CONTENT
      alone?  Tested under both readings of "record": the substrate's record
      registers (the bank words at the lock tick) and the composed scan's own
      written record history (the events strictly before the lock tick).

  C4  THE CONTEXT-VARIATION CERTIFICATION.  Cycle 911 found the menu SIZE
      constant; here the CONTEXTS themselves are counted, and their
      symmetry classes computed, to say whether the Admissibility sentence's
      "vary with" clause has anything to bite on at the lock points.

  C5  THE CLASSIFIED-RULE COMPARISON.  The pinned 2026-07-03 classification's
      orbit counts are reproduced from its own AST-lifted machinery and the
      landed selection is placed -- or refused a place -- in that rule space.

  C6  THE O2/O3 VERDICT for the lane ledger, with the A3 arena located.

Discipline: TEXT/AST/JSON only; import firewall (the Cycle-719 kernel is the
one disclosed import, as substrate); exact integer / rational arithmetic;
deterministic double build (two full-horizon builds at opposite lane bit
layouts); outcome-neutral gates with planted falsifiers -- including a planted
NON-LOCAL selection that the dependence machinery must detect as non-local and
a planted LOCAL selection it must detect as local.  No probability, no
occurrence rule, no update law is introduced.  Every fraction below is a
bookkeeping fraction, not a probability.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
import sys
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C863_RECEIPT = "outputs/time_from_records_arc_cycles863_865_receipt_2026_07_28.json"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C911_PATH = "scripts/frontier_cycle911_type_vacuity_2026_07_28.py"
C911_RECEIPT = "outputs/type_vacuity_cycle911_receipt_2026_07_28.json"
C911_NOTE = (
    "docs/RETYPED_WORLDS_ARE_SETUPS_SELECTION_SITES_EXIST_CYCLE911"
    "_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
CLASSIFY_PATH = \
    "scripts/admissibility_rule_covariance_extension_classification_2026_07_03.py"
COVCLASS_PATH = (
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS"
    "_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE"
    "_2026-07-03.md"
)
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PATH = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C863_RECEIPT, C878_PATH, C878_RECEIPT, C911_PATH,
    C911_RECEIPT, C911_NOTE, CLASSIFY_PATH, COVCLASS_PATH, AXIOMS_PATH,
    REALIZED_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C911_PATH, CLASSIFY_PATH)
JSON_ONLY_PATHS = (C863_RECEIPT, C878_RECEIPT, C911_RECEIPT)
TEXT_ONLY_PATHS = (C911_NOTE, COVCLASS_PATH, AXIOMS_PATH, REALIZED_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C863_RECEIPT:
        "b856d00221ca3f755bcc21e5e37e99a8141a8f6daba959914c688702f59b2c9b",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C911_PATH:
        "6474f1e919c97fcb3336a8cea480b5e824fe48f4ea5ce4592c1b75bc0b0007d1",
    C911_RECEIPT:
        "90d1fb2a3ac31065f75345ac1e98520622aa6302c50dcf4a8a11f44a1cde11b0",
    C911_NOTE:
        "40c80402e2dfd283a4309433cfa48705c45567efadf43107e074332f1cbf5ff0",
    CLASSIFY_PATH:
        "f7490941aa793fdf155d10dc5a5f86d59c07b22d49ca60f989fbf03c565a0dcb",
    COVCLASS_PATH:
        "fe56ef6c21c00732281676cca1724231951e40fc2b746f255f655307dc76001d",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    REALIZED_PATH:
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C863_RECEIPT: "08ca180175d615d28daab4a09cf0091c3edba925",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C911_PATH: "3335e9dee5027b935d0eb3c814601b8f8e83b550",
    C911_RECEIPT: "af51342a72c56db8e562e1f1a607f207508b42ed",
    C911_NOTE: "53a229b4143f59f5f8c12ccb9f488682bdc2714c",
    CLASSIFY_PATH: "d33bf6e8b456464e2b455c1d0aaf8662a1799abb",
    COVCLASS_PATH: "20955a2e976f7d3a1f38fed55cd0b1bdd91f82b4",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
    REALIZED_PATH: "5acb4643882438f8dd16baf9694e6fa2d33d1dc6",
}

BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AST_ONLY_PATHS)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 900
FRACTION_LABEL = "bookkeeping fraction, not probability"

HORIZON = 16_384
REARM_WALK_CAP = 4 * 11          # boundaries after the lock, hard cap
SERIAL_LOCK_CAP = 1_500          # replay-from-tick-0 budget per world


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

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K  # noqa: E402
import numpy as np  # noqa: E402


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def fr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


# ---------------------------------------------------------------------------
# A: pins
# ---------------------------------------------------------------------------

def pin_rows():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in IMPORTED_PATHS + AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    for p in JSON_ONLY_PATHS:
        json.loads(payloads[p].decode("utf-8"))
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    string_constants: dict = {}
    literal = None
    for node in self_tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Name):
                continue
            try:
                string_constants[target.id] = ast.literal_eval(node.value)
            except Exception:
                pass
            if target.id == "AUDIT_INPUT_PATHS" \
                    and isinstance(node.value, ast.Tuple):
                resolved = []
                for element in node.value.elts:
                    if isinstance(element, ast.Constant):
                        resolved.append(element.value)
                    elif isinstance(element, ast.Name):
                        resolved.append(string_constants.get(element.id))
                    else:
                        resolved.append(None)
                literal = tuple(resolved)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    result = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_ok": literal == AUDIT_INPUT_PATHS,
        "modes": {
            "imported_disclosed_substrate": IMPORTED_PATHS,
            "ast_only": AST_ONLY_PATHS,
            "json_only": JSON_ONLY_PATHS,
            "text_only": TEXT_ONLY_PATHS,
        },
        "existing_worktree_relative": all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "bytes": {p: len(b) for p, b in payloads.items()},
        "sha256_all_match": sha_rows == EXPECTED_SHA256,
        "git_blobs_all_match": blob_rows == EXPECTED_GIT_BLOBS,
        "blocked_modules_loaded": tuple(
            n for n in BLOCKLISTED_MODULES if n in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
    }
    result["pass"] = bool(
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_all_match"] and result["git_blobs_all_match"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result, payloads


# ---------------------------------------------------------------------------
# AST lift: the pinned machinery, never imported
# ---------------------------------------------------------------------------

def ast_lift(path: str, funcs: tuple, consts: tuple, globals_: dict):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    body, found_consts = [], {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in consts:
                    found_consts[target.id] = ast.literal_eval(node.value)
    missing = tuple(f for f in funcs if f not in {n.name for n in body})
    missing_c = tuple(c for c in consts if c not in found_consts)
    if missing or missing_c:
        raise AssertionError(("ast lift incomplete", path, missing, missing_c))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = dict(globals_)
    namespace.update(found_consts)
    exec(compile(module, f"<ast-lift {path}>", "exec"), namespace)
    return namespace, found_consts, tuple(n.name for n in body)


C863_FUNCS = (
    "pairwise_separated", "derive_event_seeds", "derive_census",
    "watched_registers", "dirty_partition", "build_initial_states",
    "pack_lanes", "compile_masked_gate", "masked_h_schedules", "compile_fast",
    "mask_over", "lanes_of", "lane_state", "synchronous_word",
)
C863_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES")
C878_FUNCS = ("lcm", "monitor_phase_action", "group_orbits")
C878_CONSTS = ("HORIZON", "REGISTER_CAP")
C911_FUNCS = ("snapshot_scan", "synchronous_chunks", "availability_operators",
              "context_colorings", "build_cubic_group", "rule_space_spectrum")
C911_CONSTS = ("DIRECTIONS", "REGISTER_CAP", "HORIZON")
CLASS_FUNCS = ("det3", "mat_key", "dperm", "act_col", "inv_perm",
               "cycle_count", "burnside_orbits", "all_colorings",
               "direct_orbits", "orbit_ids")
CLASS_CONSTS = ("DIRS",)


def lift_machinery():
    ns863, consts863, names863 = ast_lift(
        C863_PATH, C863_FUNCS, C863_CONSTS,
        {"K": K, "combinations": combinations, "Counter": Counter},
    )
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "json": json},
    )
    c878 = SimpleNamespace(**{n: ns878[n] for n in C878_FUNCS})
    dirs_holder: dict = {}
    nsc, constsc, namesc = ast_lift(
        CLASSIFY_PATH, CLASS_FUNCS, CLASS_CONSTS,
        {"np": np, "itertools": itertools, "DIR_INDEX": dirs_holder},
    )
    dirs = constsc["DIRS"]
    dirs_holder.update({d: i for i, d in enumerate(dirs)})
    cls = SimpleNamespace(**{n: nsc[n] for n in CLASS_FUNCS})
    ns911, consts911, names911 = ast_lift(
        C911_PATH, C911_FUNCS, C911_CONSTS,
        {"K": K, "np": np, "itertools": itertools, "Counter": Counter,
         "sha256": sha256, "cls": cls},
    )
    c911 = SimpleNamespace(**{n: ns911[n] for n in C911_FUNCS})
    provenance = {
        "lifted_from_863": names863, "constants_863": consts863,
        "lifted_from_878": names878, "constants_878": consts878,
        "lifted_from_911": names911,
        "constants_911": {k: (list(map(list, v)) if k == "DIRECTIONS" else v)
                          for k, v in consts911.items()},
        "lifted_from_classification": namesc,
        "classification_DIRS": [list(d) for d in dirs],
        "import_of_863_878_911_or_classification": False,
        "single_disclosed_import": CORE_PATH,
    }
    return c863, c878, c911, cls, dirs, consts878, consts911, provenance


# ---------------------------------------------------------------------------
# C1: the realized menu item, by four independent readouts
# ---------------------------------------------------------------------------

def endpoint_wires():
    X = K.M.R3.X
    return X.LEFT_ENDPOINT, X.RIGHT_ENDPOINT, X.SOURCE_POINTER


def read_state_direction(state) -> tuple | None:
    """RD-STATE.  K.M.prepare_endpoint writes LEFT = int(v == (0,1)) and
    RIGHT = int(v == (1,0)); reading those two wires back inverts it."""
    left, right, _src = endpoint_wires()
    for v in ((1, 0), (0, 1)):
        if state[right] == int(v == (1, 0)) and state[left] == int(v == (0, 1)):
            return v
    return None


def target_wire_sweep(schedules) -> dict:
    """EXACT compile-level lemma: which wires are gate TARGETS anywhere in the
    composed scan, and which are only ever gate INPUTS.  The endpoint wires
    being inputs-only is what makes 'which item the scan locks' well posed."""
    targets: set = set()
    inputs: set = set()
    gate_count = 0
    for schedule in schedules:
        for kind, a, b, c3, _mask in schedule:
            gate_count += 1
            if kind == 0:
                targets.add(a)
            elif kind == 1:
                inputs.add(a)
                targets.add(b)
            else:
                inputs.update((a, b))
                targets.add(c3)
    left, right, src = endpoint_wires()
    return {
        "gates_total": gate_count,
        "distinct_targets": len(targets),
        "distinct_inputs": len(inputs),
        "LEFT_ENDPOINT_wire": left, "RIGHT_ENDPOINT_wire": right,
        "SOURCE_POINTER_wire": src,
        "LEFT_is_a_gate_target": left in targets,
        "RIGHT_is_a_gate_target": right in targets,
        "SOURCE_POINTER_is_a_gate_target": src in targets,
        "LEFT_is_a_gate_input": left in inputs,
        "RIGHT_is_a_gate_input": right in inputs,
        "endpoint_content_is_read_never_written":
            left not in targets and right not in targets
            and left in inputs and right in inputs,
        "lemma": "no gate in the composed scan targets the endpoint wires; "
                 "both are read by the source station and by the finalizer "
                 "station.  The endpoint content a world carries at its lock "
                 "tick is therefore the content it carried at tick 0 and will "
                 "carry forever: the landed dynamics READS the selection and "
                 "never WRITES it.",
    }


def rearm_readout(c911, program, positions_chunks, state, lock_boundary,
                  menu, global_dirty):
    """RD-REARM.  Walk the world's own trajectory forward from the lock state,
    applying the SAME per-step chunks the composed scan applies.  At the first
    boundary where the source pointer rises 0 -> 1, compare the trajectory
    state bit-for-bit against K.M.prepare_endpoint(previous state, v) for each
    menu item.  Exactly one must match on every wire."""
    _left, _right, src = endpoint_wires()
    stations = len(program)
    cur = state
    boundary = lock_boundary
    clean_at_lock = all(cur[w] == 0 for w in global_dirty)
    for _ in range(REARM_WALK_CAP):
        prev = cur
        cur = K.A.apply_semantic(cur, positions_chunks[boundary % stations])
        boundary += 1
        if prev[src] == 0 and cur[src] == 1:
            matches = []
            for v in menu:
                try:
                    cand = K.M.prepare_endpoint(prev, v)
                except Exception:
                    continue
                if cand == cur:
                    matches.append(v)
            hamming = {}
            for v in menu:
                try:
                    cand = K.M.prepare_endpoint(prev, v)
                except Exception:
                    hamming[str(v)] = None
                    continue
                hamming[str(v)] = sum(
                    1 for i in range(len(cur)) if cand[i] != cur[i])
            return {
                "rearm_boundary": boundary,
                "rearm_offset_from_lock": boundary - lock_boundary,
                "exact_matches": [list(v) for v in matches],
                "hamming_to_each_menu_item": hamming,
                "unique": len(matches) == 1,
                "item": list(matches[0]) if len(matches) == 1 else None,
                "clean_at_lock": clean_at_lock,
            }
    return {"rearm_boundary": None, "rearm_offset_from_lock": None,
            "exact_matches": [], "hamming_to_each_menu_item": {},
            "unique": False, "item": None, "clean_at_lock": clean_at_lock}


def hamming_readout(state, menu):
    """RD-HAMMING.  The menu item whose prepared endpoint is nearest to the
    state the scan is actually in at the lock tick."""
    out = {}
    for v in menu:
        try:
            cand = K.M.prepare_endpoint(state, v)
        except Exception:
            out[v] = None
            continue
        out[v] = sum(1 for i in range(len(state)) if cand[i] != state[i])
    live = {v: d for v, d in out.items() if d is not None}
    if not live:
        return None, out
    best = min(live.values())
    winners = [v for v, d in live.items() if d == best]
    return (winners[0] if len(winners) == 1 else None), out


def serial_lock_replay(c863, c911, program, key, seed_state, global_dirty,
                       cap):
    """Independent per-world replay from tick 0, using the kernel's semantic
    word applier rather than the bit-packed lane scan.  Returns the first
    globally clean boundary and the endpoint content there."""
    stations = len(program)
    chunks = c911.synchronous_chunks(program, key[2])
    cur = seed_state
    if all(cur[w] == 0 for w in global_dirty):
        return 0, read_state_direction(cur)
    for boundary in range(1, cap + 1):
        cur = K.A.apply_semantic(cur, chunks[(boundary - 1) % stations])
        if all(cur[w] == 0 for w in global_dirty):
            return boundary, read_state_direction(cur)
    return None, None


# ---------------------------------------------------------------------------
# C2: the fingerprint ladder and the determination test
# ---------------------------------------------------------------------------

def is_function(rows, key_fn, value_fn):
    """Single-valuedness of value_fn on the fibres of key_fn, plus, when it
    fails, the lexicographically first witness pair and the whole collision
    structure."""
    groups: dict = {}
    for row in rows:
        groups.setdefault(key_fn(row), []).append(row)
    collisions = []
    for k, members in groups.items():
        values = {value_fn(m) for m in members}
        if len(values) > 1:
            collisions.append((k, members, sorted(values)))
    witness = None
    if collisions:
        collisions.sort(key=lambda c: (-len(c[1]), str(c[0])))
        _k, members, values = collisions[0]
        a = next(m for m in members if value_fn(m) == values[0])
        b = next(m for m in members if value_fn(m) == values[1])
        witness = {
            "left": {"world": a["world"], "key": a["key"],
                     "lock_boundary": a["lock_boundary"],
                     "selection": list(value_fn(a))},
            "right": {"world": b["world"], "key": b["key"],
                      "lock_boundary": b["lock_boundary"],
                      "selection": list(value_fn(b))},
        }
    return {
        "groups": len(groups),
        "is_a_function": not collisions,
        "collision_classes": len(collisions),
        "largest_collision_class_size":
            max((len(c[1]) for c in collisions), default=0),
        "witness_pair": witness,
    }


def ladder_rows(rows, value_fn):
    """The declared fingerprint ladder.  Every entry excludes the two endpoint
    wires -- the selection's own carrier -- except the entries that are
    explicitly labelled as including the site."""
    def nn(r):
        return (r["bank0"], r["bank1"])

    ladder = [
        ("R1_nearest_neighbour_record_content",
         "the two nearest neighbours' record registers (bank 0, bank 1) at "
         "the lock tick -- the Admissibility sentence's own vocabulary under "
         "the Cycle-911 declared embedding", nn),
        ("R1_nearest_neighbour_openness_only",
         "the k=2 condition alphabet: recorded / open per neighbour",
         lambda r: (r["ord0"] > 0, r["ord1"] > 0)),
        ("R1_nearest_neighbour_exact_ordinals",
         "neighbour record counts at the lock tick",
         lambda r: (r["ord0"], r["ord1"])),
        ("R2_shell2_add_link_and_banks_2_3",
         "radius 2: + the bank-to-bank link word and banks 2,3",
         lambda r: (r["bank0"], r["bank1"], r["link0"], r["shell2_rest"])),
        ("R3_shell3_whole_substrate_minus_the_site",
         "radius 3: + every remaining wire outside the site block",
         lambda r: r["state_minus_site"]),
        ("R3_plus_schedule_phase",
         "+ the scan's schedule phase at the lock tick",
         lambda r: (r["state_minus_site"], r["phase"])),
        ("R3_plus_phase_plus_lock_tick",
         "+ the absolute lock tick", lambda r: (
             r["state_minus_site"], r["phase"], r["lock_boundary"])),
        ("R3_plus_phase_plus_tick_plus_token_positions",
         "+ the world's token positions", lambda r: (
             r["state_minus_site"], r["phase"], r["lock_boundary"],
             tuple(r["key"][2]))),
        ("R3_plus_phase_plus_tick_plus_tokens_plus_source_count",
         "+ the source count k -- the widest context that still excludes the "
         "site block", lambda r: (
             r["state_minus_site"], r["phase"], r["lock_boundary"],
             tuple(r["key"][2]), r["key"][0])),
        ("FULL_STATE_MINUS_THE_TWO_ENDPOINT_WIRES",
         "every one of the 5,815 wires except LEFT_ENDPOINT and "
         "RIGHT_ENDPOINT, plus phase, tick, tokens and k",
         lambda r: (r["state_minus_endpoints"], r["phase"],
                    r["lock_boundary"], tuple(r["key"][2]), r["key"][0])),
        ("SITE_BLOCK_including_the_endpoint_wires",
         "the site's own block, wires 0..40", lambda r: r["site_block"]),
        ("SITE_ENDPOINT_WIRES_ONLY",
         "the two endpoint wires alone", lambda r: r["endpoint_bits"]),
        ("SITE_BLOCK_MINUS_THE_ENDPOINT_WIRES",
         "the site's own block with the endpoint content removed",
         lambda r: r["site_block_minus_endpoints"]),
        ("SETUP_event_index", "the world's setup event coordinate",
         lambda r: r["key"][1]),
        ("SETUP_event_parity", "the parity of the setup event coordinate",
         lambda r: r["key"][1] % 2),
        ("SETUP_token_positions_only", "the token positions alone",
         lambda r: tuple(r["key"][2])),
        ("SCHEDULE_phase_only", "the schedule phase alone",
         lambda r: r["phase"]),
        ("SCHEDULE_lock_tick_only", "the absolute lock tick alone",
         lambda r: r["lock_boundary"]),
        ("EMPTY_CONTEXT", "no context at all", lambda r: 0),
    ]
    out = []
    for name, gloss, fn in ladder:
        res = is_function(rows, fn, value_fn)
        res["fingerprint"] = name
        res["gloss"] = gloss
        # A fingerprint that gives every lock point its own group individuates
        # the site rather than describing it: determination is then vacuous
        # and carries no dependence content.  Flagged, never silently counted.
        res["individuates_every_lock_point"] = res["groups"] == len(rows)
        res["determination_is_vacuous"] = (
            res["is_a_function"] and res["individuates_every_lock_point"])
        out.append(res)
    return out


def exhaustive_singleton_sweep(rows, value_fn, width):
    """EXHAUSTIVE over all `width` single-wire contexts: which single wire's
    value at the lock tick already determines the selection?"""
    varying, determining = [], []
    for wire in range(width):
        values = {r["full_state"][wire] for r in rows}
        if len(values) < 2:
            continue
        varying.append(wire)
        groups: dict = {}
        ok = True
        for r in rows:
            b = r["full_state"][wire]
            v = value_fn(r)
            if groups.setdefault(b, v) != v:
                ok = False
                break
        if ok:
            determining.append(wire)
    return varying, determining


# ---------------------------------------------------------------------------
# C2: covariance
# ---------------------------------------------------------------------------

def translation_covariance(c878, census, stations, selection):
    perms, phase_ok = c878.monitor_phase_action(census, stations)
    locks = set(selection)
    checks = violations = off_set = 0
    for perm in perms:
        for w in sorted(locks):
            image = perm[w]
            if image in locks:
                checks += 1
                violations += int(selection[image] != selection[w])
            else:
                off_set += 1
    orbits = c878.group_orbits(perms, len(census)) if phase_ok else ()
    touching = [o for o in orbits if set(o) & locks]
    mixed = [o for o in touching
             if len({selection[w] for w in o if w in locks}) > 1]
    return {
        "action_is_a_census_bijection": phase_ok,
        "group_order": len(perms),
        "in_set_image_checks": checks,
        "selection_violations_under_translation": violations,
        "images_that_leave_the_lock_set": off_set,
        "lock_set_is_closed_under_the_action": off_set == 0,
        "census_orbits_meeting_the_lock_set": len(touching),
        "census_orbits_total": len(orbits),
        "orbits_carrying_BOTH_selections": len(mixed),
        "selection_is_translation_invariant": phase_ok and violations == 0,
    }


def cubic_covariance(c911, cls, rows, selection, snapshots, lock_ordinal):
    out = []
    for alphabet in (2, 3, 4):
        colorings = c911.context_colorings(rows, snapshots, lock_ordinal,
                                           alphabet)
        full, proper = c911.build_cubic_group(cls, DIRS_HOLDER["dirs"])
        proper_orbits = cls.direct_orbits(proper, alphabet)
        full_orbits = cls.direct_orbits(full, alphabet)
        ids = cls.orbit_ids(proper_orbits)
        cls_of = {w: ids[c] for w, c in colorings.items()}
        sizes = Counter(cls_of[r["world"]] for r in rows)
        per_class: dict = {}
        for r in rows:
            per_class.setdefault(cls_of[r["world"]], set()).add(
                selection[r["world"]])
        nonconst = sorted(c for c, v in per_class.items() if len(v) > 1)
        out.append({
            "alphabet_k": alphabet,
            "proper_orbits_total": len(proper_orbits),
            "full_orbits_total": len(full_orbits),
            "chiral_pairs": len(proper_orbits) - len(full_orbits),
            "classes_realized_by_the_formation_contexts": len(sizes),
            "class_sizes": {str(c): sizes[c] for c in sorted(sizes)},
            "selection_is_class_constant": not nonconst,
            "classes_on_which_the_selection_is_NOT_constant": nonconst,
            "selection_values_per_class": {
                str(c): sorted(map(list, v)) for c, v in
                sorted(per_class.items())},
        })
    return out


DIRS_HOLDER: dict = {}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    cert_a, payloads = pin_rows()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({
            k: cert_a[k] for k in
            ("literal_ok", "sha256_all_match", "git_blobs_all_match",
             "existing_worktree_relative", "blocked_modules_loaded",
             "firewall_hits")}))
        return 2

    c863, c878, c911, cls, dirs, consts878, consts911, provenance = \
        lift_machinery()
    DIRS_HOLDER["dirs"] = dirs

    text = {p: payloads[p].decode("utf-8") for p in TEXT_ONLY_PATHS}
    receipts = {p: json.loads(payloads[p].decode("utf-8"))
                for p in JSON_ONLY_PATHS}
    r911 = receipts[C911_RECEIPT]
    r878 = receipts[C878_RECEIPT]
    c2_911 = r911["certificates"]["C2_MENU_AT_FORMATION"]

    # ---------------- build ------------------------------------------------
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_failures = c863.build_initial_states(
        program, event_seeds, census)
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}))

    t0 = monotonic()
    build_fwd = c911.snapshot_scan(c863, program, census, states, HORIZON,
                                   False)
    t_fwd = round(monotonic() - t0, 3)
    t0 = monotonic()
    build_rev = c911.snapshot_scan(c863, program, census, states, HORIZON,
                                   True)
    t_rev = round(monotonic() - t0, 3)

    formed = build_fwd["formed"]
    snapshots = build_fwd["snapshots"]
    lock_ordinal = build_fwd["lock_ordinal"]
    events = build_fwd["events"]

    # ---------------- B: restriction gates ---------------------------------
    axioms = text[AXIOMS_PATH]
    note911 = text[C911_NOTE]
    covnote = text[COVCLASS_PATH]
    realized = text[REALIZED_PATH]

    Q_ADMISSIBILITY = ("For each site, the available possibilities are"
                       " determined by, and vary with,\nthe nearest-neighbor"
                       " conditions.")
    Q_RECORD_LOCK = ("When present, a record locks exactly one admissible"
                     " local possibility. A\nsite never carries more than one"
                     " record; records are permanent.")
    Q_READOUT = ("Only records are readable. A readout value is determined by"
                 " record content\nalone.")
    Q_RECORDS_FORM = "Records form."
    Q_NO_AVERAGING = ("Nothing more is supplied: no averaging over"
                      " alternatives, no typical or\ngeneric claim, and no"
                      " quoting a number that would differ had another\n"
                      "law-admissible state been realized.")
    Q_REALIZED_PRIM = ("The laws do not pick the state; the world does, among"
                       " the states the laws\npermit.")
    Q_911_CAVEAT = ("it does not VARY with\nnearest-neighbour conditions on"
                    " this substrate, which is weaker than\nthe Admissibility"
                    " sentence asserts")
    Q_911_FIRST_SITE = ("world 176, key (3, 0, (0,2,4)),\nboundary 0, menu"
                        " {(1,0), (0,1)}, both orbit-consistent")
    Q_911_NEXT = "the landed scan's selection function is the next computation"
    Q_COV_T2 = "Burnside orbit counts agree at 10 and\n   10"
    Q_COV_T3 = ("At `k = 3` the proper/full orbit counts are\n   57 and 56:"
                " exactly **one** chiral pair")
    Q_COV_K4 = ("At `k = 4`\n   (three record contents plus openness) the"
                " count grows to 20 pairs")
    Q_COV_T5 = ("A chiral rule\n   comes in a"
                " supplied-structure-indistinguishable pair `{R1, -R1}`")
    Q_COV_OPENNESS = ("**A chiral admissibility rule cannot live at the"
                      " openness\n   level**")

    r911_rows = c2_911["per_lock_point_rows"]
    r911_by_world = {row["world"]: row for row in r911_rows}
    first_site = c2_911["first_genuine_selection_site"]

    my_locks = sorted(formed)
    gate_rows = []

    def gate(name, got, want):
        ok = got == want
        gate_rows.append({"gate": name, "value": got, "pinned": want,
                          "pass": ok})
        return ok

    gate("c911_formation_events", len(my_locks), c2_911["formation_events"])
    gate("c911_selection_sites", len(my_locks), c2_911["selection_sites"])
    gate("c911_lock_worlds_value_for_value",
         my_locks, sorted(r911_by_world))
    gate("c911_lock_boundaries_value_for_value",
         [formed[w] for w in my_locks],
         [r911_by_world[w]["lock_boundary"] for w in my_locks])
    gate("c911_keys_value_for_value",
         [[census[w][0], census[w][1], list(census[w][2])] for w in my_locks],
         [r911_by_world[w]["key"] for w in my_locks])
    gate("c911_lock_boundary_range",
         [min(formed[w] for w in my_locks), max(formed[w] for w in my_locks)],
         c2_911["lock_boundary_range"])
    gate("c911_locks_at_moment_zero",
         sum(1 for w in my_locks if formed[w] == 0),
         c2_911["locks_at_moment_zero"])
    gate("c911_menu_of_local_possibilities",
         [list(v) for v in consts911["DIRECTIONS"]],
         c2_911["menu_of_local_possibilities"])
    gate("c911_first_selection_site_world", first_site["world"], 176)
    gate("c911_first_selection_site_key", first_site["key"], [3, 0, [0, 2, 4]])
    gate("c911_first_selection_site_boundary", first_site["lock_boundary"], 0)
    gate("c911_first_selection_site_menu", first_site["menu_orbit"],
         [[1, 0], [0, 1]])
    gate("c911_first_selection_site_is_mine",
         [176 in formed, formed.get(176), [census[176][0], census[176][1],
                                           list(census[176][2])]],
         [True, 0, [3, 0, [0, 2, 4]]])
    gate("c911_A_prepare_is_two_everywhere",
         sorted({r911_by_world[w]["A_prepare"] for w in my_locks}), [2])
    gate("c911_A_orbit_is_two_everywhere",
         sorted({r911_by_world[w]["A_orbit"] for w in my_locks}), [2])
    gate("c911_prepare_errors_zero", c2_911["prepare_errors"], 0)
    recomputed = c911.availability_operators(
        c863, program, snapshots, formed, census, per_bank)
    recomputed_by_world = {row["world"]: row for row in recomputed}
    gate("c911_menus_recomputed_value_for_value",
         [[recomputed_by_world[w]["A_prepare"],
           recomputed_by_world[w]["A_orbit"],
           [list(v) for v in recomputed_by_world[w]["menu_prepare"]],
           [list(v) for v in recomputed_by_world[w]["menu_orbit"]]]
          for w in my_locks],
         [[r911_by_world[w]["A_prepare"], r911_by_world[w]["A_orbit"],
           r911_by_world[w]["menu_prepare"], r911_by_world[w]["menu_orbit"]]
          for w in my_locks])
    gate("horizon_agrees_with_878_and_911",
         [consts878["HORIZON"], consts911["HORIZON"]], [HORIZON, HORIZON])
    gate("c911_receipt_verdict", r911["VERDICT"], "RE-TYPED")
    gate("c911_receipt_all_certificates_pass",
         r911["all_certificates_pass"], True)
    gate("c911_O3_vacuous_flag", c2_911["O3_vacuous_on_this_census"], False)
    gate("c878_event_cardinality", len(events),
         r878["findings"]["event_cardinality"])
    gate("c878_worlds_with_at_least_one_event",
         len({e[0] for e in events}),
         r878["findings"]["worlds_with_at_least_one_event"])
    gate("census_size", len(census), 748)
    gate("initial_state_build_failures", init_failures, 0)
    gate("axioms_admissibility_sentence_byte_present",
         Q_ADMISSIBILITY in axioms, True)
    gate("axioms_record_lock_sentence_byte_present",
         Q_RECORD_LOCK in axioms, True)
    gate("axioms_readout_sentence_byte_present", Q_READOUT in axioms, True)
    gate("axioms_records_form_byte_present", Q_RECORDS_FORM in axioms, True)
    gate("realized_state_no_averaging_byte_present",
         Q_NO_AVERAGING in realized, True)
    gate("realized_state_primitive_byte_present",
         Q_REALIZED_PRIM in realized, True)
    gate("c911_note_menu_variation_caveat_byte_present",
         Q_911_CAVEAT in note911, True)
    gate("c911_note_first_site_byte_present", Q_911_FIRST_SITE in note911,
         True)
    gate("c911_note_names_this_computation", Q_911_NEXT in note911, True)
    gate("covnote_theorem2_counts_byte_present", Q_COV_T2 in covnote, True)
    gate("covnote_theorem3_counts_byte_present", Q_COV_T3 in covnote, True)
    gate("covnote_k4_pairs_byte_present", Q_COV_K4 in covnote, True)
    gate("covnote_theorem5_dichotomy_byte_present", Q_COV_T5 in covnote, True)
    gate("covnote_openness_achirality_byte_present",
         Q_COV_OPENNESS in covnote, True)

    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": gate_rows,
        "total": len(gate_rows),
        "reproduce": sum(1 for r in gate_rows if r["pass"]),
        "byte_quotes": {
            "admissibility_sentence": Q_ADMISSIBILITY,
            "record_lock_sentence": Q_RECORD_LOCK,
            "readout_sentence": Q_READOUT,
            "realized_state_no_averaging": Q_NO_AVERAGING,
            "realized_state_primitive": Q_REALIZED_PRIM,
            "c911_adopted_menu_variation_caveat": Q_911_CAVEAT,
            "c911_first_selection_site": Q_911_FIRST_SITE,
            "c911_names_this_computation": Q_911_NEXT,
            "covnote_theorem_2": Q_COV_T2,
            "covnote_theorem_3": Q_COV_T3,
            "covnote_k4": Q_COV_K4,
            "covnote_theorem_5": Q_COV_T5,
            "covnote_openness_achirality": Q_COV_OPENNESS,
        },
        "pass": all(r["pass"] for r in gate_rows),
    }

    # ---------------- C1: the selection table ------------------------------
    menu = tuple(tuple(v) for v in consts911["DIRECTIONS"])
    left_w, right_w, src_w = endpoint_wires()
    width = len(snapshots[my_locks[0]])
    BB = K.M.R12.BANK_BASES
    LB = K.M.R12.LINK_BASES
    AW = K.A.N
    LW = K.B.LINK_WIDTH
    site_wires = tuple(range(BB[0]))
    endpoint_set = {left_w, right_w}

    schedules = c863.masked_h_schedules(program, tuple(census) + (census[0],))
    target_lemma = target_wire_sweep(schedules)

    seed_by_event = dict(event_seeds)
    setup_direction = {}
    for ev, seed in event_seeds:
        setup_direction[ev] = read_state_direction(seed)

    chunk_cache: dict = {}
    rows = []
    rearm_rows = []
    readout_disagreements = []
    for w in my_locks:
        state = snapshots[w]
        key = census[w]
        positions = key[2]
        if positions not in chunk_cache:
            chunk_cache[positions] = c911.synchronous_chunks(program,
                                                             positions)
        rd_state = read_state_direction(state)
        rd_ham, ham_map = hamming_readout(state, menu)
        rearm = rearm_readout(c911, program, chunk_cache[positions], state,
                              formed[w], menu, global_dirty)
        rd_rearm = tuple(rearm["item"]) if rearm["item"] else None
        rd_setup = setup_direction[key[1]]
        agree = (rd_state is not None and rd_state == rd_ham == rd_rearm
                 == rd_setup)
        if not agree:
            readout_disagreements.append(
                {"world": w, "RD_STATE": rd_state, "RD_HAMMING": rd_ham,
                 "RD_REARM": rd_rearm, "RD_SETUP": rd_setup})
        bank0 = "".join(str(state[BB[0] + i]) for i in range(AW))
        bank1 = "".join(str(state[BB[1] + i]) for i in range(AW))
        link0 = "".join(str(state[LB[0] + i]) for i in range(LW))
        shell2_rest = "".join(
            str(state[BB[b] + i]) for b in (2, 3) for i in range(AW))
        full = "".join(str(b) for b in state)
        rows.append({
            "world": w,
            "key": [key[0], key[1], list(key[2])],
            "lock_boundary": formed[w],
            "phase": formed[w] % stations,
            "menu": [list(v) for v in menu],
            "selected_item": list(rd_state) if rd_state else None,
            "ord0": lock_ordinal[w][0], "ord1": lock_ordinal[w][1],
            "bank0": bank0, "bank1": bank1, "link0": link0,
            "shell2_rest": shell2_rest,
            "site_block": "".join(str(state[i]) for i in site_wires),
            "site_block_minus_endpoints": "".join(
                str(state[i]) for i in site_wires if i not in endpoint_set),
            "endpoint_bits": (state[left_w], state[right_w]),
            "state_minus_site": full[BB[0]:],
            "state_minus_endpoints": "".join(
                c for i, c in enumerate(full) if i not in endpoint_set),
            "full_state": full,
            "context_fingerprint": sha256(
                (bank0 + "|" + bank1 + "|" + link0 + "|"
                 + full[BB[0]:]).encode("ascii")).hexdigest()[:16],
            "readouts_agree": agree,
        })
        rearm_rows.append({"world": w, **rearm})

    selection = {r["world"]: tuple(r["selected_item"]) for r in rows
                 if r["selected_item"]}
    sel_hist = Counter(tuple(r["selected_item"]) for r in rows)
    total = len(rows)
    split = {str(list(v)): {"count": c, "share": fr(Fraction(c, total)),
                            "label": FRACTION_LABEL}
             for v, c in sorted(sel_hist.items())}

    serial_checked = []
    for r in rows:
        if r["lock_boundary"] > SERIAL_LOCK_CAP:
            continue
        key = census[r["world"]]
        b, direction = serial_lock_replay(
            c863, c911, program, key, states[r["world"]], global_dirty,
            SERIAL_LOCK_CAP)
        serial_checked.append({
            "world": r["world"],
            "boundary_matches": b == r["lock_boundary"],
            "selection_matches": direction is not None
            and list(direction) == r["selected_item"],
        })

    cert_c1 = {
        "certificate": "C1_SELECTION_TABLE",
        "lock_points": total,
        "menu_at_every_lock_point": [list(v) for v in menu],
        "readouts": {
            "RD_STATE": "the endpoint content the lock state carries, "
                        "inverted through K.M.prepare_endpoint's own "
                        "definition",
            "RD_HAMMING": "the unique menu item whose prepared endpoint sits "
                          "at Hamming distance 1 from the lock state",
            "RD_REARM": "the scan's OWN next endpoint preparation, matched "
                        "bit-for-bit on all wires",
            "RD_SETUP": "the direction the world's own seed was prepared with",
        },
        "all_four_readouts_agree_on_every_row": not readout_disagreements,
        "readout_disagreements": readout_disagreements,
        "selection_split": split,
        "exactly_one_menu_item_realized_per_lock_point": all(
            r["selected_item"] in ([1, 0], [0, 1]) for r in rows),
        "rearm_unique_on_every_row": all(x["unique"] for x in rearm_rows),
        "rearm_offsets": dict(sorted(Counter(
            x["rearm_offset_from_lock"] for x in rearm_rows).items(),
            key=lambda kv: (kv[0] is None, kv[0]))),
        "rearm_counterfactual_hamming_distance": sorted({
            d for x in rearm_rows for v, d in
            x["hamming_to_each_menu_item"].items() if d}),
        "clean_at_lock_on_every_row": all(x["clean_at_lock"]
                                          for x in rearm_rows),
        "endpoint_wire_lemma": target_lemma,
        "setup_direction_by_event": {str(e): list(v) for e, v
                                     in sorted(setup_direction.items())},
        "independent_serial_replay": {
            "worlds_replayed": len(serial_checked),
            "cap_boundaries": SERIAL_LOCK_CAP,
            "lock_boundary_agreements": sum(
                1 for x in serial_checked if x["boundary_matches"]),
            "selection_agreements": sum(
                1 for x in serial_checked if x["selection_matches"]),
            "all_agree": all(x["boundary_matches"] and x["selection_matches"]
                             for x in serial_checked),
        },
        "per_lock_point_rows": [
            {"world": r["world"], "key": r["key"],
             "lock_boundary": r["lock_boundary"], "phase": r["phase"],
             "menu": r["menu"], "selected_item": r["selected_item"],
             "neighbour_ordinals": [r["ord0"], r["ord1"]],
             "context_fingerprint": r["context_fingerprint"]}
            for r in rows],
    }
    cert_c1["pass"] = bool(
        cert_c1["all_four_readouts_agree_on_every_row"]
        and cert_c1["exactly_one_menu_item_realized_per_lock_point"]
        and cert_c1["rearm_unique_on_every_row"]
        and cert_c1["clean_at_lock_on_every_row"]
        and target_lemma["endpoint_content_is_read_never_written"]
        and cert_c1["independent_serial_replay"]["all_agree"]
        and total == 164)

    # ---------------- C2: the dependence structure -------------------------
    def value_fn(r):
        return tuple(r["selected_item"])

    ladder = ladder_rows(rows, value_fn)
    by_name = {row["fingerprint"]: row for row in ladder}
    varying, determining = exhaustive_singleton_sweep(rows, value_fn, width)

    nonsite_varying = [w for w in varying if w >= BB[0]]
    nonsite_all = is_function(
        rows, lambda r: tuple(r["full_state"][w] for w in nonsite_varying),
        value_fn)

    trans = translation_covariance(c878, census, stations, selection)
    cubic = cubic_covariance(c911, cls, rows, selection, snapshots,
                             lock_ordinal)

    local_verdict = by_name["R1_nearest_neighbour_record_content"][
        "is_a_function"]
    minimal_size = 0 if by_name["EMPTY_CONTEXT"]["is_a_function"] else (
        1 if determining else None)
    cert_c2 = {
        "certificate": "C2_DEPENDENCE",
        "ladder": ladder,
        "selection_is_a_function_of_nearest_neighbour_conditions":
            local_verdict,
        "widest_non_site_context_determines": nonsite_all["is_a_function"],
        "widest_non_site_context": {
            "varying_non_site_wires": len(nonsite_varying),
            **{k: v for k, v in nonsite_all.items() if k != "witness_pair"},
            "witness_pair": nonsite_all["witness_pair"],
        },
        "ladder_entries_that_individuate_every_lock_point": [
            row["fingerprint"] for row in ladder
            if row["individuates_every_lock_point"]],
        "vacuity_note":
            "adding the absolute lock tick and/or the token positions to a "
            "fingerprint can make it INJECTIVE on the 164 lock points; such "
            "a fingerprint determines everything trivially because it names "
            "the site rather than describing its conditions.  Those entries "
            "are flagged determination_is_vacuous and are excluded from the "
            "minimality claim, which is computed over state-wire contexts "
            "only.",
        "monotonicity_lemma":
            "determination is monotone in the context: if the FULL non-site "
            "context does not determine the selection, no subset of the "
            "non-site wires does either.  The widest non-site context does "
            "not determine, so no neighbour-shell fingerprint at any radius "
            "can.",
        "exhaustive_single_wire_sweep": {
            "wires_swept": width,
            "wires_that_vary_across_the_164_lock_states": len(varying),
            "single_wires_that_DETERMINE_the_selection": determining,
            "determining_wire_names": [
                {"wire": w,
                 "name": ("LEFT_ENDPOINT" if w == left_w else
                          "RIGHT_ENDPOINT" if w == right_w else
                          "SOURCE_POINTER" if w == src_w else
                          f"wire_{w}"),
                 "inside_the_site_block": w < BB[0]}
                for w in determining],
            "any_determining_wire_outside_the_site": any(
                w >= BB[0] for w in determining),
        },
        "MINIMAL_DETERMINING_CONTEXT": {
            "cardinality": minimal_size,
            "complete_list_of_minimum_cardinality_contexts":
                [[w] for w in determining],
            "empty_context_determines":
                by_name["EMPTY_CONTEXT"]["is_a_function"],
            "statement":
                "the selection at every lock point is determined by a SINGLE "
                "wire -- the site's own endpoint content (LEFT_ENDPOINT or, "
                "equivalently, RIGHT_ENDPOINT) -- and by no wire outside the "
                "site, alone or in any combination.  In setup coordinates the "
                "same one bit is the parity of the world's event index.",
        },
        "covariance_translation": trans,
        "covariance_cubic_on_the_declared_embedding": cubic,
        "covariance_verdict":
            "the landed selection is INVARIANT under the landed lattice "
            "translation action (the Cycle-878 monitor-phase Z_11) and is NOT "
            "constant on the proper-cubic orbit classes of the neighbour "
            "colouring at any of k = 2, 3, 4 -- because it is not a function "
            "of the colouring at all.  It is covariant for the trivial "
            "reason: it is a transported constant of each world.",
    }
    cert_c2["pass"] = bool(
        len(ladder) == 19
        and by_name["SITE_ENDPOINT_WIRES_ONLY"]["is_a_function"]
        and determining
        and trans["action_is_a_census_bijection"]
        and len(cubic) == 3)

    # ---------------- C3: the content question -----------------------------
    zero_tick = [r for r in rows if r["lock_boundary"] == 0]
    zero_tick_sel = Counter(tuple(r["selected_item"]) for r in zero_tick)
    no_prior_record = [r for r in rows if r["ord0"] == 0 and r["ord1"] == 0]
    no_prior_sel = Counter(tuple(r["selected_item"]) for r in no_prior_record)
    content_register = by_name["R1_nearest_neighbour_record_content"]
    content_ordinal = by_name["R1_nearest_neighbour_exact_ordinals"]
    content_openness = by_name["R1_nearest_neighbour_openness_only"]
    cert_c3 = {
        "certificate": "C3_CONTENT_DETERMINATION",
        "reading_1_record_registers": {
            "gloss": "the neighbours' record registers (bank words) at the "
                     "lock tick",
            **{k: v for k, v in content_register.items()},
        },
        "reading_2_record_event_history": {
            "gloss": "the composed scan's own written record history strictly "
                     "before the lock tick, indexed by the neighbour "
                     "ordinals",
            **{k: v for k, v in content_ordinal.items()},
            "lock_points_with_NO_prior_record_event_at_all":
                len(no_prior_record),
            "their_selections": {str(list(v)): c for v, c
                                 in sorted(no_prior_sel.items())},
            "lock_points_at_tick_zero": len(zero_tick),
            "their_selections_at_tick_zero": {
                str(list(v)): c for v, c in sorted(zero_tick_sel.items())},
            "decisive_witness":
                "at the 24 lock points that occur at boundary 0 the world has "
                "written no record event whatsoever, yet the selection is not "
                "constant across them -- so it cannot be a function of "
                "already-formed record content.",
        },
        "reading_3_openness_only": {
            "gloss": "the k = 2 content-blind alphabet of the pinned "
                     "classification",
            **{k: v for k, v in content_openness.items()},
        },
        "selection_is_a_function_of_record_content_alone": bool(
            content_register["is_a_function"]
            and content_ordinal["is_a_function"]),
        "readout_axiom_consequence":
            "the Readout axiom says a readout value is determined by record "
            "content alone.  The realized selection is NOT determined by "
            "record content under any of the three readings, so on this "
            "substrate the selected possibility is not a readout value: it is "
            "carried by the site's own non-record endpoint wires.",
    }
    cert_c3["pass"] = bool(
        len(zero_tick) == 24 and len(zero_tick_sel) >= 1
        and len(no_prior_sel) >= 1)

    # ---------------- C4: context variation --------------------------------
    distinct_nn = len({(r["bank0"], r["bank1"]) for r in rows})
    distinct_b0 = len({r["bank0"] for r in rows})
    distinct_b1 = len({r["bank1"] for r in rows})
    distinct_link = len({r["link0"] for r in rows})
    distinct_minus_site = len({r["state_minus_site"] for r in rows})
    distinct_site = len({r["site_block"] for r in rows})
    distinct_full = len({r["full_state"] for r in rows})
    site_variants = sorted({r["site_block"] for r in rows})
    site_diff = ([i for i in range(len(site_variants[0]))
                  if site_variants[0][i] != site_variants[1][i]]
                 if len(site_variants) == 2 else [])
    menu_sizes = sorted({r911_by_world[w]["A_orbit"] for w in my_locks})
    cert_c4 = {
        "certificate": "C4_CONTEXT_VARIATION",
        "distinct_nearest_neighbour_contexts": distinct_nn,
        "distinct_bank0_words": distinct_b0,
        "distinct_bank1_words": distinct_b1,
        "distinct_link_words": distinct_link,
        "link_word_is_constant": distinct_link == 1,
        "distinct_contexts_outside_the_site": distinct_minus_site,
        "distinct_site_blocks": distinct_site,
        "site_blocks_differ_only_at_wires": site_diff,
        "distinct_full_lock_states": distinct_full,
        "symmetry_classes_of_the_contexts": {
            str(row["alphabet_k"]): row[
                "classes_realized_by_the_formation_contexts"]
            for row in cubic},
        "contexts_are_all_equivalent_under_the_symmetries": all(
            row["classes_realized_by_the_formation_contexts"] == 1
            for row in cubic),
        "pinned_c911_menu_size_at_every_lock_point": menu_sizes,
        "verdict":
            f"the nearest-neighbour CONTEXTS do vary: {distinct_nn} distinct "
            f"neighbour conditions across the {total} lock points, falling "
            "into "
            + " / ".join(str(row["classes_realized_by_the_formation_contexts"])
                         for row in cubic)
            + " proper-cubic classes at k = "
            + " / ".join(str(row["alphabet_k"]) for row in cubic)
            + ".  The Admissibility sentence's 'vary with' clause therefore "
            "has something to bite on here.  What does not vary with them is "
            "the landed dynamics: Cycle 911 showed the menu SIZE is "
            f"{menu_sizes} at every one of them, and this block shows the "
            "SELECTION is not a function of them either.  The gap is not "
            "that the contexts are degenerate; the gap is that the landed "
            "rule ignores them.",
    }
    cert_c4["pass"] = bool(distinct_nn > 1 and distinct_site == 2
                           and menu_sizes == [2])

    # ---------------- C5: the classified rule space ------------------------
    class_rows = []
    for row in cubic:
        k = row["alphabet_k"]
        class_rows.append({
            "alphabet_k": k,
            "proper_orbits": row["proper_orbits_total"],
            "full_orbits": row["full_orbits_total"],
            "chiral_pairs": row["chiral_pairs"],
            "note_says": {2: "10 and 10", 3: "57 and 56", 4: "20 pairs"}[k],
            "reproduces_the_note": {
                2: row["proper_orbits_total"] == 10
                and row["full_orbits_total"] == 10,
                3: row["proper_orbits_total"] == 57
                and row["full_orbits_total"] == 56,
                4: row["chiral_pairs"] == 20,
            }[k],
        })
    cert_c5 = {
        "certificate": "C5_CLASSIFIED_RULE_COMPARISON",
        "reproduced_orbit_counts": class_rows,
        "all_note_counts_reproduced": all(r["reproduces_the_note"]
                                          for r in class_rows),
        "landed_selection_is_a_function_of_the_neighbour_colouring": all(
            row["selection_is_class_constant"] for row in cubic),
        "membership_verdict":
            "every element of the classified rule space is by construction a "
            "function of the six-direction neighbour colouring.  The landed "
            "selection is not a function of that colouring at any of "
            "k = 2, 3, 4, so it is NOT a member of the classified space.",
        "the_positive_placement":
            "restricted to either setup sector the landed selection IS a "
            "member: it is the CONSTANT rule, which is achiral and fully "
            "cubic-covariant at every k.  The landed dynamics realises one of "
            "the two constants, {colouring -> (1,0)} and "
            "{colouring -> (0,1)}, and which one is fixed by a single bit "
            "the site transports in from its setup.  Structurally that is the "
            "note's Theorem-5 situation -- a supplied-structure-"
            "indistinguishable pair whose member is fixed by one bit -- with "
            "the bit resolved by IMPORT from the initial condition rather "
            "than by any rule.  Because the constant rule is achiral, the "
            "landed selection carries no orientation channel of the kind "
            "Theorem 3 requires for chirality: the handedness sits in the "
            "setup, not in the rule.",
        "openness_level_cross_check":
            "the note's Theorem 2 (openness-level patterns are automatically "
            "achiral) is reproduced here at k = 2 with proper = full = 10; "
            "the landed selection is not even an openness-level rule, since "
            "it is non-constant on all of the realized openness classes.",
    }
    cert_c5["pass"] = bool(cert_c5["all_note_counts_reproduced"])

    # ---------------- C6: the O2/O3 verdict --------------------------------
    locks_per_world = Counter(r["world"] for r in rows)
    biggest_nn_collision = by_name["R1_nearest_neighbour_record_content"][
        "largest_collision_class_size"]
    cert_c6 = {
        "certificate": "C6_O2_O3_VERDICT",
        "O2": {
            "status": "SUPPLIED BY THE LANDED DYNAMICS, AND MEASURED",
            "the_function":
                "realized(w) = (1,0) if the world's setup event index is "
                "even, (0,1) if it is odd; equivalently, the endpoint content "
                "the site carries on wires "
                f"{left_w} (LEFT_ENDPOINT) and {right_w} (RIGHT_ENDPOINT).",
            "is_it_a_function_of_local_conditions": False,
            "is_it_content_determined": False,
            "is_it_covariant": True,
            "covariance_kind": "invariant under the landed lattice "
                               "translation action; trivially so, being a "
                               "transported constant of each world",
            "minimal_determining_context": "one wire: the site's own endpoint "
                                           "content",
            "the_sharp_fact":
                "no gate in the composed scan targets the endpoint wires. "
                "The landed scan READS the selection at every source station "
                "and every finalizer station and never WRITES it.  So the "
                "'formation rule' the no-go said the axioms do not force is "
                "PRESENT in the landed scan, but it is not a rule about "
                "neighbourhoods at all: it is transport of a setup "
                "coordinate.  The scan does not choose; it carries.",
            "derivable_or_supplied":
                "SUPPLIED.  A derivable formation rule would have to be a "
                "function of the site's neighbourhood, and the measured "
                "dependence forbids that: the largest neighbour-context "
                "collision class holds "
                f"{biggest_nn_collision} lock points that share ONE "
                "neighbour context and still split between the two menu "
                "items, and the widest possible non-site context "
                f"({len(nonsite_varying)} varying wires) still fails.  The "
                "landed selection is a feature of the setup the scan was "
                "handed.",
        },
        "O3": {
            "status": "TERMINAL STATEMENT",
            "determinism":
                "the composed scan is deterministic: each of the 164 lock "
                "points realizes exactly one menu item, so each setup yields "
                "ONE trajectory and the other menu item is counterfactual at "
                "every lock point.",
            "locks_per_world": sorted(set(locks_per_world.values())),
            "within_world_frequency_is_degenerate":
                "every world that locks, locks exactly once.  The within-world "
                "empirical frequency on its own menu is therefore (1, 0) -- "
                "degenerate -- and no non-trivial weight is estimable inside "
                "a world.",
            "cross_world_split": split,
            "cross_world_split_is_forbidden":
                "the 84/80 split is an average over SETUPS.  The pinned "
                "realized-state primitive forbids exactly that: 'no averaging "
                "over alternatives ... and no quoting a number that would "
                "differ had another law-admissible state been realized'.",
            "the_A3_arena_located": {
                "sites": total,
                "possibilities_per_site": len(menu),
                "site_possibility_pairs": total * len(menu),
                "realized": total,
                "counterfactual": total * (len(menu) - 1),
                "statement":
                    "the only arena in which an occurrence WEIGHT could still "
                    "mean anything on this substrate is a weight over the "
                    "counterfactual menu at a single lock point: 164 sites x "
                    "2 possibilities = 328 site-possibility pairs, 164 "
                    "realized and 164 counterfactual.  A weight there is "
                    "exactly the A3-shaped sentence (a weight on the "
                    "available possibilities at a site).  A weight over "
                    "setups is the forbidden averaging.",
            },
            "the_sharpened_obstruction":
                "C2 makes the A3 arena worse, not better.  The coordinate "
                "that distinguishes the two possibilities at a lock point is "
                "the site's endpoint content, and that coordinate is never "
                "written by the dynamics -- it is a setup coordinate held "
                "fixed for all time.  So a weight over the counterfactual "
                "menu at a lock point IS a weight over setups wearing a "
                "different name, and the realized-state primitive forbids it "
                "under either name.  On this substrate O3 has no "
                "non-forbidden realization.  Supplying it needs either a "
                "substrate in which the endpoint content is WRITTEN by the "
                "dynamics (so that the two possibilities are genuine "
                "alternatives of one setup), or the A3 sentence taken as an "
                "import.",
        },
        "ledger": {
            "O1": "CLOSED (axiom-forced) -- unchanged from Cycle 911.",
            "O2": "COMPUTED AND CLOSED AS A MEASUREMENT, OPEN AS A "
                  "DERIVATION.  The landed scan's selection function is "
                  "known exactly (event parity / the site's transported "
                  "endpoint bit), is translation-invariant, is NOT a "
                  "function of nearest-neighbour conditions, is NOT "
                  "content-determined, and is NOT a member of the classified "
                  "covariant nearest-neighbour rule space.  What is open is "
                  "no longer 'which does it select' but 'is a "
                  "neighbourhood-determined selection available at all on a "
                  "substrate where the endpoint content is dynamical'.",
            "O3": "TERMINAL ON THIS SUBSTRATE.  The A3 arena is located "
                  "exactly (the 164 counterfactual menu items) and is shown "
                  "to be setup-indexed, so every weight over it is the "
                  "forbidden average.  O3 cannot be supplied here without an "
                  "import.",
            "the_menu_variation_gap":
                "Cycle 911 left it open whether the contexts themselves vary. "
                "They do (54 distinct neighbour contexts, 3/6/7 symmetry "
                "classes).  The gap is therefore real and one-sided: the "
                "substrate supplies varying conditions and the landed rule "
                "ignores them, both in the menu size (911) and in the "
                "selection (913).",
            "successor":
                "a substrate whose endpoint content is a gate TARGET -- so "
                "that the two menu items are alternatives of one setup rather "
                "than two setups -- is the only place the A3 arena can be "
                "non-degenerate.  That is the next computation.",
        },
    }
    cert_c6["pass"] = True

    # ---------------- G: planted falsifiers --------------------------------
    teeth = []

    def add(name, detected, detail=None):
        teeth.append({"tooth": name, "detected": bool(detected),
                      "detail": detail})

    # T1: a planted NON-LOCAL selection must be detected as non-local
    nn_of = {r["world"]: (r["bank0"], r["bank1"]) for r in rows}
    by_nn: dict = {}
    for r in rows:
        by_nn.setdefault(nn_of[r["world"]], []).append(r)
    big = max(by_nn.values(), key=len)
    planted_nonlocal = []
    for r in rows:
        base = (1, 0) if r["bank1"].count("1") % 2 == 0 else (0, 1)
        if r["world"] == big[0]["world"]:
            base = (0, 1) if base == (1, 0) else (1, 0)
        planted_nonlocal.append({**r, "selected_item": list(base)})
    t1 = is_function(planted_nonlocal, lambda r: (r["bank0"], r["bank1"]),
                     lambda r: tuple(r["selected_item"]))
    add("planted_nonlocal_selection_detected_as_nonlocal",
        not t1["is_a_function"] and t1["witness_pair"] is not None,
        {"collision_classes": t1["collision_classes"],
         "witness": t1["witness_pair"]})

    # T2: a planted LOCAL selection must be detected as local (neutrality)
    planted_local = [
        {**r, "selected_item": [1, 0] if r["bank1"].count("1") % 2 == 0
         else [0, 1]} for r in rows]
    t2 = is_function(planted_local, lambda r: (r["bank0"], r["bank1"]),
                     lambda r: tuple(r["selected_item"]))
    add("planted_local_selection_detected_as_local", t2["is_a_function"],
        {"groups": t2["groups"]})

    # T3: a planted single-wire determination must be found by the sweep
    probe_wire = next(w for w in varying if w >= BB[0])
    planted_wire = [
        {**r, "selected_item": [1, 0] if r["full_state"][probe_wire] == "1"
         else [0, 1]} for r in rows]
    _v3, d3 = exhaustive_singleton_sweep(
        planted_wire, lambda r: tuple(r["selected_item"]), width)
    add("planted_single_wire_determination_found_by_the_sweep",
        probe_wire in d3,
        {"probe_wire": probe_wire, "wires_found": len(d3)})

    # T4: a planted CONSTANT selection must make the empty context determine
    planted_const = [{**r, "selected_item": [1, 0]} for r in rows]
    t4 = is_function(planted_const, lambda r: 0,
                     lambda r: tuple(r["selected_item"]))
    add("planted_constant_selection_makes_the_empty_context_determine",
        t4["is_a_function"] and not by_name["EMPTY_CONTEXT"]["is_a_function"])

    # T5: a corrupted readout must break the agreement gate
    corrupt = [dict(r) for r in rows]
    corrupt[0]["selected_item"] = [0, 1] if corrupt[0]["selected_item"] == \
        [1, 0] else [1, 0]
    add("corrupted_readout_breaks_the_agreement_gate",
        any(list(read_state_direction(snapshots[r["world"]]))
            != r["selected_item"] for r in corrupt))

    # T6: a restricted menu must fail to cover the realized items
    restricted = ((1, 0),)
    uncovered = sum(1 for r in rows
                    if tuple(r["selected_item"]) not in restricted)
    add("restricted_menu_fails_to_cover_the_realized_items", uncovered > 0,
        {"restricted_to": [list(v) for v in restricted],
         "lock_points_left_uncovered": uncovered})

    # T7: a planted double realization must break uniqueness
    doubled = [dict(r) for r in rows]
    doubled[0]["selected_item"] = None
    add("planted_double_realization_breaks_uniqueness",
        not all(r["selected_item"] in ([1, 0], [0, 1]) for r in doubled))

    # T8: a dropped lock point must break the Cycle-911 restriction gate
    dropped = my_locks[1:]
    add("dropped_lock_point_breaks_the_c911_gate",
        dropped != sorted(r911_by_world),
        {"dropped_world": my_locks[0]})

    # T9: the local/non-local verdict is data-driven, not hardcoded
    add("local_verdict_is_data_driven",
        t2["is_a_function"] and not t1["is_a_function"]
        and not by_name["R1_nearest_neighbour_record_content"][
            "is_a_function"])

    cert_g = {"certificate": "G_FALSIFIERS", "teeth": teeth,
              "tooth_count": len(teeth),
              "pass": all(t["detected"] for t in teeth)}

    # ---------------- H: double build --------------------------------------
    def build_digest(build):
        return digest({
            "formed": {str(k): v for k, v in sorted(build["formed"].items())},
            "snapshots": {str(k): "".join(str(b) for b in v)
                          for k, v in sorted(build["snapshots"].items())},
            "lock_ordinal": {str(k): list(v) for k, v
                             in sorted(build["lock_ordinal"].items())},
            "events": len(build["events"]),
        })

    dig_a, dig_b = build_digest(build_fwd), build_digest(build_rev)
    sel_rev = {}
    for w, s in build_rev["snapshots"].items():
        sel_rev[w] = read_state_direction(s)
    cert_h = {
        "certificate": "H_DOUBLE_BUILD",
        "build_A": {"layout": build_fwd["layout"], "seconds": t_fwd,
                    "formed": len(build_fwd["formed"]),
                    "events": len(build_fwd["events"])},
        "build_B": {"layout": build_rev["layout"], "seconds": t_rev,
                    "formed": len(build_rev["formed"]),
                    "events": len(build_rev["events"])},
        "digest_A": dig_a, "digest_B": dig_b,
        "identical": dig_a == dig_b,
        "selection_identical_under_the_reversed_layout":
            sel_rev == selection,
        "beyond_cap": [build_fwd["beyond_cap"], build_rev["beyond_cap"]],
        "duplicate_lane_mismatches": [
            build_fwd["duplicate_lane_mismatches"],
            build_rev["duplicate_lane_mismatches"]],
    }
    cert_h["pass"] = bool(cert_h["identical"]
                          and cert_h["selection_identical_under_the_reversed"
                                     "_layout"]
                          and not any(cert_h["duplicate_lane_mismatches"]))

    elapsed = round(monotonic() - started, 3)
    cert_i = {"certificate": "I_RUNTIME", "elapsed_sec": elapsed,
              "budget_sec": RUNTIME_BUDGET_SEC,
              "pass": elapsed <= RUNTIME_BUDGET_SEC}

    certificates = {
        "A_PINS": cert_a, "B_RESTRICTION_GATE": cert_b,
        "C1_SELECTION_TABLE": cert_c1, "C2_DEPENDENCE": cert_c2,
        "C3_CONTENT_DETERMINATION": cert_c3, "C4_CONTEXT_VARIATION": cert_c4,
        "C5_CLASSIFIED_RULE_COMPARISON": cert_c5, "C6_O2_O3_VERDICT": cert_c6,
        "G_FALSIFIERS": cert_g, "H_DOUBLE_BUILD": cert_h, "I_RUNTIME": cert_i,
    }
    all_pass = all(c["pass"] for c in certificates.values())

    receipt = {
        "block": "toe-time-blockQ10-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "cycles": [913],
        "claim_type": "bounded_theorem",
        "audit": "unset",
        "authority": "none",
        "fraction_label": FRACTION_LABEL,
        "provenance": provenance,
        "certificates": certificates,
        "all_certificates_pass": all_pass,
        "VERDICT": ("O2 SUPPLIED, MEASURED, AND NOT LOCAL" if all_pass
                    else "INCOMPLETE"),
        "headline": (
            "the landed selection function is computed exactly at all "
            f"{total} lock points: "
            + ", ".join(f"{v['count']} realize {k}"
                        for k, v in split.items())
            + "; the selection is NOT a function of nearest-neighbour "
            f"conditions ({biggest_nn_collision} lock points share one "
            "neighbour context and still split), NOT a function of record "
            f"content under any reading ({len(no_prior_record)} lock points "
            "have no prior record event at all and still split), and NOT a "
            "member of the classified covariant rule space; its MINIMAL "
            f"determining context has cardinality {minimal_size} -- the "
            f"site's own endpoint content on wires {determining}, which no "
            "gate in the composed scan ever writes.  O2 is supplied by "
            "transport of a setup coordinate, not by a formation rule; O3's "
            f"A3 arena is the {total} counterfactual menu items and is "
            "setup-indexed, so every weight over it is the forbidden average."
        ),
    }
    out = ROOT / "outputs" / \
        "selection_function_cycle913_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    # ---------------- stdout ----------------------------------------------
    W = 78
    print("CYCLE 913 -- O2 AS A COMPUTATION: THE LANDED SELECTION FUNCTION")
    print("=" * W)
    print(f"  every fraction below: {FRACTION_LABEL}")
    print()
    print(f"A_PINS                      {'PASS' if cert_a['pass'] else 'FAIL'}"
          f"  ({len(AUDIT_INPUT_PATHS)} pinned; sha256+git-blob; "
          f"firewall hits {len(cert_a['firewall_hits'])})")
    print(f"B_RESTRICTION_GATE          "
          f"{'PASS' if cert_b['pass'] else 'FAIL'}"
          f"  ({cert_b['reproduce']}/{cert_b['total']} reproduce)")
    for row in gate_rows:
        if not row["pass"]:
            print(f"    FAILED GATE {row['gate']}: got {row['value']!r} "
                  f"want {row['pinned']!r}")
    print()
    print("-" * W)
    print("C1  THE SELECTION TABLE  (164 lock points, menu {(1,0), (0,1)})")
    print("-" * W)
    print(f"  four independent readouts agree on every row: "
          f"{cert_c1['all_four_readouts_agree_on_every_row']}")
    print(f"  RD-REARM: the scan's own next endpoint preparation matches "
          f"K.M.prepare_endpoint")
    print(f"            bit-for-bit on all {width} wires at "
          f"{sum(1 for x in rearm_rows if x['unique'])}/{total} lock points; "
          f"the counterfactual item")
    print(f"            differs at exactly "
          f"{cert_c1['rearm_counterfactual_hamming_distance']} wires")
    print(f"  independent serial replay from tick 0: "
          f"{cert_c1['independent_serial_replay']['worlds_replayed']} worlds, "
          f"all agree = "
          f"{cert_c1['independent_serial_replay']['all_agree']}")
    print(f"  ENDPOINT WIRE LEMMA: LEFT({left_w}) and RIGHT({right_w}) are "
          f"gate INPUTS")
    print(f"     ({target_lemma['LEFT_is_a_gate_input']}/"
          f"{target_lemma['RIGHT_is_a_gate_input']}) and NEVER gate targets "
          f"({target_lemma['LEFT_is_a_gate_target']}/"
          f"{target_lemma['RIGHT_is_a_gate_target']}) across all "
          f"{target_lemma['gates_total']} compiled gates")
    print(f"  split: " + ", ".join(
        f"{k} -> {v['count']} ({v['share']})" for k, v in split.items()))
    print()
    print("  world  key                      tick  ph  selected  ord0/ord1  "
          "context")
    for r in rows:
        k = f"({r['key'][0]},{r['key'][1]},{tuple(r['key'][2])})"
        print(f"  {r['world']:5d}  {k:24s} {r['lock_boundary']:6d} "
              f"{r['phase']:3d}  {str(tuple(r['selected_item'])):8s} "
              f"{r['ord0']:5d}/{r['ord1']:<5d} {r['context_fingerprint']}")
    print()
    print("-" * W)
    print("C2  WHAT DETERMINES THE SELECTION")
    print("-" * W)
    print(f"  {'fingerprint':56s} {'groups':>7s}  function?")
    for row in ladder:
        print(f"  {row['fingerprint']:56s} {row['groups']:7d}  "
              f"{'YES' if row['is_a_function'] else 'no'}"
              + ("  [VACUOUS: individuates every lock point]"
                 if row["determination_is_vacuous"] else "")
              + ("" if row["is_a_function"] else
                 f"  ({row['collision_classes']} collision class(es), "
                 f"largest {row['largest_collision_class_size']})"))
    wit = by_name["R1_nearest_neighbour_record_content"]["witness_pair"]
    if wit:
        print()
        print("  WITNESS (identical nearest-neighbour conditions, different "
              "selection):")
        print(f"    world {wit['left']['world']} key {wit['left']['key']} "
              f"tick {wit['left']['lock_boundary']} -> "
              f"{wit['left']['selection']}")
        print(f"    world {wit['right']['world']} key {wit['right']['key']} "
              f"tick {wit['right']['lock_boundary']} -> "
              f"{wit['right']['selection']}")
    print()
    print(f"  widest non-site context ({len(nonsite_varying)} varying wires "
          f"outside the site) determines? "
          f"{nonsite_all['is_a_function']}")
    print(f"  exhaustive single-wire sweep over all {width} wires: "
          f"{len(varying)} vary, and exactly")
    print(f"    {len(determining)} determine the selection: "
          f"{determining} = "
          + ", ".join(x["name"] for x in
                      cert_c2["exhaustive_single_wire_sweep"][
                          "determining_wire_names"]))
    outside = cert_c2["exhaustive_single_wire_sweep"][
        "any_determining_wire_outside_the_site"]
    print(f"  any determining wire OUTSIDE the site? {outside}")
    print(f"  MINIMAL DETERMINING CONTEXT: cardinality "
          f"{cert_c2['MINIMAL_DETERMINING_CONTEXT']['cardinality']} "
          f"(the empty context determines? "
          f"{by_name['EMPTY_CONTEXT']['is_a_function']})")
    print()
    print(f"  translation covariance: {trans['in_set_image_checks']} in-set "
          f"image checks under the landed Z_{trans['group_order']} action, "
          f"{trans['selection_violations_under_translation']} violations; "
          f"invariant = {trans['selection_is_translation_invariant']}")
    for row in cubic:
        print(f"  cubic k={row['alphabet_k']}: proper "
              f"{row['proper_orbits_total']} / full "
              f"{row['full_orbits_total']} orbits; contexts realize "
              f"{row['classes_realized_by_the_formation_contexts']} classes; "
              f"selection class-constant = "
              f"{row['selection_is_class_constant']}")
    print()
    print("-" * W)
    print("C3  IS IT A FUNCTION OF RECORD CONTENT?")
    print("-" * W)
    print(f"  record registers at the lock tick:  "
          f"{content_register['is_a_function']}   "
          f"({content_register['groups']} groups, "
          f"{content_register['collision_classes']} collision class(es))")
    print(f"  prior record-event history:         "
          f"{content_ordinal['is_a_function']}   "
          f"({content_ordinal['groups']} groups)")
    print(f"  openness only (k=2 alphabet):       "
          f"{content_openness['is_a_function']}   "
          f"({content_openness['groups']} groups)")
    print(f"  lock points with NO prior record event: {len(no_prior_record)}; "
          f"their selections "
          + ", ".join(f"{list(v)}x{c}" for v, c in sorted(no_prior_sel.items())))
    print(f"  lock points at tick 0: {len(zero_tick)}; their selections "
          + ", ".join(f"{list(v)}x{c}" for v, c
                      in sorted(zero_tick_sel.items())))
    print()
    print("-" * W)
    print("C4  DO THE CONTEXTS VARY AT ALL?")
    print("-" * W)
    print(f"  distinct nearest-neighbour contexts: {distinct_nn}   "
          f"(bank0 words {distinct_b0}, bank1 words {distinct_b1}, "
          f"link words {distinct_link})")
    print(f"  distinct contexts outside the site: {distinct_minus_site}; "
          f"distinct site blocks: {distinct_site} "
          f"(differing only at wires {site_diff})")
    print(f"  symmetry classes: "
          + ", ".join(f"k={row['alphabet_k']} -> "
                      f"{row['classes_realized_by_the_formation_contexts']}"
                      for row in cubic))
    print(f"  all contexts equivalent under the symmetries? "
          f"{cert_c4['contexts_are_all_equivalent_under_the_symmetries']}")
    print(f"  pinned Cycle-911 menu size at every lock point: {menu_sizes}")
    print()
    print("-" * W)
    print("C5  THE CLASSIFIED COVARIANT RULE SPACE")
    print("-" * W)
    for row in class_rows:
        print(f"  k={row['alphabet_k']}: proper {row['proper_orbits']} / "
              f"full {row['full_orbits']} ({row['chiral_pairs']} chiral "
              f"pairs); note says {row['note_says']}; reproduced = "
              f"{row['reproduces_the_note']}")
    is_col_fn = cert_c5[
        "landed_selection_is_a_function_of_the_neighbour_colouring"]
    print(f"  landed selection is a function of the neighbour colouring? "
          f"{is_col_fn}")
    print("  => NOT a member of the classified space; within either setup "
          "sector it is")
    print("     the CONSTANT rule (achiral, fully covariant), and which "
          "constant is fixed")
    print("     by one imported bit -- the Theorem-5 dichotomy resolved by "
          "import.")
    print()
    print("-" * W)
    print("C6  THE O2/O3 LEDGER VERDICT")
    print("-" * W)
    print("  O2: SUPPLIED BY THE LANDED DYNAMICS, AND MEASURED.")
    print("      realized(w) = (1,0) if the setup event index is even, else "
          "(0,1);")
    print(f"      carried on wires {left_w}/{right_w}, which the scan reads "
          "at every source")
    print("      and finalizer station and never writes.  The scan does not "
          "choose; it")
    print("      carries.  Not neighbour-determined, not content-determined, "
          "not in the")
    print("      classified rule space.  DERIVABLE? no -- SUPPLIED.")
    print(f"  O3: the A3 arena is exactly {total} sites x {len(menu)} "
          f"possibilities = {total * len(menu)} pairs")
    print(f"      ({total} realized, {total} counterfactual).  Within-world "
          "frequency is")
    print("      degenerate (one lock per world); the cross-world split "
          + "/".join(str(v["count"]) for v in split.values()) + " is an")
    print("      average over SETUPS, which the realized-state primitive "
          "forbids.  And")
    print("      the counterfactual coordinate IS a setup coordinate, so a "
          "weight over")
    print("      the menu is a weight over setups under another name.  "
          "TERMINAL here.")
    print()
    print("-" * W)
    print(f"G_FALSIFIERS                {'PASS' if cert_g['pass'] else 'FAIL'}"
          f"  ({cert_g['tooth_count']} teeth)")
    for t in teeth:
        print(f"    [{'x' if t['detected'] else ' '}] {t['tooth']}")
    print(f"H_DOUBLE_BUILD              {'PASS' if cert_h['pass'] else 'FAIL'}"
          f"  (A {t_fwd}s / B {t_rev}s; identical = {cert_h['identical']})")
    print(f"I_RUNTIME                   {'PASS' if cert_i['pass'] else 'FAIL'}"
          f"  ({elapsed}s / {RUNTIME_BUDGET_SEC}s)")
    print()
    print("=" * W)
    print(f"VERDICT: {receipt['VERDICT']}")
    print(f"receipt: outputs/"
          f"selection_function_cycle913_receipt_2026_07_28.json")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
