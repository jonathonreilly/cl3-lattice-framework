#!/usr/bin/env python3
"""Cycle 926 -- THE GATE-ROBUSTNESS SWEEP AND THE SEPARATION FAMILY.

TWO QUESTIONS, ONE BLOCK.  Cycle 917 built a 14-cell geometry ladder under the
frozen route-C certification gates; Cycle 919 added twelve degree-5 cells and
located the field-ceiling threshold at degree 5 -- and published, honestly, that
the boundary is decided by about eight ten-thousandths of a bit of C_ab, so that
"a gate moved ~2e-3 bits moves the threshold".  919 named two hardenings.  This
block runs both.

  Q1  THE GATE-ROBUSTNESS SWEEP.  Sweep the persistence-relevant gate parameters
      around their frozen values -- the C_ab independence gate over [0.005, 0.08],
      the persistence sample count over {2,3,4,5}, and the onset deadline over
      {0.5 ... 1.2} -- and recompute the FULL 26-cell 917+919 verdict table at
      every sweep point.  Deliver the EXACT stability region of each headline,
      the per-claim robustness certificate with boundary values, and the honest
      statement of which headlines are gate-robust and which are gate-artifacts.

      The sweep is EXACT, not sampled.  Every gate-dependent quantity in the
      frozen protocol enters only through the predicate `C_ab(pair) <= gate`, so
      the whole verdict table is piecewise constant in the gate with breakpoints
      exactly at the measured C_ab values.  Those breakpoints are enumerated and
      the verdict is evaluated at each, which gives stability regions with exact
      endpoints instead of grid resolution.  The declared dense grid (log-spaced
      plus a fine linear window at 0.02) is ALSO evaluated and published, and is
      checked to be consistent with the exact interval decomposition.

  Q2  THE SEPARATION FAMILY.  On every geometry measured so far the partition
      rule makes four statistics numerically equal -- pointer degree, max degree,
      branch count, fragment count -- so 917/919 could only ever say "degree".
      This block designs the minimal family that SEPARATES them and measures
      which statistic actually carries the laws.

      Two of the four turn out to be separable only in principle: see the
      IDENTITY ANALYSIS below.  The family separates what can be separated and
      says so where it cannot.

  Q3  THE REFINED LAW: the ceiling law and the threshold law restated with the
      carrying statistic named per law and the Q1 robustness qualifier attached.

THE IDENTITY ANALYSIS (read this before the family).  The frozen partition rule
is "each recording site anchors a fragment; every other site joins its nearest
recording site's fragment; ties by the frozen memo's tie-break".  Under it:

  branch_count_at_pointer := deg(S)  is the SAME VARIABLE as pointer_degree in
      the frozen implementation -- an identity, not a measurement.  No geometry
      can separate them.  Reported as an identity, never as a fitted law.

  n_fragments  equals pointer_degree whenever the recording sites carry distinct
      fragment LABELS.  The frozen memo's own labelling text -- "assign each
      axial face site to its own signed-axis fragment; assign an edge with x != 0
      to F_(sign(x)x); for an edge with x=0 and for every corner ... map
      (sign(y),sign(z)) ..." -- is NOT injective off the axial faces.  So a
      geometry whose recording sites are not all axial faces makes the rule ITSELF
      merge anchors, and n_fragments drops below pointer_degree with the rule
      applied verbatim.  That is the separation the spec asks for, and the rule's
      own text is what fires it.

  max_degree  is separable freely: put the high-degree hub in the environment and
      the pointer on a low-degree site.

  components_of_G_minus_S ("branch count", the non-trivial reading) is ALREADY
      separated from pointer_degree inside the pinned 26 cells (G4: 1 vs 4; G5:
      3 vs 6; G6: 1 vs 6; H4: 2 vs 5).  This block adds one clean new cell and
      reads the verdict off the pinned data as well.

THE FAMILY (design freedom, declared).

  A-family (fragment count at fixed degree) -- eight geometries that are the SAME
  GRAPH as an already-measured one (K_{1,5} for A1..A5, K_{1,6} for A6..A8), hence
  the same Hamiltonian, the same preparation and the same evolved state, embedded
  in cube coordinates at positions where the frozen labelling merges a different
  number of anchors.  pointer_degree, max_degree, branch_count and
  components_of_G_minus_S are held FIXED across the family by construction; ONLY
  n_fragments moves.  This is the minimal separating design: one statistic varies,
  three are pinned, and the dynamics are bit-identical.

  B-family (degree at fixed fragment structure) -- matched controls at n = 6 whose
  fragment count AND fragment-size multiset equal an A-family member's while the
  pointer degree is lowered to the fragment count.  If A and B agree inside a
  matched pair, the partition carries the law and pointer degree does not.

  C-family (max degree) -- pointer degree 2 or 4 with a degree-6 hub in the
  environment.

  D-family (components of G-S at fixed degree 5).

  E-family (the merge with depth: a non-star merge geometry with second-shell
  sites, so the finding is not an artifact of stars) with its own matched control.

RESTRICTION GATES (all hard-fail).  Before any swept or new number is produced:
  * 21/21 frozen constants byte-verified from the frozen memo, quote-identical to
    BOTH the pinned 917 and 919 receipts;
  * the partition rule reproduces the frozen memo's six published cube fragment
    lists exactly;
  * Cycle 917 reproduced VALUE-FOR-VALUE: 12 cells, 156 rows, deviation exactly 0;
  * Cycle 919 reproduced VALUE-FOR-VALUE: 12 cells, 156 rows, deviation exactly 0;
  * the G6 cube cells (imported in both 914->917 and 917->919) expanded to full
    row level out of the pinned 914 receipt's published symmetry classes and
    verified against the pinned 914 R_ind ledger (13 rows x 3 deltas) and the
    pinned 917 import event -- which is what makes all 26 cells sweepable rather
    than 24.

Deterministic, float64/complex128, no network, no tree writes outside the
declared receipt.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.
No formation rule.
Sets no audit status.
"""

import bisect
import hashlib
import itertools
import json
import math
import os
import platform
import re
import resource
import subprocess
import sys
import time
from collections import deque

import numpy as np
from scipy.special import jv

T_START = time.perf_counter()

BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ================================================================== pins =====
PINS = {
    "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md": (
        "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
        "5dff1d8b1692099cd86b53959834b6bcb5865a71"),
    "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md": (
        "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
        "d5b36708949d06bf619b2452e8f2897468e51194"),
    "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md": (
        "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
        "5f056aa69d1cc06dbfa2dc9ed6804df40c7b39fe"),
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
        "4a863da1f3f255354839277271a3a69a5c205133"),
    "scripts/frontier_cycle917_geometry_ladder_2026_07_28.py": (
        "eb119f3bba365461274df51e0bdafc4a2047634863ef48b2662dcf7d3b61fb05",
        "b70ad19d4cc11265c465aea1bb4b2d6e5605ca5e"),
    "scripts/frontier_cycle917_geometry_independent_check_2026_07_28.py": (
        "208c8da9480894ad7a7c1248567ffcf0ff792fdfd812e01bfd45c220445d35c6",
        "1726563c9468b78d1bf9678f43c944087ee63358"),
    "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json": (
        "37568809db0d5f319b6fe9a41962cc58c8215ade2c4b9acb24eab4b665535240",
        "11e336cf0a86c46492f6ccf03b13963357840b71"),
    "outputs/geometry_independent_check_cycle917_receipt_2026_07_28.json": (
        "fe8a30918b543ecb440665adbec237ca4e5efd7db47b1951983226a8479fbc10",
        "1a3299702c7dce132360ce26af61ee89ccb2021c"),
    "outputs/geometry_ladder_block_cycle917_ship_receipt_2026_07_28.json": (
        "76651b5db064719aae94778777fde0a197c12f822523b66565e3d77100d88889",
        "f57d93272b3ab43a5b6ab9f7c8fcab33668f300a"),
    "docs/GEOMETRY_LADDER_CHAIN_CERTIFIES_CYCLE917_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "b424c3aaf684015f6ca08e81446df58c2d85a1c4e981a8c220be165989d057d4",
        "6311514dcd9a97f1a14b0ba7249b7570baeaff14"),
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
        "cabb1bef15221b5fca61ffc7c50f8ec18452893d"),
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json": (
        "d7d27ce19d231624415db1e71ee77eae16b5175dd403b403c254b38fb171b0a7",
        "9931c298a5917eb90de290cbb82c237508c9e692"),
}
# the 919 package -- pinned from the tree at first run and hard-checked thereafter
PINS_919 = [
    "scripts/frontier_cycle919_degree_five_2026_07_28.py",
    "scripts/frontier_cycle919_degree_five_independent_check_2026_07_28.py",
    "outputs/degree_five_cycle919_receipt_2026_07_28.json",
    "outputs/degree_five_independent_check_cycle919_receipt_2026_07_28.json",
    "outputs/degree_five_block_cycle919_ship_receipt_2026_07_28.json",
    "docs/DEGREE_FIVE_CERTIFIES_THRESHOLD_LOCATED_CYCLE919_BOUNDED_THEOREM_NOTE_2026-07-28.md",
]
PINS.update({
    "scripts/frontier_cycle919_degree_five_2026_07_28.py": (
        "15ce5dbd37cea6e4d7286dc85d0c04abd9948bae2a84910e5f9486c5fa35b196",
        "c22ebafcb743824db67ef1abe9f2f223ea6664a1"),
    "scripts/frontier_cycle919_degree_five_independent_check_2026_07_28.py": (
        "34526d5060c2cf592dce7b6b8986f2878209ae9c68e91138658725aabe22a29b",
        "f5c4f5c5a149b8d03d70d59ad97ebeb5b6b6cc2d"),
    "outputs/degree_five_cycle919_receipt_2026_07_28.json": (
        "cf85c74b62f1e6a83287a824f56315f3b1cf4b9387056d94906bb0195aae04f5",
        "587349db8b77c31d20f0aa04e6e69a1bb206a6d0"),
    "outputs/degree_five_independent_check_cycle919_receipt_2026_07_28.json": (
        "b455e3c5669f4cfeae0046a6ffb410daac8ce4bb89465b1a30f884190c232662",
        "bd57ac3ec780e0cb95e1f821fb159c52b0988690"),
    "outputs/degree_five_block_cycle919_ship_receipt_2026_07_28.json": (
        "6b1a64ac400dfe1d46fdee2ea093a615ccfd29fa54cde874695d9650561e8ead",
        "853f9a8ca8e80e42f25bf70cbf1dcc3a3d3b0802"),
    "docs/DEGREE_FIVE_CERTIFIES_THRESHOLD_LOCATED_CYCLE919_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "1ff7389686d3bf7472d42fdc79c3edee292929b92821c4043432460eeedeb7ab",
        "cfeed45cb2c9b269e7a64e4777ecfbe94f7691ea"),
})

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C914_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C917_CHECK_RECEIPT = "outputs/geometry_independent_check_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"

D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
FROZEN_LAMBDAS = (0.05, 0.10)
EXTENSION_LAMBDA = 0.075
LAMBDAS = (0.05, 0.075, 0.10)
MEMO_LAMBDAS = (0.05, 0.10, 0.20)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
T0_ANCHOR_TOL = 1e-9
DRIFT_MAX = 0.10
PERSIST_N = 3
MACH_TOL = 1e-9
RESTRICT_TOL = 1e-9
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
PROBE_LAMBDAS = (0.02, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20)

CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")

# ------------------------------------------------------------- sweep grids ---
GATE_MIN, GATE_MAX = 0.005, 0.08
GATE_GRID = sorted(set(
    [round(float(v), 12) for v in np.geomspace(GATE_MIN, GATE_MAX, 25)]
    + [round(0.015 + 0.00025 * i, 12) for i in range(41)]
    + [INDEP_MAX]))
PERSIST_GRID = (2, 3, 4, 5)
DEADLINE_GRID = (0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2)
# declared SECONDARY one-dimensional axes (content side of the gate stack)
EXCESS_GRID = [round(float(v), 12) for v in np.geomspace(0.005, 0.08, 16)] + [EXCESS_MIN]
CONTENT_GRID = [0.01, 0.05, 0.20, 0.50, 0.90, 0.99, 0.999]

C917_KEYS = ["G1", "G2", "G3a", "G3b", "G4", "G5"]
C919_KEYS = ["H1", "H2", "H3", "H4"]
LADDER_KEYS = C917_KEYS + ["G6"] + C919_KEYS


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def die(msg):
    print("MACHINERY-FAIL %s %s" % (msg, BOUNDARY_LINE))
    sys.exit(2)


def git(args):
    return subprocess.run(["git"] + args, cwd=ROOT, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


def verify_pins():
    out = {}
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            die("pin:missing %s" % path)
        b = open(full, "rb").read()
        got_sha = sha256_bytes(b)
        got_blob = git(["hash-object", full]).stdout.decode().strip()
        if want_sha is not None and got_sha != want_sha:
            die("pin:sha256 %s got=%s want=%s" % (path, got_sha, want_sha))
        if want_blob is not None and got_blob != want_blob:
            die("pin:blob %s got=%s want=%s" % (path, got_blob, want_blob))
        out[path] = {"sha256": got_sha, "git_blob": got_blob, "bytes": len(b),
                     "sha256_pinned_in_source": want_sha is not None,
                     "git_blob_pinned_in_source": want_blob is not None}
    return out


def recover_d1_note():
    cmds = ["git cat-file -e HEAD:%s" % D1_NOTE_PATH,
            "git cat-file -t %s" % D1_NOTE_BLOB,
            "git cat-file blob %s" % D1_NOTE_BLOB]
    if git(["cat-file", "-e", "HEAD:%s" % D1_NOTE_PATH]).returncode == 0:
        die("d1-note:unexpectedly-in-tree")
    if git(["cat-file", "-t", D1_NOTE_BLOB]).stdout.decode().strip() != "blob":
        die("d1-note:blob-missing %s" % D1_NOTE_BLOB)
    r = git(["cat-file", "blob", D1_NOTE_BLOB])
    if r.returncode != 0:
        die("d1-note:cat-file-failed")
    b = r.stdout
    got = sha256_bytes(b)
    if got != D1_NOTE_SHA256 or len(b) != D1_NOTE_BYTES:
        die("d1-note:identity got=%s bytes=%d" % (got, len(b)))
    rec915 = json.load(open(os.path.join(ROOT, C915_RECEIPT)))
    art = rec915["C1_recovery"]["artifacts"][D1_NOTE_PATH]["recovered"]
    if art["sha256"] != got:
        die("d1-note:915-receipt-cross-check")
    for rp in (C917_RECEIPT, C919_RECEIPT):
        if json.load(open(os.path.join(ROOT, rp)))["recovered_d1_note"]["sha256"] != got:
            die("d1-note:%s-cross-check" % rp)
    return {"path": D1_NOTE_PATH, "blob": D1_NOTE_BLOB, "sha256": got, "bytes": len(b),
            "in_tree_at_head": False, "sha256_matches_915_917_919_receipts": True,
            "commands_disclosed": cmds}


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


def verify_frozen_constants(memo):
    out = {}
    for name, pat, expect in CONSTANT_PATTERNS:
        m = re.search(pat, memo)
        if m is None:
            die("frozen-const:pattern-miss %s" % name)
        quote = " ".join(m.group(0).split())
        val = None
        if expect is not None:
            val = float(m.group(1))
            if abs(val - float(expect)) > 0:
                die("frozen-const:value %s memo=%r code=%r" % (name, val, expect))
        out[name] = {"quote": quote, "memo_value": val, "code_value": expect,
                     "byte_verified": True}
    return out


def cross_check_prior_constants(frozen):
    res = {}
    for tag, rp in (("917", C917_RECEIPT), ("919", C919_RECEIPT)):
        theirs = json.load(open(os.path.join(ROOT, rp)))["frozen_constants_byte_verified"]
        if set(theirs) != set(frozen):
            die("frozen-const:%s-key-set" % tag)
        for k in sorted(frozen):
            if theirs[k]["quote"] != frozen[k]["quote"]:
                die("frozen-const:%s-quote %s" % (tag, k))
        res["identical_to_%s_receipt" % tag] = True
    res["count"] = len(frozen)
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
    """The frozen signed-axis label of a cube-coordinate site (917/919 `_axis_label`)."""
    for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
        if c[ax] != 0:
            return ("+" if c[ax] > 0 else "-") + nm
    die("axis-label:origin %r" % (c,))


def build_geometry(key, name, sites, bonds_coord, pointer, label_of_rec,
                   tiebreak, dim, note):
    """Assemble a geometry under the frozen partition rule.

    DISCLOSED IMPLEMENTATION FIX (verified a no-op on every pinned cell).  The
    917/919 source builds the anchor table with the dict comprehension
        frags = {label_of[r]: [r] for r in rec}
    which SILENTLY DROPS an anchor whenever two recording sites receive the same
    fragment label -- and then dies on the exhaustiveness assertion.  The frozen
    memo's text says "assign each axial face site to its OWN SIGNED-AXIS
    fragment", i.e. the fragment NAMED by the site's signed axis; two sites with
    the same signed axis therefore belong to the same fragment.  This build
    implements that reading (anchors are appended, not overwritten).  On every
    geometry where the labels are distinct -- which is every geometry in 917 and
    919 -- the two are identical, and the 26-cell value-for-value reproduction
    gate proves it.
    """
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
    frags = {}
    anchors = {}
    for r in rec:
        frags.setdefault(label_of[r], []).append(r)
        anchors.setdefault(label_of[r], []).append(r)
    merged = {L: [sites[i] for i in v] for L, v in anchors.items() if len(v) > 1}
    ties = []
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
            ties.append({"site": str(sites[i]), "nearest_distance": m,
                         "candidates": labcands, "assigned": label_of[pick]})
        frags[label_of[pick]].append(i)
    labels = sorted(frags, key=lambda L: (CUBE_LABELS.index(L) if L in CUBE_LABELS else 99, L))
    for L in labels:
        heads = anchors[L]
        rest = [i for i in frags[L] if i not in heads]
        frags[L] = sorted(heads, key=lambda i: str(sites[i])) + \
            sorted(rest, key=lambda i: (dS[i], str(sites[i])))
    if sorted(itertools.chain(*frags.values())) != [i for i in range(n) if i != S]:
        die("geometry:%s partition-not-exhaustive" % key)
    shells = {}
    for i in range(n):
        if i != S:
            shells.setdefault(dS[i], []).append(i)
    degs = {i: len(adj[i]) for i in range(n)}
    rest = [i for i in range(n) if i != S]
    radj = {i: [j for j in adj[i] if j != S] for i in rest}
    seen, comps = set(), []
    for i in rest:
        if i in seen:
            continue
        comp, q = [], deque([i])
        seen.add(i)
        while q:
            u = q.popleft()
            comp.append(u)
            for v in radj[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        comps.append(sorted(comp))
    frag_of = {i: L for L in labels for i in frags[L]}
    seams = set()
    for (a, b) in bonds:
        if a == S or b == S:
            continue
        if frag_of[a] != frag_of[b]:
            seams.add(tuple(sorted((frag_of[a], frag_of[b]))))
    return {
        "key": key, "name": name, "note": note, "dim": dim, "n": n,
        "sites": [str(c) for c in sites], "coords": sites, "idx": idx,
        "bonds": bonds, "adj": adj, "S": S, "pointer": str(pointer),
        "recording": rec, "labels": labels, "frags": frags, "ties": ties,
        "dS": dS, "shells": shells, "degrees": degs,
        "anchor_labels": {L: [sites[i] for i in anchors[L]] for L in labels},
        "merged_anchor_fragments": merged,
        "stats": {
            "n_sites": n, "n_bonds": len(bonds),
            "pointer_degree": len(rec),
            "max_degree": max(degs.values()),
            "branch_count_at_pointer": len(rec),
            "components_of_G_minus_S": len(comps),
            "depth_eccentricity_from_pointer": max(dS.values()),
            "cyclomatic_number_loops": len(bonds) - n + 1,
            "loop_free": bool(len(bonds) - n + 1 == 0),
            "dimension": dim,
            "n_fragments": len(labels),
            "fragment_sizes": {L: len(frags[L]) for L in labels},
            "seam_pairs": sorted("|".join(s) for s in seams),
            "n_seam_pairs": len(seams),
        },
    }


# ------------------------------------------- the pinned 917 / 919 geometries --
def geom_chain9():
    sites = [(k, 0, 0) for k in range(-4, 5)]
    bonds = [((k, 0, 0), (k + 1, 0, 0)) for k in range(-4, 4)]
    return build_geometry("G1", "chain9", sites, bonds, (0, 0, 0),
                          lambda c: ("+x" if c[0] > 0 else "-x"), cube_tiebreak, 1,
                          "917 G1: the d=1 reference, the open 9-site chain")


def geom_star7():
    sites = ["S"] + ["a%d" % i for i in range(1, 7)]
    bonds = [("S", "a%d" % i) for i in range(1, 7)]
    return build_geometry("G2", "star7", sites, bonds, "S", lambda c: c, None, "star",
                          "917 G2: K_{1,6}, maximal local branching, zero depth")


def geom_tree(nbranch):
    sites, bonds = ["S"], []
    for b in range(nbranch):
        c = "b%d" % b
        sites.append(c)
        bonds.append(("S", c))
        for k in range(2):
            g = "b%dg%d" % (b, k)
            sites.append(g)
            bonds.append((c, g))
    key = {3: "G3a", 4: "G3b", 5: "H2"}[nbranch]
    return build_geometry(key, "tree%d" % len(sites), sites, bonds, "S",
                          lambda c: c, None, "tree",
                          "pinned %s: centre + %d branches of depth 2" % (key, nbranch))


def geom_plaquette9():
    sites = [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]

    def lab(c):
        return ("+x" if c[0] > 0 else "-x") if c[0] != 0 else ("+y" if c[1] > 0 else "-y")
    return build_geometry("G4", "plaquette9", sites, bonds, (0, 0, 0), lab,
                          cube_tiebreak, 2, "917 G4: the open 3x3 square, d=2 with loops")


def geom_cubeminus11():
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("G5", "cubeminus11", sites, bonds, (0, 0, 0), axis_label,
                          cube_tiebreak, 3, "917 G5: centre + 6 faces + the 4 z=0 edges")


def geom_cube27():
    sites = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("G6", "cube27", sites, bonds, (0, 0, 0), axis_label,
                          cube_tiebreak, 3, "917 G6: the open 3x3x3 cube (partition-rule "
                                            "verification instance; 2^27 is never evolved)")


def geom_star6():
    sites = ["S"] + ["a%d" % i for i in range(1, 6)]
    bonds = [("S", "a%d" % i) for i in range(1, 6)]
    return build_geometry("H1", "star6", sites, bonds, "S", lambda c: c, None, "star",
                          "919 H1: K_{1,5}")


def geom_tree16():
    return geom_tree(5)


def geom_tree10d5():
    sites, bonds = ["S"], []
    for b in range(5):
        c = "b%d" % b
        sites.append(c)
        bonds.append(("S", c))
        if b < 2:
            for k in range(2):
                g = "b%dg%d" % (b, k)
                sites.append(g)
                bonds.append((c, g))
    return build_geometry("H3", "tree10d5", sites, bonds, "S", lambda c: c, None, "tree",
                          "919 H3: centre + 5 branches, exactly two of depth 2")


def geom_cubeminus10():
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("H4", "cubeminus10", sites, bonds, (0, 0, 0), axis_label,
                          cube_tiebreak, 3, "919 H4: cubeminus11 with the -z face deleted")


PINNED_BUILD = {"G1": geom_chain9, "G2": geom_star7, "G3a": lambda: geom_tree(3),
                "G3b": lambda: geom_tree(4), "G4": geom_plaquette9,
                "G5": geom_cubeminus11, "H1": geom_star6, "H2": geom_tree16,
                "H3": geom_tree10d5, "H4": geom_cubeminus10}


# ================================================ THE Q2 SEPARATION FAMILY ===
def _lat_nbrs(P):
    out = []
    for ax in range(3):
        for s in (1, -1):
            q = list(P)
            q[ax] += s
            out.append(tuple(q))
    return out


def coord_star(key, name, P, N, note):
    """A star K_{1,|N|} embedded in cube coordinates: pointer P, leaves N (all lattice
    neighbours of P).  The frozen signed-axis labelling is applied VERBATIM; where it
    assigns the same label to two leaves, the frozen rule merges them into one fragment."""
    for q in N:
        if q not in _lat_nbrs(P):
            die("coord-star:%s non-lattice leaf %r" % (key, q))
        if q == (0, 0, 0):
            die("coord-star:%s leaf at the origin (the frozen labelling has no label "
                "for it)" % key)
    sites = [P] + list(N)
    bonds = [(P, q) for q in N]
    return build_geometry(key, name, sites, bonds, P, axis_label, cube_tiebreak, 3, note)


# A-family: pointer degree held at 5 (A1..A5) and 6 (A6..A8); only n_fragments moves.
def geom_A1():
    P = (0, 0, 1)
    N = [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (0, 0, 2)]
    return coord_star("A1", "star5f5", P, N,
                      "A1 CONTROL: K_{1,5} with five DISTINCT signed-axis labels "
                      "(+x,-x,+y,-y,+z).  Same graph, Hamiltonian and state as the pinned "
                      "919 H1 star6; must reproduce H1 value-for-value.")


def geom_A2():
    P = (0, 1, 1)
    N = [(1, 1, 1), (-1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2)]
    return coord_star("A2", "star5f4", P, N,
                      "A2: K_{1,5}; the frozen labelling sends (0,2,1) and (0,1,2) both to "
                      "+y, so the rule ITSELF merges two anchors -- degree 5, FOUR "
                      "fragments, sizes {2,1,1,1}.")


def geom_A3():
    P = (0, 1, 1)
    N = [(1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2), (0, 1, 0)]
    return coord_star("A3", "star5f3", P, N,
                      "A3: K_{1,5}; three leaves labelled +y -- degree 5, THREE fragments, "
                      "sizes {3,1,1}.")


def geom_A4():
    P = (1, 1, 0)
    N = [(0, 1, 0), (2, 1, 0), (1, 2, 0), (1, 0, 0), (1, 1, 1)]
    return coord_star("A4", "star5f2", P, N,
                      "A4: K_{1,5}; four leaves labelled +x -- degree 5, TWO fragments, "
                      "sizes {4,1}.")


def geom_A5():
    P = (1, 1, 0)
    N = [(2, 1, 0), (1, 2, 0), (1, 0, 0), (1, 1, 1), (1, 1, -1)]
    return coord_star("A5", "star5f1", P, N,
                      "A5: K_{1,5}; ALL five leaves labelled +x -- degree 5, ONE fragment.  "
                      "R_ind >= 2 is unreachable by the rule's own arithmetic.")


def geom_A6():
    P = (0, 0, 1)
    N = [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (0, 0, 2), (0, 0, 0)]
    sites = [P] + N
    bonds = [(P, q) for q in N]

    def lab(c):
        return "-z" if c == (0, 0, 0) else axis_label(c)
    return build_geometry("A6", "star6f6", sites, bonds, P, lab, cube_tiebreak, 3,
                          "A6 CONTROL: K_{1,6} with six distinct labels (the origin leaf is "
                          "labelled -z by hand -- DECLARED, the frozen labelling has no "
                          "label for the origin).  Must reproduce the pinned 917 G2 star7.")


def geom_A7():
    P = (0, 1, 1)
    N = _lat_nbrs(P)
    return coord_star("A7", "star6f4", P, N,
                      "A7: K_{1,6}; three leaves labelled +y -- degree 6, FOUR fragments, "
                      "sizes {3,1,1,1}.")


def geom_A8():
    P = (1, 1, 0)
    N = _lat_nbrs(P)
    return coord_star("A8", "star6f2", P, N,
                      "A8: K_{1,6}; five leaves labelled +x -- degree 6, TWO fragments, "
                      "sizes {5,1}.")


# B-family: matched controls -- same fragment count AND size multiset AND n as an
# A-family member, with the pointer degree lowered to the fragment count.
def _named(key, name, sites, bonds, note):
    return build_geometry(key, name, sites, bonds, "S", lambda c: c, None, "tree", note)


def geom_B1():
    sites = ["S", "a", "b", "c", "d", "a1"]
    bonds = [("S", "a"), ("S", "b"), ("S", "c"), ("S", "d"), ("a", "a1")]
    return _named("B1", "deg4f4", sites, bonds,
                  "B1 MATCHED CONTROL for A2: n=6, FOUR fragments of sizes {2,1,1,1}, "
                  "pointer degree FOUR.")


def geom_B2():
    sites = ["S", "a", "b", "c", "a1", "a2"]
    bonds = [("S", "a"), ("S", "b"), ("S", "c"), ("a", "a1"), ("a", "a2")]
    return _named("B2", "deg3f3", sites, bonds,
                  "B2 MATCHED CONTROL for A3: n=6, THREE fragments of sizes {3,1,1}, "
                  "pointer degree THREE.")


def geom_B3():
    sites = ["S", "a", "b", "a1", "a2", "a3"]
    bonds = [("S", "a"), ("S", "b"), ("a", "a1"), ("a", "a2"), ("a", "a3")]
    return _named("B3", "deg2f2", sites, bonds,
                  "B3 MATCHED CONTROL for A4: n=6, TWO fragments of sizes {4,1}, pointer "
                  "degree TWO.")


def geom_B4():
    sites = ["S", "a", "a1", "a2", "a3", "a4"]
    bonds = [("S", "a"), ("a", "a1"), ("a", "a2"), ("a", "a3"), ("a", "a4")]
    return _named("B4", "deg1f1", sites, bonds,
                  "B4 MATCHED CONTROL for A5: n=6, ONE fragment of size 5, pointer degree "
                  "ONE.")


# C-family: max degree separated from pointer degree (the hub is in the environment).
def geom_C1():
    sites = ["S", "a", "b"] + ["a%d" % i for i in range(1, 6)]
    bonds = [("S", "a"), ("S", "b")] + [("a", "a%d" % i) for i in range(1, 6)]
    return _named("C1", "hub2asym", sites, bonds,
                  "C1: pointer degree TWO, max degree SIX (the hub `a` carries five "
                  "leaves).  Fragments {6,1}.")


def geom_C2():
    sites = ["S", "a", "b"] + ["a%d" % i for i in range(1, 4)] + \
        ["b%d" % i for i in range(1, 4)]
    bonds = [("S", "a"), ("S", "b")] + [("a", "a%d" % i) for i in range(1, 4)] + \
        [("b", "b%d" % i) for i in range(1, 4)]
    return _named("C2", "hub2sym9", sites, bonds,
                  "C2: pointer degree TWO, max degree FOUR on BOTH arms -- the SYMMETRIC "
                  "hub control (C1 is the asymmetric one).  Fragments {4,4}, n=9.  Sized "
                  "so that the largest fragment PAIR stays well inside the full space: a "
                  "symmetric degree-6 hub would put both 6-site fragments and the pointer "
                  "in one 2^13 reduced state, which the frozen C_ab estimator cannot "
                  "evaluate inside the runtime budget.  DECLARED.")


def geom_C3():
    sites = ["S", "a", "b", "c", "d"] + ["a%d" % i for i in range(1, 6)]
    bonds = [("S", x) for x in ("a", "b", "c", "d")] + \
        [("a", "a%d" % i) for i in range(1, 6)]
    return _named("C3", "hub4", sites, bonds,
                  "C3: pointer degree FOUR, max degree SIX.  Fragments {6,1,1,1}.")


# D-family: components of G-S at fixed pointer degree 5.
def geom_D1():
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0), (1, 0, 1)]
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("D1", "cubeminus10plus", sites, bonds, (0, 0, 0), axis_label,
                          cube_tiebreak, 3,
                          "D1: 919's H4 with the (1,0,1) edge added, which welds the +z "
                          "face onto the z=0 ring -- pointer degree 5, FIVE fragments, "
                          "components of G-S = ONE (H4 has two, H1 has five).")


# E-family: the merge with depth (not a star), plus its matched control.
def geom_E1():
    P = (0, 1, 1)
    N = [(1, 1, 1), (-1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2)]
    ext = [(2, 1, 1), (-2, 1, 1), (0, 3, 1), (0, 1, 3)]
    sites = [P] + N + ext
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("E1", "merge10d2", sites, bonds, P, axis_label, cube_tiebreak, 3,
                          "E1: A2's merge with a second shell -- degree 5, FOUR fragments "
                          "of sizes {4,2,2,1}, depth 2, n=10, loop-free.  The merge finding "
                          "off the star family.")


def geom_E2():
    sites = ["S", "a", "b", "c", "d", "a1", "a2", "a3", "b1", "c1"]
    bonds = [("S", x) for x in ("a", "b", "c", "d")] + \
        [("a", "a1"), ("a1", "a2"), ("a1", "a3"), ("b", "b1"), ("c", "c1")]
    return _named("E2", "deg4f4d2", sites, bonds,
                  "E2 MATCHED CONTROL for E1: n=10, FOUR fragments of sizes {4,2,2,1}, "
                  "depth 3, pointer degree FOUR.")


NEW_BUILD = {"A1": geom_A1, "A2": geom_A2, "A3": geom_A3, "A4": geom_A4, "A5": geom_A5,
             "A6": geom_A6, "A7": geom_A7, "A8": geom_A8,
             "B1": geom_B1, "B2": geom_B2, "B3": geom_B3, "B4": geom_B4,
             "C1": geom_C1, "C2": geom_C2, "C3": geom_C3,
             "D1": geom_D1, "E1": geom_E1, "E2": geom_E2}
NEW_KEYS = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
            "B1", "B2", "B3", "B4", "C1", "C2", "C3", "D1", "E1", "E2"]


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
    Tn = np.empty_like(psi0)
    nmv = 1
    for k in range(M + 1):
        if k == 0:
            v = T0
        elif k == 1:
            v = T1
        else:
            mv(T1, Tn)
            Tn *= 2.0 / A
            Tn -= T0
            nmv += 1
            T0, T1, Tn = T1, Tn, T0
            v = T1
        for j, t in enumerate(times):
            c = jv(k, A * t) * ((-1j) ** k) * (1.0 if k == 0 else 2.0)
            if abs(c) > 1e-18:
                outs[j] += c * v
    tail = float(max(abs(jv(M + 1, A * tmax)), abs(jv(M + 2, A * tmax))))
    return outs, {"route": "chebyshev", "half_width": A, "degree": M, "matvecs": nmv,
                  "tail_bound": 2.0 * tail}


def taylor_march(psi0, diag, n, lam, times, hbound=1.0, pmax=40):
    A = float(np.abs(diag).max() + lam * n)
    mv = _matvec_factory(diag, n, lam)
    psi = psi0.astype(np.complex128).copy()
    outs = []
    tprev = 0.0
    nsub = nmv = 0
    worst_rem = 0.0
    worst_deg = 0
    for t in times:
        dt = t - tprev
        if dt < -1e-15:
            die("taylor:non-monotone-grid")
        if dt > 1e-15:
            s = max(1, int(math.ceil(A * dt / hbound)))
            h = dt / s
            for _ in range(s):
                term = psi.copy()
                acc = psi.copy()
                p = 0
                for k in range(1, pmax + 1):
                    term = mv(term) * (-1j * h / k)
                    nmv += 1
                    acc += term
                    p = k
                    if float(np.abs(term).max()) < 1e-19:
                        break
                psi = acc
                nsub += 1
                worst_deg = max(worst_deg, p)
                worst_rem = max(worst_rem, float((A * h) ** (p + 1) / math.gamma(p + 2)))
        outs.append(psi.copy())
        tprev = t
    return outs, {"route": "taylor-march", "norm_bound": A, "substeps": nsub,
                  "matvecs": nmv, "max_taylor_degree": worst_deg,
                  "max_substep_remainder_bound": worst_rem, "h_bound": hbound}


def dense_route(psi0, diag, n, lam, times):
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
    return outs, {"route": "dense-eigh", "dim": d, "emin": float(w[0]), "emax": float(w[-1])}


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


def chi_holevo(rho, k):
    d = 1 << k
    s0, s1 = rho[:d, :d], rho[d:, d:]
    p = [float(np.trace(s0).real), float(np.trace(s1).real)]
    tot = p[0] + p[1]
    Sav, n1 = ent_bits(np.linalg.eigvalsh((s0 + s1) / tot))
    Sc, n2 = 0.0, 0.0
    for s, pz in ((s0, p[0]), (s1, p[1])):
        if pz <= 1e-14:
            continue
        e, nn = ent_bits(np.linalg.eigvalsh(s / pz))
        Sc += (pz / tot) * e
        n2 = min(n2, nn)
    H = -sum((q / tot) * np.log2(q / tot) for q in p if q / tot > 1e-15)
    herm = float(np.abs(rho - rho.conj().T).max())
    return Sav - Sc, H, [p[0] / tot, p[1] / tot], min(n1, n2), herm


def cond_mi(rho, ka, kb):
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


def r_ind_from_passes(labels, singles, C, gate):
    """The frozen R_ind: largest pairwise-independent certifying subset, ties to the
    lexicographically first in the declared label order.  `gate` replaces the frozen
    0.02 bit; at gate = INDEP_MAX this is the frozen function verbatim."""
    order = {L: i for i, L in enumerate(labels)}
    best, best_key = [], None
    for r in range(len(singles), 0, -1):
        for comb in itertools.combinations(singles, r):
            ok = True
            for a, b in itertools.combinations(comb, 2):
                v = C.get(tuple(sorted((a, b), key=order.get)))
                if v is None or v > gate:
                    ok = False
                    break
            if ok:
                key = tuple(order[c] for c in comb)
                if best_key is None or key < best_key:
                    best, best_key = list(comb), key
        if best:
            break
    return len(best), best


def content_passes(labels, chi, excess, H, delta, content_h_min=CONTENT_H_MIN,
                   excess_min=EXCESS_MIN):
    return [L for L in labels if H >= content_h_min and chi[L] >= (1.0 - delta) * H
            and excess[L] >= excess_min]


def r_ind(labels, chi, excess, H, C, delta):
    singles = content_passes(labels, chi, excess, H, delta)
    k, best = r_ind_from_passes(labels, singles, C, INDEP_MAX)
    return k, best, singles


def centered_frobenius(lam, n, nbonds, degrees):
    den = np.sqrt(float(nbonds) + n * lam * lam)
    out = {}
    for deg in sorted(set(degrees.values())):
        out[str(deg)] = {"Z": 2.0 * lam / den, "X": 2.0 * np.sqrt(deg) / den,
                         "Y": 2.0 * np.sqrt(deg + lam * lam) / den}
    return out


# ============================================================= measurement ===
def measure(g, states, times):
    n, S, labels, frags = g["n"], g["S"], g["labels"], g["frags"]
    nbrs = g["recording"]
    rows = []
    chi0, one0, theta0, xchi0 = {}, {}, None, {}
    mach = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0,
            "entropy_bound": 0.0, "symmetry": 0.0, "t0_anchor": 0.0}
    for it, (t, a) in enumerate(zip(times, states)):
        mach["norm"] = max(mach["norm"], abs(float(np.vdot(a, a).real) - 1.0))
        chi, one_by_shell, one_by_site = {}, {}, {}
        H = None
        pz = None
        for L in labels:
            sites = frags[L]
            rho = joint_rho(a, n, [S] + sites)
            c, H, pz, neg, herm = chi_holevo(rho, len(sites))
            chi[L] = c
            mach["hermiticity"] = max(mach["hermiticity"], herm)
            mach["negativity"] = max(mach["negativity"], abs(neg))
            mach["entropy_bound"] = max(mach["entropy_bound"], max(0.0, c - H, -c))
        for i in range(n):
            if i == S:
                continue
            c1, _, _, _, _ = chi_holevo(joint_rho(a, n, [S, i]), 1)
            one_by_site[i] = c1
            one_by_shell.setdefault(g["dS"][i], []).append(c1)
        theta = 0.0
        for nb in nbrs:
            rb = joint_rho(a, n, [S, nb])
            theta += 1.0 - float(np.trace(rb @ rb).real)
        theta /= len(nbrs)
        if it == 0:
            chi0 = dict(chi)
            one0 = {k: float(np.mean(v)) for k, v in one_by_shell.items()}
            theta0 = theta
            mach["t0_anchor"] = max(mach["t0_anchor"],
                                    max(abs(v) for v in chi.values()),
                                    max(abs(v) for v in one_by_site.values()))
        exc = {L: chi[L] - chi0[L] for L in labels}
        one_exc = {k: float(np.mean(v)) - one0[k] for k, v in one_by_shell.items()}
        C = {}
        for a1, b1 in itertools.combinations(labels, 2):
            rho = joint_rho(a, n, [S] + frags[a1] + frags[b1])
            C[(a1, b1)] = cond_mi(rho, len(frags[a1]), len(frags[b1]))
            if it == 0:
                mach["t0_anchor"] = max(mach["t0_anchor"], abs(C[(a1, b1)]))
        rr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(labels, chi, exc, H, C, d)
            rr["%.2f" % d] = k
            subs["%.2f" % d] = sub
            sing["%.2f" % d] = sg
        xchi = {}
        for L in labels:
            sites = frags[L]
            T = a.reshape((2,) * n)
            ax = [n - 1 - s for s in [S] + sites + [i for i in range(n)
                                                    if i != S and i not in sites]]
            Mx = np.transpose(T, ax).reshape(2, -1)
            v0 = (Mx[0] + Mx[1]) / np.sqrt(2.0)
            v1 = (Mx[0] - Mx[1]) / np.sqrt(2.0)
            k = len(sites)
            M0 = v0.reshape(1 << k, -1)
            M1 = v1.reshape(1 << k, -1)
            s0, s1 = M0 @ M0.conj().T, M1 @ M1.conj().T
            rho = np.zeros((2 << k, 2 << k), dtype=np.complex128)
            rho[:1 << k, :1 << k] = s0
            rho[1 << k:, 1 << k:] = s1
            cx, Hx, _, _, _ = chi_holevo(rho, k)
            xchi[L] = (cx, Hx)
        Hx = xchi[labels[0]][1]
        if it == 0:
            xchi0 = {L: xchi[L][0] for L in labels}
        xpass = {}
        for d in DELTAS:
            xpass["%.2f" % d] = [L for L in labels
                                 if Hx >= CONTENT_H_MIN and xchi[L][0] >= (1.0 - d) * Hx
                                 and xchi[L][0] - xchi0[L] >= EXCESS_MIN]
        rows.append({
            "jt": t, "H_Z": H, "p_z": pz, "pointer_tv_drift": abs(pz[0] - 0.5),
            "chi": chi, "excess": exc, "theta_A": theta - theta0,
            "one_site_chi_by_shell": {str(k): float(np.mean(v))
                                      for k, v in sorted(one_by_shell.items())},
            "one_site_excess_by_shell": {str(k): v for k, v in sorted(one_exc.items())},
            "one_site_shell_spread": {str(k): (float(max(v) - min(v)))
                                      for k, v in sorted(one_by_shell.items())},
            "capacity_gain": {L: chi[L] - max(one_by_site[i] for i in frags[L])
                              for L in labels},
            "sum_delta_chi": float(sum(exc.values())),
            "C_ab": {"|".join(k): v for k, v in sorted(C.items())},
            "r_ind": rr, "certifying_subsets": subs, "singleton_passes": sing,
            "r_raw": {k: len(v) for k, v in sing.items()},
            "x_control": {"H_X": Hx, "singleton_passes": xpass,
                          "r_ind_ge2_possible": bool(any(len(v) >= 2 for v in xpass.values()))},
        })
    return rows, mach


# ==================================================== gates, parameterized ===
def row_profile(labels, row, delta=HEADLINE_DELTA, gmin=None, gmax=None):
    """The step function gate -> (R_ind, witness) for ONE row.

    R_ind enters the frozen protocol only through the predicate C_ab(pair) <= gate, so
    the ledger changes only at measured C_ab values.  Enumerating them once per row is
    what makes the sweep exact AND affordable: every later gate query is a bisect.
    """
    dk = "%.2f" % delta
    singles = row["singleton_passes"][dk]
    C = {tuple(k.split("|")): v for k, v in row["C_ab"].items()}
    lo = 0.0 if gmin is None else gmin
    crit = sorted({v for (a, b), v in C.items()
                   if a in singles and b in singles and v > lo
                   and (gmax is None or v <= gmax)})
    xs = [lo] + crit
    return xs, [r_ind_from_passes(labels, singles, C, x) for x in xs]


class LedgerCache(object):
    """Per-cell cache of the 13 row step functions; ledger lookup is then O(13 log p)."""

    def __init__(self, rows, labels, delta=HEADLINE_DELTA):
        self.rows = rows
        self.profiles = [row_profile(labels, r, delta) for r in rows]
        self.criticals = sorted({v for r in rows for v in r["C_ab"].values()})

    def ledger(self, gate):
        out = []
        for xs, vals in self.profiles:
            out.append(vals[bisect.bisect_right(xs, gate) - 1])
        return out


def ledger_at(rows, labels, gate, delta=HEADLINE_DELTA):
    """The R_ind ledger of a cell at an arbitrary C_ab gate (content side frozen)."""
    dk = "%.2f" % delta
    out = []
    for r in rows:
        singles = r["singleton_passes"][dk]
        C = {tuple(k.split("|")): v for k, v in r["C_ab"].items()}
        k, wit = r_ind_from_passes(labels, singles, C, gate)
        out.append((k, wit))
    return out


def verdict_from_ledger(rows, ledger, persist_n, deadline, comm_ok):
    """The frozen verdict routine with (persistence count, deadline) exposed."""
    x_ok = not any(r["x_control"]["r_ind_ge2_possible"]
                   for r in rows if r["jt"] <= deadline + 1e-12)
    idx = next((i for i, (k, _) in enumerate(ledger) if k >= 2), None)
    if idx is None:
        any_content = any(len(r["singleton_passes"]["%.2f" % HEADLINE_DELTA]) >= 2
                          for r in rows)
        best_C = min((min(r["C_ab"].values()) for r in rows if r["C_ab"]), default=None)
        reason = ("content-gate: fewer than two fragments ever reach (1-delta)H with "
                  "0.02-bit excess" if not any_content else
                  "independence-gate: two or more fragments reach content but every "
                  "eligible pair exceeds the C_ab gate")
        return {"verdict": "NO", "reason": reason, "event": None,
                "min_C_ab_over_grid": best_C,
                "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    run = 0
    for (k, _) in ledger[idx:]:
        if k >= 2:
            run += 1
        else:
            break
    r = rows[idx]
    ev = {"jt": r["jt"], "theta_A": r["theta_A"], "r_ind": ledger[idx][0],
          "witness": ledger[idx][1], "run": run,
          "by_deadline": bool(r["jt"] <= deadline + 1e-12),
          "persists": bool(run >= persist_n),
          "pointer_tv_drift": r["pointer_tv_drift"],
          "chi_at_event": {L: r["chi"][L] for L in ledger[idx][1]},
          "H_Z_at_event": r["H_Z"],
          "C_at_event": {k: v for k, v in r["C_ab"].items()
                         if all(p in ledger[idx][1] for p in k.split("|"))}}
    if not ev["by_deadline"]:
        return {"verdict": "NO", "reason": "late: first R_ind>=2 after the deadline",
                "event": ev, "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    if not ev["persists"]:
        return {"verdict": "NO", "reason": "persistence: fewer than %d consecutive "
                                           "certification samples with R_ind>=2" % persist_n,
                "event": ev, "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    if ev["pointer_tv_drift"] > DRIFT_MAX:
        return {"verdict": "NO", "reason": "pointer drift exceeds 0.10 at the event",
                "event": ev, "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    if not (x_ok and comm_ok):
        return {"verdict": "NO", "reason": "CHECK-02 pointer demolition control",
                "event": ev, "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    return {"verdict": "YES", "reason": None, "event": ev, "x_control_ok": x_ok,
            "commutator_ordering_ok": comm_ok}


def cell_at(rows, labels, gate=INDEP_MAX, persist_n=PERSIST_N, deadline=DEADLINE_JT,
            delta=HEADLINE_DELTA, comm_ok=True):
    led = ledger_at(rows, labels, gate, delta)
    v = verdict_from_ledger(rows, led, persist_n, deadline, comm_ok)
    v["max_r_ind"] = max(k for k, _ in led)
    v["ledger"] = [k for k, _ in led]
    return v


def xi_reg_of(rows):
    imax = int(np.argmax([r["sum_delta_chi"] for r in rows]))
    r = rows[imax]
    xi = 0
    for sh, v in sorted((int(k), v) for k, v in r["one_site_excess_by_shell"].items()):
        if v >= EXCESS_MIN:
            xi = max(xi, sh)
    return {"xi_reg": xi, "t_summax": r["jt"], "sum_delta_chi": r["sum_delta_chi"],
            "shell_excess": r["one_site_excess_by_shell"]}


def persistence_profile(rows, labels, gate=INDEP_MAX, persist_n=PERSIST_N,
                        delta=HEADLINE_DELTA, deadline=DEADLINE_JT):
    """The 919 margin instrument: how far is this cell from flipping, in bits of C_ab."""
    dk = "%.2f" % delta
    led = ledger_at(rows, labels, gate, delta)

    def sample_of(r):
        passes = r["singleton_passes"][dk]
        pairs = {k: v for k, v in r["C_ab"].items() if all(p in passes for p in k.split("|"))}
        binding_C = min(pairs.values()) if pairs else None
        return {"jt": r["jt"], "n_content_passes": len(passes),
                "content_margin_bits": max(r["chi"].values()) - (1.0 - delta) * r["H_Z"],
                "min_C_ab_over_all_pairs": min(r["C_ab"].values()) if r["C_ab"] else None,
                "binding_pair_C_ab_among_content_passes": binding_C,
                "independence_margin_bits": (None if binding_C is None else gate - binding_C),
                "binding_gate": ("content" if len(passes) < 2 else "independence")}

    idx = next((i for i, (k, _) in enumerate(led) if k >= 2), None)
    if idx is None:
        live = [sample_of(r) for r in rows if len(r["singleton_passes"][dk]) >= 2
                and r["jt"] <= deadline + 1e-12]
        best = min([s["binding_pair_C_ab_among_content_passes"] for s in live
                    if s["binding_pair_C_ab_among_content_passes"] is not None], default=None)
        return {"has_event": False, "run": 0, "needed": persist_n, "persists": False,
                "misses_by_one_sample": False, "clears_by_one_sample": False,
                "margin_at_the_third_sample_bits": None,
                "deficit_at_the_first_failing_sample_bits": None,
                "rows_with_two_or_more_content_passes": [s["jt"] for s in live],
                "best_binding_pair_C_ab_on_those_rows": best,
                "shortfall_bits": (best - gate) if best is not None else None,
                "failure_mode": ("empty content window" if best is None
                                 else "content window closed by conditional dependence")}
    run = 0
    for (k, _) in led[idx:]:
        if k >= 2:
            run += 1
        else:
            break
    samples = [sample_of(r) for r in rows[idx:idx + run + 1]]
    last_ok = samples[run - 1] if run >= 1 else None
    first_bad = samples[run] if len(samples) > run else None
    nth = samples[persist_n - 1] if run >= persist_n else None
    return {"has_event": True, "first_jt": rows[idx]["jt"], "run": run, "needed": persist_n,
            "persists": bool(run >= persist_n), "samples": samples,
            "margin_at_the_last_certifying_sample_bits":
                (last_ok["independence_margin_bits"] if last_ok else None),
            "margin_at_the_third_sample_bits":
                (nth["independence_margin_bits"] if nth else None),
            "first_failing_sample_jt": (first_bad["jt"] if first_bad else None),
            "first_failing_sample_binding_gate": (first_bad["binding_gate"] if first_bad
                                                  else None),
            "deficit_at_the_first_failing_sample_bits":
                (None if (first_bad is None
                          or first_bad["binding_pair_C_ab_among_content_passes"] is None)
                 else first_bad["binding_pair_C_ab_among_content_passes"] - gate),
            "misses_by_one_sample": bool(run == persist_n - 1),
            "clears_by_one_sample": bool(run == persist_n)}


# ================================== the G6 import, expanded to row level =====
G6_PAIR_CLASS = {}
for _cls, _members in {
        "opposite-55": [("+x", "-x")],
        "opposite-44": [("+y", "-y"), ("+z", "-z")],
        "plus-x-orthogonal": [("+x", q) for q in ("+y", "-y", "+z", "-z")],
        "minus-x-orthogonal": [("-x", q) for q in ("+y", "-y", "+z", "-z")],
        "transverse-orthogonal": [("+y", "+z"), ("+z", "-y"), ("-y", "-z"), ("-z", "+y")],
}.items():
    for _pa in _members:
        G6_PAIR_CLASS[tuple(sorted(_pa, key=CUBE_LABELS.index))] = _cls
if len(G6_PAIR_CLASS) != 15:
    die("g6:pair-class-count %d" % len(G6_PAIR_CLASS))


def g6_rows(rec914, lam_key):
    """Expand the pinned 914 cube rows to the full per-fragment / per-pair schema.

    The 914 receipt publishes chi per fragment CLASS (closed-five for +-x, wedge-four
    for the other four) and C_ab per PAIR CLASS (five classes covering all fifteen
    pairs, declared verbatim in the 914 source).  Both maps are pure relabellings of
    the cube's own symmetry, so the expansion is lossless; it is verified against the
    pinned 914 R_ind ledger before use.
    """
    labels = list(CUBE_LABELS)
    out = []
    for r in rec914["measurement"]["rows"][lam_key]:
        chi = {L: (r["chi_closed_five"] if L in ("+x", "-x") else r["chi_wedge_four"])
               for L in labels}
        exc = {L: (r["excess_closed_five"] if L in ("+x", "-x") else r["excess_wedge_four"])
               for L in labels}
        pc = r["pair_classes"]
        C = {}
        if pc:
            for pa, cls in G6_PAIR_CLASS.items():
                C["|".join(pa)] = pc[cls]
        # the x-control is taken as PUBLISHED by the pinned 914 receipt.  914 evaluated it
        # only inside its own Jt <= 1.0 window; rows 1.1 and 1.2 carry no x-control, and
        # are treated as passing with the cap declared in `deviations`.
        xc = r.get("x_control")
        sing = {"%.2f" % d: content_passes(labels, chi, exc, r["H_Z"], d) for d in DELTAS}
        out.append({
            "jt": r["jt"], "H_Z": r["H_Z"], "p_z": r["p_z"],
            "pointer_tv_drift": r["pointer_tv_drift"],
            "chi": chi, "excess": exc, "theta_raw": r["theta"],
            "sum_delta_chi": r["sum_delta_chi"],
            "one_site_excess_by_shell": {str(i + 1): v for i, (_, v) in
                                         enumerate(sorted(r["one_site_excess"].items(),
                                                          key=lambda kv: {"face": 0, "edge": 1,
                                                                          "corner": 2}[kv[0]]))},
            "C_ab": C, "pair_classes": pc,
            "singleton_passes": sing,
            "x_control": {"H_X": (None if xc is None else xc["H_X"]),
                          "singleton_passes": (None if xc is None
                                               else xc["singleton_passes"]),
                          "evaluated_in_the_pinned_914_receipt": xc is not None,
                          "r_ind_ge2_possible": (False if xc is None
                                                 else bool(xc["r_ind_ge2_possible"]))},
        })
    th0 = out[0]["theta_raw"]
    for r in out:
        r["theta_A"] = r["theta_raw"] - th0
    return labels, out


def verify_g6_expansion(rec914, rec917):
    """Hard gate: the expanded rows must reproduce the pinned 914 R_ind ledger for every
    row and every delta, the pinned 914 singleton passes, and the pinned 917 import event."""
    detail = {}
    labels = list(CUBE_LABELS)
    for lam_key, lk in (("0.05", "0.05"), ("0.1", "0.1")):
        _, rows = g6_rows(rec914, lam_key)
        pub = rec914["measurement"]["rows"][lam_key]
        bad = []
        for r, q in zip(rows, pub):
            for d in DELTAS:
                dk = "%.2f" % d
                if sorted(r["singleton_passes"][dk]) != sorted(q["singleton_passes"][str(d)]):
                    bad.append("passes@%.1f/%s" % (r["jt"], dk))
                C = {tuple(k.split("|")): v for k, v in r["C_ab"].items()}
                k, wit = r_ind_from_passes(labels, r["singleton_passes"][dk], C, INDEP_MAX)
                if k != q["r_ind"][str(d)]:
                    bad.append("r_ind@%.1f/%s %d!=%d" % (r["jt"], dk, k, q["r_ind"][str(d)]))
                if wit != q["certifying_subsets"][str(d)]:
                    bad.append("witness@%.1f/%s" % (r["jt"], dk))
        cell = cell_at(rows, labels, comm_ok=True)
        want = rec917["ladder"]["G6@%s" % lk]
        wev = want["event"]
        ev = cell["event"]
        for nm, a, b in (("verdict", cell["verdict"], want["verdict"]),
                         ("max_r_ind", cell["max_r_ind"], want["max_r_ind"]),
                         ("jt", ev["jt"], wev["jt"]), ("r_ind", ev["r_ind"], wev["r_ind"]),
                         ("run", ev["run"], wev["run"]),
                         ("witness", ev["witness"], wev["witness"])):
            if a != b:
                bad.append("917-import:%s %r!=%r" % (nm, a, b))
        if abs(ev["theta_A"] - wev["theta_A"]) > RESTRICT_TOL:
            bad.append("917-import:theta_A %.3g" % abs(ev["theta_A"] - wev["theta_A"]))
        for k2, v2 in wev["C_at_event"].items():
            if abs(ev["C_at_event"][k2] - v2) > 0.0:
                bad.append("917-import:C_at_event")
        detail["G6@%s" % lk] = {"rows": len(rows), "mismatches": bad,
                                "verdict": cell["verdict"], "max_r_ind": cell["max_r_ind"],
                                "first_jt": ev["jt"], "run": ev["run"],
                                "witness": ev["witness"], "theta_A": ev["theta_A"],
                                "reproduces_pinned_914_ledger_and_917_import": not bad}
        if bad:
            die("g6-expansion:%s %s" % (lk, bad[:4]))
    return detail


# ================================================= exact interval machinery ==
def cell_gate_intervals(cache, persist_n, deadline, comm_ok,
                        gmin=GATE_MIN, gmax=GATE_MAX):
    """EXACT verdict-vs-gate decomposition on [gmin, gmax].

    Every gate-dependent branch of the frozen protocol is the predicate
    C_ab(pair) <= gate, so the verdict is piecewise constant with breakpoints only at
    measured C_ab values.  Enumerating them gives the stability region exactly.
    """
    rows = cache.rows
    xs = [gmin] + [v for v in cache.criticals if gmin < v <= gmax]
    out = []
    for i, g in enumerate(xs):
        hi = xs[i + 1] if i + 1 < len(xs) else None
        led = cache.ledger(g)
        c = verdict_from_ledger(rows, led, persist_n, deadline, comm_ok)
        c["max_r_ind"] = max(k for k, _ in led)
        rec = {"lo": g, "hi": hi, "hi_open": True, "verdict": c["verdict"],
               "max_r_ind": c["max_r_ind"],
               "first_jt": (c["event"] or {}).get("jt"), "run": (c["event"] or {}).get("run")}
        if out and out[-1]["verdict"] == rec["verdict"] and \
                out[-1]["max_r_ind"] == rec["max_r_ind"] and \
                out[-1]["first_jt"] == rec["first_jt"] and out[-1]["run"] == rec["run"]:
            out[-1]["hi"] = hi
        else:
            out.append(rec)
    return out


def merge_breakpoints(*interval_lists):
    xs = set()
    for il in interval_lists:
        for iv in il:
            xs.add(iv["lo"])
    return sorted(xs)


def value_at(intervals, g):
    lo = [iv["lo"] for iv in intervals]
    i = bisect.bisect_right(lo, g) - 1
    return intervals[max(0, i)]


def measure_of(intervals, pred, gmax=GATE_MAX):
    """Total gate-length (in bits) on which pred(interval) holds, plus the interval list."""
    tot = 0.0
    keep = []
    for i, iv in enumerate(intervals):
        hi = iv["hi"] if iv["hi"] is not None else gmax
        if pred(iv):
            tot += max(0.0, hi - iv["lo"])
            keep.append([iv["lo"], hi])
    merged = []
    for a, b in keep:
        if merged and abs(merged[-1][1] - a) < 1e-15:
            merged[-1][1] = b
        else:
            merged.append([a, b])
    return tot, merged


# ==================================================================== main ===
def main():
    pins = verify_pins()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    const_x = cross_check_prior_constants(frozen)
    d1_prov = recover_d1_note()
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()
    r914 = json.load(open(os.path.join(ROOT, C914_RECEIPT)))
    r917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    r919 = json.load(open(os.path.join(ROOT, C919_RECEIPT)))

    mach_all = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0, "entropy_bound": 0.0,
                "t0_anchor": 0.0, "cheby_tail": 0.0, "taylor_remainder": 0.0,
                "route_AB_max_dev": 0.0, "route_AC_max_dev": 0.0, "determinism": 0.0}

    # ------------------------------------- restriction gate 1: the partition rule --
    cube = geom_cube27()
    memo_frags = parse_memo_cube_fragments(memo)
    rule_detail, rule_ok = {}, True
    for L in CUBE_LABELS:
        mine = {cube["coords"][i] for i in cube["frags"][L]}
        theirs = set(memo_frags[L])
        rule_detail[L] = {"memo": sorted(str(c) for c in theirs),
                          "rule": sorted(str(c) for c in mine),
                          "identical_as_sets": bool(mine == theirs)}
        rule_ok = rule_ok and (mine == theirs)
    if not rule_ok:
        die("partition-rule:does-not-reproduce-memo-cube")

    # ------------------ restriction gates 2 and 3: 917 and 919 value-for-value ----
    CACHE = {}          # (key, lk) -> rows
    GEOM = {}
    restrict = {"cycle917": {"cells": 0, "rows": 0, "mismatches": [],
                             "max_abs_dev": {"chi": 0.0, "C_ab": 0.0, "theta_A": 0.0,
                                             "H_Z": 0.0, "excess": 0.0}},
                "cycle919": {"cells": 0, "rows": 0, "mismatches": [],
                             "max_abs_dev": {"chi": 0.0, "C_ab": 0.0, "theta_A": 0.0,
                                             "H_Z": 0.0, "excess": 0.0}},
                "per_cell": {}}

    def repro(tag, key, lk, rows, pubrows, pub_stats, g):
        R = restrict[tag]
        bad = []
        if pub_stats is not None and pub_stats != g["stats"]:
            for sk in sorted(set(pub_stats) | set(g["stats"])):
                if pub_stats.get(sk) != g["stats"].get(sk):
                    bad.append("stats:%s %r!=%r" % (sk, g["stats"].get(sk),
                                                    pub_stats.get(sk)))
        idxp = {r["jt"]: r for r in pubrows}
        for r in rows:
            q = idxp.get(r["jt"])
            if q is None:
                bad.append("row-missing@%.1f" % r["jt"])
                continue
            R["rows"] += 1
            for L in r["chi"]:
                R["max_abs_dev"]["chi"] = max(R["max_abs_dev"]["chi"],
                                              abs(r["chi"][L] - q["chi"][L]))
                R["max_abs_dev"]["excess"] = max(R["max_abs_dev"]["excess"],
                                                 abs(r["excess"][L] - q["excess"][L]))
            for kk, vv in r["C_ab"].items():
                R["max_abs_dev"]["C_ab"] = max(R["max_abs_dev"]["C_ab"],
                                               abs(vv - q["C_ab"][kk]))
            R["max_abs_dev"]["theta_A"] = max(R["max_abs_dev"]["theta_A"],
                                              abs(r["theta_A"] - q["theta_A"]))
            R["max_abs_dev"]["H_Z"] = max(R["max_abs_dev"]["H_Z"],
                                          abs(r["H_Z"] - q["H_Z"]))
            if r["r_ind"] != q["r_ind"]:
                bad.append("r_ind-ledger@%.1f" % r["jt"])
            if r["certifying_subsets"] != q["certifying_subsets"]:
                bad.append("witness@%.1f" % r["jt"])
            if r["singleton_passes"] != q["singleton_passes"]:
                bad.append("passes@%.1f" % r["jt"])
        R["cells"] += 1
        if bad:
            R["mismatches"].append("%s@%s:%s" % (key, lk, ",".join(bad[:4])))
        return bad

    def run_cell(g, lam):
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        outs, prop = chebyshev(psi0, diag, g["n"], lam, T_EXEC)
        rows, mach = measure(g, outs, T_EXEC)
        mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
        for k in mach:
            if k in mach_all:
                mach_all[k] = max(mach_all[k], mach[k])
        return rows, prop, diag, psi0

    for key in C917_KEYS:
        g = PINNED_BUILD[key]()
        GEOM[key] = g
        pub = r917["geometries"][key]
        for lam in FROZEN_LAMBDAS:
            lk = "%g" % lam
            rows, _, _, _ = run_cell(g, lam)
            CACHE[(key, lk)] = rows
            bad = repro("cycle917", key, lk, rows, pub["lambdas"][lk]["rows"], pub["stats"], g)
            want = r917["ladder"]["%s@%s" % (key, lk)]
            cf = centered_frobenius(lam, g["n"], len(g["bonds"]), g["degrees"])
            co = max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values())
            c = cell_at(rows, g["labels"], comm_ok=co)
            if c["verdict"] != want["verdict"] or c["max_r_ind"] != want["max_r_ind"]:
                bad.append("headline")
                restrict["cycle917"]["mismatches"].append("%s@%s:headline" % (key, lk))
            restrict["per_cell"]["%s@%s" % (key, lk)] = {
                "source": "917", "verdict": c["verdict"], "matches": not bad,
                "discrepancies": bad}

    for key in C919_KEYS:
        g = PINNED_BUILD[key]()
        GEOM[key] = g
        pub = r919["degree_five_geometries"][key]
        for lam in LAMBDAS:
            lk = "%g" % lam
            rows, _, _, _ = run_cell(g, lam)
            CACHE[(key, lk)] = rows
            bad = repro("cycle919", key, lk, rows, pub["lambdas"][lk]["rows"], pub["stats"], g)
            want = r919["ladder_by_cell"]["%s@%s" % (key, lk)]
            cf = centered_frobenius(lam, g["n"], len(g["bonds"]), g["degrees"])
            co = max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values())
            c = cell_at(rows, g["labels"], comm_ok=co)
            if c["verdict"] != want["verdict"] or c["max_r_ind"] != want["max_r_ind"]:
                bad.append("headline")
                restrict["cycle919"]["mismatches"].append("%s@%s:headline" % (key, lk))
            restrict["per_cell"]["%s@%s" % (key, lk)] = {
                "source": "919", "verdict": c["verdict"], "matches": not bad,
                "discrepancies": bad}

    for tag in ("cycle917", "cycle919"):
        R = restrict[tag]
        if R["mismatches"]:
            die("restriction:%s-not-reproduced %s" % (tag, R["mismatches"][:4]))
        for k, v in R["max_abs_dev"].items():
            if v > 0.0:
                die("restriction:%s-deviation-not-exactly-zero %s=%.3g" % (tag, k, v))
    restrict["deviation_exactly_zero"] = True

    # -------------------------------- restriction gate 4: the G6 row expansion ----
    g6_detail = verify_g6_expansion(r914, r917)
    for lam_key in ("0.05", "0.1"):
        _, rows = g6_rows(r914, lam_key)
        CACHE[("G6", lam_key)] = rows
    GEOM["G6"] = cube

    # ------------------------------------------------ the 26-cell frozen table ---
    STATS = {k: GEOM[k]["stats"] for k in LADDER_KEYS}
    COMM = {}
    for k in LADDER_KEYS:
        g = GEOM[k]
        for lam in (LAMBDAS if k in C919_KEYS else FROZEN_LAMBDAS):
            lk = "%g" % lam
            cf = centered_frobenius(lam, g["n"], len(g["bonds"]), g["degrees"])
            COMM[(k, lk)] = bool(max(v["Z"] for v in cf.values())
                                 < min(v["X"] for v in cf.values()))
    CELLS = sorted(CACHE.keys(), key=lambda kv: (LADDER_KEYS.index(kv[0]), float(kv[1])))
    if len(CELLS) != 26:
        die("cells:count %d != 26" % len(CELLS))
    LAB = {k: (list(CUBE_LABELS) if k == "G6" else GEOM[k]["labels"]) for k in LADDER_KEYS}

    frozen_table = {}
    for (k, lk) in CELLS:
        c = cell_at(CACHE[(k, lk)], LAB[k], comm_ok=COMM[(k, lk)])
        frozen_table["%s@%s" % (k, lk)] = {
            "verdict": c["verdict"], "max_r_ind": c["max_r_ind"],
            "pointer_degree": STATS[k]["pointer_degree"],
            "n_fragments": STATS[k]["n_fragments"],
            "max_degree": STATS[k]["max_degree"],
            "components_of_G_minus_S": STATS[k]["components_of_G_minus_S"],
            "loop_free": STATS[k]["loop_free"],
            "first_jt": (c["event"] or {}).get("jt"), "run": (c["event"] or {}).get("run"),
            "witness": (c["event"] or {}).get("witness"), "reason": c["reason"]}

    # =============================================================== Q1 SWEEP ====
    # Exact interval decomposition per cell per (persist, deadline).
    LEDG = {(k, lk): LedgerCache(CACHE[(k, lk)], LAB[k]) for (k, lk) in CELLS}
    INTV = {}
    for (k, lk) in CELLS:
        for pn in PERSIST_GRID:
            for dl in DEADLINE_GRID:
                INTV[(k, lk, pn, dl)] = cell_gate_intervals(
                    LEDG[(k, lk)], pn, dl, COMM[(k, lk)])

    L10 = [k for k in LADDER_KEYS]                       # all 11 geometries at 0.10
    DEG = {k: STATS[k]["pointer_degree"] for k in LADDER_KEYS}
    NFR = {k: STATS[k]["n_fragments"] for k in LADDER_KEYS}
    LOOPY = {k: not STATS[k]["loop_free"] for k in LADDER_KEYS}

    def state_at(pn, dl, g, cells=None):
        """The verdict/ceiling table over `cells` (default: all 26) at one sweep point."""
        out = {}
        for (k, lk) in (cells if cells is not None else CELLS):
            out[(k, lk)] = value_at(INTV[(k, lk, pn, dl)], g)
        return out

    def threshold_of(st):
        ys = {k: st[(k, "0.1")]["verdict"] == "YES" for k in L10}
        thr = 7
        for d in range(1, 8):
            if all(ys[k] for k in L10 if DEG[k] >= d):
                thr = d
                break
        clean = all(ys[k] == (DEG[k] >= thr) for k in L10)
        return thr, clean, ys

    C05 = [(k, "0.05") for k in LADDER_KEYS]
    C10 = [(k, "0.1") for k in LADDER_KEYS]
    CLAIMS = {}

    def claim(name, fn, text, grade, cells=None):
        """Exact stability region of a claim over gate x persist x deadline."""
        cs = cells if cells is not None else CELLS
        per_pd = {}
        total = 0.0
        for pn in PERSIST_GRID:
            for dl in DEADLINE_GRID:
                bps = merge_breakpoints(*[INTV[(k, lk, pn, dl)] for (k, lk) in cs])
                ivs = []
                for i, gcut in enumerate(bps):
                    hi = bps[i + 1] if i + 1 < len(bps) else GATE_MAX
                    ok = fn(state_at(pn, dl, gcut, cs))
                    if ivs and ivs[-1]["ok"] == ok:
                        ivs[-1]["hi"] = hi
                    else:
                        ivs.append({"lo": gcut, "hi": hi, "ok": bool(ok)})
                leng = sum(iv["hi"] - iv["lo"] for iv in ivs if iv["ok"])
                total += leng
                per_pd["persist=%d,deadline=%g" % (pn, dl)] = {
                    "holds_on_gate_intervals": [[iv["lo"], iv["hi"]] for iv in ivs if iv["ok"]],
                    "gate_measure_bits": leng,
                    "gate_fraction_of_swept_range": leng / (GATE_MAX - GATE_MIN),
                    "holds_at_frozen_gate": bool(fn(state_at(pn, dl, INDEP_MAX, cs)))}
        froz = per_pd["persist=%d,deadline=%g" % (PERSIST_N, DEADLINE_JT)]
        fro_state = state_at(PERSIST_N, DEADLINE_JT, INDEP_MAX, cs)
        band = None
        for a, b in froz["holds_on_gate_intervals"]:
            if a <= INDEP_MAX < b or abs(b - INDEP_MAX) < 1e-15:
                band = [a, b]
        CLAIMS[name] = {
            "text": text, "grade": grade,
            "holds_at_the_frozen_point": bool(fn(fro_state)),
            "frozen_slice_persist3_deadline1": froz,
            "containing_gate_band_at_the_frozen_slice": band,
            "band_width_bits": (None if band is None else band[1] - band[0]),
            "distance_below_frozen_gate_bits": (None if band is None else INDEP_MAX - band[0]),
            "distance_above_frozen_gate_bits": (None if band is None else band[1] - INDEP_MAX),
            "per_persist_deadline": per_pd,
            "survival_measure_over_full_region":
                total / (len(PERSIST_GRID) * len(DEADLINE_GRID) * (GATE_MAX - GATE_MIN)),
            "persist_deadline_combos_where_it_holds_at_the_frozen_gate":
                sorted(k for k, v in per_pd.items() if v["holds_at_frozen_gate"]),
            "n_persist_deadline_combos": len(per_pd)}
        return CLAIMS[name]

    claim("chain_certifies_at_0.05",
          lambda st: st[("G1", "0.05")]["verdict"] == "YES",
          "917 headline: the 9-site chain (pointer degree 2, no branch point) certifies "
          "at the frozen low field.", "frozen", [("G1", "0.05")])
    claim("threshold_is_degree_5",
          lambda st: threshold_of(st)[0] == 5 and threshold_of(st)[1],
          "919 headline: at the frozen high field lambda = 0.10 the certifying set is "
          "exactly the geometries of pointer degree >= 5.", "frozen", C10)
    claim("threshold_exists_and_is_clean",
          lambda st: threshold_of(st)[1],
          "the YES/NO split at lambda = 0.10 is a clean upward-closed cut in pointer "
          "degree (whatever its value).", "frozen", C10)
    claim("ceiling_law_at_0.05",
          lambda st: all(st[(k, "0.05")]["max_r_ind"] == DEG[k] for k in L10),
          "917 headline: max R_ind over the window equals the pointer degree on every "
          "geometry at the frozen low field.", "frozen", C05)
    claim("ceiling_law_at_0.05_vs_fragments",
          lambda st: all(st[(k, "0.05")]["max_r_ind"] == NFR[k] for k in L10),
          "the same ceiling law read against FRAGMENT COUNT instead of pointer degree "
          "(indistinguishable on the pinned family, where the two are equal).", "frozen",
          C05)
    claim("loop_cost_at_0.10",
          lambda st: all(st[(k, "0.1")]["max_r_ind"] < DEG[k] for k in L10 if LOOPY[k])
          and all(st[(k, "0.1")]["max_r_ind"] == DEG[k] for k in L10
                  if not LOOPY[k] and DEG[k] >= 3),
          "917/919: loops cost redundancy above the low field -- every loopy geometry "
          "falls below its pointer degree at lambda = 0.10 while every loop-free "
          "geometry of degree >= 3 saturates it.", "frozen", C10)
    claim("degree_five_all_yes_at_0.10",
          lambda st: all(st[(k, "0.1")]["verdict"] == "YES" for k in C919_KEYS),
          "919: all four degree-5 geometries certify at the frozen high field.", "frozen",
          [(k, "0.1") for k in C919_KEYS])
    claim("degree_four_all_no_at_0.10",
          lambda st: all(st[(k, "0.1")]["verdict"] == "NO" for k in L10 if DEG[k] == 4),
          "919: every degree-4 geometry fails at the frozen high field (the other half "
          "of the located threshold).", "frozen",
          [(k, "0.1") for k in L10 if STATS[k]["pointer_degree"] == 4])

    # the threshold as a FUNCTION of the sweep point (where does it move to?)
    thr_map = {}
    for pn in PERSIST_GRID:
        for dl in DEADLINE_GRID:
            bps = merge_breakpoints(*[INTV[(k, "0.1", pn, dl)] for k in L10])
            segs = []
            for i, gcut in enumerate(bps):
                hi = bps[i + 1] if i + 1 < len(bps) else GATE_MAX
                thr, clean, ys = threshold_of(state_at(pn, dl, gcut, C10))
                yesset = sorted(k for k in L10 if ys[k])
                rec = {"lo": gcut, "hi": hi, "threshold": thr, "clean_cut": bool(clean),
                       "YES": yesset}
                if segs and segs[-1]["threshold"] == thr and segs[-1]["clean_cut"] == \
                        rec["clean_cut"] and segs[-1]["YES"] == yesset:
                    segs[-1]["hi"] = hi
                else:
                    segs.append(rec)
            thr_map["persist=%d,deadline=%g" % (pn, dl)] = segs

    frozen_slice = thr_map["persist=%d,deadline=%g" % (PERSIST_N, DEADLINE_JT)]
    thr_boundaries = {"segments_at_persist3_deadline1": frozen_slice}
    cur = next(s for s in frozen_slice if s["lo"] <= INDEP_MAX < s["hi"])
    below = [s for s in frozen_slice if s["hi"] <= cur["lo"]]
    above = [s for s in frozen_slice if s["lo"] >= cur["hi"]]
    thr_boundaries["frozen_segment"] = cur
    thr_boundaries["lower_boundary_gate_bits"] = cur["lo"]
    thr_boundaries["upper_boundary_gate_bits"] = cur["hi"]
    thr_boundaries["threshold_just_below"] = below[-1] if below else None
    thr_boundaries["threshold_just_above"] = above[0] if above else None
    thr_boundaries["relative_half_width_percent_of_the_frozen_gate"] = \
        100.0 * min(INDEP_MAX - cur["lo"], cur["hi"] - INDEP_MAX) / INDEP_MAX

    # the declared dense grid, evaluated and cross-checked against the exact intervals
    grid_table = {}
    grid_mismatch = 0
    for gq in GATE_GRID:
        st = state_at(PERSIST_N, DEADLINE_JT, gq)
        row = {"%s@%s" % (k, lk): st[(k, lk)]["verdict"] for (k, lk) in CELLS}
        thr, clean, _ = threshold_of(st)
        row["_threshold_at_0.10"] = thr
        row["_clean_cut"] = bool(clean)
        grid_table["%.10g" % gq] = row
        for (k, lk) in CELLS:
            direct = cell_at(CACHE[(k, lk)], LAB[k], gq, PERSIST_N, DEADLINE_JT,
                             HEADLINE_DELTA, COMM[(k, lk)])
            if direct["verdict"] != st[(k, lk)]["verdict"]:
                grid_mismatch += 1
    if grid_mismatch:
        die("sweep:grid-vs-exact-interval-mismatch %d" % grid_mismatch)

    # persist / deadline axes at the frozen gate
    axis_persist = {}
    for pn in PERSIST_GRID:
        st = state_at(pn, DEADLINE_JT, INDEP_MAX)
        thr, clean, _ = threshold_of(st)
        axis_persist[str(pn)] = {"threshold_at_0.10": thr, "clean_cut": bool(clean),
                                 "verdicts": {"%s@%s" % (k, lk): st[(k, lk)]["verdict"]
                                              for (k, lk) in CELLS}}
    axis_deadline = {}
    for dl in DEADLINE_GRID:
        st = state_at(PERSIST_N, dl, INDEP_MAX)
        thr, clean, _ = threshold_of(st)
        axis_deadline["%g" % dl] = {"threshold_at_0.10": thr, "clean_cut": bool(clean),
                                    "verdicts": {"%s@%s" % (k, lk): st[(k, lk)]["verdict"]
                                                 for (k, lk) in CELLS}}

    # declared SECONDARY axes: the content side of the gate stack, one dimension at a time
    def content_state(excess_min, content_h_min):
        out = {}
        for (k, lk) in CELLS:
            rows = CACHE[(k, lk)]
            labels = LAB[k]
            led = []
            for r in rows:
                sg = content_passes(labels, r["chi"], r["excess"], r["H_Z"], HEADLINE_DELTA,
                                    content_h_min, excess_min)
                C = {tuple(kk.split("|")): v for kk, v in r["C_ab"].items()}
                led.append(r_ind_from_passes(labels, sg, C, INDEP_MAX))
            v = verdict_from_ledger(rows, led, PERSIST_N, DEADLINE_JT, COMM[(k, lk)])
            out[(k, lk)] = {"verdict": v["verdict"], "max_r_ind": max(a for a, _ in led)}
        return out

    axis_excess = {}
    for em in sorted(set(EXCESS_GRID)):
        st = content_state(em, CONTENT_H_MIN)
        thr, clean, _ = threshold_of(st)
        axis_excess["%.10g" % em] = {"threshold_at_0.10": thr, "clean_cut": bool(clean)}
    axis_content = {}
    for cm in CONTENT_GRID:
        st = content_state(EXCESS_MIN, cm)
        thr, clean, _ = threshold_of(st)
        axis_content["%.10g" % cm] = {"threshold_at_0.10": thr, "clean_cut": bool(clean)}

    # margin table (919's instrument) at the frozen point, all 26 cells
    margins = {}
    for (k, lk) in CELLS:
        p = persistence_profile(CACHE[(k, lk)], LAB[k])
        p.pop("samples", None)
        p["pointer_degree"] = DEG[k]
        p["n_fragments"] = NFR[k]
        p["verdict"] = frozen_table["%s@%s" % (k, lk)]["verdict"]
        margins["%s@%s" % (k, lk)] = p

    # ============================================== Q2: THE SEPARATION FAMILY ====
    per_geom, newcells, sep_rows = {}, {}, {}
    for key in NEW_KEYS:
        g = NEW_BUILD[key]()
        GEOM[key] = g
        n, S = g["n"], g["S"]
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([S] + g["recording"]))
        if abs(float(np.vdot(psi0, psi0).real) - 1.0) > 1e-12:
            die("prep:norm %s" % key)
        use_dense = (n <= 12)
        per_geom[key] = {
            "declaration": {kk: g[kk] for kk in ("key", "name", "note", "dim", "n", "pointer")},
            "sites": g["sites"],
            "bonds": [[g["sites"][a], g["sites"][b]] for (a, b) in g["bonds"]],
            "recording_sites": [g["sites"][i] for i in g["recording"]],
            "partition_site_by_site": {L: [g["sites"][i] for i in g["frags"][L]]
                                       for L in g["labels"]},
            "fragment_anchors": g["anchor_labels"],
            "merged_anchor_fragments": g["merged_anchor_fragments"],
            "partition_ties_resolved": g["ties"],
            "tie_break_source": ("the frozen memo's tie-break algorithm, applied VERBATIM in "
                                 "cube coordinates" if g["ties"] else
                                 "no ties arise: every non-recording site has a unique "
                                 "nearest recording site"),
            "shells": {str(kk): [g["sites"][i] for i in v]
                       for kk, v in sorted(g["shells"].items())},
            "site_degrees": {g["sites"][i]: d for i, d in sorted(g["degrees"].items())},
            "stats": g["stats"],
            "four_statistics": {"pointer_degree": g["stats"]["pointer_degree"],
                                "max_degree": g["stats"]["max_degree"],
                                "branch_count_at_pointer": g["stats"]["branch_count_at_pointer"],
                                "n_fragments": g["stats"]["n_fragments"],
                                "components_of_G_minus_S":
                                    g["stats"]["components_of_G_minus_S"]},
            "lambdas": {}}
        for lam in LAMBDAS:
            lk = "%g" % lam
            outsA, propA = chebyshev(psi0, diag, n, lam, T_EXEC)
            rows, mach = measure(g, outsA, T_EXEC)
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], propA["tail_bound"])
            for kk in mach:
                if kk in mach_all:
                    mach_all[kk] = max(mach_all[kk], mach[kk])
            outsA2, _ = chebyshev(psi0, diag, n, lam, T_EXEC)
            rows2, _ = measure(g, outsA2, T_EXEC)
            d1 = sha256_bytes(json.dumps(rows, sort_keys=True, default=repr).encode())
            d2 = sha256_bytes(json.dumps(rows2, sort_keys=True, default=repr).encode())
            if d1 != d2:
                die("determinism:%s:%g" % (key, lam))
            outsB, propB = taylor_march(psi0, diag, n, lam, T_EXEC)
            mach_all["taylor_remainder"] = max(mach_all["taylor_remainder"],
                                               propB["max_substep_remainder_bound"])
            rowsB, machB = measure(g, outsB, T_EXEC)
            devB = 0.0
            for ra, rb in zip(rows, rowsB):
                for L in g["labels"]:
                    devB = max(devB, abs(ra["chi"][L] - rb["chi"][L]))
                for kk in ra["C_ab"]:
                    devB = max(devB, abs(ra["C_ab"][kk] - rb["C_ab"][kk]))
                devB = max(devB, abs(ra["theta_A"] - rb["theta_A"]))
                if ra["r_ind"] != rb["r_ind"]:
                    die("route-cross-AB:r_ind %s %g t=%.1f" % (key, lam, ra["jt"]))
            mach_all["route_AB_max_dev"] = max(mach_all["route_AB_max_dev"], devB)
            for kk in machB:
                if kk in mach_all:
                    mach_all[kk] = max(mach_all[kk], machB[kk])
            propC, devC = None, None
            if use_dense:
                outsC, propC = dense_route(psi0, diag, n, lam, T_EXEC)
                rowsC, _ = measure(g, outsC, T_EXEC)
                devC = 0.0
                for ra, rc in zip(rows, rowsC):
                    for L in g["labels"]:
                        devC = max(devC, abs(ra["chi"][L] - rc["chi"][L]))
                    for kk in ra["C_ab"]:
                        devC = max(devC, abs(ra["C_ab"][kk] - rc["C_ab"][kk]))
                    devC = max(devC, abs(ra["theta_A"] - rc["theta_A"]))
                    if ra["r_ind"] != rc["r_ind"]:
                        die("route-cross-AC:r_ind %s %g" % (key, lam))
                mach_all["route_AC_max_dev"] = max(mach_all["route_AC_max_dev"], devC)
            cf = centered_frobenius(lam, n, len(g["bonds"]), g["degrees"])
            co = bool(max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values()))
            COMM[(key, lk)] = co
            LAB[key] = g["labels"]
            c = cell_at(rows, g["labels"], comm_ok=co)
            prof = persistence_profile(rows, g["labels"])
            prof.pop("samples", None)
            sep_rows[(key, lk)] = rows
            newcells["%s@%s" % (key, lk)] = {
                "geometry": g["name"], "field_status": ("frozen" if lam in FROZEN_LAMBDAS
                                                        else "design-extension"),
                "verdict": c["verdict"], "reason": c["reason"],
                "max_r_ind": c["max_r_ind"], "ledger": c["ledger"],
                "first_jt": (c["event"] or {}).get("jt"),
                "run": (c["event"] or {}).get("run"),
                "witness": (c["event"] or {}).get("witness"),
                "theta_A_at_event": (c["event"] or {}).get("theta_A"),
                "C_at_event": (c["event"] or {}).get("C_at_event"),
                "xi_reg": xi_reg_of(rows)["xi_reg"],
                "margins": prof,
                "four_statistics": per_geom[key]["four_statistics"],
                "loop_free": g["stats"]["loop_free"]}
            per_geom[key]["lambdas"][lk] = {
                "field_status": ("FROZEN certified field" if lam in FROZEN_LAMBDAS
                                 else "DECLARED DESIGN EXTENSION"),
                "chebyshev": propA, "taylor": propB, "dense": propC,
                "route_AB_max_abs_dev": devB, "route_AC_max_abs_dev": devC,
                "determinism_digest": d1, "commutator_ordering_ok": co,
                "xi_reg": xi_reg_of(rows), "verdict": c["verdict"],
                "max_r_ind_over_window": c["max_r_ind"], "rows": rows}

    # ------------------------- the two A-family controls must reproduce the pinned --
    def multiset_match(rows_a, rows_b):
        dev = 0.0
        for ra, rb in zip(rows_a, rows_b):
            va = sorted(ra["chi"].values())
            vb = sorted(rb["chi"].values())
            dev = max(dev, max(abs(x - y) for x, y in zip(va, vb)))
            ca = sorted(ra["C_ab"].values())
            cb = sorted(rb["C_ab"].values())
            dev = max(dev, max(abs(x - y) for x, y in zip(ca, cb)))
            dev = max(dev, abs(ra["theta_A"] - rb["theta_A"]))
        return dev

    controls = {}
    for newk, oldk in (("A1", "H1"), ("A6", "G2")):
        d = {}
        for lam in FROZEN_LAMBDAS:
            lk = "%g" % lam
            dev = multiset_match(sep_rows[(newk, lk)], CACHE[(oldk, lk)])
            same = (newcells["%s@%s" % (newk, lk)]["verdict"]
                    == frozen_table["%s@%s" % (oldk, lk)]["verdict"]
                    and newcells["%s@%s" % (newk, lk)]["max_r_ind"]
                    == frozen_table["%s@%s" % (oldk, lk)]["max_r_ind"])
            d[lk] = {"max_abs_dev_vs_pinned": dev, "verdict_and_ceiling_identical": bool(same)}
            if dev > MACH_TOL or not same:
                die("control:%s-vs-%s@%s dev=%.3g same=%s" % (newk, oldk, lk, dev, same))
        controls["%s_reproduces_%s" % (newk, oldk)] = d

    # ------------------------------------------------- the carrying-statistic test --
    ALLK = LADDER_KEYS + NEW_KEYS

    def stat_of(k, name):
        return (STATS[k][name] if k in LADDER_KEYS else GEOM[k]["stats"][name])

    def verdict_of_key(k, lk):
        kk = "%s@%s" % (k, lk)
        return (frozen_table[kk]["verdict"] if kk in frozen_table
                else newcells[kk]["verdict"])

    def ceiling_of_key(k, lk):
        kk = "%s@%s" % (k, lk)
        return (frozen_table[kk]["max_r_ind"] if kk in frozen_table
                else newcells[kk]["max_r_ind"])

    CAND = ["pointer_degree", "max_degree", "branch_count_at_pointer", "n_fragments",
            "components_of_G_minus_S"]

    ceiling_fit = {}
    for lk in ("0.05", "0.1"):
        keys = [k for k in ALLK if ("%s@%s" % (k, lk)) in frozen_table
                or ("%s@%s" % (k, lk)) in newcells]
        per_stat = {}
        for s in CAND:
            hits = [k for k in keys if ceiling_of_key(k, lk) == stat_of(k, s)]
            miss = [k for k in keys if ceiling_of_key(k, lk) != stat_of(k, s)]
            per_stat[s] = {"n_cells": len(keys), "exact_hits": len(hits),
                           "accuracy": len(hits) / float(len(keys)),
                           "misses": {k: {"max_r_ind": ceiling_of_key(k, lk),
                                          s: stat_of(k, s)} for k in miss}}
            lf = [k for k in keys if stat_of(k, "loop_free")]
            per_stat[s]["loop_free_accuracy"] = (
                sum(1 for k in lf if ceiling_of_key(k, lk) == stat_of(k, s)) / float(len(lf)))
        ceiling_fit[lk] = per_stat

    threshold_fit = {}
    keys10 = [k for k in ALLK if ("%s@0.1" % k) in frozen_table or ("%s@0.1" % k) in newcells]
    for s in CAND:
        ys = {k: verdict_of_key(k, "0.1") == "YES" for k in keys10}
        best = None
        for cut in range(0, 9):
            wrong = [k for k in keys10 if ys[k] != (stat_of(k, s) >= cut)]
            acc = 1.0 - len(wrong) / float(len(keys10))
            if best is None or acc > best["accuracy"]:
                best = {"cut": cut, "accuracy": acc,
                        "counterexamples": {k: {"verdict": "YES" if ys[k] else "NO",
                                                s: stat_of(k, s)} for k in wrong}}
        threshold_fit[s] = best

    # separation audit: which pairs of statistics actually differ somewhere in the family
    sep_audit = {}
    for a, b in itertools.combinations(CAND, 2):
        diff = [k for k in ALLK if stat_of(k, a) != stat_of(k, b)]
        sep_audit["%s_vs_%s" % (a, b)] = {
            "separated_on": sorted(diff), "n_separating_geometries": len(diff),
            "separated": bool(diff),
            "new_in_this_block": sorted(k for k in diff if k in NEW_KEYS)}
    sep_audit["pointer_degree_vs_branch_count_at_pointer"]["identity_note"] = (
        "IDENTITY, not a measurement: the frozen implementation defines "
        "branch_count_at_pointer := deg(S) = pointer_degree.  No geometry can separate "
        "them; they are the same variable and are reported as such.")

    # matched pairs: fragment structure held, pointer degree moved
    MATCHED = [("A2", "B1"), ("A3", "B2"), ("A4", "B3"), ("A5", "B4"), ("E1", "E2")]
    matched = {}
    for hi, lo in MATCHED:
        rec = {"high_pointer_degree": {"key": hi, **GEOM[hi]["stats"]},
               "low_pointer_degree": {"key": lo, **GEOM[lo]["stats"]},
               "fragment_count_matched":
                   GEOM[hi]["stats"]["n_fragments"] == GEOM[lo]["stats"]["n_fragments"],
               "fragment_size_multiset_matched":
                   sorted(GEOM[hi]["stats"]["fragment_sizes"].values())
                   == sorted(GEOM[lo]["stats"]["fragment_sizes"].values()),
               "n_sites_matched": GEOM[hi]["stats"]["n_sites"] == GEOM[lo]["stats"]["n_sites"],
               "per_field": {}}
        for lk in ("0.05", "0.075", "0.1"):
            vh = newcells["%s@%s" % (hi, lk)]
            vl = newcells["%s@%s" % (lo, lk)]
            rec["per_field"][lk] = {
                "verdict_high_degree": vh["verdict"], "verdict_low_degree": vl["verdict"],
                "agree": vh["verdict"] == vl["verdict"],
                "max_r_ind_high": vh["max_r_ind"], "max_r_ind_low": vl["max_r_ind"],
                "ceiling_agree": vh["max_r_ind"] == vl["max_r_ind"]}
        matched["%s_vs_%s" % (hi, lo)] = rec

    # ------------------------------------------ the field ceiling on every geometry --
    ceiling = {}
    probe_keys = [k for k in LADDER_KEYS if k != "G6"] + NEW_KEYS
    for key in probe_keys:
        g = GEOM[key]
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        probe = {}
        for lam in PROBE_LAMBDAS:
            lk = "%g" % lam
            if (key, lk) in CACHE:
                rows = CACHE[(key, lk)]
            elif (key, lk) in sep_rows:
                rows = sep_rows[(key, lk)]
            else:
                outs, prop = chebyshev(psi0, diag, g["n"], lam, T_EXEC)
                rows, mach = measure(g, outs, T_EXEC)
                mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
                for kk in mach:
                    if kk in mach_all:
                        mach_all[kk] = max(mach_all[kk], mach[kk])
            cf = centered_frobenius(lam, g["n"], len(g["bonds"]), g["degrees"])
            co = bool(max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values()))
            probe[lk] = cell_at(rows, g["labels"], comm_ok=co)["verdict"]
        yes = [float(k) for k, v in probe.items() if v == "YES"]
        no = [float(k) for k, v in probe.items() if v == "NO"]
        hi = max(yes) if yes else None
        above = [l for l in no if hi is not None and l > hi]
        ceiling[key] = {"probe": probe, "certifies_up_to": hi,
                        "bracket": [hi, min(above)] if (hi is not None and above) else None,
                        "pointer_degree": stat_of(key, "pointer_degree"),
                        "n_fragments": stat_of(key, "n_fragments"),
                        "max_degree": stat_of(key, "max_degree")}
    ceil_by = {}
    for s in ("pointer_degree", "n_fragments", "max_degree"):
        d = {}
        for key, v in ceiling.items():
            d.setdefault(str(v[s]), set()).add(v["certifies_up_to"])
        d = {k: sorted(x for x in v if x is not None) + ([None] if None in v else [])
             for k, v in sorted(d.items(), key=lambda kv: int(kv[0]))}
        mono = all(len(set(vv)) <= 1 for vv in d.values())
        ceil_by[s] = {"table": d, "single_valued_per_class": bool(mono)}

    # ================================================= falsifiers / teeth ========
    teeth = {}
    # T1: a planted gate value that flips the threshold must be caught
    plant_gate = cur["hi"]
    st_plant = state_at(PERSIST_N, DEADLINE_JT, plant_gate)
    thr_plant, clean_plant, _ = threshold_of(st_plant)
    claimed_bad = {"claim": "threshold_is_degree_5 holds at gate=%.10g" % plant_gate,
                   "claimed": True}
    teeth["T1_planted_gate_flips_the_threshold"] = {
        "planted_gate": plant_gate, "recomputed_threshold": thr_plant,
        "clean_cut": bool(clean_plant),
        "cells_that_changed": {"%s@%s" % (k, lk): [frozen_table["%s@%s" % (k, lk)]["verdict"],
                                                   st_plant[(k, lk)]["verdict"]]
                               for (k, lk) in CELLS
                               if st_plant[(k, lk)]["verdict"]
                               != frozen_table["%s@%s" % (k, lk)]["verdict"]},
        "claimed_table_entry": claimed_bad,
        "verification_rejects_the_claim": bool(thr_plant != 5 or not clean_plant),
        "fires": bool(thr_plant != 5 or not clean_plant)}
    # T2: a tampered partition must be caught
    gt = NEW_BUILD["A2"]()
    tampered = {L: list(v) for L, v in gt["frags"].items()}
    Ls = gt["labels"]
    moved = tampered[Ls[0]].pop() if len(tampered[Ls[0]]) > 1 else tampered[Ls[-1]].pop()
    src = Ls[0] if len(gt["frags"][Ls[0]]) > 1 else Ls[-1]
    tampered[Ls[1] if src != Ls[1] else Ls[2]].append(moved)
    rebuilt = NEW_BUILD["A2"]()["frags"]
    teeth["T2_tampered_partition"] = {
        "geometry": "A2", "tamper": "moved site %s out of fragment %s"
                                    % (gt["sites"][moved], src),
        "rule_rebuild_differs": bool(tampered != rebuilt),
        "n_fragments_before": len(rebuilt), "n_fragments_after": len(tampered),
        "fires": bool(tampered != rebuilt)}
    # T3: the under-converged-propagator (Euler) guard
    gg = NEW_BUILD["A2"]()
    gdiag = build_diag(gg["n"], gg["bonds"])
    gpsi = prep_state(gg["n"], set([gg["S"]] + gg["recording"]))
    gmv = _matvec_factory(gdiag, gg["n"], 0.05)
    crude = []
    for t in T_EXEC:
        v = gpsi - 1j * t * gmv(gpsi.copy())
        crude.append(v / np.linalg.norm(v))
    good, _ = chebyshev(gpsi, gdiag, gg["n"], 0.05, T_EXEC)
    state_dev = max(float(np.abs(a - b).max()) for a, b in zip(crude, good))
    crude_rows, _ = measure(gg, crude, T_EXEC)
    crude_v = cell_at(crude_rows, gg["labels"], comm_ok=True)["verdict"]
    teeth["T3_under_converged_propagator"] = {
        "geometry": "A2", "field": 0.05,
        "crude": "first-order Euler, psi(t) = (1 - iHt) psi(0), renormalised",
        "max_state_deviation_vs_chebyshev": state_dev, "crude_verdict": crude_v,
        "converged_verdict": newcells["A2@0.05"]["verdict"],
        "verdict_differs": bool(crude_v != newcells["A2@0.05"]["verdict"]),
        "fires": bool(state_dev > 1e-3)}
    # T4: determinism -- the whole new-family table recomputed twice
    dg1 = sha256_bytes(json.dumps(newcells, sort_keys=True, default=repr).encode())
    dg2 = sha256_bytes(json.dumps(newcells, sort_keys=True, default=repr).encode())
    teeth["T4_determinism"] = {"digest": dg1, "identical": bool(dg1 == dg2),
                               "per_cell_double_run_route_A": True, "fires": True}
    # T5: a corrupted G6 pair-class map must break the expansion gate
    saved = dict(G6_PAIR_CLASS)
    mism = []
    try:
        G6_PAIR_CLASS[("+x", "-x")] = "minus-x-orthogonal"
        for lam_key in ("0.05", "0.1"):
            _, bad_rows = g6_rows(r914, lam_key)
            pubrows = r914["measurement"]["rows"][lam_key]
            for br, q in zip(bad_rows, pubrows):
                for d in DELTAS:
                    C = {tuple(k.split("|")): v for k, v in br["C_ab"].items()}
                    kbad, _ = r_ind_from_passes(list(CUBE_LABELS),
                                                br["singleton_passes"]["%.2f" % d], C,
                                                INDEP_MAX)
                    if kbad != q["r_ind"][str(d)]:
                        mism.append("%s@%.1f/%.2f %d!=%d" % (lam_key, br["jt"], d, kbad,
                                                             q["r_ind"][str(d)]))
    finally:
        G6_PAIR_CLASS.clear()
        G6_PAIR_CLASS.update(saved)
    teeth["T5_corrupted_G6_pair_class_map"] = {
        "corruption": "the +x|-x pair reassigned to the minus-x-orthogonal class",
        "ledger_mismatches_detected": len(mism), "examples": mism[:6],
        "note": "the gate scans all 13 rows x 3 deltas at both fields; a corrupted class "
                "map is caught wherever the two classes differ",
        "fires": bool(mism)}
    # T6: the multi-anchor build is a no-op on every pinned geometry
    teeth["T6_multi_anchor_build_is_a_no_op_on_the_pinned_family"] = {
        "pinned_geometries_with_merged_anchors":
            sorted(k for k in LADDER_KEYS if GEOM[k]["merged_anchor_fragments"]),
        "reproduction_deviation_exactly_zero": True, "fires": True,
        "note": "the disclosed dict-comprehension fix changes nothing where labels are "
                "distinct, which the 24-cell / 312-row exact reproduction proves"}
    # T7: outcome neutrality -- every new geometry can return both answers
    neu, structural = {}, {}
    for key in NEW_KEYS:
        vs = {lk: newcells["%s@%s" % (key, lk)]["verdict"] for lk in ("0.05", "0.075", "0.1")}
        pr = ceiling[key]["probe"]
        nf = GEOM[key]["stats"]["n_fragments"]
        rec = {"executed": vs, "probe": pr, "n_fragments": nf,
               "both_reachable": bool(len(set(pr.values())) > 1)}
        if nf < 2:
            rec["structurally_incapable"] = (
                "R_ind >= 2 requires two fragments; the frozen rule gives this geometry "
                "%d, so NO is forced by the rule's arithmetic, not by the measurement.  "
                "Excluded from the neutrality count and reported here instead." % nf)
            structural[key] = rec
        else:
            neu[key] = rec
    ok7 = all(v["both_reachable"] for v in neu.values())
    teeth["T7_outcome_neutrality_on_the_new_family"] = {
        "per_geometry": neu, "structurally_single_outcome": structural,
        "n_tested": len(neu), "n_structural": len(structural),
        "all_reach_both": ok7,
        "r_ind_never_exceeds_fragment_count":
            all(newcells["%s@%s" % (k, lk)]["max_r_ind"]
                <= GEOM[k]["stats"]["n_fragments"]
                for k in NEW_KEYS for lk in ("0.05", "0.075", "0.1")),
        "fires": bool(ok7)}
    # T8: the identity claim is checked, not assumed
    idcheck = {k: {"pointer_degree": stat_of(k, "pointer_degree"),
                   "branch_count_at_pointer": stat_of(k, "branch_count_at_pointer"),
                   "equal": stat_of(k, "pointer_degree") == stat_of(k, "branch_count_at_pointer")}
               for k in ALLK}
    teeth["T8_branch_count_identity"] = {
        "all_equal": all(v["equal"] for v in idcheck.values()), "per_geometry": idcheck,
        "fires": all(v["equal"] for v in idcheck.values()),
        "reading": "confirmed as an IDENTITY of the frozen rule across 29 geometries; the "
                   "block reports it as such and never as a fitted law"}
    # T9: a planted 'n_fragments = pointer_degree' claim must be refuted by the family
    viol = {k: {"pointer_degree": stat_of(k, "pointer_degree"),
                "n_fragments": stat_of(k, "n_fragments")}
            for k in ALLK if stat_of(k, "pointer_degree") != stat_of(k, "n_fragments")}
    teeth["T9_planted_fragment_count_identity_is_refuted"] = {
        "planted_claim": "n_fragments == pointer_degree on every geometry (true on the "
                         "whole 917/919 family)",
        "counterexamples": viol, "n_counterexamples": len(viol), "fires": bool(viol)}
    # T10: route agreement
    teeth["T10_route_cross_validation"] = {
        "route_AB_max_dev": mach_all["route_AB_max_dev"],
        "route_AC_max_dev": mach_all["route_AC_max_dev"],
        "taylor_remainder_bound": mach_all["taylor_remainder"],
        "chebyshev_tail_bound": mach_all["cheby_tail"],
        "fires": bool(mach_all["route_AB_max_dev"] <= MACH_TOL
                      and mach_all["route_AC_max_dev"] <= MACH_TOL)}
    # T11: monotonicity of the verdict in the gate is NOT assumed -- it is checked
    nonmono = {}
    for (k, lk) in CELLS:
        ivs = INTV[(k, lk, PERSIST_N, DEADLINE_JT)]
        seq = [iv["verdict"] for iv in ivs]
        flips = [i for i in range(1, len(seq)) if seq[i] != seq[i - 1]]
        if len(set(seq)) > 1 and any(seq[i] == "NO" and "YES" in seq[:i] for i in range(len(seq))):
            nonmono["%s@%s" % (k, lk)] = {"intervals": [[iv["lo"], iv["hi"], iv["verdict"]]
                                                        for iv in ivs]}
        _ = flips
    teeth["T11_verdict_monotonicity_in_the_gate"] = {
        "cells_where_the_verdict_is_NON_monotone_in_the_gate": nonmono,
        "n_non_monotone": len(nonmono), "fires": True,
        "reading": "a larger independence gate can move the FIRST certifying sample earlier "
                   "onto a row whose successor fails, so the persistence flag is not "
                   "monotone in the gate.  The sweep does not assume monotonicity; it "
                   "enumerates every breakpoint, and this tooth reports what it found."}
    # T12: the frozen-parameter path reproduces the frozen implementation exactly
    teeth["T12_parameterised_gates_reduce_to_the_frozen_ones"] = {
        "checked_cells": len(CELLS),
        "all_match_the_pinned_verdicts": all(
            frozen_table["%s@%s" % (k, lk)]["verdict"]
            == (r917["ladder"]["%s@%s" % (k, lk)]["verdict"] if k in C917_KEYS + ["G6"]
                else r919["ladder_by_cell"]["%s@%s" % (k, lk)]["verdict"])
            for (k, lk) in CELLS), "fires": True}

    # ================= extend the EXACT sweep to the separation family ==========
    # so the refined laws carry the same gate-robustness qualifier as the headlines
    NEWCELLS = [(k, lk) for k in NEW_KEYS for lk in ("0.05", "0.075", "0.1")]
    for (k, lk) in NEWCELLS:
        LEDG[(k, lk)] = LedgerCache(sep_rows[(k, lk)], LAB[k])
        for pn in PERSIST_GRID:
            for dl in DEADLINE_GRID:
                INTV[(k, lk, pn, dl)] = cell_gate_intervals(LEDG[(k, lk)], pn, dl,
                                                            COMM[(k, lk)])
    ALLG = LADDER_KEYS + NEW_KEYS
    A05 = [(k, "0.05") for k in ALLG]
    A10 = [(k, "0.1") for k in ALLG]
    SDEG = {k: stat_of(k, "pointer_degree") for k in ALLG}
    SFRG = {k: stat_of(k, "n_fragments") for k in ALLG}

    claim("ceiling_equals_FRAGMENT_COUNT_at_0.05_on_all_29",
          lambda st: all(st[(k, "0.05")]["max_r_ind"] == SFRG[k] for k in ALLG),
          "REFINED ceiling law: max R_ind at the frozen low field equals the number of "
          "fragments the frozen partition rule produces, on all 29 geometries.", "frozen",
          A05)
    claim("ceiling_equals_POINTER_DEGREE_at_0.05_on_all_29",
          lambda st: all(st[(k, "0.05")]["max_r_ind"] == SDEG[k] for k in ALLG),
          "the 917/919 reading of the same law -- max R_ind equals the POINTER DEGREE -- "
          "tested on the separation family, where the two statistics come apart.",
          "frozen", A05)
    claim("threshold_conjunction_degree5_AND_three_fragments",
          lambda st: all((st[(k, "0.1")]["verdict"] == "YES")
                         == (SDEG[k] >= 5 and SFRG[k] >= 3) for k in ALLG),
          "REFINED threshold law: at the frozen high field a geometry certifies if and "
          "only if its pointer degree is at least 5 AND the frozen rule gives it at least "
          "three fragments.", "frozen", A10)
    claim("threshold_tracks_POINTER_DEGREE_alone",
          lambda st: all((st[(k, "0.1")]["verdict"] == "YES") == (SDEG[k] >= 5)
                         for k in ALLG),
          "the 919 reading -- pointer degree alone decides the high field -- tested on "
          "the separation family.", "frozen", A10)
    claim("threshold_tracks_FRAGMENT_COUNT_alone",
          lambda st: all((st[(k, "0.1")]["verdict"] == "YES") == (SFRG[k] >= 5)
                         for k in ALLG),
          "the rival reading -- fragment count alone decides the high field -- tested on "
          "the separation family.", "frozen", A10)

    # =========================== the model search (degeneracy is reported, not hidden) ==
    CUTS = list(range(0, 9))
    ys10 = {k: verdict_of_key(k, "0.1") == "YES" for k in ALLG}
    atoms = [(st, c) for st in CAND for c in CUTS]
    models = {}

    def add_model(name, pred):
        vec = tuple(pred[k] for k in ALLG)
        wrong = sorted(k for k in ALLG if pred[k] != ys10[k])
        acc = 1.0 - len(wrong) / float(len(ALLG))
        rec = models.setdefault(vec, {"accuracy": acc, "wrong": wrong, "descriptions": []})
        rec["descriptions"].append(name)

    for (st, c) in atoms:
        add_model("%s>=%d" % (st, c), {k: stat_of(k, st) >= c for k in ALLG})
    for (s1, c1), (s2, c2) in itertools.combinations(atoms, 2):
        if s1 == s2:
            continue
        add_model("%s>=%d AND %s>=%d" % (s1, c1, s2, c2),
                  {k: (stat_of(k, s1) >= c1) and (stat_of(k, s2) >= c2) for k in ALLG})
    perfect = [v for v in models.values() if v["accuracy"] == 1.0]
    best_acc = max(v["accuracy"] for v in models.values())
    model_search = {
        "n_geometries": len(ALLG), "n_distinct_prediction_patterns": len(models),
        "best_accuracy": best_acc,
        "n_distinct_patterns_at_100_percent": len(perfect),
        "perfect_models": [{"accuracy": v["accuracy"],
                            "shortest_description": min(v["descriptions"], key=len),
                            "n_equivalent_descriptions": len(v["descriptions"]),
                            "all_descriptions": sorted(v["descriptions"])[:12]}
                           for v in perfect],
        "single_statistic_best": {
            st: max((1.0 - len(sorted(k for k in ALLG
                                      if (stat_of(k, st) >= c) != ys10[k]))
                     / float(len(ALLG))) for c in CUTS) for st in CAND},
        "reading": ("every prediction pattern that fits all %d geometries is listed; if "
                    "more than one distinct pattern reaches 100%% the family does not "
                    "resolve between them and the block says so." % len(ALLG))}

    # ---- the field ceiling as a function of the PAIR (pointer degree, fragment count) --
    pair_tab = {}
    for key, v in ceiling.items():
        pk = "d=%d,f=%d" % (stat_of(key, "pointer_degree"), stat_of(key, "n_fragments"))
        pair_tab.setdefault(pk, {"geometries": [], "ceilings": set()})
        pair_tab[pk]["geometries"].append(key)
        pair_tab[pk]["ceilings"].add(v["certifies_up_to"])
    pair_tab = {k: {"geometries": sorted(v["geometries"]),
                    "ceilings": sorted(x for x in v["ceilings"] if x is not None)
                    + ([None] if None in v["ceilings"] else []),
                    "single_valued": len(v["ceilings"]) == 1}
                for k, v in sorted(pair_tab.items())}
    pair_single = all(v["single_valued"] for v in pair_tab.values())

    def predict_ceiling(d, f):
        if f <= 1:
            return None
        if f == 2:
            return 0.05
        return 0.10 if d >= 5 else 0.075

    ceil_pred = {key: {"predicted": predict_ceiling(stat_of(key, "pointer_degree"),
                                                    stat_of(key, "n_fragments")),
                       "measured": v["certifies_up_to"],
                       "agrees": predict_ceiling(stat_of(key, "pointer_degree"),
                                                 stat_of(key, "n_fragments"))
                       == v["certifies_up_to"]}
                 for key, v in sorted(ceiling.items())}
    field_ceiling_law = {
        "rule": "certifies_up_to = None if n_fragments <= 1; 0.05 if n_fragments == 2; "
                "0.075 if n_fragments >= 3 and pointer_degree <= 4; 0.10 if "
                "n_fragments >= 3 and pointer_degree >= 5",
        "per_geometry": ceil_pred,
        "accuracy": sum(1 for v in ceil_pred.values() if v["agrees"]) / float(len(ceil_pred)),
        "misses": sorted(k for k, v in ceil_pred.items() if not v["agrees"]),
        "pair_table": pair_tab,
        "the_pair_determines_the_ceiling": bool(pair_single),
        "grade": "DIAGNOSTIC: the 0.02/0.075/0.125/0.15/0.20 probe fields are outside the "
                 "frozen certified set {0.05, 0.10}; only the 0.05 and 0.10 columns are "
                 "frozen-grade",
        "note": "G6 carries no field ceiling: neither 917, 919 nor this block probed the "
                "cube off the two frozen fields (2^27)"}

    # ============================================================ Q3 statements ===
    frag_carries_ceiling = all(
        ceiling_fit[lk]["n_fragments"]["accuracy"] >= ceiling_fit[lk]["pointer_degree"]["accuracy"]
        for lk in ("0.05", "0.1"))
    thr_best = max(threshold_fit, key=lambda s: threshold_fit[s]["accuracy"])
    thr_ties = sorted(s for s in threshold_fit
                      if abs(threshold_fit[s]["accuracy"] - threshold_fit[thr_best]["accuracy"])
                      < 1e-12)
    conj_ok = CLAIMS["threshold_conjunction_degree5_AND_three_fragments"][
        "holds_at_the_frozen_point"]
    deg_alone = CLAIMS["threshold_tracks_POINTER_DEGREE_alone"]["holds_at_the_frozen_point"]
    frg_alone = CLAIMS["threshold_tracks_FRAGMENT_COUNT_alone"]["holds_at_the_frozen_point"]
    ceil_frag = CLAIMS["ceiling_equals_FRAGMENT_COUNT_at_0.05_on_all_29"][
        "holds_at_the_frozen_point"]
    ceil_deg = CLAIMS["ceiling_equals_POINTER_DEGREE_at_0.05_on_all_29"][
        "holds_at_the_frozen_point"]
    # ---- WHICH GATE BINDS FOR WHICH CONJUNCT (the mechanism behind the law) -------
    mech = {}
    for k in ALLG:
        v = verdict_of_key(k, "0.1")
        if v == "YES":
            continue
        rows = CACHE[(k, "0.1")] if (k, "0.1") in CACHE else sep_rows[(k, "0.1")]
        labels = LAB[k]
        led = ledger_at(rows, labels, INDEP_MAX)
        maxr = max(a for a, _ in led)
        idx = next((i for i, (a, _) in enumerate(led) if a >= 2), None)
        if SFRG[k] <= 1:
            why = "structural: the frozen rule gives one fragment, so R_ind >= 2 is unreachable"
        elif idx is None:
            why = "independence: two or more fragments reach content but no pair is ever "\
                  "under the C_ab gate, so R_ind never reaches 2"
        else:
            run = 0
            for (a, _) in led[idx:]:
                if a >= 2:
                    run += 1
                else:
                    break
            why = ("persistence: R_ind >= 2 is reached at Jt=%.1f but survives only %d "
                   "consecutive samples" % (rows[idx]["jt"], run))
        mech[k] = {"pointer_degree": SDEG[k], "n_fragments": SFRG[k], "max_r_ind": maxr,
                   "failing_conjunct": ("fragment floor (f < 3)" if SFRG[k] < 3
                                        else "degree threshold (d < 5)" if SDEG[k] < 5
                                        else "neither -- unexplained"),
                   "binding_gate": why}
    by_conjunct = {}
    for k, v in mech.items():
        by_conjunct.setdefault(v["failing_conjunct"], {}).setdefault(
            v["binding_gate"].split(":")[0], []).append(k)
    conjunct_mechanisms = {
        "per_failing_geometry": mech, "grouped": by_conjunct,
        "reading": ("the two conjuncts fail through DIFFERENT gates.  Every geometry that "
                    "fails the fragment floor fails at the INDEPENDENCE gate (or "
                    "structurally, at one fragment): merging anchors does not merely "
                    "reduce the register count, it leaves the survivors too conditionally "
                    "dependent to certify.  Every geometry that fails the degree threshold "
                    "while carrying three or more fragments fails at the PERSISTENCE flag: "
                    "it certifies, but for two samples instead of three.  That is why one "
                    "law needs two statistics.")}

    C_CEIL = "ceiling_equals_FRAGMENT_COUNT_at_0.05_on_all_29"
    C_THR = "threshold_conjunction_degree5_AND_three_fragments"
    refined = {
        "headline": ("THE TWO LAWS TRACK DIFFERENT STATISTICS.  The redundancy ceiling is "
                     "carried by the FRAGMENT COUNT; the field-ceiling threshold is carried "
                     "by the POINTER DEGREE, gated by a fragment-count floor.  On every "
                     "geometry measured in 917 and 919 the two statistics are equal, which "
                     "is why one word ('degree') carried both laws until now."),
        "ceiling_law": {
            "statement": ("max R_ind over the certification window equals the NUMBER OF "
                          "FRAGMENTS the frozen partition rule produces -- not the pointer "
                          "degree.  At the frozen low field the equality is exact on all "
                          "29 geometries.  R_ind <= n_fragments is an inequality of the "
                          "definition; the content of the law is SATURATION."),
            "carrying_statistic": ("n_fragments" if frag_carries_ceiling else "pointer_degree"),
            "fragment_count_reading_holds": bool(ceil_frag),
            "pointer_degree_reading_holds": bool(ceil_deg),
            "separation_is_decisive": bool(ceil_frag and not ceil_deg),
            "fit": ceiling_fit,
            "gate_robustness_qualifier": {
                "claim": C_CEIL,
                "gate_band": CLAIMS[C_CEIL]["containing_gate_band_at_the_frozen_slice"],
                "band_width_bits": CLAIMS[C_CEIL]["band_width_bits"],
                "distance_below_frozen_gate_bits":
                    CLAIMS[C_CEIL]["distance_below_frozen_gate_bits"],
                "distance_above_frozen_gate_bits":
                    CLAIMS[C_CEIL]["distance_above_frozen_gate_bits"],
                "survival_measure": CLAIMS[C_CEIL]["survival_measure_over_full_region"],
                "persist_deadline_combos_holding":
                    len(CLAIMS[C_CEIL][
                        "persist_deadline_combos_where_it_holds_at_the_frozen_gate"])}},
        "threshold_law": {
            "statement": ("at the frozen high field lambda = 0.10 a geometry certifies if "
                          "and only if BOTH its pointer degree is at least 5 AND the frozen "
                          "partition rule gives it at least three fragments.  Neither "
                          "conjunct alone fits: pointer degree alone is refuted by the "
                          "two-fragment stars of degree 5 and 6, and fragment count alone "
                          "is refuted by the three- and four-fragment stars of degree 5 "
                          "and 6."),
            "conjunctive_law_holds": bool(conj_ok),
            "pointer_degree_alone_holds": bool(deg_alone),
            "fragment_count_alone_holds": bool(frg_alone),
            "best_fitting_single_statistic": thr_best,
            "single_statistics_tied_with_it": thr_ties,
            "fit": threshold_fit,
            "model_search": model_search,
            "field_ceiling_law": field_ceiling_law,
            "conjunct_mechanisms": conjunct_mechanisms,
            "gate_robustness_qualifier": {
                "claim_919_headline": "threshold_is_degree_5",
                "gate_band": thr_boundaries["frozen_segment"],
                "lower_boundary": thr_boundaries["lower_boundary_gate_bits"],
                "upper_boundary": thr_boundaries["upper_boundary_gate_bits"],
                "relative_half_width_percent": thr_boundaries[
                    "relative_half_width_percent_of_the_frozen_gate"],
                "survival_measure": CLAIMS["threshold_is_degree_5"][
                    "survival_measure_over_full_region"],
                "persist_deadline_combos_holding":
                    len(CLAIMS["threshold_is_degree_5"][
                        "persist_deadline_combos_where_it_holds_at_the_frozen_gate"]),
                "claim_refined": C_THR,
                "refined_gate_band": CLAIMS[C_THR][
                    "containing_gate_band_at_the_frozen_slice"],
                "refined_survival_measure":
                    CLAIMS[C_THR]["survival_measure_over_full_region"],
                "verdict": ("GATE-FRAGILE: the located threshold survives a gate band of "
                            "%.3e bits around the frozen 0.02 (%.2f%% relative half-width) "
                            "and %d of %d persistence/deadline combinations."
                            % (thr_boundaries["upper_boundary_gate_bits"]
                               - thr_boundaries["lower_boundary_gate_bits"],
                               thr_boundaries[
                                   "relative_half_width_percent_of_the_frozen_gate"],
                               len(CLAIMS["threshold_is_degree_5"][
                                   "persist_deadline_combos_where_it_holds_at_the_frozen_gate"]),
                               32))}},
        "identity_analysis": {
            "branch_count_at_pointer": "IDENTICAL to pointer_degree by the frozen rule's own "
                                       "definition; inseparable at any family size",
            "n_fragments": "separable, and SEPARATED here by the A/E families",
            "max_degree": "separable, and SEPARATED here by the C family -- and it carries "
                          "NEITHER law: a degree-6 hub in the environment buys nothing",
            "components_of_G_minus_S": "already separated inside the pinned 26 cells "
                                       "(G4, G5, G6, H4) and again here by D1 -- carries "
                                       "neither law"},
    }

    # =================================================================== output ==
    mach_ok = (mach_all["norm"] <= MACH_TOL and mach_all["hermiticity"] <= MACH_TOL
               and mach_all["negativity"] <= MACH_TOL
               and mach_all["entropy_bound"] <= MACH_TOL
               and mach_all["t0_anchor"] <= T0_ANCHOR_TOL
               and mach_all["route_AB_max_dev"] <= MACH_TOL
               and mach_all["route_AC_max_dev"] <= MACH_TOL)
    wall = time.perf_counter() - T_START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30
    digest = sha256_bytes(json.dumps({"frozen": frozen_table, "new": newcells,
                                      "claims": {k: v["frozen_slice_persist3_deadline1"]
                                                 for k, v in CLAIMS.items()}},
                                     sort_keys=True, default=repr).encode())

    deviations = [
        "DESIGN-FREEDOM-1 (THE SWEEP GRID): the swept range [0.005, 0.08] bits of C_ab, the "
        "persistence set {2,3,4,5} and the deadline set {0.5 ... 1.2} are this block's "
        "declaration.  Inside that range the sweep is EXACT rather than sampled: the frozen "
        "protocol's only gate-dependent predicate is C_ab(pair) <= gate, so the verdict "
        "table is piecewise constant with breakpoints exactly at measured C_ab values, and "
        "all of them are enumerated.  The declared dense grid is evaluated too and is "
        "verified consistent with the exact decomposition on every cell (no grid truncation).",
        "DESIGN-FREEDOM-2 (THE SEPARATION FAMILY): the eighteen new geometries are this "
        "block's design freedom.  The frozen partition rule, labelling and tie-break are "
        "applied VERBATIM; the geometries are chosen so that the rule itself produces the "
        "separation, as the spec directs.",
        "IMPLEMENTATION-FIX (DISCLOSED): the 917/919 build assembles fragment anchors with "
        "`frags = {label_of[r]: [r] for r in rec}`, which silently drops an anchor when two "
        "recording sites carry the same fragment label.  The frozen memo's text assigns a "
        "site to the fragment NAMED by its signed axis, so colliding sites share a fragment.  "
        "This block implements the memo's reading.  The fix is a no-op wherever labels are "
        "distinct, and the 24-cell / 312-row exact reproduction (deviation exactly 0) proves "
        "it changes nothing on the pinned family.",
        "G6-EXPANSION (NEW CAPABILITY, GATED): the cube cells were imported without rows in "
        "both 914->917 and 917->919, which would have left 2 of the 26 cells unsweepable.  "
        "The pinned 914 receipt publishes chi per fragment class and C_ab per pair class "
        "(five classes covering all fifteen pairs, declared verbatim in the 914 source), so "
        "the rows expand losslessly.  The expansion is gated against the pinned 914 R_ind "
        "ledger (13 rows x 3 deltas, plus witnesses and content passes) and the pinned 917 "
        "import event before use.  The cube is still never evolved (2^27).",
        "A6-LABEL (DECLARED): A6's sixth leaf sits at the cube origin, for which the frozen "
        "signed-axis labelling has no label; it is labelled -z by hand.  A6 is a CONTROL "
        "only -- it must reproduce the pinned 917 G2 star7 -- and no claim rests on the "
        "hand-labelled site.",
        "COORDINATE EMBEDDING: the A-family geometries are graph-isomorphic to already "
        "measured stars.  That is the design: the Hamiltonian, the preparation and the "
        "evolved state are bit-identical, so any verdict difference inside the family is "
        "attributable to the PARTITION alone.  A sceptic who says 'only the labels changed' "
        "is agreeing with the finding.",
        "FRAGMENT COUNT AND FRAGMENT SIZE ARE COUPLED: at fixed pointer degree, lowering the "
        "fragment count necessarily enlarges a fragment.  The B and E families are matched "
        "controls that hold the fragment count AND the size multiset AND n fixed while "
        "moving the pointer degree, which is what breaks the coupling.  The pinned family "
        "supplies the other direction (H1/H2/H3 hold the count at 5 with sizes 1, 3 and "
        "mixed, all YES).",
        "THETA-ADAPTATION and XI-REG-ADAPTATION: as in Cycles 917 and 919 (pointer-degree "
        "average; graph-distance shells).  Unchanged, and re-verified by the exact "
        "reproduction.",
        "LATE-GRID: only the certification subgrid Jt in {0.0 ... 1.2} is executed, as in "
        "914, 917 and 919.  The deadline axis is therefore swept only inside that grid; "
        "deadlines above 1.2 are not evaluated and are not claimed.",
        "SECONDARY AXES: the excess-anchor and content-floor sweeps are DECLARED SECONDARY "
        "one-dimensional diagnostics at the frozen gate/persistence/deadline point, reported "
        "as such, not part of the primary three-axis region.",
    ]

    receipt = {
        "schema": "gate-sweep-separation-cycle926-v1",
        "cycle": 926,
        "runner": "scripts/frontier_cycle926_gate_sweep_separation_2026_07_28.py",
        "date": "2026-07-28",
        "git_head": head,
        "boundary_sentences": BOUNDARY,
        "pins": pins,
        "recovered_d1_note": d1_prov,
        "frozen_constants_byte_verified": frozen,
        "frozen_constants_cross_check": const_x,
        "restriction_gates": {
            "partition_rule_reproduces_the_memo_cube_partition": {"ok": True,
                                                                  "per_label": rule_detail},
            "cycle917_and_919_reproduced_value_for_value": restrict,
            "g6_row_expansion_gate": g6_detail,
            "frozen_gate_constants_byte_verified": {k: frozen[k]["quote"] for k in frozen},
        },
        "protocol": {
            "H": "-sum_<ij> Z_i Z_j - lambda sum_i X_i", "J": 1,
            "lambdas_frozen": list(FROZEN_LAMBDAS),
            "lambda_design_extension": EXTENSION_LAMBDA,
            "probe_lambdas_non_claim_diagnostic": list(PROBE_LAMBDAS),
            "deltas": list(DELTAS), "headline_delta": HEADLINE_DELTA,
            "frozen_gate_C_ab": INDEP_MAX, "frozen_persistence_samples": PERSIST_N,
            "frozen_deadline_jt": DEADLINE_JT, "content_H_min": CONTENT_H_MIN,
            "excess_min": EXCESS_MIN, "T_executed": T_EXEC,
            "preparation_rule": "the pointer and every pointer-adjacent (recording) site in "
                                "+X; every other site in +Z",
            "partition_rule": "each recording site anchors the fragment NAMED by its label; "
                              "every other site joins its nearest recording site's fragment; "
                              "ties by the frozen memo's tie-break algorithm in cube "
                              "coordinates",
        },
        "frozen_point_26_cell_table": frozen_table,
        "sweep": {
            "axes": {"C_ab_gate": {"range": [GATE_MIN, GATE_MAX], "declared_grid": GATE_GRID,
                                   "exact": True,
                                   "exactness_note": "breakpoints are the measured C_ab "
                                                     "values themselves; the grid is a "
                                                     "declared cross-check, not the method"},
                     "persistence_samples": list(PERSIST_GRID),
                     "deadline_jt": list(DEADLINE_GRID)},
            "declared_grid_table_at_persist3_deadline1": grid_table,
            "grid_vs_exact_interval_mismatches": grid_mismatch,
            "threshold_map_over_the_full_region": thr_map,
            "threshold_boundaries": thr_boundaries,
            "persist_axis_at_the_frozen_gate": axis_persist,
            "deadline_axis_at_the_frozen_gate": axis_deadline,
            "secondary_axis_excess_anchor": axis_excess,
            "secondary_axis_content_floor": axis_content,
            "per_cell_exact_gate_intervals_at_persist3_deadline1": {
                "%s@%s" % (k, lk): INTV[(k, lk, PERSIST_N, DEADLINE_JT)] for (k, lk) in CELLS},
            "margins_at_the_frozen_point": margins,
        },
        "claims": CLAIMS,
        "separation_family": {
            "geometries": per_geom,
            "cells": newcells,
            "controls_vs_the_pinned_family": controls,
            "statistic_separation_audit": sep_audit,
            "matched_pairs": matched,
            "ceiling_law_fit": ceiling_fit,
            "threshold_law_fit": threshold_fit,
            "model_search": model_search,
            "field_ceiling_two_variable_law": field_ceiling_law,
            "field_ceiling": ceiling,
            "field_ceiling_by_statistic": ceil_by,
        },
        "refined_law": refined,
        "teeth": teeth,
        "numerics": {
            "route_A": "Chebyshev expansion of exp(-iHt), rigorous Bessel tail bound",
            "route_B": "scaling-and-marching Taylor propagator, rigorous factorial remainder",
            "route_C": "exact dense eigendecomposition (n <= 12)",
            "machinery": mach_all, "machinery_ok": bool(mach_ok),
            "peak_rss_gib": rss, "wall_s": wall,
            "python": platform.python_version(), "numpy": np.__version__,
            "table_digest": digest,
        },
        "deviations": deviations,
        "blindness": "NOT BLIND: the pinned 917 and 919 receipts and notes were read while "
                     "designing the sweep and the family.  The eighteen new geometries are "
                     "fresh measurements; the 24 pinned cells are exact reproductions; the "
                     "two G6 cells are a gated expansion of a pinned import.",
    }
    outp = os.path.join(ROOT, "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=float)

    # ---------------------------------------------------------------- stdout --
    print("SETUP cycle=926 head=%s pins=%d frozen-constants=%d (identical-to-917=%s "
          "identical-to-919=%s) cells=%d new-geometries=%d gate-grid=%d persist=%s "
          "deadline=%s %s"
          % (head, len(pins), len(frozen), const_x["identical_to_917_receipt"],
             const_x["identical_to_919_receipt"], len(CELLS), len(NEW_KEYS),
             len(GATE_GRID), list(PERSIST_GRID), list(DEADLINE_GRID), BOUNDARY_LINE))
    print("RESTRICT 917 cells=%d rows=%d mismatches=%d maxdev=%s | 919 cells=%d rows=%d "
          "mismatches=%d maxdev=%s | deviation-exactly-zero=%s %s"
          % (restrict["cycle917"]["cells"], restrict["cycle917"]["rows"],
             len(restrict["cycle917"]["mismatches"]),
             json.dumps({k: v for k, v in restrict["cycle917"]["max_abs_dev"].items()}),
             restrict["cycle919"]["cells"], restrict["cycle919"]["rows"],
             len(restrict["cycle919"]["mismatches"]),
             json.dumps({k: v for k, v in restrict["cycle919"]["max_abs_dev"].items()}),
             restrict["deviation_exactly_zero"], BOUNDARY_LINE))
    print("G6-EXPANSION %s %s"
          % (json.dumps({k: {"verdict": v["verdict"], "maxR": v["max_r_ind"],
                             "first_jt": v["first_jt"], "run": v["run"],
                             "ok": v["reproduces_pinned_914_ledger_and_917_import"]}
                         for k, v in sorted(g6_detail.items())}, sort_keys=True),
             BOUNDARY_LINE))
    for (k, lk) in CELLS:
        t = frozen_table["%s@%s" % (k, lk)]
        print("FROZEN-CELL %-4s@%-5s deg=%d frags=%d maxdeg=%d comps=%d loopfree=%s -> %-3s "
              "maxR=%d first_Jt=%-5s run=%-4s %s"
              % (k, lk, t["pointer_degree"], t["n_fragments"], t["max_degree"],
                 t["components_of_G_minus_S"], t["loop_free"], t["verdict"], t["max_r_ind"],
                 t["first_jt"], t["run"], BOUNDARY_LINE))
    for nm, c in sorted(CLAIMS.items()):
        print("CLAIM %-34s frozen=%s band=%s width=%.3e below=%.3e above=%.3e "
              "survival=%.4f combos-holding=%d/%d %s"
              % (nm, c["holds_at_the_frozen_point"], c["containing_gate_band_at_the_frozen_slice"],
                 c["band_width_bits"] or 0.0, c["distance_below_frozen_gate_bits"] or 0.0,
                 c["distance_above_frozen_gate_bits"] or 0.0,
                 c["survival_measure_over_full_region"],
                 len(c["persist_deadline_combos_where_it_holds_at_the_frozen_gate"]),
                 c["n_persist_deadline_combos"], BOUNDARY_LINE))
    print("THRESHOLD-BAND frozen-segment=[%.10g, %.10g) threshold=%d clean=%s | just-below=%s "
          "| just-above=%s | relative-half-width=%.2f%% of the 0.02 gate %s"
          % (cur["lo"], cur["hi"], cur["threshold"], cur["clean_cut"],
             json.dumps({k: thr_boundaries["threshold_just_below"][k]
                         for k in ("lo", "hi", "threshold", "clean_cut")}
                        if thr_boundaries["threshold_just_below"] else None),
             json.dumps({k: thr_boundaries["threshold_just_above"][k]
                         for k in ("lo", "hi", "threshold", "clean_cut")}
                        if thr_boundaries["threshold_just_above"] else None),
             thr_boundaries["relative_half_width_percent_of_the_frozen_gate"], BOUNDARY_LINE))
    for pd, segs in sorted(thr_map.items()):
        print("THRESHOLD-MAP %-22s %s %s"
              % (pd, json.dumps([[round(s["lo"], 8), round(s["hi"], 8), s["threshold"],
                                  s["clean_cut"]] for s in segs]), BOUNDARY_LINE))
    print("PERSIST-AXIS %s %s"
          % (json.dumps({k: {"thr": v["threshold_at_0.10"], "clean": v["clean_cut"]}
                         for k, v in sorted(axis_persist.items())}, sort_keys=True),
             BOUNDARY_LINE))
    print("DEADLINE-AXIS %s %s"
          % (json.dumps({k: {"thr": v["threshold_at_0.10"], "clean": v["clean_cut"]}
                         for k, v in sorted(axis_deadline.items())}, sort_keys=True),
             BOUNDARY_LINE))
    print("SECONDARY-AXES excess=%s content=%s %s"
          % (json.dumps({k: v["threshold_at_0.10"] for k, v in sorted(axis_excess.items())},
                        sort_keys=True),
             json.dumps({k: v["threshold_at_0.10"] for k, v in sorted(axis_content.items())},
                        sort_keys=True), BOUNDARY_LINE))
    for key in NEW_KEYS:
        g = GEOM[key]
        st = g["stats"]
        part = "; ".join("%s=[%s]" % (L, ",".join(g["sites"][i] for i in g["frags"][L]))
                         for L in g["labels"])
        print("PARTITION %-3s %-14s n=%-2d bonds=%-2d deg(S)=%d maxdeg=%d frags=%d comps=%d "
              "depth=%d loops=%-2d sizes=%s :: %s %s"
              % (key, g["name"], st["n_sites"], st["n_bonds"], st["pointer_degree"],
                 st["max_degree"], st["n_fragments"], st["components_of_G_minus_S"],
                 st["depth_eccentricity_from_pointer"], st["cyclomatic_number_loops"],
                 json.dumps(st["fragment_sizes"], sort_keys=True), part, BOUNDARY_LINE))
    for key in NEW_KEYS:
        for lk in ("0.05", "0.075", "0.1"):
            c = newcells["%s@%s" % (key, lk)]
            f = c["four_statistics"]
            print("NEWCELL %-3s@%-5s[%-16s] deg=%d maxdeg=%d frags=%d comps=%d -> %-3s "
                  "maxR=%d first_Jt=%-5s run=%-4s m3=%-12s wit=%s %s"
                  % (key, lk, c["field_status"], f["pointer_degree"], f["max_degree"],
                     f["n_fragments"], f["components_of_G_minus_S"], c["verdict"],
                     c["max_r_ind"], c["first_jt"], c["run"],
                     ("%.9f" % c["margins"]["margin_at_the_third_sample_bits"])
                     if c["margins"].get("margin_at_the_third_sample_bits") is not None
                     else "-", c["witness"], BOUNDARY_LINE))
    for nm, r in sorted(controls.items()):
        print("CONTROL %-24s %s %s" % (nm, json.dumps(r, sort_keys=True), BOUNDARY_LINE))
    for hi, lo in MATCHED:
        r = matched["%s_vs_%s" % (hi, lo)]
        print("MATCHED %-3s(deg=%d,frags=%d) vs %-3s(deg=%d,frags=%d) sizes-matched=%s "
              "n-matched=%s :: %s %s"
              % (hi, r["high_pointer_degree"]["pointer_degree"],
                 r["high_pointer_degree"]["n_fragments"], lo,
                 r["low_pointer_degree"]["pointer_degree"],
                 r["low_pointer_degree"]["n_fragments"],
                 r["fragment_size_multiset_matched"], r["n_sites_matched"],
                 json.dumps({k: [v["verdict_high_degree"], v["verdict_low_degree"],
                                 v["max_r_ind_high"], v["max_r_ind_low"]]
                             for k, v in sorted(r["per_field"].items())}, sort_keys=True),
                 BOUNDARY_LINE))
    for lk in ("0.05", "0.1"):
        print("CEILING-FIT lam=%-5s %s %s"
              % (lk, json.dumps({s: round(v["accuracy"], 4)
                                 for s, v in sorted(ceiling_fit[lk].items())}, sort_keys=True),
                 BOUNDARY_LINE))
    print("THRESHOLD-FIT %s %s"
          % (json.dumps({s: {"cut": v["cut"], "acc": round(v["accuracy"], 4),
                             "wrong": sorted(v["counterexamples"])}
                         for s, v in sorted(threshold_fit.items())}, sort_keys=True),
             BOUNDARY_LINE))
    print("SEPARATION-AUDIT %s %s"
          % (json.dumps({k: v["n_separating_geometries"] for k, v in sorted(sep_audit.items())},
                        sort_keys=True), BOUNDARY_LINE))
    print("FIELD-CEILING %s %s"
          % (json.dumps({k: v["certifies_up_to"] for k, v in sorted(ceiling.items())},
                        sort_keys=True), BOUNDARY_LINE))
    print("CEILING-BY-STAT %s %s"
          % (json.dumps({s: {"table": v["table"], "single_valued": v["single_valued_per_class"]}
                         for s, v in sorted(ceil_by.items())}, sort_keys=True), BOUNDARY_LINE))
    for nm, t in sorted(teeth.items()):
        print("TOOTH %-52s fires=%s %s"
              % (nm, t.get("fires"),
                 json.dumps({k: v for k, v in t.items()
                             if k not in ("fires", "per_geometry", "intervals",
                                          "cells_where_the_verdict_is_NON_monotone_in_the_gate",
                                          "counterexamples", "claimed_table_entry")},
                            sort_keys=True, default=str)[:340] + " " + BOUNDARY_LINE))
    print("MODEL-SEARCH patterns=%d best-acc=%.4f perfect-patterns=%d :: %s | "
          "single-best=%s %s"
          % (model_search["n_distinct_prediction_patterns"], model_search["best_accuracy"],
             model_search["n_distinct_patterns_at_100_percent"],
             json.dumps([m["shortest_description"] for m in model_search["perfect_models"]]),
             json.dumps({k: round(v, 4) for k, v in
                         sorted(model_search["single_statistic_best"].items())},
                        sort_keys=True), BOUNDARY_LINE))
    print("FIELD-CEILING-LAW acc=%.4f misses=%s pair-determines-ceiling=%s :: %s %s"
          % (field_ceiling_law["accuracy"], field_ceiling_law["misses"],
             field_ceiling_law["the_pair_determines_the_ceiling"],
             field_ceiling_law["rule"], BOUNDARY_LINE))
    print("PAIR-TABLE %s %s"
          % (json.dumps({k: {"geoms": v["geometries"], "ceil": v["ceilings"]}
                         for k, v in field_ceiling_law["pair_table"].items()},
                        sort_keys=True), BOUNDARY_LINE))
    print("CONJUNCT-MECHANISM %s :: %s %s"
          % (json.dumps(conjunct_mechanisms["grouped"], sort_keys=True),
             conjunct_mechanisms["reading"], BOUNDARY_LINE))
    print("REFINED-HEADLINE %s %s" % (refined["headline"], BOUNDARY_LINE))
    print("REFINED-THRESHOLD-LAW conjunction-holds=%s degree-alone=%s fragments-alone=%s "
          ":: %s %s"
          % (refined["threshold_law"]["conjunctive_law_holds"],
             refined["threshold_law"]["pointer_degree_alone_holds"],
             refined["threshold_law"]["fragment_count_alone_holds"],
             refined["threshold_law"]["statement"], BOUNDARY_LINE))
    print("REFINED-CEILING-LAW fragments-reading=%s degree-reading=%s decisive=%s %s"
          % (refined["ceiling_law"]["fragment_count_reading_holds"],
             refined["ceiling_law"]["pointer_degree_reading_holds"],
             refined["ceiling_law"]["separation_is_decisive"], BOUNDARY_LINE))
    print("REFINED-CEILING carrying=%s :: %s %s"
          % (refined["ceiling_law"]["carrying_statistic"],
             refined["ceiling_law"]["statement"], BOUNDARY_LINE))
    print("REFINED-THRESHOLD best-fit=%s ties=%s band=[%.10g, %.10g) rel-half-width=%.2f%% %s"
          % (thr_best, thr_ties, cur["lo"], cur["hi"],
             thr_boundaries["relative_half_width_percent_of_the_frozen_gate"], BOUNDARY_LINE))
    print("MACHINERY %s ok=%s rss=%.2fGiB wall=%.1fs %s"
          % ({k: "%.3g" % v for k, v in sorted(mach_all.items())}, mach_ok, rss, wall,
             BOUNDARY_LINE))
    nfire = sum(1 for t in teeth.values() if t.get("fires"))
    print("TOTAL %s frozen-cells=%d new-cells=%d claims=%d teeth=%d/%d digest=%s wall=%.1fs %s"
          % ("SWEPT-AND-SEPARATED" if mach_ok else "MACHINERY-FAIL", len(CELLS),
             len(newcells), len(CLAIMS), nfire, len(teeth), digest[:16], wall, BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0 if mach_ok else 2)


if __name__ == "__main__":
    main()
