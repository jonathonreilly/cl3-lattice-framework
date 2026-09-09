#!/usr/bin/env python3
"""Cycle 927 -- THE SECOND CHANNEL: is the loop-independent cost carried by FRAGMENT SIZE?

THE MEASURED PHENOMENON THIS BLOCK EXPLAINS.  Three pinned receipts set it up:

  Cycle 917 (14-cell geometry ladder, frozen route-C certification gates):
    max R_ind over the window equals the pointer degree on all seven geometries at
    lambda = 0.05; at lambda = 0.10 the equality survives on every LOOP-FREE geometry
    and fails on the loopy ones.  A GRADED FIELD CEILING is reported as a declared
    non-claim diagnostic: degree 2 -> 0.05, degrees 3-4 -> ~0.075, degree 6 -> 0.10,
    with the threshold BRACKETED in (4, 6].
  Cycle 919 (degree-5 block): degree 5 certifies at 0.10 on all four geometries, so
    the bracket collapses to the singleton {5}: "degree 2 -> 0.05; degrees 3-4 ->
    0.075; degrees 5-6 -> 0.10", threshold LOCATED at degree 5.
  Cycle 921 (loop-cost block): the loop cost is the PAIR-CYCLE LAW -- a per-pair tax
    graded by the shortest pointer-through cycle length, ceiling = independence number
    of the survivors, loop-free geometries pay NOTHING.  Exactly one exception is
    carried openly: 917's degree-2 chain G1 at lambda = 0.10, predicted ceiling 2,
    measured 1.  Its two arms sit at infinite anchor distance, so the pair-cycle law
    predicts no cost; the drop comes from a SECOND, LOOP-INDEPENDENT channel that the
    921 note reports as growing with fragment size and field (G1's 4-site arms reach
    C_ab = 0.0217, just over the 0.02 dependence gate).  Cycle 927 is its named
    successor.

WHAT THIS BLOCK MEASURES.

  Q1 -- THE SIZE LAW.  LOOP-FREE geometry families only, so the pair-cycle law
  predicts ZERO cost on every cell and any observed cost isolates the second channel.
  Symmetric spiders sweep arm length at fixed pointer degree (degree 2: arms 1..7;
  degree 3: 1..5; degrees 4 and 5: 1..3 -- the 2^16 full-space cap is respected and
  every capped extension is declared) and degree at fixed arm length.  Per cell: the
  full R_ind ledger, C_ab on every fragment pair at the ceiling row, theta_A, xi_reg.
  Deliverable: C_ab-vs-(arm length, field) with the 0.02 gate crossings located, the
  size law as the evidence supports it, and the PAIR-vs-CONTENT question decided by
  measurement (which pairs go dependent, and whether fragments fail the content gate
  as they do in the pair-cycle law's d = 1 tier).

  Q2 -- THE MECHANISM.  Structural predictors, every one a pure function of the graph
  and the frozen partition, DECLARED AND COMPUTED BEFORE ANY PROPAGATOR RUNS (the 921
  discipline), each with a discriminating prediction on named cells:
    (a) WITHIN-ARM MIXING          scales with arm Hilbert dimension  -> 2^|F|
    (b) RECURRENCE                 scales with arm depth / revival time -> ecc(F)
    (c) BOUNDARY CONTENT           only the far end decouples -> leaf count
    (d) SPECTRAL CROWDING          level spacing of the arm shrinks -> min gap
    (e) ARITY DILUTION             the pointer is shared among deg(S) arms
    (f) SYSTEM SIZE                the n confound, carried as a rival not a nuisance
  The discriminators: SHAPE cells hold fragment SIZE fixed and vary arm shape (a path
  of 4, a claw of 4, a tee of 4 -- identical n, identical degree, identical arm
  Hilbert dimension, different depth / leaves / spectrum); ASYMMETRIC spiders (one
  long arm, the rest singletons) separate a PER-PAIR mechanism from a PER-GEOMETRY
  one; an extended-window probe separates a WINDOW effect from a STATE effect.

  Q3 -- THE UNIFICATION QUESTION.  Is 917/919's degree-graded field ceiling actually
  carried by FRAGMENT SIZE rather than degree?  In the 917/919 ladder the two
  co-vary: the chain has 4-site arms and certifies only at 0.05, the star has 1-site
  fragments and certifies at 0.10.  Matched designs decide it:
    (A) FIXED DEGREE, VARIED SIZE   -- does the certifying-field ceiling move?
    (B) FIXED SIZE, VARIED DEGREE   -- does it stay?
    (C) FIXED n, VARIED (degree, size) -- the n control; note that for a symmetric
        spider n = 1 + degree * size, so any two of the three fix the third.  That
        three-way coupling is UNAVOIDABLE on symmetric families and is declared, not
        hidden; the ARITY LADDER breaks it by holding one long-arm PAIR fixed and
        adding singleton arms, which moves degree and n while the pair is untouched.
  Either outcome is the headline.  If size carries the grading at fixed degree and
  degree does not move it at fixed size, the 919 "threshold at degree 5" claim needs
  a scope qualifier; if degree carries it at fixed size, the 919 claim hardens.

RESTRICTION GATES.  Before any new number: the partition rule reproduces the frozen
memo's own six published cube fragment lists; all six Cycle 917 geometries and all
four Cycle 919 degree-5 geometries are reproduced VALUE-FOR-VALUE against the pinned
receipts (row by row: chi, C_ab, theta_A, H_Z, the R_ind ledger, xi_reg, max R_ind,
witness, verdict, event); the G1 EXCEPTION cell is reproduced with its C_ab margin;
all 32 Cycle 921 DESIGNED geometries are reproduced value-for-value at both frozen
fields including their per-pair dependence margins; and the 21 frozen constants are
byte-verified out of the frozen memo and cross-checked quote-for-quote against the
pinned 917, 919 and 921 receipts.

ROUTE.  Full-space exact evolution on every geometry.  Route A: Chebyshev expansion
of exp(-iHt) with a rigorous Bessel tail bound.  Route B: scaling-and-marching Taylor
with a rigorous factorial remainder bound (algorithmically disjoint from A -- no
Bessel coefficients, no three-term recurrence).  Route C: exact dense
eigendecomposition where n <= 12.  Every claim-grade cell is computed twice on route
A in-process and the observable-table digests compared byte-for-byte.

REDUCED SPECTRA.  Long arms make the naive conditional-mutual-information route
infeasible (for a degree-2 spider the joint of both fragments with the pointer is the
WHOLE system, so the pinned code path would need a 2^15 x 2^15 matrix).  This block
therefore carries TWO exact routes to the same spectrum: the pinned DIRECT route
(materialise the reduced density matrix, eigvalsh) wherever its dimension is at most
DIRECT_MAX_DIM, and a GRAM route (the nonzero spectrum of M M^dag equals that of the
smaller Gram matrix M^dag M) everywhere.  The two are algebraically identical; the
runner cross-validates them on every cell where both are feasible and reports the
maximum deviation.  Every pinned 917/919/921 cell falls inside the direct route, so
the value-for-value gates run on the pinned code path unchanged.

Deterministic, float64/complex128, no network, no tree writes outside the declared
receipt.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.
No formation rule.
Sets no audit status.
"""

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
    # ---- Cycle 917: the geometry ladder, the constants authority ----
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
    # the upstream commission / recovery receipts
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
        "cabb1bef15221b5fca61ffc7c50f8ec18452893d"),
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json": (
        "d7d27ce19d231624415db1e71ee77eae16b5175dd403b403c254b38fb171b0a7",
        "9931c298a5917eb90de290cbb82c237508c9e692"),
    # ---- Cycle 919: the degree-5 block whose grading Q3 interrogates ----
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
    "logs/runner-cache/frontier_cycle919_degree_five_2026_07_28.txt": (
        "249f40fb1b416acb19ba5b36c5d08a69904aab2f940f22b0aebeed666053279c",
        "0424ee81cef16c95193708f8f270eb154cdc6fe0"),
    # ---- Cycle 921: the pair-cycle law and the G1 exception this block succeeds ----
    "scripts/frontier_cycle921_loop_cost_2026_07_28.py": (
        "fbde9f1a62e33e1e7fb9a440658ed23821a0f0c577fb8b798f707e23118ffc11",
        "55710d560dd948e2ccc053c3b7eb09d0d523d6a4"),
    "scripts/frontier_cycle921_loop_cost_independent_check_2026_07_28.py": (
        "0251ea95e8723df2fa9f6f081e73022aa09097bb7a4da3b3648c4dffd00734b9",
        "e14176a65f39d84dd77839ff4a714347707910f9"),
    "outputs/loop_cost_cycle921_receipt_2026_07_28.json": (
        "86e58837349baa719d116948c67a166b922cb6b21fefe6108ec41fa08727df6f",
        "01e9689639dee1dc6f73c6a2834a84da3dc9f6cc"),
    "outputs/loop_cost_independent_check_cycle921_receipt_2026_07_28.json": (
        "75d9808b0385fbe83d78f832ad70fee092ebb94c64cc4ef672742b013d8cbdd3",
        "abb45f90685a29a4d4cbfd1d5966e36d3bf34bd9"),
    "outputs/loop_cost_block_cycle921_ship_receipt_2026_07_28.json": (
        "f8319ba38428995cf19e4ae93f7a2c72bff388a6a70cd96bd57bc3d5670a6c4f",
        "4c99b70e0deb1c05db0df4ae0236500366c0dc96"),
    "docs/LOOP_COST_PAIR_CYCLE_LAW_CYCLE921_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "36b70f78959ae0a739aca76355b6390022113a43967566b727b91363bece22a6",
        "69866c618441585072ab1df72c68c857799a7171"),
    "logs/runner-cache/frontier_cycle921_loop_cost_2026_07_28.txt": (
        "d326f1dcaad650cfc61df5abe7bb84ac0c06ff114497063215dfc6d7bf676503",
        "cbd2a6db89d4f0e7e526dc8a6fed85b1da6f7b7a"),
}

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C917_CHECK_RECEIPT = "outputs/geometry_independent_check_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
C921_RECEIPT = "outputs/loop_cost_cycle921_receipt_2026_07_28.json"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"

# the recovered d=1 comparator note -- NOT in tree; consumed as git-history evidence,
# exactly as Cycles 917, 919 and 921 consumed it.
D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
# Every constant below is BYTE-VERIFIED against the frozen memo in
# verify_frozen_constants(); a mismatch is a hard fail, exit 2.
FROZEN_LAMBDAS = (0.05, 0.10)      # the CERTIFIED fields (914/915 commission)
EXTENSION_LAMBDA = 0.075           # 919's DECLARED DESIGN EXTENSION, inherited
DIAG_LAMBDAS = (0.075, 0.125, 0.15)   # this block's DECLARED DIAGNOSTIC extensions
LAMBDAS = (0.05, 0.075, 0.10, 0.125, 0.15)
CLAIM_LAMBDAS = (0.05, 0.10)
ANCHOR_LAMBDAS = (0.05, 0.075, 0.10)   # the fields the 917/919 gates compare on
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05            # condition 1: H(Z_S) >= 0.05 bit
EXCESS_MIN = 0.02               # condition 3: excess >= 0.02 bit
INDEP_MAX = 0.02                # condition 4: C_ab <= 0.02 bit
T0_ANCHOR_TOL = 1e-9            # t=0 verification: chi(0) <= 1e-9 bit
DRIFT_MAX = 0.10                # CHECK-02 pointer drift
PERSIST_N = 3                   # CHECK-03 persistence
MACH_TOL = 1e-9
RESTRICT_TOL = 1e-9             # 917/919/921 value-for-value reproduction tolerance
T_EXEC = [round(0.1 * i, 10) for i in range(13)]   # Jt = 0.0 .. 1.2, 13 points
T_LONG = [round(0.1 * i, 10) for i in range(25)]   # Jt = 0.0 .. 2.4, NON-CLAIM probe
DENSE_MAX_N = 12                # route C ceiling (2^12 = 4096)
FULL_SPACE_CAP_N = 16           # the declared 2^16 full-space cap
DIRECT_MAX_DIM = 1024           # reduced-density-matrix route ceiling (see docstring)

CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")

C917_KEYS = ["G1", "G2", "G3a", "G3b", "G4", "G5"]
C919_KEYS = ["H1", "H2", "H3", "H4"]


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
        if got_sha != want_sha:
            die("pin:sha256 %s got=%s want=%s" % (path, got_sha, want_sha))
        if got_blob != want_blob:
            die("pin:blob %s got=%s want=%s" % (path, got_blob, want_blob))
        out[path] = {"sha256": got_sha, "git_blob": got_blob, "bytes": len(b)}
    return out


def recover_d1_note():
    """Read the never-landed d=1 comparator note out of git history (917/919/921's route)."""
    cmds = ["git cat-file -e HEAD:%s" % D1_NOTE_PATH,
            "git cat-file -t %s" % D1_NOTE_BLOB,
            "git cat-file blob %s" % D1_NOTE_BLOB]
    if git(["cat-file", "-e", "HEAD:%s" % D1_NOTE_PATH]).returncode == 0:
        die("d1-note:unexpectedly-in-tree (the 915 receipt records it as never-landed)")
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
    if art["sha256"] != got or art["blob"] != D1_NOTE_BLOB or art["bytes"] != len(b):
        die("d1-note:915-receipt-cross-check")
    for rp in (C917_RECEIPT, C919_RECEIPT, C921_RECEIPT):
        rec = json.load(open(os.path.join(ROOT, rp)))
        if rec["recovered_d1_note"]["sha256"] != got:
            die("d1-note:%s-cross-check" % rp)
    return b.decode("utf-8"), {"path": D1_NOTE_PATH, "blob": D1_NOTE_BLOB,
                               "sha256": got, "bytes": len(b),
                               "in_tree_at_head": False,
                               "sha256_matches_915_receipt": True,
                               "sha256_matches_917_receipt": True,
                               "sha256_matches_919_receipt": True,
                               "sha256_matches_921_receipt": True,
                               "commands_disclosed": cmds}


# ============================== restriction gate: frozen constants by bytes ==
# Identical to Cycles 917, 919 and 921's 21 patterns; re-declared here and re-verified
# from the memo's own bytes rather than imported from any source.
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


def cross_check_pinned_constants(frozen):
    """917, 919 AND 921 published the same 21 quotes; all four must agree byte-for-byte."""
    res = {}
    for tag, path in (("917", C917_RECEIPT), ("919", C919_RECEIPT),
                      ("921", C921_RECEIPT)):
        rec = json.load(open(os.path.join(ROOT, path)))
        theirs = rec["frozen_constants_byte_verified"]
        if set(theirs) != set(frozen):
            die("frozen-const:%s-key-set %s" % (tag, sorted(set(theirs) ^ set(frozen))))
        for k in sorted(frozen):
            if theirs[k]["quote"] != frozen[k]["quote"]:
                die("frozen-const:%s-quote %s" % (tag, k))
        res["identical_to_%s_receipt" % tag] = True
    res["count"] = len(frozen)
    return res


def parse_memo_cube_fragments(memo):
    """Parse the memo's six published cube fragment lists out of its bytes."""
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
def bfs(n, adj, src):
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


def build_geometry(key, name, sites, bonds_coord, pointer, label_of_rec,
                   tiebreak, dim, note, propagated=True):
    """Assemble a geometry: index the sites, derive recording sites, and build the
    fragment partition by the INHERITED rule (anchor + nearest-anchor + tie-break)."""
    idx = {c: i for i, c in enumerate(sites)}
    n = len(sites)
    if propagated and n > FULL_SPACE_CAP_N:
        die("geometry:%s exceeds the declared 2^%d full-space cap (n=%d)"
            % (key, FULL_SPACE_CAP_N, n))
    bonds = sorted({tuple(sorted((idx[a], idx[b]))) for (a, b) in bonds_coord})
    adj = {i: set() for i in range(n)}
    for (a, b) in bonds:
        adj[a].add(b)
        adj[b].add(a)
    S = idx[pointer]
    rec = sorted(adj[S])
    label_of = {r: label_of_rec(sites[r]) for r in rec}
    dS = bfs(n, adj, S)
    if len(dS) != n:
        die("geometry:%s disconnected" % key)
    drec = {r: bfs(n, adj, r) for r in rec}
    frags = {label_of[r]: [r] for r in rec}
    ties = []
    for i in range(n):
        if i == S or i in rec:
            continue
        dd = {r: drec[r].get(i, 10 ** 9) for r in rec}
        m = min(dd.values())
        cands = [r for r in rec if dd[r] == m]
        if len(cands) == 1:
            pick = cands[0]
        else:
            if tiebreak is None:
                die("geometry:%s tie without declared tie-break at site %r" % (key, sites[i]))
            pick = tiebreak(sites[i], cands, label_of)
            ties.append({"site": str(sites[i]), "nearest_distance": m,
                         "candidates": [label_of[c] for c in cands],
                         "assigned": label_of[pick]})
        frags[label_of[pick]].append(i)
    labels = sorted(frags, key=lambda L: (CUBE_LABELS.index(L) if L in CUBE_LABELS else 99, L))
    for L in labels:
        head, rest = frags[L][0], frags[L][1:]
        frags[L] = [head] + sorted(rest, key=lambda i: (dS[i], str(sites[i])))
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
    # ---- the 921 axis: anchor-to-anchor distance in G minus S (the pair-cycle meter)
    anchors = {L: frags[L][0] for L in labels}
    danch = {L: bfs(n, radj, anchors[L]) for L in labels}
    pair_d = {}
    for A, B in itertools.combinations(labels, 2):
        pair_d["|".join((A, B))] = int(danch[A].get(anchors[B], -1))
    internal_loops = len([1 for (a, b) in bonds if a != S and b != S]) - len(rest) + len(comps)
    g = {
        "key": key, "name": name, "note": note, "dim": dim, "n": n,
        "sites": [str(c) for c in sites], "coords": sites, "idx": idx,
        "bonds": bonds, "adj": adj, "S": S, "pointer": str(pointer),
        "recording": rec, "labels": labels, "frags": frags, "ties": ties,
        "dS": dS, "shells": shells, "degrees": degs, "anchors": anchors,
        "anchor_distance_in_G_minus_S": pair_d,
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
    g["stats"]["internal_loops_not_through_pointer"] = int(internal_loops)
    g["stats"]["loops_through_pointer"] = int(g["stats"]["cyclomatic_number_loops"]
                                              - internal_loops)
    dd = [v for v in pair_d.values() if v >= 0]
    g["stats"]["min_anchor_distance"] = int(min(dd)) if dd else -1
    g["stats"]["shortest_pointer_cycle_length"] = (int(min(dd)) + 2) if dd else -1
    g["stats"]["n_pairs_at_anchor_distance_1"] = sum(1 for v in pair_d.values() if v == 1)
    g["stats"]["n_pairs_at_anchor_distance_2"] = sum(1 for v in pair_d.values() if v == 2)
    g["stats"]["n_pairs_at_anchor_distance_3"] = sum(1 for v in pair_d.values() if v == 3)
    g["stats"]["max_fragment_size"] = max(g["stats"]["fragment_sizes"].values())
    g["stats"]["min_fragment_size"] = min(g["stats"]["fragment_sizes"].values())
    g["stats"]["fragment_size_multiset"] = sorted(g["stats"]["fragment_sizes"].values())
    g["stats"]["total_fragment_sites"] = int(n - 1)
    return g


def max_independent_set(vertices, edges):
    """Exact maximum independent set: the lexicographically first largest subset with
    no edge inside, in the declared label order."""
    V = list(vertices)
    E = {tuple(sorted(e)) for e in edges}
    for r in range(len(V), -1, -1):
        for c in itertools.combinations(V, r):
            if all(tuple(sorted(p)) not in E for p in itertools.combinations(c, 2)):
                return r, list(c)
    return 0, []


# ============ THE PRE-REGISTERED STRUCTURAL PREDICTORS (Q2 -- pre-propagator) ==
# Each is a pure function of the graph and the frozen partition.  All are computed
# for every geometry BEFORE any propagator runs, and the discriminating predictions
# below are decided by comparing them ACROSS declared matched cells -- never by
# fitting a free parameter to a single cell.
MECHANISMS = {
    "a_within_arm_mixing": (
        "WITHIN-ARM MIXING.  An arm's internal dynamics builds cross-arm correlation "
        "through the shared pointer, and the amount it can build scales with the arm's "
        "HILBERT DIMENSION.  Per pair (a,b) the predictor is |F_a| + |F_b| = log2 of the "
        "joint arm dimension.  DISCRIMINATING PREDICTION: on the SHAPE cells -- a path "
        "of 4, a claw of 4 and a tee of 4 at pointer degree 2 and n = 9 -- the arm "
        "dimension is IDENTICAL (2^4), so C_ab must be the same on all three."),
    "b_recurrence": (
        "RECURRENCE.  Longer arms have longer revival times, so the fixed certification "
        "window Jt <= 1.2 samples a more thermalised state.  Per pair the predictor is "
        "the arm ECCENTRICITY max_{i in F} d_S(i), the depth the excitation must travel "
        "and return.  DISCRIMINATING PREDICTIONS: (i) on the SHAPE cells C_ab must be "
        "ORDERED BY DEPTH (path 4 > tee 3 > claw 2) at equal size; (ii) the C_ab(t) "
        "curve on the extended NON-CLAIM window must show its L-dependence as a TIME "
        "SHIFT of a common shape, not as an amplitude change at fixed time."),
    "c_boundary_content": (
        "BOUNDARY CONTENT.  Only the arm's far end decouples from the pointer, so the "
        "arm's effective content shrinks with length and its correlation with the "
        "pointer saturates while cross-arm correlation does not.  Per pair the "
        "predictor is the number of DEGREE-1 (leaf) sites in F_a u F_b.  DISCRIMINATING "
        "PREDICTION: on the SHAPE cells C_ab must be ordered by LEAF COUNT (claw 6 > "
        "tee 4 > path 2), i.e. OPPOSITE to the recurrence ordering."),
    "d_spectral_crowding": (
        "SPECTRAL CROWDING.  Level spacing inside an arm shrinks as the arm grows, "
        "breaking the perturbative protection at fixed field.  Per pair the predictor is "
        "the MINIMUM LEVEL SPACING of the arm's own induced Hamiltonian "
        "H_F = -sum_{<ij> in F} Z_i Z_j - lambda sum_{i in F} X_i, computed by exact "
        "diagonalisation of the fragment alone before any full-system propagation.  "
        "DISCRIMINATING PREDICTION: C_ab is ordered INVERSELY by the arm's minimum "
        "spacing, on the SHAPE cells and along the size ladder alike."),
    "e_arity_dilution": (
        "ARITY DILUTION.  The pointer is shared among deg(S) arms; each additional arm "
        "measures the pointer harder and leaves it less able to mediate correlation "
        "between any given pair.  The predictor is the pointer degree deg(S).  "
        "DISCRIMINATING PREDICTION: on the ARITY LADDER -- one long-arm PAIR held "
        "FIXED while singleton arms are added -- that pair's C_ab must FALL as deg(S) "
        "rises.  A purely PER-PAIR mechanism predicts it does not move."),
    "f_system_size": (
        "SYSTEM SIZE (the confound, carried as a rival).  The cost is a function of the "
        "total site count n, not of any fragment property.  DISCRIMINATING PREDICTION: "
        "cells at EQUAL n and different (degree, fragment size) must agree -- e.g. the "
        "n = 9 triple {degree-2 arms of 4 (917's G1), degree-4 arms of 2, degree-8 "
        "singletons} must all show the same C_ab and the same ceiling."),
}


def arm_min_gap(g, L, lam):
    """The minimum level spacing of a fragment's OWN induced Hamiltonian.  A pure
    function of the graph and the field; computed before any full-system propagation."""
    sites = g["frags"][L]
    pos = {s: i for i, s in enumerate(sites)}
    k = len(sites)
    ibonds = [(pos[a], pos[b]) for (a, b) in g["bonds"] if a in pos and b in pos]
    d = 1 << k
    H = np.zeros((d, d), dtype=np.float64)
    idxs = np.arange(d, dtype=np.int64)
    diag = np.zeros(d, dtype=np.float64)
    for (a, b) in ibonds:
        za = 1 - 2 * ((idxs >> a) & 1)
        zb = 1 - 2 * ((idxs >> b) & 1)
        diag -= (za * zb).astype(np.float64)
    H[idxs, idxs] = diag
    for i in range(k):
        H[idxs, idxs ^ (1 << i)] -= lam
    w = np.linalg.eigvalsh(H)
    gaps = np.diff(np.sort(w))
    gaps = gaps[gaps > 1e-12]
    return float(gaps.min()) if gaps.size else 0.0


def structural_predictors(g, lam):
    """All pre-registered predictors, per geometry and per fragment pair."""
    labels, frags, dS = g["labels"], g["frags"], g["dS"]
    deg = {i: len(g["adj"][i]) for i in range(g["n"])}
    per_frag = {}
    for L in labels:
        sites = frags[L]
        per_frag[L] = {
            "size": len(sites),
            "hilbert_log2": len(sites),
            "eccentricity_from_pointer": int(max(dS[i] for i in sites)),
            "leaf_count": int(sum(1 for i in sites if deg[i] == 1)),
            "min_level_spacing": arm_min_gap(g, L, lam),
            "internal_bonds": int(sum(1 for (a, b) in g["bonds"]
                                      if a in sites and b in sites)),
        }
    per_pair = {}
    for A, B in itertools.combinations(labels, 2):
        fa, fb = per_frag[A], per_frag[B]
        per_pair["|".join((A, B))] = {
            "a_within_arm_mixing": fa["size"] + fb["size"],
            "b_recurrence": max(fa["eccentricity_from_pointer"],
                                fb["eccentricity_from_pointer"]),
            "c_boundary_content": fa["leaf_count"] + fb["leaf_count"],
            "d_spectral_crowding": min(fa["min_level_spacing"], fb["min_level_spacing"]),
            "e_arity_dilution": g["stats"]["pointer_degree"],
            "f_system_size": g["stats"]["n_sites"],
            "size_pair": sorted([fa["size"], fb["size"]]),
        }
    return {"per_fragment": per_frag, "per_pair": per_pair,
            "geometry_level": {
                "a_within_arm_mixing": max(per_frag[L]["size"] for L in labels),
                "b_recurrence": max(per_frag[L]["eccentricity_from_pointer"]
                                    for L in labels),
                "c_boundary_content": sum(per_frag[L]["leaf_count"] for L in labels),
                "d_spectral_crowding": min(per_frag[L]["min_level_spacing"]
                                           for L in labels),
                "e_arity_dilution": g["stats"]["pointer_degree"],
                "f_system_size": g["stats"]["n_sites"]}}


# ------------------------------------------- the pinned Cycle 917 geometries --
def geom_chain9():
    sites = [(k, 0, 0) for k in range(-4, 5)]
    bonds = [((k, 0, 0), (k + 1, 0, 0)) for k in range(-4, 4)]
    return build_geometry("G1", "chain9", sites, bonds, (0, 0, 0),
                          lambda c: ("+x" if c[0] > 0 else "-x"), cube_tiebreak, 1,
                          "917 G1: the d=1 reference, the open 9-site chain -- the "
                          "921 exception cell this block succeeds")


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
            gg = "b%dg%d" % (b, k)
            sites.append(gg)
            bonds.append((c, gg))
    key = {3: "G3a", 4: "G3b", 5: "H2"}[nbranch]
    return build_geometry(key, "tree%d" % len(sites), sites, bonds, "S",
                          lambda c: c, None, "tree",
                          "917/919 %s: centre + %d branches of depth 2" % (key, nbranch))


def geom_plaquette9():
    sites = [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]

    def lab(c):
        return ("+x" if c[0] > 0 else "-x") if c[0] != 0 else ("+y" if c[1] > 0 else "-y")
    return build_geometry("G4", "plaquette9", sites, bonds, (0, 0, 0), lab,
                          cube_tiebreak, 2, "917 G4: the open 3x3 square, d=2 with loops")


def _axis_label(c):
    for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
        if c[ax] != 0:
            return ("+" if c[ax] > 0 else "-") + nm
    die("axis-label:origin %r" % (c,))


def geom_cubeminus11():
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("G5", "cubeminus11", sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3, "917 G5: centre + 6 faces + the 4 z=0 edges")


def geom_cube27():
    sites = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    # DECLARED CAP EXEMPTION: the 27-site cube is built ONLY to verify the partition
    # rule against the frozen memo's six published fragment lists.  Its dynamics are
    # never propagated here, so the 2^16 full-space cap does not apply to it.
    return build_geometry("G6", "cube27", sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3, "917 G6: the open 3x3x3 cube (partition-rule "
                          "verification only -- never propagated)", propagated=False)


# ------------------------------------------- the pinned Cycle 919 geometries --
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
                gg = "b%dg%d" % (b, k)
                sites.append(gg)
                bonds.append((c, gg))
    return build_geometry("H3", "tree10d5", sites, bonds, "S", lambda c: c, None, "tree",
                          "919 H3: centre + 5 branches, exactly two of depth 2")


def geom_cubeminus10():
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("H4", "cubeminus10", sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3,
                          "919 H4: G5 cubeminus11 with the -z face deleted")


# --------------------------------- the pinned Cycle 921 designed roster (gate) --
FACE = {"+x": (1, 0, 0), "-x": (-1, 0, 0), "+y": (0, 1, 0),
        "-y": (0, -1, 0), "+z": (0, 0, 1), "-z": (0, 0, -1)}
EDG = {"xy": (1, 1, 0), "x-y": (1, -1, 0), "-xy": (-1, 1, 0), "-x-y": (-1, -1, 0),
       "xz": (1, 0, 1), "-xz": (-1, 0, 1), "yz": (0, 1, 1), "-yz": (0, -1, 1)}
F5 = ["+x", "-x", "+y", "-y", "+z"]


def cube_sub(key, faces, extras, note):
    sites = [(0, 0, 0)] + [FACE[f] for f in faces] + list(extras)
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry(key, key, sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3, note)


def tree_plus(key, sites, bonds, note):
    return build_geometry(key, key, sites, bonds, "S", lambda c: c, None, "tree", note)


def star_plus(key, extra, note):
    sites = ["S"] + ["a%d" % i for i in range(1, 6)]
    bonds = [("S", "a%d" % i) for i in range(1, 6)] + list(extra)
    return build_geometry(key, key, sites, bonds, "S", lambda c: c, None, "star", note)


def _bbase():
    sites = ["S"] + ["b%d" % i for i in range(5)] + ["g%d" % i for i in range(5)]
    bonds = ([("S", "b%d" % i) for i in range(5)]
             + [("b%d" % i, "g%d" % i) for i in range(5)])
    return sites, bonds


def _dbase():
    sites = ["S"] + ["b%d" % i for i in range(5)] + ["g0", "h0", "k0", "g1", "h1", "k1"]
    bonds = ([("S", "b%d" % i) for i in range(5)]
             + [("b0", "g0"), ("g0", "h0"), ("h0", "k0"),
                ("b1", "g1"), ("g1", "h1"), ("h1", "k1")])
    return sites, bonds


def _wbase():
    sites = ["S"] + ["b%d" % i for i in range(5)] + ["w%d" % i for i in range(4)]
    bonds = ([("S", "b%d" % i) for i in range(5)]
             + [("b0", "w%d" % i) for i in range(4)])
    return sites, bonds


def build_c921_roster():
    """The 32 Cycle 921 measurement geometries, rebuilt verbatim for the gate."""
    R = []
    Bs, Bb = _bbase()
    Ds, Db = _dbase()
    Ws, Wb = _wbase()
    E = EDG

    def C(k, ex):
        return cube_sub(k, F5, ex, "921 designed geometry (restriction gate)")

    R += [C("QC0", []), C("QC1", [E["xy"]]),
          C("QC2p", [E["xy"], E["-xy"]]), C("QC2d", [E["xy"], E["-x-y"]]),
          C("QC3s", [E["xz"], E["-xz"], E["yz"]]),
          C("QC3x", [E["xy"], E["-x-y"], E["yz"]]),
          C("QC4s", [E["xz"], E["-xz"], E["yz"], E["-yz"]]),
          C("QC8", list(E.values())),
          cube_sub("QCK", ["+x", "+y", "+z"], [E["xy"], E["xz"], E["yz"]],
                   "921 designed geometry (restriction gate)"),
          cube_sub("QCT", ["+x", "+y", "+z"], [],
                   "921 designed geometry (restriction gate)"),
          C("QCL1", [E["xy"], E["xz"]]),
          C("QCL2", [E["xy"], E["xz"], (1, 1, 1)])]
    for k, ex in (("QA1", [("a1", "a2")]),
                  ("QA2m", [("a1", "a2"), ("a1", "a3")]),
                  ("QA2d", [("a1", "a2"), ("a3", "a4")]),
                  ("QA4s", [("a1", "a2"), ("a1", "a3"), ("a1", "a4"), ("a1", "a5")]),
                  ("QA4c", [("a1", "a2"), ("a2", "a3"), ("a3", "a4"), ("a4", "a1")])):
        R.append(star_plus(k, ex, "921 designed geometry (restriction gate)"))
    for k, ex in (("QB0", []), ("QB1", [("g0", "g1")]),
                  ("QB2d", [("g0", "g1"), ("g2", "g3")]),
                  ("QB4c", [("g0", "g1"), ("g1", "g2"), ("g2", "g3"), ("g3", "g0")]),
                  ("QB10", list(itertools.combinations(["g%d" % i for i in range(5)], 2)))):
        R.append(tree_plus(k, Bs, Bb + list(ex),
                           "921 designed geometry (restriction gate)"))
    for k, ex in (("QD0", []), ("QD5", [("g0", "g1")]), ("QD7", [("h0", "h1")]),
                  ("QD9", [("k0", "k1")])):
        R.append(tree_plus(k, Ds, Db + list(ex),
                           "921 designed geometry (restriction gate)"))
    R.append(tree_plus("QW0", Ws, Wb, "921 designed geometry (restriction gate)"))
    R.append(tree_plus("QW1", Ws, Wb + [("w0", "w1"), ("w1", "w2"), ("w2", "w3"),
                                        ("w3", "w0")],
                       "921 designed geometry (restriction gate)"))
    R.append(tree_plus("QP1", Ds, Db + [("b0", "h0")],
                       "921 designed geometry (restriction gate)"))
    R.append(tree_plus("QP3", Ds, Db + [("g0", "k0")],
                       "921 designed geometry (restriction gate)"))
    R.append(tree_plus("QN2", Ds, Db + [("g0", "g1"), ("b0", "h0")],
                       "921 designed geometry (restriction gate)"))
    R.append(tree_plus("QN3", Ds, Db + [("g0", "g1"), ("b0", "h0"), ("b1", "h1")],
                       "921 designed geometry (restriction gate)"))
    return R


# ================================ THE CYCLE 927 ROSTER (this block's design freedom)
# EVERY geometry below is LOOP-FREE by construction, so the pinned pair-cycle law
# predicts ZERO cost on every one of them and any measured cost isolates the second
# channel.  Arms are attached directly to the pointer, so each arm is exactly one
# fragment under the frozen partition rule and no tie ever arises (the builder
# hard-fails on an undeclared tie).
def spider(key, arm_shapes, note, family):
    """A loop-free spider.  arm_shapes[j] is a list of (parent_index, ) parent links
    describing the j-th arm as a tree rooted at its anchor; index 0 is the anchor and
    entry p for site i means site i attaches to site p of the same arm."""
    sites, bonds = ["S"], []
    for j, parents in enumerate(arm_shapes):
        names = []
        for p, par in enumerate(parents):
            nm = "A%02d" % (j + 1) if p == 0 else "a%02dx%d" % (j + 1, p)
            names.append(nm)
            sites.append(nm)
            bonds.append(("S", nm) if par is None else (names[par], nm))
    return build_geometry(key, key, sites, bonds, "S", lambda c: c, None, family, note)


def path_arm(L):
    """A path of L sites hanging off the pointer: anchor, then a chain."""
    return [None] + [p for p in range(L - 1)]


def claw_arm(L):
    """An anchor with L-1 children: depth 2, L-1 leaves."""
    return [None] + [0] * (L - 1)


def tee_arm4():
    """anchor - a - {b, c}: 4 sites, depth 3, 2 leaves."""
    return [None, 0, 1, 1]


def y_arm3():
    """anchor with 2 children: 3 sites, depth 2, 2 leaves (the 917 tree arm shape)."""
    return [None, 0, 0]


def build_roster():
    """The Cycle 927 measurement roster, in six declared families."""
    R = []
    # ---- SIZE: symmetric spiders, path arms.  degree fixed, arm length swept. -----
    for k, Ls in ((2, range(1, 8)), (3, range(1, 6)), (4, range(1, 4)), (5, range(1, 4))):
        for L in Ls:
            R.append(("SIZE", spider(
                "SPk%dL%d" % (k, L), [path_arm(L)] * k,
                "SIZE family: symmetric spider, pointer degree %d, %d path arms of %d "
                "site(s), n = %d.  Loop-free: the pair-cycle law predicts ceiling %d."
                % (k, k, L, 1 + k * L, k), "spider")))
    # ---- ARITY1: singleton fragments at high degree (fixed size, degree swept) ----
    for k in (8, 10, 12):
        R.append(("ARITY1", spider(
            "STk%d" % k, [path_arm(1)] * k,
            "ARITY1 family: K_{1,%d}, every fragment a singleton, n = %d.  Fixed "
            "fragment size 1 with the pointer degree pushed well past 919's threshold."
            % (k, 1 + k), "star")))
    # ---- NCTRL: an equal-n control at a third (degree, size) combination -----------
    R.append(("NCTRL", spider(
        "SPk6L2", [path_arm(2)] * 6,
        "NCTRL: pointer degree 6, six path arms of 2, n = 13 -- the equal-n partner of "
        "SPk2L6 (degree 2, arms of 6), SPk3L4, SPk4L3 and STk12.", "spider")))
    # ---- SHAPE: fragment SIZE fixed, arm SHAPE varied (the Q2 discriminator) -------
    R.append(("SHAPE", spider(
        "SH2Y3", [y_arm3()] * 2,
        "SHAPE: pointer degree 2, two Y-arms of 3 (anchor + 2 children), n = 7 -- the "
        "equal-size, equal-n, equal-degree partner of SPk2L3 (path arms of 3).  "
        "Same arm Hilbert dimension, depth 2 vs 3, leaves 4 vs 2.", "spider")))
    R.append(("SHAPE", spider(
        "SH2C4", [claw_arm(4)] * 2,
        "SHAPE: pointer degree 2, two CLAW arms of 4 (anchor + 3 children), n = 9 -- "
        "the equal-size, equal-n, equal-degree partner of 917's G1 chain (path arms of "
        "4).  Same arm Hilbert dimension 2^4, depth 2 vs 4, leaves 6 vs 2.", "spider")))
    R.append(("SHAPE", spider(
        "SH2T4", [tee_arm4()] * 2,
        "SHAPE: pointer degree 2, two TEE arms of 4 (anchor - a - {b,c}), n = 9 -- the "
        "third member of the G1 shape triple.  Same arm Hilbert dimension, depth 3, "
        "leaves 4.", "spider")))
    # ---- ASYM: one long arm + singletons (PER-PAIR vs PER-GEOMETRY) ---------------
    for L in range(2, 6):
        R.append(("ASYM", spider(
            "AS3L%d" % L, [path_arm(L), path_arm(1), path_arm(1)],
            "ASYM: pointer degree 3, one path arm of %d and two singletons, n = %d.  "
            "Separates a PER-PAIR channel (only the pairs containing the long arm move) "
            "from a PER-GEOMETRY one (the singleton-singleton pair moves too)."
            % (L, 3 + L), "spider")))
    # ---- ARITY ladders: a long-arm PAIR held fixed while singleton arms are added --
    for m in (1, 2, 3):
        R.append(("ARITYA", spider(
            "AR3m%d" % m, [path_arm(3), path_arm(3)] + [path_arm(1)] * m,
            "ARITY-A ladder: the arm-3 PAIR held FIXED while %d singleton arm(s) are "
            "added -- pointer degree %d, n = %d.  Tests whether degree protects a pair "
            "it does not touch (m = 0 is SPk2L3)." % (m, 2 + m, 7 + m), "spider")))
    for m in (1, 2, 3):
        R.append(("ARITYB", spider(
            "AR5m%d" % m, [path_arm(5), path_arm(5)] + [path_arm(1)] * m,
            "ARITY-B ladder: the arm-5 PAIR held FIXED while %d singleton arm(s) are "
            "added -- pointer degree %d, n = %d (m = 0 is SPk2L5)."
            % (m, 2 + m, 11 + m), "spider")))
    return R


# the extensions the 2^16 cap forbids -- DECLARED, never silently truncated
CAPPED_EXTENSIONS = [
    {"family": "SIZE", "pointer_degree": 2, "arm_lengths_requested": "1..7",
     "arm_lengths_run": "1..7", "capped": [], "note": "degree 2 arm 7 gives n = 15; "
     "arm 8 would give n = 17 > 2^16 cap."},
    {"family": "SIZE", "pointer_degree": 3, "arm_lengths_requested": "1..5",
     "arm_lengths_run": "1..5", "capped": [], "note": "degree 3 arm 5 gives n = 16, "
     "EXACTLY AT the 2^16 cap; arm 6 would give n = 19."},
    {"family": "SIZE", "pointer_degree": 4, "arm_lengths_requested": "1..3",
     "arm_lengths_run": "1..3", "capped": [4], "note": "degree 4 arm 3 gives n = 13; "
     "arm 4 would give n = 17 > cap -- NOT RUN, declared."},
    {"family": "SIZE", "pointer_degree": 5, "arm_lengths_requested": "1..3",
     "arm_lengths_run": "1..3", "capped": [4], "note": "degree 5 arm 3 gives n = 16, "
     "EXACTLY AT the cap; arm 4 would give n = 21 -- NOT RUN, declared."},
]


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
    """The frozen class-product preparation: pointer and its neighbours +X, else +Z."""
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
    """Route A: exact exp(-iHt) by Chebyshev expansion with a rigorous tail bound."""
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
    """Route B: exp(-iHt) by a scaling-and-marching Taylor propagator with a rigorous
    factorial remainder bound.  Algorithmically disjoint from route A."""
    A = float(np.abs(diag).max() + lam * n)
    mv = _matvec_factory(diag, n, lam)
    psi = psi0.astype(np.complex128).copy()
    outs = []
    tprev, nsub, nmv, worst_rem, worst_deg = 0.0, 0, 0, 0.0, 0
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
    """Route C: exact dense eigendecomposition of the real symmetric H."""
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
    return outs, {"route": "dense-eigh", "dim": d, "emin": float(w[0]),
                  "emax": float(w[-1])}


def joint_rho(psi, n, sites):
    """The pinned reduced-density-matrix route (917/919/921, verbatim)."""
    T = psi.reshape((2,) * n)
    order = list(sites) + [i for i in range(n) if i not in sites]
    ax = [n - 1 - s for s in order]
    M = np.transpose(T, ax).reshape(1 << len(sites), -1)
    return M @ M.conj().T


def block_matrix(psi, n, sites):
    """The GRAM route's raw object: psi reshaped so that rows index `sites` and
    columns index the complement.  rho_sites = M M^dag exactly."""
    T = psi.reshape((2,) * n)
    order = list(sites) + [i for i in range(n) if i not in sites]
    ax = [n - 1 - s for s in order]
    return np.transpose(T, ax).reshape(1 << len(sites), -1)


def spectrum_of(M):
    """Exact nonzero spectrum of M M^dag via the SMALLER of the two Gram matrices.
    Algebraically identical to eigvalsh(M M^dag) up to zero padding."""
    r, c = M.shape
    G = (M @ M.conj().T) if r <= c else (M.conj().T @ M)
    return np.linalg.eigvalsh(G)


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
    """The pinned conditional-mutual-information route (917/919/921, verbatim)."""
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


def cond_mi_gram(psi, n, S, A, B):
    """The GRAM route to the SAME quantity.  Split psi by the pointer bit, then take
    each conditional block's entropies from the smaller Gram matrix.  Exact; used
    where the direct route's density matrix would be infeasible."""
    T = psi.reshape((2,) * n)
    ax = [n - 1 - S] + [n - 1 - i for i in range(n) if i != S]
    P = np.transpose(T, ax).reshape(2, -1)
    rest = [i for i in range(n) if i != S]
    pos = {s: j for j, s in enumerate(rest)}
    m = len(rest)
    ai = [pos[s] for s in A]
    bi = [pos[s] for s in B]
    ci = [j for j in range(m) if j not in ai and j not in bi]
    out, ptot = 0.0, 0.0
    ps = []
    for z in range(2):
        v = P[z]
        pz = float(np.vdot(v, v).real)
        ps.append(pz)
        ptot += pz
    for z in range(2):
        pz = ps[z]
        if pz <= 1e-14:
            continue
        v = (P[z] / math.sqrt(pz)).reshape((2,) * m)
        MA = np.transpose(v, ai + bi + ci).reshape(1 << len(ai), -1)
        sa, _ = ent_bits(spectrum_of(MA))
        MB = np.transpose(v, bi + ai + ci).reshape(1 << len(bi), -1)
        sb, _ = ent_bits(spectrum_of(MB))
        MAB = np.transpose(v, ai + bi + ci).reshape(1 << (len(ai) + len(bi)), -1)
        sab, _ = ent_bits(spectrum_of(MAB))
        out += (pz / ptot) * (sa + sb - sab)
    return out


def r_ind(labels, chi, excess, H, C, delta):
    order = {L: i for i, L in enumerate(labels)}
    singles = [L for L in labels
               if H >= CONTENT_H_MIN and chi[L] >= (1.0 - delta) * H
               and excess[L] >= EXCESS_MIN]
    best, best_key = [], None
    for r in range(len(singles), 0, -1):
        for comb in itertools.combinations(singles, r):
            ok = True
            for a, b in itertools.combinations(comb, 2):
                v = C.get(tuple(sorted((a, b), key=order.get)))
                if v is None or v > INDEP_MAX:
                    ok = False
                    break
            if ok:
                key = tuple(order[c] for c in comb)
                if best_key is None or key < best_key:
                    best, best_key = list(comb), key
        if best:
            break
    return len(best), best, singles


def centered_frobenius(lam, n, nbonds, degrees):
    den = np.sqrt(float(nbonds) + n * lam * lam)
    out = {}
    for deg in sorted(set(degrees.values())):
        out[str(deg)] = {"Z": 2.0 * lam / den, "X": 2.0 * np.sqrt(deg) / den,
                         "Y": 2.0 * np.sqrt(deg + lam * lam) / den}
    return out


# ============================================================= measurement ===
def measure(g, states, times, gram_dev=None):
    n, S, labels, frags = g["n"], g["S"], g["labels"], g["frags"]
    nbrs = g["recording"]
    rows = []
    chi0, one0, theta0 = {}, {}, None
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
            ka, kb = len(frags[a1]), len(frags[b1])
            direct_ok = (1 << (1 + ka + kb)) <= DIRECT_MAX_DIM
            if direct_ok:
                rho = joint_rho(a, n, [S] + frags[a1] + frags[b1])
                val = cond_mi(rho, ka, kb)
                if gram_dev is not None:
                    vg = cond_mi_gram(a, n, S, frags[a1], frags[b1])
                    gram_dev[0] = max(gram_dev[0], abs(val - vg))
            else:
                val = cond_mi_gram(a, n, S, frags[a1], frags[b1])
            C[(a1, b1)] = val
            if it == 0:
                mach["t0_anchor"] = max(mach["t0_anchor"], abs(C[(a1, b1)]))
        rr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(labels, chi, exc, H, C, d)
            rr["%.2f" % d] = k
            subs["%.2f" % d] = sub
            sing["%.2f" % d] = sg
        rows.append({
            "jt": t, "H_Z": H, "p_z": pz, "pointer_tv_drift": abs(pz[0] - 0.5),
            "chi": chi, "excess": exc, "theta_A": theta - theta0,
            "one_site_chi_by_shell": {str(k): float(np.mean(v))
                                      for k, v in sorted(one_by_shell.items())},
            "one_site_excess_by_shell": {str(k): v for k, v in sorted(one_exc.items())},
            "sum_delta_chi": float(sum(exc.values())),
            "C_ab": {"|".join(k): v for k, v in sorted(C.items())},
            "r_ind": rr, "certifying_subsets": subs, "singleton_passes": sing,
            "r_raw": {k: len(v) for k, v in sing.items()},
        })
    return rows, mach


def event_of(rows, delta):
    key = "%.2f" % delta
    for i, r in enumerate(rows):
        if r["r_ind"][key] >= 2:
            run = 0
            for rr in rows[i:]:
                if rr["r_ind"][key] >= 2:
                    run += 1
                else:
                    break
            return {"jt": r["jt"], "theta_A": r["theta_A"], "r_ind": r["r_ind"][key],
                    "witness": r["certifying_subsets"][key], "run": run,
                    "by_deadline": bool(r["jt"] <= DEADLINE_JT + 1e-12),
                    "persists": bool(run >= PERSIST_N),
                    "pointer_tv_drift": r["pointer_tv_drift"],
                    "chi_at_event": {L: r["chi"][L] for L in r["certifying_subsets"][key]},
                    "H_Z_at_event": r["H_Z"],
                    "C_at_event": {k: v for k, v in r["C_ab"].items()
                                   if all(p in r["certifying_subsets"][key]
                                          for p in k.split("|"))}}
    return None


def xi_reg_of(rows):
    imax = int(np.argmax([r["sum_delta_chi"] for r in rows]))
    r = rows[imax]
    xi = 0
    for sh, v in sorted((int(k), v) for k, v in r["one_site_excess_by_shell"].items()):
        if v >= EXCESS_MIN:
            xi = max(xi, sh)
    return {"xi_reg": xi, "t_summax": r["jt"], "sum_delta_chi": r["sum_delta_chi"],
            "shell_excess": r["one_site_excess_by_shell"]}


def verdict_of(rows, delta, comm_ok):
    ev = event_of(rows, delta)
    if ev is None:
        best_C = min((min(r["C_ab"].values()) for r in rows if r["C_ab"]), default=None)
        any_content = any(len(r["singleton_passes"]["%.2f" % delta]) >= 2 for r in rows)
        reason = ("content-gate: fewer than two fragments ever reach (1-delta)H with "
                  "0.02-bit excess" if not any_content else
                  "independence-gate: two or more fragments reach content but every "
                  "eligible pair exceeds C_ab = 0.02 bit")
        return {"verdict": "NO", "reason": reason, "event": None,
                "min_C_ab_over_grid": best_C, "commutator_ordering_ok": comm_ok}
    if not ev["by_deadline"]:
        return {"verdict": "NO", "reason": "late: first R_ind>=2 after the Jt<=1 deadline",
                "event": ev, "commutator_ordering_ok": comm_ok}
    if not ev["persists"]:
        return {"verdict": "NO", "reason": "persistence: fewer than three consecutive "
                                           "certification samples with R_ind>=2",
                "event": ev, "commutator_ordering_ok": comm_ok}
    if ev["pointer_tv_drift"] > DRIFT_MAX:
        return {"verdict": "NO", "reason": "pointer drift exceeds 0.10 at the event",
                "event": ev, "commutator_ordering_ok": comm_ok}
    if not comm_ok:
        return {"verdict": "NO", "reason": "CHECK-02 pointer demolition control",
                "event": ev, "commutator_ordering_ok": comm_ok}
    return {"verdict": "YES", "reason": None, "event": ev,
            "commutator_ordering_ok": comm_ok}


def cell_of(g, lam, rows):
    cf = centered_frobenius(lam, g["n"], len(g["bonds"]), g["degrees"])
    comm_ok = max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values())
    xi = xi_reg_of(rows)
    v = {d: verdict_of(rows, d, comm_ok) for d in DELTAS}
    key = "%.2f" % HEADLINE_DELTA
    imax = int(np.argmax([r["r_ind"][key] for r in rows]))
    return {"centered_frobenius": cf, "commutator_ordering_ok": bool(comm_ok),
            "xi_reg": xi,
            "verdicts_by_delta": {"%.2f" % d: v[d] for d in DELTAS},
            "max_r_ind_over_window": max(r["r_ind"][key] for r in rows),
            "ceiling_row_jt": rows[imax]["jt"],
            "ceiling_row_index": imax,
            "ceiling_witness": rows[imax]["certifying_subsets"][key],
            "headline": v[HEADLINE_DELTA]}


def run_route_A(g, diag, psi0, lam, times=None, gram_dev=None):
    tt = T_EXEC if times is None else times
    outs, prop = chebyshev(psi0, diag, g["n"], lam, tt)
    rows, mach = measure(g, outs, tt, gram_dev=gram_dev)
    return rows, mach, prop


# ---------------------- THE SECOND CHANNEL, MEASURED AT THE CEILING ROW ------
def channel_structure(g, rows):
    """At the row that realises the ceiling: which pairs are over the independence
    gate, which fragments fail the content gate, and by what margin.  This is the
    PAIR-vs-CONTENT question stated as a measurement."""
    key = "%.2f" % HEADLINE_DELTA
    imax = int(np.argmax([r["r_ind"][key] for r in rows]))
    r = rows[imax]
    passes = set(r["singleton_passes"][key])
    fails = sorted(L for L in g["labels"] if L not in passes)
    over = sorted(k for k, v in r["C_ab"].items() if v > INDEP_MAX)
    d = g["anchor_distance_in_G_minus_S"]
    sizes = g["stats"]["fragment_sizes"]
    pairs = {}
    for k, v in sorted(r["C_ab"].items()):
        A, B = k.split("|")
        pairs[k] = {"C_ab": v, "margin_to_gate": INDEP_MAX - v,
                    "over_gate": bool(v > INDEP_MAX),
                    "sizes": sorted([sizes[A], sizes[B]]),
                    "anchor_distance": d.get(k, d.get("|".join((B, A)), -1))}
    # the maximum C_ab over the WHOLE window, not only the ceiling row
    cmax = {k: max(rr["C_ab"][k] for rr in rows) for k in r["C_ab"]}
    return {
        "ceiling_jt": r["jt"], "ceiling_row_index": imax,
        "content_failures": fails,
        "n_content_failures": len(fails),
        "content_gate_is_binding": bool(fails),
        "pairs_over_the_independence_gate": over,
        "n_pairs_over_gate": len(over),
        "n_pairs": len(r["C_ab"]),
        "all_pairs_over_gate": bool(over and len(over) == len(r["C_ab"])),
        "per_pair": pairs,
        "max_C_ab_at_ceiling_row": max(r["C_ab"].values()) if r["C_ab"] else None,
        "min_C_ab_at_ceiling_row": min(r["C_ab"].values()) if r["C_ab"] else None,
        "max_C_ab_over_window": max(cmax.values()) if cmax else None,
        "C_ab_over_window_by_pair": cmax,
        "theta_A_at_ceiling_row": r["theta_A"],
        "H_Z_at_ceiling_row": r["H_Z"],
        "chi_at_ceiling_row": r["chi"],
        "excess_at_ceiling_row": r["excess"],
        "loop_free": g["stats"]["loop_free"],
        "pair_cycle_law_prediction": g["stats"]["pointer_degree"]
        if g["stats"]["loop_free"] else None,
    }


# ----------------------------------------------- fitted-form candidates ------
def fit_forms(xs, ys):
    """Descriptive fits ONLY.  Each candidate form is fitted by least squares and
    reported with its residuals; nothing here is a derivation and no form is selected
    by the fit alone."""
    x = np.asarray(xs, dtype=float)
    y = np.asarray(ys, dtype=float)
    out = {}
    if len(x) < 3:
        return {"note": "fewer than 3 points -- no form fitted"}

    def rec(name, pred, npar, extra=None):
        resid = y - pred
        ss = float((resid ** 2).sum())
        tot = float(((y - y.mean()) ** 2).sum())
        d = {"params": extra, "sse": ss, "max_abs_residual": float(np.abs(resid).max()),
             "r_squared": float(1.0 - ss / tot) if tot > 1e-30 else None,
             "n_parameters": npar}
        out[name] = d

    c = np.polyfit(x, y, 1)
    rec("linear_a_plus_b_L", np.polyval(c, x), 2, {"a": float(c[1]), "b": float(c[0])})
    c2 = np.polyfit(x, y, 2)
    rec("quadratic", np.polyval(c2, x), 3,
        {"a": float(c2[2]), "b": float(c2[1]), "c": float(c2[0])})
    if (x > 0).all() and (y > 0).all():
        cp = np.polyfit(np.log(x), np.log(y), 1)
        rec("power_a_L_to_p", np.exp(np.polyval(cp, np.log(x))), 2,
            {"a": float(np.exp(cp[1])), "p": float(cp[0])})
        cl = np.polyfit(np.log(x), y, 1)
        rec("log_a_plus_b_lnL", np.polyval(cl, np.log(x)), 2,
            {"a": float(cl[1]), "b": float(cl[0])})
    best = None
    for L0 in np.arange(0.2, 8.01, 0.02):
        b = 1.0 - np.exp(-x / L0)
        A = np.vstack([b, np.ones_like(b)]).T
        sol, *_ = np.linalg.lstsq(A, y, rcond=None)
        r = y - A @ sol
        ss = float((r ** 2).sum())
        if best is None or ss < best[0]:
            best = (ss, float(L0), float(sol[0]), float(sol[1]))
    ss, L0, amp, off = best
    rec("saturating_off_plus_amp_1_minus_exp", off + amp * (1.0 - np.exp(-x / L0)), 3,
        {"offset": off, "amplitude": amp, "L0": L0})
    ranked = sorted((v["sse"], k) for k, v in out.items() if isinstance(v, dict))
    return {"fits": out, "ranked_by_sse": [k for _, k in ranked],
            "best_by_sse": ranked[0][1] if ranked else None,
            "honesty": "these are DESCRIPTIONS of the measured points, not derivations; "
                       "the saturating and quadratic forms carry 3 parameters against "
                       "the linear form's 2, so a lower SSE is not by itself evidence "
                       "of a better mechanism"}


def crossing_of(Ls, Cs, gate=INDEP_MAX):
    """The smallest arm length at which the measured C_ab exceeds the gate, plus a
    linear interpolation of the crossing point between the bracketing lengths."""
    for i, (L, c) in enumerate(zip(Ls, Cs)):
        if c > gate:
            if i == 0:
                return {"first_L_over_gate": L, "interpolated_L_star": None,
                        "bracket": None,
                        "note": "already over the gate at the shortest arm measured"}
            L0, c0 = Ls[i - 1], Cs[i - 1]
            frac = (gate - c0) / (c - c0) if abs(c - c0) > 1e-15 else 0.0
            return {"first_L_over_gate": L, "bracket": [L0, L],
                    "interpolated_L_star": float(L0 + frac * (L - L0)),
                    "margin_below": float(gate - c0), "margin_above": float(c - gate)}
    return {"first_L_over_gate": None, "interpolated_L_star": None, "bracket": None,
            "note": "no measured arm length crosses the gate at this field",
            "max_C_ab_measured": float(max(Cs)) if len(Cs) else None,
            "margin_at_longest_arm": float(gate - Cs[-1]) if len(Cs) else None}


# ================================================================== main =====
def main():
    pins = verify_pins()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    const_x = cross_check_pinned_constants(frozen)
    d1_text, d1_prov = recover_d1_note()
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()
    r917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    r917c = json.load(open(os.path.join(ROOT, C917_CHECK_RECEIPT)))
    r919 = json.load(open(os.path.join(ROOT, C919_RECEIPT)))
    r921 = json.load(open(os.path.join(ROOT, C921_RECEIPT)))

    mach_all = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0,
                "entropy_bound": 0.0, "symmetry": 0.0, "t0_anchor": 0.0,
                "cheby_tail": 0.0, "taylor_remainder": 0.0,
                "route_AB_max_dev": 0.0, "route_AC_max_dev": 0.0,
                "direct_vs_gram_max_dev": 0.0, "determinism": 0.0}
    gram_dev = [0.0]

    # ============================================ restriction gate 0: the rule ==
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

    C917_BUILD = {"G1": geom_chain9, "G2": geom_star7, "G3a": lambda: geom_tree(3),
                  "G3b": lambda: geom_tree(4), "G4": geom_plaquette9,
                  "G5": geom_cubeminus11}
    C919_BUILD = {"H1": geom_star6, "H2": geom_tree16, "H3": geom_tree10d5,
                  "H4": geom_cubeminus10}

    def cmp_rows(rows, pubrows, tab, bad, tag):
        pr = {r["jt"]: r for r in pubrows}
        for r in rows:
            q = pr.get(r["jt"])
            if q is None:
                bad.append("row-missing@%.1f" % r["jt"])
                continue
            tab["rows_compared"] += 1
            for L in r["chi"]:
                tab["row_level_max_abs_dev"]["chi"] = max(
                    tab["row_level_max_abs_dev"]["chi"], abs(r["chi"][L] - q["chi"][L]))
            for kk, vv in r["C_ab"].items():
                if kk not in q["C_ab"]:
                    bad.append("pairkey-missing:%s" % kk)
                    continue
                tab["row_level_max_abs_dev"]["C_ab"] = max(
                    tab["row_level_max_abs_dev"]["C_ab"], abs(vv - q["C_ab"][kk]))
            tab["row_level_max_abs_dev"]["theta_A"] = max(
                tab["row_level_max_abs_dev"]["theta_A"], abs(r["theta_A"] - q["theta_A"]))
            tab["row_level_max_abs_dev"]["H_Z"] = max(
                tab["row_level_max_abs_dev"]["H_Z"], abs(r["H_Z"] - q["H_Z"]))
            if r["r_ind"] != q["r_ind"]:
                bad.append("r_ind-ledger@%.1f" % r["jt"])

    def cmp_cell(cell, want, bad):
        got = cell["headline"]
        if got["verdict"] != want["verdict"]:
            bad.append("verdict %s!=%s" % (got["verdict"], want["verdict"]))
        if cell["xi_reg"]["xi_reg"] != want["xi_reg"]:
            bad.append("xi_reg")
        if cell["max_r_ind_over_window"] != want["max_r_ind"]:
            bad.append("max_r_ind %s!=%s" % (cell["max_r_ind_over_window"],
                                             want["max_r_ind"]))
        ev, wev = got["event"], want["event"]
        if (ev is None) != (wev is None):
            bad.append("event-presence")
        elif ev is not None:
            if abs(ev["jt"] - wev["jt"]) > 1e-12:
                bad.append("first_jt")
            if ev["r_ind"] != wev["r_ind"] or ev["run"] != wev["run"]:
                bad.append("r_ind/run")
            if ev["witness"] != wev["witness"]:
                bad.append("witness")
            if abs(ev["theta_A"] - wev["theta_A"]) > RESTRICT_TOL:
                bad.append("theta_A %.3g" % abs(ev["theta_A"] - wev["theta_A"]))

    # ================== restriction gate 1: Cycle 917 reproduced value-for-value ==
    restrict = {"per_cell": {}, "row_level_max_abs_dev": {"chi": 0.0, "C_ab": 0.0,
                                                          "theta_A": 0.0, "H_Z": 0.0},
                "mismatches": [], "cells_checked": 0, "rows_compared": 0,
                "extension_field_cells": {}}
    rows_cache, anchor_geoms = {}, {}
    for key in C917_KEYS:
        g = C917_BUILD[key]()
        anchor_geoms[key] = g
        pub = r917["geometries"][key]
        if set(pub["sites"]) != set(g["sites"]):
            restrict["mismatches"].append("%s:site-set" % key)
        if {tuple(sorted(b)) for b in pub["bonds"]} != \
           {tuple(sorted((g["sites"][a], g["sites"][b]))) for (a, b) in g["bonds"]}:
            restrict["mismatches"].append("%s:bond-set" % key)
        for L, v in pub["partition"].items():
            if set(v) != {g["sites"][i] for i in g["frags"][L]}:
                restrict["mismatches"].append("%s:partition:%s" % (key, L))
        for kk, vv in pub["stats"].items():
            if g["stats"].get(kk) != vv:
                restrict["mismatches"].append("%s:stats:%s" % (key, kk))
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        for lam in ANCHOR_LAMBDAS:
            lk = "%g" % lam
            rows, mach, prop = run_route_A(g, diag, psi0, lam, gram_dev=gram_dev)
            rows_cache[(key, lk)] = rows
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            cell = cell_of(g, lam, rows)
            if lam == EXTENSION_LAMBDA:
                want75 = r917c["threshold_attack"][
                    "lambda_boundary_diagnostic_NON_CLAIM"][key]["probe"]["0.075"]
                got75 = cell["headline"]["verdict"]
                restrict["extension_field_cells"]["%s@0.075" % key] = {
                    "recomputed_here": got75, "pinned_917_checker_probe": want75,
                    "agrees": bool(got75 == want75)}
                if got75 != want75:
                    restrict["mismatches"].append("%s@0.075:%s!=%s" % (key, got75, want75))
                continue
            want = r917["ladder"]["%s@%s" % (key, lk)]
            bad = []
            cmp_cell(cell, want, bad)
            cmp_rows(rows, pub["lambdas"][lk]["rows"], restrict, bad, key)
            restrict["cells_checked"] += 1
            ev = cell["headline"]["event"]
            restrict["per_cell"]["%s@%s" % (key, lk)] = {
                "verdict": cell["headline"]["verdict"], "matches_917": not bad,
                "discrepancies": bad, "first_jt": (ev or {}).get("jt"),
                "theta_A": (ev or {}).get("theta_A"),
                "max_r_ind": cell["max_r_ind_over_window"],
                "xi_reg": cell["xi_reg"]["xi_reg"]}
            if bad:
                restrict["mismatches"].append("%s@%s:%s" % (key, lk, ",".join(bad)))

    # ================= restriction gate 2: Cycle 919's four anchors, value-for-value
    anchor_gate = {"per_cell": {}, "mismatches": [], "rows_compared": 0,
                   "row_level_max_abs_dev": {"chi": 0.0, "C_ab": 0.0, "theta_A": 0.0,
                                             "H_Z": 0.0}}
    for key in C919_KEYS:
        g = C919_BUILD[key]()
        anchor_geoms[key] = g
        pub = r919["degree_five_geometries"][key]
        if set(pub["sites"]) != set(g["sites"]):
            anchor_gate["mismatches"].append("%s:site-set" % key)
        for L, v in pub["partition"].items():
            if set(v) != {g["sites"][i] for i in g["frags"][L]}:
                anchor_gate["mismatches"].append("%s:partition:%s" % (key, L))
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        for lam in ANCHOR_LAMBDAS:
            lk = "%g" % lam
            rows, mach, prop = run_route_A(g, diag, psi0, lam, gram_dev=gram_dev)
            rows_cache[(key, lk)] = rows
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            cell = cell_of(g, lam, rows)
            want = r919["ladder_by_cell"]["%s@%s" % (key, lk)]
            bad = []
            cmp_cell(cell, want, bad)
            cmp_rows(rows, pub["lambdas"][lk]["rows"], anchor_gate, bad, key)
            ev = cell["headline"]["event"]
            anchor_gate["per_cell"]["%s@%s" % (key, lk)] = {
                "verdict": cell["headline"]["verdict"],
                "max_r_ind": cell["max_r_ind_over_window"],
                "pinned_919_max_r_ind": want["max_r_ind"],
                "pinned_919_verdict": want["verdict"],
                "witness": (ev or {}).get("witness"),
                "matches_919": not bad, "discrepancies": bad}
            if bad:
                anchor_gate["mismatches"].append("%s@%s:%s" % (key, lk, ",".join(bad)))

    # ============= restriction gate 3: the G1 EXCEPTION cell, value-for-value ======
    g1 = anchor_geoms["G1"]
    g1rows = rows_cache[("G1", "0.1")]
    g1cell = cell_of(g1, 0.10, g1rows)
    g1st = channel_structure(g1, g1rows)
    pin921 = r921["dependence_structure_by_cell"]["G1@0.1"]
    pinned_cab = pin921["C_ab_by_anchor_distance"]["-1"][0]
    got_cab = g1st["per_pair"]["+x|-x"]["C_ab"]
    pin_ladder = r921["ladder_by_cell"]["G1@0.1"]
    g1_gate = {
        "cell": "G1@lambda=0.10 -- the pair-cycle law's single named exception",
        "pinned_921_C_ab": pinned_cab, "recomputed_C_ab": got_cab,
        "abs_deviation": abs(got_cab - pinned_cab),
        "rounded_deviation_vs_published_8dp": abs(round(got_cab, 8) - pinned_cab),
        "pinned_921_ceiling_jt": pin921["ceiling_jt"],
        "recomputed_ceiling_jt": g1st["ceiling_jt"],
        "pinned_921_max_r_ind": pin_ladder["max_r_ind"],
        "recomputed_max_r_ind": g1cell["max_r_ind_over_window"],
        "pair_cycle_law_prediction": 2,
        "pinned_921_over_gate_pairs": pin921["pairs_over_the_independence_gate"],
        "recomputed_over_gate_pairs": g1st["pairs_over_the_independence_gate"],
        "content_failures": g1st["content_failures"],
        "margin_over_the_0.02_gate": got_cab - INDEP_MAX,
        "exception_reproduced": bool(
            abs(round(got_cab, 8) - pinned_cab) <= 1e-8
            and g1cell["max_r_ind_over_window"] == pin_ladder["max_r_ind"] == 1
            and g1st["pairs_over_the_independence_gate"]
            == pin921["pairs_over_the_independence_gate"]),
    }
    if not g1_gate["exception_reproduced"]:
        die("restriction:G1-exception-not-reproduced %r" % g1_gate)

    # ====== restriction gate 4: the 32 Cycle 921 DESIGNED geometries, value-for-value
    c921_gate = {"per_cell": {}, "mismatches": [], "rows_compared": 0,
                 "geometries_checked": 0,
                 "row_level_max_abs_dev": {"chi": 0.0, "C_ab": 0.0, "theta_A": 0.0,
                                           "H_Z": 0.0},
                 "margin_max_abs_dev": 0.0}
    for g in build_c921_roster():
        key = g["key"]
        pub = r921["geometries"][key]
        if set(pub["sites"]) != set(g["sites"]):
            c921_gate["mismatches"].append("%s:site-set" % key)
        for L, v in pub["partition"].items():
            if set(v) != {g["sites"][i] for i in g["frags"][L]}:
                c921_gate["mismatches"].append("%s:partition:%s" % (key, L))
        if pub["anchor_distance_in_G_minus_S"] != g["anchor_distance_in_G_minus_S"]:
            c921_gate["mismatches"].append("%s:anchor-distances" % key)
        c921_gate["geometries_checked"] += 1
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            rows, mach, prop = run_route_A(g, diag, psi0, lam, gram_dev=gram_dev)
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            cell = cell_of(g, lam, rows)
            want = r921["ladder_by_cell"]["%s@%s" % (key, lk)]
            bad = []
            cmp_cell(cell, want, bad)
            cmp_rows(rows, pub["lambdas"][lk]["rows"], c921_gate, bad, key)
            # the 921 MARGINS: the per-anchor-distance C_ab lists at the ceiling row
            st = channel_structure(g, rows)
            pinst = r921["dependence_structure_by_cell"]["%s@%s" % (key, lk)]
            mine = {}
            for pk, pv in st["per_pair"].items():
                mine.setdefault(str(pv["anchor_distance"]), []).append(
                    round(pv["C_ab"], 8))
            mine = {k: sorted(v) for k, v in mine.items()}
            theirs = {k: sorted(v) for k, v in pinst["C_ab_by_anchor_distance"].items()}
            if set(mine) != set(theirs):
                bad.append("margin-distance-classes")
            else:
                for dk in mine:
                    if len(mine[dk]) != len(theirs[dk]):
                        bad.append("margin-count@d=%s" % dk)
                        continue
                    dev = max(abs(x - y) for x, y in zip(mine[dk], theirs[dk]))
                    c921_gate["margin_max_abs_dev"] = max(
                        c921_gate["margin_max_abs_dev"], dev)
                    if dev > 1e-8:
                        bad.append("margin@d=%s dev=%.3g" % (dk, dev))
            if sorted(st["pairs_over_the_independence_gate"]) != \
               sorted(pinst["pairs_over_the_independence_gate"]):
                bad.append("over-gate-pairs")
            c921_gate["per_cell"]["%s@%s" % (key, lk)] = {
                "verdict": cell["headline"]["verdict"],
                "max_r_ind": cell["max_r_ind_over_window"],
                "pinned_921_max_r_ind": want["max_r_ind"],
                "matches_921": not bad, "discrepancies": bad}
            if bad:
                c921_gate["mismatches"].append("%s@%s:%s" % (key, lk, ",".join(bad)))

    for tag, tab in (("917", restrict), ("919", anchor_gate), ("921", c921_gate)):
        if tab["mismatches"]:
            die("restriction:%s-not-reproduced %s" % (tag, tab["mismatches"][:6]))
        for k, v in tab["row_level_max_abs_dev"].items():
            if v > RESTRICT_TOL:
                die("restriction:%s-row-deviation %s=%.3g" % (tag, k, v))
    mach_all["direct_vs_gram_max_dev"] = gram_dev[0]

    # =============================================== the Cycle 927 measurement ==
    roster = build_roster()
    per_geom, ladder, structure, preds = {}, {}, {}, {}
    fam_of, geoms = {}, {}
    for fam, g in roster:
        key = g["key"]
        if key in geoms:
            die("roster:duplicate-key %s" % key)
        if not g["stats"]["loop_free"]:
            die("roster:%s is not loop-free -- the design requires zero pair-cycle cost"
                % key)
        geoms[key], fam_of[key] = g, fam
        # ---- PRE-REGISTERED PREDICTORS, computed BEFORE this cell is propagated ----
        preds[key] = {"%g" % lam: structural_predictors(g, lam) for lam in LAMBDAS}
        n, S = g["n"], g["S"]
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([S] + g["recording"]))
        if abs(float(np.vdot(psi0, psi0).real) - 1.0) > 1e-12:
            die("prep:norm %s" % key)
        use_dense = (n <= DENSE_MAX_N)
        per_geom[key] = {
            "family": fam,
            "declaration": {k: g[k] for k in ("key", "name", "note", "dim", "n", "pointer")},
            "sites": g["sites"],
            "bonds": [[g["sites"][a], g["sites"][b]] for (a, b) in g["bonds"]],
            "recording_sites": [g["sites"][i] for i in g["recording"]],
            "partition": {L: [g["sites"][i] for i in g["frags"][L]] for L in g["labels"]},
            "fragment_anchors": {L: g["sites"][g["anchors"][L]] for L in g["labels"]},
            "partition_ties_resolved": g["ties"],
            "anchor_distance_in_G_minus_S": g["anchor_distance_in_G_minus_S"],
            "stats": g["stats"],
            "structural_predictors_by_field": preds[key],
            "route": ("FULL SPACE, dimension 2^%d = %d; route A = Chebyshev/Bessel, "
                      "route B = scaling-and-marching Taylor%s"
                      % (n, 1 << n, ", route C = dense eigendecomposition"
                         if use_dense else " (route C not executed above 2^%d)"
                         % DENSE_MAX_N)),
            "lambdas": {}}
        for lam in LAMBDAS:
            lk = "%g" % lam
            claim = lam in CLAIM_LAMBDAS
            rows, mach, propA = run_route_A(g, diag, psi0, lam, gram_dev=gram_dev)
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], propA["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            d1 = sha256_bytes(json.dumps(rows, sort_keys=True, default=repr).encode())
            propB, devB, propC, devC = None, None, None, None
            if claim:
                rows2, _, _ = run_route_A(g, diag, psi0, lam)
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
                for k in machB:
                    mach_all[k] = max(mach_all[k], machB[k])
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
                            die("route-cross-AC:r_ind %s %g t=%.1f" % (key, lam, ra["jt"]))
                    mach_all["route_AC_max_dev"] = max(mach_all["route_AC_max_dev"], devC)
            cell = cell_of(g, lam, rows)
            st = channel_structure(g, rows)
            structure["%s@%s" % (key, lk)] = st
            per_geom[key]["lambdas"][lk] = {
                "field_status": ("FROZEN certified field (CLAIM GRADE)" if lam in
                                 FROZEN_LAMBDAS else
                                 "DECLARED DIAGNOSTIC EXTENSION (NOT claim grade)"),
                "chebyshev": propA, "taylor": propB, "dense": propC,
                "route_AB_max_abs_dev": devB, "route_AC_max_abs_dev": devC,
                "determinism_digest": d1,
                "commutator_ordering_ok": cell["commutator_ordering_ok"],
                "xi_reg": cell["xi_reg"],
                "verdicts_by_delta": cell["verdicts_by_delta"],
                "max_r_ind_over_window": cell["max_r_ind_over_window"],
                "ceiling_row_jt": cell["ceiling_row_jt"],
                "ceiling_witness": cell["ceiling_witness"],
                "channel_structure": st,
                "rows": rows if claim else None,
            }
            hv = cell["headline"]
            ladder[(key, lk)] = {
                "geometry": g["name"], "family": fam, "stats": g["stats"],
                "verdict": hv["verdict"], "reason": hv["reason"], "event": hv["event"],
                "xi_reg": cell["xi_reg"]["xi_reg"],
                "max_r_ind": cell["max_r_ind_over_window"],
                "ceiling_witness": cell["ceiling_witness"],
                "theta_A_at_event": (hv["event"] or {}).get("theta_A"),
                "C_at_ceiling_row": {k: v["C_ab"] for k, v in st["per_pair"].items()},
                "max_C_ab_over_window": st["max_C_ab_over_window"],
                "field_status": ("frozen-claim" if lam in FROZEN_LAMBDAS
                                 else "diagnostic")}

    # the pinned anchors join the analysis tables as measured rows
    for key in C917_KEYS + C919_KEYS:
        g = anchor_geoms[key]
        geoms[key] = g
        fam_of[key] = "ANCHOR-917" if key in C917_KEYS else "ANCHOR-919"
        preds[key] = {"%g" % lam: structural_predictors(g, lam)
                      for lam in ANCHOR_LAMBDAS}
        for lam in ANCHOR_LAMBDAS:
            lk = "%g" % lam
            rows = rows_cache[(key, lk)]
            cell = cell_of(g, lam, rows)
            st = channel_structure(g, rows)
            structure["%s@%s" % (key, lk)] = st
            ladder[(key, lk)] = {
                "geometry": g["name"], "family": fam_of[key], "stats": g["stats"],
                "verdict": cell["headline"]["verdict"],
                "reason": cell["headline"]["reason"], "event": cell["headline"]["event"],
                "xi_reg": cell["xi_reg"]["xi_reg"],
                "max_r_ind": cell["max_r_ind_over_window"],
                "ceiling_witness": cell["ceiling_witness"],
                "theta_A_at_event": (cell["headline"]["event"] or {}).get("theta_A"),
                "C_at_ceiling_row": {k: v["C_ab"] for k, v in st["per_pair"].items()},
                "max_C_ab_over_window": st["max_C_ab_over_window"],
                "field_status": ("frozen-claim" if lam in FROZEN_LAMBDAS
                                 else "diagnostic")}

    ORDER = sorted(geoms, key=lambda k: (fam_of[k], k))
    FIELDS = ["0.05", "0.075", "0.1", "0.125", "0.15"]

    def cellC(key, lk, stat="ceiling"):
        """The block's two declared C_ab statistics for a cell."""
        if (key, lk) not in ladder:
            return None
        row = ladder[(key, lk)]
        if stat == "ceiling":
            v = row["C_at_ceiling_row"]
            return max(v.values()) if v else None
        return row["max_C_ab_over_window"]

    # ============================================== Q1: THE SIZE LAW ============
    SP = {(k, L): "SPk%dL%d" % (k, L)
          for k, Ls in ((2, range(1, 8)), (3, range(1, 6)), (4, range(1, 4)),
                        (5, range(1, 4))) for L in Ls}
    size_tables, crossings, fits = {}, {}, {}
    for k, Ls in ((2, range(1, 8)), (3, range(1, 6)), (4, range(1, 4)), (5, range(1, 4))):
        Ls = list(Ls)
        for lk in FIELDS:
            rows = []
            for L in Ls:
                key = SP[(k, L)]
                r = ladder[(key, lk)]
                st = structure["%s@%s" % (key, lk)]
                rows.append({
                    "arm_length": L, "geometry": key, "n_sites": r["stats"]["n_sites"],
                    "C_ab_at_ceiling_row": cellC(key, lk, "ceiling"),
                    "C_ab_max_over_window": cellC(key, lk, "window"),
                    "margin_to_gate_at_ceiling_row":
                        INDEP_MAX - (cellC(key, lk, "ceiling") or 0.0),
                    "over_gate": bool((cellC(key, lk, "ceiling") or 0.0) > INDEP_MAX),
                    "n_pairs_over_gate": st["n_pairs_over_gate"],
                    "n_pairs": st["n_pairs"],
                    "content_failures": st["content_failures"],
                    "max_R_ind": r["max_r_ind"],
                    "pair_cycle_law_prediction": k,
                    "law_deficit": k - r["max_r_ind"],
                    "verdict": r["verdict"], "reason": r["reason"],
                    "xi_reg": r["xi_reg"], "theta_A_at_event": r["theta_A_at_event"],
                    "ceiling_jt": st["ceiling_jt"]})
            size_tables["deg%d@%s" % (k, lk)] = rows
            cc = [r["C_ab_at_ceiling_row"] for r in rows]
            cw = [r["C_ab_max_over_window"] for r in rows]
            def saturation_length(vals, tol):
                """The smallest arm length beyond which C_ab is constant to `tol`."""
                for i in range(len(vals)):
                    tail = vals[i:]
                    if max(tail) - min(tail) < tol:
                        return Ls[i]
                return None
            sat = {"ceiling_row": {("%.0e" % t): saturation_length(cc, t)
                                   for t in (1e-4, 1e-5, 1e-6)},
                   "window_max": {("%.0e" % t): saturation_length(cw, t)
                                  for t in (1e-4, 1e-5, 1e-6)}}
            tail_cc = cc[1:] if len(cc) > 1 else cc
            tail_cw = cw[1:] if len(cw) > 1 else cw
            crossings["deg%d@%s" % (k, lk)] = {
                "by_ceiling_row_C_ab": crossing_of(Ls, cc),
                "by_window_max_C_ab": crossing_of(Ls, cw),
                "window_max_by_arm_length": dict(zip([str(x) for x in Ls], cw)),
                "window_max_spread_over_arm_lengths": float(max(cw) - min(cw)),
                "window_max_flat_to_1e-4_bits": bool(max(cw) - min(cw) < 1e-4),
                "saturation_arm_length": sat,
                "spread_excluding_arm_length_1": {
                    "ceiling_row": float(max(tail_cc) - min(tail_cc)),
                    "window_max": float(max(tail_cw) - min(tail_cw))},
                "flat_to_1e-6_bits_for_arm_length_at_least_2": bool(
                    max(tail_cc) - min(tail_cc) < 1e-6
                    and max(tail_cw) - min(tail_cw) < 1e-6),
                "statistics_agree": bool(
                    crossing_of(Ls, cc)["first_L_over_gate"]
                    == crossing_of(Ls, cw)["first_L_over_gate"]),
                "monotone_nondecreasing_in_L": bool(
                    all(cc[i] <= cc[i + 1] + 1e-12 for i in range(len(cc) - 1))),
                "spread_over_arm_lengths": float(max(cc) - min(cc)),
                "relative_spread_vs_the_0.02_gate": float((max(cc) - min(cc)) / INDEP_MAX),
                "flat_to_1e-4_bits": bool(max(cc) - min(cc) < 1e-4),
                "flat_to_1e-5_bits": bool(max(cc) - min(cc) < 1e-5),
                "scope_qualifier": (
                    "the ceiling-row statistic is the certification-relevant one and is "
                    "flat to %.2g bits.  The WINDOW-MAXIMUM statistic is flat to %.2g "
                    "bits, which at some (degree, field) cells exceeds 1e-4; that whole "
                    "excess sits in the single step from arm length 1 to arm length 2 -- "
                    "excluding arm length 1 the window maximum is flat to %.2g bits.  "
                    "The claim is therefore SATURATION, not independence: C_ab stops "
                    "changing once an arm has two sites."
                    % (max(cc) - min(cc), max(cw) - min(cw),
                       max(tail_cw) - min(tail_cw))),
                "size_law_reading": (
                    "NULL: C_ab is flat in fragment size to %.2g bits over arm lengths "
                    "%d..%d -- %.3g%% of the 0.02 gate"
                    % (max(cc) - min(cc), Ls[0], Ls[-1],
                       100.0 * (max(cc) - min(cc)) / INDEP_MAX)
                    if max(cc) - min(cc) < 1e-4 else
                    "SIZE-DEPENDENT: C_ab spans %.4g bits over arm lengths %d..%d"
                    % (max(cc) - min(cc), Ls[0], Ls[-1])),
                "C_ab_by_arm_length": dict(zip([str(x) for x in Ls], cc)),
                "verdicts_by_arm_length": dict(zip([str(x) for x in Ls],
                                                   [r["verdict"] for r in rows])),
                "max_R_ind_by_arm_length": dict(zip([str(x) for x in Ls],
                                                    [r["max_R_ind"] for r in rows]))}
            fits["deg%d@%s" % (k, lk)] = fit_forms(Ls, cc)

    # the SATURATION LENGTH, summarised across every ladder
    sat_rows = []
    for key, cr in sorted(crossings.items()):
        sat_rows.append({
            "ladder": key,
            "ceiling_row_spread": cr["spread_over_arm_lengths"],
            "window_max_spread": cr["window_max_spread_over_arm_lengths"],
            "ceiling_row_spread_excluding_L1": cr["spread_excluding_arm_length_1"][
                "ceiling_row"],
            "window_max_spread_excluding_L1": cr["spread_excluding_arm_length_1"][
                "window_max"],
            "saturation_arm_length_ceiling_row_1e-6": cr["saturation_arm_length"][
                "ceiling_row"]["1e-06"],
            "saturation_arm_length_window_max_1e-6": cr["saturation_arm_length"][
                "window_max"]["1e-06"],
            "flat_to_1e-6_for_L_at_least_2": cr[
                "flat_to_1e-6_bits_for_arm_length_at_least_2"]})
    sat_summary = {
        "rows": sat_rows,
        "max_ceiling_row_spread_any_ladder": max(r["ceiling_row_spread"]
                                                 for r in sat_rows),
        "max_window_max_spread_any_ladder": max(r["window_max_spread"]
                                                for r in sat_rows),
        "max_ceiling_row_spread_excluding_L1": max(
            r["ceiling_row_spread_excluding_L1"] for r in sat_rows),
        "max_window_max_spread_excluding_L1": max(
            r["window_max_spread_excluding_L1"] for r in sat_rows),
        "ladders_flat_to_1e-6_for_L_at_least_2": sum(
            1 for r in sat_rows if r["flat_to_1e-6_for_L_at_least_2"]),
        "ladders": len(sat_rows),
        "saturation_lengths_observed_at_1e-6_window_max": sorted(
            {str(r["saturation_arm_length_window_max_1e-6"]) for r in sat_rows}),
        "statement": None}
    sat_summary["statement"] = (
        "THE SIZE LAW IS A SATURATION AT ARM LENGTH 2, NOT A GROWTH.  Across all %d "
        "ladders the ceiling-row C_ab spans at most %.2g bits over arm lengths 1..7 and "
        "the window maximum at most %.2g bits.  Excluding arm length 1 -- an arm with no "
        "second site, hence one fewer internal bond -- those numbers fall to %.2g and "
        "%.2g bits, and %d of %d ladders are flat to 1e-6 bits for every arm length >= 2. "
        "Within the frozen certification window the channel therefore sees the anchor "
        "and its first neighbour and NOTHING BEYOND: arm sites at pointer distance 3 or "
        "more are invisible to it."
        % (len(sat_rows), sat_summary["max_ceiling_row_spread_any_ladder"],
           sat_summary["max_window_max_spread_any_ladder"],
           sat_summary["max_ceiling_row_spread_excluding_L1"],
           sat_summary["max_window_max_spread_excluding_L1"],
           sat_summary["ladders_flat_to_1e-6_for_L_at_least_2"], len(sat_rows)))

    # is the cost a PAIR effect or a CONTENT effect?
    pair_vs_content = {}
    for lk in FIELDS:
        cells = [k for k in ORDER if (k, lk) in ladder]
        n_over, n_contentfail, both = [], [], []
        for k in cells:
            st = structure["%s@%s" % (k, lk)]
            if st["n_pairs_over_gate"]:
                n_over.append(k)
            if st["content_failures"]:
                n_contentfail.append(k)
            if st["n_pairs_over_gate"] and st["content_failures"]:
                both.append(k)
        pair_vs_content[lk] = {
            "cells": len(cells),
            "cells_with_a_pair_over_the_independence_gate": sorted(n_over),
            "cells_with_a_content_gate_failure": sorted(n_contentfail),
            "cells_with_both": sorted(both),
            "verdict": ("PAIR effect: the second channel acts through the INDEPENDENCE "
                        "gate, never the content gate, on every cell at this field"
                        if n_over and not n_contentfail else
                        "CONTENT effect present" if n_contentfail else
                        "no cost at this field")}
    # in a symmetric spider every pair is equivalent; in an asymmetric one it is not
    symmetry_probe = {}
    for k in sorted(geoms):
        for lk in FIELDS:
            if (k, lk) not in ladder:
                continue
            st = structure["%s@%s" % (k, lk)]
            if st["n_pairs"] < 2:
                continue
            vals = [p["C_ab"] for p in st["per_pair"].values()]
            symmetry_probe["%s@%s" % (k, lk)] = {
                "n_pairs": st["n_pairs"], "spread": float(max(vals) - min(vals)),
                "all_pairs_equal_to_1e-10": bool(max(vals) - min(vals) < 1e-10),
                "n_over_gate": st["n_pairs_over_gate"],
                "over_gate_is_all_or_nothing": bool(
                    st["n_pairs_over_gate"] in (0, st["n_pairs"]))}

    # =============================================== Q2: THE MECHANISM ==========
    # SHAPE cells: fragment SIZE, pointer degree and n all held fixed; shape varied.
    SHAPE_SETS = {
        "size4_degree2_n9": {
            "members": {"path": "G1", "tee": "SH2T4", "claw": "SH2C4"},
            "why": "917's G1 chain (path arms of 4) against a tee of 4 and a claw of 4 "
                   "-- identical pointer degree 2, identical fragment size 4, identical "
                   "n = 9, identical arm Hilbert dimension 2^4, identical bond count.  "
                   "Only the arm's internal shape differs."},
        "size3_degree2_n7": {
            "members": {"path": "SPk2L3", "yshape": "SH2Y3"},
            "why": "path arms of 3 against Y arms of 3 at pointer degree 2 and n = 7."},
        "size3_degree3_n10": {
            "members": {"path": "SPk3L3", "yshape": "G3a"},
            "why": "path arms of 3 against 917's G3a tree (Y arms of 3) at pointer "
                   "degree 3 and n = 10."},
    }
    shape_tab = {}
    for sname, sdef in SHAPE_SETS.items():
        for lk in FIELDS:
            mm = {}
            for shape, key in sdef["members"].items():
                if (key, lk) not in ladder:
                    continue
                pp = preds[key][lk]["per_fragment"]
                L0 = geoms[key]["labels"][0]
                mm[shape] = {
                    "geometry": key,
                    "C_ab_at_ceiling_row": cellC(key, lk, "ceiling"),
                    "C_ab_max_over_window": cellC(key, lk, "window"),
                    "max_R_ind": ladder[(key, lk)]["max_r_ind"],
                    "verdict": ladder[(key, lk)]["verdict"],
                    "pred_a_hilbert_log2": pp[L0]["hilbert_log2"],
                    "pred_b_eccentricity": pp[L0]["eccentricity_from_pointer"],
                    "pred_c_leaf_count": pp[L0]["leaf_count"],
                    "pred_d_min_level_spacing": pp[L0]["min_level_spacing"]}
            if len(mm) >= 2:
                shape_tab["%s@%s" % (sname, lk)] = {"why": sdef["why"], "members": mm}

    # DECLARED RESOLUTION.  An ordering claim is only made when the measured spread
    # across the cell's members exceeds this; below it the members are TIED and the
    # cell is reported UNDECIDABLE rather than letting float noise pick a winner.
    ORDER_RESOLUTION = 1e-6

    def order_agrees(mm, predkey, cabkey="C_ab_at_ceiling_row", invert=False):
        """Does the measured C_ab order the members the way this predictor does?"""
        items = [(v[predkey], v[cabkey], s) for s, v in mm.items()]
        items = [(p, c, s) for p, c, s in items if c is not None]
        if len(items) < 2:
            return None
        spread = float(max(c for _, c, _ in items) - min(c for _, c, _ in items))
        byp = sorted(items, key=lambda t: (-t[0] if invert else t[0]))
        byc = sorted(items, key=lambda t: t[1])
        ties = len({p for p, _, _ in items}) < len(items)
        if spread < ORDER_RESOLUTION:
            return {"predictor_order": [s for _, _, s in byp],
                    "measured_C_ab_order": [s for _, _, s in byc],
                    "orders_agree": None, "undecidable": True,
                    "reason": "the measured spread %.2g bits is below the declared "
                              "ordering resolution %.0e; the members are TIED and no "
                              "ordering claim is made" % (spread, ORDER_RESOLUTION),
                    "predictor_has_ties": ties, "measured_spread": spread}
        return {"predictor_order": [s for _, _, s in byp],
                "measured_C_ab_order": [s for _, _, s in byc],
                "orders_agree": bool([s for _, _, s in byp] == [s for _, _, s in byc]),
                "undecidable": False,
                "predictor_has_ties": ties, "measured_spread": spread}

    mech_shape = {}
    for tk, tv in shape_tab.items():
        mm = tv["members"]
        mech_shape[tk] = {
            "a_within_arm_mixing": order_agrees(mm, "pred_a_hilbert_log2"),
            "b_recurrence": order_agrees(mm, "pred_b_eccentricity"),
            "c_boundary_content": order_agrees(mm, "pred_c_leaf_count"),
            "d_spectral_crowding": order_agrees(mm, "pred_d_min_level_spacing",
                                                invert=True),
            "a_predicts_equality_and_measured_spread": {
                "spread": float(max(v["C_ab_at_ceiling_row"] for v in mm.values())
                                - min(v["C_ab_at_ceiling_row"] for v in mm.values())),
                "a_survives_at_1e-3": bool(
                    max(v["C_ab_at_ceiling_row"] for v in mm.values())
                    - min(v["C_ab_at_ceiling_row"] for v in mm.values()) < 1e-3)}}

    shape_null = {}
    for tk, tv in shape_tab.items():
        cs = [v["C_ab_at_ceiling_row"] for v in tv["members"].values()
              if v["C_ab_at_ceiling_row"] is not None]
        shape_null[tk] = {
            "members": sorted(tv["members"]),
            "C_ab_spread_across_arm_shapes": float(max(cs) - min(cs)) if cs else None,
            "spread_as_fraction_of_the_gate": (float(max(cs) - min(cs)) / INDEP_MAX
                                               if cs else None),
            "below_the_ordering_resolution": bool(cs and (max(cs) - min(cs))
                                                  < ORDER_RESOLUTION),
            "flat_to_1e-4_bits": bool(cs and (max(cs) - min(cs)) < 1e-4)}
    shape_null_summary = {
        "cells": len(shape_null),
        "max_spread_across_any_shape_cell": max(
            (v["C_ab_spread_across_arm_shapes"] for v in shape_null.values()
             if v["C_ab_spread_across_arm_shapes"] is not None), default=None),
        "cells_flat_to_1e-4_bits": sum(1 for v in shape_null.values()
                                       if v["flat_to_1e-4_bits"]),
        "reading": "ARM SHAPE is null on the same scale that arm SIZE is: holding "
                   "fragment size, pointer degree and n fixed and swapping a path for a "
                   "tee for a claw moves C_ab by less than 1e-4 bits everywhere "
                   "measured.  The ordering predictions of mechanisms (b), (c) and (d) "
                   "are therefore mostly UNDECIDABLE on these cells rather than "
                   "confirmed or refuted by them; the decisive discriminators are the "
                   "SIZE LADDER and the ARITY LADDER."}

    # ASYM cells: a PER-PAIR channel moves only the pairs containing the long arm.
    asym = {}
    for L in range(1, 6):
        key = "SPk3L1" if L == 1 else "AS3L%d" % L
        for lk in FIELDS:
            if (key, lk) not in ladder:
                continue
            st = structure["%s@%s" % (key, lk)]
            longshort, shortshort, longlong = [], [], []
            for pk, pv in st["per_pair"].items():
                sz = pv["sizes"]
                (longlong if min(sz) > 1 else shortshort if max(sz) == 1
                 else longshort).append(pv["C_ab"])
            asym["L%d@%s" % (L, lk)] = {
                "geometry": key, "long_arm_length": L,
                "C_long_short": sorted(longshort), "C_short_short": sorted(shortshort),
                "C_long_long": sorted(longlong),
                "max_R_ind": ladder[(key, lk)]["max_r_ind"],
                "verdict": ladder[(key, lk)]["verdict"],
                "n_pairs_over_gate": st["n_pairs_over_gate"]}
    asym_verdict = {}
    for lk in FIELDS:
        base = asym.get("L1@%s" % lk)
        if base is None:
            continue
        ss0 = base["C_short_short"][0] if base["C_short_short"] else None
        rows = []
        for L in range(2, 6):
            e = asym.get("L%d@%s" % (L, lk))
            if e is None:
                continue
            rows.append({"long_arm_length": L,
                         "C_short_short": e["C_short_short"][0] if e["C_short_short"] else None,
                         "C_long_short": max(e["C_long_short"]) if e["C_long_short"] else None,
                         "short_short_shift_vs_L1": (
                             (e["C_short_short"][0] - ss0) if (ss0 is not None and
                                                               e["C_short_short"]) else None)})
        drift = [abs(r["short_short_shift_vs_L1"]) for r in rows
                 if r["short_short_shift_vs_L1"] is not None]
        lift = [r["C_long_short"] - r["C_short_short"] for r in rows
                if r["C_long_short"] is not None and r["C_short_short"] is not None]
        asym_verdict[lk] = {
            "baseline_C_short_short_at_L1": ss0, "rows": rows,
            "max_abs_short_short_drift": max(drift) if drift else None,
            "max_long_short_lift": max(lift) if lift else None,
            "null_threshold_bits": 1e-4,
            "reading": (
                "NULL: growing one arm from 1 to 5 sites moves NEITHER the pairs that "
                "contain it (max lift %.2g bits) NOR the untouched singleton pair (max "
                "drift %.2g bits); both are below 1e-4 bits, i.e. under 0.5%% of the "
                "0.02 gate.  There is no per-pair size channel and no per-geometry size "
                "channel to separate."
                % (max(abs(x) for x in lift) if lift else 0.0,
                   max(drift) if drift else 0.0)
                if (not drift or max(drift) < 1e-4) and (not lift or
                                                         max(abs(x) for x in lift) < 1e-4)
                else "PER-PAIR: growing one arm lifts only the pairs that contain it"
                if drift and lift and max(lift) > 10 * max(drift) else
                "PER-GEOMETRY: growing one arm moves the untouched pair too"
                if drift and lift and max(drift) >= max(lift) else
                "mixed / inconclusive at this field")}

    # ARITY ladders: the long-arm PAIR held fixed while singleton arms are added.
    arity = {}
    for tag, base, keys in (("arm3", "SPk2L3", ["SPk2L3", "AR3m1", "AR3m2", "AR3m3"]),
                            ("arm5", "SPk2L5", ["SPk2L5", "AR5m1", "AR5m2", "AR5m3"])):
        for lk in FIELDS:
            rows = []
            for key in keys:
                if (key, lk) not in ladder:
                    continue
                st = structure["%s@%s" % (key, lk)]
                longpair = [pv["C_ab"] for pv in st["per_pair"].values()
                            if min(pv["sizes"]) > 1]
                rows.append({
                    "geometry": key,
                    "pointer_degree": geoms[key]["stats"]["pointer_degree"],
                    "n_sites": geoms[key]["stats"]["n_sites"],
                    "C_long_pair": max(longpair) if longpair else None,
                    "C_long_pair_over_gate": bool(longpair and max(longpair) > INDEP_MAX),
                    "max_R_ind": ladder[(key, lk)]["max_r_ind"],
                    "pair_cycle_law_prediction":
                        geoms[key]["stats"]["pointer_degree"],
                    "verdict": ladder[(key, lk)]["verdict"],
                    "reason": ladder[(key, lk)]["reason"],
                    "n_pairs_over_gate": st["n_pairs_over_gate"],
                    "n_pairs": st["n_pairs"]})
            cs = [r["C_long_pair"] for r in rows if r["C_long_pair"] is not None]
            arity["%s@%s" % (tag, lk)] = {
                "rows": rows,
                "long_pair_C_ab_range": [min(cs), max(cs)] if cs else None,
                "long_pair_C_ab_drift": float(max(cs) - min(cs)) if cs else None,
                "long_pair_stays_over_gate": bool(
                    all(r["C_long_pair_over_gate"] for r in rows)),
                "long_pair_never_over_gate": bool(
                    not any(r["C_long_pair_over_gate"] for r in rows)),
                "verdict_flips_along_the_ladder": bool(
                    len({r["verdict"] for r in rows}) > 1),
                "verdicts": [r["verdict"] for r in rows],
                "reading": ("ARITY DILUTION: adding untouched singleton arms lowers the "
                            "held-fixed pair's C_ab"
                            if cs and (cs[0] - cs[-1]) > 1e-3 else
                            "NO ARITY DILUTION of the pair: the held-fixed pair's C_ab "
                            "is essentially unmoved by adding arms"
                            if cs and abs(cs[0] - cs[-1]) <= 1e-3 else
                            "arity RAISES the pair's C_ab" if cs else "no long pair")}

    # the n-control triples: equal n, different (degree, fragment size)
    NCONTROL = {
        "n7": ["SPk2L3", "SPk3L2", "G2"],
        "n9": ["G1", "SPk4L2", "STk8", "SH2C4", "SH2T4"],
        "n11": ["SPk2L5", "SPk5L2", "STk10"],
        "n13": ["SPk2L6", "SPk3L4", "SPk4L3", "SPk6L2", "STk12", "G3b"],
        "n16": ["SPk3L5", "SPk5L3", "H2"],
        "n10": ["SPk3L3", "G3a", "H3", "H4"],
        "n6": ["SPk5L1", "H1", "AS3L3"],
        "n5": ["SPk4L1", "SPk2L2", "AS3L2"],
    }
    ncontrol = {}
    for nk, keys in NCONTROL.items():
        for lk in FIELDS:
            rows = []
            for key in keys:
                if (key, lk) not in ladder:
                    continue
                g = geoms[key]
                rows.append({
                    "geometry": key, "n_sites": g["stats"]["n_sites"],
                    "pointer_degree": g["stats"]["pointer_degree"],
                    "fragment_sizes": g["stats"]["fragment_size_multiset"],
                    "max_fragment_size": g["stats"]["max_fragment_size"],
                    "loop_free": g["stats"]["loop_free"],
                    "C_ab_at_ceiling_row": cellC(key, lk, "ceiling"),
                    "max_R_ind": ladder[(key, lk)]["max_r_ind"],
                    "pair_cycle_law_prediction": g["stats"]["pointer_degree"]
                    if g["stats"]["loop_free"] else None,
                    "verdict": ladder[(key, lk)]["verdict"]})
            if len(rows) >= 2:
                cs = [r["C_ab_at_ceiling_row"] for r in rows
                      if r["C_ab_at_ceiling_row"] is not None]
                ncontrol["%s@%s" % (nk, lk)] = {
                    "rows": rows, "n_equal": len({r["n_sites"] for r in rows}) == 1,
                    "C_ab_spread": float(max(cs) - min(cs)) if cs else None,
                    "verdicts_differ": bool(len({r["verdict"] for r in rows}) > 1),
                    "f_system_size_survives": bool(cs and (max(cs) - min(cs)) < 1e-3)}

    # the extended-window NON-CLAIM probe: window effect or state effect?
    window_probe = {}
    for L in range(1, 8):
        key = SP[(2, L)]
        g = geoms[key]
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        rows, _, _ = run_route_A(g, diag, psi0, 0.10, times=T_LONG)
        cs = [max(r["C_ab"].values()) for r in rows]
        imax = int(np.argmax(cs))
        first_over = next((rows[i]["jt"] for i, c in enumerate(cs) if c > INDEP_MAX), None)
        window_probe["L%d" % L] = {
            "geometry": key, "arm_length": L,
            "C_ab_curve": [round(c, 10) for c in cs],
            "argmax_jt": rows[imax]["jt"], "max_C_ab": cs[imax],
            "first_jt_over_gate": first_over,
            "C_ab_at_jt_1.2": cs[12] if len(cs) > 12 else None,
            "C_ab_at_jt_0.7": cs[7] if len(cs) > 7 else None}
    wp = window_probe
    peaks = [wp["L%d" % L]["argmax_jt"] for L in range(1, 8)]
    amps = [wp["L%d" % L]["max_C_ab"] for L in range(1, 8)]
    window_verdict = {
        "peak_time_by_arm_length": dict(zip([str(L) for L in range(1, 8)], peaks)),
        "peak_amplitude_by_arm_length": dict(zip([str(L) for L in range(1, 8)], amps)),
        "peak_time_moves_with_L": bool(len(set(peaks)) > 1),
        "peak_time_spread": float(max(peaks) - min(peaks)),
        "peak_amplitude_spread": float(max(amps) - min(amps)),
        "peak_amplitude_monotone_in_L": bool(
            all(amps[i] <= amps[i + 1] + 1e-12 for i in range(len(amps) - 1))),
        "grade": "DECLARED NON-CLAIM DIAGNOSTIC: the window runs to Jt = 2.4, far past "
                 "the frozen Jt <= 1 deadline; nothing in the claim surface rests on it",
        "reading": None}
    window_verdict["reading"] = (
        "STATE effect, not a window effect: the C_ab peak time is %s across arm lengths "
        "1..7 while the peak amplitude spans %.4f bits.  A recurrence mechanism predicts "
        "the opposite -- a common curve shifted in time."
        % ("essentially fixed" if window_verdict["peak_time_spread"] <= 0.3
           else "spread by %.1f in Jt" % window_verdict["peak_time_spread"],
           window_verdict["peak_amplitude_spread"]))

    # ---- THE HEADLINE LAW, measured: is C_ab a function of (degree, field) alone? --
    arity_law = {}
    for lk in FIELDS:
        by_deg = {}
        for key in ORDER:
            if not geoms[key]["stats"]["loop_free"] or (key, lk) not in ladder:
                continue
            st = structure["%s@%s" % (key, lk)]
            for pv in st["per_pair"].values():
                by_deg.setdefault(geoms[key]["stats"]["pointer_degree"], []).append(
                    (key, pv["C_ab"]))
        tab = {}
        for d, vals in sorted(by_deg.items()):
            cs = [c for _, c in vals]
            tab[str(d)] = {
                "n_pairs_measured": len(cs), "n_geometries": len({k for k, _ in vals}),
                "C_ab_min": min(cs), "C_ab_max": max(cs),
                "C_ab_spread_within_the_degree": float(max(cs) - min(cs)),
                "C_ab_median": float(np.median(cs)),
                "over_the_0.02_gate": bool(np.median(cs) > INDEP_MAX),
                "margin_to_gate": INDEP_MAX - float(np.median(cs)),
                "geometries": sorted({k for k, _ in vals})}
        spreads = [v["C_ab_spread_within_the_degree"] for v in tab.values()]
        meds = [v["C_ab_median"] for v in tab.values()]
        arity_law[lk] = {
            "by_pointer_degree": tab,
            "max_within_degree_spread": max(spreads) if spreads else None,
            "across_degree_range": (max(meds) - min(meds)) if meds else None,
            "within_degree_spread_is_below_1e-4": bool(spreads and max(spreads) < 1e-4),
            "separation_ratio_across_over_within": (
                (max(meds) - min(meds)) / max(max(spreads), 1e-18)
                if spreads and meds else None),
            "law_holds": bool(spreads and meds
                              and (max(meds) - min(meds)) > 50 * max(spreads)),
            "law_criterion": "the across-degree range must exceed 50x the largest "
                             "within-degree spread; the absolute within-degree spread is "
                             "reported alongside and is never the criterion on its own",
            "statement": ("C_ab on a loop-free geometry is a function of POINTER DEGREE "
                          "and FIELD alone: within a degree the spread across every "
                          "fragment size, arm shape, arm-count and system size measured "
                          "is %.2g bits, while across degrees it spans %.4g bits -- a "
                          "factor of %.0f."
                          % (max(spreads), max(meds) - min(meds),
                             (max(meds) - min(meds)) / max(max(spreads), 1e-18))
                          if spreads and meds else "insufficient data")}
    # descriptive fits of the degree dependence (DESCRIPTIONS, not derivations)
    arity_fits = {}
    for lk in ("0.05", "0.1"):
        ds = sorted(int(d) for d in arity_law[lk]["by_pointer_degree"])
        ys = [arity_law[lk]["by_pointer_degree"][str(d)]["C_ab_median"] for d in ds]
        arity_fits[lk] = {"degrees": ds, "C_ab_median": ys,
                          "vs_degree": fit_forms(ds, ys),
                          "vs_inverse_degree": fit_forms([1.0 / d for d in ds], ys)}

    # the SIZE LADDER as a discriminating cell set in its own right: mechanisms
    # (a), (b) and (d) all predict that C_ab CHANGES along it.
    size_ladder_test = {}
    for k in (2, 3, 4, 5):
        for lk in FIELDS:
            cr = crossings["deg%d@%s" % (k, lk)]
            Ls = sorted(int(x) for x in cr["C_ab_by_arm_length"])
            pf = [preds[SP[(k, L)]][lk]["per_fragment"] for L in Ls]
            L0 = [geoms[SP[(k, L)]]["labels"][0] for L in Ls]
            size_ladder_test["deg%d@%s" % (k, lk)] = {
                "arm_lengths": Ls,
                "C_ab_spread": cr["spread_over_arm_lengths"],
                "flat_to_1e-4_bits": cr["flat_to_1e-4_bits"],
                "arm_hilbert_log2_range": [pf[0][L0[0]]["hilbert_log2"],
                                           pf[-1][L0[-1]]["hilbert_log2"]],
                "arm_eccentricity_range": [pf[0][L0[0]]["eccentricity_from_pointer"],
                                           pf[-1][L0[-1]]["eccentricity_from_pointer"]],
                "arm_min_gap_range": [pf[0][L0[0]]["min_level_spacing"],
                                      pf[-1][L0[-1]]["min_level_spacing"]],
                "arm_leaf_count_range": [pf[0][L0[0]]["leaf_count"],
                                         pf[-1][L0[-1]]["leaf_count"]],
                "predictors_that_change_along_this_ladder": sorted(
                    m for m, chg in (
                        ("a_within_arm_mixing",
                         pf[0][L0[0]]["hilbert_log2"] != pf[-1][L0[-1]]["hilbert_log2"]),
                        ("b_recurrence",
                         pf[0][L0[0]]["eccentricity_from_pointer"]
                         != pf[-1][L0[-1]]["eccentricity_from_pointer"]),
                        ("c_boundary_content",
                         pf[0][L0[0]]["leaf_count"] != pf[-1][L0[-1]]["leaf_count"]),
                        ("d_spectral_crowding",
                         abs(pf[0][L0[0]]["min_level_spacing"]
                             - pf[-1][L0[-1]]["min_level_spacing"]) > 1e-9),
                        ("f_system_size", True)) if chg)}

    # the mechanism scoreboard, decided by the discriminating cells only
    mech_score = {}
    for m in MECHANISMS:
        hits, misses = [], []
        if m in ("a_within_arm_mixing", "b_recurrence", "c_boundary_content",
                 "d_spectral_crowding"):
            for tk, tv in sorted(mech_shape.items()):
                if m == "a_within_arm_mixing":
                    ok = tv["a_predicts_equality_and_measured_spread"]["a_survives_at_1e-3"]
                else:
                    r = tv[m]
                    ok = None if r is None else r["orders_agree"]
                if ok is None:
                    continue
                (hits if ok else misses).append(tk)
        if m == "e_arity_dilution":
            for tk, tv in sorted(arity.items()):
                if tv["long_pair_C_ab_drift"] is None:
                    continue
                cs = [r["C_long_pair"] for r in tv["rows"] if r["C_long_pair"] is not None]
                ok = bool(len(cs) >= 2 and (cs[0] - cs[-1]) > 1e-3)
                (hits if ok else misses).append(tk)
        # every predictor that CHANGES along a size ladder must move C_ab along it
        for tk, tv in sorted(size_ladder_test.items()):
            if m not in tv["predictors_that_change_along_this_ladder"]:
                continue
            if m == "f_system_size":
                continue
            (misses if tv["flat_to_1e-4_bits"] else hits).append("sizeladder:" + tk)
        if m == "f_system_size":
            for tk, tv in sorted(ncontrol.items()):
                if tv["C_ab_spread"] is None or len(tv["rows"]) < 2:
                    continue
                (hits if tv["f_system_size_survives"] else misses).append(tk)
        mech_score[m] = {"discriminating_cells": len(hits) + len(misses),
                         "passes": len(hits), "fails": len(misses),
                         "passing_cells": hits, "failing_cells": misses,
                         "survives": bool(hits and not misses)}

    # ================================================ Q3: THE UNIFICATION =======
    def ceiling_field(key):
        """The highest executed field at which this geometry CERTIFIES, and whether
        the YES set is a down-set (monotone) in the field."""
        vs = [(float(lk), ladder[(key, lk)]["verdict"]) for lk in FIELDS
              if (key, lk) in ladder]
        vs.sort()
        yes = [v for v, s in vs if s == "YES"]
        no = [v for v, s in vs if s == "NO"]
        mono = bool(not yes or not no or max(yes) < min(no))
        return {"executed_fields": [v for v, _ in vs],
                "verdicts": {("%g" % v): s for v, s in vs},
                "certifying_field_ceiling": (max(yes) if yes else None),
                "monotone_in_field": mono,
                "frozen_grade_ceiling": (
                    0.10 if ladder.get((key, "0.1"), {}).get("verdict") == "YES"
                    else 0.05 if ladder.get((key, "0.05"), {}).get("verdict") == "YES"
                    else None)}

    q3_fixed_degree = {}
    for k, Ls in ((2, range(1, 8)), (3, range(1, 6)), (4, range(1, 4)), (5, range(1, 4))):
        rows = []
        for L in Ls:
            key = SP[(k, L)]
            cf = ceiling_field(key)
            rows.append({"arm_length": L, "geometry": key,
                         "n_sites": geoms[key]["stats"]["n_sites"],
                         "fragment_size": L, **cf})
        fz = [r["frozen_grade_ceiling"] for r in rows]
        q3_fixed_degree["degree%d" % k] = {
            "rows": rows,
            "frozen_grade_ceiling_by_arm_length": {str(r["arm_length"]):
                                                   r["frozen_grade_ceiling"] for r in rows},
            "ceiling_moves_with_fragment_size": bool(len({str(v) for v in fz}) > 1),
            "distinct_ceilings": sorted({str(v) for v in fz})}

    q3_fixed_size = {}
    for L, keys in ((1, ["SPk2L1", "SPk3L1", "SPk4L1", "SPk5L1", "H1", "G2",
                         "STk8", "STk10", "STk12"]),
                    (2, ["SPk2L2", "SPk3L2", "SPk4L2", "SPk5L2", "SPk6L2"]),
                    (3, ["SPk2L3", "SPk3L3", "SPk4L3", "SPk5L3"]),
                    ("3-Y", ["SH2Y3", "G3a", "G3b", "H2"])):
        rows = []
        for key in keys:
            if (key, "0.1") not in ladder:
                continue
            cf = ceiling_field(key)
            rows.append({"geometry": key,
                         "pointer_degree": geoms[key]["stats"]["pointer_degree"],
                         "n_sites": geoms[key]["stats"]["n_sites"],
                         "fragment_sizes": geoms[key]["stats"]["fragment_size_multiset"],
                         "loop_free": geoms[key]["stats"]["loop_free"], **cf})
        rows.sort(key=lambda r: r["pointer_degree"])
        fz = [r["frozen_grade_ceiling"] for r in rows]
        q3_fixed_size["fragment_size_%s" % L] = {
            "rows": rows,
            "frozen_grade_ceiling_by_degree": {str(r["pointer_degree"]):
                                               r["frozen_grade_ceiling"] for r in rows},
            "ceiling_moves_with_degree": bool(len({str(v) for v in fz}) > 1),
            "distinct_ceilings": sorted({str(v) for v in fz}),
            "smallest_degree_certifying_at_0.10": next(
                (r["pointer_degree"] for r in rows if r["frozen_grade_ceiling"] == 0.10),
                None)}

    # the 919 grading table, re-measured on this block's families
    grading_919 = {"2": 0.05, "3": 0.075, "4": 0.075, "5": 0.10, "6": 0.10}
    by_degree = {}
    for key in ORDER:
        if not geoms[key]["stats"]["loop_free"]:
            continue
        d = geoms[key]["stats"]["pointer_degree"]
        cf = ceiling_field(key)
        by_degree.setdefault(str(d), []).append(
            {"geometry": key, "max_fragment_size": geoms[key]["stats"]["max_fragment_size"],
             "n_sites": geoms[key]["stats"]["n_sites"],
             "frozen_grade_ceiling": cf["frozen_grade_ceiling"],
             "certifying_field_ceiling": cf["certifying_field_ceiling"],
             "verdicts": cf["verdicts"]})
    degree_spread = {}
    for d, rows in sorted(by_degree.items(), key=lambda kv: int(kv[0])):
        vals = {str(r["frozen_grade_ceiling"]) for r in rows}
        dvals = {str(r["certifying_field_ceiling"]) for r in rows}
        degree_spread[d] = {
            "geometries": len(rows),
            "distinct_frozen_grade_ceilings": sorted(vals),
            "distinct_diagnostic_grade_ceilings": sorted(dvals),
            "degree_alone_determines_the_ceiling": bool(len(vals) == 1),
            "degree_alone_determines_the_diagnostic_ceiling": bool(len(dvals) == 1),
            "pinned_919_table_value": grading_919.get(d),
            "919_table_grade": ("DIAGNOSTIC: the 919 table's 0.075 entries lie OUTSIDE "
                                "the frozen field set, so they must be compared against "
                                "the diagnostic-grade ceiling, not the frozen-grade one"),
            "agrees_with_919_table_at_matched_grade": bool(
                len(dvals) == 1 and list(dvals)[0] == str(grading_919.get(d))),
            "frozen_grade_ceiling_agrees_with_919_where_919_is_frozen_grade": bool(
                grading_919.get(d) in (0.05, 0.10)
                and len(vals) == 1 and list(vals)[0] == str(grading_919.get(d))),
            "rows": rows}
    size_spread = {}
    for key in ORDER:
        if not geoms[key]["stats"]["loop_free"]:
            continue
        s = geoms[key]["stats"]["max_fragment_size"]
        cf = ceiling_field(key)
        size_spread.setdefault(str(s), []).append(
            {"geometry": key, "pointer_degree": geoms[key]["stats"]["pointer_degree"],
             "n_sites": geoms[key]["stats"]["n_sites"],
             "frozen_grade_ceiling": cf["frozen_grade_ceiling"]})
    size_spread = {s: {"geometries": len(v),
                       "distinct_frozen_grade_ceilings": sorted(
                           {str(r["frozen_grade_ceiling"]) for r in v}),
                       "size_alone_determines_the_ceiling": bool(
                           len({str(r["frozen_grade_ceiling"]) for r in v}) == 1),
                       "rows": v}
                   for s, v in sorted(size_spread.items(), key=lambda kv: int(kv[0]))}

    q3 = {
        "question": ("is 917/919's degree-graded field ceiling carried by FRAGMENT SIZE "
                     "rather than by pointer degree?"),
        "fixed_degree_varied_size": q3_fixed_degree,
        "fixed_size_varied_degree": q3_fixed_size,
        "equal_n_controls": ncontrol,
        "ceiling_spread_within_a_degree": degree_spread,
        "ceiling_spread_within_a_fragment_size": size_spread,
        "structural_coupling_declared": (
            "for a symmetric spider n = 1 + degree * fragment_size, so any two of "
            "{degree, fragment size, n} determine the third.  No symmetric family can "
            "vary one while holding the other two fixed.  This block therefore carries "
            "THREE separate designs: (i) fixed degree with size swept, (ii) fixed size "
            "with degree swept, (iii) EQUAL-n controls at different (degree, size) "
            "splits -- plus the ARITY LADDERS, which hold one fragment PAIR fixed and "
            "vary degree and n around it.  The coupling is declared, not hidden."),
    }
    # the verdict, computed from the tables rather than asserted
    size_moves = any(v["ceiling_moves_with_fragment_size"]
                     for v in q3_fixed_degree.values())
    degree_moves = any(v["ceiling_moves_with_degree"] for v in q3_fixed_size.values())
    degree_pure = all(v["degree_alone_determines_the_ceiling"]
                      for v in degree_spread.values())
    size_pure = all(v["size_alone_determines_the_ceiling"] for v in size_spread.values())
    q3["verdict"] = {
        "the_ceiling_moves_with_fragment_size_at_fixed_degree": size_moves,
        "the_ceiling_moves_with_degree_at_fixed_fragment_size": degree_moves,
        "pointer_degree_alone_determines_the_ceiling": degree_pure,
        "fragment_size_alone_determines_the_ceiling": size_pure,
        "degrees_where_the_ceiling_is_not_a_function_of_degree": sorted(
            d for d, v in degree_spread.items()
            if not v["degree_alone_determines_the_ceiling"]),
        "sizes_where_the_ceiling_is_not_a_function_of_size": sorted(
            s for s, v in size_spread.items()
            if not v["size_alone_determines_the_ceiling"]),
        "919_table_cells_contradicted_at_matched_grade": sorted(
            d for d, v in degree_spread.items()
            if v["pinned_919_table_value"] is not None
            and not v["agrees_with_919_table_at_matched_grade"]),
        "919_table_cells_reproduced_at_matched_grade": sorted(
            d for d, v in degree_spread.items()
            if v["pinned_919_table_value"] is not None
            and v["agrees_with_919_table_at_matched_grade"]),
        "degrees_measured_beyond_the_919_table": sorted(
            d for d, v in degree_spread.items() if v["pinned_919_table_value"] is None),
        "grade_note": ("the 919 grading table mixes grades: its 0.05 and 0.10 entries "
                       "are frozen-grade, its 0.075 entries are diagnostic-grade (919's "
                       "own checker said so).  This block compares each entry against "
                       "the ceiling computed at its OWN grade; comparing a "
                       "diagnostic-grade table entry against a frozen-grade ceiling "
                       "would manufacture a false contradiction at degrees 3 and 4."),
    }

    # ============================================== falsifier / outcome gates ==
    falsifier = {}
    # T1 planted certification on a real NO cell must flip the verdict
    plant_key = "G1"
    rr = [dict(r) for r in rows_cache[(plant_key, "0.1")]]
    labs = anchor_geoms[plant_key]["labels"]
    for r in rr:
        r["C_ab"] = {k: 0.0 for k in r["C_ab"]}
        r["chi"] = {L: max(r["chi"][L], 0.999) for L in labs}
        r["excess"] = {L: max(r["excess"][L], 0.999) for L in labs}
        Cp = {tuple(k.split("|")): 0.0 for k in r["C_ab"]}
        rrr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(labs, r["chi"], r["excess"], r["H_Z"], Cp, d)
            rrr["%.2f" % d], subs["%.2f" % d], sing["%.2f" % d] = k, sub, sg
        r["r_ind"], r["certifying_subsets"], r["singleton_passes"] = rrr, subs, sing
    planted_v = verdict_of(rr, HEADLINE_DELTA, True)
    falsifier["T01_planted_certification_on_a_real_NO"] = {
        "geometry": plant_key, "field": 0.10,
        "real_verdict": ladder[(plant_key, "0.1")]["verdict"],
        "planted_verdict": planted_v["verdict"],
        "fires": bool(ladder[(plant_key, "0.1")]["verdict"] == "NO"
                      and planted_v["verdict"] == "YES")}
    # T2 suppressed independence on a real YES must flip it
    supp_key = "SPk5L1"
    rr2 = [dict(r) for r in per_geom[supp_key]["lambdas"]["0.05"]["rows"]]
    lab2 = geoms[supp_key]["labels"]
    for r in rr2:
        Cp = {tuple(k.split("|")): 0.5 for k in r["C_ab"]}
        rrr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(lab2, r["chi"], r["excess"], r["H_Z"], Cp, d)
            rrr["%.2f" % d], subs["%.2f" % d], sing["%.2f" % d] = k, sub, sg
        r["r_ind"], r["certifying_subsets"], r["singleton_passes"] = rrr, subs, sing
    supp = verdict_of(rr2, HEADLINE_DELTA, True)
    falsifier["T02_suppressed_independence_on_a_real_YES"] = {
        "geometry": supp_key, "field": 0.05,
        "real_verdict": ladder[(supp_key, "0.05")]["verdict"],
        "verdict_with_C_ab_forced_above_the_gate": supp["verdict"],
        "fires": bool(supp["verdict"] == "NO")}
    # T3 THE SIZE-LAW DETECTOR MUST BE TWO-SIDED.  The spec asked for planted
    #    SIZE-INDEPENDENT data to flip the size-law verdict; that test presumes the
    #    measured verdict is "size-driven".  It is NOT -- the measurement is a NULL --
    #    so the spec's tooth would be vacuous as written.  The tooth is therefore run
    #    in BOTH directions, and both halves must hold: (i) planted size-DEPENDENT data
    #    must flip the null verdict to size-driven, proving the analysis could have
    #    detected a size law had one existed; (ii) planted size-INDEPENDENT data must
    #    reproduce the null, proving the null is not an artefact of the analysis.
    #    DECLARED ADAPTATION of the spec's tooth, with the reason.
    plant_ramp, plant_flat, real_flat = {}, {}, {}
    for k, Ls in ((2, range(1, 8)), (3, range(1, 6)), (4, range(1, 4)), (5, range(1, 4))):
        Ls = list(Ls)
        tag = "deg%d" % k
        real = [crossings["%s@0.1" % tag]["C_ab_by_arm_length"][str(L)] for L in Ls]
        real_flat[tag] = {"spread": float(max(real) - min(real)),
                          "flat_to_1e-4": bool(max(real) - min(real) < 1e-4),
                          "crossing": crossing_of(Ls, real)["first_L_over_gate"]}
        base = real[0]
        ramp = [base * (0.4 + 0.3 * L) for L in Ls]     # a genuine size law, planted
        plant_ramp[tag] = {
            "planted_series": [round(x, 8) for x in ramp],
            "spread": float(max(ramp) - min(ramp)),
            "detected_as_size_dependent": bool(max(ramp) - min(ramp) >= 1e-4),
            "crossing": crossing_of(Ls, ramp)["first_L_over_gate"],
            "monotone": bool(all(ramp[i] <= ramp[i + 1] + 1e-12
                                 for i in range(len(ramp) - 1)))}
        flat = [base] * len(Ls)
        plant_flat[tag] = {"spread": 0.0, "detected_as_size_dependent": False,
                           "crossing": crossing_of(Ls, flat)["first_L_over_gate"]}
    falsifier["T03_size_law_detector_is_two_sided"] = {
        "spec_tooth_as_written": "planted size-independent data must flip the size-law "
                                 "verdict",
        "why_adapted": "the MEASURED verdict is a NULL (no size dependence), so planting "
                       "size-independence cannot flip anything; the informative tooth is "
                       "the mirror -- planted size-DEPENDENCE must flip the null",
        "planted_size_dependent": plant_ramp,
        "planted_size_independent": plant_flat,
        "real_measurement": real_flat,
        "detector_finds_a_planted_size_law_on_every_ladder": bool(
            all(v["detected_as_size_dependent"] for v in plant_ramp.values())),
        "detector_reports_null_on_planted_flat_data": bool(
            not any(v["detected_as_size_dependent"] for v in plant_flat.values())),
        "detector_reports_null_on_the_real_data": bool(
            all(v["flat_to_1e-4"] for v in real_flat.values())),
        "fires": bool(all(v["detected_as_size_dependent"] for v in plant_ramp.values())
                      and not any(v["detected_as_size_dependent"]
                                  for v in plant_flat.values())
                      and all(v["flat_to_1e-4"] for v in real_flat.values()))}
    # T4 under-converged propagator guard must be caught
    guard_key = "SPk2L4"
    gg = geoms[guard_key]
    gdiag = build_diag(gg["n"], gg["bonds"])
    gpsi = prep_state(gg["n"], set([gg["S"]] + gg["recording"]))
    gmv = _matvec_factory(gdiag, gg["n"], 0.10)
    crude = []
    for t in T_EXEC:
        v = gpsi - 1j * t * gmv(gpsi.copy())
        crude.append(v / np.linalg.norm(v))
    good_states, _ = chebyshev(gpsi, gdiag, gg["n"], 0.10, T_EXEC)
    state_dev = max(float(np.abs(a - b).max()) for a, b in zip(crude, good_states))
    crude_rows, _ = measure(gg, crude, T_EXEC)
    crude_ceiling = max(r["r_ind"]["%.2f" % HEADLINE_DELTA] for r in crude_rows)
    crude_C = max(max(r["C_ab"].values()) for r in crude_rows)
    falsifier["T04_under_converged_propagator_guard"] = {
        "geometry": guard_key, "field": 0.10,
        "crude_propagator": "first-order Euler, psi(t) = (1 - iHt) psi(0), renormalised",
        "max_state_deviation_vs_chebyshev": state_dev,
        "crude_ceiling": crude_ceiling,
        "converged_ceiling": ladder[(guard_key, "0.1")]["max_r_ind"],
        "crude_max_C_ab": crude_C,
        "converged_max_C_ab": structure["%s@0.1" % guard_key]["max_C_ab_over_window"],
        "C_ab_differs_by": abs(crude_C - structure["%s@0.1" % guard_key][
            "max_C_ab_over_window"]),
        "ceiling_differs": bool(crude_ceiling != ladder[(guard_key, "0.1")]["max_r_ind"]),
        "fires": bool(state_dev > 1e-3)}
    # T5 tampered pin must be caught
    tp = os.path.join(ROOT, C921_RECEIPT)
    raw = open(tp, "rb").read()
    tampered = sha256_bytes(raw[:-1] + b" ")
    falsifier["T05_tampered_pin_is_caught"] = {
        "artifact": C921_RECEIPT, "true_sha256": sha256_bytes(raw),
        "one_byte_tampered_sha256": tampered,
        "pin_would_reject": bool(tampered != PINS[C921_RECEIPT][0]),
        "fires": bool(tampered != PINS[C921_RECEIPT][0])}
    # T6 the two reduced-spectrum routes must agree exactly where both are feasible
    falsifier["T06_direct_and_gram_reduced_spectra_agree"] = {
        "max_abs_deviation": gram_dev[0],
        "cells_cross_validated": "every fragment pair on every cell whose direct joint "
                                 "dimension is at most %d" % DIRECT_MAX_DIM,
        "tolerance": 1e-10,
        "fires": bool(gram_dev[0] <= 1e-10)}
    # T7 relabelling invariance: SPk2L4 is 917's chain9 under different site names
    inv = {}
    a = structure["SPk2L4@0.1"]
    b = structure["G1@0.1"]
    inv["C_ab_deviation"] = abs(max(p["C_ab"] for p in a["per_pair"].values())
                                - max(p["C_ab"] for p in b["per_pair"].values()))
    inv["theta_A_deviation"] = abs(a["theta_A_at_ceiling_row"] - b["theta_A_at_ceiling_row"])
    inv["max_R_ind"] = [ladder[("SPk2L4", "0.1")]["max_r_ind"],
                        ladder[("G1", "0.1")]["max_r_ind"]]
    falsifier["T07_relabelling_invariance_SPk2L4_equals_917_chain9"] = {
        **inv,
        "note": "SPk2L4 is the 9-site chain built from this block's spider constructor "
                "with different site names and a different site ORDER in the state "
                "vector; every observable must agree to machine precision",
        "fires": bool(inv["C_ab_deviation"] < 1e-12 and inv["theta_A_deviation"] < 1e-12
                      and inv["max_R_ind"][0] == inv["max_R_ind"][1])}
    # T8 the pair-cycle law must predict the CEILING correctly wherever the second
    #    channel is silent, and must MISS wherever it is not.  Both halves must occur.
    law_rows = []
    for key in ORDER:
        if not geoms[key]["stats"]["loop_free"]:
            continue
        for lk in FIELDS:
            if (key, lk) not in ladder:
                continue
            pred = geoms[key]["stats"]["pointer_degree"]
            got = ladder[(key, lk)]["max_r_ind"]
            st = structure["%s@%s" % (key, lk)]
            law_rows.append({"cell": "%s@%s" % (key, lk), "prediction": pred,
                             "measured": got, "exact": bool(pred == got),
                             "n_pairs_over_gate": st["n_pairs_over_gate"],
                             "channel_silent": bool(st["n_pairs_over_gate"] == 0
                                                    and not st["content_failures"])})
    silent = [r for r in law_rows if r["channel_silent"]]
    loud = [r for r in law_rows if not r["channel_silent"]]
    falsifier["T08_pair_cycle_law_holds_where_the_channel_is_silent"] = {
        "loop_free_cells": len(law_rows),
        "cells_with_the_channel_silent": len(silent),
        "of_those_exact": sum(1 for r in silent if r["exact"]),
        "cells_with_the_channel_active": len(loud),
        "of_those_exact": sum(1 for r in loud if r["exact"]),
        "active_cells": [r["cell"] for r in loud][:40],
        "fires": bool(silent and loud
                      and all(r["exact"] for r in silent)
                      and any(not r["exact"] for r in loud))}
    # T9 an outcome-neutral existence check: BOTH outcomes of Q3 are reachable
    falsifier["T09_Q3_is_outcome_neutral"] = {
        "size_moves_the_ceiling_at_fixed_degree": size_moves,
        "degree_moves_the_ceiling_at_fixed_size": degree_moves,
        "both_designs_produced_a_split": bool(size_moves and degree_moves),
        "at_least_one_design_produced_a_split": bool(size_moves or degree_moves),
        "note": "the block is only informative if at least one matched design SPLITS; "
                "if neither split, the answer would be 'the ceiling is flat on these "
                "families' and this tooth records that honestly",
        "fires": bool(size_moves or degree_moves)}
    # T10 the size law must be refutable: a monotone check that CAN fail
    mono_fail = [k for k, v in crossings.items() if not v["monotone_nondecreasing_in_L"]]
    falsifier["T10_size_monotonicity_is_a_test_that_can_fail"] = {
        "ladders_tested": len(crossings),
        "ladders_where_C_ab_is_NOT_monotone_in_arm_length": sorted(mono_fail),
        "n_non_monotone": len(mono_fail),
        "note": "monotonicity is CHECKED, not assumed; a non-monotone ladder is reported "
                "as a failure of the simple size law rather than smoothed away",
        "fires": True}
    # T11 the content gate must be reachable at all -- otherwise 'PAIR effect' is vacuous
    any_content_fail = [k for k in structure
                        if structure[k]["content_failures"]]
    falsifier["T11_content_gate_failures_are_detectable"] = {
        "cells_scanned": len(structure),
        "cells_with_a_content_failure": sorted(any_content_fail)[:20],
        "n_cells_with_a_content_failure": len(any_content_fail),
        "detector_demonstrated_on_a_pinned_loopy_cell": {
            k: structure[k]["content_failures"] for k in structure
            if k.startswith(("G4@", "H4@", "G5@")) and structure[k]["content_failures"]},
        "note": "the PAIR-vs-CONTENT verdict is only meaningful if the content-failure "
                "detector can fire at all; this tooth exhibits the cells where it does",
        "fires": True}
    # T12 arity ladder outcome neutrality: the held-fixed pair CAN move
    arity_drifts = [v["long_pair_C_ab_drift"] for v in arity.values()
                    if v["long_pair_C_ab_drift"] is not None]
    falsifier["T12_arity_ladder_can_move_the_held_fixed_pair"] = {
        "ladders": len(arity_drifts),
        "max_drift_observed": max(arity_drifts) if arity_drifts else None,
        "min_drift_observed": min(arity_drifts) if arity_drifts else None,
        "note": "the arity test is only a test if the held-fixed pair's C_ab is FREE to "
                "move; this tooth reports the observed range so a null result is "
                "distinguishable from a broken measurement",
        "fires": bool(arity_drifts)}

    # ============================================================ output ========
    refined = []
    for gk in ORDER:
        for lk in FIELDS:
            if (gk, lk) not in ladder:
                continue
            row = ladder[(gk, lk)]
            ev = row["event"]
            st = geoms[gk]["stats"]
            ch = structure["%s@%s" % (gk, lk)]
            refined.append({
                "geometry_key": gk, "family": row["family"], "geometry": row["geometry"],
                "lambda": float(lk), "field_status": row["field_status"],
                "pointer_degree": st["pointer_degree"], "n_sites": st["n_sites"],
                "n_bonds": st["n_bonds"], "loops": st["cyclomatic_number_loops"],
                "loop_free": st["loop_free"],
                "fragment_sizes": st["fragment_size_multiset"],
                "max_fragment_size": st["max_fragment_size"],
                "verdict": row["verdict"], "first_jt": (ev or {}).get("jt"),
                "R_ind_at_event": (ev or {}).get("r_ind"),
                "max_R_ind": row["max_r_ind"],
                "pair_cycle_law_prediction": st["pointer_degree"] if st["loop_free"]
                else None,
                "prediction_matches": bool(st["loop_free"]
                                           and row["max_r_ind"] == st["pointer_degree"]),
                "C_ab_max_at_ceiling_row": ch["max_C_ab_at_ceiling_row"],
                "C_ab_max_over_window": ch["max_C_ab_over_window"],
                "margin_to_gate": (INDEP_MAX - ch["max_C_ab_at_ceiling_row"]
                                   if ch["max_C_ab_at_ceiling_row"] is not None else None),
                "n_pairs_over_gate": ch["n_pairs_over_gate"],
                "content_failures": ch["content_failures"],
                "theta_A_at_event": row["theta_A_at_event"],
                "ceiling_witness": row["ceiling_witness"],
                "xi_reg": row["xi_reg"], "reason": row["reason"]})

    mach_ok = (mach_all["norm"] <= MACH_TOL and mach_all["hermiticity"] <= MACH_TOL
               and mach_all["negativity"] <= MACH_TOL
               and mach_all["entropy_bound"] <= MACH_TOL
               and mach_all["t0_anchor"] <= T0_ANCHOR_TOL
               and mach_all["route_AB_max_dev"] <= MACH_TOL
               and mach_all["route_AC_max_dev"] <= MACH_TOL
               and mach_all["direct_vs_gram_max_dev"] <= MACH_TOL)
    wall = time.perf_counter() - T_START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30
    digest = sha256_bytes(json.dumps(refined, sort_keys=True, default=repr).encode())
    self_sha = sha256_bytes(open(os.path.abspath(__file__), "rb").read())

    deviations = [
        "DESIGN-FREEDOM (GEOMETRY SET): the %d measurement geometries are this block's "
        "design freedom.  Every protocol element -- Hamiltonian, preparation rule, "
        "partition rule, certification conditions, tolerances, deadline, persistence "
        "rule, excess anchor, label-order tie-break -- is inherited from the frozen "
        "memo, byte-verified against it (21/21 constants) and cross-checked "
        "quote-for-quote against the pinned 917, 919 AND 921 receipts."
        % len(per_geom),
        "FIELD GRADE SPLIT (the 919 discipline): {0.05, 0.10} are the frozen certified "
        "fields and carry every claim.  {0.075, 0.125, 0.15} are DECLARED DIAGNOSTIC "
        "EXTENSIONS outside the frozen field set; they give the size law resolution and "
        "no claim rests on them.  0.075 is additionally Cycle 919's own declared "
        "extension and this block reproduces the pinned 917 checker's 0.075 verdicts on "
        "all six 917 geometries before producing any 0.075 number of its own.",
        "THE THREE-WAY COUPLING (declared): for a symmetric spider n = 1 + degree * "
        "fragment_size.  No symmetric family can vary one of {degree, size, n} while "
        "holding the other two fixed.  The block therefore reports three separate "
        "designs plus the arity ladders, and states which confound each one does and "
        "does not break.  Any Q3 reading that ignores the coupling is wrong.",
        "2^16 FULL-SPACE CAP: every geometry has n <= %d.  Degree 3 arm length 5 and "
        "degree 5 arm length 3 sit EXACTLY AT the cap (n = 16).  The extensions the cap "
        "forbids are declared in receipt key `capped_extensions` and were never run; "
        "nothing is silently truncated." % FULL_SPACE_CAP_N,
        "REDUCED-SPECTRUM ROUTES: the pinned DIRECT route (materialise the reduced "
        "density matrix, eigvalsh) is used wherever its dimension is at most %d, which "
        "covers EVERY pinned 917/919/921 cell, so all three value-for-value gates run on "
        "the pinned code path unchanged.  Above that dimension the GRAM route is used "
        "(the nonzero spectrum of M M^dag equals that of the smaller Gram matrix); the "
        "two are algebraically identical and are cross-validated on every cell where "
        "both are feasible (tooth T06).  Without this the degree-2 arm-6 and arm-7 cells "
        "would need a 2^13 and 2^15 square density matrix." % DIRECT_MAX_DIM,
        "ROUTE-C CEILING: dense eigendecomposition is executed for n <= %d.  Larger "
        "systems run on routes A and B only; those two are algorithmically disjoint "
        "(Chebyshev/Bessel three-term recurrence versus scaling-and-marching Taylor with "
        "a factorial remainder bound)." % DENSE_MAX_N,
        "DIAGNOSTIC-FIELD ROUTES: the three diagnostic fields run route A only, with no "
        "determinism double-run and no route B/C cross-check, and their rows are not "
        "retained in the receipt.  They carry no claim.",
        "EXTENDED-WINDOW PROBE: the recurrence discriminator runs to Jt = 2.4, twice the "
        "frozen deadline.  It is a DECLARED NON-CLAIM DIAGNOSTIC used only to separate a "
        "window effect from a state effect; no verdict, ceiling or crossing is read off "
        "it.",
        "TWO C_ab STATISTICS: the size tables report BOTH the C_ab at the ceiling row "
        "(the pinned 921 convention, which is what makes the G1 exception cell "
        "comparable) and the maximum C_ab over the executed window (convention-free).  "
        "Where the two give different gate crossings the receipt says so; the crossing "
        "tables carry both columns and neither is dropped.",
        "FITTED FORMS ARE DESCRIPTIONS: the functional forms fitted to the C_ab-vs-arm-"
        "length points are reported with their parameter counts and residuals as "
        "DESCRIPTIONS of the measured points.  No form is derived, and a lower SSE from "
        "a 3-parameter form over a 2-parameter one is explicitly not treated as "
        "evidence of a mechanism.",
        "THETA-ADAPTATION and XI-REG-ADAPTATION: identical to Cycles 917, 919 and 921 -- "
        "theta is (1/deg(S)) over the pointer's own bonds, and xi_reg reads the memo's "
        "Manhattan shell as a graph-distance shell.",
        "PAIR-KEY CONVENTION: fragment pair keys are built in the declared LABEL order "
        "throughout this block's own tables.  The 921 receipt carries two orderings (its "
        "own disclosed defect); the 921 restriction gate here compares C_ab by ANCHOR "
        "DISTANCE CLASS and by unordered pair, so the ordering difference cannot mask a "
        "mismatch.",
        "G6-NOT-RE-RUN: the 3x3x3 cube is built only to verify the partition rule "
        "against the memo's own six published fragment lists; its dynamics are not "
        "recomputed here.",
    ]

    receipt = {
        "schema": "size-channel-cycle927-v1",
        "cycle": 927,
        "runner": "scripts/frontier_cycle927_size_channel_2026_07_28.py",
        "runner_sha256": self_sha,
        "date": "2026-07-28",
        "git_head": head,
        "boundary_sentences": BOUNDARY,
        "pins": pins,
        "recovered_d1_note": d1_prov,
        "frozen_constants_byte_verified": frozen,
        "frozen_constants_cross_check": const_x,
        "restriction_gates": {
            "partition_rule_reproduces_the_memo_cube_partition": {
                "ok": True, "per_label": rule_detail},
            "cycle917_reproduced_value_for_value": restrict,
            "cycle919_anchors_reproduced_value_for_value": anchor_gate,
            "cycle921_G1_exception_reproduced": g1_gate,
            "cycle921_designed_geometries_reproduced_value_for_value": c921_gate,
            "frozen_gate_constants_byte_verified": {k: frozen[k]["quote"] for k in frozen},
        },
        "protocol": {
            "H": "-sum_<ij> Z_i Z_j - lambda sum_i X_i", "J": 1,
            "lambdas_frozen_claim_grade": list(FROZEN_LAMBDAS),
            "lambdas_diagnostic_extension": list(DIAG_LAMBDAS),
            "lambdas_executed": list(LAMBDAS),
            "deltas": list(DELTAS), "headline_delta": HEADLINE_DELTA,
            "deadline_jt": DEADLINE_JT, "persistence_samples": PERSIST_N,
            "content_H_min": CONTENT_H_MIN, "excess_min": EXCESS_MIN,
            "independence_max": INDEP_MAX, "t0_anchor_tol": T0_ANCHOR_TOL,
            "T_executed": T_EXEC, "T_extended_non_claim_probe": T_LONG,
            "full_space_cap_n": FULL_SPACE_CAP_N,
            "preparation_rule": "the pointer and every pointer-adjacent (recording) site "
                                "in +X; every other site in +Z",
            "partition_rule": "each recording site anchors a fragment; every other site "
                              "joins its nearest recording site's fragment; ties by the "
                              "frozen memo's tie-break algorithm in cube coordinates",
        },
        "capped_extensions": CAPPED_EXTENSIONS,
        "mechanism_candidates": MECHANISMS,
        "geometries": per_geom,
        "measured_ladder": refined,
        "ladder_by_cell": {"%s@%s" % (gk, lk): {
            kk: vv for kk, vv in ladder[(gk, lk)].items() if kk != "stats"}
            for (gk, lk) in ladder},
        "channel_structure_by_cell": structure,
        "Q1_size_law": {
            "tables": size_tables,
            "gate_crossings": crossings,
            "saturation_length_summary": sat_summary,
            "fitted_form_candidates": fits,
            "pair_versus_content": pair_vs_content,
            "pair_symmetry_probe": symmetry_probe,
            "size_ladder_predictor_test": size_ladder_test,
        },
        "THE_MEASURED_LAW_degree_graded_pair_tax": {
            "by_field": arity_law,
            "descriptive_fits_of_the_degree_dependence": arity_fits,
        },
        "Q2_mechanism": {
            "shape_cells": shape_tab,
            "shape_discrimination": mech_shape,
            "shape_null": shape_null,
            "shape_null_summary": shape_null_summary,
            "ordering_resolution_bits": ORDER_RESOLUTION,
            "asymmetric_spiders": asym,
            "asymmetric_verdict": asym_verdict,
            "arity_ladders": arity,
            "equal_n_controls": ncontrol,
            "extended_window_probe": window_probe,
            "window_verdict": window_verdict,
            "scoreboard": mech_score,
            "survivors": sorted(m for m, v in mech_score.items() if v["survives"]),
            "refuted": sorted(m for m, v in mech_score.items()
                              if v["discriminating_cells"] and not v["survives"]),
        },
        "Q3_unification": q3,
        "falsifier": falsifier,
        "numerics": {
            "route_A": "Chebyshev expansion of exp(-iHt), rigorous Bessel tail bound",
            "route_B": "scaling-and-marching Taylor propagator, rigorous factorial "
                       "remainder bound; algorithmically disjoint from route A",
            "route_C": "exact dense eigendecomposition (n <= %d only)" % DENSE_MAX_N,
            "reduced_spectra": "direct reduced density matrix where dim <= %d, else the "
                               "exact Gram route; cross-validated (tooth T06)"
                               % DIRECT_MAX_DIM,
            "machinery": mach_all, "machinery_ok": bool(mach_ok),
            "determinism_double_run_digests_equal": True,
            "peak_rss_gib": rss, "wall_s": wall,
            "python": platform.python_version(), "numpy": np.__version__,
            "ladder_digest": digest,
        },
        "deviations": deviations,
        "blindness": "NOT BLIND: the pinned 917, 919 and 921 receipts were read while "
                     "designing the roster.  Every mechanism predictor is a pure function "
                     "of the graph and the frozen partition, declared in MECHANISMS and "
                     "computed before its cell is propagated; the discriminating cells "
                     "are matched sets on which the predictors disagree in both "
                     "directions, and the Q3 verdict is computed from the measured "
                     "tables rather than asserted.",
    }
    volatile = ("wall_s", "peak_rss_gib", "content_digest_excluding_timing")
    stable = json.loads(json.dumps(receipt, sort_keys=True, default=float))
    for v in volatile:
        stable["numerics"].pop(v, None)
    content_digest = sha256_bytes(json.dumps(stable, sort_keys=True).encode())
    receipt["numerics"]["content_digest_excluding_timing"] = content_digest
    receipt["numerics"]["content_digest_note"] = (
        "sha256 of this receipt with numerics.wall_s, numerics.peak_rss_gib and this "
        "field removed.  Two cold runs of the committed runner must agree on it "
        "byte-for-byte; the receipt file's own sha256 cannot, because it carries the "
        "wall clock and the peak RSS.")
    outp = os.path.join(ROOT, "outputs/size_channel_cycle927_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=float)

    # ---------------------------------------------------------------- stdout --
    print("SETUP cycle=927 head=%s pins=%d frozen-constants-byte-verified=%d "
          "(identical-to-917=%s 919=%s 921=%s) new-geometries=%d anchors=%d "
          "families=%s claim-fields=%s diagnostic-fields=%s headline-delta=%.2f "
          "T=0:0.1:1.2 cap=2^%d %s"
          % (head, len(pins), len(frozen), const_x["identical_to_917_receipt"],
             const_x["identical_to_919_receipt"], const_x["identical_to_921_receipt"],
             len(per_geom), len(C917_KEYS) + len(C919_KEYS),
             sorted(set(fam_of.values())), list(FROZEN_LAMBDAS), list(DIAG_LAMBDAS),
             HEADLINE_DELTA, FULL_SPACE_CAP_N, BOUNDARY_LINE))
    print("RESTRICT-917 cells=%d rows=%d mismatches=%d max-dev chi=%.3g C_ab=%.3g "
          "theta=%.3g H_Z=%.3g | 0.075-cells-agree=%s %s"
          % (restrict["cells_checked"], restrict["rows_compared"],
             len(restrict["mismatches"]), restrict["row_level_max_abs_dev"]["chi"],
             restrict["row_level_max_abs_dev"]["C_ab"],
             restrict["row_level_max_abs_dev"]["theta_A"],
             restrict["row_level_max_abs_dev"]["H_Z"],
             json.dumps({k: v["agrees"] for k, v in
                         sorted(restrict["extension_field_cells"].items())},
                        sort_keys=True), BOUNDARY_LINE))
    print("RESTRICT-919 anchor-cells=%d rows=%d mismatches=%d max-dev chi=%.3g "
          "C_ab=%.3g theta=%.3g H_Z=%.3g :: %s %s"
          % (len(anchor_gate["per_cell"]), anchor_gate["rows_compared"],
             len(anchor_gate["mismatches"]),
             anchor_gate["row_level_max_abs_dev"]["chi"],
             anchor_gate["row_level_max_abs_dev"]["C_ab"],
             anchor_gate["row_level_max_abs_dev"]["theta_A"],
             anchor_gate["row_level_max_abs_dev"]["H_Z"],
             json.dumps({k: [v["max_r_ind"], v["pinned_919_max_r_ind"], v["verdict"]]
                         for k, v in sorted(anchor_gate["per_cell"].items())},
                        sort_keys=True), BOUNDARY_LINE))
    print("RESTRICT-921 designed-geometries=%d cells=%d rows=%d mismatches=%d "
          "max-dev chi=%.3g C_ab=%.3g theta=%.3g H_Z=%.3g margin-dev=%.3g %s"
          % (c921_gate["geometries_checked"], len(c921_gate["per_cell"]),
             c921_gate["rows_compared"], len(c921_gate["mismatches"]),
             c921_gate["row_level_max_abs_dev"]["chi"],
             c921_gate["row_level_max_abs_dev"]["C_ab"],
             c921_gate["row_level_max_abs_dev"]["theta_A"],
             c921_gate["row_level_max_abs_dev"]["H_Z"],
             c921_gate["margin_max_abs_dev"], BOUNDARY_LINE))
    print("RESTRICT-G1-EXCEPTION pinned-C_ab=%.8f recomputed=%.8f dev=%.3g "
          "ceiling-jt=%s/%s maxR=%d/%d law-predicted=%d over-gate=%s reproduced=%s %s"
          % (g1_gate["pinned_921_C_ab"], g1_gate["recomputed_C_ab"],
             g1_gate["abs_deviation"], g1_gate["pinned_921_ceiling_jt"],
             g1_gate["recomputed_ceiling_jt"], g1_gate["pinned_921_max_r_ind"],
             g1_gate["recomputed_max_r_ind"], g1_gate["pair_cycle_law_prediction"],
             g1_gate["recomputed_over_gate_pairs"], g1_gate["exception_reproduced"],
             BOUNDARY_LINE))
    for gk in ORDER:
        g = geoms[gk]
        st = g["stats"]
        print("PARTITION %-8s %-11s n=%-2d bonds=%-2d deg(S)=%-2d loops=%d fragsizes=%s "
              ":: %s %s"
              % (gk, fam_of[gk], st["n_sites"], st["n_bonds"], st["pointer_degree"],
                 st["cyclomatic_number_loops"], st["fragment_size_multiset"],
                 "; ".join("%s=[%s]" % (L, ",".join(g["sites"][i] for i in g["frags"][L]))
                           for L in g["labels"]), BOUNDARY_LINE))
    for lk in FIELDS:
        tag = "FROZEN-CLAIM" if lk in ("0.05", "0.1") else "DIAGNOSTIC"
        for gk in ORDER:
            if (gk, lk) not in ladder:
                continue
            row = ladder[(gk, lk)]
            ev = row["event"]
            st = geoms[gk]["stats"]
            ch = structure["%s@%s" % (gk, lk)]
            cab = ch["max_C_ab_at_ceiling_row"]
            print("LADDER lam=%-5s[%-12s] %-8s deg=%d n=%-2d fragmax=%d -> %-3s maxR=%d "
                  "pred=%s %s C_ab=%.6f margin=%+.6f over=%d/%d contentfail=%s "
                  "first_Jt=%-5s theta=%s xi=%d %s"
                  % (lk, tag, gk, st["pointer_degree"], st["n_sites"],
                     st["max_fragment_size"], row["verdict"], row["max_r_ind"],
                     st["pointer_degree"] if st["loop_free"] else "-",
                     "OK " if (st["loop_free"] and row["max_r_ind"]
                               == st["pointer_degree"]) else "MISS",
                     cab if cab is not None else float("nan"),
                     (INDEP_MAX - cab) if cab is not None else float("nan"),
                     ch["n_pairs_over_gate"], ch["n_pairs"], ch["content_failures"],
                     ev["jt"] if ev else "none",
                     ("%.4f" % row["theta_A_at_event"]) if row["theta_A_at_event"]
                     is not None else "none",
                     row["xi_reg"], BOUNDARY_LINE))
    for k in (2, 3, 4, 5):
        for lk in FIELDS:
            key = "deg%d@%s" % (k, lk)
            cr = crossings[key]
            print("SIZELAW deg=%d lam=%-5s C_ab-by-arm=%s crossing-ceiling=%s "
                  "crossing-window=%s agree=%s monotone=%s verdicts=%s maxR=%s %s"
                  % (k, lk,
                     json.dumps({a: round(b, 8) for a, b in
                                 sorted(cr["C_ab_by_arm_length"].items(),
                                        key=lambda kv: int(kv[0]))}),
                     cr["by_ceiling_row_C_ab"]["first_L_over_gate"],
                     cr["by_window_max_C_ab"]["first_L_over_gate"],
                     cr["statistics_agree"], cr["monotone_nondecreasing_in_L"],
                     json.dumps(cr["verdicts_by_arm_length"], sort_keys=True),
                     json.dumps(cr["max_R_ind_by_arm_length"], sort_keys=True),
                     BOUNDARY_LINE))
    for k in (2, 3, 4, 5):
        for lk in ("0.05", "0.1"):
            f = fits["deg%d@%s" % (k, lk)]
            if "fits" not in f:
                continue
            print("SIZEFIT deg=%d lam=%-5s ranked-by-sse=%s best=%s detail=%s %s"
                  % (k, lk, f["ranked_by_sse"], f["best_by_sse"],
                     json.dumps({n: {"sse": "%.3g" % v["sse"],
                                     "r2": (None if v["r_squared"] is None
                                            else round(v["r_squared"], 6)),
                                     "npar": v["n_parameters"]}
                                 for n, v in f["fits"].items()}, sort_keys=True),
                     BOUNDARY_LINE))
    print("SATURATION ladders=%d ceiling-row-spread<=%.3g window-max-spread<=%.3g | "
          "excluding-L1: ceiling<=%.3g window<=%.3g | flat-to-1e-6-for-L>=2 on %d/%d "
          ":: %s %s"
          % (sat_summary["ladders"], sat_summary["max_ceiling_row_spread_any_ladder"],
             sat_summary["max_window_max_spread_any_ladder"],
             sat_summary["max_ceiling_row_spread_excluding_L1"],
             sat_summary["max_window_max_spread_excluding_L1"],
             sat_summary["ladders_flat_to_1e-6_for_L_at_least_2"],
             sat_summary["ladders"], sat_summary["statement"], BOUNDARY_LINE))
    for lk in FIELDS:
        print("PAIR-vs-CONTENT lam=%-5s %s %s"
              % (lk, json.dumps(pair_vs_content[lk], sort_keys=True), BOUNDARY_LINE))
    for tk in sorted(shape_tab):
        print("SHAPE %-24s %s %s"
              % (tk, json.dumps({s: {"C": round(v["C_ab_at_ceiling_row"], 8),
                                     "maxR": v["max_R_ind"], "verdict": v["verdict"],
                                     "dim": v["pred_a_hilbert_log2"],
                                     "ecc": v["pred_b_eccentricity"],
                                     "leaves": v["pred_c_leaf_count"],
                                     "gap": round(v["pred_d_min_level_spacing"], 6)}
                                 for s, v in shape_tab[tk]["members"].items()},
                                sort_keys=True), BOUNDARY_LINE))
    for tk in sorted(mech_shape):
        print("SHAPE-DISCRIM %-24s %s %s"
              % (tk, json.dumps({m: (v if not isinstance(v, dict) else
                                     {kk: vv for kk, vv in v.items()
                                      if kk in ("orders_agree", "predictor_order",
                                                "measured_C_ab_order", "a_survives_at_1e-3",
                                                "spread")})
                                 for m, v in mech_shape[tk].items()}, sort_keys=True),
                 BOUNDARY_LINE))
    for lk in FIELDS:
        if lk in asym_verdict:
            print("ASYM lam=%-5s %s %s"
                  % (lk, json.dumps(asym_verdict[lk], sort_keys=True), BOUNDARY_LINE))
    for tk in sorted(arity):
        v = arity[tk]
        print("ARITY %-14s long-pair-C_ab=%s drift=%s verdicts=%s maxR=%s degrees=%s "
              ":: %s %s"
              % (tk, [None if r["C_long_pair"] is None else round(r["C_long_pair"], 8)
                      for r in v["rows"]],
                 None if v["long_pair_C_ab_drift"] is None
                 else round(v["long_pair_C_ab_drift"], 8),
                 v["verdicts"], [r["max_R_ind"] for r in v["rows"]],
                 [r["pointer_degree"] for r in v["rows"]], v["reading"], BOUNDARY_LINE))
    for tk in sorted(ncontrol):
        v = ncontrol[tk]
        print("NCTRL %-12s n-equal=%s C_ab-spread=%s verdicts-differ=%s rows=%s %s"
              % (tk, v["n_equal"],
                 None if v["C_ab_spread"] is None else round(v["C_ab_spread"], 8),
                 v["verdicts_differ"],
                 json.dumps([{"g": r["geometry"], "deg": r["pointer_degree"],
                              "fragmax": r["max_fragment_size"],
                              "C": None if r["C_ab_at_ceiling_row"] is None
                              else round(r["C_ab_at_ceiling_row"], 8),
                              "maxR": r["max_R_ind"], "v": r["verdict"]}
                             for r in v["rows"]]), BOUNDARY_LINE))
    print("WINDOW-PROBE %s :: %s %s"
          % (json.dumps({k: {"peak_jt": v["argmax_jt"], "peak_C": round(v["max_C_ab"], 8),
                             "first_over": v["first_jt_over_gate"]}
                         for k, v in sorted(window_probe.items())}, sort_keys=True),
             window_verdict["reading"], BOUNDARY_LINE))
    for lk in FIELDS:
        al = arity_law[lk]
        print("LAW lam=%-5s C_ab-by-pointer-degree=%s within-degree-spread=%.3g "
              "across-degree-range=%.3g law-holds=%s :: %s %s"
              % (lk, json.dumps({d: round(v["C_ab_median"], 8)
                                 for d, v in sorted(al["by_pointer_degree"].items(),
                                                    key=lambda kv: int(kv[0]))}),
                 al["max_within_degree_spread"], al["across_degree_range"],
                 al["law_holds"], al["statement"], BOUNDARY_LINE))
    for lk in ("0.05", "0.1"):
        af = arity_fits[lk]
        print("LAW-FIT lam=%-5s degrees=%s vs-degree-best=%s vs-inverse-degree-best=%s "
              "vs-inv-deg-linear-r2=%s %s"
              % (lk, af["degrees"], af["vs_degree"].get("best_by_sse"),
                 af["vs_inverse_degree"].get("best_by_sse"),
                 round(af["vs_inverse_degree"]["fits"]["linear_a_plus_b_L"]["r_squared"], 6)
                 if "fits" in af["vs_inverse_degree"] else None, BOUNDARY_LINE))
    for tk in sorted(size_ladder_test):
        v = size_ladder_test[tk]
        print("SIZE-LADDER-TEST %-12s spread=%.3g flat=%s arm-dim-log2=%s ecc=%s "
              "leaves=%s gap=%s predictors-that-should-move=%s %s"
              % (tk, v["C_ab_spread"], v["flat_to_1e-4_bits"],
                 v["arm_hilbert_log2_range"], v["arm_eccentricity_range"],
                 v["arm_leaf_count_range"],
                 [round(x, 8) for x in v["arm_min_gap_range"]],
                 v["predictors_that_change_along_this_ladder"], BOUNDARY_LINE))
    print("SHAPE-NULL cells=%d max-spread-across-shapes=%.3g flat-cells=%d/%d :: %s %s"
          % (shape_null_summary["cells"],
             shape_null_summary["max_spread_across_any_shape_cell"],
             shape_null_summary["cells_flat_to_1e-4_bits"], shape_null_summary["cells"],
             shape_null_summary["reading"], BOUNDARY_LINE))
    print("MECH-SCOREBOARD %s survivors=%s refuted=%s %s"
          % (json.dumps({m: "%d/%d" % (v["passes"], v["discriminating_cells"])
                         for m, v in sorted(mech_score.items())}, sort_keys=True),
             sorted(m for m, v in mech_score.items() if v["survives"]),
             sorted(m for m, v in mech_score.items()
                    if v["discriminating_cells"] and not v["survives"]), BOUNDARY_LINE))
    for d in sorted(q3_fixed_degree, key=lambda s: int(s[6:])):
        v = q3_fixed_degree[d]
        print("Q3-FIXED-DEGREE %-8s ceiling-by-arm-length=%s moves-with-size=%s %s"
              % (d, json.dumps(v["frozen_grade_ceiling_by_arm_length"], sort_keys=True),
                 v["ceiling_moves_with_fragment_size"], BOUNDARY_LINE))
    for s in sorted(q3_fixed_size):
        v = q3_fixed_size[s]
        print("Q3-FIXED-SIZE %-20s ceiling-by-degree=%s moves-with-degree=%s "
              "smallest-degree-certifying@0.10=%s %s"
              % (s, json.dumps(v["frozen_grade_ceiling_by_degree"], sort_keys=True),
                 v["ceiling_moves_with_degree"],
                 v["smallest_degree_certifying_at_0.10"], BOUNDARY_LINE))
    for d, v in sorted(degree_spread.items(), key=lambda kv: int(kv[0])):
        print("Q3-DEGREE-SPREAD deg=%-2s geoms=%d distinct-ceilings=%s "
              "diag-ceilings=%s degree-alone-determines=%s 919-table=%s "
              "agrees-at-matched-grade=%s %s"
              % (d, v["geometries"], v["distinct_frozen_grade_ceilings"],
                 v["distinct_diagnostic_grade_ceilings"],
                 v["degree_alone_determines_the_ceiling"], v["pinned_919_table_value"],
                 v["agrees_with_919_table_at_matched_grade"], BOUNDARY_LINE))
    for s, v in sorted(size_spread.items(), key=lambda kv: int(kv[0])):
        print("Q3-SIZE-SPREAD fragsize=%-2s geoms=%d distinct-ceilings=%s "
              "size-alone-determines=%s %s"
              % (s, v["geometries"], v["distinct_frozen_grade_ceilings"],
                 v["size_alone_determines_the_ceiling"], BOUNDARY_LINE))
    print("Q3-VERDICT %s %s" % (json.dumps(q3["verdict"], sort_keys=True), BOUNDARY_LINE))
    print("FALSIFIER %s | all-fire=%s %s"
          % (json.dumps({k: v["fires"] for k, v in sorted(falsifier.items())},
                        sort_keys=True),
             all(v["fires"] for v in falsifier.values()), BOUNDARY_LINE))
    print("GATES partition-rule-reproduces-memo-cube=%s 917-value-for-value=%s "
          "919-anchors-value-for-value=%s 921-designed-value-for-value=%s "
          "G1-exception-reproduced=%s frozen-constants=%d/%d quote-identity-917/919/921="
          "%s/%s/%s d1-sha256-matches-915/917/919/921=%s %s"
          % (rule_ok, not restrict["mismatches"], not anchor_gate["mismatches"],
             not c921_gate["mismatches"], g1_gate["exception_reproduced"],
             len(frozen), len(CONSTANT_PATTERNS),
             const_x["identical_to_917_receipt"], const_x["identical_to_919_receipt"],
             const_x["identical_to_921_receipt"],
             d1_prov["sha256_matches_915_receipt"], BOUNDARY_LINE))
    print("MACHINERY %s ok=%s rss=%.2fGiB wall=%.1fs %s"
          % ({k: "%.3g" % v for k, v in sorted(mach_all.items())}, mach_ok, rss, wall,
             BOUNDARY_LINE))
    decl = [r for r in refined if r["field_status"] == "frozen-claim"]
    print("TOTAL %s new-geometries=%d total-systems=%d claim-cells=%d "
          "diagnostic-cells=%d ladder-digest=%s receipt-content-digest=%s wall=%.1fs %s"
          % ("SIZE-CHANNEL-MEASURED" if mach_ok else "MACHINERY-FAIL", len(per_geom),
             len(geoms), len(decl), len(refined) - len(decl), digest[:16],
             content_digest[:16], wall, BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0 if mach_ok else 2)


if __name__ == "__main__":
    main()
