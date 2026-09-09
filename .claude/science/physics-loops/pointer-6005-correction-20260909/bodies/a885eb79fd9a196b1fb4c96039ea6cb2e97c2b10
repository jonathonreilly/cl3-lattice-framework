#!/usr/bin/env python3
"""Cycle 932 -- THE PERSISTENCE RAZOR: the continuous window behind a discrete flag.

THE QUESTION.  The mass lane's last unexplained mechanism.  Under the frozen
route-C certification protocol at lambda = 0.10, pointer degrees 3 and 4 reach
the full R_ind ceiling and hold it for only TWO of the three consecutive samples
the persistence flag demands, with C_ab far under the 0.02 independence gate
(0.0126 / 0.0104 at the event row); degree >= 5 holds three and certifies.
Cycle 919 measured the boundary as ~8e-4 bits wide; Cycle 926 certified that the
persistence COUNT is load-bearing (persist=2 -> threshold 3; persist=4/5 ->
nothing certifies) while the deadline is robust over 0.7..1.2 and the C_ab-gate
band for the threshold is [0.0191673, 0.0207835).  Nobody has said WHY.

Cycle 931's pair-complement theorem turned the per-pair statistic into a
statement about ONE entropy sequence: on exchangeable-arm geometries
C_ab(t) = 2 s(1,t) - s(2,t).  So the persistence question is a question about
the TIME PROFILE of that sequence.  This block computes the profile.

WHAT THIS BLOCK DOES.  It resolves the frozen protocol's discrete verdict into
its CONTINUOUS-TIME preimage: for every (geometry, field) it locates the exact
real interval on which the frozen certification predicate R_ind >= 2 holds,
identifies which gate clips each end, and measures the interval's width against
the frozen sample spacing.  The frozen sample-grid verdicts are NEVER re-graded
here; they are reproduced at deviation exactly 0 and then EXPLAINED.  Every
continuous-time and grid-offset number in this runner is DIAGNOSTIC-GRADE and
is labelled so in the receipt.

THE GEOMETRY SET (design freedom #1, declared here).  Seven coordinate-free
stars S2..S8 (pointer degree 2..8, n = d+1) sweep degree at fixed everything
else; S5 IS the pinned 919 geometry H1 (star6) and S6 IS the pinned 917
geometry G2 (star7), so two rungs of the new family are pinned anchors and are
cross-checked against the pinned receipts at deviation exactly 0.  The pinned
tree anchors G3a (degree 3), G3b (degree 4), H2 (degree 5) and H3 (degree 5)
carry the same sweep on non-singleton fragments; G1, G4, G5 and H4 enter
through the reproduction gate and the clip census.

THE FIELDS.  lambda in {0.05, 0.10} are the FROZEN certified fields and carry
the claim.  lambda = 0.075 is 919's DECLARED DESIGN EXTENSION, inherited with
its flag.  lambda in {0.0625, 0.0875, 0.09375} are DECLARED NON-CLAIM SEAL
TARGETS chosen inside the certified band and never evaluated before the seal.

ROUTES.  Route P is the pinned Cycle-919 code itself: the certification
functions are extracted VERBATIM from the pinned 919 source bytes and executed,
so the reproduction gate tests this environment rather than a paraphrase.
Route N is a fully independent implementation written for this block (Hamiltonian
assembled by explicit Kronecker products, entropies from singular values of the
reshaped amplitude tensor, branch split performed before any reduction), on a
dense eigendecomposition for n <= 11 and on a scaling-and-marching Taylor
propagator with a rigorous factorial remainder bound for n >= 12.  Route P's
propagator is a Chebyshev expansion with a rigorous Bessel tail bound.  The two
propagators share no algorithm.  Route N is cross-validated against route P on
every anchor cell before it is used for any new number.

RESOLUTION.  The dense grid is justified against the EXACT spectral content:
for each cell the Bohr bandwidth omega_max = E_max - E_min is computed (or
bounded by 2(||diag||_inf + lambda n)), and the dense step is reported as a
multiple of the Nyquist step pi/omega_max.  Window edges are then located by
BISECTION on the frozen predicate to 1e-12, so no edge number depends on the
scan step at all.  The scan step only has to be fine enough to find every
sign change; a quarter-step rescan verifies the block structure.

RESTRICTION GATES.  Before any new number: 24 pins by sha256 and git blob;
21/21 frozen constants byte-verified out of the memo and quote-identical to the
917, 919, 921, 926, 927, 929 AND 931 receipts (seven-way); the statistic
definition byte-verified; the memo's own six cube fragment lists reproduced by
the partition rule; the full 919 ladder (34 cells), its persistence profiles and
its C_ab certification-window table reproduced value-for-value at deviation
EXACTLY 0; 926's persistence axis, deadline axis and threshold band reproduced;
927's per-degree pair-tax minima reproduced; 931's pair-complement identity
verified on the certified cells.

Deterministic, float64/complex128, no network, no tree writes outside the
declared receipt and runner cache.

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
    "scripts/frontier_cycle919_degree_five_2026_07_28.py": (
        "15ce5dbd37cea6e4d7286dc85d0c04abd9948bae2a84910e5f9486c5fa35b196",
        "c22ebafcb743824db67ef1abe9f2f223ea6664a1"),
    "scripts/frontier_cycle926_gate_sweep_separation_2026_07_28.py": (
        "3ca9053caf419b8e549c1395acd9b568495745ac703a508dffce75ca8f136d8a",
        "40c5e71080f864db8545676b1d02f9a5e4d4b17f"),
    "scripts/frontier_cycle927_size_channel_2026_07_28.py": (
        "caa3becbd2bfc97afc106e998e5f2b9ee23cb46efd8c673d04ee69ed554314a9",
        "fe2e0f14d1762e44c00b028ca40c5ead851fb48a"),
    "scripts/frontier_cycle929_arity_variable_2026_07_28.py": (
        "626be10a174d9ff41f72daa97a7eddc403e5ce191aff56791b38d0cea740c08a",
        "1d629b43c4be15f4ffd7a2ac562ce8538088414e"),
    "scripts/frontier_cycle931_additivity_identity_2026_07_28.py": (
        "9ec41f8cc7562026e86a5332819b56b860b1ee3f4a4ca21540f129623ec80371",
        "a0cd5b6fa01ad6b262c18b0e69c57600d1979367"),
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json": (
        "d7d27ce19d231624415db1e71ee77eae16b5175dd403b403c254b38fb171b0a7",
        "9931c298a5917eb90de290cbb82c237508c9e692"),
    "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json": (
        "37568809db0d5f319b6fe9a41962cc58c8215ade2c4b9acb24eab4b665535240",
        "11e336cf0a86c46492f6ccf03b13963357840b71"),
    "outputs/degree_five_cycle919_receipt_2026_07_28.json": (
        "cf85c74b62f1e6a83287a824f56315f3b1cf4b9387056d94906bb0195aae04f5",
        "587349db8b77c31d20f0aa04e6e69a1bb206a6d0"),
    "outputs/degree_five_independent_check_cycle919_receipt_2026_07_28.json": (
        "b455e3c5669f4cfeae0046a6ffb410daac8ce4bb89465b1a30f884190c232662",
        "bd57ac3ec780e0cb95e1f821fb159c52b0988690"),
    "outputs/loop_cost_cycle921_receipt_2026_07_28.json": (
        "86e58837349baa719d116948c67a166b922cb6b21fefe6108ec41fa08727df6f",
        "01e9689639dee1dc6f73c6a2834a84da3dc9f6cc"),
    "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json": (
        "59d24f68b7bdd3ba8fa2e446a2e381c4c5dd97443915bf38b0823556369a4c07",
        "67f39ff8875def945e32e7dccc653423a8c4fc79"),
    "outputs/gate_sweep_block_cycle926_ship_receipt_2026_07_28.json": (
        "82b109a844966649f51e176d2e3cc9f3eb8ca45a39fbef39488964711905b015",
        "adba5d9f3249d23645fdfc5114d08227fbadd77e"),
    "outputs/size_channel_cycle927_receipt_2026_07_28.json": (
        "2dd871f70c6486a20babb7b74048befb51a108a0feea57aee86ba3ff7f2fe51c",
        "12edc846cdb31c19e5f9bb709533ee18d5d5a092"),
    "outputs/arity_variable_cycle929_receipt_2026_07_28.json": (
        "40440237f0af14882b06331a054c19f3da52f34e6e7b2cde846a0b390a3679a3",
        "fc0080cc4c283d6dc440ac20a614ae187f7e488b"),
    "outputs/additivity_identity_cycle931_receipt_2026_07_28.json": (
        "89699b750d39e6bbf1b953e4abc34a71784344b89012be31226acb6ccfd97b46",
        "d3894ad5792018b541eda7185399c7c979ec09cf"),
    "outputs/additivity_identity_block_cycle931_ship_receipt_2026_07_28.json": (
        "2cc09b5be0c45472ea07d96177361c1d788a02f8f23879e559508927f024625c",
        "0d32835e3ab332941aae9f1f04b31b6802c09708"),
    "docs/PAIR_COMPLEMENT_THEOREM_ADDITIVITY_DERIVED_CYCLE931_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "f9d9a3cf0051182c9608d94af37737e59735780c63a6dd0ae813891a654cfb76",
        "d5d9776fe023143d465d4da039730e431acf84ca"),
    "docs/ARITY_IS_DEGREE_MULTIPLICITY_TAX_CYCLE929_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "b45a3f9014850af577a27c4206504f6935abaccd676166d58e4e8f4f966ed4a0",
        "0b316a500c4c6768b36651d71eb8702731d19f9e"),
    "docs/SIZE_CHANNEL_NULL_ARITY_DILUTION_THRESHOLD_HARDENS_CYCLE927_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "18914fa29e3594dfb92465ba1128d61911861e12d756f910d573e662145caf2c",
        "c066b3acf0d19eb54fae5e50c07d2774f1cd8521"),
    "docs/GEOMETRY_LADDER_CHAIN_CERTIFIES_CYCLE917_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "b424c3aaf684015f6ca08e81446df58c2d85a1c4e981a8c220be165989d057d4",
        "6311514dcd9a97f1a14b0ba7249b7570baeaff14"),
}

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
C919_RUNNER = "scripts/frontier_cycle919_degree_five_2026_07_28.py"
C921_RECEIPT = "outputs/loop_cost_cycle921_receipt_2026_07_28.json"
C926_RECEIPT = "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json"
C927_RECEIPT = "outputs/size_channel_cycle927_receipt_2026_07_28.json"
C929_RECEIPT = "outputs/arity_variable_cycle929_receipt_2026_07_28.json"
C931_RECEIPT = "outputs/additivity_identity_cycle931_receipt_2026_07_28.json"

D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
FROZEN_LAMBDAS = (0.05, 0.10)
EXTENSION_LAMBDA = 0.075
LAMBDAS = (0.05, 0.075, 0.10)
SEAL_LAMBDAS = (0.0625, 0.0875, 0.09375)   # DECLARED NON-CLAIM seal targets
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
T0_ANCHOR_TOL = 1e-9
DRIFT_MAX = 0.10
PERSIST_N = 3
T_EXEC = [round(0.1 * i, 10) for i in range(13)]     # Jt = 0.0 .. 1.2, 13 points
GRID_SPACING = 0.1
CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")

REPRO_TOL = 0.0            # reproduction gates demand deviation EXACTLY zero
ROUTE_TOL = 1e-11          # route N vs route P cross-validation
BISECT_TOL = 1e-12         # window-edge bisection tolerance
SCAN_LO, SCAN_HI = 0.0, 1.3
DENSE_DT_SMALL = 0.0025    # n <= 11
DENSE_DT_BIG = 0.005       # n >= 12 (declared capped grid)
DENSE_N_CAP = 11           # above this, route N marches instead of diagonalising

# bookkeeping that makes the seal auditable
SEAL_LOCKED = {"locked": False, "cells": set()}
FROZEN_EVAL_LOG = []


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_obj(o):
    return sha256_bytes(json.dumps(o, sort_keys=True, separators=(",", ":"),
                                   default=float).encode("utf-8"))


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
    """Read the never-landed d=1 comparator note out of git history (917's route)."""
    if git(["cat-file", "-e", "HEAD:%s" % D1_NOTE_PATH]).returncode == 0:
        die("d1-note:unexpectedly-in-tree")
    if git(["cat-file", "-t", D1_NOTE_BLOB]).stdout.decode().strip() != "blob":
        die("d1-note:blob-missing %s" % D1_NOTE_BLOB)
    b = git(["cat-file", "blob", D1_NOTE_BLOB]).stdout
    got = sha256_bytes(b)
    if got != D1_NOTE_SHA256 or len(b) != D1_NOTE_BYTES:
        die("d1-note:identity got=%s bytes=%d" % (got, len(b)))
    for tag, rp, key in (("915", C915_RECEIPT, None), ("917", C917_RECEIPT, "sha256")):
        rec = json.load(open(os.path.join(ROOT, rp)))
        if tag == "915":
            art = rec["C1_recovery"]["artifacts"][D1_NOTE_PATH]["recovered"]
            if art["sha256"] != got or art["blob"] != D1_NOTE_BLOB:
                die("d1-note:915-cross-check")
        else:
            if rec["recovered_d1_note"]["sha256"] != got:
                die("d1-note:917-cross-check")
    return {"path": D1_NOTE_PATH, "blob": D1_NOTE_BLOB, "sha256": got,
            "bytes": len(b), "in_tree_at_head": False,
            "cross_checked_against": ["915 receipt", "917 receipt"]}


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

STATISTIC_PATTERNS = [
    ("C_ab_definition", r"`C_ab = I\(F_a:F_b \| Z_S\)`"),
    ("C_ab_formula",
     r"`C_ab = sum_z p_z \[S\(rho_Fa\^z\)\+S\(rho_Fb\^z\)-S\(rho_FaFb\^z\)\]`"),
    ("C_ab_tensor_order", r"The joint tensor order is `\(S,F_a,F_b\)`"),
    ("C_ab_dephasing", r"Zero the off-diagonal `S` blocks before evaluating the formula"),
    ("chi_definition",
     r"`chi_Z\(S:F\) = S\(sum_z p_z rho_F\^z\) - sum_z p_z S\(rho_F\^z\)`\."),
]

# The RUN RULE and the SAMPLE GRID are protocol text, not memo regex: they are
# quoted from the pinned 919 source bytes in quote_run_rule() below.


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


def verify_statistic_definition(memo):
    out = {}
    for name, pat in STATISTIC_PATTERNS:
        m = re.search(pat, memo)
        if m is None:
            die("statistic-def:pattern-miss %s" % name)
        out[name] = " ".join(m.group(0).split())
    return out


def cross_check_prior_constants(frozen):
    """21/21 quote-identical to EVERY pinned receipt that publishes them -- SEVEN."""
    res = {}
    for tag, rp in (("917", C917_RECEIPT), ("919", C919_RECEIPT), ("921", C921_RECEIPT),
                    ("926", C926_RECEIPT), ("927", C927_RECEIPT), ("929", C929_RECEIPT),
                    ("931", C931_RECEIPT)):
        theirs = json.load(open(os.path.join(ROOT, rp)))["frozen_constants_byte_verified"]
        if set(theirs) != set(frozen):
            die("frozen-const:%s-key-set" % tag)
        for k in sorted(frozen):
            if theirs[k]["quote"] != frozen[k]["quote"]:
                die("frozen-const:%s-quote %s" % (tag, k))
        res["identical_to_%s_receipt" % tag] = True
    res["count"] = len(frozen)
    res["ways"] = 7
    res["all_seven_receipts_agree"] = True
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


# ============================ ROUTE P: the pinned Cycle-919 code, executed ===
PINNED_FUNCTIONS = [
    "bfs", "cube_tiebreak", "build_geometry",
    "geom_chain9", "geom_star7", "geom_tree", "geom_plaquette9", "_axis_label",
    "geom_cubeminus11", "geom_cube27", "geom_star6", "geom_tree16", "geom_tree10d5",
    "geom_cubeminus10",
    "build_diag", "prep_state", "_matvec_factory", "chebyshev", "taylor_march",
    "dense_route", "joint_rho", "ent_bits", "chi_holevo", "cond_mi", "r_ind",
    "centered_frobenius", "measure", "event_of", "xi_reg_of", "verdict_of",
    "cell_of", "run_route_A", "persistence_profile",
]


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


def load_route_P():
    """Execute the pinned 919 certification code in a private namespace.

    This is stronger than paraphrasing it: the reproduction gate then tests
    whether THIS environment reproduces the pinned numbers, not whether a
    re-implementation happens to agree.
    """
    ns = {"np": np, "itertools": itertools, "math": math, "deque": deque, "jv": jv,
          "die": die, "CUBE_LABELS": CUBE_LABELS, "DELTAS": DELTAS,
          "CONTENT_H_MIN": CONTENT_H_MIN, "EXCESS_MIN": EXCESS_MIN,
          "INDEP_MAX": INDEP_MAX, "DEADLINE_JT": DEADLINE_JT,
          "PERSIST_N": PERSIST_N, "DRIFT_MAX": DRIFT_MAX,
          "HEADLINE_DELTA": HEADLINE_DELTA, "T_EXEC": T_EXEC}
    quotes = {}
    for fn in PINNED_FUNCTIONS:
        q = extract_pinned_source(C919_RUNNER, fn)
        quotes[fn] = {k: v for k, v in q.items() if k != "verbatim"}
        exec(compile(q["verbatim"], "<pinned:919:%s>" % fn, "exec"), ns)
    for fn in PINNED_FUNCTIONS:
        if fn not in ns or not callable(ns[fn]):
            die("route-P:missing %s" % fn)
    return ns, quotes


def quote_run_rule(quotes, ns):
    """The RUN RULE, the SAMPLE GRID and the DEADLINE, quoted from pinned bytes."""
    src = open(os.path.join(ROOT, C919_RUNNER), "rb").read().decode("utf-8")
    out = {}
    pats = {
        "sample_grid": r"T_EXEC = \[round\(0\.1 \* i, 10\) for i in range\(13\)\][^\n]*",
        "persist_n": r"PERSIST_N = 3[^\n]*",
        "deadline": r"DEADLINE_JT = 1\.0",
        "indep_max": r"INDEP_MAX = 0\.02[^\n]*",
        "excess_min": r"EXCESS_MIN = 0\.02[^\n]*",
        "content_h_min": r"CONTENT_H_MIN = 0\.05[^\n]*",
        "run_rule_prose": r"persistence flag requires three consecutive certification samples",
    }
    for k, p in pats.items():
        m = re.search(p, src)
        if m is None:
            die("run-rule:quote-miss %s" % k)
        out[k] = " ".join(m.group(0).split())
    out["run_rule_code"] = " ".join(quotes and
                                    extract_pinned_source(C919_RUNNER,
                                                          "event_of")["verbatim"].split())
    out["persistence_predicate"] = ('"persists": bool(run >= PERSIST_N) with run counted '
                                    "as the number of CONSECUTIVE samples from the first "
                                    "sample with R_ind >= 2, on the grid T_EXEC")
    out["sample_times"] = list(T_EXEC)
    out["grid_spacing"] = GRID_SPACING
    if list(ns["chebyshev"].__code__.co_varnames[:5]) == []:
        die("run-rule:sanity")
    return out


# =============================== ROUTE N: this block's own implementation ====
SIG_X = np.array([[0.0, 1.0], [1.0, 0.0]])
SIG_Z = np.array([[1.0, 0.0], [0.0, -1.0]])
EYE2 = np.eye(2)


def kron_op(n, ops):
    """Explicit Kronecker assembly.  Site i occupies bit i, i.e. is the (n-1-i)-th
    factor in the left-to-right Kronecker order used by joint_rho's reshape."""
    M = np.array([[1.0]])
    for f in range(n):
        M = np.kron(M, ops[n - 1 - f])
    return M


def route_N_hamiltonian(n, bonds, lam):
    d = 1 << n
    H = np.zeros((d, d))
    for (a, b) in bonds:
        ops = [EYE2] * n
        ops[a] = SIG_Z
        ops[b] = SIG_Z
        H -= kron_op(n, ops)
    for i in range(n):
        ops = [EYE2] * n
        ops[i] = SIG_X
        H -= lam * kron_op(n, ops)
    return H


def route_N_prep(n, plus_x):
    """Product preparation, assembled left-to-right (opposite of route P's fold)."""
    psi = np.array([1.0 + 0.0j])
    for f in range(n):
        i = n - 1 - f
        v = (np.array([1.0, 1.0]) / np.sqrt(2.0)) if i in plus_x else np.array([1.0, 0.0])
        psi = np.kron(psi, v.astype(np.complex128))
    return psi


def svd_entropy(psi, n, sites):
    """S of the reduced state on `sites`, from SINGULAR VALUES of the reshaped
    amplitude tensor (no density matrix, no eigensolver)."""
    T = psi.reshape((2,) * n)
    order = list(sites) + [i for i in range(n) if i not in sites]
    ax = [n - 1 - s for s in order]
    M = np.transpose(T, ax).reshape(1 << len(sites), -1)
    s = np.linalg.svd(M, compute_uv=False)
    p = s ** 2
    p = p[p > 1e-16]
    p = p / p.sum()
    return float(-(p * np.log2(p)).sum())


def branch_vectors(psi, n, S):
    """Split on the pointer's Z value FIRST, then hand back normalised branches."""
    T = psi.reshape((2,) * n)
    ax = [n - 1 - S] + [n - 1 - i for i in range(n) if i != S]
    M = np.transpose(T, ax).reshape(2, -1)
    out = []
    for z in (0, 1):
        w = float(np.vdot(M[z], M[z]).real)
        out.append((w, M[z] / math.sqrt(w) if w > 1e-14 else M[z]))
    tot = out[0][0] + out[1][0]
    return [(w / tot, v) for (w, v) in out], tot


def route_N_observables(psi, n, S, frag_list, labels):
    """H_Z, chi per fragment, C_ab per pair -- entirely via SVD on branch vectors."""
    br, _ = branch_vectors(psi, n, S)
    rest = [i for i in range(n) if i != S]
    nb = n - 1
    # branch_vectors leaves rest[j] on tensor AXIS j; svd_entropy/s_mixed address a
    # "site" s by axis nb-1-s, so the pointer-free site label of rest[j] is nb-1-j.
    pos = {s: nb - 1 - k for k, s in enumerate(rest)}
    p = [br[0][0], br[1][0]]
    H_Z = -sum(q * math.log2(q) for q in p if q > 1e-15)

    def s_branch(axes):
        return [svd_entropy(v, nb, axes) for (_, v) in br]

    def s_avg(axes):
        return sum(pz * e for pz, e in zip(p, s_branch(axes)))

    def s_mixed(axes):
        """Entropy of the branch-AVERAGED reduced state (needed for chi)."""
        acc = None
        for pz, v in br:
            T = v.reshape((2,) * nb)
            ax = [nb - 1 - s for s in list(axes) + [i for i in range(nb)
                                                    if i not in axes]]
            M = np.transpose(T, ax).reshape(1 << len(axes), -1)
            r = pz * (M @ M.conj().T)
            acc = r if acc is None else acc + r
        w = np.linalg.eigvalsh(acc)
        w = w[w > 1e-16]
        return float(-(w * np.log2(w)).sum())

    chi = {}
    for L in labels:
        axes = [pos[i] for i in frag_list[L]]
        chi[L] = s_mixed(axes) - s_avg(axes)
    C = {}
    for a, b in itertools.combinations(labels, 2):
        aa = [pos[i] for i in frag_list[a]]
        bb = [pos[i] for i in frag_list[b]]
        sa, sb, sab = s_avg(aa), s_avg(bb), s_avg(aa + bb)
        C["|".join((a, b))] = sa + sb - sab
    return {"H_Z": H_Z, "p_z": p, "chi": chi, "C_ab": C}


class CellN:
    """Route-N evolution engine for one (geometry, field) cell."""

    def __init__(self, g, lam):
        self.g = g
        self.lam = lam
        self.n = g["n"]
        self.S = g["S"]
        self.labels = g["labels"]
        self.frags = g["frags"]
        self.psi0 = route_N_prep(self.n, set([self.S] + list(g["recording"])))
        diagabs = float(max(abs(sum(-1.0 for _ in [])), 0.0))
        self.Ainf = float(len(g["bonds"]) + lam * self.n)
        self.mode = "eigh" if self.n <= DENSE_N_CAP else "taylor"
        self.calls = 0
        if self.mode == "eigh":
            H = route_N_hamiltonian(self.n, g["bonds"], lam)
            w, V = np.linalg.eigh(H)
            self.w, self.V = w, V
            self.c = V.T @ self.psi0
            self.bandwidth = float(w[-1] - w[0])
        else:
            self.bandwidth = 2.0 * self.Ainf
            self._cache = [(0.0, self.psi0.copy())]
            self._diag = np.zeros(1 << self.n)
            idx = np.arange(1 << self.n, dtype=np.uint32)
            z = np.empty((self.n, 1 << self.n), dtype=np.int8)
            for i in range(self.n):
                z[i] = 1 - 2 * ((idx >> np.uint32(i)) & np.uint32(1)).astype(np.int8)
            for (a, b) in g["bonds"]:
                self._diag -= z[a].astype(np.float64) * z[b].astype(np.float64)
            self._xor = [np.arange(1 << self.n, dtype=np.int64) ^ (1 << i)
                         for i in range(self.n)]
        self.base = self.observables(0.0)
        self.chi0 = dict(self.base["chi"])

    def _mv(self, v):
        o = self._diag * v
        for i in range(self.n):
            o = o - self.lam * v[self._xor[i]]
        return o

    def _march(self, psi, t0, t1, hbound=0.5, pmax=48):
        dt = t1 - t0
        if abs(dt) < 1e-16:
            return psi.copy()
        s = max(1, int(math.ceil(abs(dt) * self.Ainf / hbound)))
        h = dt / s
        for _ in range(s):
            term = psi.copy()
            acc = psi.copy()
            for k in range(1, pmax + 1):
                term = self._mv(term) * (-1j * h / k)
                acc = acc + term
                if float(np.abs(term).max()) < 1e-18:
                    break
            psi = acc
        return psi

    def state(self, t):
        self.calls += 1
        if self.mode == "eigh":
            return self.V @ (np.exp(-1j * self.w * t) * self.c)
        best = min(self._cache, key=lambda kv: abs(kv[0] - t))
        psi = self._march(best[1], best[0], t)
        if len(self._cache) < 4096:
            self._cache.append((t, psi.copy()))
        return psi

    def observables(self, t):
        return route_N_observables(self.state(t), self.n, self.S, self.frags, self.labels)

    def gates(self, t, delta=HEADLINE_DELTA):
        o = self.observables(t)
        chi, C, H = o["chi"], o["C_ab"], o["H_Z"]
        exc = {L: chi[L] - self.chi0[L] for L in self.labels}
        passes = [L for L in self.labels
                  if H >= CONTENT_H_MIN and chi[L] >= (1.0 - delta) * H
                  and exc[L] >= EXCESS_MIN]
        pairs = {k: v for k, v in C.items() if all(q in passes for q in k.split("|"))}
        ok_pairs = {k: v for k, v in pairs.items() if v <= INDEP_MAX}
        # R_ind >= 2 <=> at least one content-passing pair is under the gate
        r_ge2 = len(ok_pairs) >= 1
        binding = min(pairs.values()) if pairs else None
        return {"t": t, "H_Z": H, "chi": chi, "excess": exc, "C_ab": C,
                "n_content_passes": len(passes), "content_passes": passes,
                "binding_pair_C_ab": binding,
                "binding_pair": (min(pairs, key=pairs.get) if pairs else None),
                "r_ind_ge2": bool(r_ge2),
                "m_H": H - CONTENT_H_MIN,
                "m_content": (max(chi.values()) - (1.0 - delta) * H),
                "m_excess": (max(exc.values()) - EXCESS_MIN),
                "m_indep": (None if binding is None else INDEP_MAX - binding)}

    def cert(self, t, delta=HEADLINE_DELTA):
        return self.gates(t, delta)["r_ind_ge2"]


# ================================================== window-edge localisation ==
def scan_blocks(cell, dt, lo=SCAN_LO, hi=SCAN_HI, delta=HEADLINE_DELTA):
    ts = [lo + k * dt for k in range(int(round((hi - lo) / dt)) + 1)]
    flags = [cell.cert(t, delta) for t in ts]
    blocks, cur = [], None
    for i, f in enumerate(flags):
        if f and cur is None:
            cur = i
        elif not f and cur is not None:
            blocks.append((cur, i - 1))
            cur = None
    if cur is not None:
        blocks.append((cur, len(flags) - 1))
    return ts, flags, blocks


def bisect_edge(cell, t_false, t_true, delta=HEADLINE_DELTA, tol=BISECT_TOL):
    """Locate the predicate transition between a FALSE point and a TRUE point."""
    a, b = t_false, t_true
    for _ in range(200):
        m = 0.5 * (a + b)
        if cell.cert(m, delta):
            b = m
        else:
            a = m
        if abs(b - a) < tol:
            break
    return 0.5 * (a + b)


def clip_identity(cell, t_out, t_in, delta=HEADLINE_DELTA):
    """Which gate is binding just OUTSIDE the window edge."""
    g = cell.gates(t_out, delta)
    cands = {"content_H": g["m_H"], "content_chi": g["m_content"],
             "content_excess": g["m_excess"]}
    if g["m_indep"] is not None:
        cands["independence"] = g["m_indep"]
    if g["n_content_passes"] < 2:
        # no eligible pair at all: the content side has already closed
        worst = min(("content_H", "content_chi", "content_excess"),
                    key=lambda k: cands[k])
        return worst, {k: v for k, v in cands.items()}
    worst = min(cands, key=lambda k: cands[k])
    return worst, {k: v for k, v in cands.items()}


def window_of(cell, dt, delta=HEADLINE_DELTA):
    ts, flags, blocks = scan_blocks(cell, dt, delta=delta)
    out = []
    for (i, j) in blocks:
        lo = 0.0 if i == 0 else bisect_edge(cell, ts[i - 1], ts[i], delta)
        if j == len(ts) - 1:
            hi = ts[j]
            hi_clipped = "scan-horizon"
            hi_margins = {}
        else:
            hi = bisect_edge(cell, ts[j + 1], ts[j], delta)
            hi_clipped, hi_margins = clip_identity(cell, ts[j + 1], ts[j], delta)
        lo_clipped, lo_margins = (("t=0", {}) if i == 0
                                  else clip_identity(cell, ts[i - 1], ts[i], delta))
        out.append({"lo": lo, "hi": hi, "width": hi - lo,
                    "open_gate": lo_clipped, "close_gate": hi_clipped,
                    "open_margins": lo_margins, "close_margins": hi_margins})
    return {"blocks": out, "n_blocks": len(out), "scan_dt": dt,
            "n_scan_points": len(ts)}


def grid_samples_in(win, offset=0.0, grid=None):
    g = list(grid if grid is not None else T_EXEC)
    pts = [round(x + offset, 12) for x in g]
    return [x for x in pts if win["lo"] - 1e-12 <= x <= win["hi"] + 1e-12 and x >= 0.0]


def predicted_run_and_verdict(wins, offset=0.0):
    """The WINDOW-EDGE PREDICTION of the frozen protocol's run and verdict."""
    best = None
    for w in wins:
        pts = grid_samples_in(w, offset)
        if not pts:
            continue
        if best is None or pts[0] < best[0]:
            best = (pts[0], len(pts), w)
    if best is None:
        return {"run": 0, "verdict": "NO", "first_jt": None,
                "reason": "no sample inside any certifiable window"}
    first, run, _ = best
    if first > DEADLINE_JT + 1e-12:
        return {"run": run, "verdict": "NO", "first_jt": first, "reason": "late"}
    if run < PERSIST_N:
        return {"run": run, "verdict": "NO", "first_jt": first, "reason": "persistence"}
    return {"run": run, "verdict": "YES", "first_jt": first, "reason": None}


# ==================================================== geometry constructors ===
def make_star(ns, d):
    """S_d: K_{1,d} -- pointer degree d, depth 1, no loops, singleton fragments."""
    sites = ["S"] + ["a%d" % i for i in range(1, d + 1)]
    bonds = [("S", "a%d" % i) for i in range(1, d + 1)]
    return ns["build_geometry"]("S%d" % d, "star%d" % (d + 1), sites, bonds, "S",
                                lambda c: c, None, "star",
                                "Cycle 932 degree sweep: K_{1,%d}" % d)


def build_all(ns):
    G = {}
    for k, f in (("G1", ns["geom_chain9"]), ("G2", ns["geom_star7"]),
                 ("G3a", lambda: ns["geom_tree"](3)), ("G3b", lambda: ns["geom_tree"](4)),
                 ("G4", ns["geom_plaquette9"]), ("G5", ns["geom_cubeminus11"]),
                 ("H1", ns["geom_star6"]), ("H2", ns["geom_tree16"]),
                 ("H3", ns["geom_tree10d5"]), ("H4", ns["geom_cubeminus10"])):
        G[k] = f()
    for d in range(2, 9):
        G["S%d" % d] = make_star(ns, d)
    return G


# ================================================================== teeth =====
TEETH = []


def tooth(name, description, fired, detail):
    TEETH.append({"tooth": name, "description": description,
                  "fired": bool(fired), "detail": detail})
    if not fired:
        die("tooth:did-not-fire %s" % name)


# ================================================================== main =====
def main():
    pins = verify_pins()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    const_x = cross_check_prior_constants(frozen)
    statdef = verify_statistic_definition(memo)
    d1 = recover_d1_note()
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()

    P, quotes = load_route_P()
    runrule = quote_run_rule(quotes, P)
    G = build_all(P)

    r919 = json.load(open(os.path.join(ROOT, C919_RECEIPT)))
    r926 = json.load(open(os.path.join(ROOT, C926_RECEIPT)))
    r927 = json.load(open(os.path.join(ROOT, C927_RECEIPT)))
    r931 = json.load(open(os.path.join(ROOT, C931_RECEIPT)))

    lines = []

    def say(s=""):
        lines.append(s)
        print(s)

    say("===== runner cache v1 =====")
    say("runner: scripts/frontier_cycle932_persistence_razor_2026_07_28.py")
    say("cycle: 932  block: toe-time-blockM12-20260802  head: %s" % head)
    say("")
    say("-- THE FROZEN DEFINITIONS, quoted from pinned bytes --")
    say("  sample grid:  %s" % runrule["sample_grid"])
    say("                Jt = %s" % ", ".join("%.1f" % t for t in T_EXEC))
    say("  run rule:     %s" % runrule["run_rule_prose"])
    say("                %s" % runrule["persistence_predicate"])
    say("  persist_n:    %s" % runrule["persist_n"])
    say("  deadline:     %s   (memo: %s)" % (runrule["deadline"],
                                             frozen["deadline"]["quote"]))
    say("  indep gate:   %s   (memo: %s)" % (runrule["indep_max"],
                                             frozen["indep_max"]["quote"]))
    say("  C_ab:         %s" % statdef["C_ab_formula"])
    say("")

    # ================================================== RESTRICTION GATES =====
    t_gate = time.perf_counter()
    say("-- RESTRICTION GATES (all before any new number) --")
    say("  pins verified: %d" % len(pins))
    say("  21/21 frozen constants byte-verified; quote-identical to the 917, 919,")
    say("  921, 926, 927, 929 AND 931 receipts (SEVEN-way): %s"
        % const_x["all_seven_receipts_agree"])
    say("  statistic definition from memo bytes: %s" % statdef["C_ab_formula"])
    say("  route P = %d functions executed VERBATIM from the pinned 919 bytes"
        % len(PINNED_FUNCTIONS))

    # gate 1: the partition rule vs the memo's own six cube lists
    memo_frags = parse_memo_cube_fragments(memo)
    g6 = P["geom_cube27"]()
    mine = {L: sorted(tuple(g6["coords"][i]) for i in g6["frags"][L]) for L in g6["labels"]}
    theirs = {L: sorted(tuple(c) for c in memo_frags[L]) for L in memo_frags}
    part_ok = (mine == theirs)
    if not part_ok:
        die("restriction:partition-rule")
    say("  partition rule reproduces the memo's six cube lists: %s" % part_ok)

    # gate 2: the full 919 ladder, value-for-value, deviation exactly 0
    ROWS = {}       # (key, lam) -> rows (route P, frozen grid)
    def frozen_rows(key, lam):
        ck = (key, round(lam, 10))
        if ck in ROWS:
            return ROWS[ck]
        if SEAL_LOCKED["locked"] and ck in SEAL_LOCKED["cells"]:
            pass    # sealed cells are allowed AFTER the seal is locked
        elif ck in SEAL_LOCKED["cells"]:
            die("seal:frozen-machinery-ran-before-seal %s@%s" % (key, lam))
        g = G[key]
        diag = P["build_diag"](g["n"], g["bonds"])
        psi0 = P["prep_state"](g["n"], set([g["S"]] + list(g["recording"])))
        rows, mach, prop = P["run_route_A"](g, diag, psi0, lam)
        FROZEN_EVAL_LOG.append({"cell": "%s@%s" % (key, lam), "route": "P/chebyshev"})
        ROWS[ck] = (rows, mach, prop, g, diag, psi0)
        return ROWS[ck]

    dev_ladder = 0.0
    n_cells = 0
    n_rows = 0
    for ck, want in sorted(r919["ladder_by_cell"].items()):
        key, lam = ck.split("@")
        if key == "G6":
            continue                     # 919 declares G6 not re-run
        lam = float(lam)
        rows, mach, prop, g, diag, psi0 = frozen_rows(key, lam)
        cf = P["centered_frobenius"](lam, g["n"], len(g["bonds"]), g["degrees"])
        comm_ok = max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values())
        got = P["verdict_of"](rows, HEADLINE_DELTA, comm_ok)
        if got["verdict"] != want["verdict"]:
            die("restriction:919-verdict %s got=%s want=%s"
                % (ck, got["verdict"], want["verdict"]))
        mx = max(r["r_ind"]["%.2f" % HEADLINE_DELTA] for r in rows)
        if mx != want["max_r_ind"]:
            die("restriction:919-max_r_ind %s" % ck)
        if (got["event"] is None) != (want["event"] is None):
            die("restriction:919-event-presence %s" % ck)
        if got["event"] is not None:
            for f in ("jt", "run", "r_ind", "by_deadline", "persists"):
                if got["event"][f] != want["event"][f]:
                    die("restriction:919-event-%s %s" % (f, ck))
            for f in ("theta_A", "pointer_tv_drift"):
                dev_ladder = max(dev_ladder, abs(got["event"][f] - want["event"][f]))
            for k2, v2 in want["event"]["C_at_event"].items():
                dev_ladder = max(dev_ladder, abs(got["event"]["C_at_event"][k2] - v2))
            for k2, v2 in want["event"]["chi_at_event"].items():
                dev_ladder = max(dev_ladder, abs(got["event"]["chi_at_event"][k2] - v2))
        xi = P["xi_reg_of"](rows)
        if xi["xi_reg"] != want["xi_reg"]:
            die("restriction:919-xi_reg %s" % ck)
        for d in DELTAS:
            vd = P["verdict_of"](rows, d, comm_ok)["verdict"]
            if vd != want["verdict_by_delta"]["%.2f" % d]:
                die("restriction:919-verdict_by_delta %s %s" % (ck, d))
        n_cells += 1
        n_rows += len(rows)
    if dev_ladder > REPRO_TOL:
        die("restriction:919-ladder dev=%.3e (demanded exactly 0.0)" % dev_ladder)
    say("  919 ladder: %d cells / %d rows reproduced, max abs deviation %s"
        % (n_cells, n_rows, dev_ladder))

    dev_pp = 0.0
    n_pp = 0
    for lk, tab in sorted(r919["persistence_profiles"].items()):
        lam = float(lk)
        for key, want in sorted(tab.items()):
            if key == "G6":
                continue
            rows, *_ = frozen_rows(key, lam)
            got = P["persistence_profile"](rows)
            for f in ("run", "needed", "persists", "has_event", "misses_by_one_sample",
                      "clears_by_one_sample", "first_jt", "first_failing_sample_jt",
                      "first_failing_sample_binding_gate"):
                if f in want and got.get(f) != want.get(f):
                    die("restriction:919-persistence-%s %s@%s" % (f, key, lk))
            for f in ("margin_at_the_last_certifying_sample_bits",
                      "margin_at_the_third_sample_bits",
                      "deficit_at_the_first_failing_sample_bits"):
                a, b = got.get(f), want.get(f)
                if (a is None) != (b is None):
                    die("restriction:919-persistence-null-%s %s@%s" % (f, key, lk))
                if a is not None:
                    dev_pp = max(dev_pp, abs(a - b))
            for sg, sw in zip(got.get("samples", []), want.get("samples", [])):
                for f in ("jt", "r_ind", "n_content_passes", "binding_gate"):
                    if sg[f] != sw[f]:
                        die("restriction:919-sample-%s %s@%s" % (f, key, lk))
                for f in ("content_margin_bits", "min_C_ab_over_all_pairs",
                          "binding_pair_C_ab_among_content_passes",
                          "independence_margin_bits"):
                    if sw[f] is not None:
                        dev_pp = max(dev_pp, abs(sg[f] - sw[f]))
                n_pp += 1
    if dev_pp > REPRO_TOL:
        die("restriction:919-persistence dev=%.3e (demanded exactly 0.0)" % dev_pp)
    say("  919 persistence profiles: %d samples reproduced, max abs deviation %s"
        % (n_pp, dev_pp))

    dev_cw = 0.0
    n_cw = 0
    for lk, tab in sorted(r919["C_ab_at_certification_window"].items()):
        lam = float(lk)
        for key, want in sorted(tab.items()):
            rows, *_ = frozen_rows(key, lam)
            ev = P["event_of"](rows, HEADLINE_DELTA)
            for f, v in want.items():
                if not isinstance(v, (int, float)) or isinstance(v, bool):
                    continue
                cand = None
                if ev is not None and f in ("min", "max", "mean"):
                    vals = list(ev["C_at_event"].values())
                    cand = {"min": min(vals), "max": max(vals),
                            "mean": float(np.mean(vals))}[f]
                if cand is not None:
                    dev_cw = max(dev_cw, abs(cand - v))
                    n_cw += 1
    if dev_cw > REPRO_TOL:
        die("restriction:919-Cab-window dev=%.3e" % dev_cw)
    say("  919 C_ab certification-window table: %d values, max abs deviation %s"
        % (n_cw, dev_cw))

    # gate 3: 926's persistence axis, deadline axis and threshold band
    def sweep_verdict(key, lam, gate=INDEP_MAX, persist=PERSIST_N, deadline=DEADLINE_JT):
        rows, *_ = frozen_rows(key, lam)
        kk = "%.2f" % HEADLINE_DELTA
        flags = []
        for r in rows:
            passes = r["singleton_passes"][kk]
            pairs = [v for k2, v in r["C_ab"].items()
                     if all(q in passes for q in k2.split("|"))]
            flags.append(any(v <= gate for v in pairs))
        idx = next((i for i, f in enumerate(flags) if f), None)
        if idx is None:
            return "NO", 0, None
        run = 0
        for f in flags[idx:]:
            if f:
                run += 1
            else:
                break
        first = rows[idx]["jt"]
        if first > deadline + 1e-12:
            return "NO", run, first
        return ("YES" if run >= persist else "NO"), run, first

    dev_926 = 0
    for pk, want in sorted(r926["sweep"]["persist_axis_at_the_frozen_gate"].items()):
        for ck, wv in sorted(want["verdicts"].items()):
            key, lam = ck.split("@")
            if key == "G6":
                continue
            v, _, _ = sweep_verdict(key, float(lam), persist=int(pk))
            if v != wv:
                die("restriction:926-persist %s %s got=%s want=%s" % (pk, ck, v, wv))
            dev_926 += 1
    for dk, want in sorted(r926["sweep"]["deadline_axis_at_the_frozen_gate"].items()):
        for ck, wv in sorted(want["verdicts"].items()):
            key, lam = ck.split("@")
            if key == "G6":
                continue
            v, _, _ = sweep_verdict(key, float(lam), deadline=float(dk))
            if v != wv:
                die("restriction:926-deadline %s %s got=%s want=%s" % (dk, ck, v, wv))
            dev_926 += 1
    say("  926 persistence + deadline axes: %d verdicts reproduced exactly" % dev_926)

    # the 926 threshold band and the full segment ladder, recomputed from the rows.
    # 926's "threshold" is the smallest degree d such that EVERY geometry of degree
    # >= d certifies; "clean_cut" additionally requires every geometry below d to fail.
    # G6 (the 27-site cube) is excluded exactly as Cycle 919 excludes it; its removal
    # is verified not to move any pinned threshold.
    KEYS10 = ("G1", "G2", "G3a", "G3b", "G4", "G5", "H1", "H2", "H3", "H4")
    DEG11 = {k: G[k]["stats"]["pointer_degree"] for k in KEYS10}
    # G6 (the 27-site cube) is NOT re-run -- Cycle 919 declares the same exclusion.
    # Its per-segment membership is IMPORTED from the pinned 926 segment lists so that
    # thresholds and clean-cut flags are still evaluated on the full 11-key set.
    DEG11["G6"] = r919["branching_statistics"]["G6"]["pointer_degree"]

    def yes_set_at(gate, g6_yes):
        ys = [k for k in KEYS10 if sweep_verdict(k, 0.10, gate=gate)[0] == "YES"]
        if g6_yes:
            ys.append("G6")
        return sorted(ys)

    def threshold_of(yes):
        for d in range(1, 9):
            if all((DEG11[k] < d) or (k in yes) for k in DEG11):
                return d
        return 9

    def clean_of(yes, thr):
        return all(((DEG11[k] >= thr) == (k in yes)) for k in DEG11)

    segs = r926["sweep"]["threshold_boundaries"]["segments_at_persist3_deadline1"]
    n_seg = 0
    for s in segs:
        probe = 0.5 * (s["lo"] + s["hi"])
        g6 = "G6" in s["YES"]
        ys = yes_set_at(probe, g6)
        if ys != sorted(s["YES"]):
            die("restriction:926-segment-YES [%.9f,%.9f) got=%s want=%s"
                % (s["lo"], s["hi"], ys, s["YES"]))
        thr = threshold_of(ys)
        if thr != s["threshold"]:
            die("restriction:926-segment-threshold [%.9f,%.9f) got=%s want=%s"
                % (s["lo"], s["hi"], thr, s["threshold"]))
        if clean_of(ys, thr) != s["clean_cut"]:
            die("restriction:926-segment-clean [%.9f,%.9f)" % (s["lo"], s["hi"]))
        n_seg += 1
    fseg = r926["sweep"]["threshold_boundaries"]["frozen_segment"]
    band_lo, band_hi = fseg["lo"], fseg["hi"]
    # the boundary VALUES are attained: the YES set changes exactly there.  G6 is YES
    # on both sides of both boundaries in the pinned ladder, so it is held fixed here.
    band_ok = (yes_set_at(band_lo, True) == sorted(fseg["YES"])
               and yes_set_at(band_lo - 1e-12, True) != yes_set_at(band_lo, True)
               and yes_set_at(band_hi, True) != yes_set_at(band_lo, True)
               and yes_set_at(band_hi - 1e-12, True) == yes_set_at(band_lo, True)
               and threshold_of(yes_set_at(0.02, True)) == 5)
    if not band_ok:
        die("restriction:926-band")
    say("  926 gate-segment ladder: %d segments reproduced (YES sets, thresholds and "
        "clean-cut flags)" % n_seg)
    say("  926 C_ab-gate band for the threshold [%.16f, %.16f): boundary values "
        "attained exactly, threshold 5 inside" % (band_lo, band_hi))

    # gate 4: 927's per-degree pair-tax minima, on this block's own star family
    dev_927 = 0.0
    n927 = 0
    tab927 = r927["THE_MEASURED_LAW_degree_graded_pair_tax"]["by_field"]["0.1"]["by_pointer_degree"]
    for d in (3, 4, 5, 6, 8):
        rows, *_ = frozen_rows("S%d" % d, 0.10)
        ev = P["event_of"](rows, HEADLINE_DELTA)
        got = min(ev["C_at_event"].values())
        want = tab927[str(d)]["C_ab_min"]
        dev_927 = max(dev_927, abs(got - want))
        n927 += 1
    if dev_927 > REPRO_TOL:
        die("restriction:927-degree-table dev=%.3e" % dev_927)
    say("  927 per-degree pair-tax minima (stars, degrees 3,4,5,6,8): %d rows, "
        "max abs deviation %s" % (n927, dev_927))

    # gate 5: 931's pair-complement identity on the certified cells
    dev_931 = 0.0
    for d in (3, 4, 5, 6):
        for lam in FROZEN_LAMBDAS:
            cn = CellN(G["S%d" % d], lam)
            psi = cn.state(0.7)
            nb = cn.n - 1
            br, _ = branch_vectors(psi, cn.n, cn.S)
            s1 = sum(p * svd_entropy(v, nb, [0]) for p, v in br)
            s2 = sum(p * svd_entropy(v, nb, [0, 1]) for p, v in br)
            rows, *_ = frozen_rows("S%d" % d, lam)
            r7 = [r for r in rows if abs(r["jt"] - 0.7) < 1e-12][0]
            cab = min(r7["C_ab"].values())
            dev_931 = max(dev_931, abs((2 * s1 - s2) - cab))
    if dev_931 > 1e-12:
        die("restriction:931-pair-complement dev=%.3e" % dev_931)
    say("  931 pair-complement identity C_ab = 2 s(1,t) - s(2,t) on the certified "
        "star cells: max dev %.2e" % dev_931)

    # route N vs route P cross-validation on the anchors, before any new number
    dev_route = 0.0
    for key in ("S3", "S4", "S5", "S6", "G3a", "G3b", "H3"):
        for lam in LAMBDAS:
            cn = CellN(G[key], lam)
            rows, *_ = frozen_rows(key, lam)
            for r in rows:
                if r["jt"] < 0.55 or r["jt"] > 1.05:
                    continue
                o = cn.observables(r["jt"])
                dev_route = max(dev_route, abs(o["H_Z"] - r["H_Z"]))
                for L in cn.labels:
                    dev_route = max(dev_route, abs(o["chi"][L] - r["chi"][L]))
                for k2, v2 in r["C_ab"].items():
                    dev_route = max(dev_route, abs(o["C_ab"][k2] - v2))
    if dev_route > ROUTE_TOL:
        die("route:N-vs-P dev=%.3e" % dev_route)
    say("  route N (Kronecker + SVD + branch-first) vs route P (pinned Chebyshev): "
        "max abs deviation %.2e over 7 geometries x 3 fields" % dev_route)
    gate_secs = time.perf_counter() - t_gate
    say("  gate runtime: %.2f s" % gate_secs)
    say("")

    # ==================================== PRE-REGISTRATION of the discriminants
    prereg = {
        "prereg_id": "cycle932-persistence-razor-prereg-1",
        "candidates": {
            "a_window_width": {
                "statement": "the certifiable window's continuous width W(d,lambda) "
                             "grows with d and the razor is W crossing 3x the sample "
                             "spacing",
                "discriminating_computation": "W(d) by bisection on the frozen "
                                              "predicate; test monotone in d; test "
                                              "whether the YES/NO split coincides with "
                                              "W crossing 3*0.1 = 0.30",
                "signature_if_true": "W monotone in d AND the smallest certifying d is "
                                     "the smallest d with W >= 0.30",
            },
            "b_oscillation_trough": {
                "statement": "C_ab or the independence predicate oscillates and a "
                             "trough swallows the third sample at low d",
                "discriminating_computation": "count sign changes of dC_ab/dt on the "
                                              "dense grid over the window and its "
                                              "neighbourhood; count contiguous "
                                              "certifiable blocks; run the grid-offset "
                                              "diagnostic",
                "signature_if_true": ">1 contiguous block, or dC_ab/dt changing sign "
                                     "inside the window",
            },
            "c_early_closure": {
                "statement": "the window closes early at low d and the third sample "
                             "lands after closure",
                "discriminating_computation": "locate t_close(d) and its clip gate; "
                                              "test monotone-vs-oscillatory decay after "
                                              "the C_ab peak",
                "signature_if_true": "t_close monotone increasing in d with a monotone "
                                     "(non-oscillatory) approach",
            },
            "d_ceiling_churn": {
                "statement": "the R_ind ceiling fluctuates at low d and the failure is "
                             "in which pairs bind, not in C_ab",
                "discriminating_computation": "track max R_ind, the content-pass set and "
                                              "the binding-pair identity at every frozen "
                                              "sample and densely across the window",
                "signature_if_true": "binding-pair identity or content-pass set changes "
                                     "across the run on the cells that fail, in a way "
                                     "that decides the verdict",
            },
        },
        "declared_non_premise": "these four are the supervisor's candidates and are NOT "
                                "premises; if the curves show a fifth structure the "
                                "block follows it (minimal-premise rule)",
        "claim_surface": "the FROZEN sample grid Jt = 0.0(0.1)1.2 with the frozen run "
                         "rule; every continuous-time and grid-offset number below is "
                         "DIAGNOSTIC-GRADE",
    }
    prereg_sha = sha256_obj(prereg)
    say("-- PRE-REGISTRATION (candidates + discriminants, before any curve) --")
    say("  prereg_id:  %s" % prereg["prereg_id"])
    say("  prereg sha256: %s" % prereg_sha)
    say("")

    # ================================================= Q1: the dense curves ===
    t_q1 = time.perf_counter()
    STAR_KEYS = ["S%d" % d for d in range(2, 9)]
    TREE_KEYS = ["G3a", "G3b", "H2", "H3"]
    OTHER_KEYS = ["G1", "G2", "G4", "G5", "H1"]
    CURVE_KEYS = STAR_KEYS + TREE_KEYS
    CELLS = {}
    curves = {}
    say("-- Q1: the continuous window behind the discrete flag (DIAGNOSTIC-GRADE) --")
    say("     resolution: dense scan dt = %.4f (n <= %d) / %.4f (n > %d); every EDGE "
        "is located by bisection on the frozen predicate to %.0e, so no edge depends "
        "on the scan step" % (DENSE_DT_SMALL, DENSE_N_CAP, DENSE_DT_BIG, DENSE_N_CAP,
                              BISECT_TOL))
    say("")
    say("  %-5s %-6s %-9s %-9s %-8s %-14s %-14s %-6s %-5s %s"
        % ("cell", "lam", "t_open", "t_close", "W", "open gate", "close gate",
           "W/0.1", "run", "verdict"))
    for key in CURVE_KEYS + OTHER_KEYS:
        for lam in LAMBDAS:
            cn = CellN(G[key], lam)
            CELLS[(key, lam)] = cn
            dt = DENSE_DT_SMALL if cn.n <= DENSE_N_CAP else DENSE_DT_BIG
            w = window_of(cn, dt)
            pred = predicted_run_and_verdict(w["blocks"])
            rows, *_ = frozen_rows(key, lam)
            pp = P["persistence_profile"](rows)
            actual_run = pp.get("run", 0)
            actual_verdict = ("YES" if pp.get("persists")
                              and (pp.get("first_jt") is not None
                                   and pp["first_jt"] <= DEADLINE_JT + 1e-12) else "NO")
            nyq = math.pi / cn.bandwidth
            curves[(key, lam)] = {
                "key": key, "lambda": lam, "pointer_degree": G[key]["stats"]["pointer_degree"],
                "n_sites": cn.n, "n_fragments": len(cn.labels), "route": cn.mode,
                "window": w, "predicted": pred,
                "frozen_run": actual_run, "frozen_verdict": actual_verdict,
                "bandwidth": cn.bandwidth, "nyquist_dt": nyq,
                "scan_oversampling_vs_nyquist": nyq / dt,
                "frozen_grid_vs_nyquist": nyq / GRID_SPACING,
            }
            for b in w["blocks"]:
                say("  %-5s %-6s %-9.6f %-9.6f %-8.6f %-14s %-14s %-6.2f %-5d %s%s"
                    % (key, lam, b["lo"], b["hi"], b["width"], b["open_gate"],
                       b["close_gate"], b["width"] / GRID_SPACING, pred["run"],
                       pred["verdict"],
                       "" if pred["verdict"] == actual_verdict else "  <<MISMATCH"))
            if not w["blocks"]:
                say("  %-5s %-6s %-9s %-9s %-8s %-14s %-14s %-6s %-5d %s"
                    % (key, lam, "-", "-", "0", "-", "-", "0", 0, "NO"))
    say("")

    # the window-edge prediction must reproduce EVERY frozen verdict and run
    mism = [(k, v["predicted"], v["frozen_run"], v["frozen_verdict"])
            for k, v in curves.items()
            if v["predicted"]["verdict"] != v["frozen_verdict"]
            or v["predicted"]["run"] != v["frozen_run"]]
    say("  window-edge prediction vs the frozen sample-grid verdict+run: %d/%d cells "
        "agree, %d mismatches" % (len(curves) - len(mism), len(curves), len(mism)))
    for m in mism:
        say("    MISMATCH %s predicted=%s frozen run=%s verdict=%s" % m)
    if mism:
        die("q1:window-edge-prediction-mismatch %d" % len(mism))

    # monotonicity / block structure / churn census
    census = {}
    for key in CURVE_KEYS:
        for lam in LAMBDAS:
            cn = CELLS[(key, lam)]
            dt = (DENSE_DT_SMALL if cn.n <= DENSE_N_CAP else 4 * DENSE_DT_BIG)
            ts = [0.4 + k * dt for k in range(int(round((1.3 - 0.4) / dt)) + 1)]
            gg = [cn.gates(t) for t in ts]
            cvals = [min(g["C_ab"].values()) for g in gg]
            dC = np.diff(np.array(cvals))
            sign_changes = int((np.diff(np.sign(dC)) != 0).sum())
            blk = (curves[(key, lam)]["window"]["blocks"] or [None])[0]
            inwin = [g for g in gg if blk is not None
                     and blk["lo"] - 1e-12 <= g["t"] <= blk["hi"] + 1e-12]
            binding = [g["binding_pair"] for g in inwin]
            npass = [g["n_content_passes"] for g in inwin]
            # a "changing binding pair" is meaningless when the eligible pairs are
            # degenerate (every star pair is exchangeable): measure the spread first.
            spread = 0.0
            for g in inwin:
                elig = [v for k2, v in g["C_ab"].items()
                        if all(q in g["content_passes"] for q in k2.split("|"))]
                if len(elig) >= 2:
                    spread = max(spread, max(elig) - min(elig))
            degenerate = bool(spread < 1e-12)
            census[("%s@%s" % (key, lam))] = {
                "C_ab_min_over_pairs_monotone_rising_0.4_to_1.3": bool((dC > 0).all()),
                "d_dt_sign_changes": sign_changes,
                "n_certifiable_blocks": curves[(key, lam)]["window"]["n_blocks"],
                "eligible_pair_C_ab_spread_across_window": spread,
                "eligible_pairs_degenerate": degenerate,
                "binding_pair_identity_constant_across_window":
                    bool(degenerate or len(set(binding)) <= 1),
                "binding_pair_identity_constant_or_degenerate":
                    bool(degenerate or len(set(binding)) <= 1),
                "n_content_passes_constant_across_window": bool(len(set(npass)) <= 1),
                "n_content_passes_range": ([min(npass), max(npass)] if npass else None),
            }
    say("  monotonicity census over %d curve cells:" % len(census))
    say("    C_ab strictly rising on [0.4,1.3]: %d/%d"
        % (sum(1 for v in census.values()
               if v["C_ab_min_over_pairs_monotone_rising_0.4_to_1.3"]), len(census)))
    say("    exactly ONE contiguous certifiable block: %d/%d"
        % (sum(1 for v in census.values() if v["n_certifiable_blocks"] == 1), len(census)))
    say("    binding-pair identity constant (or the eligible pairs degenerate): %d/%d"
        % (sum(1 for v in census.values()
               if v["binding_pair_identity_constant_across_window"]), len(census)))
    say("    cells with genuinely non-degenerate eligible pairs: %d/%d"
        % (sum(1 for v in census.values() if not v["eligible_pairs_degenerate"]),
           len(census)))
    # the phase law's bracket must hold on every cell: floor(W/h) <= run <= floor(W/h)+1
    bracket_bad = []
    for (key, lam), v in curves.items():
        b = (v["window"]["blocks"] or [None])[0]
        w = b["width"] if b else 0.0
        lo_b = int(math.floor(w / GRID_SPACING + 1e-12))
        if not (lo_b <= v["frozen_run"] <= lo_b + 1):
            bracket_bad.append("%s@%s" % (key, lam))
    say("    sampling bracket floor(W/h) <= run <= floor(W/h)+1 holds on %d/%d cells"
        % (len(curves) - len(bracket_bad), len(curves)))
    if bracket_bad:
        die("q1:sampling-bracket-violated %s" % bracket_bad)
    say("")

    # the s(k,t) lens (931): does the SHAPE differ between d=4 and d=5?
    s_lens = {}
    tprobe = [0.62, 0.66, 0.70, 0.74, 0.78, 0.80, 0.84, 0.88, 0.92, 0.95]
    Cmat = []
    for d in range(2, 9):
        cn = CELLS[("S%d" % d, 0.10)]
        nb = cn.n - 1
        row = []
        srow = []
        for t in tprobe:
            br, _ = branch_vectors(cn.state(t), cn.n, cn.S)
            s1 = sum(p * svd_entropy(v, nb, [0]) for p, v in br)
            s2 = sum(p * svd_entropy(v, nb, [0, 1]) for p, v in br)
            row.append(2 * s1 - s2)
            srow.append({"t": t, "s1": s1, "s2": s2, "C_ab": 2 * s1 - s2})
        Cmat.append(row)
        s_lens["S%d@0.1" % d] = srow
    Cmat = np.array(Cmat)
    norm = Cmat / Cmat[:, 5:6]
    U, SV, Vt = np.linalg.svd(np.log(Cmat[1:]))
    rank1_ge3 = float(SV[0] ** 2 / (SV ** 2).sum())
    U2, SV2, _ = np.linalg.svd(np.log(Cmat))
    rank1_ge2 = float(SV2[0] ** 2 / (SV2 ** 2).sum())
    shape_spread = float(np.abs(norm[1:] - norm[1:].mean(axis=0)).max())
    shape_spread_incl2 = float(np.abs(norm - norm.mean(axis=0)).max())
    mono_in_d = bool((np.diff(Cmat, axis=0) < 0).all())
    say("  the 931 lens -- s(1,t), s(2,t) and the SHAPE question (lambda = 0.10):")
    say("    C_ab(d,t) strictly DECREASING in d at every probe time: %s" % mono_in_d)
    say("    normalised profiles C(d,t)/C(d,0.80) collapse, d = 3..8: max spread %.4f"
        % shape_spread)
    say("    same including d = 2: max spread %.4f" % shape_spread_incl2)
    say("    log-space rank-1 fraction d>=3: %.6f ; d>=2: %.6f" % (rank1_ge3, rank1_ge2))
    say("    => between d = 4 and d = 5 the s(k,t) SHAPE is the same to %.2f%%; only "
        "the AMPLITUDE moves" % (100.0 * float(np.abs(norm[2] - norm[3]).max())))
    say("")
    q1_secs = time.perf_counter() - t_q1

    # =========================================== Q2: discriminate the candidates
    t_q2 = time.perf_counter()
    say("-- Q2: the candidates, discriminated on the pre-registered computations --")
    disc = {}

    # (a) window width
    W = {d: curves[("S%d" % d, 0.10)]["window"]["blocks"][0]["width"]
         for d in range(2, 9)}
    W_mono = all(W[d] < W[d + 1] for d in range(2, 8))
    smallest_ge_3sp = min([d for d in range(2, 9)
                           if W[d] >= PERSIST_N * GRID_SPACING] or [99])
    frozen_thr = min([d for d in range(2, 9)
                      if curves[("S%d" % d, 0.10)]["frozen_verdict"] == "YES"] or [99])
    disc["a_window_width"] = {
        "W_by_degree_at_0.10": {str(d): W[d] for d in W},
        "W_monotone_increasing_in_d": W_mono,
        "smallest_d_with_W_ge_3x_spacing": smallest_ge_3sp,
        "frozen_threshold_degree": frozen_thr,
        "verdict": ("SUPPORTED (width is the carrier and the 3x-spacing crossing "
                    "coincides with the frozen threshold)"
                    if (W_mono and smallest_ge_3sp == frozen_thr) else
                    "PARTIALLY SUPPORTED (width is monotone and is the carrier, but the "
                    "frozen threshold is NOT simply W >= 3x spacing -- see the phase law)"),
    }
    say("  (a) WINDOW WIDTH: W(d) at lambda=0.10 = %s"
        % ", ".join("d%d:%.4f" % (d, W[d]) for d in range(2, 9)))
    say("      monotone increasing in d: %s ; smallest d with W >= 0.30: %s ; "
        "frozen threshold: %s" % (W_mono, smallest_ge_3sp, frozen_thr))
    say("      -> %s" % disc["a_window_width"]["verdict"])

    # (b) oscillation / trough
    n_multi = sum(1 for v in census.values() if v["n_certifiable_blocks"] != 1)
    n_nonmono = sum(1 for v in census.values()
                    if not v["C_ab_min_over_pairs_monotone_rising_0.4_to_1.3"])
    disc["b_oscillation_trough"] = {
        "cells_with_more_than_one_certifiable_block": n_multi,
        "cells_with_non_monotone_C_ab": n_nonmono,
        "max_sign_changes_of_dC_dt": max(v["d_dt_sign_changes"] for v in census.values()),
        "verdict": ("REFUTED -- C_ab is strictly monotone rising through the whole "
                    "window on every curve cell and there is exactly one contiguous "
                    "certifiable block everywhere; there is no trough to swallow a sample"
                    if (n_multi == 0 and n_nonmono == 0) else "NOT REFUTED"),
    }
    say("  (b) OSCILLATION/TROUGH: multi-block cells %d, non-monotone cells %d, max "
        "dC/dt sign changes %d" % (n_multi, n_nonmono,
                                   disc["b_oscillation_trough"]["max_sign_changes_of_dC_dt"]))
    say("      -> %s" % disc["b_oscillation_trough"]["verdict"])

    # (c) early closure
    tcl = {d: curves[("S%d" % d, 0.10)]["window"]["blocks"][0]["hi"] for d in range(2, 9)}
    topen = {d: curves[("S%d" % d, 0.10)]["window"]["blocks"][0]["lo"] for d in range(2, 9)}
    cg = {d: curves[("S%d" % d, 0.10)]["window"]["blocks"][0]["close_gate"]
          for d in range(2, 9)}
    og = {d: curves[("S%d" % d, 0.10)]["window"]["blocks"][0]["open_gate"]
          for d in range(2, 9)}
    disc["c_early_closure"] = {
        "t_close_by_degree_at_0.10": {str(d): tcl[d] for d in tcl},
        "t_open_by_degree_at_0.10": {str(d): topen[d] for d in topen},
        "t_open_spread_across_d": max(topen.values()) - min(topen.values()),
        "close_gate_by_degree": {str(d): cg[d] for d in cg},
        "open_gate_by_degree": {str(d): og[d] for d in og},
        "t_close_monotone_in_d": all(tcl[d] < tcl[d + 1] for d in range(2, 8)),
        "verdict": "SUPPORTED AND SHARPENED -- the window closes EARLY at low d, the "
                   "closure is monotone (not oscillatory), and the CLIP IDENTITY "
                   "switches: the independence gate closes it for d <= 5 and the "
                   "content gate closes it for d >= 6, at which point t_close "
                   "saturates",
    }
    say("  (c) EARLY CLOSURE: t_open spread across d = %.2e (essentially "
        "d-independent); t_close = %s"
        % (disc["c_early_closure"]["t_open_spread_across_d"],
           ", ".join("d%d:%.4f(%s)" % (d, tcl[d], cg[d][:5]) for d in range(2, 9))))
    say("      -> %s" % disc["c_early_closure"]["verdict"])

    # (d) ceiling churn
    churn_cells = {k: v for k, v in census.items()
                   if not v["binding_pair_identity_constant_across_window"]
                   or not v["n_content_passes_constant_across_window"]}
    # does churn ever DECIDE a verdict?  compare the run predicted from C_ab alone
    churn_decisive = []
    for key in CURVE_KEYS + OTHER_KEYS:
        for lam in LAMBDAS:
            rows, *_ = frozen_rows(key, lam)
            kk = "%.2f" % HEADLINE_DELTA
            ids = [tuple(sorted(r["singleton_passes"][kk])) for r in rows
                   if r["r_ind"][kk] >= 2]
            if len(set(ids)) > 1:
                churn_decisive.append("%s@%s" % (key, lam))
    disc["d_ceiling_churn"] = {
        "cells_with_churn_in_the_content_pass_set_or_binding_pair": sorted(churn_cells),
        "cells_where_the_content_pass_set_changes_during_the_certified_run":
            sorted(churn_decisive),
        "churn_decides_any_frozen_verdict": False,
        "verdict": "REAL BUT NOT THE RAZOR -- churn happens exactly where the arms are "
                   "NOT pairwise isomorphic (H3, and among the non-curve anchors G4 and "
                   "G5): there the binding pair moves and the content-pass set moves "
                   "with it.  On every star and every isomorphic-arm tree the eligible "
                   "pairs are exactly degenerate (spread < 1e-12), so 'which pair binds' "
                   "is not even a well-posed question.  Decisively: the certification "
                   "predicate is R_ind >= 2, and the window-edge prediction reproduces "
                   "every frozen run and verdict on all 48 anchor cells and all 29 "
                   "sealed cells WITHOUT any reference to pair identity -- so churn "
                   "cannot be the razor",
        "note_on_degeneracy": ("a naive 'binding-pair identity changed' counter fires "
                               "spuriously on exchangeable geometries because ties are "
                               "broken by floating-point noise; this census measures the "
                               "eligible-pair SPREAD first and reports degeneracy"),
    }
    say("  (d) CEILING CHURN: %d curve cells show churn; cells whose content-pass set "
        "changes during the certified run: %s"
        % (len(churn_cells), ", ".join(churn_decisive) or "none"))
    say("      -> %s" % disc["d_ceiling_churn"]["verdict"])

    # (e) THE FIFTH STRUCTURE: grid PHASE
    span_needed = (PERSIST_N - 1) * GRID_SPACING          # 0.2
    span_guarantee = PERSIST_N * GRID_SPACING             # 0.3
    phase_class = {}
    for d in range(2, 9):
        w = W[d]
        phase_class[d] = ("robust-YES" if w >= span_guarantee else
                          "phase-dependent" if w >= span_needed else "robust-NO")
    disc["e_grid_phase"] = {
        "law": "an interval of width W contains at least floor(W/h) grid points at "
               "EVERY phase and at most floor(W/h)+1; with h = 0.1 and persist_n = 3 "
               "this gives: W >= 3h => run >= 3 at every phase (robust YES); "
               "W < 2h => run <= 2 at every phase (robust NO); 2h <= W < 3h => the "
               "verdict is decided by the grid PHASE, not by the dynamics",
        "class_by_degree_at_0.10": {str(d): phase_class[d] for d in phase_class},
        "robust_NO_threshold": min([d for d in range(2, 9)
                                    if phase_class[d] != "robust-NO"] or [99]),
        "robust_YES_threshold": min([d for d in range(2, 9)
                                     if phase_class[d] == "robust-YES"] or [99]),
        "phase_ambiguous_degrees": [d for d in range(2, 9)
                                    if phase_class[d] == "phase-dependent"],
    }
    say("  (e) [NOT a supervisor candidate -- followed under the minimal-premise rule]")
    say("      GRID PHASE: with h = %.1f and persist_n = %d, W >= %.1f certifies at "
        "EVERY phase and W < %.1f fails at every phase; in between the verdict is a "
        "phase fact." % (GRID_SPACING, PERSIST_N, span_guarantee, span_needed))
    say("      class by degree at lambda=0.10: %s"
        % ", ".join("d%d:%s" % (d, phase_class[d]) for d in range(2, 9)))
    say("      phase-invariant content: degrees <= %d fail at every phase; degrees "
        ">= %d certify at every phase; degrees %s are decided by the phase."
        % (disc["e_grid_phase"]["robust_NO_threshold"] - 1,
           disc["e_grid_phase"]["robust_YES_threshold"],
           disc["e_grid_phase"]["phase_ambiguous_degrees"]))
    say("")
    q2_secs = time.perf_counter() - t_q2

    # ============================================================ the seal ====
    t_seal = time.perf_counter()
    say("-- SEAL (pre-registered BEFORE the frozen machinery touches these cells) --")
    seal_cells = []
    for lam in SEAL_LAMBDAS:
        for d in range(2, 9):
            seal_cells.append(("S%d" % d, lam))
    for d in (9, 10):
        G["S%d" % d] = make_star(P, d)
        seal_cells.append(("S%d" % d, 0.10))
        seal_cells.append(("S%d" % d, 0.05))
    for key in ("G3a", "G3b", "H2", "H3"):
        seal_cells.append((key, 0.0875))
    SEAL_LOCKED["cells"] = set((k, round(l, 10)) for k, l in seal_cells)
    already = [c for c in SEAL_LOCKED["cells"] if c in ROWS]
    seal_predictions = {}
    for (key, lam) in seal_cells:
        ck = (key, round(lam, 10))
        cn = CellN(G[key], lam)
        dt = DENSE_DT_SMALL if cn.n <= DENSE_N_CAP else DENSE_DT_BIG
        w = window_of(cn, dt)
        pred = predicted_run_and_verdict(w["blocks"])
        seal_predictions["%s@%s" % (key, lam)] = {
            "window": [round(b["lo"], 12) for b in w["blocks"]][:1] +
                      [round(b["hi"], 12) for b in w["blocks"]][:1],
            "width": (w["blocks"][0]["width"] if w["blocks"] else 0.0),
            "close_gate": (w["blocks"][0]["close_gate"] if w["blocks"] else None),
            "predicted_run": pred["run"], "predicted_verdict": pred["verdict"],
            "predicted_first_jt": pred["first_jt"],
        }
        CELLS[(key, lam)] = cn

    # the grid-offset map, sealed the same way (predicted from edges alone)
    OFFSETS = [-0.05, -0.03, -0.02, -0.01, -0.005, 0.0, 0.005, 0.0075, 0.01, 0.02,
               0.025, 0.03, 0.05, 0.07]
    offset_map = {}
    for off in OFFSETS:
        thr = 99
        runs = {}
        for d in range(2, 9):
            w = curves[("S%d" % d, 0.10)]["window"]["blocks"]
            pr = predicted_run_and_verdict(w, offset=off)
            runs[d] = pr["run"]
            if pr["verdict"] == "YES":
                thr = min(thr, d)
        offset_map["%+.4f" % off] = {"runs": runs, "threshold_at_0.10": thr}

    # HOW SPECIAL IS THE FROZEN PHASE?  A 401-point sweep over two full grid periods,
    # computed from the window edges alone (DIAGNOSTIC-GRADE).  Adopted mid-block from
    # the independent checker's first scope finding.
    phase_hist = {}
    for i in range(401):
        off = -0.1 + 0.0005 * i
        thr = 99
        for d in range(2, 9):
            if predicted_run_and_verdict(curves[("S%d" % d, 0.10)]["window"]["blocks"],
                                         offset=off)["verdict"] == "YES":
                thr = min(thr, d)
        phase_hist.setdefault(thr, 0)
        phase_hist[thr] += 1
    phase_frac = {str(k): v / 401.0 for k, v in sorted(phase_hist.items())}
    modal_thr = int(max(phase_frac, key=lambda k: phase_frac[k]))
    frozen_phase_frac = phase_frac.get("5", 0.0)

    seal = {
        "seal_id": "cycle932-persistence-razor-seal-1",
        "built_from": "continuous window edges only (bisection on the frozen predicate); "
                      "the frozen sample-grid machinery has NOT been run on any sealed "
                      "cell at seal time",
        "sealed_cells_never_evaluated_on_the_frozen_grid_before_this_point":
            sorted("%s@%s" % (k, l) for k, l in seal_cells),
        "n_sealed_cells": len(seal_cells),
        "already_evaluated_before_seal": sorted("%s@%s" % c for c in already),
        "predictions": seal_predictions,
        "offset_map_prediction": offset_map,
        "prereg_sha256": prereg_sha,
    }
    if already:
        die("seal:holdout-violation %s" % already)
    seal_sha = sha256_obj(seal)
    SEAL_LOCKED["locked"] = True
    say("  seal_id:     %s" % seal["seal_id"])
    say("  seal sha256: %s" % seal_sha)
    say("  sealed cells: %d (3 new fields x 7 stars, 2 new degrees, 4 tree anchors "
        "at the 919 extension field); frozen-machinery evaluations of them at seal "
        "time: %d" % (len(seal_cells), len(already)))

    seal_results = {}
    n_ok = 0
    for (key, lam) in seal_cells:
        rows, *_ = frozen_rows(key, lam)
        pp = P["persistence_profile"](rows)
        run = pp.get("run", 0)
        verdict = ("YES" if pp.get("persists") and pp.get("first_jt") is not None
                   and pp["first_jt"] <= DEADLINE_JT + 1e-12 else "NO")
        pr = seal_predictions["%s@%s" % (key, lam)]
        ok = (run == pr["predicted_run"] and verdict == pr["predicted_verdict"])
        n_ok += int(ok)
        seal_results["%s@%s" % (key, lam)] = {
            "predicted_run": pr["predicted_run"], "measured_run": run,
            "predicted_verdict": pr["predicted_verdict"], "measured_verdict": verdict,
            "agree": bool(ok)}
    say("  SEAL RESULT: %d/%d sealed cells verified (run AND verdict)"
        % (n_ok, len(seal_cells)))
    for k in sorted(seal_results):
        v = seal_results[k]
        if not v["agree"]:
            say("    FAILED %s predicted run=%s verdict=%s ; measured run=%s verdict=%s"
                % (k, v["predicted_run"], v["predicted_verdict"],
                   v["measured_run"], v["measured_verdict"]))
    if n_ok != len(seal_cells):
        die("seal:failed %d/%d" % (n_ok, len(seal_cells)))

    # verify the sealed offset map by re-running the frozen machinery on shifted grids
    offset_verified = {}
    for off in (-0.05, -0.02, 0.0, 0.01, 0.05):
        thr = 99
        runs = {}
        for d in range(2, 9):
            g = G["S%d" % d]
            grid = [round(0.1 * i + off, 10) for i in range(13) if 0.1 * i + off >= 0]
            diag = P["build_diag"](g["n"], g["bonds"])
            psi0 = P["prep_state"](g["n"], set([g["S"]] + list(g["recording"])))
            outs, _ = P["chebyshev"](psi0, diag, g["n"], 0.10, grid)
            rws, _ = P["measure"](g, outs, grid)
            kk = "%.2f" % HEADLINE_DELTA
            # NOTE: the t=0 baseline is the first sample of the SHIFTED grid; this is a
            # declared DIAGNOSTIC construction, not the frozen protocol.
            flags = [r["r_ind"][kk] >= 2 for r in rws]
            idx = next((i for i, f in enumerate(flags) if f), None)
            run = 0
            if idx is not None:
                for f in flags[idx:]:
                    if f:
                        run += 1
                    else:
                        break
            runs[d] = run
            if idx is not None and run >= PERSIST_N and rws[idx]["jt"] <= DEADLINE_JT + 1e-12:
                thr = min(thr, d)
        offset_verified["%+.4f" % off] = {"runs": runs, "threshold_at_0.10": thr}
    say("  grid-offset map (DIAGNOSTIC-GRADE, NOT a re-grading of the frozen verdicts):")
    for k in sorted(offset_map, key=lambda s: float(s)):
        v = offset_map[k]
        vv = offset_verified.get(k)
        say("    offset %s Jt -> runs %s  threshold %s%s"
            % (k, "".join("%d" % v["runs"][d] for d in range(2, 9)),
               v["threshold_at_0.10"],
               ("   [full-machinery check: threshold %s]" % vv["threshold_at_0.10"])
               if vv else ""))
    say("")
    seal_secs = time.perf_counter() - t_seal

    # ==================================================== falsifier teeth =====
    t_teeth = time.perf_counter()
    say("-- FALSIFIER TEETH (all must fire) --")

    # T1: a planted WIDE window at d=4 must flip the mechanism verdict
    class PlantedWide:
        def __init__(self, cn, factor):
            self.cn, self.factor = cn, factor
            self.n, self.S = cn.n, cn.S
            self.labels, self.frags = cn.labels, cn.frags
            self.bandwidth = cn.bandwidth
        def gates(self, t, delta=HEADLINE_DELTA):
            g = dict(self.cn.gates(t, delta))
            g["C_ab"] = {k: v * self.factor for k, v in g["C_ab"].items()}
            b = g["binding_pair_C_ab"]
            g["binding_pair_C_ab"] = None if b is None else b * self.factor
            g["m_indep"] = (None if g["binding_pair_C_ab"] is None
                            else INDEP_MAX - g["binding_pair_C_ab"])
            g["r_ind_ge2"] = bool(g["n_content_passes"] >= 2
                                  and g["binding_pair_C_ab"] is not None
                                  and g["binding_pair_C_ab"] <= INDEP_MAX)
            return g
        def cert(self, t, delta=HEADLINE_DELTA):
            return self.gates(t, delta)["r_ind_ge2"]
    pw = PlantedWide(CELLS[("S4", 0.10)], 0.5)
    wpl = window_of(pw, DENSE_DT_SMALL)
    ppl = predicted_run_and_verdict(wpl["blocks"])
    tooth("T1_planted_wide_window_at_d4",
          "halving C_ab at d=4 widens the window; the mechanism must then predict a "
          "CERTIFYING d=4 (the real d=4 predicts NO)",
          ppl["verdict"] == "YES" and curves[("S4", 0.10)]["predicted"]["verdict"] == "NO",
          {"planted_window": [wpl["blocks"][0]["lo"], wpl["blocks"][0]["hi"]],
           "planted_width": wpl["blocks"][0]["width"], "planted_run": ppl["run"],
           "planted_verdict": ppl["verdict"],
           "true_d4_verdict": curves[("S4", 0.10)]["predicted"]["verdict"]})

    # T2: a planted grid-INSENSITIVE curve must be caught by the offset diagnostic
    pw2 = PlantedWide(CELLS[("S4", 0.10)], 0.25)
    w2 = window_of(pw2, DENSE_DT_SMALL)
    offs2 = [predicted_run_and_verdict(w2["blocks"], offset=o)["verdict"]
             for o in OFFSETS]
    offs_real = [predicted_run_and_verdict(curves[("S4", 0.10)]["window"]["blocks"],
                                           offset=o)["verdict"] for o in OFFSETS]
    tooth("T2_planted_grid_insensitive_curve",
          "a quarter-amplitude d=4 curve has W >= 3h and must be YES at EVERY offset, "
          "while the true d=4 curve flips with offset -- the offset diagnostic must "
          "separate them",
          len(set(offs2)) == 1 and offs2[0] == "YES" and len(set(offs_real)) > 1,
          {"planted_width": w2["blocks"][0]["width"],
           "planted_verdicts_over_offsets": offs2,
           "true_d4_verdicts_over_offsets": offs_real})

    # T3: the Euler guard
    def euler_states(psi0, diag, n, lam, times, nstep=40):
        mv = P["_matvec_factory"](diag, n, lam)
        psi = psi0.astype(np.complex128).copy()
        outs, tprev = [], 0.0
        for t in times:
            h = (t - tprev) / nstep
            for _ in range(nstep):
                psi = psi + (-1j * h) * mv(psi)
            outs.append(psi.copy())
            tprev = t
        return outs
    g = G["S5"]
    diag = P["build_diag"](g["n"], g["bonds"])
    psi0 = P["prep_state"](g["n"], set([g["S"]] + list(g["recording"])))
    eu = euler_states(psi0, diag, g["n"], 0.10, T_EXEC)
    rows_eu, _ = P["measure"](g, eu, T_EXEC)
    rows_tr, *_ = frozen_rows("S5", 0.10)
    eu_dev = max(max(abs(a["C_ab"][k] - v) for k, v in b["C_ab"].items())
                 for a, b in zip(rows_eu, rows_tr))
    eu_chi = max(max(abs(a["chi"][k] - v) for k, v in b["chi"].items())
                 for a, b in zip(rows_eu, rows_tr))
    eu_hz = max(abs(a["H_Z"] - b["H_Z"]) for a, b in zip(rows_eu, rows_tr))
    eu_norm = max(abs(float(np.vdot(v, v).real) - 1.0) for v in eu)
    tooth("T3_euler_guard",
          "a first-order Euler propagator must visibly fail (norm drift and C_ab/chi "
          "deviation far above the route tolerance).  H_Z is NOT a usable witness here: "
          "the global X-flip symmetry pins p_z = 1/2 for any symmetry-preserving "
          "integrator, so Euler reproduces H_Z exactly -- disclosed",
          eu_norm > 1e-6 and eu_dev > ROUTE_TOL and eu_chi > ROUTE_TOL,
          {"euler_norm_drift": eu_norm, "euler_C_ab_deviation": eu_dev,
           "euler_chi_deviation": eu_chi, "euler_H_Z_deviation": eu_hz,
           "route_tolerance": ROUTE_TOL,
           "H_Z_is_symmetry_protected": bool(eu_hz <= 1e-15)})

    # T4: a tampered pin must hard-fail
    tamper_path = os.path.join(ROOT, C919_RUNNER)
    orig = open(tamper_path, "rb").read()
    tampered = orig.replace(b"PERSIST_N = 3", b"PERSIST_N = 4", 1)
    tamper_caught = (sha256_bytes(tampered) != PINS[C919_RUNNER][0]
                     and tampered != orig)
    tooth("T4_tampered_pin",
          "flipping the pinned 919 persistence constant must break the pin digest",
          tamper_caught,
          {"original_sha256": sha256_bytes(orig)[:16],
           "tampered_sha256": sha256_bytes(tampered)[:16],
           "pin_would_reject": True})

    # T5: coarse scan must miss a window the fine scan finds
    cn2 = CELLS[("S2", 0.10)]
    _, _, blocks_fine = scan_blocks(cn2, DENSE_DT_SMALL)
    _, _, blocks_coarse = scan_blocks(cn2, GRID_SPACING)
    tooth("T5_resolution_is_load_bearing",
          "the d=2 window at lambda=0.10 is narrower than the frozen grid spacing; a "
          "scan at the frozen spacing MISSES it while the dense scan finds it",
          len(blocks_fine) == 1 and len(blocks_coarse) == 0,
          {"fine_blocks": len(blocks_fine), "coarse_blocks": len(blocks_coarse),
           "d2_window_width": W[2], "frozen_grid_spacing": GRID_SPACING})

    # T6: a planted oscillation must be caught by the monotonicity detector
    tosc = np.linspace(0.4, 1.3, 361)
    real = np.array([min(CELLS[("S4", 0.10)].gates(t)["C_ab"].values()) for t in tosc])
    planted = real * (1.0 + 0.15 * np.sin(40.0 * tosc))
    sc_real = int((np.diff(np.sign(np.diff(real))) != 0).sum())
    sc_pl = int((np.diff(np.sign(np.diff(planted))) != 0).sum())
    tooth("T6_planted_oscillation",
          "the monotonicity detector must report zero sign changes on the true curve "
          "and many on a planted oscillation",
          sc_real == 0 and sc_pl >= 5,
          {"sign_changes_true": sc_real, "sign_changes_planted": sc_pl})

    # T7: mislabelling the clip gate must be caught
    b5 = curves[("S5", 0.10)]["window"]["blocks"][0]
    b6 = curves[("S6", 0.10)]["window"]["blocks"][0]
    tooth("T7_clip_identity_is_measured_not_asserted",
          "the clip identity must actually SWITCH inside the family (independence at "
          "d=5, content at d=6) -- a runner that hard-coded one answer would fail here",
          b5["close_gate"] == "independence" and b6["close_gate"].startswith("content"),
          {"d5_close_gate": b5["close_gate"], "d6_close_gate": b6["close_gate"],
           "d5_close_margins": b5["close_margins"], "d6_close_margins": b6["close_margins"]})

    # T8: the window-edge prediction must be falsifiable -- a wrong persist_n breaks it
    bad = 0
    for k, v in curves.items():
        pr = predicted_run_and_verdict(v["window"]["blocks"])
        wrong = "YES" if (pr["run"] >= 2 and pr["first_jt"] is not None) else "NO"
        if wrong != v["frozen_verdict"]:
            bad += 1
    tooth("T8_prediction_is_falsifiable",
          "the same window-edge machinery with persist_n = 2 must MISPREDICT frozen "
          "verdicts, proving the agreement at persist_n = 3 is not vacuous",
          bad > 0, {"mispredictions_at_persist_n_2": bad, "n_cells": len(curves)})

    # T9: determinism -- double run identical
    def digest_cell(key, lam):
        cn = CellN(G[key], lam)
        w = window_of(cn, DENSE_DT_SMALL if cn.n <= DENSE_N_CAP else DENSE_DT_BIG)
        return sha256_obj(w)
    dd1 = digest_cell("S4", 0.10)
    dd2 = digest_cell("S4", 0.10)
    tooth("T9_determinism",
          "recomputing a cell's window from scratch must give a bit-identical digest",
          dd1 == dd2, {"digest": dd1})

    # T10: route disagreement must be detectable
    cnx = CELLS[("S5", 0.10)]
    o_true = cnx.observables(0.8)
    rows_s5, *_ = frozen_rows("S5", 0.10)
    r08 = [r for r in rows_s5 if abs(r["jt"] - 0.8) < 1e-12][0]
    dev_true = max(abs(o_true["C_ab"][k] - v) for k, v in r08["C_ab"].items())
    dev_fake = max(abs(o_true["C_ab"][k] * 1.000001 - v) for k, v in r08["C_ab"].items())
    tooth("T10_route_cross_validation_has_teeth",
          "the route N vs route P comparator must accept the true values and reject a "
          "1e-6 relative perturbation",
          dev_true <= ROUTE_TOL < dev_fake,
          {"true_deviation": dev_true, "perturbed_deviation": dev_fake,
           "tolerance": ROUTE_TOL})

    # T11: the seal must be holdout-free by construction
    tooth("T11_seal_holdout_freedom",
          "no sealed cell may have been evaluated on the frozen grid before the seal "
          "digest was taken",
          len(already) == 0 and len(seal["sealed_cells_never_evaluated_on_the_frozen_grid_before_this_point"]) == len(seal_cells),
          {"pre_seal_evaluations": len(already), "n_sealed": len(seal_cells)})

    # T12: the phase law must have empirical content -- it must forbid something
    forbidden = []
    for d in range(2, 9):
        if phase_class[d] == "robust-NO":
            hits = [offset_map[k]["runs"][d] for k in offset_map]
            if max(hits) >= PERSIST_N:
                forbidden.append(d)
        if phase_class[d] == "robust-YES":
            hits = [offset_map[k]["runs"][d] for k in offset_map]
            if min(hits) < PERSIST_N:
                forbidden.append(d)
    tooth("T12_phase_law_forbids_something",
          "the phase law's robust classes must hold over the whole offset sweep; a "
          "violation would refute it",
          len(forbidden) == 0,
          {"violating_degrees": forbidden,
           "offsets_tested": len(offset_map),
           "note": "the law is falsifiable: any robust-NO degree reaching run 3 at any "
                   "offset, or any robust-YES degree dropping below 3, would break it"})
    say("  %d/%d teeth fired" % (sum(1 for t in TEETH if t["fired"]), len(TEETH)))
    say("")
    teeth_secs = time.perf_counter() - t_teeth

    # ============================================================= verdict ====
    say("-- Q3: THE VERDICT --")
    say("  MECHANISM (measured law, derived from the frozen predicate's own preimage):")
    say("    The frozen certification predicate R_ind >= 2 holds on a SINGLE CONTIGUOUS")
    say("    real interval [t_open, t_close] in every one of the %d curve cells."
        % len(curves))
    say("    t_open is set by the CONTENT gate and is essentially degree-independent")
    say("    (spread %.2e across degrees 2..8 at lambda = 0.10); it moves only with the"
        % disc["c_early_closure"]["t_open_spread_across_d"])
    say("    field.  t_close is set by whichever of two gates bites first: the")
    say("    INDEPENDENCE gate (C_ab crossing 0.02), strongly degree-dependent through")
    say("    927's arity dilution, or the CONTENT gate again, degree-independent.  So")
    say("    the window WIDTH W(d, lambda) rises monotonically with degree and then")
    say("    SATURATES at a content-limited ceiling.  The persistence flag is a")
    say("    COUNT OF GRID POINTS INSIDE THAT INTERVAL.  Nothing about the dynamics")
    say("    changes between degree 4 and degree 5: the normalised time profiles")
    say("    collapse onto one curve to %.2f%% (log-space rank-1 fraction %.6f) --"
        % (100 * shape_spread, rank1_ge3))
    say("    only the AMPLITUDE moves, exactly as arity dilution says it should.")
    say("    In 931's language: s(1,t) and s(2,t) keep their shape and lose height as")
    say("    degree grows, so C_ab = 2s(1,t) - s(2,t) crosses the gate later, and the")
    say("    window's right edge slides right until the content gate catches it.")
    say("")
    say("  (i) THE PERSISTENCE COUNT'S LOAD-BEARING STATUS (926):")
    say("      HONESTLY SPLIT, and the split is exact.  With spacing h = %.1f, an"
        % GRID_SPACING)
    say("      interval of width W contains at least floor(W/h) grid points at every")
    say("      phase.  Therefore persist_n = %d has PRINCIPLED content at the two ends"
        % PERSIST_N)
    say("      -- W >= %.1f certifies at every grid phase, W < %.1f fails at every grid"
        % (span_guarantee, span_needed))
    say("      phase -- and NO phase-invariant content in between.  At lambda = 0.10")
    say("      the degrees fall out as: %s"
        % ", ".join("d%d %s" % (d, phase_class[d]) for d in range(2, 9)))
    say("      Degrees 3 and 4 are in the ambiguous band: their windows (%.4f, %.4f)"
        % (W[3], W[4]))
    say("      are WIDER than the %.1f span three samples need, and they fail only"
        % span_needed)
    say("      because the window opens %.4f / %.4f AFTER the grid point at Jt = 0.6."
        % (topen[3] - 0.6, topen[4] - 0.6))
    say("      Shifting the sample grid by +0.010 in Jt -- one tenth of one spacing --")
    say("      moves the threshold from %d to %d."
        % (offset_map["+0.0000"]["threshold_at_0.10"],
           offset_map["+0.0100"]["threshold_at_0.10"]))
    say("      And the frozen phase is NOT a typical one: over a 401-point sweep of")
    say("      two full grid periods the threshold is 5 on %.1f%% of phases, 4 on"
        % (100 * phase_frac.get("5", 0.0)))
    say("      %.1f%% and 3 on %.1f%% -- the frozen grid's answer is the LEAST common"
        % (100 * phase_frac.get("4", 0.0), 100 * phase_frac.get("3", 0.0)))
    say("      of the three outcomes, and the modal outcome is threshold %d."
        % modal_thr)
    say("      SCOPE QUALIFIER, stated and not softened: the 919/926 threshold")
    say("      'degree >= 5 certifies at lambda = 0.10' is correct AT THE FROZEN SAMPLE")
    say("      GRID Jt = 0.0(0.1)1.2 AT PHASE 0.  Its phase-invariant content is")
    say("      weaker and is exactly this: degrees <= 2 fail at every phase, degrees")
    say("      >= %d certify at every phase, and degrees 3 and 4 are decided by the"
        % disc["e_grid_phase"]["robust_YES_threshold"])
    say("      grid's phase rather than by the dynamics.  The frozen phase happens to")
    say("      resolve the ambiguous band entirely to NO, which is why the frozen")
    say("      threshold COINCIDES with the phase-invariant certifying threshold -- a")
    say("      favourable accident, not a derivation.  This block does NOT re-grade the")
    say("      frozen verdicts; it qualifies their scope.")
    say("")
    say("  (ii) IS THE d-CONJUNCT DERIVABLE FROM THE CURVE FAMILY?  YES.")
    say("      run(geometry, lambda) = #{k : t_open <= 0.1k <= t_close} and the frozen")
    say("      verdict is YES iff that count >= %d and the first such k is <= %.0f."
        % (PERSIST_N, DEADLINE_JT))
    say("      This predicate, evaluated from the continuous edges alone, reproduces")
    say("      the run AND the verdict on all %d curve+anchor cells and on all %d"
        % (len(curves), len(seal_cells)))
    say("      SEALED cells, including three fields never measured before, degrees 9")
    say("      and 10, and the four tree anchors.  926's persistence axis and deadline")
    say("      axis also come out of the same two edges: persist_n = 4 kills every")
    say("      lambda = 0.10 cell because no window there holds four grid points, and")
    say("      the deadline is robust over 0.7..1.2 because every event starts at the")
    say("      first grid point after t_open and no window reaches past 0.96.")
    say("")
    say("  (iii) SEAL: %d/%d verified.  Predictions were built from window edges only "
        "and digested before the frozen machinery ran on any sealed cell."
        % (n_ok, len(seal_cells)))
    say("")
    say("  WHAT REMAINS EMPIRICAL: the AMPLITUDE law C_ab(d, lambda) itself -- 927's")
    say("  arity dilution -- and the shape of the one universal time profile.  This")
    say("  block explains the razor GIVEN that amplitude law; it does not derive it.")
    say("")

    # ============================================================== receipt ====
    runtime = time.perf_counter() - T_START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    def curve_rows():
        out = {}
        for (key, lam), v in sorted(curves.items()):
            b = v["window"]["blocks"][0] if v["window"]["blocks"] else None
            out["%s@%s" % (key, lam)] = {
                "pointer_degree": v["pointer_degree"], "n_sites": v["n_sites"],
                "n_fragments": v["n_fragments"], "route": v["route"],
                "t_open": (b["lo"] if b else None), "t_close": (b["hi"] if b else None),
                "window_width": (b["width"] if b else 0.0),
                "width_over_sample_spacing": ((b["width"] / GRID_SPACING) if b else 0.0),
                "open_gate": (b["open_gate"] if b else None),
                "close_gate": (b["close_gate"] if b else None),
                "open_margins": (b["open_margins"] if b else {}),
                "close_margins": (b["close_margins"] if b else {}),
                "n_certifiable_blocks": v["window"]["n_blocks"],
                "grid_samples_in_window": (grid_samples_in(b) if b else []),
                "predicted_run": v["predicted"]["run"],
                "predicted_verdict": v["predicted"]["verdict"],
                "frozen_run": v["frozen_run"], "frozen_verdict": v["frozen_verdict"],
                "prediction_agrees_with_frozen":
                    bool(v["predicted"]["verdict"] == v["frozen_verdict"]
                         and v["predicted"]["run"] == v["frozen_run"]),
                "bohr_bandwidth": v["bandwidth"], "nyquist_dt": v["nyquist_dt"],
                "scan_oversampling_vs_nyquist": v["scan_oversampling_vs_nyquist"],
                "frozen_grid_step_over_nyquist_step":
                    GRID_SPACING / v["nyquist_dt"],
                "monotonicity_census": census.get("%s@%s" % (key, lam)),
            }
        return out

    receipt = {
        "schema": "frontier_cycle932_persistence_razor.v1",
        "cycle": 932,
        "block": "toe-time-blockM12-20260802",
        "date": "2026-07-28",
        "runner": "scripts/frontier_cycle932_persistence_razor_2026_07_28.py",
        "runner_sha256": sha256_bytes(open(os.path.abspath(__file__), "rb").read()),
        "git_head": head,
        "boundary_sentences": BOUNDARY,
        "claim_surface": (
            "THE FROZEN GRID IS THE CLAIM SURFACE.  The frozen sample-grid verdicts are "
            "reproduced at deviation exactly 0 and are NEVER re-graded by this block.  "
            "Every continuous-time window edge, width, clip identity and grid-offset "
            "result in this receipt is DIAGNOSTIC-GRADE: it explains the frozen "
            "verdicts and qualifies their scope, and carries no certification."),
        "frozen_definitions_quoted": runrule,
        "frozen_constants_byte_verified": frozen,
        "frozen_constants_cross_check": const_x,
        "statistic_definition_byte_verified": statdef,
        "pins": pins,
        "recovered_d1_note": d1,
        "route_P_pinned_function_quotes": quotes,
        "restriction_gates": {
            "gate_order": ("pins -> frozen constants (21/21, seven-way) -> statistic "
                           "definition bytes -> partition rule -> 919 ladder -> 919 "
                           "persistence profiles -> 919 C_ab window table -> 926 "
                           "persistence+deadline axes -> 926 threshold band -> 927 "
                           "degree table -> 931 pair-complement identity -> route N vs "
                           "route P -> PRE-REGISTRATION -> curves -> SEAL -> any sealed "
                           "number"),
            "partition_rule_reproduces_memo_six_lists": part_ok,
            "c919_ladder": {"cells": n_cells, "rows": n_rows,
                            "max_abs_deviation": dev_ladder},
            "c919_persistence_profiles": {"samples": n_pp,
                                          "max_abs_deviation": dev_pp},
            "c919_C_ab_window_table": {"values": n_cw, "max_abs_deviation": dev_cw},
            "c926_axes_verdicts_reproduced": dev_926,
            "c926_threshold_band": {"lo": band_lo, "hi": band_hi,
                                    "reproduced": bool(band_ok)},
            "c927_degree_table": {"rows": n927, "max_abs_deviation": dev_927},
            "c931_pair_complement_identity_max_dev": dev_931,
            "route_N_vs_route_P_max_abs_deviation": dev_route,
            "deviation_exactly_zero_everywhere": bool(
                dev_ladder == 0.0 and dev_pp == 0.0 and dev_cw == 0.0
                and dev_927 == 0.0),
            # NOTE: no timing lives in this block -- see numerics.section_seconds.
            # A wall-clock number here would leak into the timing-free digest; the
            # guard below hard-fails if any such key reappears.
        },
        "pre_registration": prereg,
        "pre_registration_sha256": prereg_sha,
        "Q1_curves": {
            "resolution_justification": {
                "method": ("window edges are located by BISECTION on the frozen "
                           "predicate to %.0e, so no published edge depends on the scan "
                           "step; the dense scan only has to bracket every transition"
                           % BISECT_TOL),
                "dense_dt_small_n": DENSE_DT_SMALL,
                "dense_dt_large_n": DENSE_DT_BIG,
                "large_n_declared_cap": ("cells with n > %d use the marching route and "
                                         "the coarser scan step; declared" % DENSE_N_CAP),
                "spectral_bound": ("the Bohr bandwidth omega_max = E_max - E_min is "
                                   "computed exactly where the cell is diagonalised and "
                                   "bounded by 2(||diag||_inf + lambda n) otherwise; the "
                                   "Nyquist step is pi/omega_max"),
                "worst_case_scan_oversampling_vs_nyquist":
                    min(v["scan_oversampling_vs_nyquist"] for v in curves.values()),
                "frozen_grid_step_over_nyquist_step_range": [
                    min(GRID_SPACING / v["nyquist_dt"] for v in curves.values()),
                    max(GRID_SPACING / v["nyquist_dt"] for v in curves.values())],
                "note": ("the FROZEN sample grid is coarser than Nyquist on every cell "
                         "(ratio > 1 everywhere): it is a sampling protocol, not a "
                         "numerical grid.  This is stated as a fact about the protocol, "
                         "not as a criticism of it, and is part of why the persistence "
                         "flag is phase-sensitive."),
            },
            "per_cell": curve_rows(),
            "monotonicity_census": census,
            "s_of_k_lens_at_0.10": {
                "probe_times": tprobe,
                "s_curves": s_lens,
                "C_ab_decreasing_in_d_at_every_probe_time": mono_in_d,
                "normalised_profile_max_spread_d3_to_d8": shape_spread,
                "normalised_profile_max_spread_including_d2": shape_spread_incl2,
                "log_space_rank1_fraction_d_ge_3": rank1_ge3,
                "log_space_rank1_fraction_d_ge_2": rank1_ge2,
                "d4_vs_d5_max_normalised_difference":
                    float(np.abs(norm[2] - norm[3]).max()),
                "reading": ("the s(k,t) SHAPE is the SAME at d=4 and d=5; the entire "
                            "degree dependence is an amplitude, so the razor is an "
                            "amplitude threshold read through a fixed time profile"),
                "statistic_dependence_disclosed": (
                    "the sameness of d=4 and d=5 is robust: it is reproduced by the "
                    "independent checker's curvature statistic (4.6%% relative "
                    "difference).  The strength of the d=2 EXCEPTION is NOT robust: "
                    "this normalised-profile statistic isolates d=2 by ~6.9x while the "
                    "curvature statistic isolates it by only ~1.4x.  The d=2 exception "
                    "should therefore always be quoted with the statistic that measures "
                    "it; the load-bearing d=4/d=5 claim does not depend on the choice.  "
                    "Adopted mid-block from the independent checker's second finding."),
            },
        },
        "Q2_discrimination": disc,
        "Q3_verdict": {
            "mechanism_grade": "measured law, with a derived combinatorial core",
            "derived_part": ("given the two window edges, the frozen run and verdict "
                             "follow by counting grid points -- verified on every "
                             "anchor and every sealed cell; and the phase law "
                             "(floor(W/h) <= run <= floor(W/h)+1) is a theorem about "
                             "sampling an interval, not a fit"),
            "measured_part": ("the amplitude law C_ab(d, lambda) -- 927's arity "
                              "dilution -- and the single universal time profile the "
                              "normalised curves collapse onto"),
            "i_persistence_count_status": {
                "grade": "HONESTLY SPLIT",
                "principled_content": ("persist_n = 3 with spacing h has phase-invariant "
                                       "meaning at both ends: W >= 3h certifies at every "
                                       "phase, W < 2h fails at every phase"),
                "arbitrary_content": ("for 2h <= W < 3h the verdict is fixed by the grid "
                                      "PHASE and not by the dynamics; degrees 3 and 4 at "
                                      "lambda = 0.10 sit in that band"),
                "scope_qualifier_to_carry": (
                    "the 919/926 result 'pointer degree >= 5 certifies at lambda = 0.10' "
                    "holds AT THE FROZEN SAMPLE GRID Jt = 0.0(0.1)1.2 AT PHASE 0.  Its "
                    "phase-invariant content is: degree <= 2 fails at every grid phase; "
                    "degree >= 5 certifies at every grid phase; degrees 3 and 4 are "
                    "decided by the grid phase.  A grid shifted by +0.010 in Jt moves "
                    "the threshold to 3.  Over a 401-point sweep of two full grid "
                    "periods the threshold is 5 on %.1f%% of phases, 4 on %.1f%% and 3 "
                    "on %.1f%%: the frozen phase's answer is the LEAST common of the "
                    "three, and the modal answer is %d."
                    % (100 * phase_frac.get("5", 0.0), 100 * phase_frac.get("4", 0.0),
                       100 * phase_frac.get("3", 0.0), modal_thr)),
                "phase_histogram_of_the_threshold": phase_frac,
                "modal_threshold_over_phases": modal_thr,
                "frozen_phase_fraction": frozen_phase_frac,
                "phase_histogram_status": ("DIAGNOSTIC-GRADE; computed from the window "
                                           "edges alone over two full grid periods; "
                                           "adopted mid-block from the independent "
                                           "checker's first scope finding"),
                "not_softened": ("the frozen verdicts are NOT re-graded; the frozen "
                                 "phase resolves the ambiguous band to NO and therefore "
                                 "coincides with the phase-invariant certifying "
                                 "threshold -- that coincidence is an accident of phase, "
                                 "and saying so is the whole point"),
            },
            "ii_d_conjunct_derivable": {
                "answer": "YES, from the curve family",
                "predicate": ("run = #{k : t_open <= k*h <= t_close}; verdict = YES iff "
                              "run >= persist_n and the first such sample is <= the "
                              "deadline"),
                "cells_predicted_correctly": len(curves) - len(mism),
                "cells_total": len(curves),
                "sealed_cells_predicted_correctly": n_ok,
                "sealed_cells_total": len(seal_cells),
                "also_derives": ("926's persistence axis (persist 2 -> threshold 3; "
                                 "3 -> 5; 4 and 5 -> nothing at lambda = 0.10) and its "
                                 "deadline axis (robust over 0.7..1.2, dead at 0.6 and "
                                 "0.5) come out of the same two edges"),
            },
            "iii_seal": {"verified": n_ok, "total": len(seal_cells)},
            "honest_residue": ("the amplitude law is imported from 927, not derived "
                               "here; the universal time profile's functional form is "
                               "not derived; the phase analysis is DIAGNOSTIC-GRADE and "
                               "re-grades nothing"),
        },
        "seal": seal,
        "seal_sha256": seal_sha,
        "seal_results": seal_results,
        "grid_offset_diagnostic": {
            "status": "DECLARED NON-CLAIM DIAGNOSTIC -- shifts the sample grid off the "
                      "frozen phase; it explains the frozen verdicts and never replaces "
                      "them",
            "predicted_from_window_edges": offset_map,
            "verified_with_the_full_frozen_machinery_on_shifted_grids": offset_verified,
            "caveat": ("on a shifted grid the t = 0 baseline that the excess gate "
                       "subtracts is taken at the first shifted sample, so the "
                       "full-machinery check is itself a declared construction, not the "
                       "frozen protocol; the window-edge prediction uses the true t = 0 "
                       "baseline throughout"),
        },
        "teeth": TEETH,
        "numerics": {
            "python": sys.version.split()[0], "numpy": np.__version__,
            "platform": platform.platform(),
            "dtype": "float64/complex128",
            "routes": {
                "P": "pinned Cycle-919 code executed verbatim (Chebyshev + Bessel tail "
                     "bound; eigvalsh entropies)",
                "N": "this block's own implementation (Kronecker-assembled H; SVD "
                     "entropies; branch split before reduction; dense eigh for n <= %d, "
                     "scaling-and-marching Taylor with factorial remainder bound above"
                     % DENSE_N_CAP,
            },
            "max_rss_bytes": rss,
            "section_seconds": {"gates": gate_secs, "Q1": q1_secs, "Q2": q2_secs,
                                "seal": seal_secs, "teeth": teeth_secs},
        },
        "deviations": [
            "The supervisor's four candidates were declared non-premises.  Candidate "
            "(b) is REFUTED and candidate (d) is REAL BUT NOT THE RAZOR; the structure "
            "that actually decides the frozen verdicts is a FIFTH one -- grid PHASE "
            "against window width -- and it is followed under the minimal-premise rule.",
            "The spec asks whether the razor is 'W crossing 3x the sample spacing'.  "
            "Both readings are reported: W >= 3h is exactly the phase-INVARIANT "
            "certifying condition (and at lambda = 0.10 its threshold is degree 5, the "
            "frozen answer), while the frozen verdict itself is decided by W AND phase, "
            "which is why degrees 3 and 4 -- whose W already exceeds the 2h that three "
            "samples span -- still fail.",
            "The grid-offset diagnostic run through the full frozen machinery has to "
            "choose a t = 0 baseline for the excess gate; the shifted-grid construction "
            "is declared in the receipt and is not the frozen protocol.",
            "Cells with n > %d use the marching route and a %.3f scan step (declared "
            "capped grid); their window EDGES are still bisected to %.0e."
            % (DENSE_N_CAP, DENSE_DT_BIG, BISECT_TOL),
            "The seal fields 0.0625, 0.0875 and 0.09375 and the degrees 9 and 10 are "
            "DECLARED NON-CLAIM extensions; only lambda in {0.05, 0.10} carries the "
            "frozen claim, and 0.075 is 919's inherited declared extension.",
        ],
        "caveats": [
            "Every window edge, width and offset number is DIAGNOSTIC-GRADE.",
            "Stars of degree 7..10 are abstract spiders; whether the lattice and the "
            "frozen labelling can realise them at degree >= 7 was answered negatively "
            "by 929 and is not revisited.",
            "The amplitude law that makes the window widen with degree is imported from "
            "927 and is not derived here.",
            "The runtime limit 900 s is declared by the supervisor; the measured "
            "runtime is published in runtime_seconds and is deliberately excluded from "
            "the timing-free digest.",
        ],
        "runtime_seconds": runtime,
        "runtime_limit_seconds": 900,
    }

    payload = {k: v for k, v in receipt.items()
               if k not in ("runtime_seconds", "numerics")}

    # HARD GUARD: no wall-clock quantity may enter the timing-free digest.  Cycle 931
    # disclosed this exact trap; here it is a hard fail rather than a discipline.
    def scan_for_timing(o, path=""):
        bad = []
        if isinstance(o, dict):
            for k, v in o.items():
                kl = str(k).lower()
                if any(w in kl for w in ("runtime", "elapsed", "wall_clock", "_secs")) \
                        or kl.endswith("seconds"):
                    if "limit" not in kl:
                        bad.append(path + "/" + str(k))
                bad += scan_for_timing(v, path + "/" + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                bad += scan_for_timing(v, path + "[%d]" % i)
        return bad
    leaks = scan_for_timing(payload)
    if leaks:
        die("timing-free-digest:leak %s" % leaks)
    receipt["timing_free_digest"] = sha256_obj(payload)
    receipt["timing_free_digest_guard"] = {
        "keys_scanned_for_wall_clock_leakage": True, "leaks_found": leaks,
        "note": "a wall-clock value anywhere in the digested payload is a hard fail"}

    out_path = os.path.join(ROOT, "outputs",
                            "persistence_razor_cycle932_receipt_2026_07_28.json")
    with open(out_path, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=float)
    rsha = sha256_bytes(open(out_path, "rb").read())

    say("-- CAVEATS AND DECLARED NON-CLAIMS --")
    for c in receipt["deviations"] + receipt["caveats"]:
        say("  * %s" % c)
    say("")
    say("runtime: %.1f s (limit 900 s)" % runtime)
    say("timing-free digest: %s" % receipt["timing_free_digest"])
    say("receipt: outputs/persistence_razor_cycle932_receipt_2026_07_28.json")
    say("receipt sha256: %s" % rsha)
    say(BOUNDARY_LINE)
    say("===== runner cache v1 =====")

    log_path = os.path.join(ROOT, "logs", "runner-cache",
                            "frontier_cycle932_persistence_razor_2026_07_28.txt")
    with open(log_path, "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
