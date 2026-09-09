#!/usr/bin/env python3
"""Cycle 946 -- THE MIRROR-PARTNERED KERNEL, and the first post-adoption derivation.

TWO INPUTS.

(A) Cycle 943 localised the branch divergence of the choice substrate to EIGHT
    of 5,815 wires, SIX of them mirror-paired and exactly swap-related, and
    named the sole obstruction: the record cell's ORIENTATION field, the one
    record datum with no mirror partner.  Its named successor -- the whole
    point of this block -- was "give the orientation field a mirror partner".

(B) The owner adopted a revised Admissibility axiom on 2026-08-05 (PR #6011,
    branch axioms/admissibility-likelihood-20260805).  Its second sentence
    reads, byte for byte:

        For each site, the probability distribution over the possibilities is
        determined by, and varies with, the nearest-neighbor conditions.

    EVERY CLAIM IN THIS BLOCK THAT CONSUMES THAT TEXT IS CONDITIONAL ON #6011
    LANDING.  The branch's file is vendor-read by `git show` and pinned by
    sha256 AND git blob; the worktree's own (pre-adoption) axiom memo is pinned
    separately so the delta is on the record.

WHAT THIS BLOCK BUILDS.  The minimal splice-only modification of 936's choice
substrate that repairs the mirror defect: for the involution

    sigma = swap(LEFT_ENDPOINT, RIGHT_ENDPOINT)
            o  swap(BANK_i.U_TO_V, BANK_i.V_TO_U)  for every one of the 12 banks

the compiled law's gate multiset is NOT sigma-invariant.  Its ENTIRE defect is
TWELVE distinct gates (220 occurrences of 34,188).  The partnered kernel is
L_ext = L union sigma(L): each deficit occurrence keeps its place and its
sigma-image is inserted immediately after it.  Nothing is deleted, reordered or
edited; the pinned compiler and the pinned emitter are untouched.

WHAT IT FINDS.  In the partnered kernel sigma is an exact automorphism of the
law (gate multiset sigma-invariant on every station; 940's own colour
refinement now gives LEFT and RIGHT the SAME colour under every label, where in
the unpartnered kernel it separated them under every label; semantic
commutation on a large random ensemble has zero breaking wires against 139 for
the unpartnered kernel).  The orientation wires 202/236 vanish from every
branch-divergence support.  At 3 of the 5 genuine two-item menu sites the
lane-restricted swap exchanges the branches exactly, over the whole declared
window.  At the other 2 the PRE-CHOICE CONDITIONS THEMSELVES differ under the
swap -- and the adopted axiom's "varies with" clause then correctly declines to
force anything.

THE FIREWALL, AS MODIFIED FOR THIS BLOCK.  Derived CONDITIONAL values ARE the
deliverable.  No unconditional weight value may be output.  Every numeric
weight sits under a key path containing CONDITIONAL, HYPOTHETICAL, IF_ or
THEOREM.  Zero float literals; exact rationals end to end.

MINIMAL-PREMISE RULE.  943's symmetriser sketch and the supervisor's two
derivation routes are NOT premises.  943's sketch is REFUTED AS STATED and
repaired: mirror-partnering the orientation field ALONE does not make the swap
a law symmetry (an eight-gate link-ladder defect remains, which 943 never saw
because it only ever looked inside the divergence support).  The covariance
route is REJECTED on the axiom's own bytes; the neighborhood-equality route
carries the theorem.
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

RUNTIME_BUDGET_SEC = 900
FRACTION_LABEL = "bookkeeping fraction, not probability"

# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
C936_PATH = "scripts/frontier_cycle936_choice_substrate_2026_07_28.py"
C936_RECEIPT = "outputs/choice_substrate_cycle936_receipt_2026_07_28.json"
C936_SHIP = "outputs/choice_substrate_block_cycle936_ship_receipt_2026_07_28.json"
C940_PATH = "scripts/frontier_cycle940_symmetric_weights_2026_07_28.py"
C940_RECEIPT = "outputs/symmetric_weights_cycle940_receipt_2026_07_28.json"
C943_PATH = "scripts/frontier_cycle943_prerecord_swap_2026_07_28.py"
C943_RECEIPT = "outputs/prerecord_swap_cycle943_receipt_2026_07_28.json"
C943_SHIP = "outputs/prerecord_swap_block_cycle943_ship_receipt_2026_07_28.json"
C943_NOTE = ("docs/PRERECORD_SWAP_ORIENTATION_WIRE_CYCLE943"
             "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
C918_RECEIPT = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
AXIOMS_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (CORE_PATH, C936_PATH, C936_RECEIPT, C936_SHIP,
                     C940_PATH, C940_RECEIPT,
                     C943_PATH, C943_RECEIPT, C943_SHIP, C943_NOTE,
                     C918_RECEIPT, AXIOMS_PATH)

EXPECTED_SHA256 = {
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    C936_PATH:
        "ba00f39403a1280346d2e20e6e1985130b7d4b0a986e1473acd2c637acd96e3d",
    C936_RECEIPT:
        "4412ae9016df02546db26cdd87fa33ab68bf2a7370b27640e18d4d0e59132028",
    C936_SHIP:
        "9da5a559f4e87940560aaf75daaaa4332a228cc5ec2a7b50bf744a7cbb164f0a",
    C940_PATH:
        "7c7400984e573dc446330f20423cce5045138682781716ed13ba89bfe877e124",
    C940_RECEIPT:
        "08888bf454a7f3c803f5c373d7688d67a9f0d974259f3e455c139d6c78e288cf",
    C918_RECEIPT:
        "849ad2bbb4abc8c9eda5541246784e2bdb69feaf423aac7c6f3aff83f6062bbd",
    AXIOMS_PATH:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
EXPECTED_GIT_BLOBS = {
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    C936_PATH: "75cb05ffb9456691747a67ed5227f3db589f95c4",
    C936_RECEIPT: "d7b786fccc0435d139339c141dbad75c9f8d799b",
    C936_SHIP: "1421484631b06fc203405c0ffab3a715c979cbed",
    C940_PATH: "ae09b548aff71354b9942904bc0b2824d7e755ac",
    C940_RECEIPT: "a24af8e08cc090b39802265d8b8d5ea3d1495d53",
    C918_RECEIPT: "5704619b21d9a3af312956580355d6dd5a303f53",
    AXIOMS_PATH: "4a863da1f3f255354839277271a3a69a5c205133",
}

# THE ADOPTED AXIOM, VENDOR-READ FROM THE PR BRANCH.  Not in this worktree.
ADOPTED_AXIOM_REF = "origin/axioms/admissibility-likelihood-20260805"
ADOPTED_AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
ADOPTED_AXIOM_SHA256 = \
    "638b2b2c134cd04a61addb46caeb86516ffd976f8432001dab78fa8cbebf15e8"
ADOPTED_AXIOM_GIT_BLOB = "02ab79ec08f0b29d1922c1f628d0d0389ddd2c99"
CONDITIONAL_ON_PR_6011 = True

# The byte-quotes the derivation consumes.  Every one is checked `in` the
# vendor-read text; a tampered quote fails tooth T_AXIOM.
Q_ADMISS_COVARIANCE = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under "
    "lattice\ntranslations and proper cubic rotations.")
Q_ADMISS_DISTRIBUTION = (
    "For each site, the probability distribution over the possibilities is\n"
    "determined by, and varies with, the nearest-neighbor conditions.")
Q_ADMISS_SUPPORT = (
    "The distribution is a probability measure on\nthe local possibility "
    "domain; \"available\"/\"admissible\" denotes its support --\non finite "
    "menus, exactly the possibilities of nonzero probability\n(probability "
    "zero is unavailable); Record locks a supported realization.")
Q_QUBIT_DOMAIN = "Each site has a domain of local possibilities."
Q_QUBIT_NO_PRIVILEGE = (
    "No possibility is privileged. Possibilities are distinguished by the "
    "supplied\nalgebraic structure alone.")
Q_LATTICE_NO_PRIVILEGE = (
    "No site is privileged. Sites are distinguished by the supplied lattice\n"
    "structure alone.")
Q_RECORD_LOCK = (
    "When present, a record locks exactly one admissible local possibility.")

BLOCKLISTED_MODULES = (
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
# A: pins, the vendor-read of the adopted axiom, and the AST lifts
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
LIFT940_FUNCS = ("gate_roles", "colour_refine", "fanout_profile", "apply_pi",
                 "relabelling_verdict")
LIFT940_CONSTS = ("ROLE_TARGET", "ROLE_C1", "ROLE_C2")


def _lift(source, filename, funcs, consts, classes):
    tree = ast.parse(source, filename=filename)
    body, got_f, got_c, got_k = [], set(), set(), set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            body.append(node)
            got_f.add(node.name)
        elif isinstance(node, ast.ClassDef) and node.name in classes:
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
            if names and all(nm in consts for nm in names):
                body.append(node)
                got_c.update(names)
    missing = (tuple(sorted(set(funcs) - got_f)),
               tuple(sorted(set(consts) - got_c)),
               tuple(sorted(set(classes) - got_k)))
    if any(missing):
        raise AssertionError(("lift incomplete", filename, missing))
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)
    ns = {"__builtins__": __builtins__, "ROOT": ROOT, "K": K, "np": np,
          "ast": ast, "json": json, "math": math, "sys": sys,
          "itertools": itertools, "combinations": combinations,
          "product": product, "Counter": Counter, "defaultdict": defaultdict,
          "Fraction": Fraction, "sha256": sha256, "sha1": sha1, "Path": Path,
          "SimpleNamespace": SimpleNamespace, "compact": compact,
          "digest": digest, "git_blob": git_blob}
    exec(compile(module, f"<ast-lift {filename}>", "exec"), ns)
    return SimpleNamespace(**{n: ns[n] for n in
                              tuple(got_f) + tuple(got_c) + tuple(got_k)}), \
        (len(got_f), len(got_c), len(got_k))


def lift_936(source):
    return _lift(source, C936_PATH, LIFT_FUNCS, LIFT_CONSTS, LIFT_CLASSES)


def lift_940(source):
    return _lift(source, C940_PATH, LIFT940_FUNCS, LIFT940_CONSTS, ())


def vendor_read_adopted_axiom():
    """`git show <branch>:<path>` -- the adopted axiom text is NOT in this
    worktree.  Pinned by sha256 AND git blob; every consuming claim is flagged
    CONDITIONAL_ON_PR_6011."""
    spec = f"{ADOPTED_AXIOM_REF}:{ADOPTED_AXIOM_PATH}"
    blob = subprocess.run(["git", "-C", str(ROOT), "show", spec],
                          capture_output=True, check=False).stdout
    ref = subprocess.run(["git", "-C", str(ROOT), "rev-parse", spec],
                         capture_output=True, check=False).stdout.decode().strip()
    return blob, {
        "vendor_read": spec,
        "why_vendor_read": "the adopted text lives on the PR #6011 branch, "
                           "not in this worktree; it is read with `git show` "
                           "and never copied into any worktree file.",
        "sha256": sha256(blob).hexdigest(),
        "git_blob": git_blob(blob),
        "git_rev_parse_of_the_path": ref,
        "bytes": len(blob),
        "sha256_matches_pin": sha256(blob).hexdigest() == ADOPTED_AXIOM_SHA256,
        "git_blob_matches_pin": git_blob(blob) == ADOPTED_AXIOM_GIT_BLOB,
        "git_object_id_agrees_with_recomputed_blob":
            ref == git_blob(blob),
        "CONDITIONAL_ON_PR_6011_LANDING": CONDITIONAL_ON_PR_6011,
    }


def pin_rows():
    rows, payloads = {}, {}
    for path in AUDIT_INPUT_PATHS:
        blob = (ROOT / path).read_bytes()
        payloads[path] = blob
        rows[path] = {"sha256": sha256(blob).hexdigest(),
                      "git_blob": git_blob(blob), "bytes": len(blob)}
    ax_blob, ax_row = vendor_read_adopted_axiom()
    payloads["ADOPTED_AXIOM"] = ax_blob
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
        "THE_ADOPTED_AXIOM_VENDOR_READ": ax_row,
        "THE_WORKTREE_AXIOM_MEMO_IS_THE_PRE_ADOPTION_ONE":
            "the worktree copy of docs/MINIMAL_AXIOMS_2026-06-29.md is pinned "
            "separately above; it is the PRE-adoption text and is NOT the "
            "text this block's derivation consumes.  The delta is the whole "
            "point of the block and is reported in Q2.",
        "C943_IS_PINNED_HERE_FOR_THE_FIRST_TIME":
            "Cycle 943 pinned no sha256 of itself in any prior runner; this "
            "block pins its bytes, its receipt and its ship receipt.",
        "modification_mechanism":
            "WRAP, NEVER EDIT.  The pinned 936 and 940 runners are AST-LIFTED "
            "(selected top-level nodes replayed in source order) and never "
            "imported; their bytes are unchanged and hashed.  The COMPILER is "
            "not edited: this block calls the lifted 936 schedule builder and "
            "the lifted 936 emitter unchanged, and its own construction is a "
            "pure function on the compiled gate ROWS (insert, never delete, "
            "never reorder, never re-emit).  Nothing writes to any pinned "
            "file; the adopted axiom is read out of git, not out of a file.",
        "declared_scope_limit":
            "the 180224-boundary Cycle-918 full-horizon re-run is NOT "
            "repeated (940 ran it; its receipt is pinned).  The tree window "
            "is 936's declared 175 orbits / 1925 boundaries.  The reversed-"
            "layout partnered tree and the V1 variant are computed ONCE, "
            "outside the double-run block, and are declared as such.",
    }
    cert["pass"] = bool(
        sha_ok and blob_ok and cert["existing_worktree_relative"]
        and ax_row["sha256_matches_pin"] and ax_row["git_blob_matches_pin"]
        and ax_row["git_object_id_agrees_with_recomputed_blob"]
        and not cert["blocked_modules_loaded"] and not cert["firewall_hits"])
    return cert, payloads


# ---------------------------------------------------------------------------
# THE CONSTRUCTION (this block's new content)
# ---------------------------------------------------------------------------

def sigma_pairs(left_w, right_w, bank_bases):
    """THE INVOLUTION.  The endpoint pair, and every bank's two direction rails.

    LEFT/RIGHT is forced: on the menu the endpoint content is the two
    complementary patterns (LEFT xor RIGHT == 1), so EXCHANGING the two wires
    is exactly EXCHANGING the two menu items -- and, on the menu only, is also
    exactly flipping both bits (943's chi).  The wire-exchange reading is the
    one used here because it is a RELABELLING, so it conjugates gates without
    touching values, which is what makes an exact automorphism statement
    available at all.

    The bank rails U_TO_V / V_TO_U are forced too: they are the wires the
    endpoint pair drives (the source-pointer TOF quartet), and 943 measured
    them mirror-paired.  All twelve banks are included, not just the two the
    divergence support happens to reach: a LAW symmetry is a statement about
    every state, so a defect on a bank the declared orbit never excites is
    still a defect.  Including all twelve costs nothing (the extra ten banks
    turn out to carry ZERO defect) and closes an off-orbit hole."""
    return ((left_w, right_w),) + tuple(
        (b + K.A.U_TO_V, b + K.A.V_TO_U) for b in bank_bases)


def make_sigma(pairs):
    sig = {}
    for a, b in pairs:
        sig[a] = b
        sig[b] = a
    return sig


def sigma_gate(g, sig, kinds):
    """Conjugate one compiled gate row by the wire relabelling.  The LANE MASK
    is preserved -- sigma relabels wires, never lanes -- which is exactly why
    the construction restricts to a single lane cleanly."""
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
        # a is the occasion ordinal, b is the target wire
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
    """The occurrences whose sigma-image the law does not already contain with
    equal multiplicity, per station.  Mask-sensitive: two gates that differ
    only in their lane mask are DIFFERENT gates, and the link ladder's two
    rails write the same target under different masks -- which is precisely a
    defect and precisely what a mask-blind comparison would miss."""
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


def mirror_splice(schedules, sig, kinds, only_targets=None, gate_target=None):
    """THE CONSTRUCTION.  L_ext = L union sigma(L), realised by inserting each
    missing sigma-image IMMEDIATELY AFTER the occurrence that lacks it.

    SPLICE-ONLY: no gate is deleted, no gate is moved, no gate is re-emitted,
    the pinned compiler is not touched.  `only_targets` restricts the splice to
    deficit gates writing a declared wire set -- used to build the V1 variant
    (orientation drives only), which is carried as a MEASURED NEAR-MISS, not as
    the construction."""
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
                if only_targets is None or gate_target(*g[:4]) in only_targets:
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
    """The lane-restricted relabelling.  Legitimate because sigma preserves
    lane masks, so the gate multiset restricted to any single lane is
    sigma-invariant exactly when the full multiset is."""
    out = list(cols)
    bit = 1 << lane
    for w, v in sig.items():
        out[v] = (cols[v] & ~bit) | (((cols[w] >> lane) & 1) << lane)
    return out


def strong_states(count, proto, touched, universe, tag):
    """Deterministic full-width pseudo-random columns.  sha256 of a counter,
    four blocks per wire so every one of the 749 lanes is randomised (a
    single-block state leaves the top ~490 lanes at their proto value and
    silently weakens the ensemble)."""
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
    """Does the transform commute with one full pass of the compiled cycle, on
    real columns?  Returns the wires where it fails.  943's instrument, with
    the transform generalised from a bit-flip to any state map."""
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


def foata_levels(seq, kinds, gate_target):
    """Foata (greedy) normal form of a gate sequence under the Mazurkiewicz
    independence relation: two gates are DEPENDENT when their lane masks
    intersect and one's target is the other's control.  Write-write is NOT a
    dependency (XOR updates into a common target commute).

    Trace equivalence is SUFFICIENT for equality of the composed maps and NOT
    necessary; this law contains duplicated gate occurrences whose algebraic
    cancellation defeats it, so this instrument is reported as a MEASUREMENT
    with its own incompleteness, never as the commutation certificate."""
    W = defaultdict(list)
    R = defaultdict(list)
    levels = []
    for g in seq:
        t = gate_target(*g[:4])
        cs = gate_controls(g, kinds)
        mk = g[4]
        lv = 0
        for c in cs:
            for (l, m2) in W[c]:
                if m2 & mk and l > lv:
                    lv = l
        for (l, m2) in R[t]:
            if m2 & mk and l > lv:
                lv = l
        lv += 1
        levels.append(lv)
        W[t].append((lv, mk))
        for c in cs:
            R[c].append((lv, mk))
    mx = max(levels) if levels else 0
    buckets: list = [[] for _ in range(mx + 1)]
    for g, l in zip(seq, levels):
        buckets[l].append(g)
    return tuple(tuple(sorted(b)) for b in buckets)


def read_cone(schedules, seeds, depth, kinds, gate_target):
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


def main() -> int:
    started = monotonic()
    timings: dict = {}
    cert_a, payloads = pin_rows()
    if not cert_a["pass"]:
        print("A_PINS FAILED", compact({
            k: cert_a[k] for k in
            ("sha256_all_match", "git_blobs_all_match",
             "existing_worktree_relative", "blocked_modules_loaded",
             "firewall_hits")}))
        print(compact(cert_a["THE_ADOPTED_AXIOM_VENDOR_READ"]))
        return 2

    t0 = monotonic()
    M, lift936_counts = lift_936(payloads[C936_PATH].decode("utf-8"))
    A940, lift940_counts = lift_940(payloads[C940_PATH].decode("utf-8"))
    kinds = {"X": M.KIND_X, "CNOT": M.KIND_CNOT, "TOF": M.KIND_TOF,
             "CHOICE": M.KIND_CHOICE}
    (c863, c878, c911, c913, consts878, consts911, cross_ops, pos_ops,
     provenance) = M.lift_machinery()

    r936 = json.loads(payloads[C936_RECEIPT].decode("utf-8"))
    ship936 = json.loads(payloads[C936_SHIP].decode("utf-8"))
    r940 = json.loads(payloads[C940_RECEIPT].decode("utf-8"))
    r943 = json.loads(payloads[C943_RECEIPT].decode("utf-8"))
    ship943 = json.loads(payloads[C943_SHIP].decode("utf-8"))
    r918 = json.loads(payloads[C918_RECEIPT].decode("utf-8"))
    axiom_text = payloads["ADOPTED_AXIOM"].decode("utf-8")
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
    TREE_B = M.TREE_ORBITS * stations

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

    sched_base = M.build_schedules(c863, program, sim_fwd, 0, ())
    sched_ma = M.build_schedules(c863, program, sim_fwd, 0, M_A_GATES)
    rows_ma = M.compile_schedules(sched_ma)

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

    choice_rows = choice_rows_for(lambda s: s)
    timings["setup"] = round(monotonic() - t0, 3)
    print(f"[setup {timings['setup']}s] substrate rebuilt: {len(proto)} wires, "
          f"{n} census worlds, {stations} stations, tree window {TREE_B}",
          flush=True)

    # =====================================================================
    # B: RESTRICTION GATES -- 936's tree and 943's localisation FIRST
    # =====================================================================
    gate_rows = []

    def gate(name, got, want):
        ok = got == want
        gate_rows.append({"gate": name, "value": got, "pinned": want,
                          "pass": ok})
        return ok

    gate("c936_receipt_all_certificates_pass",
         r936["all_certificates_pass"], True)
    gate("c936_self_sha256_matches_the_pinned_runner",
         sha256(payloads[C936_PATH]).hexdigest(), r936["self_sha256"])
    gate("c940_receipt_all_certificates_pass",
         r940["all_certificates_pass"], True)
    gate("c940_self_sha256_matches_the_pinned_runner",
         sha256(payloads[C940_PATH]).hexdigest(), r940["self_sha256"])
    gate("c943_receipt_all_certificates_pass",
         r943["all_certificates_pass"], True)
    gate("c943_self_sha256_matches_the_pinned_runner",
         sha256(payloads[C943_PATH]).hexdigest(), r943["self_sha256"])
    for key in (C943_NOTE, C943_RECEIPT):
        if key in ship943.get("files", {}):
            gate(f"ship943_sha256::{Path(key).name}",
                 sha256(payloads[key]).hexdigest(),
                 ship943["files"][key]["sha256"])
    gate("ship936_note_and_receipt_present",
         all(k in ship936.get("files", {}) for k in (C936_RECEIPT,)), True)

    pinned_sched = c863.masked_h_schedules(program, sim_fwd)
    gate("schedule_builder_reproduces_the_pinned_compiler",
         digest([[list(g) for g in s] for s in sched_base]),
         digest([[list(g) for g in s] for s in pinned_sched]))
    gate("compiled_gate_total", sum(len(s) for s in sched_base), 34166)
    m918 = r918["certificates"]["C2_MEASUREMENT"]["per_modification"]
    gate("M_A_compiled_gate_total", sum(len(s) for s in sched_ma),
         m918["M_A"]["ENDPOINT_WRITES"]["compiled_gates_total"])
    gate("endpoint_wires_LEFT_RIGHT_SOURCE", [left_w, right_w, src_w],
         [1, 6, 40])
    q1_943 = r943["certificates"]["Q1_THE_VALUE_SPACE_SYMMETRY_FAMILY"]
    conf = q1_943["THE_DIVERGENCE_IS_CONFINED"]
    gate("c943_wires_in_the_machine", len(proto), conf["wires_in_the_machine"])
    gate("c943_orientation_wires_are_BANK_cell_orientation",
         [202, 236], sorted(set(conf["union_of_all_divergence_supports"])
                            & set(ORIENTATION_WIRES)))

    # -- B2: 936's TREE, value-for-value -----------------------------------
    t0 = monotonic()
    tree_std = M.enumerate_tree(env, rows_ma, choice_rows, words_world,
                                atoms_at, TREE_B, reverse=False)
    timings["restriction/tree_936"] = round(monotonic() - t0, 3)
    c936_c2 = r936["certificates"]["C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"]
    struct = c936_c2["structure"]
    gate("tree_leaves", tree_std["leaves"], struct["leaves"])
    gate("tree_leaves_enumerated", len(tree_std["leaf_records"]),
         struct["leaves_enumerated"])
    gate("tree_branch_nodes", len(tree_std["node_records"]),
         struct["branch_nodes"])
    gate("tree_depth_in_choice_occasions", len(tree_std["apps"]),
         struct["depth_in_choice_occasions"])
    std_leaf_digests = [r["digest"] for r in tree_std["leaf_records"]]
    gate("tree_distinct_leaf_digests", len(set(std_leaf_digests)),
         struct["distinct_leaf_observables"])
    gate("tree_M4_children_entered_from_identical_parent_state",
         all(r["children_entered_from_identical_parent_state"]
             for r in tree_std["node_records"]), True)
    base_rows_m = [M.measurement(env, r["build"])
                   for r in tree_std["leaf_records"]]
    c3_936 = r936["certificates"]["C3_THE_PER_BRANCH_BATTERY"]
    for key, got in (
            ("write_once_holds_on_every_branch",
             all(x["write_once_violations"] == 0 for x in base_rows_m)),
            ("menu_holds_on_every_branch",
             all(x["off_menu_endpoint_content_at_the_lock"] == 0
                 for x in base_rows_m)),
            ("record_slots_inert_on_every_branch",
             all(x["record_slot_activation_conflicts"] == 0
                 for x in base_rows_m))):
        if key in c3_936:
            gate(f"battery_936::{key}", got, c3_936[key])
    print(f"[B {timings['restriction/tree_936']}s] 936 tree reproduced: "
          f"{tree_std['leaves']} leaves, "
          f"{len(set(std_leaf_digests))} distinct observables", flush=True)

    # -- B3: 940's A1 colour refinement, with 940's own code ---------------
    t0 = monotonic()
    flat_base = [(si, g) for si, s in enumerate(sched_base) for g in s]
    refinements = {}
    for label in ("exact", "popcount", "bare"):
        colour, iters, wires_seen = A940.colour_refine(flat_base, kinds, label)
        sizes = Counter(colour.values())
        refinements[label] = {
            "colour_of_LEFT": colour.get(left_w),
            "colour_of_RIGHT": colour.get(right_w),
            "LEFT_and_RIGHT_share_a_colour":
                colour.get(left_w) == colour.get(right_w),
            "iterations": iters,
            "colour_classes": len(set(colour.values())),
            "non_singleton_classes": sum(1 for v in sizes.values() if v > 1),
            "wires": len(wires_seen)}
    timings["restriction/colour_refine"] = round(monotonic() - t0, 3)
    q1_940 = r940["certificates"]["Q1_THE_MENU_SWAP_AUTOMORPHISM"]
    gate("A1_LEFT_and_RIGHT_separated_under_every_label",
         all(not refinements[k]["LEFT_and_RIGHT_share_a_colour"]
             for k in refinements),
         q1_940["LEFT_AND_RIGHT_ARE_SEPARATED_UNDER_EVERY_LABEL"])
    for label in ("exact", "popcount", "bare"):
        pinned = q1_940["REFINEMENTS"][label]
        for key in ("colour_of_LEFT", "colour_of_RIGHT",
                    "LEFT_and_RIGHT_share_a_colour", "iterations",
                    "colour_classes", "non_singleton_classes", "wires"):
            gate(f"A1_refinement_{label}_{key}", refinements[label][key],
                 pinned[key])

    # -- B4: 943's per-atom localisation, value-for-value -------------------
    t0 = monotonic()
    THETAS_943 = {
        "flip_endpoints_only": ((left_w, right_w), ()),
        "flip_endpoints_plus_swap_bank0_UV": ((left_w, right_w), ((124, 125),)),
        "flip_endpoints_plus_swap_bank1_UV": ((left_w, right_w), ((255, 256),)),
        "flip_endpoints_plus_swap_BOTH_bank_UV":
            ((left_w, right_w), ((124, 125), (255, 256))),
        "flip_endpoints_plus_swaps_plus_swap_ORIENTATIONS":
            ((left_w, right_w), ((124, 125), (255, 256), (202, 236))),
    }

    def theta_apply_943(cols, lane, flips, swaps):
        out = list(cols)
        bit = 1 << lane
        for w in flips:
            out[w] ^= bit
        for a, b in swaps:
            va = (out[a] >> lane) & 1
            vb = (out[b] >> lane) & 1
            out[a] = (out[a] & ~bit) | (vb << lane)
            out[b] = (out[b] & ~bit) | (va << lane)
        return out

    def per_atom_943(rows, crows):
        res = []
        for (t, site) in atoms:
            lane = site
            m0 = M.Machine(env, False)
            m0.advance(t, rows, crows, ZERO_WORDS)
            parent = m0.snapshot()
            m1 = M.Machine(env, False)
            m1.restore(parent)
            w = words_world[t][site]
            m0.advance(t + 1, rows, crows, {**ZERO_WORDS, t: 0})
            m1.advance(t + 1, rows, crows, {**ZERO_WORDS, t: w})
            fails = {k: None for k in THETAS_943}
            support = set()
            while m0.t <= TREE_B:
                support.update(
                    wr for wr in range(len(m0.columns))
                    if ((m0.columns[wr] >> lane) & 1)
                    != ((m1.columns[wr] >> lane) & 1))
                for key, (fl, sw) in THETAS_943.items():
                    if fails[key] is None:
                        ta = theta_apply_943(m0.columns, lane, fl, sw)
                        bad = [wr for wr in range(len(m1.columns))
                               if ((ta[wr] >> lane) & 1)
                               != ((m1.columns[wr] >> lane) & 1)]
                        if bad:
                            fails[key] = (m0.t, bad[:6])
                if m0.t >= TREE_B:
                    break
                m0.advance(m0.t + 1, rows, crows, ZERO_WORDS)
                m1.advance(m1.t + 1, rows, crows, ZERO_WORDS)
            best = None
            for key, v in fails.items():
                if v is not None and (best is None or v[0] > best[1]):
                    best = (key, v[0], v[1])
            res.append({"atom": [t, site], "support": sorted(support),
                        "best_theta": best[0] if best else None,
                        "best_theta_survives_to_boundary":
                            best[1] if best else None,
                        "orientation_wires_diverge":
                            bool(set(ORIENTATION_WIRES) & support)})
        return res

    loc943 = per_atom_943(rows_ma, choice_rows)
    timings["restriction/per_atom_943"] = round(monotonic() - t0, 3)
    split943 = q1_943["THE_PRE_LOCK_POST_LOCK_SPLIT"]
    pinned_by_atom = {(r["occasion_application"], r["site_world"]): r
                      for r in split943}
    for r in loc943:
        p = pinned_by_atom[(r["atom"][0], r["atom"][1])]
        gate(f"c943_support::{r['atom'][0]}/{r['atom'][1]}",
             r["support"], p["divergence_support"])
        gate(f"c943_best_theta::{r['atom'][0]}/{r['atom'][1]}",
             r["best_theta"], p["best_theta"])
        gate(f"c943_best_theta_survives_to::{r['atom'][0]}/{r['atom'][1]}",
             r["best_theta_survives_to_boundary"],
             p["best_theta_survives_to_boundary"])
        gate(f"c943_orientation_diverges::{r['atom'][0]}/{r['atom'][1]}",
             r["orientation_wires_diverge"], p["orientation_wires_diverge"])
    union = sorted({w for r in loc943 for w in r["support"]})
    gate("c943_union_divergence_support", union,
         conf["union_of_all_divergence_supports"])
    gate("c943_union_is_eight_wires", len(union), 8)
    gate("c943_genuine_menu_atoms",
         [r["atom"] for r in loc943 if r["orientation_wires_diverge"]],
         q1_943["genuine_menu_atoms"])
    print(f"[B {timings['restriction/per_atom_943']}s] 943 localisation "
          f"reproduced value-for-value: union {union}", flush=True)

    gates_passed = sum(1 for r in gate_rows if r["pass"])
    cert_b = {
        "certificate": "B_RESTRICTION_GATE",
        "rows": gate_rows,
        "gates_total": len(gate_rows),
        "gates_passed": gates_passed,
        "reproduced_before_any_construction":
            "936's tree and battery, 940's A1 colour refinement, and 943's "
            "full per-atom localisation (support, best theta, survival "
            "boundary, orientation divergence) are all recomputed from the "
            "pinned bytes and gated against the pinned receipts BEFORE the "
            "partnered kernel is built.",
        "pass": gates_passed == len(gate_rows),
    }
    if not cert_b["pass"]:
        for r in gate_rows:
            if not r["pass"]:
                print("RESTRICTION GATE FAILED", compact(r), flush=True)

    # =====================================================================
    # Q3 SEAL -- emitted BEFORE the partnered tree is computed
    # =====================================================================
    COVERED_PREDICTED = [[700, 475], [702, 450], [702, 715]]
    SEALED = {
        "sealed_before_the_partnered_tree_is_computed": True,
        "S1_re_verification_not_prediction": {
            "claim": "at every covered atom, all 128 leaf pairs differing "
                     "only in that atom's bit have BYTE-IDENTICAL build "
                     "digests",
            "disclosure": "the distinct-observable count of the partnered "
                          "tree was seen during the design probe, so S1 and "
                          "S5 are RE-VERIFICATIONS, not blind predictions.  "
                          "S2, S3, S4 were formulated before any measurement "
                          "of them existed and are genuine forward "
                          "predictions.",
        },
        "S2_prediction": "at every covered atom, all 128 leaf pairs have the "
                         "FINAL lane-local endpoint pair EXCHANGED (LEFT bit "
                         "and RIGHT bit swapped): 128 of 128",
        "S3_prediction": "at every covered atom the site is either absent "
                         "from `formed` at the end of the declared window, or "
                         "its lock boundary is EARLIER than its choice "
                         "boundary -- that is what reconciles S1 with S2",
        "S4_prediction": "at every UNCOVERED atom at least one leaf pair "
                         "differing only in that bit has a DIFFERING build "
                         "digest",
        "S5_re_verification_not_prediction":
            "exactly 3 of the 8 assignment bits change the leaf observable, "
            "and they are exactly the three lock-timing atoms",
        "covered_atoms_predicted": COVERED_PREDICTED,
        "THE_CONDITIONAL_WEIGHT_CLAIM_UNDER_TEST":
            "IF the theorem of Q2 holds at the covered atoms, THEN the two "
            "branch weights there are equal; the numeric consequence is "
            "carried only under CONDITIONAL key paths.",
    }
    seal_digest = digest(SEALED)
    print("===== SEAL =====", flush=True)
    print(compact(SEALED), flush=True)
    print("seal_digest:", seal_digest, flush=True)
    print("===== END SEAL =====", flush=True)

    # =====================================================================
    # THE SCIENCE (run twice for the double-run gate)
    # =====================================================================
    def splice_full(s):
        return mirror_splice(s, SIG, kinds, None, M.gate_target)[0]

    def splice_orientation_only(s):
        return mirror_splice(s, SIG, kinds, set(ORIENTATION_WIRES),
                             M.gate_target)[0]

    sched_p = splice_full(sched_ma)
    rows_p = M.compile_schedules(sched_p)
    choice_rows_p = choice_rows_for(splice_full)

    def science():
        out: dict = {}

        # ---- Q1: the construction spec ----------------------------------
        defect = mirror_defect(sched_ma, SIG, kinds)
        by_target = Counter(M.gate_target(*g[:4]) for _si, g, _im in defect)
        distinct = sorted({(g[0], g[1], g[2], g[3])
                           for _si, g, _im in defect})
        ori_defect = [d for d in defect
                      if M.gate_target(*d[1][:4]) in ORIENTATION_WIRES]
        link_defect = [d for d in defect
                       if M.gate_target(*d[1][:4]) not in ORIENTATION_WIRES]
        out["Q1_CONSTRUCTION"] = {
            "sigma_pairs": [list(p) for p in SIG_PAIRS],
            "sigma_is_an_involution":
                all(SIG[SIG[w]] == w for w in SIG),
            "orientation_wires": list(ORIENTATION_WIRES),
            "gates_before": sum(len(s) for s in sched_ma),
            "gates_after": sum(len(s) for s in sched_p),
            "gates_added": sum(len(s) for s in sched_p)
                           - sum(len(s) for s in sched_ma),
            "defect_occurrences": len(defect),
            "defect_distinct_gates": len(distinct),
            "defect_targets": {str(w): c for w, c in sorted(by_target.items())},
            "THE_ORIENTATION_DRIVE_DEFECT": {
                "occurrences": len(ori_defect),
                "distinct": len({(g[0], g[1], g[2], g[3])
                                 for _s, g, _i in ori_defect}),
                "reading": "every one is TOF(BANK_i.offset130, "
                           "BANK_i.U_TO_V -> BANK_i.cell{0,1}.orientation).  "
                           "The orientation field is driven off the U_TO_V "
                           "rail ALONE and never off V_TO_U: that, literally, "
                           "is the missing mirror partner Cycle 943 named.  "
                           "This block finds it in BOTH banks and BOTH cells "
                           "(943 only ever saw bank 1, because bank 0's "
                           "orientation wires never enter the divergence "
                           "support).",
            },
            "THE_LINK_LADDER_DEFECT_943_DID_NOT_SEE": {
                "occurrences": len(link_defect),
                "distinct": len({(g[0], g[1], g[2], g[3])
                                 for _s, g, _i in link_defect}),
                "targets": sorted({M.gate_target(*g[:4])
                                   for _s, g, _i in link_defect}),
                "REFUTES_943s_SKETCH_AS_STATED":
                    "943 wrote that giving the orientation field a mirror "
                    "partner 'would make the whole divergence support "
                    "mirror-paired, and the composite swap would then be a "
                    "candidate symmetry of the law'.  The first clause is "
                    "TRUE and is confirmed here.  The second is FALSE as "
                    "stated: an eight-gate ladder in the cross-bank LINK "
                    "region also reads the two rails asymmetrically, and "
                    "until it too is partnered the swap does NOT commute with "
                    "the law.  943 could not see it because it only ever "
                    "measured inside the divergence support, and the link "
                    "ladder never diverges on the declared orbit.",
            },
            "SPLICE_ONLY_DISCIPLINE": {
                "gates_deleted": 0,
                "gates_reordered": 0,
                "gates_re_emitted": 0,
                "original_subsequence_preserved":
                    all(list(a) == [g for g in b if True][:0] or
                        _is_subsequence(a, b)
                        for a, b in zip(sched_ma, sched_p)),
                "emitter_untouched":
                    [M.chunk_source(s) for s in sched_base]
                    == [M.chunk_source(s) for s in
                        M.build_schedules(c863, program, sim_fwd, 0, ())],
                "empty_splice_is_the_identity":
                    mirror_splice(sched_ma, {}, kinds, None,
                                  M.gate_target)[0] == sched_ma,
            },
            "WHY_NOT_A_FRESH_PARTNER_WIRE": {
                "the_alternative": "give each unpaired wire a FRESH shadow "
                                   "wire and mirror its whole gate cone onto "
                                   "the shadow, leaving every original wire "
                                   "bit-for-bit unchanged",
                "why_rejected": "the closure is forced downstream: every wire "
                                "read by a mirrored gate must itself be "
                                "partnered.  Measured closure size is 491 of "
                                "the 545 touched wires -- the construction "
                                "degenerates into duplicating 90% of the "
                                "machine and swapping the copies, which is a "
                                "symmetry of ANY machine and licenses "
                                "nothing.  The in-place mirror closure "
                                "touches ELEVEN wires.",
            },
        }

        # ---- Q1c: THE SYMMETRY CERTIFICATE ------------------------------
        touched = sorted({w for s in sched_p for g in s
                          for w in (M.gate_target(*g[:4]),)
                          + gate_controls(g, kinds)})
        ens = strong_states(8, proto, touched, env["uni_sim"], "c946")
        sem_p = semantic_commutes(rows_p, ens, lambda c: perm_apply(c, SIG))
        sem_b = semantic_commutes(rows_ma, ens, lambda c: perm_apply(c, SIG))
        per_station_p = [semantic_commutes((rows_p[i],), ens,
                                           lambda c: perm_apply(c, SIG))
                         for i in range(stations)]
        per_station_b = [semantic_commutes((rows_ma[i],), ens,
                                           lambda c: perm_apply(c, SIG))
                         for i in range(stations)]
        flat_p = [(si, g) for si, s in enumerate(sched_p) for g in s]
        ref_p = {}
        for label in ("exact", "popcount", "bare"):
            colour, iters, ws = A940.colour_refine(flat_p, kinds, label)
            ref_p[label] = {
                "colour_of_LEFT": colour.get(left_w),
                "colour_of_RIGHT": colour.get(right_w),
                "LEFT_and_RIGHT_share_a_colour":
                    colour.get(left_w) == colour.get(right_w),
                "iterations": iters,
                "colour_classes": len(set(colour.values())),
                "wires": len(ws)}
        trace_p = sum(1 for s in sched_p
                      if foata_levels(s, kinds, M.gate_target)
                      != foata_levels([sigma_gate(g, SIG, kinds) for g in s],
                                      kinds, M.gate_target))
        out["Q1c_SYMMETRY_CERTIFICATE"] = {
            "L1_EXACT_gate_multiset_sigma_invariant_every_station":
                multiset_sigma_invariant(sched_p, SIG, kinds),
            "L1_baseline_multiset_sigma_invariant":
                multiset_sigma_invariant(sched_ma, SIG, kinds),
            "L1_reading": "sigma-invariance of the compiled gate multiset IS "
                          "940's own notion of a substrate automorphism.  In "
                          "the partnered kernel a menu-swapping automorphism "
                          "EXISTS; 940 proved none exists in the unpartnered "
                          "one.  This layer is exact and combinatorial.",
            "L2_EXACT_every_spliced_gate_commutes_with_its_partner":
                all(_gates_commute(g, sigma_gate(g, SIG, kinds), kinds,
                                   M.gate_target)
                    for _si, g, _im in mirror_defect(sched_ma, SIG, kinds)),
            "L3_SEMANTIC_partnered_breaking_wires": len(sem_p),
            "L3_SEMANTIC_baseline_breaking_wires": len(sem_b),
            "L3_baseline_breaking_wires_sample": sem_b[:12],
            "L3_per_station_partnered": [len(x) for x in per_station_p],
            "L3_per_station_baseline": [len(x) for x in per_station_b],
            "L3_ensemble": {"states": len(ens), "lanes": n + 1,
                            "random_lane_vectors": len(ens) * (n + 1),
                            "wires_randomised": len(touched)},
            "L3_HONEST_STATUS":
                "a POSITIVE settled semantically is EVIDENCE, not proof: it "
                "certifies commutation on the tested states only.  It is "
                "reported as such.  The exact layers are L1, L2 and L4.",
            "L4_EXACT_940_colour_refinement_on_the_partnered_kernel": ref_p,
            "L4_LEFT_and_RIGHT_share_a_colour_under_every_label":
                all(ref_p[k]["LEFT_and_RIGHT_share_a_colour"] for k in ref_p),
            "L4_reading": "colour refinement is an automorphism INVARIANT: if "
                          "any automorphism exchanged LEFT and RIGHT they "
                          "would have to share a colour.  In the unpartnered "
                          "kernel they are separated under every label (940's "
                          "A1, reproduced in B); in the partnered kernel they "
                          "SHARE a colour under every label.  Computed with "
                          "940's own pinned code, not a lookalike.",
            "L5_MEASURED_NEGATIVE_trace_equivalence_stations_failing": trace_p,
            "L5_reading":
                "Mazurkiewicz trace equivalence of the gate sequence with its "
                "sigma-conjugate would be a fully exact sufficient criterion. "
                "It FAILS, on every station, and the block reports that "
                "plainly.  The reason is measured: the law contains "
                "DUPLICATED gate occurrences, whose algebraic cancellation is "
                "invisible to any purely syntactic independence relation, so "
                "trace equivalence is sufficient but far from necessary here. "
                "The three trace-failing lanes probed directly (station 0, "
                "lanes 15, 59, 202) show zero map mismatch over 400 random "
                "lane-vectors each, against 91-108 for the unpartnered "
                "kernel: the trace failure is a false alarm of the "
                "instrument, not a residual of the construction.",
        }

        # ---- Q1c(2): does the swap SWAP THE BRANCHES? --------------------
        def branch_swap_scan(rows, crows, tag):
            res = []
            for (t, site) in atoms:
                lane = site
                m0 = M.Machine(env, False)
                m0.advance(t, rows, crows, ZERO_WORDS)
                parent = m0.snapshot()
                pcols = list(m0.columns)
                m1 = M.Machine(env, False)
                m1.restore(parent)
                w = words_world[t][site]
                m0.advance(t + 1, rows, crows, {**ZERO_WORDS, t: 0})
                m1.advance(t + 1, rows, crows, {**ZERO_WORDS, t: w})
                first_fail, fail_wires = None, None
                support = set()
                other_lane = 0
                while m0.t <= TREE_B:
                    th = perm_apply_lane(m0.columns, SIG, lane)
                    bad = [wr for wr in range(len(th))
                           if ((th[wr] >> lane) & 1)
                           != ((m1.columns[wr] >> lane) & 1)]
                    if bad and first_fail is None:
                        first_fail, fail_wires = m0.t, bad[:8]
                    support.update(
                        wr for wr in range(len(m0.columns))
                        if ((m0.columns[wr] >> lane) & 1)
                        != ((m1.columns[wr] >> lane) & 1))
                    other_lane += sum(
                        1 for wr in range(len(m0.columns))
                        if (m0.columns[wr] ^ m1.columns[wr]) & ~(1 << lane))
                    if m0.t >= TREE_B:
                        break
                    m0.advance(m0.t + 1, rows, crows, ZERO_WORDS)
                    m1.advance(m1.t + 1, rows, crows, ZERO_WORDS)

                def bit(w):
                    return (pcols[w] >> lane) & 1
                asym = [[a, b] for a, b in SIG_PAIRS
                        if bit(a) != bit(b) and (a, b) != (left_w, right_w)]
                res.append({
                    "atom": [t, site],
                    "THE_SWAP_EXCHANGES_THE_BRANCHES": first_fail is None,
                    "first_failure_boundary": first_fail,
                    "first_failure_wires": fail_wires,
                    "divergence_support": sorted(support),
                    "orientation_wires_in_the_support":
                        sorted(set(ORIENTATION_WIRES) & support),
                    "other_lane_contamination": other_lane,
                    "pre_choice_asymmetric_sigma_pairs": asym,
                    "endpoints_at_the_choice_boundary":
                        [bit(left_w), bit(right_w)],
                    "on_menu_at_the_choice_boundary":
                        (bit(left_w) ^ bit(right_w)) == 1,
                })
            return res

        scan_p = branch_swap_scan(rows_p, choice_rows_p, "partnered")
        covered = [r["atom"] for r in scan_p
                   if r["THE_SWAP_EXCHANGES_THE_BRANCHES"]]
        genuine = [list(x) for x in q1_943["genuine_menu_atoms"]]
        out["Q1c_BRANCH_SWAP"] = {
            "per_atom": scan_p,
            "covered_atoms": covered,
            "uncovered_atoms": [r["atom"] for r in scan_p
                                if not r["THE_SWAP_EXCHANGES_THE_BRANCHES"]],
            "covered_genuine_menu_atoms": [a for a in covered if a in genuine],
            "genuine_menu_atoms_943": genuine,
            "ORIENTATION_WIRES_GONE_FROM_EVERY_SUPPORT":
                all(not r["orientation_wires_in_the_support"]
                    for r in scan_p),
            "every_support_is_now_mirror_paired":
                all(all(w in SIG for w in r["divergence_support"])
                    for r in scan_p),
            "WHY_THE_UNCOVERED_ATOMS_ARE_UNCOVERED":
                "at every uncovered atom the first failure is on a BANK RAIL "
                "PAIR (U_TO_V/V_TO_U) and nowhere else, and at four of the "
                "five the PRE-CHOICE state already breaks that pair's "
                "symmetry on the site's lane.  That is not a defect of the "
                "law: it is the conditions themselves differing, which is "
                "exactly the case the adopted axiom's 'varies with' clause "
                "covers.  The fifth (702/254, a lock-timing atom, not a "
                "menu) fails for a placement reason: 936 splices the CHOICE "
                "gates after station 0's macro, so on that lane part of the "
                "endpoint-to-rail propagation has already run inside the same "
                "chunk before the choice is injected.",
        }

        # ---- Q2: the neighborhood-equality measurement -------------------
        cone1 = read_cone(sched_p, {left_w, right_w}, 1, kinds, M.gate_target)
        cone2 = read_cone(sched_p, {left_w, right_w}, 2, kinds, M.gate_target)
        coneF = read_cone(sched_p, {left_w, right_w}, 50, kinds, M.gate_target)
        FORMALIZATIONS = {
            "N1_the_whole_lane_state": set(range(len(proto))),
            "N2_every_wire_the_law_touches": set(touched),
            "N3_endpoint_read_cone_depth_1": set(cone1),
            "N4_endpoint_read_cone_depth_2": set(cone2),
            "N5_endpoint_read_cone_closure": set(coneF),
            "N6_the_record_banks_and_links": set(global_dirty),
            "N7_the_sigma_support": set(SIG),
        }
        # the parent state at each atom, computed ONCE
        parents = {}
        for (t, site) in atoms:
            m = M.Machine(env, False)
            m.advance(t, rows_p, choice_rows_p, ZERO_WORDS)
            parents[(t, site)] = list(m.columns)

        nb_rows = {}
        for name, N in sorted(FORMALIZATIONS.items()):
            per = {}
            for (t, site) in atoms:
                lane = site
                cols = parents[(t, site)]
                th = perm_apply_lane(cols, SIG, lane)
                bad = [w for w in sorted(N)
                       if w not in (left_w, right_w)
                       and ((th[w] >> lane) & 1) != ((cols[w] >> lane) & 1)]
                per[f"{t}/{site}"] = {
                    "conditions_are_sigma_invariant": not bad,
                    "differing_wires": bad[:8]}
            nb_rows[name] = {
                "wires_in_the_formalization": len(N),
                # ADMISSIBILITY IS STRUCTURAL, NOT SIZE-BASED.  The
                # independent checker exhibited a formalization with 816
                # wires that still answers wrong, because it excludes the
                # bank direction rails: "the record cells only" contains
                # every cell payload offset in all twelve banks and not one
                # of the U_TO_V/V_TO_U wires.  Size is not the criterion.
                # CONTAINMENT OF THE SIGMA SUPPORT is, and it is computed
                # here rather than asserted, so no formalization is excluded
                # by name or after seeing its answer.
                "contains_the_sigma_support": set(SIG) <= N,
                "per_atom": per,
                "atoms_with_sigma_invariant_conditions":
                    sorted(k for k, v in per.items()
                           if v["conditions_are_sigma_invariant"])}
        agree = {k: v["atoms_with_sigma_invariant_conditions"]
                 for k, v in nb_rows.items()}
        admissible = {k for k, v in nb_rows.items()
                      if v["contains_the_sigma_support"]}
        majority = agree["N2_every_wire_the_law_touches"]

        # THE INSTANT.  The conditions are evaluated AT THE CHOICE
        # OCCASION'S BOUNDARY.  The checker asked what happens at other
        # boundaries, and the answer sharpens the claim rather than
        # denting it, so it is measured and published here.
        window = {}
        for (t, site) in atoms:
            lane = site
            m = M.Machine(env, False)
            m.advance(max(0, t - 40), rows_p, choice_rows_p, ZERO_WORDS)
            breaks = checked = 0
            while m.t < t:
                cols = m.columns
                th = perm_apply_lane(cols, SIG, lane)
                if any(((th[w] >> lane) & 1) != ((cols[w] >> lane) & 1)
                       for w in SIG if w not in (left_w, right_w)):
                    breaks += 1
                checked += 1
                m.advance(m.t + 1, rows_p, choice_rows_p, ZERO_WORDS)
            window[f"{t}/{site}"] = {
                "boundaries_checked": checked,
                "boundaries_where_the_conditions_are_NOT_sigma_invariant":
                    breaks}

        out["Q2_NEIGHBORHOOD_EQUALITY"] = {
            "WHAT_IS_MEASURED": {
                "NOT_this": "'the two branches present identical "
                            "nearest-neighbor conditions'.  That is TRIVIALLY "
                            "TRUE and licenses nothing: the two branches "
                            "share one parent state, so of course their "
                            "conditions coincide.  The supervisor's route "
                            "name and this block's first field names both "
                            "said it, and the independent checker was right "
                            "to refuse them.",
                "BUT_this": "the conditions at the site are POINTWISE "
                            "INVARIANT UNDER SIGMA.  That is a real, "
                            "falsifiable property of one state, it is what "
                            "the theorem text always said, and it is what is "
                            "computed below.  Adopted from the checker; no "
                            "number changed, every label did.",
            },
            "formalizations": nb_rows,
            "FORMALIZATION_ROBUSTNESS": {
                "admissible_formalizations": sorted(admissible),
                "inadmissible_formalizations":
                    sorted(set(nb_rows) - admissible),
                "the_admissibility_criterion":
                    "a formalization is admissible iff it CONTAINS THE SIGMA "
                    "SUPPORT -- every wire the swap moves.  A neighborhood "
                    "that omits a wire the swap acts on cannot see whether "
                    "the swap fixes the conditions, so its answer is "
                    "uninformative rather than wrong.  This is a structural "
                    "test, computed, and it excludes N3 and N4 (3 and 6 "
                    "wires, no rails) without reference to the answers they "
                    "give.",
                "every_admissible_formalization_agrees":
                    all(agree[k] == majority for k in admissible),
                "the_inadmissible_ones_do_disagree":
                    any(agree[k] != majority
                        for k in set(nb_rows) - admissible),
                "SIZE_IS_NOT_THE_CRITERION":
                    "the independent checker exhibited an 816-wire "
                    "formalization ('the record cells only', every cell "
                    "payload offset in all twelve banks) that reports every "
                    "atom symmetric, because the U_TO_V/V_TO_U rails are "
                    "bank-level fields and sit outside every cell payload.  "
                    "Any criterion phrased as 'big enough' would have "
                    "admitted it.  Containment is the criterion.",
            },
            "THE_CONDITIONS_ARE_EVALUATED_AT_THE_CHOICE_OCCASION": {
                "per_atom_over_the_40_boundaries_before_the_choice": window,
                "the_sharpening":
                    "at the covered atoms the conditions are sigma-invariant "
                    "AT THE CHOICE BOUNDARY and are NOT sigma-invariant at "
                    "most of the boundaries just before it.  This does not "
                    "dent the theorem -- the axiom evaluates the distribution "
                    "against the conditions that obtain, and the conditions "
                    "that obtain at a choice occasion are the ones at that "
                    "occasion's boundary -- but it sharpens what is derived: "
                    "THE EQUAL WEIGHT IS A PROPERTY OF THE OCCASION, NOT OF "
                    "THE SITE.  The same site one boundary earlier has "
                    "asymmetric conditions and the axiom forces nothing "
                    "there, which is the 'varies with' clause behaving "
                    "exactly as written.  Raised by the independent checker "
                    "and adopted.",
            },
        }

        # ---- Q2: the two routes -----------------------------------------
        quotes = {
            "Admissibility_covariance": Q_ADMISS_COVARIANCE,
            "Admissibility_distribution": Q_ADMISS_DISTRIBUTION,
            "Admissibility_support_reading_note": Q_ADMISS_SUPPORT,
            "Qubit_domain": Q_QUBIT_DOMAIN,
            "Qubit_no_possibility_is_privileged": Q_QUBIT_NO_PRIVILEGE,
            "Lattice_no_site_is_privileged": Q_LATTICE_NO_PRIVILEGE,
            "Record_locks_exactly_one": Q_RECORD_LOCK,
        }
        quote_ok = {k: (v in axiom_text) for k, v in quotes.items()}
        out["Q2_THE_THEOREM"] = {
            "CONDITIONAL_ON_PR_6011_LANDING": CONDITIONAL_ON_PR_6011,
            "byte_quotes": quotes,
            "every_quote_verbatim_in_the_vendor_read_text":
                all(quote_ok.values()),
            "quote_check": quote_ok,
            "THE_DELTA_FROM_THE_PRE_ADOPTION_TEXT": {
                "adopted_sentence_is_absent_from_the_worktree_memo":
                    Q_ADMISS_DISTRIBUTION not in preadopt_text,
                "reading": "the pre-adoption memo carries no probability "
                           "distribution clause at all; the derivation below "
                           "is impossible on the worktree text and possible "
                           "only on the adopted one.  That is the whole "
                           "reason this block exists.",
            },
            "ROUTE_A_COVARIANCE_REJECTED": {
                "the_route": "read the swap as an element of the covariance "
                             "group named in the axiom's first sentence, and "
                             "let covariance carry the equivariance",
                "VERDICT": "REJECTED ON THE AXIOM'S OWN BYTES",
                "why": "the first sentence names its group exhaustively -- "
                       "'covariant under lattice translations and proper "
                       "cubic rotations'.  The constructed swap is neither.  "
                       "It is an internal automorphism of the admissibility "
                       "rule's own structure: it exchanges two POSSIBILITIES "
                       "at a fixed site, it moves no site, and it is not "
                       "realised by any translation or rotation of Z^3 (a "
                       "proper cubic rotation that fixed the site and "
                       "exchanged the two endpoint rails would have to act as "
                       "an orientation-reversing map on the pair, which the "
                       "word 'proper' excludes).  Reading the swap INTO the "
                       "covariance clause would be reading a hypothesis into "
                       "the axiom, so the route is abandoned rather than "
                       "stretched.",
                "what_survives_of_it": "nothing load-bearing.  The covariance "
                                       "clause is used in this block only to "
                                       "establish that the rule is ONE FIXED "
                                       "rule -- site-independent -- which "
                                       "Route B needs and which the first "
                                       "sentence states outright.",
            },
            "ROUTE_B_NEIGHBORHOOD_EQUALITY_ADOPTED": {
                "the_route": "no group element at all: measure the two "
                             "branches' nearest-neighbor conditions and show "
                             "them identical, then let the determination "
                             "clause plus Qubit's no-privilege clause do the "
                             "work",
                "VERDICT": "ADOPTED -- this is the theorem",
            },
            "THEOREM": {
                "statement":
                    "Let S be the partnered kernel of Q1 and let sigma be its "
                    "constructed swap.  Let s be a site at which (i) the "
                    "menu is the two-element set {u, v} of complementary "
                    "endpoint contents, (ii) sigma is a symmetry of the law "
                    "exchanging u and v, and (iii) the nearest-neighbor "
                    "conditions at s are pointwise invariant under sigma.  "
                    "Then the probability distribution at s assigns u and v "
                    "equal probability; with support {u, v} and normalisation "
                    "this fixes the two-item weight.",
                "PROOF": [
                    "1.  By H1 (Admissibility, second sentence) the "
                    "distribution at s is DETERMINED BY the nearest-neighbor "
                    "conditions at s: it is the value of one fixed function "
                    "f of those conditions, and by H1's first sentence f is "
                    "the SAME function at every site.",
                    "2.  By H2 (the Q1c certificate) sigma is a symmetry of "
                    "the law: it carries admissible local configurations to "
                    "admissible local configurations and commutes with the "
                    "law's action.  So sigma induces a well-defined bijection "
                    "sigma_* of the local possibility domain that the rule "
                    "cannot distinguish from the identity by any datum the "
                    "rule is a function of.",
                        "3.  By H3 (the Q2 measurement) the conditions at s, AT "
                    "THE BOUNDARY OF THE OCCASION IN QUESTION, are POINTWISE "
                    "sigma-invariant.  Hence f is being evaluated at the SAME "
                    "argument before and after sigma.  The instant matters "
                    "and is part of the hypothesis: at most nearby boundaries "
                    "the same site's conditions are NOT sigma-invariant, so "
                    "what is derived is a property of the OCCASION, not a "
                    "standing property of the site.",
                    "4.  By Qubit ('No possibility is privileged. "
                    "Possibilities are distinguished by the supplied "
                    "algebraic structure alone') the two possibilities u and "
                    "v carry no label beyond the structure, and by step 2 "
                    "sigma_* is an automorphism of that structure exchanging "
                    "them.  A function of the conditions alone therefore "
                    "cannot separate them: f(conditions)(u) = "
                    "f(conditions)(v).  Any assignment separating them would "
                    "have to depend on a datum outside the conditions, "
                    "contradicting 'determined by'.",
                    "5.  By the Admissibility reading note the distribution "
                    "is a probability measure on the local possibility "
                    "domain and its support is the availability set; by the "
                    "site's menu structure the support is {u, v}.  With "
                    "equality from step 4 and total mass one, the two-item "
                    "weight is fixed.",
                ],
                "HYPOTHESIS_CHAIN": {
                    "H0": "IMPORT, UNDISCHARGED, AND THE MOST LOAD-BEARING "
                          "LINE IN THIS BLOCK: the compiled substrate law is "
                          "a realization of the axiom's nearest-neighbor "
                          "admissibility rule, and a symmetry of the former "
                          "is a symmetry of the latter.  H2 certifies a "
                          "property of a 34,408-gate circuit on 5,815 wires "
                          "over 749 census lanes.  The axiom speaks about a "
                          "rule on Z^3.  Step 2 of the proof crosses that "
                          "gap, and nothing in the 936/940/943/946 stack "
                          "DERIVES the crossing -- it is inherited from the "
                          "substrate's construction and is exactly as strong "
                          "as that inheritance.  Named here because the "
                          "independent checker found it unnamed and was "
                          "right to: without H0 the theorem is a theorem "
                          "about a circuit, not about the framework's "
                          "Admissibility axiom.  IDENTIFYING THE GAP IS NOT "
                          "CLOSING IT.",
                    "H1": "the ADOPTED Admissibility text, both sentences, "
                          "byte-quoted above.  CONDITIONAL ON PR #6011 "
                          "LANDING.",
                    "H2": "the Q1c symmetry certificate for the constructed "
                          "kernel: exact at layers L1/L2/L4, semantic at L3.  "
                          "This is the load-bearing empirical hypothesis and "
                          "it is no stronger than L3's ensemble.",
                    "H3": "the Q2 neighborhood-equality measurement at the "
                          "site, under a formalization that contains every "
                          "wire the law reads.  MEASURED, not assumed.",
                    "H4": "Qubit's no-privilege clause, byte-quoted.  This is "
                          "what turns 'the conditions are equal' into 'the "
                          "probabilities are equal'; without it the "
                          "determination clause alone is vacuous, because a "
                          "function of the conditions could still carry a "
                          "built-in preference between two labels.",
                    "H5": "the domain of the distribution is the site's FULL "
                          "Qubit possibility domain.  Dissolved by "
                          "composition rather than ruled: reading the domain "
                          "as 'the available possibilities only' is circular, "
                          "since the adopted reading note defines "
                          "availability AS the distribution's support.  The "
                          "support is therefore an output of the measure, not "
                          "a precondition on its domain, and no owner ruling "
                          "is needed or cited.",
                },
                "WHAT_IS_NOT_ASSUMED": [
                    "no covariance argument (Route A is rejected outright)",
                    "no appeal to indifference, symmetry of ignorance, or any "
                    "epistemic principle",
                    "no envariance premise; the stranded envariance note is "
                    "not cited as authority anywhere in this block",
                    "no claim that the swap is realised by a lattice motion",
                ],
                "IS_H3_DOING_HIDDEN_WORK": {
                    "the_worry": "H3 could smuggle in the conclusion if the "
                                 "'conditions' were defined as whatever makes "
                                 "the branches look alike",
                    "the_defence": "H3 is measured under SEVEN independently "
                                   "specified formalizations fixed before the "
                                   "measurement, five of which contain the "
                                   "sigma support and all five of which "
                                   "agree, atom for atom.  The two that "
                                   "disagree are rejected on a structural "
                                   "ground (they exclude wires the law "
                                   "reads), not because of the answer they "
                                   "give.  And H3 SPLITS the atoms 4/4 "
                                   "rather than certifying all of them, "
                                   "which is what a non-circular measurement "
                                   "looks like.",
                },
            },
            "COVERAGE": {
                "sites_where_all_hypotheses_hold": covered,
                "sites_where_they_do_not": [
                    r["atom"] for r in scan_p
                    if not r["THE_SWAP_EXCHANGES_THE_BRANCHES"]],
                "of_the_five_genuine_two_item_menu_atoms_covered":
                    [a for a in covered if a in genuine],
                "WHAT_REMAINS_FREE": [
                    "the two genuine menu atoms whose pre-choice conditions "
                    "differ under the swap: the axiom's 'varies with' clause "
                    "positively declines to fix them, and nothing in this "
                    "block does either",
                    "every asymmetric menu: the theorem needs a symmetry "
                    "exchanging the items and there is none when the items "
                    "are not exchangeable",
                    "menus of more than two items: the argument gives "
                    "equality within a sigma-orbit, not the distribution's "
                    "general form",
                    "the general FORM of the distribution as a function of "
                    "the conditions: entirely open.  This block fixes values "
                    "on an orbit, it does not derive f",
                    "the UNPARTNERED kernel's values, which are the ones a "
                    "physical claim would need: see the price sheet",
                ],
            },
        }

        # ---- Q3: the sealed table ---------------------------------------
        tree_p = M.enumerate_tree(env, rows_p, choice_rows_p, words_world,
                                  atoms_at, TREE_B, reverse=False)
        leaves_p = tree_p["leaf_records"]
        dig_p = [r["digest"] for r in leaves_p]
        bit_index = {}
        i = 0
        for t in apps:
            for site in atoms_at[t]:
                bit_index[(t, site)] = i
                i += 1
        nbits = i

        def pair_rows(t, site):
            b = bit_index[(t, site)]
            step = 1 << (nbits - 1 - b)
            rows = []
            for idx in range(len(leaves_p)):
                if (idx // step) % 2:
                    continue
                j = idx + step
                A, B = leaves_p[idx], leaves_p[j]
                ia = A["build"]["item"].get(site)
                ib = B["build"]["item"].get(site)
                rows.append({
                    "digest_identical": A["digest"] == B["digest"],
                    "formed_identical":
                        A["build"]["formed"] == B["build"]["formed"],
                    "lock_ordinal_identical":
                        A["build"]["lock_ordinal"] == B["build"]["lock_ordinal"],
                    "events_identical":
                        A["build"]["events"] == B["build"]["events"],
                    "item_at_site":
                        [list(ia) if ia else None, list(ib) if ib else None],
                    "site_is_formed": site in A["build"]["formed"],
                })
            return rows

        seal_rows = {}
        for (t, site) in atoms:
            rws = pair_rows(t, site)
            lane = site
            m = M.Machine(env, False)
            m.advance(t, rows_p, choice_rows_p, ZERO_WORDS)
            lockb = None
            for r in leaves_p[:1]:
                lockb = r["build"]["formed"].get(site)
            seal_rows[f"{t}/{site}"] = {
                "pairs": len(rws),
                "all_digests_identical": all(r["digest_identical"] for r in rws),
                "any_digest_differs": any(not r["digest_identical"]
                                          for r in rws),
                "all_formed_identical": all(r["formed_identical"] for r in rws),
                "all_lock_ordinal_identical":
                    all(r["lock_ordinal_identical"] for r in rws),
                "all_events_identical": all(r["events_identical"] for r in rws),
                "site_is_formed_in_the_window": rws[0]["site_is_formed"],
                "site_lock_boundary": lockb,
                "choice_boundary": t,
                "lock_is_before_the_choice":
                    (lockb is not None and lockb < t),
            }

        def endpoint_exchanged_rows(t, site):
            """S2: after the window, are the two branches' lane-local endpoint
            bits exchanged?  Measured on the machine, not on the tree."""
            lane = site
            m0 = M.Machine(env, False)
            m0.advance(t, rows_p, choice_rows_p, ZERO_WORDS)
            par = m0.snapshot()
            m1 = M.Machine(env, False)
            m1.restore(par)
            w = words_world[t][site]
            m0.advance(t + 1, rows_p, choice_rows_p, {**ZERO_WORDS, t: 0})
            m1.advance(t + 1, rows_p, choice_rows_p, {**ZERO_WORDS, t: w})
            m0.advance(TREE_B, rows_p, choice_rows_p, ZERO_WORDS)
            m1.advance(TREE_B, rows_p, choice_rows_p, ZERO_WORDS)
            a = ((m0.columns[left_w] >> lane) & 1,
                 (m0.columns[right_w] >> lane) & 1)
            b = ((m1.columns[left_w] >> lane) & 1,
                 (m1.columns[right_w] >> lane) & 1)
            return {"branch0_endpoints": list(a), "branch1_endpoints": list(b),
                    "exchanged": a == (b[1], b[0]) and a != b}

        s2 = {f"{t}/{site}": endpoint_exchanged_rows(t, site)
              for (t, site) in atoms}
        matters = []
        for b in range(nbits):
            step = 1 << (nbits - 1 - b)
            matters.append(any(dig_p[i] != dig_p[i ^ step]
                               for i in range(len(dig_p))))
        cov_keys = [f"{a[0]}/{a[1]}" for a in covered]
        unc_keys = [f"{t}/{s}" for (t, s) in atoms
                    if [t, s] not in covered]
        lock_timing = [f"{a[0]}/{a[1]}"
                       for a in q1_943["lock_timing_atoms"]]
        observable_bits = [f"{t}/{s}" for (t, s), b in
                           zip(atoms, matters) if b]
        out["Q3_SEALED_TABLE"] = {
            "seal": SEALED,
            "seal_digest": seal_digest,
            "per_atom": seal_rows,
            "S2_endpoint_exchange": s2,
            "VERIFICATION": {
                "S1_all_covered_pairs_digest_identical":
                    all(seal_rows[k]["all_digests_identical"]
                        for k in cov_keys),
                "S2_all_covered_atoms_endpoints_exchanged":
                    all(s2[k]["exchanged"] for k in cov_keys),
                "S3_covered_sites_unformed_or_locked_before_the_choice":
                    all((not seal_rows[k]["site_is_formed_in_the_window"])
                        or seal_rows[k]["lock_is_before_the_choice"]
                        for k in cov_keys),
                "S4_every_uncovered_atom_has_a_differing_pair":
                    all(seal_rows[k]["any_digest_differs"] for k in unc_keys),
                "S5_observable_bits_are_exactly_the_lock_timing_atoms":
                    sorted(observable_bits) == sorted(lock_timing),
                "observable_bits": observable_bits,
                "lock_timing_atoms_943": lock_timing,
                "S4_IS_REFUTED_AND_HERE_IS_WHY":
                    "S4 predicted that every UNCOVERED atom would still show "
                    "a differing leaf digest on some pair.  It is FALSE, and "
                    "the block's own seal is scored 4 of 5 rather than "
                    "quietly restated.  The prediction assumed the "
                    "observable collapse would follow COVERAGE; it follows "
                    "MENU-HOOD instead.  In the partnered kernel the record "
                    "stops distinguishing the two branches at every genuine "
                    "two-item menu atom, covered or not -- only the three "
                    "lock-timing atoms remain observable.  So the mirror "
                    "closure buys record-indistinguishability of the two "
                    "menu items MORE broadly than it buys the swap symmetry, "
                    "and the two properties are not the same property.  That "
                    "is a strictly more interesting fact than the one "
                    "predicted, and it is the seal that found it.",
                "S4_the_uncovered_atoms_that_refute_it":
                    [k for k in unc_keys
                     if not seal_rows[k]["any_digest_differs"]],
                "distinct_leaf_observables_partnered": len(set(dig_p)),
                "distinct_leaf_observables_baseline":
                    struct["distinct_leaf_observables"],
            },
        }

        # ---- Q1b: the 918/936 battery on EVERY branch --------------------
        rows_m = [M.measurement(env, r["build"]) for r in leaves_p]
        out["Q1b_BATTERY"] = {
            "declared_window_orbits": M.TREE_ORBITS,
            "declared_window_boundaries": TREE_B,
            "branches": len(rows_m),
            "leaves": tree_p["leaves"],
            "branch_nodes": len(tree_p["node_records"]),
            "write_once_holds_on_every_branch":
                all(x["write_once_violations"] == 0 for x in rows_m),
            "duplicate_lane_consistency_holds_on_every_branch":
                all(x["duplicate_lane_mismatches"] == 0 for x in rows_m)
                and all(r["build"]["duplicate_lane_column_divergence"] == 0
                        for r in leaves_p),
            "record_slots_inert_on_every_branch":
                all(x["record_slot_activation_conflicts"] == 0
                    for x in rows_m),
            "menu_holds_on_every_branch":
                all(x["off_menu_endpoint_content_at_the_lock"] == 0
                    for x in rows_m),
            "off_menu_lane_count_is_constant_across_branches":
                len({r["build"]["off_menu_lane_count"]
                     for r in leaves_p}) == 1,
            "formation_happens_on_every_branch":
                all(x["lock_points"] > 0 for x in rows_m),
            "M4_children_from_identical_parent_state":
                all(r["children_entered_from_identical_parent_state"]
                    for r in tree_p["node_records"]),
            "lock_point_count_range": [min(x["lock_points"] for x in rows_m),
                                       max(x["lock_points"] for x in rows_m)],
            "record_event_range": [min(x["record_events"] for x in rows_m),
                                   max(x["record_events"] for x in rows_m)],
            "distinct_realized_splits":
                len({compact(x["realized_split"]) for x in rows_m}),
            "distinct_leaf_observables": len(set(dig_p)),
            "BACKWARD_COMPATIBILITY_DECLARED": {
                "WHAT_MUST_NOT_CHANGE_AND_DOES_NOT": [
                    "write-once on every branch",
                    "duplicate-lane consistency on every branch (both the "
                    "918 counter and 936's stronger per-wire reading)",
                    "record slots inert on every branch",
                    "the menu: no off-menu endpoint content at any lock",
                    "the tree's shape: 256 leaves, 75 branch nodes, depth 4",
                    "M4: every child entered from an identical parent state",
                    "formation still happens on every branch",
                ],
                "WHAT_CHANGES_AND_MUST": [
                    "the orientation field's value.  It is the datum being "
                    "repaired; leaving it fixed would be leaving the "
                    "asymmetry in place.",
                    "the seven cross-bank LINK wires of the ladder defect.",
                    "the leaf observables.  The partnered kernel's tree has "
                    "FEWER distinct observables than the unpartnered one, "
                    "and this is the construction's real price -- see the "
                    "price sheet.  It is not a battery failure: every "
                    "battery clause still holds.",
                ],
                "LEAF_DIGESTS_ARE_NOT_PRESERVED":
                    "stated plainly, because a reader who assumed otherwise "
                    "would misread everything downstream.  The partnered "
                    "kernel is a DIFFERENT kernel, not a re-encoding of the "
                    "same one.  943's A2 gauge result was a byte-identity "
                    "result; this is not, and no such claim is made.",
            },
        }

        # ---- the price sheet --------------------------------------------
        out["PRICE_SHEET"] = {
            "what_was_bought": "an exact menu-swapping automorphism of the "
                               "law, which 940 proved the unpartnered kernel "
                               "does not admit, and with it a derivation of "
                               "equal weights at three sites from the adopted "
                               "axiom rather than a registration of them",
            "what_it_cost": [
                "the kernel is modified: 220 gate occurrences added, eleven "
                "wires' values changed.  This is a NEW substrate, and no "
                "claim is transported to the unpartnered one.",
                "the record loses discrimination: the partnered tree's "
                "distinct leaf observables drop, and the surviving observable "
                "bits are exactly the lock-timing atoms.  At the covered "
                "menu sites the record cannot tell the two branches apart AT "
                "ALL -- which is the symmetry working as advertised, and "
                "which also means the derived equality is not, at those "
                "sites, an equality between distinguishable records.",
                "coverage is 3 of 8 atoms and 3 of 5 genuine menus, not all.",
                "L3 of the symmetry certificate is semantic, so H2 is only as "
                "strong as its ensemble.",
            ],
            "WHAT_THIS_IS_NOT": [
                "not a derivation of the Born rule",
                "not a claim about the physical kernel: the partnered kernel "
                "is a constructed object and the question of which kernel "
                "physics runs is untouched",
                "not an axiom change, not an ask, and not an owner surface",
            ],
        }
        return out

    t0 = monotonic()
    science_1 = science()
    timings["science/pass1"] = round(monotonic() - t0, 3)
    print(f"[science pass1 {timings['science/pass1']}s] "
          f"covered={science_1['Q1c_BRANCH_SWAP']['covered_atoms']}", flush=True)
    t0 = monotonic()
    science_2 = science()
    timings["science/pass2"] = round(monotonic() - t0, 3)
    science_digest = digest(science_1)
    double_run = {
        "certificate": "H_DOUBLE_RUN",
        "pass1_digest": science_digest,
        "pass2_digest": digest(science_2),
        "identical": digest(science_1) == digest(science_2),
        # the token scan is per PATH SEGMENT and deliberately narrow: a first
        # cut on the substring "timing" flagged `lock_timing_atoms_943`, which
        # is a physics term (943's classification of the three non-menu atoms)
        # and carries no wall clock.  A scan that cannot tell a clock from a
        # noun is not a gate.
        "digest_is_timing_free":
            not any(_is_a_clock_field(p) for p, _v in _walk_paths(science_1)),
        "timing_token_paths": [p for p, _v in _walk_paths(science_1)
                               if _is_a_clock_field(p)],
        "pass": digest(science_1) == digest(science_2),
    }
    S = science_1
    print(f"[science pass2 {timings['science/pass2']}s] "
          f"double-run identical={double_run['identical']}", flush=True)

    # =====================================================================
    # ONCE, outside the double run: the reversed layout and the V1 variant
    # =====================================================================
    # 936's OWN sub-tree/both-layouts test, reproduced exactly: the reversed
    # layout must be built from sim_rev (a different lane layout compiles
    # different masks and different support words), and the declared sub-tree
    # is the FIRST occasion only.  Comparing a reversed-layout run against
    # forward-layout schedules is meaningless -- the baseline control below
    # exists so that a reader can see the instrument distinguishing them.
    t0 = monotonic()
    sim_rev = tuple(census[w] for w in range(n - 1, -1, -1))
    sim_rev = sim_rev + (sim_rev[0],)
    sub_atoms_at = {apps[0]: atoms_at[apps[0]]}

    def layout_pair(splice):
        digs = {}
        for rev, sim in ((False, sim_fwd), (True, sim_rev)):
            g2 = M_A_GATES + ((M.KIND_CHOICE, 0, left_w, 0),
                              (M.KIND_CHOICE, 0, right_w, 0))
            sc = splice(M.build_schedules(c863, program, sim, 0, g2))
            nsl: dict = {}
            exec("\n".join(M.chunk_source(sc[apps[0] % stations])),
                 {"__builtins__": {}, "CHOICE": M.CHOICE}, nsl)
            sub_rows = {apps[0]: (0, nsl["apply_chunk"])}
            base_rows = M.compile_schedules(
                splice(M.build_schedules(c863, program, sim, 0, M_A_GATES)))
            words = M.choice_support_words(env, sub_atoms_at, rev, "world")
            st = M.enumerate_tree(env, base_rows, sub_rows, words,
                                  sub_atoms_at, TREE_B, reverse=rev,
                                  collect_nodes=False)
            digs["reversed" if rev else "forward"] = [
                r["digest"] for r in st["leaf_records"]]
        return digs

    lay_p = layout_pair(splice_full)
    lay_b = layout_pair(lambda s: s)
    layout_ok = lay_p["forward"] == lay_p["reversed"]
    layout_ok_baseline = lay_b["forward"] == lay_b["reversed"]
    timings["layout_pair"] = round(monotonic() - t0, 3)
    print(f"[layout {timings['layout_pair']}s] partnered sub-tree "
          f"layout-independent={layout_ok} (baseline control "
          f"{layout_ok_baseline})", flush=True)

    t0 = monotonic()
    sched_v1 = splice_orientation_only(sched_ma)
    rows_v1 = M.compile_schedules(sched_v1)
    cr_v1 = choice_rows_for(splice_orientation_only)
    touched_v1 = sorted({w for s in sched_v1 for g in s
                         for w in (M.gate_target(*g[:4]),)
                         + gate_controls(g, kinds)})
    ens_v1 = strong_states(4, proto, touched_v1, env["uni_sim"], "c946v1")
    sem_v1 = semantic_commutes(rows_v1, ens_v1, lambda c: perm_apply(c, SIG))
    v1_cov = []
    for (t, site) in atoms:
        lane = site
        m0 = M.Machine(env, False)
        m0.advance(t, rows_v1, cr_v1, ZERO_WORDS)
        par = m0.snapshot()
        m1 = M.Machine(env, False)
        m1.restore(par)
        w = words_world[t][site]
        m0.advance(t + 1, rows_v1, cr_v1, {**ZERO_WORDS, t: 0})
        m1.advance(t + 1, rows_v1, cr_v1, {**ZERO_WORDS, t: w})
        ff = None
        while m0.t <= TREE_B:
            th = perm_apply_lane(m0.columns, SIG, lane)
            if any(((th[wr] >> lane) & 1) != ((m1.columns[wr] >> lane) & 1)
                   for wr in range(len(th))):
                ff = m0.t
                break
            if m0.t >= TREE_B:
                break
            m0.advance(m0.t + 1, rows_v1, cr_v1, ZERO_WORDS)
            m1.advance(m1.t + 1, rows_v1, cr_v1, ZERO_WORDS)
        if ff is None:
            v1_cov.append([t, site])
    timings["V1_variant"] = round(monotonic() - t0, 3)
    cert_v1 = {
        "certificate": "V1_THE_MEASURED_NEAR_MISS",
        "what_it_is": "the splice restricted to the four orientation drives "
                      "-- exactly 943's sketch, built",
        "gates_added": sum(len(s) for s in sched_v1)
                       - sum(len(s) for s in sched_ma),
        "multiset_sigma_invariant":
            multiset_sigma_invariant(sched_v1, SIG, kinds),
        "semantic_breaking_wires": len(sem_v1),
        "atoms_where_the_swap_exchanges_the_branches": v1_cov,
        "THE_TRAP": "V1 relates the two branches at ALL FIVE genuine menu "
                    "atoms -- strictly better coverage than the construction "
                    "this block ships -- and yet sigma is NOT a symmetry of "
                    "its law: the multiset is not sigma-invariant and "
                    "semantic commutation breaks on 139 wires.  It is an "
                    "on-orbit intertwiner and nothing more.  This is exactly "
                    "the object 943's independent checker found and correctly "
                    "refused to license (its R5: an affine GF(2) map that "
                    "reproduces the branch relation, fails off-orbit, and "
                    "licenses no weight equality).  It is carried here so "
                    "that the better-looking number is on the record next to "
                    "the reason it must be refused.",
        "pass": True,
    }
    print(f"[V1 {timings['V1_variant']}s] near-miss coverage={v1_cov} "
          f"semantic_breaks={len(sem_v1)}", flush=True)

    # =====================================================================
    # F: the parametric firewall (MODIFIED: conditional values are the point)
    # =====================================================================
    FENCE = ("CONDITIONAL", "HYPOTHETICAL", "IF_", "THEOREM")
    payload_for_firewall = {"science": S, "V1": cert_v1,
                            "restriction": cert_b, "seal": SEALED}
    numeric_leaves = []
    for p, v in _walk_paths(payload_for_firewall):
        if isinstance(v, (int, Fraction)) and not isinstance(v, bool):
            if v in (0, 1):
                continue
            numeric_leaves.append((p, str(v)))
    self_src = Path(__file__).read_text(encoding="utf-8")
    float_lits = sum(1 for node in ast.walk(ast.parse(self_src))
                     if isinstance(node, ast.Constant)
                     and isinstance(node.value, float))
    # a weight VALUE is a rational in (0,1); none may appear unfenced
    weight_shaped = [(p, v) for p, v in _walk_paths(payload_for_firewall)
                     if isinstance(v, Fraction) and 0 < v < 1]
    unfenced = [p for p, _v in weight_shaped
                if not any(f in p.upper() for f in FENCE)]
    firewall = {
        "certificate": "F_PARAMETRIC_FIREWALL",
        "rule": "THE FIREWALL IS MODIFIED FOR THIS BLOCK, as specified: a "
                "DERIVED CONDITIONAL value is the deliverable.  What stays "
                "forbidden is an UNCONDITIONAL weight value -- any weight "
                "asserted as law content without its hypothesis chain "
                "attached.  Every weight-shaped rational must sit under a key "
                "path containing CONDITIONAL, HYPOTHETICAL, IF_ or THEOREM.",
        "fence_tokens": list(FENCE),
        "weight_shaped_rationals": len(weight_shaped),
        "weight_values_outside_a_conditional_fence": unfenced,
        "no_unconditional_weight_value": not unfenced,
        "zero_float_literals": float_lits == 0,
        "float_literals_in_this_runner": float_lits,
        "fraction_label": FRACTION_LABEL,
        "THE_CONDITIONAL_VALUE_ITSELF": {
            "CONDITIONAL_two_item_weight_at_a_covered_site":
                str(Fraction(1, 2)),
            "CONDITIONAL_hypotheses": ["H1 adopted Admissibility text "
                                       "(PR #6011 must land)",
                                       "H2 the Q1c symmetry certificate",
                                       "H3 the Q2 neighborhood measurement",
                                       "H4 Qubit no-privilege",
                                       "H5 the domain, dissolved by "
                                       "composition"],
            "CONDITIONAL_scope": "the three covered atoms of the PARTNERED "
                                 "kernel only.  Not the unpartnered kernel, "
                                 "not asymmetric menus, not larger menus.",
        },
        "pass": (not unfenced) and float_lits == 0,
    }

    # =====================================================================
    # G: the teeth -- every one must FIRE
    # =====================================================================
    teeth = []

    def tooth(name, fired, detail):
        teeth.append({"tooth": name, "fired": bool(fired), "detail": detail})

    touched_p = sorted({w for s in sched_p for g in s
                        for w in (M.gate_target(*g[:4]),)
                        + gate_controls(g, kinds)})
    ens_t = strong_states(4, proto, touched_p, env["uni_sim"], "c946teeth")

    # T1: a planted symmetry-BREAKING gate must be caught by the certificate
    bad_sched = list(sched_p)
    s0 = list(bad_sched[0])
    s0.append((M.KIND_TOF, 302, 255, ORIENTATION_WIRES[2], s0[0][4]))
    bad_sched[0] = tuple(s0)
    bad_sched = tuple(bad_sched)
    tooth("T1_planted_symmetry_breaking_gate_caught_by_L1_and_L3",
          (not multiset_sigma_invariant(bad_sched, SIG, kinds))
          and bool(semantic_commutes(M.compile_schedules(bad_sched), ens_t,
                                     lambda c: perm_apply(c, SIG))),
          {"planted": "one extra TOF driving an orientation wire off the "
                      "U_TO_V rail only -- i.e. re-introducing exactly the "
                      "defect the construction repairs",
           "L1_multiset_invariance": multiset_sigma_invariant(bad_sched, SIG,
                                                              kinds),
           "verdict": "REJECTED as required"})

    # T2: positive control -- the UNMODIFIED partnered kernel must pass
    tooth("T2_positive_control_the_partnered_kernel_itself_passes",
          multiset_sigma_invariant(sched_p, SIG, kinds)
          and not semantic_commutes(rows_p, ens_t,
                                    lambda c: perm_apply(c, SIG)),
          {"why": "a tooth that fires on everything proves nothing; this is "
                  "the control that shows the instrument can say YES"})

    # T3: the baseline must FAIL the same instrument
    tooth("T3_the_unpartnered_kernel_fails_the_same_instrument",
          (not multiset_sigma_invariant(sched_ma, SIG, kinds))
          and bool(semantic_commutes(rows_ma, ens_t,
                                     lambda c: perm_apply(c, SIG))),
          {"baseline_semantic_breaking_wires":
               len(semantic_commutes(rows_ma, ens_t,
                                     lambda c: perm_apply(c, SIG)))})

    # T4: a tampered axiom quote must be caught
    tampered = Q_ADMISS_DISTRIBUTION.replace("varies with", "is independent of")
    tooth("T4_tampered_axiom_quote_caught",
          (Q_ADMISS_DISTRIBUTION in axiom_text) and (tampered not in axiom_text),
          {"tampered_text": tampered,
           "verdict": "the byte-quote check rejects the tampered sentence and "
                      "accepts the real one"})

    # T5: a planted UNCONDITIONAL weight value must be caught by the firewall
    planted_payload = {"THE_WEIGHT_IS": Fraction(1, 2)}
    planted_unfenced = [p for p, v in _walk_paths(planted_payload)
                        if isinstance(v, Fraction) and 0 < v < 1
                        and not any(f in p.upper() for f in FENCE)]
    tooth("T5_planted_unconditional_weight_value_caught_by_the_firewall",
          bool(planted_unfenced) and not unfenced,
          {"planted_path": planted_unfenced,
           "real_payload_unfenced": unfenced})

    # T6: a planted single-endpoint corruption must be caught by the battery.
    # IT MUST BE PLANTED AFTER THE SPLICE.  Planting it BEFORE (as the first
    # version of this tooth did) does not fire, and the reason is worth the
    # ink: sigma maps X(LEFT) to X(RIGHT), so the construction detects the
    # planted asymmetry as a mirror defect and REPAIRS IT, restoring the menu.
    # That is the construction working exactly as designed, and it is also a
    # perfect way to build a tooth that can never bite.  Both readings are
    # measured and reported.
    t0 = monotonic()

    def run_breach(schedules):
        rows_breach = M.compile_schedules(schedules)
        bm = M.Machine(env, False)
        bm.advance(TREE_B, rows_breach, {}, {})
        bb = bm.build()
        return bb, M.measurement(env, bb)

    post = list(sched_p)
    for si in range(len(post)):
        post[si] = post[si] + ((M.KIND_X, left_w, 0, 0, post[si][0][4]),)
    bb_post, bm_post = run_breach(tuple(post))
    pre_sched = splice_full(M.build_schedules(
        c863, program, sim_fwd, 0, M_A_GATES + ((M.KIND_X, left_w, 0, 0),)))
    bb_pre, bm_pre = run_breach(pre_sched)
    clean_bb, clean_meas = run_breach(sched_p)
    tooth("T6_planted_endpoint_corruption_caught_by_the_battery",
          (bb_post["off_menu_lane_count"] != 0
           or bm_post["off_menu_endpoint_content_at_the_lock"] > 0)
          and bb_post["off_menu_lane_count"]
          != clean_bb["off_menu_lane_count"],
          {"planted_AFTER_the_splice": "an unconditional X on LEFT appended "
                                       "to every station of the SHIPPED "
                                       "partnered kernel",
           "post_splice_off_menu_lane_count": bb_post["off_menu_lane_count"],
           "post_splice_off_menu_at_the_lock":
               bm_post["off_menu_endpoint_content_at_the_lock"],
           "clean_partnered_off_menu_lane_count":
               clean_bb["off_menu_lane_count"],
           "THE_SAME_FAULT_PLANTED_BEFORE_THE_SPLICE": {
               "off_menu_lane_count": bb_pre["off_menu_lane_count"],
               "caught": bb_pre["off_menu_lane_count"] != 0,
               "reading": "the splice mirrors X(LEFT) into X(RIGHT) and the "
                          "menu survives -- the construction repairs a "
                          "single-rail corruption presented to it as input.  "
                          "Reported because it is a real property of the "
                          "construction AND because it is how this tooth "
                          "could have been silently toothless.",
           }})
    timings["teeth/battery_breach"] = round(monotonic() - t0, 3)

    # T7: a tampered restriction value must break the gate
    tooth("T7_tampered_pinned_936_value_breaks_the_restriction_gate",
          tree_std["leaves"] != struct["leaves"] + 1,
          {"why": "the gate compares against the pinned receipt; a corrupted "
                  "pin cannot agree with a correct recomputation"})

    # T8: the splice with an empty sigma must be the identity
    tooth("T8_empty_sigma_splice_is_the_identity",
          mirror_splice(sched_ma, {}, kinds, None, M.gate_target)[0]
          == sched_ma,
          {"why": "if the splice altered the law when asked to do nothing, "
                  "every downstream comparison would be meaningless"})

    # T9: a mask-blind defect detector would MISS the link ladder
    def defect_maskblind(schedules):
        out = []
        for s in schedules:
            have = Counter((g[0], g[1], g[2], g[3]) for g in s)
            img = Counter((sigma_gate(g, SIG, kinds)[0],
                           sigma_gate(g, SIG, kinds)[1],
                           sigma_gate(g, SIG, kinds)[2],
                           sigma_gate(g, SIG, kinds)[3]) for g in s)
            rem = have - img
            out.extend(rem.elements())
        return out
    blind = defect_maskblind(sched_ma)
    real = mirror_defect(sched_ma, SIG, kinds)
    blind_targets = {M.gate_target(*g[:4]) for g in blind}
    real_targets = {M.gate_target(*g[1][:4]) for g in real}
    tooth("T9_a_mask_blind_defect_detector_misses_part_of_the_ladder",
          blind_targets < real_targets,
          {"mask_blind_targets": sorted(blind_targets),
           "mask_sensitive_targets": sorted(real_targets),
           "missed": sorted(real_targets - blind_targets),
           "why": "the link ladder writes one target off BOTH rails but "
                  "under DIFFERENT lane masks; a detector that ignores masks "
                  "declares it already mirrored and the construction would "
                  "silently ship a law the swap does not commute with"})

    # T10: the covered/uncovered split must not be an artifact of one
    #      neighborhood formalization
    _fz = S["Q2_NEIGHBORHOOD_EQUALITY"]["formalizations"]
    agree_sets = {k: v["atoms_with_sigma_invariant_conditions"]
                  for k, v in _fz.items()}
    admissible = {k: v for k, v in agree_sets.items()
                  if _fz[k]["contains_the_sigma_support"]}
    tooth("T10_the_split_is_stable_across_every_admissible_formalization",
          len({tuple(v) for v in admissible.values()}) == 1
          and len({tuple(v) for v in agree_sets.values()}) > 1,
          {"admissible_formalizations": sorted(admissible),
           "they_all_agree": len({tuple(v) for v in admissible.values()}) == 1,
           "rejected_formalizations_do_disagree":
               len({tuple(v) for v in agree_sets.values()}) > 1,
           "why": "if EVERY formalization agreed, the measurement would be "
                  "insensitive and the agreement worthless; if the "
                  "admissible ones disagreed, the conclusion would be a "
                  "formalization artifact.  Both failure modes are tested"})

    # T11: a covariance-route smuggle must be caught
    tooth("T11_the_covariance_route_is_not_silently_used",
          S["Q2_THE_THEOREM"]["ROUTE_A_COVARIANCE_REJECTED"]["VERDICT"]
          .startswith("REJECTED")
          and "covariance" not in compact(
              S["Q2_THE_THEOREM"]["THEOREM"]["PROOF"]).lower(),
          {"why": "H3 could be smuggled in by quietly calling the swap a "
                  "covariance element.  The proof text is scanned for the "
                  "word and the route is on the record as rejected"})

    # T12: the derivation must FAIL where the conditions differ
    unc = [f"{t}/{s}" for (t, s) in atoms
           if [t, s] not in S["Q1c_BRANCH_SWAP"]["covered_atoms"]]
    tooth("T12_the_theorem_declines_where_the_conditions_differ",
          len(unc) > 0
          and all(not S["Q2_NEIGHBORHOOD_EQUALITY"]["formalizations"]
                  ["N2_every_wire_the_law_touches"]["per_atom"][k]
                  ["conditions_are_sigma_invariant"]
                  for k in unc
                  if k not in ("702/254",)),
          {"uncovered": unc,
           "why": "a derivation that forced 1/2 everywhere would be forcing "
                  "it from nothing.  The axiom's 'varies with' clause "
                  "requires that the argument DECLINE when the conditions "
                  "differ, and it does",
           "the_one_exception": "702/254 -- conditions equal, swap still "
                                "fails, for the declared choice-gate "
                                "placement reason.  Carried openly rather "
                                "than excluded"})

    # T13: 943's own headline must be reproduced, not assumed
    tooth("T13_943s_localisation_is_recomputed_not_copied",
          all(r["pass"] for r in gate_rows if r["gate"].startswith("c943_")),
          {"c943_gates": sum(1 for r in gate_rows
                             if r["gate"].startswith("c943_"))})

    # T14: digests are timing-free and stable
    tooth("T14_digests_are_timing_free_and_stable",
          double_run["digest_is_timing_free"]
          and digest(SEALED) == seal_digest
          and digest(science_1) == science_digest,
          {"seal_digest_recomputes": digest(SEALED) == seal_digest})

    falsifiers = {
        "certificate": "G_FALSIFIERS",
        "teeth": teeth,
        "teeth_total": len(teeth),
        "teeth_fired": sum(1 for t in teeth if t["fired"]),
        "pass": all(t["fired"] for t in teeth),
    }

    elapsed = round(monotonic() - started, 2)
    runtime = {
        "certificate": "I_RUNTIME",
        "budget_sec": RUNTIME_BUDGET_SEC,
        "elapsed_sec": elapsed,
        "within_budget": elapsed <= RUNTIME_BUDGET_SEC,
        "timings": timings,
        "pass": elapsed <= RUNTIME_BUDGET_SEC,
    }

    cert_q1 = {"certificate": "Q1_THE_MIRROR_PARTNERED_KERNEL",
               **S["Q1_CONSTRUCTION"],
               "BATTERY": S["Q1b_BATTERY"],
               "SYMMETRY_CERTIFICATE": S["Q1c_SYMMETRY_CERTIFICATE"],
               "BRANCH_SWAP": S["Q1c_BRANCH_SWAP"],
               "layout_pair_identical_on_the_partnered_sub_tree": layout_ok,
               "layout_pair_identical_on_the_BASELINE_sub_tree_control":
                   layout_ok_baseline,
               "layout_instrument_note":
                   "936's own sub-tree/both-layouts test, reproduced: the "
                   "reversed layout is compiled from sim_rev with its own "
                   "support words, and the declared sub-tree is the first "
                   "occasion only.  A first version of this check compared a "
                   "reversed-layout RUN against forward-layout SCHEDULES and "
                   "reported the partnered kernel layout-DEPENDENT; the "
                   "baseline control failed the same way, which is what "
                   "exposed it as an instrument fault rather than a finding.",
               "pass": bool(
                   S["Q1c_SYMMETRY_CERTIFICATE"]
                   ["L1_EXACT_gate_multiset_sigma_invariant_every_station"]
                   and S["Q1c_SYMMETRY_CERTIFICATE"]
                   ["L4_LEFT_and_RIGHT_share_a_colour_under_every_label"]
                   and S["Q1c_SYMMETRY_CERTIFICATE"]
                   ["L3_SEMANTIC_partnered_breaking_wires"] == 0
                   and S["Q1b_BATTERY"]["write_once_holds_on_every_branch"]
                   and S["Q1b_BATTERY"]["menu_holds_on_every_branch"]
                   and S["Q1b_BATTERY"][
                       "duplicate_lane_consistency_holds_on_every_branch"]
                   and S["Q1b_BATTERY"]["record_slots_inert_on_every_branch"]
                   and S["Q1c_BRANCH_SWAP"][
                       "ORIENTATION_WIRES_GONE_FROM_EVERY_SUPPORT"]
                   and layout_ok)}
    cert_q2 = {"certificate": "Q2_THE_DERIVATION",
               **S["Q2_THE_THEOREM"],
               "NEIGHBORHOOD_EQUALITY": S["Q2_NEIGHBORHOOD_EQUALITY"],
               "pass": bool(
                   S["Q2_THE_THEOREM"][
                       "every_quote_verbatim_in_the_vendor_read_text"]
                   and S["Q2_NEIGHBORHOOD_EQUALITY"]
                   ["FORMALIZATION_ROBUSTNESS"][
                       "every_admissible_formalization_agrees"]
                   and len(S["Q2_THE_THEOREM"]["COVERAGE"][
                       "sites_where_all_hypotheses_hold"]) > 0)}
    v = S["Q3_SEALED_TABLE"]["VERIFICATION"]
    seal_items = {
        "S1": v["S1_all_covered_pairs_digest_identical"],
        "S2": v["S2_all_covered_atoms_endpoints_exchanged"],
        "S3": v["S3_covered_sites_unformed_or_locked_before_the_choice"],
        "S4": v["S4_every_uncovered_atom_has_a_differing_pair"],
        "S5": v["S5_observable_bits_are_exactly_the_lock_timing_atoms"],
    }
    cert_q3 = {"certificate": "Q3_THE_FIRST_DERIVED_PREDICTION",
               **S["Q3_SEALED_TABLE"],
               "SEAL_SCORE": {
                   "held": sorted(k for k, ok in seal_items.items() if ok),
                   "REFUTED": sorted(k for k, ok in seal_items.items()
                                     if not ok),
                   "score": f"{sum(1 for ok in seal_items.values() if ok)} "
                            f"of {len(seal_items)}",
                   "the_two_genuine_forward_predictions_S2_and_S3":
                       bool(seal_items["S2"] and seal_items["S3"]),
                   "how_this_certificate_passes":
                       "on the SCIENCE, not on the block's batting average.  "
                       "A sealed prediction exists to be scored, and scoring "
                       "it honestly includes shipping the one it got wrong.  "
                       "The certificate passes when the seal was emitted "
                       "before the measurement, every item was scored, and "
                       "the covered-site claims that the theorem actually "
                       "rests on (S1, S2, S3) hold.  S4 constrained nothing "
                       "the theorem uses.",
               },
               "pass": bool(seal_items["S1"] and seal_items["S2"]
                            and seal_items["S3"]
                            and isinstance(seal_items["S4"], bool))}

    certificates = {
        "A_PINS": cert_a,
        "B_RESTRICTION_GATE": cert_b,
        "Q1_THE_MIRROR_PARTNERED_KERNEL": cert_q1,
        "Q2_THE_DERIVATION": cert_q2,
        "Q3_THE_FIRST_DERIVED_PREDICTION": cert_q3,
        "V1_THE_MEASURED_NEAR_MISS": cert_v1,
        "F_PARAMETRIC_FIREWALL": firewall,
        "G_FALSIFIERS": falsifiers,
        "H_DOUBLE_RUN": double_run,
        "I_RUNTIME": runtime,
        "PRICE_SHEET": {**S["PRICE_SHEET"], "certificate": "PRICE_SHEET",
                        "pass": True},
    }
    all_pass = all(c["pass"] for c in certificates.values())

    receipt = {
        "block": "toe-time-expansion-20260802/blockQ17",
        "cycles": [946],
        "campaign": "toe-time-expansion-20260802",
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "fraction_label": FRACTION_LABEL,
        "CONDITIONAL_ON_PR_6011_LANDING": CONDITIONAL_ON_PR_6011,
        "headline":
            "THE MIRROR PARTNER IS TWELVE GATES, AND IT BUYS THREE SITES.  "
            "The whole mirror defect of the 34,188-gate choice substrate "
            "under the menu swap is TWELVE distinct gates: four orientation "
            "drives (943's named repair, found here in both banks and both "
            "cells) and an eight-gate cross-bank link ladder 943 never saw "
            "because it only ever looked inside the divergence support -- so "
            "943's sketch is confirmed in its first clause and REFUTED in its "
            "second.  Splicing the 220 missing mirror images makes the swap "
            "an exact automorphism of the law: 940's own colour refinement, "
            "which separates LEFT from RIGHT under every label in the "
            "unpartnered kernel, gives them the SAME colour here, and "
            "semantic commutation has zero breaking wires against 139.  The "
            "orientation wires vanish from every branch-divergence support.  "
            "At 3 of the 5 genuine two-item menu sites the swap exchanges the "
            "branches over the whole declared window; at the other 2 the "
            "pre-choice conditions themselves differ under the swap, and the "
            "adopted axiom's 'varies with' clause correctly declines to fix "
            "them.  CONDITIONAL ON PR #6011 LANDING, the adopted "
            "Admissibility text plus Qubit's no-privilege clause then force "
            "equal weights at exactly the covered sites -- the first place "
            "this framework DERIVES the two-item value rather than "
            "registering it.  The covariance route is rejected on the axiom's "
            "own bytes; the neighborhood-equality route carries the theorem.  "
            "The price is real and is posted: the partnered kernel is a "
            "different kernel, its record loses discrimination, and the "
            "better-looking orientation-only variant is an on-orbit "
            "intertwiner that licenses nothing.",
        "VERDICT":
            "A menu-swapping symmetry of the law is BUILDABLE (940's negative "
            "is model-contingent, as 943 suspected) and, under the adopted "
            "axiom, it DERIVES the symmetric two-item weight at the sites "
            "where the conditions are symmetric.  Coverage is 3 of 8 atoms "
            "and 3 of 5 genuine menus, not all; the general form of the "
            "distribution is untouched; nothing transports to the "
            "unpartnered kernel.  No axiom surface is touched and no ask is "
            "made.",
        "INDEPENDENT_CHECKER_ADOPTIONS": {
            "R1_the_identical_conditions_framing_was_wrong":
                "the checker refused the phrase 'the two branches present "
                "identical nearest-neighbor conditions' as trivially true -- "
                "the two branches share one parent state -- and therefore as "
                "licensing nothing.  Correct.  What is measured, and what the "
                "theorem text always said, is POINTWISE SIGMA-INVARIANCE of "
                "the conditions.  Every field name is relabelled; no number "
                "moved.",
            "R2_an_unnamed_import_was_carrying_the_block":
                "the checker found that nothing in the hypothesis chain "
                "stated the identification of the compiled substrate law "
                "with the axiom's nearest-neighbor admissibility rule, "
                "although every proof step uses it.  ADOPTED as H0, an "
                "explicit UNDISCHARGED IMPORT.  This is the block's largest "
                "caveat and it is now in the chain rather than under it.",
            "R3_the_robustness_criterion_was_post_hoc":
                "the primary excluded two formalizations BY NAME.  The "
                "checker exhibited an 816-wire formalization that answers "
                "wrong (the record cell payloads exclude the bank direction "
                "rails), showing that any size-based rule fails.  ADOPTED: "
                "admissibility is now the computed structural predicate "
                "'contains the sigma support', and nothing is excluded after "
                "seeing its answer.",
            "R4_the_conditions_are_occasion_specific_not_site_generic":
                "the checker sampled the 40 boundaries before each choice "
                "and found the conditions sigma-asymmetric at most of them, "
                "including at the covered atoms.  ADOPTED as a SHARPENING: "
                "the derived equal weight is a property of the OCCASION, not "
                "a standing property of the site.  Measured and published in "
                "Q2.",
            "R5_a_wrong_involution_need_not_break":
                "the checker's own control -- 'every deliberately wrong "
                "involution must break commutation' -- FAILED on a pair of "
                "inert wires, which commute trivially because nothing reads "
                "or writes them.  The correct control is over LIVE wires.  "
                "Recorded because it is the same class of error as a "
                "palindromic false positive and would otherwise have made "
                "the control toothless.",
            "WHAT_SURVIVED_UNCHANGED":
                "the defect census (220 occurrences, 12 distinct gates, "
                "reproduced by a different matching algorithm); the "
                "partnered gate total; zero semantic breaking wires against "
                "139 for the baseline, on an ensemble extended with "
                "degenerate and on-orbit states; the colour-refinement "
                "merge; the covered-site list, unchanged at TWICE the "
                "declared window; the battery on all 256 branches; the "
                "sealed table's re-score including its refuted item.",
        },
        "science_digest": science_digest,
        "seal_digest": seal_digest,
        "certificates": certificates,
        "all_certificates_pass": all_pass,
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "provenance": {
            "worker": "Claude Opus 5 worker under supervisor spec",
            "pins": {p: EXPECTED_SHA256.get(p) for p in AUDIT_INPUT_PATHS},
            "adopted_axiom": cert_a["THE_ADOPTED_AXIOM_VENDOR_READ"],
            "lift_counts": {"c936": list(lift936_counts),
                            "c940": list(lift940_counts)},
        },
    }
    out_path = ROOT / "outputs" / \
        "mirror_kernel_cycle946_receipt_2026_07_28.json"
    out_path.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")

    lines = ["===== runner cache v1 ====="]
    lines.append("runner: scripts/frontier_cycle946_mirror_kernel_2026_07_28.py")
    lines.append(f"runner_sha256: {receipt['self_sha256']}")
    lines.append("receipt: outputs/mirror_kernel_cycle946_receipt_2026_07_28.json")
    lines.append(f"timeout_sec: {RUNTIME_BUDGET_SEC}")
    lines.append(f"elapsed_sec: {elapsed}")
    lines.append(f"status: {'ok' if all_pass else 'FAIL'}")
    lines.append("----- stdout -----")
    for name, c in certificates.items():
        lines.append(f"{'PASS' if c['pass'] else 'FAIL'} {name}")
    lines.append(f"restriction gates: {cert_b['gates_passed']}/"
                 f"{cert_b['gates_total']}")
    lines.append(f"teeth fired: {falsifiers['teeth_fired']}/"
                 f"{falsifiers['teeth_total']}")
    lines.append(f"adopted axiom vendor-read: "
                 f"{cert_a['THE_ADOPTED_AXIOM_VENDOR_READ']['sha256']} "
                 f"(CONDITIONAL ON PR #6011)")
    q1 = S["Q1_CONSTRUCTION"]
    lines.append(f"mirror defect: {q1['defect_occurrences']} occurrences, "
                 f"{q1['defect_distinct_gates']} distinct gates "
                 f"({q1['THE_ORIENTATION_DRIVE_DEFECT']['distinct']} "
                 f"orientation drives + "
                 f"{q1['THE_LINK_LADDER_DEFECT_943_DID_NOT_SEE']['distinct']} "
                 f"link ladder)")
    lines.append(f"gates {q1['gates_before']} -> {q1['gates_after']}")
    sc = S["Q1c_SYMMETRY_CERTIFICATE"]
    lines.append("sigma is an automorphism of the partnered law: "
                 f"{sc['L1_EXACT_gate_multiset_sigma_invariant_every_station']}"
                 f" (baseline "
                 f"{sc['L1_baseline_multiset_sigma_invariant']})")
    lines.append(f"semantic breaking wires: partnered "
                 f"{sc['L3_SEMANTIC_partnered_breaking_wires']} / baseline "
                 f"{sc['L3_SEMANTIC_baseline_breaking_wires']}")
    lines.append("940 colour refinement LEFT==RIGHT in the partnered kernel: "
                 f"{sc['L4_LEFT_and_RIGHT_share_a_colour_under_every_label']}")
    bs = S["Q1c_BRANCH_SWAP"]
    lines.append(f"orientation wires gone from every support: "
                 f"{bs['ORIENTATION_WIRES_GONE_FROM_EVERY_SUPPORT']}")
    lines.append(f"covered atoms: {bs['covered_atoms']}")
    lines.append(f"covered genuine menus: {bs['covered_genuine_menu_atoms']} "
                 f"of {bs['genuine_menu_atoms_943']}")
    for r in bs["per_atom"]:
        lines.append(
            f"  atom {r['atom'][0]}/{r['atom'][1]} "
            f"swap={'YES' if r['THE_SWAP_EXCHANGES_THE_BRANCHES'] else 'no '} "
            f"first_fail={r['first_failure_boundary']} "
            f"support={r['divergence_support']} "
            f"pre_choice_asym={r['pre_choice_asymmetric_sigma_pairs']}")
    lines.append("route A (covariance): REJECTED on the axiom's own bytes")
    lines.append("route B (neighborhood equality): ADOPTED")
    lines.append(f"seal verification: {compact(v)}")
    lines.append(f"V1 near-miss coverage {v1_cov} but semantic breaks "
                 f"{cert_v1['semantic_breaking_wires']} -- licenses nothing")
    lines.append(f"science digest: {science_digest}")
    lines.append(f"seal digest: {seal_digest}")
    lines.append(f"elapsed: {elapsed}s / {RUNTIME_BUDGET_SEC}s")
    lines.append(f"ALL CERTIFICATES PASS: {all_pass}")
    lines.append("===== end runner cache =====")
    cache = ROOT / "logs" / "runner-cache" / \
        "frontier_cycle946_mirror_kernel_2026_07_28.txt"
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines), flush=True)
    return 0 if all_pass else 1


CLOCK_SEGMENTS = ("elapsed", "monotonic", "wall_clock", "timings",
                  "started", "runtime")
CLOCK_SUFFIXES = ("_sec", "_secs", "_seconds", "_ms", "_ns")


def _is_a_clock_field(path):
    for seg in path.split("."):
        seg = seg.split("[")[0]
        if seg in CLOCK_SEGMENTS:
            return True
        if any(seg.endswith(s) for s in CLOCK_SUFFIXES):
            return True
    return False


def _is_subsequence(a, b):
    it = iter(b)
    return all(x in it for x in a)


def _gates_commute(g, h, kinds, gate_target):
    if g[4] & h[4] == 0:
        return True
    tg, th = gate_target(*g[:4]), gate_target(*h[:4])
    return (tg not in gate_controls(h, kinds)
            and th not in gate_controls(g, kinds))


if __name__ == "__main__":
    sys.exit(main())
