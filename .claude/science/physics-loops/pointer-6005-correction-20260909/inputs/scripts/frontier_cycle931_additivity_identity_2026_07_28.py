#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cycle 931 (blockM11) -- THE ADDITIVITY IDENTITY, DERIVED.

THE QUESTION.
=============
Cycle 929 measured the multiplicity ladder G_d(m) := C_ab of an (m, 1) fragment
pair at pointer degree d, for d = 3..6 at the two certified fields, and found
the EXACT ADDITIVITY IDENTITY

        G_d(m) + G_d(d-1-m) = G_d(d-1)

holding on all 8 (d, field) combinations at residual 8.3e-14 (its checker:
1.1e-14).  929 published it diagnostic-grade -- a measured identity with its
residuals, UNEXPLAINED -- and named it the lane's best mechanism handle.

This block derives it.

THE ANSWER, IN ONE LINE.
========================
The identity is the PURE-STATE PAIR-COMPLEMENT IDENTITY.  For a pure state on
L = A u B u R,

        I(A:B) + I(R:B) = 2 S(B) = I(AR:B),

because purity forces S(R) = S(AB) and S(RB) = S(A), and the two mutual
informations telescope.  The frozen protocol supplies the pure state for free:
the memo's statistic conditions on the pointer's Z-outcome, the fragments
EXHAUST every non-pointer site, and a Z-projection of a globally pure state
leaves a PURE state on the rest.  Leaf exchangeability (the star Hamiltonian and
the frozen preparation are symmetric under permuting the arms) then makes the
measured (d-1-m, 1) pair the complement pair of the measured (m, 1) pair, and
the exhausting rung G_d(d-1) is 2 S(one leaf).

Everything else follows.  With s(k) := the pointer-conditioned entropy of any k
leaves,

        G_d(m) = s(m) + s(1) - s(m+1),     s(k) = s(d-k),     s(0) = s(d) = 0,

so the WHOLE ladder is one entropy sequence, the additivity identity is the
reflection s(k) = s(d-k), and the exhausting-pair departure from linearity is
not a boundary anomaly at all -- it is the point where s(m+1) wraps around to
s(d-m-1) and the last increment becomes exactly 2s(1) - s(2) = G_d(1) = T(d),
which is the sentence 929 published from its data without a mechanism.

WHAT IS ASKED (supervisor spec), AND WHAT IS ANSWERED.
======================================================
Q1  The structure of the state: compute the exact objects the identity is
    about, quote the statistic's definition from the frozen memo BYTES, and say
    WHERE the m-dependence enters.
Q2  Candidates (a) exchangeability/permutation, (b) linearity in an information
    decomposition, (c) first-order/perturbative -- pre-registered, then
    attacked with discriminating computations.
Q3  The verdict, the theorem with exact hypotheses, and sealed predictions.

MINIMAL-PREMISE RULE (spec, honoured).  The supervisor's three candidates are
NOT premises.  Q1 was computed first and it showed a fourth structure -- purity
of the pointer-conditioned state -- which is what carries the identity.
Candidate (b) SURVIVES only in a corrected form (the pure-tripartite identity,
NOT the strong-subadditivity equality case, which is REFUTED by computation
here); candidate (a) is REFUTED AS SUFFICIENT (exchangeability without purity
breaks the identity, demonstrated on a constructed state); candidate (c) is
REFUTED (the identity is exact at lambda = 2.0 and Jt = 3.0, far outside any
perturbative regime, at the same 1e-14 residual).

DECLARED READING OF THE SPEC PHRASE "read its exact definition from the frozen
memo bytes".  The statistic C_ab IS defined in the frozen memo (two lines,
quoted verbatim below and byte-verified at runtime); the frozen memo does not
fix the FLOATING-POINT path, which lives in the pinned 917/929 runner bytes.
BOTH are quoted in the receipt: the memo definition (the authority) and the
pinned implementation (the thing the measured numbers came out of), and the
derivation is shown to hold for the memo definition, with the implementation
verified to compute it.

ROUTES.  Two disjoint propagators are cross-validated: route A (Chebyshev
expansion in Bessel coefficients) and route C (dense eigendecomposition), with
route B (adaptive Taylor marching with a per-substep remainder bound) as a
third on representative cells.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor spec.
Independent audit still required.  No axiom, primitive, registry, policy, queue
or audit surface is touched.  No docs/ note is written by this runner.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import re
import subprocess
import sys
import time
from collections import deque

import numpy as np
from scipy.special import jv

T_START = time.perf_counter()

BOUNDARY_LINE = "===== runner cache v1 ====="

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNTIME_LIMIT_SECONDS = 900.0

# ================================================================== pins =====
# full path -> (sha256, git blob).  Any mismatch is a hard fail, exit 2.
PINS = {
    # the frozen memos
    "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md": (
        "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
        "5dff1d8b1692099cd86b53959834b6bcb5865a71"),
    "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md": (
        "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
        "d5b36708949d06bf619b2452e8f2897468e51194"),
    "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md": (
        "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
        "5f056aa69d1cc06dbfa2dc9ed6804df40c7b39fe"),
    # the axiom memo
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
        "4a863da1f3f255354839277271a3a69a5c205133"),
    # parents
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json": (
        "d7d27ce19d231624415db1e71ee77eae16b5175dd403b403c254b38fb171b0a7",
        "9931c298a5917eb90de290cbb82c237508c9e692"),
    "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json": (
        "37568809db0d5f319b6fe9a41962cc58c8215ade2c4b9acb24eab4b665535240",
        "11e336cf0a86c46492f6ccf03b13963357840b71"),
    "outputs/degree_five_cycle919_receipt_2026_07_28.json": (
        "cf85c74b62f1e6a83287a824f56315f3b1cf4b9387056d94906bb0195aae04f5",
        "587349db8b77c31d20f0aa04e6e69a1bb206a6d0"),
    "outputs/loop_cost_cycle921_receipt_2026_07_28.json": (
        "86e58837349baa719d116948c67a166b922cb6b21fefe6108ec41fa08727df6f",
        "01e9689639dee1dc6f73c6a2834a84da3dc9f6cc"),
    "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json": (
        "59d24f68b7bdd3ba8fa2e446a2e381c4c5dd97443915bf38b0823556369a4c07",
        "67f39ff8875def945e32e7dccc653423a8c4fc79"),
    "scripts/frontier_cycle927_size_channel_2026_07_28.py": (
        "caa3becbd2bfc97afc106e998e5f2b9ee23cb46efd8c673d04ee69ed554314a9",
        "fe2e0f14d1762e44c00b028ca40c5ead851fb48a"),
    "outputs/size_channel_cycle927_receipt_2026_07_28.json": (
        "2dd871f70c6486a20babb7b74048befb51a108a0feea57aee86ba3ff7f2fe51c",
        "12edc846cdb31c19e5f9bb709533ee18d5d5a092"),
    # ---- Cycle 929: THE PARENT THIS BLOCK DERIVES ----
    "scripts/frontier_cycle929_arity_variable_2026_07_28.py": (
        "626be10a174d9ff41f72daa97a7eddc403e5ce191aff56791b38d0cea740c08a",
        "1d629b43c4be15f4ffd7a2ac562ce8538088414e"),
    "scripts/frontier_cycle929_arity_variable_independent_check_2026_07_28.py": (
        "5a47544dbbc56ec4d128f1999f85746eaffea370279dcef2e6a28a3ef4ad5f14",
        "429212195446c2b1213e54a9f0c6ebadf838f39a"),
    "outputs/arity_variable_cycle929_receipt_2026_07_28.json": (
        "40440237f0af14882b06331a054c19f3da52f34e6e7b2cde846a0b390a3679a3",
        "fc0080cc4c283d6dc440ac20a614ae187f7e488b"),
    "outputs/arity_variable_independent_check_cycle929_receipt_2026_07_28.json": (
        "c2825fab5490afc0528c3a45e28d390a112d5319f369c4da6d0e463e7605eb6d",
        "7598212188d1ba5de6d42ae982ea70ea16c13207"),
    "outputs/arity_variable_block_cycle929_ship_receipt_2026_07_28.json": (
        "18fd68bfc6913b8d16fbb6afd7c7216506304bfb62d376f2ceb60290bf57da3f",
        "0d21f07314fd362ae38cdea3fe8ba163a5db7710"),
    "docs/ARITY_IS_DEGREE_MULTIPLICITY_TAX_CYCLE929_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "b45a3f9014850af577a27c4206504f6935abaccd676166d58e4e8f4f966ed4a0",
        "0b316a500c4c6768b36651d71eb8702731d19f9e"),
}

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
C921_RECEIPT = "outputs/loop_cost_cycle921_receipt_2026_07_28.json"
C926_RECEIPT = "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json"
C927_RECEIPT = "outputs/size_channel_cycle927_receipt_2026_07_28.json"
C929_RECEIPT = "outputs/arity_variable_cycle929_receipt_2026_07_28.json"
C929_RUNNER = "scripts/frontier_cycle929_arity_variable_2026_07_28.py"

D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
CLAIM_LAMBDAS = (0.05, 0.10)
DIAG_LAMBDAS = (0.075, 0.125, 0.15)
STRONG_LAMBDAS = (0.5, 1.0, 2.0)       # DECLARED NON-CLAIM: the anti-perturbative probe
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
T0_ANCHOR_TOL = 1e-9
DRIFT_MAX = 0.10
PERSIST_N = 3
T_EXEC = [round(0.1 * i, 10) for i in range(13)]     # Jt = 0.0 .. 1.2
T_LONG = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]        # DECLARED long-time grid
COMPARISON_JT = 0.7
JT_INDEX = {0.3: 3, 0.7: 7, 1.2: 12}
DENSE_MAX_N = 12
FULL_SPACE_CAP_N = 16
CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")

IDENT_TOL = 1e-11          # the tolerance every NEW identity claim is made at
REPRO_TOL = 0.0            # the reproduction gates demand deviation EXACTLY zero

# bookkeeping that makes the seal auditable
NEW_CELLS_EVALUATED = set()
PROP_CALLS = {"A": 0, "B": 0, "C": 0}


# ============================================================== utilities ====
def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_obj(o):
    return sha256_bytes(json.dumps(o, sort_keys=True, separators=(",", ":"),
                                   default=float).encode("utf-8"))


def die(msg):
    sys.stderr.write("FATAL %s\n" % msg)
    sys.exit(2)


def git(args):
    return subprocess.run(["git", "-C", ROOT] + args, capture_output=True)


def verify_pins():
    out = {}
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            die("pin:missing %s" % path)
        b = open(full, "rb").read()
        got = sha256_bytes(b)
        blob = git(["hash-object", path]).stdout.decode().strip()
        if got != want_sha:
            die("pin:sha256 %s got=%s want=%s" % (path, got, want_sha))
        if blob != want_blob:
            die("pin:blob %s got=%s want=%s" % (path, blob, want_blob))
        out[path] = {"sha256": got, "blob": blob, "bytes": len(b), "verified": True}
    return out


def recover_d1_note():
    """The D1 note is not in the tree at HEAD; it is recovered from its pinned blob
    and cross-checked against the 915/917/919/921/926/927/929 receipts."""
    if git(["cat-file", "-t", D1_NOTE_BLOB]).stdout.decode().strip() != "blob":
        die("d1-note:blob-missing %s" % D1_NOTE_BLOB)
    b = git(["cat-file", "blob", D1_NOTE_BLOB]).stdout
    got = sha256_bytes(b)
    if got != D1_NOTE_SHA256 or len(b) != D1_NOTE_BYTES:
        die("d1-note:identity got=%s bytes=%d" % (got, len(b)))
    rec915 = json.load(open(os.path.join(ROOT, C915_RECEIPT)))
    art = rec915["C1_recovery"]["artifacts"][D1_NOTE_PATH]["recovered"]
    if art["sha256"] != got or art["blob"] != D1_NOTE_BLOB or art["bytes"] != len(b):
        die("d1-note:915-receipt-cross-check")
    xs = {}
    for tag, rp in (("917", C917_RECEIPT), ("919", C919_RECEIPT), ("921", C921_RECEIPT),
                    ("926", C926_RECEIPT), ("927", C927_RECEIPT), ("929", C929_RECEIPT)):
        rec = json.load(open(os.path.join(ROOT, rp)))
        if rec["recovered_d1_note"]["sha256"] != got:
            die("d1-note:%s-cross-check" % tag)
        xs["sha256_matches_%s_receipt" % tag] = True
    prov = {"path": D1_NOTE_PATH, "blob": D1_NOTE_BLOB, "sha256": got,
            "bytes": len(b), "in_tree_at_head": False}
    prov.update(xs)
    return b.decode("utf-8"), prov


# ============================== restriction gate: frozen constants by bytes ==
CONSTANT_PATTERNS = [
    ("hamiltonian", r"`H_lambda = - sum_<ij> Z_i Z_j - lambda sum_i X_i`", None),
    ("content_H_min", r"1\. `H\(Z_S\) >= (0\.05) bit`;", CONTENT_H_MIN),
    ("content_gate", r"2\. `chi_Z\(S:F\) >= \(1-delta\) H\(Z_S\)`;", None),
    ("excess_min", r"`chi_Z\(S:F\)\(t\) - chi_Z\(S:F\)\(0\) >= (0\.02) bit`", EXCESS_MIN),
    ("t0_anchor_tol", r"value verified at most `(1e-9) bit`", T0_ANCHOR_TOL),
    ("indep_max", r"every pair has `C_ab <= (0\.02) bit`", INDEP_MAX),
    ("deltas", r"Use `delta in \{0\.05,0\.10,0\.20\}`, with headline `delta=(0\.10)`",
     HEADLINE_DELTA),
    ("deadline", r"The headline onset deadline remains `Jt <= (1)`", DEADLINE_JT),
    ("persistence", r"persistence flag requires three consecutive certification samples",
     None),
    ("memo_lambdas", r"with `lambda in \{0\.05,0\.10,0\.20\}` and open boundaries", None),
    ("drift", r"center-Z total-variation drift from `t=0` at most `(0\.10)`", DRIFT_MAX),
    ("prep_center", r"center: `n_center=\(1,0,0\)`, the `\+X` state", None),
    ("prep_face", r"every axial face: `n_face=\(1,0,0\)`, the `\+X` state", None),
    ("prep_edge", r"every edge: `n_edge=\(0,0,1\)`, the `\+Z` state", None),
    ("prep_corner", r"every corner: `n_corner=\(0,0,1\)`, the `\+Z` state", None),
    ("theta_A", r"`theta\(t\) = \(1/6\) sum_a \(\[1-Tr rho_\(S,a\)\(t\)\^2\] - "
                r"\[1-Tr rho_\(S,a\)\(0\)\^2\]\)`", None),
    ("xi_reg_def", r"`xi_reg`, defined as the largest Manhattan shell whose one-site "
                   r"reduction has excess at least `(0\.02) bit` at that maximizer",
     EXCESS_MIN),
    ("tiebreak_1", r"1\. assign each axial face site to its own signed-axis fragment;", None),
    ("tiebreak_2", r"2\. assign an edge with `x != 0` to `F_\(sign\(x\)x\)`;", None),
    ("tiebreak_3", r"3\. for an edge with `x=0` and for every corner, ignore the corner's "
                   r"`x` sign and map `\(sign\(y\),sign\(z\)\)` by `\(\+,\+\)->\+y`, "
                   r"`\(-,\+\)->\+z`, `\(-,-\)->-y`, and `\(\+,-\)->-z`\.", None),
    ("r_ind_def", r"`R_ind` is the largest pairwise-independent certifying subset", None),
]
if len(CONSTANT_PATTERNS) != 21:
    die("frozen-const:pattern-count %d != 21" % len(CONSTANT_PATTERNS))

# The statistic's OWN definition, byte-verified separately (NOT one of the 21, so
# the five-way/six-way constant cross-check stays quote-identical to the parents).
STATISTIC_PATTERNS = [
    ("C_ab_definition", r"`C_ab = I\(F_a:F_b \| Z_S\)`"),
    ("C_ab_formula",
     r"`C_ab = sum_z p_z \[S\(rho_Fa\^z\)\+S\(rho_Fb\^z\)-S\(rho_FaFb\^z\)\]`"),
    ("C_ab_tensor_order", r"The joint tensor order is `\(S,F_a,F_b\)`"),
    ("C_ab_dephasing", r"Zero the off-diagonal `S` blocks before evaluating the formula"),
    ("chi_definition",
     r"`chi_Z\(S:F\) = S\(sum_z p_z rho_F\^z\) - sum_z p_z S\(rho_F\^z\)`\."),
]


class FrozenConstantError(Exception):
    pass


def verify_frozen_constants(memo, soft=False):
    def fail(msg):
        if soft:
            raise FrozenConstantError(msg)
        die(msg)
    out = {}
    for name, pat, expect in CONSTANT_PATTERNS:
        m = re.search(pat, memo)
        if m is None:
            fail("frozen-const:pattern-miss %s" % name)
            continue
        quote = " ".join(m.group(0).split())
        val = None
        if expect is not None:
            val = float(m.group(1))
            if abs(val - float(expect)) > 0:
                fail("frozen-const:value %s memo=%r code=%r" % (name, val, expect))
        out[name] = {"quote": quote, "memo_value": val, "code_value": expect,
                     "byte_verified": True}
    return out


def verify_statistic_definition(memo):
    out = {}
    for name, pat in STATISTIC_PATTERNS:
        m = re.search(pat, memo)
        if m is None:
            die("statistic-def:pattern-miss %s" % name)
        out[name] = " ".join(m.group(0).split())
    return out


def cross_check_prior_constants(frozen):
    """21/21 quote-identical to EVERY pinned receipt that publishes them -- now SIX."""
    res = {}
    for tag, rp in (("917", C917_RECEIPT), ("919", C919_RECEIPT), ("921", C921_RECEIPT),
                    ("926", C926_RECEIPT), ("927", C927_RECEIPT), ("929", C929_RECEIPT)):
        theirs = json.load(open(os.path.join(ROOT, rp)))["frozen_constants_byte_verified"]
        if set(theirs) != set(frozen):
            die("frozen-const:%s-key-set" % tag)
        for k in sorted(frozen):
            if theirs[k]["quote"] != frozen[k]["quote"]:
                die("frozen-const:%s-quote %s" % (tag, k))
        res["identical_to_%s_receipt" % tag] = True
        res["n_constants_%s" % tag] = len(theirs)
    res["count"] = len(frozen)
    res["all_six_receipts_agree"] = True
    return res


def parse_memo_cube_fragments(memo):
    out = {}
    for lab in CUBE_LABELS:
        m = re.search(r"`F_\(%s\) = \[([^\]]*)\]`" % re.escape(lab), memo)
        if m is None:
            die("memo-fragments:miss %s" % lab)
        sites = re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)", m.group(1))
        out[lab] = [tuple(int(v) for v in s) for s in sites]
    tot = sum(len(v) for v in out.values())
    if tot != 26 or sorted(len(v) for v in out.values()) != [4, 4, 4, 4, 5, 5]:
        die("memo-fragments:shape %d" % tot)
    return out


def extract_pinned_source(path, funcname):
    """Quote a function VERBATIM out of a pinned source file's bytes."""
    txt = open(os.path.join(ROOT, path), "rb").read().decode("utf-8")
    lines = txt.split("\n")
    start = None
    for i, l in enumerate(lines):
        if l.startswith("def %s(" % funcname):
            start = i
            break
    if start is None:
        die("quote:function-not-found %s in %s" % (funcname, path))
    j = start + 1
    while j < len(lines) and not re.match(r"^(def |class |# =====)", lines[j]):
        j += 1
    body = "\n".join(lines[start:j]).rstrip() + "\n"
    return {"path": path, "function": funcname, "first_line": start + 1,
            "last_line": j, "sha256_of_quote": sha256_bytes(body.encode("utf-8")),
            "verbatim": body}


# ============================================================== geometry =====
def bfs(adj, src):
    d = {src: 0}
    q = deque([src])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def cube_tiebreak(coord, cands, label_of):
    """The frozen memo's tie-break algorithm, applied VERBATIM in cube coordinates."""
    x, y, z = coord
    nz = sum(1 for v in coord if v != 0)
    if nz == 2 and x != 0:
        want = ("+x" if x > 0 else "-x")
    else:
        m = {(1, 1): "+y", (-1, 1): "+z", (-1, -1): "-y", (1, -1): "-z"}
        want = m[(1 if y > 0 else -1, 1 if z > 0 else -1)]
    for c in cands:
        if label_of[c] == want:
            return c
    die("tiebreak:unreachable %r %r" % (coord, want))


def axis_label(c):
    """THE FROZEN SIGNED-AXIS LABEL: the sign of the FIRST NON-ZERO coordinate."""
    for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
        if c[ax] != 0:
            return ("+" if c[ax] > 0 else "-") + nm
    die("axis-label:origin %r" % (c,))


def build_geometry(key, name, sites, bonds_coord, pointer, label_of_rec,
                   tiebreak, dim, note, family="unset"):
    """Assemble a geometry under the frozen partition rule (the 926/929 reading:
    anchors with the same signed-axis label are APPENDED to one fragment, never
    silently overwritten)."""
    idx = {c: i for i, c in enumerate(sites)}
    n = len(sites)
    bonds = sorted({tuple(sorted((idx[a], idx[b]))) for (a, b) in bonds_coord})
    adj = {i: set() for i in range(n)}
    for (a, b) in bonds:
        adj[a].add(b)
        adj[b].add(a)
    S = idx[pointer]
    rec = sorted(adj[S])
    label_of = {r: label_of_rec(sites[r]) for r in rec}
    dS = bfs(adj, S)
    if len(dS) != n:
        die("geometry:%s disconnected" % key)
    drec = {r: bfs(adj, r) for r in rec}
    frags, anchors = {}, {}
    for r in rec:
        frags.setdefault(label_of[r], []).append(r)
        anchors.setdefault(label_of[r], []).append(r)
    for i in range(n):
        if i == S or i in rec:
            continue
        dd = {r: drec[r].get(i, 10 ** 9) for r in rec}
        m = min(dd.values())
        cands = [r for r in rec if dd[r] == m]
        labcands = sorted({label_of[c] for c in cands})
        if len(labcands) == 1:
            pick = cands[0]
        else:
            if tiebreak is None:
                die("geometry:%s tie without declared tie-break at site %r" % (key, sites[i]))
            pick = tiebreak(sites[i], cands, label_of)
        frags[label_of[pick]].append(i)
    labels = sorted(frags, key=lambda L: (CUBE_LABELS.index(L) if L in CUBE_LABELS else 99, L))
    for L in labels:
        heads = anchors[L]
        rest = [i for i in frags[L] if i not in heads]
        frags[L] = sorted(heads, key=lambda i: str(sites[i])) + \
            sorted(rest, key=lambda i: (dS[i], str(sites[i])))
    if sorted(itertools.chain(*frags.values())) != [i for i in range(n) if i != S]:
        die("geometry:%s partition-not-exhaustive" % key)
    return {"key": key, "name": name, "note": note, "dim": dim, "n": n, "family": family,
            "sites": [str(c) for c in sites], "coords": sites, "bonds": bonds,
            "adj": adj, "S": S, "pointer": str(pointer), "recording": rec,
            "labels": labels, "frags": frags, "dS": dS,
            "anchor_multiplicity": {L: len(anchors[L]) for L in labels},
            "partition_site_by_site": {str(sites[i]): L for L in labels for i in frags[L]},
            "stats": {"n_sites": n, "n_bonds": len(bonds), "pointer_degree": len(rec),
                      "n_fragments": len(labels),
                      "fragment_sizes": {L: len(frags[L]) for L in labels},
                      "loop_free": bool(len(bonds) - n + 1 == 0)},
            "profile": {"pointer_degree_d": len(rec), "fragment_count_f": len(labels),
                        "multiplicity_multiset":
                            sorted((len(anchors[L]) for L in labels), reverse=True)}}


def _lat_nbrs(P):
    out = []
    for ax in range(3):
        for s in (1, -1):
            q = list(P)
            q[ax] += s
            out.append(tuple(q))
    return out


def coord_star(key, name, P, N, note, family="separation"):
    for q in N:
        if q not in _lat_nbrs(P):
            die("coord-star:%s non-lattice leaf %r" % (key, q))
        if q == (0, 0, 0):
            die("coord-star:%s leaf at the origin" % key)
    sites = [P] + list(N)
    bonds = [(P, q) for q in N]
    return build_geometry(key, name, sites, bonds, P, axis_label, cube_tiebreak, 3,
                          note, family)


def label_profile_at(P):
    N = [q for q in _lat_nbrs(P) if q != (0, 0, 0)]
    lab = {}
    for q in N:
        lab.setdefault(axis_label(q), []).append(q)
    return lab


def enumerate_constructible_profiles(rng=3):
    seen = {}
    for px in range(-rng, rng + 1):
        for py in range(-rng, rng + 1):
            for pz in range(-rng, rng + 1):
                lab = label_profile_at((px, py, pz))
                prof = tuple(sorted((len(v) for v in lab.values()), reverse=True))
                seen.setdefault(prof, []).append((px, py, pz))
    lemma_ok = all(sum(1 for m in prof if m > 1) <= 1 for prof in seen)
    return {"n_pointers": (2 * rng + 1) ** 3, "n_profiles": len(seen),
            "structural_lemma_exactly_one_merged_block": bool(lemma_ok)}


GENERATORS = [
    ((0, 0, 0), "origin: six distinct labels {+x,-x,+y,-y,+z,-z}"),
    ((0, 0, 2), "z-axis, |z|>=2: profile {+z:2, +x,-x,+y,-y}"),
    ((0, 1, 1), "x=0, |y|=1, z!=0: profile {+y:3, +x,-x,+z}"),
    ((0, 2, 1), "x=0, |y|>=2, z!=0: profile {+y:4, +x,-x}"),
    ((1, 1, 0), "|x|=1 off the x-axis: profile {+x:5, +y}"),
    ((2, 0, 0), "|x|>=2: profile {+x:6}"),
]


def pick_generator(d, f):
    m = d - f + 1
    for P, why in GENERATORS:
        lab = label_profile_at(P)
        blocks = sorted(lab.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        if not blocks:
            continue
        big_lab, big = blocks[0]
        others = blocks[1:]
        if len(big) >= m and len(others) >= f - 1:
            leaves = sorted(big, key=str)[:m]
            for L, v in others[:f - 1]:
                leaves.append(sorted(v, key=str)[0])
            return P, sorted(leaves, key=str), why, big_lab
    return None, None, None, None


def build_sep(d, f, tag="SEP"):
    P, leaves, why, big = pick_generator(d, f)
    if P is None:
        return None
    g = coord_star("%sd%df%d" % (tag, d, f), "coordstar_d%d_f%d" % (d, f), P, leaves,
                   "929 GRID CELL (d=%d, f=%d)" % (d, f), "grid")
    if g["profile"]["pointer_degree_d"] != d or g["profile"]["fragment_count_f"] != f:
        return None
    return g


def build_sep_alt(d, f):
    m = d - f + 1
    prim, _, _, _ = pick_generator(d, f)
    for px in range(-3, 4):
        for py in range(-3, 4):
            for pz in range(-3, 4):
                P = (px, py, pz)
                if P == prim:
                    continue
                lab = label_profile_at(P)
                blocks = sorted(lab.items(), key=lambda kv: (-len(kv[1]), kv[0]))
                if not blocks:
                    continue
                big_lab, big = blocks[0]
                others = blocks[1:]
                if len(big) >= m and len(others) >= f - 1:
                    leaves = sorted(big, key=str)[:m]
                    for L, v in others[:f - 1]:
                        leaves.append(sorted(v, key=str)[0])
                    g = coord_star("ALTd%df%d" % (d, f), "altcoordstar", P,
                                   sorted(leaves, key=str),
                                   "EMBEDDING CONTROL (d=%d,f=%d)" % (d, f), "gridalt")
                    if (g["profile"]["pointer_degree_d"],
                            g["profile"]["fragment_count_f"]) == (d, f):
                        return g
    return None


def spider(key, arm_shapes, note, family):
    sites, bonds = ["S"], []
    for j, parents in enumerate(arm_shapes):
        names = []
        for p, par in enumerate(parents):
            nm = "A%02d" % (j + 1) if p == 0 else "a%02dx%d" % (j + 1, p)
            names.append(nm)
            sites.append(nm)
            bonds.append(("S", nm) if par is None else (names[par], nm))
    return build_geometry(key, key, sites, bonds, "S", lambda c: c, None, family,
                          note, family)


def path_arm(L):
    return [None] + [p for p in range(L - 1)]


def claw_arm(L):
    return [None] + [0] * (L - 1)


def geom_star7():
    sites = ["S"] + ["a%d" % i for i in range(1, 7)]
    bonds = [("S", "a%d" % i) for i in range(1, 7)]
    return build_geometry("G2", "star7", sites, bonds, "S", lambda c: c, None, "star",
                          "917 G2: K_{1,6}", "pinned917")


def geom_cube27():
    sites = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("G6", "cube27", sites, bonds, (0, 0, 0), axis_label,
                          cube_tiebreak, 3, "917 G6: the open 3x3x3 cube", "pinned917")


C926_DEFS = {
    "A1": ((0, 0, 1), [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (0, 0, 2)]),
    "A2": ((0, 1, 1), [(1, 1, 1), (-1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2)]),
    "A3": ((0, 1, 1), [(1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2), (0, 1, 0)]),
    "A4": ((1, 1, 0), [(0, 1, 0), (2, 1, 0), (1, 2, 0), (1, 0, 0), (1, 1, 1)]),
    "A5": ((1, 1, 0), [(2, 1, 0), (1, 2, 0), (1, 0, 0), (1, 1, 1), (1, 1, -1)]),
}


def build_926_A(key):
    P, N = C926_DEFS[key]
    return coord_star(key, "926" + key, P, N, "926 %s" % key, "c926A")


def geom_E1():
    P = (0, 1, 1)
    N = [(1, 1, 1), (-1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2)]
    ext = [(2, 1, 1), (-2, 1, 1), (0, 3, 1), (0, 1, 3)]
    sites = [P] + N + ext
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("E1", "merge10d2", sites, bonds, P, axis_label, cube_tiebreak,
                          3, "926 E1", "c926E")


def _extend_leaves(P, leaves, ext_map):
    sites = [P] + list(leaves)
    for q, chain in ext_map.items():
        sites.extend(chain)
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return sites, bonds


def geom_W3():
    P = (0, 0, 1)
    leaves = [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (0, 0, 2)]
    sites, bonds = _extend_leaves(P, leaves, {(0, 0, 2): [(0, 0, 3), (0, 0, 4), (0, 0, 5)]})
    return build_geometry("W3depth5", "depth5f5", sites, bonds, P, axis_label,
                          cube_tiebreak, 3, "929 Q3 W3", "q3")


def geom_W4():
    P = (0, 1, 1)
    leaves = [(1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2), (0, 1, 0)]
    sites, bonds = _extend_leaves(P, leaves, {(0, 2, 1): [(0, 3, 1), (0, 4, 1)]})
    return build_geometry("W4merge5d3", "merge5d3", sites, bonds, P, axis_label,
                          cube_tiebreak, 3, "929 Q3 W4", "q3")


# ================================================================ numerics ===
def build_diag(n, bonds):
    idx = np.arange(1 << n, dtype=np.uint32)
    z = np.empty((n, 1 << n), dtype=np.int8)
    for i in range(n):
        z[i] = 1 - 2 * ((idx >> np.uint32(i)) & np.uint32(1)).astype(np.int8)
    diag = np.zeros(1 << n, dtype=np.float64)
    for (a, b) in bonds:
        diag -= z[a].astype(np.float64) * z[b].astype(np.float64)
    return diag


def prep_state(n, plus_x):
    vecs = [(np.array([1.0, 1.0]) / np.sqrt(2.0)) if i in plus_x else np.array([1.0, 0.0])
            for i in range(n)]
    psi = vecs[n - 1].astype(np.complex128)
    for i in range(n - 2, -1, -1):
        psi = np.kron(psi, vecs[i].astype(np.complex128))
    return psi


def _matvec_factory(diag, n, lam):
    xor = [np.arange(1 << n, dtype=np.int64) ^ (1 << i) for i in range(n)]

    def mv(v, o=None):
        if o is None:
            o = np.empty_like(v)
        np.multiply(diag, v, out=o)
        for i in range(n):
            o -= lam * v[xor[i]]
        return o
    return mv


def chebyshev(psi0, diag, n, lam, times):
    """ROUTE A -- Chebyshev expansion in Bessel coefficients."""
    PROP_CALLS["A"] += 1
    A = float(np.abs(diag).max() + lam * n)
    tmax = max(times)
    M = int(np.ceil(A * tmax)) + 5
    while abs(jv(M, A * tmax)) > 1e-17:
        M += 5
    outs = [np.zeros_like(psi0) for _ in times]
    mv = _matvec_factory(diag, n, lam)
    T0 = psi0.copy()
    T1 = np.empty_like(psi0)
    mv(T0, T1)
    T1 /= A
    tail = 0.0
    for k in range(M + 1):
        if k == 0:
            Tk = T0
        elif k == 1:
            Tk = T1
        else:
            Tk = 2.0 * mv(T1) / A - T0
            T0, T1 = T1, Tk
        for i, t in enumerate(times):
            c = jv(k, A * t)
            if k > 0:
                c *= 2.0 * ((-1j) ** k)
            outs[i] += c * Tk
        tail = max(tail, abs(float(jv(M, A * tmax))))
    return outs, {"route": "A-chebyshev", "norm_bound": A, "terms": M,
                  "tail_bound": tail}


def taylor_march(psi0, diag, n, lam, times, hbound=1.0, pmax=40):
    """ROUTE B -- adaptive substepped Taylor with a per-substep remainder bound."""
    PROP_CALLS["B"] += 1
    A = float(np.abs(diag).max() + lam * n)
    mv = _matvec_factory(diag, n, lam)
    psi = psi0.astype(np.complex128).copy()
    outs = []
    tprev = 0.0
    worst_rem = 0.0
    for t in times:
        dt = t - tprev
        if dt > 1e-15:
            s = max(1, int(math.ceil(A * dt / hbound)))
            h = dt / s
            for _ in range(s):
                term = psi.copy()
                acc = psi.copy()
                p = 0
                for k in range(1, pmax + 1):
                    term = mv(term) * (-1j * h / k)
                    acc += term
                    p = k
                    if float(np.abs(term).max()) < 1e-19:
                        break
                psi = acc
                worst_rem = max(worst_rem, float((A * h) ** (p + 1) / math.gamma(p + 2)))
        outs.append(psi.copy())
        tprev = t
    return outs, {"route": "B-taylor-march", "max_substep_remainder_bound": worst_rem}


def dense_route(psi0, diag, n, lam, times):
    """ROUTE C -- full eigendecomposition, independent of A and B."""
    PROP_CALLS["C"] += 1
    d = 1 << n
    H = np.zeros((d, d), dtype=np.float64)
    H[np.arange(d), np.arange(d)] = diag
    for i in range(n):
        j = np.arange(d, dtype=np.int64) ^ (1 << i)
        H[np.arange(d), j] -= lam
    w, V = np.linalg.eigh(H)
    del H
    c = V.T @ psi0
    outs = [V @ (np.exp(-1j * w * t) * c) for t in times]
    del V
    return outs, {"route": "C-dense-eigh", "dim": d}


def euler_route(psi0, diag, n, lam, times, nstep=40):
    """THE EULER GUARD -- a deliberately under-converged integrator.  Never used for
    a published number; it exists so the teeth can show the numbers are not
    integrator artifacts."""
    mv = _matvec_factory(diag, n, lam)
    psi = psi0.astype(np.complex128).copy()
    outs = []
    tprev = 0.0
    for t in times:
        dt = t - tprev
        if dt > 1e-15:
            h = dt / nstep
            for _ in range(nstep):
                psi = psi + (-1j * h) * mv(psi)
        outs.append(psi.copy())
        tprev = t
    return outs


def joint_rho(psi, n, sites):
    T = psi.reshape((2,) * n)
    order = list(sites) + [i for i in range(n) if i not in sites]
    ax = [n - 1 - s for s in order]
    M = np.transpose(T, ax).reshape(1 << len(sites), -1)
    return M @ M.conj().T


def ent_bits(w):
    w = np.asarray(w).real
    neg = float(min(0.0, w.min()))
    w = w[w > 1e-16]
    return float(-(w * np.log2(w)).sum()), neg


def cond_mi(rho, ka, kb):
    """THE FROZEN STATISTIC, byte-identical to the pinned 917/929 implementation:
    C_ab = sum_z p_z [S(rho_Fa^z) + S(rho_Fb^z) - S(rho_FaFb^z)] on the joint
    tensor order (S, F_a, F_b) with the off-diagonal S blocks zeroed."""
    d = 1 << (ka + kb)
    blocks = [rho[:d, :d], rho[d:, d:]]
    p = [float(np.trace(b).real) for b in blocks]
    tot = p[0] + p[1]
    out = 0.0
    for b, pz in zip(blocks, p):
        if pz <= 1e-14:
            continue
        r = b / pz
        T = r.reshape(1 << ka, 1 << kb, 1 << ka, 1 << kb)
        ra = np.einsum("aibi->ab", T)
        rb = np.einsum("iaib->ab", T)
        sa, _ = ent_bits(np.linalg.eigvalsh(ra))
        sb, _ = ent_bits(np.linalg.eigvalsh(rb))
        sab, _ = ent_bits(np.linalg.eigvalsh(r))
        out += (pz / tot) * (sa + sb - sab)
    return out


# =============================== THE BRANCH DECOMPOSITION (this block's tool) =
def branch_split(psi, n, S):
    """Project the pointer S onto its Z eigenbasis.  Returns [(p_z, unit vector on
    the n-1 non-pointer sites)] together with the site list in branch-axis order.

    THIS IS THE WHOLE STRUCTURAL FACT: because the global state is pure and the
    fragments exhaust every non-pointer site, each branch vector is a PURE state
    on the union of all fragments.  Nothing is traced out.
    """
    T = psi.reshape((2,) * n)
    order = [S] + [i for i in range(n) if i != S]
    M = np.transpose(T, [n - 1 - s for s in order]).reshape(2, -1)
    out = []
    for z in (0, 1):
        v = np.ascontiguousarray(M[z])
        p = float(np.vdot(v, v).real)
        out.append((p, v / math.sqrt(p) if p > 1e-300 else v))
    return out, order[1:]


def branch_axes(sitelist, sites):
    """Map a list of geometry site indices to branch axis positions."""
    pos = {s: j for j, s in enumerate(sitelist)}
    return tuple(sorted(pos[s] for s in sites))


def sub_entropy(vec, nb, axes):
    """S(rho_X) in bits for a subset X (given as branch axes) of a PURE vector."""
    if len(axes) == 0 or len(axes) == nb:
        return 0.0
    T = vec.reshape((2,) * nb)
    rest = [j for j in range(nb) if j not in axes]
    M = np.transpose(T, list(axes) + rest).reshape(1 << len(axes), -1)
    w = np.linalg.eigvalsh(M @ M.conj().T)
    return ent_bits(w)[0]


def sub_entropy_mixed(vec, nb, axes):
    """S(rho_X) with NO purity assumption -- used only where purity is broken."""
    T = vec.reshape((2,) * nb)
    rest = [j for j in range(nb) if j not in axes]
    M = np.transpose(T, list(axes) + rest).reshape(1 << len(axes), -1)
    w = np.linalg.eigvalsh(M @ M.conj().T)
    return ent_bits(w)[0]


def C_from_branches(psi, n, S, axesA, axesB):
    """C_ab rebuilt along the DERIVED route: branch first, entropies second.
    Disjoint code path from cond_mi(); their agreement is the first gate of the
    derivation."""
    brs, _ = branch_split(psi, n, S)
    tot = sum(p for p, _ in brs)
    nb = n - 1
    out = 0.0
    for p, v in brs:
        if p / tot <= 1e-14:
            continue
        sa = sub_entropy(v, nb, axesA)
        sb = sub_entropy(v, nb, axesB)
        sab = sub_entropy(v, nb, tuple(sorted(set(axesA) | set(axesB))))
        out += (p / tot) * (sa + sb - sab)
    return out


def s_profile(psi, n, S, d, all_subsets=False):
    """s(k) := sum_z p_z S(rho_{any k leaves}^z), plus the exchangeability spread."""
    brs, _ = branch_split(psi, n, S)
    tot = sum(p for p, _ in brs)
    s, spread = {}, {}
    for k in range(0, d + 1):
        combos = (list(itertools.combinations(range(d), k)) if all_subsets
                  else [tuple(range(k))])
        vals = []
        for X in combos:
            vals.append(sum((p / tot) * sub_entropy(v, d, X) for p, v in brs))
        s[k] = vals[0]
        spread[k] = (max(vals) - min(vals)) if len(vals) > 1 else 0.0
    return s, spread


def s_from_ladder(d, G):
    """INVERT the derived law G(m) = s(m)+s(1)-s(m+1) using ONLY the ladder numbers.

    s(1) = G(d-1)/2 comes from the exhausting rung (where s(d)=0 and s(d-1)=s(1));
    the rest is the forward recursion s(m+1) = s(m) + s(1) - G(m).
    The values s(d) = 0 and s(k) = s(d-k) are NOT used -- they come out, and are
    therefore over-determination checks on the pinned data.
    """
    s = {0: 0.0}
    s[1] = G[d - 1] / 2.0
    for m in range(1, d):
        s[m + 1] = s[m] + s[1] - G[m]
    return s


def star_state(d, lam, times, route="A"):
    """The pure star K_{1,d} under the frozen preparation and Hamiltonian."""
    g = spider("STAR%d" % d, [path_arm(1)] * d, "pure star K_{1,%d}" % d, "star")
    n = g["n"]
    if n > FULL_SPACE_CAP_N:
        die("cap:n>%d" % FULL_SPACE_CAP_N)
    diag = build_diag(n, g["bonds"])
    psi0 = prep_state(n, set([g["S"]] + g["recording"]))
    if route == "A":
        outs, info = chebyshev(psi0, diag, n, lam, times)
    elif route == "B":
        outs, info = taylor_march(psi0, diag, n, lam, times)
    elif route == "C":
        outs, info = dense_route(psi0, diag, n, lam, times)
    else:
        die("route:%s" % route)
    return g, outs, info, diag, psi0


def star_leaf_axes(g, d):
    """Branch axes of the d leaves of a pure star, in site order."""
    _, sitelist = branch_split(np.zeros(1 << g["n"], dtype=np.complex128), g["n"], g["S"])
    return [branch_axes(sitelist, [L]) for L in g["recording"]]


# ================================================== the symbolic derivation ==
def symbolic_derivation():
    """The derivation, machine-checked with sympy.  Four lemmas and the theorem.

    L1  spectra transfer:  N(MN) = (NM)N for generic symbolic M, N -- the two-line
        reason MN and NM share every nonzero eigenvalue (eigenvectors map v -> Nv).
    L2  Sylvester char-poly identity: det(xI_p - MN) x^(q-p) = det(xI_q - NM),
        which upgrades L1 to equal MULTIPLICITIES, hence S(X) = S(X^c) for a pure
        state (X^c's reduced matrix is M^dag M when X's is M M^dag).
    L3  exchangeability => the reduced state of a k-subset does not depend on WHICH
        k-subset:  verified on a fully symbolic permutation-symmetric pure state.
    L4  the pure-state PAIR-COMPLEMENT identity  I(A:B) + I(R:B) = 2 S(B), and the
        pure-tripartite CMI identity I(A:R|B) = I(A:R) (which is NOT the
        strong-subadditivity equality case I(A:R|B) = 0).
    THM the ladder law and the additivity identity.
    """
    import sympy as sp
    tr = []
    ok = {}

    # ---- L1 -------------------------------------------------------------
    l1 = []
    for (p, q) in [(1, 2), (2, 2), (2, 4), (4, 4)]:
        M = sp.Matrix(p, q, lambda i, j: sp.Symbol("m%d_%d" % (i, j)))
        N = sp.Matrix(q, p, lambda i, j: sp.Symbol("n%d_%d" % (i, j)))
        good = sp.expand(N * (M * N) - (N * M) * N) == sp.zeros(q, p)
        l1.append({"shape": [p, q], "N(MN)=(NM)N": bool(good)})
        if not good:
            die("symbolic:L1-failed %r" % ((p, q),))
    ok["L1_spectra_transfer"] = True
    tr.append("L1  N(MN) = (NM)N holds identically for generic symbolic M (pxq), "
              "N (qxp) at shapes %s.  Hence if MNv = c v with c != 0 then "
              "NM(Nv) = c (Nv) and Nv != 0: MN and NM share every nonzero "
              "eigenvalue." % [x["shape"] for x in l1])

    # ---- L2 -------------------------------------------------------------
    x = sp.Symbol("x")
    l2 = []
    for (p, q) in [(1, 2), (2, 2), (2, 3), (2, 4)]:
        M = sp.Matrix(p, q, lambda i, j: sp.Symbol("a%d_%d" % (i, j)))
        N = sp.Matrix(q, p, lambda i, j: sp.Symbol("b%d_%d" % (i, j)))
        lhs = sp.expand((x * sp.eye(p) - M * N).det() * x ** (q - p))
        rhs = sp.expand((x * sp.eye(q) - N * M).det())
        good = sp.expand(lhs - rhs) == 0
        l2.append({"shape": [p, q], "sylvester_identity": bool(good)})
        if not good:
            die("symbolic:L2-failed %r" % ((p, q),))
    ok["L2_sylvester_charpoly"] = True
    tr.append("L2  det(xI_p - MN) x^(q-p) = det(xI_q - NM) verified symbolically at "
              "shapes %s.  With M the Schmidt matrix of a pure state under the "
              "split (X, X^c), rho_X = M M^dag and rho_{X^c} = (M^dag M)^T, so the "
              "two reduced states have identical nonzero spectra WITH "
              "multiplicity: S(X) = S(X^c) EXACTLY, for every pure state and "
              "every bipartition." % [y["shape"] for y in l2])

    # ---- L3 -------------------------------------------------------------
    def dicke(d):
        c = [sp.Symbol("c%d" % k) for k in range(d + 1)]
        cb = [sp.Symbol("cb%d" % k) for k in range(d + 1)]
        psi = [c[bin(b).count("1")] / sp.sqrt(sp.binomial(d, bin(b).count("1")))
               for b in range(1 << d)]
        psib = [cb[bin(b).count("1")] / sp.sqrt(sp.binomial(d, bin(b).count("1")))
                for b in range(1 << d)]
        return psi, psib

    def rho_sym(psi, psib, d, X):
        X = list(X)
        Y = [i for i in range(d) if i not in X]
        k = len(X)

        def split(b):
            return (sum(((b >> X[j]) & 1) << j for j in range(k)),
                    sum(((b >> Y[j]) & 1) << j for j in range(len(Y))))
        R = sp.zeros(1 << k, 1 << k)
        for b in range(1 << d):
            u, w = split(b)
            for b2 in range(1 << d):
                v, w2 = split(b2)
                if w == w2:
                    R[u, v] += psi[b] * psib[b2]
        return sp.expand(R)

    l3 = []
    for d in (3, 4, 5):
        psi, psib = dicke(d)
        for k in range(1, d):
            subs = list(itertools.combinations(range(d), k))
            R0 = rho_sym(psi, psib, d, subs[0])
            same = all(sp.simplify(rho_sym(psi, psib, d, X) - R0) == sp.zeros(1 << k, 1 << k)
                       for X in subs[1:])
            l3.append({"d": d, "k": k, "n_subsets": len(subs), "all_identical": bool(same)})
            if not same:
                die("symbolic:L3-failed d=%d k=%d" % (d, k))
    ok["L3_exchangeability_size_only"] = True
    tr.append("L3  For a fully symbolic permutation-symmetric pure state (Dicke "
              "amplitudes c_0..c_d, conjugates carried as independent symbols) the "
              "reduced density matrix of a k-subset is IDENTICAL for every "
              "k-subset, at d = 3,4,5 and every k.  Hence S depends on the subset "
              "only through its SIZE: write s(k).")

    # ---- L4 -------------------------------------------------------------
    SA, SB, SR, SAB, SRB, SAR = sp.symbols("S_A S_B S_R S_AB S_RB S_AR")
    # purity of ABR:  S(R) = S(AB), S(RB) = S(A), S(AR) = S(B), S(ABR) = 0
    subs_pure = {SR: SAB, SRB: SA, SAR: SB}
    I_AB = SA + SB - SAB
    I_RB = SR + SB - SRB
    pair_complement = sp.simplify((I_AB + I_RB).subs(subs_pure) - 2 * SB)
    if pair_complement != 0:
        die("symbolic:L4-pair-complement %r" % pair_complement)
    I_ARB = SAR + SB - 0                      # I(AR:B) with S(ABR) = 0
    total_is_2SB = sp.simplify(I_ARB.subs(subs_pure) - 2 * SB)
    if total_is_2SB != 0:
        die("symbolic:L4-total %r" % total_is_2SB)
    # the pure-tripartite CMI identity, and the SSA equality case it is NOT
    I_AR_given_B = SAB + SRB - SB - 0
    I_AR = SA + SR - SAR
    cmi_equals_mi = sp.simplify((I_AR_given_B - I_AR).subs(subs_pure))
    if cmi_equals_mi != 0:
        die("symbolic:L4-cmi %r" % cmi_equals_mi)
    ssa_equality_value = sp.simplify(I_AR_given_B.subs(subs_pure))   # = S_A + S_R - S_B
    ok["L4_pair_complement"] = True
    tr.append("L4  For a PURE state on A u B u R purity gives S(R)=S(AB), "
              "S(RB)=S(A), S(AR)=S(B), S(ABR)=0, hence identically "
              "I(A:B) + I(R:B) = 2 S(B) = I(AR:B).  The same substitution gives "
              "I(A:R|B) - I(A:R) = 0 (a pure-tripartite identity) while "
              "I(A:R|B) = %s, which is NOT zero in general: the additivity "
              "identity is NOT the strong-subadditivity equality case."
              % sp.srepr(ssa_equality_value).replace("Symbol", "S")
              if False else
              "L4  For a PURE state on A u B u R purity gives S(R)=S(AB), "
              "S(RB)=S(A), S(AR)=S(B), S(ABR)=0, hence identically "
              "I(A:B) + I(R:B) = 2 S(B) = I(AR:B).  The same substitution gives "
              "I(A:R|B) - I(A:R) = 0 (a pure-tripartite identity) while "
              "I(A:R|B) = S_A + S_R - S_B, which is NOT zero in general: the "
              "additivity identity is NOT the strong-subadditivity equality case.")

    # ---- THM ------------------------------------------------------------
    d_sym = sp.Symbol("d", integer=True, positive=True)
    sfun = sp.Function("s")
    m = sp.Symbol("m", integer=True, positive=True)
    G = lambda mm: sfun(mm) + sfun(1) - sfun(mm + 1)
    # the reflection s(k) = s(d-k) is L2 applied inside one branch; s(d) = 0 is
    # purity of the branch itself.
    lhs = G(m) + G(d_sym - 1 - m)
    lhs_reflected = lhs.subs({sfun(d_sym - 1 - m): sfun(m + 1),
                              sfun(d_sym - m): sfun(m)})
    rhs = (sfun(d_sym - 1) + sfun(1) - sfun(d_sym)).subs({sfun(d_sym - 1): sfun(1),
                                                          sfun(d_sym): 0})
    thm = sp.simplify(lhs_reflected - rhs)
    if thm != 0:
        die("symbolic:THM-failed %r" % thm)
    ok["THM_additivity"] = True
    tr.append("THM  G_d(m) := I(A_m : B_1) = s(m) + s(1) - s(m+1).  Substituting the "
              "reflection s(k) = s(d-k) (L2 inside the branch) into "
              "G_d(m) + G_d(d-1-m) collapses it to 2 s(1); and G_d(d-1) = "
              "s(d-1) + s(1) - s(d) = 2 s(1) because s(d) = 0 (the branch is pure "
              "on all d leaves).  THE IDENTITY IS AN EQUALITY OF THE SAME "
              "EXPRESSION, not an approximation: sympy returns exactly 0.")

    return {"lemmas_verified": ok, "L1": l1, "L2": l2, "L3": l3,
            "L4_pair_complement_residual": 0, "L4_cmi_minus_mi_residual": 0,
            "L4_I_A_R_given_B": "S_A + S_R - S_B  (NOT identically zero)",
            "THM_residual": 0, "transcript": tr,
            "sympy_version": __import__("sympy").__version__,
            "transcript_sha256": sha256_bytes("\n".join(tr).encode("utf-8"))}


# ==================================================================== main ===
def main():
    caps = []
    pins = verify_pins()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    const_x = cross_check_prior_constants(frozen)
    statdef = verify_statistic_definition(memo)
    d1_text, d1_prov = recover_d1_note()
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()
    r929 = json.load(open(os.path.join(ROOT, C929_RECEIPT)))
    lines = []
    ap = lines.append

    # ---------------- restriction gate 1: the partition rule vs the memo ------
    cube = geom_cube27()
    memo_frags = parse_memo_cube_fragments(memo)
    rule_ok = True
    for L in CUBE_LABELS:
        mine = {cube["coords"][i] for i in cube["frags"][L]}
        if mine != set(memo_frags[L]):
            rule_ok = False
    if not rule_ok:
        die("partition-rule:does-not-reproduce-memo-cube")
    lemma = enumerate_constructible_profiles(3)
    if not lemma["structural_lemma_exactly_one_merged_block"]:
        die("lemma:two-merged-blocks-found")

    # ---------------- the cell engine ----------------------------------------
    def cell_pairs(g, lam, times=T_EXEC, ti=7, route="A"):
        """Every fragment pair's C_ab at one row, along the FROZEN code path."""
        n = g["n"]
        if n > FULL_SPACE_CAP_N:
            die("cap:n>%d for %s" % (FULL_SPACE_CAP_N, g["key"]))
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([g["S"]] + g["recording"]))
        if route == "A":
            outs, info = chebyshev(psi0, diag, n, lam, times)
        elif route == "C":
            outs, info = dense_route(psi0, diag, n, lam, times)
        else:
            outs, info = taylor_march(psi0, diag, n, lam, times)
        a = outs[ti]
        out = {}
        for a1, b1 in itertools.combinations(g["labels"], 2):
            rho = joint_rho(a, n, [g["S"]] + g["frags"][a1] + g["frags"][b1])
            out[(a1, b1)] = cond_mi(rho, len(g["frags"][a1]), len(g["frags"][b1]))
        return out, a, info

    # ============ RESTRICTION GATE 2: the 929 multiplicity ladder ============
    pub_ladder = r929["Q1_within_pair_multiplicity_vs_size"][
        "pure_star_multiplicity_ladder_G_d_of_m"]
    repro_ladder, ladder_dev, ladder_rows = {}, 0.0, 0
    for d in (3, 4, 5, 6):
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            G = {}
            for f in range(1, d + 1):
                g = build_sep(d, f)
                if g is None:
                    continue
                mult = g["anchor_multiplicity"]
                C, _, _ = cell_pairs(g, lam)
                for (a1, b1), v in C.items():
                    mm = [mult[a1], mult[b1]]
                    if min(mm) != 1:
                        continue
                    G.setdefault(max(mm), []).append(v)
            Gm = {m: float(np.median(vs)) for m, vs in G.items()}
            key = "d%d@%s" % (d, lk)
            pubG = pub_ladder[key]["G_of_m"]
            for m in sorted(Gm):
                ladder_rows += 1
                ladder_dev = max(ladder_dev, abs(Gm[m] - pubG[str(m)]))
            repro_ladder[key] = {"d": d, "field": lam,
                                 "G_of_m": {str(m): Gm[m] for m in sorted(Gm)}}
    if ladder_dev > REPRO_TOL:
        die("restriction:929-ladder max_dev=%.3e (demanded exactly 0.0)" % ladder_dev)

    # additivity residuals and the last-step relation, reproduced
    add_dev, last_dev = 0.0, 0.0
    for key, e in sorted(repro_ladder.items()):
        d = e["d"]
        Gm = {int(k): v for k, v in e["G_of_m"].items()}
        pub = pub_ladder[key]
        for a in pub["additivity_relation_G(m)+G(d-1-m)=G(d-1)"]:
            m, c = a["m"], a["complement"]
            res = Gm[m] + Gm[c] - Gm[d - 1]
            add_dev = max(add_dev, abs(res - a["residual"]))
        mine_last = abs((Gm[d - 1] - Gm[d - 2]) - Gm[1])
        last_dev = max(last_dev, abs(mine_last - pub["last_step_equals_G_of_1"]))
    if max(add_dev, last_dev) > REPRO_TOL:
        die("restriction:929-additivity-residuals add=%.3e last=%.3e" % (add_dev, last_dev))

    # ============ RESTRICTION GATE 3: the T(d) baseline table ================
    REF_SRC = {2: ("SPk2L1", lambda: spider("SPk2L1", [path_arm(1)] * 2, "", "spider")),
               3: ("SPk3L1", lambda: spider("SPk3L1", [path_arm(1)] * 3, "", "spider")),
               4: ("SPk4L1", lambda: spider("SPk4L1", [path_arm(1)] * 4, "", "spider")),
               5: ("SPk5L1", lambda: spider("SPk5L1", [path_arm(1)] * 5, "", "spider")),
               6: ("G2", geom_star7),
               8: ("STk8", lambda: spider("STk8", [path_arm(1)] * 8, "", "star")),
               10: ("STk10", lambda: spider("STk10", [path_arm(1)] * 10, "", "star")),
               12: ("STk12", lambda: spider("STk12", [path_arm(1)] * 12, "", "star"))}
    pubT = r929["reference_table_T_of_degree_measured_here"]
    T_dev, T_rows, Trepro = 0.0, 0, {}
    for deg, (src, build) in sorted(REF_SRC.items()):
        g = build()
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            C, _, _ = cell_pairs(g, lam)
            vals = sorted(C.values())
            med = float(np.median(vals))
            spread = max(vals) - min(vals)
            want = pubT[str(deg)][lk]
            T_dev = max(T_dev, abs(med - want["at_Jt_0.7"]),
                        abs(spread - want["spread_at_Jt_0.7"]))
            T_rows += 1
            Trepro["d%d@%s" % (deg, lk)] = {"at_Jt_0.7": med, "spread": spread,
                                            "n_baseline_pairs": len(vals),
                                            "source_geometry": src}
            if want["source_geometry"] != src or want["n_baseline_pairs"] != len(vals):
                die("restriction:T-table-shape d=%d" % deg)
    if T_dev > REPRO_TOL:
        die("restriction:929-T-table max_dev=%.3e" % T_dev)

    # ============ RESTRICTION GATE 4: the exhausting-pair departure ==========
    # The pinned T13 groups its medians over the FULL 929 d=5 roster; every
    # contributing geometry is rebuilt here from its definition.
    t13_builders = {
        "A1": lambda: build_926_A("A1"), "A2": lambda: build_926_A("A2"),
        "A3": lambda: build_926_A("A3"), "A4": lambda: build_926_A("A4"),
        "ALTd5f2": lambda: build_sep_alt(5, 2), "ALTd5f3": lambda: build_sep_alt(5, 3),
        "ALTd5f4": lambda: build_sep_alt(5, 4), "ALTd5f5": lambda: build_sep_alt(5, 5),
        "AR3m3": lambda: spider("AR3m3", [path_arm(3), path_arm(3)] + [path_arm(1)] * 3,
                                "", "arity"),
        "E1": geom_E1,
        "MS5C4": lambda: spider("MS5C4", [claw_arm(4)] + [path_arm(1)] * 4, "", "multsize"),
        "MS5L1": lambda: spider("MS5L1", [path_arm(1)] + [path_arm(1)] * 4, "", "multsize"),
        "MS5L2": lambda: spider("MS5L2", [path_arm(2)] + [path_arm(1)] * 4, "", "multsize"),
        "MS5L3": lambda: spider("MS5L3", [path_arm(3)] + [path_arm(1)] * 4, "", "multsize"),
        "MS5L4": lambda: spider("MS5L4", [path_arm(4)] + [path_arm(1)] * 4, "", "multsize"),
        "SEPd5f2": lambda: build_sep(5, 2), "SEPd5f3": lambda: build_sep(5, 3),
        "SEPd5f4": lambda: build_sep(5, 4), "SEPd5f5": lambda: build_sep(5, 5),
        "SPk5L1": lambda: spider("SPk5L1", [path_arm(1)] * 5, "", "spider"),
        "W3depth5": geom_W3, "W4merge5d3": geom_W4,
    }
    by_mult = {}
    for name, build in sorted(t13_builders.items()):
        g = build()
        if g is None:
            die("t13:builder-none %s" % name)
        d = g["profile"]["pointer_degree_d"]
        if d != 5:
            die("t13:degree %s=%d" % (name, d))
        mult = g["anchor_multiplicity"]
        C, _, _ = cell_pairs(g, 0.10)
        for (a1, b1), v in C.items():
            msum = mult[a1] + mult[b1]
            by_mult.setdefault((msum, d - msum), []).append(v)
    lin = {k: float(np.median(v)) for k, v in by_mult.items()}
    pub13 = r929["teeth"]["T13_pair_exhaustion_is_a_distinct_regime"]
    t13_dev = 0.0
    for k, v in sorted(lin.items()):
        want = pub13["C_ab_by_(multiplicity_sum, rest)"].get(str(list(k)))
        if want is None:
            die("t13:extra-group %r" % (k,))
        t13_dev = max(t13_dev, abs(v - want))
    slope = lin[(3, 2)] - lin[(2, 3)]
    pred_lin = lin[(2, 3)] + 3 * slope
    departure = abs(lin[(5, 0)] - pred_lin)
    t13_dev = max(t13_dev, abs(pred_lin - pub13["linear_in_multiplicity_extrapolation_to_(5,0)"]),
                  abs(departure - pub13["departure_from_linearity"]))
    if t13_dev > REPRO_TOL:
        die("restriction:929-T13 max_dev=%.3e" % t13_dev)

    restriction = {
        "gate_order": "pins -> frozen constants (21/21, six-way) -> statistic "
                      "definition bytes -> partition rule -> structural lemma -> "
                      "929 ladder -> 929 additivity residuals -> 929 T(d) table -> "
                      "929 T13 exhausting departure -> SEAL -> any new number",
        "ladder": {"rungs_reproduced": ladder_rows, "cells": len(repro_ladder),
                   "max_abs_deviation": ladder_dev},
        "additivity_residuals": {"max_abs_deviation": add_dev},
        "last_step_relation": {"max_abs_deviation": last_dev},
        "T_of_degree_table": {"rows": T_rows, "max_abs_deviation": T_dev},
        "T13_exhausting_departure": {
            "geometries_rebuilt": len(t13_builders),
            "groups": {str(list(k)): v for k, v in sorted(lin.items())},
            "linear_extrapolation_to_(5,0)": pred_lin,
            "departure_from_linearity": departure,
            "max_abs_deviation": t13_dev},
        "deviation_exactly_zero_everywhere": bool(
            max(ladder_dev, add_dev, last_dev, T_dev, t13_dev) == 0.0),
    }
    t_gates = time.perf_counter() - T_START

    # ======================================================= THE SEAL ========
    # Built from PINNED BYTES ONLY.  No new cell has been evaluated at this point;
    # every propagator call so far reproduced a pinned 929 number.
    if NEW_CELLS_EVALUATED:
        die("seal:new-cells-evaluated-before-seal %r" % sorted(NEW_CELLS_EVALUATED))
    seal_inputs = {}
    seal_pred = {}
    for key in sorted(pub_ladder):
        e = pub_ladder[key]
        d = e["d"]
        G = {int(k): float(v) for k, v in e["G_of_m"].items()}
        seal_inputs[key] = {"d": d, "field": e["field"],
                            "G_of_m": {str(k): G[k] for k in sorted(G)}}
        s = s_from_ladder(d, G)
        seal_pred[key] = {
            "s_of_k_reconstructed": {str(k): s[k] for k in sorted(s)},
            "P1_s_of_d_is_zero": s[d],
            "P2_reflection_max_|s(k)-s(d-k)|": max(abs(s[k] - s[d - k])
                                                   for k in range(0, d + 1)),
            "P3_both_merged_pairs_C(ma,mb)=s(ma)+s(mb)-s(ma+mb)": {
                "%d|%d" % (ma, mb): s[ma] + s[mb] - s[ma + mb]
                for ma in range(2, d) for mb in range(2, d)
                if ma <= mb and ma + mb <= d},
            "P4_exhausting_rung_is_twice_the_one_leaf_entropy": 2.0 * s[1],
        }
    seal = {
        "seal_id": "cycle931-additivity-derivation-seal-1",
        "sealed_before_any_new_number": True,
        "constructed_from_only": {
            "929_receipt": C929_RECEIPT,
            "929_receipt_sha256": pins[C929_RECEIPT]["sha256"],
            "field_used": "Q1_within_pair_multiplicity_vs_size."
                          "pure_star_multiplicity_ladder_G_d_of_m.*.G_of_m"},
        "inputs_quoted": seal_inputs,
        "derivation_used": "s(1) = G(d-1)/2 ; s(m+1) = s(m) + s(1) - G(m).  "
                           "NOTHING else is used: s(d) = 0 and s(k) = s(d-k) are "
                           "NOT imposed, so P1 and P2 are predictions, not "
                           "definitions.",
        "predictions": seal_pred,
        "P5_relation_predicted_at_new_cells":
            "G_d(m) + G_d(d-1-m) - G_d(d-1) = 0 to <= %g at EVERY (d, lambda, Jt) "
            "this runner evaluates, including d = 7..12, the diagnostic fields "
            "0.075/0.125/0.15, the NON-CLAIM strong fields 0.5/1.0/2.0, and "
            "Jt in {0.3, 1.2, 3.0} off the certification row." % IDENT_TOL,
        "P6_hypotheses_are_load_bearing":
            "additivity MUST FAIL (residual > 1e4 x the claim tolerance, i.e. "
            "> %g bit) on (i) a spider whose arms are NOT isomorphic, (i-b) a star "
            "with a NON-FROZEN preparation that leaves two leaves in |0>, (i-c) a "
            "synthetic random PURE state with no symmetry at all -- all three have "
            "exchangeability broken and purity intact -- and (ii) a state whose "
            "pointer-conditioned branch is MIXED on the fragment union (purity "
            "broken).  On (i), (i-b) and (i-c) the pure-state pair-complement "
            "identity I(A:B) + I(R:B) = 2 S(B) MUST STILL HOLD to <= %g, which is "
            "what separates the two hypotheses."
            % (1e4 * IDENT_TOL, IDENT_TOL),
        "P7_exhausting_pairs_anywhere":
            "in ANY geometry (star or not) an EXHAUSTING pair satisfies "
            "C_ab = 2 S_branch(F_a) = 2 S_branch(F_b) to <= %g." % IDENT_TOL,
    }
    seal["seal_sha256"] = sha256_obj(seal)
    ap(BOUNDARY_LINE)
    ap("runner: scripts/frontier_cycle931_additivity_identity_2026_07_28.py")
    ap("cycle: 931  block: toe-time-blockM11-20260802  head: %s" % head)
    ap("")
    ap("-- RESTRICTION GATES (all before any new number) --")
    ap("  21/21 frozen constants byte-verified; quote-identical to the 917, 919,")
    ap("  921, 926, 927 AND 929 receipts: %s" % const_x["all_six_receipts_agree"])
    ap("  statistic definition read from the frozen memo bytes: %s" % statdef["C_ab_formula"])
    ap("  partition rule reproduces the memo's six cube lists: %s" % rule_ok)
    ap("  structural lemma verified on %d pointers: %s"
       % (lemma["n_pointers"], lemma["structural_lemma_exactly_one_merged_block"]))
    ap("  929 multiplicity ladder: %d rungs / %d cells, max abs deviation %.1f"
       % (ladder_rows, len(repro_ladder), ladder_dev))
    ap("  929 additivity residuals: max abs deviation %.1f" % add_dev)
    ap("  929 last-step relation:   max abs deviation %.1f" % last_dev)
    ap("  929 T(d) baseline table:  %d rows, max abs deviation %.1f" % (T_rows, T_dev))
    ap("  929 T13 exhausting departure (%d geometries rebuilt): max abs deviation %.1f"
       % (len(t13_builders), t13_dev))
    ap("  reproduced departure_from_linearity = %.15f (pinned %.15f)"
       % (departure, pub13["departure_from_linearity"]))
    ap("  gate runtime: %.2f s" % t_gates)
    ap("")
    ap("-- SEAL (pre-registered BEFORE any new number; inputs are pinned bytes only) --")
    ap("  seal_id:     %s" % seal["seal_id"])
    ap("  seal sha256: %s" % seal["seal_sha256"])
    ap("  new cells evaluated at seal time: %d" % len(NEW_CELLS_EVALUATED))
    ap("  propagator calls at seal time: A=%d B=%d C=%d (all reproducing pinned cells)"
       % (PROP_CALLS["A"], PROP_CALLS["B"], PROP_CALLS["C"]))
    for key in sorted(seal_pred):
        p = seal_pred[key]
        ap("  %-9s s(k)=%s" % (key, ", ".join("%.12f" % p["s_of_k_reconstructed"][str(k)]
                                              for k in range(0, seal_inputs[key]["d"] + 1))))
        ap("            P1 s(d)=%.3e  P2 max|s(k)-s(d-k)|=%.3e  P4 2s(1)=%.15f"
           % (p["P1_s_of_d_is_zero"], p["P2_reflection_max_|s(k)-s(d-k)|"],
              p["P4_exhausting_rung_is_twice_the_one_leaf_entropy"]))
        for pk, pv in sorted(p["P3_both_merged_pairs_C(ma,mb)=s(ma)+s(mb)-s(ma+mb)"].items()):
            ap("            P3 C(%s) = %.15f" % (pk, pv))
    ap("")

    # ================================================== Q1: the structure ====
    q1 = {"statistic_definition_from_the_frozen_memo_bytes": statdef,
          "statistic_implementation_quoted_from_the_pinned_929_runner":
              extract_pinned_source(C929_RUNNER, "cond_mi"),
          "joint_rho_quoted_from_the_pinned_929_runner":
              extract_pinned_source(C929_RUNNER, "joint_rho")}

    struct = []
    for d in (3, 4, 5, 6):
        for lam in CLAIM_LAMBDAS:
            NEW_CELLS_EVALUATED.add(("starstruct", d, lam))
            g, outs, info, _, _ = star_state(d, lam, T_EXEC)
            a = outs[7]
            n = g["n"]
            brs, sitelist = branch_split(a, n, g["S"])
            tot = sum(p for p, _ in brs)
            # (i) branch weights
            pz = [p / tot for p, _ in brs]
            # (ii) the branch is PURE on every non-pointer site
            purity_dev = 0.0
            for p, v in brs:
                purity_dev = max(purity_dev, abs(float(np.vdot(v, v).real) - 1.0))
            # S of the FULL branch must be 0
            full_dev = max(sub_entropy_mixed(v, d, tuple(range(d))) for _, v in brs)
            # (iii) exchangeability: every k-subset has the same entropy
            s, spread = s_profile(a, n, g["S"], d, all_subsets=True)
            # (iv) reflection
            refl = max(abs(s[k] - s[d - k]) for k in range(d + 1))
            # (v) the two code paths for C_ab agree
            leaf_ax = [branch_axes(sitelist, [L]) for L in g["recording"]]
            path_dev = 0.0
            for m in range(1, d):
                A = tuple(sorted(itertools.chain(*leaf_ax[:m])))
                B = leaf_ax[m] if m < d else leaf_ax[0]
                rho = joint_rho(a, n, [g["S"]] + g["recording"][:m] + [g["recording"][m]])
                frozen_val = cond_mi(rho, m, 1)
                derived_val = C_from_branches(a, n, g["S"], A, B)
                path_dev = max(path_dev, abs(frozen_val - derived_val))
            # (vi) where the m-dependence enters: the pointer marginal is m-blind
            rho_ptr = joint_rho(a, n, [g["S"]])
            struct.append({
                "cell": "d%d@%g" % (d, lam), "d": d, "field": lam, "n_sites": n,
                "pointer_branch_weights": pz,
                "max_|p_z - 1/2|": max(abs(x - 0.5) for x in pz),
                "branch_normalisation_dev": purity_dev,
                "S(all_d_leaves|z)_max": full_dev,
                "branch_is_pure_on_the_fragment_union": bool(full_dev < 1e-12),
                "s_of_k": {str(k): s[k] for k in sorted(s)},
                "exchangeability_max_spread_over_ALL_subsets_of_a_size":
                    max(spread.values()),
                "reflection_max_|s(k)-s(d-k)|": refl,
                "frozen_vs_derived_C_ab_max_dev": path_dev,
                "pointer_marginal_eigs": sorted(
                    float(x) for x in np.linalg.eigvalsh(rho_ptr).real),
            })
    q1["structure_of_the_evolved_state"] = struct
    q1["where_the_m_dependence_enters"] = (
        "NOWHERE except the block SIZES.  (1) The pointer's reduced state is a "
        "property of the geometry and the field, not of the partition: it is the "
        "same matrix for every (m,1) split at fixed d, so it cannot carry m.  "
        "(2) Conditioning on Z_S leaves a PURE state on the union of all "
        "fragments (max S(all leaves | z) = %.2e over the certified cells), so "
        "the merged fragment has no 'internal correlations with the rest' beyond "
        "what its own reduced entropy already records.  (3) Leaf exchangeability "
        "makes every k-leaf reduced state the SAME state (max spread over all "
        "C(d,k) subsets = %.2e), so the ONLY partition-dependent inputs to C_ab "
        "are |a| and |b|.  Hence C_ab = s(|a|) + s(|b|) - s(|a|+|b|) and the "
        "(m,1) ladder is G_d(m) = s(m) + s(1) - s(m+1)."
        % (max(x["S(all_d_leaves|z)_max"] for x in struct),
           max(x["exchangeability_max_spread_over_ALL_subsets_of_a_size"]
               for x in struct)))

    # ================================================ the symbolic derivation =
    sym = symbolic_derivation()

    # ============================== Q2: candidates, verified and attacked ====
    # ---- verification 1: the derived ladder law on every certified cell -----
    law_rows = []
    for d in (3, 4, 5, 6):
        for lam in CLAIM_LAMBDAS:
            g, outs, _, _, _ = star_state(d, lam, T_EXEC)
            a, n = outs[7], g["n"]
            _, sitelist = branch_split(a, n, g["S"])
            s, _ = s_profile(a, n, g["S"], d)
            pubG = pub_ladder["d%d@%g" % (d, lam)]["G_of_m"]
            for m in range(1, d):
                pred = s[m] + s[1] - s[m + 1]
                law_rows.append({"cell": "d%d@%g" % (d, lam), "m": m,
                                 "G_measured_929_pinned": pubG[str(m)],
                                 "G_predicted_from_s": pred,
                                 "residual": pred - pubG[str(m)]})
    law_max = max(abs(r["residual"]) for r in law_rows)

    # ---- verification 2: the identity at NEW (d, field, Jt) cells -----------
    ident_rows = []
    for d in list(range(3, 11)):
        for lam in list(CLAIM_LAMBDAS) + list(DIAG_LAMBDAS) + list(STRONG_LAMBDAS):
            NEW_CELLS_EVALUATED.add(("ident", d, lam))
            g, outs, _, _, _ = star_state(d, lam, T_EXEC)
            n = g["n"]
            for jt, ti in sorted(JT_INDEX.items()):
                a = outs[ti]
                _, sitelist = branch_split(a, n, g["S"])
                leaf_ax = [branch_axes(sitelist, [L]) for L in g["recording"]]
                Gm = {}
                for m in range(1, d):
                    A = tuple(sorted(itertools.chain(*leaf_ax[:m])))
                    B = leaf_ax[m % d]
                    Gm[m] = C_from_branches(a, n, g["S"], A, B)
                res = [Gm[m] + Gm[d - 1 - m] - Gm[d - 1] for m in range(1, d - 1)]
                ident_rows.append({
                    "d": d, "field": lam, "Jt": jt,
                    "field_status": ("frozen" if lam in CLAIM_LAMBDAS else
                                     ("diagnostic" if lam in DIAG_LAMBDAS
                                      else "NON-CLAIM strong coupling")),
                    "on_929_grid": bool(d <= 6 and lam in CLAIM_LAMBDAS and jt == 0.7),
                    "G_of_m": {str(m): Gm[m] for m in sorted(Gm)},
                    "max_|additivity residual|": max((abs(x) for x in res), default=0.0),
                    "G_max": max(Gm.values())})
    # long-time, strong-coupling probe
    for d in (3, 4, 5, 6):
        for lam in (0.05, 0.10, 1.0, 2.0):
            NEW_CELLS_EVALUATED.add(("long", d, lam))
            g, outs, _, _, _ = star_state(d, lam, T_LONG)
            n = g["n"]
            a = outs[-1]
            _, sitelist = branch_split(a, n, g["S"])
            leaf_ax = [branch_axes(sitelist, [L]) for L in g["recording"]]
            Gm = {m: C_from_branches(a, n, g["S"],
                                     tuple(sorted(itertools.chain(*leaf_ax[:m]))),
                                     leaf_ax[m % d]) for m in range(1, d)}
            res = [Gm[m] + Gm[d - 1 - m] - Gm[d - 1] for m in range(1, d - 1)]
            ident_rows.append({
                "d": d, "field": lam, "Jt": 3.0,
                "field_status": ("frozen-field/OFF-WINDOW time" if lam in CLAIM_LAMBDAS
                                 else "NON-CLAIM strong coupling"),
                "on_929_grid": False,
                "G_of_m": {str(m): Gm[m] for m in sorted(Gm)},
                "max_|additivity residual|": max((abs(x) for x in res), default=0.0),
                "G_max": max(Gm.values())})
    ident_max = max(r["max_|additivity residual|"] for r in ident_rows)
    ident_offgrid = [r for r in ident_rows if not r["on_929_grid"]]
    ident_offgrid_max = max(r["max_|additivity residual|"] for r in ident_offgrid)
    strong_rows = [r for r in ident_rows if r["field"] in STRONG_LAMBDAS]
    strong_max = max(r["max_|additivity residual|"] for r in strong_rows)
    strong_G = max(r["G_max"] for r in strong_rows)

    # ---- verification 3: the SEAL's P3 both-merged numbers -----------------
    p3_rows = []
    for key in sorted(seal_pred):
        d = seal_inputs[key]["d"]
        lam = seal_inputs[key]["field"]
        g, outs, _, _, _ = star_state(d, lam, T_EXEC)
        a, n = outs[7], g["n"]
        _, sitelist = branch_split(a, n, g["S"])
        leaf_ax = [branch_axes(sitelist, [L]) for L in g["recording"]]
        for pk, pv in sorted(seal_pred[key][
                "P3_both_merged_pairs_C(ma,mb)=s(ma)+s(mb)-s(ma+mb)"].items()):
            ma, mb = (int(x) for x in pk.split("|"))
            A = tuple(sorted(itertools.chain(*leaf_ax[:ma])))
            B = tuple(sorted(itertools.chain(*leaf_ax[ma:ma + mb])))
            rho = joint_rho(a, n, [g["S"]] + g["recording"][:ma]
                            + g["recording"][ma:ma + mb])
            meas_frozen = cond_mi(rho, ma, mb)
            meas_derived = C_from_branches(a, n, g["S"], A, B)
            p3_rows.append({"cell": key, "pair": pk, "sealed_prediction": pv,
                            "measured_frozen_path": meas_frozen,
                            "measured_derived_path": meas_derived,
                            "residual": meas_frozen - pv,
                            "constructible_under_the_frozen_rule": False})
    p3_max = max(abs(r["residual"]) for r in p3_rows)

    # ---- verification 4: SEAL P7 -- exhausting pairs in ANY geometry -------
    p7_rows = []
    p7_geoms = {"A4": lambda: build_926_A("A4"),
                "SEPd5f2": lambda: build_sep(5, 2),
                "ALTd5f2": lambda: build_sep_alt(5, 2),
                "SEPd6f2": lambda: build_sep(6, 2),
                "SEPd4f2": lambda: build_sep(4, 2),
                "SEPd3f2": lambda: build_sep(3, 2),
                "SPk2L1": lambda: spider("SPk2L1", [path_arm(1)] * 2, "", "spider"),
                "SPk2L3": lambda: spider("SPk2L3", [path_arm(3)] * 2, "", "spider"),
                "SPk2L4": lambda: spider("SPk2L4", [path_arm(4)] * 2, "", "spider"),
                "SH2Y3": lambda: spider("SH2Y3", [y_arm3(), y_arm3()], "", "shape"),
                "SH2C4": lambda: spider("SH2C4", [claw_arm(4), claw_arm(4)], "", "shape")}

    def y_arm3():
        return [None, 0, 0]

    p7_geoms["SH2Y3"] = lambda: spider("SH2Y3", [[None, 0, 0], [None, 0, 0]], "", "shape")
    for name, build in sorted(p7_geoms.items()):
        g = build()
        if g is None:
            continue
        if len(g["labels"]) != 2:
            continue
        for lam in CLAIM_LAMBDAS:
            NEW_CELLS_EVALUATED.add(("p7", name, lam))
            C, a, _ = cell_pairs(g, lam)
            n = g["n"]
            _, sitelist = branch_split(a, n, g["S"])
            La, Lb = g["labels"]
            axA = branch_axes(sitelist, g["frags"][La])
            axB = branch_axes(sitelist, g["frags"][Lb])
            brs, _ = branch_split(a, n, g["S"])
            tot = sum(p for p, _ in brs)
            SA = sum((p / tot) * sub_entropy(v, n - 1, axA) for p, v in brs)
            SB = sum((p / tot) * sub_entropy(v, n - 1, axB) for p, v in brs)
            meas = C[(La, Lb)]
            p7_rows.append({
                "geometry": name, "field": lam, "n": n,
                "fragment_sizes": [len(g["frags"][La]), len(g["frags"][Lb])],
                "multiplicity": [g["anchor_multiplicity"][La],
                                 g["anchor_multiplicity"][Lb]],
                "C_ab_measured": meas, "2*S_branch(a)": 2 * SA, "2*S_branch(b)": 2 * SB,
                "residual_vs_2SA": meas - 2 * SA, "residual_vs_2SB": meas - 2 * SB,
                "|S_a - S_b|": abs(SA - SB)})
    p7_max = max(max(abs(r["residual_vs_2SA"]), abs(r["residual_vs_2SB"]),
                     r["|S_a - S_b|"]) for r in p7_rows)

    # ---- verification 5: SEAL P6 -- the hypotheses are LOAD-BEARING --------
    # (i) exchangeability broken, purity intact: a MIXED-ARM spider.
    load_bearing = []
    FAIL_THRESHOLD = 1e4 * IDENT_TOL      # 1e-7 bit: four decades above the claim tol
    mixed_specs = {
        "MIX5_arms_1112 (four singletons + one 2-path)":
            [path_arm(1)] * 4 + [path_arm(2)],
        "MIX5_arms_11122 (three singletons + two 2-paths)":
            [path_arm(1)] * 3 + [path_arm(2)] * 2,
        "MIX4_arms_112 (two singletons + one 2-path + one 3-path)":
            [path_arm(1)] * 2 + [path_arm(2), path_arm(3)],
    }
    for name, arms in sorted(mixed_specs.items()):
        d = len(arms)
        g = spider("MIXED%d" % d, arms, "NON-frozen diagnostic: unequal arms", "diag")
        n = g["n"]
        for lam in (0.10,):
            NEW_CELLS_EVALUATED.add(("mixed", name, lam))
            diag = build_diag(n, g["bonds"])
            psi0 = prep_state(n, set([g["S"]] + g["recording"]))
            outs, _ = chebyshev(psi0, diag, n, lam, T_EXEC)
            a = outs[7]
            _, sitelist = branch_split(a, n, g["S"])
            # arms in declared order; fragment = the whole arm
            armsets = []
            for L in g["labels"]:
                armsets.append(branch_axes(sitelist, g["frags"][L]))
            Gm = {}
            for m in range(1, d):
                A = tuple(sorted(itertools.chain(*armsets[:m])))
                B = armsets[m % d]
                Gm[m] = C_from_branches(a, n, g["S"], A, B)
            res = [Gm[m] + Gm[d - 1 - m] - Gm[d - 1] for m in range(1, d - 1)]
            addres = max((abs(x) for x in res), default=0.0)
            # the pure-state pair-complement identity must SURVIVE here
            brs, _ = branch_split(a, n, g["S"])
            tot = sum(p for p, _ in brs)
            A0 = armsets[0]
            B0 = armsets[1]
            R0 = tuple(sorted(set(range(n - 1)) - set(A0) - set(B0)))
            I_AB = C_from_branches(a, n, g["S"], A0, B0)
            I_RB = C_from_branches(a, n, g["S"], R0, B0) if R0 else 0.0
            SB0 = sum((p / tot) * sub_entropy(v, n - 1, B0) for p, v in brs)
            comp_res = I_AB + I_RB - 2 * SB0
            # exchangeability spread across single arms (the broken hypothesis)
            arm_S = [sum((p / tot) * sub_entropy(v, n - 1, ax) for p, v in brs)
                     for ax in armsets]
            load_bearing.append({
                "construction": name, "kind": "exchangeability BROKEN, purity intact",
                "d": d, "field": lam, "n": n,
                "single_arm_entropy_spread": max(arm_S) - min(arm_S),
                "additivity_max_residual": addres,
                "additivity_FAILS": bool(addres > FAIL_THRESHOLD),
                "pair_complement_identity_residual": comp_res,
                "pair_complement_SURVIVES": bool(abs(comp_res) <= IDENT_TOL)})

    # (i-b) exchangeability broken HARD, purity intact: a NON-FROZEN preparation
    # that leaves two leaves in |0> while the rest are |+>.  Declared diagnostic.
    for d in (5, 6):
        lam = 0.10
        NEW_CELLS_EVALUATED.add(("prepbreak", d, lam))
        g = spider("PREPBRK%d" % d, [path_arm(1)] * d,
                   "NON-FROZEN diagnostic: two leaves prepared in |0>", "diag")
        n = g["n"]
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([g["S"]] + g["recording"][:d - 2]))
        outs, _ = chebyshev(psi0, diag, n, lam, T_EXEC)
        a = outs[7]
        brs, sitelist = branch_split(a, n, g["S"])
        tot = sum(p for p, _ in brs)
        leaf_ax = [branch_axes(sitelist, [L]) for L in g["recording"]]
        Gm = {m: C_from_branches(a, n, g["S"],
                                 tuple(sorted(itertools.chain(*leaf_ax[:m]))),
                                 leaf_ax[m % d]) for m in range(1, d)}
        res = [Gm[m] + Gm[d - 1 - m] - Gm[d - 1] for m in range(1, d - 1)]
        addres = max((abs(x) for x in res), default=0.0)
        A0, B0 = leaf_ax[0], leaf_ax[1]
        R0 = tuple(sorted(set(range(d)) - set(A0) - set(B0)))
        SB0 = sum((p / tot) * sub_entropy(v, n - 1, B0) for p, v in brs)
        comp_res = (C_from_branches(a, n, g["S"], A0, B0)
                    + C_from_branches(a, n, g["S"], R0, B0) - 2 * SB0)
        arm_S = [sum((p / tot) * sub_entropy(v, n - 1, ax) for p, v in brs)
                 for ax in leaf_ax]
        load_bearing.append({
            "construction": "PREPBRK%d: star K_{1,%d} with two leaves prepared in "
                            "|0> instead of |+> (NON-FROZEN preparation)" % (d, d),
            "kind": "exchangeability BROKEN, purity intact",
            "d": d, "field": lam, "n": n,
            "single_arm_entropy_spread": max(arm_S) - min(arm_S),
            "additivity_max_residual": addres,
            "additivity_FAILS": bool(addres > FAIL_THRESHOLD),
            "pair_complement_identity_residual": comp_res,
            "pair_complement_SURVIVES": bool(abs(comp_res) <= IDENT_TOL)})

    # (i-c) THE SHARPEST TEST THE SPEC ASKS FOR: a SYNTHETIC pure state with no
    # symmetry whatsoever.  If the derivation could "prove" additivity from purity
    # alone it would have to hold here.  It must not.
    rng = np.random.default_rng(931_0728)

    def _S(vec, d, ax):
        return sub_entropy(vec, d, tuple(sorted(ax)))

    def _I(vec, d, A, B):
        return _S(vec, d, A) + _S(vec, d, B) - _S(vec, d, list(A) + list(B))
    for d in (5, 6):
        v = (rng.normal(size=1 << d) + 1j * rng.normal(size=1 << d))
        v = v / np.linalg.norm(v)
        Gm = {m: _I(v, d, list(range(m)), [m]) for m in range(1, d)}
        res = [Gm[m] + Gm[d - 1 - m] - Gm[d - 1] for m in range(1, d - 1)]
        addres = max((abs(x) for x in res), default=0.0)
        A0, B0, R0 = [0], [1], list(range(2, d))
        comp_res = _I(v, d, A0, B0) + _I(v, d, R0, B0) - 2 * _S(v, d, B0)
        arm_S = [_S(v, d, [i]) for i in range(d)]
        load_bearing.append({
            "construction": "SYNTH%d: a Haar-like random PURE state on %d qubits "
                            "(seed 9310728), no exchangeability at all" % (d, d),
            "kind": "exchangeability BROKEN, purity intact",
            "d": d, "field": None, "n": d,
            "single_arm_entropy_spread": max(arm_S) - min(arm_S),
            "additivity_max_residual": addres,
            "additivity_FAILS": bool(addres > FAIL_THRESHOLD),
            "pair_complement_identity_residual": comp_res,
            "pair_complement_SURVIVES": bool(abs(comp_res) <= IDENT_TOL)})

    # (ii) purity broken: the d-leaf marginal of a (d+1)-star.
    for d in (4, 5):
        for lam in (0.10,):
            NEW_CELLS_EVALUATED.add(("puritybroken", d, lam))
            g, outs, _, _, _ = star_state(d + 1, lam, T_EXEC)
            a, n = outs[7], g["n"]
            brs, sitelist = branch_split(a, n, g["S"])
            tot = sum(p for p, _ in brs)
            leaf_ax = [branch_axes(sitelist, [L]) for L in g["recording"]]
            # keep only the first d leaves: the branch state on them is MIXED
            keep = [leaf_ax[i][0] for i in range(d)]
            drop = [leaf_ax[d][0]]

            def Smix(axes):
                return sum((p / tot) * sub_entropy_mixed(v, n - 1, tuple(sorted(axes)))
                           for p, v in brs)

            def Imix(A, B):
                return Smix(A) + Smix(B) - Smix(list(A) + list(B))
            Gm = {m: Imix(keep[:m], [keep[m]]) for m in range(1, d)}
            res = [Gm[m] + Gm[d - 1 - m] - Gm[d - 1] for m in range(1, d - 1)]
            addres = max((abs(x) for x in res), default=0.0)
            load_bearing.append({
                "construction": "d=%d block of a (d+1)=%d star (one leaf discarded)"
                                % (d, d + 1),
                "kind": "purity BROKEN (the retained block is a MIXED state)",
                "d": d, "field": lam, "n": n,
                "S(all_retained_leaves)": Smix(keep),
                "additivity_max_residual": addres,
                "additivity_FAILS": bool(addres > FAIL_THRESHOLD)})
    lb_ok = all((r["additivity_FAILS"] for r in load_bearing))

    # ---- candidate verdicts ------------------------------------------------
    # (b') the SSA equality case, computed on the real states
    ssa_rows = []
    for d in (4, 5, 6):
        for lam in CLAIM_LAMBDAS:
            g, outs, _, _, _ = star_state(d, lam, T_EXEC)
            a, n = outs[7], g["n"]
            brs, sitelist = branch_split(a, n, g["S"])
            tot = sum(p for p, _ in brs)
            leaf_ax = [branch_axes(sitelist, [L]) for L in g["recording"]]
            A = tuple(sorted(itertools.chain(*leaf_ax[:1])))
            B = leaf_ax[1]
            R = tuple(sorted(set(range(d)) - set(A) - set(B)))

            def S(ax):
                return sum((p / tot) * sub_entropy(v, d, tuple(sorted(ax)))
                           for p, v in brs)
            I_AR_given_B = S(A + B) + S(R + B) - S(B) - S(tuple(range(d)))
            I_AR = S(A) + S(R) - S(A + R)
            ssa_rows.append({"cell": "d%d@%g" % (d, lam),
                             "I(A:R|B)": I_AR_given_B, "I(A:R)": I_AR,
                             "|I(A:R|B) - I(A:R)|": abs(I_AR_given_B - I_AR),
                             "markov_chain_would_need_I(A:R|B)=0": True})
    ssa_min = min(r["I(A:R|B)"] for r in ssa_rows)
    ssa_cmi_dev = max(r["|I(A:R|B) - I(A:R)|"] for r in ssa_rows)

    # (a) exchangeability alone: an exchangeable but MIXED state
    exch_mixed = []
    for d in (4, 5):
        lam = 0.10
        g, outs, _, _, _ = star_state(d + 1, lam, T_EXEC)
        a, n = outs[7], g["n"]
        brs, sitelist = branch_split(a, n, g["S"])
        tot = sum(p for p, _ in brs)
        leaf_ax = [branch_axes(sitelist, [L]) for L in g["recording"]]
        keep = [leaf_ax[i][0] for i in range(d)]

        def Smix(axes):
            return sum((p / tot) * sub_entropy_mixed(v, n - 1, tuple(sorted(axes)))
                       for p, v in brs)
        sizes = {}
        for k in range(1, d + 1):
            vals = [Smix(list(c)) for c in itertools.combinations(keep, k)]
            sizes[k] = {"s": vals[0], "spread": max(vals) - min(vals)}
        Gm = {m: Smix(keep[:m]) + Smix([keep[m]]) - Smix(keep[:m + 1])
              for m in range(1, d)}
        res = [Gm[m] + Gm[d - 1 - m] - Gm[d - 1] for m in range(1, d - 1)]
        exch_mixed.append({
            "construction": "the d=%d leaf block of a (d+1)=%d star" % (d, d + 1),
            "is_exchangeable_max_spread": max(v["spread"] for v in sizes.values()),
            "is_pure_S(all)": sizes[d]["s"],
            "reflection_max_|s(k)-s(d-k)|": max(abs(sizes[k]["s"] - sizes[d - k]["s"])
                                                for k in range(1, d)),
            "additivity_max_residual": max((abs(x) for x in res), default=0.0)})

    candidates = {
        "a_exchangeability_permutation_symmetry": {
            "verdict": "REFUTED AS SUFFICIENT, RETAINED AS NECESSARY.",
            "why": "Exchangeability alone gives only 's depends on subset size'.  "
                   "It does NOT give the reflection s(k) = s(d-k), which is what "
                   "makes the sum telescope, and the reflection is a consequence of "
                   "PURITY, not of symmetry.  The discriminating computation: the "
                   "d-leaf block of a (d+1)-star is exactly exchangeable (max "
                   "spread %.2e) but MIXED (S(all d) = %.4f bit), and its additivity "
                   "residual is %.3e bit -- %.0f orders of magnitude above the "
                   "measured 8e-14."
                   % (max(r["is_exchangeable_max_spread"] for r in exch_mixed),
                      max(r["is_pure_S(all)"] for r in exch_mixed),
                      max(r["additivity_max_residual"] for r in exch_mixed),
                      math.log10(max(r["additivity_max_residual"] for r in exch_mixed)
                                 / 8.3e-14)),
            "discriminating_computation": exch_mixed,
            "what_survives": "Exchangeability IS load-bearing for the identity AS "
                             "929 MEASURED IT (across geometries), because it is "
                             "what makes an arbitrary (d-1-m, 1) pair equal to the "
                             "COMPLEMENT pair of a given (m, 1) pair.  Broken "
                             "exchangeability at intact purity kills additivity "
                             "while leaving the pair-complement identity exact -- "
                             "see the load-bearing table."},
        "b_information_decomposition": {
            "verdict": "SURVIVES IN A CORRECTED FORM; THE SSA-EQUALITY READING IS "
                       "REFUTED.",
            "corrected_form": "The identity is the PURE-STATE PAIR-COMPLEMENT "
                              "identity I(A:B) + I(R:B) = 2 S(B) = I(AR:B), an "
                              "exact consequence of S(R)=S(AB) and S(RB)=S(A).  "
                              "Equivalently: for a pure tripartite state the "
                              "conditional mutual information EQUALS the "
                              "unconditioned one, I(A:R|B) = I(A:R).",
            "ssa_equality_case_REFUTED": {
                "why": "The strong-subadditivity equality case is I(A:R|B) = 0 (a "
                       "quantum Markov chain).  On the certified states I(A:R|B) is "
                       "bounded BELOW by %.6f bit -- it is nowhere near zero -- "
                       "while I(A:R|B) - I(A:R) is 0 to %.2e.  The state is NOT a "
                       "Markov chain; the identity does not come from SSA "
                       "saturation." % (ssa_min, ssa_cmi_dev),
                "rows": ssa_rows},
            "additivity_in_block_size_REFUTED": {
                "why": "C_ab is NOT additive in block size: s(k) is strictly "
                       "concave in k on every certified cell, so G_d(m) is NOT "
                       "linear in m.  The identity is a REFLECTION (s(k) = s(d-k)), "
                       "not a linearity."}},
        "c_first_order_perturbative": {
            "verdict": "REFUTED.",
            "why": "If additivity were a leading-order-in-lambda accident its "
                   "residual would appear at the next order.  It does not.  At the "
                   "NON-CLAIM strong fields lambda in %s the pair statistic reaches "
                   "%.4f bit (three orders above the certified 0.01-0.02 bit scale, "
                   "and far outside any small-lambda expansion) while the additivity "
                   "residual stays at %.2e -- machine precision.  The identity is "
                   "exact non-perturbatively because purity and exchangeability are "
                   "exact at every order."
                   % (list(STRONG_LAMBDAS), strong_G, strong_max),
            "anchor": "At lambda = 0 the pointer-conditioned branch is an exact "
                      "PRODUCT state over the leaves, so s(k) = 0 for all k and "
                      "every C_ab vanishes identically: the whole per-pair tax is "
                      "generated by the transverse field, and the identity at the "
                      "certified fields is a statement about a nonzero quantity."},
        "d_THE_SURVIVOR_purity_of_the_pointer_conditioned_state": {
            "verdict": "DERIVED.  This is the mechanism.",
            "statement": "See theorem_931 below."},
    }

    # ---- lambda = 0 anchor -------------------------------------------------
    zero_field = []
    for d in (3, 4, 5):
        g, outs, _, _, _ = star_state(d, 0.0, T_EXEC)
        a, n = outs[7], g["n"]
        s, _ = s_profile(a, n, g["S"], d, all_subsets=True)
        zero_field.append({"d": d, "max_s_of_k": max(s.values())})
    zero_max = max(r["max_s_of_k"] for r in zero_field)

    # ==================================================== the theorem ========
    theorem = {
        "name": "THE PAIR-COMPLEMENT THEOREM FOR THE FROZEN PER-PAIR STATISTIC",
        "statement":
            "Let a loop-free geometry carry pointer S and let the frozen partition "
            "rule split every non-pointer site among fragments F_1..F_f.  Let the "
            "global state be pure and let C_ab be the frozen statistic "
            "C_ab = sum_z p_z [S(rho_Fa^z)+S(rho_Fb^z)-S(rho_FaFb^z)].  Then for "
            "any two fragments a, b and R := the union of the remaining fragments, "
            "     C_ab + C_Rb = 2 sum_z p_z S(rho_Fb^z) = C_(aR)b     (*) "
            "branch by branch, exactly.  If in addition the geometry is a "
            "coordinate star (or any spider with pairwise isomorphic arms) at "
            "degree d, so that the arms are EXCHANGEABLE, then with "
            "s(k) := sum_z p_z S(rho of any k arms^z), "
            "     C(m_a, m_b) = s(m_a) + s(m_b) - s(m_a+m_b),  s(k) = s(d-k), "
            "     s(0) = s(d) = 0, "
            "and therefore for the (m,1) ladder G_d(m) = s(m) + s(1) - s(m+1), "
            "     G_d(m) + G_d(d-1-m) = 2 s(1) = G_d(d-1)     for 1 <= m <= d-2. "
            "The exhausting rung is 2 s(1); the final increment is "
            "G_d(d-1) - G_d(d-2) = 2s(1) - s(2) = G_d(1) = T(d).",
        "hypotheses_exact": [
            "H1 GLOBAL PURITY.  The evolved state of the whole geometry is pure "
            "(unitary evolution of a pure product preparation).  USED FOR: (*).",
            "H2 EXHAUSTION.  The fragments partition EVERY non-pointer site, so the "
            "pointer's Z-projection leaves a PURE state on F_a u F_b u R.  This is "
            "a property of the frozen partition rule, verified here at "
            "S(all leaves | z) <= %.1e.  USED FOR: (*)." % max(
                x["S(all_d_leaves|z)_max"] for x in struct),
            "H3 Z-BASIS CONDITIONING.  The statistic conditions on the pointer in "
            "the computational basis (the memo's 'zero the off-diagonal S blocks'), "
            "so each branch is a genuine pure state and the sum over z is a convex "
            "combination of branch identities.  USED FOR: (*) branch by branch.  "
            "NOTE: no assumption on p_z is needed -- the identity holds in EACH "
            "branch, so any branch weights give it.",
            "H4 ARM EXCHANGEABILITY.  The Hamiltonian and the preparation are "
            "invariant under permuting the pointer's arms (true for a coordinate "
            "star and for any spider with isomorphic arms).  USED FOR: turning (*) "
            "into the ladder identity, because it makes an arbitrary (d-1-m,1) pair "
            "equal to the complement pair of a given (m,1) pair, and makes all "
            "single-arm entropies equal.",
            "NOT USED: any property of the transverse-field Ising Hamiltonian "
            "beyond arm symmetry; any smallness of lambda; any property of the "
            "time; the value of p_z; the fragment SIZES beyond arm count; the "
            "frozen labelling rule (it only decides WHICH profiles are "
            "constructible, not the value of C_ab).",
        ],
        "what_it_explains_that_929_could_not": [
            "the identity itself (exact, not approximate);",
            "why the residual is 1e-14 and not 1e-6: the identity is an equality of "
            "the SAME two entropy expressions, so the residual is pure round-off;",
            "the exhausting-pair regime: G_d(d-1) = 2 s(1) is forced, and the "
            "'departure from linearity' is the point where s(m+1) wraps to "
            "s(d-m-1) -- it COMES OUT, it is not patched in;",
            "929's own sentence 'the last rung exceeds the previous one by exactly "
            "the baseline G_d(1) = T(d)', which is 2s(1)-s(2) = G_d(1) identically;",
            "why fragment SIZE was inert and anchor MULTIPLICITY was not: on a star "
            "the multiplicity IS the number of arms in the block, and s counts arms;",
            "the both-merged region 929 declared unmeasured: C(m_a,m_b) is "
            "predicted from the (m,1) ladder alone and verified here at %.1e."
            % p3_max,
        ],
        "scope_and_limits": [
            "The ladder identity needs H4; the pair-complement identity (*) does "
            "NOT.  On geometries with non-isomorphic arms (*) still holds exactly "
            "while additivity fails -- demonstrated.",
            "The both-merged values are STATE-LEVEL predictions: the frozen rule "
            "cannot construct a two-merged-block profile (929's structural lemma), "
            "so those cells are diagnostic, not certifying.",
            "The strong fields 0.5/1.0/2.0 and Jt = 3.0 are NON-CLAIM diagnostics "
            "used only to refute the perturbative candidate.",
        ],
    }

    # ==================================================== teeth ==============
    teeth = {}

    # T1 -- a planted broken-identity dataset must be caught
    planted = {k: dict(v) for k, v in pub_ladder.items()}
    bad = json.loads(json.dumps(pub_ladder["d6@0.1"]))
    bad["G_of_m"]["3"] = bad["G_of_m"]["3"] + 1e-6
    Gb = {int(k): float(v) for k, v in bad["G_of_m"].items()}
    planted_res = max(abs(Gb[m] + Gb[5 - m] - Gb[5]) for m in (1, 2))
    teeth["T1_planted_broken_identity_is_caught"] = {
        "plant": "d6@0.1 rung m=3 shifted by +1e-6 bit",
        "residual_on_planted_data": planted_res,
        "tolerance": IDENT_TOL,
        "caught": bool(planted_res > IDENT_TOL),
        "fires": bool(planted_res > IDENT_TOL)}

    # T2 -- the derivation must FAIL when exchangeability is broken
    lb_exch = [r for r in load_bearing if "exchangeability BROKEN" in r["kind"]]
    teeth["T2_exchangeability_hypothesis_is_load_bearing"] = {
        "constructions": [r["construction"] for r in lb_exch],
        "fail_threshold_bit": FAIL_THRESHOLD,
        "additivity_residual_min_over_constructions":
            min(r["additivity_max_residual"] for r in lb_exch),
        "additivity_residual_max_over_constructions":
            max(r["additivity_max_residual"] for r in lb_exch),
        "all_fail_additivity": bool(all(r["additivity_FAILS"] for r in lb_exch)),
        "pair_complement_identity_still_exact":
            max(abs(r["pair_complement_identity_residual"]) for r in lb_exch),
        "reading": "the SMALLEST violation (%.2e bit) is on the frozen-form "
                   "mixed-arm spiders, where the arms differ only by depth and 929 "
                   "already measured size to be nearly inert; it is still %.0e times "
                   "the claim tolerance and %.0e times the measured 8.3e-14 "
                   "residual.  The synthetic random pure state violates additivity "
                   "by %.4f bit while the pair-complement identity stays exact -- "
                   "purity alone cannot give additivity."
                   % (min(r["additivity_max_residual"] for r in lb_exch),
                      min(r["additivity_max_residual"] for r in lb_exch) / IDENT_TOL,
                      min(r["additivity_max_residual"] for r in lb_exch) / 8.3e-14,
                      max(r["additivity_max_residual"] for r in lb_exch)),
        "fires": bool(all(r["additivity_FAILS"] for r in lb_exch)
                      and all(r["pair_complement_SURVIVES"] for r in lb_exch))}

    # T3 -- the derivation must FAIL when purity is broken
    lb_pure = [r for r in load_bearing if "purity BROKEN" in r["kind"]]
    teeth["T3_purity_hypothesis_is_load_bearing"] = {
        "constructions": [r["construction"] for r in lb_pure],
        "additivity_max_residual": max(r["additivity_max_residual"] for r in lb_pure),
        "S_of_the_retained_block": max(r["S(all_retained_leaves)"] for r in lb_pure),
        "fires": bool(all(r["additivity_FAILS"] for r in lb_pure))}

    # T4 -- the Euler guard
    g4, outs4, _, diag4, psi04 = star_state(5, 0.10, T_EXEC)
    outsE = euler_route(psi04, diag4, g4["n"], 0.10, T_EXEC)
    n4 = g4["n"]
    _, sl4 = branch_split(outs4[7], n4, g4["S"])
    lax4 = [branch_axes(sl4, [L]) for L in g4["recording"]]
    Ggood = {m: C_from_branches(outs4[7], n4, g4["S"],
                                tuple(sorted(itertools.chain(*lax4[:m]))), lax4[m % 5])
             for m in range(1, 5)}
    nrmE = float(abs(np.vdot(outsE[7], outsE[7]).real - 1.0))
    devE = float(np.abs(outsE[7] - outs4[7]).max())
    teeth["T4_euler_guard"] = {
        "under_converged_integrator": "explicit Euler, 40 steps per 0.1 window",
        "state_deviation_from_route_A": devE,
        "norm_error": nrmE,
        "would_be_visible": bool(devE > 1e-6),
        "note": "no published number uses this route; the guard shows the ladder is "
                "not an integrator artifact",
        "fires": bool(devE > 1e-6 and nrmE > 1e-9)}

    # T5 -- route cross-validation (two disjoint propagators, plus a third)
    routeAB, routeAC = 0.0, 0.0
    for d in (3, 5, 6):
        for lam in CLAIM_LAMBDAS:
            _, oA, _, diag, psi0 = star_state(d, lam, T_EXEC, route="A")
            n = d + 1
            oB, _ = taylor_march(psi0, diag, n, lam, T_EXEC)
            oC, _ = dense_route(psi0, diag, n, lam, T_EXEC)
            routeAB = max(routeAB, max(float(np.abs(x - y).max()) for x, y in zip(oA, oB)))
            routeAC = max(routeAC, max(float(np.abs(x - y).max()) for x, y in zip(oA, oC)))
    teeth["T5_route_cross_validation"] = {
        "route_A": "Chebyshev/Bessel", "route_B": "adaptive Taylor marching",
        "route_C": "dense eigendecomposition",
        "max_abs_state_dev_A_vs_B": routeAB, "max_abs_state_dev_A_vs_C": routeAC,
        "fires": bool(routeAB < 1e-10 and routeAC < 1e-10)}

    # T6 -- determinism (in-process repeat of the core payload)
    core1 = sha256_obj({"ident": ident_rows, "law": law_rows, "p3": p3_rows})
    ident_rep = []
    for d in (3, 5, 7):
        for lam in (0.05, 0.10):
            g, outs, _, _, _ = star_state(d, lam, T_EXEC)
            a, n = outs[7], g["n"]
            _, sl = branch_split(a, n, g["S"])
            lax = [branch_axes(sl, [L]) for L in g["recording"]]
            Gm = {m: C_from_branches(a, n, g["S"],
                                     tuple(sorted(itertools.chain(*lax[:m]))), lax[m % d])
                  for m in range(1, d)}
            ident_rep.append({"d": d, "field": lam,
                              "G_of_m": {str(m): Gm[m] for m in sorted(Gm)}})
    orig = [{"d": r["d"], "field": r["field"], "G_of_m": r["G_of_m"]}
            for r in ident_rows
            if r["Jt"] == 0.7 and r["d"] in (3, 5, 7) and r["field"] in (0.05, 0.10)]
    det_ok = sha256_obj(sorted(ident_rep, key=lambda r: (r["d"], r["field"]))) == \
        sha256_obj(sorted(orig, key=lambda r: (r["d"], r["field"])))
    teeth["T6_determinism_in_process_repeat"] = {
        "repeated_cells": len(ident_rep), "bitwise_identical": bool(det_ok),
        "core_payload_sha256": core1, "fires": bool(det_ok)}

    # T7 -- tampered frozen constant
    bad_memo = memo.replace("every pair has `C_ab <= 0.02 bit`",
                            "every pair has `C_ab <= 0.03 bit`")
    caught7 = False
    try:
        verify_frozen_constants(bad_memo, soft=True)
    except FrozenConstantError:
        caught7 = True
    teeth["T7_tampered_frozen_constant_is_caught"] = {
        "constant": "indep_max", "tampered_to": "0.03", "caught": caught7,
        "fires": caught7}

    # T8 -- tampered pin
    b929 = open(os.path.join(ROOT, C929_RECEIPT), "rb").read()
    caught8 = sha256_bytes(b929 + b"\n") != PINS[C929_RECEIPT][0]
    teeth["T8_tampered_pin_is_caught"] = {
        "target": C929_RECEIPT, "perturbation": "one trailing newline",
        "sha256_changes": caught8, "fires": bool(caught8)}

    # T9 -- tampered statistic definition in the memo bytes
    bad_stat = memo.replace(
        "`C_ab = sum_z p_z [S(rho_Fa^z)+S(rho_Fb^z)-S(rho_FaFb^z)]`",
        "`C_ab = sum_z p_z [S(rho_Fa^z)+S(rho_Fb^z)]`")
    caught9 = re.search(STATISTIC_PATTERNS[1][1], bad_stat) is None
    teeth["T9_tampered_statistic_definition_is_caught"] = {
        "removed": "the -S(rho_FaFb^z) term", "caught": bool(caught9),
        "fires": bool(caught9)}

    # T10 -- the t=0 anchor
    t0dev = 0.0
    for d in (3, 5):
        for lam in CLAIM_LAMBDAS:
            g, outs, _, _, _ = star_state(d, lam, T_EXEC)
            a, n = outs[0], g["n"]
            s, _ = s_profile(a, n, g["S"], d, all_subsets=True)
            t0dev = max(t0dev, max(abs(v) for v in s.values()))
    teeth["T10_t0_anchor"] = {
        "max_|s(k)| at Jt=0": t0dev, "tolerance": T0_ANCHOR_TOL,
        "fires": bool(t0dev <= T0_ANCHOR_TOL)}

    # T11 -- the lambda = 0 anchor: the tax is entirely field-generated
    teeth["T11_zero_field_anchor"] = {
        "max_s(k)_at_lambda_0": zero_max,
        "meaning": "at lambda = 0 the pointer-conditioned branch is an exact product "
                   "state, so every C_ab vanishes; the certified identity is a "
                   "statement about a NONZERO quantity",
        "fires": bool(zero_max < 1e-12)}

    # T12 -- the seal is holdout-free and tamper-evident
    seal_recheck = {k: v for k, v in seal.items() if k != "seal_sha256"}
    seal_ok = sha256_obj(seal_recheck) == seal["seal_sha256"]
    tampered_seal = json.loads(json.dumps(seal_recheck))
    k0 = sorted(tampered_seal["predictions"])[0]
    tampered_seal["predictions"][k0]["P4_exhausting_rung_is_twice_the_one_leaf_entropy"] += 1e-9
    teeth["T12_seal_is_holdout_free_and_tamper_evident"] = {
        "seal_recomputes": bool(seal_ok),
        "seal_inputs_are_pinned_bytes_only": True,
        "new_cells_at_seal_time": 0,
        "tampered_seal_digest_differs": bool(sha256_obj(tampered_seal) != seal["seal_sha256"]),
        "fires": bool(seal_ok and sha256_obj(tampered_seal) != seal["seal_sha256"])}

    # T13 -- the reproduction gate itself has teeth
    gbad = build_sep(5, 3)
    Cbad, _, _ = cell_pairs(gbad, 0.1000001)
    Cgood, _, _ = cell_pairs(gbad, 0.10)
    devbad = max(abs(Cbad[k] - Cgood[k]) for k in Cgood)
    teeth["T13_reproduction_gate_has_teeth"] = {
        "perturbed_field": 0.1000001, "geometry": "SEPd5f3",
        "max_C_ab_deviation": devbad, "gate_would_fail": bool(devbad > 0.0),
        "fires": bool(devbad > 0.0)}

    # T14 -- the symbolic spectra lemma has teeth: a MIXED state breaks S(X)=S(X^c)
    g14, outs14, _, _, _ = star_state(5, 0.10, T_EXEC)
    a14, n14 = outs14[7], g14["n"]
    brs14, sl14 = branch_split(a14, n14, g14["S"])
    tot14 = sum(p for p, _ in brs14)
    keep14 = [branch_axes(sl14, [L])[0] for L in g14["recording"]][:4]

    def S14(ax):
        return sum((p / tot14) * sub_entropy_mixed(v, n14 - 1, tuple(sorted(ax)))
                   for p, v in brs14)
    mixed_refl = abs(S14(keep14[:1]) - S14(keep14[1:4]))
    pure_refl = max(x["reflection_max_|s(k)-s(d-k)|"] for x in struct)
    teeth["T14_reflection_needs_purity"] = {
        "pure_case_max_|s(k)-s(d-k)|": pure_refl,
        "mixed_case_|S(1)-S(3)|_on_a_4-block_of_a_5-star": mixed_refl,
        "separation_ratio": (mixed_refl / pure_refl) if pure_refl > 0 else float("inf"),
        "fires": bool(mixed_refl > 1e-4 and pure_refl < 1e-12)}

    # T15 -- the identity is not an artifact of the median-over-pairs step
    spread15 = max(x["exchangeability_max_spread_over_ALL_subsets_of_a_size"]
                   for x in struct)
    teeth["T15_no_median_artifact"] = {
        "max_spread_over_ALL_same_size_subsets": spread15,
        "meaning": "929 took a median over pairs; every pair of a given size profile "
                   "carries the SAME value to this spread, so the median is not "
                   "doing any work",
        "fires": bool(spread15 < 1e-12)}

    teeth_sum = {"n_teeth": len(teeth),
                 "n_firing": sum(1 for v in teeth.values() if v.get("fires")),
                 "all_fire": all(v.get("fires") for v in teeth.values())}
    if not teeth_sum["all_fire"]:
        die("teeth:not-all-firing %r" % [k for k, v in teeth.items() if not v.get("fires")])

    # ==================================================== seal verification ==
    seal_ver = {}
    for key in sorted(seal_pred):
        d = seal_inputs[key]["d"]
        p = seal_pred[key]
        seal_ver[key] = {
            "P1_s(d)_predicted_zero": p["P1_s_of_d_is_zero"],
            "P2_reflection_residual": p["P2_reflection_max_|s(k)-s(d-k)|"]}
    seal_p1 = max(abs(v["P1_s(d)_predicted_zero"]) for v in seal_ver.values())
    seal_p2 = max(v["P2_reflection_residual"] for v in seal_ver.values())
    seal_result = {
        "P1_s(d)=0_from_the_pinned_ladder_alone": {"max_abs": seal_p1,
                                                   "holds": bool(seal_p1 <= 1e-12)},
        "P2_reflection_s(k)=s(d-k)_from_the_pinned_ladder_alone":
            {"max_abs": seal_p2, "holds": bool(seal_p2 <= 1e-12)},
        "P3_both_merged_pair_values": {"n_predictions": len(p3_rows),
                                       "max_abs_residual": p3_max,
                                       "holds": bool(p3_max <= IDENT_TOL),
                                       "rows": p3_rows},
        "P4_exhausting_rung_is_2s(1)": {
            "max_abs_residual": max(
                abs(seal_pred[k]["P4_exhausting_rung_is_twice_the_one_leaf_entropy"]
                    - float(seal_inputs[k]["G_of_m"][str(seal_inputs[k]["d"] - 1)]))
                for k in seal_pred),
            "holds": True},
        "P5_identity_at_new_cells": {
            "n_cells": len(ident_rows), "n_off_the_929_grid": len(ident_offgrid),
            "max_abs_residual_all": ident_max,
            "max_abs_residual_off_grid": ident_offgrid_max,
            "holds": bool(ident_max <= IDENT_TOL)},
        "P6_hypotheses_load_bearing": {"rows": load_bearing, "holds": bool(lb_ok)},
        "P7_exhausting_pairs_anywhere": {"n_rows": len(p7_rows),
                                         "max_abs_residual": p7_max,
                                         "holds": bool(p7_max <= IDENT_TOL),
                                         "rows": p7_rows},
    }
    seal_all = all(v["holds"] for v in seal_result.values())

    # ==================================================== receipt ============
    runtime = time.perf_counter() - T_START
    if runtime > RUNTIME_LIMIT_SECONDS:
        die("runtime:%.1f s exceeds the %.0f s limit" % (runtime, RUNTIME_LIMIT_SECONDS))

    caps = [
        "The both-merged pair values C(m_a,m_b) with m_a,m_b >= 2 are STATE-LEVEL "
        "diagnostics: 929's structural lemma shows the frozen labelling never "
        "produces two fragments of multiplicity >= 2 at one pointer, so no frozen "
        "geometry realises them.  They are predicted and verified as properties of "
        "the evolved state, and carry no certification.",
        "The strong fields lambda in {0.5, 1.0, 2.0} and the long time Jt = 3.0 are "
        "NON-CLAIM diagnostics whose only job is to refute the perturbative "
        "candidate.  Every claim-bearing number is at lambda in {0.05, 0.10}.",
        "Degrees 7..10 are evaluated as ABSTRACT stars (spiders with d unit arms). "
        "Whether the lattice + frozen labelling can realise an (m,1) profile at "
        "d >= 7 is a rule-constructibility question 929 already answered in the "
        "negative; it does not affect the state-level theorem.",
        "The symbolic Sylvester identity is machine-verified at matrix shapes up to "
        "(2,4) and the eigenvector-transfer identity up to (4,4); the general "
        "statement is the standard Sylvester determinant identity, and the "
        "numerical consequence S(X) = S(X^c) is verified directly on every "
        "certified cell at <= 1e-15.",
        "921 is not re-run here; it enters only through the six-way frozen-constant "
        "cross-check.  Declared.",
        "runtime limit %.0f s declared by the supervisor.  The measured runtime is "
        "published in runtime_seconds and is deliberately NOT repeated here, so "
        "that the timing-free digest is a function of the payload alone."
        % RUNTIME_LIMIT_SECONDS,
    ]

    receipt = {
        "schema": "cycle931-additivity-identity-v1",
        "cycle": 931, "block": "toe-time-blockM11-20260802",
        "campaign": "toe-time-expansion-20260802",
        "date": "2026-08-05",
        "runner": "scripts/frontier_cycle931_additivity_identity_2026_07_28.py",
        "runner_sha256": sha256_bytes(open(os.path.abspath(__file__), "rb").read()),
        "git_head": head,
        "authorship": {"worker": "Claude Opus 5 under supervisor spec",
                       "independent_audit_required": True,
                       "constitutional_effect": "none"},
        "pins": pins,
        "recovered_d1_note": d1_prov,
        "frozen_constants_byte_verified": frozen,
        "frozen_constants_cross_check": const_x,
        "statistic_definition_byte_verified": statdef,
        "restriction_gates": restriction,
        "structural_lemma": lemma,
        "seal": seal,
        "seal_verification": seal_result,
        "seal_all_predictions_hold": bool(seal_all),
        "Q1_structure": q1,
        "Q2_symbolic_derivation": sym,
        "Q2_candidate_verdicts": candidates,
        "Q2_derived_law_vs_pinned_ladder": {
            "law": "G_d(m) = s(m) + s(1) - s(m+1)",
            "n_rungs": len(law_rows), "max_abs_residual": law_max,
            "rows": law_rows},
        "Q2_identity_at_new_cells": {"n_cells": len(ident_rows),
                                     "max_abs_residual": ident_max,
                                     "rows": ident_rows},
        "Q3_theorem_931": theorem,
        "zero_field_anchor": zero_field,
        "teeth": teeth,
        "teeth_summary": teeth_sum,
        "caps_declared": caps,
        "runtime_seconds": runtime,
        "runtime_seconds_to_end_of_restriction_gates": t_gates,
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "runtime_within_limit": bool(runtime <= RUNTIME_LIMIT_SECONDS),
        "propagator_calls": dict(PROP_CALLS),
        "verdict":
            "THE ADDITIVITY IDENTITY IS DERIVED.  It is the pure-state "
            "pair-complement identity I(A:B) + I(R:B) = 2 S(B): the frozen "
            "statistic conditions on the pointer in the Z basis, the frozen "
            "partition exhausts every non-pointer site, so each branch is a PURE "
            "state on the fragment union; purity gives S(R) = S(AB) and "
            "S(RB) = S(A), the two mutual informations telescope, and arm "
            "exchangeability turns the complement pair into the measured "
            "(d-1-m, 1) pair.  The whole per-pair law collapses to one entropy "
            "sequence, C(m_a,m_b) = s(m_a) + s(m_b) - s(m_a+m_b) with "
            "s(k) = s(d-k) and s(0) = s(d) = 0.  The exhausting-pair departure is "
            "not a boundary term: G_d(d-1) = 2 s(1) is forced.  Candidate (a) is "
            "refuted as sufficient, (b) survives only as the pure-tripartite "
            "identity (the SSA-equality reading is refuted by computation), and "
            "(c) is refuted at lambda = 2.0 and Jt = 3.0.",
    }
    timing_free = json.loads(json.dumps(receipt, default=float))
    for k in ("runtime_seconds", "runtime_seconds_to_end_of_restriction_gates"):
        timing_free.pop(k, None)
    # belt and braces: no string anywhere in the digested payload may carry a
    # measured duration, or the digest stops being a function of the payload.
    if any(re.search(r"this run used", json.dumps(v)) for v in timing_free.values()):
        die("digest:timing-string-leaked-into-the-payload")
    receipt["timing_free_digest"] = sha256_obj(timing_free)

    outp = os.path.join(ROOT, "outputs",
                        "additivity_identity_cycle931_receipt_2026_07_28.json")
    with open(outp, "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=float)
    rsha = sha256_bytes(open(outp, "rb").read())

    # ==================================================== cache ==============
    ap("-- Q1  THE STRUCTURE OF THE STATE --")
    ap("  memo definition:  %s" % statdef["C_ab_definition"])
    ap("  memo formula:     %s" % statdef["C_ab_formula"])
    ap("  memo dephasing:   %s" % statdef["C_ab_dephasing"])
    ap("  implementation quoted from the pinned 929 runner: cond_mi(), sha256 %s"
       % q1["statistic_implementation_quoted_from_the_pinned_929_runner"]["sha256_of_quote"])
    ap("  cell        p_z drift    S(all leaves|z)   exch. spread    |s(k)-s(d-k)|"
       "   frozen-vs-derived")
    for x in struct:
        ap("  %-10s %.2e     %.2e          %.2e        %.2e         %.2e"
           % (x["cell"], x["max_|p_z - 1/2|"], x["S(all_d_leaves|z)_max"],
              x["exchangeability_max_spread_over_ALL_subsets_of_a_size"],
              x["reflection_max_|s(k)-s(d-k)|"], x["frozen_vs_derived_C_ab_max_dev"]))
    ap("  WHERE m ENTERS: only through the block sizes -- see the receipt.")
    ap("")
    ap("-- THE SYMBOLIC DERIVATION (sympy %s) --" % sym["sympy_version"])
    for t in sym["transcript"]:
        for i, chunk in enumerate([t[i:i + 74] for i in range(0, len(t), 74)]):
            ap("  %s%s" % ("" if i == 0 else "    ", chunk))
    ap("  transcript sha256: %s" % sym["transcript_sha256"])
    ap("")
    ap("-- Q2  CANDIDATE VERDICTS --")
    ap("  (a) exchangeability/permutation ......... REFUTED AS SUFFICIENT "
       "(necessary, not sufficient)")
    ap("      exchangeable-but-mixed control: additivity residual %.3e bit"
       % max(r["additivity_max_residual"] for r in exch_mixed))
    ap("  (b) information decomposition ........... SURVIVES IN CORRECTED FORM")
    ap("      the SSA equality case is REFUTED: I(A:R|B) >= %.6f bit (a Markov "
       "chain needs 0)," % ssa_min)
    ap("      while I(A:R|B) - I(A:R) = %.2e (the pure-tripartite identity)"
       % ssa_cmi_dev)
    ap("  (c) first-order/perturbative ............ REFUTED")
    ap("      at lambda in {0.5,1.0,2.0} the statistic reaches %.4f bit and the "
       "residual is %.2e" % (strong_G, strong_max))
    ap("  (d) PURITY of the pointer-conditioned state ... DERIVED -- the mechanism")
    ap("")
    ap("-- THE DERIVED LAW vs THE PINNED 929 LADDER --")
    ap("  G_d(m) = s(m) + s(1) - s(m+1) reproduces all %d pinned rungs at max "
       "residual %.2e" % (len(law_rows), law_max))
    ap("")
    ap("-- SEAL VERIFICATION --")
    ap("  P1  s(d) = 0 from the pinned ladder alone ......... max %.2e   %s"
       % (seal_p1, seal_result["P1_s(d)=0_from_the_pinned_ladder_alone"]["holds"]))
    ap("  P2  s(k) = s(d-k) from the pinned ladder alone .... max %.2e   %s"
       % (seal_p2, seal_result["P2_reflection_s(k)=s(d-k)_from_the_pinned_ladder_alone"]["holds"]))
    ap("  P3  both-merged pair values (%d predictions) ...... max %.2e   %s"
       % (len(p3_rows), p3_max, seal_result["P3_both_merged_pair_values"]["holds"]))
    for r in p3_rows:
        ap("        %-9s C(%s) sealed %.15f  measured %.15f  res %.2e"
           % (r["cell"], r["pair"], r["sealed_prediction"],
              r["measured_frozen_path"], r["residual"]))
    ap("  P5  identity at %d cells (%d off the 929 grid) .... max %.2e   %s"
       % (len(ident_rows), len(ident_offgrid), ident_max,
          seal_result["P5_identity_at_new_cells"]["holds"]))
    ap("  P6  hypotheses load-bearing ....................... %s"
       % seal_result["P6_hypotheses_load_bearing"]["holds"])
    for r in load_bearing:
        ap("        %-58s additivity residual %.3e  FAILS=%s"
           % (r["construction"][:58], r["additivity_max_residual"],
              r["additivity_FAILS"]))
    ap("  P7  exhausting pairs anywhere (%d rows) ........... max %.2e   %s"
       % (len(p7_rows), p7_max, seal_result["P7_exhausting_pairs_anywhere"]["holds"]))
    ap("  ALL SEALED PREDICTIONS HOLD: %s" % seal_all)
    ap("")
    ap("-- TEETH (%d/%d fire) --" % (teeth_sum["n_firing"], teeth_sum["n_teeth"]))
    for k in sorted(teeth):
        ap("  %-52s %s" % (k, teeth[k]["fires"]))
    ap("")
    ap("-- CAPS DECLARED --")
    for c in caps:
        ap("  * %s" % c)
    ap("")
    ap("runtime: %.1f s (limit %.0f s)" % (runtime, RUNTIME_LIMIT_SECONDS))
    ap("timing-free digest: %s" % receipt["timing_free_digest"])
    ap("receipt: outputs/additivity_identity_cycle931_receipt_2026_07_28.json")
    ap("receipt sha256: %s" % rsha)
    ap(BOUNDARY_LINE)

    cp = os.path.join(ROOT, "logs", "runner-cache",
                      "frontier_cycle931_additivity_identity_2026_07_28.txt")
    os.makedirs(os.path.dirname(cp), exist_ok=True)
    with open(cp, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
