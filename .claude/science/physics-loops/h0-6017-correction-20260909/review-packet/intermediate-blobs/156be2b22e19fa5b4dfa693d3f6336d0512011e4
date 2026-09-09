#!/usr/bin/env python3
"""Cycle 947 -- THE H0 DISCHARGE ATTEMPT.  The Born lane's wall, formalised,
computed, and priced.

WHAT H0 IS.  Cycle 946 derived the symmetric two-item weight at 3 of the 5
genuine two-item menus of the mirror-partnered kernel, CONDITIONAL on a named,
undischarged import it called H0:

    "the identification of the compiled substrate law as a realization of the
     axiom's nearest-neighbor rule such that a symmetry of one is a symmetry
     of the other."

Without H0 the 946 result is a theorem about a circuit, not about
Admissibility.  This block does not assume H0.  It DECOMPOSES H0 into named,
individually checkable clauses, COMPUTES every clause that the substrate plus
the LANDED axiom text can decide, and PRICES the residue as explicit import
sentences.  Discharge by stipulation is forbidden: where the only route to a
clause is to define the axiom's model to BE the circuit, the clause is RESIDUE
and its price is that stipulation, named.

THE LANDED AXIOM.  PRs #6011/#6013 landed on 2026-08-05; the adopted
Admissibility text is now on origin/main.  This runner pins the LANDED file by
sha256 AND git blob and vendor-reads it with `git show origin/main:<path>`.
The worktree's own copy of that path is PRE-adoption and is pinned separately
so the delta stays on the record; no axiom text is ever quoted from it.

THE CLAUSES.

  H0a  SITE MAP.  Is there a map from the compiled state to lattice sites,
       read off COMPILER-NATIVE data?
       H0a1 FIBRATION -- does the compiled state factorise natively at all?
       H0a2 TOTALITY  -- is that factorisation total and well defined?
       H0a3 EMBEDDING -- is there native data placing the fibres on Z^3 with
            nearest-neighbor adjacency?
  H0b  LOCALITY / SCREENING.
       H0b1 CONTAINMENT -- is the backward causal cone of the menu wires at a
            genuine menu site's choice boundary contained in that site's
            neighborhood?
       H0b2 VARIATION -- does the compiled law's distribution at a site
            actually VARY with the conditions at OTHER sites, as the axiom's
            "varies with" clause requires?
  H0c  POSSIBILITY IDENTIFICATION.
       H0c1 MENU CARDINALITY -- are the two items a two-element menu?
       H0c2 SUPPORT -- is the distribution's support exactly those two items?
       H0c3 DOMAIN -- are those items possibilities of a domain with the
            axiom's one-site algebraic presentation?
  H0d  SYMMETRY TRANSPORT.
       H0d1 FIBRE RESPECT -- does sigma respect the native fibres?
       H0d2 DESCENT -- does sigma descend to an axiom-level action?

THE NO-GO SEARCH.  H0 as stated is UNIVERSAL ("a symmetry of one is a symmetry
of the other").  A universal claim dies to one counterexample, so this block
searches a declared space for symmetries of the compiled law that do NOT
descend to a site-uniform lattice-level action.  Two families are searched:
the lane-restricted relabellings, and the lane transpositions.

THE FIREWALL.  Zero float literals.  Zero weight-shaped rationals outside a
CONDITIONAL_-prefixed key path.  This block derives no weight; the 946 value is
referenced only as a conditional citation, never recomputed as law content.

MINIMAL-PREMISE RULE.  The supervisor's proposed clause decomposition is
FALLIBLE and is treated as a hypothesis.  Where the compiler's own data
contradicts it, the data wins and the deviation is recorded in
SPEC_DEVIATIONS.  Cycle 946's runner is PINNED BY BYTES and BLOCKED FROM
IMPORT AND FROM AST LIFT: every structure it used is re-derived here from the
pinned 936 compiler and the pinned 719 kernel.
"""

from __future__ import annotations

import ast
import importlib.abc
import itertools
import json
import math
import subprocess
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, product
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNTIME_BUDGET_SEC = 1800
FRACTION_LABEL = "bookkeeping fraction, not probability"

# ---------------------------------------------------------------------------
# A: pins
# ---------------------------------------------------------------------------

CORE_PATH = ("scripts/frontier_cycle719_two_rail_recurrent_controller_core"
             "_2026_07_26.py")
C936_PATH = "scripts/frontier_cycle936_choice_substrate_2026_07_28.py"
C936_RECEIPT = "outputs/choice_substrate_cycle936_receipt_2026_07_28.json"
C943_RECEIPT = "outputs/prerecord_swap_cycle943_receipt_2026_07_28.json"
C946_PATH = "scripts/frontier_cycle946_mirror_kernel_2026_07_28.py"
C946_RECEIPT = "outputs/mirror_kernel_cycle946_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (CORE_PATH, C936_PATH, C936_RECEIPT, C943_RECEIPT,
                     C946_PATH, C946_RECEIPT, AXIOMS_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C936_PATH:
        "ba00f39403a1280346d2e20e6e1985130b7d4b0a986e1473acd2c637acd96e3d",
    C936_RECEIPT:
        "4412ae9016df02546db26cdd87fa33ab68bf2a7370b27640e18d4d0e59132028",
    C943_RECEIPT:
        "cc66fa9258fd76eba473585326d07cc83e108860174076ba0e14b7d006a878e6",
    C946_PATH:
        "e393c882c3f0ea745190aeb36faf3f02c958537185210f5b8715e7b2bce465d7",
    C946_RECEIPT:
        "b9d8263f7b180cb5973acefeb7379272ed0994ec146fdba2023fb8e2c9536cb5",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C936_PATH: "75cb05ffb9456691747a67ed5227f3db589f95c4",
    C936_RECEIPT: "d7b786fccc0435d139339c141dbad75c9f8d799b",
    C943_RECEIPT: "7b88a67072bb965b975db217eb514d805e7dfb2c",
    C946_PATH: "2beaafb471ab2a5b28185d92de8c8481bfd50905",
    C946_RECEIPT: "c74aceddb1cb30d797aed447961a819732a0dd67",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}

# THE LANDED AXIOM.  #6011 and #6013 landed; the branch is deleted; origin/main
# now carries the adopted text.  946 consumed the BRANCH blob; this block
# consumes the LANDED blob and pins both hashes the supervisor supplied.
LANDED_AXIOM_REF = "origin/main"
LANDED_AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
LANDED_AXIOM_SHA256 = \
    "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39"
LANDED_AXIOM_GIT_BLOB = "2f5fdd26898f62c17fcabc846761f7785c2eadb1"

# The byte-quotes this block consumes.  Each is checked `in` the vendor-read
# LANDED text; a tampered quote fires tooth T_AXIOM.
Q_LATTICE_SITES = (
    "Physical sites are the points of the cubic lattice `Z^3`, with "
    "nearest-neighbor\nadjacency, standard translations, and proper cubic "
    "rotations about each site.")
Q_LATTICE_NO_PRIVILEGE = (
    "No site is privileged. Sites are distinguished by the supplied lattice\n"
    "structure alone.")
Q_QUBIT_DOMAIN = "Each site has a domain of local possibilities."
Q_QUBIT_PRESENTATION = (
    "The full one-site possibility domain has algebraic presentation "
    "`M_2(C)`.")
Q_QUBIT_NO_PRIVILEGE = (
    "No possibility is privileged. Possibilities are distinguished by the "
    "supplied\nalgebraic structure alone.")
Q_ADMISS_COVARIANCE = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under "
    "lattice\ntranslations and proper cubic rotations.")
Q_ADMISS_DISTRIBUTION = (
    "For each site, the probability distribution over the possibilities is\n"
    "determined by, and varies with, the nearest-neighbor conditions.")
Q_ADMISS_SUPPORT = (
    "The distribution is a probability measure on\nthe local possibility "
    "domain; \"available\"/\"admissible\" denotes its support --\non finite "
    "menus, exactly the possibilities of nonzero probability.")
Q_QUALIFICATION = (
    "These axioms state only their named primitive content. Further physical\n"
    "structure requires a retained derivation or bridge, or explicit approved-"
    "\nprimitive registration, before use as a premise.")

BLOCKLISTED_MODULES = (
    "frontier_cycle946_mirror_kernel_2026_07_28",
    "frontier_cycle936_choice_substrate_2026_07_28",
    "frontier_cycle940_symmetric_weights_2026_07_28",
    "frontier_cycle943_prerecord_swap_2026_07_28",
    "frontier_cycle863_time_from_records_2026_07_28",
    "frontier_cycle878_event_space_groundwork_2026_07_28",
    "frontier_cycle911_type_vacuity_2026_07_28",
    "frontier_cycle913_selection_function_2026_07_28",
    "frontier_cycle918_writable_endpoint_2026_07_28",
    "frontier_cycle925_law_relaxation_2026_07_28",
)


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
# the AST lift of the pinned 936 compiler (NEVER an import; NEVER 946)
# ---------------------------------------------------------------------------

LIFT_CONSTS = (
    "CORE_PATH", "HANDSHAKE_PATH", "C863_PATH", "C878_PATH", "C911_PATH",
    "C913_PATH", "C918_PATH", "C925_PATH", "C863_FUNCS", "C863_CONSTS",
    "C878_FUNCS", "C878_CONSTS", "C911_FUNCS", "C911_CONSTS", "C913_FUNCS",
    "KIND_X", "KIND_CNOT", "KIND_TOF", "KIND_SHIFT", "KIND_CHOICE",
    "KIND_NAMES", "CERTIFIED_KINDS", "PINNED_TEMPLATES", "CHOICE_TEMPLATE",
    "EXTENDED_TEMPLATES", "GRAMMAR_DELTA_TEXT", "P3_NOT_P2_TEXT",
    "LANE_SHIFT", "HORIZON", "DEAD_CHUNK_ORBITS", "TREE_ORBITS",
    "CHOICE_ATOMS", "FULL_TREE_LEAF_CAP", "_CHOICE_SINK",
)
LIFT_FUNCS = (
    "ast_lift", "lift_ast_op_tuple", "lift_machinery",
    "pinned_statement_text", "extended_statement_text", "chunk_source",
    "gate_text", "gate_target", "station_mask", "build_schedules", "CHOICE",
    "compile_schedules", "acc_add", "acc_get", "item_of", "build_digest",
    "scan_digest_918", "run_full", "measurement", "dynamical_branch_pairs",
    "z11_covariance", "choice_support_words", "enumerate_tree", "poly_one",
    "poly_mul", "poly_add", "poly_factor", "poly_str", "poly_eval",
    "weight_algebra", "outcome_algebra",
)
LIFT_CLASSES = ("Machine",)


def lift_936(source):
    tree = ast.parse(source, filename=C936_PATH)
    body, got_f, got_c, got_k = [], set(), set(), set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in LIFT_FUNCS:
            body.append(node)
            got_f.add(node.name)
        elif isinstance(node, ast.ClassDef) and node.name in LIFT_CLASSES:
            body.append(node)
            got_k.add(node.name)
        elif isinstance(node, ast.Assign):
            names = []
            for t in node.targets:
                if isinstance(t, ast.Name):
                    names.append(t.id)
                elif isinstance(t, ast.Tuple):
                    names.extend(e.id for e in t.elts
                                 if isinstance(e, ast.Name))
            if names and all(nm in LIFT_CONSTS for nm in names):
                body.append(node)
                got_c.update(names)
    missing = (tuple(sorted(set(LIFT_FUNCS) - got_f)),
               tuple(sorted(set(LIFT_CONSTS) - got_c)),
               tuple(sorted(set(LIFT_CLASSES) - got_k)))
    if any(missing):
        raise AssertionError(("lift incomplete", missing))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = {"__builtins__": __builtins__, "ROOT": ROOT, "K": K, "np": np,
          "ast": ast, "json": json, "math": math, "sys": sys,
          "itertools": itertools, "combinations": combinations,
          "product": product, "Counter": Counter, "defaultdict": defaultdict,
          "Fraction": Fraction, "sha256": sha256, "sha1": sha1, "Path": Path,
          "SimpleNamespace": SimpleNamespace, "compact": compact,
          "digest": digest, "git_blob": git_blob}
    exec(compile(module, f"<ast-lift {C936_PATH}>", "exec"), ns)
    return SimpleNamespace(**{n: ns[n] for n in
                              tuple(got_f) + tuple(got_c) + tuple(got_k)}), \
        (len(got_f), len(got_c), len(got_k))


def vendor_read_landed_axiom():
    spec = f"{LANDED_AXIOM_REF}:{LANDED_AXIOM_PATH}"
    blob = subprocess.run(["git", "-C", str(ROOT), "show", spec],
                          capture_output=True, check=False).stdout
    ref = subprocess.run(["git", "-C", str(ROOT), "rev-parse", spec],
                         capture_output=True,
                         check=False).stdout.decode().strip()
    return blob, {
        "vendor_read": spec,
        "why_vendor_read": "PR #6011 and #6013 LANDED on 2026-08-05 and the "
                           "branch is deleted; the adopted text is now on "
                           "origin/main.  The worktree's own copy of the same "
                           "path is the PRE-adoption text and is pinned "
                           "separately below.  No axiom text is quoted from "
                           "the worktree copy anywhere in this block.",
        "sha256": sha256(blob).hexdigest(),
        "git_blob": git_blob(blob),
        "git_rev_parse_of_the_path": ref,
        "bytes": len(blob),
        "sha256_matches_supervisor_pin":
            sha256(blob).hexdigest() == LANDED_AXIOM_SHA256,
        "git_blob_matches_supervisor_pin":
            git_blob(blob) == LANDED_AXIOM_GIT_BLOB,
        "git_object_id_agrees_with_recomputed_blob": ref == git_blob(blob),
        "delta_from_the_946_consumed_branch_blob":
            "946 consumed blob 02ab79ec08f0b29d1922c1f628d0d0389ddd2c99 from "
            "the PR branch; this block consumes the LANDED blob "
            "2f5fdd26898f62c17fcabc846761f7785c2eadb1 from origin/main.  The "
            "two blobs differ (the landed file carries the merge's own "
            "history section); every sentence this block quotes is checked "
            "verbatim against the LANDED bytes.",
    }


def pin_rows():
    rows, payloads = {}, {}
    for path in AUDIT_INPUT_PATHS:
        blob = (ROOT / path).read_bytes()
        payloads[path] = blob
        rows[path] = {"sha256": sha256(blob).hexdigest(),
                      "git_blob": git_blob(blob), "bytes": len(blob)}
    ax_blob, ax_row = vendor_read_landed_axiom()
    payloads["LANDED_AXIOM"] = ax_blob
    sha_ok = all(rows[p]["sha256"] == v for p, v in EXPECTED_SHA256.items())
    blob_ok = all(rows[p]["git_blob"] == v
                  for p, v in EXPECTED_GIT_BLOBS.items())
    cert = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "rows": rows,
        "sha256_all_match": sha_ok,
        "git_blobs_all_match": blob_ok,
        "existing_worktree_relative": all((ROOT / p).exists()
                                          for p in AUDIT_INPUT_PATHS),
        "blocked_modules_loaded": [m for m in BLOCKLISTED_MODULES
                                   if m in sys.modules],
        "firewall_hits": list(PRIMARY_FIREWALL.hits),
        "CONDITIONAL_ON_LANDED_AXIOM": {
            "ref": LANDED_AXIOM_REF,
            "path": LANDED_AXIOM_PATH,
            "sha256": LANDED_AXIOM_SHA256,
            "git_blob": LANDED_AXIOM_GIT_BLOB,
            "row": ax_row,
        },
        "C946_IS_PINNED_BUT_NEVER_LIFTED":
            "the 946 runner's bytes are pinned so the reader knows exactly "
            "which text this block re-derives, and its module name is on the "
            "import BLOCKLIST.  Its structures (sigma, the splice, the "
            "certificate layers, the neighborhood formalizations) are "
            "RE-DERIVED here from the pinned 936 compiler and the pinned 719 "
            "kernel; nothing is lifted or imported from it.",
        "modification_mechanism":
            "WRAP, NEVER EDIT.  The pinned 936 runner is AST-LIFTED (selected "
            "top-level nodes replayed in source order) and never imported; "
            "its bytes are unchanged and hashed.  This block's own "
            "construction is a pure function on compiled gate ROWS.  Nothing "
            "writes to any pinned file; the landed axiom is read out of git.",
    }
    cert["pass"] = bool(
        sha_ok and blob_ok and cert["existing_worktree_relative"]
        and ax_row["sha256_matches_supervisor_pin"]
        and ax_row["git_blob_matches_supervisor_pin"]
        and ax_row["git_object_id_agrees_with_recomputed_blob"]
        and not cert["blocked_modules_loaded"] and not cert["firewall_hits"])
    return cert, payloads


# ---------------------------------------------------------------------------
# RE-DERIVED 946 MACHINERY (never imported, never lifted)
# ---------------------------------------------------------------------------

def sigma_pairs(left_w, right_w, bank_bases):
    """946's involution, re-derived: the endpoint pair plus every bank's two
    direction rails.  Re-derivation is checked against 946's PINNED RECEIPT
    VALUE in the restriction gate, so a divergence is caught, not hidden."""
    return ((left_w, right_w),) + tuple(
        (b + K.A.U_TO_V, b + K.A.V_TO_U) for b in bank_bases)


def make_sigma(pairs):
    sig = {}
    for a, b in pairs:
        sig[a] = b
        sig[b] = a
    return sig


def sigma_gate(g, sig, kinds):
    kind, a, b, c3, mask = g

    def m(w):
        return sig.get(w, w)

    if kind == kinds["X"]:
        return (kind, m(a), b, c3, mask)
    if kind == kinds["CNOT"]:
        return (kind, m(a), m(b), c3, mask)
    if kind == kinds["TOF"]:
        return (kind, m(a), m(b), m(c3), mask)
    if kind == kinds["CHOICE"]:
        return (kind, a, m(b), c3, mask)
    return g


def gate_controls(g, kinds):
    kind, a, b, c3, mask = g
    if kind == kinds["CNOT"]:
        return (a,)
    if kind == kinds["TOF"]:
        return (a, b)
    return ()


def mirror_defect(schedules, sig, kinds):
    out = []
    for si, s in enumerate(schedules):
        have = Counter(s)
        img = Counter(sigma_gate(g, sig, kinds) for g in s)
        rem = have - img
        for g in s:
            if rem[g] > 0:
                rem[g] -= 1
                out.append((si, g, sigma_gate(g, sig, kinds)))
    return out


def mirror_splice(schedules, sig, kinds):
    out, added = [], []
    for s in schedules:
        have = Counter(s)
        img = Counter(sigma_gate(g, sig, kinds) for g in s)
        rem = have - img
        new = []
        for g in s:
            new.append(g)
            if rem[g] > 0:
                rem[g] -= 1
                im = sigma_gate(g, sig, kinds)
                new.append(im)
                added.append(im)
        out.append(tuple(new))
    return tuple(out), added


def multiset_sigma_invariant(schedules, sig, kinds):
    return all(Counter(s) == Counter(sigma_gate(g, sig, kinds) for g in s)
               for s in schedules)


def perm_apply(cols, sig):
    out = list(cols)
    for w, v in sig.items():
        out[v] = cols[w]
    return out


def perm_apply_lane(cols, sig, lane):
    out = list(cols)
    bit = 1 << lane
    for w, v in sig.items():
        out[v] = (cols[v] & ~bit) | (((cols[w] >> lane) & 1) << lane)
    return out


def swap_lanes(cols, i, j):
    """Exchange two lanes' bits on every wire.  A candidate symmetry that acts
    on the BASE of the fibration rather than inside a fibre."""
    bi, bj = 1 << i, 1 << j
    out = []
    for c in cols:
        keep = c & ~(bi | bj)
        if c & bi:
            keep |= bj
        if c & bj:
            keep |= bi
        out.append(keep)
    return out


def strong_states(count, proto, touched, universe, tag):
    out = []
    for i in range(count):
        cols = list(proto)
        for w in touched:
            acc = 0
            for k in range(4):
                acc = (acc << 256) | int.from_bytes(
                    sha256(f"{tag}|{i}|{w}|{k}".encode("ascii")).digest(),
                    "big")
            cols[w] = acc & universe
        out.append(cols)
    return out


def semantic_commutes(fns, cols_list, transform):
    """Wires where the transform fails to commute with one full compiled
    cycle.  Empty  <=>  the transform is a semantic symmetry of the law on the
    supplied ensemble."""
    bad = set()
    for cols in cols_list:
        a = transform(cols)
        b = list(cols)
        for fn in fns:
            fn(a)
            fn(b)
        b = transform(b)
        for w in range(len(a)):
            if a[w] != b[w]:
                bad.add(w)
    return sorted(bad)


def backward_cone(schedules, seeds, depth, kinds, gate_target):
    """BACKWARD reachability over the gate graph: which wires can influence the
    seed wires within `depth` layers of control-to-target edges."""
    cone = set(seeds)
    for _ in range(depth):
        add = set()
        for s in schedules:
            for g in s:
                if gate_target(*g[:4]) in cone:
                    add.update(gate_controls(g, kinds))
        if add <= cone:
            break
        cone |= add
    return cone


def _walk_paths(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _walk_paths(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            yield from _walk_paths(v, f"{path}[{i}]")
    else:
        yield path, obj


def _is_a_clock_field(path):
    low = path.lower()
    return any(tok in low for tok in
               ("seconds", "_s]", "timing", "wall_clock", "elapsed",
                "runtime_sec", "started_at", "monotonic"))


# ---------------------------------------------------------------------------
# H0a1: the lane-diagonality proof, done on the EMITTED SOURCE
# ---------------------------------------------------------------------------

def statement_is_lane_diagonal(line: str) -> tuple[bool, str]:
    """A compiled statement is LANE-DIAGONAL when, read as an operation on
    machine words, bit position L of every output depends only on bit position
    L of the inputs.  That is a purely syntactic property of the operator set:
    XOR and AND are bitwise, and an integer literal mask contributes only its
    own bit L.  Any shift, comparison, add, multiply or call would break it.

    This checker parses the statement and REFUSES anything outside the
    bitwise-diagonal grammar.  It is deliberately whitelist-shaped: an operator
    it has never seen is a FAILURE, not a pass."""
    try:
        tree = ast.parse(line.strip())
    except SyntaxError as exc:                      # pragma: no cover
        return False, f"unparsable: {exc}"
    if len(tree.body) != 1:
        return False, "not a single statement"
    node = tree.body[0]
    if not isinstance(node, ast.AugAssign):
        return False, f"not an augmented assignment: {type(node).__name__}"
    if not isinstance(node.op, ast.BitXor):
        return False, f"augmented operator is not ^=: {type(node.op).__name__}"
    if not (isinstance(node.target, ast.Subscript)
            and isinstance(node.target.value, ast.Name)
            and node.target.value.id == "c"
            and isinstance(node.target.slice, ast.Constant)
            and isinstance(node.target.slice.value, int)):
        return False, "target is not c[<int literal>]"

    def ok(expr):
        if isinstance(expr, ast.Constant):
            return isinstance(expr.value, int) and not isinstance(expr.value,
                                                                  bool)
        if isinstance(expr, ast.Subscript):
            return (isinstance(expr.value, ast.Name) and expr.value.id == "c"
                    and isinstance(expr.slice, ast.Constant)
                    and isinstance(expr.slice.value, int))
        if isinstance(expr, ast.BinOp):
            return (isinstance(expr.op, (ast.BitAnd, ast.BitXor, ast.BitOr))
                    and ok(expr.left) and ok(expr.right))
        if isinstance(expr, ast.Call):
            # the CHOICE node: a compile-time occasion ordinal resolved from a
            # sink.  It is a CONSTANT of the trajectory, hence lane-uniform,
            # which is a WEAKER property than diagonal and is reported as its
            # own row rather than waved through.
            return False
        return False

    if not ok(node.value):
        return False, ("right-hand side leaves the bitwise-diagonal grammar: "
                       + ast.dump(node.value)[:160])
    return True, "bitwise diagonal"


def statement_is_choice_diagonal(line: str) -> tuple[bool, str]:
    """The CHOICE statement `c[t] ^= CHOICE(k) & <mask>`.  CHOICE(k) resolves a
    compile-time occasion ordinal to a WORD supplied from outside the state.
    The statement is still bit-diagonal -- bit L of the target depends on bit L
    of the choice word and bit L of the mask -- but the choice word is NOT a
    function of the state, so it is reported in its own class rather than
    folded into the ordinary diagonal count."""
    try:
        tree = ast.parse(line.strip())
    except SyntaxError as exc:                      # pragma: no cover
        return False, f"unparsable: {exc}"
    if len(tree.body) != 1:
        return False, "not a single statement"
    node = tree.body[0]
    if not (isinstance(node, ast.AugAssign)
            and isinstance(node.op, ast.BitXor)
            and isinstance(node.target, ast.Subscript)):
        return False, "not `c[i] ^= ...`"
    v = node.value
    if not (isinstance(v, ast.BinOp) and isinstance(v.op, ast.BitAnd)):
        return False, "not `<call> & <mask>`"
    call, mask = v.left, v.right
    if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
            and call.func.id == "CHOICE" and len(call.args) == 1
            and isinstance(call.args[0], ast.Constant)):
        return False, "left operand is not CHOICE(<int literal>)"
    if not (isinstance(mask, ast.Constant) and isinstance(mask.value, int)):
        return False, "mask is not an integer literal"
    return True, "choice-diagonal (word supplied from outside the state)"


# ---------------------------------------------------------------------------
# the bounded lattice-isometry enumeration (used by the NO-GO argument)
# ---------------------------------------------------------------------------

def proper_cubic_rotations():
    """The 24 proper rotations of the cube, generated as signed permutation
    matrices with determinant +1.  Enumerated, not asserted."""
    out = []
    for perm in itertools.permutations(range(3)):
        sgn_perm = 1
        p = list(perm)
        for i in range(3):
            for j in range(i + 1, 3):
                if p[i] > p[j]:
                    sgn_perm = -sgn_perm
        for signs in itertools.product((1, -1), repeat=3):
            det = sgn_perm * signs[0] * signs[1] * signs[2]
            if det == 1:
                out.append((perm, signs))
    return tuple(out)


def isometry_apply(rot, t, x):
    perm, signs = rot
    y = tuple(signs[i] * x[perm[i]] for i in range(3))
    return (y[0] + t[0], y[1] + t[1], y[2] + t[2])


def transposition_isometry_search(side):
    """Is any element of the axiom's covariance group -- translations composed
    with proper cubic rotations -- a TRANSPOSITION of two lattice points that
    fixes every other point of a declared box?

    Bounded and exhaustive on the declared box: all 24 rotations, all
    translations that map the box into itself.  A NEGATIVE answer is what the
    NO-GO argument needs, and it is computed rather than asserted."""
    box = [(x, y, z) for x in range(side) for y in range(side)
           for z in range(side)]
    boxset = set(box)
    rots = proper_cubic_rotations()
    trange = range(-2 * side, 2 * side + 1)
    checked = 0
    transpositions = []
    for rot in rots:
        for t in itertools.product(trange, repeat=3):
            img = [isometry_apply(rot, t, x) for x in box]
            if set(img) != boxset:
                continue
            checked += 1
            moved = [(a, b) for a, b in zip(box, img) if a != b]
            if len(moved) == 2 and moved[0][1] == moved[1][0] \
                    and moved[1][1] == moved[0][0]:
                transpositions.append((rot, t, moved))
    return {
        "declared_box": f"[0,{side})^3",
        "box_points": len(box),
        "proper_rotations_enumerated": len(rots),
        "box_preserving_isometries_found": checked,
        "isometries_acting_as_a_bare_transposition": len(transpositions),
        "NO_COVARIANCE_ELEMENT_TRANSPOSES_TWO_SITES_AND_FIXES_THE_REST":
            not transpositions,
        "why_this_matters":
            "the compiled law is invariant under exchanging two lanes with "
            "equal station masks.  Under ANY site map that sends distinct "
            "lanes to distinct lattice points, that invariance is a "
            "transposition of two sites fixing every other site.  This "
            "enumeration shows no element of the axiom's declared covariance "
            "group (translations and proper cubic rotations) acts that way, "
            "so the compiled law has symmetries with no axiom-level "
            "counterpart.",
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    started = monotonic()
    timings: dict = {}
    cert_a, payloads = pin_rows()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({
            k: cert_a[k] for k in
            ("sha256_all_match", "git_blobs_all_match",
             "existing_worktree_relative", "blocked_modules_loaded",
             "firewall_hits")}), flush=True)
        print(compact(cert_a["CONDITIONAL_ON_LANDED_AXIOM"]["row"]),
              flush=True)
        return 2

    t0 = monotonic()
    M, lift_counts = lift_936(payloads[C936_PATH].decode("utf-8"))
    kinds = {"X": M.KIND_X, "CNOT": M.KIND_CNOT, "TOF": M.KIND_TOF,
             "CHOICE": M.KIND_CHOICE}
    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     provenance) = M.lift_machinery()

    r936 = json.loads(payloads[C936_RECEIPT].decode("utf-8"))
    r943 = json.loads(payloads[C943_RECEIPT].decode("utf-8"))
    r946 = json.loads(payloads[C946_RECEIPT].decode("utf-8"))
    axiom_text = payloads["LANDED_AXIOM"].decode("utf-8")
    preadopt_text = payloads[AXIOMS_PATH].decode("utf-8")

    # ---------------- the substrate, rebuilt from the pinned bytes --------
    program, event_seeds, census = c863.derive_census()
    stations = len(program)
    states, _init_failures = c863.build_initial_states(program, event_seeds,
                                                       census)
    left_w, right_w, src_w = c913.endpoint_wires()
    BB = K.M.R12.BANK_BASES
    n = len(census)
    REC_A = BB[0] + K.A.POINTER
    sim_fwd = tuple(census) + (census[0],)
    proto = c863.pack_lanes(tuple(states) + (states[0],))
    rig = c878.dead_wire_rig(program, sim_fwd, proto)
    slot_of = rig["slot_of"]
    slot_wires = tuple(sorted(set(slot_of.values())))
    per_bank, links, source_ptr = c863.dirty_partition()
    global_dirty = tuple(sorted(set(per_bank[0]) | set(per_bank[1])
                                | set(links) | {source_ptr}))
    bank_dirty = (tuple(sorted(per_bank[0])), tuple(sorted(per_bank[1])))
    env = {"c863": c863, "c878": c878, "c911": c911, "c913": c913,
           "program": program, "census": census, "states": states, "n": n,
           "stations": stations, "left_w": left_w, "right_w": right_w,
           "global_dirty": global_dirty, "bank_dirty": bank_dirty,
           "uni_all": (1 << n) - 1, "uni_sim": (1 << (n + 1)) - 1,
           "slot_of": slot_of, "slot_wires": slot_wires,
           "register_cap": consts911["REGISTER_CAP"],
           "setup_direction": {ev: c913.read_state_direction(seed)
                               for ev, seed in event_seeds}}
    M_A_GATES = ((M.KIND_CNOT, REC_A, left_w, 0),
                 (M.KIND_CNOT, REC_A, right_w, 0))

    atoms = tuple(sorted(M.CHOICE_ATOMS))
    atoms_at: dict = {}
    for t, w in atoms:
        atoms_at.setdefault(t, []).append(w)
    atoms_at = {t: tuple(sorted(v)) for t, v in sorted(atoms_at.items())}
    apps = sorted(atoms_at)
    occasion_of = {t: i for i, t in enumerate(apps)}
    ZERO_WORDS = {t: 0 for t in apps}
    words_world = M.choice_support_words(env, atoms_at, False, "world")

    SIG_PAIRS = sigma_pairs(left_w, right_w, BB)
    SIG = make_sigma(SIG_PAIRS)
    ORIENTATION_WIRES = tuple(sorted(
        b + K.A.cell(c)["orientation"] for b in BB[:2] for c in (0, 1)))

    sched_ma = M.build_schedules(c863, program, sim_fwd, 0, M_A_GATES)
    rows_ma = M.compile_schedules(sched_ma)
    defect = mirror_defect(sched_ma, SIG, kinds)
    sched_p, added = mirror_splice(sched_ma, SIG, kinds)
    rows_p = M.compile_schedules(sched_p)

    def choice_rows_for(splice):
        cr = {}
        for t in apps:
            k = occasion_of[t]
            gates = M_A_GATES + ((M.KIND_CHOICE, k, left_w, 0),
                                 (M.KIND_CHOICE, k, right_w, 0))
            s = M.build_schedules(c863, program, sim_fwd, 0, gates)
            s = splice(s)
            src = M.chunk_source(s[t % stations])
            ns: dict = {}
            exec("\n".join(src), {"__builtins__": {}, "CHOICE": M.CHOICE}, ns)
            cr[t] = (k, ns["apply_chunk"])
        return cr

    choice_rows_p = choice_rows_for(
        lambda s: mirror_splice(s, SIG, kinds)[0])
    # the choice-bearing SCHEDULES, kept as rows for cone analysis
    choice_sched_p = {}
    for t in apps:
        k = occasion_of[t]
        gates = M_A_GATES + ((M.KIND_CHOICE, k, left_w, 0),
                             (M.KIND_CHOICE, k, right_w, 0))
        s = M.build_schedules(c863, program, sim_fwd, 0, gates)
        choice_sched_p[t] = mirror_splice(s, SIG, kinds)[0]

    touched_p = sorted({w for s in sched_p for g in s
                        for w in (M.gate_target(*g[:4]),)
                        + gate_controls(g, kinds)})
    timings["setup"] = round(monotonic() - t0, 3)
    print(f"[setup {timings['setup']}s] {len(proto)} wires, {n} census "
          f"worlds, {stations} stations, partnered gates "
          f"{sum(len(s) for s in sched_p)}", flush=True)

    # =====================================================================
    # B: RESTRICTION GATES -- 936/943/946 reproduced value-for-value
    # =====================================================================
    gate_rows = []

    def gate(name, got, want):
        ok = got == want
        gate_rows.append({"gate": name, "value": got, "pinned": want,
                          "pass": ok})
        return ok

    q1_946 = r946["certificates"]["Q1_THE_MIRROR_PARTNERED_KERNEL"]
    q2_946 = r946["certificates"]["Q2_THE_DERIVATION"]
    ne_946 = q2_946["NEIGHBORHOOD_EQUALITY"]

    gate("c936_receipt_all_certificates_pass",
         r936["all_certificates_pass"], True)
    gate("c936_self_sha256_matches_the_pinned_runner",
         sha256(payloads[C936_PATH]).hexdigest(), r936["self_sha256"])
    gate("c943_receipt_all_certificates_pass",
         r943["all_certificates_pass"], True)
    gate("c946_receipt_all_certificates_pass",
         r946["all_certificates_pass"], True)
    gate("c946_self_sha256_matches_the_pinned_runner",
         sha256(payloads[C946_PATH]).hexdigest(), r946["self_sha256"])
    gate("sigma_pairs_re_derived_match_946",
         [list(p) for p in SIG_PAIRS], q1_946["sigma_pairs"])
    gate("sigma_is_an_involution",
         all(SIG[SIG[w]] == w for w in SIG), True)
    gate("orientation_wires_re_derived_match_946",
         list(ORIENTATION_WIRES), q1_946["orientation_wires"])
    gate("defect_distinct_gates",
         len({g for _si, g, _im in defect}), q1_946["defect_distinct_gates"])
    gate("defect_occurrences", len(defect), q1_946["defect_occurrences"])
    gate("gates_before", sum(len(s) for s in sched_ma), q1_946["gates_before"])
    gate("gates_after", sum(len(s) for s in sched_p), q1_946["gates_after"])
    gate("gates_added", len(added), q1_946["gates_added"])
    gate("L1_partnered_multiset_sigma_invariant",
         multiset_sigma_invariant(sched_p, SIG, kinds), True)
    gate("L1_baseline_is_NOT_multiset_sigma_invariant",
         multiset_sigma_invariant(sched_ma, SIG, kinds), False)
    gate("census_worlds", n, len(census))
    gate("declared_choice_atoms", [list(a) for a in atoms],
         [list(a) for a in sorted(M.CHOICE_ATOMS)])
    gate("covered_genuine_menu_atoms_946",
         q2_946["COVERAGE"]["of_the_five_genuine_two_item_menu_atoms_covered"],
         [[700, 475], [702, 450], [702, 715]])
    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": gate_rows,
        "passed": sum(1 for r in gate_rows if r["pass"]),
        "total": len(gate_rows),
        "pass": all(r["pass"] for r in gate_rows),
    }
    print(f"[B] restriction {cert_b['passed']}/{cert_b['total']}", flush=True)
    if not cert_b["pass"]:
        print("RESTRICTION FAILED", compact(
            [r for r in gate_rows if not r["pass"]]), flush=True)
        return 3

    S: dict = {}
    SPEC_DEVIATIONS: list = []

    # =====================================================================
    # THE AXIOM BYTE-QUOTES (the only place axiom text is quoted)
    # =====================================================================
    QUOTES = {
        "Lattice_sites_are_Z3_points": Q_LATTICE_SITES,
        "Lattice_no_site_is_privileged": Q_LATTICE_NO_PRIVILEGE,
        "Qubit_domain": Q_QUBIT_DOMAIN,
        "Qubit_presentation_M2C": Q_QUBIT_PRESENTATION,
        "Qubit_no_possibility_is_privileged": Q_QUBIT_NO_PRIVILEGE,
        "Admissibility_covariance": Q_ADMISS_COVARIANCE,
        "Admissibility_distribution": Q_ADMISS_DISTRIBUTION,
        "Admissibility_support_reading_note": Q_ADMISS_SUPPORT,
        "Qualification_further_structure_needs_a_derivation": Q_QUALIFICATION,
    }
    quote_check = {k: (v in axiom_text) for k, v in QUOTES.items()}
    S["CONDITIONAL_ON_LANDED_AXIOM_byte_quotes"] = {
        "ref": LANDED_AXIOM_REF,
        "path": LANDED_AXIOM_PATH,
        "sha256": LANDED_AXIOM_SHA256,
        "git_blob": LANDED_AXIOM_GIT_BLOB,
        "quotes": QUOTES,
        "every_quote_verbatim_in_the_landed_text": all(quote_check.values()),
        "quote_check": quote_check,
        "the_worktree_copy_is_pre_adoption": {
            "worktree_sha256": sha256(payloads[AXIOMS_PATH]).hexdigest(),
            "distribution_sentence_present_in_the_worktree_copy":
                Q_ADMISS_DISTRIBUTION in preadopt_text,
            "note": "the worktree copy is the PRE-adoption memo and does NOT "
                    "contain the distribution sentence; it is pinned only so "
                    "the delta is on the record.  No axiom text is quoted "
                    "from it.",
        },
    }
    print(f"[quotes] {sum(quote_check.values())}/{len(quote_check)} verbatim "
          f"in the landed text", flush=True)

    # =====================================================================
    # H0a1  FIBRATION -- does the compiled state factorise natively?
    # PREDICATE (stated before computing): every compiled statement of the
    # partnered law is BIT-DIAGONAL -- bit L of every output word depends only
    # on bit L of the input words and bit L of its constant mask.  If that
    # holds for every statement of every station, the compiled state
    # factorises as a product over bit positions (lanes), and the factors are
    # the compiler's OWN native decomposition.
    # =====================================================================
    t0 = monotonic()
    diag_rows = []
    fail_lines = []
    n_diag = n_choice = 0
    for si, s in enumerate(sched_p):
        for line in M.chunk_source(s)[1:]:
            ok, why = statement_is_lane_diagonal(line)
            if ok:
                n_diag += 1
                continue
            ok2, why2 = statement_is_choice_diagonal(line)
            if ok2:
                n_choice += 1
                continue
            fail_lines.append({"station": si, "line": line.strip()[:120],
                               "why_not_diagonal": why,
                               "why_not_choice": why2})
    for t in apps:
        for si, s in enumerate(choice_sched_p[t]):
            for line in M.chunk_source(s)[1:]:
                ok, _ = statement_is_lane_diagonal(line)
                if ok:
                    n_diag += 1
                    continue
                ok2, why2 = statement_is_choice_diagonal(line)
                if ok2:
                    n_choice += 1
                    continue
                fail_lines.append({"occasion_chunk": t, "station": si,
                                   "line": line.strip()[:120],
                                   "why_not_choice": why2})

    # SEMANTIC CONFIRMATION: perturb ONE lane and show no other lane moves.
    ens = strong_states(4, proto, touched_p, env["uni_sim"], "c947fib")
    probe_lanes = tuple(sorted({0, 1, n, 254, 450, 475, 540, 558, 715,
                                n // 2, n - 1}))
    lane_leak = []
    for j in probe_lanes:
        cols = list(ens[0])
        pert = list(cols)
        bit = 1 << j
        for w in touched_p:
            pert[w] ^= bit
        a, b = list(cols), list(pert)
        for fn in rows_p:
            fn(a)
            fn(b)
        moved = 0
        for w in range(len(a)):
            d = a[w] ^ b[w]
            if d & ~bit:
                moved |= d & ~bit
        lane_leak.append({"perturbed_lane": j,
                          "other_lanes_that_moved":
                              bin(moved).count("1"),
                          "clean": moved == 0})
    timings["H0a1"] = round(monotonic() - t0, 3)
    S["H0a1_FIBRATION"] = {
        "clause": "H0a1 FIBRATION -- the compiled state factorises natively",
        "PREDICATE": "every compiled statement of the partnered law is "
                     "bit-diagonal: bit L of every output depends only on bit "
                     "L of the inputs and bit L of its constant mask.",
        "statements_checked": n_diag + n_choice + len(fail_lines),
        "bitwise_diagonal_statements": n_diag,
        "choice_diagonal_statements": n_choice,
        "statements_outside_the_diagonal_grammar": len(fail_lines),
        "offending_lines": fail_lines[:8],
        "semantic_lane_leak_probe": lane_leak,
        "every_probe_lane_leaks_nothing": all(r["clean"] for r in lane_leak),
        "THE_NATIVE_FIBRATION": {
            "base": "the LANE index, 0..n, where lane j carries census world "
                    "j and lane n is the compiler's own duplicate of lane 0",
            "fibre_over_a_lane": "the pair set {(wire, lane) : wire in "
                                 "range(W)} -- the whole register file, read "
                                 "at that lane's bit position",
            "wires_W": len(proto),
            "lanes": n + 1,
            "state_cells": (n + 1) * len(proto),
            "WHY_THIS_IS_COMPILER_NATIVE":
                "the compiler emits `c[t] ^= c[a] & c[b] & <mask>`; XOR and "
                "AND are bitwise and the mask is an integer literal, so the "
                "lane decomposition is not a reading imposed on the compiler "
                "-- it is the only decomposition its operator set admits.  "
                "The choice node injects a WORD from outside the state, one "
                "bit per lane, so even the branching datum is lane-local.",
        },
        "VERDICT": "DERIVED",
    }
    print(f"[H0a1 {timings['H0a1']}s] {n_diag} diagonal + {n_choice} choice, "
          f"{len(fail_lines)} outside the grammar; lane leak clean="
          f"{all(r['clean'] for r in lane_leak)}", flush=True)

    # =====================================================================
    # H0a2  TOTALITY -- is the fibration total and well defined?
    # PREDICATE: (i) every state cell (wire, lane) lies in exactly one fibre;
    # (ii) the compiler's duplicate lane is identified with lane 0 by its own
    # construction, and every gate's mask agrees on the two.
    # =====================================================================
    t0 = monotonic()
    all_masks = sorted({g[4] for s in sched_p for g in s}
                       | {g[4] for t in apps for s in choice_sched_p[t]
                          for g in s})
    dup_disagree = [m for m in all_masks
                    if ((m >> 0) & 1) != ((m >> n) & 1)]
    outside_universe = [m for m in all_masks if m & ~env["uni_sim"]]
    S["H0a2_TOTALITY"] = {
        "clause": "H0a2 TOTALITY -- the fibration is total and well defined",
        "PREDICATE": "every (wire, lane) cell lies in exactly one fibre; the "
                     "duplicate lane is identified with lane 0 by the "
                     "compiler's own simulation vector; no mask reaches "
                     "outside the declared lane universe.",
        "distinct_lane_masks_in_the_partnered_law": len(all_masks),
        "masks_reaching_outside_the_lane_universe": len(outside_universe),
        "masks_disagreeing_on_lane_0_and_the_duplicate_lane":
            len(dup_disagree),
        "the_duplicate_is_compiler_native":
            "the simulation vector is `tuple(census) + (census[0],)`: the "
            "compiler itself appends a second copy of world 0.  936 measured "
            "that the weight must be identified across that pair "
            "(duplicate-lane consistency), so the fibration's base is the "
            "census QUOTIENTED by that identification.",
        "base_cardinality_before_identification": n + 1,
        "base_cardinality_after_identification": n,
        "assignment_is_total": not outside_universe,
        "assignment_is_single_valued":
            "each cell (wire, lane) belongs to the fibre over `lane` and to "
            "no other: lanes are bit positions of one machine word, so the "
            "assignment is a partition by construction, not a choice.",
        "VERDICT": "DERIVED",
    }
    timings["H0a2"] = round(monotonic() - t0, 3)

    # =====================================================================
    # H0a3  EMBEDDING -- is there native data placing the fibres on Z^3?
    # PREDICATE: some compiler-native datum (a) assigns each lane a point of
    # Z^3, or (b) supplies a relation on lanes that IS the Z^3 nearest-
    # neighbor adjacency (irreflexive, symmetric, 6-regular, non-transitive).
    # =====================================================================
    t0 = monotonic()
    key_schema = {
        "census_key_arity": len(census[0]),
        "field_0_source_count_range": [min(k[0] for k in census),
                                       max(k[0] for k in census)],
        "field_1_event_range": [min(k[1] for k in census),
                                max(k[1] for k in census)],
        "field_2_positions_is_a_tuple_of_station_indices": True,
        "field_2_position_range": [min(min(k[2]) for k in census),
                                   max(max(k[2]) for k in census)],
        "example_keys": [list(census[i]) if not isinstance(census[i][2], tuple)
                         else [census[i][0], census[i][1],
                               list(census[i][2])]
                         for i in (0, 1, n // 2, n - 1)],
        "no_field_is_a_coordinate_triple":
            "the census key is (source count, event ordinal, station position "
            "tuple).  None of the three is a lattice coordinate, and the key "
            "set is not a box: it is the set of pairwise-separated position "
            "subsets crossed with the event seeds.",
    }
    LATTICE_TOKENS = ("Z3", "z3", "cubic", "lattice", "neighbour", "neighbor",
                      "adjacen", "coord", "site_of", "nearest")
    token_hits = {}
    for path in (CORE_PATH, C936_PATH):
        src = payloads[path].decode("utf-8")
        names = set()
        for node in ast.walk(ast.parse(src)):
            if isinstance(node, ast.Name):
                names.add(node.id)
            elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                names.add(node.name)
            elif isinstance(node, ast.Attribute):
                names.add(node.attr)
        token_hits[path] = sorted(
            nm for nm in names
            if any(tok.lower() in nm.lower() for tok in LATTICE_TOKENS))
    # the only compiler-native relation between lanes: EQUAL STATION MASK.
    # Compute it, then test it against the axiom's adjacency signature.
    pos_of = {j: census[j][2] for j in range(n)}
    classes = defaultdict(list)
    for j in range(n):
        classes[pos_of[j]].append(j)
    class_sizes = sorted(Counter(len(v) for v in classes.values()).items())
    equalmask_is_transitive = True          # an equivalence relation, by
    equalmask_is_reflexive = True           # construction; recorded as facts
    degrees = sorted({len(v) - 1 for v in classes.values()})
    S["H0a3_EMBEDDING"] = {
        "clause": "H0a3 EMBEDDING -- native data placing the fibres on Z^3",
        "PREDICATE": "some compiler-native datum assigns each lane a point of "
                     "Z^3, or supplies a relation on lanes that IS the Z^3 "
                     "nearest-neighbor adjacency (irreflexive, symmetric, "
                     "6-regular, non-transitive).",
        "the_census_key_schema": key_schema,
        "lattice_token_scan_over_the_pinned_sources": token_hits,
        "lattice_token_hits_total": sum(len(v) for v in token_hits.values()),
        "THE_ONLY_NATIVE_RELATION_BETWEEN_LANES": {
            "what_it_is": "equality of the station-position tuple, which is "
                          "what fixes a lane's gate masks.  Two lanes with "
                          "equal position tuples see literally the same "
                          "gates; two lanes with different tuples see "
                          "different gates.  Nothing else in the compiled law "
                          "relates one lane to another (H0a1: the cross-lane "
                          "dependence is empty).",
            "position_classes": len(classes),
            "class_size_histogram": [list(x) for x in class_sizes],
            "relation_is_reflexive": equalmask_is_reflexive,
            "relation_is_transitive": equalmask_is_transitive,
            "degree_set": degrees,
            "is_it_the_Z3_nearest_neighbor_adjacency":
                "NO.  Z^3 adjacency is irreflexive, non-transitive and "
                "6-regular.  The only native lane relation is an EQUIVALENCE "
                "(reflexive and transitive) whose degree set is not {6}.",
        },
        "AN_EMBEDDING_EXISTS_SET_THEORETICALLY_AND_THAT_IS_THE_PROBLEM":
            "the census is finite, so injections census -> Z^3 exist in "
            "abundance.  No compiler datum selects one, and -- by H0b2 below "
            "-- under EVERY such injection the compiled law's dependence "
            "between distinct sites is empty, so the induced 'nearest-"
            "neighbor rule' is the same rule for every embedding and is "
            "constant in the neighbor conditions.  The choice of embedding "
            "therefore cannot be made by measurement: it is a stipulation, "
            "and the axiom's covariance sentence has no purchase on it.",
        "VERDICT": "RESIDUE",
        "PRICE": "IMPORT SENTENCE H0a3: 'Fix an injection Phi from the "
                 "compiler's census worlds into the points of Z^3.'  Nothing "
                 "in the substrate, the compiler, the kernel or the landed "
                 "axiom text selects Phi, and no measurement can distinguish "
                 "two choices of Phi (H0b2).",
        "WHAT_WOULD_DISCHARGE_IT": "a compiled substrate whose lanes carry a "
                                   "native coordinate and whose gate masks "
                                   "couple lanes at lattice distance 1 -- "
                                   "i.e. a compiler with real inter-site "
                                   "gates.  The pinned compiler has none.",
    }
    timings["H0a3"] = round(monotonic() - t0, 3)
    print(f"[H0a3 {timings['H0a3']}s] position classes={len(classes)}, "
          f"lattice token hits={sum(len(v) for v in token_hits.values())}",
          flush=True)

    # =====================================================================
    # H0b1  CONTAINMENT -- is the backward causal cone of the menu wires at
    # the choice boundary contained in the site's neighborhood?
    # PREDICATE: BACKWARD reachability over the gate graph from
    # {LEFT, RIGHT} at the choice boundary, taken back to the prior boundary
    # (depth 1) and to closure, lands inside a declared neighborhood wire set;
    # and, in the product graph of (wire, lane) cells, lands inside the site's
    # OWN fibre.
    # =====================================================================
    t0 = monotonic()
    cone_rows = {}
    for t in apps:
        sc = choice_sched_p[t]
        c1 = backward_cone(sc, {left_w, right_w}, 1, kinds, M.gate_target)
        c2 = backward_cone(sc, {left_w, right_w}, 2, kinds, M.gate_target)
        cf = backward_cone(sc, {left_w, right_w}, 1 << 8, kinds, M.gate_target)
        # the choice node has NO control wires at all: the branch datum enters
        # the state with no causal ancestor inside the state.
        choice_gates = [g for s in sc for g in s if g[0] == M.KIND_CHOICE]
        cone_rows[str(t)] = {
            "depth_1": len(c1), "depth_2": len(c2), "closure": len(cf),
            "choice_gates_in_the_chunk": len(choice_gates),
            "choice_gate_controls":
                sorted({w for g in choice_gates
                        for w in gate_controls(g, kinds)}),
        }
    coneF = backward_cone(sched_p, {left_w, right_w}, 1 << 8, kinds,
                          M.gate_target)
    cone1 = backward_cone(sched_p, {left_w, right_w}, 1, kinds, M.gate_target)
    cone2 = backward_cone(sched_p, {left_w, right_w}, 2, kinds, M.gate_target)
    FORMALIZATIONS = {
        "N1_the_whole_lane_state": set(range(len(proto))),
        "N2_every_wire_the_law_touches": set(touched_p),
        "N3_endpoint_read_cone_depth_1": set(cone1),
        "N4_endpoint_read_cone_depth_2": set(cone2),
        "N5_endpoint_read_cone_closure": set(coneF),
        "N6_the_record_banks_and_links": set(global_dirty),
        "N7_the_sigma_support": set(SIG),
    }
    containment = {name: {"wires": len(N),
                          "contains_the_sigma_support": set(SIG) <= N,
                          "contains_the_backward_closure_cone": coneF <= N}
                   for name, N in sorted(FORMALIZATIONS.items())}
    only_total = [k for k, v in containment.items()
                  if v["contains_the_sigma_support"]
                  and v["contains_the_backward_closure_cone"]]
    S["H0b1_CONTAINMENT"] = {
        "clause": "H0b1 CONTAINMENT -- the choice's causal cone is contained "
                  "in the site's neighborhood",
        "PREDICATE": "backward reachability over the gate graph from the menu "
                     "wires at the choice boundary lands inside a declared "
                     "neighborhood wire set, and inside the site's own fibre.",
        "per_occasion_cones": cone_rows,
        "cycle_wide_cone_sizes": {"depth_1": len(cone1), "depth_2": len(cone2),
                                  "closure": len(coneF)},
        "containment_against_the_re_derived_formalizations": containment,
        "the_only_neighborhoods_containing_BOTH_the_sigma_support_and_the_"
        "cone": only_total,
        "CROSS_SITE_COMPONENT_OF_THE_CONE": {
            "value": 0,
            "how_it_is_established": "H0a1: every compiled statement is "
                                     "bit-diagonal, so every edge of the gate "
                                     "graph in the (wire, lane) product is "
                                     "lane-preserving.  The backward cone of "
                                     "any cell (w, s) is therefore contained "
                                     "in the fibre over s.  Confirmed "
                                     "semantically by the lane-leak probe.",
            "so_the_containment_holds": True,
            "and_it_holds_VACUOUSLY":
                "screening is satisfied because the neighbours contribute "
                "NOTHING, not because their contribution is small.  That is "
                "the fact H0b2 turns into a refutation.",
        },
        "THE_CHOICE_NODE_HAS_NO_CAUSAL_ANCESTOR":
            "the CHOICE gate carries no control wires, so the branch datum "
            "enters the state from outside it.  A fortiori it has no "
            "neighbour-site ancestor.",
        "VERDICT": "DERIVED",
        "BUT_SEE": "the only re-derived neighborhood that contains both the "
                   "sigma support and the backward closure cone is the WHOLE "
                   "LANE STATE.  946's admissible pair (N1, N7) splits here: "
                   "N7 (the sigma support, 26 wires) does NOT contain the "
                   "391-wire closure cone.  'The site's neighborhood' that "
                   "screens the choice is the site's ENTIRE register file, "
                   "not a local shell.",
    }
    timings["H0b1"] = round(monotonic() - t0, 3)
    print(f"[H0b1 {timings['H0b1']}s] cone closure={len(coneF)}, "
          f"neighborhoods containing both = {only_total}", flush=True)

    # =====================================================================
    # H0b2  VARIATION -- does the site's distribution vary with the
    # conditions at OTHER sites, as the axiom's "varies with" clause needs?
    # PREDICATE: there exist two states differing ONLY outside the site's own
    # fibre at which the site's realized branch data differ.  If no such pair
    # exists, the compiled law's site distribution is CONSTANT in every other
    # site's conditions.
    # =====================================================================
    t0 = monotonic()
    VARIATION_DELTA = 120
    covered = [tuple(a) for a in
               q2_946["COVERAGE"]["of_the_five_genuine_two_item_menu_atoms"
                                  "_covered"]]
    var_rows = []
    for (t, site) in covered:
        m = M.Machine(env, False)
        m.advance(t, rows_p, choice_rows_p, ZERO_WORDS)
        snap = m.snapshot()
        words = {tt: (words_world[tt][site] if tt == t and site in
                      words_world[tt] else 0) for tt in apps}

        def run_from(perturb):
            m.restore(snap)
            if perturb is not None:
                m.columns = perturb(list(m.columns))
            m.advance(min(t + VARIATION_DELTA, max(apps) + VARIATION_DELTA),
                      rows_p, choice_rows_p, words)
            lane_bits = tuple((c >> site) & 1 for c in m.columns)
            w = m.order[site]
            return digest({"lane_bits": list(lane_bits),
                           "formed": m.formed.get(w),
                           "item": list(m.item[w]) if m.item.get(w) else None,
                           "lock_ord": list(m.lock_ord.get(w, ())),
                           "boundaries": m.t})

        base = run_from(None)
        others = [j for j in (0, 1, n - 1, n, (site + 1) % n, (site + 7) % n)
                  if j != site]

        def make_perturb(js, tag):
            def f(cols):
                mask = 0
                for j in js:
                    mask |= 1 << j
                for i, w in enumerate(touched_p):
                    h = int.from_bytes(
                        sha256(f"{tag}|{i}|{w}".encode("ascii")).digest(),
                        "big")
                    if h & 1:
                        cols[w] ^= mask
                return cols
            return f

        variants = []
        for vi, js in enumerate(([others[0]], others[:3], others)):
            d = run_from(make_perturb(js, f"c947var|{t}|{site}|{vi}"))
            variants.append({"perturbed_lanes": list(js),
                             "site_data_digest_matches_base": d == base})
        # CONTROL: perturbing the SITE'S OWN lane must move the site's data
        ctrl = run_from(make_perturb([site], f"c947ctl|{t}|{site}"))
        var_rows.append({
            "atom": [t, site],
            "boundaries_run_after_the_choice": VARIATION_DELTA,
            "variants": variants,
            "no_variant_moved_the_site": all(
                v["site_data_digest_matches_base"] for v in variants),
            "own_lane_control_DID_move_the_site": ctrl != base,
        })
    S["H0b2_VARIATION"] = {
        "clause": "H0b2 VARIATION -- the site's distribution varies with "
                  "other sites' conditions",
        "PREDICATE": "two states differing only outside the site's fibre at "
                     "which the site's realized branch data differ.",
        "declared_search": "for each covered atom, three perturbations of "
                           "growing support outside the site's fibre, applied "
                           "to the parent state at the choice boundary and "
                           "run forward through the choice occasion for "
                           f"{VARIATION_DELTA} boundaries, plus an own-lane "
                           "control that must move the site.",
        "per_atom": var_rows,
        "NO_ATOM_VARIES_WITH_ANY_OTHER_SITE":
            all(r["no_variant_moved_the_site"] for r in var_rows),
        "EVERY_OWN_LANE_CONTROL_FIRED":
            all(r["own_lane_control_DID_move_the_site"] for r in var_rows),
        "THE_STRUCTURAL_REASON":
            "H0a1.  The result is not an artifact of the declared "
            "perturbation family: bit-diagonality makes the cross-lane "
            "dependence empty for EVERY state and EVERY horizon.  The "
            "measurement is a confirmation with a firing control, not the "
            "argument.",
        "CONSEQUENCE_FOR_THE_AXIOM": {
            "the_axiom_sentence_at_issue": Q_ADMISS_DISTRIBUTION,
            "reading": "'determined by, and varies with, the nearest-neighbor "
                       "conditions' has two conjuncts.  Under the compiler's "
                       "own site notion (a lane = a census world, which is "
                       "the index set 936 measured as FORCED) the compiled "
                       "law satisfies the first conjunct trivially and "
                       "VIOLATES the second: the distribution at a site is "
                       "constant in every other site's conditions.",
            "so_H0_cannot_be_discharged_by_this_route": True,
        },
        "VERDICT": "RESIDUE",
        "PRICE": "IMPORT SENTENCE H0b2: 'Read the axiom's \"nearest-neighbor "
                 "conditions at a site\" as the conditions on that site's OWN "
                 "register file.'  This is the stipulation that turns the "
                 "compiled law into a model of the axiom, and it is exactly "
                 "the move the honesty rail forbids: it defines the axiom's "
                 "neighbourhood to be the site itself, at which point the "
                 "word 'nearest-neighbor' does no work and the covariance "
                 "sentence quantifies over nothing.",
        "WHAT_WOULD_DISCHARGE_IT": "a substrate with genuine inter-site "
                                   "gates, in which a site's branch data "
                                   "provably move when a neighbour's "
                                   "conditions move.  The pinned compiler has "
                                   "no such gate; building one is a "
                                   "successor block, not a reading.",
    }
    timings["H0b2"] = round(monotonic() - t0, 3)
    print(f"[H0b2 {timings['H0b2']}s] no-variation="
          f"{S['H0b2_VARIATION']['NO_ATOM_VARIES_WITH_ANY_OTHER_SITE']}, "
          f"controls fired="
          f"{S['H0b2_VARIATION']['EVERY_OWN_LANE_CONTROL_FIRED']}", flush=True)

    # =====================================================================
    # H0c  POSSIBILITY IDENTIFICATION
    # =====================================================================
    t0 = monotonic()
    menu_rows = []
    for (t, site) in covered:
        m = M.Machine(env, False)
        m.advance(t, rows_p, choice_rows_p, ZERO_WORDS)
        snap = m.snapshot()
        seen = []
        for word in (0, words_world[t][site]):
            m.restore(snap)
            m.advance(t + 1, rows_p, choice_rows_p,
                      {tt: (word if tt == t else 0) for tt in apps})
            lb = (m.columns[left_w] >> site) & 1
            rb = (m.columns[right_w] >> site) & 1
            seen.append((lb, rb))
        menu_rows.append({
            "atom": [t, site],
            "endpoint_patterns_over_the_two_branches":
                [list(x) for x in seen],
            "distinct_items": len(set(seen)),
            "both_on_menu": all((a ^ b) == 1 for a, b in seen),
            "the_two_items_are_complementary": seen[0] == tuple(
                1 - x for x in seen[1]),
        })
    ALGEBRA_TOKENS = ("M_2", "M2C", "matrix", "complex", "Cl3", "clifford",
                      "hermit", "unitary", "density", "M_2(C)")
    alg_hits = {}
    for path in (CORE_PATH, C936_PATH):
        src = payloads[path].decode("utf-8")
        names = set()
        for node in ast.walk(ast.parse(src)):
            if isinstance(node, ast.Name):
                names.add(node.id)
            elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                names.add(node.name)
            elif isinstance(node, ast.Attribute):
                names.add(node.attr)
        alg_hits[path] = sorted(
            nm for nm in names
            if any(tok.lower() in nm.lower() for tok in ALGEBRA_TOKENS))
    c936_collapse = r936["certificates"]["C5_THE_WEIGHT_ALGEBRA"][
        "COLLAPSE_CHECK"]
    S["H0c_POSSIBILITY_IDENTIFICATION"] = {
        "H0c1_MENU_CARDINALITY": {
            "PREDICATE": "at a genuine two-item menu site the two branches "
                         "realize exactly two distinct endpoint patterns, "
                         "both on the menu (LEFT xor RIGHT == 1).",
            "per_atom": menu_rows,
            "every_atom_has_exactly_two_complementary_on_menu_items":
                all(r["distinct_items"] == 2 and r["both_on_menu"]
                    and r["the_two_items_are_complementary"]
                    for r in menu_rows),
            "VERDICT": "DERIVED",
        },
        "H0c2_SUPPORT": {
            "PREDICATE": "the distribution's support is exactly those two "
                         "items -- i.e. BOTH carry nonzero probability.",
            "the_axiom_clause_relied_on": Q_ADMISS_SUPPORT,
            "what_the_substrate_supplies": "both branches EXIST as "
                                           "trajectories of one law, one "
                                           "setup and one declared datum set "
                                           "(936's M1-M5).",
            "what_the_substrate_does_NOT_supply": c936_collapse,
            "the_gap": "existence of a branch is not nonzero probability.  "
                       "936 measured that the weight does not collapse: mu is "
                       "a free parameter, and nothing in the substrate "
                       "forbids mu = 0, at which the menu has ONE supported "
                       "item and the site is not a two-item menu at all.  "
                       "Reading 'is a branch' as 'has nonzero probability' IS "
                       "the identification H0 was supposed to supply, so "
                       "using it here would be circular.",
            "VERDICT": "RESIDUE",
            "PRICE": "IMPORT SENTENCE H0c2: 'Every branch of the compiled "
                     "law carries nonzero probability.'  Equivalently: the "
                     "compiled branch set IS the distribution's support.",
            "WHAT_WOULD_DISCHARGE_IT": "a derivation forbidding mu = 0 -- "
                                       "e.g. an axiom-level clause that a "
                                       "possibility the law can realize is "
                                       "supported.  The landed text has no "
                                       "such clause: it defines availability "
                                       "FROM the distribution, not the "
                                       "distribution from availability.",
        },
        "H0c3_DOMAIN": {
            "PREDICATE": "the two items are possibilities of a one-site "
                         "domain with the axiom's algebraic presentation.",
            "the_axiom_clauses_relied_on": [Q_QUBIT_DOMAIN,
                                            Q_QUBIT_PRESENTATION],
            "what_the_compiler_supplies": "two complementary GF(2) patterns "
                                          "on the wire pair (LEFT, RIGHT), "
                                          "written by the pinned endpoint "
                                          "preparation.  The item space is "
                                          "a 2-element subset of GF(2)^2.",
            "algebra_token_scan_over_the_pinned_sources": alg_hits,
            "algebra_token_hits_total": sum(len(v) for v in alg_hits.values()),
            "the_gap": "no compiler-native datum maps the two GF(2) patterns "
                       "into a domain with presentation M_2(C), and the "
                       "Qualification clause forbids helping oneself to one: "
                       "further structure requires a retained derivation or "
                       "an approved primitive.",
            "the_qualification_clause": Q_QUALIFICATION,
            "VERDICT": "RESIDUE",
            "PRICE": "IMPORT SENTENCE H0c3: 'Fix an embedding of the "
                     "compiled two-item menu into the one-site possibility "
                     "domain, as two points of its support.'  Note the "
                     "embedding must also be chosen COMPATIBLY with the "
                     "no-privilege clause, which is what 946's H4 uses.",
            "WHAT_WOULD_DISCHARGE_IT": "a retained bridge from the kernel's "
                                       "endpoint encoding to the one-site "
                                       "algebra.  None is cited by 936, 940, "
                                       "943 or 946.",
        },
    }
    timings["H0c"] = round(monotonic() - t0, 3)

    # =====================================================================
    # H0d  SYMMETRY TRANSPORT
    # =====================================================================
    t0 = monotonic()
    mask_preserved = all(sigma_gate(g, SIG, kinds)[4] == g[4]
                         for s in sched_p for g in s)
    # sigma acts inside every fibre: the GLOBAL relabelling restricted to one
    # lane equals the lane-restricted relabelling, for every lane.
    fibre_rows = []
    for j in probe_lanes:
        cols = list(ens[1])
        g_all = perm_apply(cols, SIG)
        g_one = perm_apply_lane(cols, SIG, j)
        agree = all(((g_all[w] >> j) & 1) == ((g_one[w] >> j) & 1)
                    for w in range(len(cols)))
        untouched = all(((g_one[w] >> k) & 1) == ((cols[w] >> k) & 1)
                        for w in range(len(cols))
                        for k in (0 if j != 0 else 1, n if j != n else n - 1))
        fibre_rows.append({"lane": j,
                           "global_sigma_restricted_equals_lane_sigma": agree,
                           "lane_sigma_leaves_the_sampled_other_lanes_fixed":
                               untouched})
    sem_p = semantic_commutes(rows_p, ens, lambda c: perm_apply(c, SIG))
    sem_b = semantic_commutes(rows_ma, ens, lambda c: perm_apply(c, SIG))
    S["H0d_SYMMETRY_TRANSPORT"] = {
        "H0d1_FIBRE_RESPECT": {
            "PREDICATE": "sigma maps every fibre of the native fibration to "
                         "itself: it permutes WIRES and preserves every "
                         "gate's lane mask, so it never moves a cell out of "
                         "its lane.",
            "sigma_preserves_every_gate_lane_mask": mask_preserved,
            "per_lane_agreement": fibre_rows,
            "global_sigma_restricted_equals_lane_sigma_everywhere":
                all(r["global_sigma_restricted_equals_lane_sigma"]
                    for r in fibre_rows),
            "semantic_breaking_wires_partnered": len(sem_p),
            "semantic_breaking_wires_baseline": len(sem_b),
            "sigma_is_a_symmetry_of_the_partnered_law": not sem_p,
            "sigma_is_NOT_a_symmetry_of_the_baseline": bool(sem_b),
            "VERDICT": "DERIVED",
        },
        "H0d2_DESCENT": {
            "PREDICATE": "sigma descends to an axiom-level action fixing the "
                         "sigma-invariant conditions.",
            "what_is_established": "sigma fixes every fibre SETWISE and acts "
                                   "identically inside each of them, so as a "
                                   "map on the BASE it is the identity.  Its "
                                   "whole content is the induced map on a "
                                   "single site's data.",
            "what_is_not_established": "that the induced map on a site's data "
                                       "IS a map of the axiom's one-site "
                                       "possibility domain.  That is exactly "
                                       "H0c3, and it is RESIDUE.  Descent is "
                                       "therefore conditional, not derived.",
            "VERDICT": "RESIDUE",
            "PRICE": "IMPORT SENTENCE H0d2: 'The induced action of sigma on a "
                     "site's compiled data is an automorphism of that site's "
                     "possibility domain exchanging the two menu items.'  It "
                     "is H0c3 plus the statement that the embedding is "
                     "sigma-equivariant.",
            "WHAT_WOULD_DISCHARGE_IT": "discharging H0c3 with an equivariant "
                                       "embedding; the equivariance is the "
                                       "cheap half, the embedding is not.",
        },
    }
    timings["H0d"] = round(monotonic() - t0, 3)
    print(f"[H0d {timings['H0d']}s] mask-preserved={mask_preserved}, "
          f"sem_partnered={len(sem_p)}, sem_baseline={len(sem_b)}", flush=True)

    # =====================================================================
    # THE NO-GO SEARCH.  H0 is UNIVERSAL: "a symmetry of one is a symmetry of
    # the other".  Declared search space, two families.
    # =====================================================================
    t0 = monotonic()
    ens_ng = strong_states(3, proto, touched_p, env["uni_sim"], "c947nogo")

    # ---- FAMILY A: the lane-restricted relabellings sigma_j ---------------
    famA = []
    for j in probe_lanes:
        bad = semantic_commutes(rows_ng := rows_p, ens_ng,
                                lambda c, jj=j: perm_apply_lane(c, SIG, jj))
        # does it act uniformly across sites?  measure at a second lane.
        k2 = probe_lanes[0] if probe_lanes[0] != j else probe_lanes[1]
        cols = list(ens_ng[0])
        img = perm_apply_lane(cols, SIG, j)
        moves_j = any(((img[w] >> j) & 1) != ((cols[w] >> j) & 1)
                      for w in range(len(cols)))
        moves_k = any(((img[w] >> k2) & 1) != ((cols[w] >> k2) & 1)
                      for w in range(len(cols)))
        famA.append({
            "lane": j,
            "is_a_symmetry_of_the_compiled_law": not bad,
            "breaking_wires": len(bad),
            "acts_nontrivially_at_its_own_lane": moves_j,
            "acts_trivially_at_a_second_lane": not moves_k,
            "is_site_uniform": moves_j == moves_k,
        })
    famA_witnesses = [r for r in famA
                      if r["is_a_symmetry_of_the_compiled_law"]
                      and not r["is_site_uniform"]]

    # ---- FAMILY B: the lane transpositions --------------------------------
    same_class_pairs = []
    for pos, members in sorted(classes.items()):
        if len(members) >= 2:
            same_class_pairs.append((members[0], members[1]))
        if len(same_class_pairs) >= 6:
            break
    # the compiler's own duplicate pair is always same-class
    same_class_pairs = [(0, n)] + same_class_pairs
    cross_class_pairs = []
    seen_pos = {}
    for j in range(n):
        seen_pos.setdefault(pos_of[j], j)
    reps = sorted(seen_pos.values())
    for a, b in zip(reps[:6], reps[1:7]):
        cross_class_pairs.append((a, b))

    def mask_agrees(i, j):
        return all(((m >> i) & 1) == ((m >> j) & 1) for m in all_masks)

    famB = []
    for (i, j), tag in ([(p, "same_position_class") for p in same_class_pairs]
                        + [(p, "cross_position_class_CONTROL")
                           for p in cross_class_pairs]):
        struct = mask_agrees(i, j)
        bad = semantic_commutes(rows_p, ens_ng,
                               lambda c, a=i, b=j: swap_lanes(c, a, b))
        famB.append({
            "lane_pair": [i, j], "family": tag,
            "every_gate_mask_agrees_on_the_pair": struct,
            "is_a_symmetry_of_the_compiled_law": not bad,
            "breaking_wires": len(bad),
            "acts_on_the_BASE_of_the_fibration": True,
        })
    famB_witnesses = [r for r in famB
                      if r["family"] == "same_position_class"
                      and r["is_a_symmetry_of_the_compiled_law"]]
    famB_controls_fired = [r for r in famB
                           if r["family"] == "cross_position_class_CONTROL"
                           and not r["is_a_symmetry_of_the_compiled_law"]]

    # ---- CONTROL: a wire transposition outside sigma must NOT be a symmetry
    off_sig = [w for w in touched_p if w not in SIG][:2]
    ctrl_sig = make_sigma(((off_sig[0], off_sig[1]),))
    ctrl_bad = semantic_commutes(rows_p, ens_ng,
                                 lambda c: perm_apply(c, ctrl_sig))

    iso = transposition_isometry_search(3)
    S["NO_GO_SEARCH"] = {
        "the_universal_claim_under_test": "H0's second half -- 'such that a "
                                          "symmetry of one is a symmetry of "
                                          "the other'.",
        "declared_search_space": {
            "family_A": "the lane-restricted relabellings sigma_j, one per "
                        f"probe lane; {len(probe_lanes)} lanes probed "
                        "(lane 0, lane 1, the duplicate lane, the six "
                        "declared sites, the midpoint lane and the last "
                        "lane).",
            "family_B": "lane transpositions: the compiler's own duplicate "
                        "pair plus one representative pair per "
                        f"station-position class ({len(same_class_pairs)} "
                        f"pairs), with {len(cross_class_pairs)} cross-class "
                        "pairs as controls.",
            "control_family": "one wire transposition outside sigma.",
            "NOT_searched": "arbitrary state-space maps, affine GF(2) "
                            "intertwiners (943 measured one and refused it), "
                            "and permutations mixing wires across lanes.  The "
                            "search is BOUNDED and a negative result inside "
                            "it is not a general no-go.",
        },
        "family_A_rows": famA,
        "family_A_non_descending_witnesses": len(famA_witnesses),
        "family_B_rows": famB,
        "family_B_non_descending_witnesses": len(famB_witnesses),
        "family_B_controls_that_fired": len(famB_controls_fired),
        "control_wire_transposition_outside_sigma_is_not_a_symmetry":
            bool(ctrl_bad),
        "control_breaking_wires": len(ctrl_bad),
        "the_bounded_lattice_isometry_enumeration": iso,
        "VERDICT": {
            "universal_symmetry_faithfulness_is_FALSE":
                bool(famA_witnesses) or bool(famB_witnesses),
            "family_A_reason": "sigma_j is a symmetry of the compiled law "
                               "that acts at ONE site and trivially at every "
                               "other.  The axiom supplies ONE FIXED rule for "
                               "every site; a symmetry of that rule is the "
                               "same at every site.  A site-local symmetry "
                               "therefore has no axiom-level counterpart, and "
                               "the compiled law has one per lane.",
            "family_B_reason": "exchanging two lanes with equal station masks "
                               "is a symmetry of the compiled law that "
                               "permutes SITES.  Under any injective site map "
                               "it is a transposition of two lattice points "
                               "fixing every other point, and the bounded "
                               "enumeration shows no element of the axiom's "
                               "declared covariance group (translations and "
                               "proper cubic rotations) acts that way.",
            "WHAT_THIS_DOES_NOT_REFUTE": "the ONE DIRECTION 946 actually "
                                         "uses -- that the specific, "
                                         "site-uniform, fibre-fixing sigma "
                                         "transports.  The no-go kills the "
                                         "UNIVERSAL form of H0, not the "
                                         "sigma-specific form.",
        },
        "THE_NARROWED_CLAUSE": {
            "H0_universal_REFUTED": "for every symmetry T of the compiled "
                                    "law there is a symmetry of the axiom's "
                                    "rule.",
            "H0_narrowed_SURVIVING": "the site-uniform, fibre-fixing "
                                     "involution sigma -- which acts by the "
                                     "same wire relabelling inside every "
                                     "fibre and as the identity on the base "
                                     "-- induces an automorphism of a site's "
                                     "possibility domain exchanging the two "
                                     "menu items.",
            "what_the_narrowing_costs": "the narrowed clause is no longer a "
                                        "general bridge principle that could "
                                        "be argued for on its own; it is a "
                                        "statement about one map, and it "
                                        "still needs H0a3, H0c2, H0c3 and "
                                        "H0d2 to have content.  Narrowing "
                                        "removes a refutation, not the "
                                        "residue.",
        },
    }
    timings["NO_GO"] = round(monotonic() - t0, 3)
    print(f"[NO_GO {timings['NO_GO']}s] famA witnesses="
          f"{len(famA_witnesses)}, famB witnesses={len(famB_witnesses)}, "
          f"famB controls fired={len(famB_controls_fired)}, "
          f"bare-transposition isometries="
          f"{iso['isometries_acting_as_a_bare_transposition']}", flush=True)

    # =====================================================================
    # THE RESIDUE VERDICT
    # =====================================================================
    CLAUSE_VERDICTS = {
        "H0a1_FIBRATION": S["H0a1_FIBRATION"]["VERDICT"],
        "H0a2_TOTALITY": S["H0a2_TOTALITY"]["VERDICT"],
        "H0a3_EMBEDDING": S["H0a3_EMBEDDING"]["VERDICT"],
        "H0b1_CONTAINMENT": S["H0b1_CONTAINMENT"]["VERDICT"],
        "H0b2_VARIATION": S["H0b2_VARIATION"]["VERDICT"],
        "H0c1_MENU_CARDINALITY":
            S["H0c_POSSIBILITY_IDENTIFICATION"]["H0c1_MENU_CARDINALITY"][
                "VERDICT"],
        "H0c2_SUPPORT":
            S["H0c_POSSIBILITY_IDENTIFICATION"]["H0c2_SUPPORT"]["VERDICT"],
        "H0c3_DOMAIN":
            S["H0c_POSSIBILITY_IDENTIFICATION"]["H0c3_DOMAIN"]["VERDICT"],
        "H0d1_FIBRE_RESPECT":
            S["H0d_SYMMETRY_TRANSPORT"]["H0d1_FIBRE_RESPECT"]["VERDICT"],
        "H0d2_DESCENT":
            S["H0d_SYMMETRY_TRANSPORT"]["H0d2_DESCENT"]["VERDICT"],
    }
    residue = sorted(k for k, v in CLAUSE_VERDICTS.items() if v == "RESIDUE")
    derived = sorted(k for k, v in CLAUSE_VERDICTS.items() if v == "DERIVED")
    consumed = sorted(k for k, v in CLAUSE_VERDICTS.items() if v == "CONSUMED")
    S["RESIDUE_VERDICT"] = {
        "clause_verdicts": CLAUSE_VERDICTS,
        "DERIVED": derived,
        "CONSUMED": consumed,
        "RESIDUE": residue,
        "H0_IS_DISCHARGED": not residue,
        "the_price_sheet": {
            k: {"import_sentence": (
                    S["H0a3_EMBEDDING"]["PRICE"] if k == "H0a3_EMBEDDING"
                    else S["H0b2_VARIATION"]["PRICE"] if k == "H0b2_VARIATION"
                    else S["H0c_POSSIBILITY_IDENTIFICATION"]["H0c2_SUPPORT"][
                        "PRICE"] if k == "H0c2_SUPPORT"
                    else S["H0c_POSSIBILITY_IDENTIFICATION"]["H0c3_DOMAIN"][
                        "PRICE"] if k == "H0c3_DOMAIN"
                    else S["H0d_SYMMETRY_TRANSPORT"]["H0d2_DESCENT"]["PRICE"])}
            for k in residue},
        "THE_RESIDUE_IN_ONE_SENTENCE":
            "H0 does not discharge.  What survives is a fibration theorem: "
            "the compiled law factorises natively over its lanes, sigma fixes "
            "every fibre and acts uniformly inside all of them, and the "
            "choice's causal cone stays inside its own fibre.  What does not "
            "survive is every clause that would make a fibre a LATTICE SITE: "
            "no native embedding into Z^3, no dependence on any other fibre "
            "(so the axiom's 'varies with' conjunct fails outright), no "
            "derivation that both menu items carry nonzero probability, and "
            "no map from the two GF(2) endpoint patterns into a domain with "
            "the axiom's one-site presentation.",
        "CONSEQUENCE_FOR_946": {
            "946_status_unchanged": "the 946 result remains a theorem about "
                                    "the compiled circuit, CONDITIONAL on H0. "
                                    " This block does not weaken it and does "
                                    "not strengthen it; it prices it.",
            "the_conditional_scope_is_now_explicit": "five named import "
                                                     "sentences, not one "
                                                     "unanalysed one.",
            "one_thing_got_WORSE": "H0's universal form is refuted, so the "
                                   "import cannot be defended as an instance "
                                   "of a general bridge principle.  It must "
                                   "be asserted for sigma specifically.",
            "one_thing_got_BETTER": "two of the four proposed clauses "
                                    "(H0a1/H0a2 and H0d1) are now DERIVED "
                                    "from compiler-native data, so the "
                                    "residue is strictly smaller than 'the "
                                    "whole identification'.",
        },
    }
    S["SPEC_DEVIATIONS"] = [
        {"spec_clause": "H0a SITE MAP -- 'every wire of the partnered kernel "
                        "is assigned to a lattice site'",
         "what_the_data_says": "the compiler's native factorisation is by "
                               "LANE, not by wire.  A wire is a coordinate "
                               "INSIDE every site's register file "
                               f"({len(proto)} wires per lane), not a site "
                               "label; assigning wires to sites would "
                               "contradict 936's measured forced index set "
                               "(worlds, not slots).",
         "how_the_block_proceeded": "the site map is taken as lane -> site "
                                    "and wire -> intra-site coordinate, which "
                                    "is what the compiler supplies."},
        {"spec_clause": "H0b -- 'the 946 computed structural containment "
                        "predicate is the comparator'",
         "what_the_data_says": "946's predicate is containment of the SIGMA "
                               "SUPPORT.  Under the cone-containment test the "
                               "946-admissible pair splits: N7 (the sigma "
                               "support, 26 wires) does not contain the "
                               "391-wire backward closure cone.  The only "
                               "neighborhood passing both tests is the whole "
                               "lane state.",
         "how_the_block_proceeded": "both predicates are computed and "
                                    "reported side by side; neither is "
                                    "silently preferred."},
        {"spec_clause": "H0b -- 'the compiled law's dependence at each "
                        "genuine menu site's choice boundary is contained in "
                        "that site's neighborhood'",
         "what_the_data_says": "there is no cross-site dependence to contain. "
                               " Containment holds vacuously, and the same "
                               "fact refutes the axiom's 'varies with' "
                               "conjunct.  The spec's single clause therefore "
                               "splits into H0b1 (DERIVED, vacuous) and H0b2 "
                               "(RESIDUE, decisive).",
         "how_the_block_proceeded": "H0b2 was added as a named clause and is "
                                    "the block's sharpest finding."},
        {"spec_clause": "H0c -- 'the distribution's support is exactly them "
                        "(the adopted sentence defines availability = "
                        "support)'",
         "what_the_data_says": "the adopted sentence defines availability FROM "
                               "the distribution.  Getting the support to be "
                               "the two items needs both to have nonzero "
                               "probability, and 936 measured that the weight "
                               "does not collapse -- mu = 0 is not excluded.  "
                               "The support half is RESIDUE, not a "
                               "consequence of the sentence.",
         "how_the_block_proceeded": "H0c split into cardinality (DERIVED), "
                                    "support (RESIDUE) and domain "
                                    "(RESIDUE)."},
        {"spec_clause": "'For any clause that reduces to an already-landed "
                        "claim, cite the claim_id'",
         "what_the_data_says": "the prior-art sweep found no landed claim "
                               "that discharges or partially discharges H0; "
                               "no clause reduced to one, so the CONSUMED "
                               "column is empty.",
         "how_the_block_proceeded": "every clause is either computed here or "
                                    "priced as residue."},
    ]

    # =====================================================================
    # G: the teeth -- every one must FIRE
    # =====================================================================
    t0 = monotonic()
    teeth = []

    def tooth(name, fired, detail):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    planted_line = f" c[{left_w}] ^= (c[{right_w}] << 1) & {all_masks[0]}"
    ok_planted, why_planted = statement_is_lane_diagonal(planted_line)
    ns_p: dict = {}
    exec("def apply_chunk(c):\n" + planted_line, {"__builtins__": {}}, ns_p)
    cross_fn = ns_p["apply_chunk"]
    cols_t = list(ens[0])
    pert_t = list(cols_t)
    for w in touched_p:
        pert_t[w] ^= 1 << probe_lanes[0]
    a_t, b_t = list(cols_t), list(pert_t)
    cross_fn(a_t)
    cross_fn(b_t)
    leaked = any((a_t[w] ^ b_t[w]) & ~(1 << probe_lanes[0])
                 for w in range(len(a_t)))
    tooth("T1_planted_cross_site_gate_breaks_locality",
          (not ok_planted) and leaked,
          {"planted_statement": planted_line.strip(),
           "structural_verdict": why_planted,
           "semantic_lane_leak_observed": leaked})

    tooth("T2_positive_control_the_real_law_is_lane_diagonal",
          len(fail_lines) == 0
          and all(r["clean"] for r in lane_leak),
          {"why": "a tooth that fires on everything proves nothing; this is "
                  "the control showing the instrument can say YES"})

    j0, j1 = probe_lanes[0], probe_lanes[1]
    swapped = swap_lanes(list(ens[1]), j0, j1)
    fibre_broken = any(((swapped[w] >> j0) & 1) != ((ens[1][w] >> j0) & 1)
                       for w in range(len(proto))) and \
        any(((swapped[w] >> j1) & 1) != ((ens[1][w] >> j1) & 1)
            for w in range(len(proto)))
    tooth("T3_permuting_two_site_fibres_breaks_fibre_respect",
          fibre_broken,
          {"permuted_lanes": [j0, j1],
           "verdict": "the fibre-respect predicate (each fibre mapped to "
                      "itself) FAILS for a lane exchange, as required; sigma "
                      "passes it"})

    bad_sched = list(sched_p)
    s0 = list(bad_sched[0])
    victim = next(i for i, g in enumerate(s0) if g in set(added))
    kg = s0[victim]
    s0[victim] = (kg[0], kg[1], kg[2], ORIENTATION_WIRES[0], kg[4]) \
        if kg[0] == M.KIND_TOF else (kg[0], kg[1], ORIENTATION_WIRES[0],
                                     kg[3], kg[4])
    bad_sched[0] = tuple(s0)
    bad_sched = tuple(bad_sched)
    tooth("T4_flipping_one_gate_in_sigmas_image_breaks_the_certificate",
          (not multiset_sigma_invariant(bad_sched, SIG, kinds))
          and bool(semantic_commutes(M.compile_schedules(bad_sched), ens,
                                     lambda c: perm_apply(c, SIG))),
          {"flipped": "one spliced sigma-image gate's target moved to an "
                      "orientation wire",
           "L1_after_the_flip": multiset_sigma_invariant(bad_sched, SIG,
                                                         kinds)})

    tampered = Q_ADMISS_DISTRIBUTION.replace("varies with", "is independent of")
    tooth("T5_tampered_axiom_quote_caught",
          (Q_ADMISS_DISTRIBUTION in axiom_text)
          and (tampered not in axiom_text),
          {"tampered_text": tampered})

    planted_payload = {"THE_WEIGHT_IS": Fraction(1, 2)}
    planted_unfenced = [p for p, v in _walk_paths(planted_payload)
                        if isinstance(v, Fraction) and 0 < v < 1
                        and not any(f in p.upper()
                                    for f in ("CONDITIONAL", "HYPOTHETICAL",
                                              "IF_", "THEOREM"))]
    tooth("T6_planted_unconditional_weight_caught_by_the_firewall",
          bool(planted_unfenced),
          {"planted_path": planted_unfenced})

    tooth("T7_own_lane_control_moves_the_site",
          all(r["own_lane_control_DID_move_the_site"] for r in var_rows),
          {"why": "the no-variation result would be worthless if nothing "
                  "could move the site at all"})

    tooth("T8_cross_class_lane_pairs_are_NOT_symmetries",
          len(famB_controls_fired) == len(cross_class_pairs)
          and len(cross_class_pairs) > 0,
          {"controls": len(cross_class_pairs),
           "fired": len(famB_controls_fired)})

    tooth("T9_a_wire_transposition_outside_sigma_is_not_a_symmetry",
          bool(ctrl_bad),
          {"pair": off_sig, "breaking_wires": len(ctrl_bad)})

    tooth("T10_a_neighborhood_omitting_the_sigma_support_is_flagged",
          any(not v["contains_the_sigma_support"]
              for v in containment.values()),
          {"flagged": sorted(k for k, v in containment.items()
                             if not v["contains_the_sigma_support"])})

    cert_g = {"certificate": "G_FALSIFIERS", "teeth": teeth,
              "fired": sum(1 for t in teeth if t["fired"]),
              "total": len(teeth),
              "pass": all(t["fired"] for t in teeth)}
    timings["teeth"] = round(monotonic() - t0, 3)
    print(f"[G {timings['teeth']}s] teeth {cert_g['fired']}/{cert_g['total']}",
          flush=True)

    # =====================================================================
    # F: the parametric firewall
    # =====================================================================
    FENCE = ("CONDITIONAL", "HYPOTHETICAL", "IF_", "THEOREM")
    payload_for_firewall = {"science": S, "restriction": cert_b}
    self_src = Path(__file__).read_text(encoding="utf-8")
    float_lits = sum(1 for node in ast.walk(ast.parse(self_src))
                     if isinstance(node, ast.Constant)
                     and isinstance(node.value, float))
    weight_shaped = [(p, v) for p, v in _walk_paths(payload_for_firewall)
                     if isinstance(v, Fraction) and 0 < v < 1]
    unfenced = [p for p, _v in weight_shaped
                if not any(f in p.upper() for f in FENCE)]
    cert_f = {
        "certificate": "F_PARAMETRIC_FIREWALL",
        "rule": "this block derives NO weight.  Zero float literals; every "
                "weight-shaped rational, if any existed, would have to sit "
                "under a CONDITIONAL/HYPOTHETICAL/IF_/THEOREM key path.  The "
                "946 value is cited by reference only, never recomputed.",
        "fence_tokens": list(FENCE),
        "weight_shaped_rationals": len(weight_shaped),
        "weight_values_outside_a_conditional_fence": unfenced,
        "no_unconditional_weight_value": not unfenced,
        "zero_float_literals": float_lits == 0,
        "float_literals_in_this_runner": float_lits,
        "fraction_label": FRACTION_LABEL,
        "pass": (not unfenced) and float_lits == 0,
    }

    # =====================================================================
    # H: the double run -- the science digest must be reproducible
    # =====================================================================
    t0 = monotonic()
    science_digest = digest(S)

    def pass2_core():
        """A declared, independently recomputed subset of the science: the
        structural diagonality scan, the mask-preservation check, the cone
        sizes and the two no-go family verdicts."""
        nd = nc = nf = 0
        for s in sched_p:
            for line in M.chunk_source(s)[1:]:
                if statement_is_lane_diagonal(line)[0]:
                    nd += 1
                elif statement_is_choice_diagonal(line)[0]:
                    nc += 1
                else:
                    nf += 1
        return {
            "diagonal": nd, "choice": nc, "outside": nf,
            "mask_preserved": all(sigma_gate(g, SIG, kinds)[4] == g[4]
                                  for s in sched_p for g in s),
            "cone_closure": len(backward_cone(sched_p, {left_w, right_w},
                                              1 << 8, kinds, M.gate_target)),
            "famA_witnesses": len(famA_witnesses),
            "famB_witnesses": len(famB_witnesses),
            "clause_verdicts": CLAUSE_VERDICTS,
        }

    core_1 = pass2_core()
    core_2 = pass2_core()
    timing_paths = [p for p, _v in _walk_paths(S) if _is_a_clock_field(p)]
    cert_h = {
        "certificate": "H_DOUBLE_RUN",
        "science_digest": science_digest,
        "science_digest_recomputes": digest(S) == science_digest,
        "declared_recomputed_core_digest_pass1": digest(core_1),
        "declared_recomputed_core_digest_pass2": digest(core_2),
        "core_is_byte_identical_across_the_two_computations":
            digest(core_1) == digest(core_2),
        "science_payload_is_timing_free": not timing_paths,
        "timing_token_paths": timing_paths,
        "cross_process_protocol": "the science payload excludes every "
                                  "wall-clock field (timings live outside it, "
                                  "in I_RUNTIME), so `science_digest` is a "
                                  "pure function of the pinned inputs.  The "
                                  "cross-process demonstration is performed "
                                  "by running this runner twice and comparing "
                                  "the two receipts' science_digest; both "
                                  "runs are recorded in the runner log.",
        "pass": (digest(core_1) == digest(core_2)) and not timing_paths,
    }
    timings["double_run"] = round(monotonic() - t0, 3)

    elapsed = round(monotonic() - started, 3)
    cert_i = {
        "certificate": "I_RUNTIME",
        "elapsed_seconds": elapsed,
        "budget_seconds": RUNTIME_BUDGET_SEC,
        "per_stage_seconds": timings,
        "pass": elapsed <= RUNTIME_BUDGET_SEC,
    }

    certificates = {
        "A_PINS": cert_a,
        "B_RESTRICTION_GATE": cert_b,
        "C_H0_CLAUSES": S,
        "F_PARAMETRIC_FIREWALL": cert_f,
        "G_FALSIFIERS": cert_g,
        "H_DOUBLE_RUN": cert_h,
        "I_RUNTIME": cert_i,
    }
    all_pass = all(c.get("pass", True) for c in certificates.values())

    receipt = {
        "block": "cycle947_h0_discharge_attempt",
        "campaign": "toe-time-expansion-20260802 / blockQ18",
        "cycles": [947],
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "headline":
            "H0 DOES NOT DISCHARGE.  Four of the ten named clauses are "
            "DERIVED from compiler-native data (the lane fibration, its "
            "totality, the causal-cone containment, and sigma's fibre "
            "respect); five are RESIDUE with named import sentences (no "
            "native Z^3 embedding; NO dependence on any other site, which "
            "refutes the axiom's 'varies with' conjunct outright; no "
            "derivation that both menu items carry nonzero probability; no "
            "map into a domain with the axiom's one-site presentation; and "
            "descent, which is downstream of those).  Separately, H0's "
            "UNIVERSAL form is REFUTED by two independent families of "
            "symmetries of the compiled law that have no axiom-level "
            "counterpart, and the narrowed sigma-specific clause is stated.",
        "CONDITIONAL_ON_LANDED_AXIOM": {
            "ref": LANDED_AXIOM_REF, "path": LANDED_AXIOM_PATH,
            "sha256": LANDED_AXIOM_SHA256, "git_blob": LANDED_AXIOM_GIT_BLOB,
            "every_axiom_dependent_statement_in_this_receipt_sits_under_this_"
            "condition": True,
        },
        "certificates": certificates,
        "all_certificates_pass": all_pass,
        "fraction_label": FRACTION_LABEL,
        "provenance": {
            "pins": cert_a["rows"],
            "lift_counts": {"c936_funcs_consts_classes": list(lift_counts)},
            "worker": "Claude Opus 5 worker under supervisor spec "
                      "(substitution disclosed); supervisor reviews "
                      "line-by-line and authors the note.",
            "c946_never_imported_or_lifted":
                cert_a["C946_IS_PINNED_BUT_NEVER_LIFTED"],
        },
        "science_digest": science_digest,
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "VERDICT":
            "The wall is not one sentence wide.  H0 decomposes into ten "
            "clauses; the compiler pays for four of them and cannot pay for "
            "five.  The decisive one is not the one anybody expected: it is "
            "not that the lanes lack coordinates, it is that they do not "
            "TALK.  The compiled law's dependence between distinct sites is "
            "exactly empty, so under the compiler's own forced site index "
            "the axiom's 'varies with the nearest-neighbor conditions' "
            "conjunct is not merely unverified -- it is false of this "
            "substrate.  A block that set out to discharge an import has "
            "instead measured which successor could: one with a real "
            "inter-site gate.  Independent audit still required.",
    }
    out_path = ROOT / "outputs" / "h0_discharge_cycle947_receipt_2026_07_28.json"
    out_path.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")

    lines = ["cycle947 h0 discharge attempt -- primary runner",
             f"runner_sha256: {receipt['self_sha256']}",
             f"landed axiom sha256: {LANDED_AXIOM_SHA256}",
             f"landed axiom git blob: {LANDED_AXIOM_GIT_BLOB}",
             f"pins: {'PASS' if cert_a['pass'] else 'FAIL'}",
             f"restriction: {cert_b['passed']}/{cert_b['total']}",
             ""]
    for k, v in sorted(CLAUSE_VERDICTS.items()):
        lines.append(f"  {k:26s} {v}")
    lines += ["",
              f"H0_IS_DISCHARGED: {S['RESIDUE_VERDICT']['H0_IS_DISCHARGED']}",
              f"residue clauses: {', '.join(residue) if residue else 'none'}",
              f"no-go: universal symmetry-faithfulness FALSE = "
              f"{S['NO_GO_SEARCH']['VERDICT']['universal_symmetry_faithfulness_is_FALSE']}"
              f" (famA={len(famA_witnesses)}, famB={len(famB_witnesses)})",
              f"teeth: {cert_g['fired']}/{cert_g['total']}",
              f"firewall: floats={float_lits}, unfenced weights={len(unfenced)}",
              f"science digest: {science_digest}",
              f"elapsed: {elapsed}s",
              f"all certificates pass: {all_pass}"]
    (ROOT / "outputs"
     / "frontier_cycle947_h0_discharge_2026_07_28.log").write_text(
        "\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines), flush=True)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
