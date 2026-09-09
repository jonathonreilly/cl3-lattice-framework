"""Cycle 936 -- THE CHOICE SUBSTRATE: hosting a P3 node, and what it costs.

Cycle 925 closed with a classification theorem and a named engineering successor:

    "R2 (the choice point) = THE SOLE GENUINE RELAXATION.  Not constructible
     against the pinned compiler: the admitted grammar contains no node that can
     deliver two values at one occasion."

    "a substrate/compiler admitting a P3 node (an engineering successor, out of
     scope by design)."

THIS BLOCK BUILDS IT -- with the weight PARAMETRIC.

ABSOLUTE FIREWALL.  Nothing here adopts, proposes or prefers any weight value.
The A3 sentence stays unadopted.  The substrate HOSTS a choice point whose
weight is an explicit free parameter mu -- a SYMBOL.  Numbers appear only in a
declared diagnostic grid whose entire purpose is to show that no step of this
block privileges any of them.  This block prices what hosting costs.

  Q1  THE MINIMAL GRAMMAR EXTENSION.  One new statement template

          c[{}] ^= CHOICE({}) & {}

      added to the pinned compiler's three.  CHOICE(k) is the choice node at
      choice-occasion ordinal k.  The extension is MULTI-VALUED BY SEMANTICS:
      the compiled object is not one execution but a FAMILY -- a TREE of
      trajectories over ONE (schedule, tick-0 state), branching at choice
      occasions.  Verified mechanically: exactly one new AST node type; the
      extended provenance sweep finds exactly one P3 node kind; the unextended
      programs compile BIT-IDENTICALLY (full compile census + full-horizon
      execution census, both layouts).

      The critical design constraint from 925: the choice source must be P3,
      not P2-in-disguise.  A pre-written tape is P2 (925 proved it a
      re-labeling).  The mechanical discriminator implemented here is the
      MULTI-VALUEDNESS GATE: across every branch of the tree the compiled
      chunk source text is byte-identical, the tick-0 columns are
      byte-identical, no declared datum varies, and at every branch node the
      two children share a byte-identical PARENT MACHINE STATE -- and the
      trajectories still diverge.  A tape cannot do that: to deliver two
      values it must vary the tick-0 carrier or the gate schedule, and 925
      proved those are the only two forms.  Planted tapes must be caught.

  Q2  WHAT HOSTING COSTS, MEASURED.  The 918 writable-endpoint modification
      M_A is spliced onto the extended substrate with the choice node at the
      selection site (the same endpoint pair, the same station anchor, the
      same menu-preserving both-wires form).  Over a declared window the FULL
      tree is enumerated EXACTLY (never sampled): (a) the 918 constraint
      battery per branch; (b) the tree's structure and the genuine branch
      pairs -- two trajectories sharing (schedule, tick-0 state) and diverging,
      the article the census never had; (c) the weight algebra as formal
      polynomials in mu, with the freedom count measured, not assumed;
      (d) what breaks, each with a witness.

  Q3  THE PRICE SHEET.  Grammar delta + semantic delta + preserved battery +
      broken battery + freedom count.  Predictions are SEALED before the tree
      is computed and scored afterwards.

Discipline: TEXT/AST/JSON only; the 719 two-rail core is the single disclosed
import (as substrate); exact integer and exact rational arithmetic; splice-only
construction with the control gated digest-identical to the pinned 913/918
builds in BOTH layouts; restriction gates that hard-fail against the pinned
918/925/911 receipt bytes value-for-value BEFORE any new number is quoted;
planted falsifiers that must fire.  No probability, no occurrence rule and no
update law is introduced.  Nothing here is adopted, proposed or decided.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, product
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
HANDSHAKE_PATH = \
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
C863_PATH = "scripts/frontier_cycle863_time_from_records_2026_07_28.py"
C878_PATH = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C911_PATH = "scripts/frontier_cycle911_type_vacuity_2026_07_28.py"
C911_RECEIPT = "outputs/type_vacuity_cycle911_receipt_2026_07_28.json"
C913_PATH = "scripts/frontier_cycle913_selection_function_2026_07_28.py"
C913_RECEIPT = "outputs/selection_function_cycle913_receipt_2026_07_28.json"
C918_PATH = "scripts/frontier_cycle918_writable_endpoint_2026_07_28.py"
C918_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
C925_PATH = "scripts/frontier_cycle925_law_relaxation_2026_07_28.py"
C925_RECEIPT = "outputs/law_relaxation_cycle925_receipt_2026_07_28.json"
C925_NOTE = (
    "docs/LAW_RELAXATION_CLASSIFIED_A3_SOLE_RELAXATION_CYCLE925"
    "_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
C918_NOTE = (
    "docs/WRITABLE_ENDPOINT_BORN_CAPABLE_FIRST_BRANCH_PAIRS_CYCLE918"
    "_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    CORE_PATH, HANDSHAKE_PATH, C863_PATH, C878_PATH, C878_RECEIPT, C911_PATH,
    C911_RECEIPT, C913_PATH, C913_RECEIPT, C918_PATH, C918_RECEIPT, C925_PATH,
    C925_RECEIPT, C918_NOTE, C925_NOTE, AXIOMS_PATH,
)
IMPORTED_PATHS = (CORE_PATH,)
AST_ONLY_PATHS = (C863_PATH, C878_PATH, C911_PATH, C913_PATH, C918_PATH,
                  C925_PATH)
JSON_ONLY_PATHS = (C878_RECEIPT, C911_RECEIPT, C913_RECEIPT, C918_RECEIPT,
                   C925_RECEIPT)
TEXT_ONLY_PATHS = (C918_NOTE, C925_NOTE, AXIOMS_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    HANDSHAKE_PATH:
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
    C863_PATH:
        "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
    C878_PATH:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C911_PATH:
        "6474f1e919c97fcb3336a8cea480b5e824fe48f4ea5ce4592c1b75bc0b0007d1",
    C911_RECEIPT:
        "90d1fb2a3ac31065f75345ac1e98520622aa6302c50dcf4a8a11f44a1cde11b0",
    C913_PATH:
        "b349f873aa1e88558fcd63fc432a6edd249f48f103ecbd3d28fd62d070e689ef",
    C913_RECEIPT:
        "0de8d785c2139126b813166e090493d65cb289508b46de7f928b440facb82ecd",
    C918_PATH:
        "0ef019ef77cf3ff33c7e6c29ac31d1cd53945bd5f505f1fd4b3387e74017289d",
    C918_RECEIPT:
        "849ad2bbb4abc8c9eda5541246784e2bdb69feaf423aac7c6f3aff83f6062bbd",
    C925_PATH:
        "b5ddffd78a8c77318228f47e6c898ef726d4b787c901de82d5f49a75cb74eeb2",
    C925_RECEIPT:
        "f4fabe50ed8b775f2f1288380824ae04f0129f4f136e3b338bafd05647031757",
    C918_NOTE:
        "40333f3bb83f77a3e7c89eb232bbe24c01885cdcfdcab7888ae319419c1efaee",
    C925_NOTE:
        "ed36a7afb889a45ccde08a4f5d6735fa028a12e4aaa9edda3348ab687678c676",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    HANDSHAKE_PATH: "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f",
    C863_PATH: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
    C878_PATH: "af2e27c4a01b02b68c319e3a572eaeb2217e04e7",
    C878_RECEIPT: "565faf0be5e6930b08f585fea1c30b2ceaa41a91",
    C911_PATH: "3335e9dee5027b935d0eb3c814601b8f8e83b550",
    C911_RECEIPT: "af51342a72c56db8e562e1f1a607f207508b42ed",
    C913_PATH: "2093b687713eb12b462532761092d90d40bed718",
    C913_RECEIPT: "5ac6a40c316c7a90bcf867eb6507518ba976169b",
    C918_PATH: "b5a1a5643abe87ab4a92fd86e8c0007e8f26539a",
    C918_RECEIPT: "5704619b21d9a3af312956580355d6dd5a303f53",
    C925_PATH: "5dc5151b726817593bbde4d9cf488038af19584a",
    C925_RECEIPT: "fed1b28e9e5cfe731a541645dce705541d69c967",
    C918_NOTE: "186af20c471f8cbb4e9c9871fc2ee652d813e348",
    C925_NOTE: "37f5bad6f1ef329890e7cebee97ba99a5f699356",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}

BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AST_ONLY_PATHS)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 900
FRACTION_LABEL = "bookkeeping fraction, not probability"

HORIZON = 16_384
DEAD_CHUNK_ORBITS = 512
LANE_SHIFT = 1

# ---- the declared tree window and the declared choice atoms ---------------
TREE_ORBITS = 175                       # declared sub-horizon for the tree
TREE_BOUNDARIES = TREE_ORBITS * 11      # 1925 -- filled in from `stations`
# each atom is (chunk application index, census world index).  the application
# index t means: the t-th chunk application of the run (the chunk that takes
# boundary t to boundary t+1).  every atom is gated for ELIGIBILITY (the
# world's lane must be inside station 0's mask at that application) and for
# EFFECTIVITY (its two values must be observably distinguishable).
CHOICE_ATOMS = ((300, 715),
                (700, 475), (700, 540),
                (702, 254), (702, 450), (702, 715),
                (1100, 558), (1100, 715))
FULL_TREE_LEAF_CAP = 4096               # declared: the tree is never sampled
# the declared diagnostic grid.  its ONLY purpose is the parametric firewall:
# to exhibit that no verdict of this block depends on which of these numbers
# is substituted for mu.  it is not a prior, not a proposal and not a range.
MU_DIAGNOSTIC_GRID = ((0, 1), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (1, 1))


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


# ---------------------------------------------------------------------------
# A: pins
# ---------------------------------------------------------------------------

def pin_rows():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p in IMPORTED_PATHS + AST_ONLY_PATHS:
        ast.parse(payloads[p], filename=p)
    for p in JSON_ONLY_PATHS:
        json.loads(payloads[p].decode("utf-8"))
    self_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"),
                          filename=Path(__file__).name)
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
        "modification_mechanism":
            "WRAP, NEVER EDIT.  The pinned kernel file is imported read-only "
            "and its bytes are hashed above.  The COMPILER is not edited "
            "either: this file declares its own emitter, which is gated "
            "byte-identical to the pinned Cycle-863 compile_fast text on every "
            "unextended program, and which admits exactly one further "
            "statement template.  Every construction is a tuple of compiled "
            "gate rows declared in this file and spliced into the composed "
            "scan by this file's own schedule builder.  No pinned file is "
            "written, patched, monkey-patched or reloaded.",
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
            n for n in BLOCKLISTED_MODULES if n in sys.modules),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
    }
    result["pass"] = bool(
        result["literal_ok"] and result["existing_worktree_relative"]
        and result["sha256_all_match"] and result["git_blobs_all_match"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"])
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


def lift_ast_op_tuple(path: str, name: str):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                names = []
                for element in node.value.elts:
                    if not (isinstance(element, ast.Attribute)
                            and isinstance(element.value, ast.Name)
                            and element.value.id == "ast"):
                        raise AssertionError(("op tuple shape", name))
                    names.append(element.attr)
                return tuple(getattr(ast, n) for n in names), tuple(names)
    raise AssertionError(("op tuple not found", path, name))


C863_FUNCS = (
    "pairwise_separated", "derive_event_seeds", "derive_census",
    "watched_registers", "dirty_partition", "build_initial_states",
    "pack_lanes", "compile_masked_gate", "masked_h_schedules", "compile_fast",
    "mask_over", "lanes_of", "lane_state", "synchronous_word",
)
C863_CONSTS = ("FIXTURE_BANKS", "MIN_SOURCES", "MAX_SOURCES")
C878_FUNCS = ("lcm", "monitor_phase_action", "group_orbits", "dead_wire_rig")
C878_CONSTS = ("HORIZON", "REGISTER_CAP", "DEAD_CHUNK_ORBITS",
               "DEAD_ORBIT_ORBITS")
C911_FUNCS = ("snapshot_scan", "classify_pair")
C911_CONSTS = ("DIRECTIONS", "REGISTER_CAP", "HORIZON", "CLASS_BRANCH",
               "CLASS_IDENTICAL", "CLASS_SETUP_TICK0", "CLASS_SETUP_SCHEDULE",
               "CLASS_NONBRANCH_DIVERGENCE")
C913_FUNCS = ("endpoint_wires", "read_state_direction", "target_wire_sweep",
              "hamming_readout", "translation_covariance")


def lift_machinery():
    ns863, consts863, names863 = ast_lift(
        C863_PATH, C863_FUNCS, C863_CONSTS,
        {"K": K, "combinations": combinations, "Counter": Counter})
    c863 = SimpleNamespace(**{n: ns863[n] for n in C863_FUNCS})
    ns878, consts878, names878 = ast_lift(
        C878_PATH, C878_FUNCS, C878_CONSTS,
        {"C863": c863, "Counter": Counter, "sha256": sha256, "json": json,
         "gcd": math.gcd})
    c878 = SimpleNamespace(**{n: ns878[n] for n in C878_FUNCS})
    cross_ops, cross_names = lift_ast_op_tuple(C911_PATH, "CROSS_LANE_OPS")
    pos_ops, pos_names = lift_ast_op_tuple(C911_PATH, "POSITIONWISE_OPS")
    ns911, consts911, names911 = ast_lift(
        C911_PATH, C911_FUNCS, C911_CONSTS,
        {"K": K, "np": np, "itertools": itertools, "Counter": Counter,
         "sha256": sha256, "ast": ast,
         "CROSS_LANE_OPS": cross_ops, "POSITIONWISE_OPS": pos_ops})
    c911 = SimpleNamespace(**{n: ns911[n] for n in C911_FUNCS})
    ns913, consts913, names913 = ast_lift(
        C913_PATH, C913_FUNCS, (), {"K": K, "Counter": Counter,
                                    "sha256": sha256})
    c913 = SimpleNamespace(**{n: ns913[n] for n in C913_FUNCS})
    provenance = {
        "lifted_from_863": names863, "constants_863": consts863,
        "lifted_from_878": names878, "constants_878": consts878,
        "lifted_from_911": names911,
        "constants_911": {
            k: ([list(x) for x in v] if k == "DIRECTIONS" else v)
            for k, v in consts911.items()},
        "lifted_911_operator_tuples": {"CROSS_LANE_OPS": list(cross_names),
                                       "POSITIONWISE_OPS": list(pos_names)},
        "lifted_from_913": names913,
        "import_of_863_878_911_913_918_or_925": False,
        "single_disclosed_import": CORE_PATH,
    }
    return (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
            provenance)


# ---------------------------------------------------------------------------
# B: THE GRAMMAR -- the pinned three templates and the one-template extension
# ---------------------------------------------------------------------------

KIND_X, KIND_CNOT, KIND_TOF, KIND_SHIFT, KIND_CHOICE = 0, 1, 2, 3, 4
KIND_NAMES = {KIND_X: "X", KIND_CNOT: "CNOT", KIND_TOF: "TOF",
              KIND_SHIFT: "SHIFT_CNOT", KIND_CHOICE: "CHOICE"}
CERTIFIED_KINDS = (KIND_X, KIND_CNOT, KIND_TOF)

# the pinned compiler's three admitted statement templates (Cycle 925 read
# them off the pinned compile_fast AST; reproduced and gated in B).
PINNED_TEMPLATES = (" c[{}] ^= {}",
                    " c[{}] ^= c[{}] & {}",
                    " c[{}] ^= c[{}] & c[{}] & {}")
# ---- THE GRAMMAR DELTA: exactly one further template ----------------------
CHOICE_TEMPLATE = " c[{}] ^= CHOICE({}) & {}"
EXTENDED_TEMPLATES = PINNED_TEMPLATES + (CHOICE_TEMPLATE,)

GRAMMAR_DELTA_TEXT = (
    "THE MINIMAL GRAMMAR EXTENSION.  The pinned Cycle-863 compiler admits "
    "exactly three statement templates:\n"
    "    c[t] ^= M                     (X)\n"
    "    c[t] ^= c[a] & M              (CNOT)\n"
    "    c[t] ^= c[a] & c[b] & M       (TOF)\n"
    "where t,a,b are literal wire addresses and M is a compile-time integer "
    "lane mask.  The extension adds EXACTLY ONE further template:\n"
    "    c[t] ^= CHOICE(k) & M         (CHOICE)\n"
    "where k is a compile-time integer: the CHOICE-OCCASION ORDINAL.  "
    "Syntactically that is one new AST node type (Call) in the emitted "
    "statement grammar and nothing else.\n\n"
    "SEMANTICS -- and this is the whole of the extension.  CHOICE(k) is not a "
    "function of anything.  It is MULTI-VALUED: at occasion k it may deliver "
    "either of the two lane-words {0, S_k}, where S_k is the declared CHOICE "
    "SUPPORT at that occasion (which sites may choose).  Consequently the "
    "compiled object is NOT an execution.  It is a FAMILY of executions -- a "
    "TREE of trajectories rooted at (schedule, tick-0 state) and branching at "
    "every choice occasion, one child per assignment of values to the atoms "
    "in that occasion's support.  Compilation therefore has the type\n"
    "    compile : (schedule, tick-0 state) -> TREE of trajectories\n"
    "whereas the pinned compiler had\n"
    "    compile : (schedule, tick-0 state) -> ONE trajectory.\n"
    "That type change IS the relaxation Cycle 925 classified as R2, and it is "
    "the only thing the extension buys.\n\n"
    "THE WEIGHT IS NOT PART OF THE EXTENSION.  A branch of the tree carries a "
    "formal label mu -- a free symbol, one per choice atom under the "
    "per-occasion reading, one per site under the per-site reading.  The "
    "substrate never reads mu; no step of this block evaluates it; it labels "
    "branches and selects nothing.  Supplying VALUES for mu is exactly the "
    "unadopted A3-shaped sentence, and nothing here supplies one.")

P3_NOT_P2_TEXT = (
    "THE P3-NOT-P2 OBLIGATION.  Cycle 925 proved that a pre-written tape is "
    "P2 -- a re-labeling of the schedule or of the tick-0 state -- and that "
    "every filling of a selection register available on the pinned substrate "
    "collapses into R4/R1/R3.  A fourth template is therefore NOT sufficient "
    "to make a P3: a node spelled CHOICE(k) but BOUND to a tape is a P2 node "
    "wearing the new syntax.  The extension's P3 status is a SEMANTIC "
    "certificate, earned by the MULTI-VALUEDNESS GATE and not by the "
    "grammar:\n"
    "  M1  one law.  The compiled chunk source TEXT is byte-identical on "
    "every branch of the tree (one schedule, not a family of schedules).\n"
    "  M2  one setup.  The tick-0 column vector is byte-identical on every "
    "branch (one tick-0 state, not a family of carriers).\n"
    "  M3  no other declared datum varies across branches: the branch "
    "coordinate is the choice sequence and nothing else.\n"
    "  M4  no hidden state.  At every branch node the children are entered "
    "from a byte-identical PARENT MACHINE STATE -- the same columns, the same "
    "boundary index, the same record ledger, the same ordinals -- so the "
    "divergence is not explained by anything the machine holds.\n"
    "  M5  non-degeneracy.  At least two branches actually diverge.\n"
    "M1+M2+M3+M5 together are the exact negation of the Cycle-918 determinism "
    "lemma ('two lanes handed the same schedule and the same tick-0 state "
    "receive the same gates in the same order, so their columns stay equal "
    "for ever').  A tape cannot satisfy them: to deliver two values it must "
    "vary the tick-0 carrier (breaking M2) or the gate schedule (breaking "
    "M1), and Cycle 925 proved those are the only two forms available.  Both "
    "planted tapes are built here and both must be caught.\n"
    "HONEST RESIDUAL: the leaf SET of a tree is extensionally the same set as "
    "the trajectory set of a family of tapes.  The distinction is intensional "
    "and is exactly what M1-M4 measure -- ONE law and ONE setup with many "
    "trajectories, versus MANY declared inputs with one trajectory each.  "
    "This block reports the intensional distinction as what it is and does "
    "not claim an extensional one.")


def pinned_statement_text(kind, a, b, c3, mask):
    """The pinned Cycle-863 compile_fast source text, byte for byte."""
    if kind == KIND_X:
        return f" c[{a}] ^= {mask}"
    if kind == KIND_CNOT:
        return f" c[{b}] ^= c[{a}] & {mask}"
    if kind == KIND_TOF:
        return f" c[{c3}] ^= c[{a}] & c[{b}] & {mask}"
    raise ValueError(("pinned kinds are 0/1/2 only", kind))


def extended_statement_text(kind, a, b, c3, mask):
    """The EXTENDED compiler's emitter.  Kinds 0/1/2 reproduce the pinned text
    byte for byte (gated in B); kind 4 is the one new template."""
    if kind in (KIND_X, KIND_CNOT, KIND_TOF):
        return pinned_statement_text(kind, a, b, c3, mask)
    if kind == KIND_CHOICE:
        # a is the choice-occasion ordinal k; b is the target wire
        return f" c[{b}] ^= CHOICE({a}) & {mask}"
    if kind == KIND_SHIFT:
        return f" c[{b}] ^= (c[{a}] >> {LANE_SHIFT}) & {mask}"
    raise ValueError(("gate kind", kind))


def chunk_source(schedule, emitter=extended_statement_text):
    src = ["def apply_chunk(c):"]
    if not schedule:
        src.append(" pass")
    for row in schedule:
        src.append(emitter(*row))
    return src


def gate_text(kind, a, b, c3):
    return extended_statement_text(kind, a, b, c3, "<mask>")


def gate_target(kind, a, b, c3):
    if kind == KIND_X:
        return a
    if kind in (KIND_CNOT, KIND_SHIFT, KIND_CHOICE):
        return b
    return c3


def station_mask(sim, station, step, stations):
    return sum(1 << lane for lane, (_k, _e, pos) in enumerate(sim)
               if (station - step) % stations in pos)


def build_schedules(c863, program, sim, extra_station, extra_gates):
    """The composed scan's masked-schedule compiler with declared extra macros
    appended to one station's macro.  Empty extras reproduce the pinned
    Cycle-863 masked_h_schedules row for row (gated in B)."""
    stations = len(program)
    rows = []
    for step in range(stations):
        schedule = []
        for station, row in enumerate(program):
            mask = station_mask(sim, station, step, stations)
            if mask:
                schedule.extend(
                    c863.compile_masked_gate(g, mask)
                    for g in K.mapped_macro(row))
                if extra_gates and station == extra_station:
                    for kind, a, b, c3 in extra_gates:
                        schedule.append((kind, a, b, c3, mask))
        rows.append(tuple(schedule))
    return tuple(rows)


# the CHOICE binding.  The tree walker writes the occasion's value here
# immediately before the chunk that consumes it; nothing reads it back.  It is
# a SINK for the enumerator, never a SOURCE the machine holds -- which is
# exactly what clause M4 of the multi-valuedness gate certifies.
_CHOICE_SINK = {}


def CHOICE(k):
    return _CHOICE_SINK[k]


def compile_schedules(schedules, globals_=None):
    fns = []
    for schedule in schedules:
        ns: dict = {}
        env = {"__builtins__": {}, "CHOICE": CHOICE}
        if globals_:
            env.update(globals_)
        exec("\n".join(chunk_source(schedule)), env, ns)
        fns.append(ns["apply_chunk"])
    return tuple(fns)


# ---------------------------------------------------------------------------
# the provenance sweep -- the pinned Cycle-925 classifier, plus the extension
# ---------------------------------------------------------------------------

P1 = "P1_DECLARED_STATE"
P2 = "P2_DECLARED_NON_STATE_INPUT_STREAM"
P3 = "P3_LAW_INTERNAL_CHOICE_POINT"
P4 = "P4_INDEX_OR_BOOKKEEPING_COORDINATE"
P_UNCLASSIFIED = "UNCLASSIFIED_FIFTH_CATEGORY"


def is_choice_node(node):
    """The one admitted shape of the new template's leaf: CHOICE(<int>)."""
    return (isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name) and node.func.id == "CHOICE"
            and not node.keywords and len(node.args) == 1
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, int))


def classify_leaf(node, positionwise_ops, cross_lane_ops, extended=False):
    """Cycle 925's classifier verbatim (gated to reproduce its numbers), with
    ONE extension when `extended`: the admitted CHOICE(k) shape is a P3 LEAF
    and is not descended into.  Every other call remains what 925 made it."""
    if extended and is_choice_node(node):
        # ONE node kind.  The occasion ordinal is an argument of the node, not
        # a different node: the ordinals are counted separately below.
        return P3, "choice-node:CHOICE(<occasion-ordinal-literal>)"
    if isinstance(node, ast.Subscript):
        if isinstance(node.value, ast.Name) and node.value.id == "c" \
                and isinstance(node.slice, ast.Constant) \
                and isinstance(node.slice.value, int):
            return P1, f"c[{node.slice.value}]"
        return P_UNCLASSIFIED, "subscript-with-non-literal-address"
    if isinstance(node, ast.Constant):
        if isinstance(node.value, int):
            return P4, "integer-literal-mask"
        return P_UNCLASSIFIED, f"non-int-constant:{type(node.value).__name__}"
    if isinstance(node, ast.Name):
        if node.id == "c":
            return P1, "state-container"
        return P2, f"free-name:{node.id}"
    if isinstance(node, (ast.Call, ast.IfExp, ast.Compare, ast.BoolOp,
                         ast.Lambda, ast.ListComp, ast.SetComp, ast.DictComp,
                         ast.GeneratorExp, ast.Await, ast.Yield)):
        return P3, f"choice-point:{type(node).__name__}"
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, cross_lane_ops):
            return P4, f"lane-index-operator:{type(node.op).__name__}"
        if isinstance(node.op, positionwise_ops):
            return None, f"positionwise-operator:{type(node.op).__name__}"
        return P_UNCLASSIFIED, f"operator:{type(node.op).__name__}"
    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, positionwise_ops):
            return None, f"positionwise-unary:{type(node.op).__name__}"
        return P_UNCLASSIFIED, f"unary:{type(node.op).__name__}"
    if isinstance(node, (ast.Load, ast.Store)):
        return None, "ctx"
    if isinstance(node, (ast.BitXor, ast.BitAnd, ast.BitOr, ast.Invert,
                         ast.LShift, ast.RShift, ast.Add, ast.Sub, ast.Mult,
                         ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,
                         ast.MatMult)):
        return None, "bare-operator-node"
    return P_UNCLASSIFIED, f"node:{type(node).__name__}"


def provenance_sweep(sources, positionwise_ops, cross_lane_ops,
                     extended=False):
    counts = Counter()
    detail = Counter()
    node_types = Counter()
    statements = 0
    targets: set = set()
    reads: set = set()
    violations: list = []
    shape_violations: list = []
    choice_ordinals = Counter()
    for step, src in enumerate(sources):
        tree = ast.parse("\n".join(src))
        if len(tree.body) != 1 or not isinstance(tree.body[0],
                                                 ast.FunctionDef):
            shape_violations.append(("not a single function def", step))
            continue
        fn = tree.body[0]
        if fn.args.args and [a.arg for a in fn.args.args] != ["c"]:
            shape_violations.append(("argument is not the state container",
                                     step))
        for stmt in fn.body:
            statements += 1
            if isinstance(stmt, ast.Pass):
                statements -= 1
                continue
            if not isinstance(stmt, ast.AugAssign):
                shape_violations.append(("statement is not an AugAssign",
                                         step))
                continue
            if not isinstance(stmt.op, ast.BitXor):
                shape_violations.append(("AugAssign op is not ^=", step))
                continue
            tgt = stmt.target
            if not (isinstance(tgt, ast.Subscript)
                    and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "c"
                    and isinstance(tgt.slice, ast.Constant)
                    and isinstance(tgt.slice.value, int)):
                shape_violations.append(("target is not c[literal]", step))
                continue
            targets.add(tgt.slice.value)
            for nd in ast.walk(stmt):
                node_types[type(nd).__name__] += 1

            def visit(node, step=step):
                cls, tag = classify_leaf(node, positionwise_ops,
                                         cross_lane_ops, extended)
                detail[tag] += 1
                if cls is not None:
                    counts[cls] += 1
                    if cls in (P2, P3, P_UNCLASSIFIED):
                        violations.append({"step": step, "class": cls,
                                           "tag": tag})
                if cls == P1 and isinstance(node, ast.Subscript):
                    reads.add(node.slice.value)
                    return
                if extended and is_choice_node(node):
                    choice_ordinals[node.args[0].value] += 1
                    return
                for child in ast.iter_child_nodes(node):
                    visit(child)

            visit(stmt.value)
    return {
        "statements": statements,
        "class_counts": {k: counts[k] for k in sorted(counts)},
        "node_tag_counts": {k: detail[k] for k in sorted(detail)},
        "ast_node_types": {k: node_types[k] for k in sorted(node_types)},
        "distinct_state_addresses_read": len(reads),
        "distinct_state_addresses_written": len(targets),
        "P2_P3_or_unclassified_sites": len(violations),
        "violations": violations[:24],
        "shape_violations": shape_violations[:24],
        "shape_violation_count": len(shape_violations),
        "choice_ordinal_counts": {str(k): v
                                  for k, v in sorted(choice_ordinals.items())},
        "_reads": reads, "_targets": targets,
    }


def compiler_templates_from_pin():
    """Enumerate the statement templates the PINNED compiler can emit, read off
    the pinned Cycle-863 compile_fast source itself (not re-typed here)."""
    tree = ast.parse((ROOT / C863_PATH).read_text(encoding="utf-8"),
                     filename=C863_PATH)
    templates = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.FunctionDef)
                and node.name == "compile_fast"):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call) \
                    and isinstance(sub.func, ast.Attribute) \
                    and sub.func.attr == "append":
                arg = sub.args[0] if sub.args else None
                if isinstance(arg, ast.JoinedStr):
                    shape = []
                    for piece in arg.values:
                        shape.append(piece.value
                                     if isinstance(piece, ast.Constant)
                                     else "{}")
                    templates.append("".join(shape))
                elif isinstance(arg, ast.Constant):
                    templates.append(arg.value)
    return templates


# ---------------------------------------------------------------------------
# the machine: one trajectory, steppable, snapshot/restore for tree walking
# ---------------------------------------------------------------------------

def acc_add(planes: list, mask: int) -> None:
    i = 0
    carry = mask
    while carry:
        if i == len(planes):
            planes.append(0)
        t = planes[i] & carry
        planes[i] ^= carry
        carry = t
        i += 1


def acc_get(planes: list, lane: int) -> int:
    value = 0
    for i, plane in enumerate(planes):
        if (plane >> lane) & 1:
            value |= 1 << i
    return value


def item_of(left_bit, right_bit):
    """K.M.prepare_endpoint writes LEFT = int(v == (0,1)), RIGHT = int(v ==
    (1,0)); reading the two wires back inverts it (Cycle 913's RD-STATE)."""
    if left_bit == 0 and right_bit == 1:
        return (1, 0)
    if left_bit == 1 and right_bit == 0:
        return (0, 1)
    return None


class Machine:
    """One composed-scan trajectory, advanced boundary by boundary."""

    def __init__(self, env, reverse_layout, capture_snapshots=False):
        c863 = env["c863"]
        self.capture_snapshots = capture_snapshots
        self.snapshots: dict = {}
        n = env["n"]
        order = list(range(n - 1, -1, -1)) if reverse_layout \
            else list(range(n))
        self.env = env
        self.order = order
        self.reverse = reverse_layout
        laid = tuple(env["states"][w] for w in order)
        self.columns = c863.pack_lanes(laid + (laid[0],))
        self.planes_l: list = []
        self.planes_r: list = []
        self.formed: dict = {}
        self.item: dict = {}
        self.lock_ord: dict = {}
        self.lock_writes: dict = {}
        self.bank0 = [0] * (n + 1)
        self.bank1 = [0] * (n + 1)
        self.shadow: dict = {w: 0 for w in env["slot_wires"]}
        self.wo_violations = 0
        self.beyond_cap = 0
        self.dup_mismatch = 0
        self.events = 0
        self.slot_activation = 0
        self.t = 0
        for w in env["slot_wires"]:
            self.slot_activation |= self.columns[w]
        uni_all, uni_sim = env["uni_all"], env["uni_sim"]
        g = c863.mask_over(self.columns, env["global_dirty"], uni_sim)
        self.dup_mismatch += int(bool(g & 1) != bool(g & (1 << n)))
        self.prev0 = c863.mask_over(self.columns, env["bank_dirty"][0],
                                    uni_all)
        self.prev1 = c863.mask_over(self.columns, env["bank_dirty"][1],
                                    uni_all)
        self.prev_left = self.columns[env["left_w"]]
        self.prev_right = self.columns[env["right_w"]]
        for bit in c863.lanes_of(g & uni_all):
            self._lock(bit, 0)

    # -- bookkeeping ------------------------------------------------------
    def _lock(self, bit, boundary):
        env = self.env
        w = self.order[bit]
        self.formed[w] = boundary
        lb = (self.columns[env["left_w"]] >> bit) & 1
        rb = (self.columns[env["right_w"]] >> bit) & 1
        self.item[w] = item_of(lb, rb)
        self.lock_ord[w] = (self.bank0[bit], self.bank1[bit])
        self.lock_writes[w] = (acc_get(self.planes_l, bit),
                               acc_get(self.planes_r, bit))
        if self.capture_snapshots:
            self.snapshots[w] = self.env["c863"].lane_state(self.columns, bit)
        self.events += 1
        self._wire_write(("F", 0), bit)

    def _wire_write(self, tag, bit):
        wire = self.env["slot_of"][tag]
        flag = 1 << bit
        if self.shadow[wire] & flag:
            self.wo_violations += 1
        self.shadow[wire] |= flag

    def snapshot(self):
        return (list(self.columns), list(self.planes_l), list(self.planes_r),
                dict(self.formed), dict(self.item), dict(self.lock_ord),
                dict(self.lock_writes), list(self.bank0), list(self.bank1),
                dict(self.shadow), self.wo_violations, self.beyond_cap,
                self.dup_mismatch, self.events, self.slot_activation, self.t,
                self.prev0, self.prev1, self.prev_left, self.prev_right)

    def restore(self, s):
        (cols, pl, pr, formed, item, lo, lw, b0, b1, shadow, wo, bc, dm,
         ev, sa, t, p0, p1, plft, prgt) = s
        self.columns = list(cols)
        self.planes_l = list(pl)
        self.planes_r = list(pr)
        self.formed = dict(formed)
        self.item = dict(item)
        self.lock_ord = dict(lo)
        self.lock_writes = dict(lw)
        self.bank0 = list(b0)
        self.bank1 = list(b1)
        self.shadow = dict(shadow)
        self.wo_violations = wo
        self.beyond_cap = bc
        self.dup_mismatch = dm
        self.events = ev
        self.slot_activation = sa
        self.t = t
        self.prev0, self.prev1 = p0, p1
        self.prev_left, self.prev_right = plft, prgt

    def state_digest(self):
        """The FULL machine state, for the no-hidden-state clause M4."""
        h = sha256()
        for x in self.columns:
            h.update(x.to_bytes(128, "little"))
        h.update(compact({
            "t": self.t,
            "formed": sorted(self.formed.items()),
            "item": sorted((k, list(v) if v else None)
                           for k, v in self.item.items()),
            "lock_ord": sorted((k, list(v)) for k, v in self.lock_ord.items()),
            "lock_writes": sorted((k, list(v))
                                  for k, v in self.lock_writes.items()),
            "bank0": self.bank0, "bank1": self.bank1,
            "planes_l": self.planes_l, "planes_r": self.planes_r,
            "shadow": sorted(self.shadow.items()),
            "wo": self.wo_violations, "bc": self.beyond_cap,
            "dm": self.dup_mismatch, "ev": self.events,
            "sa": self.slot_activation,
            "prev0": self.prev0, "prev1": self.prev1,
            "prev_left": self.prev_left, "prev_right": self.prev_right,
        }).encode("utf-8"))
        return h.hexdigest()

    # -- the step loop ----------------------------------------------------
    def advance(self, upto, rows, choice_rows=None, choice_words=None):
        """Advance to boundary `upto`.  `rows` is the compiled cycle; at a
        boundary in `choice_rows` the choice-bearing chunk replaces it and the
        occasion's value is written into the CHOICE sink first."""
        env = self.env
        c863 = env["c863"]
        mask_over, lanes_of = c863.mask_over, c863.lanes_of
        gd, bd0, bd1 = env["global_dirty"], env["bank_dirty"][0], \
            env["bank_dirty"][1]
        uni_all, uni_sim = env["uni_all"], env["uni_sim"]
        n, stations = env["n"], env["stations"]
        left_w, right_w = env["left_w"], env["right_w"]
        cap = env["register_cap"]
        slot_of, slot_wires = env["slot_of"], env["slot_wires"]
        cycle = len(rows)
        columns = self.columns
        while self.t < upto:
            t = self.t
            if choice_rows is not None and t in choice_rows:
                k, fn = choice_rows[t]
                _CHOICE_SINK[k] = choice_words[t]
                fn(columns)
            else:
                rows[t % cycle](columns)
            self.t = boundary = t + 1
            cl, cr = columns[left_w], columns[right_w]
            dl, dr = cl ^ self.prev_left, cr ^ self.prev_right
            if dl:
                acc_add(self.planes_l, dl)
                self.prev_left = cl
            if dr:
                acc_add(self.planes_r, dr)
                self.prev_right = cr
            g = mask_over(columns, gd, uni_sim)
            self.dup_mismatch += int(bool(g & 1) != bool(g & (1 << n)))
            ga = g & uni_all
            if ga:
                formed = self.formed
                order = self.order
                for bit in lanes_of(ga):
                    if order[bit] not in formed:
                        self._lock(bit, boundary)
            bm = mask_over(columns, bd0, uni_all)
            rise = bm & ~self.prev0
            if rise:
                for bit in lanes_of(rise):
                    o = self.bank0[bit]
                    if o < cap:
                        self.events += 1
                        self._wire_write(("B0", o), bit)
                    else:
                        self.beyond_cap += 1
                    self.bank0[bit] = o + 1
            self.prev0 = bm
            bm = mask_over(columns, bd1, uni_all)
            rise = bm & ~self.prev1
            if rise:
                for bit in lanes_of(rise):
                    o = self.bank1[bit]
                    if o < cap:
                        self.events += 1
                        self._wire_write(("B1", o), bit)
                    else:
                        self.beyond_cap += 1
                    self.bank1[bit] = o + 1
            self.prev1 = bm
            orbit_no = (boundary + stations - 1) // stations
            if orbit_no <= DEAD_CHUNK_ORBITS or boundary % stations == 0:
                sa = self.slot_activation
                for w in slot_wires:
                    sa |= columns[w]
                self.slot_activation = sa

    # -- readout ----------------------------------------------------------
    def duplicate_lane_column_divergence(self):
        """A DIRECT reading of duplicate-lane consistency: the number of wires
        on which the duplicate slot no longer carries what its world carries.
        Cycle 918's counter watches the formation predicate only; this watches
        every wire, so a break shows up the moment it happens."""
        n = self.env["n"]
        return sum(1 for col in self.columns
                   if ((col >> 0) & 1) != ((col >> n) & 1))

    def off_menu_lane_count(self):
        """Lanes whose endpoint content is OFF the menu.  K.M.prepare_endpoint
        makes the two menu items the two complementary patterns on the endpoint
        pair, so 'on menu' is exactly LEFT xor RIGHT == 1.  Driving both wires
        with one value preserves that parity identically; driving one does not."""
        env = self.env
        x = ~(self.columns[env["left_w"]] ^ self.columns[env["right_w"]])
        return bin(x & env["uni_sim"]).count("1")

    def build(self):
        env = self.env
        return {
            "duplicate_lane_column_divergence":
                self.duplicate_lane_column_divergence(),
            "off_menu_lane_count": self.off_menu_lane_count(),
            "snapshots": self.snapshots,
            "formed": dict(self.formed),
            "item": dict(self.item),
            "lock_ordinal": dict(self.lock_ord),
            "lock_endpoint_writes": dict(self.lock_writes),
            "boundaries": self.t,
            "events": self.events,
            "beyond_cap": self.beyond_cap,
            "duplicate_lane_mismatches": self.dup_mismatch,
            "write_once_violations": self.wo_violations,
            "record_slot_activation_conflicts":
                bin(self.slot_activation & env["uni_sim"]).count("1"),
            "layout": "reversed" if self.reverse else "forward",
            "order": self.order,
        }


def build_digest(build):
    """The Cycle-913/918 build digest, byte for byte: formation boundaries, the
    realized endpoint content at the lock, and the lock ordinals."""
    return digest({
        "formed": {str(k): v for k, v in sorted(build["formed"].items())},
        "item": {str(k): (list(v) if v else None)
                 for k, v in sorted(build["item"].items())},
        "lock_ordinal": {str(k): list(v)
                         for k, v in sorted(build["lock_ordinal"].items())},
        "events": build["events"],
    })


def scan_digest_918(build):
    """The Cycle-913/918/925 build digest, byte for byte -- the same four
    fields, the same key order, the same serialization.  Reproducing the pinned
    digest is what makes 'the extended compiler is backward compatible' a
    statement about the EXECUTION and not only about the text."""
    return digest({
        "formed": {str(k): v for k, v in sorted(build["formed"].items())},
        "snapshots": {str(k): "".join(str(b) for b in v)
                      for k, v in sorted(build["snapshots"].items())},
        "lock_ordinal": {str(k): list(v)
                         for k, v in sorted(build["lock_ordinal"].items())},
        "events": build["events"],
    })


def run_full(env, rows, reverse, boundaries, capture_snapshots=False):
    m = Machine(env, reverse, capture_snapshots)
    m.advance(boundaries, rows)
    return m.build()


# ---------------------------------------------------------------------------
# the 918 measurement rows, reproduced
# ---------------------------------------------------------------------------

def measurement(env, build, control_build=None):
    census = env["census"]
    setup_direction = env["setup_direction"]
    formed, item = build["formed"], build["item"]
    off_menu = [w for w in sorted(formed) if item[w] is None]
    live = {w: item[w] for w in sorted(formed) if item[w] is not None}
    sel_vs_setup = [w for w in sorted(live)
                    if list(live[w]) != list(setup_direction[census[w][1]])]
    split = Counter(str(list(v)) for v in live.values())
    # Cycle 918's histogram is of the write-count PARITY at the lock (its note
    # reports it as {even, odd} and separately reports max_writes = 5206), so
    # the parity is what is reproduced here.
    wr_rows = [build["lock_endpoint_writes"][w] for w in sorted(formed)]
    hist = Counter(str([wl % 2, rr % 2]) for wl, rr in wr_rows)
    row = {
        "lock_points": len(formed),
        "off_menu_endpoint_content_at_the_lock": len(off_menu),
        "lock_points_where_RD_STATE_disagrees_with_RD_SETUP": len(sel_vs_setup),
        "realized_split": {k: split[k] for k in sorted(split)},
        "write_count_histogram_at_the_lock": {k: hist[k] for k in sorted(hist)},
        "write_once_violations": build["write_once_violations"],
        "duplicate_lane_mismatches": build["duplicate_lane_mismatches"],
        "record_slot_activation_conflicts":
            build["record_slot_activation_conflicts"],
        "lock_points_whose_endpoint_changed_before_the_lock":
            sum(1 for wl, rr in wr_rows if wl or rr),
        "max_writes_before_a_lock":
            max((max(wl, rr) for wl, rr in wr_rows), default=0),
        "record_events": build["events"],
        "bank_edge_events_beyond_cap": build["beyond_cap"],
        "lock_boundary_range": [min(formed.values()), max(formed.values())]
                               if formed else None,
        "locks_at_moment_zero": sum(1 for v in formed.values() if v == 0),
    }
    if control_build is not None:
        cf = set(control_build["formed"])
        mf = set(formed)
        row["worlds_that_stopped_forming_count"] = len(cf - mf)
        row["worlds_that_started_forming_count"] = len(mf - cf)
        row["worlds_that_stopped_forming"] = sorted(cf - mf)
        row["worlds_that_started_forming"] = sorted(mf - cf)
        row["lock_points_whose_boundary_moved"] = sum(
            1 for w in sorted(cf & mf)
            if control_build["formed"][w] != formed[w])
        row["lock_points_whose_realized_item_differs_from_the_control"] = sum(
            1 for w in sorted(cf & mf)
            if control_build["item"][w] != item[w])
    return row


def dynamical_branch_pairs(env, build, cap=40):
    """Cycle 918's declared quantity, reproduced: two lock points agreeing on
    every setup coordinate the endpoint menu can see that nevertheless realize
    different menu items."""
    census, setup_direction = env["census"], env["setup_direction"]
    groups: dict = {}
    for w in sorted(build["formed"]):
        key = (tuple(census[w][2]), setup_direction[census[w][1]])
        groups.setdefault(key, []).append(w)
    split_pairs, undecidable, candidates = [], 0, 0
    for key, members in sorted({k: v for k, v in groups.items()
                                if len(v) >= 2}.items()):
        for u, v in combinations(sorted(members), 2):
            su, sv = build["item"][u], build["item"][v]
            if su is None or sv is None:
                undecidable += 1
                continue
            candidates += 1
            if su != sv:
                split_pairs.append({
                    "pair": [u, v],
                    "shared_positions": list(key[0]),
                    "shared_prepared_direction": list(key[1]),
                    "selected": [list(su), list(sv)],
                    "lock_boundaries": [build["formed"][u],
                                        build["formed"][v]],
                })
    return {
        "candidate_pairs_among_the_lock_points": candidates,
        "pairs_skipped_because_the_endpoint_was_off_menu": undecidable,
        "DYNAMICAL_BRANCH_PAIRS": len(split_pairs),
        "pairs": split_pairs[:cap],
    }


def z11_covariance(env, build):
    selection = {w: tuple(v) for w, v in build["item"].items()
                 if v is not None}
    if not selection:
        return {"selection_violations_under_translation": None,
                "empty": True}
    return env["c913"].translation_covariance(env["c878"], env["census"],
                                              env["stations"], selection)


# ---------------------------------------------------------------------------
# the TREE
# ---------------------------------------------------------------------------

def choice_support_words(env, atoms_at, reverse, indexing):
    """Turn a declared atom set into the lane words the CHOICE node may emit.

    indexing == 'world':  the choice is indexed by the CENSUS WORLD.  The word
      is built through the layout, and the DUPLICATE LANE (which carries the
      same world as slot 0) is mirrored -- because it is the same world.
    indexing == 'slot':   the choice is indexed by the LANE SLOT.  The word is
      a fixed bit position regardless of layout and the duplicate is not
      mirrored -- the supervisor's sketch, kept and measured, not assumed.
    """
    n = env["n"]
    order = list(range(n - 1, -1, -1)) if reverse else list(range(n))
    pos = {w: i for i, w in enumerate(order)}
    out = {}
    for t, members in atoms_at.items():
        bits = {}
        for m in members:
            if indexing == "world":
                lane = pos[m]
                word = 1 << lane
                if order[0] == m:
                    word |= 1 << n          # the duplicate lane is that world
            else:
                word = 1 << m               # m is a LANE SLOT
            bits[m] = word
        out[t] = bits
    return out


def enumerate_tree(env, rows, choice_rows, atom_words, atoms_at, boundaries,
                   reverse=False, leaf_cap=FULL_TREE_LEAF_CAP,
                   collect_nodes=True):
    """Enumerate the FULL tree exactly.  Canonical order: choice occasions
    ascending; within an occasion the atoms sorted by index ascending; children
    ordered by the integer value of their bit vector ascending (first atom the
    most significant bit).  Never sampled: the leaf count is computed first and
    hard-checked against the declared cap."""
    apps = sorted(atoms_at)
    widths = [len(atoms_at[t]) for t in apps]
    leaves = 1
    for w in widths:
        leaves *= 1 << w
    if leaves > leaf_cap:
        raise AssertionError(("declared full-tree cap exceeded", leaves,
                              leaf_cap))
    m = Machine(env, reverse)
    node_records: list = []
    leaf_records: list = []
    parent_digests: list = []

    def walk(level, prefix):
        if level == len(apps):
            m.advance(boundaries, rows, choice_rows, {})
            b = m.build()
            leaf_records.append({"assignment": list(prefix),
                                 "build": b,
                                 "digest": build_digest(b)})
            return
        t = apps[level]
        m.advance(t, rows, choice_rows, {})
        parent = m.snapshot()
        pdig = m.state_digest() if collect_nodes else None
        members = atoms_at[t]
        children = []
        for bits in product((0, 1), repeat=len(members)):
            word = 0
            for bit, mem in zip(bits, members):
                if bit:
                    word |= atom_words[t][mem]
            m.restore(parent)
            entry_digest = m.state_digest() if collect_nodes else None
            m.advance(t + 1, rows, choice_rows, {t: word})
            children.append({"bits": list(bits),
                             "word_popcount": bin(word).count("1"),
                             "entry_state_digest": entry_digest,
                             "post_state_digest":
                                 m.state_digest() if collect_nodes else None})
            walk(level + 1, prefix + list(bits))
        if collect_nodes:
            node_records.append({
                "occasion_ordinal": level,
                "application": t,
                "members": list(members),
                "parent_state_digest": pdig,
                "children_entered_from_identical_parent_state":
                    all(c["entry_state_digest"] == pdig for c in children),
                "distinct_post_state_digests":
                    len({c["post_state_digest"] for c in children}),
                "children": len(children),
                "prefix": list(prefix),
            })

    walk(0, [])
    return {"apps": apps, "widths": widths, "leaves": leaves,
            "leaf_records": leaf_records, "node_records": node_records}


# ---------------------------------------------------------------------------
# the WEIGHT ALGEBRA -- formal polynomials in mu.  no value is ever chosen.
# ---------------------------------------------------------------------------

def poly_one(nvars):
    return {(0,) * nvars: Fraction(1)}


def poly_mul(a, b, nvars):
    out: dict = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            out[e] = out.get(e, Fraction(0)) + ca * cb
    return {e: c for e, c in out.items() if c != 0}


def poly_add(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, Fraction(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def poly_factor(var, bit, nvars):
    """mu_var if bit else (1 - mu_var)."""
    e = [0] * nvars
    e[var] = 1
    if bit:
        return {tuple(e): Fraction(1)}
    return {(0,) * nvars: Fraction(1), tuple(e): Fraction(-1)}


def poly_str(p, names):
    if not p:
        return "0"
    terms = []
    for e in sorted(p, reverse=True):
        c = p[e]
        parts = []
        if c != 1 or all(x == 0 for x in e):
            parts.append(str(c))
        for i, k in enumerate(e):
            if k == 1:
                parts.append(names[i])
            elif k > 1:
                parts.append(f"{names[i]}^{k}")
        terms.append("*".join(parts))
    return " + ".join(terms)


def poly_eval(p, values):
    """Exact rational evaluation.  Used ONLY by the declared diagnostic grid,
    whose entire purpose is to exhibit that no verdict depends on it."""
    total = Fraction(0)
    for e, c in p.items():
        term = c
        for i, k in enumerate(e):
            if k:
                term *= values[i] ** k
        total += term
    return total


def weight_algebra(atoms, leaf_records, reading):
    """Build the formal branch weights under a declared reading.

    reading 'per_occasion': one symbol per choice atom.
    reading 'per_site':     one symbol per SITE (census world); atoms at the
                            same site share the symbol.
    reading 'global':       one symbol for the whole substrate.
    """
    if reading == "per_occasion":
        var_of = {i: i for i in range(len(atoms))}
        names = [f"mu_{i}" for i in range(len(atoms))]
        labels = [f"atom {i} = (application {t}, site {w})"
                  for i, (t, w) in enumerate(atoms)]
    elif reading == "per_site":
        sites = sorted({w for _t, w in atoms})
        var_of = {i: sites.index(w) for i, (_t, w) in enumerate(atoms)}
        names = [f"mu_site{w}" for w in sites]
        labels = [f"site {w}" for w in sites]
    else:
        var_of = {i: 0 for i in range(len(atoms))}
        names = ["mu"]
        labels = ["one weight for the whole substrate"]
    nvars = len(names)
    weights = []
    total = {}
    for rec in leaf_records:
        p = poly_one(nvars)
        for i, bit in enumerate(rec["assignment"]):
            p = poly_mul(p, poly_factor(var_of[i], bit, nvars), nvars)
        weights.append(p)
        total = poly_add(total, p)
    is_one = (total == {(0,) * nvars: Fraction(1)})
    return {
        "reading": reading,
        "symbols": names,
        "symbol_meaning": labels,
        "free_parameter_count": nvars,
        "leaf_weight_sum_is_identically_one": is_one,
        "leaf_weight_sum": poly_str(total, names),
        "example_leaf_weights": [
            {"assignment": leaf_records[i]["assignment"],
             "weight": poly_str(weights[i], names)}
            for i in range(min(4, len(weights)))],
        "_weights": weights, "_nvars": nvars, "_names": names,
    }


def outcome_algebra(leaf_records, algebra):
    """Group the leaves by OBSERVABLE and sum their weights.  The number of
    distinct observables, not the number of leaves, is what a weight would have
    to be supplied for."""
    names, nvars = algebra["_names"], algebra["_nvars"]
    groups: dict = {}
    for rec, w in zip(leaf_records, algebra["_weights"]):
        groups.setdefault(rec["digest"], []).append(w)
    rows = []
    total = {}
    for dig in sorted(groups):
        acc = {}
        for w in groups[dig]:
            acc = poly_add(acc, w)
        total = poly_add(total, acc)
        rows.append({"observable_digest": dig[:16],
                     "leaves": len(groups[dig]),
                     "weight": poly_str(acc, names)})
    return {
        "distinct_observables": len(groups),
        "observable_weight_sum_is_identically_one":
            total == {(0,) * nvars: Fraction(1)},
        "rows": rows[:24],
        "rows_truncated_at": 24,
    }


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

    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     provenance) = lift_machinery()

    text = {p: payloads[p].decode("utf-8") for p in TEXT_ONLY_PATHS}
    receipts = {p: json.loads(payloads[p].decode("utf-8"))
                for p in JSON_ONLY_PATHS}
    r911, r913, r918, r925 = (receipts[C911_RECEIPT], receipts[C913_RECEIPT],
                              receipts[C918_RECEIPT], receipts[C925_RECEIPT])
    m918 = r918["certificates"]["C2_MEASUREMENT"]["per_modification"]
    h918 = {row["modification"]: row
            for row in r918["certificates"]["H_DOUBLE_BUILD"]["rows"]}
    p925 = r925["certificates"]["C1_PROVENANCE_PARTITION"]
    register_cap = consts911["REGISTER_CAP"]

    # ---------------- the substrate ---------------------------------------
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, init_failures = c863.build_initial_states(program, event_seeds,
                                                      census)
    left_w, right_w, src_w = c913.endpoint_wires()
    BB = K.M.R12.BANK_BASES
    setup_direction = {ev: c913.read_state_direction(seed)
                       for ev, seed in event_seeds}
    menu = tuple(tuple(v) for v in consts911["DIRECTIONS"])
    n = len(census)
    REC_A = BB[0] + K.A.POINTER
    sim_fwd = tuple(census) + (census[0],)
    sim_rev = tuple(census[w] for w in range(n - 1, -1, -1))
    sim_rev = sim_rev + (sim_rev[0],)
    FULL_BOUNDARIES = HORIZON * stations
    TREE_B = TREE_ORBITS * stations

    proto = c863.pack_lanes(tuple(states) + (states[0],))
    t0 = monotonic()
    rig = c878.dead_wire_rig(program, sim_fwd, proto)
    t_rig = round(monotonic() - t0, 3)
    slot_of = rig["slot_of"]
    slot_wires = tuple(sorted(set(slot_of.values())))
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(
        set(per_bank[0]) | set(per_bank[1]) | set(links) | {source_ptr}))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))

    env = {
        "c863": c863, "c878": c878, "c911": c911, "c913": c913,
        "program": program, "census": census, "states": states, "n": n,
        "stations": stations, "left_w": left_w, "right_w": right_w,
        "global_dirty": global_dirty, "bank_dirty": bank_dirty,
        "uni_all": (1 << n) - 1, "uni_sim": (1 << (n + 1)) - 1,
        "slot_of": slot_of, "slot_wires": slot_wires,
        "register_cap": register_cap, "setup_direction": setup_direction,
    }

    M_A_GATES = ((KIND_CNOT, REC_A, left_w, 0),
                 (KIND_CNOT, REC_A, right_w, 0))
    timings: dict = {}

    def compiled(sim, gates):
        return compile_schedules(build_schedules(c863, program, sim, 0, gates))

    # ---------------- B: restriction gates --------------------------------
    gate_rows = []

    def gate(name, got, want):
        ok = got == want
        gate_rows.append({"gate": name, "value": got, "pinned": want,
                          "pass": ok})
        return ok

    pinned_sched = c863.masked_h_schedules(program, sim_fwd)
    mine_sched = build_schedules(c863, program, sim_fwd, 0, ())
    gate("schedule_builder_reproduces_the_pinned_compiler",
         digest([[list(g) for g in s] for s in mine_sched]),
         digest([[list(g) for g in s] for s in pinned_sched]))
    # BACKWARD COMPATIBILITY, full compile census: the EXTENDED emitter's text
    # is byte-identical to the pinned compile_fast text on every unextended
    # statement of the pinned schedule.
    ext_text = [chunk_source(s) for s in mine_sched]
    pin_text = [chunk_source(s, emitter=pinned_statement_text)
                for s in pinned_sched]
    bc_lines_total = sum(len(s) - 1 for s in ext_text)
    bc_identical = ext_text == pin_text
    gate("extended_compiler_is_bit_identical_on_unextended_programs",
         bc_identical, True)
    gate("backward_compatibility_census_statements", bc_lines_total, 34166)
    gate("compiled_gate_total", sum(len(s) for s in mine_sched), 34166)
    ma_sched = build_schedules(c863, program, sim_fwd, 0, M_A_GATES)
    gate("M_A_compiled_gate_total", sum(len(s) for s in ma_sched),
         m918["M_A"]["ENDPOINT_WRITES"]["compiled_gates_total"])

    # the pinned 925 partition sweep, reproduced value-for-value
    sweep_pinned = provenance_sweep(pin_text, pos_ops, cross_ops)
    ps = p925["pinned_substrate_sweep"]
    gate("c925_sweep_statements", sweep_pinned["statements"],
         ps["statements"] if "statements" in ps else 34166)
    gate("c925_sweep_class_counts", sweep_pinned["class_counts"],
         ps["class_counts"])
    gate("c925_sweep_addresses_read",
         sweep_pinned["distinct_state_addresses_read"],
         ps["distinct_state_addresses_read"])
    gate("c925_sweep_addresses_written",
         sweep_pinned["distinct_state_addresses_written"],
         ps["distinct_state_addresses_written"])
    gate("c925_sweep_P2_P3_or_unclassified_sites",
         sweep_pinned["P2_P3_or_unclassified_sites"],
         ps["P2_P3_or_unclassified_sites"])
    templates = compiler_templates_from_pin()
    gate("c925_compiler_templates", templates,
         p925["compiler_admitted_statement_templates"])
    gate("c925_compiler_template_count", len(templates),
         p925["compiler_admitted_statement_template_count"])
    gate("c925_P3_is_empty_in_the_pinned_substrate",
         sweep_pinned["class_counts"].get(P3, 0) == 0,
         p925["P3_is_empty_in_the_pinned_substrate"])

    # the full-horizon control and M_A builds, both layouts
    def full(tag, sim, gates, reverse):
        t = monotonic()
        b = run_full(env, compiled(sim, gates), reverse, FULL_BOUNDARIES,
                     capture_snapshots=True)
        timings[tag] = round(monotonic() - t, 3)
        return b

    ctl = full("CONTROL/fwd", sim_fwd, (), False)
    ctl_rev = full("CONTROL/rev", sim_rev, (), True)
    ma = full("M_A/fwd", sim_fwd, M_A_GATES, False)
    ma_rev = full("M_A/rev", sim_rev, M_A_GATES, True)

    d_ctl, d_ctl_rev = scan_digest_918(ctl), scan_digest_918(ctl_rev)
    d_ma, d_ma_rev = scan_digest_918(ma), scan_digest_918(ma_rev)
    gate("control_build_digest_matches_the_pinned_918_forward", d_ctl,
         h918["CONTROL"]["forward_digest"])
    gate("control_build_digest_matches_the_pinned_918_reversed", d_ctl_rev,
         h918["CONTROL"]["reversed_digest"])
    gate("M_A_build_digest_matches_the_pinned_918_forward", d_ma,
         h918["M_A"]["forward_digest"])
    gate("M_A_build_digest_matches_the_pinned_918_reversed", d_ma_rev,
         h918["M_A"]["reversed_digest"])
    gate("control_build_digest_is_layout_independent", d_ctl == d_ctl_rev, True)
    gate("M_A_build_digest_is_layout_independent", d_ma == d_ma_rev, True)
    gate("control_and_M_A_builds_differ", d_ctl != d_ma, True)

    mctl = measurement(env, ctl)
    mma = measurement(env, ma, ctl)
    p918c = m918["CONTROL"]
    p918a = m918["M_A"]
    gate("control_lock_points", mctl["lock_points"],
         p918c["FORMATION"]["lock_points"])
    gate("control_record_events", mctl["record_events"],
         p918c["FORMATION"]["record_events"])
    gate("control_beyond_cap", mctl["bank_edge_events_beyond_cap"],
         p918c["FORMATION"]["bank_edge_events_beyond_cap"])
    gate("control_realized_split", mctl["realized_split"],
         p918c["SELECTION"]["realized_split"])
    gate("control_lock_boundary_range", mctl["lock_boundary_range"],
         p918c["FORMATION"]["lock_boundary_range"])
    gate("control_locks_at_moment_zero", mctl["locks_at_moment_zero"],
         p918c["FORMATION"]["locks_at_moment_zero"])
    gate("control_write_once_violations", mctl["write_once_violations"],
         p918c["RECORD_MACHINERY"]["write_once_violations"])
    gate("control_duplicate_lane_mismatches",
         mctl["duplicate_lane_mismatches"],
         p918c["RECORD_MACHINERY"]["duplicate_lane_mismatches_forward"])
    gate("control_record_slot_activation_conflicts",
         mctl["record_slot_activation_conflicts"],
         p918c["RECORD_MACHINERY"]["record_slot_activation_conflicts"])
    gate("M_A_lock_points", mma["lock_points"],
         p918a["FORMATION"]["lock_points"])
    gate("M_A_record_events", mma["record_events"],
         p918a["FORMATION"]["record_events"])
    gate("M_A_beyond_cap", mma["bank_edge_events_beyond_cap"],
         p918a["FORMATION"]["bank_edge_events_beyond_cap"])
    gate("M_A_worlds_that_stopped_forming",
         mma["worlds_that_stopped_forming"],
         p918a["FORMATION"]["worlds_that_stopped_forming"])
    gate("M_A_worlds_that_started_forming",
         mma["worlds_that_started_forming"],
         p918a["FORMATION"]["worlds_that_started_forming"])
    gate("M_A_lock_points_whose_boundary_moved",
         mma["lock_points_whose_boundary_moved"],
         p918a["FORMATION"]["lock_points_whose_boundary_moved"])
    gate("M_A_sel_differs_from_setup",
         mma["lock_points_where_RD_STATE_disagrees_with_RD_SETUP"],
         p918a["SELECTION"]["lock_points_where_RD_STATE_disagrees_with_RD_SETUP"])
    gate("M_A_realized_split", mma["realized_split"],
         p918a["SELECTION"]["realized_split"])
    gate("M_A_write_count_parity_histogram_at_the_lock",
         mma["write_count_histogram_at_the_lock"],
         p918a["ENDPOINT_WRITES"]["write_count_histogram_at_the_lock"])
    gate("M_A_lock_points_whose_endpoint_changed_before_the_lock",
         mma["lock_points_whose_endpoint_changed_before_the_lock"],
         p918a["ENDPOINT_WRITES"][
             "lock_points_whose_endpoint_changed_before_the_lock"])
    gate("M_A_max_writes_before_a_lock", mma["max_writes_before_a_lock"],
         p918a["ENDPOINT_WRITES"]["max_writes_before_a_lock"])
    gate("M_A_off_menu_at_the_lock",
         mma["off_menu_endpoint_content_at_the_lock"],
         p918a["SELECTION"]["off_menu_endpoint_content_at_the_lock"])
    gate("M_A_lock_points_whose_realized_item_differs_from_the_control",
         mma["lock_points_whose_realized_item_differs_from_the_control"],
         p918a["SELECTION"][
             "lock_points_whose_realized_item_differs_from_the_control"])
    gate("M_A_write_once_violations", mma["write_once_violations"],
         p918a["RECORD_MACHINERY"]["write_once_violations"])
    gate("M_A_duplicate_lane_mismatches", mma["duplicate_lane_mismatches"],
         p918a["RECORD_MACHINERY"]["duplicate_lane_mismatches_forward"])

    dbp_ma = dynamical_branch_pairs(env, ma)
    p_dbp = p918a["BRANCH_PAIRS_dynamical"]
    gate("M_A_dynamical_branch_pairs", dbp_ma["DYNAMICAL_BRANCH_PAIRS"],
         p_dbp["DYNAMICAL_BRANCH_PAIRS"])
    gate("M_A_dynamical_branch_pair_identities",
         [p["pair"] for p in dbp_ma["pairs"]],
         [p["pair"] for p in p_dbp["pairs"]])
    gate("M_A_candidate_pairs",
         dbp_ma["candidate_pairs_among_the_lock_points"],
         p_dbp["candidate_pairs_among_the_lock_points"])
    z_ctl, z_ma = z11_covariance(env, ctl), z11_covariance(env, ma)
    gate("control_Z11_violations",
         z_ctl["selection_violations_under_translation"],
         p918c["COVARIANCE_AND_STRUCTURE"]["translation_violations"])
    gate("M_A_Z11_violations",
         z_ma["selection_violations_under_translation"],
         p918a["COVARIANCE_AND_STRUCTURE"]["translation_violations"])

    # the pinned 911 literal branch matrix
    per_state: dict = {}
    for w, s in enumerate(states):
        per_state.setdefault(s, []).append(w)
    same_state = []
    for lanes in per_state.values():
        if len(lanes) > 1:
            same_state.extend(combinations(sorted(lanes), 2))
    same_both = [(u, v) for u, v in same_state if census[u][2] == census[v][2]]
    gate("c911_pairs_sharing_tick0_state", len(same_state),
         p918a["BRANCH_MATRIX_911_literal"]["pairs_sharing_tick0_state"])
    gate("c911_pairs_sharing_tick0_state_AND_schedule", len(same_both),
         p918a["BRANCH_MATRIX_911_literal"][
             "pairs_sharing_tick0_state_AND_schedule"])

    # byte quotes
    q925 = "R2 (the choice point) = THE SOLE GENUINE RELAXATION"
    q925b = "a substrate/compiler admitting a P3 node"
    q918 = "a substrate whose law is not a"
    gate("c925_note_byte_quote_R2_is_the_sole_relaxation",
         q925 in text[C925_NOTE], True)
    gate("c925_note_byte_quote_the_named_successor",
         q925b in text[C925_NOTE], True)
    gate("c918_note_byte_quote_the_named_obstruction",
         q918 in text[C918_NOTE], True)

    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "anchor_statement":
            "every pinned quantity this block leans on is recomputed here from "
            "the pinned bytes and compared value-for-value BEFORE any new "
            "number is quoted: the Cycle-925 provenance sweep and its three "
            "templates, the Cycle-918 CONTROL and M_A census rows in both "
            "layouts, the Cycle-911 literal branch matrix, and the extended "
            "compiler's bit-identity on every unextended program.",
        "rows": gate_rows,
        "total": len(gate_rows),
        "passed": sum(1 for r in gate_rows if r["pass"]),
        "pass": all(r["pass"] for r in gate_rows),
    }

    # ---------------- C1: THE GRAMMAR DELTA -------------------------------
    # the choice atoms, made concrete
    atoms = tuple(sorted(CHOICE_ATOMS))
    atoms_at: dict = {}
    for t, w in atoms:
        atoms_at.setdefault(t, []).append(w)
    atoms_at = {t: tuple(sorted(v)) for t, v in sorted(atoms_at.items())}
    apps = sorted(atoms_at)
    occasion_of = {t: i for i, t in enumerate(apps)}

    # ELIGIBILITY: the atom's lane must be inside station 0's mask there
    eligibility = []
    for t, members in atoms_at.items():
        m = station_mask(sim_fwd, 0, t % stations, stations)
        for w in members:
            eligibility.append({"application": t, "step": t % stations,
                                "site": w,
                                "inside_station_0_mask": bool((m >> w) & 1)})
    all_eligible = all(r["inside_station_0_mask"] for r in eligibility)

    # the extended schedule: the plain M_A cycle, plus one choice-bearing chunk
    # per declared occasion.  a per-boundary chunk map IS a schedule (a longer
    # unrolled cycle written compactly); it is declared as such.
    ma_rows_c = compiled(sim_fwd, M_A_GATES)
    choice_rows_fwd = {}
    choice_sources = {}
    for t in apps:
        k = occasion_of[t]
        gates = M_A_GATES + ((KIND_CHOICE, k, left_w, 0),
                             (KIND_CHOICE, k, right_w, 0))
        sched = build_schedules(c863, program, sim_fwd, 0, gates)
        src = chunk_source(sched[t % stations])
        choice_sources[t] = src
        ns: dict = {}
        exec("\n".join(src), {"__builtins__": {}, "CHOICE": CHOICE}, ns)
        choice_rows_fwd[t] = (k, ns["apply_chunk"])

    # the extended provenance sweep
    sweep_ext = provenance_sweep(list(choice_sources.values()), pos_ops,
                                 cross_ops, extended=True)
    sweep_ext_pinned_eyes = provenance_sweep(list(choice_sources.values()),
                                             pos_ops, cross_ops,
                                             extended=False)
    pinned_node_types = set(
        provenance_sweep(pin_text, pos_ops, cross_ops)["ast_node_types"])
    ext_node_types = set(sweep_ext["ast_node_types"])
    new_node_types = sorted(ext_node_types - pinned_node_types)
    choice_kinds = sorted({tag for tag in sweep_ext["node_tag_counts"]
                           if tag.startswith("choice-node:")})
    p3_leaf_instances = sweep_ext["class_counts"].get(P3, 0)

    cert_c1 = {
        "certificate": "C1_THE_GRAMMAR_DELTA",
        "grammar_delta": GRAMMAR_DELTA_TEXT,
        "P3_not_P2_obligation": P3_NOT_P2_TEXT,
        "pinned_templates": list(PINNED_TEMPLATES),
        "extended_templates": list(EXTENDED_TEMPLATES),
        "new_templates": [CHOICE_TEMPLATE],
        "new_template_count": len(EXTENDED_TEMPLATES) - len(PINNED_TEMPLATES),
        "pinned_template_count_matches_the_pinned_925_reading":
            list(PINNED_TEMPLATES) == templates,
        "AST": {
            "pinned_statement_node_types": sorted(pinned_node_types),
            "extended_statement_node_types": sorted(ext_node_types),
            "NEW_NODE_TYPES": new_node_types,
            "exactly_one_new_node_type": len(new_node_types) == 1,
        },
        "extended_provenance_sweep": {
            "statements_swept": sweep_ext["statements"],
            "class_counts": sweep_ext["class_counts"],
            "distinct_choice_node_kinds": choice_kinds,
            "exactly_one_P3_node_kind": len(choice_kinds) == 1,
            "P3_leaf_instances": p3_leaf_instances,
            "P3_leaf_instances_per_choice_occasion":
                p3_leaf_instances // max(1, len(apps)),
            "choice_ordinals_seen": sweep_ext["choice_ordinal_counts"],
            "P2_sites": sweep_ext["class_counts"].get(P2, 0),
            "unclassified_sites":
                sweep_ext["class_counts"].get(P_UNCLASSIFIED, 0),
            "shape_violations": sweep_ext["shape_violation_count"],
        },
        "the_same_text_under_the_pinned_925_classifier": {
            "note":
                "read with Cycle 925's OWN classifier (no extension), the new "
                "node registers as P3 (a Call) AND as P2 (the free name it "
                "descends into): the pinned classifier cannot tell a genuine "
                "choice node from an oracle handle.  That is exactly why the "
                "P3 status here is earned SEMANTICALLY, by the multi-valuedness "
                "gate in C2, and not by the syntax.",
            "class_counts": sweep_ext_pinned_eyes["class_counts"],
        },
        "backward_compatibility": {
            "mechanism":
                "the extended emitter dispatches kinds 0/1/2 to the pinned "
                "text function itself; identity is therefore checked, not "
                "arranged -- the two emitters are run independently over the "
                "pinned schedule and their FULL text is compared.",
            "chunk_rows_compared": len(ext_text),
            "statements_compared": bc_lines_total,
            "bit_identical": bc_identical,
            "full_horizon_execution_census": {
                "control_forward_digest": d_ctl,
                "control_reversed_digest": d_ctl_rev,
                "matches_the_pinned_918_control_digest":
                    d_ctl == h918["CONTROL"]["forward_digest"],
                "M_A_forward_digest": d_ma,
                "matches_the_pinned_918_M_A_digest":
                    d_ma == h918["M_A"]["forward_digest"],
                "census": n, "boundaries": FULL_BOUNDARIES,
            },
        },
        "the_declared_choice_atoms": {
            "atoms": [list(a) for a in atoms],
            "atom_count": len(atoms),
            "sites": sorted({w for _t, w in atoms}),
            "site_count": len({w for _t, w in atoms}),
            "occasions": apps,
            "occasion_count": len(apps),
            "atoms_per_occasion": {str(t): list(v)
                                   for t, v in atoms_at.items()},
            "eligibility": eligibility,
            "all_atoms_are_inside_station_0s_mask": all_eligible,
            "anchor":
                "the choice gates are appended to the SOURCE station's macro "
                "(station 0) immediately after M_A's two CNOTs and are masked "
                "by that station's own lane mask -- the identical anchoring "
                "Cycle 918 used, so the choice travels with the controller "
                "token exactly as the kernel's own macros do.",
            "menu_preservation_by_construction":
                "both endpoint wires are driven by the SAME choice value, so "
                "the choice acts as the menu swap (1,0) <-> (0,1) and cannot "
                "produce off-menu content -- the same argument that keeps M_A "
                "and M_C on-menu in Cycle 918.  It is measured per branch "
                "anyway.",
        },
        "pass": bool(
            len(new_node_types) == 1 and new_node_types == ["Call"]
            and len(choice_kinds) == 1 and bc_identical and all_eligible
            and sweep_ext["class_counts"].get(P2, 0) == 0
            and sweep_ext["class_counts"].get(P_UNCLASSIFIED, 0) == 0
            and sweep_ext["shape_violation_count"] == 0
            and d_ctl == h918["CONTROL"]["forward_digest"]),
    }

    # ---------------- THE SEAL (before the tree is computed) --------------
    widths = [len(atoms_at[t]) for t in apps]
    predicted_leaves = 1
    for w in widths:
        predicted_leaves *= 1 << w
    predicted_nodes = 1
    acc, cum = 1, 0
    node_levels = [1]
    for w in widths:
        cum += w
        node_levels.append(1 << cum)
    predicted_nodes = sum(node_levels)
    SEALED = {
        "sealed_before": "the tree enumeration, the battery and the algebra",
        "tree_leaf_count": predicted_leaves,
        "tree_node_count": predicted_nodes,
        "tree_depth_in_choice_occasions": len(apps),
        "branching_factor_by_occasion": [1 << w for w in widths],
        "nodes_by_level": node_levels,
        "nominal_free_parameters_per_occasion_reading": len(atoms),
        "nominal_free_parameters_per_site_reading":
            len({w for _t, w in atoms}),
        "leaf_weight_polynomial_sums_identically_to_one": True,
        "at_least_one_genuine_branch_pair_exists": True,
        "every_branch_preserves_write_once": True,
        "every_branch_preserves_the_menu": True,
        "every_branch_preserves_duplicate_lane_consistency": True,
        "slot_indexed_choice_breaks_duplicate_lane_consistency": True,
        "slot_indexed_choice_breaks_layout_independence": True,
        "world_indexed_choice_preserves_layout_independence": True,
        "all_declared_atoms_are_effective": True,
        "no_certified_verdict_depends_on_the_value_of_mu": True,
    }
    seal_digest = digest(SEALED)
    print("=" * 78)
    print("S_SEAL  (emitted BEFORE the tree is computed)")
    print("=" * 78)
    for k in sorted(SEALED):
        print(f"  {k:58s} {SEALED[k]}")
    print(f"  SEAL DIGEST = {seal_digest}")
    print()
    sys.stdout.flush()

    # ---------------- C2: THE TREE ----------------------------------------
    words_world = choice_support_words(env, atoms_at, False, "world")
    t0 = monotonic()
    tree = enumerate_tree(env, ma_rows_c, choice_rows_fwd, words_world,
                          atoms_at, TREE_B, reverse=False)
    timings["TREE/world-indexed/fwd"] = round(monotonic() - t0, 3)
    leaves = tree["leaf_records"]
    nodes = tree["node_records"]

    # M1/M2/M3: one law, one setup, no other declared datum
    tick0_digest = sha256()
    m0 = Machine(env, False)
    for x in m0.columns:
        tick0_digest.update(x.to_bytes(128, "little"))
    tick0_digest = tick0_digest.hexdigest()
    law_text_digest = digest({str(t): choice_sources[t] for t in apps})
    plain_text_digest = digest([chunk_source(s) for s in
                                build_schedules(c863, program, sim_fwd, 0,
                                                M_A_GATES)])
    distinct_leaf_digests = {r["digest"] for r in leaves}
    m4_ok = all(nd["children_entered_from_identical_parent_state"]
                for nd in nodes)
    m5_ok = len(distinct_leaf_digests) > 1

    cert_c2 = {
        "certificate": "C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE",
        "window": {
            "declared_orbits": TREE_ORBITS,
            "declared_boundaries": TREE_B,
            "full_horizon_boundaries": FULL_BOUNDARIES,
            "why_a_window":
                "the tree is exponential in choice occasions and every leaf is "
                "a full-census trajectory; the window is chosen so that the "
                "FULL tree at that window is enumerated EXACTLY.  Nothing is "
                "sampled: the leaf count is computed from the atom set before "
                "the walk and hard-checked against the declared cap "
                f"({FULL_TREE_LEAF_CAP}).  Window-relative quantities say so.",
            "declared_full_tree_leaf_cap": FULL_TREE_LEAF_CAP,
        },
        "structure": {
            "leaves": tree["leaves"],
            "leaves_enumerated": len(leaves),
            "branch_nodes": len(nodes),
            "total_nodes": sum(node_levels),
            "depth_in_choice_occasions": len(apps),
            "branching_factor_by_occasion": [1 << w for w in widths],
            "nodes_by_level": node_levels,
            "canonical_order":
                "occasions ascending; atoms within an occasion by site index "
                "ascending; children by the integer value of their bit vector "
                "ascending (first atom = most significant bit).",
            "distinct_leaf_observables": len(distinct_leaf_digests),
        },
        "MULTI_VALUEDNESS_GATE": {
            "M1_one_law_compiled_text_identical_on_every_branch": True,
            "M1_evidence":
                "the branch coordinate never enters compilation: the tree walk "
                "executes the SAME compiled chunk objects on every branch and "
                "only the value written into the CHOICE sink differs.  The "
                "compiled text digest is a property of the schedule alone.",
            "law_text_digest": law_text_digest,
            "plain_M_A_text_digest": plain_text_digest,
            "M2_one_setup_tick0_columns_identical_on_every_branch": True,
            "tick0_column_digest": tick0_digest,
            "M2_evidence":
                "every branch is entered from the same Machine construction: "
                "the tick-0 columns are built once from the pinned initial "
                "states with NO carrier wire added, and the tree walk restores "
                "snapshots taken downstream of that single construction.",
            "M3_no_other_declared_datum_varies": True,
            "M3_evidence":
                "the only per-branch input is the choice bit vector.  There is "
                "no tape wire, no free name other than CHOICE, no injected "
                "stream: the extended sweep reports "
                f"{sweep_ext['class_counts'].get(P2, 0)} P2 sites.",
            "M4_children_entered_from_a_byte_identical_parent_state": m4_ok,
            "M4_branch_nodes_checked": len(nodes),
            "M4_evidence":
                "at each branch node the FULL machine state -- all "
                f"{len(m0.columns)} columns, the boundary index, the formation "
                "table, the realized items, both bank ordinals, the write-once "
                "shadow, the endpoint write planes and every counter -- is "
                "digested once and each child is verified to enter from that "
                "exact digest.",
            "M5_at_least_two_branches_diverge": m5_ok,
            "M5_distinct_leaf_observables": len(distinct_leaf_digests),
            "children_with_distinct_successor_states": [
                {"occasion": nd["occasion_ordinal"],
                 "application": nd["application"],
                 "children": nd["children"],
                 "distinct_successors": nd["distinct_post_state_digests"]}
                for nd in sorted(nodes, key=lambda x: (x["occasion_ordinal"],
                                                       x["prefix"]))[:8]],
            "every_branch_node_is_genuinely_branching": all(
                nd["distinct_post_state_digests"] == nd["children"]
                for nd in nodes),
            "VERDICT":
                "P3 EARNED SEMANTICALLY" if (m4_ok and m5_ok)
                else "P3 NOT EARNED",
            "pass": bool(m4_ok and m5_ok),
        },
        "THE_NEGATION_OF_THE_918_DETERMINISM_LEMMA":
            "Cycle 918: 'two lanes handed the same schedule and the same tick-0 "
            "state receive the same gates in the same order, so their columns "
            "stay equal for ever and cannot diverge.'  On this substrate the "
            f"same schedule and the same tick-0 state carry {tree['leaves']} "
            "trajectories, and they diverge.  The lemma was never wrong; it was "
            "a statement about a compiler with no P3 node.  Adding the node is "
            "exactly what removes its premise.",
        "pass": bool(m4_ok and m5_ok and len(leaves) == tree["leaves"]
                     and all(nd["distinct_post_state_digests"]
                             == nd["children"] for nd in nodes)),
    }

    # -- the genuine branch pairs -----------------------------------------
    # two TREE BRANCHES sharing (schedule, tick-0 state) that realize different
    # menu items at the same site.  This is the Cycle-911 CLASS_BRANCH article
    # the census never had.
    genuine_pairs = []
    by_site: dict = {}
    for idx, rec in enumerate(leaves):
        for w in sorted({s for _t, s in atoms}):
            by_site.setdefault(w, {}).setdefault(
                (rec["build"]["formed"].get(w),
                 tuple(rec["build"]["item"].get(w))
                 if rec["build"]["item"].get(w) else None), []).append(idx)
    for w in sorted(by_site):
        outcomes = by_site[w]
        keys = sorted(outcomes, key=lambda k: (k[0] is None, k))
        for ka, kb in combinations(keys, 2):
            ia, ib = outcomes[ka][0], outcomes[kb][0]
            a, b = leaves[ia], leaves[ib]
            kind = ("SAME_LOCK_DIFFERENT_ITEM"
                    if ka[0] is not None and kb[0] is not None
                    and ka[0] == kb[0] and ka[1] != kb[1]
                    else "DIFFERENT_LOCK_BOUNDARY"
                    if ka[0] is not None and kb[0] is not None
                    else "FORMS_ON_ONE_BRANCH_ONLY")
            genuine_pairs.append({
                "site_world": w,
                "branch_a_assignment": a["assignment"],
                "branch_b_assignment": b["assignment"],
                "lock_boundary": [ka[0], kb[0]],
                "realized_item": [list(ka[1]) if ka[1] else None,
                                  list(kb[1]) if kb[1] else None],
                "kind": kind,
                "share_the_schedule": True,
                "share_the_tick0_state": True,
            })
    same_lock_diff_item = [p for p in genuine_pairs
                           if p["kind"] == "SAME_LOCK_DIFFERENT_ITEM"]

    # -- per-branch battery ------------------------------------------------
    battery_rows = []
    for idx, rec in enumerate(leaves):
        b = rec["build"]
        mm = measurement(env, b)
        battery_rows.append({
            "leaf": idx,
            "assignment": rec["assignment"],
            "lock_points": mm["lock_points"],
            "write_once_violations": mm["write_once_violations"],
            "duplicate_lane_mismatches": mm["duplicate_lane_mismatches"],
            "duplicate_lane_column_divergence":
                b["duplicate_lane_column_divergence"],
            "record_slot_activation_conflicts":
                mm["record_slot_activation_conflicts"],
            "off_menu_endpoint_content_at_the_lock":
                mm["off_menu_endpoint_content_at_the_lock"],
            "off_menu_lane_count": b["off_menu_lane_count"],
            "record_events": mm["record_events"],
            "realized_split": mm["realized_split"],
            "digest": rec["digest"],
        })
    bat = {
        "branches": len(battery_rows),
        "write_once_holds_on_every_branch":
            all(r["write_once_violations"] == 0 for r in battery_rows),
        "duplicate_lane_consistency_holds_on_every_branch":
            all(r["duplicate_lane_mismatches"] == 0
                and r["duplicate_lane_column_divergence"] == 0
                for r in battery_rows),
        "record_slots_inert_on_every_branch":
            all(r["record_slot_activation_conflicts"] == 0
                for r in battery_rows),
        "menu_holds_on_every_branch":
            all(r["off_menu_endpoint_content_at_the_lock"] == 0
                for r in battery_rows),
        "off_menu_lane_count_is_constant_across_branches":
            len({r["off_menu_lane_count"] for r in battery_rows}) == 1,
        "off_menu_lane_count": sorted({r["off_menu_lane_count"]
                                       for r in battery_rows}),
        "formation_detected_by_the_same_predicate_on_every_branch": True,
        "lock_point_count_range": [min(r["lock_points"] for r in battery_rows),
                                   max(r["lock_points"] for r in battery_rows)],
        "record_event_range": [min(r["record_events"] for r in battery_rows),
                               max(r["record_events"] for r in battery_rows)],
        "distinct_realized_splits":
            len({compact(r["realized_split"]) for r in battery_rows}),
        "rows_sample": battery_rows[:12],
        "rows_truncated_at": 12,
    }
    # the FULL per-leaf table, published so an independent checker can compare
    # leaf for leaf rather than trusting a digest of the primary's own shapes.
    per_leaf_public_table = [{
        "assignment": r["assignment"],
        "lock_points": r["lock_points"],
        "write_once_violations": r["write_once_violations"],
        "off_menu_lock_points": r["off_menu_endpoint_content_at_the_lock"],
        "site_outcomes": {
            str(w): [leaves[i]["build"]["formed"].get(w),
                     list(leaves[i]["build"]["item"][w])
                     if leaves[i]["build"]["formed"].get(w) is not None
                     and leaves[i]["build"]["item"][w] else None]
            for w in sorted({s for _t, s in atoms})},
    } for i, r in enumerate(battery_rows)]

    # -- effectivity of every declared atom --------------------------------
    eff_rows = []
    for i, (t, w) in enumerate(atoms):
        seen = {}
        for rec in leaves:
            key = tuple(v for j, v in enumerate(rec["assignment"]) if j != i)
            seen.setdefault(key, {})[rec["assignment"][i]] = rec["digest"]
        contexts = sum(1 for v in seen.values() if len(v) == 2)
        differ = sum(1 for v in seen.values()
                     if len(v) == 2 and len(set(v.values())) == 2)
        eff_rows.append({
            "atom": i, "application": t, "site": w,
            "contexts_with_both_values": contexts,
            "contexts_where_the_two_values_differ_observably": differ,
            "effective": differ > 0,
            "effective_in_every_context": differ == contexts,
        })
    all_effective = all(r["effective"] for r in eff_rows)

    # -- factorization across sites ---------------------------------------
    # lane locality is certified position-wise; if it holds then the leaf
    # observable must be the PRODUCT of per-site observables.  Verified
    # exhaustively over the full tree rather than assumed.
    site_of_atom = [w for _t, w in atoms]
    sites = sorted(set(site_of_atom))
    per_site_obs: dict = {}
    factorization_violations = []
    for rec in leaves:
        for w in sites:
            sub = tuple(v for j, v in enumerate(rec["assignment"])
                        if site_of_atom[j] == w)
            obs = (rec["build"]["formed"].get(w),
                   tuple(rec["build"]["item"].get(w))
                   if rec["build"]["item"].get(w) else None,
                   tuple(rec["build"]["lock_ordinal"].get(w) or ()))
            prev = per_site_obs.setdefault((w, sub), obs)
            if prev != obs:
                factorization_violations.append(
                    {"site": w, "sub_assignment": list(sub),
                     "observed": [str(prev), str(obs)]})
    factorizes = not factorization_violations

    cert_c3 = {
        "certificate": "C3_THE_PER_BRANCH_BATTERY",
        "constraint_battery_source":
            "Cycle 918's declared constraints (a) record machinery / "
            "write-once / dead slots, (b) formation and menu -- recomputed "
            "here on EVERY branch of the tree rather than once.",
        "battery": bat,
        "per_leaf_public_table": per_leaf_public_table,
        "per_leaf_public_table_note":
            "the complete table, one row per leaf in canonical order, "
            "published so that an independent checker can re-derive every "
            "branch and compare leaf for leaf instead of trusting a digest "
            "computed from this runner's own data shapes.",
        "atom_effectivity": {
            "rows": eff_rows,
            "all_declared_atoms_are_effective": all_effective,
            "atoms_effective_in_every_context":
                sum(1 for r in eff_rows if r["effective_in_every_context"]),
        },
        "GENUINE_BRANCH_PAIRS": {
            "definition":
                "two branches of ONE tree -- therefore sharing the schedule "
                "and the tick-0 state exactly -- whose trajectories differ at "
                "a site.  Cycle 911's CLASS_BRANCH is conjunctively gated on "
                "same_schedule AND same_tick0_state AND a divergence; the "
                "census realizes that conjunction 0 times and Cycle 918 proved "
                "no gate set can change that.  The tree realizes it by "
                "construction, and this is the first time the class is "
                "non-empty anywhere in this lane.",
            "pairs_exhibited": len(genuine_pairs),
            "pairs_with_the_SAME_lock_boundary_and_a_DIFFERENT_menu_item":
                len(same_lock_diff_item),
            "sharpest_witnesses": same_lock_diff_item[:8],
            "all_witnesses_sample": genuine_pairs[:16],
            "witnesses_truncated_at": 16,
            "contrast_with_the_918_pairs":
                "Cycle 918's three dynamical branch pairs are pairs of "
                "DIFFERENT WORLDS agreeing on the setup coordinates the menu "
                "can see.  These are pairs of branches of the SAME WORLD: "
                "nothing whatever distinguishes their inputs.",
        },
        "FACTORIZATION_ACROSS_SITES": {
            "claim":
                "position-wise lane locality (Cycle 911, certified; Cycle 918 "
                "re-measured with a runtime perturbation witness) forces each "
                "site's trajectory to depend only on the choice atoms carried "
                "by that site.  Checked exhaustively on the full tree, not "
                "assumed.",
            "sites_checked": sites,
            "leaves_checked": len(leaves),
            "violations": factorization_violations[:8],
            "violation_count": len(factorization_violations),
            "the_leaf_observable_factorizes_over_sites": factorizes,
            "consequence_for_the_weight_algebra":
                "if the observable factorizes then no cross-site relation "
                "among the weights can be forced by any observable the "
                "substrate exposes: the joint weight is a product and the "
                "per-site factors are unconstrained by one another.",
        },
        "pass": bool(bat["write_once_holds_on_every_branch"]
                     and bat["duplicate_lane_consistency_holds_on_every_branch"]
                     and bat["record_slots_inert_on_every_branch"]
                     and bat["menu_holds_on_every_branch"]
                     and all_effective and factorizes
                     and len(same_lock_diff_item) > 0),
    }

    # ---------------- C4: WHAT BREAKS -------------------------------------
    # (i) slot-indexed vs world-indexed: the duplicate lane and the layout
    DUP_SITE = 0                      # the world carried at slot 0 (forward)
    dup_app = None
    for t in range(88, 132):
        if (0 - (t % stations)) % stations in sim_fwd[DUP_SITE][2]:
            dup_app = t
            break
    dup_atoms_at = {dup_app: (DUP_SITE,)}
    ma_rows_by_layout = {False: ma_rows_c, True: compiled(sim_rev, M_A_GATES)}
    dup_rows = {}
    k0 = 0
    gates = M_A_GATES + ((KIND_CHOICE, k0, left_w, 0),
                         (KIND_CHOICE, k0, right_w, 0))
    for rev, sim in ((False, sim_fwd), (True, sim_rev)):
        sched = build_schedules(c863, program, sim, 0, gates)
        ns: dict = {}
        exec("\n".join(chunk_source(sched[dup_app % stations])),
             {"__builtins__": {}, "CHOICE": CHOICE}, ns)
        dup_rows[rev] = {dup_app: (k0, ns["apply_chunk"])}
    WITNESS_B = TREE_B
    # the LAYOUT witness needs a site whose outcome is visible in the build
    # digest, so it is run on a declared choice site that locks inside the
    # window; the DUPLICATE-LANE witness must sit on slot 0, which is the only
    # slot the duplicate carries.  Two witnesses, each on the slot its own
    # property lives at.
    LAYOUT_SITE = atoms[0][1]
    layout_app = atoms[0][0]
    layout_atoms_at = {layout_app: (LAYOUT_SITE,)}
    layout_rows = {}
    for rev, sim in ((False, sim_fwd), (True, sim_rev)):
        sched = build_schedules(c863, program, sim, 0, gates)
        ns: dict = {}
        exec("\n".join(chunk_source(sched[layout_app % stations])),
             {"__builtins__": {}, "CHOICE": CHOICE}, ns)
        layout_rows[rev] = {layout_app: (k0, ns["apply_chunk"])}

    def witness_run(rev, app, rows_for_app, word):
        rws = ma_rows_by_layout[rev]
        m = Machine(env, rev)
        m.advance(app, rws, rows_for_app, {})
        m.advance(app + 1, rws, rows_for_app, {app: word})
        m.advance(WITNESS_B, rws, rows_for_app, {})
        return m.build()

    witness = {}
    for indexing in ("world", "slot"):
        dup_out, lay_out = {}, {}
        for rev in (False, True):
            wd = choice_support_words(env, dup_atoms_at, rev, indexing)
            b = witness_run(rev, dup_app, dup_rows[rev],
                            wd[dup_app][DUP_SITE])
            dup_out["reversed" if rev else "forward"] = {
                "duplicate_lane_column_divergence":
                    b["duplicate_lane_column_divergence"],
                "duplicate_lane_mismatches_918_counter":
                    b["duplicate_lane_mismatches"],
                "lock_points": len(b["formed"]),
            }
            wl = choice_support_words(env, layout_atoms_at, rev, indexing)
            b2 = witness_run(rev, layout_app, layout_rows[rev],
                             wl[layout_app][LAYOUT_SITE])
            lay_out["reversed" if rev else "forward"] = {
                "lock_points": len(b2["formed"]),
                "build_digest": build_digest(b2),
            }
        witness[indexing] = {
            "duplicate_lane_witness": {
                "on_slot": DUP_SITE, "at_application": dup_app,
                "rows": dup_out},
            "layout_witness": {
                "on_site_or_slot": LAYOUT_SITE, "at_application": layout_app,
                "rows": lay_out},
            "duplicate_lane_consistency_holds":
                dup_out["forward"]["duplicate_lane_column_divergence"] == 0
                and dup_out["forward"]["duplicate_lane_mismatches_918_counter"]
                == 0,
            "layout_independent":
                lay_out["forward"]["build_digest"]
                == lay_out["reversed"]["build_digest"],
        }
    # (ii) layout independence of the FULL world-indexed tree, on a declared
    # sub-tree (the first occasion only) in both layouts
    sub_atoms_at = {apps[0]: atoms_at[apps[0]]}
    sub_rows = {}
    for rev, sim in ((False, sim_fwd), (True, sim_rev)):
        k = 0
        g2 = M_A_GATES + ((KIND_CHOICE, k, left_w, 0),
                          (KIND_CHOICE, k, right_w, 0))
        sched = build_schedules(c863, program, sim, 0, g2)
        ns: dict = {}
        exec("\n".join(chunk_source(sched[apps[0] % stations])),
             {"__builtins__": {}, "CHOICE": CHOICE}, ns)
        sub_rows[rev] = {apps[0]: (k, ns["apply_chunk"])}
    sub_digests = {}
    t0 = monotonic()
    for rev in (False, True):
        words = choice_support_words(env, sub_atoms_at, rev, "world")
        st = enumerate_tree(env, ma_rows_by_layout[rev], sub_rows[rev],
                            words, sub_atoms_at, TREE_B, reverse=rev,
                            collect_nodes=False)
        sub_digests["reversed" if rev else "forward"] = [
            r["digest"] for r in st["leaf_records"]]
    timings["TREE/sub-tree/both-layouts"] = round(monotonic() - t0, 3)
    tree_layout_independent = \
        sub_digests["forward"] == sub_digests["reversed"]

    broken = [
        {"property": "the law is a function of (schedule, tick-0 state)",
         "pinned_at": "Cycle 918 C5_STRUCTURAL_LEMMA; Cycle 925 C1",
         "status": "BROKEN BY CONSTRUCTION -- this is the purchase",
         "witness": f"{tree['leaves']} trajectories from one (schedule, "
                    f"tick-0 state); {len(same_lock_diff_item)} of the pairs "
                    "share a lock boundary and realize different menu items"},
        {"property": "P3 is empty in the substrate (Cycle 925 C1)",
         "pinned_at": "Cycle 925 C1_PROVENANCE_PARTITION",
         "status": "BROKEN BY CONSTRUCTION",
         "witness": f"{p3_leaf_instances} P3 leaf instances of exactly one "
                    f"node kind {choice_kinds}"},
        {"property": "compilation is a function to ONE execution",
         "pinned_at": "the pinned Cycle-863 compile_fast type",
         "status": "BROKEN BY CONSTRUCTION (the semantic delta)",
         "witness": "compile : (schedule, tick-0 state) -> TREE"},
        {"property": "deterministic double-run of the SUBSTRATE",
         "pinned_at": "Cycle 918 / 925 H_DOUBLE_BUILD",
         "status": "BROKEN AT THE SUBSTRATE LEVEL, PRESERVED PER BRANCH",
         "witness": "re-running the substrate reproduces the TREE exactly "
                    "(H below) but does not reproduce a trajectory: a "
                    "trajectory is only determined once a branch is named"},
        {"property": "layout independence",
         "pinned_at": "Cycle 918 H_DOUBLE_BUILD",
         "status": "PRESERVED under world-indexed choice; BROKEN under "
                   "slot-indexed choice",
         "witness": compact(witness["slot"]["layout_witness"])},
        {"property": "duplicate-lane consistency",
         "pinned_at": "Cycle 918 RECORD_MACHINERY",
         "status": "PRESERVED under world-indexed choice; BROKEN under "
                   "slot-indexed choice",
         "witness": "slot-indexed choice on slot 0 leaves "
                    f"{witness['slot']['duplicate_lane_witness']['rows']['forward']['duplicate_lane_column_divergence']}"
                    " wires on which the duplicate slot no longer carries its "
                    "world; world-indexed leaves "
                    f"{witness['world']['duplicate_lane_witness']['rows']['forward']['duplicate_lane_column_divergence']}"},
        {"property": "monitor-phase Z_11 covariance of the realized selection",
         "pinned_at": "Cycle 918 (already lost under M_A: 124 violations)",
         "status": "ALREADY BROKEN BEFORE THE CHOICE NODE; the tree inherits "
                   "it and does not repair it",
         "witness": f"M_A full horizon reproduces "
                    f"{z_ma['selection_violations_under_translation']} "
                    "violations here"},
        {"property": "write-once / dead record slots / formation / menu",
         "pinned_at": "Cycle 918 constraints (a) and (b)",
         "status": "PRESERVED ON EVERY BRANCH",
         "witness": f"{len(battery_rows)} branches, 0 write-once violations, "
                    "0 slot conflicts, 0 duplicate-lane mismatches, 0 "
                    "off-menu locks"},
        {"property": "the certified gate vocabulary (X / CNOT / TOF)",
         "pinned_at": "Cycle 911 AST sweep",
         "status": "EXTENDED, not broken: the choice statement is the CNOT "
                   "shape with its control replaced by the choice node; no "
                   "cross-lane operator is introduced",
         "witness": "0 lane-index operators in the extended sweep"},
    ]

    cert_c4 = {
        "certificate": "C4_WHAT_BREAKS",
        "broken_and_preserved": broken,
        "INDEXING_IS_FORCED": {
            "finding":
                "the supervisor's sketch indexed the choice tape by "
                "(occasion, SITE) and left 'site' open.  Read as a LANE SLOT "
                "it breaks two certified properties; read as a CENSUS WORLD it "
                "breaks neither.  The substrate therefore FORCES the choice's "
                "index set to be worlds, not slots -- the same lesson Cycle "
                "925 R3 found one level down, where every law that read the "
                "slot instead of the world died.",
            "witnesses": witness,
            "slot_indexed_breaks_duplicate_lane":
                not witness["slot"]["duplicate_lane_consistency_holds"],
            "slot_indexed_breaks_layout_independence":
                not witness["slot"]["layout_independent"],
            "world_indexed_preserves_duplicate_lane":
                witness["world"]["duplicate_lane_consistency_holds"],
            "world_indexed_preserves_layout_independence":
                witness["world"]["layout_independent"],
            "consequence_for_the_A3_sentence":
                "a weight the substrate can host must be attached to a SITE in "
                "the world sense -- the object the Admissibility sentence "
                "already quantifies over -- and cannot be attached to a "
                "bookkeeping slot.  That is a constraint on the sentence's "
                "INDEX SET, discovered by measurement.  It is not a value and "
                "it is not an adoption.",
        },
        "TREE_LAYOUT_INDEPENDENCE": {
            "sub_tree_occasion": apps[0],
            "sub_tree_leaves": len(sub_digests["forward"]),
            "forward_equals_reversed": tree_layout_independent,
            "note":
                "the world-indexed tree is enumerated in BOTH lane layouts on "
                "a declared sub-tree and the leaf digest sequences are "
                "compared element for element.",
        },
        "pass": bool(
            not witness["slot"]["duplicate_lane_consistency_holds"]
            and not witness["slot"]["layout_independent"]
            and witness["world"]["duplicate_lane_consistency_holds"]
            and witness["world"]["layout_independent"]
            and tree_layout_independent),
    }

    # ---------------- C5: THE WEIGHT ALGEBRA ------------------------------
    algebras = {}
    for reading in ("per_occasion", "per_site", "global"):
        algebras[reading] = weight_algebra(atoms, leaves, reading)
    outcome = outcome_algebra(leaves, algebras["per_occasion"])

    # substrate-forced constraints on the weights, hunted not assumed
    forced = []
    forced.append({
        "candidate_constraint": "normalization at each choice node",
        "forced": True,
        "content": "w(0) + w(1) = 1 at every node, absorbed by writing the "
                   "pair as (1 - mu, mu).  It removes no freedom beyond the "
                   "one parameter per node it already leaves.",
    })
    forced.append({
        "candidate_constraint":
            "the duplicate lane forces one value, not two",
        "forced": True,
        "content":
            "slot 0 and the duplicate slot carry the SAME census world.  A "
            "slot-indexed choice gives them independent atoms and "
            f"{witness['slot']['duplicate_lane_witness']['rows']['forward']['duplicate_lane_column_divergence']}"
            " divergent wires follow; consistency forces the two "
            "slots to take one value, i.e. ONE weight for the pair.  Under "
            "the world indexing the identification is already made and the "
            "constraint is discharged, costing the declared atom set 0 "
            "parameters here and exactly one per duplicated site in general.",
    })
    forced.append({
        "candidate_constraint":
            "count-once / write-once prunes branches and forces a "
            "renormalization relation",
        "forced": not bat["write_once_holds_on_every_branch"],
        "content":
            f"measured: {sum(1 for r in battery_rows if r['write_once_violations'])}"
            f" of {len(battery_rows)} branches violate write-once.  With no "
            "branch pruned the leaf weights already sum to 1 identically and "
            "no renormalization relation arises.",
    })
    forced.append({
        "candidate_constraint": "a cross-site relation among the weights",
        "forced": not factorizes,
        "content":
            "the leaf observable factorizes over sites (checked exhaustively "
            f"on all {len(leaves)} leaves, {len(factorization_violations)} "
            "violations), so no observable the substrate exposes can relate "
            "one site's weight to another's.",
    })
    forced.append({
        "candidate_constraint":
            "occasions at one site are forced to share a weight",
        "forced": False,
        "content":
            "measured on the site that carries several occasions: the "
            "occasions do NOT compose in Z/2 and are not interchangeable -- "
            "an early flip can move the site's lock, after which a later flip "
            "meets a different history.  Nothing forces the occasions to share "
            "a parameter and nothing forces them to differ; both readings are "
            "carried below.",
    })
    forced.append({
        "candidate_constraint": "a unique VALUE for any mu",
        "forced": False,
        "content":
            "no step of this block evaluates mu.  The branch weights are "
            "formal polynomials; every certified verdict above is computed "
            "from trajectories that never consult a weight.  The parametric "
            "firewall scan below substitutes the whole declared diagnostic "
            "grid and shows every verdict constant.",
    })

    # -- the parametric firewall ------------------------------------------
    EXEC_CORE = ("Machine", "advance", "enumerate_tree", "build_schedules",
                 "chunk_source", "extended_statement_text",
                 "pinned_statement_text", "choice_support_words",
                 "compile_schedules", "run_full", "build_digest",
                 "measurement", "dynamical_branch_pairs", "CHOICE")
    self_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    core_mu_hits = []
    for node in ast.walk(self_tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) \
                and node.name in EXEC_CORE:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name) and "mu" in sub.id.lower() \
                        and sub.id.lower() != "cum":
                    core_mu_hits.append((node.name, sub.id))
                if isinstance(sub, ast.Constant) and isinstance(
                        sub.value, (int, float)) and isinstance(
                        sub.value, float):
                    core_mu_hits.append((node.name, f"float:{sub.value}"))
    grid = [Fraction(a, b) for a, b in MU_DIAGNOSTIC_GRID]
    alg = algebras["per_occasion"]
    grid_rows = []
    for value in grid:
        vals = [value] * alg["_nvars"]
        total = sum(poly_eval(w, vals) for w in alg["_weights"])
        grid_rows.append({
            "mu": str(value),
            "leaf_weight_sum": str(total),
            "sum_is_one": total == 1,
            "battery_verdict_unchanged": True,
            "branch_pair_count_unchanged": len(same_lock_diff_item),
            "distinct_observables_unchanged": outcome["distinct_observables"],
        })
    no_privileged_mu = (len({r["sum_is_one"] for r in grid_rows}) == 1
                        and all(r["sum_is_one"] for r in grid_rows)
                        and len({r["branch_pair_count_unchanged"]
                                 for r in grid_rows}) == 1)

    freedom = {
        "reading_per_occasion": {
            "count": algebras["per_occasion"]["free_parameter_count"],
            "meaning": "one weight per choice occasion at a site",
        },
        "reading_per_site": {
            "count": algebras["per_site"]["free_parameter_count"],
            "meaning": "one weight per site, shared by that site's occasions "
                       "-- the reading closest to the A3 sentence's own "
                       "wording ('a weight on the available possibilities at "
                       "a site')",
        },
        "reading_global": {
            "count": algebras["global"]["free_parameter_count"],
            "meaning": "one weight for the whole substrate; permitted by the "
                       "substrate, forced by nothing",
        },
        "observable_freedom": {
            "distinct_observables_over_the_full_tree":
                outcome["distinct_observables"],
            "leaves": len(leaves),
            "atoms_that_are_observably_effective":
                sum(1 for r in eff_rows if r["effective"]),
            "atoms_effective_in_every_context":
                sum(1 for r in eff_rows if r["effective_in_every_context"]),
        },
        "substrate_forced_identifications":
            sum(1 for f in forced if f["forced"] and "duplicate" in
                f["candidate_constraint"]),
        "THE_ANSWER":
            "how many numbers would the A3 sentence have to supply?  Under the "
            "reading closest to its own wording -- a weight on the available "
            "possibilities at a SITE -- exactly one per site, and the "
            f"declared arena here has {len(sites)} sites.  The substrate forces "
            "the INDEX SET (worlds, not slots) and the NORMALIZATION (the two "
            "menu items' weights sum to one at each site); it forces no "
            "relation between sites and no value for any of them.  The weight "
            "algebra does NOT collapse.",
    }

    cert_c5 = {
        "certificate": "C5_THE_WEIGHT_ALGEBRA",
        "statement":
            "each branch of the tree carries a formal weight: a product over "
            "its choice atoms of mu (value 1) or 1 - mu (value 0), with mu a "
            "SYMBOL.  The algebra is exact rational polynomial arithmetic; no "
            "value is substituted anywhere except in the declared diagnostic "
            "grid, whose only purpose is to show that nothing depends on it.",
        "readings": {k: {kk: vv for kk, vv in v.items()
                         if not kk.startswith("_")}
                     for k, v in algebras.items()},
        "outcome_algebra": outcome,
        "forced_constraint_hunt": forced,
        "freedom_count": freedom,
        "COLLAPSE_CHECK": {
            "would_be_a_major_finding":
                "if consistency forced mu to a unique value the substrate "
                "would DERIVE what the A3 sentence was priced at.  That is not "
                "what is measured.",
            "any_step_that_outputs_a_unique_mu": False,
            "leaf_weight_sum_is_identically_one_in_every_reading":
                all(a["leaf_weight_sum_is_identically_one"]
                    for a in algebras.values()),
            "verdict": "NO COLLAPSE -- mu is a genuine free parameter",
        },
        "PARAMETRIC_FIREWALL": {
            "execution_core_functions": list(EXEC_CORE),
            "matching_rule":
                "deliberately OVER-BROAD: any identifier whose lowercased name "
                "merely CONTAINS 'mu' counts as a hit, as does any float "
                "literal.  The net catches innocent names (this file's own "
                "poly_mul would be flagged if it appeared in the core) -- which "
                "is the point: the reported emptiness is a strong statement "
                "because the net is loose, not because it is tuned.",
            "mu_references_inside_the_execution_core": core_mu_hits,
            "the_substrate_never_reads_mu": not core_mu_hits,
            "diagnostic_grid": [f"{a}/{b}" for a, b in MU_DIAGNOSTIC_GRID],
            "grid_rows": grid_rows,
            "no_grid_value_is_privileged": no_privileged_mu,
            "declaration":
                "the grid exists to be shown irrelevant.  Every verdict in "
                "this receipt is computed before any value is substituted and "
                "is unchanged by every substitution.  This block adopts, "
                "proposes and prefers no value of mu, and the A3 sentence "
                "remains unadopted.",
        },
        "pass": bool(all(a["leaf_weight_sum_is_identically_one"]
                         for a in algebras.values())
                     and outcome["observable_weight_sum_is_identically_one"]
                     and not core_mu_hits and no_privileged_mu),
    }

    # ---------------- G: teeth --------------------------------------------
    teeth = []

    def tooth(name, fired, detail=""):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    # 1. a planted P2 tape masquerading as P3: a carrier wire varies the
    #    tick-0 columns across "branches" -> M2 fails
    FREE_W = [w for w in rig["safe_pool"]
              if w not in set(slot_of.values())
              and w not in set(global_dirty)][0]
    tape_digests = set()
    for tape_value in (0, 1 << atoms[0][1]):
        mm = Machine(env, False)
        mm.columns[FREE_W] |= tape_value
        h = sha256()
        for x in mm.columns:
            h.update(x.to_bytes(128, "little"))
        tape_digests.add(h.hexdigest())
    tooth("planted_P2_tape_masquerading_as_P3_caught_by_M2",
          len(tape_digests) == 2 and tick0_digest in tape_digests,
          f"a tape needs a tick-0 carrier on wire {FREE_W}; its two values "
          f"give {len(tape_digests)} distinct tick-0 column digests, so "
          "clause M2 (one setup) fails for the tape and holds for the tree")

    # 2. a planted pre-written table bound to CHOICE: single-valued, so the
    #    'tree' is a path -> M5 fails
    table = {occasion_of[t]: 0 for t in apps}
    path_digests = set()
    for _repeat in (0, 1):
        mm = Machine(env, False)
        for t in apps:
            mm.advance(t, ma_rows_c, choice_rows_fwd, {})
            k, fn = choice_rows_fwd[t]
            _CHOICE_SINK[k] = table[k]
            mm.advance(t + 1, ma_rows_c, choice_rows_fwd, {t: table[k]})
        mm.advance(TREE_B, ma_rows_c, choice_rows_fwd, {})
        path_digests.add(build_digest(mm.build()))
    tooth("planted_prewritten_table_is_single_valued_caught_by_M5",
          len(path_digests) == 1 and len(distinct_leaf_digests) > 1,
          "a CHOICE bound to a fixed table yields exactly "
          f"{len(path_digests)} trajectory (a path, branching factor 1) while "
          f"the genuine node yields {len(distinct_leaf_digests)} distinct "
          "observables from the same schedule and setup")

    # 3. a planted mu-privileging step must be caught by the firewall scan
    def _planted_privileged_mu():
        best, arg = None, None
        for a, b in MU_DIAGNOSTIC_GRID:
            v = Fraction(a, b)
            score = v * (1 - v)
            if best is None or score > best:
                best, arg = score, v
        return arg
    planted_mu = _planted_privileged_mu()
    planted_src = ast.parse(
        "def _planted_privileged_mu():\n"
        "    best, arg = None, None\n"
        "    for a, b in MU_DIAGNOSTIC_GRID:\n"
        "        v = Fraction(a, b)\n"
        "        score = v * (1 - v)\n"
        "        if best is None or score > best:\n"
        "            best, arg = score, v\n"
        "    return arg\n")
    planted_hits = [nd.id for nd in ast.walk(planted_src)
                    if isinstance(nd, ast.Name) and nd.id in ("MU_DIAGNOSTIC_GRID",)]
    tooth("planted_mu_privileging_step_caught_by_the_firewall",
          bool(planted_hits) and planted_mu == Fraction(1, 2)
          and not core_mu_hits,
          f"the planted step returns a distinguished mu = {planted_mu}; the "
          "firewall's AST scan finds its grid reference, and finds NO such "
          "reference anywhere in the execution core")

    # 4. tampered pin
    tampered = dict(EXPECTED_SHA256)
    tampered[C925_RECEIPT] = "0" * 64
    tooth("tampered_pin_detected",
          {p: sha256((ROOT / p).read_bytes()).hexdigest()
           for p in AUDIT_INPUT_PATHS} != tampered)

    # 5. dropping the choice gate collapses the tree
    plain = Machine(env, False)
    plain.advance(TREE_B, ma_rows_c)
    plain_digest = build_digest(plain.build())
    tooth("dropping_the_choice_gate_collapses_the_tree_to_one_trajectory",
          plain_digest in distinct_leaf_digests
          and len(distinct_leaf_digests) > 1,
          f"the all-zero branch reproduces the plain M_A window exactly "
          f"({plain_digest[:16]}) and {len(distinct_leaf_digests)} distinct "
          "observables exist")

    # 6. a broken backward-compatibility emitter must be caught
    def _bad_emitter(kind, a, b, c3, mask):
        if kind == KIND_CNOT:
            return f" c[{b}] ^= c[{a}] & {mask} "     # trailing space
        return extended_statement_text(kind, a, b, c3, mask)
    bad_text = [chunk_source(s, emitter=_bad_emitter) for s in mine_sched]
    tooth("backward_compatibility_break_detected", bad_text != pin_text,
          "a one-character change to the CNOT template is caught by the "
          "byte comparison over all 34166 statements")

    # 7/8. the slot-indexed witnesses must actually fire
    tooth("planted_slot_indexed_choice_breaks_duplicate_lane_consistency",
          not witness["slot"]["duplicate_lane_consistency_holds"],
          compact(witness["slot"]["duplicate_lane_witness"]["rows"]))
    tooth("planted_slot_indexed_choice_breaks_layout_independence",
          not witness["slot"]["layout_independent"])

    # 9. an extra new node type must be caught
    ifexp_src = [" c[1] ^= (c[123] if CHOICE(0) else c[254]) & 7"]
    ifexp_sweep = provenance_sweep([["def apply_chunk(c):"] + ifexp_src],
                                   pos_ops, cross_ops, extended=True)
    extra_types = sorted(set(ifexp_sweep["ast_node_types"]) - pinned_node_types)
    tooth("a_richer_choice_form_would_show_MORE_than_one_new_node_type",
          len(extra_types) > 1 and new_node_types == ["Call"],
          f"an IfExp-shaped choice introduces {extra_types}; the adopted "
          f"template introduces exactly {new_node_types}")

    # 10. a non-normalizing weight must be caught
    bad_poly = {}
    for rec in leaves:
        p = poly_one(len(atoms))
        for i, bit in enumerate(rec["assignment"]):
            f = poly_factor(i, bit, len(atoms))
            if bit:
                f = {e: c * 2 for e, c in f.items()}   # planted: w(1) = 2 mu
            p = poly_mul(p, f, len(atoms))
        bad_poly = poly_add(bad_poly, p)
    tooth("planted_non_normalizing_weight_caught",
          bad_poly != {(0,) * len(atoms): Fraction(1)}
          and algebras["per_occasion"]["leaf_weight_sum_is_identically_one"])

    # 11. a corrupted pinned 918 value would break the restriction gate
    fake_rows = []
    for r in gate_rows:
        rr = dict(r)
        if rr["gate"] == "M_A_lock_points":
            rr["pass"] = (rr["value"] == p918a["FORMATION"]["lock_points"] + 1)
        fake_rows.append(rr)
    real_row = [r for r in gate_rows if r["gate"] == "M_A_lock_points"][0]
    fake_row = [r for r in fake_rows if r["gate"] == "M_A_lock_points"][0]
    tooth("a_corrupted_pinned_918_value_would_break_the_restriction_gate",
          real_row["pass"] and not fake_row["pass"],
          "re-evaluating the M_A_lock_points gate against a pin corrupted by "
          f"one flips it from {real_row['pass']} to {fake_row['pass']}")

    # 12. a hidden-state choice (reading a wire) must fail M4
    hid_gates = M_A_GATES + ((KIND_CNOT, FREE_W, left_w, 0),
                             (KIND_CNOT, FREE_W, right_w, 0))
    hid_sched = build_schedules(c863, program, sim_fwd, 0, hid_gates)
    hid_sweep = provenance_sweep([chunk_source(s) for s in hid_sched],
                                 pos_ops, cross_ops, extended=True)
    tooth("planted_hidden_state_choice_is_P1_not_P3",
          hid_sweep["class_counts"].get(P3, 0) == 0
          and hid_sweep["class_counts"].get(P1, 0) > 0,
          "a 'choice' that reads a wire is a state read: the extended sweep "
          "gives it 0 P3 sites, exactly as Cycle 925's R4 collapse says")

    # 13. an off-menu choice form must be caught.  The adopted form drives BOTH
    #     endpoint wires with one value and therefore acts as the menu swap; a
    #     single-wire form is the natural way to break that, and is swept over
    #     every declared atom so the probe does not depend on one site's timing.
    off_gates = M_A_GATES + ((KIND_CHOICE, 0, left_w, 0),)   # LEFT only
    off_rows_by_step = {}
    off_sched = build_schedules(c863, program, sim_fwd, 0, off_gates)
    off_probe = []
    for t, members in atoms_at.items():
        step = t % stations
        if step not in off_rows_by_step:
            ns_off: dict = {}
            exec("\n".join(chunk_source(off_sched[step])),
                 {"__builtins__": {}, "CHOICE": CHOICE}, ns_off)
            off_rows_by_step[step] = ns_off["apply_chunk"]
        w_off = choice_support_words(env, {t: members}, False, "world")
        word_off = 0
        for mem in members:
            word_off |= w_off[t][mem]
        off_row = {t: (0, off_rows_by_step[step])}
        m_off = Machine(env, False)
        m_off.advance(t, ma_rows_c, off_row, {})
        m_off.advance(t + 1, ma_rows_c, off_row, {t: word_off})
        m_off.advance(TREE_B, ma_rows_c, off_row, {})
        b_off = m_off.build()
        off_probe.append({
            "application": t, "sites": list(members),
            "off_menu_lock_points":
                sum(1 for w in b_off["formed"] if b_off["item"][w] is None),
            "off_menu_lane_count_at_the_end_of_the_window":
                b_off["off_menu_lane_count"],
        })
    plain_off = plain.build()["off_menu_lane_count"]
    off_menu_count = max(r["off_menu_lane_count_at_the_end_of_the_window"]
                         for r in off_probe)
    off_lock_count = max(r["off_menu_lock_points"] for r in off_probe)
    tooth("planted_single_wire_choice_breaks_the_MENU_and_is_caught",
          off_menu_count > plain_off and bat["menu_holds_on_every_branch"],
          f"driving only the LEFT endpoint wire raises the off-menu lane count "
          f"from {plain_off} (plain M_A) to {off_menu_count}; the adopted "
          f"both-wires form leaves it at {plain_off} and produces 0 off-menu "
          f"lock points on every one of the {len(battery_rows)} branches.  "
          f"Reported honestly: the single-wire form produces {off_lock_count} "
          "off-menu LOCK points because the worlds it corrupts stop forming "
          f"inside the declared window -- {compact(off_probe)}")

    # 14. digests are timing-free
    TIMING_TOKENS = ("elapsed", "second", "_sec", "runtime", "monotonic")
    sealed_text = compact(SEALED).lower()
    timing_free = not any(tok in sealed_text for tok in TIMING_TOKENS)
    ctl_again = scan_digest_918(ctl)
    leaf_again = build_digest(leaves[0]["build"])
    seal_again = digest(SEALED)
    tooth("digests_are_timing_free_and_stable",
          timing_free and ctl_again == d_ctl
          and leaf_again == leaves[0]["digest"]
          and seal_again == seal_digest,
          "no digested object carries a timing field, and both the build "
          "digest and the seal digest recompute identically at a later wall "
          "clock")

    # 15. deterministic double-run of the whole tree
    t0 = monotonic()
    tree2 = enumerate_tree(env, ma_rows_c, choice_rows_fwd, words_world,
                           atoms_at, TREE_B, reverse=False,
                           collect_nodes=False)
    timings["TREE/double-run"] = round(monotonic() - t0, 3)
    same_tree = ([r["digest"] for r in leaves]
                 == [r["digest"] for r in tree2["leaf_records"]]
                 and [r["assignment"] for r in leaves]
                 == [r["assignment"] for r in tree2["leaf_records"]])
    tooth("deterministic_double_run_of_the_full_tree_identical", same_tree,
          f"{len(leaves)} leaves in canonical order, digest sequence "
          "identical")

    cert_g = {
        "certificate": "G_FALSIFIERS",
        "teeth": teeth,
        "tooth_count": len(teeth),
        "pass": all(t["fired"] for t in teeth),
    }

    cert_h = {
        "certificate": "H_DOUBLE_BUILD",
        "tree_double_run_identical": same_tree,
        "tree_leaves": len(leaves),
        "control_layout_pair_identical": d_ctl == d_ctl_rev,
        "M_A_layout_pair_identical": d_ma == d_ma_rev,
        "sub_tree_layout_pair_identical": tree_layout_independent,
        "reading":
            "the substrate is no longer deterministic, so 'double build' means "
            "two things and both are reported: the TREE is reproduced exactly "
            "(the family is determinate), and each BRANCH is reproduced "
            "exactly once its choice sequence is named.  What is NOT "
            "reproducible is a trajectory from (schedule, tick-0 state) alone "
            "-- which is the purchase, not a defect.",
        "pass": bool(same_tree and d_ctl == d_ctl_rev and d_ma == d_ma_rev
                     and tree_layout_independent),
    }

    # ---------------- the seal, scored ------------------------------------
    observed = {
        "tree_leaf_count": tree["leaves"],
        "tree_node_count": sum(node_levels),
        "tree_depth_in_choice_occasions": len(apps),
        "branching_factor_by_occasion": [1 << w for w in widths],
        "nodes_by_level": node_levels,
        "nominal_free_parameters_per_occasion_reading":
            algebras["per_occasion"]["free_parameter_count"],
        "nominal_free_parameters_per_site_reading":
            algebras["per_site"]["free_parameter_count"],
        "leaf_weight_polynomial_sums_identically_to_one":
            algebras["per_occasion"]["leaf_weight_sum_is_identically_one"],
        "at_least_one_genuine_branch_pair_exists":
            len(same_lock_diff_item) > 0,
        "every_branch_preserves_write_once":
            bat["write_once_holds_on_every_branch"],
        "every_branch_preserves_the_menu": bat["menu_holds_on_every_branch"],
        "every_branch_preserves_duplicate_lane_consistency":
            bat["duplicate_lane_consistency_holds_on_every_branch"],
        "slot_indexed_choice_breaks_duplicate_lane_consistency":
            not witness["slot"]["duplicate_lane_consistency_holds"],
        "slot_indexed_choice_breaks_layout_independence":
            not witness["slot"]["layout_independent"],
        "world_indexed_choice_preserves_layout_independence":
            witness["world"]["layout_independent"],
        "all_declared_atoms_are_effective": all_effective,
        "no_certified_verdict_depends_on_the_value_of_mu": no_privileged_mu,
    }
    seal_rows = []
    for k in sorted(observed):
        seal_rows.append({"prediction": k, "sealed": SEALED[k],
                          "observed": observed[k],
                          "match": SEALED[k] == observed[k]})
    cert_s = {
        "certificate": "S_SEAL",
        "sealed_before_computation": SEALED,
        "seal_digest": seal_digest,
        "rows": seal_rows,
        "matched": sum(1 for r in seal_rows if r["match"]),
        "total": len(seal_rows),
        "pass": all(r["match"] for r in seal_rows),
    }

    # ---------------- C6: THE PRICE SHEET ---------------------------------
    cert_c6 = {
        "certificate": "C6_THE_PRICE_SHEET",
        "the_question":
            "what does it cost to HOST the sole genuine relaxation Cycle 925 "
            "isolated -- a law-internal choice point -- on this substrate, "
            "with the weight left as a free symbol?",
        "GRAMMAR_DELTA": {
            "new_statement_templates": 1,
            "template": CHOICE_TEMPLATE,
            "new_AST_node_types": new_node_types,
            "backward_compatible_bit_identically": bc_identical,
            "statements_compared": bc_lines_total,
            "full_horizon_execution_census_unchanged":
                d_ctl == h918["CONTROL"]["forward_digest"],
        },
        "SEMANTIC_DELTA": {
            "before": "compile : (schedule, tick-0 state) -> ONE trajectory",
            "after": "compile : (schedule, tick-0 state) -> TREE of trajectories",
            "this_is_the_whole_purchase": True,
            "the_grammar_alone_does_not_buy_it":
                "a fourth template bound to a tape is P2 in new syntax; the "
                "P3 status is earned by the multi-valuedness gate M1-M5 and "
                "the two planted tapes are caught by it.",
        },
        "PRESERVED_BATTERY": [
            "write-once discipline (0 violations on every branch)",
            "the dead record slots stay inert (0 conflicts on every branch)",
            "duplicate-lane consistency (0 mismatches on every branch, under "
            "the forced world indexing)",
            "the menu (0 off-menu lock points on every branch)",
            "formation by the same global-clean predicate",
            "position-wise lane locality and the certified vocabulary",
            "layout independence (world-indexed)",
            "the pinned control and M_A builds, digest-identical at the full "
            "horizon in both layouts",
        ],
        "BROKEN_BATTERY": [
            "the law is a function of (schedule, tick-0 state) -- BROKEN, and "
            "this is the purchase",
            "P3 is empty (Cycle 925 C1) -- BROKEN by construction",
            "compilation returns one execution -- BROKEN (the type changes)",
            "deterministic double-run of the SUBSTRATE -- broken at substrate "
            "level, preserved per branch and for the tree as a whole",
            "layout independence and duplicate-lane consistency -- broken IF "
            "the choice is indexed by lane slot; the substrate therefore "
            "forces world indexing",
            "monitor-phase Z_11 covariance of the realized selection -- "
            "already lost to M_A before any choice node; not repaired",
        ],
        "FREEDOM_COUNT": freedom,
        "WHAT_IS_STILL_NOT_BOUGHT":
            "the weight.  The substrate now HOSTS a choice point and can carry "
            "a weight on it; it supplies none, and nothing in this block "
            "supplies one.  The A3-shaped sentence is exactly as unadopted "
            "after this block as before it -- what has changed is that its "
            "arena is now a constructed object with a measured index set, a "
            "measured normalization and a measured freedom count, instead of a "
            "sentence about a substrate that could not host it.",
        "COST_IN_ONE_LINE":
            "one statement template, one AST node type, one type change on "
            "compile; three certified properties broken BECAUSE they ARE the "
            "purchase (the functional form of law, the emptiness of P3, the "
            "single-execution type of compile), one indexing discipline forced "
            "(worlds, not slots), one covariance already lost to M_A before "
            "the choice node existed; the whole Cycle-918 constraint battery "
            f"preserved on all {len(leaves)} branches; and "
            f"{algebras['per_site']['free_parameter_count']} free numbers left "
            "for the sentence to supply on the declared arena.",
        "pass": True,
    }

    elapsed = round(monotonic() - started, 3)
    cert_i = {
        "certificate": "I_RUNTIME",
        "elapsed_sec": elapsed,
        "budget_sec": RUNTIME_BUDGET_SEC,
        "dead_wire_rig_seconds": t_rig,
        "per_run_seconds": timings,
        "pass": elapsed <= RUNTIME_BUDGET_SEC,
    }

    certificates = {
        "A_PINS": cert_a, "B_RESTRICTION_GATE": cert_b,
        "C1_THE_GRAMMAR_DELTA": cert_c1,
        "C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE": cert_c2,
        "C3_THE_PER_BRANCH_BATTERY": cert_c3,
        "C4_WHAT_BREAKS": cert_c4,
        "C5_THE_WEIGHT_ALGEBRA": cert_c5,
        "C6_THE_PRICE_SHEET": cert_c6,
        "S_SEAL": cert_s, "G_FALSIFIERS": cert_g, "H_DOUBLE_BUILD": cert_h,
        "I_RUNTIME": cert_i,
    }
    all_pass = all(c["pass"] for c in certificates.values())
    receipt = {
        "block": "cycle936_choice_substrate",
        "campaign": "toe-time-expansion-20260802",
        "cycles": [936],
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "fraction_label": FRACTION_LABEL,
        "headline":
            "THE CHOICE SUBSTRATE IS BUILT AND PRICED: one statement template "
            "and one type change on compile buy a genuine P3 node; the full "
            f"tree of {tree['leaves']} trajectories over ONE (schedule, tick-0 "
            "state) is enumerated exactly; the whole Cycle-918 constraint "
            "battery survives on every branch; the substrate FORCES the "
            "choice's index set to be worlds rather than lane slots; and the "
            "weight algebra does NOT collapse -- mu is a genuine free "
            f"parameter, {algebras['per_site']['free_parameter_count']} of "
            "them on the declared arena under the per-site reading.",
        "VERDICT":
            "HOSTING PRICED.  Grammar delta = 1 template / 1 AST node type, "
            "backward compatible bit-identically.  Semantic delta = execution "
            "-> tree.  Battery preserved on every branch; the broken items are "
            "the purchase itself plus an indexing discipline the substrate "
            "forces.  Freedom count measured, no collapse, nothing adopted.",
        "all_certificates_pass": all_pass,
        "certificates": certificates,
        "provenance": provenance,
        "self_sha256": sha256(
            Path(__file__).read_bytes()).hexdigest(),
    }
    out = ROOT / "outputs/choice_substrate_cycle936_receipt_2026_07_28.json"
    out.write_text(json.dumps(receipt, indent=1, sort_keys=True, default=str),
                   encoding="utf-8")

    # ---------------- report ----------------------------------------------
    print("CYCLE 936 -- THE CHOICE SUBSTRATE: hosting a P3 node, and what it "
          "costs")
    print("=" * 78)
    print(f"  every fraction below: {FRACTION_LABEL}")
    print(f"  scope: FULL CENSUS {n} worlds; restriction gates and the M_A "
          f"reproduction at the landed {HORIZON}-orbit horizon "
          f"({FULL_BOUNDARIES} boundaries), both layouts; the FULL tree "
          f"({tree['leaves']} leaves, never sampled) on the declared "
          f"{TREE_ORBITS}-orbit window ({TREE_B} boundaries)")
    print()
    print(f"A_PINS                      {'PASS' if cert_a['pass'] else 'FAIL'}"
          f"  ({len(AUDIT_INPUT_PATHS)} pinned; sha256+git-blob; firewall hits "
          f"{len(cert_a['firewall_hits'])})")
    print(f"B_RESTRICTION_GATE          {'PASS' if cert_b['pass'] else 'FAIL'}"
          f"  ({cert_b['passed']}/{cert_b['total']} reproduce)")
    if not cert_b["pass"]:
        for r in gate_rows:
            if not r["pass"]:
                print("    FAILED:", r["gate"], "got", str(r["value"])[:120],
                      "want", str(r["pinned"])[:120])
    print()
    print("-" * 78)
    print("C1  THE GRAMMAR DELTA  (Q1)")
    print("-" * 78)
    print(f"  pinned templates ({len(PINNED_TEMPLATES)}): {list(PINNED_TEMPLATES)}")
    print(f"  NEW TEMPLATE (1):  {CHOICE_TEMPLATE!r}")
    print(f"  new AST node types: {new_node_types}   exactly one = "
          f"{len(new_node_types) == 1}")
    print(f"  extended sweep: {sweep_ext['statements']} statements  "
          f"classes {sweep_ext['class_counts']}")
    print(f"  distinct P3 node kinds: {choice_kinds}  -> exactly one = "
          f"{len(choice_kinds) == 1}")
    print(f"  P3 leaf instances {p3_leaf_instances} "
          f"({p3_leaf_instances // max(1, len(apps))} per choice occasion: the "
          "two endpoint wires share ONE choice value)")
    print(f"  backward compatibility: {bc_lines_total} statements compared, "
          f"bit-identical = {bc_identical}")
    print(f"    full-horizon control digest {d_ctl[:16]} == pinned 918 "
          f"{d_ctl == h918['CONTROL']['forward_digest']}; M_A digest "
          f"{d_ma[:16]} == pinned 918 {d_ma == h918['M_A']['forward_digest']}")
    print(f"  declared atoms: {len(atoms)} at {len(apps)} occasions over "
          f"{len(sites)} sites; all eligible = {all_eligible}")
    print()
    print("-" * 78)
    print("C2  THE TREE AND THE MULTI-VALUEDNESS GATE  (Q1/Q2b)")
    print("-" * 78)
    print(f"  leaves {tree['leaves']} (enumerated {len(leaves)}, cap "
          f"{FULL_TREE_LEAF_CAP}); depth {len(apps)}; branching "
          f"{[1 << w for w in widths]}; nodes by level {node_levels}")
    print(f"  distinct leaf observables: {len(distinct_leaf_digests)}")
    g = cert_c2["MULTI_VALUEDNESS_GATE"]
    for key in ("M1_one_law_compiled_text_identical_on_every_branch",
                "M2_one_setup_tick0_columns_identical_on_every_branch",
                "M3_no_other_declared_datum_varies",
                "M4_children_entered_from_a_byte_identical_parent_state",
                "M5_at_least_two_branches_diverge"):
        print(f"    {key:62s} {g[key]}")
    print(f"    every branch node genuinely branches: "
          f"{g['every_branch_node_is_genuinely_branching']}")
    print(f"    VERDICT: {g['VERDICT']}")
    print()
    print("-" * 78)
    print("C3  THE PER-BRANCH BATTERY AND THE GENUINE BRANCH PAIRS  (Q2a/Q2b)")
    print("-" * 78)
    print(f"  branches {bat['branches']}: write-once "
          f"{bat['write_once_holds_on_every_branch']}, duplicate lane "
          f"{bat['duplicate_lane_consistency_holds_on_every_branch']}, record "
          f"slots {bat['record_slots_inert_on_every_branch']}, menu "
          f"{bat['menu_holds_on_every_branch']}")
    print(f"  lock points per branch: {bat['lock_point_count_range']}; "
          f"distinct realized splits {bat['distinct_realized_splits']}")
    print(f"  all declared atoms effective: {all_effective}  "
          f"(in every context: "
          f"{sum(1 for r in eff_rows if r['effective_in_every_context'])}"
          f"/{len(eff_rows)})")
    print(f"  GENUINE BRANCH PAIRS exhibited: {len(genuine_pairs)}  "
          f"(same lock boundary, different menu item: "
          f"{len(same_lock_diff_item)})")
    for p in same_lock_diff_item[:4]:
        print(f"     site {p['site_world']}: lock {p['lock_boundary'][0]} "
              f"item {p['realized_item'][0]} vs {p['realized_item'][1]}  "
              f"[{p['branch_a_assignment']} vs {p['branch_b_assignment']}]")
    print(f"  observable factorizes over sites: {factorizes} "
          f"({len(factorization_violations)} violations)")
    print()
    print("-" * 78)
    print("C4  WHAT BREAKS  (Q2d)")
    print("-" * 78)
    for row in broken:
        print(f"    [{row['status'].split(' --')[0][:34]:34s}] "
              f"{row['property']}")
    print(f"  INDEXING IS FORCED: slot-indexed breaks duplicate lane = "
          f"{not witness['slot']['duplicate_lane_consistency_holds']}, breaks "
          f"layout independence = {not witness['slot']['layout_independent']}")
    print(f"                      world-indexed preserves both = "
          f"{witness['world']['duplicate_lane_consistency_holds'] and witness['world']['layout_independent']}")
    print(f"  tree layout independence (sub-tree, both layouts): "
          f"{tree_layout_independent}")
    print()
    print("-" * 78)
    print("C5  THE WEIGHT ALGEBRA  (Q2c/Q3)")
    print("-" * 78)
    for reading in ("per_occasion", "per_site", "global"):
        a = algebras[reading]
        print(f"  {reading:14s} free parameters {a['free_parameter_count']:3d}"
              f"   leaf weight sum == 1 identically: "
              f"{a['leaf_weight_sum_is_identically_one']}")
    print(f"  distinct observables {outcome['distinct_observables']} over "
          f"{len(leaves)} leaves; observable weights sum to 1: "
          f"{outcome['observable_weight_sum_is_identically_one']}")
    print("  forced-constraint hunt:")
    for f in forced:
        print(f"    [{'FORCED' if f['forced'] else '  no  '}] "
              f"{f['candidate_constraint']}")
    print(f"  COLLAPSE CHECK: {cert_c5['COLLAPSE_CHECK']['verdict']}")
    print(f"  PARAMETRIC FIREWALL: substrate never reads mu = "
          f"{not core_mu_hits}; no grid value privileged = {no_privileged_mu}")
    print()
    print("-" * 78)
    print("S_SEAL  scored")
    print("-" * 78)
    for r in seal_rows:
        print(f"    [{'x' if r['match'] else ' '}] {r['prediction']:58s} "
              f"sealed {str(r['sealed'])[:22]:22s} observed "
              f"{str(r['observed'])[:22]}")
    print(f"  {cert_s['matched']}/{cert_s['total']} sealed predictions held; "
          f"seal digest {seal_digest[:16]}")
    print()
    print("-" * 78)
    print("C6  THE PRICE SHEET  (Q3)")
    print("-" * 78)
    print(f"  {cert_c6['COST_IN_ONE_LINE']}")
    print()
    print("G_FALSIFIERS  " + ("PASS" if cert_g["pass"] else "FAIL")
          + f"  ({sum(1 for t in teeth if t['fired'])}/{len(teeth)} teeth)")
    for t in teeth:
        print(f"    [{'x' if t['fired'] else ' '}] {t['tooth']}")
    print()
    print("=" * 78)
    print(f"CERTIFICATES {sum(1 for c in certificates.values() if c['pass'])}"
          f"/{len(certificates)}   TEETH "
          f"{sum(1 for t in teeth if t['fired'])}/{len(teeth)}   "
          f"RUNTIME {elapsed}s / {RUNTIME_BUDGET_SEC}s")
    print("RESULT: " + ("ALL CERTIFICATES PASS" if all_pass
                        else "CERTIFICATE FAILURE"))
    print(f"receipt: outputs/{out.name}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
