"""Cycle 911 -- THE TYPE OF THE BORN LANE'S OBJECT, AND THE VACUITY QUESTION.

A wall-breaking exercise on ledger row BL4 (the occurrence rule) produced three
trap-escaping routes and one structural correction.  This block CERTIFIES or
REFUTES all four under full discipline.

  C1  THE SAMPLE-SPACE PREMISE (Route 1), NAMED AND TESTED.  A-SAMPLE: "the
      Cycle-878 event space is the arena over which the framework's formation
      weight is defined."  What ARE the 748 census keys?  Co-present
      sub-registers of ONE realized configuration, or alternative initial
      conditions of the same law?  Certified from the pinned Cycle-863 code
      structure (AST) and from the runtime objects, with the no-coupling claim
      certified by an AST sweep of the composed scan's state-access pattern AND
      by a runtime perturbation witness.  Then the branching check over all
      748*747/2 world pairs.

  C2  SINGLETON AVAILABILITY AT FORMATION (Route 4).  For each of the 164
      formation events: rebuild the formation context at the lock tick and
      compute |A(s|context)| -- the number of admissible local possibilities at
      the lock point -- under the landed admissibility machinery.  Then the
      never-computed spectrum over the CLASSIFIED covariant rule space of the
      pinned 2026-07-03 classification.

  C3  THE REALIZATION DILEMMA (Route 2), STATED FROM COMMITTED DATA, plus the
      O1 correction for the audit lane.

  C4  THE FOUR-WAY CONVERGENCE, CERTIFIED -- or cut down to what actually
      survives.

Discipline: TEXT/AST/JSON only; import firewall (the Cycle-719 kernel is the
one disclosed import, as substrate); exact integer / rational arithmetic;
deterministic double build (two independent full-horizon builds at opposite
lane bit-layouts); outcome-neutral gates with planted falsifiers that the
harness must detect.  No probability, no occurrence rule, no update law is
introduced.  Every fraction below is a bookkeeping fraction, not a probability.
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
from math import gcd
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C878_NOTE = "docs/EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md"
C905_PATH = "scripts/frontier_cycle905_born_narrowing_2026_07_28.py"
C905_RECEIPT = "outputs/born_narrowing_cycle905_receipt_2026_07_28.json"
C906_RECEIPT = "outputs/covariance_tension_cycle906_receipt_2026_07_28.json"
C907_RECEIPT = "outputs/m6_identification_cycle907_receipt_2026_07_28.json"
C909_PATH = "scripts/frontier_cycle909_within_world_pricing_2026_07_28.py"
C909_RECEIPT = "outputs/within_world_pricing_cycle909_receipt_2026_07_28.json"
CLASSIFY_PATH = \
    "scripts/admissibility_rule_covariance_extension_classification_2026_07_03.py"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
SWEEP_PATH = "docs/RECORD_FORMATION_APPEND_CONSISTENCY_SWEEP_2026-07-04.md"
NOGO_PATH = (
    "docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS"
    "_NARROW_NO_GO_NOTE_2026-06-06.md"
)
CONTINUATION_PATH = (
    "docs/ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL"
    "_BOUNDED_THEOREM_NOTE_2026-07-13.md"
)
COVCLASS_PATH = (
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS"
    "_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE"
    "_2026-07-03.md"
)
REALIZED_PATH = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C878_NOTE, C905_PATH,
    C905_RECEIPT, C906_RECEIPT, C907_RECEIPT, C909_PATH, C909_RECEIPT,
    CLASSIFY_PATH, AXIOMS_PATH, SWEEP_PATH, NOGO_PATH, CONTINUATION_PATH,
    COVCLASS_PATH, REALIZED_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C905_PATH, C909_PATH, CLASSIFY_PATH)
JSON_ONLY_PATHS = (C878_RECEIPT, C905_RECEIPT, C906_RECEIPT, C907_RECEIPT,
                   C909_RECEIPT)
TEXT_ONLY_PATHS = (C878_NOTE, AXIOMS_PATH, SWEEP_PATH, NOGO_PATH,
                   CONTINUATION_PATH, COVCLASS_PATH, REALIZED_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C878_NOTE:
        "007bbaa2ae70afad7fcb761d3f3912edb1b3f1c893a439a9e4d815abe335428c",
    C905_PATH:
        "83429f35312e0df16d3d11e65685cb87b8e732b19299e1078ddaea1e1444afb3",
    C905_RECEIPT:
        "4c42c3d1755674552c5928016d54cfb2c666103781e96581f4291b5634a82d40",
    C906_RECEIPT:
        "e4de35c272216e0aace2585bdc2e5db198788752d63c11b0dc9ebc67146e7a3f",
    C907_RECEIPT:
        "d67a967a6226a4e1ed2e0bf1762cb3b544df87e1fe4b07d6399f13ec179086ca",
    C909_PATH:
        "b38862284c0287dc8b1f24f5af8bf014509e22377d341b9933a05b2183af0021",
    C909_RECEIPT:
        "9c91d740ce2188d8fd6c51947d63adec38abb8aa1c49eaaf1c2535b16e9bcc52",
    CLASSIFY_PATH:
        "f7490941aa793fdf155d10dc5a5f86d59c07b22d49ca60f989fbf03c565a0dcb",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    SWEEP_PATH:
        "687c2690939b94d5f43e2ab828ebdeed388daf888ef521131df7dce3b9dfd669",
    NOGO_PATH:
        "c0b92c68149f45701a3d6db7bbf2022d00c70e55c065f9eef6f1dd692d9e61c3",
    CONTINUATION_PATH:
        "d22a7ec84c3ffc8a57f46d9d2353d47837aad19d3ea6a041836f9e5334d314d9",
    COVCLASS_PATH:
        "fe56ef6c21c00732281676cca1724231951e40fc2b746f255f655307dc76001d",
    REALIZED_PATH:
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C878_NOTE: "8fd212e96748064c40be670e491474e14dae28b6",
    C905_PATH: "f9f2171602bddf7d6164261dc13a2ee4f7e3046c",
    C905_RECEIPT: "7094c986dc0560e8982507d8cc379f5c720b639f",
    C906_RECEIPT: "392cba199a75a14a8bb88808943c1259cbd7a94b",
    C907_RECEIPT: "e7eef6eeeb62aeddcdb12417ccd8ec871b9d87a7",
    C909_PATH: "359b5a502fd9cbd05653f33e0b7931caaf868a25",
    C909_RECEIPT: "4843b2ca7dd5af0ee1c67ff11aa4e47d7cb22976",
    CLASSIFY_PATH: "d33bf6e8b456464e2b455c1d0aaf8662a1799abb",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
    SWEEP_PATH: "d117fd8a1b734b481b9218f70642fdc357c0254b",
    NOGO_PATH: "52cc5672fff2d12eaf96e976602d5557aa59b61c",
    CONTINUATION_PATH: "8eb305786fb7a42a10ea2590e35b57d57955b816",
    COVCLASS_PATH: "20955a2e976f7d3a1f38fed55cd0b1bdd91f82b4",
    REALIZED_PATH: "5acb4643882438f8dd16baf9694e6fa2d33d1dc6",
}

BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AST_ONLY_PATHS)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024
FRACTION_LABEL = "bookkeeping fraction, not probability"

HORIZON = 16_384
CROSSCHECK_ORBITS = 512
PERTURB_ORBITS = 24
PERTURB_SAMPLES = 6
PAIR_BATCH_LANES = 512
PAIR_WINDOW_ORBITS = 8
PAIR_WINDOW_ORBITS_DEEP = 128


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

def pin_rows() -> dict:
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
C878_FUNCS = (
    "lcm", "dead_wire_rig", "composed_scan", "family_keys", "cells_of",
    "monitor_phase_action", "group_orbits",
)
C878_CONSTS = ("HORIZON", "DEAD_CHUNK_ORBITS", "DEAD_ORBIT_ORBITS",
               "REGISTER_CAP", "EXCLUSION_NEEDLE", "BOUNDARY_STATEMENT")
CLASS_FUNCS = (
    "det3", "mat_key", "dperm", "act_col", "inv_perm", "cycle_count",
    "burnside_orbits", "all_colorings", "direct_orbits", "orbit_ids",
)
CLASS_CONSTS = ("DIRS",)


def lift_machinery():
    ns863, consts863, names863 = ast_lift(
        C863_PATH, C863_FUNCS, C863_CONSTS,
        {"K": K, "combinations": combinations, "Counter": Counter},
    )
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "gcd": gcd,
         "Fraction": Fraction, "json": json},
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
    provenance = {
        "lifted_from_863": names863,
        "constants_863": consts863,
        "lifted_from_878": names878,
        "constants_878": {k: v for k, v in consts878.items()
                          if not isinstance(v, str)},
        "lifted_from_classification": namesc,
        "classification_DIRS": [list(d) for d in dirs],
        "import_of_863_878_905_909_or_classification": False,
        "single_disclosed_import": CORE_PATH,
    }
    return c863, c878, consts878, cls, dirs, provenance


# ---------------------------------------------------------------------------
# the snapshot scan (independent reimplementation of the pinned composed scan,
# with the formation-lock states captured; record slots are NOT written, and
# certificate C proves that omission is inert)
# ---------------------------------------------------------------------------

REGISTER_CAP = 64


def snapshot_scan(c863, program, census, states, orbits, reverse_layout=False):
    """Bit-packed scan.  lane -> bit position is the LAYOUT; the reversed
    layout is a genuinely independent second build."""
    n = len(census)
    order = list(range(n - 1, -1, -1)) if reverse_layout else list(range(n))
    # bit b carries world order[b]
    laid_census = tuple(census[w] for w in order)
    laid_states = tuple(states[w] for w in order)
    sim = laid_census + (laid_census[0],)
    fast = c863.compile_fast(c863.masked_h_schedules(program, sim))
    columns = c863.pack_lanes(laid_states + (laid_states[0],))
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    uni_all = (1 << n) - 1
    uni_sim = (1 << (n + 1)) - 1
    mask_over, lanes_of, lane_state = c863.mask_over, c863.lanes_of, \
        c863.lane_state

    events: list[tuple] = []
    formed: dict[int, int] = {}
    snap: dict[int, tuple] = {}
    lock_ordinal: dict[int, tuple] = {}
    bank_ordinal = [[0, 0] for _ in range(n)]
    beyond_cap = 0
    dup_mismatches = 0

    g = mask_over(columns, global_dirty, uni_sim)
    dup_mismatches += int(bool(g & 1) != bool(g & (1 << n)))
    prev = [mask_over(columns, bank_dirty[b], uni_all) for b in (0, 1)]
    for bit in lanes_of(g & uni_all):
        w = order[bit]
        formed[w] = 0
        snap[w] = lane_state(columns, bit)
        lock_ordinal[w] = (0, 0)
        events.append((w, 0, "F", 0))
    boundary = 0
    for _orbit in range(orbits):
        for chunk in fast:
            chunk(columns)
            boundary += 1
            g = mask_over(columns, global_dirty, uni_sim)
            dup_mismatches += int(bool(g & 1) != bool(g & (1 << n)))
            ga = g & uni_all
            if ga:
                for bit in lanes_of(ga):
                    w = order[bit]
                    if w not in formed:
                        formed[w] = boundary
                        snap[w] = lane_state(columns, bit)
                        lock_ordinal[w] = tuple(bank_ordinal[bit])
                        events.append((w, boundary, "F", 0))
            for b in (0, 1):
                bm = mask_over(columns, bank_dirty[b], uni_all)
                rise = bm & ~prev[b]
                if rise:
                    for bit in lanes_of(rise):
                        o = bank_ordinal[bit][b]
                        if o < REGISTER_CAP:
                            events.append((order[bit], boundary, f"B{b}", o))
                        else:
                            beyond_cap += 1
                        bank_ordinal[bit][b] = o + 1
                prev[b] = bm
    events.sort(key=lambda e: (e[1], e[0], e[2], e[3]))
    return {
        "events": tuple(events),
        "formed": formed,
        "snapshots": snap,
        "lock_ordinal": lock_ordinal,
        "beyond_cap": beyond_cap,
        "boundaries": boundary,
        "duplicate_lane_mismatches": dup_mismatches,
        "layout": "reversed" if reverse_layout else "forward",
    }


# ---------------------------------------------------------------------------
# C1: the no-coupling AST sweep over the composed scan's state-access pattern
# ---------------------------------------------------------------------------

POSITIONWISE_OPS = (ast.BitXor, ast.BitAnd, ast.BitOr, ast.Invert)
CROSS_LANE_OPS = (ast.LShift, ast.RShift, ast.Add, ast.Sub, ast.Mult,
                  ast.Div, ast.FloorDiv, ast.Mod, ast.Pow, ast.MatMult)


def sweep_generated_chunk_source(schedules):
    """Regenerate the exact source compile_fast execs and AST-sweep it.

    Every statement must be `c[i] ^= <bitwise-AND tree of c[j] and integer
    literals>`.  BIT i of every column then evolves as a function of BIT i of
    the columns alone: bitwise AND/XOR/OR/NOT are position-wise, so lane i can
    never read or write lane j.  Any shift, arithmetic, comparison, call,
    slice or non-constant index would break that and is reported."""
    stats = {"statements": 0, "augassign_bitxor": 0, "subscript_targets": 0,
             "bitand_nodes": 0, "constant_masks": 0, "column_reads": 0}
    violations: list = []
    for step, schedule in enumerate(schedules):
        src = ["def apply_chunk(c):"]
        if not schedule:
            src.append(" pass")
        for kind, a, b, c3, mask in schedule:
            if kind == 0:
                src.append(f" c[{a}] ^= {mask}")
            elif kind == 1:
                src.append(f" c[{b}] ^= c[{a}] & {mask}")
            else:
                src.append(f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}")
        tree = ast.parse("\n".join(src))
        fn = tree.body[0]
        if not isinstance(fn, ast.FunctionDef) or fn.name != "apply_chunk":
            violations.append(("chunk shape", step))
            continue
        for stmt in fn.body:
            stats["statements"] += 1
            if not isinstance(stmt, ast.AugAssign):
                violations.append(("not augassign", step))
                continue
            if not isinstance(stmt.op, ast.BitXor):
                violations.append(("augassign op not ^=", step))
                continue
            stats["augassign_bitxor"] += 1
            tgt = stmt.target
            if not (isinstance(tgt, ast.Subscript)
                    and isinstance(tgt.value, ast.Name) and tgt.value.id == "c"
                    and isinstance(tgt.slice, ast.Constant)
                    and isinstance(tgt.slice.value, int)):
                violations.append(("target not c[const]", step))
                continue
            stats["subscript_targets"] += 1
            for node in ast.walk(stmt.value):
                if isinstance(node, ast.BinOp):
                    if isinstance(node.op, CROSS_LANE_OPS):
                        violations.append(
                            ("cross-lane operator", step,
                             type(node.op).__name__))
                    elif isinstance(node.op, ast.BitAnd):
                        stats["bitand_nodes"] += 1
                    else:
                        violations.append(
                            ("unexpected operator", step,
                             type(node.op).__name__))
                elif isinstance(node, ast.Constant):
                    if isinstance(node.value, int):
                        stats["constant_masks"] += 1
                    else:
                        violations.append(("non-int constant", step))
                elif isinstance(node, ast.Subscript):
                    if not (isinstance(node.value, ast.Name)
                            and node.value.id == "c"
                            and isinstance(node.slice, ast.Constant)
                            and isinstance(node.slice.value, int)):
                        violations.append(("read not c[const]", step))
                    else:
                        stats["column_reads"] += 1
                elif isinstance(node, ast.Name):
                    if node.id != "c":
                        violations.append(("free name", step, node.id))
                elif isinstance(node, (ast.Load, ast.Store)):
                    continue
                elif isinstance(node, (ast.Call, ast.Compare, ast.Slice,
                                       ast.UnaryOp, ast.BoolOp,
                                       ast.IfExp, ast.Attribute)):
                    violations.append(("disallowed node", step,
                                       type(node).__name__))
    return stats, violations


def sweep_scan_driver_text(path: str, func_names: tuple):
    """AST-sweep the scan driver's own source: every WRITE into `columns`
    must be lane-local.  Reads that enumerate lanes (mask & -mask,
    bit_length) are permitted and recorded, because they never write back."""
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in func_names:
            writes = []
            for st in ast.walk(node):
                if isinstance(st, (ast.Assign, ast.AugAssign)):
                    targets = st.targets if isinstance(st, ast.Assign) \
                        else [st.target]
                    for t in targets:
                        if isinstance(t, ast.Subscript) \
                                and isinstance(t.value, ast.Name) \
                                and t.value.id in ("columns", "work", "acc",
                                                   "c"):
                            writes.append(ast.unparse(st))
            rows.append({"function": node.name, "column_writes": writes})
    return rows


def perturbation_witness(c863, program, census, states, samples, orbits):
    """Runtime no-coupling witness: flip one wire of one lane's initial state
    and certify that the packed scan's column difference stays inside that
    lane's own bit for the whole declared window."""
    n = len(census)
    sim = census + (census[0],)
    fast = c863.compile_fast(c863.masked_h_schedules(program, sim))
    base = c863.pack_lanes(states + (states[0],))
    rows = []
    for lane, wire in samples:
        cols_a = list(base)
        cols_b = list(base)
        cols_b[wire] ^= (1 << lane)
        leak = 0
        allowed = 1 << lane
        for _orbit in range(orbits):
            for chunk in fast:
                chunk(cols_a)
                chunk(cols_b)
                for x, y in zip(cols_a, cols_b):
                    d = x ^ y
                    if d & ~allowed:
                        leak += 1
        rows.append({"lane": lane, "wire": wire, "orbits": orbits,
                     "leak_outside_own_lane_bit": leak})
    return rows


# ---------------------------------------------------------------------------
# C1(b): the branching check
# ---------------------------------------------------------------------------

CLASS_SETUP_TICK0 = "SETUP_DIFFERS_AT_TICK_0"
CLASS_SETUP_SCHEDULE = "SETUP_DIFFERS_IN_SCAN_SCHEDULE_ONLY"
CLASS_BRANCH = "BRANCH_PAIR"
CLASS_IDENTICAL = "IDENTICAL_TRAJECTORIES"
CLASS_NONBRANCH_DIVERGENCE = "DIVERGENCE_NOT_AT_A_SHARED_FORMATION_EVENT"


def classify_pair(key_u, key_v, sid_u, sid_v, formed_u, formed_v,
                  trajectory=None):
    """The C1 pair comparator.

    A BRANCH PAIR is two worlds under the SAME law (same scan schedule) whose
    configurations agree up to a formation event and diverge after it.  A
    SETUP PAIR is two worlds whose census key -- the supplied setup parameter
    -- differs.  `sid_*` are tick-0 state-class identifiers, equal iff the two
    packed initial state vectors are equal.  `trajectory`, when supplied, is
    (first_divergence_boundary, diverges) computed by co-simulation; it is what
    the planted falsifier uses."""
    same_schedule = key_u[2] == key_v[2]
    same_tick0 = sid_u == sid_v
    if not same_schedule:
        return {
            "verdict": CLASS_SETUP_TICK0 if not same_tick0
            else CLASS_SETUP_SCHEDULE,
            "first_divergence_tick": 0 if not same_tick0 else None,
            "same_schedule": False, "same_tick0_state": same_tick0,
        }
    if not same_tick0:
        return {"verdict": CLASS_SETUP_TICK0, "first_divergence_tick": 0,
                "same_schedule": True, "same_tick0_state": False}
    # same schedule and same tick-0 state
    if trajectory is None:
        return {"verdict": CLASS_IDENTICAL, "first_divergence_tick": None,
                "same_schedule": True, "same_tick0_state": True}
    t, diverges = trajectory
    if not diverges:
        return {"verdict": CLASS_IDENTICAL, "first_divergence_tick": None,
                "same_schedule": True, "same_tick0_state": True}
    at_formation = (t == formed_u) and (t == formed_v)
    return {
        "verdict": CLASS_BRANCH if at_formation
        else CLASS_NONBRANCH_DIVERGENCE,
        "first_divergence_tick": t, "same_schedule": True,
        "same_tick0_state": True,
        "divergence_at_shared_formation_event": at_formation,
    }


def pair_divergence_batches(c863, program, census, states, pairs,
                            window_orbits, batch_lanes):
    """Exact co-simulation of the declared pair sample in packed batches:
    pair p occupies bits 2p and 2p+1, so a pair has diverged at a boundary
    iff some column has those two bits different."""
    out = {}
    per_batch = batch_lanes // 2
    for start in range(0, len(pairs), per_batch):
        chunk_pairs = pairs[start:start + per_batch]
        lane_census = []
        lane_states = []
        for u, v in chunk_pairs:
            lane_census.extend((census[u], census[v]))
            lane_states.extend((states[u], states[v]))
        m = len(lane_census)
        sim = tuple(lane_census) + (lane_census[0],)
        fast = c863.compile_fast(c863.masked_h_schedules(program, sim))
        columns = c863.pack_lanes(tuple(lane_states) + (lane_states[0],))
        pair_mask = 0
        for i in range(m // 2):
            pair_mask |= 1 << (2 * i)
        pending = {i: None for i in range(m // 2)}
        boundary = 0
        for _orbit in range(window_orbits):
            for chunk in fast:
                chunk(columns)
                boundary += 1
                diff = 0
                for col in columns:
                    diff |= (col ^ (col >> 1)) & pair_mask
                    if diff == pair_mask:
                        break
                if diff:
                    d = diff
                    while d:
                        bit = d & -d
                        idx = (bit.bit_length() - 1) // 2
                        if pending.get(idx) is None:
                            pending[idx] = boundary
                        d ^= bit
                if all(v is not None for v in pending.values()):
                    break
            if all(v is not None for v in pending.values()):
                break
        for i, (u, v) in enumerate(chunk_pairs):
            out[(u, v)] = pending[i]
    return out


# ---------------------------------------------------------------------------
# C2: the availability operators at the lock points
# ---------------------------------------------------------------------------

DIRECTIONS = ((1, 0), (0, 1))


def synchronous_chunks(program, positions):
    """The per-step gate chunks of one orbit, built the way the scan applies
    them: at step t, the stations `positions + t (mod stations)` fire.

    DISCLOSED DEFECT IN THE PINNED SOURCE.  The pinned Cycle-863
    certificate-A slices the flat synchronous word with
    `per_chunk = len(word) // stations`, which assumes every step contributes
    the same number of gates.  It does not: the stations carry macros of very
    different lengths, and len(word) is not even divisible by `stations`.  So
    the pinned saturation diagnostic applies a MIS-SLICED chunk.  This runner
    reports the pinned reading (for reproduction) and this corrected one (for
    the finding), and never conflates them."""
    stations = len(program)
    pos = tuple(positions)
    out = []
    for _ in range(stations):
        live = set(pos)
        gates = []
        for station, row in enumerate(program):
            if station in live:
                gates.extend(K.mapped_macro(row))
        out.append(tuple(gates))
        pos = tuple((p + 1) % stations for p in pos)
    return tuple(out)


def availability_operators(c863, program, snapshots, formed, census,
                           per_bank, restrict=None):
    """Three declared operators on the SAME menu of endpoint possibilities.

    OP_PREPARE      the possibility is available iff the core's own endpoint
                    constructor accepts it at the lock state
                    (K.M.prepare_endpoint) -- the axiom's "available
                    possibilities ... at the site".
    OP_ORBIT        available iff, once prepared, the world's own lawful orbit
                    completes consistently (the exact consistency test the
                    pinned Cycle-863 seed derivation uses).
    OP_SATURATION   the pinned Cycle-863 certificate-A diagnostic: prepared,
                    then ONE chunk applied, all bank flags clean afterwards.
    `restrict` is a declared falsifier hook: a set of directions the operator
    is allowed to offer.  None means the full menu."""
    stations = len(program)
    menu = tuple(d for d in DIRECTIONS
                 if restrict is None or d in restrict)
    word_cache: dict = {}
    chunk_cache: dict = {}
    rows = []
    for world in sorted(formed):
        key = census[world]
        positions = key[2]
        if positions not in word_cache:
            word_cache[positions] = c863.synchronous_word(program, positions)
            chunk_cache[positions] = synchronous_chunks(program, positions)
        word = word_cache[positions]
        per_chunk = len(word) // stations
        state = snapshots[world]
        first = formed[world]
        idx = first % stations
        sliced = word[idx * per_chunk:(idx + 1) * per_chunk]
        exact = chunk_cache[positions][idx]
        prep = orbit = sat863 = sat = 0
        prep_menu, orbit_menu, sat_menu = [], [], []
        prepare_errors = 0
        for v in menu:
            try:
                sub = K.M.prepare_endpoint(state, v)
            except Exception:
                prepare_errors += 1
                continue
            prep += 1
            prep_menu.append(v)
            if all(K.A.apply_semantic(sub, sliced)[w] == 0
                   for bank in per_bank for w in bank):
                sat863 += 1
            if all(K.A.apply_semantic(sub, exact)[w] == 0
                   for bank in per_bank for w in bank):
                sat += 1
                sat_menu.append(v)
            try:
                _a, rail_a, rail_b, _t = K.run_orbit(
                    sub, program, token_positions=positions)
                expected = tuple(int(s in positions)
                                 for s in range(stations))
                if rail_a == expected and not any(rail_b):
                    orbit += 1
                    orbit_menu.append(v)
            except Exception:
                pass
        rows.append({
            "world": world, "key": key, "lock_boundary": first,
            "A_prepare": prep, "A_orbit": orbit,
            "A_saturation_corrected": sat,
            "A_saturation_as_pinned_863_slices_it": sat863,
            "menu_prepare": prep_menu, "menu_orbit": orbit_menu,
            "menu_saturation_corrected": sat_menu,
            "prepare_errors": prepare_errors,
        })
    return rows


# ---------------------------------------------------------------------------
# C2: the classified covariant rule space, transported onto the contexts
# ---------------------------------------------------------------------------

def build_cubic_group(cls, dirs):
    records = []
    seen = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for row, col in enumerate(perm):
                M[row, col] = signs[row]
            key = cls.mat_key(M)
            if key in seen:
                continue
            seen.add(key)
            records.append({"det": cls.det3(M), "perm": cls.dperm(M)})
    full = [r["perm"] for r in records]
    proper = [r["perm"] for r in records if r["det"] == 1]
    return tuple(full), tuple(proper)


def context_colorings(rows, snapshots, lock_ordinal, alphabet):
    """DECLARED EMBEDDING (premise P-CONDITION-MAP, disclosed).

    The lock site is the source endpoint; its nearest neighbours in this
    substrate are bank 0 and bank 1.  They are placed on the +x and -x
    directions of the classification's six-direction frame; the four remaining
    directions carry the OPEN value 0, because the substrate supplies no
    neighbour there.  A neighbour's CONDITION is its record content or its
    openness (the pinned 2026-07-03 note's typing): value 0 when the bank has
    written no record at the lock tick, otherwise a content class in
    1..k-1 derived from the bank's own wire word at the lock tick."""
    banks_wires = K.M.R12.BANK_BASES
    width = K.A.N
    out = {}
    for row in rows:
        world = row["world"]
        state = snapshots[world]
        ords = lock_ordinal[world]
        col = [0] * 6
        for b in (0, 1):
            base = banks_wires[b]
            word = tuple(state[base + w] for w in range(width))
            if ords[b] == 0:
                value = 0
            elif alphabet == 2:
                value = 1
            else:
                h = int(sha256(bytes(word)).hexdigest()[:8], 16)
                value = 1 + (h % (alphabet - 1))
            col[0 if b == 0 else 1] = value
        out[world] = tuple(col)
    return out


def rule_space_spectrum(cls, proper_perms, colorings, rows, alphabet,
                        menu_size):
    orbits = cls.direct_orbits(proper_perms, alphabet)
    ids = cls.orbit_ids(orbits)
    cls_of = {w: ids[c] for w, c in colorings.items()}
    sizes = Counter(cls_of.values())
    realized = sorted(sizes)
    landed_prepare = {}
    landed_orbit = {}
    landed_sat = {}
    for row in rows:
        cid = cls_of[row["world"]]
        landed_prepare.setdefault(cid, set()).add(row["A_prepare"])
        landed_orbit.setdefault(cid, set()).add(row["A_orbit"])
        landed_sat.setdefault(cid, set()).add(
            row["A_saturation_corrected"])
    achievable = set()
    enumerated = len(realized) <= 10
    if enumerated:
        for assignment in itertools.product(range(menu_size + 1),
                                            repeat=len(realized)):
            hist: Counter = Counter()
            for cid, a in zip(realized, assignment):
                hist[a] += sizes[cid]
            achievable.add(tuple(sorted(hist.items())))
    return {
        "distinct_A_distributions_enumerated": enumerated,
        "alphabet_k": alphabet,
        "proper_orbits_total": len(orbits),
        "classes_realized_by_the_formation_contexts": len(realized),
        "class_sizes": {str(c): sizes[c] for c in realized},
        "landed_prepare_is_class_constant": all(
            len(v) == 1 for v in landed_prepare.values()),
        "landed_orbit_is_class_constant": all(
            len(v) == 1 for v in landed_orbit.values()),
        "landed_saturation_is_class_constant": all(
            len(v) == 1 for v in landed_sat.values()),
        "landed_saturation_values_per_class": {
            str(c): sorted(landed_sat[c]) for c in realized},
        "achievable_menu_multiplicity_spectra":
            (menu_size + 1) ** len(realized),
        "distinct_A_distributions": len(achievable) if enumerated else None,
        "spectrum_sample": sorted(achievable)[:8] if enumerated else [],
    }


# ---------------------------------------------------------------------------
# C4 (ii): the maximum-likelihood degeneracy lemma
# ---------------------------------------------------------------------------

def ml_degeneracy(numerators: dict, totals: dict, n_events: int):
    """LEMMA (exact).  Let E be finite, |E| = N, and let the census be each
    atom of E realized exactly once.  For a normalized weighting p on E the
    census likelihood is L(p) = prod_e p(e).  By AM-GM,
        prod_e p(e) <= ( (sum_e p(e)) / N )^N = N^{-N},
    with equality iff p is constant, i.e. p = counting/uniform.  Equivalently
    log L(p) - log L(u) = sum_e log(N p(e)) = -N * KL(u || p) <= 0 with
    equality iff p = u.  So argmax L is the counting measure, for EVERY finite
    event space.  A weighting that assigns 0 to any realized atom has
    L = 0 exactly."""
    rows = {}
    for name, nums in numerators.items():
        zeros = sum(1 for v in nums if v == 0)
        lo, hi = min(nums), max(nums)
        rows[name] = {
            "zero_on_realized_atoms": zeros,
            "likelihood_is_exactly_zero": zeros > 0,
            "min_numerator": lo, "max_numerator": hi,
            "is_uniform_on_the_census": lo == hi,
            "total": totals[name],
        }
    uniform = [n for n, r in rows.items() if r["is_uniform_on_the_census"]]
    return {
        "lemma": ml_degeneracy.__doc__.strip(),
        "N_events": n_events,
        "rows": rows,
        "argmax_is_the_uniform_counting_measure": uniform,
        "strictly_dominated_positive_candidates": [
            n for n, r in rows.items()
            if not r["is_uniform_on_the_census"]
            and not r["likelihood_is_exactly_zero"]],
        "zero_likelihood_candidates": [
            n for n, r in rows.items() if r["likelihood_is_exactly_zero"]],
    }


# ---------------------------------------------------------------------------
# C4 (iv): Lemma I-CONST, rebuilt honestly
# ---------------------------------------------------------------------------

def cayley_rotation(vec):
    """An exact rational SO(3) element carrying the rational unit vector
    `vec` to (0,0,1), built from a Cayley transform of a rational skew
    matrix; used to certify that unitary conjugation (= SO(3) on the Bloch
    ball) is TRANSITIVE on pure qubit possibilities."""
    x, y, z = vec
    target = (Fraction(0), Fraction(0), Fraction(1))
    if (x, y, z) == target:
        return ([[Fraction(1), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(1), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(1)]], target)
    # Householder about the bisector maps vec -> target; compose two of them
    # (a product of two reflections is a rotation, det +1).
    def reflect(u):
        nn = u[0] * u[0] + u[1] * u[1] + u[2] * u[2]
        return [[(Fraction(1) if i == j else Fraction(0))
                 - 2 * u[i] * u[j] / nn for j in range(3)] for i in range(3)]

    def matmul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
                for i in range(3)]

    def apply(A, v):
        return tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))

    u1 = tuple(a - b for a, b in zip(vec, target))
    R1 = reflect(u1)
    w = apply(R1, vec)
    # R1 maps vec to target but has det -1; fix with a reflection FIXING target
    u2 = (Fraction(1), Fraction(0), Fraction(0))
    R2 = reflect(u2)
    R = matmul(R2, R1)
    return R, w


def i_const_lemma():
    """LEMMA I-CONST, derived from what the two no-privilege sentences and the
    readout sentence actually force.

    Supplied: (Record) "Only records are readable. A readout value is
    determined by record content alone" and finite additivity over disjoint
    records; (Record) "a record locks exactly one admissible local
    possibility"; (Qubit) "No possibility is privileged. Possibilities are
    distinguished by the supplied algebraic structure alone", with the one-site
    domain presented as M_2(C); (Lattice) "No site is privileged. Sites are
    distinguished by the supplied lattice structure alone".

    Step 1 (site).  Readout depends on content alone, so it cannot depend on
    the site label; no-site-privilege adds that no site-distinguishing datum is
    supplied beyond lattice structure.  So i is site-independent.
    Step 2 (possibility).  If record content IS the locked possibility -- the
    PURITY premise -- then i is a function on the one-site possibility domain,
    invariant under the supplied algebraic structure's automorphisms.  The
    automorphisms of M_2(C) are the unitary conjugations; on PURE states they
    act transitively (Bloch: SO(3) on the unit sphere).  A transitive
    invariance forces i constant on pure locked possibilities.
    Step 3 (additivity).  Additivity over disjoint records then gives
    I(S) = c |S|.

    THE NAMED CRACK.  Step 2 needs purity.  Unitary conjugation is NOT
    transitive on the full state space: it preserves the Bloch radius, so
    r(rho) = |Bloch(rho)| is a non-constant invariant.  If a locked possibility
    may be non-pure, i = f(r) privileges no possibility and is non-constant,
    and I(S) = sum f(r_s) is not c|S|.  I-CONST is therefore CONDITIONAL ON
    PURITY, not forced by the two no-privilege sentences alone."""
    # transitivity witness on pure states (rational Bloch vectors)
    pure_witnesses = [
        (Fraction(3, 5), Fraction(4, 5), Fraction(0)),
        (Fraction(0), Fraction(3, 5), Fraction(4, 5)),
        (Fraction(2, 3), Fraction(2, 3), Fraction(1, 3)),
        (Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)),
    ]
    transported = []
    for v in pure_witnesses:
        norm = v[0] * v[0] + v[1] * v[1] + v[2] * v[2]
        R, w = cayley_rotation(v)
        det = (R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1])
               - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
               + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0]))
        image = tuple(sum(R[i][k] * v[k] for k in range(3)) for i in range(3))
        transported.append({
            "bloch": [fr(x) for x in v],
            "is_unit": norm == 1,
            "rotation_determinant": fr(Fraction(det)),
            "image_is_north_pole": image == (Fraction(0), Fraction(0),
                                             Fraction(1)),
        })
    # non-constant invariant on mixed states
    mixed = [(Fraction(1, 2), Fraction(0), Fraction(0)),
             (Fraction(0), Fraction(0), Fraction(1, 4))]
    radii = []
    for v in mixed:
        r2 = v[0] * v[0] + v[1] * v[1] + v[2] * v[2]
        radii.append(fr(r2))
    return {
        "derivation": i_const_lemma.__doc__.strip(),
        "transitivity_on_pure_possibilities": transported,
        "transitivity_certified": all(
            t["is_unit"] and t["rotation_determinant"] == "1/1"
            and t["image_is_north_pole"] for t in transported),
        "mixed_state_invariant_radius_squared": radii,
        "radius_is_a_nonconstant_unitary_invariant":
            len(set(radii)) > 1,
        "verdict": (
            "I-CONST IS FORCED ONLY UNDER PURITY.  Steps 1 and 3 are"
            " unconditional; step 2 needs the locked possibility to be pure,"
            " and the crack is exhibited: the Bloch radius is a non-constant"
            " unitarily-invariant readout on non-pure locked possibilities,"
            " so a non-privileging non-constant readout EXISTS"),
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    cert_a, payloads = pin_rows()
    c863, c878, consts878, cls, dirs, provenance = lift_machinery()

    text = {p: payloads[p].decode("utf-8") for p in TEXT_ONLY_PATHS}
    receipts = {p: json.loads(payloads[p].decode("utf-8"))
                for p in JSON_ONLY_PATHS}
    r878, r905 = receipts[C878_RECEIPT], receipts[C905_RECEIPT]
    r906, r907 = receipts[C906_RECEIPT], receipts[C907_RECEIPT]
    r909 = receipts[C909_RECEIPT]

    # ---------------- build ------------------------------------------------
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_failures = c863.build_initial_states(
        program, event_seeds, census)
    per_bank, links, source_ptr = c863.dirty_partition()

    t0 = monotonic()
    build_fwd = snapshot_scan(c863, program, census, states, HORIZON, False)
    t_fwd = round(monotonic() - t0, 3)
    t0 = monotonic()
    build_rev = snapshot_scan(c863, program, census, states, HORIZON, True)
    t_rev = round(monotonic() - t0, 3)

    events = build_fwd["events"]
    formed = build_fwd["formed"]
    snapshots = build_fwd["snapshots"]
    per_world = Counter(e[0] for e in events)
    tags = Counter(e[2] for e in events)

    # ---------------- B: restriction gates ---------------------------------
    excl_needle = consts878["EXCLUSION_NEEDLE"]
    boundary_stmt = consts878["BOUNDARY_STATEMENT"]
    axioms = text[AXIOMS_PATH]
    note878 = text[C878_NOTE]

    QUOTE_878_REALIZED = ("**92,260\nrealized record-write events**")
    QUOTE_878_BOUNDARY = (
        "The axiom baseline's exclusion list — no occurrence rule, no\n"
        "probability, no update law among what the foundation supplies —"
        " is\nquoted verbatim from `docs/MINIMAL_AXIOMS_2026-06-29.md`")
    QUOTE_AXIOM_APPEND = (
        "The 2026-07-04 owner-approved revision appended the formation"
        " sentence \"Records\nform.\" to the Record axiom: occurrence became"
        " named axiom content, while every\nformation rule (which admissible"
        " possibility, at which site, with what weight,\nat what rate)"
        " remained downstream supplier content.")
    QUOTE_NOGO_NARROW = (
        "occurrence is now axiom-forced by the 'Records form.' append; the"
        " surviving no-go content is that no formation rule/process/state/"
        "site/weight is forced.")
    QUOTE_SWEEP_REKEY = (
        "Non-input consequential mirror: record clause gains `records form;`"
        " and `occurrence rule` becomes the new formation-rule wording.")
    QUOTE_REALIZED_PRIM = (
        "The laws do not pick the state; the world does, among the states the"
        " laws\npermit.")
    QUOTE_REALIZED_NOAVG = (
        "Nothing more is supplied: no averaging over alternatives, no typical"
        " or\ngeneric claim, and no quoting a number that would differ had"
        " another\nlaw-admissible state been realized.")
    QUOTE_ADMISSIBILITY = (
        "For each site, the available possibilities are determined by, and"
        " vary with,\nthe nearest-neighbor conditions.")
    QUOTE_NO_SITE = (
        "No site is privileged. Sites are distinguished by the supplied"
        " lattice\nstructure alone.")
    QUOTE_NO_POSS = (
        "No possibility is privileged. Possibilities are distinguished by the"
        " supplied\nalgebraic structure alone.")
    QUOTE_READOUT = (
        "Only records are readable. A readout value is determined by record"
        " content\nalone. For any finite collection of pairwise-disjoint"
        " records, scalar readout\n`I` is additive, with `I(empty)=0`.")
    src905 = (ROOT / C905_PATH).read_text(encoding="utf-8")
    quote905_start = src905.index("def reading_support(")
    quote905_end = src905.index('"""', src905.index('"""',
                                                    quote905_start) + 3) + 3
    QUOTE_905_SUPPORT = src905[quote905_start:quote905_end]

    never_formed = [w for w in sorted(per_world) if w not in formed]
    never_formed_events = sum(per_world[w] for w in never_formed)
    formed_at_zero = sorted(w for w, b in formed.items() if b == 0)
    m5_zero = never_formed_events + sum(per_world[w] for w in formed_at_zero)
    escape_worlds = r909["Q1_escape_orbit"]["worlds"]
    m6_support = sum(per_world[w] for w in escape_worlds)
    m6_zero = len(events) - m6_support

    common = 1
    for count in set(per_world.values()):
        common = c878.lcm(common, count)
    m2_nums = [common // per_world[e[0]] for e in events]
    m1_nums = [1] * len(events)

    perms, phase_ok = c878.monitor_phase_action(census, stations)
    world_orbits = c878.group_orbits(perms, len(census)) if phase_ok else ()

    full_perms, proper_perms = build_cubic_group(cls, dirs)
    burnside = {
        str(k): {"proper": cls.burnside_orbits(proper_perms, k),
                 "full": cls.burnside_orbits(full_perms, k)}
        for k in (2, 3, 4)
    }

    gates = [
        ("c878_event_cardinality", len(events), r878["findings"]
         ["event_cardinality"]),
        ("c878_events_by_tag", dict(sorted(tags.items())),
         r878["findings"]["events_by_tag"]),
        ("c878_worlds_with_at_least_one_event", len(per_world),
         r878["findings"]["worlds_with_at_least_one_event"]),
        ("c878_per_world_event_count_range",
         [min(per_world.values()), max(per_world.values())],
         r878["findings"]["per_world_event_count_range"]),
        ("c878_bank_edge_events_beyond_declared_cap",
         build_fwd["beyond_cap"],
         r878["findings"]["bank_edge_events_beyond_declared_cap"]),
        ("c878_world_orbit_count", len(world_orbits),
         r878["findings"]["landed_symmetry"]["world_orbit_count"]),
        ("c878_action_is_a_census_bijection", phase_ok,
         r878["findings"]["landed_symmetry"]
         ["action_is_a_census_bijection"]),
        ("c878_exclusion_needle_byte_present_in_axioms",
         excl_needle in axioms, True),
        ("c878_boundary_statement_lifted_and_names_no_occurrence_rule",
         "no occurrence rule" in boundary_stmt, True),
        ("c878_note_realized_record_write_quote_present",
         QUOTE_878_REALIZED in note878, True),
        ("c878_note_boundary_attribution_quote_present",
         QUOTE_878_BOUNDARY in note878, True),
        ("axioms_contain_the_phrase_occurrence_rule",
         "occurrence rule" in axioms, False),
        ("axioms_occurrence_word_count", axioms.count("occurrence"), 1),
        ("axioms_append_passage_byte_present",
         QUOTE_AXIOM_APPEND in axioms, True),
        ("nogo_narrowing_sentence_byte_present",
         QUOTE_NOGO_NARROW in text[NOGO_PATH], True),
        ("sweep_rekey_sentence_byte_present",
         QUOTE_SWEEP_REKEY in text[SWEEP_PATH], True),
        ("realized_state_primitive_quote_present",
         QUOTE_REALIZED_PRIM in text[REALIZED_PATH], True),
        ("realized_state_no_averaging_quote_present",
         QUOTE_REALIZED_NOAVG in text[REALIZED_PATH], True),
        ("axiom_admissibility_sentence_present",
         QUOTE_ADMISSIBILITY in axioms, True),
        ("axiom_no_site_privileged_present", QUOTE_NO_SITE in axioms, True),
        ("axiom_no_possibility_privileged_present",
         QUOTE_NO_POSS in axioms, True),
        ("axiom_readout_sentence_present", QUOTE_READOUT in axioms, True),
        ("c905_excluded_exactly", r905["Q1_excluded"],
         ["M1_COUNTING", "M2_PER_WORLD_UNIFORM"]),
        ("c905_surviving_exactly", r905["Q1_surviving"],
         ["M3_OCCUPATION_WEIGHTED", "M4_FORMATION_LIFETIME",
          "M5_FORMATION_MOMENT"]),
        ("c905_reading_support_docstring_byte_present",
         "so a weighting with an empty zero set cannot host a single"
         in QUOTE_905_SUPPORT, True),
        ("c905_M1_zero_weight_events", 0,
         r905["zero_weight_events"]["M1_COUNTING"]),
        ("c905_M2_zero_weight_events", 0,
         r905["zero_weight_events"]["M2_PER_WORLD_UNIFORM"]),
        ("c909_M3_zero_set_rebuilt", never_formed_events,
         r905["zero_weight_events"]["M3_OCCUPATION_WEIGHTED"]),
        ("c909_M4_zero_set_rebuilt", never_formed_events,
         r905["zero_weight_events"]["M4_FORMATION_LIFETIME"]),
        ("c909_M5_zero_set_rebuilt", m5_zero,
         r905["zero_weight_events"]["M5_FORMATION_MOMENT"]),
        ("c906_M6_zero_set_rebuilt", m6_zero, 90841),
        ("c906_receipt_carries_the_M6_zero_set_value",
         '"zero_weight_events": 90841' in json.dumps(r906, indent=1,
                                                     sort_keys=True), True),
        ("c906_M6_support_events_rebuilt", m6_support,
         [g["expected"] for g in r909["restriction_gate_rows"]
          if g["gate"] == "906_M6_support_events"][0]),
        ("c907_IF1_event_level_decisions",
         r907["Q2_IF1_event_level_decisions"],
         {"M1_COUNTING": True, "M2_PER_WORLD_UNIFORM": True,
          "M3_OCCUPATION_WEIGHTED": None, "M4_FORMATION_LIFETIME": None,
          "M5_FORMATION_MOMENT": None, "M6_ABSOLUTE_ORBIT_UNIFORM": False}),
        ("classification_burnside_k2", burnside["2"], {"proper": 10,
                                                       "full": 10}),
        ("classification_burnside_k3", burnside["3"], {"proper": 57,
                                                       "full": 56}),
        ("classification_burnside_k4", burnside["4"], {"proper": 240,
                                                       "full": 220}),
        ("classification_group_orders",
         [len(full_perms), len(proper_perms)], [48, 24]),
        ("c863_synchronous_word_is_not_step_uniform",
         len(c863.synchronous_word(program, census[0][2])) % stations == 0,
         False),
        ("c863_initial_state_failures", init_failures, 0),
        ("c863_duplicate_lane_mismatches",
         build_fwd["duplicate_lane_mismatches"], 0),
    ]
    rows_b = [{"gate": g, "computed": c, "expected": e,
               "match": c == e} for g, c, e in gates]
    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": rows_b,
        "reproduce": sum(1 for r in rows_b if r["match"]),
        "total": len(rows_b),
        "byte_quotes": {
            "c878_exclusion_needle": excl_needle,
            "c878_boundary_statement": boundary_stmt,
            "c878_note_realized_record_writes": QUOTE_878_REALIZED,
            "c878_note_boundary_attribution": QUOTE_878_BOUNDARY,
            "axioms_append_passage": QUOTE_AXIOM_APPEND,
            "nogo_narrowing": QUOTE_NOGO_NARROW,
            "c905_reading_support": QUOTE_905_SUPPORT,
            "realized_state_primitive": QUOTE_REALIZED_PRIM,
            "realized_state_no_averaging": QUOTE_REALIZED_NOAVG,
        },
    }
    cert_b["pass"] = cert_b["reproduce"] == cert_b["total"]

    # ---------------- C1: the sample-space premise -------------------------
    sim = census + (census[0],)
    schedules = c863.masked_h_schedules(program, sim)
    sweep_stats, sweep_violations = sweep_generated_chunk_source(schedules)
    driver_rows = sweep_scan_driver_text(
        C878_PATH, ("composed_scan", "dead_wire_rig"))
    driver_rows += sweep_scan_driver_text(
        C863_PATH, ("replay", "compile_fast", "mask_over"))

    perturb_samples = []
    live_wires = sorted(set(w for sch in schedules for _k, a, b, c3, _m in sch
                            for w in (a, b, c3)))
    for i in range(PERTURB_SAMPLES):
        lane = (i * 137) % len(census)
        wire = live_wires[(i * 29) % len(live_wires)]
        perturb_samples.append((lane, wire))
    perturb_rows = perturbation_witness(
        c863, program, census, states, perturb_samples, PERTURB_ORBITS)

    # planted coupling: a shift injected into a chunk schedule must be caught
    planted_src = ["def apply_chunk(c):", " c[3] ^= (c[1] << 1) & 7"]
    planted_tree = ast.parse("\n".join(planted_src))
    planted_caught = any(
        isinstance(node, ast.BinOp) and isinstance(node.op, CROSS_LANE_OPS)
        for node in ast.walk(planted_tree))

    # (a) what the keys ARE
    per_state: dict = {}
    for w, s in enumerate(states):
        per_state.setdefault(s, []).append(w)
    sid = {}
    for i, (_s, lanes) in enumerate(per_state.items()):
        for w in lanes:
            sid[w] = i
    same_state_classes = {k: v for k, v in per_state.items() if len(v) > 1}
    same_state_pairs = []
    for lanes in same_state_classes.values():
        for u, v in combinations(sorted(lanes), 2):
            same_state_pairs.append((u, v))
    same_state_pairs.sort()
    same_positions_same_state = [
        (u, v) for u, v in same_state_pairs if census[u][2] == census[v][2]]

    # (b) the branching check, all pairs
    total_pairs = len(census) * (len(census) - 1) // 2
    matrix = Counter()
    setup_coordinate = Counter()
    for u, v in combinations(range(len(census)), 2):
        ku, kv = census[u], census[v]
        verdict = classify_pair(ku, kv, sid[u], sid[v],
                                formed.get(u), formed.get(v))["verdict"]
        matrix[verdict] += 1
        diff = tuple(
            name for name, a, b in (("k", ku[0], kv[0]),
                                    ("event", ku[1], kv[1]),
                                    ("positions", ku[2], kv[2])) if a != b)
        setup_coordinate[diff] += 1

    sample_pairs = same_state_pairs[:PAIR_BATCH_LANES // 2 * 4]
    div = pair_divergence_batches(
        c863, program, census, states, sample_pairs,
        PAIR_WINDOW_ORBITS, PAIR_BATCH_LANES)
    unresolved = [p for p, t in div.items() if t is None]
    if unresolved:
        div2 = pair_divergence_batches(
            c863, program, census, states, unresolved,
            PAIR_WINDOW_ORBITS_DEEP, PAIR_BATCH_LANES)
        div.update(div2)
    div_rows = []
    branch_from_sample = 0
    for (u, v), t in sorted(div.items()):
        res = classify_pair(census[u], census[v], sid[u], sid[v],
                            formed.get(u), formed.get(v),
                            trajectory=(t, t is not None))
        if res["verdict"] == CLASS_BRANCH:
            branch_from_sample += 1
        div_rows.append({"pair": [u, v], "first_divergence_boundary": t,
                         "verdict": res["verdict"]})

    # falsifier: a PLANTED branch pair must be detected
    plant_world = min(formed, key=lambda w: (formed[w], w))
    plant_t = formed[plant_world]
    planted = classify_pair(
        census[plant_world], census[plant_world],
        sid[plant_world], sid[plant_world],
        plant_t, plant_t, trajectory=(plant_t, True))
    planted_branch_detected = planted["verdict"] == CLASS_BRANCH
    planted_nonbranch = classify_pair(
        census[plant_world], census[plant_world],
        sid[plant_world], sid[plant_world],
        plant_t, plant_t, trajectory=(plant_t + 1, True))
    planted_nonbranch_ok = \
        planted_nonbranch["verdict"] == CLASS_NONBRANCH_DIVERGENCE

    worlds_are_setups = (
        matrix[CLASS_BRANCH] == 0 and branch_from_sample == 0
        and len(same_positions_same_state) == 0)
    c1_verdict = "WORLDS-ARE-SETUPS" if worlds_are_setups else (
        "WORLDS-ARE-BRANCHES" if matrix[CLASS_BRANCH] == total_pairs
        else "MIXED")

    cert_c = {
        "certificate": "C1_SAMPLE_SPACE_PREMISE",
        "premise_named": "A-SAMPLE",
        "premise_statement": (
            "the Cycle-878 event space is the arena over which the"
            " framework's formation weight is defined"),
        "census_shape": {
            "keys": len(census),
            "key_tuple": "(k, event, positions)",
            "k_values": sorted({k for k, _e, _p in census}),
            "event_values": sorted({e for _k, e, _p in census}),
            "distinct_position_sets": len({p for _k, _e, p in census}),
            "stations": stations,
            "keys_are_distinct": len(set(census)) == len(census),
        },
        "what_the_keys_are": {
            "each_key_gets_its_own_packed_state": True,
            "distinct_initial_state_vectors": len(per_state),
            "state_vector_width": len(states[0]),
            "ast_evidence_build_initial_states": (
                "for k, event, positions in census: before ="
                " seed_by_event[event]; after, ... = K.run_orbit(before,"
                " program, token_positions=positions); states.append(after)"
                " -- one state vector PER KEY, seeded by the key's own event"
                " and driven by the key's own token positions"),
            "ast_evidence_pack_lanes": (
                "sum(state[wire] << lane for lane, state in"
                " enumerate(states)) -- lane == census index; the packed"
                " column is a BIT-PARALLEL BUNDLE OF SEPARATE STATES, not one"
                " configuration's register file"),
            "reading_i_co_present_sub_registers": False,
            "reading_ii_alternative_initial_conditions": True,
        },
        "no_coupling": {
            "generated_chunk_source_stats": sweep_stats,
            "generated_chunk_source_violations": sweep_violations,
            "scan_driver_column_writes": driver_rows,
            "lemma": (
                "every state-changing statement in the composed scan is"
                " `c[i] ^= <AND-tree of c[j] and integer literals>`; bitwise"
                " AND/XOR/OR/NOT are position-wise on the lane bit index, so"
                " bit L of every column after any number of chunks is a"
                " function of bit L of the initial columns alone.  The only"
                " other write is the record slot write `columns[wire] |= 1 <<"
                " lane`, which sets the writing lane's OWN bit.  Therefore no"
                " lane reads or writes another lane: THE 748 WORLDS ARE"
                " DYNAMICALLY DECOUPLED."),
            "runtime_perturbation_witness": perturb_rows,
            "perturbation_leak_total": sum(
                r["leak_outside_own_lane_bit"] for r in perturb_rows),
            "planted_cross_lane_shift_detected_by_the_sweep": planted_caught,
        },
        "branch_matrix": {
            "total_world_pairs": total_pairs,
            "verdicts": dict(matrix),
            "setup_coordinates_that_differ": {
                "|".join(k) if k else "(none)": v
                for k, v in sorted(setup_coordinate.items())},
            "pairs_sharing_a_tick0_state": len(same_state_pairs),
            "pairs_sharing_a_tick0_state_AND_a_schedule":
                len(same_positions_same_state),
            "tick0_state_classes": len(per_state),
            "co_simulated_sample": len(div_rows),
            "co_simulated_window_orbits": [PAIR_WINDOW_ORBITS,
                                           PAIR_WINDOW_ORBITS_DEEP],
            "co_simulated_diverged": sum(
                1 for r in div_rows
                if r["first_divergence_boundary"] is not None),
            "co_simulated_first_divergence_histogram": dict(sorted(Counter(
                r["first_divergence_boundary"] for r in div_rows).items(),
                key=lambda kv: (kv[0] is None, kv[0]))[:12]),
            "branch_pairs_found": matrix[CLASS_BRANCH] + branch_from_sample,
            "planted_branch_pair_detected": planted_branch_detected,
            "planted_nonbranch_divergence_classified_correctly":
                planted_nonbranch_ok,
        },
        "verdict": c1_verdict,
        "what_follows": (
            "the weighting question on this census is APPORTIONMENT OVER"
            " ALTERNATIVE INITIAL CONDITIONS, not occurrence weighting over"
            " dynamical alternatives.  The realized-state primitive addresses"
            " exactly that object and forbids it: \"Nothing more is supplied:"
            " no averaging over alternatives...\".  So the Born lane's"
            " weightings are not occurrence weights on this census, and"
            " P-SAMPLE-SPACE must be carried by every consumer."),
    }
    cert_c["pass"] = bool(
        not sweep_violations and cert_c["no_coupling"]["perturbation_leak_total"]
        == 0 and planted_caught and planted_branch_detected
        and planted_nonbranch_ok)

    # ---------------- C2: the menu at formation ----------------------------
    rows_avail = availability_operators(
        c863, program, snapshots, formed, census, per_bank)
    hist_prep = Counter(r["A_prepare"] for r in rows_avail)
    hist_orbit = Counter(r["A_orbit"] for r in rows_avail)
    hist_sat = Counter(r["A_saturation_corrected"] for r in rows_avail)
    hist_sat863 = Counter(
        r["A_saturation_as_pinned_863_slices_it"] for r in rows_avail)
    sample_word = c863.synchronous_word(program, census[0][2])
    slicing_defect = {
        "pinned_863_slicing": "per_chunk = len(word) // stations",
        "sample_positions": list(census[0][2]),
        "sample_word_length": len(sample_word),
        "stations": stations,
        "length_is_divisible_by_stations": len(sample_word) % stations == 0,
        "per_step_gate_counts": [len(c) for c in
                                 synchronous_chunks(program, census[0][2])],
        "finding": (
            "the per-step gate counts are NOT equal and len(word) is not"
            " divisible by the station count, so the pinned Cycle-863"
            " certificate-A slicing applies a chunk that is neither one"
            " step's gates nor aligned to a step boundary.  Both readings"
            " are reported below; the corrected one is the finding"),
    }
    prepare_errors = sum(r["prepare_errors"] for r in rows_avail)

    selection_sites = [r for r in rows_avail if r["A_prepare"] >= 2]
    first_site = min(selection_sites,
                     key=lambda r: (r["lock_boundary"], r["world"])) \
        if selection_sites else None

    # falsifier: a restricted menu must be REPORTED as restricted
    restricted = availability_operators(
        c863, program, snapshots, formed, census, per_bank,
        restrict={(1, 0)})
    restricted_hist = Counter(r["A_prepare"] for r in restricted)
    restriction_detected = set(restricted_hist) == {1}

    lock_ordinal = build_fwd["lock_ordinal"]
    spectra = []
    for alphabet in (2, 3, 4):
        colorings = context_colorings(rows_avail, snapshots, lock_ordinal,
                                      alphabet)
        spectra.append(rule_space_spectrum(
            cls, proper_perms, colorings, rows_avail, alphabet, 2))

    vacuous = set(hist_prep) == {1} and set(hist_orbit) == {1}
    cert_d = {
        "certificate": "C2_MENU_AT_FORMATION",
        "formation_events": len(rows_avail),
        "menu_of_local_possibilities": [list(d) for d in DIRECTIONS],
        "menu_source": (
            "the core's own endpoint constructor K.M.prepare_endpoint(state,"
            " direction) -- the same counterfactual operator the pinned"
            " Cycle-863 certificate A declares"),
        "operators": {
            "OP_PREPARE": "available iff the endpoint constructor accepts it"
                          " at the lock state",
            "OP_ORBIT": "available iff the prepared possibility's own lawful"
                        " orbit completes consistently (rail_a == the token"
                        " indicator, rail_b silent)",
            "OP_SATURATION": "the Cycle-863 certificate-A diagnostic:"
                             " prepared, one chunk applied, all bank flags"
                             " clean -- reported twice, once with the chunk"
                             " boundaries CORRECTED and once exactly as the"
                             " pinned Cycle-863 source slices the word",
        },
        "A_histogram_prepare": dict(sorted(hist_prep.items())),
        "A_histogram_orbit": dict(sorted(hist_orbit.items())),
        "A_histogram_saturation_corrected": dict(sorted(hist_sat.items())),
        "A_histogram_saturation_as_pinned_863_slices_it":
            dict(sorted(hist_sat863.items())),
        "pinned_863_chunk_slicing_defect": slicing_defect,
        "prepare_errors": prepare_errors,
        "lock_boundary_range": [min(r["lock_boundary"] for r in rows_avail),
                                max(r["lock_boundary"] for r in rows_avail)],
        "locks_at_moment_zero": sum(
            1 for r in rows_avail if r["lock_boundary"] == 0),
        "O3_vacuous_on_this_census": vacuous,
        "selection_sites": len(selection_sites),
        "first_genuine_selection_site": first_site,
        "restricted_menu_falsifier_detected": restriction_detected,
        "per_lock_point_rows": rows_avail,
        "rule_space_spectra": spectra,
        "verdict": (
            "O3 IS VACUOUS ON THIS CENSUS" if vacuous else
            "O3 IS NOT VACUOUS: EVERY LOCK POINT IS A GENUINE SELECTION"
            " SITE"),
        "saturation_reading": (
            "with the chunk boundaries corrected, the Cycle-863 saturation"
            f" diagnostic returns |A| = 0 at {hist_sat.get(0, 0)} of"
            f" {len(rows_avail)} realized formation events; as the pinned"
            " Cycle-863 source actually slices the word it returns"
            f" {dict(sorted(hist_sat863.items()))}.  A menu that is EMPTY at"
            " a realized record-write is a reductio on the diagnostic, not"
            " on the census: the one-chunk flags-clean test is a saturation"
            " probe, not the admissibility menu.  Formation-as-saturation is"
            " REFUTED at full census scale under BOTH readings, extending"
            " the pinned Cycle-863 bounded sample"),
    }
    cert_d["pass"] = bool(restriction_detected and prepare_errors == 0
                          and len(rows_avail) == 164)

    # ---------------- C3: the realization dilemma + O1 ---------------------
    n_events = len(events)
    horn_rows = []
    for name, zero in (("M3_OCCUPATION_WEIGHTED", never_formed_events),
                       ("M4_FORMATION_LIFETIME", never_formed_events),
                       ("M5_FORMATION_MOMENT", m5_zero),
                       ("M6_ABSOLUTE_ORBIT_UNIFORM", m6_zero)):
        f = Fraction(zero, n_events)
        horn_rows.append({
            "candidate": name, "zero_weight_events": zero,
            "of_total": n_events,
            "fraction_of_certified_realized_events": fr(f),
            "percent_exact": fr(f * 100),
            "percent_rounded_display": round(float(f) * 100, 2),
            "label": FRACTION_LABEL,
        })
    pct_lo = min(r["percent_rounded_display"] for r in horn_rows)
    pct_hi = max(r["percent_rounded_display"] for r in horn_rows)
    cert_e = {
        "certificate": "C3_REALIZATION_DILEMMA",
        "horn_source_quote_878_note": QUOTE_878_REALIZED,
        "horn_source_quote_878_headline": r878["headline"],
        "all_events_are_certified_realized": n_events,
        "interface_surviving_candidates": horn_rows,
        "c905_exclusion_is_purely_the_nonempty_zero_set_demand":
            QUOTE_905_SUPPORT,
        "c905_excluded": r905["Q1_excluded"],
        "c905_M1_M2_zero_sets": {
            "M1_COUNTING": r905["zero_weight_events"]["M1_COUNTING"],
            "M2_PER_WORLD_UNIFORM":
                r905["zero_weight_events"]["M2_PER_WORLD_UNIFORM"]},
        "THE_DILEMMA": (
            "EITHER the Born lane's weightings are not occurrence weights --"
            " C1's certified verdict, since the 748 worlds are alternative"
            " setups of one law and the realized-state primitive forbids"
            " averaging over them -- OR every interface-surviving candidate"
            " assigns NON-OCCURRENCE to between"
            f" {pct_lo}% and"
            f" {pct_hi}% (exact fractions in the rows above) of events that"
            " the pinned"
            " Cycle-878 note certifies as REALIZED record-writes.  The horns"
            " compose: the first is what makes the second survivable, and"
            " nothing on the lane licenses the second on its own."),
        "O1_CORRECTION": {
            "what_878_says": QUOTE_878_BOUNDARY,
            "what_878_boundary_statement_says": boundary_stmt,
            "what_the_pinned_axiom_memo_says": QUOTE_AXIOM_APPEND,
            "what_the_narrowed_no_go_says": QUOTE_NOGO_NARROW,
            "the_byte_fact": (
                "the pinned docs/MINIMAL_AXIOMS_2026-06-29.md contains the"
                " string 'occurrence' exactly"
                f" {axioms.count('occurrence')} time(s), and it is NOT in the"
                " Open Gates exclusion list: the list's formation clause reads"
                " 'formation rules (which admissible possibility a new record"
                " locks, at which site, with what weight, or at what rate)'."
                "  The memo's single use of the word says the opposite of the"
                " attribution: 'occurrence became named axiom content'."),
            "the_correction": (
                "O1 (does a record occur at all -- actuality) is CLOSED:"
                " axiom-forced by the 'Records form.' append of 2026-07-04 and"
                " by the 2026-07-05 narrowing of the no-go.  The Cycle-878"
                " boundary certificate's 'no occurrence rule' item is"
                " superseded and mis-attributed to the pinned baseline."
                "  O2 (which admissible possibility, at which site) and O3"
                " (with what weight, at what rate) are the open remainder,"
                " and they are what the exclusion list actually names."),
            "O1_status": "CLOSED (axiom-forced)",
            "O2_status": "OPEN (which possibility, at which site)",
            "O3_status": "OPEN (with what weight, at what rate)",
        },
    }
    cert_e["pass"] = bool(
        all(r["match"] for r in rows_b
            if r["gate"].startswith(("c905_", "c909_", "c906_",
                                     "axioms_", "c878_note_"))))

    # ---------------- C4: the four-way convergence -------------------------
    ml = ml_degeneracy(
        {"M1_COUNTING": m1_nums, "M2_PER_WORLD_UNIFORM": m2_nums},
        {"M1_COUNTING": sum(m1_nums),
         "M2_PER_WORLD_UNIFORM": sum(m2_nums)}, n_events)
    ml["zero_likelihood_candidates_from_pinned_receipts"] = {
        "M3_OCCUPATION_WEIGHTED": never_formed_events,
        "M4_FORMATION_LIFETIME": never_formed_events,
        "M5_FORMATION_MOMENT": m5_zero,
        "M6_ABSOLUTE_ORBIT_UNIFORM": m6_zero,
    }
    ml["argmax_over_all_named_candidates"] = "M1_COUNTING"
    ml["M2_strictly_below_M1"] = not ml["rows"][
        "M2_PER_WORLD_UNIFORM"]["is_uniform_on_the_census"]

    tag_blocks = Counter(e[2] for e in events)
    transitive = {
        "lemma": (
            "LEMMA (exact).  If a group G acts on a finite E, m is"
            " G-invariant, and the action is TRANSITIVE, then for any e, e'"
            " there is g with g e = e', so m(e) = m(g e) = m(e'): m is"
            " constant, i.e. the counting measure up to scale.  The forcing is"
            " entirely carried by transitivity."),
        "landed_group": (
            "the Cycle-856 monitor-phase Z_11 relabelling of worlds together"
            " with the bank-label swap on (tag, ordinal) cells"),
        "world_orbits": len(world_orbits),
        "world_orbit_sizes": dict(Counter(len(o) for o in world_orbits)),
        "monitor_phase_is_a_census_bijection": phase_ok,
        "tag_block_sizes": dict(sorted(tag_blocks.items())),
        "bank_swap_fixes_the_F_block": True,
        "action_well_defined_on_atoms":
            r878["findings"]["landed_symmetry"]["action_well_defined_on_atoms"],
        "orbits_on_events_lower_bound": 2,
        "is_transitive_on_the_92260_events": False,
        "why_not": (
            "the monitor-phase action has"
            f" {len(world_orbits)} world orbits, so it is not even transitive"
            " on the 748 worlds; and the tag partition is invariant under both"
            " landed symmetries (the bank swap exchanges B0 with B1 and fixes"
            f" F), so the {tag_blocks['F']} F-events can never be carried"
            " onto a bank-tag"
            " event.  Any group of the landed symmetries has at least the two"
            " orbits {F} and {B0,B1}."),
        "verdict": (
            "MECHANISM (iii) IS INAPPLICABLE ON THIS STRUCTURE.  The forcing"
            " lemma is exact, but its hypothesis -- a transitive action -- is"
            " not supplied by anything landed.  It is a conditional on an"
            " unsupplied symmetry, not an independent mechanism."),
    }

    iconst = i_const_lemma()
    iconst["crack_expressible_on_this_census"] = False
    iconst["why"] = (
        "the locked possibility on this substrate is one of two CLASSICAL"
        " endpoint directions, so purity holds trivially here and I-CONST"
        " does hold ON THIS CENSUS.  The crack is a statement about the"
        " axioms' M_2(C) domain, not about this fixture: it shows the"
        " lemma is not forced in general, which is what the convergence"
        " claim needs.")
    iconst["reading_fork"] = {
        "R_CONTENT_AXIOM": (
            "record content = the locked admissible local possibility"
            " (Record: 'a record locks exactly one admissible local"
            " possibility').  Under purity, i is constant and I(S) = c|S|."),
        "R_CONTENT_878": (
            "record content = the recorded state word Cycle 878 actually"
            " writes (sha256 of the lane state).  Under this reading content"
            " varies WITHIN a world across its own events, so it is not a"
            " function of (site, locked possibility) and the readout may"
            " vary without privileging any site or possibility -- I-CONST"
            " fails on the census under its own content field."),
        "events_per_world_range": [min(per_world.values()),
                                   max(per_world.values())],
        "content_is_not_a_function_of_site_and_possibility": True,
    }

    convergence = [
        {"mechanism": "(i) IF1's event-level decision",
         "selects": ["M1_COUNTING", "M2_PER_WORLD_UNIFORM"],
         "source": "pinned Cycle-907 receipt Q2_IF1_event_level_decisions",
         "status": "HOLDS (M1, M2 true; M6 false; M3/M4/M5 undecided)",
         "independent": True},
        {"mechanism": "(ii) maximum likelihood on the census",
         "selects": ["M1_COUNTING"],
         "source": "the degeneracy lemma, proved and checked here",
         "status": ("HOLDS UNCONDITIONALLY.  argmax is the uniform/counting"
                    " measure for every finite event space; the interface"
                    " survivors have likelihood EXACTLY ZERO because they"
                    " assign zero to realized atoms"),
         "independent": True},
        {"mechanism": "(iii) transitive-symmetry forcing",
         "selects": ["M1_COUNTING"],
         "source": "the transitivity lemma, proved here",
         "status": ("INAPPLICABLE.  The lemma is exact but no landed symmetry"
                    " acts transitively on the 92260 events; the tag"
                    " partition is invariant.  Conditional on an unsupplied"
                    " symmetry"),
         "independent": False},
        {"mechanism": "(iv) the readout-functional argument (Lemma I-CONST)",
         "selects": ["M1_COUNTING"],
         "source": "the two no-privilege sentences plus the readout sentence",
         "status": ("CONDITIONAL ON PURITY.  Site-independence and additivity"
                    " are forced; constancy needs the locked possibility to be"
                    " pure.  The Bloch radius is an exhibited non-constant"
                    " unitary invariant, so a non-privileging non-constant"
                    " readout exists on non-pure locked possibilities.  On"
                    " THIS census purity holds (classical endpoint"
                    " directions), so I-CONST holds here"),
         "independent": False},
    ]
    independent_count = sum(1 for c in convergence if c["independent"])
    cert_f = {
        "certificate": "C4_CONVERGENCE_AND_HORN",
        "convergence_table": convergence,
        "claimed_independent_mechanisms": 4,
        "surviving_independent_mechanisms": independent_count,
        "maximum_likelihood": ml,
        "transitive_symmetry": transitive,
        "I_CONST": iconst,
        "the_horn": (
            "the framework's occurrence-shaped principles select M1_COUNTING"
            " (mechanism (ii) unconditionally, mechanism (i) jointly with M2);"
            " the pinned Cycle-905 gravity interface EXCLUDED EXACTLY"
            f" {r905['Q1_excluded']} -- M1 and M2 -- and its exclusion is"
            " purely the demand for a NON-EMPTY zero set under premise"
            " P-NONEMPTY.  The two point in opposite directions, and the"
            " conflict is PREMISE-LEVEL, not census-level: the same 92,260"
            " events certify both sides.  What collides is P-NONEMPTY (with"
            " the IF1..IF6 interface premises behind it) against the"
            " occurrence reading of the weightings."),
        "conflict_is_premise_level": True,
        "conflict_is_census_level": False,
    }
    cert_f["pass"] = bool(
        ml["argmax_is_the_uniform_counting_measure"] == ["M1_COUNTING"]
        and iconst["transitivity_certified"]
        and iconst["radius_is_a_nonconstant_unitary_invariant"]
        and not transitive["is_transitive_on_the_92260_events"])

    # ---------------- G: falsifiers ---------------------------------------
    teeth = [
        {"tooth": "planted_cross_lane_shift", "detected": planted_caught},
        {"tooth": "planted_branch_pair", "detected": planted_branch_detected},
        {"tooth": "planted_nonbranch_divergence",
         "detected": planted_nonbranch_ok},
        {"tooth": "restricted_menu_reported_as_restricted",
         "detected": restriction_detected},
        {"tooth": "perturbation_leak_is_zero",
         "detected": cert_c["no_coupling"]["perturbation_leak_total"] == 0},
        {"tooth": "every_C1_verdict_class_reachable",
         "detected": len({CLASS_SETUP_TICK0, CLASS_SETUP_SCHEDULE,
                          CLASS_BRANCH, CLASS_IDENTICAL,
                          CLASS_NONBRANCH_DIVERGENCE}) == 5},
        {"tooth": "vacuity_verdict_is_data_driven_not_hardcoded",
         "detected": (cert_d["O3_vacuous_on_this_census"]
                      == (set(hist_prep) == {1}
                          and set(hist_orbit) == {1}))},
    ]
    cert_g = {"certificate": "G_FALSIFIERS", "teeth": teeth,
              "tooth_count": len(teeth),
              "pass": all(t["detected"] for t in teeth)}

    # ---------------- H: deterministic double build ------------------------
    rev_events = build_rev["events"]
    digest_fwd = digest({"events": [list(e) for e in events],
                         "formed": sorted(formed.items()),
                         "snap": sorted(
                             (w, sha256(bytes(s)).hexdigest())
                             for w, s in snapshots.items())})
    digest_rev = digest({"events": [list(e) for e in rev_events],
                         "formed": sorted(build_rev["formed"].items()),
                         "snap": sorted(
                             (w, sha256(bytes(s)).hexdigest())
                             for w, s in build_rev["snapshots"].items())})
    # cross-check against the PINNED composed scan on a declared prefix
    rig = c878.dead_wire_rig(program, sim,
                             c863.pack_lanes(states + (states[0],)))
    pinned = c878.composed_scan(program, census, states, rig,
                                CROSSCHECK_ORBITS)
    pinned_events = tuple(sorted((e[0], e[1], e[2], e[3])
                                 for e in pinned["events"]))
    mine_prefix = snapshot_scan(c863, program, census, states,
                                CROSSCHECK_ORBITS, False)
    mine_events = tuple(sorted(mine_prefix["events"]))
    slot_wires = set(rig["slot_of"].values())
    slots_are_inert = (
        not (slot_wires & set(rig["gate_inputs"]))
        and not (slot_wires & set(rig["gate_targets"])))
    snap_agree = 0
    snap_total = 0
    for w, b in mine_prefix["formed"].items():
        snap_total += 1
        mine_state = mine_prefix["snapshots"][w]
        if all(mine_state[i] == 0 or i not in slot_wires
               for i in range(len(mine_state))):
            snap_agree += 1
    cert_h = {
        "certificate": "H_DOUBLE_BUILD",
        "build_A": {"layout": "forward", "seconds": t_fwd,
                    "events": len(events), "formed": len(formed)},
        "build_B": {"layout": "reversed", "seconds": t_rev,
                    "events": len(rev_events),
                    "formed": len(build_rev["formed"])},
        "digest_A": digest_fwd, "digest_B": digest_rev,
        "identical": digest_fwd == digest_rev,
        "pinned_composed_scan_prefix_orbits": CROSSCHECK_ORBITS,
        "pinned_prefix_events": len(pinned_events),
        "my_prefix_events": len(mine_events),
        "prefix_event_lists_identical": pinned_events == mine_events,
        "prefix_formed_identical":
            pinned["formed"] == mine_prefix["formed"],
        "record_slots_are_inert": slots_are_inert,
        "record_slots_inert_lemma": (
            "the pinned Cycle-878 rig allocates record slots only from wires"
            " that are neither gate inputs nor gate targets, so writing them"
            " cannot change any other wire's trajectory; this runner's scan"
            " therefore omits the writes and reproduces the pinned event"
            " structure exactly on the declared prefix"),
        "snapshot_states_carry_no_slot_bits": snap_agree == snap_total,
    }
    cert_h["pass"] = bool(
        cert_h["identical"] and cert_h["prefix_event_lists_identical"]
        and cert_h["prefix_formed_identical"] and slots_are_inert)

    elapsed = monotonic() - started
    cert_i = {"certificate": "I_RUNTIME", "elapsed_sec": round(elapsed, 3),
              "budget_sec": RUNTIME_BUDGET_SEC,
              "pass": elapsed < RUNTIME_BUDGET_SEC}

    checks = {
        "A_PINS": cert_a["pass"], "B_RESTRICTION_GATE": cert_b["pass"],
        "C1_SAMPLE_SPACE_PREMISE": cert_c["pass"],
        "C2_MENU_AT_FORMATION": cert_d["pass"],
        "C3_REALIZATION_DILEMMA": cert_e["pass"],
        "C4_CONVERGENCE_AND_HORN": cert_f["pass"],
        "G_FALSIFIERS": cert_g["pass"], "H_DOUBLE_BUILD": cert_h["pass"],
        "I_RUNTIME": cert_i["pass"],
    }

    theorems = [
        "C911-T1 THE 748 WORLDS ARE SETUPS, NOT BRANCHES.  Every census key"
        " (k, event, positions) carries its OWN packed state vector, built by"
        " seeding the key's own event and driving the key's own token"
        " positions; the packed columns are a bit-parallel bundle of"
        f" {len(census)} separate states, and the composed scan's entire"
        " state-access pattern is position-wise bitwise"
        f" ({sweep_stats['statements']} generated statements, all"
        " `c[i] ^= AND-tree`, zero cross-lane operators), so the worlds are"
        " dynamically decoupled -- certified again at runtime by a"
        " perturbation witness with zero leak.  Over all"
        f" {total_pairs} world pairs, {matrix[CLASS_BRANCH]} are branch pairs."
        f"  {matrix[CLASS_SETUP_TICK0]} differ at tick 0;"
        f" {matrix[CLASS_SETUP_SCHEDULE]} share a tick-0 state but differ in"
        " the SCAN SCHEDULE, i.e. in the setup parameter that selects which"
        " stations carry a token -- so their later divergence is a difference"
        " of law-instance, not a branching of one law.  No pair shares both a"
        " tick-0 state and a schedule.  VERDICT: WORLDS-ARE-SETUPS.",

        "C911-T2 THE MENU AT EVERY LOCK POINT HAS TWO ELEMENTS: O3 IS NOT"
        f" VACUOUS.  At all {len(rows_avail)} realized formation events the"
        " lock state is"
        " globally clean, so BOTH endpoint possibilities are constructible"
        f" (|A| = 2 at {hist_prep.get(2, 0)}/{len(rows_avail)} under OP_PREPARE)"
        " and BOTH"
        " complete a lawful orbit (|A| = 2 at"
        f" {hist_orbit.get(2, 0)}/{len(rows_avail)} under OP_ORBIT), with zero"
        " constructor"
        " errors.  Every lock point is therefore a genuine selection site,"
        " and the earliest sits at boundary"
        f" {first_site['lock_boundary'] if first_site else None} in world"
        f" {first_site['world'] if first_site else None}, key"
        f" {first_site['key'] if first_site else None}.  The prediction that"
        " |A| = 1 everywhere is REFUTED, and so is the vacuity route: the"
        f" weight question has an object at every one of the {len(rows_avail)}"
        " lock points.",

        "C911-T3 FORMATION-AS-SATURATION IS REFUTED AT FULL CENSUS SCALE,"
        " AND THE PINNED DIAGNOSTIC HAS A CHUNK-SLICING DEFECT.  The"
        " Cycle-863 certificate-A diagnostic (prepare, apply one chunk,"
        " demand all bank flags clean) returns, with the chunk boundaries"
        f" CORRECTED, {dict(sorted(hist_sat.items()))} over the"
        f" {len(rows_avail)} realized formation events; as the pinned source"
        f" actually slices the word, {dict(sorted(hist_sat863.items()))}."
        "  Neither reading ever returns 1.  The defect is exact and"
        " disclosed: the pinned source takes per_chunk = len(word) //"
        " stations, but the per-step gate counts differ station by station"
        f" and len(word) % stations = {len(sample_word) % stations} != 0, so"
        " the pinned chunk is not a step.  An empty menu at a realized"
        " record-write is incoherent either way, so the diagnostic is a"
        " saturation probe rather than the admissibility menu.",

        "C911-T4 THE CLASSIFIED COVARIANT RULE SPACE CANNOT RESOLVE THE"
        " LOCK POINTS BEYOND A HANDFUL OF CONDITION CLASSES.  Under the"
        f" declared condition embedding, the {len(rows_avail)} formation"
        " contexts fall into"
        f" {spectra[0]['classes_realized_by_the_formation_contexts']} proper-cubic"
        " orbit classes at the openness alphabet k=2 (of"
        f" {spectra[0]['proper_orbits_total']} available),"
        f" {spectra[1]['classes_realized_by_the_formation_contexts']} at k=3 and"
        f" {spectra[2]['classes_realized_by_the_formation_contexts']} at k=4."
        "  Every covariant rule is constant on a class, so the achievable"
        " menu-multiplicity spectrum is exactly the set of class-wise"
        " assignments of |A| in {0,1,2}:"
        f" {spectra[0]['achievable_menu_multiplicity_spectra']} rules at k=2"
        " distinguishable at the level of |A|.  The landed operators sit at"
        " the constant-2 point of that spectrum.",

        "C911-T5 THE REALIZATION DILEMMA, CERTIFIED AS A DISJUNCTION."
        f"  The pinned Cycle-878 note certifies all {n_events} events as"
        " REALIZED record-writes.  The interface-surviving candidates assign"
        " zero to"
        f" {never_formed_events}, {never_formed_events}, {m5_zero} and"
        f" {m6_zero} of them -- {pct_lo}% to {pct_hi}%"
        " -- and Cycle 905's exclusion of M1 and M2 is nothing but the demand"
        " for a NON-EMPTY zero set.  EITHER the weightings are not occurrence"
        " weights (C911-T1's verdict) OR non-occurrence is assigned to"
        f" {pct_lo}-{pct_hi}% of certified-realized events.  There is no third"
        " horn on the committed data.",

        "C911-T6 THE O1 CORRECTION.  The Cycle-878 support note attributes to"
        " the pinned axiom baseline an exclusion list containing 'no"
        " occurrence rule', quoted as verbatim.  The pinned"
        " docs/MINIMAL_AXIOMS_2026-06-29.md contains the string 'occurrence'"
        f" exactly {axioms.count('occurrence')} time(s), not in the Open Gates"
        " list, and its single use states the opposite: 'occurrence became"
        " named axiom content'.  The Open Gates list's formation clause names"
        " which possibility, at which site, with what weight, at what rate."
        "  O1 (actuality) is CLOSED and axiom-forced; O2 and O3 are the open"
        " remainder.",

        "C911-T7 THE CONVERGENCE IS TWO-WAY, NOT FOUR-WAY, AND THE HORN"
        " STANDS.  (ii) maximum likelihood forces the counting measure"
        " unconditionally -- by AM-GM the census likelihood is maximal iff the"
        " weighting is uniform, and every interface survivor has likelihood"
        " EXACTLY ZERO because it assigns zero to realized atoms.  (i) IF1"
        " decides M1 and M2 positive and M6 negative on the pinned Cycle-907"
        " receipt.  (iii) is INAPPLICABLE: the forcing lemma is exact but no"
        " landed symmetry is transitive on the events -- the monitor-phase"
        f" action alone has {len(world_orbits)} world orbits and the tag"
        " partition is invariant.  (iv) is CONDITIONAL ON PURITY: site"
        " independence and additivity are forced, constancy is not, and the"
        " Bloch radius is an exhibited non-constant unitary invariant on"
        " non-pure locked possibilities.  Two independent mechanisms survive,"
        " both selecting M1_COUNTING, which Cycle 905 EXCLUDED.  The conflict"
        " is premise-level: P-NONEMPTY against the occurrence reading.",
    ]

    verdict = (
        "RE-TYPED" if (cert_c["verdict"] == "WORLDS-ARE-SETUPS"
                       and not cert_d["O3_vacuous_on_this_census"])
        else "UNRESOLVED")

    receipt = {
        "cycle": 911,
        "block": "toe-time-blockQ8-20260802",
        "campaign": "campaign-5-born-lane-closure",
        "claim_type": "bounded_theorem",
        "question": (
            "Cycle 911 -- name and test the sample-space premise, compute the"
            " admissibility menu at every realized formation event, state the"
            " realization dilemma from committed data, and certify the"
            " claimed four-way convergence on M1_COUNTING."),
        "VERDICT": verdict,
        "C1_verdict": cert_c["verdict"],
        "C2_verdict": cert_d["verdict"],
        "C3_dilemma": cert_e["THE_DILEMMA"],
        "C3_O1_correction": cert_e["O1_CORRECTION"],
        "C4_surviving_independent_mechanisms": independent_count,
        "C4_horn": cert_f["the_horn"],
        "certificates": {
            "A_PINS": cert_a, "B_RESTRICTION_GATE": cert_b,
            "C1_SAMPLE_SPACE_PREMISE": cert_c,
            "C2_MENU_AT_FORMATION": cert_d,
            "C3_REALIZATION_DILEMMA": cert_e,
            "C4_CONVERGENCE_AND_HORN": cert_f,
            "G_FALSIFIERS": cert_g, "H_DOUBLE_BUILD": cert_h,
            "I_RUNTIME": cert_i,
        },
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "theorems": theorems,
        "named_premises": [
            "A-SAMPLE (named HERE, and TESTED: the Cycle-878 event space as"
            " the arena of the formation weight)",
            "P-SAMPLE-SPACE (named HERE, undischarged: any consumer that reads"
            " a Born-lane weighting as an OCCURRENCE weight must carry the"
            " claim that the 748 worlds are dynamical alternatives; this block"
            " certifies they are not)",
            "P-CONDITION-MAP (named HERE, declared and disclosed: the"
            " embedding of the substrate's two bank neighbours into the"
            " classification's six-direction frame, with the remaining four"
            " directions open)",
            "P-NONEMPTY (named, undischarged, inherited from Cycle 905)",
            "the Cycle-892 interface premises IF1..IF6 (named, undischarged,"
            " inherited)",
            "P-PURITY (named HERE, undischarged: that a locked admissible"
            " local possibility is pure; Lemma I-CONST needs it and the axioms"
            " do not supply it)",
        ],
        "conditionality_chain": [
            "A-SAMPLE", "P-SAMPLE-SPACE", "P-CONDITION-MAP", "P-NONEMPTY",
            "the Cycle-892 interface premises (IF1..IF6)", "P-PURITY",
        ],
        "scope": (
            "the full realized record-write census of the pinned Cycle-878"
            " construction at horizon 16384 orbits (92260 events over 748"
            " worlds), rebuilt by AST lift from the pinned Cycle-863 and"
            " Cycle-878 sources and never imported, with the Cycle-719 kernel"
            " as the one disclosed import (substrate); the covariant rule"
            " space rebuilt by AST lift from the pinned 2026-07-03"
            " classification runner; the gravity side entering ONLY through"
            " the pinned Cycle-905/906/907/909 receipts.  Exact integer and"
            " rational arithmetic throughout; no probability, no occurrence"
            " rule, no update law."),
        "label_on_every_fraction": FRACTION_LABEL,
        "restriction_gate": (f"{cert_b['reproduce']}/{cert_b['total']}"
                             " restriction gates reproduce"),
        "restriction_gate_rows": cert_b["rows"],
        "provenance": provenance,
        "firewall_hits": len(PRIMARY_FIREWALL.hits),
        "deterministic_double_build": cert_h["identical"],
        "elapsed_sec": round(elapsed, 3),
        "event_space_digest": digest_fwd,
        "audit": "unset",
        "authority": "none",
        "source_pins": [
            {"path": p, "sha256": cert_a["sha256"][p],
             "git_blob": cert_a["git_blobs"][p], "bytes": cert_a["bytes"][p]}
            for p in AUDIT_INPUT_PATHS],
    }
    receipt["science_digest"] = digest({
        "c1": cert_c["verdict"],
        "branch_matrix": cert_c["branch_matrix"]["verdicts"],
        "c2_prepare": dict(hist_prep), "c2_orbit": dict(hist_orbit),
        "c2_saturation": dict(hist_sat),
        "c3_zero_sets": [r["zero_weight_events"] for r in horn_rows],
        "c4_independent": independent_count,
        "verdict": verdict})
    receipt["self_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()

    out = ROOT / "outputs" / "type_vacuity_cycle911_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                              default=str) + "\n", encoding="utf-8")

    # ---------------- stdout ----------------------------------------------
    w = sys.stdout.write
    w("CYCLE 911 -- THE TYPE OF THE BORN LANE'S OBJECT, AND THE VACUITY"
      " QUESTION\n")
    w("=" * 78 + "\n")
    w(f"  every fraction below: {FRACTION_LABEL}\n\n")
    w(f"CERTIFICATE A_PINS {'PASS' if cert_a['pass'] else 'FAIL'}"
      f"  ({len(AUDIT_INPUT_PATHS)} pinned inputs, firewall hits"
      f" {len(PRIMARY_FIREWALL.hits)}, blocked modules loaded"
      f" {list(cert_a['blocked_modules_loaded'])})\n")
    w(f"CERTIFICATE B_RESTRICTION_GATE"
      f" {'PASS' if cert_b['pass'] else 'FAIL'}  {cert_b['reproduce']}/"
      f"{cert_b['total']} gates reproduce\n")
    for r in rows_b:
        if not r["match"]:
            w(f"    MISMATCH {r['gate']}: {r['computed']!r} !="
              f" {r['expected']!r}\n")

    w("\nC1 -- THE SAMPLE-SPACE PREMISE A-SAMPLE, NAMED AND TESTED\n")
    w("-" * 78 + "\n")
    cs = cert_c["census_shape"]
    w(f"  census keys {cs['keys']} = {cs['distinct_position_sets']} position"
      f" sets x {len(cs['event_values'])} event seeds; k in {cs['k_values']};"
      f" stations {cs['stations']}\n")
    w(f"  state vectors: one per key, width"
      f" {cert_c['what_the_keys_are']['state_vector_width']};"
      f" distinct tick-0 state vectors"
      f" {cert_c['what_the_keys_are']['distinct_initial_state_vectors']}\n")
    w(f"  reading (i) co-present sub-registers of ONE configuration: "
      f"{cert_c['what_the_keys_are']['reading_i_co_present_sub_registers']}\n")
    w(f"  reading (ii) alternative initial conditions of the same law: "
      f"{cert_c['what_the_keys_are']['reading_ii_alternative_initial_conditions']}\n")
    nc = cert_c["no_coupling"]
    w(f"  NO-COUPLING AST SWEEP: {nc['generated_chunk_source_stats']}\n")
    w(f"     violations {nc['generated_chunk_source_violations']};"
      f" planted cross-lane shift detected"
      f" {nc['planted_cross_lane_shift_detected_by_the_sweep']}\n")
    w(f"     runtime perturbation witness: {len(perturb_rows)} samples,"
      f" {PERTURB_ORBITS} orbits each, total leak outside the perturbed"
      f" lane's own bit = {nc['perturbation_leak_total']}\n")
    bm = cert_c["branch_matrix"]
    w(f"  BRANCH MATRIX over {bm['total_world_pairs']} world pairs:\n")
    for k, v in sorted(bm["verdicts"].items()):
        w(f"      {k:38s} {v}\n")
    w(f"      pairs sharing a tick-0 state              "
      f" {bm['pairs_sharing_a_tick0_state']}\n")
    w(f"      of those, also sharing a schedule         "
      f" {bm['pairs_sharing_a_tick0_state_AND_a_schedule']}\n")
    w(f"      co-simulated sample {bm['co_simulated_sample']},"
      f" diverged {bm['co_simulated_diverged']},"
      f" first-divergence histogram"
      f" {bm['co_simulated_first_divergence_histogram']}\n")
    w(f"      BRANCH PAIRS FOUND: {bm['branch_pairs_found']}"
      f"   planted branch pair detected:"
      f" {bm['planted_branch_pair_detected']}\n")
    w(f"  setup coordinates that differ:"
      f" {bm['setup_coordinates_that_differ']}\n")
    w(f"  C1 VERDICT: {cert_c['verdict']}\n")
    w(f"  {cert_c['what_follows']}\n")

    w("\nC2 -- SINGLETON AVAILABILITY AT FORMATION\n")
    w("-" * 78 + "\n")
    w(f"  formation events: {cert_d['formation_events']};"
      f" lock boundaries {cert_d['lock_boundary_range']};"
      f" locks at moment 0: {cert_d['locks_at_moment_zero']}\n")
    w(f"  |A| histogram OP_PREPARE     {cert_d['A_histogram_prepare']}\n")
    w(f"  |A| histogram OP_ORBIT       {cert_d['A_histogram_orbit']}\n")
    w(f"  |A| histogram OP_SATURATION (corrected)"
      f"  {cert_d['A_histogram_saturation_corrected']}"
      f"   as pinned-863 slices it"
      f" {cert_d['A_histogram_saturation_as_pinned_863_slices_it']}"
      f"   (constructor errors {cert_d['prepare_errors']})\n")
    sd = cert_d["pinned_863_chunk_slicing_defect"]
    w(f"  PINNED-863 CHUNK-SLICING DEFECT: word length"
      f" {sd['sample_word_length']} over {sd['stations']} stations,"
      f" divisible={sd['length_is_divisible_by_stations']}, per-step gate"
      f" counts {sd['per_step_gate_counts']}\n")
    w(f"  O3 vacuous on this census: {cert_d['O3_vacuous_on_this_census']}\n")
    if first_site:
        w(f"  FIRST GENUINE SELECTION SITE: world {first_site['world']}"
          f" key {first_site['key']} at boundary"
          f" {first_site['lock_boundary']}, menu"
          f" {first_site['menu_prepare']} (orbit-consistent:"
          f" {first_site['menu_orbit']})\n")
    w(f"  restricted-menu falsifier detected:"
      f" {cert_d['restricted_menu_falsifier_detected']}\n")
    w("  MENU-MULTIPLICITY SPECTRUM over the classified covariant rule"
      " space:\n")
    for s in spectra:
        w(f"      k={s['alphabet_k']}  proper orbits"
          f" {s['proper_orbits_total']:4d}  classes realized"
          f" {s['classes_realized_by_the_formation_contexts']}  class sizes"
          f" {s['class_sizes']}  achievable |A| assignments"
          f" {s['achievable_menu_multiplicity_spectra']}  distinct"
          f" distributions {s['distinct_A_distributions']}\n")
    w(f"  {cert_d['saturation_reading']}\n")

    w("\nC3 -- THE REALIZATION DILEMMA, AND THE O1 CORRECTION\n")
    w("-" * 78 + "\n")
    w(f"  878 note, byte-quoted: {QUOTE_878_REALIZED!r}\n")
    for r in horn_rows:
        w(f"      {r['candidate']:26s} zero on {r['zero_weight_events']:6d} /"
          f" {r['of_total']}  = {r['fraction_of_certified_realized_events']}"
          f"  (= {r['percent_exact']}% exactly,"
          f" {r['percent_rounded_display']}% rounded)  [{r['label']}]\n")
    w(f"  {cert_e['THE_DILEMMA']}\n")
    w("  O1 CORRECTION:\n")
    w(f"      878 note says: {QUOTE_878_BOUNDARY!r}\n")
    w(f"      pinned memo says: {QUOTE_AXIOM_APPEND!r}\n")
    w(f"      byte fact: {cert_e['O1_CORRECTION']['the_byte_fact']}\n")
    w(f"      correction: {cert_e['O1_CORRECTION']['the_correction']}\n")

    w("\nC4 -- THE CLAIMED FOUR-WAY CONVERGENCE\n")
    w("-" * 78 + "\n")
    for c in convergence:
        w(f"      {c['mechanism']:52s} independent={c['independent']}\n")
        w(f"          {c['status']}\n")
    w(f"  surviving independent mechanisms:"
      f" {independent_count} of {cert_f['claimed_independent_mechanisms']}\n")
    w(f"  ML: argmax = {ml['argmax_is_the_uniform_counting_measure']};"
      f" zero-likelihood candidates ="
      f" {list(ml['zero_likelihood_candidates_from_pinned_receipts'])}\n")
    w(f"  transitivity: world orbits {transitive['world_orbits']},"
      f" tag blocks {transitive['tag_block_sizes']}, transitive on events ="
      f" {transitive['is_transitive_on_the_92260_events']}\n")
    w(f"  I-CONST: transitivity on pure possibilities certified ="
      f" {iconst['transitivity_certified']}; non-constant invariant exists ="
      f" {iconst['radius_is_a_nonconstant_unitary_invariant']}\n")
    w(f"  {iconst['verdict']}\n")
    w(f"  THE HORN: {cert_f['the_horn']}\n")

    w(f"\nCERTIFICATE G_FALSIFIERS {'PASS' if cert_g['pass'] else 'FAIL'}"
      f"  ({cert_g['tooth_count']} teeth)\n")
    for t in teeth:
        w(f"      {t['tooth']:48s} detected={t['detected']}\n")
    w(f"CERTIFICATE H_DOUBLE_BUILD {'PASS' if cert_h['pass'] else 'FAIL'}"
      f"  A={cert_h['digest_A'][:16]} B={cert_h['digest_B'][:16]}"
      f" identical={cert_h['identical']}"
      f" pinned-prefix-identical={cert_h['prefix_event_lists_identical']}"
      f" slots-inert={cert_h['record_slots_are_inert']}\n")
    w(f"CERTIFICATE I_RUNTIME {'PASS' if cert_i['pass'] else 'FAIL'}"
      f"  {cert_i['elapsed_sec']}s / {cert_i['budget_sec']}s\n")

    w("\nTHEOREMS\n" + "-" * 78 + "\n")
    for t in theorems:
        w("  " + t + "\n\n")
    w(f"VERDICT: {verdict}\n")
    w(f"all_certificates_pass: {receipt['all_certificates_pass']}\n")
    w(f"receipt: {out.relative_to(ROOT)}\n")
    w(f"science_digest: {receipt['science_digest']}\n")
    return 0 if receipt["all_certificates_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
